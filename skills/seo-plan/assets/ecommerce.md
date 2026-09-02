<!-- Updated: 2026-09-02 -->
# E-commerce SEO Strategy Template

## Industry Characteristics

- High transaction intent
- Product comparison behavior
- Price sensitivity
- Visual-first decision making
- Seasonal demand patterns
- Competitive marketplace listings

## Recommended Site Architecture

```
/
├── Home
├── /collections (or /categories)
│   ├── /category-1
│   │   ├── /subcategory-1
│   │   └── ...
│   ├── /category-2
│   └── ...
├── /products
│   ├── /product-1
│   ├── /product-2
│   └── ...
├── /brands
│   ├── /brand-1
│   └── ...
├── /sale (or /deals)
├── /new-arrivals
├── /best-sellers
├── /gift-guide
├── /blog
│   ├── /buying-guides
│   ├── /how-to
│   └── /trends
├── /about
├── /contact
├── /shipping
├── /returns
└── /faq
```

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Product Page | Product, Offer, AggregateRating, Review, BreadcrumbList |
| Category Page | CollectionPage, ItemList, BreadcrumbList |
| Brand Page | Brand, Organization |
| Blog | Article, BlogPosting |

### Additional E-commerce Schema (2025)

- **ProductGroup**: Use for products with variants (size, color). Wraps individual Product entries with `variesBy` and `hasVariant` properties. See `schema/templates.json`.
- **Certification**: For product certifications (Energy Star, safety, organic). Replaced EnergyConsumptionDetails (April 2025). Use `hasCertification` on Product.
- **OfferShippingDetails**: Include shipping rate, handling time, and transit time. Critical for Merchant Center eligibility.

> **Google Merchant Center Free Listings:** Products can appear in Google Shopping for free. Ensure Product structured data is in the initial server-rendered HTML (not JavaScript-injected) with required properties: `name`, `image`, `price`, `priceCurrency`, `availability`.

> **JS Rendering Note:** Product structured data should be in initial server-rendered HTML — not dynamically injected via JavaScript (per December 2025 Google JS SEO guidance).

### Product Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/product.jpg"],
  "description": "Product description",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/product"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "42"
  }
}
```

## Content Requirements

### Product Pages (min 400 words)
- Unique product descriptions (not manufacturer copy)
- Feature highlights
- Use cases / who it's for
- Specifications table
- Size/fit guide (for apparel)
- Care instructions
- Customer reviews

### Category Pages (min 400 words)
- Category introduction
- Buying guide excerpt
- Featured products
- Subcategory links
- Filter/sort options

## Technical Considerations

### Pagination
- Self-referencing canonical per page plus crawlable links (rel=next/prev unsupported since 2019)
- Ensure all products are crawlable
- Canonical to main category page

### Faceted Navigation
- Noindex filter combinations that create duplicate content
- Use canonical tags appropriately
- Ensure popular filters are indexable

### Product Variations
- Single URL for parent product with variants
- Or separate URLs with canonical to parent
- Structured data for all variants

## Content Priorities

### High Priority
1. Category pages (top level)
2. Best-selling product pages
3. Homepage
4. Buying guides for main categories

### Medium Priority
1. Subcategory pages
2. Brand pages
3. Comparison content
4. Seasonal landing pages

### Blog Topics
- Buying guides ("How to Choose...")
- Product comparisons
- Trend reports
- Use cases and inspiration
- Care and maintenance guides

## Key Metrics to Track

- Revenue from organic search
- Product page rankings
- Category page rankings
- Click-through rate (rich results)
- Average order value from organic

## Generative Engine Optimization (GEO) for E-commerce

AI search platforms increasingly answer product queries directly. Optimize for AI citation:

- [ ] Include clear product specifications, dimensions, materials in structured format
- [ ] Use ProductGroup schema for variant products
- [ ] Provide original product photography with descriptive alt text
- [ ] Include genuine customer review content (AggregateRating schema)
- [ ] Maintain consistent product entity data across all platforms (site, Amazon, Merchant Center)
- [ ] Structure comparison content with clear feature tables AI can parse
- [ ] Add detailed FAQ content for common product questions

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

**E-commerce note:** product specifications are the highest-value citable content you have,
so keep them in server-rendered HTML as structured specs rather than JS-injected prose.
Never ship `aggregateRating` without visible reviews on the page: it is a guideline breach
and the fastest way to lose trust signals across every surface at once.
