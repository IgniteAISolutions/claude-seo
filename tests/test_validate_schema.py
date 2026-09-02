#!/usr/bin/env python3
"""Regression tests for hooks/validate-schema.py.

These cover the three bugs fixed in v1.5.0, each of which broke real setups:

1. The JSON-LD <script> regex required `type` to be the only attribute, so
   Next.js/Astro markup (`<script type="application/ld+json" id="...">`) was
   skipped entirely and the hook exited clean having validated nothing.
2. "REPLACE" was substring-matched case-insensitively, so any site whose schema
   mentioned "replacement" or "replaces" had its edits blocked.
3. Connected entity graphs (`@graph`) have no top-level `@type` and were flagged
   "Missing @type" — the exact pattern seo/references/entity-schema-graph.md
   now recommends.

Run: python3 -m pytest tests/ -q
"""

import importlib.util
import pathlib
import sys

import pytest

HOOK = pathlib.Path(__file__).resolve().parent.parent / "hooks" / "validate-schema.py"

_spec = importlib.util.spec_from_file_location("validate_schema", HOOK)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["validate_schema"] = _mod
_spec.loader.exec_module(_mod)

validate_jsonld = _mod.validate_jsonld


def wrap(payload: str, attrs: str = "") -> str:
    return f'<script type="application/ld+json"{attrs}>{payload}</script>'


# --- Bug 1: extra script attributes must not hide the block -------------------

@pytest.mark.parametrize(
    "attrs",
    ["", ' id="schema-org"', ' id="x" data-foo="bar"', " data-nscript='beforeInteractive'"],
)
def test_script_with_extra_attributes_is_still_validated(attrs):
    """Next.js/Astro emit extra attributes; the block must still be parsed."""
    bad = wrap('{"@context":"https://schema.org"}', attrs)  # no @type
    errors = validate_jsonld(bad)
    assert any("Missing @type" in e for e in errors), (
        "block was silently skipped instead of validated"
    )


def test_single_quoted_type_attribute():
    html = wrap('{"@context":"https://schema.org","@type":"Article"}').replace('"application', "'application").replace('json"', "json'")
    assert validate_jsonld(html) == []


# --- Bug 2: placeholder matching must not catch legitimate copy ---------------

@pytest.mark.parametrize(
    "name",
    [
        "Acme Replacement Windows",
        "We replace and repair old frames",
        "Irreplaceable Antiques Ltd",
        "Replacements and repairs",
    ],
)
def test_legitimate_replacement_copy_is_not_a_placeholder(name):
    html = wrap(
        '{"@context":"https://schema.org","@type":"LocalBusiness","name":"%s"}' % name
    )
    errors = validate_jsonld(html)
    assert not any("placeholder" in e.lower() for e in errors), (
        f"false positive placeholder on legitimate copy: {name!r} -> {errors}"
    )


@pytest.mark.parametrize("token", ["REPLACE", "TODO", "FIXME"])
def test_genuine_bare_token_placeholders_are_caught(token):
    html = wrap(
        '{"@context":"https://schema.org","@type":"LocalBusiness","telephone":"%s"}' % token
    )
    errors = validate_jsonld(html)
    assert any("placeholder" in e.lower() for e in errors)


def test_bracketed_placeholders_are_caught():
    html = wrap('{"@context":"https://schema.org","@type":"LocalBusiness","name":"[Business Name]"}')
    assert any("[Business Name]" in e for e in validate_jsonld(html))


# --- Bug 3: connected @graph support -----------------------------------------

VALID_GRAPH = """
{"@context":"https://schema.org","@graph":[
 {"@type":"Organization","@id":"https://ex.com/#organization","name":"Ex Ltd"},
 {"@type":"Person","@id":"https://ex.com/about#jane","name":"Jane Doe",
  "worksFor":{"@id":"https://ex.com/#organization"}},
 {"@type":"Article","@id":"https://ex.com/p#article","headline":"Hi",
  "author":{"@id":"https://ex.com/about#jane"}}]}
"""


def test_valid_entity_graph_passes_clean():
    assert validate_jsonld(wrap(VALID_GRAPH, ' id="site-graph"')) == []


def test_graph_node_missing_type_is_reported_with_index():
    payload = """
    {"@context":"https://schema.org","@graph":[
     {"@type":"Organization","@id":"https://ex.com/#o","name":"Ex"},
     {"@id":"https://ex.com/#no-type","name":"Untyped"}]}
    """
    errors = validate_jsonld(wrap(payload))
    assert any("@graph[2]" in e and "Missing @type" in e for e in errors)


def test_graph_must_be_an_array():
    payload = '{"@context":"https://schema.org","@graph":{"@type":"Organization"}}'
    assert any("@graph must be an array" in e for e in validate_jsonld(wrap(payload)))


# --- @context forms (all valid JSON-LD) --------------------------------------

@pytest.mark.parametrize(
    "ctx",
    [
        '"https://schema.org"',
        '"http://schema.org"',
        '"https://schema.org/"',
        '["https://schema.org"]',
        '{"@vocab":"https://schema.org/"}',
    ],
)
def test_accepted_context_forms(ctx):
    html = wrap('{"@context":%s,"@type":"Article","headline":"Hi"}' % ctx)
    assert not any("@context" in e for e in validate_jsonld(html))


def test_missing_context_is_reported():
    assert any("Missing @context" in e for e in validate_jsonld(wrap('{"@type":"Article"}')))


def test_wrong_context_is_reported():
    html = wrap('{"@context":"https://example.com","@type":"Article"}')
    assert any("@context" in e for e in validate_jsonld(html))


# --- Type posture -------------------------------------------------------------

def test_howto_warns_but_is_not_a_blocking_word():
    """HowTo has no rich result but still aids LLM extraction: warn, never block."""
    errors = validate_jsonld(wrap('{"@context":"https://schema.org","@type":"HowTo","name":"X"}'))
    assert errors, "HowTo should still be surfaced"
    blocking = ("placeholder", "deprecated", "retired")
    assert not any(kw in e.lower() for e in errors for kw in blocking), (
        f"HowTo must not trip the blocking keywords: {errors}"
    )


def test_faqpage_warns_but_is_not_blocking():
    errors = validate_jsonld(wrap('{"@context":"https://schema.org","@type":"FAQPage"}'))
    assert errors
    blocking = ("placeholder", "deprecated", "retired")
    assert not any(kw in e.lower() for e in errors for kw in blocking)


def test_genuinely_retired_type_is_reported():
    html = wrap('{"@context":"https://schema.org","@type":"ClaimReview"}')
    assert any("retired" in e.lower() for e in validate_jsonld(html))


def test_array_type_uses_first_entry():
    html = wrap('{"@context":"https://schema.org","@type":["ClaimReview","Thing"]}')
    assert any("retired" in e.lower() for e in validate_jsonld(html))


# --- General ------------------------------------------------------------------

def test_no_schema_is_not_an_error():
    assert validate_jsonld("<html><body><p>No schema here</p></body></html>") == []


def test_invalid_json_is_reported():
    assert any("Invalid JSON" in e for e in validate_jsonld(wrap("{not json}")))


def test_top_level_array_of_objects():
    payload = '[{"@context":"https://schema.org","@type":"Article","headline":"A"},' \
              ' {"@context":"https://schema.org","name":"B"}]'
    errors = validate_jsonld(wrap(payload))
    assert any("item 2" in e and "Missing @type" in e for e in errors)


def test_multiple_blocks_are_numbered_independently():
    html = wrap('{"@context":"https://schema.org","@type":"Article"}') + wrap('{"@type":"Article"}')
    errors = validate_jsonld(html)
    assert any("Block 2" in e for e in errors)
    assert not any("Block 1" in e for e in errors)


def test_repo_entity_graph_template_validates_clean():
    """The SiteEntityGraph template we ship must pass our own hook when filled."""
    import json

    tpl_path = pathlib.Path(__file__).resolve().parent.parent / "schema" / "templates.json"
    data = json.loads(tpl_path.read_text())
    tpl = next(t for t in data["templates"] if t["type"] == "SiteEntityGraph")["template"]

    payload = json.dumps(tpl)
    for placeholder, value in {
        "[Site URL]": "https://example.com",
        "[Page URL]": "https://example.com/post",
        "[Organization Name]": "Example Ltd",
        "[Logo URL]": "https://example.com/logo.png",
        "[LinkedIn URL]": "https://linkedin.com/company/example",
        "[Wikidata QID URL]": "https://www.wikidata.org/wiki/Q42",
        "[Site Name]": "Example",
        "[Author Name]": "Jane Doe",
        "[Job Title]": "CTO",
        "[Topic 1]": "AI",
        "[Topic 2]": "SEO",
        "[Page Title]": "A Post",
        "[Article Headline]": "A Post",
        "[YYYY-MM-DD]": "2026-09-02",
    }.items():
        payload = payload.replace(placeholder, value)

    assert validate_jsonld(wrap(payload, ' id="site-graph"')) == []
