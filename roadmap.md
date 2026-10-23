# Roadmap

Planned work is recorded as concrete, actionable items. Completed items move
to `CHANGELOG.md`; this file keeps only open work and the coverage review.

## Classification

- Category: planning record for all categories.

When to use:

- After each deep editorial review, to record the next improvements.
- Before starting a change, to check whether it is already planned.

When to avoid:

- As a log of completed work; that belongs in `CHANGELOG.md`.

## Elements and components

- Coverage matrix, reviewed on a fixed cycle.
- Improvement actions, each with an owner step and a done condition.
- A list of the least covered areas, in priority order.

## Layout and responsive rules

- This file stays a single page; long detail belongs in the file it improves.
- Matrix rows are dimensions; columns are coverage levels.

## States

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A roadmap item at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty roadmap after a review is a defect; every deep review adds at least three actions. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | An item that cannot be done as written is rewritten with a smaller, testable step. | Keep entered data, place the message next to the problem, and offer a retry. |

## Coverage matrix

Rating: full = defined with states and an example or rule set; partial =
defined without an example; gap = named but not yet defined.

| Dimension | Full | Partial | Gap |
| --- | --- | --- | --- |
| Platform | Web, mobile, tablet, kiosk, television, embedded, wearable, desktop | — | — |
| Device input | Touch, pointer, keyboard, voice, gesture-only, remote | — | — |
| Interface type | Web app, mobile app, kiosk, conversational, embedded, spatial, automotive | — | — |
| Page pattern | Dashboard, mobile navigation, data table, checkout variants, onboarding, comparison, permission request, search results, command palette, notification escalation, offline-first sync, file upload, chat and messaging, map comparison, list navigation, stepper, landing, authentication, settings, commerce | — | — |
| State | All seven in catalog; offline, read-only, permission-denied; loading variants; error-state groups | — | — |

## Improvement actions

1. Add internationalization rules to `catalog/primitives.md`:
   right-to-left mirroring, text-expansion budgets, locale-aware
   date/number/currency formatting, and locale-aware sorting. Done
   when the new section passes all quality gates.
2. Add a third worked example (`examples/onboarding/`): the onboarding
   layout's step sequence, skip-and-return, and compact-screen rules
   demonstrated with all seven states. Done when the example builds
   and passes all quality gates.
3. Deepen `trends/2026/machine-experience.md` (the thinnest trend file
   after this review's modular-card-grids work): structured-data
   summaries for agent readers, explicit task affordances, consent
   signals for automated access, and human-first ordering guarantees.
   Done when the expanded file passes all quality gates.
4. Add a media-controls primitive row to `catalog/primitives.md`: the
   expected control set (play/pause, seek, volume, captions, speed,
   settings), placement conventions, feedback confirming every control
   responds, full keyboard operation with named controls, captions
   always available, and no auto-playing sound. Done when the row
   passes all quality gates.
5. Extend the chat and messaging pattern row in `catalog/patterns.md`
   with group-conversation rules: per-participant read indicators,
   reply threading, presence states, and mention handling —
   cross-checked against `trends/2026/conversational-interfaces.md`.
   Done when the extended row passes all quality gates.

## Review notes

- Completed this review: new `layouts/automotive.md` (two-second
  glance budget, 12-second task budget, one question per glance, stable
  information positions, 0.25 s input response, 76x76 dp targets,
  32/24 dp text, physical controls for essential functions, day/night
  modes, distraction suppression while moving, one-handed gestures);
  three new pattern rows in `catalog/patterns.md` — map comparison
  (hover notes, visited markers, small multiples, peel-back swipe,
  pop-up versus panel, rich markers), chat and messaging (capabilities
  up front, quick actions, progressive streaming with stop, inline
  error on the failed bubble, offline queue with visible banner, live
  regions, 44 px targets), and list navigation (infinite scroll for
  exploration, pagination for goal-oriented tasks, load-more as the
  safe default, place-restoring URL handling) — plus the Wizard row
  strengthened with total step count up front, non-interactive future
  steps, contextual forward labels, data-preserving back, vertical
  steppers on narrow screens, and save-and-resume; new Date picker
  primitive row in `catalog/primitives.md` (lightest control per
  intent, seven day-cell states, typed entry as a first-class path,
  explicit ranges, timezone-explicit times, presets, keyboard
  contract); dashboard KPI rules in `layouts/dashboard.md`
  (three-slot tiles, grayscale readability, 3:1 density ratio,
  always-visible filter chips, cadence matched to the decision cycle,
  stated last-updated time); kiosk accessibility deepening in
  `layouts/kiosk.md` (assistive entry point usable without vision,
  multi-sense time alerts with extension, 800–1600 mm reach bounds,
  one-tap reset, offline fallback, speech-available receipts); APCA
  perceptual-contrast note in `trends/2026/standards-outlook.md`
  (0–120 lightness score, polarity-aware, 90/75/60/45 thresholds,
  test against both systems) plus the assistive-entry-point
  principle; new `trends/2026/dark-mode.md` (dark greys not black,
  type adjustments, elevation over shadows, redesigned accents,
  semantic token contract, system default with user override,
  200–300 ms switch honouring reduced motion, OLED/LCD/e-ink
  testing); 13 new source records (177 total). Completes roadmap
  actions 3, 4, 5, and 6 from the previous review.
- Completed this review: search-health evaluation checklist in the
  Search pattern row of `catalog/patterns.md` (success rate,
  time-to-result, zero-result rate, click position, refinement rate;
  rising zero-result or refinement rates point at vocabulary or scope
  design, and zero-result queries are logged as free research);
  supporting-state rows for focused, selected, expanded, and warning in
  `catalog/states.md` with appearance, behaviour, and recovery for
  each; new `trends/2026/standards-outlook.md` horizon note on the
  WCAG 3.0 draft (Working Draft status, final recommendation not
  expected before 2028, outcomes-based Bronze/Silver/Gold scoring
  with Bronze mapping approximately to 2.2 AA, no deprecation of
  2.x, build to 2.2 AA today and instrument outcomes); deepened
  `trends/2026/modular-card-grids.md` (fixed size tiers by importance,
  density as a grid property, overflow to a "view all" surface,
  reorder feedback with plain-text announcements and persistence).
  Completes roadmap actions 3, 4, 5, and 6.
  (subsequence matching, synonyms, grouped typed results, stable selection,
  safe execution) with a cross-link from the shortcut rules in
  `layouts/desktop.md`; notification-escalation pattern (urgency-to-channel
  scale, notification-debt rule); offline-first-sync pattern (durable
  mutation queue, granular sync states, marked-pending optimistic updates);
  file-upload resilience pattern (chunking, per-file retry, accurate
  progress after resume); extended Search row with typeahead rules;
  automotive HMI interface entry with glance budgets and
  physical-control rules (Interface type promoted in the coverage matrix);
  reduced-motion nuance in `trends/2026/functional-motion.md`
  (informational versus decorative motion, fail-closed gating, visible
  pause control); focus-indicator strengthening in `catalog/states.md`
  (3:1 contrast, forced-colours outline, scroll padding); glass-layer
  constraints in `trends/2026/spatial-interfaces.md`; merged the two
  identical Media effect rows in `catalog/primitives.md` into one;
  web-components refresh in `resources/libraries.md` (successor library
  entry, unstyled-primitives direction); 15 new source records (162
  total); coverage matrix refreshed (automotive, command palette,
  notification escalation, offline-first sync, file upload promoted to
  full).
- Completed actions 1–4 from the previous review: the duplicated
  seven-state tables and pre-publish checklists are consolidated (one
  canonical states file, per-file notes and checklists, canonical
  checklist kept in `CONTRIBUTING.md`; `check_quality.py` reports zero
  duplicate paragraphs); spatial page patterns with per-window fallback
  modes, priority ordering, proxemic rings, and the 1.25–5 m comfort band
  in `trends/2026/spatial-interfaces.md`; remote-control input guidance
  (directional-pad, pointer, touch-surface, scroll-wheel) in
  `catalog/interfaces.md` cross-linked from `layouts/tv.md`; new
  `layouts/watch.md` with glance-first rules, the two-tap rule,
  percentage-based round-display margins, and a separate ambient variant.
- Most duplicated area: none remaining; the duplicate-paragraph warning
  is cleared.
- Least covered area: internationalization rules (no coverage), a third
  worked example (only two exist), and the machine-experience trend
  file (thinnest file); now actions 1, 2, and 3.
- Completed this review: responsive data-table strategies in
  `layouts/dashboard.md` (four strategies with shared rules); new
  `layouts/onboarding.md` (success action, smart defaults, prefill,
  skip-and-return, measurable activation); new `layouts/desktop.md`
  (menu bars, mnemonics, shortcuts, context menus, drag-and-drop as
  progressive enhancement, multi-window rules); desktop interface row
  cross-linked in `catalog/interfaces.md`; Desktop promoted from
  partial to full in the coverage matrix; 7 new source records (141
  total).
- Completed this review: comparison pattern, permission-request flow
  pattern, and search-results pattern in `catalog/patterns.md` (with a
  cross-link from the permission-denied row in `catalog/states.md`);
  data-table grouped-loading and cell-action rules; new
  `layouts/tablet.md` (window size bands, navigation switching, two-pane
  thresholds, foldable postures); television layout deepened (type
  minimums, safe-area margins, spatial focus, remote input variants,
  real-distance testing); landing layout deepened (outcome-first hero,
  section order, form friction); authentication layout deepened
  (passkey-first flow, visible fallback chain, one-time enrollment,
  QR context, credential management); settings layout deepened (sidebar
  navigation, settings search design, danger zone); wearable interfaces
  section in `catalog/interfaces.md` with a cross-link to the spatial
  trend file; conversational trend gained an interruption-budget section;
  functional-motion trend gained reduced-motion swap rules; agentic trend
  gained the six trust patterns and the orchestration surface; new
  `trends/2026/spatial-interfaces.md`; headless behaviour primitive and
  form-builder confirmation rules in `catalog/primitives.md`; 55 new
  source records (115 total); coverage matrix refreshed (tablet, wearable,
  landing, authentication, settings, comparison, permission request,
  search results, and loading variants promoted to full).
- Completed this review: embedded display layout (`layouts/embedded.md`,
  referenced from `catalog/interfaces.md`); gesture-only worked example
  with thresholds and recovery; voice state matrix extended with
  per-state timeouts, barge-in timing, and backchannel rules; spatial
  interface note with depth arrangements, comfort zone, and flat-view exit;
  empty-state taxonomy (already recorded in `CHANGELOG.md`); inline
  assistant-action pattern cross-linked from
  `trends/2026/agentic-ux.md`; multimodal voice-plus-screen pairing
  cross-linked from `catalog/interfaces.md`; onboarding prefill and
  default rules.

## Pre-publish checklist

The canonical publishing checklist lives in `CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The coverage matrix matches the actual files and directories.
- [ ] Only open improvement actions remain listed; completed ones moved to CHANGELOG.md.
- [ ] Exactly three new actions were added at the last deep review.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
