# Television Example

A minimal, framework-free television surface: a persistent section bar, a
featured hero row, shelves of cards navigated with a remote, visible focus
at all times, focus memory across Back navigation, and 10-foot legibility.
Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / television

When to use:

- Checking the television layout rules in `layouts/tv.md` against a
  working page.
- Testing visible focus, focus memory, Back-button behaviour, and
  10-foot legibility on a room screen.

When to avoid:

- Production use; content is structural placeholder text.
- Tasks that need typing, precise selection, or dense comparison; those
  belong on a second device.

## Elements and components

A persistent section bar across the top; a featured hero row with one
primary action; shelves (horizontal rails) of cards grouped by category,
stacked vertically; a playback screen where transport controls appear on
demand; a voice-search entry point beside an on-screen keyboard route;
a statement on every screen of where Back goes next; inline
demonstrations of every state.

## Layout and responsive rules

- Focus is the whole navigation scheme: exactly one element is focused at
  a time, drawn larger, brighter, and lifted off the surface; each
  direction press moves focus to the obvious neighbour.
- Rows and columns form a grid: left and right move within a row, up and
  down move to the neighbouring row keeping the column, clamped to that
  row's length. No focus traps anywhere.
- A default focus is set on every screen and restored when returning;
  focus memory survives back-and-forth navigation, so leaving a shelf
  and coming back lands on the same card.
- Back moves backward: pressing Back takes the viewer one step back
  through the experience, never a second select; every screen states
  where Back goes next.
- Ten-foot legibility: large high-contrast type, short lines, generous
  spacing, no thin strokes; light text on a dark background; critical
  content stays inside a 5% safe margin from every edge.
- Text entry is the weakest point: voice search is offered first, and
  account or payment steps hand off to a second device through a
  displayed code.
- Playback runs on its own screen: controls stay hidden until a button is
  pressed, subtitles and audio tracks are reachable, and the playback
  position is remembered.
- One primary action stays reachable within a few presses from the home
  screen.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The television surface at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | No pointer exists; the focused state carries the same role. | The focus indicator is always visible; focus alone conveys position. |
| Active | Pressed select feedback: the focused element confirms the press visibly within 100 ms. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast; the item is skipped in focus order so navigation never lands on it. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty shelf shows a neutral prompt and one starting action. | Offer one clear next action that sets up the shelf. |
| Error | A variant in the markup shows a full-screen failure note with retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the television rules it documents.
- [ ] Focus stays visible at all times and focus memory survives Back navigation.
- [ ] Run instructions work from a fresh checkout.
