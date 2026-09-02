# E-E-A-T Evaluation Framework
## Updated per Google Quality Rater Guidelines — September 11, 2025
## Plus December 2025 Core Update Implications

## Overview

E-E-A-T = **E**xperience, **E**xpertise, **A**uthoritativeness, **T**rustworthiness

Trustworthiness is the most important factor. It is assessed based on the
other three signals plus direct trust indicators.

## CRITICAL: December 2025 Core Update

> **E-E-A-T now applies to ALL competitive queries, not just YMYL.**

The December 2025 core update was described as a "watershed moment" that:
- Extended E-E-A-T evaluation to virtually all competitive queries
- Made author attribution standards tighter across all categories
- Penalized anonymous or generic authorship even for non-YMYL content
- Significantly improved AI content quality detection

**Impact by industry:**
| Industry | Traffic Drops |
|----------|--------------|
| Affiliate sites | 71% average decline |
| Health/YMYL | 67% average decline |
| E-commerce | 52% average decline |

> **Sourcing caveat:** these are third-party industry aggregates, not figures published by
> Google. Attribute them as such in client deliverables, or omit them. An audit that models
> sloppy sourcing while recommending rigorous sourcing undermines its own advice.

**Key takeaway:** Even entertainment and lifestyle content now requires demonstrated expertise. Generic content no longer ranks.

## YMYL (Your Money or Your Life)

Topics requiring **highest** E-E-A-T standards (but E-E-A-T now matters everywhere):
- Health and safety
- Financial advice and transactions
- Legal information
- News and current events
- **Elections and civic trust** (added Sept 2025)
- **Democratic processes** (added Sept 2025)
- Groups of people (potential for harm)

---

## Experience (Weight: 20%)

First-hand knowledge and personal involvement with the topic.

### Signals to Check
- [ ] Author has demonstrable first-hand experience with the topic
- [ ] Content includes original photos, screenshots, or data
- [ ] Case studies or real-world examples with specific details
- [ ] Personal process documentation or methodology descriptions
- [ ] Before/after results or outcome data
- [ ] Specific anecdotes that couldn't be fabricated

### Scoring
- **Strong**: Multiple first-hand experience signals, original content
- **Moderate**: Some personal experience evident
- **Weak**: Generic information, no personal touch
- **None**: Clearly AI-generated or scraped content

---

## Expertise (Weight: 25%)

Formal qualifications, training, and demonstrated knowledge.

### Signals to Check
- [ ] Author credentials relevant to topic (bio, certifications)
- [ ] Technical accuracy and depth appropriate for audience
- [ ] Claims supported by evidence or sources
- [ ] Specialized vocabulary used correctly
- [ ] Up-to-date with current developments in the field
- [ ] Byline with author name and credentials visible

### Scoring
- **Strong**: Verified credentials, deep technical accuracy
- **Moderate**: Demonstrable knowledge, some credentials
- **Weak**: Surface-level information, no credentials
- **None**: Factual errors, misinformation

---

## Authoritativeness (Weight: 25%)

Recognition by others as a go-to source.

### Signals to Check
- [ ] Site recognized as authority in its niche
- [ ] Author recognized as expert (external citations, speaking, publications)
- [ ] Content cited by other authoritative sources
- [ ] Industry awards, certifications, or accreditations
- [ ] Consistent publication history in the topic area
- [ ] Featured in reputable media outlets
- [ ] Professional affiliations

### Scoring
- **Strong**: Widely recognized authority, cited by others
- **Moderate**: Growing recognition, some external validation
- **Weak**: No external recognition
- **None**: Negative reputation, known for misinformation

---

## Trustworthiness (Weight: 30%)

The most important factor — overall reliability and transparency.

### Signals to Check
- [ ] Clear contact information (physical address, phone, email)
- [ ] Privacy policy and terms of service
- [ ] HTTPS with valid certificate
- [ ] Transparent about who creates content and why
- [ ] Customer reviews and testimonials
- [ ] Corrections and update history visible
- [ ] No deceptive practices (hidden ads, clickbait)
- [ ] Secure payment processing (for e-commerce)
- [ ] Return/refund policy visible

### Scoring
- **Strong**: Full transparency, verified business, positive reputation
- **Moderate**: Good trust signals, minor gaps
- **Weak**: Missing key trust signals
- **None**: Deceptive practices, scam indicators

---

## September 2025 QRG Updates

### AI Content Assessment
Raters now formally evaluate whether content appears AI-generated:
- AI content is **acceptable** if it demonstrates genuine E-E-A-T
- Low-quality AI content (generic, no unique value) is penalized
- The presence of AI-generated content is not inherently penalizing
- What matters: does the content provide unique value regardless of creation method?

### Markers of Low-Quality AI Content
- Generic phrasing without specificity
- Lack of original insight or unique perspective
- No first-hand experience signals
- Factual inaccuracies
- Repetitive structure across multiple pages
- No author attribution or expertise signals

### New Spam Categories
- **Expired domain abuse**: Buying expired domains for their backlinks
- **Site reputation abuse**: Using reputable site to host low-quality content
- **Scaled content abuse**: Mass-producing content without value

### AI Overview Evaluation
Raters assess quality of AI-generated summaries in search results.

### RSL 1.0 (Really Simple Licensing)
New machine-readable content licensing standard (December 2025) for AI training:
- Backed by: Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons
- Allows publishers to specify AI licensing terms
- Augments robots.txt for AI-specific permissions

---

## Experience Signals Are Critical Differentiators

The December 2025 update elevated the "Experience" dimension as a key differentiator:
- First-person narrative ("I tested this...", "In my experience...")
- Original photos and screenshots (not stock images)
- Specific examples with verifiable details
- Process documentation showing actual work done

**Why:** AI can generate expertise-sounding content but cannot fabricate genuine experience.

---

## Machine-Readable E-E-A-T

**The most common E-E-A-T failure is not missing credentials. It is credentials that exist
only in prose.** A bio paragraph is read by humans; it is not parsed into structured claims
by machines. Search engines and LLMs resolving "who stands behind this page" need explicit
markup.

Every E-E-A-T signal you can prove should exist in **both** places: visible on the page, and
as a structured property on a `Person` node.

| E-E-A-T dimension | Visible on page | Structured property |
|-------------------|-----------------|---------------------|
| Experience | First-hand account, original photos, process documentation | `Person` linked as `author` on the `Article` |
| Expertise | Credentials in byline and bio | `hasCredential`, `knowsAbout`, `alumniOf` |
| Authoritativeness | Awards, press, external profiles | `award`, `sameAs` (Wikidata, publications, LinkedIn) |
| Trustworthiness | Contact details, dates, corrections | `Organization` with `contactPoint`; honest `dateModified` |

**Implementation:** see `entity-schema-graph.md` for the connected `@graph` pattern and the
full `Person` node specification.

### Audit rules
- [ ] Every article has a named author resolving to a `Person` node by `@id` (never a bare name string)
- [ ] Author credentials, awards and external profiles appear in markup **and** on the page
- [ ] `sameAs` includes a Wikidata QID where one legitimately exists
- [ ] Author entities reflect **current** staff — markup naming a departed author is a Critical drift error
- [ ] Claims in markup never exceed what the page actually shows

---

## Information Gain

Google's Information Gain patent (US20200349181A1) scores a document on the **additional,
non-redundant** information it adds relative to what the user has already seen for that query.

This is the mechanism that decides between two pages with equal credentials. A page that
restates the same definitions and generic examples as the incumbent top 10 has an information
gain approaching zero, and there is no algorithmic reason to promote it.

**It is also the strongest overlap between E-E-A-T and AI citation:** original material is
simultaneously what quality raters reward and what generative engines quote.

### What creates information gain
- Proprietary data, surveys, benchmarks
- Named case outcomes with real numbers
- First-hand testing and process documentation
- Novel frameworks or original technical analysis
- Expert commentary that takes a position

### What creates none
- Restated definitions available everywhere
- Generic examples and hypotheticals
- Summarised competitor content
- Advice with no specifics attached

**Audit question for every page:** *what does this contain that the current top 10 do not?*
If there is no answer, the page has an originality problem, not a keyword problem. See
`aeo-geo-benchmarks.md`.

---

## Overall Scoring Guide

| Score | Description |
|-------|-------------|
| 90-100 | Exceptional E-E-A-T — authority site, recognized expert, full transparency |
| 70-89 | Strong E-E-A-T — demonstrated expertise, good trust signals |
| 50-69 | Moderate E-E-A-T — some signals, room for improvement |
| 30-49 | Weak E-E-A-T — minimal signals, significant gaps |
| 0-29 | Very low E-E-A-T — no visible signals, potential trust issues |

---

## Improvement Recommendations by Score

### 0-29 (Critical)
1. Add contact information and about page
2. Establish author identity with credentials
3. Implement HTTPS
4. Remove deceptive elements

### 30-49 (Major)
1. Add author bios with credentials
2. Include first-hand experience content
3. Get external citations/mentions
4. Add customer testimonials

### 50-69 (Moderate)
1. Deepen content with original research
2. Build topical authority through content clusters
3. Pursue industry recognition
4. Document processes and methodologies

### 70-89 (Minor)
1. Maintain freshness with regular updates
2. Expand author presence across platforms
3. Pursue speaking/publication opportunities
4. Add video/multimedia demonstrating expertise

### 90-100 (Maintenance)
1. Continue publishing high-quality content
2. Monitor and respond to reputation issues
3. Keep credentials and certifications current
