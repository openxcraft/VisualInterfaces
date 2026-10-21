# Roadmap

Planned work is recorded as concrete, actionable items. Completed items move
to `CHANGELOG.md`; this file keeps only open work and the coverage review.

## Classification

- Category: planning record for all categories.

When to use:

- After each deep editorial review, to record the next improvements.
- Before starting a change, to check whether it is already planned.

When to avoid:

- As a log of completed work; that belongs in `CHANGELOG.md`.

## Elements and components

- Coverage matrix, reviewed on a fixed cycle.
- Improvement actions, each with an owner step and a done condition.
- A list of the least covered areas, in priority order.

## Layout and responsive rules

- This file stays a single page; long detail belongs in the file it improves.
- Matrix rows are dimensions; columns are coverage levels.

## States

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A roadmap item at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty roadmap after a review is a defect; every deep review adds at least three actions. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | An item that cannot be done as written is rewritten with a smaller, testable step. | Keep entered data, place the message next to the problem, and offer a retry. |

## Coverage matrix

Rating: full = defined with states and an example or rule set; partial =
defined without an example; gap = named but not yet defined.

| Dimension | Full | Partial | Gap |
| --- | --- | --- | --- |
| Platform | Web, mobile, kiosk | Tablet, desktop, wearable, television, embedded | — |
| Device input | Touch, pointer, keyboard | Voice, remote | Gesture-only |
| Interface type | Web app, mobile app, kiosk | Conversational, spatial | Embedded |
| Page pattern | Dashboard, mobile navigation, data table | Landing, authentication, commerce, settings, onboarding | Checkout variants |
| State | All seven in catalog; offline, read-only, permission-denied | Loading variants | — |

## Improvement actions

1. Add a television layout file with focus-based navigation, 10-foot
   legibility rules, and overscan margins. Done when `layouts/tv.md` passes
   all quality gates.
2. Add an embedded display layout note covering fixed-size canvases, offline
   operation, and high-contrast rules for bright light. Done when a new
   section or `layouts/embedded.md` passes all quality gates and is referenced
   from `catalog/interfaces.md`.
3. Consolidate the duplicated seven-state tables: replace the full table in
   each layout and trend file with a short pointer to `catalog/states.md`
   plus file-specific state notes. Done when `check_quality.py` no longer
   reports the duplicate-paragraph warning.

## Review notes

- Most duplicated area: state descriptions repeated across layout and trend
  files. Consolidation target: keep the full wording in `catalog/states.md`
  and short rows plus a pointer elsewhere (now a numbered action).
- Least covered area: television and embedded display interfaces; gesture-only
  input remains a gap.

## Pre-publish checklist

- [ ] Title and short description are present and accurate.
- [ ] Classification and when-to-use guidance are present.
- [ ] Elements, layout, and responsive rules are complete.
- [ ] All seven states are defined: default, hover, active, disabled, loading, empty, error.
- [ ] Text is neutral, short, and free of names of persons and organisations in editorial prose.
- [ ] No references appear outside the resources files.
- [ ] No secrets, contact details, local filenames, or system paths are present.
- [ ] Visuals, if any, are abstract shapes only.
- [ ] Internal links resolve and headings follow a consistent order.
