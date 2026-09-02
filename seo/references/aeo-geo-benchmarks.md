<!-- Updated: 2026-09-02 -->
# AEO & GEO — Benchmarks and Passage Mechanics

Evidence base for answer-engine and generative-engine optimization. **Peer-reviewed
findings are separated from vendor claims below.** Cite accordingly: never present a
vendor blog figure as research.

## The three retrieval layers

Modern visibility is won across three distinct systems, each with different selection logic.
Optimising for one does not deliver the others.

| Layer | Mechanism | Ranking driver | Output |
|-------|-----------|----------------|--------|
| **SEO** | Crawlers + inverted index | Link topology, lexical match, user interaction | Classic organic results |
| **AEO** | Neural passage segmentation, cross-encoder re-ranking | Direct extractable answers, concise syntax | Featured snippets, answer boxes, zero-click |
| **GEO** | Dense vector retrieval, multi-source RAG synthesis | Fact density, quotations, citations | AI Overviews, ChatGPT, Perplexity, Claude |

A page can rank top-3 organically and never be cited in an AI Overview. Treat classic rank
and AI citation as **separate objectives with separate measurement** (see
`search-console-ai-reports.md`).

---

## Peer-reviewed: the Princeton GEO benchmark

**Source:** Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan & Deshpande.
*GEO: Generative Engine Optimization.* ACM SIGKDD 2024. [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)

**Method:** GEO-bench, approximately 10,000 queries across 9 datasets.

**Two metrics defined by the study:**
- **Position-Adjusted Word Count (PAWC)** — volume of the AI answer attributable to a
  source, weighted by where the citation appears. Earlier citations score higher.
- **Subjective Impression** — citation quality across relevance, influence on the answer,
  and distinctiveness.

**Headline results:** the best-performing methods improved on baseline by **up to 41% on
PAWC** and **28% on Subjective Impression**. Overall visibility gains of roughly **22–41%**
were achievable through content optimization alone.

| Strategy | Effect | Notes |
|----------|--------|-------|
| **Statistics Addition** | Among the strongest | Strongest in Law & Government domains and Opinion-type questions |
| **Quotation Addition** | Among the strongest | Strongest in People & Society, Explanation and History domains |
| **Cite Sources** | Positive | Establishes provenance; signals external validation |
| **Authoritative tone** | Positive | Declarative assertions over tentative hedging |
| **Keyword stuffing** | **Not effective** | Classic keyword density does not transfer to generative retrieval |

**The practical takeaway:** generative engines reward *evidence*, not keywords. Adding a
verifiable statistic, a named source, or an attributed quotation does more for AI citation
than any amount of keyword placement.

> **Accuracy note for auditors:** the widely circulated "+115% for position-5 documents"
> figure is frequently attributed to this paper in secondary blog coverage. Do not cite it
> as a study finding unless verified against the paper itself. Use the 41% / 28% figures,
> which are confirmed.

---

## Vendor and industry claims — use with attribution, not as research

These are directionally useful but are not peer-reviewed. Attribute them explicitly or
leave them out of client deliverables.

- Brand mentions correlating more strongly with AI visibility than backlinks (Ahrefs, 2025).
- Citation position skewing toward the earlier portion of a document (Zyppy).
- Multi-modal content selection-rate uplift.

Where a claim cannot be traced to a primary source, mark it **unverified** in the report
rather than repeating it as fact. This is itself an E-E-A-T standard: the audit should model
the sourcing behaviour it recommends.

---

## AEO: how passages actually get extracted

Answer engines run a two-stage pipeline:

1. **Recall** — bi-encoder embedding models retrieve a broad candidate pool by vector similarity.
2. **Re-rank** — cross-encoder models process the query and candidate passage *together*,
   scoring semantic alignment and answer completeness.

Cross-encoders discard passages that delay the answer, rely on surrounding context, or bury
the claim in narrative. That produces concrete structural requirements.

### The canonical answer block

Two distinct structures, often confused:

| Structure | Length | Purpose |
|-----------|--------|---------|
| **Canonical answer block** | **40–58 words** | The extractable direct answer. One per question heading. |
| **Supporting citable passage** | ~130–170 words | The depth around it that AI engines quote from. |

Write the 40–58 word block first, then the depth beneath it. They are complementary, not alternatives.

### Rules for the answer block

- **Entity first.** The subject appears within the first few words, followed by a definitive
  verb: "X is…", "X refers to…". No lead-ins.
- **Self-contained.** No unresolved pronouns ("it", "these", "they") that depend on earlier
  paragraphs. The block must parse standalone.
- **Question-formatted heading.** H2 or H3 phrased as the actual query, with the answer block
  immediately beneath.
- **Front-load it.** Place priority answers early in the document, not after a long preamble.
- **Match the format to the intent.** Comparisons resolve into tables. Processes resolve into
  numbered lists. Definitions resolve into prose.

---

## Fact density target

For generative citation, aim for **at least one verifiable statistic, named entity, or
explicit source attribution per 100 words** of substantive content.

Check during content audits:
- [ ] Every priority page opens its sections with a 40–58 word answer block
- [ ] Question-formatted H2/H3 headings
- [ ] At least one attributed statistic or quotation per major section
- [ ] Sources cited inline and linked
- [ ] Comparison content rendered as tables
- [ ] No unresolved pronouns opening any answer block
- [ ] Declarative phrasing rather than hedged assertions

---

## Freshness and citation decay

Generative citation decays faster than organic rank. Newly published content can enter
citation pools within days of indexation, while stale statistics and dated references lose
citation priority more quickly than they lose ranking position.

**Implication:** pages carrying statistics need a scheduled refresh cycle. A page that ranks
fine on classic search can quietly drop out of AI citation because its numbers went stale.
Track `dateModified` and keep it honest (see schema drift in `entity-schema-graph.md`).

---

## Information Gain

Google's Information Gain patent (US20200349181A1) scores a document on the **additional,
non-redundant** information it contributes relative to sources the user has already seen.

If a page restates the same definitions and the same generic examples as everything else
ranking, its information gain approaches zero, and there is no algorithmic reason to rank
or cite it above the incumbent.

**What creates information gain:**
- Proprietary data, surveys, or benchmarks
- Named case outcomes with real numbers
- First-hand testing and process documentation
- Novel frameworks or original technical analysis

This is the strongest overlap between GEO and E-E-A-T: original material is simultaneously
the thing AI engines cite and the thing quality raters reward. See `eeat-framework.md`.
