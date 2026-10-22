# Dashboard Layout

An overview surface that summarises status and trends, then links to detail. Built for scanning, comparison, and repeated daily use.

## Classification

- Category: layouts / dashboard

When to use:

- An operational or analytical overview that is checked repeatedly.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Top bar with title, search, and account actions; side navigation on expanded screens; filter row; summary cards with label, value, and change indicator; chart area; data table; activity or alert list.

## Layout and responsive rules

- Summary cards come first; detail follows in order of frequency of use.
- Expanded: persistent side navigation and a 12-column grid; charts span 6 to 8 columns.
- Compact: navigation collapses to a top bar with a menu; cards stack; charts become single-column and tables become card lists or gain horizontal scroll with a sticky first column.
- Filters stay visible while results update; the result area shows loading in place.
- Numbers use tabular figures; units and time ranges are always labelled.
- Synthesis over widgets: alongside static charts, offer narrative summaries
  and "what changed" reports that explain the movement, not only the numbers.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The dashboard layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

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
