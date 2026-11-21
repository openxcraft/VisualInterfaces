# Watch Example

A minimal, framework-free watch surface: one datum and one action per
screen, a complications-first face layer, a persistent live-activity
anchor, and a separate ambient always-on variant. Open `index.html` in
a browser; no build step is required.

## Classification

- Category: examples / watch

When to use:

- Checking the watch layout rules in `layouts/watch.md` against a
  working page.
- Testing glance-first placement, the two-tap rule, and the ambient
  always-on variant on a small round display.

When to avoid:

- Production use; content is structural placeholder text.

## Elements and components

A round watch face showing one datum (a timer) with a progress ring;
a single primary action; an overflow button for secondary actions; a
complication tile carrying the most-checked datum with a tap target
into the app; a persistent live-activity anchor at the bottom of the
face layer; a separate ambient always-on panel with no animation, a
reduced palette, and low brightness; inline demonstrations of every
state.

## Layout and responsive rules

- Glance-first: the essential datum is visible with no scrolling; the
  interaction lasts a few seconds.
- One screen, one action: the timer value sits at the centre with one
  primary action beneath it; anything longer moves to the phone
  companion app.
- Two-tap rule: pause, resume, and stop are each one tap; a task
  needing more than two taps is not on the watch.
- Round-display margins use percentages of the screen size so nothing
  clips at the curved edge.
- Touch targets are at least 38–48dp with at least 8pt between them;
  the crown or bezel is the scroll mechanism, not fine swipes.
- Secondary actions sit behind an explicit overflow button; no hidden
  gesture is the only route to an action.
- Haptic confirmation is stated in text beside the action, so the
  feedback does not depend on looking at the screen.
- The ambient always-on variant is a separate layout: no animation,
  reduced colour palette, low brightness, and the time and current
  value still visible. It never shows sensitive detail.
- The live-activity anchor stays in one place — at the bottom of the
  face layer — so the person can return to the ongoing activity
  without hunting; it clears when the activity ends.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The watch surface at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | No hover on watches; designs that work without it. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed appearance with an immediate haptic pulse. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, still readable on a small bright screen. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | A compact progress ring around the datum; never a full-screen spinner. | Keep layout dimensions stable so content does not shift. |
| Empty | A variant in the markup shows the empty message with a single starting action. | Offer one clear next action that sets up the datum being watched. |
| Error | A variant in the markup shows a one-line failure note with retry or exit. | Keep the note short, place it next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the watch rules it documents.
- [ ] The ambient always-on variant is a separate layout, not the same layout dimmed.
- [ ] Run instructions work from a fresh checkout.
