# Kiosk Layout

Self-service screens for shared, public terminals: check-in, ordering,
ticketing, and information. The layout assumes a distracted first-time user,
a fixed touch screen at standing distance, and a session that must end
cleanly without leaving personal data behind.

## Classification

- Category: layouts / kiosk

When to use:

- Walk-up terminals where each session is short and the user is unknown.

When to avoid:

- Using this layout for personal devices; account and persistence rules
  assume the screen is shared.

## Elements and components

Large touch targets; one task per screen with a short step indicator;
language and accessibility options reachable from the first screen;
session timer and start-over control visible throughout; clear end-of-session
confirmation that states what was done and that the session is closed.

## Layout and responsive rules

- Fixed screen size: design for the exact terminal, not for breakpoints;
  type is legible at standing distance with large touch targets.
- One task per screen; steps advance linearly and a start-over control is
  always visible.
- An idle countdown warns before resetting, then returns to the start screen
  and clears entered data and any printed or emailed artifacts.
- No session carries personal data to the next session: identifiers,
  receipts, and loyalty entries are cleared on completion or timeout.
- Accessibility controls (text size, contrast, audio guidance) sit on the
  first screen, not in a settings page.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The kiosk layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Idle timeout, session reset, and no-retained-data rules are documented.
- [ ] Large-target and standing-distance guidance is present.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
