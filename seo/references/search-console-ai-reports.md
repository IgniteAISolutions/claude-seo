<!-- Updated: 2026-09-02 -->
# Google Search Console — Generative AI Reporting (2026)

**Status: current as of September 2026.** This supersedes any guidance that treats
Search Console as organic-clicks-only reporting.

## What changed

Google launched **Search Generative AI performance reports** in Search Console on
**3 June 2026**, with global rollout to all properties completed **31 August 2026**.
Before this, impressions inside AI Overviews were folded into overall Search totals
with no way to isolate them.

| Feature | Launched | What it does |
|---------|----------|--------------|
| Generative AI performance reports (Search) | 3 Jun 2026 (global 31 Aug 2026) | Dedicated view of impressions inside AI Overviews and AI Mode |
| Generative AI performance reports (Discover) | 3 Jun 2026 | Same for generative AI features in Discover |
| AI features blocking control | Global 31 Aug 2026 | Toggle to exclude a site from AI Overviews / AI Mode / AI Overviews in Discover |
| Preferred Sources in AI surfaces | 2026 | Users' Preferred Sources choices now carry into AI Overviews and AI Mode |

Sources: [Google Search Central](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports),
[Google blog](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/),
[Search Engine Land](https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269).

## The critical limitation — do not misreport this

**The generative AI reports include impressions, pages, countries, devices and dates.
They do NOT include click data.**

This matters for every audit and every client report:

- You can measure **AI visibility** (are we being surfaced in AI Overviews / AI Mode).
- You **cannot** measure AI-surface CTR or clicks from these reports.
- Never present an AI-surface "CTR" derived from these reports. The denominator exists;
  the numerator does not. Any CTR figure would be fabricated.
- Falling total clicks alongside rising AI impressions is the expected shape of
  zero-click behaviour. Report it as such rather than as a ranking loss.

## How to use it in an audit

1. **Baseline AI visibility.** Pull the generative AI report and record impressions by page.
   This is the first reliable measure of GEO performance from a first-party source.
2. **Compare surfaces.** Diff the pages appearing in generative AI reports against the
   pages ranking in standard Search. Low overlap is normal (see below) and shows which
   assets earn AI citation versus classic rank.
3. **Find the GEO gap.** Pages with strong organic rank but no generative AI impressions
   are the priority candidates for answer-first restructuring (see `aeo-geo-benchmarks.md`).
4. **Track after changes.** Generative AI impressions are the metric that moves when
   answer blocks, statistics and citations are added.

## Overlap between organic rank and AI citation

Organic top-10 position does not guarantee AI Overview citation. Measured overlap between
Google's top-10 organic results and the domains cited in AI Overviews is materially
incomplete, so treat classic rank and AI citation as **two separate objectives** with two
separate measurements. A page can hold position 3 and never be cited, and a page ranking
below the fold can be cited.

## The blocking control — advise carefully

The new toggle lets a site exclude itself from AI Overviews, AI Mode and AI Overviews in
Discover.

**Default recommendation: leave it off (stay eligible).** Opting out removes the site from
a surface that is now a primary discovery route, and the impressions lost are not recovered
elsewhere.

Only consider opting out where the client has a specific, deliberate reason (for example a
licensing or paywall position they have decided commercially). Flag it as a business
decision, never apply it as a default technical fix.

## Audit checklist

- [ ] Generative AI performance report reviewed (Search and Discover)
- [ ] AI impressions baselined by page
- [ ] Pages with organic rank but zero AI impressions identified
- [ ] AI features blocking toggle confirmed OFF (unless deliberately set)
- [ ] No AI-surface CTR reported anywhere (click data does not exist)
- [ ] Reported alongside `aeo-geo-benchmarks.md` recommendations
