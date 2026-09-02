<!-- Updated: 2026-09-02 -->
# Core Web Vitals Thresholds

## Current Metrics

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5s–4.0s | >4.0s |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 |

## Key Facts
- INP replaced FID (First Input Delay) on **March 12, 2024**. FID was fully removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on **September 9, 2024**. INP is the sole interactivity metric.
- Evaluation uses the **75th percentile** of real user data (field data from CrUX).
- Google assesses at the **page level** and the **origin level**.
- Core Web Vitals are a **tiebreaker** ranking signal — they matter most when content quality is similar between competitors.
- **Thresholds unchanged since original definitions** — ignore claims of "tightened thresholds" from SEO blogs.
- December 2025 core update appeared to weight **mobile CWV more heavily**.
- Roughly half of sites pass all three CWV, with mobile trailing desktop. Pull a current
  figure from the CrUX public dataset if a deliverable needs one; the split moves each release.

## LCP Subparts (February 2025 CrUX Addition)

LCP can now be broken into diagnostic subparts:

| Subpart | What It Measures | Target |
|---------|------------------|--------|
| **TTFB** | Time to First Byte (server response) | <800ms |
| **Resource Load Delay** | Time from TTFB to resource request start | Minimize |
| **Resource Load Time** | Time to download the LCP resource | Depends on size |
| **Element Render Delay** | Time from resource loaded to rendered | Minimize |

**Total LCP = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay**

Use this breakdown to identify which phase is causing LCP issues.

## Soft Navigations API (Experimental)

**Soft Navigations API** — measures CWV across SPA route changes. Status has moved through
several Chrome milestones; verify current availability before relying on it.

- Addresses the long-standing SPA measurement blind spot
- Currently experimental, **no ranking impact yet**
- Detects "soft navigations" (URL changes without full page load)
- May affect future SPA CWV measurement

**Detection:** Check for SPA frameworks (React, Vue, Angular, Svelte) and warn about current CWV measurement limitations.

## Measurement Sources

### Field Data (Real Users)
- Chrome User Experience Report (CrUX)
- PageSpeed Insights (uses CrUX data)
- Search Console Core Web Vitals report

### Lab Data (Simulated)
- Lighthouse
- WebPageTest
- Chrome DevTools

> Field data is what Google uses for ranking. Lab data is useful for debugging.

## Common Bottlenecks

### LCP (Largest Contentful Paint)
- Unoptimized hero images (compress, use WebP/AVIF, add preload)
- Render-blocking CSS/JS (defer, async, critical CSS inlining)
- Slow server response (TTFB >800ms — use edge CDN, caching)
- Third-party script blocking (defer analytics, chat widgets)
- Web font loading delay (use font-display: swap + preload)

### INP (Interaction to Next Paint)
- Long JavaScript tasks on main thread (break into smaller tasks <50ms)
- Heavy event handlers (debounce, use requestAnimationFrame)
- Excessive DOM size (>1,500 elements is concerning)
- Third-party scripts hijacking main thread
- Synchronous XHR or localStorage operations
- Layout thrashing (multiple forced reflows)

### CLS (Cumulative Layout Shift)
- Images/iframes without width/height dimensions
- Dynamically injected content above existing content
- Web fonts causing layout shift (use font-display: swap + preload)
- Ads/embeds without reserved space
- Late-loading content pushing down the page

## Optimization Priority

1. **LCP** — Most impactful for perceived performance
2. **CLS** — Most common issue affecting user experience
3. **INP** — Matters most for interactive applications

## Tools

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json --output-path report.json
```

## Performance Tooling Notes

- **Lighthouse 13.0** (October 2025): Major audit restructuring with reorganized performance categories and updated scoring weights. Lighthouse is a lab tool (simulated conditions) — always cross-reference with CrUX field data for real-world performance.
- **CrUX Vis** replaced the CrUX Dashboard (November 2025). The old Looker Studio dashboard was deprecated. Use [CrUX Vis](https://cruxvis.withgoogle.com) or the CrUX API directly.
- **LCP subparts** added to CrUX (February 2025): Time to First Byte (TTFB), resource load delay, resource load time, and element render delay are now available as sub-components of LCP in CrUX data.
- **Search Console**: branded vs non-branded query filters, hourly API data, chart
  annotations. For AI-surface reporting see `search-console-ai-reports.md` — the generative
  AI performance reports (June 2026) superseded the earlier feature set described here.

> **Mobile-first indexing** is 100% complete as of July 5, 2024. Google now crawls and indexes ALL websites exclusively with the mobile Googlebot user-agent. Ensure your mobile version contains all critical content, structured data, and meta tags.
