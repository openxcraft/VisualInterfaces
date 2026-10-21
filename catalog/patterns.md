# Patterns

Composite patterns assembled from primitives. Each pattern solves a recurring task and inherits the state rules of its parts.

## Classification

- Category: patterns

When to use:

- Composing a screen for a recurring task such as finding, filtering, or editing information.
- Checking a flow for missing steps, exits, or recovery paths.

When to avoid:

- Inventing a one-off arrangement for a task a pattern already covers.

## Elements and components

| Pattern | Purpose | Core elements | Rules |
| --- | --- | --- | --- |
| Primary navigation | Move between top-level sections | Nav list, current indicator, badge | Current section is marked in text or shape, not colour alone |
| Search | Find content by query | Search input, suggestions, results list, clear action | Show recent and suggested queries only where appropriate; results state the query |
| Filtering and sorting | Narrow a list | Filter controls, active filter tags, sort menu, result count | Result count updates with filters; one action clears all filters |
| Data table | Compare structured rows | Header row, sort controls, pagination or load-more, row actions | Sticky header on long tables; density is a user choice where feasible |
| Form flow | Collect structured input | Grouped fields, inline validation, summary of errors, submit | Validate on submit and on correction; errors are listed and linked to fields |
| Wizard | Complete a multi-step task | Step indicator, back and next, save and resume | Steps can be revisited; progress is preserved on interruption |
| Detail view | Inspect one item | Title, key facts, actions, related items | Primary action stays reachable while scrolling on compact screens |
| Notification list | Review updates | Grouped items, read state, mark-all action | Unread state uses shape or text in addition to colour |
| Confirmation | Prevent a costly mistake | Plain statement of effect, confirm and cancel actions | Destructive actions name the item and the effect; no pre-selected confirm |
| Paywall and upgrade prompt | Explain a limit and an option | Limit statement, option summary, dismiss action | Dismiss is always present and equally easy to find |
| Consent choice | Record a preference | Plain description, accept and decline, link to detail | Decline is as prominent as accept; choice is changeable later |
| Media viewer | Inspect visual content | Stage, previous and next, caption, close | Keyboard and swipe both work; captions are text, not embedded in the visual |

## Layout and responsive rules

- One pattern owns the primary action of a screen; supporting patterns stay visually quieter.
- On compact screens, patterns stack in task order: search, filters, results, actions.
- On expanded screens, filters may sit beside results; the result count stays with the results.
- Keep the path back: every pattern that opens a detail or a step offers a clear return.
- Do not nest dialogs; use a new view when a second layer of decisions appears.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A pattern at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | State why the area is empty and offer the action that fills it, or a reset when filters cause it. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep the pattern's structure, show the failure in place, and offer retry without losing input. | Keep entered data, place the message next to the problem, and offer a retry. |

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
