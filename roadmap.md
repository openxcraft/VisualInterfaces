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
account menu, recently viewed, invitation response, modal dialog, guest checkout, time-zone picker, accessibility preferences, long-document navigation, in-app update prompt, pull-to-refresh, scrolling tab bar, system share sheet, find-in-page, collaborative editing presence,
    draft autosave and recovery, saved-filter view, toast feedback, list reorder, date-range picker, accordion disclosure, carousel, passkey sign-in, low-bandwidth mode, what's-new announcement, version history and restore, external-link departure, described media, saved-cart recovery, colour picker, guest-to-account conversion, sensitive-content preview, order tracking, order cancellation, time picker, verification-code entry, background-task progress, automated-to-human support handoff, subscription plan change, promo-code entry, master-detail, threaded message reply, gift option, saved address selection, delivery slot picker, product variant selection, home-screen widget, deep-link landing, progressive disclosure, return and exchange request, back-in-stock alert request, contact picker, primary navigation, bypass link, search, filtering and sorting, data table density, inline editing, bulk selection, data visualisation, guided tour, setup checklist, inline assistant actions, form flow, character count, wizard, detail view, notification list, notification preferences, activity feed, confirmation, sensitive-action re-confirmation, install prompt, offline download, multi-device handoff, paywall and upgrade prompt, subscription cancellation, restore purchases, account switcher, in-product feedback and problem report, account recovery, consent choice, granular consent, media viewer, code scanner, simplified view, location selection, voice message, message reaction, pinned message, message edit and delete, swipe-to-reveal actions, poll, conversation branching, sticky section headers, appointment management, review prompt, rating distribution summary, limited-time offer countdown, age verification gate, suggestion review, code scanning, image gallery viewer, reading progress indicator, print-friendly view, text-selection action menu, picture-in-picture, reorder past order, live broadcast chat overlay, kanban board, gift card and stored-credit redemption, address entry, delivery instructions, saved payment method selection, split payment, media chapters, waitlist, loyalty rewards, link preview, live activity, billing overview, usage allowance, password strength meter, emoji picker, seat selection, selecting an option from a list, home control map, follow, payment instalment plan, subscribe-and-save purchase option, pickup point selection | — | — |
| State | All seven in catalog; offline, read-only, permission-denied; loading variants; error-state groups | — | — |
| Worked examples | Dashboard, mobile navigation, onboarding — each demonstrating the rules it documents with all seven states | — | — |
| Localization | Right-to-left mirroring rules, what-not-to-mirror list, logical properties, text-expansion budgets, locale-aware date/number/currency formatting and sorting, mixed-direction text | — | — |
| Responsive technique | Container-query component adaptation verified in full-page, sidebar, modal, and dense-dashboard grid contexts; viewport queries for page-level bands | — | — |

## Improvement actions

1. Add an agent-checkpoint pattern row to `catalog/patterns.md`: the
   delegate–monitor–approve–interrupt–refine loop, interruption points
   before irreversible actions, explicit approval surfaces for cost,
   purchase, privacy, or booking decisions, and a recovery path when
   an automated flow took a plausible but wrong route — cross-checked
   against the supervision and trust-gradient sections in
   `trends/2026/agentic-ux.md`. Done when the row passes all quality
   gates. (Implemented this run.)

2. Add voice hybrid-flow rules to
   `trends/2026/conversational-interfaces.md`: voice-to-initiate with
   physical (tap or biometric) confirmation for sensitive actions, and
   visual mishearing repair that shows what was heard with tappable
   correction instead of a dead-end message — cross-checked against
   the voice state matrix in `catalog/states.md`. Done when the
   extended file passes all quality gates. (Implemented this run.)

3. Add container-query responsiveness guidance to the layout rules:
   components must adapt to their container's size rather than only
   the viewport, verified in full-page, sidebar, modal, and
   dense-dashboard grid contexts. Done when the rules pass all quality
   gates. (Implemented this run.)

4. Add a machine-composed content disclosure pattern row to
   `catalog/patterns.md`: label every block the system composed as
   composed, state uncertainty and grounding plainly, keep a visible
   correction and override path, and pair any composed decision with
   effects outside the screen with an explicit approval step —
   cross-checked against the trust patterns in
   `trends/2026/agentic-ux.md` and the disclosure rules in
   `trends/2026/conversational-interfaces.md`. Done when the row
   passes all quality gates. (Implemented this run.)

5. Add a multimodal input-bar primitive row to
   `catalog/primitives.md`: text field with mic and media-attach
   entries, a hint naming all three modes, per-mode feedback (waveform
   while listening, thumbnails for attachments, processing states), an
   echo of what was heard with a quick correction path, and keyboard
   and screen-reader parity for every mode — cross-checked against the
   voice state matrix in `catalog/states.md`. Done when the row passes
   all quality gates. (Implemented this run.)

6. Add a personalized-content disclosure pattern row to
   `catalog/patterns.md`: when order, content, or recommendations
   adapt to the person, state what signal drove the adaptation, offer
   the unadapted view, and provide a change or turn-off path;
   inference-driven adaptation is reversible by default —
   cross-checked against the granular-consent row. Done when the row
   passes all quality gates. (Implemented this run.)

7. Add a sync-conflict resolution pattern row to
   `catalog/patterns.md`: when a locally queued change and a newer
   server version diverge, show both versions side by side, keep the
   local copy safe until resolved, let the person pick one version or
   merge field by field, and never silently overwrite either side —
   cross-checked against the offline-first sync row. Done when the row
   passes all quality gates. (Implemented this run.)

8. Add a voice command discovery section to
   `trends/2026/conversational-interfaces.md`: teach what can be asked
   in context — suggested prompts on first use, example utterances for
   the current screen, and a browsable list of capabilities — rather
   than a tour or a help page nobody opens. Done when the section
   passes all quality gates. (Implemented this run.)

9. Add a multi-device handoff pattern row to `catalog/patterns.md`:
   continue a task on another device from an explicit resume point,
   state what transferred and what did not, and resolve the case where
   both devices edited the same item before handing off —
   cross-checked against the offline-first sync row. Done when the row
   passes all quality gates.

10. Add a collaborative editing presence pattern row to
   `catalog/patterns.md`: show who else is present in the shared
   document, which field each person is editing, and a visible lock or
   hold on the field being edited, so two people never overwrite the
   same field unknowingly — cross-checked against the sync-conflict
   resolution row. Done when the row passes all quality gates.
   (Implemented this run.)

11. Add a draft autosave and recovery pattern row to
   `catalog/patterns.md`: save drafts continuously with a visible
   saved indicator, restore the latest draft after a crash or
   interruption with a clear review step, and offer an explicit
   discard path — cross-checked against the wizard save-and-resume
   rules. Done when the row passes all quality gates. (Implemented
   this run.)

12. Add a notification digest pattern row to `catalog/patterns.md`:
   group low-urgency updates into a scheduled digest the person
   controls (daily or weekly), keep every item individually openable,
   and never digest a critical or time-sensitive item — cross-checked
   against the notification escalation scale. Done when the row passes
   all quality gates. (Implemented this run.)

13. Add a saved-filter view pattern row to `catalog/patterns.md`: a
   named view that stores a filter combination for one-tap return,
   with rename and delete controls, a stated scope (private or
   shared), and a visible sign when the saved view no longer matches
   the current data — cross-checked against the filtering and sorting
   row. Done when the row passes all quality gates. (Implemented this
   run.)

14. Add a version history and restore pattern row to
   `catalog/patterns.md`: a dated list of saved versions with a
   preview of what changed, a restore action that saves the restored
   version as a new version rather than silently overwriting the
   current one, and a clear statement of what restore does and does
   not bring back — cross-checked against the sync-conflict resolution
   row. Done when the row passes all quality gates. (Implemented this
   run.)

15. Add a keyboard shortcut reference pattern row to
   `catalog/patterns.md`: a searchable, context-grouped list of
   shortcuts reachable from help, with remapping controls and a
   conflict warning when a new shortcut collides with an existing one
   — distinct from the command palette, which executes commands rather
   than teaching them. Done when the row passes all quality gates.
   (Implemented this run.)

16. Add an undo and trash recovery pattern row to
   `catalog/patterns.md`: an immediate undo offer after a destructive
   action, a trash area with a stated retention period and a
   restore-to-original-place action, and a separate permanent-delete
   step that states what is lost — cross-checked against the version
   history row and the confirmation row. Done when the row passes all
   quality gates. (Implemented this run.)

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
   content, selection, and entered input survive a pane-width change —
   cross-checked against the width-band and foldable-posture rules in
   the same file. Done when the rules pass all quality gates.
   (Implemented this run.)

23. Add a session-expiry warning pattern row to `catalog/patterns.md`:
   warn before a session ends with the time remaining stated plainly,
   offer a keep-working action that preserves entered input, and never
   discard a draft or a form on expiry — the person returns to the
   same place with the same input, or to a saved draft with a clear
   restore step — cross-checked against the draft autosave row and the
   timeout rules in `catalog/states.md`. Done when the row passes all
   quality gates. (Implemented this run.)

24. Add a data export pattern row to `catalog/patterns.md`: export in
   common formats the person can actually open elsewhere, state
   plainly what the export includes and excludes, show progress for
   large exports instead of a silent wait, state how long the download
   link stays live, and handle a partial failure by naming what
   exported and what did not rather than delivering a silent short
   file — cross-checked against the file upload row. Done when the row
   passes all quality gates. (Implemented this run.)

25. Add an account deletion pattern row to `catalog/patterns.md`:
   delete from the same channel used to sign up, state the effect
   before confirmation — what content is removed, what is kept for
   other people, and when removal completes — offer a grace period
   with a plain undo path inside it, and confirm removal in writing
   once it is done — cross-checked against the subscription
   cancellation row and the confirmation row. Done when the row passes
   all quality gates. (Implemented this run.)

19. Add data-table sort-state rules to the Data table row in
   `catalog/patterns.md`: an unsorted column shows a neutral indicator
   distinct from ascending and descending, the current direction is
   visible in the header and announced to assistive technology,
   multi-column sort states its column order and uses a unique field
   as the final tie-breaker so paging stays stable, sorting moves to
   the server once the set exceeds what the client can sort without
   lag, and the sort survives paging and filtering. Done when the
   extended row passes all quality gates. (Implemented this run.)

20. Add form validation timing rules to the Form flow row in
   `catalog/patterns.md`: never flag a field before the person has
   left it or submitted the form, re-validate on each keystroke only
   once a field is already marked invalid so a fix clears at once,
   keep the error message in place and linked to its field rather than
   removing and re-inserting it, focus the first invalid field for a
   single error and an error summary for several, and retain all
   entered input after a failed submission — cross-checked against the
   error state rules in `catalog/states.md`. Done when the extended
   row passes all quality gates.

21. Add contextual guidance rules to the Onboarding row in
   `catalog/patterns.md` and `layouts/onboarding.md`: inline help is
   the default, coach marks appear only when the person first reaches
   the feature they explain, never more than three in a sequence,
   always dismissable, and never a substitute for a clear label or a
   first screen that teaches by doing — cross-checked against the skip
   and progress-persistence rules in the same files. Done when the
   rules pass all quality gates.

22. Add an empty-state fallback rule to the Empty row in
   `catalog/states.md`: the empty state renders as a static fallback
   even when the data request fails, so a failed load never produces a
   blank screen; the fallback states what is missing, offers one next
   action, and states whether a retry will restore the content —
   cross-checked against the error state rules in the same file. Done
   when the extended row passes all quality gates.

26. Add a saved-item collection pattern row to `catalog/patterns.md`:
   save an item with one action, show its saved state wherever the
   item appears, offer named collections with rename and delete
   controls, and state what happens to saved items when the original
   item changes or is removed — cross-checked against the filtering
   and sorting row. Done when the row passes all quality gates.
   (Implemented this run.)

27. Add a bulk-action pattern row to `catalog/patterns.md`: state the
   selection scope before acting (page, filtered set, or all matching
   items), summarise the action and its count for confirmation, report
   per-item failures separately from successes, and offer an undo for
   the whole batch where the action is reversible — cross-checked
   against the confirmation row. Done when the row passes all quality
   gates. (Implemented this run.)

28. Add a rating and review submission pattern row to
   `catalog/patterns.md`: a structured rating with an optional written
   review, an edit window after submission, a plain statement of what
   is shown publicly and what is moderated, and no gating of core
   features behind a rating request — cross-checked against the
   confirmation row. Done when the row passes all quality gates.
   (Implemented this run.)

29. Add a help-search recovery rule to the In-product help row in
   `catalog/patterns.md`: when in-product search returns nothing,
   suggest the nearest topics by wording rather than an empty page,
   and carry the failed query into the escalation path so the person
   never retypes it. Done when the rule passes all quality gates.

30. Add a link-preview rule to the Share link row in
   `catalog/patterns.md`: before sending, show the recipient what the
   link opens, who can open it, and when it expires, with an edit step
   for scope and expiry from the same screen. Done when the rule
   passes all quality gates.

31. Add a method-change rule to the Second-factor sign-in row in
   `catalog/patterns.md`: changing the second-factor method requires a
   successful check with the current method first, and the old method
   stays active until the new one verifies, so a failed switch never
   locks the person out. Done when the rule passes all quality gates.

32. Add a content reporting and blocking pattern row to
   `catalog/patterns.md`: a report action reachable from the item
   itself, a plain choice of reason, a stated outcome for the reported
   item and for the reporter, a block control that hides the blocked
   party everywhere at once, and a review path for a report decided in
   error — cross-checked against the confirmation row. Done when the
   row passes all quality gates. (Implemented this run.)

33. Add a language and locale selection pattern row to
   `catalog/patterns.md`: language names written in their own
   language, a stated scope for the choice (current session or saved
   preference), an immediate preview of the change without losing
   entered input, and a fallback that never strands the person on a
   page they cannot read — cross-checked against the
   internationalization section in `catalog/primitives.md`. Done when
   the row passes all quality gates. (Implemented this run.)

34. Add a scheduled action pattern row to `catalog/patterns.md`: an
   action set for a later time states its scheduled time in plain
   words, stays editable and cancellable until it runs, confirms once
   it has run, and reports a missed or failed scheduled run with a
   retry path rather than silently dropping it — cross-checked against
   the confirmation row and the draft autosave row. Done when the row
   passes all quality gates. (Implemented this run.)

35. Add a payment failure recovery pattern row to
   `catalog/patterns.md`: keep the person in the same checkout with
   the order intact after a failed payment, state the failure in plain
   words with an actionable cause where known, offer retry only where
   it can succeed and another eligible method on the same screen,
   check the real status before any second attempt so one order is
   never charged twice, and hold a pending payment with a stated
   status check rather than showing failure prematurely —
   cross-checked against the checkout variants in
   `layouts/ecommerce.md` and the confirmation row. Done when the row
   passes all quality gates. (Implemented this run.)

36. Add an annotation and comment thread pattern row to
   `catalog/patterns.md`: each thread anchored to the specific
   section, sentence, or element it discusses, with a stated rule for
   threads whose anchor was deleted or heavily rewritten, reply
   nesting with a resolve and reopen path, thread visibility following
   the visibility of the content itself, and an overview listing open
   and resolved threads — distinct from open action 10 (collaborative
   editing presence and field locks) and from the chat and messaging
   row (conversation, not anchored comment). Done when the row passes
   all quality gates. (Implemented this run.)

37. Add a what's-new announcement pattern row to
   `catalog/patterns.md`: grade announcement visibility by impact —
   minor changes stay in the changelog, workflow changes get a
   dismissible in-place announcement, and changes that block a task
   get a prominent once-only notice — with action-oriented wording, a
   direct route to the new capability, a persistent entry point for
   later review, and a seen state so a dismissed announcement is never
   shown again — distinct from onboarding (first use), the
   notification digest (grouped updates), and the install and review
   prompts. Done when the row passes all quality gates. (Implemented
   this run.)

38. Add a breadcrumb navigation pattern row to `catalog/patterns.md`:
   a trail showing the path from the home view to the current page,
   each step a working link except the current page, collapse and
   truncation rules on narrow screens that always keep the home view
   and the parent step reachable, and a stated rule for when a trail
   is omitted (single-level pages and task flows where a trail would
   imply a hierarchy that does not exist) — distinct from the primary
   navigation row, which moves between top-level sections rather than
   showing where the current page sits. Done when the row passes all
   quality gates. (Implemented this run.)

39. Add an account recovery pattern row to `catalog/patterns.md`:
   identify the account without revealing whether it exists, verify
   through a route the person can still reach, let a failed
   verification fall back to another route rather than locking the
   account, restore sessions and saved work after recovery, and state
   plainly what recovery does and does not restore — cross-checked
   against the second-factor sign-in row and the session-expiry
   warning row. Done when the row passes all quality gates.

40. Add a theme selection pattern row to `catalog/patterns.md`: a
   choice between light, dark, and system-following themes with an
   immediate preview that loses no entered input, a saved preference
   that survives visits, a stated rule for what changes when the
   system theme changes, and a guarantee that text stays readable in
   every theme — distinct from the token and contrast rules in
   `trends/2026/dark-mode.md`, which describe how themes are built
   rather than how the choice is offered. Done when the row passes all
   quality gates. (Implemented this run.)

41. Add a profile and account menu pattern row to
   `catalog/patterns.md`: a menu anchored to the current-account
   trigger listing the account's own actions — view account, open
   settings, manage sign-in methods, and sign out — with the active
   account named in text, sign-out kept separate from destructive
   account actions, and a return to the same place after any menu
   action that does not leave the task — distinct from the account
   switcher row, which moves between signed-in accounts, and from the
   settings layout, which is a full page rather than a menu. Done when
   the row passes all quality gates. (Implemented this run.)

42. Add a recently viewed pattern row to `catalog/patterns.md`: a
   recents list that returns the person to items opened before, with
   each entry naming the item and when it was last opened, a stated
   scope for what is remembered, a clear-all control, and a rule for
   items that no longer exist — distinct from the saved-item
   collection row, which keeps items the person chose to keep, and
   from the command palette, which lists recents only as a blank-state
   shortcut. Done when the row passes all quality gates. (Implemented
   this run.)

43. Add an invitation response pattern row to `catalog/patterns.md`:
   an invitation states what is asked, who sent it, and when it needs
   an answer, and offers accept, decline, and tentative replies with a
   stated effect for each; a changed reply updates the organiser and
   the attendees without creating a duplicate item, and a withdrawn or
   expired invitation states plainly that it no longer applies —
   distinct from the calendar and scheduling row, which covers how
   times are shown across zones. Done when the row passes all quality
   gates. (Implemented this run.)

44. Add a modal dialog pattern row to `catalog/patterns.md`: a dialog
   that asks one decision, takes focus on opening and returns it on
   closing, offers a visible dismiss path besides the decision
   actions, traps focus only while open, and never nests a second
   dialog — a second layer of decisions becomes a new view —
   cross-checked against the no-nesting rule in the layout rules of
   the same file. Done when the row passes all quality gates.
   (Implemented this run.)

45. Add a guest checkout pattern row to `catalog/patterns.md`:
   completing a purchase without creating an account, with the order
   and its details preserved if the person later creates an account, a
   stated difference between guest and signed-in checkout (such as
   saved details and order history), and no account creation forced
   mid-checkout — distinct from the checkout variants in
   `layouts/ecommerce.md`, which describe page shapes rather than the
   guest path. Done when the row passes all quality gates.
   (Implemented this run.)

46. Add a time-zone picker pattern row to `catalog/patterns.md`: a
   picker that lists zones by place name with the current local time
   and offset shown for each, searchable by place or zone name,
   ordered by current time rather than alphabet alone, and stating
   plainly whether the chosen zone follows clock changes — distinct
   from the cross-zone scheduling rules, which cover how booked times
   are shown to attendees. Done when the row passes all quality gates.
   (Implemented this run.)

47. Add a pull-to-refresh pattern row to `catalog/patterns.md`: a
   refresh gesture and control for list content, a visible refreshing
   state that never hides the existing list, a stated result after
   refresh (new items, no change, or failure with retry), and a
   keyboard and assistive-technology route that matches the gesture —
   distinct from the offline-first sync row, which covers queued
   changes rather than re-reading content. Done when the row passes
   all quality gates. (Implemented this run.)

48. Add a file preview pattern row to `catalog/patterns.md`: a preview
   shown before opening or downloading a file, with the file name,
   type, and size stated, a readable excerpt or thumbnail where the
   type allows one, and a plain fallback where no preview exists —
   distinct from the file upload row, which covers sending files
   rather than inspecting them. Done when the row passes all quality
   gates.

49. Add a search history pattern row to `catalog/patterns.md`: past
   queries kept as a list the person can re-run, edit, or delete one
   at a time or all at once, with a stated retention scope — distinct
   from the recently viewed row, which lists opened items rather than
   queries, and from the search row, which covers finding content.
   Done when the row passes all quality gates.

50. Add an accessibility preferences pattern row to
   `catalog/patterns.md`: text size, bold text, increased contrast,
   reduced motion, reduced transparency, and captions gathered in one
   reachable place, each applied at once to a live preview, a stated
   rule for where a choice follows the system and where it overrides
   it, a single reset to the starting values, and a saved preference
   across visits — distinct from theme selection, which chooses
   colours rather than size, contrast, motion, and captions. Done when
   the row passes all quality gates. (Implemented this run.)

51. Add a long-document navigation pattern row to
   `catalog/patterns.md`: a sticky outline of the page headings with
   the current section marked in text as well as in shape, jump links
   that move focus to the section heading, a collapse to a single
   outline control on narrow screens, and a return to the top that
   never loses the person's place in a form — distinct from breadcrumb
   navigation, which shows where the page sits in a hierarchy rather
   than where the person sits in a long page. Done when the row passes
   all quality gates. (Implemented this run.)

52. Add an in-app update prompt pattern row to `catalog/patterns.md`:
   a flexible prompt that downloads in the background and lets the
   person keep working, a blocking prompt reserved for versions that
   can no longer work safely, a stated deferral limit and deadline for
   the flexible prompt, no prompt during a task or a payment, and a
   resume step after an interrupted update — distinct from the
   what's-new announcement row, which reports changes rather than
   requiring an update. Done when the row passes all quality gates.
   (Implemented this run.)

53. Add a scrolling tab bar pattern row to `catalog/patterns.md`: a
   tab list that scrolls horizontally when tabs overflow the available
   width, with a visible affordance that more tabs exist beyond the
   edge, arrow-key movement between tabs, the current tab marked in
   text as well as in shape, and a stated rule for when tabs collapse
   into a menu instead — distinct from the primary navigation row,
   which moves between top-level sections, and from the mobile tab
   bar, which is a fixed bottom control rather than a scrolling list.
   Done when the row passes all quality gates. (Implemented this run.)

54. Add a system share sheet pattern row to `catalog/patterns.md`:
   sharing content through the platform share sheet, with a preview of
   exactly what will be shared, recent targets offered first, a cancel
   path that shares nothing, and a fallback route where no share sheet
   exists — distinct from the share link row, which covers link scope
   and expiry rather than the sheet itself. Done when the row passes
   all quality gates. (Implemented this run.)

55. Add a find-in-page pattern row to `catalog/patterns.md`: searching
   within the current long page or document, with a persistent query,
   a match count, next and previous controls, highlighted matches,
   focus moved to the matched text, and a dismiss step that returns to
   the previous place — distinct from the search row, which finds
   content across the product, and from the long-document navigation
   row, which outlines sections rather than searching text. Done when
   the row passes all quality gates. (Implemented this run.)

56. Add a text-selection action menu pattern row to
   `catalog/patterns.md`: actions offered on selected text — copy,
   share, and define — shown near the selection without covering it,
   dismissed by tapping elsewhere or pressing escape, and never
   replacing the selection itself — distinct from the inline assistant
   actions row, which acts on a selected object rather than on
   selected text. Done when the row passes all quality gates.

57. Add a no-results recovery rule to the Search row in
   `catalog/patterns.md`: when a query returns nothing, state plainly
   that nothing matched, offer one spelling or scope correction, and
   keep the query editable in place with a route back to the full list
   — distinct from the zero-result metric in the same row, which
   measures the problem rather than repairing it. Done when the rule
   passes all quality gates.

58. Add a print-friendly view pattern row to `catalog/patterns.md`: a
   reading view that removes navigation and interactive controls for
   printing, keeps headings and tables intact across page breaks, and
   states the page count before printing — distinct from the
   long-document navigation row, which moves within a screen rather
   than preparing it for print. Done when the row passes all quality
   gates.

59. Add a toast feedback pattern row to `catalog/patterns.md`: a short
   non-blocking confirmation after an action completes, with a visible
   duration and a manual dismiss control, reserved for low-stakes
   confirmations only — never for errors, failures, or actions that
   need a decision — distinct from the notification escalation row,
   which grades interruption by urgency, and from the confirmation
   row, which asks before an action. Done when the row passes all
   quality gates. (Implemented this run.)

60. Add a list reorder pattern row to `catalog/patterns.md`: reorder
   items by drag with a visible drop preview, keyboard and button
   alternatives that never rely on drag alone, a live announcement of
   the new position, and a cancel path that restores the original
   order — distinct from the column reorder controls in the data table
   row, which arrange columns rather than list items, and from the
   drag-between-panes rules in `layouts/tablet.md`. Done when the row
   passes all quality gates. (Implemented this run.)

61. Add a date-range picker pattern row to `catalog/patterns.md`: pick
   a start and an end date in one control, with preset ranges for
   common spans, prevention of an end before a start, a stated rule
   for whether both ends are included, and a plain statement of the
   chosen span before it applies — distinct from the calendar and
   scheduling row, which shows objects in time rather than collecting
   a range value, and from the time-zone picker row, which chooses a
   zone rather than dates. Done when the row passes all quality gates.
   (Implemented this run.)

62. Add an overflow menu pattern row to `catalog/patterns.md`:
   secondary actions that do not fit the primary surface gathered in
   one menu anchored to its trigger, with the trigger naming what it
   opens, the menu closing on selection, on dismiss, and on focus
   leaving it, and destructive actions kept out of the overflow menu
   or separated plainly — distinct from the profile and account menu
   row, which lists account actions, and from the command palette row,
   which executes typed commands. Done when the row passes all quality
   gates.

63. Add an aggregate rating display pattern row to
   `catalog/patterns.md`: a read-only summary showing the average, the
   count of ratings, and the spread across rating values, with a
   stated rule for which ratings count and a filter for verified
   ratings where verification exists — distinct from the rating and
   review submission row, which collects a rating, and from the review
   prompt row, which asks for one. Done when the row passes all
   quality gates.

64. Add a setup checklist pattern row to `catalog/patterns.md`: an
   ordered list of setup tasks with done, current, and remaining
   states, a resume point that returns the person to the first
   unfinished task, and a skip path that keeps skipped tasks reachable
   — distinct from the onboarding row, which teaches a first run, and
   from the wizard row, which completes one task in steps. Done when
   the row passes all quality gates.

65. Add an accordion disclosure pattern row to `catalog/patterns.md`:
   one heading button per section with the expanded or collapsed state
   stated in text as well as in shape, focus kept on the header when
   toggling, sections opening independently unless a one-open rule is
   stated up front, a single reveal kept as a simple disclosure and
   peer sections kept as tabs, and never the only route to a task
   hidden inside a collapsed panel — distinct from the scrolling tab
   bar row, which moves between sections of one view, and from the
   tooltip primitive, which supplements a label rather than hiding
   content. Done when the row passes all quality gates. (Implemented
   this run.)

66. Add a carousel pattern row to `catalog/patterns.md`: a rotating
   set of slides or cards with previous, next, and slide-picker
   controls that name each slide, a visible pause control for any
   auto-rotation that also stops on focus or hover and starts stopped
   where reduced motion is preferred, a stated slide position, and a
   keyboard route that never relies on drag or swipe alone — distinct
   from the media viewer row, which inspects one visual in depth, and
   from the image gallery viewer row, which browses a set of images
   without rotation. Done when the row passes all quality gates.
   (Implemented this run.)

67. Add a passkey sign-in pattern row to `catalog/patterns.md`:
   sign-in with a device-held credential unlocked by the device's own
   check, offered beside a visible fallback route rather than as the
   only option, a plain explanation of what the device check is before
   the system prompt appears, a cross-device route with its context
   stated before any code is shown, and a recovery path for a lost
   device that never strands the account — distinct from the
   second-factor sign-in row, which adds a second check after a first,
   and from the account recovery row, which restores access after it
   is lost. Done when the row passes all quality gates.

68. Add a low-bandwidth mode pattern row to `catalog/patterns.md`: a
   stated mode that reduces media weight, defers non-essential
   content, and keeps text, navigation, forms, and actions fully
   usable, offered as a person-controlled choice and honoured where
   the system already signals a data-saving preference, with a plain
   statement of what the mode changes and a one-action return to the
   full view — distinct from the offline-first sync row, which queues
   changes without a connection, and from the simplified view row,
   which reduces cognitive load rather than data weight. Done when the
   row passes all quality gates. (Implemented this run.)

69. Add an external-link departure pattern row to
   `catalog/patterns.md`: before leaving the current service, state
   the destination in plain words, state that it opens elsewhere, and
   keep a return route to the task left behind — distinct from the
   share link row, which sends the person's own item elsewhere, and
   from the in-product help row, which opens help in place. Done when
   the row passes all quality gates. (Implemented this run.)

70. Add a described-media pattern row to `catalog/patterns.md`: where
   media carries visual information beyond dialogue, offer a
   description track as a named choice beside captions, keep the
   description separate from the dialogue so neither drowns the other,
   and state plainly where no description exists — distinct from the
   media controls primitive, which operates playback, and from the
   captions rule, which transcribes speech. Done when the row passes
   all quality gates. (Implemented this run.)

71. Add a saved-cart recovery pattern row to `catalog/patterns.md`:
   when a person returns to a saved cart, state what is still
   available, what changed in price or availability, and what expired,
   with a one-action removal for unavailable items and the order kept
   intact otherwise — distinct from the saved-item collection row,
   which saves single items, and from the payment failure recovery
   row, which preserves an order after a failed payment. Done when the
   row passes all quality gates. (Implemented this run.)

72. Add a home-screen widget pattern row to `catalog/patterns.md`: a
   glanceable summary with size tiers, a tap route to the matching
   view, a stated refresh cadence, and empty, loading, and error
   states that never hide the task — distinct from the notification
   list row, which reports events, and from the simplified view row,
   which reduces a full view rather than summarising it from outside.
   Done when the row passes all quality gates. (Implemented this run.)

73. Add a deep-link landing pattern row to `catalog/patterns.md`: a
   link from outside lands on the exact content with its owning
   navigation selected, a plain fallback surface where the content is
   no longer available, and a return route to the section root —
   distinct from the external-link departure row, which leaves the
   current service, and from the share link row, which sends the
   person's own item elsewhere. Done when the row passes all quality
   gates.

74. Add a progressive disclosure pattern row to `catalog/patterns.md`:
   a collapsed preview with an expand control, the expanded state
   stated in text as well as in shape, content kept in reading order
   when expanded, and the expanded state kept where returning matters
   — never the only route to a task hidden inside a collapsed block —
   distinct from the accordion disclosure row, which organises
   sections under headings, and from the long-document navigation row,
   which moves within a page. Done when the row passes all quality
   gates. (Implemented this run.)

75. Add a colour picker pattern row to `catalog/patterns.md`: named
   swatches rather than colour names alone, a keyboard-operable
   picker with a typed value entry beside the visual control, a
   contrast check against the surface it will sit on, and a stated
   value that never relies on colour alone — distinct from the
   filtering and sorting swatch rule, which selects among existing
   options, and from the theme selection row, which applies a whole
   palette. Done when the row passes all quality gates. (Implemented this run.)

76. Add a guest-to-account conversion pattern row to
   `catalog/patterns.md`: after a guest purchase, offer a single-step
   account creation that reuses the order details already given,
   states plainly what the account adds, and never re-asks for
   information just entered — distinct from the guest checkout row,
   which keeps purchase possible without an account, and from the
   account deletion row, which closes an account. Done when the row
   passes all quality gates.

77. Add a sensitive-content preview pattern row to
   `catalog/patterns.md`: content that may distress or surprise
   first shows a plain preview stating what kind of content follows
   and why it is flagged, with an explicit reveal control and the
   choice remembered per content type — distinct from the consent
   choice row, which asks permission for data use, and from the
   notification grouping rules, which summarise events. Done when the
   row passes all quality gates. (Implemented this run.) (Implemented this run.)

78. Add a time picker pattern row to `catalog/patterns.md`: a typed
   time entry beside a visual picker, preset times for common
   choices, a plain statement of the time-zone context where it
   matters, and a 12-hour / 24-hour display that follows the
   person's locale setting — distinct from the date-range picker
   row, which collects a span of dates, and from the time-zone
   picker row, which chooses a zone by place. Done when the row
   passes all quality gates. (Implemented this run.)

79. Add a verification-code entry pattern row to `catalog/patterns.md`:
   a single-field entry that accepts pasted codes, per-digit
   advancement only where it never traps focus, a stated expiry
   and resend route, and an error message that names the problem
   without locking the person out — distinct from the second-factor
   sign-in row, which chooses the factor, and from the passkey
   sign-in row, which avoids codes entirely. Done when the row
   passes all quality gates. (Implemented this run.)

80. Add a background-task progress pattern row to `catalog/patterns.md`:
   a long-running task that continues away from its starting view
   states its progress, offers pause and cancel where safe, and
   reports completion or failure in place with a return route —
   distinct from the wizard row, which steps through a task in
   view, and from the toast feedback row, which confirms a task
   already finished. Done when the row passes all quality gates. (Implemented this run.)

81. Add an order tracking pattern row to `catalog/patterns.md`: a
   staged progress view naming the current stage in plain words,
   a stated delivery window with a revised window and reason
   where delayed, a support route attached to delays and failed
   deliveries, and split shipments labelled as separate stages —
   distinct from the saved-cart recovery row, which revisits an
   unfinished cart, and from the notification escalation row,
   which routes urgent updates. Done when the row passes all
   quality gates.

82. Add an automated-to-human support handoff pattern row to
   `catalog/patterns.md`: handoff triggers that fire on an
   explicit request for a person, on repeated unhelpful answers,
   and where the next step needs authority the automated help
   does not hold; full conversation context carried across so
   nothing is re-asked, and a stated next step with a waiting
   route where no person is available — distinct from the
   in-product help row, which opens help in place, and from
   the agent checkpoint row, which approves an automated task.
   Done when the row passes all quality gates. (Implemented this run.)

83. Add a subscription plan change pattern row to
   `catalog/patterns.md`: a before-and-after statement of price,
   entitlements, and effective date shown before confirmation,
   upgrades taking effect at once with the prorated charge
   stated, downgrades taking effect at the next renewal with
   the higher tier kept until then, and a stated route back —
   distinct from the subscription cancellation row, which ends
   a subscription, and from the paywall row, which first offers
   a paid tier. Done when the row passes all quality gates. (Implemented this run.)

84. Add a promo-code entry pattern row to `catalog/patterns.md`:
   a collapsed entry that keeps checkout uncluttered, instant
   confirmation with the discount shown as a line item beside
   the recalculated total, a named reason where a code fails
   (expired, already used, below the qualifying spend, or not
   matching the items), and a one-action removal — distinct
   from the guest checkout row, which collects payment details,
   and from the payment failure recovery row, which preserves
   an order after a failed payment. Done when the row passes
   all quality gates. (Implemented this run.)


85. Add a poll and voting pattern row to `catalog/patterns.md`: a
   single question with a stated vote rule, results shown as counts
   and shares in text as well as in shape, a stated rule for whether
   results appear before or after voting, a change-vote route where
   votes may change, and a plain closed state once voting ends —
   distinct from the rating and review submission row, which judges
   a single item, and from the annotation and comment thread row,
   which holds discussion. Done when the row passes all quality
   gates.

86. Add an age verification gate pattern row to
   `catalog/patterns.md`: a gate that states the age requirement and
   why it applies, asks only for the threshold where that suffices
   rather than full identity details, offers a plain decline route
   with somewhere useful to go, and remembers the answer only where
   that is appropriate — distinct from the consent choice row, which
   asks permission for data use, and from the passkey sign-in row,
   which proves a credential. Done when the row passes all quality
   gates.

87. Add a limited-time offer countdown pattern row to
   `catalog/patterns.md`: a countdown shown beside the exact end
   time and its zone, a timer that never resets on revisit, a plain
   statement of what happens when the time runs out, and the offer
   terms reachable from the countdown itself — distinct from the
   session-expiry warning row, which ends a session, and from the
   scheduled action row, which runs an action at a future time.
   Done when the row passes all quality gates.

88. Add a master-detail pattern row to `catalog/patterns.md`: a
   list beside its detail on wide screens, the selected item
   stated in text as well as in shape, the detail updating
   without losing the list position, a stacked list-then-detail
   route with a clear back step on narrow screens, and a stated
   empty detail state before anything is selected — distinct
   from the detail view row, which inspects one item without a
   sibling list, and from the data table row, which compares
   rows rather than pairing a list with its detail. Done when
   the row passes all quality gates.

89. Add a threaded message reply pattern row to `catalog/patterns.md`: a
   reply anchored to the message it answers, a thread view that
   keeps the original message visible, an unread count per thread
   stated in text, and a return route from the thread to the
   main conversation — distinct from the annotation and comment
   thread row, which anchors discussion to document content, and
   from the message edit and delete row, which changes a message
   rather than answering it. Done when the row passes all quality
   gates.

90. Add a gift option pattern row to `catalog/patterns.md`: an
   option at checkout marking an order as a gift, prices hidden
   from the recipient, an optional gift message shown to the
   recipient, and a separate delivery address for the gift that
   never overwrites the buyer's own address — distinct from the
   guest checkout row, which completes a purchase without an
   account, and from the saved-cart recovery row, which revisits
   an unfinished cart. Done when the row passes all quality
   gates.

91. Add a saved address selection pattern row to `catalog/patterns.md`: a
   named list of saved addresses with a clear default, a one-action
   choice at checkout, an edit route that never overwrites another
   saved address, and a plain statement of which address receives
   the order — distinct from the location selection row, which
   picks a place on a map, and from the gift option row, which
   takes a separate recipient address for one order. Done when the
   row passes all quality gates. (Implemented this run.)

92. Add a delivery slot picker pattern row to `catalog/patterns.md`: a
   choice of delivery window at checkout with available windows
   stated, unavailable windows marked as unavailable with a reason,
   a stated cut-off time for each window, and the chosen window
   carried into the order confirmation — distinct from the order
   tracking row, which states a window after placement, and from
   the scheduled action row, which runs an action at a future time.
   Done when the row passes all quality gates. (Implemented this run.)

93. Add a product variant selection pattern row to `catalog/patterns.md`:
   a choice among variants of one product with the price and
   availability updated for the chosen combination, unavailable
   combinations marked as unavailable rather than silently
   disappearing, and a stated route back when a chosen combination
   cannot be supplied — distinct from the filtering and sorting
   row, which narrows a list of products, and from the data table
   row, which compares separate items. Done when the row passes
   all quality gates. (Implemented this run.)

94. Add a saved payment method selection pattern row to
   `catalog/patterns.md`: a named list of saved payment methods
   with a clear default, a one-action choice at checkout, an
   edit and removal route that never exposes full payment
   details, and a plain statement of which method will be
   charged before payment — distinct from the payment failure
   recovery row, which preserves an order after a failed
   payment, and from the guest checkout row, which completes a
   purchase without a saved account. Done when the row passes
   all quality gates.

95. Add a return and exchange request pattern row to
   `catalog/patterns.md`: a request started from the order
   itself naming the item and the reason in plain words, a
   stated choice between return, exchange, and refund where
   each applies, a stated label and drop-off or pickup route,
   and a stated status for the request until the outcome is
   settled — distinct from the order tracking row, which
   follows a delivery forward, and from the saved-cart
   recovery row, which revisits an unfinished cart. Done when
   the row passes all quality gates.
   (Implemented this run.)

96. Add a back-in-stock alert request pattern row to
   `catalog/patterns.md`: a request for one unavailable item
   stating plainly what the alert covers and how it arrives,
   a single alert per restock rather than repeated messages,
   a stated route to stop the alerts, and the item's
   availability re-checked at the moment the alert is opened
   rather than promised in the message — distinct from the
   notification digest row, which groups low-urgency updates,
   and from the in-app update prompt row, which requires an
   update rather than reporting availability. Done when the
   row passes all quality gates.
   (Implemented this run.)

97. Add an order cancellation pattern row to `catalog/patterns.md`:
   a cancel action offered from the order itself while it can
   still be stopped, a plain statement of whether cancellation
   is still possible and until when, partial cancellation of
   the unfulfilled part where part of the order has shipped, a
   confirmation stating what is cancelled and what refund
   follows and when, and a cancelled order kept visible with
   its refund state rather than deleted — distinct from the
   subscription cancellation row, which ends a recurring plan,
   and from the order tracking row, which follows an order
   forward. Done when the row passes all quality gates.
   (Implemented this run.)

98. Add an in-product feedback and problem report pattern row
   to `catalog/patterns.md`: a report entry reachable from
   every screen without leaving the task, a plain choice of
   what went wrong, an optional screenshot or screen capture
   attached with consent, the current screen and task carried
   into the report so nothing is retyped, and a stated
   follow-up route rather than a silent submission — distinct
   from the content reporting and blocking row, which reports
   an item rather than a problem with the product, and from
   the rating and review submission row, which judges a
   single item. Done when the row passes all quality gates.

99. Add a gift card and stored-credit redemption pattern row
   to `catalog/patterns.md`: a code entry at checkout that
   applies stored value as a payment line, a stated remaining
   balance after a partial redemption, a plain statement of
   what happens when the stored value covers only part of
   the total, a balance check route outside checkout, and a
   stated expiry or no-expiry rule before the code is applied
   — distinct from the promo-code entry row, which applies a
   discount rather than spending stored value, and from the
   gift option row, which marks an order as a gift rather
   than paying for it. Done when the row passes all quality
   gates.

100. Add a contact picker pattern row to `catalog/patterns.md`: a
   named list of contacts with a search field, a one-action choice
   that carries only the chosen contact into the task, a stated
   scope for what the contact is used for, and a plain route to
   add a contact that is missing — distinct from the invitation
   response row, which answers an invitation, and from the share
   link row, which sends an item elsewhere. Done when the row
   passes all quality gates.
   (Implemented this run.)

101. Add an offline download pattern row to `catalog/patterns.md`:
   a download action stating size and storage before starting,
   progress with pause and resume, a stated expiry where downloaded
   content expires, and removal that frees storage at once —
   distinct from the offline-first sync row, which queues changes
   without a connection, and from the file upload row, which sends
   content rather than fetching it. Done when the row passes all
   quality gates.
   (Implemented this run.)

102. Add a sensitive-action re-confirmation pattern row to
   `catalog/patterns.md`: before a consequential action such as
   changing payment details or deleting shared content, ask for a
   fresh confirmation tied to that action, state plainly what will
   change, and never reuse an old sign-in as silent approval —
   distinct from the second-factor sign-in row, which adds a check
   at sign-in, and from the confirmation row, which confirms an
   ordinary action. Done when the row passes all quality gates.
   (Implemented this run.)

103. Add a delivery instructions pattern row to
   `catalog/patterns.md`: a place at checkout to state where
   an order should be left and any access note the carrier
   needs, carried into the delivery record and shown back to
   the person before payment, with a plain route to change it
   while the order can still be changed — distinct from the
   delivery slot picker row, which chooses when a delivery
   arrives, and from the saved address selection row, which
   chooses a stored address. Done when the row passes all
   quality gates.
   (Implemented this run.)

104. Add a payment instalment plan pattern row to
   `catalog/patterns.md`: a choice at checkout to spread one
   total across a stated number of dated payments, each
   payment's amount and date shown before confirmation, a
   stated total cost including any charges, and a stated
   route to view remaining payments and change the payment
   method — distinct from the split payment row, which
   divides one total across payers or methods at once, and
   from the saved payment method selection row, which
   chooses a single method for the whole order. Done when
   the row passes all quality gates.
   (Implemented this run.)

105. Add a subscribe-and-save purchase option pattern row to
   `catalog/patterns.md`: a recurring purchase choice beside
   the one-time purchase, stating the repeat interval, the
   price that applies to repeats, and a plain route to pause,
   skip, change, or cancel before the next order — distinct
   from the subscription plan change row, which changes a
   service tier, and from the reorder past order row, which
   repeats a past order on demand. Done when the row passes
   all quality gates.
   (Implemented this run.)

106. Add a pickup point selection pattern row to
   `catalog/patterns.md`: a choice at checkout to collect an
   order from a named pickup point, with distance and opening
   hours stated for each point, a stated holding period after
   arrival, and a plain route to change the point while the
   order can still be changed — distinct from the delivery
   slot picker row, which chooses when a delivery arrives,
   and from the saved address selection row, which chooses a
   stored address. Done when the row passes all quality
   gates.
   (Implemented this run.)

107. Add a referral invitation pattern row to
   `catalog/patterns.md`: a shareable invitation stating
   plainly what the inviter and the invitee each receive, a
   stated state for each invitation sent, accepted, and
   completed, and a route to withdraw an invitation that has
   not been accepted — distinct from the invitation response
   row, which answers an invitation, and from the share link
   row, which sends an item elsewhere. Done when the row
   passes all quality gates.

108. Add a household member management pattern row to
   `catalog/patterns.md`: a member list stating each
   member's role in plain words, an invite route that states
   what the new member can see and change, a role-change
   control with its effect stated before confirmation, and a
   removal route that states what the removed member loses
   access to — distinct from the account switcher row, which
   moves between signed-in accounts, and from the invitation
   response row, which answers a single invitation. Done
   when the row passes all quality gates.

109. Add a pass and ticket display pattern row to
   `catalog/patterns.md`: a display for a pass or ticket held
   for later use, with a scannable code shown large enough to
   scan, brightness raised while it is displayed, availability
   without a connection, and a stated route when the code
   cannot be scanned — distinct from the code scanner row,
   which captures a code, and from the order tracking row,
   which follows an order's progress. Done when the row
   passes all quality gates.

110. Add a shared cart pattern row to `catalog/patterns.md`:
   a cart several people can add to, with each item naming
   who added it, a stated owner for checkout, and a plain
   rule for removing another person's item — distinct from
   the split payment row, which divides payment, and from
   the saved-item collection row, which keeps items for one
   person. Done when the row passes all quality gates.

111. Add a stored payment method expiry warning pattern row
   to `catalog/patterns.md`: a warning before a stored
   method expires, stating which method and when, with a
   replacement route that keeps future orders and plans
   working — distinct from the saved payment method
   selection row, which chooses a method, and from the
   payment failure recovery row, which recovers after a
   failure. Done when the row passes all quality gates.

## Review notes

- Completed this review (deep editorial 2026-10-30): new
  Return and exchange request, Back-in-stock alert request,
  and Contact picker pattern rows in `catalog/patterns.md`,
  completing roadmap actions 95, 96, and 100; coverage
  matrix updated with the three new rows; three new
  improvement actions added (103 delivery instructions, 104
  payment instalment plan, 105 subscribe-and-save purchase
  option); 3 new source records (390 total).

- Completed this review (deep editorial 2026-10-30): new
  Home-screen widget, Deep-link landing, and Progressive
  disclosure pattern rows in `catalog/patterns.md`, completing
  roadmap actions 72, 73, and 74; coverage matrix updated with
  the three new rows; three new improvement actions added (100
  contact picker, 101 offline download, 102 sensitive-action
  re-confirmation); 3 new source records (368 total).


- Completed this review (deep editorial 2026-10-30): new
  Delivery slot picker pattern row in `catalog/patterns.md`
  (date first, then only windows still open for that date,
  unavailable windows marked with a reason in words, cut-off
  times stated in the person's own zone, availability
  re-checked at confirmation with the nearest open window
  offered where a chosen window fills, chosen window carried
  into the confirmation); new Product variant selection
  pattern row (one control per option group, price, image,
  and availability updated together on a complete choice,
  unavailable combinations marked in place with reasons,
  options ruled out by another choice marked at once, add
  action held until every group has a choice, nearest
  available combination offered where a choice cannot be
  supplied, an arrived-with combination preselected exactly).
  Saved address selection row already present from earlier
  local work is now marked as completing action 91.
  Completes roadmap actions 91, 92, and 93; actions 94, 95,
  and 96 added as follow-ups. Coverage matrix updated with
  the three new rows; 3 new source records (351 total).

- Completed this review (deep editorial 2026-10-29): new
  Master-detail pattern row in `catalog/patterns.md` (list beside
  detail on wide screens, selected item stated in words as well as
  in shape, list position kept on selection change, stacked
  list-then-detail route with a clear back step on narrow screens,
  stated empty detail placeholder before selection); new Threaded
  message reply pattern row (reply anchored to its message, thread
  view keeping the original visible, reply and unread counts stated
  in text, replies staying in the thread unless explicitly shared
  to the main conversation, clear return route, shallow nesting);
  new Gift option pattern row (gift choice before payment, per-item
  choice for mixed orders, prices hidden from the recipient while
  the buyer still sees full totals, gift message with a stated
  length limit, separate recipient address never overwriting the
  buyer's own address). Completes roadmap actions 88, 89, and 90;
  actions 91, 92, and 93 added as follow-ups. Coverage matrix
  updated with the three new rows; 3 new source records (347 total).

- Completed this review (deep editorial 2026-10-29): new
  Automated-to-human support handoff pattern row in
  `catalog/patterns.md` (triggers for an explicit request,
  repeated unhelpful answers, and steps needing authority
  automated help does not hold; a saved case carrying the
  stated issue, steps tried, and details already given; queue
  position and waiting route stated; a stated next step where
  no person is available); new Subscription plan change pattern
  row (before-and-after comparison of price, entitlements, and
  effective date before confirmation; upgrades at once with the
  prorated charge stated; downgrades at the next renewal with
  the higher tier kept until then); new Promo-code entry
  pattern row (collapsed entry, discount as a line item beside
  the recalculated total, named failure reasons, stated
  one-code limit, one-action removal). Completes roadmap
  actions 82, 83, and 84; actions 88, 89, and 90 added as
  follow-ups. Coverage matrix updated with the three new rows.
  3 new source records (343 total).

- Completed this review (deep editorial 2026-10-29): new Colour
  picker pattern row in `catalog/patterns.md` (named swatches with
  a stated value in text, keyboard-operable picker with a typed
  value entry, contrast check against the target surface); new
  Guest-to-account conversion pattern row (single optional step
  after confirmation reusing order details, plain benefit
  statement, existing-account link route, guest lookup route kept
  for anyone who declines); new Sensitive-content preview pattern
  row (plain preview stating kind and reason, explicit reveal
  only, per-type remembered choice, hide-again control, private
  material kept out of the page until revealed). Completes roadmap
  actions 75, 76, and 77; actions 78, 79, and 80 added as
  follow-ups. Coverage matrix updated with the three new rows.
  3 new source records (324 total).

- Completed this review (deep editorial 2026-10-28): new Carousel
  pattern row in `catalog/patterns.md` (named slide-picker controls,
  stated position, visible pause control that also stops on focus or
  hover and never restarts after a deliberate pause, stopped start
  where reduced motion is preferred, keyboard and pointer routes
  for every change, never the only route to a task inside rotation);
  new Passkey sign-in pattern row (device-held credential beside a
  visible fallback, plain explanation before the device prompt,
  cross-device context stated before any code is shown, named
  credentials with a revoke control each, one-time enrolment prompt,
  recovery path for a lost device); new Low-bandwidth mode pattern
  row (person-controlled choice honoured where a data-saving
  preference is already signalled, plain statement of what changes,
  visible content first with labelled load-on-request placeholders,
  text, navigation, forms, and actions fully usable, one-action
  return to the full view). Completes roadmap actions 66, 67, and
  68; actions 69, 70, and 71 added as follow-ups. Coverage matrix
  updated with the three new rows. 1 new source record (311 total).

- Completed this review (daily planning 2026-10-28): research
  pass of 4 searches covering accordion disclosure, passkey
  sign-in, carousel auto-rotation, and low-bandwidth design; 3
  new source records (310 total), URLs copied verbatim from
  results and deduplicated against the existing set, with the
  passkey topic supported by records already in the set. Four
  new actions added (65–68), ordered by coverage impact;
  action 65 implemented this run as the Accordion disclosure
  row in `catalog/patterns.md` (heading-wrapped buttons with
  the expanded state stated in text and shape, focus kept on
  the header, independent sections unless a one-open rule is
  stated, single reveals kept as disclosures, peer sections
  kept as tabs, no task route hidden only inside a collapsed
  panel). Actions 66, 67, and 68 left to the deep cycle.
  Action 60 marked implemented to match its existing List
  reorder row and CHANGELOG entry. Since the last daily run,
  the deep cycle completed actions 59, 60, and 61 and added
  actions 62, 63, and 64, and a light cycle added
  faceted-filter accessibility rules to the Filtering and
  sorting row; those outcomes are already recorded in
  `CHANGELOG.md`, and the light cycles since then reported no
  changes.

- Completed this review (deep editorial 2026-10-28): new Toast
  feedback pattern row in `catalog/patterns.md` (one short line
  naming what completed, one consistent placement, duration scaled
  to message length, manual dismiss with the timer paused on focus
  or hover, polite announcement without moving focus, one toast at
  a time, never for errors, failures, decisions, or promotion); new
  List reorder pattern row (drag with a visible drop preview plus
  move controls and a keyboard path for every item, announced new
  position, cancel restoring the original order, manual reordering
  disabled while sorted by another attribute); new Date-range
  picker pattern row (one linked span with hover preview of the
  span as it forms, presets setting both ends in one action, two
  months side by side on wide screens, end-before-start prevented
  or swapped with a plain statement, stated inclusion rule for
  both ends, chosen span stated in plain words before it applies).
  Completes roadmap actions 59, 60, and 61; actions 62, 63, and 64
  added as follow-ups. Coverage matrix updated with the three new
  rows. 3 new source records (306 total).

- Completed this review (deep editorial 2026-10-27): new
  Collaborative editing presence pattern row in
  `catalog/patterns.md` (presence list naming each person in text
  as well as in colour, visible hold on the field being edited,
  warning before an overwrite with the sync-conflict rules as the
  fallback, presence kept separate from read and approval
  signals); new Draft autosave and recovery pattern row
  (continuous saving with a visible last-saved indicator, restore
  after interruption with a clear review step, draft and delivery
  states kept separate, explicit discard path, stated scope and
  retention period); new Saved-filter view pattern row (named
  view storing a filter combination as a definition that stays
  current, rename and delete controls, stated private or shared
  scope, visible stale marker with a repair step, query text kept
  out unless chosen). Completes roadmap actions 10, 11, and 13;
  actions 59, 60, and 61 added as follow-ups. Coverage matrix
  updated with the three new rows. 3 new source records (301
  total).

- Completed this review (deep editorial 2026-10-27): new
  Long-document navigation pattern row in `catalog/patterns.md`
  (heading-built outline labelled as the page outline, current
  section marked in text and shape, sticky outline on wide
  screens with a single collapsed control on narrow screens,
  focus-moving jump links, form-safe return to top); new
  In-app update prompt pattern row (flexible background
  download versus blocking prompt for versions that can no
  longer work safely, stated deferral limit and deadline, no
  prompt during a task or a payment, chosen-moment restart
  and resume after an interrupted update); new Pull-to-refresh
  pattern row (gesture plus a visible control, threshold
  cancel, list kept visible during refresh, stated result
  with place kept). Completes roadmap actions 47, 51, and 52;
  actions 53, 54, and 55 added as follow-ups. Coverage matrix
  updated with the three new rows. 3 new source records (290
  total).

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

- Completed this review (deep editorial 2026-10-28): new What's-new
  announcement and Version history and restore pattern rows in
  `catalog/patterns.md`, completing roadmap actions 37 and 14 — the
  announcement row also resolves the cross-reference already present in
  the in-app update prompt row; mobile navigation layout deepened
  (badge semantics, per-tab back stacks, deep-entry landing); coverage
  matrix updated with both new rows; three new improvement actions
  added (72 home-screen widget, 73 deep-link landing, 74 progressive
  disclosure); 3 new source records (315 total).

- Completed this review (deep editorial 2026-10-28): new
  External-link departure, Described media, and Saved-cart recovery
  pattern rows in `catalog/patterns.md`, completing roadmap actions
  69, 70, and 71; coverage matrix updated with all three new rows;
  three new improvement actions added (75 colour picker, 76
  guest-to-account conversion, 77 sensitive-content preview); 2 new
  source records (319 total).

- Completed this review (deep editorial 2026-10-29): new Time
  picker, Verification-code entry, and Background-task progress
  pattern rows in `catalog/patterns.md`, completing roadmap actions
  78, 79, and 80; coverage matrix updated with the three new rows;
  three new improvement actions added (85 poll and voting, 86 age
  verification gate, 87 limited-time offer countdown); 3 new source
  records (331 total).

- Completed this review (daily planning 2026-10-30): new
  Order cancellation pattern row in `catalog/patterns.md`
  (cancel from the order itself while it can still be
  stopped, a stated cancellable window, partial cancellation
  where part of the order shipped, a confirmation stating
  the refund and its timing, and a cancelled order kept
  visible with its refund state); three new improvement
  actions added (97 order cancellation, 98 in-product
  feedback and problem report, 99 gift card and
  stored-credit redemption); coverage matrix updated with
  the new row; 3 new source records (358 total).
- Completed this review (deep editorial 2026-10-30): new
  Offline download, Sensitive-action re-confirmation, and
  Delivery instructions pattern rows in `catalog/patterns.md`,
  completing roadmap actions 101, 102, and 103; coverage
  matrix refreshed to match the actual catalogue (page
  pattern list extended with all rows added since the last
  matrix refresh); three new improvement actions added (106
  pickup point selection, 107 referral invitation, 108
  household member management); 3 new source records (404
  total).


- Completed this review (deep editorial 2026-10-31): new
  Payment instalment plan, Subscribe-and-save purchase
  option, and Pickup point selection pattern rows in
  `catalog/patterns.md`, completing roadmap actions 104,
  105, and 106; coverage matrix updated with the three new
  rows; three new improvement actions added (109 pass and
  ticket display, 110 shared cart, 111 stored payment
  method expiry warning); 3 new source records (409 total).


## Pre-publish checklist

The canonical publishing checklist lives in `CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The coverage matrix matches the actual files and directories.
- [ ] Only open improvement actions remain listed; completed ones moved to CHANGELOG.md.
- [ ] Exactly three new actions were added at the last deep review.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
