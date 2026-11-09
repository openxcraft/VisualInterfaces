# Standards Outlook

Where accessibility standards are heading, so today's work stays compatible with tomorrow's conformance approach. A horizon note, not a rule set.

## Classification

- Category: trends / 2026 / standards-outlook

When to use:

- Planning new work that will live for several years: design-system foundations, design tokens, component libraries, and conformance reporting.

When to avoid:

- Treating the draft as a conformance target today; it is not final and has no testable criteria yet.

## Elements and components

The current stable guidelines (2.x) as the build target; the draft 3.0 direction as the planning horizon; a conformance report that records both.

## Layout and responsive rules

- Keep building and testing to the current 2.x success criteria at AA: nothing in the draft deprecates 2.x, and 2.x remains the testable standard.
- Plan for the European harmonised standard for ICT accessibility moving its baseline: version 4.1.1, published September 2026, points the web and software clauses at WCAG 2.2 Level AA instead of 2.1. Until it is cited in the Official Journal — expected late November to mid-December 2026, with the date still liable to move — the earlier version stays the legal reference, so treat 2.2 as good practice today rather than an obligation. The move adds six criteria: help that stays in the same place across pages, no repeated entry of the same information, focus never fully hidden behind sticky headers or banners, a single-pointer alternative for any dragging interaction, a 24-pixel minimum target size, and sign-in that does not depend on remembering or retyping a puzzle; one old parsing criterion is removed. Practical stance: build to 2.2 AA now, since it covers the 2.1 requirements too.
- The 3.0 draft is at Working Draft status, with a final recommendation not expected before 2028; treat its details as direction, not requirements.
- The September 2026 draft restructures conformance: one conformance level — meeting every core requirement — with six numbered reporting tiers around it: Avoid physical harm, Foundational access, Conformance, Bronze, Silver, and Gold. Each core requirement carries one of four impact tags — physical harm, risk, barrier, or friction — so a report can show which failures stop people and which only slow them down; the first two tiers are progress markers below conformance, and the last three measure practice above it through supplemental requirements and assertions. Treat this as direction, not requirements: the draft warns its details will change substantially, and it explicitly advises meeting 2.2 success criteria today as the best preparation. Design and test for outcomes — can people complete the task — rather than for checkbox compliance alone.
- Structure work so outcomes are measurable: instrument task completion, error recovery, and assistive-technology use now, so a future scoring scheme has data to score.
- Watch the perceptual-contrast direction: the proposed lightness-contrast
  score (roughly 0–120) factors in text size, weight, and polarity, where
  the old fixed ratios treat light-on-dark the same as dark-on-light and
  thin type the same as bold. Proposed thresholds sit near 90 for body
  text, 75 for large or bold text, 60 as a floor, and 45 for non-text
  components. Practical stance today: keep meeting the current 2.x AA
  baseline, and test new palettes against both systems — a pair that
  passes both is robust, while one that passes the old ratios but fails
  the perceptual score is a future risk.
- Treat entry points to assistive features as regulated surface, not
  decoration: a speech mode or help path that itself requires the
  ability it replaces fails conformance in spirit and, on regulated
  terminals, in letter. Test the assistive path with the people who
  need it, not only the software layer.
- Avoid locking designs to criterion numbers that may be renumbered or replaced; name the underlying user need in the design record instead.
- Treat design tokens as machine-readable infrastructure: the W3C Design Tokens Format Module (v2025.10) formalises token architecture — names, colour mathematics, and alias mapping — into a single platform-agnostic JSON format. Author the token set in that standard form so tooling consumes one deterministic source instead of CSS variables exported once per sprint; automated assembly and restyling then read the same aliases and values the design record documents, and cannot silently drift away from the accessibility constraints that travel with the tokens.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The standards note at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The draft status and the no-deprecation statement are accurate as written.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
