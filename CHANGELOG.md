# Changelog

All notable changes are recorded here. Format: newest first, grouped by
version, with Added, Changed, and Fixed sections where they apply.

## [Unreleased]

### Added

- Layouts: responsive data-table strategies in `layouts/dashboard.md` —
  horizontal scroll with a frozen leading column, column dropping by
  priority, priority-plus disclosure, and card transformation, with
  shared rules for state stability, focus order, labelled card values,
  and truncation. Completes roadmap action 1.
- Layouts: new `layouts/onboarding.md` — success action first, welcome
  modal removed, one question per step, deferred sign-in, skip-and-return
  with persisted progress, smart-default and prefill rules consolidated
  from `catalog/patterns.md`, sample data over blank slates, progressive
  disclosure with intent, mechanism-agnostic guidance, measurable
  activation, and compact-screen rules. Completes roadmap action 2.
- Layouts: new `layouts/desktop.md` — menu bars with keyboard patterns,
  mnemonics, shortcut rules, context-menu rules, drag and drop as a
  progressive enhancement with a required non-drag path, multi-window
  management, density rules, and narrow-window bands. Promotes Desktop
  from partial to full in the coverage matrix. Completes roadmap action
  3.
- Interface catalogue: desktop application row now cross-links
  `layouts/desktop.md`.
- Seven new source records in `resources/sources.json` (141 total).

- States catalogue: focus-obscurity rule — keyboard focus must stay
  visible above fixed overlays such as sticky headers, consent controls,
  chat launchers, and banners; scrolling a control into focus lands it
  fully clear of any fixed chrome.
- Source record for the October 2026 web design trends roundup in
  resources/sources.json.
- Functional motion: expressive shape-morph reduced-motion rule — variants
  must disable spring and bounce physics intensity and component shape
  morphing themselves, since zeroing the duration leaves the physics alive;
  the reduced state ships the static resting shape.
- Layouts: new `layouts/watch.md` — glance-first rule (one datum or
  decision per screen, 2–5 second tasks), two-tap rule with phone
  companion overflow, percentage-based round-display margins, finger-size
  targets with crown or bezel as the primary scroll mechanism, explicit
  overflow button, haptic-first confirmation, and an independent ambient
  always-on variant. Completes roadmap action 4.
- Spatial trend: spatial page patterns — multi-window contract with
  per-window fallback modes (inline versus drop), priority ordering when
  panel slots run out, tiered viewing modes, proxemic rings
  (intimate 0–0.5 m, personal 0.5–1.2 m, social 1.2–3.7 m), and the
  1.25–5 m comfort band. Completes roadmap action 2.
- Interface catalogue: remote-control input section — directional-pad
  first as the common denominator, pointer remotes without pad-exclusive
  actions, touch-surface remotes on the focus behaviour, scroll-wheel mapping,
  low-fatigue focus order; display-side television rules stay in
  `layouts/tv.md`. Completes roadmap action 3.
- States catalogue: error-state groups — presentations grouped by the
  next action (input rejected, session or permission lost, conflict or
  gone, rate-limited, server error, offline or timeout with visible
  queuing); permission-denied now names who can grant the access.
- Dashboard layout: data-table rules — grouped loading (headers
  immediate, body skeleton rows, 50–100 ms stagger) and row actions under
  a single overflow menu with destructive actions guarded and separate.
- Conversational trend: mandatory automation disclosure — identity,
  purpose, recording notice, opt-out, and path to a person stated up
  front in the caller's language, repeated after transfer, never claiming
  to be human; false-interruption recovery from the last confirmed-played
  boundary with stale results discarded.
- Patterns catalogue: permission-request row — never nag within the same
  session after a denial; a single in-app screen listing all permissions
  with one-tap revocation. Comparison row — cards when few real
  differences, tabs, accordions, or a collapsible matrix when the feature
  list is long. Onboarding row — smart defaults from location, common
  choice, or past behaviour; editable, validation deferred, standard
  autocomplete tokens, no defaults for decisions needing deliberation.
- Roadmap: actions 1–4 completed and three new actions added (responsive
  data-table strategies, onboarding layout file, desktop application
  layout file); coverage matrix promotes remote input and spatial to
  full.

### Changed

- Consolidated the duplicated seven-state tables and pre-publish
  checklists across 27 files: each file now points to
  `catalog/states.md` for canonical state definitions and keeps
  file-specific state notes; the canonical publishing checklist lives in
  `CONTRIBUTING.md` with per-file checks tailored to each file's subject.
  Completes roadmap action 1; `check_quality.py` reports zero duplicate
  paragraphs.

- Layouts: barely-there restraint direction for dashboards — on data-and-trust surfaces, extreme restraint signals seriousness: one typeface doing most of the work, hairline low-opacity borders, structure from white space and typographic weight instead of boxes and shadows; a two-to-three-tone palette; treated as a fit decision that suits operational overviews and fits poorly where warmth or character must come through.

- Patterns catalogue: simplified-view pattern — an on-demand simplified
  version that hides non-essential features and shortens text, easy to
  enter and easy to leave; content on critical paths is marked for
  simplification (data-simplification attribute) so personalization tools
  can reduce it; extra features stay discoverable, never permanently
  removed.
- Trends: anchored-popup sizing rule — popups default to the trigger's
  width; widen only when the content needs the room; re-anchor after
  resize so the overlay stays aligned with its trigger.
- Patterns catalogue: comparison pattern — fixed criterion order, three to
  four option columns, plain audience labels, "everything in the previous
  tier, plus" summaries, differences-only toggle, gentle winner marking
  with shading plus a text cue (never colour alone), computed deltas,
  explicit metric direction, sticky labels and decision row, annual saving
  spelled out. Completes roadmap action 2.
- Patterns catalogue: permission-request flow pattern — two-stage flow
  (custom pre-permission rationale stating the concrete value, system
  dialog only after a positive response), asked in context and never on
  first launch, one permission at a time, graceful denial into a
  feature-limited experience, plain explanation and settings route on
  permanent denial; cross-linked from the permission-denied row in the
  states catalogue. Completes roadmap action 3.
- Patterns catalogue: search-results pattern — search narrows by intent and
  filters by attribute; ordered no-results recovery (spelling suggestion,
  scope broadening, removable carried filters, create action); exact
  query-and-filter echo with no silent clearing; mirrored filter chips;
  reset clears filters but keeps the query; facet placement with live
  result counts.
- Patterns catalogue: data-table grouped-loading and cell-action rules —
  loading state per section rather than whole-table only, expanded rows
  aligned to the visible viewport, cell-level actions combining one link
  with one or two adjacent actions.
- Layouts: new tablet layout file (`layouts/tablet.md`) — window size
  bands (compact under ~600dp, medium 600–840dp, expanded 840–1200dp),
  navigation switching with width (bottom bar, rail around 600dp,
  permanent drawer around 840dp), two-pane list-detail threshold,
  supporting-pane splits, orientation-change continuity, and
  posture-aware foldable rules (tabletop, book, no interactive elements
  across the fold, in-progress state preserved). Completes roadmap
  action 4.
- Television layout: deepened 10-foot rules — type minimums (~12sp minimum,
  18sp default, ~24pt practical floor at 3 m), no thin typefaces, light
  text on dark backgrounds, ~5% safe-area margin (27 px top/bottom,
  48 px left/right on 1080p), centre-weighted content, real-distance
  testing from ~3 m, near-white #f1f1f1 to reduce flicker, per-variant
  remote input planning.
- Landing layout: outcome-first hero rules — named audience and measurable
  outcome headline, one primary action with a risk reducer, proof before
  first scroll, product shown in motion, decision-mirroring section order,
  three-field form discipline with multi-step forms for longer asks.
- Authentication layout: passkey-first flow — passkeys in the username
  autofill dropdown via conditional mediation, visible fallback chain
  (passkey, app push, email magic link, email code, SMS last), one-time
  enrollment timing, labelled QR cross-device context, credential
  management page with rename and revoke.
- Settings layout: sidebar-over-icon-grid navigation, edit chrome matched
  to stakes, settings-search design rules (20+ field heuristic, synonym
  matching, section and current-value results, zero-result logging), and
  a danger-zone pattern with effort-graded confirmation.
- Interfaces catalogue: wearable interfaces section — 2–5 second task
  window, one primary item per screen, two-tap overflow to the phone app,
  non-scrollable glanceable tiles, 38–48dp targets, swipe and crown
  navigation, haptic-first confirmation, round-first margins, ambient
  always-on state.
- Conversational interfaces trend: interruption-budget section — the
  interruption budget is separate from the response-latency budget;
  200–300 ms stop pipeline with an explicit interrupted state; learned
  turn-taking over bare silence thresholds; chunked turn-taking rhythm;
  voice-plus-screen channel fusion; spoken fallbacks in voice-only
  contexts.
- Functional motion trend: reduced-motion swap rules — ship a deliberate
  final static state per effect, swap movement for calm (keep the fade,
  drop the travel), slower essential spinners (~1.5 s), visible
  pause-animations control.
- Agentic interfaces trend: six trust patterns across the action lifecycle
  (intent preview, autonomy dial, explainable rationale, confidence
  signal, action audit and undo, escalation pathway) and the
  orchestration surface with post-action receipts.
- Trends: new spatial interfaces file (`trends/2026/spatial-interfaces.md`)
  — comfort zones by gaze angle, distance placement tiers, flat versus
  curved panel choice, per-component capability tiers with 2D fallbacks,
  translucent-panel contrast testing and battery discipline; cross-linked
  from `catalog/interfaces.md`.
- Primitives catalogue: headless behaviour primitive — behavioural
  guarantees listed separately from visual styling; and form-builder
  confirmation rule — per-part keyboard coverage with an explicit
  confirmation step for high-stakes popovers.
- States catalogue: loading-state rules — skeletons reserved for waits of
  roughly 1 to 10 seconds, layout-matched placeholders with a spinner
  fallback when layout is unknown, per-placeholder replacement as content
  arrives, empty states never shown during fetch, static reduced-motion
  variants, and assistive-technology announcements for loading status.

- Functional motion trend: native platform capability convergence section —
  anchor positioning for tethering tooltips, menus, and popovers to their
  trigger with a static-placement fallback; scroll-driven animation
  timelines animating transform and opacity only so motion stays off the
  main thread; view transitions for document-to-document navigation;
  native dialog and popover semantics for overlays.
- Primitives catalogue: target-size audit rules — audits separate the 44 px
  aspiration from the 24 px requirement; a finding records page, viewport,
  target, clickable dimensions, nearby controls, exception analysis, and user
  consequence; remediation enlarges the hit area, increases spacing, or
  changes the shared component; retesting happens after the change ships,
  including responsive states.
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
