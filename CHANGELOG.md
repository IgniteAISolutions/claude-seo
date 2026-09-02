# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2026-09-02

Currency pass. The knowledge layer was frozen at February 2026 and had drifted ~7 months
out of date, missing the year's largest Search Console change. This release also fixes
three functional bugs in the schema hook and one broken plugin manifest.

### Fixed
- **`plugin.json` shipped a broken audit**: `agents/seo-geo.md` was missing from the agents
  array, so plugin-directory installs ran 6 of 7 subagents while still scoring "AI Search
  Readiness". Version also corrected (1.3.2 → 1.5.0).
- **Schema hook silently validated nothing on modern frameworks**: the JSON-LD `<script>`
  regex required `type` to be the only attribute, so Next.js/Astro output
  (`<script type="application/ld+json" id="...">`) was skipped and the hook exited clean.
- **Schema hook blocked legitimate edits**: `"REPLACE"` was substring-matched
  case-insensitively, so any schema containing "replacement" or "replaces" (e.g. a window
  replacement business) triggered a blocking placeholder error. Bare tokens now match
  case-sensitively on word boundaries.
- **Schema hook rejected connected entity graphs**: documents using `@graph` have no
  top-level `@type` and were flagged "Missing @type". `@graph` is now traversed per node,
  and `@context` accepts string, array and object forms plus trailing slashes.
- **HowTo downgraded from blocking to warning**: no Google rich result since Sept 2023, but
  still parsed by LLMs for step extraction. Mirrors the existing FAQPage posture.
- **`rel=next/prev` recommended in 4 files**: Google dropped support in March 2019. Replaced
  with self-referencing canonicals and crawlable links.
- **TTFB threshold corrected** 200ms → 800ms (Google's documented figure) in
  `cwv-thresholds.md` and `agents/seo-performance.md`.
- **Sitelinks `SearchAction`** moved out of "recommend freely" — the sitelinks search box was
  removed in November 2024.
- **Audit scoring weights reconciled**: `seo-audit/SKILL.md` disagreed with the orchestrator
  (AI Search Readiness 5% vs 10%). Orchestrator is now declared authoritative.
- **`seo-geo` added to audit delegation**: `/seo audit` scored AI Search Readiness without
  ever running the GEO agent.
- **Install docs re-introduced a removed security risk**: `INSTALLATION.md` still documented
  the `irm | iex` one-liner that v1.4.0 removed, and cloned from `main` rather than a tag.
- Count inconsistencies across README/CLAUDE.md/ARCHITECTURE.md (6 vs 7 agents, 8 vs 9
  technical categories, 12 vs 13 sub-skills); removed reference to a non-existent `tests/`.

### Added
- **`references/search-console-ai-reports.md`**: Search Console generative AI performance
  reports (launched 3 Jun 2026, global 31 Aug 2026) and the AI features blocking toggle.
  Includes the hard rule that these reports carry **no click data**, so any AI-surface CTR
  is fabricated.
- **`references/aeo-geo-benchmarks.md`**: the three retrieval layers (SEO/AEO/GEO), the
  Princeton GEO benchmark (Aggarwal et al., ACM SIGKDD 2024, arXiv:2311.09735) with verified
  figures, cross-encoder passage-extraction mechanics, the 40–58 word canonical answer block,
  fact-density targets, citation decay, and Information Gain.
- **`references/entity-schema-graph.md`**: connected `@graph` architecture, stable `@id` URIs,
  `sameAs` to Wikidata, machine-readable E-E-A-T on the `Person` node, and schema drift.
- **AEO, entity and AI-access quality gates** in `quality-gates.md` — previously the gates
  were entirely word-count/title/meta/alt-text.
- **Machine-readable E-E-A-T and Information Gain** sections in `eeat-framework.md`, which
  previously gave improvement advice with no structured-data implementation.
- **Three-layer retrieval model** in `seo/SKILL.md`, plus new hard rules: blocked AI crawlers,
  `aggregateRating` without visible reviews, and author markup naming departed staff.

### Changed
- Word-count gates reframed as thin-content diagnostics rather than targets, resolving a
  direct contradiction with `seo-content/SKILL.md` ("word count is NOT a ranking factor").
- GEO passage guidance reconciled: the 134–167 word figure conflicted with the 40–60 word
  answer-first rule. Now defined as two complementary structures.
- Unsourced and unreproducible statistics either attributed, caveated, or removed
  (platform citation shares, "92% of AI Overview citations", core-update traffic drops).
- "AI crawlers do NOT execute JavaScript" softened — rendering support varies by crawler.
- Platform table now includes Google AI Mode and Claude.

## [1.4.0] - 2026-03-12

### Security
- **Install script supply chain fix**: Replaced `irm | iex` Windows PowerShell one-liner with `git clone + powershell -File` as primary install method. Claude Code's own security guardrails flagged the old pattern as a supply chain risk (reported by community member). Added collapsible "review before running" section for Unix curl method.
- **Version pinning**: `install.sh` and `install.ps1` now clone a specific release tag (`v1.3.0`) by default rather than `main`, preventing silent updates. Override with `CLAUDE_SEO_TAG=main`.
- **PowerShell Invoke-External hardening**: Comprehensive `PSNativeCommandUseErrorActionPreference` handling in `Invoke-External` wrapper (fixes Windows git clone stderr false-positive termination, from PR #13 + PR #15).

### Added
- **GEO agent deployed**: `agents/seo-geo.md` created — `/seo audit` now spawns 7 parallel agents (was 6). GEO analysis covers AI crawler access, llms.txt, passage-level citability, brand mention signals, platform-specific scoring (Google AI Overviews, ChatGPT, Perplexity, Bing Copilot).
- **`--googlebot` flag in `fetch_page.py`**: Detect prerender/dynamic rendering services by comparing response size with default UA vs Googlebot UA. First phase of SPA/CSR support (Issue #11).

### Fixed
- **URL normalization**: `capture_screenshot.py` and `analyze_visual.py` now accept bare domains (`example.com` → `https://example.com`) via shared `normalize_url()` helper (from PR #16 by @shuofengzhang).
- **GEO weight**: AI Search Readiness weight increased from 5% to 10% in overall SEO Health Score. Technical SEO adjusted to 22%, Content Quality to 23%.
- **FAQPage guidance**: Blanket "remove FAQPage on commercial sites" updated to nuanced guidance — existing FAQPage → Info priority (not Critical), noting AI/LLM citation benefit. Adding new FAQPage → not recommended for Google, note AI benefit. Updated in `seo/SKILL.md`, `agents/seo-schema.md`, `seo/references/schema-types.md`.
- **Uninstall agents list**: Added `seo-geo` to `uninstall.sh` and `uninstall.ps1` removal lists.
- **Python requirement**: Corrected from `3.8+` to `3.10+` in `README.md` and `docs/INSTALLATION.md`.

### Changed
- Subagent count: 6 → 7 (added seo-geo to core audit pipeline)
- `.gitignore`: Added generated audit artifacts (charts/, PDFs, report.html, firebase-debug.log, generated-schema.json)

---

## [1.3.0] - 2026-03-06

### Added
- **Extension system**: `extensions/` directory convention for self-contained add-ons with install/uninstall scripts
- **DataForSEO extension**: 22 commands across 9 API modules (SERP, keywords, backlinks, on-page, content, business listings, AI visibility, LLM mentions). Install: `./extensions/dataforseo/install.sh`
- **DataForSEO integration**: seo-audit, seo-content, seo-geo, seo-page, seo-plan, seo-technical auto-detect DataForSEO MCP tools for enriched analysis
- **Plugin manifest**: `.claude-plugin/plugin.json` for official plugin directory submission
- **Documentation**: Extensions architecture in ARCHITECTURE.md, 22 new commands in COMMANDS.md, updated MCP integration guide

### Fixed
- **Title tag threshold**: Pre-commit hook now uses 60-char max, aligned with quality-gates.md and echo message
- **SSRF prevention**: Added to `capture_screenshot.py` (defense-in-depth, matching `fetch_page.py`)
- **Frontmatter cleanup**: Removed non-standard `allowed-tools` from main SKILL.md

### Changed
- Sub-skill count: 12 + 1 extension (added seo-dataforseo via DataForSEO extension)
- Subagent count: 6 + 1 optional (added seo-dataforseo agent via extension)
- DataForSEO promoted from "Community" to "Official extension" in MCP docs

---

## [1.2.1] - 2026-02-28

### Fixed
- **User-Agent header**: Changed default from bot-style `ClaudeSEO/1.0` to Chrome-like string with `ClaudeSEO/1.2` suffix. SSR frameworks (Next.js, Nuxt, Angular) now pre-render properly instead of serving empty client-side shells (#9)
- **Custom User-Agent support**: Added `--user-agent` flag to `fetch_page.py` for configurable UA strings

### Added
- **install.cat support**: Added alternative install method via `curl install.cat/AgriciDaniel/claude-seo | bash` to README (#10)

---

## [1.2.0] - 2026-02-19

### Security
- **SSRF prevention**: Added private IP blocking to `fetch_page.py` and `analyze_visual.py`
- **Path traversal prevention**: Added output path sanitization to `capture_screenshot.py` and file validation to `parse_html.py`
- **Install hardening**: Removed `--break-system-packages`, switched to venv-based pip install
- **requirements.txt**: Now persisted to `~/.claude/skills/seo/` for user retry

### Fixed
- **YAML frontmatter parsing**: Removed HTML comments before `---` delimiter in 8 files (skills: seo-content, seo-images, seo-programmatic, seo-schema, seo-technical; agents: seo-content, seo-performance, seo-technical). Thanks @kylewhirl for identifying this in the codex-seo fork.
- **Windows installer**: Merged @kfrancis improvements — `python -m pip`, `py -3` launcher fallback, requirements.txt persistence, non-fatal subagent copy, better error diagnostics (PR #6)
- **requirements.txt missing after install**: Now copied to skill directory so users can retry (#1)

### Changed
- Python dependencies now installed in a venv at `~/.claude/skills/seo/.venv/` with `--user` fallback (#2)
- Playwright marked as explicitly optional in install output
- Windows installer uses `Resolve-Python` helper for robust Python detection (#5)

---

## [1.1.0] - 2026-02-07

### Security (CRITICAL)
- **urllib3 ≥2.6.3**: Fixes CVE-2026-21441 (CVSS 8.9) - decompression bypass vulnerability
- **lxml ≥6.0.2**: Updated from 5.3.2 for additional libxml2 security patches
- **Pillow ≥12.1.0**: Fixes CVE-2025-48379
- **playwright ≥1.55.1**: Fixes CVE-2025-59288 (macOS)
- **requests ≥2.32.4**: Fixes CVE-2024-47081, CVE-2024-35195

### Added
- **GEO (Generative Engine Optimization) major enhancement**:
  - Brand mention analysis (3× more important than backlinks for AI visibility)
  - AI crawler detection (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, etc.)
  - llms.txt standard detection and recommendations
  - RSL 1.0 (Really Simple Licensing) detection
  - Passage-level citability scoring (optimal 134-167 words)
  - Platform-specific optimization (Google AI Overviews vs ChatGPT vs Perplexity)
  - Server-side rendering checks for AI crawler accessibility
- **LCP Subparts analysis**: TTFB, resource load delay, resource load time, render delay
- **Soft Navigations API detection** for SPA CWV measurement limitations
- **Schema.org v29.4 additions**: ConferenceEvent, PerformingArtsEvent, LoyaltyProgram
- **E-commerce schema updates**: returnPolicyCountry now required, organization-level policies

### Changed
- **E-E-A-T framework**: Updated for December 2025 core update - now applies to ALL competitive queries, not just YMYL
- **SKILL.md description**: Expanded to leverage new 1024-character limit
- **Schema deprecations expanded**: Added ClaimReview, VehicleListing (June 2025)
- **WebApplication schema**: Added as correct type for browser-based SaaS (vs SoftwareApplication)

### Fixed
- Schema-types.md now correctly distinguishes SoftwareApplication (apps) vs WebApplication (SaaS)

---

## [1.0.0] - 2026-02-07

### Added
- Initial release of Claude SEO
- 9 specialized skills: audit, page, sitemap, schema, images, technical, content, geo, plan
- 6 subagents for parallel analysis: seo-technical, seo-content, seo-schema, seo-sitemap, seo-performance, seo-visual
- Industry templates: SaaS, local service, e-commerce, publisher, agency, generic
- Schema library with deprecation tracking:
  - HowTo schema marked deprecated (September 2023)
  - FAQ schema restricted to government/healthcare sites only (August 2023)
  - SpecialAnnouncement schema marked deprecated (July 31, 2025)
- AI Overviews / GEO optimization skill (seo-geo) - new for 2026
- Core Web Vitals analysis using current metrics:
  - LCP (Largest Contentful Paint): <2.5s
  - INP (Interaction to Next Paint): <200ms - replaced FID on March 12, 2024
  - CLS (Cumulative Layout Shift): <0.1
- E-E-A-T framework updated to September 2025 Quality Rater Guidelines
- Quality gates for thin content and doorway page prevention:
  - Warning at 30+ location pages
  - Hard stop at 50+ location pages
- Pre-commit and post-edit automation hooks
- One-command install and uninstall scripts (Unix and Windows)
- Bounded Python dependency pinning with CVE-aware minimums (lxml >= 5.3.2)

### Architecture
- Follows Anthropic's official Claude Code skill specification (February 2026)
- Standard directory layout: `scripts/`, `references/`, `assets/`
- Valid hook matchers (tool name only, no argument patterns)
- Correct subagent frontmatter fields (name, description, tools)
- CLI command is `claude` (not `claude-code`)
