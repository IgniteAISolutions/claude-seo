<!-- Updated: 2026-09-02 -->
# Entity Schema — Connected @graph Architecture

Schema markup has moved from "a tactic for rich snippets" to **the mechanism by which
machines resolve who you are**. This reference covers connected entity graphs, external
knowledge-base alignment, and machine-readable E-E-A-T.

Pairs with `schema-types.md` (which types are valid) and `eeat-framework.md` (what to prove).

## The problem with fragmented schema

Most sites ship isolated schema blocks: a standalone `Article`, an unlinked `FAQPage`, an
`Organization` that references nothing. Each block is individually valid and collectively
meaningless, because nothing states how the entities relate.

A connected `@graph` states the relationships explicitly, so a crawler or an LLM does not
have to infer them from prose.

## The pattern

Wrap all page entities in a single `@graph` array. Give every node a stable, canonical
`@id` using a URL fragment. Reference nodes by `@id` instead of repeating their definitions.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Ltd",
      "url": "https://example.com/",
      "sameAs": ["https://www.wikidata.org/wiki/Q00000000"]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com/",
      "publisher": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "Person",
      "@id": "https://example.com/about#jane-doe",
      "name": "Jane Doe",
      "worksFor": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "Article",
      "@id": "https://example.com/post#article",
      "headline": "…",
      "author": { "@id": "https://example.com/about#jane-doe" },
      "publisher": { "@id": "https://example.com/#organization" },
      "isPartOf": { "@id": "https://example.com/#website" }
    }
  ]
}
```

**Rules:**
1. One `@graph` per page. Do not ship multiple competing `<script>` blocks that redefine the same entity.
2. Every node gets an `@id`. Use `#fragment` identifiers so they are globally unique and stable.
3. Reference, do not repeat. `{"@id": "…"}` instead of a duplicated object.
4. `@id` values must never change once published. They are the entity's persistent identity.

## External alignment: sameAs and Wikidata

`sameAs` resolves ambiguity by anchoring your entity to an external knowledge base. Without
it, an engine has to guess whether "Ignite AI" is your company, a different company, or a
product.

**Priority order for `sameAs` targets:**
1. **Wikidata QID** — the strongest signal. Anchors directly to the global knowledge graph.
2. **Wikipedia article** — where one legitimately exists.
3. **Official profiles** — LinkedIn company/person, Companies House, industry registries.
4. **Authored profiles** — publication author pages, conference speaker pages.

Only ever assert `sameAs` for profiles that genuinely belong to the entity. A wrong or
aspirational `sameAs` is a trust problem, not a shortcut.

## Machine-readable E-E-A-T: the Person node

This is where most sites lose E-E-A-T value. Credentials sit in prose that a human reads and
a machine does not parse into structured claims. The `Person` node converts a bio into
machine-readable evidence.

| Property | Carries | Example |
|----------|---------|---------|
| `jobTitle` | Role | "Chief AI Officer" |
| `worksFor` | Organisational tie | `{"@id": "…#organization"}` |
| `knowsAbout` | Topical expertise | ISO 42001, AI governance |
| `hasCredential` | Formal qualification | `EducationalOccupationalCredential` |
| `alumniOf` | Institutional background | University, institution |
| `award` | Recognition | Named awards and honours |
| `sameAs` | External verification | LinkedIn, publication author page, Wikidata |

```json
{
  "@type": "Person",
  "@id": "https://example.com/about#jane-doe",
  "name": "Jane Doe",
  "jobTitle": "Chief AI Officer",
  "worksFor": { "@id": "https://example.com/#organization" },
  "knowsAbout": ["AI governance", "ISO 42001"],
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "certification",
    "name": "Certified Chief AI Officer"
  },
  "award": ["Named industry award 2026"],
  "sameAs": [
    "https://www.linkedin.com/in/…",
    "https://www.publication.com/author/…"
  ]
}
```

**Audit rule:** every credential, award and byline visible in page copy should have a
corresponding structured property, and every structured claim should be visible on the page.
Structured data that asserts something the page does not show is a drift risk (below).

## Schema drift

**Schema drift** is when structured data and visible content disagree. It happens whenever
copy is updated and markup is not.

Common drift, all of it damaging:
- `dateModified` that never changes while the article is edited
- Prices in `Offer` that no longer match the pricing table
- `author` naming someone who has left the organisation
- `aggregateRating` with no visible reviews on the page
- Availability, opening hours or contact details out of step with the page

Two of these are severe. **Review markup without visible reviews** breaches Google's
guidelines and risks a manual action. **An author who has departed** is both a drift error
and a factual misrepresentation of who stands behind the content.

**Audit step:** diff every structured claim against the rendered page. Flag any mismatch as
Critical when it concerns reviews, pricing, or authorship; High otherwise.

## Why this matters beyond Google

For retrieval-augmented systems, structured markup is materially cheaper to parse than raw
HTML. An LLM extracting claims from a clean `@graph` does far less work than one inferring
relationships from a DOM. Cheaper, unambiguous extraction means a higher chance of being
selected and correctly attributed.

## Validation checklist

- [ ] Single `@graph` per page, no competing duplicate blocks
- [ ] Every node has a stable `@id` fragment
- [ ] Entities referenced by `@id`, not redefined inline
- [ ] `Organization` node is the anchor and is referenced by `publisher`
- [ ] `Person` node carries `knowsAbout`, `hasCredential`, `award`, `sameAs` where genuine
- [ ] `sameAs` includes a Wikidata QID where one legitimately exists
- [ ] Author entities reflect **current** staff only
- [ ] No `aggregateRating` without visible reviews
- [ ] `dateModified` matches real edit history
- [ ] Validated in [Rich Results Test](https://search.google.com/test/rich-results) and [Schema validator](https://validator.schema.org/)
