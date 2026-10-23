# Functional Motion

Motion used as feedback and orientation: confirming an action, showing where content came from, and keeping place during a transition. Decorative motion is removed.

## Classification

- Category: trends / 2026 / functional-motion

When to use:

- Any interface where actions change content, location, or state.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.

## Elements and components

Short transitions of 100 to 300 ms; shared-element moves between list and detail; progress motion tied to real progress; a reduced-motion variant for every animation.

## Layout and responsive rules

- Motion follows the direction of the change: content enters from where it was triggered.
- No animation blocks input for longer than its own duration.
- Reduced-motion settings replace movement with fades or instant change.
- Looping motion is limited to loading indicators.
- Content revealed by scroll-triggered animation stays available to
  screen-reader and keyboard users; scroll position never gates content
  alone.

## Motion values

Three production durations cover most needs: about 115 ms for quick,
responsive feedback (menus, popovers, panels); about 165 ms for more
expressive change (form-field error shakes, link transitions); about 250 ms
for complex attention-drawing moves (notification banners). Pair each with a
matching easing curve: a responsive decelerating curve for feedback, a
"sticky" curve for state retention, an expressive curve for drawing attention.

- Scale draws attention to incoming items; slide signals a structural move,
  such as a panel entering from its trigger. Keep transform patterns unified
  across the product.
- Never flash more than three times per second.
- Never rely on motion alone: the change must be perceivable without it, and
  the operating system's reduced-motion setting deactivates all non-essential
  animation.
- Ship motion tokens (durations, easings, keyframes) so custom components
  reuse the same values instead of inventing their own.

## Native platform capabilities

Three platform capabilities are converging toward cross-browser parity, so
design systems can drop scripted equivalents:

- Anchor overlays to their trigger (tooltips, menus, popovers) with anchor
  positioning instead of a scripted positioning library; keep a static
  placement behind a support check so the overlay stays visible and aligned
  where anchors are unsupported.
- Default anchored popups to the trigger's width; widen only when the
  content genuinely needs the room, and re-anchor after resize so the
  overlay stays aligned with its trigger.
- Drive scroll-linked motion with scroll-driven animation timelines, not
  scroll listeners; animate transform and opacity only, so the motion stays
  off the main thread; content starts visible and readable, with the
  enhancement added only where supported.
- Run document-to-document transitions with view transitions instead of
  scripted page fades; navigation works identically without them.
- Use native dialog and popover semantics for overlays: a dismiss-on-outside
  action, a subordinate hint popover for tooltips, and keyboard handling that
  ships with the platform.

## Reduced motion: swap, do not delete

Reduced motion is a substitution, not a removal: every effect ships a
deliberate final static state.

- Guard every effect with the operating system's reduced-motion setting and
  ship the resting state per effect: progress bars at full, reveals at full
  opacity, parallax removed.
- Swap movement for calm: keep the fade, drop the travel; keep state
  changes, remove bounce.
- Disable the physics, not only the duration: expressive components carry
  spring and bounce tokens, and shape morphing built into the component,
  that stay alive when only the duration is zeroed; the reduced-motion
  variant must switch the physics intensity and the shape morph off itself
  and settle on the static resting shape.
- Keep essential feedback: spinners run slower (around 1.5 s) rather than
  vanishing; remove parallax backgrounds, scroll reveals, and infinite
  pulsing; retain small contained motion such as icon rotations and button
  presses.
- Offer a visible "pause animations" control alongside the system setting,
  so the choice is discoverable in the product itself.

## States

Canonical state definitions live in `../../catalog/states.md`. Notes specific to functional motion:

| State | Motion note |
| --- | --- |
| Default | Motion at rest; the settled layout is the reference frame. |
| Hover | Pointer-only micro-motion; never the only signal. |
| Active | The transition in flight; completes within about 100–300 ms. |
| Disabled | No motion on unavailable controls; contrast carries the state. |
| Loading | Static progress under reduced motion; skeletons otherwise. |
| Empty | Motion introduces the message once, then settles. |
| Error | Motion never substitutes for a readable message. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Functional-motion purposes and reduced-motion swap rules are documented.
- [ ] Scroll-triggered animation availability rules are present.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
