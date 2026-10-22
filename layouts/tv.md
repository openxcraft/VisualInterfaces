# Television Layout

Lean-back interfaces for screens viewed across a room: media browsing,
playback, and casual information. The layout assumes a simple remote as the
primary control, a viewer at room distance, and short, glanceable text.

## Classification

- Category: layouts / television

When to use:

- Media and entertainment surfaces navigated with a directional remote at
  room distance.

When to avoid:

- Tasks that need typing, precise selection, or dense comparison; hand
  those to a second device or a different surface.

## Elements and components

Shelves (horizontal rails) of posters or cards grouped by category, stacked
vertically under a featured hero row; a persistent section bar across the
top; a playback screen with transport controls that appear on demand; a
voice-search entry point beside a step-through on-screen keyboard.

## Layout and responsive rules

- Focus is the whole navigation scheme: exactly one element is focused at a
  time, drawn larger, brighter, or lifted off the surface; each direction
  press moves focus to the obvious neighbour in that direction. With no
  cursor, focus must be visibly highlighted at all times; grid arrangements
  make the next element in each direction predictable, and the layout lets
  a viewer glance away and return while still knowing their position.
- Arrange content as a grid or a stack of rows so every element has a clear
  neighbour in each direction; there are no focus traps anywhere.
- Set a default focus on every screen and restore it when returning; focus
  memory survives back-and-forth navigation.
- Design for 10-foot legibility: large high-contrast type, short lines of
  about 40 characters, generous spacing, no thin strokes or single-pixel
  details, and keep critical content inside safe margins that survive
  overscan. Type minimums are stricter than on nearer screens: roughly 12sp
  is an absolute minimum and 18sp the default, with about 24pt as the
  practical floor at a 3-metre viewing distance; avoid thin or light
  typefaces, which jag and flicker on television panels; prefer light text
  on dark backgrounds; break copy into short scannable chunks.
- Keep a margin of about 5% from every edge: legacy overscan crops edges,
  and a commonly used overscan-safe margin on 1080p is 27px top and bottom
  and 48px left and right. Gaze concentrates in the centre of the screen,
  so place primary content centrally and keep all critical content and
  controls inside the safe area.
- Actual viewing distance varies between households, so test type and focus
  indicators at several real distances rather than one nominal distance:
  test on a real set from around 3 metres and from several angles in the
  room. Avoid pure white surfaces and over-saturated reds; near-white
  values around #f1f1f1 reduce flicker and halation.
- Different remotes add pointer, touch-surface, or scroll-wheel behaviour
  on top of the directional pad, so plan navigation per input variant
  rather than assuming a plain directional remote.
- Text entry is the weakest point: prefer spoken queries; complex flows such
  as account creation or payment hand off to a second device via a displayed
  code.
- Playback runs on its own screen: controls stay hidden until a button is
  pressed, transport controls are standard and consistent, subtitles and
  audio tracks are reachable, playback position is remembered, and
  interruptions are handled gracefully.
- Keep motion light and transitions cheap: room screens often run on slower
  hardware, so preload visuals and avoid heavy animated transitions.
- Keep one primary action reachable within a few presses; reduce the steps
  needed to reach the most-used content.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The television layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | No pointer exists; the focused state carries the same role. | The focus indicator is always visible; focus alone conveys position. |
| Active | Pressed select feedback: the focused element confirms the press visibly within 100 ms. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast; the item is skipped in focus order so navigation never lands on it. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty shelf shows a neutral prompt and one starting action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A full-screen message states the failure and offers retry; entered data is kept. | Keep entered data, place the message next to the problem, and offer a retry. |

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
