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
- Prefer sidebar or list navigation over an icon grid: cards with a left sidebar let people scan what each category contains, while icon grids hide where a setting lives.
- Group related choices under short headings; one topic per group.
- Match the edit chrome to the stakes: inline edits for low-stakes changes, modal dialogs where focus or a confirm step is warranted, confirmation dialogs for destructive actions.
- State the save behaviour in words: either changes apply immediately or a save action is required, never a mix without labels.
- Irreversible actions are separated, labelled plainly, and require a confirmation pattern.
- Search within settings is optional; if present, results link to the exact section.
- Treat settings search as a design, not a box: roughly more than 20 fields warrants a search bar; match the words people type (synonyms), not internal labels; each result states where the setting lives and its current value; choosing a result opens the section, scrolls to the field, and briefly highlights it with the cursor in place; log zero-result searches as free research.
- Group irreversible actions (delete, wipe, access-changing) in a danger zone at the bottom of the page or on a dedicated page, visually distinct; each action states what will happen before the person commits; require extra effort (re-entry, a second factor, or type-to-confirm) since access to the page is not proof of identity; keep only truly critical actions there.

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

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Sidebar navigation, settings search, and danger-zone rules are documented.
- [ ] Irreversible actions carry consequence descriptions and extra-effort guards.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
