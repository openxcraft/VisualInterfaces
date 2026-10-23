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

## Data-table rules

- Grouped loading: render column headers immediately and skeletonise only
  the body rows; headers never pulse. Load the page shell first, then
  content zones in priority order, and stagger row appearance by about
  50–100 ms to reduce layout shift.
- Group all row actions under a single overflow menu at the row end,
  instead of inline icon clusters. Show contextual icons only when they
  are relevant to that row. Keep destructive actions guarded and separate
  from frequent ones.

## Responsive data-table strategies

Tables are the hardest component to shrink: their power is horizontal
comparison, and compact screens are vertical. Four strategies cover the
space; choose by asking which columns a person truly cannot decide
without:

- Horizontal scroll with a frozen leading column: keeps the table
  honest and comparison intact. Freeze the identifier column with
  sticky positioning, keep the header row sticky inside the scroll
  region, and add a scroll indicator so people know more columns exist
  beyond the viewport. Keep the corner cell where sticky header and
  frozen column meet above both.
- Column dropping by priority: rank every column essential, important,
  or optional, and hide the optional ones below chosen breakpoints.
  The pragmatic default when some attributes clearly matter more;
  dropped data stays reachable through row expansion or a detail
  view.
- Priority-plus disclosure: show the top few columns and tuck the rest
  behind a per-row expansion control. The most adaptive option for
  mixed importance, trading a tap for full detail.
- Card transformation: each row becomes a stacked card with labelled
  values. Reads well for small sets that are read one record at a
  time; it falls apart past a few dozen records and destroys
  cross-row comparison, so never use it for comparison tasks.

Rules for all four:

- Pick one strategy per table, never a mix of strategies row by row.
- Keep sort, filter, and selection state stable across strategy
  changes at breakpoints.
- Keep keyboard focus order matching visual order; a frozen column
  must not reorder the tab flow.
- Label stacked card values with the column name, so each card reads
  correctly without the header row.
- Truncate cell text with the three-part combination (no wrapping,
  hidden overflow, ellipsis) and always expose the full value on
  demand.

## Visual restraint

- On data-and-trust surfaces, extreme restraint reads as seriousness: one typeface does most of the work, borders thin down to low-opacity hairlines, and structure comes from white space and typographic weight rather than boxes and shadows.
- Keep the palette to two or three tones; reserve heavier treatments for the brand moments that must carry personality, since a restrained surface leaves little room for storytelling.
- Treat restraint as a fit decision, not a default: it suits operational overviews and developer-facing surfaces, and fits poorly where warmth or character must come through.

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

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Summary-card order, grid rules, and the compact fallback are documented.
- [ ] Data-table rules cover grouped loading and row-action grouping.
- [ ] Responsive data-table strategies name all four strategies and the shared rules.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
