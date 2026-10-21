# Dashboard Example

A minimal, framework-free dashboard using semantic markup and a single stylesheet. Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / dashboard

When to use:

- Checking the dashboard layout rules in `layouts/dashboard.md` against a working page.
- Testing responsive behaviour and state presentation.

When to avoid:

- Production use; data, charts, and values are structural placeholders.

## Elements and components

Top bar, side navigation, filter row, four summary cards, a bar chart built from plain blocks, and a data table.

## Layout and responsive rules

- Expanded screens show side navigation and a multi-column grid.
- Compact screens collapse navigation into the top bar and stack all regions.
- The chart is a set of labelled blocks with values in text, so it reads without colour.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The example page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | A table variant in the markup shows the empty message with a reset action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A banner variant in the markup shows an error message with a retry action. | Keep entered data, place the message next to the problem, and offer a retry. |

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
