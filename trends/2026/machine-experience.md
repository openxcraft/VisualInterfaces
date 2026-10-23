# Machine Experience Design

Pages structured so automated agents can read, compare, and complete tasks accurately. The machine reader is treated as a real audience alongside the human one, without weakening the human experience.

## Classification

- Category: trends / 2026 / machine-experience

When to use:

- Pages where automated agents look up facts or complete tasks for a person: prices, availability, schedules, bookings, purchases, comparisons.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.
- Treating machine readability as a replacement for human usability; the human page comes first.

## Elements and components

Semantic sections whose source order matches the visual order; headings that describe the content below them; key facts — price, availability, primary action, contact — as real text, never image-only; labels tied to every input, an explicit submit action, and error messages placed next to the field they concern.

Components that ship in shared libraries carry machine-readable intent metadata alongside their styling tokens: each component is marked as a required safety control or as removable convenience, and required safety controls — confirmations, dependent-selection steps, consent and disclosure checks — may never be stripped out by tooling that assembles or restyles screens automatically. Accessibility constraints travel with the component in the same metadata, so restyling cannot quietly drop keyboard support or visible focus.

## Layout and responsive rules

- The source sequence reads the same as the visual sequence at every breakpoint; reordering by sight alone breaks machine reading.
- Critical information never lives only in scripts, canvas, gesture-only controls, or hover-only reveals.
- Headings, lists, tables, and forms use native structures so every part keeps its role.
- The first useful content is available without completing any interaction.
- Keyboard focus order matches the reading order everywhere.
- Compact variants keep the same source order; nothing important drops out of the sequence at small sizes.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The page at rest; machine-readable structure invisible to the eye, human layout unchanged. | Ready for reading or input; key facts present as text. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable as text. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator with labelled roles, not empty containers. | Keep layout dimensions stable so content does not shift; progress remains legible. |
| Empty | Show a neutral starting prompt or placeholder with one example action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | State in plain words what could not be completed, next to the field it concerns, with the structured fallback or a retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Machine-legibility rules are current and neutral.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
