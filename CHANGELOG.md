# Changelog

All notable changes are recorded here. Format: newest first, grouped by
version, with Added, Changed, and Fixed sections where they apply.

## [Unreleased]

### Added

- States catalogue: grouped action-state rule — one component owns an
  action's idle, loading, and success presentations and the transitions
  between them, instead of scattering state logic across icons, labels,
  and handlers; transitions announce to assistive technology, dimensions
  stay fixed while loading, and focus returns when the success
  presentation clears.
- Conversational interfaces trend: author-side validation gate for rendered
  interface answers — validate each interface tree against the registered
  component set before shipping; unknown components are caught when the
  tree is produced, not at render time; forms may submit only to approved
  destinations; the check stays cheap enough to run on every tree.
- Interfaces catalogue: new extension interfaces section — the inline
  overlay replaces the classic click-icon dropdown flow: anchor the
  floating panel to the cursor or the target element, show results next
  to their source, dismiss cheaply returning focus to the anchor, build
  with a web component and closed shadow root (not iframes), defend
  against host pages on shadow DOM/z-index/scroll, size to content, full
  keyboard access.
- Functional motion trend: scroll-triggered animation rule — content
  revealed by scroll position stays available to screen-reader and keyboard
  users; scroll position never gates content alone.
- Primitives catalogue: citation card primitive — source label, excerpt,
  open-source link, optional page or timestamp reference; one card per
  source, evidence placed beside the claim it supports, excerpts never
  invented, long excerpts collapsed behind an expand control.
- Layouts: new embedded display layout file (`layouts/embedded.md`) —
  fixed-size canvases, bright-light contrast rules (800-1500+ nit panels
  paired with anti-reflection treatment, readability starting at the glass
  layer), offline-first operation, single-touch and button-based navigation
  rules, resistive-versus-capacitive matching, and e-paper refresh
  constraints; referenced from `catalog/interfaces.md`. Completes roadmap
  action 1.
- Interfaces catalogue: gesture-only worked example (swipe-to-archive) —
  discoverability cues, progressive teaching, tap/drag thresholds,
  continuous tracking feedback, lift-off commit with cancel, and an
  inline undo; plus a spatial interfaces note (flat/layered/deep depth
  arrangements, 1.25-5 m comfort zone, home zone, flat-view exit), each with
  all seven states defined. Completes roadmap actions 3 and 5.
- Conversational interfaces trend: voice state matrix extended with
  per-state timeouts (re-prompt once, then alternative input, then polite
  end), ~300 ms barge-in target, backchannel-word handling, and mandatory
  disclosure protection; new voice-plus-screen pairing section with
  channel-assignment rules, synchronised transcript, and third-turn exit;
  cross-linked from `catalog/interfaces.md`. Completes roadmap actions 4
  and 8.
- Agentic interfaces trend: trust gradient and partial-work rules —
  preview to supervised to autonomous graduation, first-class rollback,
  honest per-step status, and inline overrides.
- Patterns catalogue: new inline assistant-action pattern (commands as
  verbs on the existing surface, inline-beats-chat rule,
  reversibility-graded scope) cross-linked from
  `trends/2026/agentic-ux.md`; onboarding extended with language and
  region prefill, one-tap correction, no pre-selected sensitive fields,
  and one question at a time. Completes roadmap actions 7 and 9.
- roadmap.md: coverage matrix refreshed (embedded, voice, gesture-only,
  conversational, and onboarding promoted; spatial partially defined);
  exactly three new improvement actions (comparison pattern,
  permission-request flow pattern, tablet middle-zone layout guidance);
  state-table consolidation remains open.
- 10 new source records in resources/sources.json (embedded displays,
  gesture thresholds, spatial design, voice states, multimodal pairing,
  agentic patterns).

### Added

- trends/2026: "Machine Experience Design" — designing pages so automated
  agents can read, compare, and complete tasks accurately: source order
  matching visual order at every breakpoint, key facts as real text, native
  structures for headings/lists/tables/forms, critical content never
  hidden in scripts, canvas, gesture-only controls, or hover-only reveals.
- 1 new source record in resources/sources.json (machine-readable page
  structure for automated agents).
- States catalogue: "Empty-state variants" section — first-use, naturally
  empty, and restricted-or-failed variants with copy rules, one clear next
  action each, and an explicit status value that never infers state from an
  item count. Completes roadmap action 6.
- roadmap.md: four new improvement actions (empty-state taxonomy done;
  inline assistant-action pattern; multimodal voice-plus-screen pairing;
  onboarding prefill and default rules), ordered by coverage impact.
- 4 new source records in resources/sources.json (empty-state design,
  assistant surface patterns, onboarding defaults).

### Added

- Layouts: new television layout file (`layouts/tv.md`) — focus-based
  navigation as the whole scheme, 10-foot legibility rules (large
  high-contrast type, short lines, safe margins), shelf-and-hero content
  structure, spoken-query text entry, second-device handoff for complex
  flows, dedicated playback screen, and light-motion rules for slower
  hardware. Completes roadmap action 1.
- Interfaces catalogue: gesture-only input section — small consistent
  gesture set, teach-without-manual hints, variation tolerance thresholds,
  immediate recognition feedback, cheap reversible errors, and a
  non-gesture alternative for every essential task.
- Conversational interfaces trend: voice dialogue state rules — consistent
  interruption handling with resume from the last confirmed step, short
  interruptible utterances, generous adjustable timeouts with tapered
  reprompts, noisy-environment fallbacks, and loop limits with safe
  handoff.
- roadmap.md: television completed; exactly three new improvement actions
  (gesture-only worked example, full voice state matrix, spatial page
  patterns); coverage matrix refreshed — television and checkout variants
  promoted to full, gesture-only promoted to partial.
- 7 new source records in resources/sources.json.

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
