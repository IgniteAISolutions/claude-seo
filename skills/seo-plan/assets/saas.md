<!-- Updated: 2026-09-02 -->
# SaaS SEO Strategy Template

## Industry Characteristics

- Long sales cycles with multiple touchpoints
- Feature-focused decision making
- Comparison shopping behavior
- Heavy research phase before purchase
- Integration and ecosystem considerations

## Recommended Site Architecture

```
/
├── Home
├── /product (or /platform)
│   ├── /features
│   │   ├── /feature-1
│   │   ├── /feature-2
│   │   └── ...
│   ├── /integrations
│   │   ├── /integration-1
│   │   └── ...
│   └── /security
├── /solutions
│   ├── /by-industry
│   │   ├── /industry-1
│   │   └── ...
│   └── /by-use-case
│       ├── /use-case-1
│       └── ...
├── /pricing
├── /customers
│   ├── /case-studies
│   │   ├── /case-study-1
│   │   └── ...
│   └── /testimonials
├── /resources
│   ├── /blog
│   ├── /guides
│   ├── /webinars
│   ├── /templates
│   └── /glossary
├── /docs (or /help)
│   └── /api
├── /company
│   ├── /about
│   ├── /careers
│   ├── /press
│   └── /contact
└── /compare
    ├── /vs-competitor-1
    └── /vs-competitor-2
```

## Content Priorities

### High Priority Pages
1. Homepage (value proposition, social proof)
2. Features overview
3. Pricing page
4. Key integrations
5. Top 3-5 use case pages

### Medium Priority Pages
1. Individual feature pages
2. Industry solution pages
3. Case studies (2-3 detailed ones)
4. Comparison pages (vs competitors)

### Content Marketing Focus
1. Bottom-of-funnel: Comparison guides, ROI calculators
2. Middle-of-funnel: How-to guides, best practices
3. Top-of-funnel: Industry trends, educational content

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, WebSite, SoftwareApplication |
| Product/Features | SoftwareApplication, Offer |
| Pricing | SoftwareApplication, Offer (with pricing) |
| Blog | Article, BlogPosting |
| Case Studies | Article, Organization (customer) |
| Documentation | TechArticle |

## Key Metrics to Track

- Organic traffic to pricing page
- Demo/trial signups from organic
- Blog → pricing page conversion
- Comparison page rankings
- Integration page performance

## Comparison & Alternative Pages

Comparison pages are among the highest-converting content types for SaaS, with conversion rates of **4-7%** vs. 0.5-1.8% for standard blog content (35.8% of marketers report comparison content performs "better than ever" per Intergrowth November 2025 survey).

**Recommended page types:**
- `/{product}-vs-{competitor}` — Direct 1:1 comparison
- `/{competitor}-alternative` — Targeting competitor brand searches
- `/compare/{category}` — Category comparison hub
- `/best-{category}-tools` — Roundup-style pages

**Best practices:**
- Include structured comparison tables with pricing, features, pros/cons
- Be factually accurate about competitors — verify claims regularly
- Include customer testimonials from users who switched
- Add FAQ schema for common comparison questions (valuable for AI search)
- Update regularly — stale comparison data damages credibility
- Cross-reference the `seo-competitor-pages` skill for detailed frameworks

**Legal considerations:**
- Nominative fair use generally permits competitor brand mentions for comparison purposes
- Do NOT imply endorsement or affiliation
- Do NOT make false or unverifiable claims about competitor products
- Different jurisdictions have different trademark laws — consult legal counsel

## Competitive Considerations

- Monitor competitor feature releases
- Track competitor content strategies
- Identify keyword gaps in feature coverage
- Watch for new comparison opportunities

## Generative Engine Optimization (GEO) for SaaS

- [ ] Include clear, structured feature comparisons that AI systems can parse and cite
- [ ] Use SoftwareApplication schema with complete feature lists and pricing
- [ ] Publish original benchmark data, case studies, and ROI metrics
- [ ] Build content clusters around key product categories and use cases
- [ ] Ensure integration pages have clear, quotable descriptions
- [ ] Structure pricing information in tables AI can extract
- [ ] Monitor AI citation across Google AI Overviews, ChatGPT, and Perplexity

---

## Modern Search Readiness

Applies to every plan in this file. Rank and AI citation are separate outcomes: a page can
rank well and never be cited. Cover both.

**1. Stay citable.** Confirm retrieval crawlers are not blocked in robots.txt **or at the
CDN/WAF edge**: `OAI-SearchBot`, `ClaudeBot`, `Claude-SearchBot`, `PerplexityBot`, `GPTBot`.
Also check the Search Console AI features toggle. A blocked retrieval agent is Critical.

**2. Answer-first structure.** Every page targeting a question opens that section with a
**40-58 word self-contained answer** under a question-formatted H2/H3, before any preamble.
Comparisons become tables; processes become numbered lists.

**3. Fact density.** At least one verifiable statistic, named entity or cited source per
100 words. Evidence is what generative engines quote.

**4. Entity graph.** One connected `@graph` per page with stable `@id` values, authors as
`Person` nodes (never bare name strings), and `sameAs` to genuine external profiles.

**5. Information gain.** For each planned page ask: what does this contain that the current
top 10 do not? If there is no answer, the page has an originality problem, not a keyword one.

**6. Measure it.** Baseline AI visibility from the Search Console generative AI reports.
They carry impressions only, with **no click data**, so never report an AI-surface CTR.

References: `seo/references/aeo-geo-benchmarks.md`,
`seo/references/entity-schema-graph.md`, `seo/references/search-console-ai-reports.md`.

**SaaS note:** comparison and alternatives pages are heavily surfaced in AI answers, so
build them as genuine feature tables with sourced claims rather than marketing prose.
Docs and help-centre content are strong citation targets; keep them crawlable and never
place them behind JS-only rendering or a login wall.
