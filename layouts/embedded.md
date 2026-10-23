# Embedded Display Layout

Panels fixed into appliances, machinery, and wall-mounted controls: status
readouts, simple controls, and setup screens on a canvas that never
changes size. The layout assumes a known panel, often bright or dirty
surroundings, and operation with or without a network connection.

## Classification

- Category: layouts / embedded-display

When to use:

- Fixed panels embedded in equipment, vehicles, or walls, where the
  screen size is known in advance and the surroundings are demanding.

When to avoid:

- Personal devices or variable window sizes; use web and mobile layouts
  where the canvas is not fixed.

## Elements and components

Status readout with the primary value large and the unit labelled; a
small set of touch targets beside or below it; a persistent connection
indicator; an offline-capable control set that never needs the network
for core functions; a service or setup path kept out of the daily flow.

## Layout and responsive rules

- Design for the exact panel, not for breakpoints: common panels run
  7 to 10 inches at 1024 by 600 up to 1280 by 800; there is no reflow,
  so every element has a fixed position.
- Bright light: outdoor or high-ambient panels commonly need 800 to 1500
  or more nits, but brightness alone is not enough — pair it with
  anti-reflection treatment and optical enhancement, because readability
  starts at the glass layer, not the software.
- Keep contrast high in bright light: strong text-to-background contrast,
  no thin strokes or single-pixel detail, generous spacing, and a scheme
  that survives glare (dark on light or inverted).
- Operate fully offline: core functions never depend on a network; state
  is stored locally, actions that need sync queue visibly, and nothing
  silently fails or silently reorders when the connection returns.
- Prefer single touch over multi-touch so behaviour stays consistent
  across heterogeneous panels; keep momentary controls such as jog
  buttons as physical buttons or automated timers, since a stuck touch
  input can leave values changing.
- Do not rely on gestures for navigation: use straightforward
  button-based navigation; minimise swipes and sliders, and avoid
  on-screen keyboards on resistive panels.
- Match the touch technology to the environment: capacitive for modern
  multi-touch panels, resistive where gloves, stylus, or harsh conditions
  dominate — the technology follows the workplace, not the trend.
- E-paper panels: full refreshes take on the order of seconds and flash
  visibly, so never use video, moving cursors, or fast-changing charts;
  reserve quick localized updates for panels whose controller supports
  partial refresh (a firmware capability to specify early); e-paper is
  readable in sunlight and needs no backlight, so small panels suit
  single-value readouts and status flags, large ones documents and
  drawings.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The embedded panel at rest, primary value legible, connection indicator showing state. | Ready for input; core controls operate without a network. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch panels; hover never carries essential information alone. |
| Active | Pressed appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no touch response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Progress indicator or named step; on e-paper, a static step label replaces animation. | Keep layout dimensions stable so content does not shift. |
| Empty | The panel structure shows with a neutral prompt and one setup action. | Offer one clear next action. |
| Error | The failure is stated in place with the cause named; entered data is kept. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Fixed-canvas, bright-light contrast, and offline-first rules are documented.
- [ ] Refresh and power constraints are stated.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
