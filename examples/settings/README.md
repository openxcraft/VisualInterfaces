# Settings Example

A minimal, framework-free settings page: section navigation beside
grouped preferences, scope labels on every control, a stated save
behaviour, settings search, and a danger zone for irreversible
actions, with all seven states. It demonstrates the settings layout
rules in `../../layouts/settings.md` — grouped preferences, scope
labels, save behaviour, settings search, and the danger zone.
Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / settings

When to use:

- Checking the settings layout rules in
  `../../layouts/settings.md` against a working page.
- Testing grouped preferences, scope labels, save behaviour,
  settings search, and the danger-zone guards.

When to avoid:

- Production use; content is structural placeholder text and no
  setting is stored anywhere.
- A single preference on its own; one choice belongs inline where
  it is used, not on a settings page.

## Elements and components

Section navigation with one entry per group; grouped form sections
with one topic per group; switch and select controls; a scope label
beside every control; a save-behaviour statement; a settings search
that links each result to its exact section; a danger zone at the
end holding irreversible actions, each with its consequence stated
and an extra-effort guard; inline demonstrations of every state.

## Layout and responsive rules

- On an expanded screen the section navigation sits on the left
  and the content on the right; on a compact screen the section
  list comes first, then one section per view.
- Related choices sit under short headings, one topic per group.
- The edit chrome matches the stakes: inline edits for
  low-stakes changes, a confirm step for destructive actions.
- The save behaviour is stated in words: changes on this page
  apply at once, and the statement sits beside the first group.
- Every control carries its scope beside it: account everywhere,
  current device, current workspace, or a single project; scopes
  are never mixed inside one group without a label.
- Irreversible actions are separated in a danger zone at the
  bottom of the page, visually distinct; each states what will
  happen before the person commits and requires extra effort.
- Settings search results state where the setting lives and its
  current value; choosing a result opens the section and
  highlights the field.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The settings page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on section links and controls. | No essential information on hover alone. |
| Active | The open section is marked in text and shape, not colour alone, within 100 ms of the choice. | Feedback appears within 100 ms of input. |
| Disabled | A control that cannot change renders dimmed with the reason stated beside it. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | A skeleton replaces a group while its values load, and a pending change shows its saving state before the saved confirmation. | Keep layout dimensions stable so content does not shift. |
| Empty | A search with no match states that nothing matched and offers one correction, keeping the query editable in place. | Offer one clear next action that returns to the full list. |
| Error | A variant in the markup shows a failed save that keeps the entered values, names the problem, and offers a retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the settings layout rules it documents.
- [ ] Scope labels, the save-behaviour statement, settings search, and the danger zone are all present.
- [ ] The failed-save variant keeps the entered values and offers a retry.
- [ ] Run instructions work from a fresh checkout.
