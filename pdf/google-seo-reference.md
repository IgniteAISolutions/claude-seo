<!-- Updated: 2026-09-02 -->
# Google Search Quick Reference (September 2026)

Concise reference for subagents. Summarizes how Google Search works today, including
the generative serving layer. Not a reproduction of Google's documentation — see
Official Documentation Links at the bottom.

> **Single sources of truth.** Do not restate details that live elsewhere in this repo,
> or the files drift apart:
> - Schema type status → `seo/references/schema-types.md`
> - Entity graphs and author markup → `seo/references/entity-schema-graph.md`
> - E-E-A-T scoring → `seo/references/eeat-framework.md`
> - AEO/GEO benchmarks → `seo/references/aeo-geo-benchmarks.md`
> - Search Console AI reporting → `seo/references/search-console-ai-reports.md`
> - CWV detail → `seo/references/cwv-thresholds.md`

---

## How Google Search Works

**Crawling** (Googlebot discovers pages via links and sitemaps) → **Indexing** (content,
metadata and signals are processed and stored) → **Serving** (ranking systems return
results for a query). Pages must be crawlable and indexable to appear at all.

**Since 2024 the serving stage is no longer only ten blue links.** The same index now
feeds several surfaces:

| Surface | How it selects | Implication |
|---------|----------------|-------------|
| Classic organic results | Ranked list by relevance, quality, usability | Traditional SEO |
| Featured snippets / answer boxes | Passage-level extraction from a ranked page | Needs extractable answer blocks |
| **AI Overviews** | Retrieval and synthesis across multiple sources, with citations | Classic rank helps but does not guarantee citation |
| **AI Mode** | Query fan-out into many sub-queries, each retrieved and synthesized | Rewards broad topical coverage with depth per sub-question |

**Consequences for audits:**
- Ranking and citation are **separate outcomes**. A page can hold position 3 and never be
  cited; a page below the fold can be cited.
- Impressions inside AI surfaces are reported separately in Search Console, and **carry no
  click data**. Never compute a CTR for them.
- Zero-click behaviour is expected: rising AI impressions alongside falling clicks is a
  surface shift, not necessarily a ranking loss.

See `seo/references/aeo-geo-benchmarks.md` and `seo/references/search-console-ai-reports.md`.

---

## Google Search Essentials

Formerly "Webmaster Guidelines."

### Technical Requirements
- Accessible to Googlebot (not blocked by robots.txt or `noindex`)
- Returns HTTP 200 for indexable content
- Format Google can process (HTML preferred; JS-rendered content supported but slower)
- Served over HTTPS
- **Mobile-first indexing is 100% complete** (5 July 2024) — all sites are crawled and
  indexed with the mobile Googlebot user-agent

### AI crawler access (separate from Googlebot)
Googlebot access does **not** grant access to third-party AI engines. Each has its own
user-agent, and blocking one removes you from that engine entirely.

| Crawler | Owner | Purpose |
|---------|-------|---------|
| `Googlebot` | Google | Search index; also feeds AI Overviews and AI Mode |
| `Google-Extended` | Google | Controls Gemini/Vertex training use, **not** AI Overview eligibility |
| `GPTBot` | OpenAI | Training and retrieval |
| `OAI-SearchBot` | OpenAI | ChatGPT search retrieval |
| `ChatGPT-User` | OpenAI | User-initiated browsing |
| `ClaudeBot` | Anthropic | Claude crawling |
| `Claude-User` | Anthropic | User-initiated fetch |
| `Claude-SearchBot` | Anthropic | Claude search retrieval |
| `PerplexityBot` | Perplexity | Perplexity index |
| `Applebot-Extended` | Apple | Controls Apple AI training use |
| `CCBot` | Common Crawl | Open crawl corpus |
| `Bytespider` | ByteDance | ByteDance AI |

**Default recommendation:** allow the search/retrieval agents (`OAI-SearchBot`,
`ClaudeBot`, `Claude-SearchBot`, `PerplexityBot`, `GPTBot`). Training-only crawlers are a
licensing decision for the client, not a technical default. Blocking a retrieval agent is
**Critical** unless the client chose it deliberately.

Also check hosting-layer blocking (CDN bot rules can block AI crawlers even when
robots.txt allows them) and the Search Console **AI features toggle**.

### Spam Policies
No cloaking, doorway pages, hidden text/links, keyword stuffing, link spam, scraped or
auto-generated content without added value, sneaky redirects, or thin affiliate pages.

Scaled content abuse, site reputation abuse and expired domain abuse are explicitly
covered policies.

---

## Content Quality Signals

Google evaluates quality through **E-E-A-T**: Experience, Expertise, Authoritativeness,
Trustworthiness. Trust is the most important, and is inferred from the other three plus
direct trust indicators. Full criteria in `seo/references/eeat-framework.md`.

> **YMYL**: health, finance, safety, legal, civic. Held to the highest standard.
> **December 2025**: E-E-A-T assessment extends to all competitive queries, not only YMYL.

### Information Gain
Google's Information Gain patent (US20200349181A1) scores a document on the **additional,
non-redundant** information it adds relative to what the user has already seen.

This is what separates two pages with equal credentials. A page restating the same
definitions as the incumbent top 10 has near-zero information gain and no algorithmic
reason to outrank it. It is also what generative engines quote, which makes originality
the strongest shared requirement across classic ranking and AI citation.

**Audit question for every page:** what does this contain that the current top 10 do not?

---

## Core Web Vitals

Measured at the 75th percentile of real-user (field) data.

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** | ≤ 2.5s | 2.5s – 4.0s | > 4.0s |
| **INP** | ≤ 200ms | 200ms – 500ms | > 500ms |
| **CLS** | ≤ 0.1 | 0.1 – 0.25 | > 0.25 |

**Key facts:**
- INP replaced FID on 12 March 2024; FID was removed from all Chrome tooling on
  9 September 2024. **Never reference FID.**
- Core Web Vitals are used by ranking systems, but the effect is **lightweight** relative
  to relevance and quality. The standalone "page experience" ranking system was retired,
  and the Page Experience report was folded into individual CWV and HTTPS reports.
  Do not present CWV as a primary ranking lever — fix them for users, and as a tiebreaker.
- Field data (CrUX) beats lab data (Lighthouse) for assessment.
- **Lighthouse and PageSpeed lab runs cannot produce INP.** INP is field-only; Total
  Blocking Time (TBT) is the lab proxy. Never report a lab INP figure.

---

## Structured Data

- **JSON-LD preferred** over Microdata and RDFa
- Always include `@context` and `@type`
- Only mark up content **visible on the page**
- Validate in the Rich Results Test before deploying
- Keep markup in step with the page — stale dates, prices or authors are schema drift
- Prefer a single connected `@graph` per page over isolated blocks
  (see `seo/references/entity-schema-graph.md`)

**Never** ship `aggregateRating` without visible reviews, or author markup naming someone
who has left the organisation. Both are guideline and trust problems, not style choices.

Type status (deprecated, restricted, current) lives in `seo/references/schema-types.md`.
Do not duplicate that list here.

---

## Penalties and Recovery

### Manual Actions
Reported in Search Console. Common causes: unnatural links, thin content, cloaking or
sneaky redirects, user-generated spam, spammy structured data.

**On disavow:** Google's guidance is that **most sites never need the disavow tool**.
SpamBrain neutralises the overwhelming majority of link spam automatically. Use it only
for (a) an active manual action for unnatural links, or (b) a documented negative-SEO
event you cannot resolve at the source. Routine "hygiene" disavow files are net-negative
and can strip legitimate signals. Do not recommend disavow as a default remedy.

### Algorithmic Demotions
No notification; detected via ranking timelines.
- **Helpful Content System**: merged into core ranking in March 2024, no longer standalone.
- **Core Updates**: broad quality reassessment.
- **Spam / Link Spam Updates**: automated detection and devaluation.

### Recovery
1. Identify the issue (Search Console, ranking timeline)
2. Fix the root cause
3. Manual action → reconsideration request; algorithmic → improve and wait for reassessment
4. Monitor Search Console performance **and** the generative AI reports, since a shift
   between surfaces can look like a loss when it is not

---

## Official Documentation Links

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [How Google Search Works](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Structured Data Overview](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Understanding Page Experience](https://developers.google.com/search/docs/appearance/page-experience)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Disavow links](https://support.google.com/webmasters/answer/2648487)
- [Generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)
- [Google Search Status Dashboard](https://status.search.google.com/)
- [Google Search Central Blog](https://developers.google.com/search/blog)

> E-E-A-T is defined in Google's Search Quality Rater Guidelines, published separately as
> a PDF and revised periodically. The rater guidelines describe how humans evaluate
> quality; they are not a direct description of ranking systems. Treat them as intent, not
> algorithm.
