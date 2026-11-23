# Kiosk Example

A minimal, framework-free self-service terminal: one task per screen, a
first-screen choice of language and accessibility options, a visible
session timer with a start-over control, and a session that ends cleanly
with nothing carried over. Open `index.html` in a browser; no build step
is required.

## Classification

- Category: examples / kiosk

When to use:

- Checking the kiosk layout rules in `layouts/kiosk.md` against a
  working page.
- Testing one-task-per-screen flow, reach range, glance budgets, and the
  assistive entry point on a shared public terminal.

When to avoid:

- Production use; content is structural placeholder text.
- Personal devices; the session and persistence rules here assume a
  shared screen.

## Elements and components

A first screen offering language choice and accessibility options before
any task starts; one task per screen with a short step indicator; large
touch targets sized for standing distance; a session timer and a
start-over control visible throughout; an idle countdown that warns
through text and tone before resetting; an end-of-session confirmation
that states what was done and that the session is closed; inline
demonstrations of every state.

## Layout and responsive rules

- Fixed terminal size: the page is designed for one screen size, not for
  breakpoints; type stays legible at standing distance.
- One task per screen: the check-in task advances linearly, one step at a
  time, and the start-over control is always visible.
- Language and accessibility options sit on the first screen, never in a
  settings page; the spoken-guidance entry point is reachable without
  vision, through a labelled control at the top of the screen.
- The session timer counts down in view; an idle countdown warns before
  resetting, then returns to the start screen and clears entered data.
- Nothing essential sits below about 800 mm or above about 1600 mm from
  the floor in the terminal's own mounting; on this page the equivalent
  rule is that no essential control sits at the extreme edge of the
  screen.
- Time-limit alerts arrive through more than one sense: the countdown is
  shown in text and announced, and the person can extend the time.
- Sensitive input is kept out of sight lines: the confirmation code is
  entered on a shielded keypad layout with no echo of the digits.
- The terminal moves between steps in under about two seconds; where the
  network is unavailable, an offline notice replaces the step rather
  than a dead end.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The terminal at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed appearance with an immediate visible change. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | A variant in the markup shows the empty message with a single starting action. | Offer one clear next action that sets up the task. |
| Error | A variant in the markup shows a one-line failure note with retry or start-over. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the kiosk rules it documents.
- [ ] The idle countdown, session reset, and no-retained-data rules are visible.
- [ ] Run instructions work from a fresh checkout.
