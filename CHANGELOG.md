# Changelog

All notable changes are recorded here. Format: newest first, grouped by
version, with Added, Changed, and Fixed sections where they apply.

## [Unreleased]

### Added

- Patterns catalogue: new Automated-to-human support handoff row
  in `catalog/patterns.md` — handoff triggers for an explicit
  request, repeated unhelpful answers, and steps needing authority
  automated help does not hold, a saved case carrying the stated
  issue, steps already tried, and details already given so nothing
  is re-asked, a plain statement of queue position and waiting
  route, and a stated next step where no person is available
  instead of a pretended transfer.

- Patterns catalogue: new Subscription plan change row in
  `catalog/patterns.md` — a before-and-after comparison of price,
  entitlements, billing period, and effective date shown before
  confirmation, upgrades taking effect at once with the prorated
  charge stated, downgrades taking effect at the next renewal with
  the higher tier kept until then, a named loss where a downgrade
  removes an entitlement in use, and a cancellable pending
  downgrade.

- Patterns catalogue: new Promo-code entry row in
  `catalog/patterns.md` — a collapsed entry keeping checkout
  uncluttered, the discount shown at once as a line item beside the
  recalculated total, a named failure reason (expired, already
  used, below the qualifying spend, not matching the items, or
  unable to combine) instead of a bare rejection, a stated
  one-code limit, and a one-action removal restoring the total.

- Patterns catalogue: new Kanban board row in
  `catalog/patterns.md` — stage columns mirroring the real stages
  of the work, a visible work-in-progress limit with a plain
  warning when passed, drag plus keyboard or menu move controls
  with undo, lane grouping for blocked or urgent work, scannable
  cards with detail one step away, and collapsed columns that
  keep their counts visible on narrow screens.

- Patterns catalogue: new Age verification gate row in
  `catalog/patterns.md` — a gate stating the age requirement and
  why it applies before asking anything, asking only for the
  threshold where that suffices rather than fuller details by
  default, a neutral gate with nothing pre-selected, a plain
  decline route leading somewhere useful, plain statements of
  each outcome, and a remembered answer only where appropriate.

- Patterns catalogue: new Limited-time offer countdown row in
  `catalog/patterns.md` — a countdown shown beside the exact end
  date, time, and zone, tied to one real deadline that never resets
  on revisit, a plain statement of what happens when the time runs
  out, offer terms reachable from the countdown itself, and live
  updates announced at most once a minute, with a static end
  statement preferred for assistive technology.

- Patterns catalogue: new Swipe-to-reveal actions row in
  `catalog/patterns.md` — a partial swipe revealing at most two or
  three named actions beside a list row, a full swipe committing
  only a non-destructive primary action, every action also
  reachable without a gesture, an undo offer after a destructive
  action, and direction locking so scrolling never reveals actions
  by accident.

- Patterns catalogue: new Poll row in
  `catalog/patterns.md` — a stated single- or multiple-choice rule with a
  pick limit, an immediate confirmation marked in words, results held
  until voting or closing where early results would bias later votes,
  live results shown in text as well as bar length, a stated anonymous
  or named vote with change-before-close replacing the earlier vote,
  a stated close time, and closed polls kept readable but no longer
  votable.

- Patterns catalogue: new Message edit and delete row in
  `catalog/patterns.md` — editing from the message itself with a
  visible editing state and an edited marker in words, a plain
  statement where a correction changes the meaning, confirmation
  before deleting with a stated scope for one person or for
  everyone, a deletion placeholder so the thread still reads
  coherently, and attachments following the same scope as the
  text.

- Patterns catalogue: new Live broadcast chat overlay row in
  `catalog/patterns.md` — a small number of recent messages with a
  short display time over a moving picture, high-contrast text with
  a backing tested on light and dark scenes, sender names
  distinguishable in text or shape as well as colour, clearance
  from captions and other on-screen controls, a one-action hide
  control, never showing private messages, moderator notes, or
  messages held for review, and a highlighted message shown one at
  a time for a few seconds.

- Patterns catalogue: new Pinned message row in
  `catalog/patterns.md` — pinning from the message itself, a stated
  shared or personal scope, a banner at the top of the conversation
  with sender, time, and preview that jumps to the original message,
  confirmation before replacing a shared pin, one-action unpinning,
  a stated limit where several pins are allowed, and a distinction
  from saved items.

- Patterns catalogue: new Message reaction row in
  `catalog/patterns.md` — a reaction bar opened from the message
  itself, a small fixed quick set with a full picker behind an add
  control, tap-to-remove and tap-to-replace with at most one
  reaction per person per message, a grouped reaction cluster that
  opens a reactors list, and keyboard operation with reactions
  labelled in words.

- Patterns catalogue: new Voice message row in
  `catalog/patterns.md` — a stated send gesture for held versus
  locked recording, pause and resume while recording, listen
  before sending with discard beside send, the waveform as the
  scrub control with played and unplayed portions distinct in
  shape or text as well as colour, speed choices, resume from
  the last listened position, and a transcript offered as a text
  alternative beside the player.

- Patterns catalogue: new Code scanner row in
  `catalog/patterns.md` — a viewfinder frame guide with a dimmed
  surround, in-place highlight of the detected code, immediate
  visual plus sound or vibration confirmation, a result preview
  with a confirm control before any action is taken, a
  scan-again control, failure guidance naming distance, angle,
  light, or flash, and an image-from-library route where camera
  access is refused or unavailable.

- Patterns catalogue: new Time picker, Verification-code entry,
  and Background-task progress rows in `catalog/patterns.md`,
  completing roadmap actions 78, 79, and 80 — typed entry beside a
  visual picker with a stated format and zone context; a single code
  field accepting paste and autofill with a stated expiry and resend
  route; and a task list with named states, pause and cancel where
  safe, and completion or failure reported in place.

- Roadmap: three new improvement actions (85–87) — poll and voting,
  age verification gate, and limited-time offer countdown — with
  actions 78, 79, and 80 marked implemented; coverage matrix updated
  with the three new rows.

- Resources: 3 new source records (331 total): time picker
  component guidance, verification-code input guidance, and
  background-task progress guidance.

- Patterns catalogue: new Order tracking row in
  `catalog/patterns.md`, completing roadmap action 81 — named
  stages from placement to delivery, a stated delivery window
  with a revised window and reason where delayed, updates at
  every stage that changes expectations, separately labelled
  stages for split shipments, and a support route attached to
  delays and failed deliveries with order details carried over.

- Roadmap: four new improvement actions (81–84) — order
  tracking, automated-to-human support handoff, subscription
  plan change, and promo-code entry — with action 81 marked
  implemented; coverage matrix updated with the new row.

- Resources: 4 new source records (328 total): order tracking
  page guidance, automated-to-human support handoff, promo-code
  entry, and subscription plan change proration.

- Patterns catalogue: new Colour picker, Guest-to-account
  conversion, and Sensitive-content preview rows in
  `catalog/patterns.md`, completing roadmap actions 75, 76, and
  77 — named swatches with a stated text value, a
  keyboard-operable picker with typed entry, and a contrast check
  against the target surface; a single optional post-purchase step
  that carries a guest order into a new account without re-asking
  for details; and a plain preview stating content kind and reason
  with an explicit reveal control and a per-type remembered choice.

- Roadmap: three new improvement actions (78–80) — time picker,
  verification-code entry, and background-task progress — with
  actions 75, 76, and 77 marked implemented; coverage matrix updated
  with the three new rows.

- Resources: 3 new source records (324 total): accessibility colour
  tools, guest checkout conversion, and sensitive content warnings.

- Patterns catalogue: new Print-friendly view row in `catalog/patterns.md` — a reading view that removes navigation, banners, and interactive controls before printing, states the page count before printing, keeps headings with their content, repeats table headers on each printed page, wraps wide tables, prints link destinations in text, and keeps charts readable without colour alone.

- Resources: 1 new source record (321 total): printable websites checklist.

- Patterns catalogue: new Picture-in-picture row in `catalog/patterns.md` — a floating video window that keeps playing while the person does another task, with tap-to-reveal play/pause, restore, and close controls, drag-to-move, edge stash, pinch resize, and dismissal that stops playback, keeping playback state identical across sizes.

- Resources: 1 new source record (320 total): picture-in-picture interaction guidance.

- Patterns catalogue: new External-link departure, Described media,
  and Saved-cart recovery rows in `catalog/patterns.md`, completing
  roadmap actions 69, 70, and 71 — departure notices that state the
  destination, that it opens elsewhere, and what happens to
  unfinished work, with a return route; a description track offered
  as a named choice beside captions, kept separate from dialogue,
  with a plain statement where none exists; and saved-cart recovery
  that states availability, price, and expiry changes before
  checkout, with one-action removal and no silent drops or swaps.

- Roadmap: three new improvement actions (75–77) — colour picker,
  guest-to-account conversion, and sensitive-content preview — with
  actions 69, 70, and 71 marked implemented; coverage matrix updated
  with all three new pattern rows.

- Resources: 2 new source records (319 total): accessible video
  player practices including description tracks, and external-link
  departure guidance.

- Primitives catalogue: new Image crop editor row in `catalog/primitives.md` — ratio presets with a locked ratio while resizing, a keyboard path with nudge controls, a live preview before commit, the original kept unchanged until commit, and a reset to the original frame.

- Resources: 1 new source record (317 total): accessible image crop editor controls.

- Patterns catalogue: Search results row in `catalog/patterns.md`
  deepened with applied-filter chip overflow rules — a horizontally
  scrollable chip row or a single expandable chip for the excess, a
  visible reset control, and stable chip order on selection.

- Resources: 1 new source record (316 total): filter chip overflow
  handling.

- Patterns catalogue: new What's-new announcement and Version
  history and restore rows in `catalog/patterns.md`, completing
  roadmap actions 37 and 14 — announcement visibility graded by
  impact with a persistent entry point and a seen state so a dismissed
  announcement is never shown again, and version history with
  session-folded entries, milestone entries, a compare preview, and a
  restore that saves the current version first. The announcement row
  also resolves the cross-reference already present in the in-app
  update prompt row.

- Layouts: mobile navigation deepened in `layouts/mobile-nav.md` —
  badge semantics (count only where the number matters, capped
  counts, cleared on opening), per-tab back stacks with tap-to-root,
  and deep-entry landing with the owning tab selected and a plain
  fallback where linked content is unavailable.

- Roadmap: three new improvement actions (72–74) — home-screen
  widget, deep-link landing, and progressive disclosure — with
  actions 14 and 37 marked implemented; coverage matrix updated with
  both new pattern rows.

- Resources: 3 new source records (315 total): announcement
  visibility guidance, in-app update announcement channels, and
  version history management.

- Trends: new System-initiated surfaces section in
  `trends/2026/agentic-ux.md` — the system proposes, prepares,
  and reports back while the person confirms, redirects, or
  dismisses; interruption only when worth it, queued proposals
  during work in progress, dismissal that quiets a proposal
  class, and a visible history of proposals and outcomes.

- Resources: 1 new source record (312 total): interface
  architectures replacing the single conversational surface.

- Patterns catalogue: new Carousel, Passkey sign-in, and
  Low-bandwidth mode rows in `catalog/patterns.md`, completing
  roadmap actions 66, 67, and 68 — carousel with named
  slide-picker controls, a stated position, a visible pause
  control that stops on focus or hover and never restarts after
  a deliberate pause, and a stopped start where reduced motion
  is preferred; passkey sign-in with a visible fallback route, a
  plain explanation before the device prompt, cross-device
  context stated before any code is shown, and a recovery path
  for a lost device; low-bandwidth mode as a person-controlled
  choice with a plain statement of what changes, visible content
  first, and a one-action return to the full view.

- Roadmap: three new improvement actions (69–71) — external-link
  departure, described media, and saved-cart recovery — with
  actions 66, 67, and 68 marked implemented.

- Resources: 1 new source record (311 total): carousel pattern
  with previous and next controls.

- Patterns catalogue: new Accordion disclosure row in
  `catalog/patterns.md` — one heading button per section with
  the expanded or collapsed state stated in text as well as in
  shape, focus kept on the header when toggling, sections
  opening independently unless a one-open rule is stated up
  front, a single reveal kept as a simple disclosure and peer
  sections kept as tabs, and never the only route to a task
  hidden inside a collapsed panel. Completes roadmap action 65.

- Roadmap: four new improvement actions (65–68) — accordion
  disclosure, carousel, passkey sign-in, and low-bandwidth
  mode — ordered by coverage impact, with action 60 marked
  implemented to match its existing List reorder row.

- Resources: 3 new source records (310 total): accessible
  accordion and disclosure sections, accessible auto-rotating
  carousels and sliders, and designing for limited data plans
  and slow connections.

- Patterns catalogue: faceted-filter accessibility rules added to
  the Filtering and sorting row in `catalog/patterns.md` — group
  each facet's options under a named group, name each chip's remove
  control for the filter it removes, and announce the new result
  count as a status message without moving focus.

- Resources: 1 new source record (307 total): accessible faceted
  search and filter chips.

- Patterns catalogue: new Toast feedback row in
  `catalog/patterns.md` — one short line naming what completed,
  one consistent placement, duration scaled to message length, a
  manual dismiss control with the timer paused on focus or hover, a
  polite announcement without moving focus, one toast at a time,
  and never for errors, failures, decisions, or promotion.
  Completes roadmap action 59.

- Patterns catalogue: new List reorder row in
  `catalog/patterns.md` — drag with a visible drop preview plus
  move-up and move-down controls and a keyboard path for every
  item, an announced new position, a cancel path restoring the
  original order, and manual reordering disabled while the list is
  sorted by another attribute. Completes roadmap action 60.

- Patterns catalogue: new Date-range picker row in
  `catalog/patterns.md` — one linked span with a hover preview as
  the span forms, presets setting both ends in one action, two
  months side by side on wide screens, end-before-start prevented
  or swapped with a plain statement, a stated inclusion rule for
  both ends, and the chosen span stated in plain words before it
  applies. Completes roadmap action 61.

- Resources: 3 new source records (306 total): toast feedback
  guidance, accessible drag-and-drop without dragging, and date
  picker design for enterprise use.

- Conversational interfaces trend: answer-shape menu rules in the
  Rendered interface answers section — fix one shape per intent
  (comparison, diagram, map, calculator, plain text) and keep every
  answer inside that menu, so answers stay consistent instead of each
  inventing its own shape, plus a control to show fewer visuals.

- Resources: 1 new source record (303 total): answer-shape menu
  guidance for composed conversational answers.

- Patterns catalogue: new Image gallery viewer row in
  `catalog/patterns.md` — thumbnails that name what each selects
  with the active thumbnail marked as current in text as well as
  in shape, focus returned to the opening thumbnail on close,
  viewer controls reachable without horizontal scrolling at high
  magnification, and an inline magnifier offered as an alternative
  to a separate viewer layer. Cross-checks the modal dialog row.

- Resources: 1 new source record (302 total): product image
  gallery zoom accessibility guidance.


- Patterns catalogue: new Collaborative editing presence row in
  `catalog/patterns.md` — a presence list naming each person in
  text as well as in colour, a visible hold on the field being
  edited, a warning rather than a silent overwrite on collision,
  and presence kept separate from read and approval signals.
  Completes roadmap action 10.

- Patterns catalogue: new Draft autosave and recovery row in
  `catalog/patterns.md` — continuous saving with a visible
  last-saved indicator, restore after interruption with a clear
  review step, draft and delivery states kept separate, an
  explicit discard path, and a stated scope and retention period.
  Completes roadmap action 11.

- Patterns catalogue: new Saved-filter view row in
  `catalog/patterns.md` — a named view storing a filter
  combination as a definition that stays current, rename and
  delete controls, a stated private or shared scope, a visible
  marker with a repair step when the view no longer matches the
  data, and a stated rule keeping query text out unless chosen.
  Completes roadmap action 13.

- Resources: 3 new source records (301 total): presence as a
  short-lived session claim rather than proof of attention,
  form drafts that survive navigation without implying delivery,
  and saved views as reusable filter combinations.

- Patterns catalogue: File upload row in `catalog/patterns.md` —
  accepted formats, size limit, and file-count limit stated beside
  the control before anyone chooses a file, checked before the
  upload starts with the exact limit named on failure, and
  drag-and-drop kept as an enhancement beside a visible,
  keyboard-operable browse control that always offers the same upload.

- Resources: 1 new source record (298 total): accessible file
  upload field guidance on stating limits up front, keeping
  drag-and-drop as a bonus, and announcing attachment and failure.

- Conversational interfaces trend: live in-conversation visuals in
  `trends/2026/conversational-interfaces.md` — a visual inside a
  conversation stays manipulable in place, changing a control updates
  its linked values and explanations, selecting a part of a diagram
  swaps in that part's explanation, and a visual that cannot update
  says so and offers the same result as text or a form.

- Resources: 1 new source record (297 total): in-conversation
  interactive visuals guidance on manipulable visuals rather than
  flat pictures.

- Patterns catalogue: Wizard row in `catalog/patterns.md` — validation
  scoped to the visible step, so a required field on a hidden step
  never blocks submission silently; check each step on its own
  transition, or give each step its own form.

- Resources: 1 new source record (296 total): multi-step form
  validation guidance on hidden-step fields blocking submission.

- Commerce layout: delivery-date labelling and aided address entry in
  `layouts/ecommerce.md` — each delivery option states the date it
  arrives rather than speed alone, and address entry offers suggestions
  as the person types with validation before payment.

- Resources: 1 new source record (295 total): mass merchant checkout
  benchmark guidance on delivery-date labelling and aided address
  entry.

- Patterns catalogue: new System share sheet row in
  `catalog/patterns.md` — a preview of exactly what will be
  shared, recent targets first with a stable order, a cancel
  path that shares nothing and returns to the same place, and a
  fallback route where no share sheet exists. Completes roadmap
  action 54.

- Patterns catalogue: new Find-in-page row in
  `catalog/patterns.md` — a persistent query, a match count,
  next and previous controls, highlighted matches with the
  current match distinct in shape as well as colour, focus moved
  to the matched text, a plain no-match statement, and a
  dismiss step that returns to the previous place. Completes
  roadmap action 55.

- Resources: 3 new source records (294 total): web share
  fallback and cancellation guidance, find-in-document match
  count and navigation guidance, and find pattern guidance for
  list, table, and card views.

### Changed

- Calendar and scheduling row in `catalog/patterns.md`:
  drag-to-move and edge-resize rules — preview of the new time
  with conflicts shown before committing, undo for a move,
  keyboard or menu routes for every drag, month-view drags
  keeping the clock time, and timed resizing in day or week
  views with the dragged edge naming which end it changes.

- Search row in `catalog/patterns.md`: suggestion-panel rules —
  a small scannable set of suggestions, grouped and labelled
  where more than one content type returns, Escape closing the
  panel before it clears the query, and Enter committing the
  query as typed.

- Mobile navigation layout: a More destination rule for more
  than five top-level sections — the five most-used stay in the
  bar, the rest list under one More destination, and no
  destination is dropped silently.

- Coverage summaries in `README.md` and the roadmap matrix now
  list every layout page and the three newest pattern rows, so
  the matrix matches the actual files.

- Roadmap: actions 53–55 marked complete; actions 56–58 added
  (text-selection action menu, no-results recovery rule, and
  print-friendly view).

- Patterns catalogue: new Scrolling tab bar row in
  `catalog/patterns.md` — a single scrolling row that never
  wraps, an overflow hint and snap so no tab rests half-cut,
  the current tab marked in text as well as in shape, arrow-key
  movement with the selected tab brought fully into view, and a
  stated rule for collapsing a large set into a menu instead.
  Completes roadmap action 53.

- Resources: 1 new source record (291 total): tab design
  guidance for scrollable tab strips.

- Patterns catalogue: new Long-document navigation row in
  `catalog/patterns.md` — a heading-built section outline
  labelled as the page outline, the current section marked in
  text as well as in shape, a sticky outline on wide screens
  with a single collapsed control on narrow screens,
  focus-moving jump links, and a form-safe return to the top.
  Completes roadmap action 51.

- Patterns catalogue: new In-app update prompt row in
  `catalog/patterns.md` — a flexible prompt that downloads in
  the background and lets the person keep working, a blocking
  prompt reserved for versions that can no longer work safely,
  a stated deferral limit and deadline, no prompt during a
  task or a payment, and a chosen-moment restart with resume
  after an interrupted update. Completes roadmap action 52.

- Patterns catalogue: new Pull-to-refresh row in
  `catalog/patterns.md` — a pull gesture paired with a visible
  refresh control, a threshold cancel, the existing list kept
  visible during refresh, and a stated result (new items, no
  change, or failure with retry) with the person's place kept.
  Completes roadmap action 47.

- Roadmap: three new improvement actions (scrolling tab bar,
  system share sheet, find-in-page) and a refreshed coverage
  matrix (long-document navigation, in-app update prompt, and
  pull-to-refresh promoted to full).

- Resources: 3 new source records (290 total): pull-to-refresh
  pattern guidance, in-app update prompt design guidance, and
  table of contents and jump link guidance.

- Patterns catalogue: new Location selection row in
  `catalog/patterns.md` — choosing a place from a paired map
  and list, with detail cards carrying hours and availability,
  area refresh on request rather than on every pan, and
  location-access failures that keep area search open.
- Source record for map interface design guidance in
  resources/sources.json (287 total).

- Patterns catalogue: new Accessibility preferences row in
  `catalog/patterns.md` — text size, bold text, increased
  contrast, reduced motion, reduced transparency, and captions
  gathered in one reachable place, each applied at once to a
  live preview with no entered input lost, a stated rule for
  where a choice follows the system and where it overrides it,
  a single reset to the starting values, and a preference saved
  across visits. Completes roadmap action 50.

- Roadmap: three new improvement actions (accessibility
  preferences, long-document navigation, in-app update prompt)
  and a refreshed coverage matrix (accessibility preferences
  promoted to full).

- Resources: 3 new source records (286 total): in-app updates
  guidance, accessibility settings guidance, and table of
  contents design guidance.

- Patterns catalogue: new Guided tour row in
  `catalog/patterns.md` — one highlighted element at a time with a
  dimmed surround, a short anchored bubble, step position, back,
  next, and an always-visible skip path, shown once per feature,
  at most three steps in sequence, with the content findable
  afterwards.
- Source record for coach mark guidance in
  resources/sources.json.

- Patterns catalogue: new Modal dialog row in
  `catalog/patterns.md` — one decision per dialog, focus taken
  on opening and returned on closing, focus trapped while open,
  a visible dismiss path besides the decision actions, never a
  nested dialog, and a full-width sheet on narrow screens.
  Completes roadmap action 44.

- Patterns catalogue: new Guest checkout row in
  `catalog/patterns.md` — guest path beside sign-in, fulfilment
  details only before payment, the difference from signed-in
  checkout stated before payment, a post-purchase account offer
  carrying the order into the new account, and no forced account
  step mid-checkout. Completes roadmap action 45.

- Patterns catalogue: new Time-zone picker row in
  `catalog/patterns.md` — zones by place name with current local
  time and offset, search by place, zone name, or offset, the
  detected zone suggested at the top, clock-change behaviour
  stated plainly, and an example time shown beside the person's
  own time for confirmation. Completes roadmap action 46.

- Patterns catalogue: new Code scanning row in
  `catalog/patterns.md` — framing guide, multi-sense capture
  confirmation, result preview before acting, actionable
  failure guidance with a manual-entry route, camera stop
  rules, and large high-contrast codes with a plain-text note
  for codes shown to others.

- Patterns catalogue: Map comparison row in
  `catalog/patterns.md` strengthened — dragging is never the
  only way to pan, place a stop, or reorder a route, with
  directional pan controls, tap-to-place, address entry, and
  reorder controls, arrow-key panning, a documented focus
  exit, and accessible names on zoom, locate, and close
  controls.

- Patterns catalogue: new Profile and account menu row in
  `catalog/patterns.md` — the account's own actions only, the
  active account named in text, sign-out kept separate from
  destructive account actions, and a return to the same place
  after menu actions that do not leave the task. Completes
  roadmap action 41.

- Patterns catalogue: new Recently viewed row in
  `catalog/patterns.md` — a newest-first list with last-opened
  labels, a stated scope for what is remembered, clear-all and
  single-entry removal, an in-place notice for items that no
  longer exist, and recents kept distinct from saved items.
  Completes roadmap action 42.

- Patterns catalogue: new Invitation response row in
  `catalog/patterns.md` — accept, decline, and tentative
  replies with a stated effect for each, reply changes that
  update organiser and attendees without a duplicate item,
  proposed times kept unconfirmed until accepted, and
  withdrawn or expired invitations stated plainly with no
  reply actions. Completes roadmap action 43.

- Roadmap: three new improvement actions (modal dialog, guest
  checkout, time-zone picker) and a refreshed coverage matrix
  (profile and account menu, recently viewed, and invitation
  response promoted to full).

- Resources: 3 new source records (276 total): profile menu
  guidance, recently viewed pattern guidance, and meeting
  invitation response guidance.

- Patterns catalogue: filtering and sorting rule in
  `catalog/patterns.md` — within one facet, selecting several
  options widens the result, while selections across facets
  narrow it, with that combination stated plainly where it
  is not obvious; long facet lists offer a search field
  inside the facet instead of a full scroll.

- Patterns catalogue: new Activity feed row in
  `catalog/patterns.md` — a chronological history presented
  as a list with item count and position for assistive
  technology, grouping carried in structure or text rather
  than spacing or a connecting line alone, plain timestamps
  and type cues for scanning, load-more announcements that
  state how many entries were added while keeping the
  person's place, and in-place expansion for detail.

- Patterns catalogue: new Breadcrumb navigation row in
  `catalog/patterns.md` — a trail from the home view to the
  current page, each step a working link except the current
  page marked as current in text, middle steps collapsed
  into an overflow control on narrow screens that keeps the
  home view and the parent step reachable, and an omission
  rule for single-level pages and task flows. Completes
  roadmap action 38.

- Patterns catalogue: new Annotation and comment thread row
  in `catalog/patterns.md` — threads anchored to the specific
  section, sentence, or element they discuss, nested replies,
  thread visibility following the visibility of the content,
  resolve hiding a thread without deleting it, reopen
  restoring it with its history, an overview of open and
  resolved threads, and an outdated-anchor rule that keeps
  the quoted original text rather than silently deleting the
  discussion. Completes roadmap action 36.

- Patterns catalogue: new Theme selection row in
  `catalog/patterns.md` — light, dark, and system-following
  choices with an immediate undoable preview that loses no
  entered input, a saved preference that survives visits and
  keeps overriding the system theme, a system-following
  choice that applies system changes at once, and contrast
  checked in every theme. Completes roadmap action 40.

- Roadmap: three new improvement actions (profile and
  account menu, recently viewed, invitation response) and a
  refreshed coverage matrix (breadcrumb navigation,
  annotation and comment thread, and theme selection
  promoted to full).

- Resources: 4 new source records (271 total): breadcrumb
  navigation guidance (two records), discussion comments
  guidance, and dark-mode toggle guidance.

- Patterns catalogue: expanded Filtering and sorting row in
  `catalog/patterns.md` — compact-screen faceted search rules:
  sticky filter control with an active count and sort kept
  separate, bottom sheet for a few facets and a full-screen
  panel for long facet lists, deferred apply with a live result
  count, facet counts recalculated after each selection and
  built only from currently obtainable items, applied filters
  kept visible as removable chips, whole labels tappable at
  the standard target size, typed or preset range inputs
  beside sliders, and swatches for colour choices.

- Resources: 2 new source records (267 total): mobile
  faceted search guidance and faceted search best practices.

- Patterns catalogue: new Content reporting and blocking row in
  `catalog/patterns.md` — report from the item itself with a
  plain reason choice, immediate hide for the reporter, a stated
  outcome and check-back place, blocking that hides the blocked
  party everywhere at once without revealing the reporter, a
  blocked list with unblock, and a review path for a decision in
  error. Completes roadmap action 32.

- Patterns catalogue: new Language and locale selection row in
  `catalog/patterns.md` — language names in their own language,
  no flag standing for a language, stated current-session or
  saved-preference scope, same-page switch with entered input
  and drafts kept, immediate undoable preview, and item-by-item
  fallback that never strands the person on an unreadable page.
  Completes roadmap action 33.

- Patterns catalogue: new Scheduled action row in
  `catalog/patterns.md` — plain-words scheduled time with zone
  where it matters, a returnable scheduled list, edit and cancel
  until the run with content and time edits kept independent, a
  single confirmation once the action runs, and missed or failed
  runs reported with cause and a retry path rather than silently
  dropped. Completes roadmap action 34.

- Roadmap: three new improvement actions (breadcrumb
  navigation, account recovery, theme selection) and a refreshed
  coverage matrix (content reporting and blocking, language and
  locale selection, and scheduled action promoted to full).

- Resources: 3 new source records (265 total): content
  reporting and blocking guidance, language selector design
  guidance, and scheduled message editing guidance.

- Patterns catalogue: new Account switcher row in
  `catalog/patterns.md` — the trigger always names the active
  account in text, the list marks the active account in text
  as well as in shape, a switch keeps the person in the same
  place where that place exists for the new account, data,
  drafts, and settings never carry across a switch unless
  moved explicitly, signed-in accounts stay signed in after a
  switch, and signing out of one account never signs out of
  the others unless chosen explicitly.

- Resources: 1 new source record (262 total): account and
  app switcher guidance.

- Patterns catalogue: new Payment failure recovery row in
  `catalog/patterns.md` — a failed payment keeps the person in
  the same checkout with the order intact, states the failure
  in plain words with an actionable cause where known, offers
  a retry only where it can succeed plus another eligible
  method on the same screen, checks the real status before
  any second attempt so one order is never charged twice,
  and holds a pending payment with a stated status check
  rather than showing failure prematurely. Completes roadmap
  action 35.

- Roadmap: three new improvement actions (payment failure
  recovery, annotation and comment threads, what's-new
  announcement) and a refreshed coverage matrix (payment
  failure recovery promoted to full).

- Resources: 3 new source records (261 total): payment
  failure recovery guidance, anchored comment thread
  guidance, and in-product update announcement guidance.

- Primitives catalogue: Switch row in `catalog/primitives.md` —
  keep the switch beside its label, never at the far edge of a wide
  row, with the switch immediately beside the label on wide desktop
  columns so label and control stay visible together under
  magnification, and label on the left with the switch on the right
  on narrow columns; never use a switch for an action that needs
  confirmation or cannot be undone.

- Resources: 1 new source record (258 total): switch placement and
  use guidance.

- Patterns catalogue: new Saved-item collection row in
  `catalog/patterns.md` — save with one action, saved state shown
  wherever the item appears, named collections with rename and
  delete controls, stated private or shared scope, and a plain
  statement when the original item changed or was removed, with
  a nearest available alternative rather than a silent drop or
  swap. Completes roadmap action 26.

- Patterns catalogue: new Bulk action row in
  `catalog/patterns.md` — stated scope (page, filtered set, or
  all matching items) before acting, confirmation summarising
  action, count, and scope with skipped items named, per-item
  failures reported separately with cause and retry path, failed
  items kept selected for retry, whole-batch undo where the
  action is reversible, and a partial success never reported as
  a full success. Completes roadmap action 27.

- Patterns catalogue: new Rating and review submission row in
  `catalog/patterns.md` — structured rating with an optional
  written review, keyboard-operable steps labelled in words,
  public and moderated parts stated before submitting, a stated
  edit window with moderation on edit, reasoned moderation
  decisions with a revise path, and no gating of core features
  behind a rating or reward for one. Completes roadmap action 28.

- Resources: 3 new source records (257 total): favourites
  pattern guidance, bulk-action scope and partial-failure
  guidance, and content review and rating guidance.

- Roadmap: three new improvement actions (content reporting and
  blocking, language and locale selection, scheduled action) and
  a refreshed coverage matrix (saved-item collection, bulk
  action, and rating and review submission promoted to full).

- Patterns catalogue: new Bypass link row in
  `catalog/patterns.md` — first-focusable link, visible on
  focus, that moves focus (not just the view) to the main
  content or to a task-specific target such as a checkout
  form, with a visible focus indicator landing on the target.

- Patterns catalogue: new Review prompt row in
  `catalog/patterns.md` — ask only after a clear success moment
  and repeated value, never on first launch, during a task, during
  payment, or after an error; use the system review prompt where
  one exists, never gate a feature behind a rating or reward one,
  suppress the prompt while a support issue is open, treat a
  suppressed prompt as a declined opportunity, and keep a quiet
  manual review route in settings or about.

- Patterns catalogue: new Inline editing row in
  `catalog/patterns.md` — single-value low-risk changes inline,
  multi-field or high-stakes edits in a dedicated surface,
  keyboard contract for entering, committing, and cancelling
  edits, validation that keeps the editor open with a named
  problem, and announced edit-mode transitions with a visible
  focus indicator on the live cell.

- Patterns catalogue: new In-product help row in
  `catalog/patterns.md` — one help entry reachable from every
  screen, suggestions following the current screen and task,
  in-place search that preserves entered input, answer-first
  single-task articles, escalation carrying task context when
  search finds nothing, and per-article feedback marking weak
  articles for rewrite.

- Patterns catalogue: new Share link row in
  `catalog/patterns.md` — access scope and expiry stated before
  sharing, named access as the default for sensitive items,
  confirmed copy state with a manual fallback on failure,
  expired or revoked links explained with a request-access path,
  and one-step revocation where access is named.

- Patterns catalogue: new Second-factor sign-in row in
  `catalog/patterns.md` — strongest method first with all methods
  listed plainly, full paste support for codes, resend timer
  stating the destination, attempt count without revealing
  failures, an always-visible single-use backup-code path,
  opt-in trusted-device choice, and enabled only after a code
  verifies successfully.

- Patterns catalogue: Offline-first sync row in
  `catalog/patterns.md` extended with two rules — derive
  the shown sync status from queue progress and real
  request outcomes rather than from a connectivity signal
  alone, and restrict optimistic display to reversible
  edits, keeping actions with lasting consequences marked
  unconfirmed until the server confirms them and never
  clearing entered input until the local copy is durable.

- Patterns catalogue: File upload row in
  `catalog/patterns.md` extended with a reuse-first rule —
  where a suitable file is already held, offer it as a
  one-step reuse choice naming the file and its source,
  with a plain decline-and-upload-different-file path and
  no silent reuse; a held file that no longer meets the
  format or recency requirements is flagged before any
  upload is requested.

- Patterns catalogue: Data table row in
  `catalog/patterns.md` extended with column customisation —
  show, hide, and reorder columns to fit the task, the choice
  persisting across sessions where repeated use is likely,
  hiding and reordering never relying on drag alone, and
  resizable columns that expose a value in full rather than
  leaving it truncated.

- Patterns catalogue: new Session-expiry warning row in
  `catalog/patterns.md` — plain time-remaining warning that stays
  visible, never blocks continued work, and is announced to
  assistive technology; a simple keep-working action that preserves
  entered input; an idle limit stated separately from an absolute
  limit that activity cannot extend; entered input saved before
  expiry and restored on return to the same place or to a saved
  draft with a clear restore step. Completes roadmap action 23.

- Patterns catalogue: new Data export row in
  `catalog/patterns.md` — common formats the person can actually
  open elsewhere, includes and excludes stated before starting,
  real progress with named stages and a stated download-link
  lifetime, background running with a status check where leaving
  does not cancel the export, and a partial failure that names
  what exported and what did not with a retry for the missing part
  only, never a silent short file. Completes roadmap action 24.

- Patterns catalogue: new Account deletion row in
  `catalog/patterns.md` — deletion from the same channel used to
  sign up, effect stated before confirmation including what is
  kept and why, an export offered before deletion starts,
  sign-out everywhere on request, a stated grace period with a
  plain undo path that restores the account whole, and written
  confirmation once removal completes. Completes roadmap action 25.

- Resources: 4 new source records (245 total): session-timeout
  data-loss guidance, session-timeout warning guidance, transfer
  progress and partial-result guidance, and account-deletion
  grace-period guidance.

- Patterns catalogue: expanded Paywall and upgrade prompt row in
  `catalog/patterns.md` — explicit trial offer statement (whether a
  trial is included, its length, the price that follows, and the
  first charge date), trial choice kept separate from purchase
  confirmation so changing a trial cannot silently commit the person
  to an auto-renewing charge, a visible trial timeline with a
  reminder before the first charge, and a side-by-side plan
  comparison in the same price units with the total for the billing
  period. New source record (241 total): paywall trial-offer
  guidance.

- Patterns catalogue: expanded Data visualisation row in
  `catalog/patterns.md` — point-by-point chart explorer mode entered
  from the plot area, with arrow-key movement between neighbouring
  data points, keyboard-reachable legend selection, zoom, and search,
  the focused region kept visible when zoomed, and movement geometry
  following the chart type (free for scatter plots and maps, along
  one axis and within series for line, area, and stacked charts,
  along the horizontal axis only for waterfall, small-multiple, and
  grouped-column charts). New source record (240 total): keyboard
  chart-explorer guidance.

- Patterns catalogue: new Conversation branching row in
  `catalog/patterns.md` — branching from any message with the
  original thread preserved, intent labels and a branch list or tree,
  editing or re-requesting creates a branch instead of overwriting
  history, one-at-a-time walking with side-by-side comparison before
  carrying content across, and archiving for stalled branches. New
  source record (239 total): conversation branching guidance.

- Patterns catalogue: new Install prompt row in
  `catalog/patterns.md` — offer installation of a web app only after
  engagement (a completed task or a return visit), never on first
  load, on exit, or repeatedly after a dismissal; a dismissal stays
  dismissed with a quiet persistent route kept instead, the concrete
  benefit stated beside a single primary action, manual steps where
  the platform offers no prompt event, and success confirmed with the
  prompt hidden once installed. New source record (238 total):
  progressive web app install-prompt guidance.

- Patterns catalogue: new Undo and trash recovery row in
  `catalog/patterns.md` — an immediate undo offer after every
  destructive action restoring the item to its original place, undo
  alone for easily repeated actions, confirmation plus the trash
  safety net for wider effects, a stated retention period that is
  never silently shortened, parent-child restore rules, and a
  separate permanent-delete step stating exactly what is lost.
  Completes roadmap action 16. Cross-zone scheduling rules added to
  the Calendar and scheduling row — organiser and attendee zones
  stated where they differ, ambiguous or repeated times around zone
  transitions flagged before booking, recurring events pinned to a
  named zone with a preview of local-time changes across transitions,
  and edit scope stated as series zone or local zone. Completes
  roadmap action 17. Tablet layout: multitasking and split-window
  rules in `layouts/tablet.md` — a stated primary pane, lossless
  drag between panes, resize as a continuity event, saved app pairs,
  and an upfront statement when an app cannot run in a pane.
  Completes roadmap action 18. Roadmap actions 23-25 added for the
  next cycles: session-expiry warning, data export, and account
  deletion. New source records (237 total): reversible-action
  recovery guidance, cross-timezone scheduling guidance, and tablet
  split-screen guidance.

- Patterns catalogue: data-table sort-state rules in
  `catalog/patterns.md` — an unsorted column shows a neutral
  indicator distinct from ascending and descending, the current
  direction is visible in the header and announced to assistive
  technology, multi-column sort states its column order and uses a
  unique field as the final tie-breaker so paging stays stable,
  sorting moves to the server once the set exceeds what the client
  can sort without lag, and the sort survives paging and filtering.
  Completes roadmap action 19. New source records (234 total):
  data-table design guidance, accessible form validation and error
  recovery, contextual onboarding guidance, and empty-state design.
  Roadmap actions 20-22 added for the next cycles: form validation
  timing, contextual guidance, and an empty-state static fallback.

- Conversational interfaces trend: voice correction and reconnect
  rules in `trends/2026/conversational-interfaces.md` — a genuine
  correction cancels any pending action and is kept as the current
  instruction with the old answer never resumed, playback after a
  dropped connection is treated as unknown unless a receipt proves
  it, and a reconnected request is reconciled before retrying so it
  never takes effect twice. New source record (230 total): voice
  turn-taking and recovery guidance.

- Authentication layout: biometric sign-in rules in `layouts/auth.md` —
  offer biometric sign-in only after a first successful sign-in rather
  than during registration, treat the operating-system prompt as owned
  by the system, show the option only where the device can use it,
  always keep a password or PIN fallback visible, treat dismissal as a
  return rather than an error, and state the plain cause with a retry
  on genuine failure. New source record (229 total): biometric
  authentication sign-in guidance.

- Patterns catalogue: new Keyboard shortcut reference row in
  `catalog/patterns.md` — a searchable, context-grouped reference
  reachable from help, searchable by action name and by key, with
  single-character shortcuts limited to the focused component and
  always turn-off or remappable, remapping with a conflict warning
  naming the displaced action and confirmation before replacement, a
  per-group or full reset, changes that apply at once and persist,
  and no shortcut ever being the only route to an action.
  Completes roadmap action 15. New source record
  (228 total): keyboard shortcut guidance.

- Patterns catalogue: new Multi-device handoff row in
  `catalog/patterns.md` — continue a task on another device from an
  explicit resume point offered as a one-tap suggestion, never an
  automatic takeover, resuming at the exact screen and state, stating
  plainly what transferred and what did not, falling back to a
  browser view where the receiving device lacks the app, and
  resolving both-devices-edited conflicts with the sync-conflict
  rules. Completes roadmap action 9. New source record
  (227 total): cross-device task handoff research.

- Patterns catalogue: new Subscription cancellation row in
  `catalog/patterns.md` — cancel in the same channel used to sign up
  with a plain label reachable from billing or account settings, the
  effect stated before confirmation (what ends, when access ends, what
  happens to saved content, next billing date), pause or a cheaper
  plan offered beside cancellation rather than as a gate, plain
  parallel confirmation wording, written confirmation with a resume
  path kept visible until access ends, and no slower-channel
  requirement when sign-up was self-serve. New source record
  (226 total): cancellation-flow research on transparent versus
  obstructive exit paths.

- Settings layout: scope and save-lifecycle rule in
  `layouts/settings.md` — each setting states whether it applies to
  the account everywhere, the current device, the current workspace,
  or a single project, scopes are never mixed inside one group
  without a label, a change affecting other people is stated before
  it is applied, and the change lifecycle is shown plainly as
  pending, confirmed, or failed with a retry that keeps entered
  values. New source record (225 total): settings page design
  guidance.

- Patterns catalogue: new Notification digest row in
  `catalog/patterns.md` — low-urgency updates grouped by thread, type,
  or time window into a scheduled summary with a period label, every
  item individually openable with per-item read state, a person-
  controlled daily, weekly, or no-digest schedule, and a rule never to
  digest a critical or time-sensitive item. Completes roadmap action 12.
  New source record (224 total): notification batching and digest
  strategies.

- Patterns catalogue: new Personalized-content disclosure row in
  `catalog/patterns.md` — when order, content, or recommendations adapt
  to the person, the driving signal is stated in plain words at the
  point of adaptation, the unadapted view is offered beside the adapted
  one, and the adaptation is reversible by changing the signal or
  turning it off, with what cannot be changed stated plainly. Completes
  roadmap action 6. New source record (224 total): transparency and
  control in adapted content.

- Patterns catalogue: new Calendar and scheduling row in
  `catalog/patterns.md` — time scale chosen by planning question with
  context preserved across switches, calendar kept distinct from a date
  picker, predictable day-click effect, distinct available, pending,
  booked, and unavailable slot states, context kept with a nearest
  alternative when a slot becomes unavailable, inspectable recurrence
  rule with stated edit scope, and per-event timezone labels. New source
  record (224 total): user-centred scheduling interface guidance.

- Roadmap: three new improvement actions (saved-filter view, version
  history and restore, keyboard shortcut reference) and a refreshed
  coverage matrix (notification digest, personalized-content
  disclosure, and calendar and scheduling promoted to full).

- Television layout: dual-input focus rule in `layouts/tv.md` — when
  pointer and directional input coexist, pointer movement highlights
  the element under the pointer without erasing the stored directional
  focus, scroll containers and overlays respond to both input modes,
  and returning to directional buttons resumes from the stored focus.
  New source record (221 total).

- Watch layout: staged disclosure for sensitive notifications in
  `layouts/watch.md` — a generic alert first, with the detail revealed
  only after a deliberate action such as a tap; a wrist raise alone
  never reveals sensitive detail, and the ambient, always-on variant
  never shows it either. New source record (220 total).

- Patterns catalogue: new Sync-conflict resolution row in
  `catalog/patterns.md` — side-by-side versions with differing fields
  highlighted, field-by-field merge with a merged preview as the exact
  result to be saved, sensitive fields always asking, deletion-versus-
  edit treated as a conflict, and the local copy kept safe until
  resolved. Completes roadmap action 7. New source record
  (219 total): offline-first conflict resolution guidance.

- Primitives catalogue: new Multimodal input-bar row in
  `catalog/primitives.md` — one bar for text, voice, and media entry,
  a hint naming all three modes, waveform while listening, editable
  transcript before sending, thumbnails with remove and zoom, named
  processing steps, and keyboard and screen-reader parity for every
  mode. Completes roadmap action 5. New source record (219 total):
  multimodal input user-experience guidance.

- "Voice command discovery" section in
  `trends/2026/conversational-interfaces.md` — suggested prompts on
  first use as editable chips, screen-specific example utterances, a
  browsable and searchable capability list, teaching inside replies,
  progressive introduction, and recovery suggestions after a failed
  understanding. Completes roadmap action 8. New source record
  (219 total): voice interface discoverability guidance.

- Roadmap: three new improvement actions (collaborative editing
  presence, draft autosave and recovery, notification digest) and a
  refreshed coverage matrix (sync-conflict resolution promoted to
  full).

- Watch layout: composable glance tiles and a persistent
  live-activity anchor in `layouts/watch.md` — small fixed-size tiles
  (for example 2×1 or 2×2) instead of one full-screen card per datum,
  each tile keeping one datum and one action at full touch-target
  size, and one ongoing-activity tracker anchored at the bottom of
  the face layer and the top of the notification list. New source
  record (216 total).

- Patterns catalogue: new Agent checkpoint row in
  `catalog/patterns.md` — the delegate–monitor–approve–interrupt–
  refine loop, checkpoints that pause execution before irreversible
  actions, approval cards showing the exact payload (recipient,
  change, amount, tool) with approve, edit, or reject decisions, a
  stated autonomy budget for low-stakes reversible actions, recovery
  from a plausible but wrong route, and a decision record.
  Completes roadmap action 1. New source records (215 total):
  human-in-the-loop approval patterns and checkpoint placements.

- "Voice hybrid flows" section in
  `trends/2026/conversational-interfaces.md` — voice-to-initiate
  with physical (tap or biometric) confirmation for sensitive
  actions, visual mishearing repair showing what was heard with
  tappable correction of low-confidence words, confirmation graded
  by stakes, and screen fallback after repeated failures.
  Completes roadmap action 2.

- Container-query responsiveness guidance in `layouts/desktop.md` —
  components adapt to their container's size rather than only the
  viewport, with named containers, verification in full-page,
  sidebar, modal, and dense-dashboard grid contexts, and the size-
  containment caveat. Completes roadmap action 3.

- Primitives catalogue: new "Kinetic type" row in `catalog/primitives.md`
  — text animated through variable-font axes or motion driven by scroll,
  interaction, or state; motion as punctuation for headlines and moments
  only, static-first design with reduced-motion fallback, whole-word
  screen-reader announcements, transform-and-opacity-only animation, and
  a pause or stop control on any looping motion. New source record
  (210 total).

- Patterns catalogue: new machine-composed content disclosure pattern row
  in `catalog/patterns.md` — every system-composed block labelled as
  composed, uncertainty and grounding stated plainly, a visible correction
  path and override control, and an explicit approval step for composed
  decisions with effects outside the screen; cross-checked against the
  trust patterns in `trends/2026/agentic-ux.md` and the disclosure rules
  in `trends/2026/conversational-interfaces.md`. Completes roadmap
  action 4 (added this run). 6 new source records (209 total): agent
  checkpoint design, agentic human-in-the-loop controls, multimodal input
  feedback, voice surface modes, and two late-October 2026 trend roundups.

- "Step trace and tool output" section in `trends/2026/agentic-ux.md`:
  a structured step list for agent runs — one line per step with icon,
  title, optional description, and status; running/error/pending statuses
  with a shimmer while a step runs; expandable and nested lines; links or
  dialog/sheet/drawer/popover detail on demand; keyboard and screen-reader
  support on every expandable line — plus a dedicated code block for
  technical output with a titled action header, line numbers, wrapping,
  diff styling, highlighted lines, and a small size inside traces. No new
  source record (source already recorded 2026-10-21).

- "Accessibility gate for generated interfaces" section in
  `trends/2026/agentic-ux.md`: a release-day accessibility pass for
  agent-rendered markup — freeze before measuring, automated scan first
  then keyboard-only and screen-reader manual checks, explicit WCAG 2.2
  checks (focus never hidden by sticky layers, single-pointer drag
  alternatives, 24 px targets, consistent help, no redundant entry,
  memory-free authentication), native elements over patched-up roles,
  recorded residual risk with an owner, and re-run on every regeneration.
  New source record (203 total).

- Media controls and Haptic feedback primitive rows in
  `catalog/primitives.md`: the transport control set in one reading
  order with 100 ms response confirmation, full keyboard operation,
  captions always available, no auto-playing sound, volume memory that
  never reopens at full; confirm/alert/error haptic intensities always
  paired with a visual or spoken signal, a clear user disable, reduced-
  motion honouring, no loops. Completes roadmap actions 1 and 5. New source
  records.

- Group-conversation rules in the chat and messaging pattern row of
  `catalog/patterns.md`: per-participant read indicators marking each
  person's latest read message in place, collapsible reply threading,
  honest presence states, mentions that notify only the named people
  with name suggestion after the trigger — cross-checked against
  `trends/2026/conversational-interfaces.md`. Completes roadmap
  action 2.

- Granular consent pattern row in `catalog/patterns.md`: per-category
  toggles never pre-checked with one-sentence consequences,
  just-in-time disclosure naming the specific purpose, frictionless
  revocation with immediate effect, an audit trail of decisions —
  cross-checked against the consent signals in
  `trends/2026/machine-experience.md`. Completes roadmap action 3.
  New source records.

- Contrast-verification routine in `trends/2026/dark-mode.md`: test
  every text/background pair against both token sets, verify muted and
  disabled text at its used size, define forced-colours-mode behaviour
  with opaque fallbacks for elevation steps, place text over
  photography on scrims tested against worst-case brightness, and
  re-check whenever a new surface or accent is added. Completes
  roadmap action 4.

- Research-driven additions from the deep review: Ask/Infer/Defer/
  Confirm form-collection rules and the low-risk-only boundary for
  smart defaults in the Form flow row of `catalog/patterns.md`;
  unknown-outcome error group, restricted-message and failure-copy
  rules in `catalog/states.md` (verify-before-retry, never reuse the
  zero-item message for a load failure, restricted messages never
  imply a workaround); September 2026 WCAG 3.0 draft structure in
  `trends/2026/standards-outlook.md` (one conformance level, six
  reporting tiers, four impact tags); spatial interaction ergonomics
  in `trends/2026/spatial-interfaces.md` (gaze targeting with
  intent-confirming hover, lap-level micro-gestures, positional audio
  anchors). 8 new source records (202 total).

- Material-meaning rule in `catalog/primitives.md`: material qualities must
  carry meaning rather than decorate — a reflective surface suggests
  importance, a soft surface approachability, a firm high-contrast control
  stability or authority; affordances stay legible so users can tell what
  they can tap, drag, open, or change. Reflects an October 2026
  design-direction review. New source record.

- Payment-method selection rule in `layouts/ecommerce.md`: a tiled grid for
  four or fewer methods (each tile shows the method's mark and label at a
  glance), a vertical list once the count exceeds four — reflecting an
  October 2026 platform-level rollout that switched payment layouts
  automatically by method count. New source record.

- Runtime-assembly decision rule in `trends/2026/machine-experience.md`:
  when an interface is composed at runtime, design decisions must be
  recorded as explicit machine-readable constraints (allowed
  components, order, density, what may not change), because decisions
  that are only implied collapse to the median default. New source
  record.

- Horizon note in `trends/2026/standards-outlook.md`: the W3C Design
  Tokens Format Module (v2025.10) formalises token architecture into a
  platform-agnostic JSON format; multi-year design-system foundations
  should author tokens in that machine-readable form so automated
  assembly and restyling tooling consumes one deterministic source and
  cannot drift from the documented semantics, including accessibility
  constraints. Source already recorded in `resources/sources.json`.

- `resources/libraries.md`: GOV.UK Frontend listing — public-service
  design system; new components ship under lifecycle statuses such as
  "Trial" while usage guidance is gathered; current line v6.6.0
  (October 2026) refines the character count component. New source
  record.

- Internationalization section in `catalog/primitives.md`: right-to-left
  mirroring rules with a never-mirror list, directional-icon rules,
  logical properties, text-expansion budgets, locale-aware
  date/number/currency formatting and sorting, mixed-direction text,
  and direction testing. Completes roadmap action 1. New source
  records.

- Third worked example `examples/onboarding/`: stated step total,
  one task per step with a prefilled smart default, always-available
  skip with a resume panel for skipped steps, sticky thumb-reach action
  bar for compact screens, and all seven states demonstrated.
  Completes roadmap action 2.

- Machine-experience deepening in `trends/2026/machine-experience.md`:
  structured-data summaries for agent readers, explicit task
  affordances, typed errors carrying retryable/hint/partial-result
  fields, consent signals with human confirmation for high-risk
  actions, human-first ordering guarantees, idempotent operations, and
  a machine-legibility release checklist. Completes roadmap action 3.
  New source records.

- Maz-UI listing in `resources/libraries.md`: a component set shipping logical
  direction by default (`start`/`end` instead of `left`/`right` for props,
  slots, and style hooks) so layouts mirror correctly under right-to-left
  settings, plus a theming overhaul on a perceptually uniform colour scale
  with per-component token overrides. Source already recorded.

- Worked-example rule for the pre-populated empty-state variant in
  `catalog/states.md`: a pre-filled sample, clearly marked as an example
  with one action to adopt it, teaches the shape of the result before
  commitment; where a sample is impossible, show a faded preview of the
  populated state behind the call to action. New source record.

- Pre-populated empty-state variant in `catalog/states.md`: a fourth
  variant alongside first-use, naturally empty, and restricted-or-failed
  — when available context suggests what the user is likely to want, the
  area offers suggestions instead of a blank screen; suggestions stay
  visually distinct from real items, are easy to dismiss, and are never
  stored as user data. Two new source records.

- Machine-experience trend: machine-readable intent metadata in
  `trends/2026/machine-experience.md` — components marked as required
  safety controls or removable convenience, so automated screen assembly
  cannot strip confirmations, dependent-selection steps, or disclosure
  checks; accessibility constraints travel with the component. New
  source record.

- Translucency content-layer rule in `trends/2026/spatial-interfaces.md`:
  keep translucent materials on navigation and controls, not the content
  layer — contrast shifts as content scrolls beneath translucent
  surfaces, so text- and number-dense screens stay opaque, with opaque
  variants under the reduce-transparency preference. New source record.

- Deep editorial review: new `layouts/automotive.md` — glance-budget
  layout for driving interfaces (two-second glance and twelve-second
  task budgets, one question per glance, stable information positions,
  0.25 s input response, 76x76 dp targets, 32/24 dp text, physical
  controls for essential functions, day/night modes, distraction
  suppression while moving, one-handed gestures), with all seven
  states. New source records (findings 1–2).
- Patterns catalogue: three new pattern rows in `catalog/patterns.md` —
  map comparison (hover notes, visited markers, small multiples,
  peel-back swipe, pop-up versus panel, rich markers), chat and
  messaging (capabilities stated up front, quick actions, progressive
  streaming with stop control, inline error on the failed bubble,
  offline queue with visible banner, live regions, 44 px targets),
  and list navigation (infinite scroll for exploration, pagination
  for goal-oriented tasks, load-more as the safe default,
  place-restoring URL handling, paginated crawler fallback); the
  Wizard row strengthened with total step count up front,
  non-interactive future steps, contextual forward labels,
  data-preserving back, vertical steppers on narrow screens, and
  save-and-resume. New source records (findings 5–8).
- Primitives catalogue: new `Date picker` row in
  `catalog/primitives.md` — lightest control per intent, seven
  day-cell states distinguishable without colour alone, typed entry
  as a first-class path, ranges as their own pattern with explicit
  commit, timezone-explicit times, presets, and a full keyboard
  contract. New source records (findings 10–11).
- Layout deepening: dashboard KPI rules in `layouts/dashboard.md`
  (three-slot tiles, grayscale readability, 3:1 density ratio,
  always-visible filter chips, cadence matched to the decision cycle,
  stated last-updated time); kiosk accessibility rules in
  `layouts/kiosk.md` (assistive entry point usable without vision,
  multi-sense time alerts with extension, 800–1600 mm reach bounds,
  one-tap session reset, offline fallback, speech-available
  receipts). New source records (findings 3–4, 9).
- Trends: new `trends/2026/dark-mode.md` — dark greys over pure black,
  type adjustments, elevation over shadows, redesigned accents,
  semantic token contract, system default with user override,
  200–300 ms switch honouring reduced motion; APCA
  perceptual-contrast note in `trends/2026/standards-outlook.md`
  (0–120 lightness score, polarity-aware, 90/75/60/45 thresholds,
  test new palettes against both systems) plus the assistive
  entry-point principle. New source records (findings 12–13).
- Roadmap: exactly three new improvement actions (deepen the
  machine-experience trend file, add a media-controls primitive row,
  extend the chat pattern with group-conversation rules); coverage
  matrix refreshed (chat and messaging, map comparison, list
  navigation, stepper promoted to full); completed actions 3–6 moved
  here: search-health evaluation checklist in the Search pattern row,
  focused/selected/expanded/warning supporting-state rows in
  `catalog/states.md`, the WCAG 3.0 standards-outlook horizon note,
  and the modular-card-grids deepening (fixed size tiers by
  importance, density as a grid property, reorder feedback with
  plain-text announcements).
- Primitives catalogue: new `Shape` row in `catalog/primitives.md` —
  native geometric shape control (path coordinates, border geometry,
  corner presets such as bevel, notch, scoop, and squircle) as a
  first-class primitive, with rules that keep shape decorative
  (hit target, reading order, and focus order unchanged), prefer
  system corner presets, and require a rectangular fallback on
  platforms without native shape support. New source record
  (164 total).
- Component libraries: new `Accessible Components Library` listing in
  `resources/libraries.md` — a small v1.0.0 accessibility-documented
  component set whose per-component requirements are mapped to WCAG 2.2
  success criteria and grouped into ten themes, with test scenarios and
  assistive-technology compatibility notes. New source record (163 total).
- Patterns catalogue: three new pattern rows in `catalog/patterns.md` —
  notification escalation (urgency-to-pattern-and-channel scale: badge,
  toast, banner, notification centre, modal, full-screen dialog;
  nothing critical lives only in a toast; notification-debt rule
  against high-urgency patterns on low-urgency events), offline-first
  sync (durable mutation queue with identifiers and attempt counts,
  granular syncing / local-changes-pending / stale states,
  optimistic updates marked pending until reconciled or rolled back,
  visible sync-status area with retry and freshness indicators), and
  file upload (5–10 MB chunking with per-chunk retry, per-file queue
  items with pause/retry/remove, progress accurate after resume, full
  keyboard operability with state announcements). Search row extended
  with typeahead rules (instant results, per-row context, scope filters).
- Patterns catalogue: new command-palette pattern in
  `catalog/patterns.md` — one standard summon shortcut, autofocus on
  open, verb-led commands with forgiving subsequence matching and
  synonyms, grouped typed results with unscathed scope information,
  recents in the blank state, stable selection while results stream,
  safe execution ordering, full keyboard operation with focus returned
  to the trigger. Cross-linked from the shortcut rules in
  `layouts/desktop.md`. Completes roadmap action 5.
- Interface catalogue: new automotive HMI entry in
  `catalog/interfaces.md` — two-second glance and twelve-second task
  budgets as hard rules, essential functions on tactile physical
  controls, contextual minimalism by driving conditions, voice for
  secondary tasks, and adaptive narrowing as attention demands rise.
- Functional motion: informational-versus-decorative motion rules in
  `trends/2026/functional-motion.md` — informational motion (progress,
  focus) keeps moving without large transforms; decorative motion is
  gated behind a no-preference check so it fails closed; auto-playing
  content over five seconds always gets a visible pause control.
- States catalogue: focus-indicator strengthening in
  `catalog/states.md` — 3:1 contrast minimum against adjacent colours,
  outline in system colours for forced-colours mode, and root scroll
  padding matched to fixed chrome so focused controls are never fully
  hidden behind sticky elements.
- Spatial trend: glass-layer constraints in
  `trends/2026/spatial-interfaces.md` — no layered translucent
  surfaces, translucency disabled under high-contrast settings with an
  opaque default, and default opacities treated as
  accessibility-tested values.
- Libraries: web-components refresh in `resources/libraries.md` — a
  successor web-components library entry (component count, palettes,
  cascade layers, SSR, commercial additions) and the unstyled-primitives
  direction with token-based theming, cross-linked to the headless
  behaviour primitive.
- Fifteen new source records in `resources/sources.json` (162 total):
  command-palette and search UX, notification urgency mapping,
  offline-first stores and sync, resumable uploads, automotive HMI,
  web-component library succession, unstyled primitives, reduced-motion
  nuance, focus indicators, and glass theming.

### Fixed

- Primitives: merged the two identical Media effect rows in
  `catalog/primitives.md` into one canonical row. Completes roadmap
  action 6.

- Patterns catalogue: new data-visualisation pattern in
  `catalog/patterns.md` — match the chart type to the story, takeaway
  titles, direct data labelling, colour never alone, a text alternative
  stating the key insight, the underlying data offered as a table,
  keyboard-operable interactive charts, and charts not mirrored in
  right-to-left layouts. Completes roadmap action 4 (added this run).
- Roadmap: three new improvement actions ordered by coverage impact —
  the data-visualisation pattern (implemented this run), a
  command-palette pattern for `catalog/patterns.md` with a cross-link
  from `layouts/desktop.md`, and a merge of the two identical Media
  effect rows in `catalog/primitives.md`; both left to the deep cycle.
- Five new source records in `resources/sources.json` (147 total):
  interface internationalization guide, bidirectionality mirroring
  guidance, card grid density guidance, CSS grid layout reference, and
  accessible data-visualisation guidance.

- States catalogue: new theme-preference state rules in
  `catalog/states.md` — automatic mode re-reads the live system
  preference on every load instead of freezing a resolved value; the
  configured theme is authoritative over stale or foreign stored values;
  label, stored value, and applied theme agree before first paint.

- Primitives: new button-group entry in `catalog/primitives.md` —
  shared container for related buttons with a single connected shape,
  grouped and segmented variants, rules for related actions only, visible
  and announced selection state, subtle shape changes, and a reduced-motion
  cross-fade instead of spring or morph motion.

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
