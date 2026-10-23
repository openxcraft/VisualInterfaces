# Automotive Layout

Interfaces used while driving: cluster displays, centre-stack screens, and head-up projections. Every rule here serves one goal — the driver's eyes return to the road quickly.

## Classification

- Category: layouts / automotive

When to use:

- In-vehicle interfaces where the person using them is also driving.

When to avoid:

- Passenger-only or parked-only screens, which follow the standard
  platform rules instead of glance budgets.
- Treating this as a styling exercise; the budgets below are the layout.

## Elements and components

Stable information zones (speed, warnings, navigation each in a fixed place); glance-sized content cards; physical controls for essential functions; day and night themes; interruption and resumption of non-driving tasks.

## Layout and responsive rules

- Two-second glance budget: every screen must be readable and its state
  understandable within a single glance of about two seconds; a full task
  totals no more than about twelve seconds of eyes-off-road time.
- Design for glances, not taps: one glance answers one question
  completely — assembling meaning across several glances is unsafe, so
  never split one answer across two screens.
- Positions are stable: the same information always appears in the same
  place, and warnings always appear in the same zone; the eye learns
  positions, and learned positions are the cheapest glance reduction.
- Input responses land within 0.25 seconds; when content needs longer to
  load, show that the device is responding rather than a dead screen.
- Touch targets are at least 76 x 76 dp with at least 23 dp spacing;
  primary text is at least 32 dp, secondary at least 24 dp; keep text
  brief, on the order of 120 characters per message.
- Essential functions stay on physical controls; core functions are never
  touchscreen-only. Well-structured touch flows may serve the rest when
  menus are shallow, responses fast, and common tasks short.
- Day mode uses dark text on light surfaces and night mode uses light
  text on dark surfaces; contrast stays at least 4.5:1 in both.
- Driving-relevant content wins: non-driving tasks can be interrupted and
  resumed, and other audio ducks while navigation prompts are spoken.
- Suppress distraction while moving: restrict games and browsing, mark
  unavailable features visually rather than hiding them, never use video
  or auto-scrolling text, and pause notifications mid-manoeuvre.
- Gestures are one-handed; no driving-time gesture may require two hands,
  including map movement.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The automotive layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift; never leave a dead screen. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Glance budgets, input-response timing, and target sizes are documented with numbers.
- [ ] Stable positions, physical controls, and distraction-suppression rules are present.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
