#!/usr/bin/env python3
"""Post-edit schema validation hook for Claude Code.

Validates JSON-LD schema after file edits. Returns exit code 2 to block
if critical validation errors found.

Hook configuration in ~/.claude/settings.json:
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/seo/hooks/validate-schema.py \"$FILE_PATH\"",
            "exitCodes": { "2": "block" }
          }
        ]
      }
    ]
  }
}

Note: matcher filters by tool name only (Edit, Write). The script itself
checks if the file contains schema markup before validating.
"""

import json
import re
import sys
import os
from typing import List


# Matches <script> tags carrying any attribute order/extra attributes, e.g.
# <script type="application/ld+json" id="schema"> as emitted by Next.js and Astro.
JSONLD_SCRIPT_RE = re.compile(
    r'<script[^>]*\btype=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)

# Bracketed template placeholders — safe to match as case-insensitive substrings.
BRACKETED_PLACEHOLDERS = [
    "[Business Name]",
    "[City]",
    "[State]",
    "[Phone]",
    "[Address]",
    "[Your",
    "[INSERT",
    "[URL]",
    "[Email]",
]

# Bare tokens — matched case-SENSITIVELY on word boundaries so that legitimate
# copy ("replacement windows", "replaces the old unit") is not flagged.
TOKEN_PLACEHOLDER_RES = [
    ("REPLACE", re.compile(r"\bREPLACE\b")),
    ("TODO", re.compile(r"\bTODO\b")),
    ("FIXME", re.compile(r"\bFIXME\b")),
]

VALID_CONTEXTS = {
    "https://schema.org",
    "http://schema.org",
    "https://schema.org/",
    "http://schema.org/",
}


def validate_jsonld(content: str) -> List[str]:
    """Validate JSON-LD blocks in HTML content."""
    errors = []
    blocks = JSONLD_SCRIPT_RE.findall(content)

    if not blocks:
        return []  # No schema found — not an error

    for i, block in enumerate(blocks, 1):
        block = block.strip()
        prefix = f"Block {i}"
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"{prefix}: Invalid JSON — {e}")
            continue

        if isinstance(data, dict):
            errors.extend(_check_context(data, prefix))
            if "@graph" in data:
                # Connected entity graph: @context sits at document level and each
                # node in @graph carries its own @type. See references/entity-schema-graph.md
                graph = data["@graph"]
                if not isinstance(graph, list):
                    errors.append(f"{prefix}: @graph must be an array")
                else:
                    for j, node in enumerate(graph, 1):
                        if isinstance(node, dict):
                            errors.extend(_validate_node(node, f"{prefix} @graph[{j}]"))
                        else:
                            errors.append(f"{prefix} @graph[{j}]: node must be an object")
            else:
                errors.extend(_validate_node(data, prefix))
        elif isinstance(data, list):
            for j, item in enumerate(data, 1):
                if isinstance(item, dict):
                    item_prefix = f"{prefix} item {j}"
                    errors.extend(_check_context(item, item_prefix))
                    errors.extend(_validate_node(item, item_prefix))

    return errors


def _check_context(obj: dict, prefix: str) -> List[str]:
    """Validate @context. Accepts string, array, or object forms (all valid JSON-LD)."""
    if "@context" not in obj:
        return [f"{prefix}: Missing @context"]

    ctx = obj["@context"]
    if isinstance(ctx, str):
        if ctx not in VALID_CONTEXTS:
            return [f"{prefix}: @context should be 'https://schema.org'"]
    elif isinstance(ctx, list):
        if not any(isinstance(c, str) and c in VALID_CONTEXTS for c in ctx):
            return [f"{prefix}: @context array should include 'https://schema.org'"]
    elif not isinstance(ctx, dict):
        return [f"{prefix}: @context must be a string, array, or object"]

    return []


def _validate_node(obj: dict, prefix: str) -> List[str]:
    """Validate a single schema node (no @context check — that is document level)."""
    errors = []

    # Check @type
    if "@type" not in obj:
        errors.append(f"{prefix}: Missing @type")

    # Check for placeholder text
    text = json.dumps(obj)
    lowered = text.lower()
    for p in BRACKETED_PLACEHOLDERS:
        if p.lower() in lowered:
            errors.append(f"{prefix}: Contains placeholder text: {p}")
    for name, pattern in TOKEN_PLACEHOLDER_RES:
        if pattern.search(text):
            errors.append(f"{prefix}: Contains placeholder text: {name}")

    # Check for deprecated types
    schema_type = obj.get("@type", "")
    if isinstance(schema_type, list):
        schema_type = schema_type[0] if schema_type else ""

    deprecated = {
        "SpecialAnnouncement": "deprecated July 31, 2025",
        "CourseInfo": "retired June 2025",
        "EstimatedSalary": "retired June 2025",
        "LearningVideo": "retired June 2025",
        "ClaimReview": "retired June 2025 — fact-check rich results discontinued",
        "VehicleListing": "retired June 2025 — vehicle listing structured data discontinued",
    }
    if schema_type in deprecated:
        errors.append(f"{prefix}: @type '{schema_type}' is {deprecated[schema_type]}")

    # Types with no Google rich result but retained value for AI/LLM extraction.
    # Warn, never block — mirrors the FAQPage posture in references/schema-types.md.
    no_rich_result = {
        "HowTo": "no Google rich result since September 2023 — still parsed by LLMs for step extraction",
        "FAQPage": "restricted to government and healthcare sites only (Aug 2023) — retains AI citation value",
    }
    if schema_type in no_rich_result:
        errors.append(f"{prefix}: @type '{schema_type}' {no_rich_result[schema_type]}")

    return errors


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        sys.exit(0)

    # Only validate HTML-like files
    valid_extensions = (".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".php", ".ejs")
    if not filepath.endswith(valid_extensions):
        sys.exit(0)

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except (OSError, IOError):
        sys.exit(0)

    errors = validate_jsonld(content)

    if not errors:
        sys.exit(0)

    # Categorize errors
    critical_keywords = ["placeholder", "deprecated", "retired"]
    critical = [e for e in errors if any(kw in e.lower() for kw in critical_keywords)]
    warnings = [e for e in errors if e not in critical]

    if warnings:
        print("⚠️  Schema validation warnings:")
        for w in warnings:
            print(f"  - {w}")

    if critical:
        print("🛑 Schema validation ERRORS (blocking):")
        for e in critical:
            print(f"  - {e}")
        sys.exit(2)  # Block the edit

    sys.exit(1)  # Warnings only — proceed


if __name__ == "__main__":
    main()
