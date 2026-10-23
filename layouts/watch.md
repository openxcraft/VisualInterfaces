# Watch Layout

Glanceable single-action surfaces for wrist-worn screens, designed for
2–5 second tasks, with the paired phone app as the overflow for anything
longer.

## Classification

- Category: layouts / watch

When to use:

- Wrist-worn screens and other tiny always-worn displays where the
  person checks one datum or makes one decision.

When to avoid:

- Multi-step forms, long reading, or any task needing more than two
  taps; those belong on the phone companion surface.

## Elements and components

One key metric or one decision per screen; a single primary action;
progress shown as rings, arcs, or edge-hugging indicators; secondary
information follows the screen edge rather than stacking as text; an
explicit overflow button for secondary actions; haptic confirmation for
actions so the person need not look at the screen.

## Layout and responsive rules

- Glance-first: the essential datum is visible with no scrolling; a
  typical interaction lasts 3–5 seconds.
- One screen, one action: centre the single most important datum and
  action; keep micro-tasks only — check, accept/decline, start/stop,
  confirm.
- Two-tap rule: if a task needs more than two taps on the watch,
  relocate it to the phone companion app.
- Define margins as percentages of screen size on round displays so
  nothing clips at curved edges; add vertical constraints on
  non-scrolling views so central content fills the available area; round
  displays offer roughly a fifth less usable space than square ones.
- Size targets to the finger: minimum touch targets around 38–48dp
  spaced at least 8pt apart; treat the rotating crown or bezel as the
  primary scroll mechanism rather than fine swipes; favour full-screen
  swipes for navigation, long-press for context menus, and edge-based
  gestures.
- Visible overflow, never hidden gestures: provide an explicit overflow
  button for secondary actions; do not rely on gestures that demand
  memorisation.
- Confirm actions with haptic feedback first, so confirmation arrives
  without needing to look.
- Prefer dark interfaces with minimal background work to protect battery
  life.

## States

Full state definitions live in `../catalog/states.md`. The watch
layout's additions are below.

| State | Watch-specific note |
| --- | --- |
| Default | The watch surface at rest; one datum, one action, full contrast. |
| Hover | No hover on watches; designs that work without it. |
| Active | Immediate haptic pulse on press; feedback within 100 ms of input. |
| Disabled | Reduced contrast, still readable on small bright screens. |
| Loading | Compact progress ring around the datum; never a full-screen spinner. |
| Empty | A single starting action that sets up the datum being watched. |
| Error | One-line failure note with retry or exit; no long explanations. |

Every watch screen also ships an independent ambient, always-on
variant: no animation, reduced colour palette, low brightness, and the
critical datum (time, current value) still visible. Ambient and active
are separate layouts, not the same layout dimmed.

## Pre-publish checklist

- [ ] One datum and one action per screen; no scrolling needed to see them.
- [ ] Two-tap rule verified: longer tasks point at the phone companion.
- [ ] Round-display margins use percentages; nothing clips at curved edges.
- [ ] Ambient, always-on variant designed as a separate layout.
- [ ] All seven states defined with watch-specific notes: default, hover, active, disabled, loading, empty, error.
- [ ] Text is neutral, short, and free of names of persons and organisations in editorial prose.
- [ ] No references appear outside the resources files.
- [ ] No secrets, contact details, local filenames, or system paths are present.
- [ ] Internal links resolve and headings follow a consistent order.
