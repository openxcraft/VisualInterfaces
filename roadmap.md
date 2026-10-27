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
| Page pattern | Dashboard, mobile navigation, data table, checkout variants, onboarding, comparison, permission request, search results, command palette, notification escalation, offline-first sync, sync-conflict resolution, file upload, chat and messaging, map comparison, list navigation, machine-composed content disclosure, agent checkpoint, voice hybrid flows, stepper, landing, authentication, settings, commerce, consent, notification digest, personalized-content disclosure, calendar and scheduling, keyboard shortcut reference, undo and trash recovery, session-expiry warning, data export, account deletion, in-product help, share link, second-factor sign-in, saved-item collection, bulk action, rating and review submission, payment failure recovery, content reporting and blocking, language and locale selection, scheduled action, breadcrumb navigation, annotation and comment thread, theme selection, profile and
account menu, recently viewed, invitation response, modal dialog, guest checkout, time-zone picker, accessibility preferences | — | — |
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
   passes all quality gates. (Implemented this run.)

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
    all quality gates. (Implemented this run.)

13. Add a saved-filter view pattern row to `catalog/patterns.md`: a
    named view that stores a filter combination for one-tap return, with
    rename and delete controls, a stated scope (private or shared), and a
    visible sign when the saved view no longer matches the current data —
    cross-checked against the filtering and sorting row. Done when the row
    passes all quality gates.
14. Add a version history and restore pattern row to
    `catalog/patterns.md`: a dated list of saved versions with a preview
    of what changed, a restore action that saves the restored version as a
    new version rather than silently overwriting the current one, and a
    clear statement of what restore does and does not bring back —
    cross-checked against the sync-conflict resolution row. Done when the
    row passes all quality gates.
15. Add a keyboard shortcut reference pattern row to
    `catalog/patterns.md`: a searchable, context-grouped list of shortcuts
    reachable from help, with remapping controls and a conflict warning
    when a new shortcut collides with an existing one — distinct from the
    command palette, which executes commands rather than teaching them.
    Done when the row passes all quality gates. (Implemented this run.)

16. Add an undo and trash recovery pattern row to `catalog/patterns.md`:
    an immediate undo offer after a destructive action, a trash area
    with a stated retention period and a restore-to-original-place
    action, and a separate permanent-delete step that states what is
    lost — cross-checked against the version history row and the
    confirmation row. Done when the row passes all quality gates.
    (Implemented this run.)
17. Add cross-zone scheduling rules to the calendar and scheduling row
    in `catalog/patterns.md`: each event states the organiser zone and
    the attendee zone where they differ, ambiguous or repeated times
    around zone transitions are flagged before booking, and editing a
    recurring event states whether the change follows the series zone
    or the local zone — cross-checked against the timezone labels in
    the calendar row. Done when the rules pass all quality gates.
    (Implemented this run.)
18. Add multitasking and split-window rules to `layouts/tablet.md`:
    two apps side by side with a stated primary pane, drag between
    panes without losing the dragged item, and resize continuity so
    content, selection, and entered input survive a pane-width change
    — cross-checked against the width-band and foldable-posture rules
    in the same file. Done when the rules pass all quality gates.
    (Implemented this run.)

23. Add a session-expiry warning pattern row to
    `catalog/patterns.md`: warn before a session ends with the time
    remaining stated plainly, offer a keep-working action that
    preserves entered input, and never discard a draft or a form on
    expiry — the person returns to the same place with the same
    input, or to a saved draft with a clear restore step —
    cross-checked against the draft autosave row and the timeout
    rules in `catalog/states.md`. Done when the row passes all
    quality gates. (Implemented this run.)
24. Add a data export pattern row to `catalog/patterns.md`: export
    in common formats the person can actually open elsewhere, state
    plainly what the export includes and excludes, show progress for
    large exports instead of a silent wait, state how long the
    download link stays live, and handle a partial failure by
    naming what exported and what did not rather than delivering a
    silent short file — cross-checked against the file upload row.
    Done when the row passes all quality gates.
    (Implemented this run.)
25. Add an account deletion pattern row to `catalog/patterns.md`:
    delete from the same channel used to sign up, state the effect
    before confirmation — what content is removed, what is kept
    for other people, and when removal completes — offer a grace
    period with a plain undo path inside it, and confirm removal in
    writing once it is done — cross-checked against the
    subscription cancellation row and the confirmation row. Done
    when the row passes all quality gates.
    (Implemented this run.)

19. Add data-table sort-state rules to the Data table row in
    `catalog/patterns.md`: an unsorted column shows a neutral
    indicator distinct from ascending and descending, the current
    direction is visible in the header and announced to assistive
    technology, multi-column sort states its column order and uses a
    unique field as the final tie-breaker so paging stays stable,
    sorting moves to the server once the set exceeds what the client
    can sort without lag, and the sort survives paging and filtering.
    Done when the extended row passes all quality gates.
    (Implemented this run.)
20. Add form validation timing rules to the Form flow row in
    `catalog/patterns.md`: never flag a field before the person has
    left it or submitted the form, re-validate on each keystroke only
    once a field is already marked invalid so a fix clears at once,
    keep the error message in place and linked to its field rather
    than removing and re-inserting it, focus the first invalid field
    for a single error and an error summary for several, and retain
    all entered input after a failed submission — cross-checked
    against the error state rules in `catalog/states.md`. Done when
    the extended row passes all quality gates.
21. Add contextual guidance rules to the Onboarding row in
    `catalog/patterns.md` and `layouts/onboarding.md`: inline help is
    the default, coach marks appear only when the person first
    reaches the feature they explain, never more than three in a
    sequence, always dismissable, and never a substitute for a clear
    label or a first screen that teaches by doing — cross-checked
    against the skip and progress-persistence rules in the same
    files. Done when the rules pass all quality gates.
22. Add an empty-state fallback rule to the Empty row in
    `catalog/states.md`: the empty state renders as a static
    fallback even when the data request fails, so a failed load never
    produces a blank screen; the fallback states what is missing,
    offers one next action, and states whether a retry will restore
    the content — cross-checked against the error state rules in the
    same file. Done when the extended row passes all quality gates.

26. Add a saved-item collection pattern row to
    `catalog/patterns.md`: save an item with one action, show its
    saved state wherever the item appears, offer named collections
    with rename and delete controls, and state what happens to
    saved items when the original item changes or is removed —
    cross-checked against the filtering and sorting row. Done when
    the row passes all quality gates.
    (Implemented this run.)
27. Add a bulk-action pattern row to `catalog/patterns.md`: state
    the selection scope before acting (page, filtered set, or all
    matching items), summarise the action and its count for
    confirmation, report per-item failures separately from
    successes, and offer an undo for the whole batch where the
    action is reversible — cross-checked against the confirmation
    row. Done when the row passes all quality gates.
    (Implemented this run.)
28. Add a rating and review submission pattern row to
    `catalog/patterns.md`: a structured rating with an optional
    written review, an edit window after submission, a plain
    statement of what is shown publicly and what is moderated, and
    no gating of core features behind a rating request — cross-checked
    against the confirmation row. Done when the row passes all
    quality gates.
    (Implemented this run.)

29. Add a help-search recovery rule to the In-product help row in
    `catalog/patterns.md`: when in-product search returns nothing,
    suggest the nearest topics by wording rather than an empty page,
    and carry the failed query into the escalation path so the person
    never retypes it. Done when the rule passes all quality gates.
30. Add a link-preview rule to the Share link row in
    `catalog/patterns.md`: before sending, show the recipient what
    the link opens, who can open it, and when it expires, with an
    edit step for scope and expiry from the same screen. Done when
    the rule passes all quality gates.
31. Add a method-change rule to the Second-factor sign-in row in
    `catalog/patterns.md`: changing the second-factor method requires
    a successful check with the current method first, and the old
    method stays active until the new one verifies, so a failed
    switch never locks the person out. Done when the rule passes all
    quality gates.

32. Add a content reporting and blocking pattern row to
    `catalog/patterns.md`: a report action reachable from the
    item itself, a plain choice of reason, a stated outcome for
    the reported item and for the reporter, a block control that
    hides the blocked party everywhere at once, and a review
    path for a report decided in error — cross-checked against
    the confirmation row. Done when the row passes all quality
    gates.
    (Implemented this run.)
33. Add a language and locale selection pattern row to
    `catalog/patterns.md`: language names written in their own
    language, a stated scope for the choice (current session or
    saved preference), an immediate preview of the change
    without losing entered input, and a fallback that never
    strands the person on a page they cannot read — cross-checked
    against the internationalization section in
    `catalog/primitives.md`. Done when the row passes all quality
    gates.
    (Implemented this run.)
34. Add a scheduled action pattern row to `catalog/patterns.md`:
    an action set for a later time states its scheduled time in
    plain words, stays editable and cancellable until it runs,
    confirms once it has run, and reports a missed or failed
    scheduled run with a retry path rather than silently
    dropping it — cross-checked against the confirmation row
    and the draft autosave row. Done when the row passes all
    quality gates.
    (Implemented this run.)
35. Add a payment failure recovery pattern row to
    `catalog/patterns.md`: keep the person in the same checkout
    with the order intact after a failed payment, state the
    failure in plain words with an actionable cause where known,
    offer retry only where it can succeed and another eligible
    method on the same screen, check the real status before any
    second attempt so one order is never charged twice, and hold
    a pending payment with a stated status check rather than
    showing failure prematurely — cross-checked against the
    checkout variants in `layouts/ecommerce.md` and the
    confirmation row. Done when the row passes all quality
    gates. (Implemented this run.)
36. Add an annotation and comment thread pattern row to
    `catalog/patterns.md`: each thread anchored to the specific
    section, sentence, or element it discusses, with a stated
    rule for threads whose anchor was deleted or heavily
    rewritten, reply nesting with a resolve and reopen path,
    thread visibility following the visibility of the content
    itself, and an overview listing open and resolved threads —
    distinct from open action 10 (collaborative editing
    presence and field locks) and from the chat and messaging
    row (conversation, not anchored comment). Done when the
    row passes all quality gates.
    (Implemented this run.)
37. Add a what's-new announcement pattern row to
    `catalog/patterns.md`: grade announcement visibility by
    impact — minor changes stay in the changelog, workflow
    changes get a dismissible in-place announcement, and
    changes that block a task get a prominent once-only notice
    — with action-oriented wording, a direct route to the new
    capability, a persistent entry point for later review, and
    a seen state so a dismissed announcement is never shown
    again — distinct from onboarding (first use), the
    notification digest (grouped updates), and the install and
    review prompts. Done when the row passes all quality
    gates.

38. Add a breadcrumb navigation pattern row to
    `catalog/patterns.md`: a trail showing the path from the home
    view to the current page, each step a working link except the
    current page, collapse and truncation rules on narrow screens
    that always keep the home view and the parent step reachable,
    and a stated rule for when a trail is omitted (single-level
    pages and task flows where a trail would imply a hierarchy
    that does not exist) — distinct from the primary navigation
    row, which moves between top-level sections rather than
    showing where the current page sits. Done when the row passes
    all quality gates.
    (Implemented this run.)
39. Add an account recovery pattern row to
    `catalog/patterns.md`: identify the account without revealing
    whether it exists, verify through a route the person can
    still reach, let a failed verification fall back to another
    route rather than locking the account, restore sessions and
    saved work after recovery, and state plainly what recovery
    does and does not restore — cross-checked against the
    second-factor sign-in row and the session-expiry warning row.
    Done when the row passes all quality gates.
40. Add a theme selection pattern row to
    `catalog/patterns.md`: a choice between light, dark, and
    system-following themes with an immediate preview that loses
    no entered input, a saved preference that survives visits, a
    stated rule for what changes when the system theme changes,
    and a guarantee that text stays readable in every theme —
    distinct from the token and contrast rules in
    `trends/2026/dark-mode.md`, which describe how themes are
    built rather than how the choice is offered. Done when the
    row passes all quality gates.
    (Implemented this run.)

41. Add a profile and account menu pattern row to
    `catalog/patterns.md`: a menu anchored to the current-account
    trigger listing the account's own actions — view account,
    open settings, manage sign-in methods, and sign out — with
    the active account named in text, sign-out kept separate
    from destructive account actions, and a return to the same
    place after any menu action that does not leave the task —
    distinct from the account switcher row, which moves between
    signed-in accounts, and from the settings layout, which is
    a full page rather than a menu. Done when the row passes
    all quality gates.
    (Implemented this run.)
42. Add a recently viewed pattern row to `catalog/patterns.md`:
    a recents list that returns the person to items opened
    before, with each entry naming the item and when it was
    last opened, a stated scope for what is remembered, a
    clear-all control, and a rule for items that no longer
    exist — distinct from the saved-item collection row, which
    keeps items the person chose to keep, and from the command
    palette, which lists recents only as a blank-state shortcut.
    Done when the row passes all quality gates.
    (Implemented this run.)
43. Add an invitation response pattern row to
    `catalog/patterns.md`: an invitation states what is asked,
    who sent it, and when it needs an answer, and offers accept,
    decline, and tentative replies with a stated effect for each;
    a changed reply updates the organiser and the attendees
    without creating a duplicate item, and a withdrawn or
    expired invitation states plainly that it no longer applies
    — distinct from the calendar and scheduling row, which
    covers how times are shown across zones. Done when the row
    passes all quality gates.
    (Implemented this run.)

44. Add a modal dialog pattern row to `catalog/patterns.md`:
    a dialog that asks one decision, takes focus on opening and
    returns it on closing, offers a visible dismiss path besides
    the decision actions, traps focus only while open, and never
    nests a second dialog — a second layer of decisions becomes
    a new view — cross-checked against the no-nesting rule in
    the layout rules of the same file. Done when the row passes
    all quality gates.
    (Implemented this run.)
45. Add a guest checkout pattern row to `catalog/patterns.md`:
    completing a purchase without creating an account, with the
    order and its details preserved if the person later creates
    an account, a stated difference between guest and signed-in
    checkout (such as saved details and order history), and no
    account creation forced mid-checkout — distinct from the
    checkout variants in `layouts/ecommerce.md`, which describe
    page shapes rather than the guest path. Done when the row
    passes all quality gates.
    (Implemented this run.)
46. Add a time-zone picker pattern row to `catalog/patterns.md`:
    a picker that lists zones by place name with the current
    local time and offset shown for each, searchable by place or
    zone name, ordered by current time rather than alphabet
    alone, and stating plainly whether the chosen zone follows
    clock changes — distinct from the cross-zone scheduling
    rules, which cover how booked times are shown to attendees.
    Done when the row passes all quality gates.
    (Implemented this run.)

47. Add a pull-to-refresh pattern row to `catalog/patterns.md`:
    a refresh gesture and control for list content, a visible
    refreshing state that never hides the existing list, a stated
    result after refresh (new items, no change, or failure with
    retry), and a keyboard and assistive-technology route that
    matches the gesture — distinct from the offline-first sync
    row, which covers queued changes rather than re-reading
    content. Done when the row passes all quality gates.
48. Add a file preview pattern row to `catalog/patterns.md`:
    a preview shown before opening or downloading a file, with
    the file name, type, and size stated, a readable excerpt or
    thumbnail where the type allows one, and a plain fallback
    where no preview exists — distinct from the file upload row,
    which covers sending files rather than inspecting them.
    Done when the row passes all quality gates.
49. Add a search history pattern row to `catalog/patterns.md`:
    past queries kept as a list the person can re-run, edit, or
    delete one at a time or all at once, with a stated retention
    scope — distinct from the recently viewed row, which lists
    opened items rather than queries, and from the search row,
    which covers finding content. Done when the row passes all
    quality gates.

50. Add an accessibility preferences pattern row to
    `catalog/patterns.md`: text size, bold text, increased
    contrast, reduced motion, reduced transparency, and captions
    gathered in one reachable place, each applied at once to a
    live preview, a stated rule for where a choice follows the
    system and where it overrides it, a single reset to the
    starting values, and a saved preference across visits —
    distinct from theme selection, which chooses colours rather
    than size, contrast, motion, and captions. Done when the row
    passes all quality gates. (Implemented this run.)
51. Add a long-document navigation pattern row to
    `catalog/patterns.md`: a sticky outline of the page headings
    with the current section marked in text as well as in shape,
    jump links that move focus to the section heading, a collapse
    to a single outline control on narrow screens, and a return
    to the top that never loses the person's place in a form —
    distinct from breadcrumb navigation, which shows where the
    page sits in a hierarchy rather than where the person sits
    in a long page. Done when the row passes all quality gates.
52. Add an in-app update prompt pattern row to
    `catalog/patterns.md`: a flexible prompt that downloads in
    the background and lets the person keep working, a blocking
    prompt reserved for versions that can no longer work safely,
    a stated deferral limit and deadline for the flexible prompt,
    no prompt during a task or a payment, and a resume step
    after an interrupted update — distinct from the what's-new
    announcement row, which reports changes rather than
    requiring an update. Done when the row passes all quality
    gates.

## Review notes

- Completed this review (daily planning 2026-10-27): research
  pass of 3 searches covering in-app update prompts,
  accessibility preferences, and long-document navigation; 3 new
  source records (286 total), URLs copied verbatim from results
  and deduplicated against the existing set. Three new actions
  added (50–52), ordered by coverage impact; action 50
  implemented this run as the Accessibility preferences row in
  `catalog/patterns.md` (one reachable place for text size,
  bold text, contrast, motion, transparency, and captions, live
  preview with no input lost, system-follow versus override
  stated, single reset, saved across visits). Actions 51 and 52
  left to the deep cycle. Since the last daily run, the deep
  cycle completed actions 44, 45, and 46 and added actions 47,
  48, and 49; those outcomes are already recorded in
  `CHANGELOG.md`, and the light cycles since then reported no
  changes.

- Completed this review (deep editorial 2026-10-27): new Modal
  dialog pattern row in `catalog/patterns.md` (one decision per
  dialog, focus taken on opening and returned on closing, focus
  trapped while open, visible dismiss path besides the decision
  actions, never a nested dialog, full-width sheet on narrow
  screens); new Guest checkout pattern row (guest path beside
  sign-in, fulfilment details only before payment, stated
  difference from signed-in checkout, post-purchase account
  offer carrying the order into the new account, no forced
  account step mid-checkout); new Time-zone picker pattern row
  (zones by place name with current local time and offset,
  search by place, zone name, or offset, detected zone
  suggested at the top, clock-change behaviour stated plainly,
  example time shown beside the person's own time for
  confirmation). Completes roadmap actions 44, 45, and 46;
  actions 47, 48, and 49 added as follow-ups. Coverage matrix
  updated with the three new rows. 3 new source records (282
  total).

- Completed this review (deep editorial 2026-10-26): new Profile
  and account menu pattern row in `catalog/patterns.md` (account's
  own actions only, active account named in text, sign-out kept
  separate from destructive actions, return to the same place
  after actions that do not leave the task); new Recently viewed
  pattern row (newest-first list with last-opened labels, stated
  scope, clear-all and single-entry removal, in-place notice for
  items that no longer exist, kept distinct from saved items);
  new Invitation response pattern row (accept, decline, and
  tentative replies with a stated effect for each, reply changes
  updating organiser and attendees without a duplicate item,
  proposed times kept unconfirmed until accepted, withdrawn or
  expired invitations stated plainly with no reply actions).
  Completes roadmap actions 41, 42, and 43; actions 44, 45, and
  46 added as follow-ups. Coverage matrix updated with the three
  new rows. 3 new source records (276 total).

- Completed this review (deep editorial 2026-10-26): new
  Breadcrumb navigation pattern row in `catalog/patterns.md`
  (home-to-current trail, current page marked in text, middle
  steps collapsed into an overflow control on narrow screens
  keeping home and parent reachable, omission rule for
  single-level pages and task flows); new Annotation and
  comment thread pattern row (threads anchored to the specific
  section, sentence, or element, nested replies, resolve
  without delete, reopen with history, overview of open and
  resolved threads, outdated-anchor rule keeping quoted text);
  new Theme selection pattern row (light, dark, and
  system-following choices, immediate undoable preview with
  no input lost, saved preference overriding the system theme,
  contrast checked in every theme). Completes roadmap actions
  36, 38, and 40; actions 41, 42, and 43 added as follow-ups.
  Coverage matrix updated with the three new rows. 4 new
  source records (271 total).

- Completed this review (deep editorial 2026-10-26): new Content
  reporting and blocking pattern row in `catalog/patterns.md`
  (report from the item itself, plain reason choice, immediate
  hide for the reporter, block hiding the blocked party
  everywhere at once, review path for a decision in error); new
  Language and locale selection pattern row (names in their own
  language, no flag standing for a language, stated session or
  saved scope, same-page switch with input kept, item-by-item
  fallback that never strands the person); new Scheduled action
  pattern row (plain-words scheduled time, edit and cancel until
  the run, content and time edits kept independent, single run
  confirmation, missed or failed runs reported with a retry
  path). Completes roadmap actions 32, 33, and 34; actions 38,
  39, and 40 added as follow-ups. Coverage matrix updated with
  the three new rows. 3 new source records (265 total).

- Completed this review (daily planning 2026-10-26): research
  pass of 3 searches covering payment failure recovery,
  anchored comment threads, and in-product update
  announcements; 3 new source records (261 total), URLs copied
  verbatim from results and deduplicated against the existing
  set. Three new actions added (35–37), ordered by coverage
  impact; action 35 implemented this run as the Payment failure
  recovery row in `catalog/patterns.md` (order kept intact in
  the same checkout, plain-word cause, retry only where it can
  succeed, another method on the same screen, real status
  check before any second attempt, pending payments held with
  a status check). Actions 36 and 37 left to the deep cycle.
  Since the last daily run, the deep cycle completed actions
  26, 27, and 28 and added actions 32, 33, and 34; those
  outcomes are already recorded in `CHANGELOG.md`, and the
  light cycles since then reported no changes.

- Completed this review (deep editorial 2026-10-26): new Saved-item
  collection pattern row in `catalog/patterns.md` (one-action save,
  saved state wherever the item appears, named collections with
  rename and delete controls, stated private or shared scope,
  stale or removed originals stated plainly with a nearest
  alternative); new Bulk action pattern row (stated scope of page,
  filtered set, or all matching items, confirmation summarising
  action, count, and scope, per-item failures named with cause and
  retry path, whole-batch undo where reversible, partial success
  never reported as full success); new Rating and review
  submission pattern row (structured rating with optional written
  review, keyboard-operable steps labelled in words, public and
  moderated parts stated before submitting, stated edit window
  with moderation on edit, reasoned moderation decisions with a
  revise path, no gating of core features behind a rating).
  Completes roadmap actions 26, 27, and 28; actions 32, 33, and 34
  added as follow-ups. Coverage matrix updated with the three new
  rows. 3 new source records (257 total).


- Completed this review (deep editorial 2026-10-25): new In-product
  help pattern row in `catalog/patterns.md` (persistent help entry,
  context-aware suggestions, in-place search without losing entered
  input, answer-first articles, escalation carrying task context,
  article feedback); new Share link pattern row (access scope and
  expiry stated before sharing, named-access default for sensitive
  items, confirmed copy state with a manual fallback on failure,
  expired or revoked links explained with a request-access path,
  one-step revocation); new Second-factor sign-in pattern row
  (strongest method first, full paste support, resend timer with
  stated destination, attempt count without revealing failures,
  always-visible single-use backup-code path, opt-in trusted-device
  choice, enabled only after successful verification). Completes
  roadmap actions for the three new rows; actions 29, 30, and 31
  added as follow-ups. Coverage matrix updated with the three new
  rows. 3 new source records (251 total).


- Completed this review (deep editorial 2026-10-25): new Session-expiry
  warning pattern row in `catalog/patterns.md` (plain time-remaining
  warning that never blocks work, simple keep-working action, idle
  limit stated separately from an absolute limit, entered input saved
  and restored after expiry); new Data export pattern row (common
  formats, includes and excludes stated before starting, real progress
  with a stated link lifetime, partial failure naming what exported
  and what did not with a retry for the missing part only); new
  Account deletion pattern row (same-channel deletion, effect stated
  before confirmation including what is kept and why, export offered
  before deletion, sign-out everywhere, stated grace period with a
  plain undo path, written confirmation on completion). Completes
  roadmap actions 23, 24, and 25. Coverage matrix updated with the
  three new rows. 4 new source records (245 total).


- Completed this review (deep editorial 2026-10-25): new Undo and
  trash recovery pattern row in `catalog/patterns.md` (immediate undo
  offer restoring to the original place, undo alone for easily
  repeated actions, confirmation plus trash safety net for wider
  effects, stated retention period, parent-child restore rules, a
  separate permanent-delete step stating what is lost); cross-zone
  scheduling rules added to the Calendar and scheduling row
  (organiser and attendee zones stated where they differ, ambiguous
  or repeated times around zone transitions flagged before booking,
  recurring events pinned to a named zone with a preview of local-time
  changes across transitions, edit scope stated as series zone or
  local zone, date-boundary dates stated per attendee, shared
  multi-zone timeline); multitasking and split-window rules in
  `layouts/tablet.md` (stated primary pane, lossless drag between
  panes with a plain explanation on refusal, resize as a continuity
  event, saved app pairs, dismissible floating window, upfront
  statement when an app cannot run in a pane). Completes roadmap
  actions 16, 17, and 18. 3 new source records (237 total).

- Completed this review (deep editorial 2026-10-24): new Notification
  digest pattern row in `catalog/patterns.md` (grouping by thread, type,
  or time window, period label, per-item open and read state, person-
  controlled daily, weekly, or no-digest schedule, never digesting
  critical or time-sensitive items); new Personalized-content disclosure
  pattern row (plain-words signal statement at the point of adaptation,
  unadapted view beside the adapted one, reversible change or turn-off,
  plain statement of what cannot be changed); new Calendar and
  scheduling pattern row (scale chosen by planning question, context
  preserved across scale switches, calendar kept distinct from a date
  picker, predictable day-click effect, distinct slot states, context
  kept with a nearest alternative when a slot becomes unavailable,
  inspectable recurrence rule with stated edit scope, per-event timezone
  labels). Completes roadmap actions 6 and 12. 3 new source records
  (224 total). This publish also carries the television dual-input focus
  rule already present in the local tree.

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
- Completed this review (deep editorial 2026-10-25): new Keyboard
  shortcut reference pattern row in `catalog/patterns.md` (searchable
  by action and by key, grouped by context, single-character
  shortcuts focus-limited and remappable, conflict warning with
  confirmation, per-group or full reset, never the only route to an
  action); coverage matrix updated with the new row; three new
  improvement actions added (16 undo and trash recovery, 17
  cross-zone scheduling, 18 tablet multitasking and split-window).
  Completes roadmap action 15.

## Pre-publish checklist

The canonical publishing checklist lives in `CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The coverage matrix matches the actual files and directories.
- [ ] Only open improvement actions remain listed; completed ones moved to CHANGELOG.md.
- [ ] Exactly three new actions were added at the last deep review.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
