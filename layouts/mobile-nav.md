# Mobile Navigation Layout

Navigation for handheld screens: a bottom tab bar for top-level sections, a top app bar for context and actions, and a drawer only where a tab bar cannot fit the structure.

## Classification

- Category: layouts / mobile-nav

When to use:

- Handheld applications with three to five top-level sections.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Bottom tab bar with three to five destinations, each with a short label and an abstract mark; top app bar with title, back action where relevant, and at most two actions; optional drawer for secondary sections; badge for counts that need attention.

## Layout and responsive rules

- Tab bar stays fixed; content scrolls beneath it with bottom padding equal to bar height plus safe area.
- Labels are always visible; marks alone are not sufficient.
- The thumb zone holds primary navigation and primary actions; destructive actions stay out of it.
- Back behaviour is consistent: back returns to the previous view, the tab returns to the section root.
- On tablets, the tab bar may become a side rail; destinations and order do not change.
- When top-level sections exceed five, keep the five most-used destinations in the bar and move the rest behind a single More destination that lists every remaining section with its label; never scroll the bottom bar itself, and never drop a destination silently. The More list keeps the current section marked in text as well as in shape, and returning from a More destination keeps the bar state unchanged.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The mobile-nav layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Compact navigation patterns and reach rules are complete.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
