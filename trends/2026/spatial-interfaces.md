# Spatial Interfaces

Interfaces placed in three-dimensional space around the viewer: panels at
arm's length or across the room, arranged by depth as well as by plane. The
viewer is treated as a body with a neck and a gaze, not as a cursor.

## Classification

- Category: trends / 2026 / spatial-interfaces

When to use:

- Head-worn or room-scale experiences where content lives at distance and
  depth: dashboards around the viewer, object-anchored information,
  multi-window workspaces.

When to avoid:

- Adding depth to a task that a flat panel does better; precision data,
  forms, and keyboards stay on flat panels.
- Assuming a window always gets a spatial panel; every component ships a
  documented two-dimensional fallback.

## Elements and components

Comfort zones by gaze angle; distance placement tiers; flat, layered, and
deep arrangements; capability tiers per component with two-dimensional
fallbacks; high-contrast opaque alternatives to translucent panels.

## Layout and responsive rules

- Keep critical elements within the primary zone: roughly a 40-degree cone
  around the centre gaze (about ±20° horizontal, ±15° vertical, with the
  critical core within ~30° of forward gaze). Use the secondary zone,
  20–40° off-axis, for contextual or ambient content — larger and simpler.
- Place content at 1.2–1.5 m height for standing or sitting neutral gaze;
  never force upward neck tilt beyond about 15°.
- Tier by distance: arm's length for detailed interactive work, 1–3 m for
  general viewing, beyond 3 m for ambient information only; let content
  clarity adapt automatically by zone.
- Choose the panel by task: flat panels for precision data, forms, and
  keyboards (less distortion, easier ray or poke hits); curved panels for
  panoramic dashboards with the radius matched to the focal distance
  (2–3 m); never over-curve past about a 90° arc, which distorts edges.
- Define capability tiers per component (full spatial, basic, 2D fallback)
  and document which tier each component supports. Ordinary 2D surfaces run
  by default as 2D panels inside 3D space; spatial dialogs fall back to
  standard 2D dialogs.
- In multi-window spatial systems, cap promoted panels and give each
  window a fallback mode: inline (content stays in the main layout, nothing
  disappears) or drop (renders nothing until a panel is available), with
  priority ordering when slots run out.
- Translucent multi-layer panels are the current spatial look, but they
  fail legibility routinely: test all text on translucent backgrounds to a
  minimum AA contrast, provide a user toggle to a high-contrast opaque
  version, and profile blur effects for frame rate and power. Prefer
  progressive disclosure (gaze-triggered detail) over filling the space
  with panels.
- Never layer translucent surfaces on each other: stacked glass blurs into
  itself, burns performance, and turns text illegible; keep one
  translucent layer per view and put everything else on opaque panels.
- Translucency is conditional, not cosmetic: it disables automatically
  under high-contrast settings, with a high-contrast opaque variant as
  the default for that mode.
- Treat default translucency values as accessibility-tested: opacities and
  blur radii measured for legibility stay fixed, and anyone overriding
  them owns the resulting contrast evaluation.
- Map content to proxemic rings around the viewer: intimate (0–0.5 m) for
  highly personal lean-in items; personal (0.5–1.2 m, within arm's reach)
  for objects the viewer manipulates; social (1.2–3.7 m) for lean-out and
  shared content.
- Keep interactive content inside the comfortable depth band of about
  1.25–5 m: detailed frequent work near arm's length, general viewing at
  1–3 m, ambient information only beyond 3 m.

## Spatial page patterns

Multi-window spatial workspaces need an explicit panel contract.

- Give every window a declared fallback mode: inline (the window's
  content stays in the main layout, nothing disappears) or drop (renders
  nothing until a panel is available).
- Order windows by priority for when panel slots run out: centre the
  primary window at natural eye level, push supplementary windows to the
  periphery, and never let a secondary window occlude the full environment
  or cover critical space.
- Offer tiered viewing modes per window: a calm regular window for
  everyday tasks, full immersion only for experiences that genuinely need
  it, so the viewer can always step a window back instead of abandoning
  it.
- Reserve the peripheral field for larger, simpler, ambient elements;
  keep critical controls and fine text within about 30 degrees of forward
  gaze so they stay legible without eye strain.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A spatial layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change; gaze hover needs a dwell threshold before it counts. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Spatial page patterns, proxemic rings, and the comfort-zone band are documented.
- [ ] Fallback modes and panel priority ordering are stated.
- [ ] Translucent-panel rules cover legibility, no layering, high-contrast fallback, and tested opacity values.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
