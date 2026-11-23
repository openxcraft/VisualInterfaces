# Automotive Example

A minimal, framework-free centre-stack surface for a vehicle in
motion: fixed information zones, glance-sized cards, and a
driver-state variant that changes emphasis only, never position.
Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / automotive

When to use:

- Checking the automotive layout rules in `layouts/automotive.md`
  against a working page.
- Testing glance budgets, fixed zones, and emphasis-only adaptation
  under load on a centre-stack screen.

When to avoid:

- Production use; content is structural placeholder text.
- Passenger-only or parked-only screens, which follow the standard
  platform rules instead of glance budgets.

## Elements and components

A fixed cluster zone showing speed; a centre-stack card showing the
next manoeuvre with distance and a single primary action; a head-up
strip carrying speed, the next manoeuvre, and a critical warning only;
a media card that can be interrupted and resumed; a driver-state
variant that strengthens the highlight on the likely next control
without moving anything; day and night theme variants; inline
demonstrations of every state.

## Layout and responsive rules

- Two-second glance budget: every screen is readable and its state
  understandable within a single glance of about two seconds; a full
  task totals no more than about twelve seconds of eyes-off-road time.
- One glance answers one question completely: the next manoeuvre,
  its distance, and its direction sit together on one card, never
  split across two screens.
- Positions are stable: speed always sits in the cluster zone, the
  next manoeuvre always sits in the centre card, and warnings always
  appear in the same zone; the eye learns positions, and learned
  positions are the cheapest glance reduction.
- Input responses land within 0.25 seconds; when content needs
  longer to load, the screen shows that the vehicle is responding
  rather than a dead screen.
- Touch targets are at least 76 by 76 dp with at least 23 dp
  spacing; primary text is at least 32 dp, secondary at least
  24 dp; messages stay brief, on the order of 120 characters.
- Essential functions stay on physical controls; the five
  safety-critical functions — indicators, hazard lights, windscreen
  wipers, horn, and emergency call — are never touchscreen-only.
- The head-up strip shows only the highest-priority content — speed,
  the next manoeuvre, and critical warnings — and nothing else.
- Day mode uses dark text on light surfaces and night mode uses
  light text on dark surfaces; contrast stays at least 4.5:1 in both.
- Non-driving tasks can be interrupted and resumed, and other audio
  ducks while navigation prompts are spoken.
- Adapt to the driver's state without moving anything while driving:
  under higher load the likely next control gains a stronger
  highlight, a clearer label, or a small animation, while everything
  else stays where it was; short-term changes alter emphasis only,
  never position.
- Gestures are one-handed; no driving-time gesture requires two hands.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The centre-stack surface at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift; never leave a dead screen. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the automotive rules it documents.
- [ ] The driver-state variant changes emphasis only and moves nothing.
- [ ] The head-up strip carries speed, the next manoeuvre, and warnings only.
- [ ] Run instructions work from a fresh checkout.
