<!-- Updated: 2026-09-02 -->
# Agency/Consultancy SEO Strategy Template

## Industry Characteristics

- Service-based, high-value transactions
- Expertise and trust are paramount
- Long consideration cycles
- Portfolio/case study driven decisions
- Relationship-based sales
- Niche specialization benefits

## Recommended Site Architecture

```
/
├── Home
├── /services
│   ├── /service-1
│   │   ├── /sub-service-1
│   │   └── ...
│   └── /service-2
├── /industries
│   ├── /industry-1
│   ├── /industry-2
│   └── ...
├── /work (or /case-studies)
│   ├── /case-study-1
│   ├── /case-study-2
│   └── ...
├── /about
│   ├── /team
│   │   ├── /team-member-1
│   │   └── ...
│   ├── /culture
│   └── /careers
├── /insights (or /blog)
│   ├── /articles
│   ├── /guides
│   ├── /webinars
│   └── /podcasts
├── /contact
├── /process
└── /faq
```

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | Organization, ProfessionalService |
| Service Page | Service, ProfessionalService |
| Case Study | Article, Organization (client) |
| Team Member | Person, ProfilePage |
| Blog | Article, BlogPosting |

### ProfessionalService Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Agency Name",
  "description": "What the agency does",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Agency St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "areaServed": "National",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Service 1"
        }
      }
    ]
  }
}
```

## E-E-A-T Requirements

### Team Pages Must Include
- Professional headshots
- Detailed bios with credentials
- Industry experience
- Speaking engagements
- Publications
- Social profiles

### Case Studies Must Include
- Client name (with permission) or industry
- Challenge/problem statement
- Approach/methodology
- Results with specific metrics
- Timeline
- Testimonial quote

## Content Priorities

### High Priority
1. Service pages (detailed, specific)
2. Industry pages (vertical expertise)
3. 3-5 detailed case studies
4. Team/leadership pages

### Medium Priority
1. Methodology/process page
2. Blog with thought leadership
3. Comparison content (vs alternatives)
4. FAQ page

### Thought Leadership Topics
- Industry trend analysis
- How-to guides (non-competitive)
- Original research/surveys
- Event recaps and insights
- Expert interviews
- Tool/technology reviews

## Content Strategy

### Service Pages (min 800 words)
- Clear value proposition
- Methodology overview
- Deliverables list
- Relevant case studies
- Team members who deliver this service
- CTA to schedule consultation

### Industry Pages (min 800 words)
- Industry-specific challenges
- How you solve them differently
- Relevant case studies
- Industry credentials/experience
- Client logos (with permission)

### Case Studies (min 1,000 words)
- Executive summary
- Client background
- Challenge details
- Solution approach
- Implementation process
- Measurable results
- Client testimonial
- Related services/CTA

## Key Metrics to Track

- Organic traffic to service pages
- Case study page views
- Contact form submissions from organic
- Time on page for key content
- Blog → service page conversion

## Generative Engine Optimization (GEO) for Agencies

- [ ] Publish original case studies with specific, citable metrics and results
- [ ] Use Person schema with sameAs links for all team members (builds entity authority)
- [ ] Use ProfilePage schema for team member pages
- [ ] Include clear, quotable expertise statements in service page descriptions
- [ ] Produce original industry research and surveys AI systems can cite
- [ ] Structure thought leadership content with clear headings and extractable insights
- [ ] Maintain consistent agency entity information across directories, social profiles, and industry sites
- [ ] Monitor AI citation in ChatGPT, Perplexity, and Google AI Overviews for brand and key service terms

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

**Agency note:** case studies with real, named outcomes are your highest information-gain
asset and the thing AI engines can actually cite. Publish them with numbers. Founder and
team credentials belong in `Person` markup, not only in prose on an about page.
