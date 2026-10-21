# Adaptive Interfaces

Interfaces that adjust density, content order, and defaults to context such as device, time, and stated preferences, within fixed guardrails so the layout never becomes unpredictable.

## Classification

- Category: trends / 2026 / adaptive-interfaces

When to use:

- Products used across devices and contexts where one fixed arrangement serves none of them well.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.

## Elements and components

Preference controls for density, theme, and text size; a rules layer that reorders secondary content; a stable core layout that never moves; a visible way to reset to defaults.

## Layout and responsive rules

- Primary navigation, primary action, and account controls never move.
- Adaptation changes order and emphasis of secondary content only.
- Every adaptation can be inspected and undone from settings.
- Compact and expanded variants follow the same adaptation rules.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The pattern in use at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show a neutral starting prompt or placeholder with one example action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | State what could not be completed and offer the structured fallback or a retry. | Keep entered data, place the message next to the problem, and offer a retry. |

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
