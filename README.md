# UI/UX Pattern Atlas

A structured reference for interface types, design elements, page patterns,
layouts, platforms, and devices. Content is organised by classification so a
pattern can be found by purpose first, then adapted to platform and device.

## Classification

- Category: index and entry point for the full reference.

When to use:

- Starting a new screen and choosing an interface type or layout.
- Reviewing an existing screen for missing states or inconsistent elements.
- Comparing patterns before committing to a layout.

When to avoid:

- As a substitute for product-specific research or usability testing.
- As a source of copy for production text; examples here are structural only.

## Elements and components

- `catalog/` — interface types, primitives, patterns, and states.
- `layouts/` — page-level layouts for common product surfaces.
- `trends/` — dated notes on current directions, grouped by year.
- `examples/` — minimal, framework-free examples that can be opened in a browser.
- `resources/` — the only place where external references are listed.

## Layout and responsive rules

- Compact: below 640 px. Single column, primary action first.
- Medium: 640 px to 1023 px. Two columns where content allows.
- Expanded: 1024 px and above. Full grid, persistent navigation where useful.
- Touch targets are at least 44 px in the smallest dimension.
- Reading order in markup matches visual order at every breakpoint.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | Each referenced pattern at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | The index never renders empty; an empty category is a defect to record on the roadmap. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A broken internal link is treated as an error and fixed before publishing. | Keep entered data, place the message next to the problem, and offer a retry. |

## How to use this reference

1. Find the interface type in `catalog/interfaces.md`.
2. Compose the screen from `catalog/primitives.md` and `catalog/patterns.md`.
3. Apply a page layout from `layouts/`.
4. Check every element against `catalog/states.md`.
5. Record gaps and planned additions in `roadmap.md`.

## Coverage summary

| Dimension | Covered |
| --- | --- |
| Platform | Web, mobile, tablet, desktop, kiosk, wearable, television, embedded |
| Device input | Touch, pointer, keyboard, voice, remote, gesture |
| Interface type | See `catalog/interfaces.md` |
| Page pattern | Landing, dashboard, authentication, commerce, settings, mobile navigation |
| State | Default, hover, active, disabled, loading, empty, error |

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
