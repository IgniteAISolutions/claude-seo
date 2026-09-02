<!-- Updated: 2026-09-02 -->
# Generic Business SEO Strategy Template

## Overview

This template applies to businesses that don't fit neatly into SaaS, local service, e-commerce, publisher, or agency categories. Customize based on your specific business model.

## Recommended Site Architecture

```
/
├── Home
├── /products (or /services)
│   ├── /product-1
│   ├── /product-2
│   └── ...
├── /solutions (if applicable)
│   ├── /solution-1
│   └── ...
├── /about
│   ├── /team
│   ├── /history
│   └── /values
├── /resources
│   ├── /blog
│   ├── /guides
│   ├── /faq
│   └── /glossary
├── /contact
├── /support
└── /legal
    ├── /privacy
    └── /terms
```

## Universal SEO Principles

### Every Page Should Have
- Unique title tag (30-60 chars)
- Unique meta description (120-160 chars)
- Single H1 matching page intent
- Logical heading hierarchy (H1→H2→H3)
- Internal links to related content
- Clear call-to-action

### Schema for All Sites
| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, WebSite |
| About | Organization, AboutPage |
| Contact | ContactPage |
| Blog | Article, BlogPosting |
| FAQ | (FAQPage only for gov/health) |
| Product/Service | Product or Service |

## Content Quality Standards

### Minimum Word Counts
| Page Type | Min Words |
|-----------|-----------|
| Homepage | 500 |
| Product/Service | 800 |
| Blog Post | 1,500 |
| About Page | 400 |
| Landing Page | 600 |

### E-E-A-T Essentials
1. **Experience**: Share real examples and case studies
2. **Expertise**: Display credentials and qualifications
3. **Authoritativeness**: Earn mentions and citations
4. **Trustworthiness**: Full contact info, policies visible

## Technical Foundations

### Must-Haves
- [ ] HTTPS enabled
- [ ] Mobile-responsive design
- [ ] robots.txt configured
- [ ] XML sitemap submitted
- [ ] Google Search Console verified
- [ ] Core Web Vitals passing (LCP <2.5s, INP <200ms, CLS <0.1)

### Should-Haves
- [ ] Structured data on key pages
- [ ] Internal linking strategy
- [ ] 404 error page optimized
- [ ] Redirect chains eliminated
- [ ] Image optimization (WebP, lazy loading)

## Content Priorities

### Phase 1: Foundation (weeks 1-4)
1. Homepage optimization
2. Core product/service pages
3. About and contact pages
4. Basic schema implementation

### Phase 2: Expansion (weeks 5-12)
1. Blog launch (2-4 posts/month)
2. FAQ page
3. Additional product/service pages
4. Internal linking audit

### Phase 3: Growth (weeks 13-24)
1. Consistent content publishing
2. Link building outreach
3. GEO optimization
4. Performance optimization

### Phase 4: Authority (months 7-12)
1. Thought leadership content
2. Original research
3. PR and media mentions
4. Advanced schema

## Key Metrics to Track

- Organic traffic (overall and by section)
- Keyword rankings (branded and non-branded)
- Conversion rate from organic
- Pages indexed
- Core Web Vitals scores
- Backlinks acquired

## Customization Points

Adjust this template based on:

1. **Business Model**: B2B vs B2C vs D2C
2. **Geographic Scope**: Local, national, or international
3. **Content Type**: Product-focused vs content-heavy
4. **Competition Level**: Niche vs competitive market
5. **Resources**: Budget and team capacity

## Generative Engine Optimization (GEO) Checklist

- [ ] Include clear, quotable facts and statistics that AI systems can extract and cite
- [ ] Use structured data (Schema.org) to help AI systems understand content
- [ ] Build topical authority through comprehensive content clusters
- [ ] Provide original data, research, or unique perspectives AI cannot find elsewhere
- [ ] Maintain consistent entity information (brand, people, products) across the web
- [ ] Structure content with clear headings, definitions, and step-by-step formats
- [ ] Consider adding an `llms.txt` file at site root (emerging convention for AI crawlers — Google treats it as a regular text file)
- [ ] Monitor AI citation across Google AI Overviews, ChatGPT, Perplexity, and Bing Copilot

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

**Industry note:** with no vertical specialism to lean on, information gain is the whole
game. Original data, real examples and first-hand process documentation are what separate
this plan from every other generic site competing for the same terms.
