# Changelog

All notable changes are recorded here. Format: newest first, grouped by
version, with Added, Changed, and Fixed sections where they apply.

## [Unreleased]

### Added

- Primitives catalogue: new "Media effect" primitive — cursor-reactive
  layered effects (ripple, pixel blocks, lens dispersion) over media on one
  shared full-page canvas; the DOM element stays the source of truth, each
  element opts out of global effects explicitly, effects are disabled under
  a reduced-motion preference, and position sync rules cover scroll, resize,
  and transformed elements.
- Layouts: new kiosk layout file (`layouts/kiosk.md`) — fixed-size screens,
  one task per screen, idle countdown with session reset, no personal data
  carried between sessions, accessibility controls on the first screen.
  Completes roadmap action 1.
- Patterns catalogue: onboarding pattern (step indicator, skip action,
  progress persistence) and data-table density and bulk-selection variants
  (user-chosen density, selection surviving sort and paging, stated action
  scope). Completes roadmap actions 2 and 4.
- States catalogue: offline, read-only, and permission-denied supporting
  states with appearance, behaviour, and recovery rules; loading rules for
  named steps and optimistic updates with quiet revert. Completes roadmap
  action 5.
- Interfaces catalogue: wearable glanceable rules (one glance per screen,
  ambient versus active display states, voice fallback), foldable posture
  rules (fold as a seam, warm transitions with exact scroll and focus
  restoration), and multi-surface continuity rules (task handoff across
  surfaces, navigation migration, morphing components). Cross-linked from
  `trends/2026/adaptive-interfaces.md`. Completes roadmap action 3.
- Functional motion trend: production motion values — 115/165/250 ms
  durations with matching easing curves, scale for incoming items and slide
  for structural moves, three-flashes-per-second ceiling, motion tokens.
  Based on an October 2026 design-system motion specification.
- Conversational interfaces trend: "When chat is the wrong surface" decision
  rules, conversational-layer handoff rules, and voice interaction states
  (one step at a time, per-step confirmation, repair asks only for the
  missing piece, barge-in support).
- Confirmation pattern: reversibility-tiered approval grades — free, confirm,
  and gate — plus standing permissions.
- Commerce layout: checkout variant rules — one-page versus multi-step by
  purchase type, always-shown step count, running total, instalment options,
  guest and wallet-accelerated checkout, explicit payment-retry states.
- Dashboard layout: synthesis-over-widgets rule for narrative summaries and
  what-changed reports.
- 14 new source records in resources/sources.json.

### Changed

- roadmap.md: coverage matrix updated to match reality (kiosk, onboarding,
  wearable, data-table variants, and offline/permission states promoted;
  television and embedded remain the least covered); completed items moved
  here; exactly three new improvement actions recorded.

### Added

- Modular card grids trend: layout rule for rearranged tiles — tile markup
  is written in priority order and named placement areas rearrange tiles at
  each breakpoint without changing source order, keeping assistive
  technology and keyboard focus in the same sequence at every size. Based
  on an October 2026 web design trends roundup on modular tile layouts and
  their reading-order failure modes.
- Source record for the October 2026 modular tile layout trend roundup in
  resources/sources.json.

- Adaptive interfaces trend: "Style variants" section — guidance for kits
  that ship every block in two complete visual styles (compact precise
  monochrome and roomy warm tactile) sharing layout, data, states, keyboard
  handling, and motion; rules on full coverage, theme-panel switching,
  per-style installation, and choosing by product context. Based on October
  2026 release notes for a component library's dual-style App UI update.
- Source record for the October 2026 dual-style component library changelog
  in resources/sources.json.

- Primitives catalogue: Markdown block entry with anatomy (headings,
  paragraphs, lists, tables, images, links, code blocks), read-only and
  editable-source variants, and rules (standard specification, sanitised
  input, responsive images, readable tables on narrow widths). Based on
  October 2026 release notes for a new Markdown content component.
- Source record for the October 2026 Markdown component release notes in
  resources/sources.json.

- States catalogue: focus retention rule for scrollable composite controls —
  after a scroll button is activated, focus returns to that button, and
  paging keeps keyboard focus inside the control (October 2026 UI kit
  release notes: carousel focus fixes).
- Source record for the October 2026 UI kit changelog in
  resources/sources.json.

- Primitives catalogue: form builder entry with anatomy (field palette,
  drag canvas, settings panel, live preview), builder variants, and rules
  (palette matches runtime fields; preview before saving; keyboard path for
  arranging fields). Based on October 2026 release notes for a drag-and-drop
  form-designing component with more than 20 built-in field types.
- Source record for the October 2026 form builder release notes in
  resources/sources.json.

- Primitives catalogue: leaderboard entry with anatomy, start/middle/end
  slot composition, and rules for ranked lists (October 2026 release notes:
  bar-list component retired in favour of composed leaderboard entries).

- Conversational interfaces trend: rendered interface answers section —
  compact interface programs from registered components, streamed rendering,
  version-matched syntax instructions, and blank-on-cut-off behaviour.
- Source record for the October 2026 streaming interface rendering release
  analysis in resources/sources.json.

- Primitives catalogue: sheet entry with anatomy, edge variants, and overlay
  composition rules (trigger wrapper, opening edge, composed parts).
- Source record for the October 2026 overlay composition release notes in
  resources/sources.json.
- Primitives catalogue: step trace and code block entries with anatomy,
  variants, and rules for interfaces that show the steps of an automated
  task and its code, terminal output, logs, or diffs.
- Source record for the October 2026 component release notes in
  resources/sources.json.

## [0.1.0] - 2026-10-21

### Added

- Initial structure: catalog, layouts, trends, examples, and resources.
- Interface taxonomy covering web, mobile, tablet, desktop, kiosk, wearable,
  television, conversational, spatial, and embedded interfaces.
- Primitive and pattern catalogues with a shared seven-state scheme.
- Page layouts for landing, dashboard, authentication, commerce, settings,
  and mobile navigation.
- Trend notes for 2026: adaptive interfaces, functional motion, modular card
  grids, and conversational interfaces.
- Two framework-free examples: dashboard and mobile navigation.
- Roadmap with a coverage matrix and concrete improvement actions.
