---
name: seo-geo
description: >
  Optimize content for AI Overviews (formerly SGE), ChatGPT web search,
  Perplexity, and other AI-powered search experiences. Generative Engine
  Optimization (GEO) analysis including brand mention signals, AI crawler
  accessibility, llms.txt compliance, passage-level citability scoring, and
  platform-specific optimization. Use when user says "AI Overviews", "SGE",
  "GEO", "AI search", "LLM optimization", "Perplexity", "AI citations",
  "ChatGPT search", or "AI visibility".
---

# AI Search / GEO Optimization (February 2026)

## Why GEO matters

AI surfaces are now a primary discovery route: AI Overviews and AI Mode appear across a
large and growing share of queries, and ChatGPT, Perplexity and Claude all resolve
questions that previously produced a click. The direction is not in dispute.

**Do not quote usage or market-share figures from this file.** Adoption numbers move
monthly, are reported inconsistently, and go stale faster than this repo updates. If a
client deliverable needs a figure, pull it from the provider's own current disclosure and
date it. For your own measurement, use first-party Search Console data
(`references/search-console-ai-reports.md`), which is the only AI-visibility number you can
actually stand behind for a given site.

## Critical Insight: Brand Mentions > Backlinks

Brand mentions across third-party platforms correlate more strongly with AI visibility than
backlink metrics do (Ahrefs, December 2025, 75,000 brands).

> Vendor correlation study, not peer-reviewed, and correlation is not causation. Attribute
> it if you cite it. The actionable point stands on its own: being *talked about* on
> platforms AI engines draw from matters, and a backlink-only strategy misses it.

| Signal | Correlation with AI Citations |
|--------|------------------------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit mentions | High |
| Wikipedia presence | High |
| LinkedIn presence | Moderate |
| Domain Rating (backlinks) | ~0.266 (weak) |

**Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query — platform-specific optimization is essential.

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Two complementary structures — write both, they are not alternatives:**

| Structure | Length | Purpose |
|-----------|--------|---------|
| Canonical answer block | **40–58 words** | The extractable direct answer, immediately under a question-formatted H2/H3 |
| Supporting citable passage | ~130–170 words | The surrounding depth that generative engines quote from |

See `references/aeo-geo-benchmarks.md` for extraction mechanics and the evidence base.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (no unresolved pronouns — must parse standalone)
- Direct answer opens the section, before any preamble
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

Organic rank and AI citation are **separate objectives with separate selection logic**.
Strong organic position does not guarantee citation, and pages ranking below the fold are
routinely cited. Measure them independently — see `references/search-console-ai-reports.md`
for baselining AI impressions from first-party Search Console data.

**Strong signals:**
- Clean H1→H2→H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**Most AI crawlers have limited or no JavaScript execution** — server-side rendering is the
safe default. Rendering support varies by crawler and changes often, so never assume a
client-rendered page is visible to a given engine. Verify against the raw HTML response.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt` for these AI crawlers:

| Crawler | Owner | Purpose |
|---------|-------|---------|
| GPTBot | OpenAI | ChatGPT web search |
| OAI-SearchBot | OpenAI | OpenAI search features |
| ChatGPT-User | OpenAI | ChatGPT browsing |
| ClaudeBot | Anthropic | Claude web features |
| PerplexityBot | Perplexity | Perplexity AI search |
| CCBot | Common Crawl | Training data (often blocked) |
| anthropic-ai | Anthropic | Claude training |
| Bytespider | ByteDance | TikTok/Douyin AI |
| cohere-ai | Cohere | Cohere models |

**Recommendation:** Allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot for AI search visibility. Block CCBot and training crawlers if desired.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Skews to ranking pages, but not exclusively | Traditional SEO + answer-block optimization |
| **Google AI Mode** | Query fan-out across many sub-queries | Broad topical coverage; depth per sub-question |
| **ChatGPT** | Wikipedia, Reddit, authoritative reference | Entity presence, external validation |
| **Perplexity** | Reddit, Wikipedia, community sources | Community validation, discussions |
| **Claude** | Cited web sources via search | Clean structure, verifiable claims |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

> Platform citation-share percentages circulate widely but move fast and are rarely
> reproducible. Report them only with a dated source, or measure directly.

---

## Output

Generate `GEO-ANALYSIS.md` with:

1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity scores)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Server-Side Rendering Check** (JavaScript dependency analysis)
8. **Top 5 Highest-Impact Changes**
9. **Schema Recommendations** (for AI discoverability)
10. **Content Reformatting Suggestions** (specific passages to rewrite)

---

## Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

## Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

## High Impact

1. Create original research/surveys (unique citability)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `ai_optimization_chat_gpt_scraper` to check what ChatGPT web search returns for target queries (real GEO visibility check) and `ai_opt_llm_ment_search` with `ai_opt_llm_ment_top_domains` for LLM mention tracking across AI platforms.
