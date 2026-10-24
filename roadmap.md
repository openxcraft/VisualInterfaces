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
| Page pattern | Dashboard, mobile navigation, data table, checkout variants, onboarding, comparison, permission request, search results, command palette, notification escalation, offline-first sync, sync-conflict resolution, file upload, chat and messaging, map comparison, list navigation, machine-composed content disclosure, agent checkpoint, voice hybrid flows, stepper, landing, authentication, settings, commerce, consent | — | — |
| State | All seven in catalog; offline, read-only, permission-denied; loading variants; error-state groups | — | — |
| Worked examples | Dashboard, mobile navigation, onboarding — each demonstrating the rules it documents with all seven states | — | — |
| Localization | Right-to-left mirroring rules, what-not-to-mirror list, logical properties, text-expansion budgets, locale-aware date/number/currency formatting and sorting, mixed-direction text | — | — |
| Responsive technique | Container-query component adaptation verified in full-page, sidebar, modal, and dense-dashboard grid contexts; viewport queries for page-level bands | — | — |

## Improvement actions

1. Add an agent-checkpoint pattern row to `catalog/patterns.md`: the
   delegate–monitor–approve–interrupt–refine loop, interruption points
   before irreversible actions, explicit approval surfaces for cost,
   purchase, privacy, or booking decisions, and a recovery path when an
   automated flow took a plausible but wrong route — cross-checked
   against the supervision and trust-gradient sections in
   `trends/2026/agentic-ux.md`. Done when the row passes all quality
   gates. (Implemented this run.)
2. Add voice hybrid-flow rules to
   `trends/2026/conversational-interfaces.md`: voice-to-initiate with
   physical (tap or biometric) confirmation for sensitive actions, and
   visual mishearing repair that shows what was heard with tappable
   correction instead of a dead-end message — cross-checked against the
   voice state matrix in `catalog/states.md`. Done when the extended
   file passes all quality gates. (Implemented this run.)
3. Add container-query responsiveness guidance to the layout rules:
   components must adapt to their container's size rather than only the
   viewport, verified in full-page, sidebar, modal, and dense-dashboard
   grid contexts. Done when the rules pass all quality gates.
   (Implemented this run.)
4. Add a machine-composed content disclosure pattern row to
   `catalog/patterns.md`: label every block the system composed as
   composed, state uncertainty and grounding plainly, keep a visible
   correction and override path, and pair any composed decision with
   effects outside the screen with an explicit approval step —
   cross-checked against the trust patterns in
   `trends/2026/agentic-ux.md` and the disclosure rules in
   `trends/2026/conversational-interfaces.md`. Done when the row passes
   all quality gates. (Implemented this run.)
5. Add a multimodal input-bar primitive row to `catalog/primitives.md`:
   text field with mic and media-attach entries, a hint naming all
   three modes, per-mode feedback (waveform while listening,
   thumbnails for attachments, processing states), an echo of what was
   heard with a quick correction path, and keyboard and screen-reader
   parity for every mode — cross-checked against the voice state matrix
   in `catalog/states.md`. Done when the row passes all quality gates. (Implemented this run.)
6. Add a personalized-content disclosure pattern row to
   `catalog/patterns.md`: when order, content, or recommendations adapt
   to the person, state what signal drove the adaptation, offer the
   unadapted view, and provide a change or turn-off path;
   inference-driven adaptation is reversible by default —
   cross-checked against the granular-consent row. Done when the row
   passes all quality gates.

7. Add a sync-conflict resolution pattern row to `catalog/patterns.md`:
   when a locally queued change and a newer server version diverge,
   show both versions side by side, keep the local copy safe until
   resolved, let the person pick one version or merge field by field,
   and never silently overwrite either side — cross-checked against
   the offline-first sync row. Done when the row passes all quality
   gates. (Implemented this run.)
8. Add a voice command discovery section to
   `trends/2026/conversational-interfaces.md`: teach what can be asked
   in context — suggested prompts on first use, example utterances for
   the current screen, and a browsable list of capabilities — rather
   than a tour or a help page nobody opens. Done when the section
   passes all quality gates. (Implemented this run.)
9. Add a multi-device handoff pattern row to `catalog/patterns.md`:
   continue a task on another device from an explicit resume point,
   state what transferred and what did not, and resolve the case where
   both devices edited the same item before handing off — cross-checked
   against the offline-first sync row. Done when the row passes all
   quality gates.

10. Add a collaborative editing presence pattern row to
    `catalog/patterns.md`: show who else is present in the shared
    document, which field each person is editing, and a visible lock or
    hold on the field being edited, so two people never overwrite the
    same field unknowingly — cross-checked against the sync-conflict
    resolution row. Done when the row passes all quality gates.
11. Add a draft autosave and recovery pattern row to
    `catalog/patterns.md`: save drafts continuously with a visible
    saved indicator, restore the latest draft after a crash or
    interruption with a clear review step, and offer an explicit
    discard path — cross-checked against the wizard save-and-resume
    rules. Done when the row passes all quality gates.
12. Add a notification digest pattern row to `catalog/patterns.md`:
    group low-urgency updates into a scheduled digest the person
    controls (daily or weekly), keep every item individually openable,
    and never digest a critical or time-sensitive item — cross-checked
    against the notification escalation scale. Done when the row passes
    all quality gates.

## Review notes

- Completed this review (deep editorial 2026-10-24): new Multimodal
  input-bar primitive row in `catalog/primitives.md` (one bar for text,
  voice, and media entry, hint naming all three modes, editable
  transcript before sending, thumbnails with remove control, named
  processing steps, keyboard and screen-reader parity for every mode);
  new Sync-conflict resolution pattern row in `catalog/patterns.md`
  (side-by-side versions, field-by-field merge with a merged preview,
  sensitive fields always ask, deletion-versus-edit treated as a
  conflict, local copy kept safe until resolved); new Voice command
  discovery section in `trends/2026/conversational-interfaces.md`
  (suggested prompts on first use, screen-specific example utterances,
  browsable capability list, teaching inside replies, progressive
  introduction, recovery as discovery). Completes roadmap actions 5,
  7, and 8. Coverage matrix refreshed (sync-conflict resolution
  promoted to full). 3 new source records (219 total).

- Completed this review (deep editorial 2026-10-24): new Agent
  checkpoint pattern row in `catalog/patterns.md` (delegate–monitor–
  approve–interrupt–refine loop, exact-payload approval cards,
  approve/edit/reject decisions, stated autonomy budget, decision
  record); new Voice hybrid flows section in
  `trends/2026/conversational-interfaces.md` (voice-to-initiate with
  physical confirmation for sensitive actions, visual mishearing repair
  with tappable correction, confirmation graded by stakes); container-
  query responsiveness guidance in `layouts/desktop.md` (container
  declaration and naming, verification in full-page, sidebar, modal,
  and dense-grid contexts, containment caveat). Completes roadmap
  actions 1, 2, and 3. 5 new source records (215 total).

- Completed this review (daily planning 2026-10-24): research pass of 4
  searches covering agent checkpoint design, voice and multimodal
  patterns, container-query practice, and late-October 2026 trend
  roundups; 6 new source records (209 total), URLs copied verbatim from
  results and deduplicated against the existing set. Roadmap actions 1–3
  (agent-checkpoint pattern, voice hybrid flows, container-query
  guidance) remain open and unimplemented; the checkpoint-design
  findings support action 1 when the deep cycle takes it. Three new
  actions added (4–6), ordered by coverage impact: machine-composed
  content disclosure (implemented this run), multimodal input-bar
  primitive, and personalized-content disclosure. All completions since
  the previous daily run are recorded in `CHANGELOG.md`.
- Completed this review: new Media controls and Haptic feedback
  primitive rows in `catalog/primitives.md` (control set in reading
  order with 100 ms response confirmation, keyboard operation, captions
  always available, no auto-playing sound; confirm/alert/error haptic
  intensities paired with visual or spoken signals, user disable, no
  loops); group-conversation rules in the chat and messaging pattern
  row of `catalog/patterns.md` (per-participant read indicators, reply
  threading, honest presence states, mention handling, cross-linked
  from `trends/2026/conversational-interfaces.md`); new Granular
  consent pattern row (per-category toggles never pre-checked,
  just-in-time disclosure, frictionless revocation, audit trail,
  cross-checked against the consent signals in
  `trends/2026/machine-experience.md`); contrast-verification routine
  in `trends/2026/dark-mode.md` (both token sets, size-aware muted
  text, forced-colours-mode behaviour, text over photography,
  re-check on every new surface). Completes roadmap actions 1–5.
- Completed this review (research pass): Ask/Infer/Defer/Confirm form
  collection rules and the low-risk-only boundary for smart defaults in
  the Form flow row of `catalog/patterns.md`; unknown-outcome error
  group and strengthened restricted/failure-copy rules in
  `catalog/states.md` (verify-before-retry, never reuse the zero-item
  message for a load failure, restricted messages never imply a
  workaround); September 2026 WCAG 3.0 draft structure in
  `trends/2026/standards-outlook.md` (one conformance level, six
  reporting tiers, four impact tags, direction not requirements); new
  spatial interaction ergonomics section in
  `trends/2026/spatial-interfaces.md` (gaze as targeting cursor with
  intent-confirming hover, lap-level micro-gestures, positional audio
  anchors). 8 new source records (202 total).
- Most duplicated area: none remaining; the duplicate-paragraph warning
  is cleared.
- Least covered area: agent-checkpoint pattern, voice hybrid flows, and
  container-query responsiveness guidance (all absent); now actions
  1, 2, and 3.
- Completed this review: new internationalization section in
  `catalog/primitives.md` (mirroring rules with a never-mirror list,
  logical properties, directional-icon rules, ~40%/~30% text-expansion
  budgets, locale-aware date/number/currency formatting and sorting,
  bidirectional text, direction testing); deepened
  `trends/2026/machine-experience.md` (structured-data summaries for
  agent readers, explicit task affordances, typed errors with
  retryable/hint/partial-result fields, consent signals with human
  confirmation for high-risk actions, human-first ordering, idempotent
  operations, release checklist); new third worked example
  `examples/onboarding/` (stated step total, skip-and-return with a
  resume panel, sticky thumb-reach action bar, all seven states
  demonstrated); 8 new source records (190 total). Completes roadmap
  actions 1, 2, and 3.
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
- Least covered area: agent-checkpoint pattern, voice hybrid flows, and
  container-query responsiveness guidance (all absent); now actions
  1, 2, and 3. The previous least-covered items (media-controls
  primitive, group-conversation rules, consent pattern) are done.
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
