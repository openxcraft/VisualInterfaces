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
| Platform | Web, mobile | Tablet, desktop | Kiosk, wearable, television, embedded |
| Device input | Touch, pointer, keyboard | Voice, remote | Gesture-only |
| Interface type | Web app, mobile app | Conversational, spatial | Embedded, kiosk |
| Page pattern | Dashboard, mobile navigation | Landing, authentication, commerce, settings | Checkout variants, onboarding |
| State | All seven in catalog | Loading variants | Offline, read-only, permission-denied |

## Improvement actions

1. Add a kiosk layout file with large targets, idle timeout, and session reset
   rules. Done when `layouts/kiosk.md` passes all quality gates and is linked
   from the index.
2. Add an onboarding pattern with step states, skip rules, and progress
   persistence. Done when `catalog/patterns.md` gains the section and
   `catalog/states.md` covers its loading and error cases.
3. Add a wearable pattern note covering glanceable content, two-action screens,
   and voice fallback. Done when `catalog/interfaces.md` and
   `trends/2026/adaptive-interfaces.md` are updated and cross-linked.
4. Add data-table variants for density, sticky headers, and bulk selection.
   Done when `catalog/patterns.md` includes the variants with all seven states.
5. Add an offline state note. Done when `catalog/states.md` defines offline,
   read-only, and permission-denied behaviour and recovery.

## Review notes

- Most duplicated area: state descriptions repeated across layout files.
  Consolidation target: keep the full wording in `catalog/states.md` and short
  rows elsewhere.
- Least covered area: non-screen and small-screen interfaces.

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
