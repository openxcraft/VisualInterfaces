# Contributing

Short, neutral, and verifiable changes are preferred. One change should cover
one pattern, layout, or correction so it can be reviewed on its own.

## Classification

- Category: process guidance for all other categories.

When to use:

- Adding a pattern, layout, state note, trend note, or example.
- Correcting structure, wording, or a broken internal link.

When to avoid:

- Bundling unrelated edits into a single change.
- Publishing a change that has not passed every quality gate below.

## Elements and components

- A working branch for each change; the main branch is not edited directly.
- A commit message in a neutral form, for example:
  - `docs: expand interface taxonomy`
  - `docs: add dashboard layout patterns`
  - `docs: refresh reference links`
  - `chore: improve consistency and coverage`
- An entry in `CHANGELOG.md` for every substantive change.
- An update to `roadmap.md` when coverage changes.

## Layout and responsive rules

- Keep the file structure shown in `README.md`; do not add new top-level folders without a roadmap entry.
- New dated notes go under `trends/<year>/`.
- Examples stay framework-free so they open directly in a browser.

## States

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A proposed change at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty change is not published. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A change that fails a quality gate is not published; fix it and run the checks again. | Keep entered data, place the message next to the problem, and offer a retry. |

## Quality gates

1. Markdown formatting and lint check.
2. Broken link check for internal links.
3. Secret and personal-data scan.
4. Scan for names of persons and organisations in editorial prose.
5. Scan for depictions of people in visuals; abstract shapes only.
6. Duplication and index consistency check.
7. Example build check when examples change.
8. `CHANGELOG.md` and `roadmap.md` updated for substantive changes.

## Content rules

- Write clear, neutral English with short points, rules, and examples.
- Paraphrase sources; do not copy long protected text.
- Put external references only in files under `resources/`.
- Add no secrets, tokens, keys, contact details, local filenames, system paths, or internal logs.

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
