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
| Interface type | Web app, mobile app, kiosk, conversational, embedded, spatial, automotive, game | — | — |
| Page pattern | Dashboard, mobile navigation, data table, checkout variants, onboarding, comparison, permission request, search results, command palette, notification escalation, offline-first sync, sync-conflict resolution, file upload, chat and messaging, map comparison, list navigation, machine-composed content disclosure, agent checkpoint, voice hybrid flows, stepper, landing, authentication, settings, commerce, consent, notification digest, personalized-content disclosure, calendar and scheduling, keyboard shortcut reference, undo and trash recovery, session-expiry warning, data export, account deletion, in-product help, share link, second-factor sign-in, saved-item collection, bulk action, rating and review submission, payment failure recovery, content reporting and blocking, language and locale selection, scheduled action, breadcrumb navigation, annotation and comment thread, theme selection, profile and account menu, recently viewed, invitation response, modal dialog, guest checkout, time-zone picker, accessibility preferences, long-document navigation, in-app update prompt, pull-to-refresh, scrolling tab bar, system share sheet, find-in-page, collaborative editing presence,
    draft autosave and recovery, saved-filter view, toast feedback, list reorder, date-range picker, accordion disclosure, carousel, passkey sign-in, low-bandwidth mode, what's-new announcement, version history and restore, external-link departure, described media, saved-cart recovery, colour picker, guest-to-account conversion, sensitive-content preview, order tracking, order cancellation, time picker, verification-code entry, background-task progress, automated-to-human support handoff, subscription plan change, promo-code entry, master-detail, threaded message reply, gift option, saved address selection, delivery slot picker, product variant selection, home-screen widget, deep-link landing, progressive disclosure, return and exchange request, back-in-stock alert request, contact picker, primary navigation, bypass link, search, filtering and sorting, data table density, inline editing, bulk selection, data visualisation, guided tour, setup checklist, inline assistant actions, form flow, character count, wizard, detail view, notification list, notification preferences, activity feed, confirmation, sensitive-action re-confirmation, install prompt, offline download, multi-device handoff, paywall and upgrade prompt, subscription cancellation, restore purchases, account switcher, in-product feedback and problem report, account recovery, consent choice, granular consent, media viewer, code scanner, simplified view, location selection, voice message, message reaction, pinned message, message edit and delete, swipe-to-reveal actions, poll, conversation branching, sticky section headers, appointment management, review prompt, rating distribution summary, limited-time offer countdown, age verification gate, suggestion review, image gallery viewer, reading progress indicator, print-friendly view, text-selection action menu, picture-in-picture, reorder past order, live broadcast chat overlay, kanban board, gift card and stored-credit redemption, address entry, delivery instructions, saved payment method selection, split payment, media chapters, waitlist, loyalty rewards, link preview, live activity, billing overview, usage allowance, password strength meter, emoji picker, seat selection, selecting an option from a list, home control map, follow, payment instalment plan, subscribe-and-save purchase option, pickup point selection, expandable table row, pass and ticket display, shared cart, stored payment method expiry warning, workspace switcher, undo send, view switcher, tree view, timeline view, quote reply, product configurator, referral invitation, live captions, route planning, pass or ticket transfer, document signing, transcript editing, meeting and event creation, shared resource booking, backup payment method, household member management, checkout price-change confirmation, split shipment display, price-drop alert, guest order lookup, signed-in device management, service status notice, order substitution choice, commercial content disclosure, Trial-end reminder, Subscription pause, Data import, In-app survey, Document scanner, Delivery address validation, Shared expense splitting, In-store availability check, Guided route navigation, Saved search alert, Magic link sign-in, Preorder purchase, Tip selection, Live call controls, Device pairing, Hands-busy step guidance, Guardian approval request, Live poll, Delivery photo proof, Warranty claim, Overflow menu, Translated content, scheduled message send, saved reply, order receipt, subscription billing-date change, card freeze, travel disruption rebooking, size guide and fit recommendation, shared item access, app lock, transaction dispute, habit streak, contactless payment confirmation, profile photo upload and crop, playback queue, security incident notice, file preview, search history, download manager, voice message transcript, product recall notice, account merge, loyalty points expiry warning, QR sign-in, high-demand queue, group checkout, gift receipt, store pickup, reduced-motion preference, archive conversation, in-conversation message search, expiring payment method replacement, dual approval, stored payment method label, conversation export, appointment reminder, shoppable video, appointment check-in, travel check-in, stored payment method removal, aggregate rating display, recurring appointment series, travel document checklist, travel itinerary view, bill explanation, appointment late-cancellation and no-show policy, emergency assistance request, shared trip itinerary, ride booking, bottom sheet choice, trigger-character suggestion menu, booking deposit, appointment standby list, medication reminder, verified account badge, virtual background in video calls, world clock, expense claim submission, read receipt, typing indicator, video-call waiting room, focus mode schedule, sticker and GIF picker, product questions and answers, shared whiteboard, raise hand in video calls, screen sharing in video calls, disappearing messages, call recording notice, incoming call, missed call, scan-to-pay, launch screen, call waiting, outgoing call, call quality and reconnection, in-app browser, visual voicemail, safety check-in, breakout rooms in video calls, call transfer, conference call, suspected spam call warning, digital identity wallet presentation, call screening, reading view, add people to a live call, call history, transaction history, deceptive design patterns, accessibility labels on a store listing, PIN entry, cookie consent banner, parking session payment, screenshot markup, group chat administration, call forwarding, voicemail greeting, hotel booking, electric vehicle charging session, smart home dashboard, sleep and rest data, telehealth video consultation, museum audio guide, QR code payment at a till, crowdfunding campaign page, shared bike and scooter rental, digital car key sharing, parcel locker pickup, mobile plan setup (eSIM), voice dictation input, guest mode, live auction bidding, Back to top, Saved collection sharing, Identity verification onboarding, Broadcast emergency alert, Lightweight app entry, Receipt capture, Gated feature entry, Subscription gifting, Neuro-inclusive design, Live location sharing, Read-along narration, Group scheduling poll, Page not found, Order editing after placement, Human verification challenge, Gift card purchase, Message forwarding, Conversation catch-up summary, Conversation mute, Pinned conversation, Group conversation participant management, Sleep timer, System-mediated snippet, Return label and drop-off, Recording consent, Turn-by-turn guidance, Shared shopping list, Shared subscription plan, Donation at checkout, Checkout upsell and cross-sell offer, Shared presentation control, Paired handover record, Message translation, Converted price display, Fare-capped transit payment, Automation routine builder, Price history display, Delivery reschedule, Loyalty tier progress, Recipe serving scaling, Supervised usage limits, Appointment preparation checklist, Deposit refund status, Medication refill request, Recurring payment setup, Transit card top-up, In-flight entertainment, Hotel self check-in, Tenant portal, QR table ordering, Screen time dashboard, Health record sharing, E-reader and reading app, Ballot, Flight disruption compensation claim, Keyless shared-car pickup, Self-checkout grocery kiosk, School parent portal, Live translated captions, Real-time departure board, Care decision card, Recurring donation, Indoor wayfinding, Hotel room controls, University course registration, Veterinary appointment booking, Rental property viewing and tenancy application, Insurance claim submission, Tax filing and self-assessment, Temporary home access code, Car rental and car sharing booking, Cooking mode, Government document application, Mortgage application, Smartwatch fall detection and emergency SOS, Virtual try-on, Pension dashboard, Visa application, Parking fine payment and appeal, Phone voice menu | Drive-through and curbside pickup, Laundry pickup and delivery, Childcare booking, Public library borrowing (holds and renewals), ATM interface, Home energy usage dashboard | — |
| State | All seven in catalog; offline, read-only, permission-denied; loading variants; error-state groups | — | — |
| Worked examples | Dashboard, mobile navigation, onboarding, watch, kiosk, television, desktop, checkout, authentication, settings — each demonstrating the rules it documents with all seven states | — | — |
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
   passes all quality gates. (Implemented this run.)

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
   this run.) (Implemented this run.)

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
   run.) (Implemented this run.)

14. Add a version history and restore pattern row to
   `catalog/patterns.md`: a dated list of saved versions with a
   preview of what changed, a restore action that saves the restored
   version as a new version rather than silently overwriting the
   current one, and a clear statement of what restore does and does
   not bring back — cross-checked against the sync-conflict resolution
   row. Done when the row passes all quality gates. (Implemented this
   run.) (Implemented this run.)

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
   row passes all quality gates. (Implemented this run.)

21. Add contextual guidance rules to the Onboarding row in
   `catalog/patterns.md` and `layouts/onboarding.md`: inline help is
   the default, coach marks appear only when the person first reaches
   the feature they explain, never more than three in a sequence,
   always dismissable, and never a substitute for a clear label or a
   first screen that teaches by doing — cross-checked against the skip
   and progress-persistence rules in the same files. Done when the
   rules pass all quality gates. (Implemented this run.)

22. Add an empty-state fallback rule to the Empty row in
   `catalog/states.md`: the empty state renders as a static fallback
   even when the data request fails, so a failed load never produces a
   blank screen; the fallback states what is missing, offers one next
   action, and states whether a retry will restore the content —
   cross-checked against the error state rules in the same file. Done
   when the extended row passes all quality gates. (Implemented this run.)

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
   never retypes it. Done when the rule passes all quality gates (Implemented this run.)

30. Add a link-preview rule to the Share link row in
   `catalog/patterns.md`: before sending, show the recipient what the
   link opens, who can open it, and when it expires, with an edit step
   for scope and expiry from the same screen. Done when the rule
   passes all quality gates (Implemented this run.)

31. Add a method-change rule to the Second-factor sign-in row in
   `catalog/patterns.md`: changing the second-factor method requires a
   successful check with the current method first, and the old method
   stays active until the new one verifies, so a failed switch never
   locks the person out. Done when the rule passes all quality gates (Implemented this run.)

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
   this run.) (Implemented this run.)

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
   warning row. Done when the row passes all quality gates. (Implemented this run.)

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
   this run.) (Implemented this run.)

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
   gates. (Implemented this run.)

49. Add a search history pattern row to `catalog/patterns.md`: past
   queries kept as a list the person can re-run, edit, or delete one
   at a time or all at once, with a stated retention scope — distinct
   from the recently viewed row, which lists opened items rather than
   queries, and from the search row, which covers finding content.
   Done when the row passes all quality gates. (Implemented this run.)

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
   selected text. Done when the row passes all quality gates. (Implemented this run.)

57. Add a no-results recovery rule to the Search row in
   `catalog/patterns.md`: when a query returns nothing, state plainly
   that nothing matched, offer one spelling or scope correction, and
   keep the query editable in place with a route back to the full list
   — distinct from the zero-result metric in the same row, which
   measures the problem rather than repairing it. Done when the rule
   passes all quality gates. (Implemented this run.)

58. Add a print-friendly view pattern row to `catalog/patterns.md`: a
   reading view that removes navigation and interactive controls for
   printing, keeps headings and tables intact across page breaks, and
   states the page count before printing — distinct from the
   long-document navigation row, which moves within a screen rather
   than preparing it for print. Done when the row passes all quality
   gates. (Implemented this run.)

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
   gates. (Implemented this run.)

63. Add an aggregate rating display pattern row to
   `catalog/patterns.md`: a read-only summary showing the average, the
   count of ratings, and the spread across rating values, with a
   stated rule for which ratings count and a filter for verified
   ratings where verification exists — distinct from the rating and
   review submission row, which collects a rating, and from the review
   prompt row, which asks for one. Done when the row passes all
   quality gates. (Implemented this run.)

64. Add a setup checklist pattern row to `catalog/patterns.md`: an
   ordered list of setup tasks with done, current, and remaining
   states, a resume point that returns the person to the first
   unfinished task, and a skip path that keeps skipped tasks reachable
   — distinct from the onboarding row, which teaches a first run, and
   from the wizard row, which completes one task in steps. Done when
   the row passes all quality gates. (Implemented this run.)

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
   this run.) (Implemented this run.)

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
   is lost. Done when the row passes all quality gates. (Implemented this run.)

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
   gates. (Implemented this run.)

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
   passes all quality gates. (Implemented this run.)

77. Add a sensitive-content preview pattern row to
   `catalog/patterns.md`: content that may distress or surprise
   first shows a plain preview stating what kind of content follows
   and why it is flagged, with an explicit reveal control and the
   choice remembered per content type — distinct from the consent
   choice row, which asks permission for data use, and from the
   notification grouping rules, which summarise events. Done when the
   row passes all quality gates. (Implemented this run.)

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
   quality gates. (Implemented this run.)

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
   gates. (Implemented this run.)

86. Add an age verification gate pattern row to
   `catalog/patterns.md`: a gate that states the age requirement and
   why it applies, asks only for the threshold where that suffices
   rather than full identity details, offers a plain decline route
   with somewhere useful to go, and remembers the answer only where
   that is appropriate — distinct from the consent choice row, which
   asks permission for data use, and from the passkey sign-in row,
   which proves a credential. Done when the row passes all quality
   gates. (Implemented this run.)

87. Add a limited-time offer countdown pattern row to
   `catalog/patterns.md`: a countdown shown beside the exact end
   time and its zone, a timer that never resets on revisit, a plain
   statement of what happens when the time runs out, and the offer
   terms reachable from the countdown itself — distinct from the
   session-expiry warning row, which ends a session, and from the
   scheduled action row, which runs an action at a future time.
   Done when the row passes all quality gates. (Implemented this run.)

88. Add a master-detail pattern row to `catalog/patterns.md`: a
   list beside its detail on wide screens, the selected item
   stated in text as well as in shape, the detail updating
   without losing the list position, a stacked list-then-detail
   route with a clear back step on narrow screens, and a stated
   empty detail state before anything is selected — distinct
   from the detail view row, which inspects one item without a
   sibling list, and from the data table row, which compares
   rows rather than pairing a list with its detail. Done when
   the row passes all quality gates. (Implemented this run.)

89. Add a threaded message reply pattern row to `catalog/patterns.md`: a
   reply anchored to the message it answers, a thread view that
   keeps the original message visible, an unread count per thread
   stated in text, and a return route from the thread to the
   main conversation — distinct from the annotation and comment
   thread row, which anchors discussion to document content, and
   from the message edit and delete row, which changes a message
   rather than answering it. Done when the row passes all quality
   gates. (Implemented this run.)

90. Add a gift option pattern row to `catalog/patterns.md`: an
   option at checkout marking an order as a gift, prices hidden
   from the recipient, an optional gift message shown to the
   recipient, and a separate delivery address for the gift that
   never overwrites the buyer's own address — distinct from the
   guest checkout row, which completes a purchase without an
   account, and from the saved-cart recovery row, which revisits
   an unfinished cart. Done when the row passes all quality
   gates. (Implemented this run.)

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
   all quality gates. (Implemented this run.)

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
   single item. Done when the row passes all quality gates. (Implemented this run.)

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
   gates. (Implemented this run.)

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
   passes all quality gates. (Implemented this run.)

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
   (Implemented this run.)

109. Add a pass and ticket display pattern row to
   `catalog/patterns.md`: a display for a pass or ticket held
   for later use, with a scannable code shown large enough to
   scan, brightness raised while it is displayed, availability
   without a connection, and a stated route when the code
   cannot be scanned — distinct from the code scanner row,
   which captures a code, and from the order tracking row,
   which follows an order's progress. Done when the row
   passes all quality gates.
   (Implemented this run.)

110. Add a shared cart pattern row to `catalog/patterns.md`:
   a cart several people can add to, with each item naming
   who added it, a stated owner for checkout, and a plain
   rule for removing another person's item — distinct from
   the split payment row, which divides payment, and from
   the saved-item collection row, which keeps items for one
   person. Done when the row passes all quality gates.
   (Implemented this run.)

111. Add a stored payment method expiry warning pattern row
   to `catalog/patterns.md`: a warning before a stored
   method expires, stating which method and when, with a
   replacement route that keeps future orders and plans
   working — distinct from the saved payment method
   selection row, which chooses a method, and from the
   payment failure recovery row, which recovers after a
   failure. Done when the row passes all quality gates.
   (Implemented this run.)

112. Add an expandable table row pattern row to `catalog/patterns.md`: a
   named toggle per row that holds detail, short detail shown in a
   detail row beneath its parent row and long detail opened as a
   separate detail view, the expanded state stated in text as well
   as in shape and announced to assistive technology, focus kept
   on the toggle when expanding, and collapsing never discarding
   entered input inside the detail — distinct from the accordion
   disclosure row, which organises sections under headings, and
   from the detail view row, which inspects one item without a
   sibling table. Done when the row passes all quality gates.
   (Implemented this run.)

113. Add a meeting and event creation pattern row to
   `catalog/patterns.md`: a creation flow that checks attendee
   and resource availability before confirming, states conflicts
   in plain words with the next available time offered, states
   the time zone for every time shown, and offers a route to
   carry the confirmed event into the person's own calendar —
   distinct from the calendar and scheduling row, which shows
   objects in time, and from the invitation response row, which
   answers an invitation. Done when the row passes all quality
   gates.
   (Implemented this run.)

114. Add a shared resource booking pattern row to
   `catalog/patterns.md`: booking a shared room or item from its
   availability, with capacity and equipment stated for each
   choice, buffer time between bookings treated as blocked time,
   a plain statement where a booking needs approval before it is
   confirmed, a freed booking released at once for others, and a
   stated rule for what happens when one item of a bundled
   booking is unavailable — distinct from the appointment
   management row, which manages a person's own booked time, and
   from the calendar and scheduling row, which shows objects in
   time. Done when the row passes all quality gates.
   (Implemented this run.)

115. Add a pass or ticket transfer pattern row to
   `catalog/patterns.md`: passing a held pass or ticket to
   another person, with the transfer stated to both sides,
   the original pass invalidated once transferred where
   transfer is single-use, and a plain route to take the
   transfer back before it is accepted — distinct from the
   pass and ticket display row, which shows a held pass,
   and from the gift option row, which marks an order as
   a gift. Done when the row passes all quality gates. (Implemented this run.)

116. Add a backup payment method pattern row to
   `catalog/patterns.md`: a second stored method used only
   when the primary method fails, chosen in advance, stated
   at checkout, and never charged without a failed primary
   attempt and a plain notice — distinct from the stored
   payment method expiry warning row, which warns before
   expiry, and from the payment failure recovery row,
   which recovers after a failure. Done when the row
   passes all quality gates.
   (Implemented this run.)

117. Add a checkout price-change confirmation pattern row
   to `catalog/patterns.md`: when a price changes between
   the cart view and payment, stop before charging, state
   the old price, the new price, and what changed, and
   require a fresh confirmation of the new total — distinct
   from the saved-cart recovery row, which states changes
   on return to a saved cart, and from the limited-time
   offer countdown row, which states an offer deadline.
   Done when the row passes all quality gates.
   (Implemented this run.)

118. Add a subscription pause pattern row to
   `catalog/patterns.md`: pausing a plan rather than cancelling
   it, with the pause start and resume date stated before
   confirming, access during the pause stated plainly, charges
   stopped for the paused period, and a resume route that
   restores the same plan without re-entering details —
   distinct from the subscription cancellation row, which ends
   a plan, and from the subscription plan change row, which
   moves to a different plan. Done when the row passes all
   quality gates. (Implemented this run.)

119. Add a saved search alert pattern row to
   `catalog/patterns.md`: an alert that watches a saved search
   and reports new matches, with the search criteria stated in
   the alert itself, a stated check frequency, a route to pause
   or stop the alert, and a stated rule for what happens when
   the search itself changes — distinct from the back-in-stock
   alert request row, which watches one item, and from the
   saved-item collection row, which keeps items the person
   chose. Done when the row passes all quality gates. (Implemented this run.)

120. Add a data import pattern row to `catalog/patterns.md`:
   bringing an existing set of records into the product, with
   a stated mapping from the incoming fields to the product's
   fields, a preview of what will be added before anything is
   committed, a plain report of rows that could not be
   imported with a route to fix them, and a stated rule that a
   failed import never leaves a half-imported set behind —
   distinct from the data export row, which takes records out,
   and from the file upload row, which sends a single file.
   Done when the row passes all quality gates.
   (Implemented this run; row verified pre-existing and
   satisfying the action.)

121. Add a split shipment display pattern row to
   `catalog/patterns.md`: one order shown as its separate
   shipments, each with its own items, delivery window, and
   tracking route, a single order total charged once, and an
   order state folded from its shipments rather than taken
   from the latest event — distinct from the order tracking
   row, which follows one delivery, and from the order
   cancellation row, which stops an order. Done when the
   row passes all quality gates. (Implemented this run.)

122. Add a price-drop alert pattern row to
   `catalog/patterns.md`: an alert watching one item for a
   price fall, with the watched price and the trigger stated
   at setup, only the first fall past the trigger reported,
   and pause and stop controls from the alert itself —
   distinct from the saved search alert row, which watches
   a search for new matches, and from the back-in-stock
   alert request row, which watches availability. Done
   when the row passes all quality gates. (Implemented this run.)

123. Add a guest order lookup pattern row to
   `catalog/patterns.md`: finding an order without signing
   in, using only the order reference and one identifier
   from the order itself, with no account created as a side
   effect and no other order reachable by guessing a
   reference — distinct from the order tracking row, which
   follows a signed-in order, and from the guest checkout
   row, which buys without an account. Done when the row
   passes all quality gates.
   (Implemented this run.)

124. Add a trial-end reminder pattern row to
   `catalog/patterns.md`: a notice sent before a trial's first
   charge, stating the charge date, the amount, and the plan
   that follows, with a cancel route that works before the
   charge and a stated rule for what access continues after
   cancelling — distinct from the paywall and upgrade prompt
   row, which offers the trial, and from the subscription
   cancellation row, which ends a paid plan. Done when the
   row passes all quality gates. (Implemented this run.)

125. Add a tip selection pattern row to
   `catalog/patterns.md`: preset amounts, a custom amount,
   and an explicit no-tip choice shown together, with the
   total updated before confirmation and a stated rule for
   whether the tip can change after the order is placed —
   distinct from the payment instalment plan row, which
   spreads a total, and from the promo-code entry row, which
   reduces a total. Done when the row passes all quality
   gates. (Implemented this run.)

126. Add a delivery photo proof pattern row to
   `catalog/patterns.md`: a photo attached to the delivered
   stage, viewable from the tracking view, with a route at
   once where the photo does not match the order received,
   and a stated rule for how long the photo is kept and who
   can see it — distinct from the order tracking row, which
   follows the delivery, and from the proof-of-delivery
   record mentioned there. Done when the row passes all
   quality gates. (Implemented this run.)

127. Add a signed-in device management pattern row to
   `catalog/patterns.md`: a list of every device and session
   signed in to the account, each with a recognisable name and
   a last-activity statement, the device in use marked, sign-out
   for one device or session and a sign-out-everywhere control
   that keeps the current device signed in unless chosen
   otherwise, and a direct route to change the password and
   review recent activity after an unfamiliar device is signed
   out — distinct from the account switcher row, which moves
   between signed-in accounts, and from the second-factor
   sign-in row, which adds a check at sign-in. Done when the
   row passes all quality gates. (Implemented this run.)

128. Add a service status notice pattern row to
   `catalog/patterns.md`: a notice stating which parts of the
   service are affected and what the person can and cannot do
   right now, updates on a stated cadence with the next update
   time given even when nothing is new, a workaround where one
   exists, a plain cause once known, and a resolution statement
   stating when service returned and what happens next, with
   no invented return time and a status route that stays
   reachable outside the affected service — distinct from the
   notification escalation row, which grades interruption by
   urgency, and from the in-app update prompt row, which
   requires an update rather than reporting an outage. Done
   when the row passes all quality gates. (Implemented this run.)

129. Add an order substitution choice pattern row to
   `catalog/patterns.md`: a per-item preference set before
   fulfilment — accept a named substitute, ask first, or
   remove the item — with any substitute stated beside the
   original with its price difference before the final total
   is charged, no substitution across a dietary or allergen
   boundary without explicit approval, and a refund of any
   price difference where the substitute costs less —
   distinct from the back-in-stock alert request row, which
   watches availability, and from the product variant
   selection row, which chooses a variant at purchase. Done
   when the row passes all quality gates. (Implemented this run.)

130. Add a commercial content disclosure pattern row to
   `catalog/patterns.md`: paid, sponsored, and affiliate
   content labelled at the point of recommendation in plain
   words stating what the publisher earns, the label placed
   with the recommendation itself rather than only on a
   separate policy page, and the label kept with the content
   when it is shared or quoted — distinct from the
   personalized-content disclosure row, which states the
   signal behind an adaptation to the person, and from the
   machine-composed content disclosure row, which labels
   content the system composed. Done when the row passes
   all quality gates. (Implemented this run.)

131. Add a warranty claim pattern row to
   `catalog/patterns.md`: a claim started from the order or
   item it covers, the proof needed stated up front, claim
   states that match events the service can establish
   (received, under review, approved, declined with a
   reason), repair, replacement, and refund options with
   their timeframes, a return route where the item must be
   sent back, and a decision notice stating the reason and
   the next step — distinct from the return and exchange
   request row, which returns an item by choice, and from
   the order cancellation row, which cancels before
   fulfilment. Done when the row passes all quality gates. (Implemented this run.)

132. Add an in-store availability check pattern row to
   `catalog/patterns.md`: stock at nearby stores checked
   before a visit, with distance and opening times beside
   each store, the time the stock was checked stated, a
   hold or reserve route where offered, and the next
   nearest store or a delivery route offered where the
   nearest store has none — distinct from the pickup point
   selection row, which chooses where a placed order is
   collected, and from the delivery slot picker row, which
   chooses a delivery window. Done when the row passes
   all quality gates. (Implemented this run.)

133. Add a delivery address validation pattern row to
   `catalog/patterns.md`: when an entered address looks
   incomplete or mismatched, a suggested correction shown
   beside the field, never silently rewriting what was
   entered, the suggested address shown beside the entered
   one for confirmation, the original kept where the person
   insists on it, and the address re-checked at
   confirmation — distinct from the address entry row,
   which collects an address, and from the saved address
   selection row, which reuses a stored address. Done when
   the row passes all quality gates. (Implemented this run.)

143. Add an app lock pattern row to
   `catalog/patterns.md`: locking a signed-in app behind the
   device's own check or a sign-in fallback after a stated
   period of inactivity, with a lock-on-leaving option, a
   visible fallback that never depends on the device check
   alone, a stated pause after repeated failed attempts
   without locking the account, hidden sensitive content in
   previews and notifications while locked, and a plain
   statement of what the lock does and does not protect —
   distinct from the second-factor sign-in row, which
   confirms identity at sign-in, and from the session-expiry
   warning row, which warns before a session ends. Done
   when the row passes all quality gates. (Implemented
   this run.) (Implemented this run.)

144. Add a profile photo upload and crop pattern row to
   `catalog/patterns.md`: choosing a photo from the device
   or camera, a crop step that previews exactly the shape
   shown to others, a stated size and format limit before
   choosing, a remove route that restores a neutral
   placeholder, and a keyboard-operable crop with a stated
   alternative where cropping by drag is not possible —
   distinct from the file upload row, which moves files
   in reliably, and from the profile and account menu row,
   which lists account actions. Done when the row passes
   all quality gates. (Implemented this run.)

145. Add a playback queue pattern row to
   `catalog/patterns.md`: an ordered list of items to play
   next with the current item marked in text as well as in
   shape, add, remove, and reorder controls that never
   interrupt the item now playing, stated shuffle and
   repeat modes with shuffle never repeating an item until
   the list has played through, and a stated rule for what
   plays when the queue ends — distinct from the media
   chapters row, which marks sections inside one item, and
   from the list reorder row, which reorders a list
   without playback. Done when the row passes all quality
   gates. (Implemented this run.)

146. Add a security incident notice pattern row to
   `catalog/patterns.md`: a notice sent when account or
   personal data may have been exposed, stating plainly
   what happened, what data was involved, what the person
   should do now, and what is already being done, with a
   dated update route as facts change — distinct from the
   service status notice row, which reports availability,
   and from the account recovery row, which restores
   access. Done when the row passes all quality gates. (Implemented this run.)

147. Add a recording consent pattern row to
   `catalog/patterns.md`: consent asked before a call or
   meeting is recorded, stating who can hear the recording
   and where it is kept, a visible recording indicator
   while recording runs, and a route to withdraw consent
   that stops recording without ending the call — distinct
   from the live captions row, which transcribes speech,
   and from the consent choice row, which records a
   general permission. Done when the row passes all
   quality gates. (Implemented this run.)

148. Add a group checkout pattern row to
   `catalog/patterns.md`: several people contributing to
   one order, with each contribution stated, a single
   payer or split charges chosen up front, a stated rule
   for what happens when one contribution fails, and a
   receipt each contributor can check — distinct from the
   shared cart row, which shares one cart, and from the
   split payment row, which splits one payment. Done when
   the row passes all quality gates. (Implemented this run.)
149. Add a product recall notice pattern row to
   `catalog/patterns.md`: a notice for a product already
   bought that must be returned, repaired, or stopped from
   use, stating which items are affected and how to check
   one, the risk in plain words, the remedy offered at no
   extra cost, and a route that keeps a record of the
   remedy — distinct from the service status notice row,
   which reports availability, and from the warranty claim
   row, which starts a claim for a fault. Done when the
   row passes all quality gates. (Implemented this run.)

150. Add an account merge pattern row to
   `catalog/patterns.md`: bringing two accounts held by
   the same person into one, stating before confirmation
   what moves, what is kept from each account where both
   hold the same kind of record, and what is lost, with a
   preview of the merged account and a route back where
   the merge can still be undone — distinct from the
   account switcher row, which moves between accounts,
   and from the account deletion row, which closes an
   account. Done when the row passes all quality gates. (Implemented this run.)

151. Add a loyalty points expiry warning pattern row to
   `catalog/patterns.md`: a warning before points expire,
   stating the amount at risk, the exact expiry date, the
   smallest use that saves them, and a route to use them
   from the warning itself, with the warning repeated in
   the balance view — distinct from the loyalty rewards
   row, which earns and spends points, and from the
   trial-end reminder row, which warns before a charge.
   Done when the row passes all quality gates. (Implemented this run.)


- Completed this review (deep editorial 2026-11-02): new
  Profile photo upload and crop, Playback queue, and
  Security incident notice pattern rows in
  `catalog/patterns.md`, completing roadmap actions 144,
  145, and 146; coverage matrix updated with the three new
  rows; three new improvement actions added (149 product
  recall notice, 150 account merge, 151 loyalty points
  expiry warning); 3 new source records (489 total).

- Completed this review (deep editorial 2026-11-02): new
  Transaction dispute, Habit streak, and Contactless
  payment confirmation pattern rows in
  `catalog/patterns.md`, completing roadmap actions 140,
  141, and 142; coverage matrix updated with the three new
  rows; three new improvement actions added (146 security
  incident notice, 147 recording consent, 148 group
  checkout); 3 new source records (483 total).

- Completed this review (deep editorial 2026-11-01): new
  Service status notice, Order substitution choice, and
  Commercial content disclosure pattern rows in
  `catalog/patterns.md`, completing roadmap actions 128,
  129, and 130; coverage matrix updated with the three new
  rows; three new improvement actions added (131 warranty
  claim, 132 in-store availability check, 133 delivery
  address validation); 1 new source record (458 total).

- Completed this review (daily planning 2026-11-01): new
  Signed-in device management pattern row in
  `catalog/patterns.md`, completing roadmap action 127;
  coverage matrix updated with the new row; four new
  improvement actions added (127 signed-in device
  management, 128 service status notice, 129 order
  substitution choice, 130 commercial content disclosure);
  3 new source records (456 total). Since the last daily
  run, the deep cycle completed actions 121, 122, and 123
  and light cycles added the Tip selection and Trial-end
  reminder rows and an audio-rendering extension to the
  Data visualisation row; those outcomes are already
  recorded in `CHANGELOG.md`.

- Completed this review (deep editorial 2026-11-01): new
  Split shipment display, Price-drop alert, and Guest order
  lookup pattern rows in `catalog/patterns.md`, completing
  roadmap actions 121, 122, and 123; coverage matrix updated
  with the three new rows; three new improvement actions added
  (124 trial-end reminder, 125 tip selection, 126 delivery
  photo proof); 3 new source records (450 total).

- Completed this review (deep editorial 2026-10-31): new
  Household member management and Checkout price-change
  confirmation pattern rows in `catalog/patterns.md`,
  completing roadmap actions 108 and 117; roadmap action
  120 verified complete against the pre-existing Data
  import row, which already covers field mapping, preview
  counts, per-row failure reporting, and the no-silent-
  half-import commit rule; coverage matrix updated with
  the two new rows; three new improvement actions added
  (121 split shipment display, 122 price-drop alert, 123
  guest order lookup); 1 new source record added by this run (442 total in file).


134. Add a translated-content pattern row to
   `catalog/patterns.md`: where content arrives in a language
   the person does not read, offer a translation beside the
   original, state the source language and that the text is
   translated, keep the original reachable in one action, and
   never present a translated legal or safety-critical text
   without a stated review route — distinct from the
   language and locale selection row, which chooses the
   interface language, and from the live captions row, which
   transcribes speech. Done when the row passes all quality
   gates. (Implemented this run.)

135. Add a converted-price display pattern row to
   `catalog/patterns.md`: where a price is shown in a second
   currency, show the converted amount beside the original
   price, state the conversion rate and the date it was set,
   never replace the original price at checkout, and re-state
   the final charge in the charging currency before payment
   — distinct from the locale-aware formatting rules in
   `catalog/primitives.md`, which format a price, and from
   the promo-code entry row, which reduces a total. Done
   when the row passes all quality gates. (Implemented this run.)

136. Add a scheduled message send pattern row to
   `catalog/patterns.md`: a message composed now and sent
   later, with its scheduled time stated in plain words,
   editable and cancellable until it sends, a plain
   confirmation once sent, and a failed send reported with a
   retry path rather than silently dropped — distinct from
   the scheduled action row, which schedules a general
   action, and from the draft autosave row, which saves
   unfinished work. Done when the row passes all quality
   gates. (Implemented this run.)

137. Add an order receipt pattern row to
   `catalog/patterns.md`: a receipt kept after purchase
   stating the items, the charges, the payment method, and
   the delivery or pickup details, retrievable later from
   the order, with a correction route where a detail is
   wrong — distinct from the order tracking row, which
   follows a delivery, and from the billing overview row,
   which summarises recurring charges. Done when the row
   passes all quality gates. (Implemented this run.)

138. Add a subscription billing-date change pattern row to
   `catalog/patterns.md`: moving a renewal date states the
   effect on the current period, the next charge date, and
   any prorated amount before confirming, with a pending
   change cancellable until it takes effect — distinct from
   the subscription plan change row, which changes what is
   paid for, and from the subscription pause row, which
   suspends billing for a set period. Done when the row
   passes all quality gates. (Implemented this run.)

139. Add a saved reply pattern row to `catalog/patterns.md`:
   a reusable message template inserted into a conversation
   or support reply, editable before sending, with
   placeholders checked before send and no silent sending
   of an unreviewed template — distinct from the draft
   autosave row, which saves unfinished work, and from the
   scheduled message send row, which sends a composed
   message later. Done when the row passes all quality
   gates. (Implemented this run.)

140. Add a transaction dispute pattern row to
   `catalog/patterns.md`: disputing a transaction from its
   detail view, with the disputed amount and date stated, a
   reason choice in plain words, a place to add evidence,
   a provisional state while the dispute is reviewed, and
   a final outcome notice stating what was refunded or
   upheld and why — distinct from the payment failure
   recovery row, which recovers a payment that already
   failed, and from the card freeze row, which stops a
   card from paying. Done when the row passes all quality
   gates. (Implemented this run.)

141. Add a habit streak pattern row to
   `catalog/patterns.md`: a visible count of consecutive
   days a habit was kept, with the current streak, the
   longest streak, and a stated rule for what breaks it,
   a missed-day recovery route where one is offered, and
   a pause that holds the streak without counting a miss
   — distinct from the activity feed row, which lists
   past activity, and from the setup checklist row, which
   tracks one-off setup steps. Done when the row passes
   all quality gates. (Implemented this run.)

142. Add a contactless payment confirmation pattern row
   to `catalog/patterns.md`: paying by tapping a card or
   device at a terminal, with the amount and the method
   shown before the tap, an immediate success or failure
   signal at the terminal, a receipt route for the payment,
   and a fallback to another method where the tap fails
   — distinct from the saved payment method selection
   row, which chooses a stored method at checkout, and
   from the payment failure recovery row, which recovers
   a failed online payment. Done when the row passes all
   quality gates. (Implemented this run.)

- Completed this review (deep editorial 2026-11-01): new
  Delivery photo proof, Warranty claim, and Overflow menu
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 126, 131, and 62; coverage matrix updated with the
  new rows and with pattern rows previously missing from it;
  three new improvement actions added (134 translated
  content, 135 converted-price display, 136 scheduled
  message send); 3 new source records (468 total).

- Completed this review (deep editorial 2026-11-02): new
  Card freeze, Travel disruption rebooking, and Size guide
  and fit recommendation pattern rows in
  `catalog/patterns.md`; coverage matrix updated with the
  new rows and with three rows previously missing from it
  (saved reply, order receipt, subscription billing-date
  change); three new improvement actions added (140
  transaction dispute, 141 habit streak, 142 contactless
  payment confirmation); 3 new source records (476 total).

- Completed this review (daily planning 2026-11-02): new
  App lock pattern row in `catalog/patterns.md`, completing
  roadmap action 143; coverage matrix updated with the new
  row; three new improvement actions added (143 app lock,
  144 profile photo upload and crop, 145 playback queue);
  no new source records — the biometric sign-in guidance
  source was already recorded (478 total).

152. Add a download manager pattern row to `catalog/patterns.md`:
   a list of files downloaded or downloading, each with name,
   size, progress, and a stated state, pause and resume where
   the download can continue, an open action for a finished
   download, a retry route for a failed one, and a remove
   control that frees storage at once — distinct from the
   offline download row, which keeps content for use without
   a connection, and from the file preview row, which inspects
   a file before opening it. Done when the row passes all quality
   gates. (Implemented this run.)

153. Add a voice message transcript pattern row to
   `catalog/patterns.md`: a written transcript shown beside a
   voice message, with the spoken words in reading order, a
   stated note where parts could not be transcribed, a route to
   the spoken message from any point in the transcript, and the
   transcript kept available where sound cannot be played —
   distinct from the voice message row, which sends and plays
   a message, and from the live captions row, which transcribes
   live speech. Done when the row passes all quality gates. (Implemented this run.)

154. Add a checkout worked example under `examples/`: a worked
   example demonstrating the ecommerce layout and the checkout
   pattern rows — guest checkout, saved payment method
   selection, delivery slot picker, and promo-code entry —
   with all seven states, so the checkout rules can be checked
   against a complete screen rather than a single row —
   distinct from the dashboard, mobile navigation, and
   onboarding examples, which demonstrate other layouts. Done
   when the example passes all quality gates. (Implemented this run.)

155. Add a high-demand queue pattern row to `catalog/patterns.md`: a
   queue entered when demand exceeds capacity, with the person's
   position stated, a wait estimate that never promises a time
   that cannot be kept, a kept place on a brief interruption, and
   a plain route out with the place released at once — distinct
   from the waitlist row, which watches one item for restock,
   and from the appointment management row, which manages a
   booked time. Done when the row passes all quality gates. (Implemented this run.)

156. Add a price history display pattern row to
   `catalog/patterns.md`: past prices for one item shown with
   their dates, the current price marked as a sale only where a
   higher price genuinely applied before, and a stated rule for
   how far back the history reaches — distinct from the
   price-drop alert row, which watches for a future fall, and
   from the converted-price display row, which restates a price
   in a second currency. Done when the row passes all quality
   gates. (Implemented this run.)

157. Add a subscription gifting pattern row to
   `catalog/patterns.md`: giving a subscription to another
   person, with the gift length and what it includes stated
   before purchase, the recipient accepting before access
   starts, a stated rule for who pays on renewal, and a plain
   route for the recipient to decline without the giver being
   charged for access never taken — distinct from the gift
   option row, which marks one order as a gift, and from the
   referral invitation row, which invites a person to join.
   Done when the row passes all quality gates. (Implemented this run.)


158. Add a QR sign-in pattern row to
   `catalog/patterns.md`: sign in on a screen with awkward
   input by approving on a phone already signed in, with the
   account and the asking device named on the approving
   phone, an explicit approval there before sign-in completes,
   a typed short code beside the QR code, a stated code
   expiry, and a cancel control that ends the attempt on both
   screens — distinct from the passkey sign-in row, which
   signs in with a device-held credential, and from the code
   scanner row, which reads codes for content rather than for
   sign-in. Done when the row passes all quality gates.
   (Implemented this run.)

159. Add a delivery reschedule pattern row to
   `catalog/patterns.md`: changing the delivery window of a
   placed order from the order itself, with a stated cut-off
   after which the window can no longer change, a fee
   difference stated before confirmation where one applies,
   the new window carried into the tracking view, and a plain
   statement where rescheduling is no longer possible rather
   than a missing control — distinct from the delivery slot
   picker row, which chooses a window at checkout, and from
   the order editing row, which changes the order itself.
   Done when the row passes all quality gates. (Implemented this run.)

160. Add a loyalty tier progress pattern row to
   `catalog/patterns.md`: the current tier stated with the
   progress toward the next tier in plain figures, the
   benefits of the next tier listed beside the gap, a stated
   rule for how the tier is kept or lost, and progress that
   never relies on shape or colour alone — distinct from the
   loyalty rewards row, which earns and spends a points
   balance, and from the loyalty points expiry warning row,
   which warns before points expire. Done when the row passes
   all quality gates. (Implemented this run.)


161. Add a message forwarding pattern row to
   `catalog/patterns.md`: forwarding a message to another
   conversation, with a preview of the message being sent,
   a recipient choice that states where it will land, an
   edit route before sending, and a stated rule for
   forwarded media and links — distinct from the quote
   reply row, which answers in place, and from the threaded
   message reply row, which answers inside a thread. Done
   when the row passes all quality gates. (Implemented this run.)

162. Add a return label and drop-off pattern row to
   `catalog/patterns.md`: returning an item with a label
   and a drop-off route, stating where the label is found,
   how long it stays valid, what to show at drop-off, and
   the refund timing after the return is scanned — distinct
   from the return and exchange request row, which starts
   the return, and from the order tracking row, which
   follows a delivery. Done when the row passes all
   quality gates. (Implemented this run.)

163. Add a saved collection sharing pattern row to
   `catalog/patterns.md`: sharing a saved collection with
   another person, with a stated scope for what is shared,
   a view-only or editable choice, a revoke control, and a
   plain statement of what happens to shared items when
   access is revoked — distinct from the saved-item
   collection row, which keeps items for one person, and
   from the shared cart row, which shares items for a
   single checkout. Done when the row passes all quality
   gates. (Implemented this run.)

164. Add a conversation mute pattern row to
   `catalog/patterns.md`: silencing one conversation without
   leaving it, with a stated mute length or until-unmuted
   choice, a plain muted mark visible in the list, messages
   still arriving without an alert, and a one-action unmute
   from the conversation itself — distinct from the pinned
   message row, which keeps a message in view, and from the
   notification preferences row, which sets alerts for all
   conversations. Done when the row passes all quality
   gates. (Implemented this run.)

165. Add a reduced-motion preference pattern row to
   `catalog/patterns.md`: honouring a stated preference for
   less movement, with animated elements replaced by instant
   or faded changes, no essential information carried by
   motion alone, and the preference respected on every
   screen without re-asking — distinct from the functional
   motion trend file, which describes when motion helps,
   and from the accessibility preferences row, which
   gathers preference controls in one place. Done when
   the row passes all quality gates.
   (Implemented this run.)

166. Add an archive conversation pattern row to
   `catalog/patterns.md`: moving a finished conversation out
   of the main list without deleting it, with a stated
   archive location, search still finding archived
   conversations, new messages returning a conversation to
   the main list or stating plainly that they do not, and
   a one-action restore from the archive — distinct from
   the message edit and delete row, which changes or
   removes single messages, and from the saved-item
   collection row, which keeps chosen items. Done when
   the row passes all quality gates.
   (Implemented this run.)

167. Add an in-conversation message search pattern row to
   `catalog/patterns.md`: searching inside one conversation,
   with a match count, jump-to-match controls, matched
   words highlighted in the message, and a plain route back
   to the latest message — distinct from the find-in-page
   row, which searches a page or document, and from the
   search history row, which returns to a past query.
   Done when the row passes all quality gates.
   (Implemented this run.)

168. Add an expiring payment method replacement pattern row
   to `catalog/patterns.md`: replacing a card before it
   expires from the warning itself, with the replacement
   carried into every subscription and saved checkout that
   used the old card, a stated date from which the new
   card is charged, and a plain statement where a payment
   cannot move — distinct from the stored payment method
   expiry warning row, which warns before expiry, and
   from the saved payment method selection row, which
   chooses a card at checkout. Done when the row passes
   all quality gates.
   (Implemented this run.)

169. Add a pinned conversation pattern row to
   `catalog/patterns.md`: keeping a chosen conversation at
   the top of the list, with a plain pinned mark, a stated
   order where several conversations are pinned, and a
   one-action unpin that returns the conversation to its
   place by latest message — distinct from the pinned
   message row, which keeps one message in view inside a
   conversation, and from the archive conversation row,
   which moves a conversation out of the main list. Done
   when the row passes all quality gates. (Implemented this run.)

170. Add a stored payment method label pattern row to
   `catalog/patterns.md`: giving each stored method a
   plain name chosen by the person, shown beside its type
   and last digits wherever methods are listed, so two
   methods of the same type are told apart without opening
   either — distinct from the saved payment method
   selection row, which chooses a method at checkout, and
   from the expiring payment method replacement row, which
   carries a replacement into every use. Done when the
   row passes all quality gates. (Implemented this run.)

171. Add a conversation export pattern row to
   `catalog/patterns.md`: exporting one conversation as a
   file with messages in order, a stated scope for what is
   included, and a plain statement of what is left out —
   distinct from the data export row, which exports
   account data in bulk, and from the transcript editing
   row, which corrects a recorded transcript. Done when
   the row passes all quality gates. (Implemented this run.)

172. Add an appointment reminder pattern row to
   `catalog/patterns.md`: reminding before a booked
   appointment with its time, place, and route in the
   reminder itself, plus reschedule and cancel routes —
   distinct from the appointment management row, which
   manages booked time, and from the notification digest
   row, which groups low-urgency updates. Done when the
   row passes all quality gates. (Implemented this run.)

173. Add a dual approval pattern row to
   `catalog/patterns.md`: a sensitive change that takes
   effect only after a second, different person approves
   it, with the exact change stated in the request, a
   pending state that blocks any partial effect, an
   approval bound to the request as written and used
   once, a stated expiry, and a decision record naming
   who requested and who decided — distinct from the
   guardian approval request row, which lets one person
   approve for another, and from the sensitive-action
   re-confirmation row, which checks the same person's
   intent again. Done when the row passes all quality
   gates. (Implemented this run.)

174. Add an appointment check-in pattern row to
   `catalog/patterns.md`: checking in for a booked
   appointment from the booking or its reminder, with
   an arrival window stated separately from the service
   start, early, on-time, and late arrival states, a
   visible queue position, and a plain next step after
   check-in — distinct from the appointment management
   row, which manages booked time, and from the
   appointment reminder row, which reminds before the
   appointment. Done when the row passes all quality
   gates.
   (Implemented this run.)

175. Add a travel check-in pattern row to
   `catalog/patterns.md`: confirming travel for a booked
   trip, with a stated check-in window, seat and bag
   choices, a boarding pass kept reachable offline, and
   a plain next step for bag drop or direct boarding —
   distinct from the seat selection row, which chooses a
   seat, and from the travel disruption rebooking row,
   which changes a disrupted trip. Done when the row
   passes all quality gates.
   (Implemented this run.)

176. Add a stored payment method removal pattern row to
   `catalog/patterns.md`: removing a stored method with a
   stated list of the subscriptions and saved checkouts
   that used it, a plain statement of what happens to
   each — kept, re-pointed, or left without a method —
   and a confirmation that names the method by its
   label, distinct from the expiring payment method
   replacement row, which swaps a method before expiry,
   and from the backup payment method row, which keeps
   a second method ready for a failed charge. Done when
   the row passes all quality gates.
   (Implemented this run.)

177. Add a recurring appointment series pattern row to
   `catalog/patterns.md`: a repeating booking with a
   stated series rule, an edit-one versus edit-all
   choice for changes, and a cancel-one versus
   cancel-series choice, distinct from the appointment
   management row, which changes a single booking, and
   from the appointment reminder row, which reminds
   before one appointment. Done when the row passes all
   quality gates. (Implemented this run.)

178. Add a group conversation participant management
   pattern row to `catalog/patterns.md`: adding and
   removing participants in a group conversation, with
   a stated history rule for a new joiner — what past
   messages they can see — and a plain statement when
   a removed participant loses access, distinct from
   the conversation mute row, which silences alerts
   for one person, and from the saved collection
   sharing row, which shares a collection rather than
   a conversation. Done when the row passes all quality
   gates. (Implemented this run.)


179. Add a travel document checklist pattern row to
   `catalog/patterns.md`: the documents a trip needs
   listed before travel with an expiry check for each,
   a stated route to renew or replace a document that
   will expire during the trip, and a plain warning
   where a missing document blocks boarding — distinct
   from the travel check-in row, which confirms travel
   for a booked trip, and from the pass and ticket
   display row, which presents a pass already held. Done
   when the row passes all quality gates. (Implemented this run.)

180. Add an expense claim submission pattern row to
   `catalog/patterns.md`: a claim built from receipts
   with the amount, date, and category stated for each
   item, a stated approval route, and a plain state for
   each claim — submitted, approved, paid, or returned
   with a reason — distinct from the document scanner
   row, which captures a document, and from the order
   receipt row, which keeps a receipt after purchase.
   Done when the row passes all quality gates. (Implemented this run.)

181. Add a back-to-top control pattern row to
   `catalog/patterns.md`: a control that returns to the
   top of a long page, shown only after the person has
   scrolled past a stated distance, keeping focus at the
   top on activation, and never covering content or
   controls — distinct from the long-document navigation
   row, which moves within a document, and from the
   scrolling tab bar row, which moves between sections.
   Done when the row passes all quality gates. (Implemented this run.)

182. Add a travel itinerary view pattern row to
   `catalog/patterns.md`: a trip shown day by day with
   each day's bookings, places, and travel legs in order,
   changes to one day stated plainly with affected bookings
   named, and the whole itinerary reachable without a
   connection — distinct from the travel document
   checklist row, which checks documents before travel,
   and from the travel check-in row, which confirms
   travel for a booked trip. Done when the row passes all
   quality gates.
   (Implemented this run.)

183. Add a bill explanation pattern row to
   `catalog/patterns.md`: one bill broken down line by
   line with each charge named and dated, any discount,
   credit, or fee shown as its own line, and a dispute
   route from any line that looks wrong — distinct from
   the billing overview row, which summarises recurring
   charges across a period, and from the transaction
   dispute row, which disputes a charge already paid.
   Done when the row passes all quality gates.
   (Implemented this run.)

184. Add an appointment late-cancellation and no-show
   policy pattern row to `catalog/patterns.md`: the
   cancellation deadline, any fee for a late cancellation
   or a missed appointment, and the route to cancel late
   all stated before booking, with the policy repeated at
   confirmation and a plain statement of what happens to
   any prepayment — distinct from the appointment
   management row, which changes or cancels a booking,
   and from the appointment reminder row, which reminds
   before one appointment. Done when the row passes all
   quality gates.
   (Implemented this run.)

185. Add a shared trip itinerary pattern row to
   `catalog/patterns.md`: a trip itinerary shared with
   travelling companions, with a stated view-only or
   editable scope per person, changes by one person
   visible to the others with affected bookings named,
   and a route to stop sharing that keeps each person's
   own copy — distinct from the travel itinerary view
   row, which shows one person's trip, and from the
   saved collection sharing row, which shares saved
   items rather than a trip. Done when the row passes all
   quality gates. (Implemented this run.)

186. Add a booking deposit pattern row to
   `catalog/patterns.md`: a deposit taken at booking
   that counts toward the price, with the deposit amount,
   what it secures, and the refund rule for on-time
   cancellation, late cancellation, and a no-show all
   stated before payment, and the remaining balance and
   its due date shown beside the deposit — distinct from
   the appointment late-cancellation and no-show policy
   row, which states fees, and from the payment
   instalment plan row, which spreads a total. Done when
   the row passes all quality gates. (Implemented this run.)

187. Add an appointment standby list pattern row to
   `catalog/patterns.md`: a list joined when no booking
   is free, with the person's place stated, a stated
   offer window when a slot opens, a one-action accept
   that books the slot, and a plain expiry when the
   window passes — distinct from the waitlist row, which
   watches one item for restock, and from the appointment
   management row, which changes a booked time. Done when
   the row passes all quality gates. (Implemented this run.)

188. Add an emergency assistance request pattern row to
   `catalog/patterns.md`: a request sent with one action
   from wherever the person is, stating what kind of help
   is needed and sharing location at once, a short cancel
   window for accidental requests, a plain receipt stating
   what was sent and to whom, separate states for sent,
   received, and accepted, and a route to add essential
   details after the request rather than before it —
   distinct from the automated-to-human support handoff
   row, which moves a support conversation to a person,
   and from the service status notice row, which reports
   an outage. Done when the row passes all quality
   gates. (Implemented this run.)

189. Add a medication reminder pattern row to
   `catalog/patterns.md`: a reminder naming the dose in
   plain words with its amount and time, a stated schedule
   with a snooze and a taken or missed mark, a visible
   history of taken and missed doses, a plain route to
   change the schedule without losing the history, and a
   stated rule for what is shared and with whom — distinct
   from the appointment reminder row, which reminds before
   one booked time, and from the habit streak row, which
   counts consecutive days. Done when the row passes all
   quality gates. (Implemented this run.)

190. Add a recurring payment setup pattern row to
   `catalog/patterns.md`: a setup flow kept separate from
   a one-time payment, stating the amount, the date, and
   the method before the person authorises future payments,
   a stated pause, change, and cancel route from the setup
   itself, a plain notice before each charge and after a
   failed charge, and a stated rule for what happens when
   the payment method changes — distinct from the billing
   overview row, which summarises recurring charges, and
   from the subscription plan change row, which changes
   what is paid for. Done when the row passes all quality
   gates. (Implemented this run.)

191. Add an appointment preparation checklist pattern row to
   `catalog/patterns.md`: a short list of what to bring, what
   to do, and what to expect before a booked appointment, shown
   with the booking and again in the reminder, with each item
   checkable and a stated route where a preparation step cannot
   be completed — distinct from the appointment reminder row,
   which reminds before one booked time, and from the travel
   document checklist row, which checks documents before travel.
   Done when the row passes all quality gates. (Implemented this run.)

192. Add a deposit refund status pattern row to
   `catalog/patterns.md`: a plain statement of where a deposit
   refund stands after a cancellation — requested, sent, or
   received — with the amount, the method it returns to, and
   how long it takes to appear, and a stated route where a
   refund is delayed or missing — distinct from the booking
   deposit row, which states the refund rule before payment,
   and from the transaction dispute row, which disputes a
   charge already paid. Done when the row passes all quality
   gates. (Implemented this run.)

193. Add a medication refill request pattern row to
   `catalog/patterns.md`: a request sent before the supply runs
   out, stating how much is left and when it runs out, with a
   choice of delivery or pickup and a plain state for each
   request — sent, confirmed, or ready — distinct from the
   medication reminder row, which reminds the person to take a
   dose, and from the reorder past order row, which repeats a
   purchase already made. Done when the row passes all quality
   gates. (Implemented this run.)


194. Add a verified account badge pattern row to
   `catalog/patterns.md`: a badge shown beside the name
   only once a check is confirmed, stating what was checked
   and when, with levels named where they differ, and removed
   at once when the check no longer holds — distinct from the
   profile and account menu row, which shows who is signed
   in, and from the second-factor sign-in row, which proves
   the person at sign-in. Done when the row passes all
   quality gates. (Implemented this run.)

195. Add a virtual background in video calls pattern row to
   `catalog/patterns.md`: background blur as the plain
   default with a preview before joining, a stated limit
   that blur hides detail and not movement, a still-image
   replacement choice, a per-device setting changeable
   mid-call, and a camera-off offer where the device cannot
   run the effect — distinct from the live call controls
   row, which governs microphone, camera, and sharing
   toggles. Done when the row passes all quality gates.
   (Implemented this run.)

196. Add a world clock pattern row to `catalog/patterns.md`:
   several places shown at once with local time, date, and
   offset in plain figures, day-or-night marks and
   working-hours bands on a shared timeline, an overlap
   finder naming the shared window, and a share control
   stating every local time for a chosen moment — distinct
   from the time-zone picker row, which picks one zone for
   a single event. Done when the row passes all quality
   gates. (Implemented this run.)

197. Add a video-call waiting room pattern row to
   `catalog/patterns.md`: people joining before the host
   wait in a named holding view with a plain statement of
   what happens next, the host admits or declines each
   person by name, and nobody joins the call unannounced —
   distinct from the live call controls row, which governs
   microphone, camera, and sharing toggles once inside the
   call. Done when the row passes all quality gates.
   (Implemented this run.)

198. Add a sticker and GIF picker pattern row to
   `catalog/patterns.md`: a searchable picker inside the
   compose view with recent and saved items first, a plain
   text description for every item, and a preview before
   sending — distinct from the emoji picker row, which
   inserts a single character, and from the message
   reaction row, which responds to a message already sent.
   Done when the row passes all quality gates.
   (Implemented this run.)

199. Add a focus mode schedule pattern row to
   `catalog/patterns.md`: a named quiet-hours schedule
   with allowed contacts and apps stated plainly, a visible
   state while it is on, and a stated end that returns
   notifications in one summary — distinct from the
   reduced-motion preference row, which changes motion
   rather than delivery, and from the notification digest
   row, which groups low-urgency updates on a schedule.
   Done when the row passes all quality gates.
   (Implemented this run.)

200. Add a screen sharing in video calls pattern row to
   `catalog/patterns.md`: a share control that states what
   will be visible before sharing starts, a choice between
   one window and the whole screen, a visible sharing state
   with a one-action stop, and a stated rule that private
   content stays hidden — distinct from the live call
   controls row, which governs microphone, camera, and
   sharing toggles once inside the call, and from the
   virtual background row, which hides what is behind the
   person rather than what is on their screen. Done when the row passes all quality gates.
   (Implemented this run.)

201. Add a mute conversation pattern row to
   `catalog/patterns.md`: silence one conversation without
   leaving it, with a stated duration or until unmuted, a
   visible muted state, and messages still delivered and
   readable on opening — distinct from the focus mode
   schedule row, which silences delivery across the whole
   device, and from the archived conversation row, which
   removes a conversation from the list. Done when the row passes all quality gates.
   (Implemented this run.)

202. Add a page not found pattern row to
   `catalog/patterns.md`: a plain statement that the page
   does not exist, with the address kept visible, a way
   back to a known place, and a search offer — distinct
   from the error state rules in `catalog/states.md`, which
   cover failures inside a working page, and from the
   service status notice row, which reports a service-wide
   problem. Done when the row passes all quality gates.
   (Implemented this run.)

203. Add a raise hand in video calls pattern row to
   `catalog/patterns.md`: one control in the call controls and
   in the participants panel, a raised-hand mark on the tile and
   in the list, a visible queue in the order hands were raised,
   moderator lower-one and lower-all controls, auto-lower when
   the person speaks with a cancel step to keep the hand
   raised, and gesture detection off by default — distinct
   from the live call controls row, which governs microphone,
   camera, and sharing toggles, and from the video-call
   waiting room row, which holds people before they join.
   Done when the row passes all quality gates. (Implemented
   this run.) (Implemented this run.)

204. Add a disappearing messages pattern row to
   `catalog/patterns.md`: a per-conversation setting with a
   stated lifetime, a distinct visual style and a visible
   countdown for messages that will vanish, a stated rule for
   what happens to messages already sent when the setting
   changes, and a plain statement that a screenshot or a
   second device can keep a copy — distinct from the message
   edit and delete row, which removes one message on request,
   and from the conversation export row, which keeps a copy
   of the whole conversation. Done when the row passes all quality gates.
   (Implemented this run.)

205. Add a breakout rooms in video calls pattern row to
   `catalog/patterns.md`: a host-created set of smaller rooms
   with a stated size and a return route to the main call,
   assignment shown before joining, a stated rule for who can
   move between rooms, and a plain statement that breakout
   rooms are not recorded or streamed — distinct from the
   video-call waiting room row, which holds people before
   they join, and from the group conversation participant
   management row, which manages who is in a text
   conversation. Done when the row passes all quality gates. (Implemented this run.)

206. Add a call recording notice pattern row to
   `catalog/patterns.md`: a plain statement before recording starts,
   shown to everyone in the call, with a stated rule for who can
   start and stop it, a visible recording state for the whole
   recording, and a stated place where the recording is kept and
   for how long — distinct from the screen sharing row, which
   shares a live view rather than keeping a copy, and from the
   live call controls row, which governs microphone, camera, and
   sharing toggles. Done when the row passes all quality gates. (Implemented this run.)

207. Add an incoming call pattern row to
   `catalog/patterns.md`: the caller's identity stated plainly,
   accept and decline controls that work without unlocking the
   device, a quick reply for a declined call, and a stated rule
   that declining sends the caller to a missed-call note rather
   than silence — distinct from the live call controls row,
   which governs a call once it has started, and from the
   video-call waiting room row, which holds people before the
   host admits them. Done when the row passes all quality gates. (Implemented this run.)

208. Add a missed call pattern row to
   `catalog/patterns.md`: a missed-call entry in the call list
   with the caller's identity and the time of the call, a
   one-action call back, and a stated rule that a missed call
   never clears itself without the person choosing to clear it
   — distinct from the incoming call pattern in action 207,
   which handles a call while it is ringing, and from the
   notification list row, which gathers alerts rather than
   calls. Done when the row passes all quality gates. (Implemented this run.)

209. Add a call waiting pattern row to `catalog/patterns.md`:
   a second incoming call during a live call — the new
   caller's identity stated plainly, accept puts the current
   call on hold with a stated hold state and a one-action
   return, decline sends the caller to a missed-call note,
   and merge is offered only where the call supports it —
   with a plain warning before any action that would drop
   the first call — distinct from the incoming call row,
   which handles a call while the device is idle, and from
   the live call controls row, which governs toggles once
   inside a call. Done when the row passes all quality gates. (Implemented this run.)

210. Add an outgoing call pattern row to `catalog/patterns.md`:
   dialling, ringing, connecting, busy, no-answer, and
   failed states, each stated plainly with a next action; a
   ringing call can be cancelled in one action; a failed call
   states the cause where known and offers retry or a
   message instead of redialling blindly — distinct from the
   incoming call row, which handles a call while it is
   ringing in, and from the missed call row, which records
   a call that was not answered. Done when the row passes
   all quality gates. (Implemented this run.)

211. Add a call quality and reconnection pattern row to
   `catalog/patterns.md`: when the connection weakens, a
   plain warning on the affected tile states what is
   happening and what to do; an audio-only fallback keeps
   the call alive where video cannot; on a dropped
   connection the call reconnects automatically where
   possible and states plainly what was lost and what was
   kept — distinct from the live call controls row, which
   shows a connection-trouble indicator, and from the
   background-task progress row, which reports work that
   continues out of sight. Done when the row passes all
   quality gates. (Implemented this run.)

212. Add a call transfer pattern row to `catalog/patterns.md`:
   moving a live call to another person or team — a blind
   transfer sends the call straight through, an attended
   transfer holds the caller while the receiving person is
   briefed first, and the caller is told the reason and who
   they are being passed to before the move; the caller never
   has to repeat what was already said, because the reason and
   the details already given travel with the call; where the
   receiving person cannot take the call, the caller is
   offered a message or a call back rather than being
   dropped — distinct from the automated-to-human support
   handoff row, which moves a conversation from automated
   help to a person, and from the pass or ticket transfer row,
   which passes a held item to another person. Done when the
   row passes all quality gates. (Implemented this run.)

213. Add a visual voicemail pattern row to `catalog/patterns.md`:
   a list of recorded messages with the caller's identity,
   the time, and the length, each playable in any order with
   pause and scrub controls, and a written transcript where
   one is available that is labelled as a transcript and never
   trusted for exact details such as times or numbers without
   listening; messages are marked as heard only after they are
   played or read, never by opening the list; a message can be
   saved, shared, or deleted one at a time, with deletion
   confirmed and a full inbox stated plainly before new
   messages are refused — distinct from the missed call row,
   which records a call that was not answered, and from the
   voice message row, which carries a recorded message inside
   a conversation. Done when the row passes all quality gates. (Implemented this run.)

214. Add a suspected spam call warning pattern row to
   `catalog/patterns.md`: when a call is flagged as likely
   unwanted, the warning is shown in plain words on the
   incoming call screen before any action is taken, with the
   reason stated where it is known and the number shown in
   full; the person can answer, decline, or block and report
   the number from the same screen; a wrongly flagged call can
   be marked as not unwanted so it is not flagged again;
   suspected calls are never silenced without the person's
   choice, and a blocked number's calls go to a stated place
   rather than vanishing — distinct from the incoming call
   row, which handles an ordinary call while it is ringing in,
   and from the content reporting and blocking row, which
   reports content rather than calls. Done when the row passes
   all quality gates. (Implemented this run.)

215. Add a reading view pattern row to
   `catalog/patterns.md`: a screen reading mode that removes
   navigation, banners, and interactive controls, with text
   size, line spacing, and light-or-dark background controls,
   a stated reading position that survives leaving and
   returning, and a one-action exit back to the full page —
   distinct from the simplified view row, which reduces
   cognitive load across the whole product, and from the
   print-friendly view row, which prepares a page for
   printing rather than for reading on screen. Done when the
   row passes all quality gates. (Implemented this run.)

216. Add a call screening pattern row to
   `catalog/patterns.md`: for an unknown caller, ask who is
   calling and why before the person answers, showing the
   spoken answer as text on the incoming-call screen, with
   accept, decline, and block-and-report from the same
   screen, and a stated rule that a screened call is never
   answered silently — distinct from the suspected spam call
   warning row, which labels a call from known patterns, and
   from the visual voicemail row, which records a message
   after the call is missed. Done when the row passes all
   quality gates. (Implemented this run.)

217. Add an add-people-to-a-live-call pattern row to
   `catalog/patterns.md`: invite others into a call already
   in progress, with the invite sent from the call itself, a
   stated announcement naming each person as they join, and
   a host control to remove someone who joined by mistake —
   distinct from the video-call waiting room row, which holds
   people before the host admits them, and from the group
   conversation participant management row, which manages
   who is in a text conversation. Done when the row passes
   all quality gates. (Implemented this run.)

218. Add a conference call pattern row to
   `catalog/patterns.md`: merge two or more live calls into
   one call, with a participant list naming everyone on the
   line, a drop-one-participant control, a speak-privately
   control that holds the others, a stated participant limit,
   a warning where the host leaving ends the call for
   everyone, and a plain notice where merging is not
   supported — distinct from the call waiting row, which
   handles a second incoming call during a live call, and
   from the breakout rooms row, which splits one call into
   smaller rooms. Done when the row passes all quality
   gates. (Implemented this run.)

219. Add a call history pattern row to
   `catalog/patterns.md`: a chronological list of incoming,
   outgoing, and missed calls with the type, time, and
   duration of each, a filter by call type, a one-action
   redial or call back, per-entry delete and a clear-all
   control, a stated retention limit, and a rule that a
   missed call never clears itself without the person's
   choice — distinct from the missed call row, which records
   a single missed call, and from the recently viewed row,
   which lists opened items rather than calls. Done when
   the row passes all quality gates. (Implemented this run.)

220. Add a call forwarding pattern row to
   `catalog/patterns.md`: forward incoming calls to another
   number, always or only when busy, unanswered, or
   unreachable, with a separate destination per rule, the
   active rules stated with their destinations shown, a
   one-action turn-off for each rule, and a plain warning
   where forwarding overrides voicemail — distinct from the
   call transfer row, which moves a live call to another
   person, and from the visual voicemail row, which holds
   messages left after a missed call. Done when the row
   passes all quality gates. (Implemented this run.)

221. Add a voicemail greeting pattern row to
   `catalog/patterns.md`: a default or custom greeting that
   callers hear before leaving a message, record with
   playback before saving, re-record without losing the
   previous greeting until the new one saves, a stated
   length limit, and a plain return to the default greeting
   — distinct from the visual voicemail row, which lists
   messages already left, and from the call screening row,
   which asks an unknown caller who they are before the
   person answers. Done when the row passes all quality
   gates. (Implemented this run.)

222. Add a parking session payment pattern row to
   `catalog/patterns.md`: start a parking session by entering
   the zone shown on the sign or choosing it on a map, choose
   the vehicle and the duration with the rate and total cost
   stated before payment, show the remaining time live with a
   reminder before expiry that extends the session from the
   notice itself, state the maximum stay for the zone, and
   keep a receipt for the session — distinct from the ride
   booking row, which books a trip rather than a parking
   stay, and from the order tracking row, which follows a
   delivery rather than a timed session. Done when the row
   passes all quality gates. (Implemented this run.)

223. Add a screenshot markup pattern row to
   `catalog/patterns.md`: crop, arrows, shapes, text labels,
   highlights, and numbered steps for marking up a captured
   image, with a blur or solid block for private details
   applied before sharing, every mark editable, movable, or
   removable after it is placed, and the original capture kept
   unchanged — distinct from the media viewer row, which shows
   an image without changing it, and from the document scanner
   row, which captures a page rather than explaining a
   capture. Done when the row passes all quality gates. (Implemented this run.)

224. Add a group chat administration pattern row to
   `catalog/patterns.md`: owner, admin, and member roles with
   per-permission toggles for editing group details, sending
   messages, adding members, approving new members, and
   removing members, an ownership transfer that names the new
   owner before it happens, and blocked and removed member
   lists with a stated route back — distinct from the group
   conversation participant management row, which manages who
   is in a conversation without the role and permission rules,
   and from the invitation response row, which answers one
   invitation rather than governing a group. Done when the row
   passes all quality gates. (Implemented this run.)

225. Add a worked example for the watch layout under
   `examples/watch/`: a glance-first watch surface demonstrating
   the two-tap rule, complications-first placement, the ambient
   always-on variant, and all seven states — distinct from the
   dashboard and mobile navigation examples, which demonstrate
   larger-screen rules, and from the onboarding example, which
   demonstrates a multi-step flow. Done when the example passes
   all quality gates. (Implemented this run.)
226. Add a tenant-portal pattern row to `catalog/patterns.md`:
   rent payment with a stated due date and receipt, maintenance
   requests tracked from report to fix with a stated response
   time, document access for the agreement and notices, and
   messaging with the property contact — recorded only when a
   non-vendor quality source is found; single-vendor help pages
   do not meet the source-quality bar — distinct from the
   payment rows, which cover one payment without the tenancy
   record, and from the request-tracking rows, which follow one
   request without the tenancy context. Done when the row passes
   all quality gates. (Implemented this run.)

227. Add a worked example for the television layout under
   `examples/tv/`: a row-and-column shelf surface demonstrating
   visible focus, focus memory, Back-button behaviour, and
   10-foot legibility with all seven states — distinct from the
   dashboard example, which demonstrates dense multi-pane rules,
   and from the mobile navigation example, which demonstrates
   touch-first navigation. Done when the example passes all
   quality gates. (Implemented this run.)

228. Add a hotel booking pattern row to
   `catalog/patterns.md`: search by destination, dates, and
   guests, compare stays by the full cost including taxes and
   fees rather than the nightly headline, choose a room and a
   rate with its cancellation terms stated for that rate, hold
   the price with a stated expiry while payment is entered,
   and confirm with a booking reference, a full price
   breakdown, and a plain cancellation route — distinct from
   the travel check-in row, which handles arrival rather than
   booking, and from the travel itinerary view row, which
   shows a booked trip rather than choosing a stay. Done when
   the row passes all quality gates. (Implemented this run.)

229. Add an electric vehicle charging session pattern row to
   `catalog/patterns.md`: find a charger with live
   availability, connector type, and price before driving
   there, start the session by scanning the code on the
   charger or tapping in the app, show the live session with
   energy delivered, power, cost, and estimated completion,
   end the session at any time from the same screen, and keep
   a receipt for every session with a session history —
   distinct from the parking session payment row, which pays
   for a timed stay rather than energy delivered, and from
   the contactless payment confirmation row, which confirms
   one payment without a live session. Done when the row
   passes all quality gates. (Implemented this run.)

230. Add a smart home dashboard pattern row to
   `catalog/patterns.md`: organise by room rather than by
   device list, with a tile per device showing its current
   state and its own controls, scenes that run several
   devices at once, automations that state their trigger,
   conditions, and actions, and guest profiles limited to
   chosen rooms — distinct from the home control map row,
   which places devices on a floor plan rather than in room
   lists, and from the device pairing row, which connects a
   new device rather than controlling the home. Done when the
   row passes all quality gates. (Implemented this run.)

## Review notes

- Completed this review (deep editorial 2026-11-08): new Transit card top-up and In-flight entertainment pattern rows in `catalog/patterns.md`, completing roadmap actions 240 and 241; coverage matrix reconciled with the catalogue (47 rows added, two stale entries removed); three new improvement actions added (243 screen time dashboard, 244 standardised accessibility labels, 245 desktop worked example); 4 new source records (675 total). QR table ordering (action 242) re-checked: consumer-protection guidance on fake QR codes confirms the genuine-code check, but the primary advisory page did not surface and the order-and-pay flow still rests only on vendor guides, so the action stays open.

- Completed this review (daily planning 2026-11-08): new Sleep and
  rest data pattern row in `catalog/patterns.md`, completing roadmap
  action 234; coverage matrix updated with the new row; three new
  improvement actions added (234 sleep and rest data, 235 telehealth
  video consultation, 236 museum audio guide); no new source records
  — the five searches (sleep tracking dashboard, museum audio guide,
  telehealth video consultation, tenant portal, EN 301 549 citation)
  returned only single-topic blogs, agency pieces, single-designer
  case studies, vendor help pages, and tutorial sites below the
  source-quality bar; the EN 301 549 v4.1.1 citation in the Official
  Journal is still pending, with a provisional target of 30 November
  2026, so the standards outlook note stands as written. Since the
  last daily run, the deep cycle completed actions 215, 216, 217,
  219, 220, 221, 222, 223, 224, 228, 229, and 230 and the light
  cycles added the cookie consent banner, PIN entry, accessibility
  labels, deceptive design patterns, transaction history, fare-capped
  transit payment, and spatial interfaces placement rows; those
  outcomes are already recorded in `CHANGELOG.md`.

- Completed this review (deep editorial 2026-11-07): new
  Parking session payment, Screenshot markup, and Group chat
  administration pattern rows in `catalog/patterns.md`,
  completing roadmap actions 222, 223, and 224; coverage
  matrix updated with the three new rows; three new
  improvement actions added (228 hotel booking, 229 electric
  vehicle charging session, 230 smart home dashboard); no new
  source records — the six searches (parking session payment,
  screenshot markup, group chat administration, hotel booking,
  electric vehicle charging, smart home dashboard) returned
  only single-product help pages, app store listings, vendor
  blogs, and single-author guides below the source-quality
  bar, so the three genuine gaps they confirmed (hotel
  booking, electric vehicle charging, smart home dashboard)
  are recorded as actions 228-230 instead.

- Completed this review (deep editorial 2026-11-07): watch,
  automotive, television, and modular card grid rules expanded
  from current research — complications-first placement and
  quick-dismiss gesture on watch, five safety-critical physical
  controls and control-by-task split for automotive, row-and-column
  grid navigation and Back-button behaviour for television, and
  independent card loading, failure, refresh, and stale-data age
  for card grids; coverage matrix updated with watch and television
  worked examples as gaps; three new improvement actions added
  (225 watch worked example, 226 tenant portal, 227 television
  worked example); 4 new source records (636 total).

- Completed this review (deep editorial 2026-11-07): new
  Reading view, Add people to a live call, and Call history
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 215, 217, and 219; coverage matrix updated with the
  three new rows; three new improvement actions added (222
  parking session payment, 223 screenshot markup, 224 group
  chat administration); no new source records — the seven
  searches returned only single-product help pages, device
  manuals, single-topic blogs, and app listings below the
  source-quality bar, so the three genuine gaps they confirmed
  (parking, screenshot markup, group chat administration)
  are recorded as actions 222-224 instead.

- Completed this review (daily planning 2026-11-07): new
  Conference call pattern row in `catalog/patterns.md`,
  completing roadmap action 218; coverage matrix updated
  with the new row; four new improvement actions added
  (218 conference call, 219 call history, 220 call
  forwarding, 221 voicemail greeting); no new source
  records — the four searches (conference call merging and
  participant management, call history lists, voicemail
  greeting recording, call forwarding rules) returned
  how-to guides and manuals below the source-quality bar
  (626 total). Since the last daily run, the deep cycle
  completed actions 205, 212, and 214 and the catalogue
  gained the Game interfaces section and the Digital
  identity wallet presentation row; those outcomes are
  already recorded in `CHANGELOG.md`.

- Completed this review (deep editorial 2026-11-07): new
  Breakout rooms in video calls, Call transfer, and Suspected
  spam call warning pattern rows in `catalog/patterns.md`,
  completing roadmap actions 205, 212, and 214; coverage
  matrix updated with the three new rows; three new
  improvement actions added (215 reading view, 216 call
  screening, 217 add people to a live call); 3 new source
  records (623 total).

- Completed this review (deep editorial 2026-11-06, fourth cycle): new
  Call waiting, Outgoing call, and Call quality and reconnection
  pattern rows in `catalog/patterns.md`, completing roadmap actions
  209, 210, and 211; coverage matrix updated with the three new
  rows; three new improvement actions added (212 call transfer,
  213 visual voicemail, 214 suspected spam call warning); 2 new
  source records (613 total; the call waiting source was already
  recorded).

- Completed this review (deep editorial 2026-11-06, third cycle): new
  Call recording notice, Incoming call, and Missed call pattern rows
  in `catalog/patterns.md`, completing roadmap actions 206, 207, and
  208; coverage matrix updated with the three new rows; three new
  improvement actions added (209 call waiting, 210 outgoing call,
  211 call quality and reconnection); 3 new source records (606 total).

- Completed this review (deep editorial 2026-11-06, second cycle): new
  Screen sharing in video calls, Mute conversation, and Disappearing
  messages pattern rows in `catalog/patterns.md`, completing roadmap
  actions 200, 201, and 204; coverage matrix updated with the three
  new rows; three new improvement actions added (206 call recording
  notice, 207 incoming call, 208 missed call); 3 new source records
  (595 total).

- Completed this review (daily planning 2026-11-06): new
  Raise hand in video calls pattern row in `catalog/patterns.md`,
  completing roadmap action 203; coverage matrix updated with
  the new row; three new improvement actions added (203 raise
  hand in video calls, 204 disappearing messages, 205
  breakout rooms in video calls); 3 new source records (591
  total). Since the last daily run,
  the deep cycle completed actions 197, 198, and 199 and the
  catalogue gained the Sticker and GIF picker row; those
  outcomes are already recorded in `CHANGELOG.md`.

- Completed this review (deep editorial 2026-11-06): new
  Sticker and GIF picker pattern row in `catalog/patterns.md`,
  completing roadmap action 198; actions 197 (video-call
  waiting room) and 199 (focus mode schedule) marked
  implemented to match rows already in the catalogue, and
  the coverage matrix updated with the five rows added by
  earlier runs (video-call waiting room, focus mode
  schedule, sticker and GIF picker, product questions and
  answers, shared whiteboard); three new improvement
  actions added (200 screen sharing in video calls, 201
  mute conversation, 202 page not found); duplicate
  implemented marker removed from action 180; 3 new source
  records (583 total).

- Completed this review (deep editorial 2026-11-05): new
  Expense claim submission, Read receipt, and Typing
  indicator pattern rows in `catalog/patterns.md`, completing
  roadmap action 180 (which was marked implemented but had
  no row in the catalogue) and adding the two messaging rows
  after verifying no existing row covered them; coverage
  matrix updated with the three new rows; three new
  improvement actions added (197 video-call waiting room,
  198 sticker and GIF picker, 199 focus mode schedule);
  3 new source records (574 total).

- Completed this review (daily planning 2026-11-05): new
  Emergency assistance request pattern row in
  `catalog/patterns.md`, completing roadmap action 188;
  coverage matrix updated with the new row; three new
  improvement actions added (189 medication reminder,
  190 recurring payment setup); 3 new source records
  (551 total). Since the last daily run, the deep cycle
  completed actions 170, 171, 172, 174, 175, and 176 and
  the catalogue gained rows completing actions 63, 177,
  179, 181, 182, 183, 184, and 185, plus the Shared
  subscription plan, Group scheduling poll, Bottom sheet
  choice, and Trigger-character suggestion menu rows;
  those outcomes are already recorded in `CHANGELOG.md`.


- Completed this review (deep editorial 2026-11-04, second cycle): new
  Appointment check-in, Travel check-in, and Stored
  payment method removal pattern rows in
  `catalog/patterns.md`, completing roadmap actions 174,
  175, and 176; coverage matrix updated with the three
  new rows; three new improvement actions added (179
  travel document checklist, 180 expense claim
  submission, 181 back-to-top control); 1 new source
  record (537 total).


- Completed this review (deep editorial 2026-11-04): new
  Stored payment method label, Conversation export, and
  Appointment reminder pattern rows in
  `catalog/patterns.md`, completing roadmap actions 170,
  171, and 172; coverage matrix updated with the three
  new rows; three new improvement actions added (176
  stored payment method removal, 177 recurring
  appointment series, 178 group conversation
  participant management); 3 new source records (535
  total).



- Completed this review (daily planning 2026-11-04): new
  Dual approval pattern row in `catalog/patterns.md`,
  completing roadmap action 173; coverage matrix updated
  with the new row; three new improvement actions added
  (174 appointment check-in, 175 travel check-in);
  1 new source record (531 total).


- Completed this review (deep editorial 2026-11-04): new
  In-conversation message search and Expiring payment
  method replacement pattern rows in `catalog/patterns.md`,
  completing roadmap actions 167 and 168; coverage matrix
  updated with the two new rows; three new improvement
  actions added (170 stored payment method label, 171
  conversation export, 172 appointment reminder); 2 new
  source records (529 total).


- Completed this review (deep editorial 2026-11-03): new
  help-search recovery rule in the In-product help row,
  link-preview rule in the Share link row, and
  second-factor method-change rule in the Second-factor
  sign-in row in `catalog/patterns.md`, completing roadmap
  actions 29, 30, and 31; coverage matrix checked against
  the actual catalogue and left unchanged, since the three
  changes extend existing rows rather than adding new
  pattern rows; three new improvement actions added (164
  conversation mute, 165 reduced-motion preference, 166
  archive conversation); 3 new source records (518 total).


- Completed this review (deep editorial 2026-11-03): new
  Group checkout, Gift receipt, and Store pickup pattern
  rows in `catalog/patterns.md`, completing roadmap
  action 148; coverage matrix updated with the three new
  rows; three new improvement actions added (161 message
  forwarding, 162 return label and drop-off, 163 saved
  collection sharing); 3 new source records (509 total).

- Completed this review (daily planning 2026-11-03): new
  QR sign-in pattern row in `catalog/patterns.md`,
  completing roadmap action 158; coverage matrix updated
  with the QR sign-in row and the previously missing
  high-demand queue row; three new improvement actions
  added (158 QR sign-in, 159 delivery reschedule, 160
  loyalty tier progress); 1 new source record (501 total).
  Since the last daily run, the deep cycle completed actions
  149, 150, and 151 and a light cycle completed action 155;
  those outcomes are already recorded in `CHANGELOG.md`.

- Completed this review (deep editorial 2026-11-03): new
  Product recall notice, Account merge, and Loyalty points
  expiry warning pattern rows in `catalog/patterns.md`,
  completing roadmap actions 149, 150, and 151; coverage
  matrix updated with the three new rows; three new
  improvement actions added (155 high-demand queue, 156 price
  history display, 157 subscription gifting); 3 new source
  records (499 total).


- Completed this review (deep editorial 2026-11-02): new
  File preview, Search history, and Passkey sign-in pattern
  rows in `catalog/patterns.md`, completing roadmap actions
  48, 49, and 67; coverage matrix updated with the new rows;
  three new improvement actions added (152 download manager,
  153 voice message transcript, 154 checkout worked example);
  3 new source records (494 total).

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


- Completed this review (deep editorial 2026-10-31): new
  Pass and ticket display, Shared cart, and Stored payment
  method expiry warning pattern rows in `catalog/patterns.md`,
  completing roadmap actions 109, 110, and 111; coverage
  matrix updated with the three new rows; three new
  improvement actions added (115 pass or ticket transfer,
  116 backup payment method, 117 checkout price-change
  confirmation); 3 new source records (419 total).


- Completed this review (deep editorial 2026-10-31): new
  Meeting and event creation, Shared resource booking, and
  Backup payment method pattern rows in `catalog/patterns.md`,
  completing roadmap actions 113, 114, and 116; coverage
  matrix refreshed to match the actual catalogue (pattern
  rows added since the last matrix refresh plus the three new
  rows); three new improvement actions added (118
  subscription pause, 119 saved search alert, 120 data
  import); 1 new source record (434 total).


- Completed this review (deep editorial 2026-11-03): new
  Reduced-motion preference and Archive conversation
  pattern rows in `catalog/patterns.md`, completing
  roadmap actions 165 and 166; a reduced-motion rule
  added to the hero section of `layouts/landing.md`;
  coverage matrix updated with the two new rows; three
  new improvement actions added (167 in-conversation
  message search, 168 expiring payment method
  replacement, 169 pinned conversation); 2 new source
  records (523 total).

- Completed this review (deep editorial 2026-11-05): new
  Travel itinerary view, Bill explanation, and
  Appointment late-cancellation and no-show policy
  pattern rows in `catalog/patterns.md`, completing
  roadmap actions 182, 183, and 184; coverage matrix
  updated with the three new rows; three new
  improvement actions added (185 shared trip itinerary,
  186 booking deposit, 187 appointment standby list);
  3 new source records (545 total).

- Completed this review (deep editorial 2026-11-05): new
  Booking deposit, Appointment standby list, and Medication
  reminder pattern rows in `catalog/patterns.md`, completing
  roadmap actions 186, 187, and 189, and marking action 185
  (Shared trip itinerary, implemented in an earlier run)
  implemented to match the catalogue; coverage matrix updated
  with the three new rows and with four rows added by earlier
  runs (shared trip itinerary, ride booking, bottom sheet
  choice, trigger-character suggestion menu); three new
  improvement actions added (191 appointment preparation
  checklist, 192 deposit refund status, 193 medication
  refill request); 3 new source records (555 total).


## Pre-publish checklist

The canonical publishing checklist lives in `CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The coverage matrix matches the actual files and directories.
- [ ] Only open improvement actions remain listed; completed ones moved to CHANGELOG.md.
- [ ] Exactly three new actions were added at the last deep review.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.

231. Add a guest mode pattern row to `catalog/patterns.md`:
   a temporary session on a shared device that needs no sign-in,
   with a stated scope of what the guest can see and do, a
   one-action start and a one-action end, and everything the
   guest did cleared on exit, including history, downloads, and
   signed-in state — distinct from the household member
   management row, which gives a named person persistent access,
   and from the guest checkout row, which covers one purchase
   without an account. Done when the row passes all quality
   gates. (Implemented this run.)

232. Add a worked example for the kiosk layout under
   `examples/kiosk/`: a single-task public surface demonstrating
   the reach range, one task per screen, glance budgets, an
   assistive entry point usable without vision, a session reset
   after inactivity, and all seven states — distinct from the
   dashboard and mobile navigation examples, which demonstrate
   private-screen rules, and from the onboarding example, which
   demonstrates a multi-step flow. Done when the example passes
   all quality gates. (Implemented this run.)

233. Add a range-band refinement to the Date picker primitive row
   in `catalog/primitives.md`: a month grid for a day or a
   range, with a fluid hover across both months and a range band
   that follows the pointer, so the span under consideration
   stays visible while the person moves — distinct from the
   date-range picker pattern row, which governs the flow around
   choosing a range, and from the calendar date grid rules,
   which govern one month at a time. Done when the row passes
   all quality gates. (Implemented this run.)

234. Add a sleep and rest data pattern row to
   `catalog/patterns.md`: a morning view that leads with the
   seven-day trend rather than a single night's grade, plain
   words with no judgement language and no red grading, stated
   measurement limits, missing nights stated rather than filled
   in, and at most one suggested change tied to the pattern —
   distinct from the focus mode schedule row, which silences
   interruptions, and from the sleep timer row, which stops
   playback. Done when the row passes all quality gates.
   (Implemented this run.)

235. Add a telehealth video consultation pattern row to
   `catalog/patterns.md`: a pre-call check of camera,
   microphone, and connection before a paid consultation
   starts, the clinician's name and role visible throughout,
   large labelled controls for mute, camera, and ending the
   call, a stated state when the connection drops, and a
   summary after the call naming the next step — prescription,
   follow-up booking, or test referral — distinct from the
   appointment management row, which books the time, and from
   the video-call waiting room row, which holds people before
   admission. Done when the row passes all quality gates. (Implemented this run.)
236. Add a museum audio guide pattern row to
   `catalog/patterns.md`: per-exhibit audio tracks reachable by
   map, search, scan, or a track list, a structured tour in
   exhibit order or freestyle exploration, language choice
   offered first, fine-grained playback control including speed,
   a written text alternative beside each track, and tracks kept
   available without a connection where the visit is indoors —
   distinct from the guided tour row, which points out elements
   inside the product itself, and from the media chapters row,
   which marks sections inside one item. Done when the row passes all quality gates. (Implemented this run.)

237. Extend the crowdfunding campaign page row in
   `catalog/patterns.md` with reward-tier and backer-update rules
   once a qualifying source surfaces: tier structure with what
   each tier includes and when it is delivered, and an update
   cadence that reports progress and delays to backers — the
   current row covers purpose, identity, fees, target, and time
   limit from regulator guidance, and the reward and update
   material rests only on single-vendor platform guides below
   the source-quality bar. Done when the extended row passes all
   quality gates. (Implemented this run.)

238. Extend the shared bike and scooter rental row in
   `catalog/patterns.md` with the unlock, ride, and park
   interaction flow once a platform or design-system source
   surfaces: the in-app sequence from finding a vehicle through
   unlocking, riding, and ending the ride — the current row
   covers pricing, parking, end-of-ride confirmation, and
   accessibility from regulator and industry-body guidance, and
   the interaction flow itself has no qualifying source yet.
   Done when the extended row passes all quality gates. (Implemented this run.)

239. Reconcile the improvement-actions list in `roadmap.md` with
   the catalogue: mark every action whose row already exists in
   `catalog/patterns.md` or whose example already exists under
   `examples/` as implemented, so the open list reflects real
   gaps rather than work already done — several early actions
   were implemented without the marker being added. Done when
   the open-action count matches the catalogue and the change is
   recorded in `CHANGELOG.md`. (Implemented this run.)

240. Add a transit card top-up pattern row to
   `catalog/patterns.md`: add stored value to a travel card from a
   phone or a station machine, with the balance and the fare shown
   before paying, preset and custom amounts, a stated minimum and
   card limit, an auto top-up with a stated threshold and a way to
   stop it, and a receipt that states the new balance — distinct
   from the gift card and stored-credit redemption row, which
   covers merchant credit rather than fare value, and from the
   pass and ticket display row, which shows a ticket rather than
   adding value. Done when the row passes all quality gates.
   (Implemented this run.)

241. Add an in-flight entertainment pattern row to
   `catalog/patterns.md`: a seatback screen for one passenger, with
   a welcome step that sets language first, browse and search over
   content held on board, playback that survives a restart,
   captions and audio description, touch and a hand-held remote,
   and a stated offline state — distinct from the television
   layout, which assumes a room screen and a shared remote, and
   from the media chapters row, which marks sections inside one
   item. Done when the row passes all quality gates. (Implemented this run.)

242. Add a QR table ordering pattern row to
   `catalog/patterns.md`: order and pay from a table without
   waiting for staff, with one code per table that opens the menu
   with the table already known, no app to install, the table
   named on the kitchen ticket, a call-staff action on the same
   screen, and a stated check that the code on the table is
   genuine — distinct from the QR code payment at a till row,
   which pays a fixed amount at a counter, and from the store
   pickup row, which hands an order over in person. Done when
   the row passes all quality gates. (Implemented this run: an
   independent review of the order-and-pay flow covering the
   genuine-code check and accessibility guidance for the menu page,
   plus an end-to-end table-ordering guide, now recorded as
   sources.)

243. Add a screen time dashboard pattern row to
   `catalog/patterns.md`: show how much time was spent in each
   app or category over a stated period, with a daily limit the
   person sets, a warning before the limit, and a plain route to
   change or remove the limit — distinct from the usage allowance
   row, which meters a paid allowance rather than time, and from
   the focus mode schedule row, which silences interruptions
   rather than reporting use. Done when the row passes all
   quality gates. (Implemented this run: design-principles
   guidance for wellbeing dashboards and a cross-platform setup
   guide for limits, downtime, and focus presets now recorded as
   sources.)

244. Extend the accessibility labels on a store listing row in
   `catalog/patterns.md` with a standardised label format once
   platform or standards guidance surfaces: a fixed set of labels
   with the same wording and order on every listing, so labels
   can be compared across apps — the current row covers per-app
   declared support from one platform help page, and no published
   label schema has surfaced. Done when the extended row passes
   all quality gates. (Implemented this run.)

245. Add a desktop worked example under `examples/`: a worked
   example demonstrating the desktop layout — multiple windows or
   panes, a menu bar, keyboard shortcuts, and drag-and-drop
   between panes — with all seven states, so the desktop rules
   can be checked against a complete screen rather than a single
   layout file — distinct from the dashboard, mobile navigation,
   onboarding, watch, kiosk, and television examples, which
   demonstrate other layouts. Done when the example passes all
   quality gates. (Implemented this run: a worked example under
   `examples/desktop/` with a menu bar, toolbar, two panes with
   drag-and-drop and a keyboard path, window strip, status bar,
   and all seven states.)

246. Add a recurring donation pattern row to
   `catalog/patterns.md`: a gift repeated on a stated interval
   with the amount, the interval, and the next gift date shown
   before confirmation, a plain pause, change, or cancel route
   that takes effect before the next gift, and a yearly summary
   for the person's own records — distinct from the donation at
   checkout row, which takes a one-off gift with a purchase, and
   from the recurring payment setup row, which schedules a
   payment for a service rather than a gift. Done when the row
   passes all quality gates. (Implemented this run.)

247. Add a temporary home access code pattern row to
   `catalog/patterns.md`: a time-limited code for a guest or a
   worker that opens one door for a stated period, with the code,
   the door, and the expiry stated before it is shared, a revoke
   route that ends access at once, and a plain entry record
   naming when the code was used — distinct from the digital car
   key sharing row, which shares a vehicle key, and from the
   guest mode row, which lends a device session rather than entry
   to a place. Done when the row passes all quality gates.
   (Implemented this run.)

248. Add a health record sharing pattern row to
   `catalog/patterns.md`: sharing a health record with a clinician
   or a carer with the scope stated before sharing, an expiry
   after which access ends on its own, and a revoke route that
   ends access at once, with a plain record of who saw what and
   when — distinct from the telehealth video consultation row,
   which holds a consultation rather than sharing a record, and
   from the medication refill request row, which asks for a repeat
   prescription. Done when the row passes all quality gates.
   (Implemented this run: a standards specification for sharing
   health records by link or code, government consent guidance,
   and record-sharing design notes now recorded as sources.)

249. Add a self-checkout grocery kiosk pattern row to
   `catalog/patterns.md`: a scan-and-pay loop on a shared public
   screen — scan each item with a running total always visible,
   produce lookup for items without a code, a stated void route
   for a wrong scan, bagging-area verification that states what
   it checks and what to do when it disagrees, an age check that
   hands to staff without exposing the purchase, and payment on
   the same screen with a plain receipt route — cross-checked
   against the kiosk rules in `layouts/kiosk.md` and the
   contactless payment confirmation row. Sources so far are
   vendor guides only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. (Implemented this run.)

250. Add an indoor wayfinding pattern row to
   `catalog/patterns.md`: finding a destination inside a
   building from a directory or a phone — a prominent
   you-are-here marker oriented to the viewer's facing
   direction, a short list of common destinations first with
   search for the rest, a route shown step by step with a stated
   distance and time, a step-free route offered where one
   exists, and a handoff to the person's own phone that keeps
   the same destination and route — cross-checked against the
   guided route navigation row and the kiosk rules in
   `layouts/kiosk.md`. Sources so far are vendor guides only; a
   platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates. (Implemented this run.)

251. Add a live translated captions pattern row to
   `catalog/patterns.md`: speech in a live call or event shown
   as captions in a language the reader chooses, with the
   caption language a per-person choice, the delay stated
   plainly, the original wording available beside the
   translation where it matters, a stated fallback when
   translation is unavailable for a language, and a transcript
   kept after the session — distinct from the live captions row,
   which transcribes speech without translating it, and from
   the translated content row, which translates written text
   rather than live speech. Sources so far are vendor guides
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates. (Implemented this run.)

252. Add a drive-through and curbside pickup pattern row to
   `catalog/patterns.md`: ordering from a vehicle or collecting
   an order without entering the building — an order placed
   ahead states the pickup point and the arrival signal, the
   order is confirmed on screen before payment, the wait is
   stated with a plain update when it changes, and a wrong or
   missing item is reported from the vehicle with a stated fix
   — cross-checked against the store pickup row, the order
   tracking row, and the kiosk rules in `layouts/kiosk.md`.
   Sources so far are patents, a vendor listing, and a student
   project only, with peer-reviewed work on in-car voice
   interaction covering the interaction generally rather than the
   ordering conversation. The exception route for customers who
   cannot use the voice box is now covered directly by a city
   disability office's drive-through guidelines — a printed menu
   at the window, pen and paper on request, and staff training —
   and by a standards-body cognitive-accessibility pattern on
   avoiding voice menus, already recorded, which covers reaching
   a person without navigating a menu; Re-checked this run: platform guidance now covers simplified
   in-car ordering and a confirmation step before payment, but
   the pickup point and arrival signal, a stated wait with
   updates, and reporting a wrong or missing item from the vehicle
   still have no platform or standards source, so the row stays
   open. Done when the row passes all
   quality gates.

253. Add an e-reader and reading app pattern row to
   `catalog/patterns.md`: long-form reading on a phone or a
   dedicated reader — type size, line spacing, and margins the
   reader controls and that survive between sessions, a reading
   position kept across devices, chapter navigation with a
   stated place, a plain route to look up a word without losing
   the page, and a low-glare reading mode for long sessions —
   distinct from the reading progress indicator row, which
   shows progress rather than the reading surface, and from the
   long-document navigation row, which outlines sections rather
   than setting type. Sources so far are a single-topic
   magazine piece, a designer case study, and app listings
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates. (Implemented this run: an independent accessibility
   organisation overview of reading-app settings and a
   cross-device reader guide now recorded as sources.)

254. Add a hotel room controls pattern row to
   `catalog/patterns.md`: controls for a guest's own room during
   a stay — temperature, lighting, curtains, do-not-disturb,
   and checkout time — on the room screen or the guest's phone,
   with the current state shown before any control, a plain
   route to ask for help or housekeeping, and controls that stop
   working when the stay ends — distinct from the smart home
   dashboard row, which controls a home the person owns rather
   than a room lent for a stay, and from the hotel booking row,
   which chooses the stay rather than running the room. Sources
   so far are single-vendor product pages and case studies
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates. (Implemented this run.)

255. Add a school parent portal pattern row to
   `catalog/patterns.md`: one place for a parent or guardian to
   follow a child's school life — attendance, grades, messages
   from teachers, permission slips, and payments — with each
   child kept separate where several children attend, a plain
   route to answer a permission request, and a record of what
   was shared and when — distinct from the guardian approval
   request row, which answers one approval rather than holding
   the whole relationship, and from the tenant portal row,
   which gathers one tenancy rather than a school record.
   Sources so far are single-vendor product pages, agency
   pages, and an app listing only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates. (Implemented this run.)

256. Add a flight disruption compensation claim pattern row to
   `catalog/patterns.md`: claiming money back after a cancelled
   or badly delayed flight — an evidence file the person can
   add to, a stated split between compensation, expenses, and
   refund, eligibility bands shown before the claim is sent,
   and claim states from sent to paid — distinct from the
   travel disruption rebooking row, which finds a new flight
   rather than claiming money, and from the warranty claim row,
   which claims on a product rather than a journey. Sources so
   far are commercial claim services, a single-vendor support
   page, and a vendor product page only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented
   this run: a national enforcement body complaint form under
   Regulation (EC) 261/2004 and a step-by-step claim guide now
   recorded as sources.) (Implemented this run.)

257. Add a university course registration pattern row to
   `catalog/patterns.md`: plan a timetable first, then register —
   a course bin or shortlist held apart from registered courses,
   conflict detection against the timetable and against other
   chosen courses, seat availability shown beside each course,
   registration windows and holds stated before registration
   opens, and a seat-hold countdown once a place is claimed —
   distinct from the appointment management row, which books a
   time with a service, and from the shared resource booking
   row, which books a shared place rather than a place on a
   course. Sources so far are single-institution help pages and
   manuals only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run.)

258. Add a veterinary appointment booking pattern row to
   `catalog/patterns.md`: book a vet visit for a named animal —
   search by animal type, a pet profile carried into the booking,
   service, vet, and time chosen in that order, and a video
   option for minor concerns — distinct from the appointment
   management row, which books a person's own appointment, and
   from the telehealth video consultation row, which covers a
   video visit for a person rather than an animal. Sources so
   far are a single-designer portfolio, a single-topic content
   site, and a student case study only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates. (Implemented this run.)

259. Add a laundry pickup and delivery pattern row to
   `catalog/patterns.md`: send laundry out and get it back —
   a bag or load list with item counts, a pickup window, a
   cleaning and return estimate, a per-item state from received
   to returned, and a plain route for a missing or damaged item
   — distinct from the shared resource booking row, which books
   a shared machine rather than a pickup service, and from the
   parcel locker pickup row, which collects a parcel rather than
   returning cleaned laundry. Sources so far are a state regulator
   guide and a public advice-body page covering only the
   missing-or-damaged route — a lost or damaged garment counts
   as a major problem with compensation based on age and
   condition — with the flow itself resting on app listings, a
   single-author project blog, and a single-vendor supplier blog
   only; Re-checked this run: no platform or standards source found for
   the bag and load list, pickup window, cleaning and return
   estimate, or per-item state; the nearest support is a generic
   order-tracking pattern for wallet passes, which is not
   laundry-specific, so the row stays open. Done when the row passes all quality
   gates.

260. Add a rental property viewing and tenancy application
   pattern row to `catalog/patterns.md`: find a home to rent and
   apply for it — an intent-first search with predictable filters,
   scannable listing cards, and a step-based application flow with
   a stated decision time — distinct from the tenant portal row,
   which covers life after the tenancy starts. Sources so far are
   a single-author post, agency case studies, and a student study
   of one platform only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. (Implemented this run.)

261. Add an insurance claim submission pattern row to
   `catalog/patterns.md`: send a claim after a loss — a plain
   statement of what happened, the evidence the claim needs, and
   a stated decision time, with the claim's state visible
   throughout — distinct from the warranty claim row, which covers
   a faulty product, and from the expense claim submission row,
   which covers a receipted cost. Sources so far are
   auto-generated docs of a single project, an agency guide,
   vendor case studies, and single-product sites only; a platform
   or standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented this run.)

262. Add a tax filing and self-assessment pattern row to
   `catalog/patterns.md`: file a tax return — one section at a
   time with the figures the return needs, a running estimate of
   what is owed or due back, and a review step before sending —
   distinct from the expense claim submission row, which covers a
   receipted cost, and from the document scanner row, which
   captures a paper record. Sources so far are app listings and
   single-vendor blogs only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates. (Implemented this run.)

263. Add a passport renewal pattern row to
   `catalog/patterns.md`: renew a travel document online — an
   eligibility check first, a stepped flow with save-and-resume, a
   photo upload with stated requirements and rejection reasons, a
   review step, a fee total, and status tracking — distinct from
   the travel document checklist row, which lists documents for a
   trip, and from the identity verification onboarding row, which
   proves identity for a new account. State before submission that
   the current document becomes invalid the moment the renewal is
   submitted. Sources are government design-system guidance for the stepped
   flow with saved answers and a check-answers page, passport-office
   operational guidance for the photo upload, fee, and tracking
   stages, and a national passport authority renewal page for the
   fee total, the invalid-on-submission rule, and status updates,
   all recorded as new source records. Done when the row
   passes all quality gates. (Implemented this run.)

264. Add a visa application pattern row to `catalog/patterns.md`:
   apply for permission to enter a country — travel purpose and
   dates first, a document checklist with what each document must
   show, a biometrics appointment where one applies, a stated
   decision wait, and a refusal that states the reason and the
   route to challenge it — distinct from the Government document
   application row, which covers the shared flow for any official
   document, and from the identity verification onboarding row, which
   proves identity for a new account. The shared document-application flow is now covered by the
   Government document application row in `catalog/patterns.md` —
   eligibility, fee and timescale stated first, a stepped form with
   save and return, document upload with capture guidance, a review
   before submission, and tracking by named stages. Government guidance now covers the visa-specific elements:
   travel purpose and dates, a biometrics appointment, a stated
   decision wait, and a refusal that states the reason and the route
   to challenge it. Four new source records. Done when the row
   passes all quality gates. (Implemented this run.)

265. Add a childcare booking pattern row to `catalog/patterns.md`:
   book a nursery or childcare place for a child — the child's age
   and the days needed first, availability by day, a visit before
   committing, and deposit and notice terms stated before booking
   — distinct from the appointment management row, which books a
   person's own appointment, and from the school parent portal
   row, which covers a child already enrolled. Sources so far are
   national statutory guidance for early education and childcare,
   which requires clear admissions information, only refundable
   deposits for funded places, and published days and sessions on
   offer — covering the deposit element and part of the
   availability element — with the remaining elements resting on
   single-provider terms pages only; Re-checked this run: government guidance now covers the visit
   before committing — visit at least two or three settings while
   children are being looked after, with a second visit where there
   are misgivings — and the child's age as a first factor to
   consider; asking the child's age and the days needed first, and
   availability shown by day, still have no platform or standards
   source, so the row stays open. Two new source records for the
   visit guidance. Done when the row passes all quality gates.

266. Add a public library borrowing pattern row to
   `catalog/patterns.md`: borrow, hold, and renew items from one
   account — loans listed with due dates, holds shown with queue
   place and pickup window, renewals offered before the due date
   with a stated limit, a digital card shown on the phone where
   the library offers one, and any fee stated plainly before it
   blocks a new loan — distinct from the saved-item collection
   row, which keeps items the person chose, and from the order
   tracking row, which follows a delivery rather than a loan.
   Sources so far are the international library federation's
   public-library guidelines, which set high-level service
   standards without specifying loan periods, hold queues, renewal
   limits, digital cards, or fee-blocking, with the rule set
   itself resting on single-designer case studies and an app
   listing only; a platform or standards source for the combined
   flow is still needed before the row is written. Done when the row passes all
   quality gates.

267. Add a car rental and car sharing booking pattern row to
   `catalog/patterns.md`: choose pickup place, dates, and vehicle
   class, with the full cost including fees and any deposit stated
   before payment, a stated pickup window, a condition check with
   photos at pickup and return, fuel or charge level stated at
   handover, and a stated route where the vehicle is late or
   damaged — distinct from the ride booking row, which books a
   trip with a driver, and from the paired handover record row,
   which records a handover rather than booking the vehicle.
   Sources so far are vendor blogs and a template listing only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

268. Add an ATM interface pattern row to
   `catalog/patterns.md`: a public terminal for cash withdrawal
   and deposit — popular amounts first, the amount and any fee
   stated before confirming, the card returned only after all
   steps finish, a stated choice of denominations where offered,
   a receipt choice that never blocks the cash, and a screen
   readable in bright light — distinct from the self-checkout
   grocery kiosk row, which scans items rather than dispensing
   cash, and from the PIN entry row, which covers one entry step
   rather than the whole terminal flow. Sources so far are a national disability-access standard for
   cash machines, covering speech output, display readability,
   tactile controls, input privacy, and audible receipt
   information, plus regulator sources now recorded for the amount
   and fee stated before confirming — a consumer-protection rule
   requiring the fee amount to be disclosed on screen before the
   person is committed to paying it, with no fee where the person
   declines after seeing it — and for the receipt — a regulator
   rule on the contents of a receipt at an electronic terminal;
   the remaining transactional rules still rest on agency case
   studies, single-designer concepts, and a low-tier academic
   paper only; Re-checked this run: a regulator consultation paper now recorded
   covers denomination stocking in part — at least two
   denominations, one below 50 in local currency — and receipts
   provided at the request of the user; the paper is a consultation,
   so the requirements are proposed rather than final. Popular
   amounts first and the card returned only after all steps finish
   still have no platform or standards source, and the card-return
   rule as written is contradicted by single-bank evidence showing
   the card returned before the cash on some machines. One new
   source record. Done when the row
   passes all quality gates.

269. Add a parking fine payment and appeal pattern row to
   `catalog/patterns.md`: pay or challenge a parking fine from
   the notice itself — the fine amount, the reduced amount and
   its deadline where one applies, and the evidence window all
   stated at once, payment by the notice reference without an
   account, an appeal route that states what evidence helps and
   how long a decision takes, and a stated rule on whether payment counts as an admission
   where an appeal is still open — distinct from the
   parking session payment row, which pays for a timed stay, and
   from the transaction dispute row, which disputes a charge
   already paid. Sources so far are national government guidance on challenging
   a penalty charge and a sector-wide code of practice (found only
   as a third-party-hosted mirror copy), together covering the
   challenge window, the reduced amount and its deadline, the
   evidence to supply, and the appeal route and response times;
   two elements remain uncovered — payment by the notice reference
   without an account, and whether payment counts as an admission
   while an appeal is open, where a single operator page states
   that payment closes the matter, so that draft rule needs
   correcting before the row is written. Government guidance now covers both elements: payment by the
   notice reference and vehicle registration without an account, and
   payment counting as an admission that closes any open challenge.
   Three new source records. Done when the row passes all quality
   gates. (Implemented this run.)

270. Add a mortgage application pattern row to
   `catalog/patterns.md`: apply for a home loan online — an
   affordability estimate before the detail, a stepped application
   with save-and-resume, a document checklist with what each
   document must show, a stated decision time, and status tracking
   — distinct from the rental property viewing and tenancy
   application row, which applies for a tenancy rather than a loan,
   and from the wizard row, which covers a stepped flow without
   the financial decision. Sources are a financial-regulator rulebook instrument for the
   affordability assessment, a financial-regulator consumer
   protection code for the acknowledgement and decision times and
   refusal reasons, and government-backed money guidance for the
   affordability stress test and the document checklist, all
   recorded as new source records. Done when the row passes all
   quality gates. (Implemented this run.)

271. Add a home energy usage dashboard pattern row to
   `catalog/patterns.md`: show how much energy a home uses and
   what it costs — usage over time with cost beside it, a
   breakdown by appliance or circuit where the meter supports it,
   a comparison against a previous period, and an alert when usage
   or cost passes a stated threshold — distinct from the smart
   home dashboard row, which controls devices rather than
   explaining usage, and from the billing overview row, which
   explains one bill rather than use over time. Sources so far are an energy-regulator programme document, now
   recorded, covering use over time, cost shown beside use in
   money as well as in units, comparison against a previous
   period, and a visual marker for high and low use — though it is
   a 2010 consultation-proposals document, so it must be verified
   against the current metering specification before a row is
   published — with the remaining elements resting on a
   single-author content site, community-forum posts for one
   single-product app, a single-designer portfolio, and a
   single-author personal blog only; Re-checked this run: the 2010 programme document is verified as
   consultation proposals, and the current licence conditions
   confirm the duty to provide an in-home display without restating
   the display-content rules, so the content items still rest on the
   2010 document; a breakdown by appliance or circuit and an alert
   when use or cost passes a stated threshold still have no platform
   or standards source, so the row stays open. Done when the row passes all
   quality gates.

272. Add a smartwatch fall detection and emergency SOS pattern row
   to `catalog/patterns.md`: detect a hard fall and offer help —
   an automatic trigger on impact plus immobility, a stated
   cancel window of about a minute before an automatic call to
   emergency services and a location message to contacts, a large
   cancel control, and a press-and-hold manual SOS — distinct
   from the emergency assistance request row, which sends a
   request the person starts, and from the safety check-in row,
   which confirms the person is well rather than detecting a
   fall. Sources are platform support documentation from two platforms,
   agreeing on the shape — impact plus immobility, a stated cancel
   window, a large cancel control, and press-and-hold manual SOS —
   recorded as new source records. Done when the row passes all
   quality gates. (Implemented this run.)

273. Add a phone voice menu pattern row to `catalog/patterns.md`:
   reach a person without navigating a menu — a reserved digit or
   word that skips the menu at any time, plain words throughout,
   waiting for slow speakers, and a directed-dialog fallback or
   transfer to a person where the menu cannot serve the task —
   distinct from the voice hybrid flows in
   `trends/2026/conversational-interfaces.md`, which mix voice and
   screen, and from the in-product help row, which covers help
   inside a screen. Sources are a standards-body cognitive-accessibility pattern on
   avoiding voice menus, already recorded, with two further patterns
   from the same body now recorded for waiting for slow speakers and
   for human help that never requires navigating a menu. Done when
   the row passes all quality gates. (Implemented this run.)

274. Add a worked example for the authentication layout under
   `examples/`: a worked example demonstrating the sign-in,
   second-factor, passkey, and account-recovery rules with all seven
   states, cross-checked against `layouts/auth.md` and the sign-in
   rows in `catalog/patterns.md`. Done when the example passes all
   quality gates. (Implemented this run.)

275. Add a worked example for the settings layout under `examples/`:
   a worked example demonstrating grouped preferences, scope labels,
   save behaviour, settings search, and the danger zone with all
   seven states, cross-checked against `layouts/settings.md`. Done
   when the example passes all quality gates. (Implemented this run.)

276. Add a mobile cheque deposit pattern row to
   `catalog/patterns.md`: deposit a paper cheque with the phone
   camera — a restrictive endorsement written on the cheque before
   capture, a dark flat background with all four corners and the
   printed line legible, the entered amount matched against the
   amount read from the cheque, and a stated cutoff time with the
   paper cheque kept after deposit — distinct from the document
   scanner row, which captures a paper record without acting on
   its amount, and from the code scanner row, which reads a printed
   code rather than a payment instrument. Sources so far are a
   fintech vendor blog, single-institution help pages, and a
   content-site guide only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

277. Add a dating app profile and matching pattern row to
   `catalog/patterns.md`: decide on a person from one card — one
   photo, name, age, and one personality signal, like and pass
   controls in thumb reach, a brief match celebration with one
   next step, safety actions within one or two taps, and no-match
   empty states that offer a next step — distinct from the contact
   picker row, which chooses a known contact, and from the safety
   check-in row, which confirms a person is well rather than
   keeping a stranger at a distance. Sources so far are a UI-kit
   vendor blog, a development-agency blog, and an agency blog
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates.

278. Add a museum timed-entry ticket booking pattern row to
   `catalog/patterns.md`: book a timed entry to a venue — an entry
   time chosen from the slots the venue can keep, the entry window
   and the late-arrival rule stated before payment, the ticket
   shown with its entry time, and a rebooking route where the slot
   is missed — distinct from the pass and ticket display row, which
   shows a ticket already held, and from the appointment management
   row, which books a person's own appointment. Sources so far are
   a student design critique, vendor pages, a single-designer case
   study, and a travel content site only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates.

- Completed this review (deep editorial 2026-11-09): new
  Tenant portal, QR table ordering, and Screen time dashboard
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 226, 242, and 243; coverage matrix updated with the
  three new rows; three new improvement actions added (246
  recurring donation, 247 temporary home access code, 248 health
  record sharing); 6 new source records (683 total).

- Completed this review (daily planning 2026-11-09): five new
  improvement actions added (249 self-checkout grocery kiosk,
  250 indoor wayfinding, 251 live translated captions, 252
  drive-through and curbside pickup, 253 e-reader and reading
  app), ordered by coverage impact; coverage matrix Gap column
  corrected — the six rows implemented since the last review
  (transit card top-up, in-flight entertainment, hotel self
  check-in, tenant portal, QR table ordering, screen time
  dashboard) were listed as gaps while also listed as full, and
  are now removed from the gap list, replaced by the five new
  named gaps. No new source records — the five searches (live
  translated captions, self-checkout grocery kiosk, indoor
  wayfinding, drive-through and curbside pickup, e-reader and
  reading app) returned only vendor guides, patents, a student
  project, a designer case study, and app listings below the
  source-quality bar, so the five genuine gaps are recorded as
  actions instead of rows. Since the last daily run, the deep
  cycle completed actions 226, 242, and 243 and the light cycles
  added the parcel locker pickup, digital car key sharing, mobile
  plan setup (eSIM), voice dictation input, and screenless sensor
  interface rows; those outcomes are already recorded in
  `CHANGELOG.md`. The five new pattern rows are left to the deep
  cycle, pending a platform or standards source for each.

- Completed this review (deep editorial 2026-11-09): new
  Health record sharing and E-reader and reading app pattern
  rows in `catalog/patterns.md`, completing roadmap actions
  248 and 253; a desktop worked example under
  `examples/desktop/`, completing action 245; coverage matrix
  updated with the two new rows and the desktop example, and
  the gap list corrected — e-reader and reading app moved from
  gap to full, replaced by three new named gaps; three new
  improvement actions added (254 hotel room controls, 255
  school parent portal, 256 flight disruption compensation
  claim); 5 new source records (688 total). Re-checked the
  remaining open gaps against deeper sources: recurring
  donation (246) still rests on single-vendor help pages;
  temporary home access code (247) on vendor blogs;
  self-checkout grocery kiosk (249) on vendor guides with only
  a general accessibility-organisation page on self-service
  terminals; indoor wayfinding (250) on vendor product pages
  and a student project; live translated captions (251) on
  vendor blogs and help pages; drive-through and curbside
  pickup (252) on a vendor blog, a patent, and vendor guides —
  all still below the source-quality bar, so those actions stay
  open. Action 244 (standardised accessibility labels) also
  stays open, pending a published label schema.

- Completed this review (light cycle 2026-11-09): new Flight
  disruption compensation claim pattern row in
  `catalog/patterns.md`, completing roadmap action 256; coverage
  matrix updated with the claim moved from gap to full; 2 new
  source records (693 total). School parent portal (action 255)
  re-checked: sources remain agency pages, a single-designer
  portfolio, and vendor pages, with no platform or standards
  source, so the action stays open. Veterinary appointment
  booking has no coverage but rests only on agency and vendor
  guides, so it stays a future-cycle candidate.

- Completed this review (deep editorial 2026-11-09): new
  Self-checkout grocery kiosk, School parent portal, and Live
  translated captions pattern rows in `catalog/patterns.md`,
  completing roadmap actions 249, 251, and 255; coverage matrix
  updated with the three rows moved from gap to full; three new
  improvement actions added (257 university course registration,
  258 veterinary appointment booking, 259 laundry pickup and
  delivery); 3 new source records (697 total). Re-checked the
  remaining open gaps against this run's searches: recurring
  donation (246) still rests on single-vendor help pages;
  temporary home access code (247) on vendor blogs; indoor
  wayfinding (250) on vendor product pages and a student project;
  drive-through and curbside pickup (252) on a vendor blog, a
  patent, and vendor guides; hotel room controls (254) on
  single-vendor product pages — all still below the
  source-quality bar, so those actions stay open. Action 244
  (standardised accessibility labels) also stays open, pending a
  published label schema.

- Completed this review (deep editorial 2026-11-09): reconciled
  the improvement-actions list with the catalogue, completing
  roadmap action 239 — 76 actions marked implemented, 66 of them
  implemented in earlier runs without any marker (rows already in
  `catalog/patterns.md`, the desktop example already under
  `examples/desktop/`); actions 120, 242, 243, 245, 248, and 253
  already carried a variant marker and were left as written. The
  two naming-only mismatches are action 85 (row named Poll) and
  action 181 (row named Back to top). Completed the partly-
  implemented actions: 20 (form validation timing:
  single-invalid-field focus and input retention after a failed
  submission), 21 (contextual guidance rules in the Onboarding row
  and `layouts/onboarding.md`), 22 (empty-state fallback rule in
  `catalog/states.md`), and 57 (no-results recovery rule in the
  Search row). New pattern rows for actions 246 (recurring
  donation), 250 (indoor wayfinding), 254 (hotel room controls),
  and 257 (university course registration); coverage matrix
  updated (four rows to full; indoor wayfinding, hotel room
  controls, and university course registration out of the partial
  list). Three new improvement actions added (260 rental property
  viewing and tenancy application, 261 insurance claim
  submission, 262 tax filing and self-assessment). 8 new source
  records (707 total). Re-checked against deeper sources:
  temporary home access code (247) now rests on standards-body
  and regulator guidance for the security framing, with the
  code-creation flow itself still unsourced; drive-through and
  curbside pickup (252) now rests on regulator guidance for the
  pickup area and an eye-tracking study for menu boards, with the
  in-vehicle ordering conversation still unsourced — both are
  ready for a row in a later cycle. Crowdfunding reward tiers
  (237) and the standardised accessibility-label format (244)
  still have no qualifying source. Open actions after this review:
  154, 237, 244, 247, 252, 258, 259, 260, 261, 262.

- Completed this review (deep editorial 2026-11-10): new
  Veterinary appointment booking, Rental property viewing and
  tenancy application, Insurance claim submission, and Tax filing
  and self-assessment pattern rows in `catalog/patterns.md`,
  completing roadmap actions 258, 260, 261, and 262; Crowdfunding
  campaign page row extended with reward-tier and backer-update
  rules and Accessibility labels on a store listing row extended
  with a fixed label set, completing actions 237 and 244;
  checkout worked example added under `examples/`, completing
  action 154; coverage matrix updated; three new improvement
  actions added (263 passport renewal, 264 visa application, 265
  childcare booking); 8 new source records (717 total). The
  Accessibility Nutrition Labels source was already recorded
  (2026-11-07), so the labels extension adds no new record.
  Re-checked against deeper sources: temporary home access code
  (247) still rests on vendor blogs for the code-creation flow,
  with regulator and standards-body guidance covering only the
  security framing; laundry pickup and delivery (259) still rests
  on single-vendor terms pages only; drive-through and curbside
  pickup (252) still rests on regulator guidance for the pickup
  area and an eye-tracking study for menu boards, with the
  in-vehicle ordering conversation still unsourced. Open actions
  after this review: 247, 252, 259, 263, 264, 265.

- Completed this review (daily planning 2026-11-10): four new
  improvement actions added (266 public library borrowing, holds
  and renewals, 267 car rental and car sharing booking, 268 ATM
  interface, 269 parking fine payment and appeal), ordered by
  coverage impact; coverage matrix Partial list updated with the
  four new named items. No new source records — the five searches
  (temporary home access code, drive-through and curbside pickup,
  laundry pickup and delivery, public library borrowing, home
  insurance claim submission) returned only vendor blogs,
  single-designer case studies, patents, a low-tier journal paper,
  and app listings below the source-quality bar, so the four
  genuine gaps are recorded as actions instead of rows. Re-checked
  against this run's searches: temporary home access code (247)
  still rests on vendor blogs and single-author guides with no
  platform or standards source; drive-through and curbside pickup
  (252) still rests on a vendor blog and patents with the
  in-vehicle ordering conversation still unsourced; laundry pickup
  and delivery (259) still rests on a low-tier journal paper,
  single-designer portfolios, and a student project; home insurance
  claim submission is now covered by the Insurance claim
  submission row (action 261), so no new action for it. Since the
  last daily run, the deep cycle completed actions 154, 237, 244,
  258, 260, 261, and 262 and the light cycles added the care
  decision card row and the pass and ticket display and document
  signing extensions; those outcomes are already recorded in
  `CHANGELOG.md`. The four new pattern rows are left to the deep
  cycle, pending a platform or standards source for each. Open
  actions after this review: 247, 252, 259, 263, 264, 265, 266,
  267, 268, 269.

- Completed this review (deep editorial 2026-11-10): new
  Temporary home access code and Car rental and car sharing
  booking pattern rows in `catalog/patterns.md`, completing
  roadmap actions 247 and 267; Passkey sign-in, Code scanner,
  and Conversation mute rows consolidated, each pair into one row
  keeping the union of their rules, with cross-references updated;
  coverage matrix updated (two rows to full, one item out of the
  partial list, three missing named gaps added to the partial
  list); three new improvement actions added (270 mortgage
  application, 271 home energy usage dashboard, 272 smartwatch
  fall detection and emergency SOS); 4 new source records (721
  total). Re-checked against deeper sources: drive-through and
  curbside pickup (252) still rests on patents, a vendor listing,
  and a student project, with a regulator settlement quoted
  second-hand covering only the exception route; laundry pickup
  and delivery (259) still rests on app listings and vendor
  material for the flow, with a state regulator guide covering
  only the missing-or-damaged route; public library borrowing
  (266) still rests on single-designer case studies and an app
  listing, with federation guidelines setting only high-level
  service standards; passport renewal (263), visa application
  (264), childcare booking (265), ATM interface (268), and
  parking fine payment and appeal (269) all stay open, with
  their source notes updated — the parking fine action's draft
  rule on payment as an admission needs correcting before the
  row is written. Open actions after this review: 252, 259, 263,
  264, 265, 266, 268, 269, 270, 271, 272.

- Completed this review (deep editorial 2026-11-10): new
  Government document application, Mortgage application, and
  Smartwatch fall detection and emergency SOS pattern rows in
  `catalog/patterns.md`, completing roadmap actions 263, 270, and
  272; four rules from the current accessibility standard added to
  `catalog/states.md` (single-pointer alternative for dragging,
  help in the same relative order, no repeated entry, sign-in
  without a memory or puzzle test); coverage matrix updated (three
  new rows to full, Cooking mode added to full, Passport renewal
  out of the partial list, Home energy usage dashboard and Phone
  voice menu added to the partial list, Authentication and Settings
  added as worked-example gaps); three new improvement actions
  added (273 phone voice menu, 274 authentication worked example,
  275 settings worked example); 16 new source records (738 total).
  Re-checked against deeper sources: drive-through and curbside
  pickup (252) gains a city disability office's guidelines for
  the exception route, with the in-vehicle ordering conversation
  still needing a platform or standards source; laundry pickup
  and delivery (259) still rests on vendor blogs and app listings
  for the flow; ATM interface (268) gains regulator sources for
  the fee-before-commitment and receipt rules, with popular
  amounts, denomination choice, card-return order, and a receipt
  choice that never blocks the cash still needing a source; home
  energy usage dashboard (271) gains an energy-regulator programme
  document for use, cost, and previous-period comparison, with
  appliance breakdown and threshold alerts still needing a source
  and the programme document needing verification against the
  current specification; visa application (264) keeps only its
  visa-specific elements open now that the shared flow is covered
  by the new document-application row. Open actions after this
  review: 252, 259, 264, 265, 266, 268, 269, 271, 273, 274, 275.

- Completed this review (deep editorial 2026-11-10): new Visa
  application, Parking fine payment and appeal, and Phone voice
  menu pattern rows in `catalog/patterns.md`, completing roadmap
  actions 264, 269, and 273; worked examples for the
  authentication and settings layouts added under `examples/`,
  completing actions 274 and 275; coverage matrix updated (three
  new rows to Full, Authentication and Settings moved from
  worked-example gaps to Full); three new improvement actions
  added (276 mobile cheque deposit, 277 dating app profile and
  matching, 278 museum timed-entry ticket booking); 12 new source
  records (753 total). Re-checked against deeper sources:
  drive-through and curbside pickup (252) gains platform guidance
  for simplified in-car ordering and a confirmation step, with the
  pickup point and arrival signal, a stated wait with updates, and
  reporting a wrong or missing item from the vehicle still needing
  a source; laundry pickup and delivery (259) still rests on
  vendor material for the flow, with only a generic order-tracking
  pattern as partial support; childcare booking (265) gains
  government guidance for the visit before committing and the
  child's age as a first factor, with asking the age and days
  needed first and availability shown by day still needing a
  source; ATM interface (268) gains a regulator consultation paper
  for denomination stocking and receipt-on-request in part, with
  popular amounts first and the card-return order still needing a
  source and the card-return rule contradicted by single-bank
  evidence; home energy usage dashboard (271) keeps the 2010
  programme document verified as consultation proposals, with the
  current licence duty confirmed but the display-content rules not
  restated there, and appliance breakdown and threshold alerts
  still needing a source; public library borrowing (266) was not
  re-checked this run. Open actions after this review: 252, 259,
  265, 266, 268, 271, 276, 277, 278.
