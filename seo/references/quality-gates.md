<!-- Updated: 2026-09-02 -->
# Content Quality Gates

> **How to read the word counts below.** Word count is **not** a ranking factor, and Google
> has said so repeatedly. These figures are *thin-content diagnostics*, not targets: a page
> materially below them usually fails to cover its topic, and a page padded to hit them is
> worse, not better. Never recommend "add words". Recommend the missing substance.
>
> Originality matters more than length. A 400-word page with proprietary data outranks a
> 1,500-word page that restates the top 10. See Information Gain in `eeat-framework.md`.

## Minimum Word Counts by Page Type

| Page Type | Min Words | Unique Content % | Notes |
|-----------|-----------|-----------------|-------|
| Homepage | 500 | 100% | Must clearly communicate value proposition |
| Service / Feature Page | 800 | 100% | Detailed explanation of offering |
| Location (Primary) | 600 | 60%+ | City headquarters or main service area |
| Location (Secondary) | 500 | 40%+ | Satellite locations |
| Blog Post | 1,500 | 100% | In-depth, valuable content |
| Product Page | 400 | 80%+ | Unique descriptions, specs |
| Category Page | 400 | 100% | Unique intro, not just product listings |
| About Page | 400 | 100% | Company story, team, values |
| Landing Page | 600 | 100% | Focused conversion content |
| FAQ Page | 800 | 100% | Comprehensive Q&A |

---

## Uniqueness Scale (single source of truth)

Every skill referencing "unique content %" uses this one scale. Uniqueness means genuinely
different substance, not string-swapped city or keyword tokens.

| Unique content | Verdict | Action |
|----------------|---------|--------|
| ≥ 60% | Acceptable at scale | Required for location pages past the warning gate |
| 40–59% | Marginal | Warn; strengthen before adding more pages |
| 30–39% | Thin | ❌ Flag as thin content, likely penalty risk |
| < 30% | 🛑 **HARD STOP** | Scaled content abuse risk; require justification |

Corollary: if more than 60% of a page is shared template boilerplate, it fails by definition.

---

## Location Page Thresholds

### Warning Level (30+ pages)
- ⚠️ **WARNING** at 30+ location pages
- Enforce 60%+ unique content per page
- Content must include:
  - Unique local information (landmarks, neighborhoods)
  - Location-specific services or offerings
  - Local team or staff information
  - Genuine customer testimonials from that area

### Hard Stop (50+ pages)
- 🛑 **HARD STOP** at 50+ location pages
- Require explicit user justification
- Must demonstrate:
  - Legitimate business presence in each location
  - Unique content strategy for each page
  - Local signals (Google Business Profile, local reviews)

### Why This Matters
Google's doorway page algorithm penalizes programmatic location pages with thin/duplicate content. Signs of doorway pages:
- Only city/state name changed between pages
- No unique local information
- No local business signals
- Keyword-stuffed URLs

---

## Safe vs. Risky Programmatic Pages

### Safe at Scale ✅
| Page Type | Why It's Safe |
|-----------|---------------|
| Integration pages | Real setup documentation, unique technical content |
| Template/tool pages | Downloadable assets, unique functionality |
| Glossary pages | 200+ word unique definitions |
| Product pages | Unique specs, images, reviews |
| User profile pages | User-generated unique content |

### Penalty Risk ❌
| Page Type | Why It's Risky |
|-----------|----------------|
| Location pages with only city swapped | Duplicate content, doorway pages |
| "Best [tool] for [industry]" | Often thin, no industry-specific value |
| "[Competitor] alternative" | Requires genuine comparison data |
| AI-generated mass content | No unique value, E-E-A-T failure |

---

## Title Tag Requirements

| Aspect | Requirement |
|--------|-------------|
| Minimum length | 30 characters |
| Maximum length | 60 characters (Google truncates ~60) |
| Primary keyword | Near the beginning |
| Brand name | At end (if included) |
| Uniqueness | Each page must have unique title |

### Good Examples
- "Emergency Plumbing Services in Austin | ABC Plumbing"
- "How to Fix a Leaky Faucet: Step-by-Step Guide"
- "Enterprise SEO Software | Comprehensive Platform"

### Bad Examples
- "Home" (too short, not descriptive)
- "Best Plumbing Services for All Your Plumbing Needs in Austin Texas and Surrounding Areas" (too long)
- "ABC Plumbing - Plumbing - Plumber - Plumbing Services" (keyword stuffing)

---

## Meta Description Requirements

| Aspect | Requirement |
|--------|-------------|
| Minimum length | 120 characters |
| Maximum length | 160 characters (Google truncates ~155-160) |
| Call-to-action | Include compelling CTA |
| Primary keyword | Include naturally |
| Uniqueness | Each page must have unique description |

---

## Image Alt Text Requirements

| Aspect | Requirement |
|--------|-------------|
| Required on | All non-decorative images |
| Length | 10-125 characters |
| Content | Describe the image content, not "image" or filename |
| Keywords | Include naturally where relevant |
| Decorative images | Use `alt=""` or `role="presentation"` |

### Good Examples
- "Professional plumber repairing kitchen sink faucet"
- "Red 2024 Toyota Camry sedan front view"
- "Team meeting in modern office conference room"

### Bad Examples
- "image.jpg" (filename, not description)
- "plumber plumbing plumber services" (keyword stuffing)
- "Click here" (not descriptive)

---

## Internal Linking Guidelines

**The rule is density, not a fixed count: 3–5 relevant internal links per 1,000 words.**
The table below is that rule applied to typical page lengths, not a separate standard.

| Page Type | Typical target |
|-----------|----------------|
| Blog post (1,500+ words) | 5-10 internal links |
| Service page | 3-5 internal links |
| Category page | Links to all child pages |
| Product page | 2-4 internal links |

### Anchor Text Rules
- Use descriptive anchor text (not "click here")
- Vary anchor text (don't always use exact match keywords)
- Link to relevant, related content
- Ensure no orphan pages (every page linked from at least one other page)

---

## Content Freshness Signals

| Content Type | Update Frequency |
|--------------|------------------|
| News/current events | Within hours/days |
| Blog posts (evergreen) | Review annually |
| Product pages | When specs change |
| Service pages | Review quarterly |
| Company info | When changes occur |

### Required Elements
- Publication date visible (for articles/blogs)
- Last updated date (if significantly revised)
- Changelog for major updates (optional but good)

---

## AEO Gates (answer extraction)

Applied to any page targeting a question or informational query.

| Gate | Threshold | Severity if failed |
|------|-----------|--------------------|
| Canonical answer block present | 40–58 words, directly under a question-formatted H2/H3 | High |
| Answer block is self-contained | No unresolved pronouns; parses standalone | High |
| Answer placed before preamble | Answer opens the section | Medium |
| Question-formatted headings | H2/H3 phrased as the real query | Medium |
| Format matches intent | Comparisons as tables, processes as numbered lists | Medium |
| Fact density | ≥1 verifiable statistic, named entity or cited source per 100 words | Medium |

See `aeo-geo-benchmarks.md` for the evidence base and extraction mechanics.

## Entity & E-E-A-T Gates

| Gate | Requirement | Severity if failed |
|------|-------------|--------------------|
| Connected `@graph` | One graph per page, stable `@id` per node | Medium |
| Author is an entity | `author` references a `Person` by `@id`, not a bare name string | High |
| Credentials in markup | `hasCredential` / `knowsAbout` / `award` where genuine | Medium |
| External verification | `sameAs` to Wikidata / official profiles where genuine | Medium |
| Author currency | No markup naming departed staff | **Critical** |
| Review integrity | No `aggregateRating` without visible reviews | **Critical** |
| Schema drift | Structured claims match the rendered page | High |

## AI Search Access Gates

| Gate | Requirement | Severity if failed |
|------|-------------|--------------------|
| AI crawler access | GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot not blocked | **Critical** unless deliberate |
| Search Console AI toggle | AI features blocking control OFF unless deliberate | **Critical** unless deliberate |
| Server-side rendering | Primary content present in raw HTML response | High |
| `llms.txt` | Present at domain root | Low |

> **Reporting rule:** never state a CTR for AI surfaces. Search Console generative AI
> reports provide impressions only, with no click data. Any AI-surface CTR would be fabricated.
