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
- Small-surface variants, such as wearables, reduce to one glance per screen with at most two actions; see the wearable rules in `catalog/interfaces.md`.

## Style variants

A kit may ship its whole block set in two complete visual styles: a compact,
precise monochrome style and a roomy, warm, tactile one. Both styles share
the same layout, data, states, keyboard handling, and motion; only density,
type, surface treatment, and radius change.

- Every block ships in every style. A switch that leaves some blocks behind
  breaks the promise.
- One theme panel switches every preview at once; accent, base, font, and
  radius compose on top of either style.
- Blocks are installed per style, keeping a project to the style it uses.
- Choose the compact style where operators and consoles need precision;
  choose the warm style for consumer products that invite touch.

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

## Machine experience

Pages increasingly serve a second audience: automated software that reads,
interprets, and acts on a page on someone's behalf. This direction, sometimes
called machine experience, asks whether a page is as legible to a parser as
it is to a person.

- Use real semantic markup: headings in genuine order, real buttons, real
  lists, real form labels. An element built from generic containers forces
  every reader to guess.
- Write the document order to match the visual order; whatever comes first
  in the source is reported first.
- Publish structured data for the key facts a page asserts: products, prices,
  dates, locations, contact details. It states what the page offers without
  requiring prose to be parsed.
- Server-render the content that matters. Copy that exists only after
  client-side execution may never reach a reader that does not run it.
- Keep key facts in extractable form: tables, lists, and concise definitions
  rather than facts trapped inside images or animated sequences.
- Make the main content distinguishable from surrounding furniture —
  headers, navigation, footers, promotional panels — so a summary captures
  the page's substance.
- Declare the machine-access policy plainly: which parts may be read and
  which may not. It is a publishing decision, not an afterthought.

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
