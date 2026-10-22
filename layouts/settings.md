# Settings Layout

A structured area for preferences and account-level choices, grouped by topic, with predictable save behaviour.

## Classification

- Category: layouts / settings

When to use:

- Preferences, profile details, notifications, privacy, and billing-adjacent choices.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Section navigation; grouped form sections; switch and select controls; save action or immediate-apply note; a clearly separated irreversible-actions area at the end.

## Layout and responsive rules

- Expanded: section navigation on the left, content on the right; compact: section list first, then one section per view.
- Group related choices under short headings; one topic per group.
- State the save behaviour in words: either changes apply immediately or a save action is required, never a mix without labels.
- Irreversible actions are separated, labelled plainly, and require a confirmation pattern.
- Search within settings is optional; if present, results link to the exact section.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The settings layout at rest, with full contrast and a clear label. | Ready for input or selection. |
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
