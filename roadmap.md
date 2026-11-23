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
| Page pattern | Dashboard, mobile navigation, data table, checkout variants, onboarding, comparison, permission request, search results, command palette, notification escalation, offline-first sync, sync-conflict resolution, file upload, chat and messaging, map comparison, list navigation, machine-composed content disclosure, agent checkpoint, voice hybrid flows, stepper, landing, authentication, settings, commerce, consent, notification digest, personalized-content disclosure, calendar and scheduling, keyboard shortcut reference, undo and trash recovery, session-expiry warning, data export, account deletion, in-product help, share link, second-factor sign-in, saved-item collection, bulk action, rating and review submission, payment failure recovery, content reporting and blocking, language and locale selection, scheduled action, breadcrumb navigation, annotation and comment thread, theme selection, profile and account menu, recently viewed, invitation response, modal dialog, guest checkout, time-zone picker, accessibility preferences, long-document navigation, in-app update prompt, pull-to-refresh, scrolling tab bar, system share sheet, find-in-page, collaborative editing presence, draft autosave and recovery, saved-filter view, toast feedback, list reorder, date-range picker, accordion disclosure, carousel, passkey sign-in, low-bandwidth mode, what's-new announcement, version history and restore, external-link departure, described media, saved-cart recovery, colour picker, guest-to-account conversion, sensitive-content preview, order tracking, order cancellation, time picker, verification-code entry, background-task progress, automated-to-human support handoff, subscription plan change, promo-code entry, master-detail, threaded message reply, gift option, saved address selection, delivery slot picker, product variant selection, home-screen widget, deep-link landing, progressive disclosure, return and exchange request, back-in-stock alert request, contact picker, primary navigation, bypass link, search, filtering and sorting, data table density, inline editing, bulk selection, data visualisation, guided tour, setup checklist, inline assistant actions, form flow, character count, wizard, detail view, notification list, notification preferences, Email list unsubscribe, activity feed, confirmation, sensitive-action re-confirmation, install prompt, offline download, multi-device handoff, paywall and upgrade prompt, subscription cancellation, restore purchases, account switcher, in-product feedback and problem report, account recovery, consent choice, granular consent, media viewer, code scanner, simplified view, location selection, voice message, message reaction, pinned message, message edit and delete, swipe-to-reveal actions, poll, conversation branching, sticky section headers, appointment management, review prompt, rating distribution summary, limited-time offer countdown, age verification gate, suggestion review, image gallery viewer, reading progress indicator, print-friendly view, text-selection action menu, picture-in-picture, reorder past order, live broadcast chat overlay, kanban board, gift card and stored-credit redemption, address entry, delivery instructions, saved payment method selection, split payment, media chapters, waitlist, loyalty rewards, link preview, live activity, billing overview, usage allowance, password strength meter, emoji picker, seat selection, selecting an option from a list, home control map, follow, payment instalment plan, subscribe-and-save purchase option, pickup point selection, expandable table row, pass and ticket display, shared cart, stored payment method expiry warning, workspace switcher, undo send, view switcher, tree view, timeline view, quote reply, product configurator, referral invitation, live captions, route planning, pass or ticket transfer, document signing, transcript editing, meeting and event creation, shared resource booking, backup payment method, household member management, checkout price-change confirmation, split shipment display, price-drop alert, guest order lookup, signed-in device management, service status notice, order substitution choice, commercial content disclosure, Trial-end reminder, Subscription pause, Data import, In-app survey, Document scanner, Delivery address validation, Shared expense splitting, In-store availability check, Guided route navigation, Saved search alert, Magic link sign-in, Preorder purchase, Tip selection, Live call controls, Device pairing, Hands-busy step guidance, Guardian approval request, Live poll, Delivery photo proof, Warranty claim, Overflow menu, Translated content, scheduled message send, saved reply, order receipt, subscription billing-date change, card freeze, travel disruption rebooking, size guide and fit recommendation, shared item access, app lock, transaction dispute, habit streak, contactless payment confirmation, profile photo upload and crop, playback queue, security incident notice, file preview, search history, download manager, voice message transcript, product recall notice, account merge, loyalty points expiry warning, QR sign-in, high-demand queue, group checkout, gift receipt, store pickup, reduced-motion preference, archive conversation, in-conversation message search, expiring payment method replacement, dual approval, stored payment method label, conversation export, appointment reminder, shoppable video, appointment check-in, travel check-in, stored payment method removal, aggregate rating display, recurring appointment series, travel document checklist, travel itinerary view, bill explanation, appointment late-cancellation and no-show policy, emergency assistance request, shared trip itinerary, ride booking, bottom sheet choice, trigger-character suggestion menu, booking deposit, appointment standby list, medication reminder, verified account badge, virtual background in video calls, world clock, expense claim submission, read receipt, typing indicator, video-call waiting room, focus mode schedule, sticker and GIF picker, product questions and answers, shared whiteboard, raise hand in video calls, screen sharing in video calls, disappearing messages, call recording notice, incoming call, missed call, scan-to-pay, launch screen, call waiting, outgoing call, agent-placed call, call quality and reconnection, in-app browser, visual voicemail, safety check-in, breakout rooms in video calls, call transfer, conference call, suspected spam call warning, digital identity wallet presentation, call screening, reading view, add people to a live call, call history, transaction history, deceptive design patterns, accessibility labels on a store listing, PIN entry, cookie consent banner, parking session payment, screenshot markup, group chat administration, call forwarding, voicemail greeting, hotel booking, electric vehicle charging session, smart home dashboard, sleep and rest data, telehealth video consultation, museum audio guide, QR code payment at a till, crowdfunding campaign page, shared bike and scooter rental, digital car key sharing, parcel locker pickup, mobile plan setup (eSIM), voice dictation input, guest mode, live auction bidding, Back to top, Saved collection sharing, Identity verification onboarding, Broadcast emergency alert, Lightweight app entry, Receipt capture, Gated feature entry, Subscription gifting, Neuro-inclusive design, Live location sharing, Read-along narration, Group scheduling poll, Page not found, Order editing after placement, Human verification challenge, Gift card purchase, Message forwarding, Conversation catch-up summary, Conversation mute, Pinned conversation, Group conversation participant management, Sleep timer, System-mediated snippet, Return label and drop-off, Recording consent, Turn-by-turn guidance, Shared shopping list, Shared subscription plan, Donation at checkout, Checkout upsell and cross-sell offer, Shared presentation control, Paired handover record, Message translation, Converted price display, Fare-capped transit payment, Automation routine builder, Price history display, Delivery reschedule, Loyalty tier progress, Recipe serving scaling, Supervised usage limits, Appointment preparation checklist, Deposit refund status, Medication refill request, Recurring payment setup, Transit card top-up, In-flight entertainment, Hotel self check-in, Tenant portal, QR table ordering, Screen time dashboard, Health record sharing, E-reader and reading app, Ballot, Flight disruption compensation claim, Flight search and booking, Keyless shared-car pickup, Self-checkout grocery kiosk, School parent portal, Live translated captions, Real-time departure board, Care decision card, Recurring donation, Indoor wayfinding, Hotel room controls, University course registration, Veterinary appointment booking, Rental property viewing and tenancy application, Insurance claim submission, Tax filing and self-assessment, Temporary home access code, Car rental and car sharing booking, Cooking mode, Government document application, Mortgage application, Smartwatch fall detection and emergency SOS, Virtual try-on, Pension dashboard, Visa application, Parking fine payment and appeal, Phone voice menu, Mobile cheque deposit, Home energy usage dashboard, Benefits claim application, Blood donation appointment booking, Virtual court hearing, Remote online notarization, Proctored exam, Restaurant online ordering, Virtual museum tour, Job application portal, Waste collection schedule and missed bin reporting, Smart TV programme guide, Vaccination appointment booking and digital certificate, Contact a GP surgery online, Live-viewing app, Passport renewal, Meal planning, Online course lesson player and progress, Online voter registration and mail-in ballot tracking, Jury duty summons response, Smartwatch workout tracking, Personal budgeting dashboard, Board game app interface, Language learning lesson, Digital wallet add-card and tap-to-pay setup, Music streaming playlist and queue, Banking fraud alert, Digital health record patient portal, Podcast app playback interface, Audiobook library app, Student accommodation booking, Train ticket booking, Public transport ticket purchase, Mental health journaling and mood tracking, Period and fertility tracking, Airport lounge access, Smart thermostat heating schedule, Shared family calendar, Peer-to-peer marketplace selling, Self-service food ordering kiosk, Personalised news feed, Kids' launcher / curated home screen, Real estate property search, Smart lock guest access, Carpool coordination, Phone-side fitness workout logging, Digital loyalty card wallet pass, Online therapy booking, Museum timed-entry ticket booking, Age assurance flow, Appliance remote control, Civic issue reporting, Freelancer invoicing, Stock trading and investing, Food delivery courier/driver app, Grocery price comparison, Public transport season ticket purchase, Peer-to-peer payment, Smart-display voice screen, Hotel room service ordering, Concert and festival ticket booking, Appliance and device repair booking, ATM interface, Mobile banking app, Energy tariff comparison and switching, Digital parking permit application, Parcel sending and courier booking, Video streaming player interface, School admissions application portal, Childcare booking, Gym and fitness class booking, Public library borrowing, Laundry pickup and delivery, Dating app profile and matching, Hot-desk and co-working booking, Drive-through and curbside pickup, Government citizen services portal, Weather app interface, Smart home security camera, Theme park virtual queue reservation, Road toll and congestion charge payment, Agent-described interface, Cinema ticket booking, Driving licence renewal, Ferry booking, Student loan application, Travel insurance purchase, Food rescue and surplus food pickup, Multiplayer game lobby and matchmaking, Agent run controls, Recommendation feedback (two-intent dismissal), Note-taking app, Job search discovery | — | University admissions application, Wedding registry and gift list, Driving test booking, Home broadband installation and router setup, Online will creation, Timed cart-hold, Home cleaning service booking, University student portal dashboard, Airport self-service bag drop, Online prize draw and raffle entry, Streaming household viewer profiles, Pet adoption application, Lost property reporting, Video doorbell visitor interface, Community sports league team registration, Vehicle registration renewal and car tax payment, Wedding planning app, Pet grooming appointment booking, School lunch ordering, Home solar energy monitoring, Council tax payment and discount application, Meal kit delivery subscription, Volunteer shift signup, Neighbourhood noticeboard, Digital business card sharing, Home EV charger scheduling, Smart fridge and food inventory, Smart baby monitor, Smart garden and plant care, Salon and spa appointment booking, Meditation and mindfulness app, Smartwatch sensitive-notification reveal, Conversational companion safeguards for minors, Spending controls for minors, Car wash booking and membership, Fantasy sports app, House moving and removals booking, Baby feeding and sleep tracking, Children's pocket money and allowance, Tradesperson and plumber booking, Restaurant table reservation, Wedding invitation RSVP, Water utility bill payment, Pregnancy tracking, Restaurant waitlist management, School homework assignment tracking, Cruise booking, Service-provider booking intake, Multi-role availability, Book on behalf, Volunteer shift cover and substitute request, Cruise embarkation and onboard check-in, Sensitive lifecycle change in a health tracker, Guardian falling-behind alert, Bounded neighbourhood noticeboard, Recipient-side agent action, Free-agent pool placement, Multi-pet appointment booking, Connected-device prompt, Cloud device recovery, Energy supplier account, Car insurance quote and purchase, Home care coordinator rostering |
| State | All seven in catalog; offline, read-only, permission-denied; loading variants; error-state groups | — | — |
| Worked examples | Dashboard, mobile navigation, onboarding, watch, kiosk, television, desktop, checkout, authentication, settings, tablet, landing, automotive — each demonstrating the rules it documents with all seven states | — | — |
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

- Completed this review (deep editorial 2026-11-18): three new
  pattern rows in `catalog/patterns.md` — Childcare booking, Gym and
  fitness class booking, and Public library borrowing — completing
  roadmap actions 397, 398, and 399; the platform source for 397 is
  the statutory guidance on funded early education and childcare, for
  398 the published booking policies of council leisure services, and
  for 399 the published circulation policies of public library
  systems. Coverage matrix updated with the three new rows (482
  pattern rows, Full 492, Gap 57). Three new improvement actions added
  (400 dating app profile and matching, 401 hot-desk and co-working
  booking, 402 home cleaning service booking), ordered by coverage
  impact, each a genuine gap with its source position stated. 9 new
  source records (1023 total). Re-checked: laundry pickup and delivery
  (395) stays open — fresh sources are design-gallery concepts, vendor
  case studies, and an academic prototyping paper only, with no
  platform or standards source; drive-through and curbside pickup
  (252) stays open, last re-checked 2026-11-18 with no new evidence
  in this run's searches. The held findings stay held; no new evidence
  surfaced in this run's searches. Open actions after this review: 252,
  259, 265, 266, 268, 277, 279, 280, 285, 286, 287, 288, 291, 292, 294,
  296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
  312, 313, 314, 315, 316, 318, 319, 327, 328, 329, 330, 331, 332, 333,
  334, 335, 336, 341, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356,
  357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370,
  372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387,
  388, 389, 390, 391, 392, 393, 395, 400, 401, 402.

- Completed this review (deep editorial 2026-11-18): four new
  pattern rows in `catalog/patterns.md` — Digital parking permit
  application, Parcel sending and courier booking, Video streaming
  player interface, and School admissions application portal — the
  first two completing roadmap actions 396 and 394, the last two
  closing gaps with no action number; the platform source for 396
  is the local-government service-pattern work and for 394 the
  carrier's official shipping API platform, with council, vendor,
  and platform sources behind the other two rows. Coverage matrix
  updated with the four new rows (479 pattern rows, Full 489, Gap
  60). Three new improvement actions added (397 childcare booking,
  398 gym and fitness class booking, 399 public library borrowing),
  ordered by coverage impact, each a genuine gap with its source
  position stated. 11 new source records (1011 total). Re-checked:
  laundry pickup and delivery (395) stays open — fresh sources are
  vendor pages and a vendor blog only, with no platform or standards
  source; drive-through and curbside pickup (252) stays open — a
  state disability-access document and a quick-service
  accessibility checklist add the accessible alternative route, but
  the stated wait with updates and reporting a wrong or missing item
  from the vehicle still lack a platform or standards source. The
  held findings stay held; no new evidence surfaced in this run's
  searches. Open actions after this review: 252, 259, 265, 266, 268,
  277, 279, 280, 285, 286, 287, 288, 291, 292, 294, 296, 297, 299,
  301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,
  314, 315, 316, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334,
  335, 336, 341, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356,
  357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369,
  370, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385,
  386, 387, 388, 389, 390, 391, 392, 393, 395, 397, 398, 399.

- Completed this review (daily planning 2026-11-18): three new
  improvement actions added (394 parcel sending and courier
  booking, 395 laundry pickup and delivery, 396 digital parking
  permit application), ordered by coverage impact, each a genuine
  gap with its source position stated; no new pattern rows this
  review, as each of the three still needs a platform or standards
  source before the row is written — the top improvement is
  therefore left to the deep cycle. Re-checked: drive-through and
  curbside pickup (252) stays open — fresh sources are
  single-vendor app pages and a student project only, with a
  stated wait with updates and reporting a wrong or missing item
  from the vehicle still lacking a platform or standards source;
  new interface types and UI updates for November 2026 already
  assessed in earlier cycles (NHS manual updates, Spaces Flex
  R52, RebelMouse redesign, Omni DAW modular workspace,
  ArtisanPack UI roundup, Duve product updates) with no new rule.
  This run also publishes the working tree left unpublished since
  the 2026-11-18T00:11:00Z sync, including the mobile banking and
  energy tariff rows and the standards outlook corrections.
  Coverage matrix unchanged by this review (475 pattern rows, Full
  485, Gap 64). No new source records. Open actions after this
  review: 252, 259, 265, 266, 268, 277, 279, 280, 285, 286, 287,
  288, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306,
  307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 318, 319, 327,
  328, 329, 330, 331, 332, 333, 334, 335, 336, 341, 343, 344, 346,
  347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362,
  363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377,
  378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391,
  392, 393, 394, 395, 396.

- Completed this review (deep editorial 2026-11-18): two new
  pattern rows in `catalog/patterns.md` — Mobile banking app and
  Energy tariff comparison and switching — the second completing
  roadmap action 342, the first closing the genuine gap noted in
  review with no action number; coverage matrix repaired and
  updated (gap list moved from the Partial column to the Gap
  column, State row restored as its own row, two rows to Full,
  one newly named gap; 475 pattern rows, Full 485, Gap 64).
  Standards outlook corrected: EN 303 919 published 17 November
  2026 and announced together with the fourth edition (published
  2 September 2026), and the Official Journal citation date now
  recorded as disputed between trackers (mid-December 2026
  against late January 2027) — resolving the held EN 301 549
  citation-date item; this run also publishes the EN 303 919 note
  and source record added since the last sync. Three new
  improvement actions added (391 school homework assignment
  tracking, 392 worked mobile banking example, 393
  total-conversation rules for the Emergency assistance request
  row). 5 new source records (1000 total). Re-checked:
  smartwatch sensitive-notification reveal (388) still rests on
  vendor help pages and content sites with no platform or
  standards source surfacing, so it stays open; the held
  expressive-design-language, agent-operable library, browser
  modern-web guidance, and accessible design system findings stay
  held with no new rule. Open actions after this review: 252, 259, 265, 266, 268, 277, 279, 280, 285, 286, 287, 288, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 341, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393.

- Completed this review (deep editorial 2026-11-17): two new
  pattern rows in `catalog/patterns.md` — Public transport season
  ticket purchase and Peer-to-peer payment — completing roadmap
  action 289; coverage matrix updated with the two new rows (468
  pattern rows, all in Full; Full 478; Partial 65). Three new
  improvement actions added (379 ferry booking, 380 theme park
  virtual queue reservation, 381 video doorbell visitor
  interface), ordered by coverage impact, each a genuine gap with
  its source position stated. 8 new source records (973 total).
  Re-checked: driving test booking (287) gains a transport
  department consultation outcome on learner-only booking and
  change limits; airport self-service bag drop (301) still rests
  on single-operator guides with standards material covering only
  the shared infrastructure; ATM interface (268) re-surfaces the
  same accessibility standards already recorded, so all three stay
  open. The publish approval from the 2026-11-17T05:37Z deep cycle
  timed out with no decision, so this run retried the publish of
  the working tree, including the electric vehicle charging
  advance-reservation extension and the two new rows; the new
  approval is pending (see the operations log). Open actions after
  this review: 252, 259, 265, 266, 268, 277, 279, 280, 285, 286, 287, 288, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381.

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
   open. Re-checked this run: platform guidance now covers the
   pickup point and the arrival signal — a designated pickup area
   with numbered spaces and a phone or text arrival route, with an
   expected pickup time at checkout and a ready notification —
   recorded as a new source record; a stated wait with updates and
   reporting a wrong or missing item from the vehicle still have no
   platform or standards source, so the row stays open. Re-checked
   this run (deep editorial 2026-11-12): peer-reviewed operations
   research covers order-ahead pickup and promised pickup times as
   queueing concepts, and a regulator enforcement report covers a
   non-spoken ordering route at the drive-through window, but the
   curbside flow itself — vehicle identification, bay assignment,
   arrival check-in, handoff confirmation, and substitutions —
   still has no qualifying source. Re-checked this run (deep editorial 2026-11-16): platform developer guidance now covers simplified in-car ordering with confirmation before payment — recorded as a new source record — and a peer-reviewed retail study covers the substitution leg; vehicle identification, bay assignment, arrival check-in, handoff confirmation, a stated wait with updates, and reporting a wrong or missing item from the vehicle still have no platform or standards source, so the row stays open. Re-checked this run (deep editorial 2026-11-17): ordering guides now cover numbered pickup bays, a text arrival route, an expected pickup time stated at checkout, and a ready notification — recorded as two new source records — but a live wait with updates when the time moves, vehicle identification, handoff confirmation, and reporting a wrong or missing item from the vehicle still have no platform or standards source, so the row stays open. Done when the row passes all
   quality gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: a preorder pickup queue management guide, a curbside pickup wait-times guide, and drive-through ordering assistance legislation; the non-voice exception route rests on the already-recorded city disability office guidelines and cognitive-accessibility pattern.)

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
   laundry-specific, so the row stays open. Re-checked this run
   (deep editorial 2026-11-12): a 2026 published prototyping study
   of a laundry pickup and delivery app and a 2023 conference paper
   on a user-centred laundry system cover pickup and return
   scheduling with weight-based pricing and staged order tracking,
   but per-item inventory and pricing, per-item wash preferences, a
   distinct delivery window, and in-app damage or missing-item
   reporting still have no qualifying source. Re-checked this run (deep editorial 2026-11-16): a 2026 journal prototyping study and a 2025 journal study reinforce scheduling, weight-based pricing and staged tracking — recorded as a new source record; per-item inventory and pricing, per-item wash preferences, a distinct delivery window, and in-app damage or missing-item reporting still have no qualifying source, so the row stays open. Re-checked this run (deep editorial 2026-11-17): fresh sources are single-designer case studies and vendor feature pages only — a staged order tracker, weight-based pricing with an upfront buffer for count differences, and a three-step booking flow — with no qualifying source for per-item inventory and pricing, per-item wash preferences, a distinct delivery window, or in-app damage or missing-item reporting, so the row stays open.
   Done when the row passes all quality gates. (Implemented under roadmap action 395: the row is in `catalog/patterns.md` — reconciled this review.)

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
   passes all quality gates. (Implemented this run: the row was
   added in the deep editorial cycle of 2026-11-12; the earlier
   record rested on the shared Government document application
   row, which holds the stepped flow, fee, timescale, and
   invalid-on-submission rules in general form, while this row
   carries the renewal-specific eligibility, photo, fee-total,
   and tracking rules. Coverage matrix corrected the same run:
   Passport renewal moved from Partial to Full.)

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
   visit guidance. Re-checked this run: a single-organisation
   advice checklist now covers asking the child's age and the days
   needed first and asking for the exact sessions available rather
   than opening hours, but it is a single-organisation guide rather
   than a platform or standards source, so the row stays open. Re-checked this run (deep editorial 2026-11-17): an agency case study of on-demand childcare booking now covers availability shown by day with a care-type filter, multi-child and multi-day booking in one action, and per-child pricing — recorded as a new source record — but as an agency case study it is the same class as the single-organisation guide, so the row stays open.
   Done when the row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

266. Merged into action 341 (public library borrowing): the substance
   of this action — loans listed with due dates, holds shown with
   queue place and pickup window, renewals offered before the due
   date with a stated limit, a digital card shown on the phone
   where the library offers one, and any fee stated plainly before
   it blocks a new loan — now sits in action 341, which carries the
   combined row. Done when action 341 is done.

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

268. Merged into action 340 (ATM interface): the substance of this
   action — popular amounts first, the amount and any fee stated
   before confirming, a stated choice of denominations where
   offered, a receipt choice that never blocks the cash, and a
   screen readable in bright light — now sits in action 340, which
   carries the combined row; the card-return rule is not carried
   over, since single-bank evidence contradicts it and it still
   needs correcting before the row is written. Done when action 340
   is done.

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
   or standards source, so the row stays open. Sources are now a
   programme specification for home energy management systems,
   covering energy information by device across time intervals of a
   day or less, comparison with previous periods, sub-metering
   devices, and user notification, and a 2026 peer-reviewed design
   framework for home energy management interfaces with five core
   functions and thirty guidelines, recorded as new source records.
   Done when the row passes all
   quality gates. (Implemented this run.)

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
   still needed before the row is written. Sources are now regulator
   guidance on remote deposit capture, covering image quality and
   inaccurate data as capture risks, endorsement or marking of items
   as already processed, cut-off times, and retention of the original
   until destruction or voiding, recorded as a new source record.
   Done when the row
   passes all quality gates. (Implemented this run.)

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
   gates. (Implemented under roadmap action 400: the row is in `catalog/patterns.md` — reconciled this review.)

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
   source is still needed before the row is written. Re-checked
   this run (deep editorial 2026-11-11): the fresh results are
   single-venue travel guides and a ticket-reseller page covering
   the entry window, release schedule, named tickets, and the
   no-refund rule in substance, with no platform or standards
   guidance, so the row stays open. Re-checked this run (deep
   editorial 2026-11-12): a 2019 university thesis and a 2020
   research paper cover timed slots and per-slot capacity as a
   crowd-management mechanism, and 2020 government reopening
   guidance mentions pre-booked timed tickets, but the booking flow
   itself — slot choice with capacity shown, concessions, arrival
   and late-entry rules before payment, ticket handling, group
   booking — still has no qualifying source. Re-checked this run (deep editorial 2026-11-16): a sector-body ticketing guide and a 2019 university thesis now cover the booking flow — timed sessions with pre-defined capacity, the entry window and late-arrival rule stated before payment, accessibility and companion tickets in each slot, and a stated walk-in share — recorded as new source records; capacity shown to the visitor and group booking stay thin and are left out of the row. Done when the row passes all quality gates. (Implemented this run.)

279. Add a university admissions application pattern row to
   `catalog/patterns.md`: apply for a university place online — a
   per-section status dashboard with one clear next action, data
   carried forward between sections, late validation so optional stays
   optional, uploaded shown as not yet verified, and submitted shown
   as not yet paid, the fee is a separate step that opens only once
   the form is in, course and institution choice with entry
   requirements stated before starting, the programme chosen before
   any account is created, qualifications and predicted
   grades entered once, a personal statement with a stated length and
   a plain-language guide, references requested directly from the
   referee, a stated decision window with the offer types explained,
   and a reply deadline with the consequence of missing it stated —
   distinct from the university course registration row, which
   registers for courses after admission, and from the wizard row,
   which covers a stepped flow without the application decision.
   Sources so far are a vendor portal blog, single-product help pages,
   a sector admissions-service adviser guide that is staff-facing, a
   single-institution internal wiki, and a single-designer portfolio
   only; a platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates. Re-checked
   this run (deep editorial 2026-11-20): agency and content-site
   guides restate the same portal guidance — progress indicators,
   mobile-first forms, pre-filled data, staged communication — with
   no platform or standards source, so the row stays open.

280. Add a gym and fitness class booking pattern row to
   `catalog/patterns.md`: book a place in a timetabled class — a
   timetable with remaining places beside each session, a credit
   ledger for late cancellation and no-show, waiting-list promotion
   on release with a short claim window, and a door roster for
   check-in — distinct from the appointment management row, which
   books a time with a service, and from the shared resource booking
   row, which books a shared place rather than a place in a class.
   Sources so far are small-business blogs, a developer tutorial, a
   single-vendor help page, and an agency blog only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

281. Add a job application portal pattern row to
   `catalog/patterns.md`: apply for a job online — a short form with
   resume import instead of retyping, a progress indicator, no more
   than ten to fifteen fields, a single-column mobile layout, and
   the process stated plainly with the application status visible
   after submission — distinct from the form flow row, which covers
   a form without the hiring decision, and from the wizard row,
   which covers a stepped flow without the application. Sources so
   far are plugin documentation, vendor tutorials, and a
   form-builder blog only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. (Implemented this run: the row rests on two
   peer-reviewed usability studies of online job applications and
   two government candidate guides; the action's resume-import and
   ten-to-fifteen-field elements had no qualifying source and are
   not in the row, and the state after submission is the account's
   named state only.)

282. Add a blood donation appointment booking pattern row to
   `catalog/patterns.md`: book a donation appointment — an
   eligibility check first with the next eligible date named, a
   short pre-visit questionnaire in plain blocks answered before
   arrival, centre choice with opening hours and directions, a
   scannable check-in code at arrival, a donor card with the
   donation history and tally, and a reminder when the next
   donation is due — distinct from the appointment management row,
   which books a time with a service without the eligibility gate,
   and from the medication refill request row, which repeats a
   prescription rather than booking a donation. Sources so far are
   a single-designer case study, single-service app listings, and
   a single-service product page only; a platform or standards
   source is still needed before the row is written. Sources are
   now national blood service guidance from three services,
   covering the eligibility check with the next eligible date,
   donation-type choice, centre choice with hours and directions,
   the pre-visit questionnaire answered before arrival, book,
   move, and cancel, reminders, and the donation history and
   tally; the scannable check-in code element still has no source
   and stays out of the row. Done when the row passes all quality
   gates. (Implemented this run.)

283. Add a virtual court hearing pattern row to
   `catalog/patterns.md`: take part in a hearing by video — a
   waiting room where the host admits each person by name and role,
   the judge and the active speaker kept prominent, evidence shown
   in place of the video feed while it is reviewed, an interpreter
   added in real time where needed, the recording stated before
   the hearing starts, and a phone route where video is not
   possible — distinct from the video-call waiting room row, which
   admits people to a call without the formal roles and record, and
   from the telehealth video consultation row, which checks
   identity and privacy for a consultation rather than a
   proceeding. Sources so far are single-jurisdiction court pages,
   a vendor marketplace listing, a vendor case study, and a
   single-product site only; a platform or standards source is
   still needed before the row is written. Sources are now court
   and ministry guidance from three jurisdictions, covering the
   waiting room with name and role, the formal rules, the test
   call, the recording warning, the phone route, and the
   reconnection route; the evidence-in-place view and live
   interpreter elements still have no source and stay out of the
   row. Done when the row passes all quality gates.
   (Implemented this run.)

284. Add a proctored exam pattern row to `catalog/patterns.md`:
   sit a timed assessment under supervision online — an identity
   check with a photo document before the timer starts, a room and
   desk check in plain steps, numbered question navigation with
   any-order answering and autosave, the remaining time kept
   visible, a stated lock on rule violation with a route to resume
   where allowed, and the result stated only after submission —
   distinct from the identity verification onboarding row, which
   verifies a person once for an account rather than for each
   sitting, and from the wizard row, which covers a stepped flow
   without the timed assessment and supervision. Sources so far are
   a single-institution policy page, a single-vendor guide, a
   single-product page, a patent, and a single-institution help
   page only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run.)

285. Add a wedding registry and gift list pattern row to
   `catalog/patterns.md`: build and share a gift list for an
   occasion through one link with no account needed to view it —
   gifts shown as cards with price, link, notes, and availability
   status, items added from any store with a note on each, group
   gifting towards a higher-priced item with the amount still
   needed shown, purchased items marked so two guests never buy
   the same gift, the buyer's name hidden from the list owner
   until after the occasion, and a thank-you record naming who
   gave what — distinct from the saved-item collection row, which
   keeps items for one person, and from the gift card purchase row,
   which buys a value rather than a shared list. Sources so far are
   a vendor plugin page, app listings, a single-service guide, and
   a single-designer project brief only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates.

286. Add a hot-desk and co-working booking pattern row to
   `catalog/patterns.md`: book a desk in a shared workplace — a
   floor plan with only free desks choosable, capacity and
   equipment beside each desk, a check-in window after which an
   unclaimed desk is released at once, colleague location shown
   only with consent, and a recurring booking with a stated end —
   distinct from the shared resource booking row, which books a
   shared place without the floor plan and check-in-or-release
   rule, and from the appointment management row, which books a
   time with a service rather than a desk. Sources so far are
   vendor blogs, a single-product case study, and buyer guides
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates. (Implemented under roadmap action 401: the row is in `catalog/patterns.md` — reconciled this review.)

287. Add a driving test booking pattern row to
   `catalog/patterns.md`: book a driving theory or practical test
   — a licence number checked before dates are shown, a test
   centre chosen with its distance and earliest date, a date and
   time with a stated reschedule and cancellation window, a waiting
   list where no date is free, and a confirmation naming the
   centre, the date, the documents to bring, and what happens on
   arrival — distinct from the appointment management row, which
   books a time with a service without the licence gate, and from
   the university admissions application row, which applies for a
   place rather than booking a test. Sources so far are
   single-author booking guides, a driving-school blog, a
   third-party booking site, and a single-jurisdiction government
   service page that describes the booking steps without interface
   rules only. Re-checked this run (deep editorial 2026-11-12): a
   government consultation response now gives booking policy
   rules — only the learner books and manages the test, at most
   two changes, location changes limited to nearby centres — but
   no interface rules, so the row stays open; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. Re-checked this run (deep editorial 2026-11-17): the transport department's consultation outcome now covers learner-only booking with a limit of two changes and one area move — recorded as a new source record; the licence check before dates, centre choice with distance and earliest date, waiting list, and confirmation contents still have no platform or standards source, so the row stays open. Re-checked this run (deep editorial 2026-11-20): the national booking platform trial of July 2026 tested payments, bookings, and scheduling with real learners, and the 12 November 2026 booking-rules update confirms learner-only booking with at most two changes and one area move — both state booking policy and trial process, with no interface rules published, so the row stays open. Re-checked this run (deep editorial 2026-11-21): the government booking-rules guidance page now states the change-counting rules in full and the ten-full-working-day refund cutoff, recorded as a new source record; the licence check before dates, centre choice with distance and earliest date, waiting list, and confirmation contents still have no platform or standards source, so the row stays open. Re-checked this run (deep editorial 2026-11-21): the transport department bulletin announcing the new rules now in effect adds that booking through a third party is against the law and that online access can be restricted where licence details are misused, recorded as a new source record; the licence check before dates, centre choice with distance and earliest date, waiting list, and confirmation contents still have no platform or standards source, so the row stays open.

288. Add a home broadband installation and router setup pattern
   row to `catalog/patterns.md`: get a home internet connection
   working — an engineer appointment with a stated time window and
   an adult present at the visit, router placement advice with a
   signal check, guided setup in the app with the network name and
   password, a speed test with the result stated in plain words,
   and guest network and connected-device controls — distinct from
   the device pairing row, which connects one device, and from the
   appointment management row, which books a time with a service
   without the installation steps. Sources so far are comparison
   and self-install guides only; a platform or standards source is
   still needed before the row is written. Done when the row passes
   all quality gates.

289. Add a public transport season ticket purchase pattern row to
   `catalog/patterns.md`: buy a period pass for travel — the zones
   or route chosen before the price, a start date with the pass
   running from it, auto-renewal stated with its cancel route, and
   a refund for the unused period where the pass is no longer
   needed — distinct from the transit card top-up row, which adds
   credit to a card rather than buying a period pass, and from the
   fare-capped transit payment row, which charges per journey up to
   a cap. Sources so far are travel guides, a retailer help page,
   a fare-policy research report, and an operator app page only.
   Re-checked this run (deep editorial 2026-11-12): fresh results
   are single-operator help pages on smartcard season tickets —
   renewal windows, loading a ticket onto the card, and collection
   delays — with no interface guidance, so the row stays open; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.
   (Implemented this run: new pattern row in
   `catalog/patterns.md`, grounded in the sector-wide conditions of
   travel and the season-ticket information page.)

290. Add an online will creation pattern row to
   `catalog/patterns.md`: make a will online — one question per
   page with progress shown as section checklists, answers saved
   as they are given with an edit-before-submit step, plain-language
   explanations beside legal terms, a visual diagram of the estate
   with backup layers for each gift, a scenario tester for what-if
   outcomes, prompts to revisit the will after life changes, and a
   print-and-sign step with two witnesses and safe storage stated
   — distinct from the document signing row, which captures a
   signature on a document already made, and from the remote online
   notarization row, which witnesses a signing over live video.
   Sources so far are consumer-law guidance for will-writing
   businesses, which sets business obligations without interface
   rules, a single-product review, and a state trustee guide.
   Re-checked this run (deep editorial 2026-11-12): fresh results
   are a content-site guide, single-vendor product pages, and a
   comparison site, with no interface rules, so the row stays open;
   a platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates.
   (Reconciled this review: the earlier implemented marker was incorrect — no row exists, so the action stays open.)

291. Add a timed cart-hold pattern row to `catalog/patterns.md`:
   hold selected items for a bounded time while checkout
   completes — the hold stated at selection with a visible
   countdown from a server-held expiry, the held price kept with
   the hold, expiry treated as an ordinary state that clears the
   stale selection, explains what happened, and lets the person
   choose again, and one extension where offered — distinct from
   the seat selection row, which holds a chosen seat rather than
   cart items, from the high-demand queue row, which orders access
   when demand exceeds supply, and from the saved-cart recovery
   row, which restores a cart after the visit ends. Sources so far
   are single-vendor ticketing and storefront help pages only.
   Re-checked this run (deep editorial 2026-11-12): fresh results
   are storefront-platform extension guides repeating the
   honest-timer rules — never call a hold reserved unless stock is
   truly held, persist the countdown, let it expire visibly —
   still single-vendor class, so the row stays open; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates.

292. Add a digital parking permit application pattern row to
   `catalog/patterns.md`: apply for a permit to park in a zone —
   the permit type and zone chosen first, proof uploaded with
   capture guidance, save part-way with a stated return window,
   status shown by named stages from submitted to issued with a
   sent-back stage that names what to fix, renewal reminders
   before expiry, and a plate-based permit that allows a vehicle
   swap — distinct from the parking session payment row, which
   pays for one timed stay, and from the government document
   application row, which covers the shared flow for any official
   document without the permit stages. Sources so far are
   single-vendor product pages only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

293. Add a waste collection schedule and missed bin reporting
   pattern row to `catalog/patterns.md`: check when waste is
   collected and report a missed collection — an
   address-personalised schedule with holiday changes stated, an
   evening reminder before collection day, a missed-collection
   report that gives a reference number at once with named-stage
   status, a searchable guide to what goes where, a bulk pickup
   booking with photos and a volume estimate, and due times by
   report type with escalation where a report is overdue —
   distinct from the appointment management row, which books a
   time with a service, from the order tracking row, which follows
   a parcel rather than a report, and from the service status
   notice row, which states a service state without the report
   flow. Sources so far are vendor product pages and app-store
   listings only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run: the row rests on local-government
   service guidance; the action's holiday-change, what-goes-where
   guide, bulk pickup and escalation elements had no qualifying
   source and are not in the row; report and re-collection windows
   are stated as the service defines them, since services differ.)

294. Add a home cleaning service booking pattern row to
   `catalog/patterns.md`: book a cleaner for a home — a three- or
   four-step booking with the full price shown in a summary card
   before confirmation, a verified provider with trust signals shown
   before booking, the duration for the job type with a travel buffer,
   deposit rules stated up front, recurring work offered as a stated
   choice, and named booking states from booked to done, a home-size
   intake that sets the duration and price, access notes carried
   forward to each visit, and a cancellation cutoff with the fee shown
   — distinct from the appointment management row, which books a time
   with a service without the provider and price detail, from the
   shared resource booking row, which books a shared place rather than
   a service in the home, and from the recurring appointment series
   row, which repeats a booking without the per-visit provider choice.
   Sources so far are single-designer case studies, agency blogs, and
   a single-vendor scheduling blog only; a platform or standards
   source is still needed before the row is written. Done when the row
   passes all quality gates.

295. Add a smart TV programme guide pattern row to
   `catalog/patterns.md`: find what is on live television and plan
   viewing — a channel grid with a time axis and the current
   programme marked, a now-and-next strip over the picture, a
   favourites filter that shortens the grid, a programme
   description beside the entry before tuning in, a reminder set
   on a future programme, and catch-up or recording where the
   service offers it — distinct from the real-time departure board
   row, which shows a time grid for departures rather than
   programmes, and from the television layout, which covers focus
   navigation and ten-foot legibility without the guide grid.
   Sources so far are single-product programme-guide pages, a
   vendor documentation page, and an agency article only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.
   (Implemented this run: the row rests on platform developer
   guidance, the regulator's programme-guide code and published
   usability research; the action's favourites filter and
   catch-up or recording elements had no qualifying source and
   are not in the row.)

296. Add a school admissions application portal pattern row to
   `catalog/patterns.md`: apply for a school place online — an
   admissions-first landing page, a programme finder narrowing to
   course cards, a dedicated parent band with fees, safety, and
   support in plain words, a milestone timeline with cutoffs and
   deposit windows, staged inquiry forms, and a document checklist
   — distinct from the school parent portal row, which covers life
   after enrolment, and from the government document application
   row, which covers the shared flow for any official document
   without the admissions steps. Sources so far are a
   single-designer case study, an agency landing page, a
   single-author review, and an agency blog only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

297. Add a multiplayer game lobby and matchmaking pattern row to
   `catalog/patterns.md`: gather a party and find a match — a
   party roster with live updates, a queue with stated wait
   milestones and an updating estimate, a match-found accept as a
   deadline-bound consensus, role or character selection with
   contention visible, and constraint widening as the wait grows
   — distinct from the high-demand queue row, which orders access
   when demand exceeds supply, and from the waitlist row, which
   holds a place without the party and match steps. Sources so far
   are a tutorial site, a single-author system-design post, a
   code-documentation page, a system-design article, and
   single-platform vendor docs only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates.

298. Add a smartwatch workout tracking pattern row to
   `catalog/patterns.md`: follow a workout on a watch — three or
   four fields per screen with sport-specific defaults, zone
   colouring, focus pages for one measure, smoothing shown as
   display-only, and per-kilometre split cards — distinct from the
   sleep and rest data row, which reports rest rather than
   activity, and from the smartwatch fall detection row, which
   covers emergency response rather than workout data. Sources so
   far are a single-author blog and single-app documentation only;
   a platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.
   Re-checked this run (deep editorial 2026-11-12): platform
   guidance now recorded from two platform sources — watch
   design guidance covering glanceable single-screen interactions
   with minimal hierarchy, and workout guidance covering the
   figures people are most likely to care about, large session
   controls on their own screen, a dedicated glanceable metrics
   screen, a distinct active-workout appearance, large type and
   high contrast for reading in motion, and a summary at the end
   of a session — plus watch development guidance covering
   critical tasks only on the wrist, data gathering on the watch
   with detailed analysis on the phone, offline use, ongoing
   activity, haptic confirmation, and touch lock during a workout.
   The field-count, sport-specific-default, zone-colouring,
   focus-page, smoothing, and split-card specifics in the action
   as written have no platform source and are not in the row.
   Done when the row passes all quality gates. (Implemented this run.)
299. Add a university student portal dashboard pattern row to
   `catalog/patterns.md`: the enrolled student's home view — an
   alert banner for urgent items at the top, enrolled courses with
   grades and assessment deadlines, a timetable with upcoming
   lectures, and a fee balance, with each item opening its own
   view and a stated route to support — distinct from the
   university admissions application portal row, which covers
   applying, and from the university course registration row,
   which covers choosing and registering for courses. Sources so
   far are a vendor blog, a marketing blog, a vendor
   learning-platform blog, an agency blog, and a course-site page
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates.

300. Add an online course lesson player and progress pattern row
   to `catalog/patterns.md`: follow a course lesson by lesson —
   chunked lessons with a resume position that returns the learner
   to the exact place left, completion stated separately from
   mastery, progress shown at lesson, module, and course level in
   plain words beside any figure, short video chunks with captions
   on by default, checkpoint questions before the next lesson
   unlocks, and a syllabus that works as both a map and a progress
   record — distinct from the university student portal dashboard
   row, which shows the student's whole enrolment, and from the
   media chapters row, which marks points inside one recording.
   Sources so far are an accessibility-organisation baseline
   standard for e-learning, which covers captions, keyboard
   access, and plain language but not the player flow, plus
   single-author accessibility guides only; a platform or
   standards source for the player flow is still needed before the
   row is written. Done when the row passes all quality gates.
   (Implemented this run: five peer-reviewed sources now ground
   the player flow — a randomised trial of dashboard feedback and
   three-attempt practice questions, a dashboard design and
   evaluation study, a per-competency mastery scoring method, and two
   spaced-repetition studies — recorded as new source records.
   The row also carries two sub-elements beyond the action's
   original scope, quiz retry with escalating feedback and a
   spaced-repetition review queue, both grounded by those
   sources. The cross-check to the enrolment-wide student view
   is stated as a separate pattern, since that row does not
   exist yet.)

301. Add an airport self-service bag drop kiosk pattern row to
   `catalog/patterns.md`: check a bag in without staff — weigh the
   bag, print and attach the tag, place the bag, and confirm, with
   overweight and oversize handling stated at the point of
   weighing, a staff help route visible at every step, audio
   prompts and a stated availability indicator, and a touchless
   route that dispatches the bag once the tag and weight check pass
   — distinct from the travel check-in row, which confirms the
   trip and issues the pass, and from the self-checkout grocery
   kiosk row, which scans items rather than weighing and tagging a
   bag. An air-carrier accessibility rule for automated airport
   kiosks now grounds the accessibility layer — function parity
   with staffed routes, speech output, tactile controls, priority
   access, and visible identification — but the bag-drop flow
   itself still rests on vendor product pages and a single-vendor
   case study; a platform or standards source for the flow is
   still needed before the row is written. Done when the row
   passes all quality gates. Re-checked this run (deep editorial 2026-11-17): the industry standards body's common-use pages still cover only the shared infrastructure and data exchange, and the passenger flow still rests on single-operator guides — three new source records; overweight and oversize handling at weighing, a stated wait with updates, and a touchless dispatch route still have no platform or standards source, so the row stays open.

302. Add an online prize draw and raffle entry pattern row to
   `catalog/patterns.md`: enter a draw for a prize — live draws
   ordered by closing soonest, a ticket selector with bulk
   bundles, a countdown tied to a genuine deadline, a free entry
   route shown with the same prominence as the paid route and no
   more burdensome to use, the same odds for free and paid entries
   stated plainly, a skill question where the draw rests on skill,
   guest checkout, ticket numbers as the support reference, and
   draw verification with winner publication — distinct from the
   crowdfunding campaign page row, which funds a project, and from
   the limited-time offer countdown row, which times an offer
   rather than a draw. A regulator report on free draws and prize
   competitions now grounds the free-route rules — the free route
   clearly promoted alongside the paid route, no less convenient,
   at no more than the standard cost of communication, and treated
   equally in the draw — with a voluntary code of good practice
   adding age checks and spend controls; the ticket and draw
   mechanics still rest on single-author and agency sources only.
   Done when the row passes all quality gates.

303. Add a streaming household viewer profiles pattern row to
   `catalog/patterns.md`: several viewers inside one
   subscription — a profile picker on opening, each profile
   keeping its own watch history, recommendations,
   continue-watching state, and language, a PIN lock on adult
   profiles so a child cannot switch into one, per-profile content
   rating limits with a simplified view for younger viewers, and a
   stated profile limit where the plan sets one — distinct from the
   household member management row, which names who belongs to the
   household, and from the shared subscription plan row, which
   shares seats across accounts. Sources so far are a vendor
   glossary, a single-app guide, a vendor help page, and content
   sites only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates.

304. Add a pet adoption application pattern row to
   `catalog/patterns.md`: apply to adopt an animal from a shelter
   — browse without an account, each pet profile stating health
   records, vaccination status, and availability beside the shelter's
   verification mark, questionnaire-based matching on household,
   other animals, and experience, filters running on lifestyle and
   compatibility rather than looks alone, saved favourites for
   comparison, a meet-before-commit appointment, and a stated
   decision time with the next steps named, and the steps, documents,
   and fees explained before the application is started — distinct
   from the
   veterinary appointment booking row, which books care for an
   animal already owned, and from the appointment management row,
   which books a time with a service without the matching steps.
   Sources so far are a template marketplace page, a seven-day
   solo design challenge, a form-template vendor page, and a
   coursework portfolio only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

305. Add a lost property reporting pattern row to
   `catalog/patterns.md`: report something left behind — the right
   reporting route named first, since a terminal, an aircraft, and
   checked baggage each go elsewhere, a category-led description
   with brand, colour, and distinguishing marks, a photo where one
   is available, a reference issued at once, and status tracked by
   named stages with a stated retention period — distinct from the
   insurance claim submission row, which claims on a loss, and
   from the order tracking row, which follows a parcel already
   sent. Sources so far are a content-site guide, a single-airport
   news release, single-airport help pages, and a travel content
   site only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates.

306. Merged into action 381 (video doorbell visitor interface):
   the substance of this action — a loud indoor chime with a large
   visitor picture, one-action preset replies, a head-to-toe view
   showing the visitor and any parcel, and an event history with a
   stated retention rule — now sits in action 381, which carries
   the combined row. Done when action 381 is done.

307. Add a community sports league team registration pattern row
   to `catalog/patterns.md`: register a team or join as a free
   agent — division choice with a minimum roster size, teams
   movable between divisions for balance, roster deadlines with
   an add-and-drop form after the stated week, free-agent sign-up
   with placement not guaranteed, instalment payments, and a
   schedule and standings view that is the single up-to-date
   source — distinct from the waitlist row, which covers joining
   a full list, from the payment instalment plan row, which covers
   dated instalments without the registration flow, and from the
   university course registration row, which covers plan-then-
   register for courses. Sources so far are a municipal
   parks-district FAQ, a national governing-body membership portal
   for club membership rather than league registration, and a
   generic account-creation pattern only; a governing-body,
   regulator, standards-body, or peer-reviewed source for league
   registration is still needed before the row is written. Done
   when the row passes all quality gates.

308. Add a vehicle registration renewal and car tax payment pattern
   row to `catalog/patterns.md`: renew a vehicle registration and
   pay the tax online — renewal by registration number with the
   vehicle and its class looked up, the fee stated by vehicle class
   before payment, a renewal window tied to the expiry date, proof
   of inspection or emissions where required, and a digital record
   of the renewed registration — distinct from the Government
   document application row, which covers the shared flow for any
   official document without the vehicle lookup, class-based fee,
   and expiry-tied window, and from the parking fine payment and
   appeal row, which pays a fine from a notice rather than
   renewing a registration. Sources so far are government service
   pages describing the service, not design guidance; a platform
   or standards source is still needed before the row is written.
   Done when the row passes all quality gates.

309. Extend the Voice dictation input row in `catalog/patterns.md`
   with entry-control distinction rules once a platform or
   standards source surfaces: where a surface offers both
   dictation into a field and a voice-mode conversation, the two
   entries must not look alike — the voice-mode entry is the
   heavier control and dictation stays a line icon — so a person
   never starts a conversation when they meant to dictate, or
   dictates into a void when they meant to talk; the current row
   covers the microphone control, interim transcript, and editing
   without the two-entry distinction. Sources so far are a
   single-author survey of 19 apps only; a platform or standards
   source is still needed before the row is extended. Done when
   the extended row passes all quality gates.

310. Add a council tax payment and discount application pattern row to
   `catalog/patterns.md`: pay council tax online — the balance and the
   instalment plan shown before payment, payment by card or Direct
   Debit with a stated route to change the instalment plan, discounts
   and exemptions applied before the total is shown with the reason
   for each, and a stated route where the bill looks wrong, the bill
   with the band stated, the remaining balance shown after each
   payment, a discount or exemption check that asks only the questions
   that change the outcome, eligibility for each discount checked
   before the application starts so ineligible applicants are not
   asked for evidence, instalments already shown on the bill staying
   payable while the application is assessed, a change of
   circumstances carrying a stated reporting duty with its deadline
   and penalty, and a stated decision time with the revised bill
   issued at once — distinct from the benefits claim
   application row, which applies for support rather than paying a
   bill, and from the billing overview row, which explains one bill
   rather than a recurring local charge. Sources so far are council
   service pages only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   written. Done when the row passes all quality gates.

311. Merged into action 379 (ferry booking): the substance of
   this action — a cabin or seat choice where offered, vehicle
   details and the check-in window stated before payment, and a
   stated change and cancellation window with the fee for each —
   now sits in action 379, which carries the combined row. Done
   when action 379 is done.

312. Merged into action 342 (energy tariff comparison and
   switching): the substance of this action — the unit price and
   standing charge shown side by side with the estimated yearly
   cost for the household's own use, exit fees stated before the
   switch is confirmed, and a stated switch date with no gap in
   supply and a named route where the switch stalls — now sits in
   action 342, which carries the combined row. Done when action
   342 is done.

313. Extend the Virtual court hearing row in
   `catalog/patterns.md` with tribunal-guidance rules: during
   examination only the presiding member, the witness, the
   examining counsel and one opposing counsel have cameras on;
   chat is used only to reach the registry; during breaks
   microphones stay muted and cameras off until the hearing
   resumes — distinct from the video-call waiting room row,
   which admits people to a call without the formal roles and
   record, and from the live call controls row, which covers
   controls rather than hearing conduct. Sources so far are one
   tribunal's published guiding principles only; a second
   jurisdiction's published guidance is still needed before the
   rules are written. Done when the row passes all quality
   gates.

314. Add a worked flight booking example under `examples/`: a
   worked example demonstrating search, fare selection,
   passenger details, payment and confirmation with all seven
   states — distinct from the checkout worked example, which
   covers a goods purchase rather than a journey booking. The
   example follows the Flight search and booking pattern row
   added this run. Done when the example passes all quality
   gates.

315. Extend the Ballot row in `catalog/patterns.md` with remote
   ballot marking rules: voter privacy and ballot secrecy on a
   personal device, audio and language options with settings
   and selections preserved across a switch, and a display size
   suited to marking away from a polling place — distinct from
   the electronic display rules added this run, which cover
   text size, touch targets and scrolling on the ballot
   itself. Sources so far are the voting-system-guidelines
   application to remote ballot marking systems recorded this
   run; the privacy, audio and language specifics still need to
   be drawn from it before the row is extended. Done when the
   row passes all quality gates.

316. Add a personal budgeting and expense tracking dashboard
   pattern row to `catalog/patterns.md`: a period view showing
   planned, spent, and remaining amounts together with a single
   safe-to-spend figure, category budgets with spent-against-
   planned indicators, charts used as navigational summaries
   with labelled values and drill-down to the entries behind
   them, posted, pending, forecast, and manually entered values
   kept distinct with data freshness stated, and over-budget
   states worded as plain figures without judgement — distinct
   from the billing overview row, which explains one bill, from
   the transaction history row, which lists past payments
   without a plan to compare against, and from the expense claim
   submission row, which claims costs back rather than tracking
   them against a budget. Sources so far are a design-gallery
   content site reviewing recorded screens, a single-author
   article on financial dashboards, an agency guide, a
   single-designer portfolio, and a design-concept page only; a
   platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates.
   (Implemented: row added to `catalog/patterns.md`, completing
   the action; 2 new source records.)

317. Add a shared family calendar pattern row to
   `catalog/patterns.md`: a week-at-a-glance planning surface
   as the default view, with every adult able to add an event in
   a few actions, one colour per person with the owner named in
   the event title, preparation reminders tied to a specific
   action rather than to the event itself, documents linked from
   the event, and a shared wall display mode that opens on today
   with the week reachable in one action — distinct from the
   calendar and scheduling row, which shows one person's objects
   in time, from the household member management row, which
   governs who belongs to the household without the shared
   schedule, and from the shared shopping list row, which shares
   items rather than time. Sources so far are a content-site
   roundup, a sponsored product review, a personal build log,
   and a news digest only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates. (Implemented this run: row added to
   `catalog/patterns.md`, completing the action in narrower form
   — the who-is-next strip and claiming over assigning are in
   the row; the colour rules rest on vendor guides, with no
   platform or standards source. Five new source records: the
   family-calendar failure analysis, two colour-coding guides,
   and the calendar colour documentation.)

318. Add a wedding planning app pattern row to
   `catalog/patterns.md`: a countdown dashboard with confirmed
   guests, upcoming deadlines, and planning progress at a
   glance, a guest list with reply states, dietary needs, and a
   stated guest limit, a checklist with due dates counted back
   from the event date, a seating plan that shows the whole room
   at a glance, and a budget with spent against allocated, cost
   per guest, and upcoming payments, shared with a co-host who
   sees and edits the same guests, checklist, schedule, and
   budget — distinct from the wedding registry and gift list
   row, which covers gifts rather than planning, from the
   invitation response row, which answers one invitation rather
   than managing a guest list, and from the shared expense
   splitting row, which divides costs without the event plan.
   Sources so far are app-store listings, a magazine content
   piece, and a content-site roundup only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates.

319. Merged into action 380 (theme park virtual queue
   reservation): the substance of this action — the party size
   stated, a return time shown with the live wait beside it, a
   day view of reserved return times in time order, per-person
   eligibility checked before joining, and a plain notice where
   the return time moves — now sits in action 380, which carries
   the combined row. Done when action 380 is done.

320. Add a board game app interface pattern row to
   `catalog/patterns.md`: the board as the primary area with
   squares large enough for touch input, drag-and-drop and
   tap-to-move both offered, legal moves shown when a piece is
   selected, time controls explained in plain words,
   high-contrast board and piece options, a move history and a
   plain statement of the game state, and an intent-based first
   run with one choice per screen — distinct from the
   multiplayer game lobby and matchmaking row, which covers
   finding and joining a game rather than playing on a board,
   and from the live poll row, which collects votes rather than
   moves. Sources so far are a content-site guide, a vendor
   development blog, a code-documentation page, and a review
   aggregator only; a platform or standards source is still
   needed before the row is written. Done when the row passes
   all quality gates. Re-checked this run (deep editorial
   2026-11-13): platform guidance now recorded from two
   platform sources — board-game platform studio guidelines
   covering a square-ratio centred board, no hidden components,
   an action bar of at most four actions, compact player panels,
   full-scale play without zoom controls, 32 px minimum targets,
   standard contrast, short animations, tooltips, single-tap
   play, and a game log — and a publisher art and interface
   guide covering separate out-of-game and in-game screens,
   shared elements kept in the same place on every screen, a
   consistent element library, phone-to-desktop responsiveness,
   and room for longer translated text. The multiplayer game
   lobby and matchmaking distinction in the action as written is
   against open action 297, which is still open; the row as
   written distinguishes itself from the live poll row instead.
   Done when the row passes all quality gates. (Implemented this run.)

321. Add a music streaming playlist and queue pattern row to
   `catalog/patterns.md`: a now-playing view with large artwork,
   a progress bar with elapsed and remaining time, and transport
   controls in the thumb zone; a queue that shows what is playing
   now, what is next, and what was played, with drag handles to
   reorder, a remove control on each queued track, and shuffle and
   repeat states that survive the session; a mini player pinned
   above the tab bar while browsing; and per-track menus with add
   to playlist, add to queue, and save to library as one action
   each — distinct from the playback queue row, which orders items
   for one session without the library and playlist management,
   and from the sleep timer row, which stops playback after a set
   time. Sources so far are an interview-preparation architecture
   document, a student design critique of one product, a
   UI-challenge exercise prompt, a wireframe template page, and an
   open-source player guide only; a platform or standards source is
   still needed before the row is written. Done when the row passes
   all quality gates. (Implemented this run.)

322. Add a podcast app playback interface pattern row to
   `catalog/patterns.md`: a now-playing view with chapter marks in
   the waveform and a chapter list that follows playback, a synced
   transcript with a search, speed control in small steps, skip
   back and forward in stated seconds, a sleep timer that stops at
   a chosen time or at the end of the episode or chapter, bookmarks
   at a position, and a persistent mini player with resume position
   kept across sessions — distinct from the online course lesson
   player and progress row, which follows lessons with graded
   assessments, and from the media chapters row, which marks
   sections without the playback and transcript behaviour. Sources
   so far are a design-gallery screen listing, a vendor blog,
   single-product support pages, and a small-product blog only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run: row added to `catalog/patterns.md`, completing the action in narrower form — bookmarks at a position have no platform or standards source and are not in the row. Three new source records: the media session standard, its reference documentation, and the podcast player controls article.)

323. Add a digital wallet add-card and tap-to-pay setup pattern row
   to `catalog/patterns.md`: adding a card by camera capture with
   manual entry as the fallback, bank verification by code before
   the card is usable, a stated choice of default card, a tap-to-pay
   switch with a plain statement of what it does, and a pass that
   shows balance, code, and expiry with a barcode for scanning —
   distinct from the contactless payment confirmation row, which
   confirms one payment rather than setting up the wallet, and from
   the digital identity wallet presentation row, which presents an
   identity credential rather than a payment card. Sources so far
   are vendor developer documentation and an unofficial mirror of
   platform wallet guidance only; official platform wallet guidance
   is still needed before the row is written. Done when the row
   passes all quality gates. (Implemented this run: row added to `catalog/patterns.md` with two new official platform source records (849 total). Re-checked this run (deep editorial 2026-11-13): official platform guidance now recorded — the pass design and creation guide and the wallet getting-started guide — covering pass styles, the field layout set by the style, barcode use, and designing for every device; the pass-display element is now written into the row, completing the action.)

324. Add a banking fraud alert pattern row to
   `catalog/patterns.md`: notify at the moment of the decision
   through a channel the person has shown they read, naming the
   exact transaction with the amount, the merchant as the person
   would recognise it, the location, and the time; offer three
   choices — confirm, deny, and an unsure path that freezes the
   card while the person checks — with the consequence of each
   stated; keep recurring payments flowing while the card is
   frozen; close the loop with the outcome of the report; and let
   the person tune which alerts they receive and where — distinct
   from the card freeze row, which freezes the card without the
   alert, from the transaction dispute row, which disputes a
   charge after the fact, and from the suspected spam call warning
   row, which warns about a call rather than a transaction.
   Sources so far are a single-author content site, a vendor blog,
   a single-author post, and a vendor blog only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented this run.)

325. Add a digital health record patient portal pattern row to
   `catalog/patterns.md`: a home that shows results, medicines,
   appointments, and messages as separate tasks rather than
   everything at once; a result shown with a plain-language
   explanation of what it means and a route to a clinician, never
   as a bare value; proxy access for a carer with a stated scope
   that the person can change or remove; records shared as a
   summary the person reviews first rather than raw data; a
   session-timeout warning with time to save; and consent in plain
   language at the point it is given — distinct from the health
   record sharing row, which shares a record outward, from the
   medication refill request row, which refills one medicine, and
   from the telehealth video consultation row, which holds a live
   visit. Sources so far are a single-author content site, a
   vendor blog, a parliamentary record, and a single-designer
   portfolio only; the general service standard found covers
   services as a whole rather than the portal itself, so
   portal-specific platform or standards guidance is still needed
   before the row is written. Done when the row passes all quality gates. (Implemented this run.)

326. Add an audiobook library app pattern row to
   `catalog/patterns.md`: a library organised by book with the
   listening position kept per title; a player with large cover
   art, progress with elapsed and remaining time, skip back and
   forward in stated seconds, speed in small steps, and a sleep
   timer that stops at a chosen time or at the end of the chapter;
   a chapter list that follows playback; bookmarks at a position
   with a note; a resume position kept across devices and
   sessions; and downloads stated plainly with their size and a
   remove control — distinct from the e-reader and reading app
   row, which reads text rather than playing narration, from the
   podcast app playback interface row, which follows episodic
   shows with transcripts rather than books with chapters, and
   from the media chapters row, which marks sections without the
   book library and resume behaviour. Sources so far are
   single-product how-to sites and a content site only; a platform
   or standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented this run: row added to `catalog/patterns.md`, completing the action in narrower form — bookmarks with a note, downloads with size and a remove control, and a resume position kept across devices have no platform or standards source and are not in the row. One new source record: the audiobook profile of the publication manifest.)

327. Add a pet grooming appointment booking pattern row to
   `catalog/patterns.md`: pet first, then service, then groomer,
   then time; multi-pet profiles with per-pet notes; a repeat
   series for regular grooms; status updates from drop-off to
   ready; and a stated cancellation and late-arrival policy —
   distinct from the veterinary appointment booking row, which
   covers clinical care rather than grooming, from the
   appointment management row, which books a service slot
   without the pet and groomer choices, and from the delivery
   slot picker row, which picks a time window rather than a
   named groomer. Sources so far are a content site, a
   single-designer portfolio, a vendor blog, and a journal paper
   on a single-shop system only; a platform or standards source
   is still needed before the row is written. Done when the row
   passes all quality gates.

328. Add a school lunch ordering pattern row to
   `catalog/patterns.md`: pre-order by date with a stated
   cutoff, allergy and diet flags on every meal, ordering per
   child from one account, a calendar view of ordered meals, and
   cancellation before the deadline with automatic credit —
   distinct from the restaurant online ordering row, which orders
   one meal at a time without the school calendar, from the
   school parent portal row, which covers school administration
   rather than meals, from the meal planning row, which plans
   home cooking rather than school orders, and from the order
   substitution choice row, which swaps one item rather than
   cancelling a whole order. Sources so far are single-operator
   product pages, app-store listings, and a single-designer
   portfolio only; a platform or standards source is still
   needed before the row is written. Done when the row passes
   all quality gates.

329. Add a home solar energy monitoring pattern row to
   `catalog/patterns.md`: production first, with live generation
   beside consumption and savings, production versus consumption
   over time, export to the grid, battery state, and
   system-health alerts, with separate views for the homeowner
   and the installer — distinct from the home energy usage
   dashboard row, which covers consumption and cost over time
   without generation, export, or battery state, and from the
   smart home dashboard row, which controls devices rather than
   reporting generation. Sources so far are a single-designer
   portfolio, agency case studies, a student project, and two
   recent homeowner guides that agree on the measurement rules —
   state what the app measures, keep measured figures apart from
   calculated ones, and treat battery state as stored energy
   rather than hours of use — but no platform or standards source
   yet; one is still needed before the row is written. Done when
   the row passes all quality gates.

330. Add a meal kit delivery subscription pattern row to
   `catalog/patterns.md`: plan choice with the number of meals
   per week, servings, and diet preferences, and the weekly
   price stated; weekly menu selection with a stated cutoff
   days before delivery and a save confirmation; skip a
   delivery week from the menu with the cutoff stated; pause
   the subscription without losing credits; cancel online
   through the same channel used to sign up, with the
   consequence for credits stated; and reactivate from the
   account — distinct from the restaurant online ordering row,
   which orders one meal at a time, from the meal planning row,
   which plans home cooking rather than a delivered box, from
   the subscription pause row, which pauses any subscription
   without the weekly menu and cutoff, and from the order
   substitution choice row, which swaps one item rather than
   skipping a whole week. Sources so far are vendor help pages
   for five operators and summaries of consumer-protection law
   on cancellation only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

331. Extend the pass or ticket transfer row in
   `catalog/patterns.md` with the resale-marketplace side: a
   price cap stated on the listing, seller verification before
   payout, and the seller paid only after the buyer has
   received a valid ticket — distinct from the gift option row,
   which gives a purchase as a gift rather than reselling a
   ticket, and from the order cancellation row, which returns a
   purchase rather than passing it to another buyer. Sources so
   far are single-designer case studies, a student critique,
   and a single-app journal paper only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates.

332. Add a volunteer shift signup pattern row to
   `catalog/patterns.md`: recurring shifts built once with holidays
   removable; roles locked to qualified volunteers, so volunteers only
   see shifts they can take; a sign-up sheet with one line per spot;
   reminders before each shift and an urgent call-out when someone
   drops out close to the day; hours counted automatically per
   volunteer; cancellation by the volunteer with the spot reopened at
   once; and a coordinator view with a live roster and day-of
   attendance, open shifts browsed by time or by role with places left
   shown, shift detail naming the meeting point, preparation, and who
   to ask for, a request that stays a request until confirmed, a
   commitments view with the cancellation effect shown before
   cancelling, and day-of check-in with approved hours — distinct from
   the group scheduling poll row, which finds one time for a group,
   from the appointment management row, which books a service slot,
   and from the shared resource booking row, which books a resource
   rather than a volunteer shift. Sources so far are single-product
   help pages and marketing pages only; a platform or standards source
   is still needed before the row is written. Done when the row passes
   all quality gates. Re-checked this run (deep editorial 2026-11-20):
   four single-vendor scheduling products corroborate the signup flow
   already recorded — no-account signup link, shift-first or job-first
   browsing, waitlist auto-promotion, reminders, and two-click
   cancellation; the substitute-request material belongs to new action
   426; the row stays open.

333. Add a peer-to-peer payment pattern row to
   `catalog/patterns.md`: choose a recipient from recent people
   or by name, handle, or code, with the recipient shown plainly
   before any amount is entered; enter the amount with the
   available balance and any fee visible while typing; offer send
   and request as two plain choices with the consequence of each
   stated; confirm the recipient, amount, source, and fee on one
   review screen before anything moves; authorise with the device
   check; and show a receipt with a stated state — sent, pending,
   or failed — and a plain route to cancel a pending payment and
   to report a payment sent to the wrong person — distinct from
   the split payment row, which divides one total across payers
   at once, from the transaction history row, which lists past
   payments without moving money, and from the scan-to-pay row,
   which pays a seller by code rather than sending money to a
   person. Sources so far are a UI-kit vendor guide, an agency
   article on one product, a single-designer case study, a
   personal post, an agency portfolio, and an agency guide only;
   a platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates.

334. Add a parcel sending and courier booking pattern row to
   `catalog/patterns.md`: pickup and drop-off addresses first
   with a map pin where an address is unclear, a plain
   description of the contents with weight and size, a stated
   price before booking with the payer chosen — sender or
   receiver — a pickup code shown on screen to hand the parcel
   to the right courier, a label offered for home printing or as
   a code to print at a drop-off point, live tracking with the
   courier's position, and a stated route for a missed pickup or
   a damaged parcel — distinct from the parcel locker pickup row,
   which collects a parcel already sent, from the order tracking
   row, which follows a placed order, and from the delivery slot
   picker row, which chooses when a delivery arrives rather than
   sending a parcel. Sources so far are single-operator help
   pages and a blog, app-store listings, a vendor user guide, and
   a carrier guide only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

335. Add a smart home security camera pattern row to
   `catalog/patterns.md`: a live view per camera with the camera's
   name and place shown, a multi-camera grid with a still preview per
   camera, an event timeline with a thumbnail and a plain label for
   what triggered each event, a scrubbable recording timeline with
   event markers, a filter by event kind — person, vehicle, animal, or
   sound — two-way talk and a snapshot control on the live view,
   privacy zones stated where the camera does not record, and a plain
   statement of how long recordings are kept and who can watch them —
   distinct from the smart home dashboard row, which controls devices
   rather than watching cameras, from the video doorbell visitor
   interface row, which answers a visitor at the door, and from the
   media viewer row, which inspects one visual rather than a live feed
   with events. Sources so far are app-store listings, an open-source
   project documentation site, a listing site, a content site, a
   vendor product page, and a single-author review only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates. (Implemented through 407.)

336. Add a food rescue and surplus food pickup pattern row to
   `catalog/patterns.md`: nearby offers on a map and in a list
   with the pickup window and the discounted price beside each, a
   plain statement that the contents are a surprise assortment
   rather than a chosen meal, a reserve step that states the
   collection window and the place before payment, a handover code
   or confirmation shown at pickup, a stated rule for a missed
   pickup window, and a favourites route with alerts when a chosen
   place posts a new offer — distinct from the restaurant online
   ordering row, which orders a chosen meal, from the meal
   planning row, which plans home cooking, and from the pickup
   point selection row, which collects an order already placed
   rather than reserving surplus food. Sources so far are
   app-review content sites, a download listing, a single-designer
   case study, and a news site only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates.

337. Add a period and fertility tracking pattern row to
   `catalog/patterns.md`: a prediction shown as a window drawn
   from recent cycles rather than a single date, the window
   widening for irregular cycles, no phase named without
   evidence of ovulation, calm wording when a period is late,
   privacy by default, and never diagnosing — distinct from the
   medication reminder row, which reminds about doses on a
   schedule, and from the sleep and rest data row, which records
   rest rather than cycles. Sources so far are a single-designer
   portfolio, a single-designer fertility redesign, two agency
   prototype case studies, and a student design-lab document
   only; a platform or standards source is still needed before the row is written. Done when the row passes all quality gates. (Implemented this run.)

338. Add an airport lounge access pattern row to
   `catalog/patterns.md`: a digital membership card with a
   scannable code, entitlement and remaining visits stated
   before entry, walk-in versus pre-booked entry, charges stated
   before entry, and an offline card — distinct from the pass
   and ticket display row, which shows a ticket already held,
   and from the hotel booking row, which books a stay rather
   than entry to a lounge. Sources so far are bank instruction
   and customer-journey documents, a vendor help-centre page,
   and app-store listings only; a platform or standards source is still needed before the row is written. Done when the row passes all quality gates. (Implemented this run.)

339. Add a smart thermostat heating schedule pattern row to
   `catalog/patterns.md`: one target temperature with the system
   choosing heat or cool, a vertical schedule timeline, reusable
   named schedule events applied across days, and system state
   first — distinct from the smart home dashboard row, which
   shows the whole home, and from the home energy usage
   dashboard row, which reports use and cost. Sources so far are
   two single-designer redesign portfolios of one vendor
   thermostat, a single-designer concept app, a converted vendor
   user manual, and a 2003 patent only; a platform or standards source is still needed before the row is written. Done when the row passes all quality gates. (Implemented this run.)

340. Add an ATM interface pattern row to
   `catalog/patterns.md`: one transaction at a time with the
   amount and the account shown before confirming, tactile keys
   and speech output for every step, a session limit warned
   through more than one sense with a way to extend it, privacy
   of input and output equal to the screen, and card, cash, and
   receipt handling stated at each step, popular amounts first,
   a stated choice of denominations where offered, a receipt choice
   that never blocks the cash, and a screen readable in bright
   light — distinct from the
   self-checkout grocery kiosk row, which scans and pays for
   goods at a retail till, and from the QR code payment at a
   till row, which pays at a till rather than withdrawing cash.
   Merged with action 268 this review; the combined row carries
   both actions' substance. Sources so far are the self-service-terminal accessibility
   duties in the European Accessibility Act and the 2010
   accessibility standards for automatic teller machines — both
   standards sources — plus a banking accessibility regulation,
   a national disability-access standard for cash machines, and
   regulator rules for the fee stated before confirming and for
   receipt contents; a design-focused source is still useful
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run: the design-focused sources are now recorded — an accessibility organisation's self-service terminal guide, a cash-machine software accessibility guide, and a standards explainer on terminal duties — alongside the standards sources already recorded.)

341. Add a public library borrowing pattern row to
   `catalog/patterns.md`: search the catalogue and place a hold
   with a pickup location and a collection expiry, loans with due
   dates and remaining renewals shown together, renew one item
   or renew all with failures named, overdue and auto-renewal
   states stated plainly, and a digital card barcode for
   borrowing at a self-service point, holds shown with queue place
   and pickup window, renewals offered before the due date with a
   stated limit, and any fee stated plainly before it blocks a new
   loan — distinct from the
   audiobook library app row, which plays borrowed media rather
   than tracking loans, and from the parcel locker pickup row,
   which collects a parcel rather than borrowing an item.
   Merged with action 266 this review; the combined row carries
   both actions' substance. Sources so far are council library help pages and
   single-designer case studies only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

342. Add an energy tariff comparison and switching pattern row
   to `catalog/patterns.md`: compare by the annual cost at the
   household's actual consumption, unit rate and standing charge
   shown separately for each fuel, contract length and exit fee
   stated beside the saving, a switch with a stated start date
   and a cooling-off period, and supply never interrupted by the
   switch, with a named route where the switch stalls — distinct
   from the home energy usage dashboard row,
   which reports use and cost without comparing tariffs, and from
   the billing overview row, which shows one bill without a
   switch. Merged with action 312 this review; the combined row
   carries both actions' substance. Sources so far are consumer comparison guides citing
   regulator switching guidance and a regulator price-cap
   explainer; a direct regulator switching page is still needed
   before the row is written. Done when the row passes all
   quality gates. (Implemented: the row is in `catalog/patterns.md`, completing this action — reconciled this review.)

343. Add a crypto wallet app pattern row to
   `catalog/patterns.md`: a balance shown in both the token
   amount and the local currency value, send and receive flows
   with the address checked before confirming, a stated network
   fee before sending, seed-phrase backup with a recovery test,
   and transaction history with a plain-language state —
   distinct from the digital wallet add-card and tap-to-pay setup
   row, which adds a card for tap payments, and from the
   transaction history row, which lists past payments without
   holding assets. Sources so far are a single-author newsletter,
   an agency teardown, a vendor case study, and a content wiki
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates.

344. Add a drone and robot delivery tracking pattern row to
   `catalog/patterns.md`: named stages with handoffs shown as
   progress, a flight or travel window rather than a simulated
   live position, payload and drop-zone limits stated before
   ordering, a handoff confirmation with a code or photo, and a
   delay or return state with a plain next step — distinct from
   the order tracking row, which follows a parcel through
   depots, and from the delivery slot picker row, which books a
   time window for a courier. Sources so far are agency design
   concepts, a student portfolio, a single-designer pilot
   direction with no live results, a thesis abstract, and a
   patent only; a platform or standards source is still needed
   before the row is written. Re-checked this run (deep editorial 2026-11-16): regulator pages for unmanned traffic management and delivery-operator certification are now recorded as source records, but both are operator-facing with no consumer tracking interface guidance, and the beyond-visual-line-of-sight rule is still a proposal; a platform or standards source for the consumer tracking view is still needed, so the row stays open. Done when the row passes all
   quality gates.

345. Add a smart door lock and keyless entry pattern row to
   `catalog/patterns.md`: lock state first on the home screen,
   one-tap lock and unlock with a stated result, time-limited
   guest codes with expiry shown, an access log naming who
   entered and when, a stated offline fallback when the
   connection drops, and a battery warning with a stated number
   of remaining entries — distinct from the temporary home
   access code row, which grants a one-off code for a visit, and
   from the digital car key sharing row, which shares a vehicle
   key rather than a home lock. Sources so far are an agency
   case study for one vendor lock, a hardware review, a
   design-award entry, a single-designer kiosk concept, a vendor
   product sheet, and app-store listings only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented this run.)

346. Add a video streaming player interface pattern row to
   `catalog/patterns.md`: auto-hiding controls with play, pause,
   skip, volume, and fullscreen reachable without hunting;
   an expanding progress bar with thumbnail scrub previews and
   chapter markers; a stated keyboard map; captions and
   audio-description toggles with a transcript route; playback
   speed; picture-in-picture; and gesture-first mobile controls
   — distinct from the podcast app playback interface row, which
   is audio-first with resume and queue, from the live-viewing
   app row, which follows a broadcast schedule, and from the
   smart TV programme guide row, which covers ten-foot
   navigation. Sources so far are an agency media-player guide,
   a developer tutorial, a vendor accessibility guide, a vendor
   player blog, and an accessibility content site restating
   media criteria only; a platform or standards source for the
   player interface itself is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented: the row is in `catalog/patterns.md` and recorded in `CHANGELOG.md`; reconciled this review — the original action number was never marked when the row was added.)

347. Add a government citizen services portal pattern row to
   `catalog/patterns.md`: services organised by the resident's
   task rather than department structure, the task begun before
   account creation, one sign-on across services, plain-language
   service cards with eligibility and timescale stated, progress
   indication across services, and errors that explain the
   solution — distinct from the government document application
   row, which covers a single-service flow. Sources so far are
   the government design-system service-structure patterns
   (start page, eligibility, check answers, confirmation) and
   agency blogs only; a platform or standards source for the
   portal-level organisation of many services is still needed
   before the row is written. Done when the row passes all
   quality gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: a cross-government service-patterns specification, a local-service pattern taxonomy, and a citizen-portal planning guide; the per-service structure rests on the already-recorded government design-system service-structure patterns.)

348. Add a weather app interface pattern row to
   `catalog/patterns.md`: the place, observation time, and
   current conditions anchored before detail; hourly data for
   near-term timing and daily summaries for planning; observed
   versus forecast radar frames labelled with animation time
   and legend; alerts with type, severity, area, issuer, start
   and end, and an action summary, in colour plus text and icon,
   never rewriting official safety instructions — distinct from
   the broadcast emergency alert row, which covers a single
   alert. Sources so far are a design-gallery roundup, a vendor
   blog, and an agency case study of one government weather app
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: the international alert standard, its national weather-service documentation, and a professional-body guide to forecast presentation; the glanceability rules rest on the already-recorded weather-app design guide.)

349. Add a neighbourhood noticeboard pattern row to
   `catalog/patterns.md`: membership verified by address so only
   people from the area can post, posts grouped by offer, request,
   event, and lost and found, each post expiring after a stated
   period with a re-post route, safety reports kept apart from
   discussion with a stated route to local services,
   recommendations naming the service and the experience rather
   than a bare score, and private contact that never exposes an
   address or a phone number — distinct from the lost property
   reporting action (305), which covers a single report, and from
   the group conversation rows, which carry an open chat rather
   than a categorised board. Sources so far are app-store listings
   for three neighbourhood apps, a generated demo board page, and
   an app-download mirror only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

350. Add a digital business card sharing pattern row to
   `catalog/patterns.md`: share by QR code, NFC tap, or link with
   the recipient needing no app, a save-contact action at the top
   of the profile, one card that updates for every recipient when
   details change, a wallet pass for offline access, separate cards
   for different contexts, and scan and save counts stated plainly
   with a turn-off — distinct from the QR sign-in row, which signs
   the person in, from the scan-to-pay row, which takes a payment,
   and from the contact picker row, which chooses a contact rather
   than sharing one's own details. Sources so far are a vendor
   marketing page, a vendor guide, a vendor comparison blog, and
   app-store listings only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

351. Add a carpool coordination pattern row to
   `catalog/patterns.md`: drivers publish a route with pickup
   points, departure time, seats, and a per-seat price shown in
   full before booking, recurring routes for regular commutes with
   a stated detour limit for the driver, the cost shared by
   distance with a plain breakdown and a stated rule that payment
   covers costs only, identity and vehicle checks before the first
   shared trip, in-app messages without sharing phone numbers, and
   a stated rule for cancellations and no-shows on both sides —
   distinct from the ride booking row, which hires a ride on
   demand, and from the shared trip itinerary row, which shares a
   plan between travellers rather than booking seats. Sources so
   far are a vendor white-label page, app-store listings, a
   system-design walkthrough, and a hackathon project page only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

352. Add a home EV charger scheduling pattern row to
   `catalog/patterns.md`: a ready-by time set once per day with a
   target charge level, charging shifted to off-peak hours with the
   saving shown in plain money terms, solar surplus used first
   where the home generates it with a stated fallback to the grid,
   a boost control that charges at once and states the extra cost,
   a live view of the current session with energy and cost so far,
   and a stated rule for a late plug-in or an early unplug —
   distinct from the electric vehicle charging session row, which
   covers public charging found and paid per session, and from the
   home energy usage dashboard row, which covers whole-home use
   rather than one charger's schedule. Sources so far are vendor
   product pages, an installer guide, a content-site guide, and an
   app-store listing only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates.

353. Add a phone-side fitness workout logging pattern row to
   `catalog/patterns.md`: start, pause, and resume from the phone
   during a workout, live stats that stay readable at a glance,
   a post-workout summary with route and effort, recording that
   keeps working offline and syncs later, and a stated rule for a
   workout interrupted by a call or a dead battery — distinct from
   the smartwatch workout tracking row, which covers glance-first
   tracking on the wrist, and from the sleep and rest data row,
   which covers rest rather than activity. Sources so far are
   vendor app pages, agency case studies, and app-store listings
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates. (Implemented this run.)

354. Add a digital loyalty card wallet pass pattern row to
   `catalog/patterns.md`: a fixed-slot pass that states the reward
   itself rather than only a points balance, the balance and expiry
   shown on the pass, a per-pass control for notifications, and a
   stated rule for a pass whose balance or tier changes — distinct
   from the loyalty rewards row, which covers earning and
   redeeming inside an app, and from the pass and ticket display
   row, which covers showing a pass rather than its loyalty
   content. Sources so far are vendor guides and the wallet pass
   field documentation already recorded; a platform or standards
   source for the loyalty-pass presentation itself is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run.)

355. Add an online discussion forum pattern row to
   `catalog/patterns.md`: hierarchical categories with tagging,
   search by date, relevance, and category, reply threading with a
   stated depth limit, badges and reputation shown beside the
   author, moderation and reporting controls on every post, and
   sign-in with an existing account — distinct from the chat and
   messaging row, which covers private conversation, and from the
   annotation and comment thread row, which covers comments on one
   item rather than a board of topics. Sources so far are four
   content-site articles only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

356. Add a smart fridge and food inventory pattern row to
   `catalog/patterns.md`: one list across fridge, freezer, and
   pantry sorted by what expires first, suggested dates from
   built-in shelf-life data, opened-item dates that adjust when a
   pack is opened, a single daily reminder naming what must be
   used, recipe suggestions from what must be used first, and
   household sharing so the list stays true for everyone who
   shops and cooks — distinct from the meal planning row, which
   plans meals rather than tracking what is stored, and from the
   shared shopping list row, which lists what to buy rather than
   what is already in the kitchen. Sources so far are app-store
   listings, vendor guides, a single-designer case study, and an
   open-source app listing only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

357. Add a smart baby monitor app pattern row to
   `catalog/patterns.md`: live video with night vision, cry,
   motion, and sound alerts with a history list, two-way audio,
   room temperature and humidity with safe-range alerts, a local
   parent-unit mode and a remote app mode, and an encrypted feed
   and storage — distinct from the smart home dashboard row,
   which controls heating, lights, and locks rather than watching
   a child, and from the sleep and rest data row, which records
   one person's own rest rather than live monitoring of another
   room. Sources so far are product reviews, tech-news reports,
   and an app-comparison site only; a platform or standards
   source is still needed before the row is written. Done when
   the row passes all quality gates.

358. Add a smart garden and plant care app pattern row to
   `catalog/patterns.md`: per-plant watering and feeding
   intervals adjusted for light, pot size, and season, reminders
   framed as soil checks rather than fixed calendars, one gentle
   reminder a day, a care history with a rolling average
   interval, and a holiday mode with a care plan for a sitter —
   distinct from the habit streak row, which rewards repetition
   rather than timing care to a plant's needs, and from the
   medication reminder row, which reminds a person to take their
   own medicine on a fixed schedule. Sources so far are
   app-store listings, single-developer project pages, and a
   content-site guide only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

359. Add a salon and spa appointment booking pattern row to
   `catalog/patterns.md`: service menu with prices and durations,
   stylist choice, only slots that fit the total duration, a stated
   free-cancellation window with late and no-show fees, and a review
   step naming price, payment timing, and cancellation rules, a
   deposit stated where one is taken, and a stated route to change or
   cancel with the consequence named — distinct from the appointment
   management row, which covers booked appointments rather than
   choosing a service and a stylist, and from the delivery slot picker
   row, which picks a delivery window rather than a service slot.
   Sources so far are an agency blog, a wireframe template traced from
   one booking app, a vendor blog, and UI-kit listings only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.

360. Add a meditation and mindfulness app pattern row to
   `catalog/patterns.md`: a first session reachable within a
   minute, one recommended session on the home screen, a large
   play and pause control with a progress ring and a skip-back
   control, a sleep timer with a fade-out, and a dark sleep
   screen — distinct from the sleep timer row, which times a
   single session's end rather than guiding a practice, and from
   the habit streak row, which rewards repetition rather than a
   single guided session. Sources so far are an app-store
   listing, single-designer case studies, and template pages
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates.

361. Extend the Wearable interfaces row in
   `catalog/interfaces.md` with sensitive-notification reveal
   rules once a platform or standards source surfaces: a
   sensitive notification first arrives as a generic haptic with
   the sender only, and its content is revealed only on a
   deliberate gesture on the watch, with a per-app preview
   control on the phone — distinct from the notification
   preferences row, which chooses which alerts arrive rather
   than how much they reveal on the wrist. Sources so far are
   content-site guides only; a platform or standards source is
   still needed before the row is extended. Done when the
   extended row passes all quality gates.

362. Add a conversational companion safeguards for minors pattern
   row to `catalog/patterns.md`: a companion that holds a
   conversation with a minor keeps memory of past chats off by
   default, avoids designs that foster emotional dependence, and
   offers a plain route to a person — distinct from the
   conversational-interfaces trend notes, which cover general
   voice and chat design, and from the guardian approval request
   row, which approves one item at a time. Sources so far are a
   2026 proposal on children's online safety and adopted
   minors-safety guidelines, which mention safeguards around
   conversational companions, only; no platform documentation,
   standards source, or peer-reviewed study on companion
   behaviour itself has been found. Done when the row passes all
   quality gates.

363. Add a spending controls for minors pattern row to
   `catalog/patterns.md`: caps, cooling-off steps and plain
   spending statements on purchases and paid chance items inside
   a service used by minors, with guardian visibility —
   distinct from the guardian approval request row, which
   approves one item at a time, and from the supervised usage
   limits row, which caps time rather than money. Sources so
   far are proposal texts covering economic transactions and
   paid chance items, per secondary summaries, only; no platform
   documentation or standards source on the controls themselves
   has been found. Done when the row passes all quality gates.

364. Add a car wash booking and membership pattern row to
   `catalog/patterns.md`: book a wash or a full detail, or hold
   a recurring unlimited plan tied to one vehicle, with gate
   entry by plate recognition and a stated cancellation route —
   distinct from the car rental and car sharing booking row,
   which covers hiring a vehicle, and from the parking session
   payment row, which covers a stay rather than a plan tied to
   one vehicle. Sources so far are a university thesis on
   registration for a car wash service application and platform
   and regulator rules for the payment leg only; no platform or
   standards source for the booking flow itself has been found.
   Done when the row passes all quality gates.

365. Add a fantasy sports app pattern row to
   `catalog/patterns.md`: a live draft room showing whose pick
   is next, the pick clock, roster positions and the available
   player list at once, with snake order, position limits and
   an automatic pick on a missed turn; a squad built under a
   credit cap with role constraints and captain multipliers,
   locked once play starts; and leaderboards with rank movement,
   trade proposals and a watchlist — distinct from the live
   auction bidding row, which sells one lot at a time rather
   than drafting a season squad, and from the live activity row,
   which follows one event rather than a season of fixtures.
   Sources so far are an agency case study with a live draft
   room, a single-designer case study, a hiring brief, a vendor
   product update and a 2010 patent only; no platform or
   standards source for the draft-room and squad rules has been
   found. Done when the row passes all quality gates.

366. Add a house moving and removals booking pattern row to
   `catalog/patterns.md`: a room-by-room inventory with photos
   or a video survey, a quote sent for approval before any crew
   is dispatched, a deposit to hold the date, and a week-by-week
   checklist to moving day with crew and van scheduling —
   distinct from the appointment management row, which books a
   time rather than a priced move, and from the delivery slot
   picker row, which chooses a window rather than a quote.
   Sources so far are an app-store listing, a white-label
   marketplace page, vendor software pages and an agency case
   study only; no platform or standards source for the
   inventory-to-quote flow has been found. Done when the row
   passes all quality gates.

367. Add a baby feeding and sleep tracking pattern row to
   `catalog/patterns.md`: one-tap logging usable with one hand,
   a today-first view with time since the last feed visible,
   layered cards per activity type, trends as graphs and lists,
   a night-friendly dark mode, and caregiver sharing with
   offline access — distinct from the sleep and rest data row,
   which records one person's sleep rather than a baby's day,
   and from the medication reminder row, which schedules doses
   rather than logging care as it happens. Sources so far are a
   vendor design article, single-designer product pages,
   app-store listings and a 2025 academic paper on engagement
   patterns in baby tracker apps only; no platform or standards
   source for the logging flow has been found. Done when the row
   passes all quality gates.

368. Add a children's pocket money and allowance pattern row to
   `catalog/patterns.md`: a weekly allowance per child, chores
   with photo proof and parent approval before any reward is
   recorded, visual savings goals, age-adapted views, and
   spending requests that need a parent's approval — distinct
   from the spending controls for minors row, which caps money
   inside a service, and from the supervised usage limits row,
   which caps time rather than money. Sources so far are vendor
   product pages and app-store listings, with a 2024 academic
   feature analysis of child finance apps, only; no platform or
   standards source for the allowance and approval flow has been
   found. Done when the row passes all quality gates.

369. Add a tradesperson and plumber booking pattern row to
   `catalog/patterns.md`: find a local verified tradesperson by
   reviews and past work, describe the job in a questionnaire with
   photos, receive a quote to accept or reject, and follow the visit
   with on-site check-in and photos, quotes compared side by side with
   what each covers, an arrival window stated with a message if it
   slips, and a stated guarantee and complaint route after the work —
   distinct from the appointment management row, which books a time
   without the verification and quote steps, and from the home
   cleaning service booking action, which covers a repeatable service
   rather than a one-off repair. Sources so far are vendor blogs and a
   marketplace guide only; no platform or standards source for the
   find-describe-quote-visit flow has been found. Done when the row
   passes all quality gates.

370. Add a restaurant table reservation pattern row to
   `catalog/patterns.md`: location, party size, date and time first,
   bookable slots on every result, a short booking form with only what
   the restaurant needs, confirmation with reminders, and a stated
   route when the night is full, a confirmation that states the hold
   length and the change-or-cancel route, a stated deposit where one
   is taken with its refund rule, and a no-show rule stated before
   booking — distinct from the restaurant online ordering row, which
   orders food rather than booking a table, and from the appointment
   management row, which books a person's own appointment rather than
   a table for a party. Sources so far are a wireframe template
   rebuilding one operator's screens, a single-author guide, a vendor
   agency guide, and a single-author guide citing store payment
   policies for deposits only; no platform or standards source for the
   reservation flow has been found. Done when the row passes all
   quality gates.

371. Add a food delivery courier/driver app pattern row to
   `catalog/patterns.md`: an offer card showing payout, distance,
   and pickup and drop-off points with an accept timer, a
   multi-stop task queue in delivery order, route guidance that
   suggests rather than dictates, earnings shown net of fees and
   tips, photo proof of delivery at the door, and a report-issue
   route from the active delivery screen — distinct from the ride
   booking row, which moves a passenger rather than a parcel,
   from the order tracking row, which follows an order from the
   customer side, and from the parcel sending and courier booking
   action, which books a courier rather than working as one.
   Sources are the platform-work directive and the regulator
   driver-distraction safety guidance. Done when the row passes all
   quality gates. (Implemented this run.)

372. Add a wedding invitation RSVP pattern row to
   `catalog/patterns.md`: one link per household opening a private
   invitation page, a reply per household with a name for each
   additional guest, a meal choice per guest, a stated reply deadline
   with reminders to those who have not answered, and a route to
   change a reply on the same link, with no account needed to respond,
   the invitation with the date, venue, and schedule shown first,
   attending, maybe, and declining answers, and the consequence of
   changing a reply stated — distinct from the invitation response
   row, which records one person's accept, decline, or tentative
   answer, and from the meeting and event creation row, which creates
   an event rather than collecting replies to one. Sources so far are
   vendor guides and an app-store listing only; no platform or
   standards source for the invitation-to-reply flow has been found.
   Done when the row passes all quality gates.

373. Add a water utility bill payment pattern row to
   `catalog/patterns.md`: a multi-service hub by address, balance,
   account number and last payment shown before commitment,
   per-service reminders, paid and unpaid tabs, partial payments,
   meter-reading history behind the bill, and usage analytics, usage
   compared with the previous period so a change is explained, a
   meter-reading submission route beside the bill, with a plausibility
   check on the reading where the bill rests on it, a stated route to
   dispute a charge with the response time named, and the receipt
   issued at once with the payment reference kept beside the bill —
   distinct from the bill explanation row, which
   explains one bill line by line, from the billing overview row,
   which shows what a customer pays, and from the home energy usage
   dashboard row, which shows energy use rather than bills across
   services. Sources so far are an agency case study, a
   single-designer case study, a low-quality content-site article,
   vendor documentation, an app-store listing and a designer portfolio
   only; a platform or standards source is still needed before the row
   is written. Done when the row passes all quality gates.

374. Add a pregnancy tracking pattern row to
   `catalog/patterns.md`: a week-by-week timeline, kick counter,
   contraction timer, symptom and mood logging, preparation
   checklists, partner access, keepsake export, and explicit
   not-medical framing throughout — distinct from the period and
   fertility tracking row, which tracks cycles rather than a
   pregnancy, from the sleep and rest data row, which records rest
   rather than pregnancy progress, and from the mental health
   journaling and mood tracking row, which covers self-guided mood
   tracking rather than pregnancy. Sources so far are regulator
   guidance on device software in general, a health record
   standard for providers, a single-platform support page,
   generic health-app assessment frameworks, and single-app
   product pages only; a pregnancy-specific platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates. Re-checked this run (deep editorial
   2026-11-20): a single-designer case study restates the
   week-by-week structure and adds one finding — the absence of a
   graceful path when a pregnancy ends — which belongs to new action
   428; the row stays open.

375. Add a restaurant waitlist management pattern row to
   `catalog/patterns.md`: a host-side waitlist with a floor map,
   party tags for preferences, server distribution, place
   confirmation with a deadline, and a leave action — distinct
   from the waitlist row, which covers joining a waitlist as a
   customer, from the high-demand queue row, which queues for
   scarce stock rather than tables, and from the appointment
   standby list row, which holds a standby place for one person's
   appointment rather than a party's table. Sources so far are a
   single-designer usability study of one waitlist product, a
   vendor audit, a studio blog and student certificate projects
   only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates.

376. Add a concert and festival ticket booking pattern row to
   `catalog/patterns.md`: a choice of seating arrangement —
   general admission, zoned, or reserved — section, row, and seat
   names identical on the chart, the ticket, the confirmation, and
   the venue signage, restricted-view seats labelled and priced
   accordingly, a seat hold with a stated expiry, a high-demand
   queue showing the place in line with the place kept on refresh,
   the total kept visible above the payment action, and a QR
   e-ticket — distinct from the train ticket booking row, which
   books a seat on a timetabled service, from the museum
   timed-entry ticket booking row, which books an entry slot
   rather than a seat, and from the pass and ticket display row,
   which shows a ticket already held rather than buying one.
   Sources so far are a system-design tutorial on seat holds and
   queues, a single-designer best-practices document, vendor
   seating-chart and seat-map guides, and an agency ticketing
   page only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates.
   (Implemented this run: new pattern row in `catalog/patterns.md`,
   grounded in regulator price-transparency guidance, the sector
   ticket-selling code, and trading-standards guidance.)

377. Add a dentist appointment booking pattern row to
   `catalog/patterns.md`: treatments named in patient words with
   durations, a slot picker showing the next few days with the
   first available first, a details form after the slot is chosen,
   guest booking without a forced account, a confirmation that
   works as a working document with add-to-calendar, and two
   reminders carrying a one-tap reschedule link — distinct from
   the veterinary appointment booking row, which books care for
   an animal rather than a patient, from the blood donation
   appointment booking row, which settles eligibility and
   donation type before the visit, and from the appointment
   management row, which manages appointments already booked
   rather than booking a treatment. Sources so far are a
   feedback-platform content series, an agency
   mobile-patient-journey guide, and a single-designer
   multi-clinic booking case study only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates.

378. Add an online tutoring live class pattern row to
   `catalog/patterns.md`: three roles with distinct interfaces —
   student, tutor, and parent — a teacher-controlled room with
   muting, an ordered hand-raise queue, and promotion to the
   stage, a shared whiteboard centre-stage with every stroke
   mirrored live, class and lecture layouts fixed at creation, a
   student lobby with admission, and a recording that captures
   the board — distinct from the online course lesson player row,
   which plays recorded lessons with progress rather than a live
   room, from the language learning lesson row, which teaches one
   lesson rather than running a live class, and from the live call
   controls row, which covers call controls without classroom
   roles and moderation. Sources so far are vendor software-kit
   tutorials, an agency tutor-app guide, a content-site
   classroom-design piece, and three vendor tutoring platforms
   with tightly convergent rules — per-role dashboards for
   student, tutor, and parent, rescheduling proposed and
   approved in one tap, lesson recording only with the
   student's consent, a child studying without their own email
   through the parent's account, and a lesson balance showing
   who has paid and who owes; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.

379. Add a ferry booking pattern row to `catalog/patterns.md`: book a
   sailing with or without a vehicle — route and sailing chosen with
   the vehicle length and height stated, foot-passenger and vehicle
   options kept distinct, a cabin or seat choice where offered,
   vehicle details and the check-in window stated before payment,
   amendments and cancellations with a stated fee and cut-off, and a
   confirmation naming the sailing, the vehicle booked, and the
   arrival time — distinct from the train ticket booking row, which
   books a seat on a timetabled service, and from the pass and ticket
   display row, which shows a ticket already held. Merged with action
   311 this review; the combined row carries both actions' substance.
   Sources so far are a single-operator travel-information page,
   aggregator help pages, and a vendor help centre only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates. (Implemented through 403.)

380. Add a theme park virtual queue reservation pattern row to
   `catalog/patterns.md`: join a virtual queue for an attraction — one
   active reservation at a time, the party size stated, a boarding
   group with a stated return window shown with the live wait beside
   it, a day view of reserved return times in time order, per-person
   eligibility checked before joining, a plain route to leave the
   queue that releases the place at once, a plain notice where the
   return time moves, and an accessible queuing route for guests who
   cannot stand in a physical queue with the same wait as the standard
   queue — distinct from the high-demand queue row, which orders
   access to a scarce item, and from the appointment standby list row,
   which holds a place for a booked service. Merged with action 319
   this review; the combined row carries both actions' substance.
   Sources so far are a single-operator accessibility page, a vendor
   queue-design article, and a content-site guide only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates. (Implemented through 408.)

381. Add a video doorbell visitor interface pattern row to
   `catalog/patterns.md`: answer the door from a phone — a loud
   indoor chime with a large visitor picture, a live view with
   two-way talk, a head-to-toe view showing the visitor and any
   parcel, a stated choice of what to say to a courier with
   one-action preset replies, a recording kept with a stated
   retention, an event history with a stated retention rule, and
   a plain route to ignore a caller without opening the door —
   distinct from the incoming call row, which handles a phone
   call, and from the live call controls row, which covers call
   controls without a visitor at a door. Merged with action 306
   this review; the combined row carries both actions' substance.
   Sources so far are a vendor blog, a manufacturer product page,
   and patents only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates.

382. Extend the Agent checkpoint row in `catalog/patterns.md`
   with tiered permission gates and batch approval: three tiers
   with distinct visuals — read actions proceed without a prompt,
   write actions ask once per session per scope with an
   always-allow choice, destructive actions ask every time with
   no always-allow — and same-tier actions grouped into one
   approval surface with a scrollable checklist and one approve
   action, while destructive items always surface alone —
   cross-checked against the confirmation row and the
   autonomy-budget rule in the same row. Sources so far are a
   single-author pattern library and research write-ups only; a
   platform or standards source is still needed before the
   extension is written. Done when the extended row passes all
   quality gates.

383. Add an appliance and device repair booking pattern row to
   `catalog/patterns.md`: a diagnostic fee stated at booking and
   credited toward the repair when approved, appliance, brand,
   and symptoms captured up front with photos and error codes,
   the repair priced on site after diagnosis with repair-or-
   replace options on one quote, no work before the quote is
   approved, parts lead time stated with the return visit booked
   before the technician leaves, and a warranty on the repair
   stated at approval — distinct from the tradesperson and
   plumber booking row, which finds a local tradesperson rather
   than booking a diagnosis and repair, from the home cleaning
   service booking row, which books a repeatable service rather
   than a diagnosis, and from the appointment management row,
   which manages appointments already booked rather than booking
   a repair visit. Sources so far are vendor software pages and
   an app-builder guide only; a platform or standards source is
   still needed before the row is written. Done when the row
   passes all quality gates.
   (Implemented this run: new pattern row in `catalog/patterns.md`,
   grounded in the repair-of-goods directive summary, the statutory
   right to repair, and the ecodesign spare-parts rules; the
   fee-credit clause was dropped as ungrounded.)

384. Add a home care visit booking pattern row to
   `catalog/patterns.md`: a request naming the help needed and
   the days, an assessment visit booked before any regular
   schedule, care needs and routines captured at the assessment,
   recurring visits with a named carer and stated windows, a care
   plan and visit notes the family can follow through a
   permission-controlled view, medication and task records kept
   with the visit, and a plain route to raise a concern —
   distinct from the childcare booking row, which books care for
   a child rather than support at home, from the tradesperson and
   plumber booking row, which books one-off trade work rather
   than recurring care, and from the appointment management row,
   which manages appointments already booked rather than booking
   a care visit. Sources so far are vendor care-software pages,
   an app-builder guide, a vendor launch notice, and three vendor
   scheduling pages with tightly convergent coordinator-side
   rules — a client-centred week view, recurring visits as one
   run, conflict detection, preferred-carer matching, and a draft
   and publish workflow; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates.

385. Add a ticket resale listing pattern row to
   `catalog/patterns.md`: list a ticket for resale with the
   original event, date, seat or standing area, and entry terms
   carried over unchanged, price it with the face value shown
   beside the asking price and any fee stated before listing, keep
   the listing live only while the ticket is still held, transfer
   the ticket to the buyer at sale with the entry code reissued,
   and refund the buyer in full where the event is cancelled —
   distinct from the pass or ticket transfer row, which moves a
   ticket to a named person without a sale, and from the concert
   and festival ticket booking row, which buys a ticket from the
   seller rather than reselling one. Sources so far are
   trading-standards guidance on the sale and resale of tickets
   and three vendor ticketing platforms with tightly convergent
   rules — resale at face value with the fee stated before
   listing, a fee of ten percent of the price originally paid,
   the old entry code voided and a new one issued at sale, a
   waitlist with a time-limited hold, and add-ons travelling
   with the ticket unless withheld; a second platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates.

386. Add a repair information form pattern row to
   `catalog/patterns.md`: present the pre-repair form before any
   repair contract is signed — the repairer, the work, the cost,
   and the time stated plainly, the form given free and valid for
   at least 30 days, the price and time fixed for that period, and
   a plain route to accept or decline without losing the form —
   distinct from the appliance and device repair booking row,
   which books the repair visit rather than stating the
   pre-contract terms, and from the warranty claim row, which
   claims a remedy rather than stating repair terms in advance.
   Sources so far are the repair-of-goods directive summary only;
   a second platform or standards source is still needed before
   the row is written. Done when the row passes all quality
   gates.

387. Add a recurring scheduled grocery order pattern row to
   `catalog/patterns.md`: place a grocery order once that repeats
   on a schedule — the basket and delivery slot chosen for each
   repeat, substitutions stated per repeat with a plain route to
   change them, a reminder before each repeat with a pause, skip,
   or change route before the cut-off, and the price re-checked at
   each repeat with any change stated before the order is placed —
   distinct from the subscribe-and-save purchase option row, which
   repeats one product purchase rather than a whole basket, from
   the reorder past order row, which repeats a previous order once
   rather than on a schedule, and from the delivery slot picker
   row, which chooses one slot rather than a repeating slot.
   Sources so far are vendor help documents and marketing pages
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates.

388. Add a smartwatch sensitive-notification reveal pattern row to
   `catalog/patterns.md`: a notification on a watch worn in public
   shows only that something arrived until the wearer asks for more —
   message content, sign-in codes, and health details stay hidden
   behind a tap or an unlock, the watch locks the moment it leaves
   the wrist, and each app's notification access is stated and
   changeable — distinct from the notification preferences row,
   which chooses which updates arrive, and from the app lock row,
   which locks the whole app rather than hiding one notification.
   Re-checked 2026-11-23: guides to wearable notification-privacy
   settings across several systems converge on the same rules — tap
   to reveal the full notification, summary only while locked,
   per-app sensitivity, and nothing shown on wrist-down — and the
   rules in this action already state them; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates.

389. Extend the order tracking row in `catalog/patterns.md` with
   pickup wait-time rules: a pickup order states its expected
   ready time at checkout, sends a ready notification when the
   order is ready, and states a revised time with the reason when
   the wait moves, with a stated handoff window from arrival to
   handover — cross-checked against the drive-through and curbside
   pickup row (action 252) and the delivery slot picker row. Done
   when the extended row passes all quality gates.

390. Extend the appointment management row in `catalog/patterns.md`
   with a multi-person, multi-day booking rule: book for several
   people across several days in one action, with availability
   shown by day, per-person pricing shown before confirming, and a
   stated effect when one person's slot becomes unavailable after
   the rest are held — distinct from the recurring appointment
   series row, which repeats one booking rather than booking
   several people at once, and from the shared resource booking
   row, which books a shared place rather than people's times.
   Sources so far are an agency case study of on-demand childcare
   booking, recorded as a new source record. Done when the extended
   row passes all quality gates.

391. Add a school homework assignment tracking pattern row to
   `catalog/patterns.md`: one dashboard across the child's
   portals, a per-child week view filtered by type, big
   assignments split into steps, and an evening reminder of
   tomorrow's work — requires a platform or standards source
   before the row is written. Done when the row passes all quality
   gates.

392. Add a worked mobile banking example under
   `examples/mobile-banking/`: a worked example demonstrating
   device-check sign-in, balance with one next action, a payment
   with a recipient-name check, a card freeze, and a fraud alert,
   with all seven states — distinct from the worked checkout
   example, which covers one purchase rather than account
   management. Done when the example passes all quality gates.

393. Extend the Emergency assistance request row in
   `catalog/patterns.md` with total-conversation rules: voice,
   real-time text, and video in one session where the interface
   touches emergency contact, a stated route where voice is not
   possible, and a session kept live until help confirms —
   cross-checked against the EN 303 919 note in
   `trends/2026/standards-outlook.md`. Done when the extended row
   passes all quality gates.

394. Add a parcel sending and courier booking pattern row to
   `catalog/patterns.md`: quote by size, weight, and distance
   before booking, label route with a print or code option,
   drop-off point choice, pickup-code handover, live tracking, and
   proof of delivery — distinct from the return label and drop-off
   row, which returns a purchase rather than sending a parcel, and
   from the order tracking row, which follows a placed order
   rather than creating a shipment. Sources so far are vendor
   guides and app-store listings only; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates. (Implemented this run.)

395. Add a laundry pickup and delivery pattern row to
   `catalog/patterns.md`: pickup window rather than an exact
   minute, access notes for the driver, per-pound pricing with the
   weighing basis stated, weighed versus itemised handling, staged
   status through processing, and reschedule or cancel — distinct
   from the delivery slot picker row, which books a delivery
   window for goods, and from the order tracking row, which
   follows a placed order rather than a service in progress.
   Sources so far are vendor pages, a vendor blog, app-store
   listings, and a design-gallery concept only; a platform or
   standards source is still needed before the row is written.
   Done when the row passes all quality gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: a laundry-app feature guide, a customer, driver, and admin feature guide, and a booking case study.)

396. Add a digital parking permit application pattern row to
   `catalog/patterns.md`: permit linked to the vehicle
   registration number with no physical display, proof of
   residency and vehicle-keeper documents, expiry reminders before
   the permit ends, visitor permits, same-day issue where no
   documents are needed, and a stated route without internet
   access — distinct from the parking session payment row, which
   pays for a timed stay, and from the vehicle registration
   renewal and car tax payment row, which renews the vehicle
   record rather than a parking permission. Sources so far are
   council service pages only; a platform or standards source is
   still needed before the row is written. Done when the row passes
   all quality gates. (Implemented this run.)

397. Add a childcare booking pattern row to `catalog/patterns.md`:
   book sessions by room and age group with capacity shown, a
   waitlist that fills cancelled places in order, settling-in and
   show-round bookings before a regular place, funded-hours and fee
   splitting shown on the invoice, and a stated cancellation and
   rescheduling notice period — distinct from the appointment
   management row, which manages appointments already booked, and
   from the school admissions application portal row, which applies
   for a school place rather than booking care sessions. Sources so
   far are vendor scheduling-platform pages and a parent-app guide
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates. (Implemented this run.)

398. Add a gym and fitness class booking pattern row to
   `catalog/patterns.md`: booking window with the opening time
   stated, class capacity shown with a waitlist that promotes in
   order, free-cancellation cutoff with the late-cancel and no-show
   fee stated at booking, and a stated minimum-attendance rule for
   the class to run — distinct from the appointment management row,
   which manages appointments already booked, and from the
   appointment check-in row, which confirms arrival rather than
   booking the class. Sources so far are vendor blogs and platform
   pages only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality gates. (Implemented this run.)

399. Add a public library borrowing pattern row to
   `catalog/patterns.md`: holds with a place in line and a pickup
   window that expires, automatic renewal where no one is waiting
   with the blockers stated, a stated loan period per format with
   automatic return for digital loans, and a digital library card
   with fines and fees shown — distinct from the saved-item
   collection row, which saves items without borrowing them, and
   from the e-reader and reading app row, which covers reading
   rather than borrowing. Sources so far are library-system pages
   and platform app guides only; a platform or standards source is
   still needed before the row is written. Done when the row passes
   all quality gates. (Implemented this run.)

400. Add a dating app profile and matching pattern row to
   `catalog/patterns.md`: profile creation with prompts and photo
   order, discovery by swipe, browse, or curated picks, mutual-interest
   matching with a first-message prompt, verification badge, and block
   and report within two taps — distinct from the conversation
   branching row, which branches a chat rather than matching two
   people, and from the verified account badge row, which marks an
   account rather than building a profile. Sources so far are agency
   design guides only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: a dating-app design guide, a matching and chat guide, and a 2026 pattern roundup.)

401. Add a hot-desk and co-working booking pattern row to
   `catalog/patterns.md`: floor-plan and list views of free desks, desk
   filters by equipment and area, day-pass and hourly booking,
   colleague finder, and door access tied to the booking — distinct
   from the shared resource booking row, which books a shared resource
   rather than a desk in a shared space, and from the meeting and event
   creation row, which books a room for a meeting rather than a desk
   for a day. Sources so far are vendor platform pages and
   documentation only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. (Implemented this run: new pattern row in `catalog/patterns.md`, grounded in three new source records: a government booking design-patterns document, a booking-engine case study, and a workplace booking redesign case study.)

402. Add a home cleaning service booking pattern row to
   `catalog/patterns.md`: service menu with standard, deep, and
   move-out cleans, home-size intake that sets duration and price,
   recurring cadence chosen at booking, access notes carried forward,
   and a stated cancellation cutoff with the fee shown — distinct from
   the recurring appointment series row, which repeats an appointment
   rather than setting a cleaning cadence with access notes, and from
   the appointment management row, which manages appointments already
   booked. Sources so far are vendor scheduling-software pages only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Superseded by
   294: the same row specified twice, and 294 carries the fuller
   specification.

403. Add a ferry booking pattern row to `catalog/patterns.md`:
   route choice with the nearest terminal and landmarks shown, fare
   types grouped by traveller and pass with the price beside each,
   schedule and travel time visible before ticket selection, tickets
   bought and held inside the app rather than through an external
   redirect, and vehicle size asked in plain words with the effect
   stated — distinct from the train ticket booking row, which books
   a rail journey with reserved seats, and from the public transport
   ticket purchase row, which buys a ticket for a scheduled urban
   service rather than a ferry crossing with vehicle options.
   Sources so far are ferry-app design critiques and a moderated
   usability study of a ferry app, recorded as new source records; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

404. Add a volunteer shift signup pattern row to
   `catalog/patterns.md`: open shifts browsed by time or by role with
   places left shown, shift detail naming the meeting point,
   preparation, and who to ask for, a request that stays a request
   until confirmed rather than becoming a confirmed place, a
   commitments view with the cancellation effect shown before
   cancelling, and day-of check-in with approved hours — distinct from
   the appointment management row, which manages appointments already
   booked, and from the group scheduling poll row, which picks a time
   rather than filling shifts. Sources so far are a volunteer
   shift-scheduling guide and a signup-sheet guide, recorded as new
   source records; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates. Superseded by 332: the same row specified twice, and 332
   carries the fuller specification.

405. Add a weather app interface pattern row to
   `catalog/patterns.md`: one answer at the top — current
   temperature, condition, and the day's range — with the next
   decision one step down, hourly and daily views matched to the
   next decision, observed conditions, nowcasts, forecasts, radar
   estimates, and alerts kept visibly distinct with their freshness
   stated, and uncertainty shown where the forecast is unsure rather
   than a confident number — distinct from the data visualisation
   row, which charts data in general rather than answering what it
   is like outside, and from the notification preferences row, which
   chooses which updates arrive rather than presenting a forecast.
   Sources so far are a weather-app design guide and a
   weather-dashboard pattern review, recorded as new source records;
   a platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Merged into action 348 (weather app interface): the same substance now sits in action 348, which carries the row. (Implemented this run with action 348.)

406. Add a government citizen services portal pattern row to
   `catalog/patterns.md`: services organised by the task the
   resident needs to complete rather than by department, eligibility
   and what is needed stated before starting, a transaction begun
   before account creation with saving offered where it helps, plain
   language labels with help on where to find each answer, a visible
   progress indicator with save-and-return on long forms, and errors
   that explain the fix rather than only naming the problem —
   distinct from the government document application row, which
   files one document rather than gathering many services, and from
   the tax filing row, which completes one filing rather than
   routing many services. Sources so far are civic design guides
   and a citizen-portal best-practices guide, recorded as new source
   records; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality gates. Merged into action 347 (government citizen services portal): the same substance now sits in action 347, which carries the row. (Implemented this run with action 347.)

407. Add a smart home security camera pattern row to
   `catalog/patterns.md`: one calm live view that ranks the urgent
   information first, alerts ordered by severity with the place, the
   time, and the next step beside each, live previews inside the
   alert rather than a jump to another screen, a clear armed and
   disarmed state with a two-step arm that cannot trigger by
   accident, and recording and sharing controls that state plainly
   what is kept, where it is kept, and who can see it — distinct
   from the smart home dashboard row, which gathers many device
   types rather than answering a security alert, and from the smart
   lock guest access row, which grants entry rather than watching a
   property. Sources so far are a home security app concept, a
   security dashboard case study, and a privacy-focused surveillance
   redesign, recorded as new source records; a platform or standards
   source is still needed before the row is written. Done when the
   row passes all quality gates. (Implemented this run.)

408. Add a theme park virtual queue reservation pattern row to
   `catalog/patterns.md`: a return time held for a ride with the
   wait stated in plain words, live wait times beside each
   attraction on the map and in the list, a day plan that keeps
   reservations, return windows, and dining in time order, a change
   or cancel path that frees the place for another guest, and a
   stated rule for what happens when the park loses signal —
   distinct from the concert and festival ticket booking row, which
   sells a seat for one event rather than holding places across a
   day, and from the high-demand queue row, which holds a place in
   line for a purchase rather than a return time for a ride.
   Sources so far are a theme-park app redesign audit, a virtual
   queue feature case study, and a park visit planning concept,
   recorded as new source records; a platform or standards source
   is still needed before the row is written. Done when the row
   passes all quality gates. (Implemented this run.)

409. Add a road toll and congestion charge payment pattern row to
   `catalog/patterns.md`: pay a charge for driving in a zone or on a
   road — the charge, the charging hours, and the payment deadline
   stated before payment, one-off payment by registration number
   without an account, an automatic payment option for regular
   drivers with the vehicles and payment method named, a plain
   warning against unofficial payment sites, and a penalty notice
   with the amount, the reduced amount for early payment, and the
   payment route — distinct from the vehicle registration renewal
   row, which renews a registration rather than paying for road use,
   and from the parking fine payment row, which pays a fine rather
   than a charge for driving. Sources so far are an official city
   transport authority payment guide and consumer payment guides; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

410. Add a student loan application pattern row to
   `catalog/patterns.md`: apply for a loan for study — eligibility
   and the borrowing limit stated before starting, the applicant,
   parent, or preparer route chosen first, a stated list of schools,
   documents asked for only when the step needs them, a review of all
   answers before submission, and a plain statement of the decision
   time, the repayment terms, and the counselling step before funds
   arrive — distinct from the university admissions application row,
   which applies for a study place rather than funding, and from the
   mortgage application row, which borrows against a property rather
   than for study. Sources so far are application-procedure guides
   only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates. (Implemented this run.)

411. Add a travel insurance purchase pattern row to
   `catalog/patterns.md`: buy cover for a trip — trip details and
   traveller ages first, plans compared side by side with price and
   cover limits in plain words, optional extras chosen explicitly
   with the price change shown, a summary of cover read before
   payment rather than price alone, and the policy documents and
   emergency contact issued at once with a stated claim window —
   distinct from the insurance claim submission row, which claims on
   a loss rather than buying cover, and from the flight search and
   booking row, which books travel rather than insuring it. Sources
   so far are vendor and comparison-site buying guides only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

412. Add a cinema ticket booking pattern row to
   `catalog/patterns.md`: film, cinema, and screening chosen in that
   order with the total price shown before payment, an interactive
   seat map with the screen marked and the best-view area named, a
   stated hold on chosen seats while payment completes, ticket types
   per seat with proof asked only where a discount needs it, and a
   stated refund and exchange cutoff with the route beside it —
   distinct from the concert and festival ticket booking row, which
   sells a seat for one event with a stage view rather than a screen
   with a marked best-view area, and from the seat selection row,
   which picks a seat in general rather than booking a screening.
   Sources so far are a cinema-chain booking FAQ and a
   ticket-reservation guide, recorded as new source records; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. (Implemented this run.)

413. Add a cruise booking pattern row to `catalog/patterns.md`:
   sailing, departure port, and cabin chosen in that order with the
   fare and what it covers stated before the deposit, cabin types
   compared with light, space, noise, and position named, optional
   extras priced per person per day with the break-even stated, a
   deposit that holds the place with the final-payment date beside
   it, and documents and embarkation steps listed before sailing —
   distinct from the flight search and booking row, which books a
   flight rather than a sailing with a cabin, and from the hotel
   booking row, which books a room for nights rather than a cabin
   with dining and excursions bundled. Sources so far are two
   cruise-booking guides, recorded as new source records; a platform
   or standards source is still needed before the row is written.
   Re-checked 2026-11-19: no regulator, platform, or industry-body
   guidance specific to cruise booking interfaces was found; operator
   terms and independent guides corroborate cabin, fare-inclusion,
   and cost structure, but deposit, cancellation, and add-on rules
   are operator-specific with no common standard — the row stays open
   pending a side-by-side comparison of operator terms.
   Done when the row passes all quality gates. Re-checked this run
   (deep editorial 2026-11-20): travel guides and operator content
   corroborate the cabin, fare-inclusion, and cost structure already
   recorded; the embarkation checklist material belongs to new action
   427; the row stays open.

414. Add a driving licence renewal pattern row to
   `catalog/patterns.md`: a reminder with the expiry date shown, the
   renewal route chosen first with the fee and the delivery time
   stated for each, a photo reused from a valid passport where one
   exists with a new-photo route beside it, changed details routed
   away from the online flow with the reason stated, and a medical
   declaration asked plainly with the consequence of not declaring
   named — distinct from the passport renewal row, which renews a
   travel document rather than a driving licence, and from the
   government document application row, which files one document
   rather than renewing a licence. Sources so far are the official
   renewal service page and a renewal guide, recorded as new source
   records. Done when the row passes all quality gates. (Implemented this run.)

415. Add a university admissions application pattern row to
   `catalog/patterns.md`: apply for a university place — course and
   institution choice with entry requirements stated before starting,
   qualifications and predicted grades entered once, a personal
   statement with a stated length and a plain-language guide,
   references requested directly from the referee, a stated decision
   window with the offer types explained, and a reply deadline with
   the consequence of missing it stated — distinct from the university
   course registration row, which registers for courses after
   admission rather than applying for a place, and from the school
   admissions application portal row, which applies for a school place
   rather than a university place. Sources so far are none; a platform
   or standards source is still needed before the row is written. Done
   when the row passes all quality gates. Superseded by 279: the same
   row specified twice, and 279 carries the fuller specification.

416. Add a council tax payment and discount application pattern row to
   `catalog/patterns.md`: pay a council tax bill and claim a discount
   or exemption — the bill with the band, the amount, and the
   instalment dates stated before payment, payment by instalment with
   the remaining balance after each payment, a discount or exemption
   check that asks only the questions that change the outcome, and a
   stated decision time with the revised bill issued at once —
   distinct from the vehicle registration renewal row, which renews a
   registration rather than paying a recurring bill, and from the
   benefits claim application row, which claims an entitlement rather
   than paying a bill with a discount. Sources so far are none; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Superseded by
   310: the same row specified twice, and 310 carries the fuller
   specification.

417. Add a meal kit delivery subscription pattern row to
   `catalog/patterns.md`: subscribe to a weekly box of meals — plan
   and box size chosen with the price per serving stated, a weekly
   menu with dietary filters and the swap deadline named, a skip or
   pause path that keeps the subscription, and a cancellation route
   that states the last delivery date — distinct from the grocery
   price comparison row, which compares prices rather than
   subscribing to a box, and from the subscribe-and-save purchase
   option row, which repeats a single product rather than a weekly
   menu. Sources so far are none; a platform or standards source is
   still needed before the row is written. Done when the row passes
   all quality gates. Superseded by 330: the same row specified
   twice, and 330 carries the fuller specification.

418. Add a restaurant table reservation pattern row to
   `catalog/patterns.md`: location, party size, date, and time chosen
   in that order with only times that fit a free table offered, a
   confirmation that states the hold length and the change-or-cancel
   route, a stated deposit where one is taken with its refund rule,
   and a no-show rule stated before booking — distinct from the
   restaurant online ordering row, which orders one meal at a time,
   from the restaurant waitlist management row, which queues walk-ins
   rather than booking a table, and from the hotel booking row, which
   books a room by the night rather than a table by the hour. Sources
   so far are vendor reservation guides only; a platform or standards
   source is still needed before the row is written. Done when the row
   passes all quality gates. Superseded by 370: the same row specified
   twice, and 370 carries the fuller specification.

419. Add a tradesperson and plumber booking pattern row to
   `catalog/patterns.md`: trade and job chosen first, the job
   described with photos where they help, quotes compared side by side
   with what each covers, an arrival window stated with a message if
   it slips, and a stated guarantee and complaint route after the work
   — distinct from the home cleaning service booking row, which books
   a repeatable visit rather than a priced job, and from the appliance
   and device repair booking row, which repairs one named device
   rather than quoting a job. Sources so far are none; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates. Superseded by 369: the same
   row specified twice, and 369 carries the fuller specification.

420. Add a salon and spa appointment booking pattern row to
   `catalog/patterns.md`: service, practitioner, date, and time chosen
   in that order with the duration and the full price stated before
   booking, a deposit or cancellation window stated where one applies,
   and a stated route to change or cancel with the consequence named —
   distinct from the veterinary appointment booking row, which books
   care for an animal rather than a person, and from the gym and
   fitness class booking row, which books a place in a class rather
   than a one-to-one appointment. Sources so far are none; a platform
   or standards source is still needed before the row is written. Done
   when the row passes all quality gates. Superseded by 359: the same
   row specified twice, and 359 carries the fuller specification.

421. Add a wedding invitation RSVP pattern row to
   `catalog/patterns.md`: reply to a wedding invitation — the
   invitation with the date, venue, and schedule shown first, a reply
   that needs no account and no app install, attending, maybe, and
   declining answers with plus-ones named at once, a stated reply
   deadline with a reminder before it, and a stated route to change
   the reply with the consequence named — distinct from the invitation
   response row, which answers a general invitation rather than a
   wedding with plus-ones and a meal choice, and from the wedding
   planning app, which plans the event rather than replying to an
   invitation. Sources so far are vendor invitation guides only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Superseded by
   372: the same row specified twice, and 372 carries the fuller
   specification.

422. Add a water utility bill payment pattern row to
   `catalog/patterns.md`: pay a water bill — the bill with the amount,
   the due date, and the meter reading behind it shown first, usage
   compared with the previous period so a change is explained, payment
   by card or direct debit with the receipt issued at once, a
   meter-reading submission route beside the bill, and a stated route
   to dispute a charge with the response time named — distinct from
   the road toll and congestion charge payment row, which pays for
   road use rather than a metered household supply, and from the
   energy tariff comparison and switching row, which compares tariffs
   rather than paying a metered bill. Sources so far are
   single-designer case studies and content-site guides only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Superseded by
   373: the same row specified twice, and 373 carries the fuller
   specification.

423. Add a service-provider booking intake pattern row to
   `catalog/patterns.md`: requests arrive through two paths — created
   by the provider for walk-ins and calls, and sent by customers
   through a message thread — both landing on one shared calendar; the
   provider approves or declines each request with a plain notice to
   the customer, reminders go out automatically before the visit, and
   a client history with per-client notes sits beside the calendar —
   distinct from the appointment management row, which manages
   bookings already made, and from the tradesperson and plumber
   booking row, which covers the customer side of finding and quoting
   a job. Sources so far are a single-designer concept case study and
   a single-vendor marketplace case study only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates.

424. Add a multi-role availability pattern row to
   `catalog/patterns.md`: one shared availability record that every
   role reads, with each role shown only its own small view —
   customers see nearby businesses with their next open times, owners
   see the day's bookings and what changed, staff see their own queue
   — slot rules enforced on the server so conflicts are impossible
   rather than unlikely, and an account asked for only once a slot
   worth booking has been found — distinct from the appointment
   management row, which manages one person's bookings, and from the
   shared resource booking row, which books one resource rather than
   showing the same availability to several roles. Sources so far are
   a single-vendor marketplace case study only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates.

425. Add a book-on-behalf pattern row to `catalog/patterns.md`: choose
   who the booking is for first — a household member, a child, a pet,
   or an extra driver — with each person's details and notes carried
   into the booking, one checkout covering every person booked, and a
   confirmation naming who each part is for — distinct from the
   household member management row, which manages members rather than
   booking for them, and from the group checkout row, which splits
   payment rather than booking for several people at once. Sources so
   far are a shipped-product portfolio piece, a single-designer
   concept case study, a single-designer concept, and an app-store
   listing only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality gates.

426. Add a volunteer shift cover and substitute request pattern row to
   `catalog/patterns.md`: a volunteer who cannot make a confirmed shift
   asks for cover from the shift itself, the request names the shift,
   the role, and the preparation already done, other qualified
   volunteers see the open cover with the same detail the original
   volunteer saw, the original volunteer is released only when a
   substitute confirms, and the coordinator is told at once with the
   roster updated — distinct from the volunteer shift signup row,
   which fills an open shift rather than replacing a confirmed
   volunteer, and from the appointment management row, which manages
   bookings already made rather than cover for a shift. Sources so
   far are single-vendor volunteer scheduling products only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.

427. Add a cruise embarkation and onboard check-in pattern row to
   `catalog/patterns.md`: a pre-sailing checklist completed at home —
   travel documents, health forms, and payment method verified before
   arrival — with each item shown as done or still needed, an arrival
   window stated with the terminal and what to bring, a fast-track
   lane for travellers whose checklist is complete, and onboard
   check-in that reuses what was already verified rather than asking
   again — distinct from the cruise booking row, which books the
   sailing and the cabin rather than preparing for boarding, and from
   the travel check-in row, which checks in for a flight rather than
   a sailing with documents verified in advance. Sources so far are
   travel guides and operator content only; a platform or standards
   source is still needed before the row is written. Done when the row
   passes all quality gates.

428. Add a sensitive lifecycle change in a health tracker pattern row
   to `catalog/patterns.md`: when a tracked condition ends, the
   tracker offers a plain route to record the change without demanding
   a status update first, stops reminders and week-by-week content at
   once, asks whether past entries are kept or deleted with the choice
   honoured without further prompts, and never shows celebratory
   content after the change — distinct from the pregnancy tracking
   row, which follows a pregnancy week by week, and from the account
   deletion row, which removes the whole account rather than closing
   one tracked condition. Sources so far are a single-designer case
   study and single-designer portfolio pieces only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates.

429. Add a split button primitive row to `catalog/primitives.md`: one
   primary action with an attached dropdown of related variants — the
   primary action is the most common and safe choice and fires at once,
   the dropdown holds two to five closely related variants, and the two
   halves are two real buttons in a labelled group, each with its own
   name and focus ring, the dropdown trigger named for what it opens; a
   persistent variant keeps the last chosen action as the new default
   and says so plainly — never use it where no action is primary, where
   the options are navigation, or where the variants are unrelated.
   Distinct from the Button group primitive, which holds related
   buttons of equal weight, and from the Overflow menu pattern, which
   gathers secondary actions with no primary action on the surface.
   Cross-check the Overflow menu row and the Button group primitive.
   Sources so far are two design systems, an accessibility guide citing
   published success criteria, an agency article, and a pattern guide; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.

430. Add a guardian falling-behind alert pattern row to
   `catalog/patterns.md`: when a child starts to fall behind, the
   guardian is told early, kindly, and with a next step — the alert
   names what changed, shows the same record the student sees, and
   offers one clear next step, such as viewing the missed work or
   contacting the teacher, rather than a bare warning; the guardian
   view stays glanceable on a phone, one account across several
   children, each mapped to a school and class; assignment status runs
   assigned, submitted, due, and returned with teacher feedback in one
   place. Distinct from the school homework assignment tracking row,
   which tracks assignments rather than telling a guardian early that
   a child is slipping, and from the notification escalation row, which
   raises the urgency of a message rather than opening a support route
   for a child. Sources so far are single-designer case studies and a
   vendor school-management product page only; a platform or standards
   source is still needed before the row is written. Done when the row
   passes all quality gates.

431. Add a bounded neighbourhood noticeboard pattern row to
   `catalog/patterns.md`: notices are filed as topics with flat
   chronological replies on a bounded, paginated board rather than an
   endless ranked activity stream — no reactions, ranking,
   recommendations, or "what you missed" machinery; a newer discussion
   can be prominent without older ones disappearing; heated or civic
   topics move to a separate opt-in room rather than being removed or
   downvoted; safety alerts stay prominent and recommendations stay as
   pages that persist rather than scrolling away. Distinct from the
   neighbourhood noticeboard row, which covers the board's topics and
   replies, and from the activity feed row, which lists past point
   events in a stream. Sources so far are a single-author development
   log, a single-vendor neighbourhood product page, and vendor blog
   posts only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality gates.

432. Add a recipient-side agent action pattern row to
   `catalog/patterns.md`: when an agent contacts a person on
   someone's behalf — an email, a booking, a purchase — the message
   names the person it acts for, states plainly that it was sent by
   an automated agent rather than by that person, gives a human
   contact and a way to reply to a person, and never presents the
   agent as the person; the recipient can see what was asked for and
   what was decided, and can refuse or redirect the request without
   going through the agent — distinct from the agent checkpoint row,
   which supervises the agent for the person delegating, and from the
   automated-to-human support handoff row, which hands a
   conversation to a person inside the same product rather than
   designing for a stranger receiving an agent's message. Sources so
   far are a single pattern guide (six patterns, v1, updated
   November 2026); a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates.

433. Add a free-agent pool placement pattern row to
   `catalog/patterns.md`: a person without a team joins a pool,
   states skill level and availability, and is placed on a team with
   open spots — the pool shows the wait and the placement rule before
   joining, the placement is confirmed with the team, the division,
   and the first fixture, and the person can leave the pool or turn
   down a placement without losing their place in line for the next
   one — distinct from the community sports league team registration
   row, which registers a whole team with a captain and a roster, and
   from the group scheduling poll row, which finds one time for a
   group rather than placing a person on a team. Sources so far are
   vendor league-registration guides only; a platform or standards
   source is still needed before the row is written. Done when the row
   passes all quality gates.

434. Add a multi-pet appointment booking pattern row to
   `catalog/patterns.md`: book services for several pets in one visit
   — each pet chosen with its own service and price, the total shown
   per pet and for the visit, the visit length set by the longest
   service with buffers between pets, and each pet's notes,
   temperament, and vaccination state carried into the appointment —
   distinct from the pet grooming appointment booking row, which books
   one appointment for one pet, and from the veterinary appointment
   booking row, which books care for an animal with a clinician
   rather than a set of grooming services for several pets. Sources
   so far are vendor scheduling product pages only; a platform or
   standards source is still needed before the row is written. Done
   when the row passes all quality gates.

435. Extend the Overflow menu row in `catalog/patterns.md` with
   user-customizable menu rules: the person can remove entries they
   never use, manage entries added by third-party extensions, and
   restore the default layout in one action; the menu states which
   entries are built in and which come from an add-on, and removing
   an entry never removes the underlying action, which stays
   reachable elsewhere — distinct from the profile and account menu
   row, which lists account actions rather than a customisable
   command set, and from the command palette row, which executes
   typed commands. Sources so far are secondary tech-news reports
   of a November 2026 desktop operating-system update only; a
   primary platform source is still needed before the rule is
   written, so implementation stays with the deep cycle. Done when
   the extended row passes all quality gates. (Implemented this run:
   the extended Overflow menu row now carries the customisable-menu
   rules, grounded in the platform release notes for the October 2026
   preview update, which the November 2026 security update includes,
   and a hands-on test of the November 2026 update; the one-action
   restore of the default layout has no platform source and is not
   in the row.)

436. Extend the Appointment management row in `catalog/patterns.md`
   with booking change-allowance rules: where a booking allows only
   a stated number of changes or moves, the booking itself shows
   how many changes remain and where a move may go before any
   change is attempted, and states the fee or forfeiture
   consequence of cancelling inside the cutoff — distinct from the
   order editing row, which changes a placed order rather than a
   booked time, and from the payment failure recovery row, which
   handles a failed payment rather than a change limit. Sources so
   far are a 2026 government booking-rules update stating the policy
   — only the named person books and manages, at most two changes,
   moves limited to nearby centres, a ten-full-working-day
   cancellation cutoff — with no interface rules, plus a
   single-designer redesign noting manual cancellation hunting; a
   platform or standards source is still needed before the rule is
   written. Done when the extended row passes all quality gates.
   Re-checked this run (deep editorial 2026-11-21): the government
   booking-rules guidance page now states the change-counting rules
   in full — changing the date, the centre, or swapping with another
   learner each counts as one change, changing several at once still
   counts as one, updating contact details does not count, and a
   change made by the agency resets the allowance to two — recorded
   as a new source record; the refund cutoff is ten full working days,
   corrected from three. A platform or standards source with interface
   rules is still needed before the rule is written, so the action
   stays open.

437. Extend the Payment failure recovery row in
   `catalog/patterns.md` with a discreet-decline rule for
   supervised payments: when a payment is declined on a supervised
   account — a child's card at a till, a shared household card —
   the decline is shown quietly to the payer only, without an alarm
   or a reason others nearby can read, and the detail goes to the
   supervising account instead — distinct from the spending controls
   for minors row, which caps money inside a service, and from the
   children's pocket money row, which covers the allowance and
   approval flow rather than the decline itself. Sources so far are
   two shipped-product case studies of one family-finance product
   and a vendor product page only; a second independent source is
   still needed before the rule is written. Done when the extended
   row passes all quality gates.

438. Extend the Accessibility preferences row in
   `catalog/patterns.md` with per-display magnification rules: where
   more than one display is in use, each display keeps its own zoom
   level with the magnified view staying inside that display, the
   view on one display can be locked in place while the pointer
   moves to another, and a contrast theme toggle sits on the
   magnification toolbar beside the colour-inversion control, with
   per-display zoom on by default and adjustable from the toolbar or
   the accessibility settings — distinct from the theme selection
   row, which chooses light, dark, or system-following colours for
   the whole interface rather than magnification per display, and
   from the live captions row, which follows spoken content as text.
   Sources so far are the platform release notes for the October 2026
   preview update, corroborated by hands-on tests of the November 2026
   update. Done when the extended row passes all quality gates.

439. Add a connected-device prompt pattern row to
   `catalog/patterns.md`: when a device such as a phone, camera, or
   removable drive is connected, offer the actions that fit that
   device in one dialog, keep the dialog usable with dark mode and
   larger text, and keep its notification in the notification centre
   so the person can return to it later rather than losing the offer
   when the dialog is dismissed — distinct from the device pairing
   row, which connects a new device rather than offering actions for
   one already connected, and from the notification list row, which
   lists messages rather than offering an action for a connected
   device. Sources so far are the platform release notes for the
   October 2026 preview update only; a second independent source is
   still needed before the row is written. Done when the row passes
   all quality gates.

440. Add a cloud device recovery pattern row to
   `catalog/patterns.md`: when the system cannot start, offer a
   reinstall from an image downloaded over the network with no
   physical media needed, reuse the saved network credentials so the
   device gets online during recovery without re-entering them, state
   the target build, edition, and language before anything is
   downloaded, and ask the person to confirm a data-loss warning
   with a choice to remove files or to remove and sanitise them
   before the reinstall begins — distinct from the account recovery
   row, which restores access to an account rather than reinstalling
   the system, and from the in-product update prompt row, which
   updates a working system rather than recovering one that cannot
   start. Sources so far are the platform release notes for the
   October 2026 preview update only; a second independent source is
   still needed before the row is written. Done when the row passes
   all quality gates.

441. Add an energy supplier account pattern row to
   `catalog/patterns.md`: the supplies on the account with contract
   status and meter identifiers, a guided meter-reading flow with a
   photo option and a plausibility check on the entered value,
   consumption shown as a chart with a comparison against a previous
   period, bills listed with payment state and downloadable detail,
   and an instalment forecast the person can adjust with the effect
   on the next payment stated — distinct from the home energy usage
   dashboard row, which shows usage for one home rather than managing
   the account, from the energy tariff comparison and switching row,
   which compares tariffs rather than managing a supply, and from the
   billing overview row, which lists charges rather than covering
   readings, consumption, and instalments together. Sources so far
   are a supplier app page, an agency guide, and two case studies; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.

442. Add a car insurance quote and purchase pattern row to
   `catalog/patterns.md`: one question per screen in named stages,
   the vehicle first and personal details later, every sensitive
   question explained where it is asked, answers shown as tappable
   options rather than typed where the choice is closed, a visible
   stage count with a time estimate, a save-and-resume route, and the
   full price with what it covers stated before payment — distinct
   from the insurance claim submission row, which reports a loss on a
   policy already held rather than buying cover, and from the travel
   insurance purchase row, which buys cover for one trip rather than
   quoting a vehicle policy. Sources so far are single-designer case
   studies only, two of them corroborating the one-question-at-a-time
   flow with tap-to-advance answers and easy-first ordering; a
   platform, standards, or regulator source is still needed before
   the row is written. Done when the row passes all quality gates.

443. Add a water utility bill payment pattern row to
   `catalog/patterns.md`: the account balance with the amount due and
   the due date stated up front, a meter-reading entry with a
   plausibility check where the bill rests on a reading, payment by
   the full amount or a chosen amount with the remaining balance
   stated, and a receipt with the payment reference kept beside the
   bill — distinct from the billing overview row, which lists charges
   rather than paying one bill, and from the home energy usage
   dashboard row, which shows usage rather than taking a payment.
   Sources so far are none; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. Superseded by 373: the same row specified twice,
   and 373 carries the fuller specification.

444. Extend the Medication refill request row in
   `catalog/patterns.md` with eligibility-before-button rules: one
   plain eligibility state per prescription — ready to request, too
   early until a named date, needs a new prescription, out of stock
   at this pharmacy, controlled fill in person or by phone, or an
   insurance issue with a short reason — with the rule stated in one
   line on the card, no primary refill action on a blocked
   prescription, and secondary actions instead such as a readiness
   notice, a renewal request, or a pharmacy change; order states
   answer what happened, what happens next, and whether the person
   must act; and the request list is revised so a blocked
   prescription stays visible on its card with its eligibility state
   and secondary actions, rather than appearing only in the history
   — distinct from the Medication reminder row, which reminds the
   person to take a dose, and from the Order tracking row, which
   follows a parcel rather than a prescription. Sources so far are a
   single-agency guide, a shipped-product case study, and a vendor
   product update only; a platform or standards source is still
   needed before the extension is written. Done when the extension
   passes all quality gates.

445. Extend the smart baby monitor app pattern row (action 357) in
   `catalog/patterns.md` with alert triage rules: urgent alerts —
   crying, movement, or a change in breathing — arrive at once with
   what changed and what to do, routine events such as sleep
   summaries and room-condition changes wait for a digest, each
   alert states its urgency in words rather than by colour alone,
   and a quiet-hours rule states plainly when it ends and which
   urgent alerts still break through — distinct from the
   notification preferences row, which sets channels and cadence
   for any topic, and from the notification escalation row, which
   raises the urgency of a message rather than sorting alerts by
   urgency. Sources so far are a single-designer case study, an
   award listing, and a vendor comparison site only; a platform or
   standards source is still needed before the extension is written.
   Done when the extension passes all quality gates.

446. Extend the online prize draw and raffle entry pattern row
   (action 302) in `catalog/patterns.md` with draw-transparency
   rules: the entry list is published before the draw, the draw
   method is stated with a verifiable trail, the winner is contacted
   by a stated route within a stated time with the fallback named
   where the winner does not reply, and the full terms are linked
   before entry — distinct from the limited-time offer countdown row,
   which times an offer rather than a draw, and from the
   crowdfunding campaign page row, which funds a project. Sources so
   far are a promoter's published draw terms and a draw operator's
   public entry list and draw-trail description only; a platform or
   standards source is still needed before the extension is written.
   Done when the extension passes all quality gates.

447. Add a university admissions application pattern row to
   `catalog/patterns.md`: the programme is chosen before any
   account is created, with its requirements shown in the flow for
   the applicant's qualification only, each section of the
   application carries its own status on a dashboard with one clear
   next action, the fee is a separate step that opens only once the
   form is in, drafts can be saved with only final submission
   enforcing the core requirements, and status is stated precisely
   — uploaded is not verified, submitted is not paid — distinct
   from the school admissions application portal row, which
   applies for a child's school place, and from the university
   course registration row, which registers for courses after
   enrolment. Sources so far are a single-designer case study and
   agency guides only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates. Superseded by 279: the same row specified twice,
   and 279 carries the fuller specification.

448. Add an airport self-service bag drop pattern row to
   `catalog/patterns.md`: the boarding pass is scanned to authorise
   the drop, the bag is weighed and measured with an overweight
   prompt offering repack or an excess-fee payment, the tag is
   printed and attached before the bag is placed, and a receipt
   with the tracking route closes the flow, with a staff route
   visible on every screen for anything that needs a person —
   distinct from the travel check-in row, which confirms travel
   and issues a pass, from the hotel self check-in row, which
   checks in for a stay, and from the self-checkout grocery kiosk
   row, which pays for groceries. Sources so far are vendor
   product pages only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates.

449. Add a home broadband installation and router setup pattern row
   to `catalog/patterns.md`: the phone joins the router's default
   network, a guided setup in the app or the browser detects or
   asks for the connection type, the Wi-Fi name, password, and
   security mode are set in one step, a summary with a connection
   test closes the setup, a firmware update is offered where one is
   available, and the route to reconnect existing devices is stated
   — distinct from the device pairing row, which pairs one device,
   and from the smart home dashboard row, which controls the home
   once it is set up. Sources so far are a vendor setup guide and
   content blogs only; a platform or standards source is still
   needed before the row is written. Done when the row passes all
   quality gates.

450. Add a council tax payment and discount application pattern
    row to `catalog/patterns.md`: the bill states the band, the
    yearly amount, and the instalment plan up front, eligibility
    for each discount is checked before the application starts so
    ineligible applicants are not asked for evidence, the
    application runs as a signed-in self-service task with a
    stated decision time, instalments already shown on the bill
    stay payable while the application is assessed, a successful
    application produces a revised bill with any refund stated,
    and a change of circumstances carries a stated reporting duty
    with its deadline and penalty — distinct from the government
    citizen services portal row, which organises many services
    into tasks, and from the water utility bill payment row, which
    explains a metered bill with usage comparison. Sources so far
    are council service pages only; a platform or standards
    source is still needed before the row is written. Done when
    the row passes all quality gates. Superseded by 310: the same
    row specified twice, and 310 carries the fuller specification.

451. Add a wedding registry and gift list pattern row to
    `catalog/patterns.md`: gifts are shown as cards with price,
    link, notes, and availability status, a guest reserves or
    claims a gift so the same item is not bought twice, the list
    is shared through one link with no account needed to view it,
    the couple adds and edits items in short tasks across devices,
    and a purchased gift stays visible as given with a thank-you
    route attached — distinct from the gift option row, which adds
    a gift message and wrapping to one purchase at checkout, and
    from the shared shopping list row, which coordinates household
    buying without reservations. Sources so far are a vendor
    tutorial, an agency case study of one registry service, and a
    single-designer project only; a platform or standards source
    is still needed before the row is written. Done when the row
    passes all quality gates. Superseded by 285: the same row
    specified twice, and 285 carries the fuller specification.

452. Add a pet adoption application pattern row to
    `catalog/patterns.md`: browsing needs no account, each pet
    profile states health records, vaccination status, and
    availability beside the shelter's verification mark, filters
    run on lifestyle and compatibility rather than looks alone, a
    meet-and-greet is booked from the profile with its time and
    place stated, and the steps, documents, and fees are explained
    before the application is started so the applicant knows what
    happens next — distinct from the veterinary appointment booking
    row, which books a visit for a pet already owned, and from the
    appointment management row, which tracks bookings already
    made. Sources so far are single-designer case studies only; a
   platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates. Superseded
   by 304: the same row specified twice, and 304 carries the
   fuller specification.

453. Add a book on behalf pattern row to `catalog/patterns.md`:
   book a service or appointment for another person — ask early
   whether the booking is for the person booking or for someone else,
   keep the booker and the attendee apart with the booker name and
   contact, the attendee name, the relationship, the confirmation
   contact, the on-the-day contact, and who may change or cancel
   stated separately, send the confirmation to the chosen contact,
   and show the booking in the attendee's record with a delegate or
   permission route where the attendee must approve — distinct from
   the appointment management row, which books the person's own
   time, and from the guardian approval request row, which approves
   an action for a minor rather than booking for another adult.
   Sources so far are vendor help pages and a vendor proxy-booking
   guide only; a platform or standards source is still needed before
   the row is written. Done when the row passes all quality gates.

454. Add a worked example for the tablet layout under
   `examples/tablet/`: a worked example demonstrating the tablet
   layout — width-band navigation switching from bottom bar to rail
   to permanent drawer, list-detail side by side at or above 600dp
   with a supporting pane at roughly a 70/30 split at expanded
   widths, orientation-change continuity that preserves scroll
   position, entered input, and selection, and posture-aware
   foldable arrangements that keep content clear of the crease —
   with all seven states shown. Done when the example passes all
   quality gates. (Implemented this run.)

455. Add a worked example for the landing layout under
   `examples/landing/`: a worked example demonstrating the landing
   layout — an outcome-first hero with one primary action and a
   proof point before the first scroll, sections ordered to mirror
   the decision from social proof through benefit blocks to
   objection handling and a closing action, a lead form kept to
   three fields, and a sticky action bar on compact screens that
   appears only after the hero action scrolls away — with all seven
   states shown. Done when the example passes all quality gates.
   (Implemented this run.)

456. Add a cruise booking pattern row to `catalog/patterns.md`: search by
   dates, ports, and length with the full price shown beside each sailing,
   cabin chosen with deck, grade, and price stated before booking, the
   travel party linked so plans stay together, dining and shore excursions
   booked against the sailing with change and cancel routes, travel
   documents gathered with a stated check-in step and safety briefing
   before sailing day, and the onboard account shown with its running
   balance — distinct from the hotel booking row, which books a room by
   the night rather than a cabin for a sailing, from the flight booking
   row, which books a seat on a flight rather than a cabin with onboard
   services, and from the cruise embarkation and onboard check-in gap,
   which covers boarding the ship rather than booking the sailing.
   Sources so far are a content-site guide and app-store listings only; a
   platform or standards source is still needed before the row is written.
   Done when the row passes all quality gates.

457. Add a pet grooming appointment booking pattern row to
   `catalog/patterns.md`: service, practitioner, date, and time chosen in
   that order with the duration and the full price stated before booking,
   the pet's profile carried into the booking with vaccination state
   shown where the groomer requires it, a request-based approval step
   where the groomer confirms each booking, automated reminders with a
   stated change-or-cancel route, and a before-and-after record kept on
   the pet's profile — distinct from the salon and spa appointment booking
   row, which books care for a person rather than an animal, from the
   veterinary appointment booking row, which books medical care rather
   than grooming, and from the pet adoption application row, which places
   an animal in a home rather than booking its care. Sources so far are a
   single-designer case study, a commissioned comparison, and a vendor
   blog only; a platform or standards source is still needed before the
   row is written. Done when the row passes all quality gates.

458. Add a volunteer shift signup pattern row to `catalog/patterns.md`:
   open shifts shown with the role, meeting point, start and end time,
   and places left, a waitlist that opens when the last place goes, role
   clearance checked before a shift can be claimed, signup without an
   account through one link with a confirmation and a reminder carrying
   the shift, time, place, and coordinator contact, swaps that keep
   capacity enforced, and check-in on the day with an approved hours log
   — distinct from the volunteer shift cover and substitute request gap,
   which finds a replacement for an absent volunteer rather than filling
   open shifts, from the community sports league team registration row,
   which joins a team rather than claiming named shifts, and from the
   group scheduling poll row, which finds a time that suits a group
   rather than filling shifts with named volunteers. Sources so far are
   two commissioned comparisons, a tool-builder page, and a vendor page
   only; a platform or standards source is still needed before the row is
   written. Done when the row passes all quality gates.

459. Add a connected-device prompt pattern row to
   `catalog/patterns.md`: when a new device asks to sign in, the trusted
   device shows what asked — device, place, time, and network address —
   with a short code shown on both sides to compare, approve and deny
   equally visible, a deny that blocks the sign-in and offers a password
   change, a request that expires within a short window, and an approval
   screen that lists in plain words what the device receives and how
   long it stays connected — distinct from the signed-in device
   management row, which lists devices already trusted, from the QR
   sign-in row, which signs in by scanning a code, from the second-factor
   sign-in row, which proves identity with a code, and from the device
   pairing row, which links two devices for use. Sources so far are the
   device authorisation standard and several vendor help pages with
   convergent rules. Done when the row passes all quality gates.

460. Add a multi-pet appointment booking pattern row to
   `catalog/patterns.md`: one booking with one invoice and one payment,
   each pet with its own service, time, and staff member, a one-tap
   booking for the same service across all pets, scheduling modes that
   place pets together, with clustered starts, or by best fit, a
   merge-with-existing-visit prompt when a pet already has a booking
   that day, per-pet tabs showing completion state, and no mixing of
   multi-day and same-day services in one booking — distinct from the
   veterinary appointment booking row, which books medical care for one
   animal, from the pet grooming appointment booking action, which books
   care for one animal, and from the appointment management row, which
   manages bookings already made. Sources so far are four
   booking-platform help pages with tightly convergent rules; a platform
   or standards source is still needed before the row is written. Done
   when the row passes all quality gates.

461. Add a smart baby monitor pattern row to `catalog/patterns.md`:
   alerts split by category — crying, waking, stirring, dozing, and
   in and out of the crib — each toggled on its own, sensitivity levels
   for sound and motion, a distinct sound per detection type so a
   critical alert is told apart from a routine one, a tap on an alert
   that opens the live view, and connection and low-battery alerts that
   arrive before monitoring fails — distinct from the baby feeding and
   sleep tracking gap, which logs care rather than monitoring, from the
   notification preferences row, which chooses which updates arrive,
   and from the smartwatch sensitive-notification reveal action, which
   hides content rather than surfacing alerts. Sources so far are
   vendor pages only; a platform or standards source is still needed
   before the row is written. Done when the row passes all quality
   gates.

462. Add a home care coordinator rostering pattern row to
   `catalog/patterns.md`: a week view built around the client with
   every visit colour-coded by status — draft, published, confirmed,
   cancelled, late, and overtime — recurring visits created as one
   run with a one-action carer swap across the whole run, a
   suggested carer ranked by availability, preferred-carer match,
   and travel distance, a conflict badge where a carer is
   double-booked, on leave, or unavailable, a flag where a
   non-preferred carer is assigned, and a draft and publish
   workflow with bulk changes previewed before they apply,
   undoable, and restorable for thirty days — distinct from the
   home care visit booking action (384), which books care from
   the family's side rather than rostering it, from the
   appointment management row, which manages appointments
   already booked, and from the shared resource booking row,
   which books a shared resource rather than rostering people.
   Sources so far are three vendor scheduling pages with tightly
   convergent rules; a platform or standards source is still
   needed before the row is written. Done when the row passes
   all quality gates.

463. Extend the overflow menu row in `catalog/patterns.md` with a
   restore-earlier-layout rule: where the person can switch
   built-in commands on or off and add hidden commands, offer a
   one-action restore that returns the menu to its earlier
   layout, state plainly what the restore changes and what it
   keeps, and keep the underlying actions reachable after the
   restore — cross-checked against the user-customisable menu
   rules in the same row. The earlier review noted this restore
   had no platform source; the platform release notes for the
   November 2026 update now record the customisable menu with a
   restore to the earlier layout. Done when the extended row
   passes all quality gates. (Implemented deep editorial 2026-11-23.)

464. Add a worked example for the automotive layout under
   `examples/automotive/`: a worked example demonstrating the
   driver-state adaptation rules, glanceable controls sized for
   the current task, adaptation that never moves anything while
   driving, and short-term emphasis-only changes under load,
   with all seven states — distinct from the worked desktop
   example, which covers a stationary screen rather than a
   moving vehicle, and from the worked tablet example, which
   covers width bands rather than driver load. Done when the
   example passes all quality gates. (Implemented deep editorial 2026-11-23.)

465. Add an agent run controls pattern row to
   `catalog/patterns.md`: while an agent works, keep stop, resume,
   retry, steer, and queue controls in one place — stop ends the run
   and keeps the work already done, resume carries on from the point
   it stopped at, retry starts the step again as a new attempt
   without repeating an uncertain side effect, steer hands a note to
   the running turn at its next opportunity, interrupt stops the turn
   and sends the message next, and queue lines the next message up
   above the composer with a remove control — with a finite set of run
   states, each with a timestamp and the reason it entered that state
   and what moves it forward, approval cards that separate proposed
   actions from completed ones, and status changes announced in a
   polite live region while streamed words are not announced, so
   assistive technology is not flooded — distinct from the agent
   checkpoint row, which pauses at decision points before
   irreversible actions, from the agent-placed call row, which places
   a call on the person's behalf, and from the agent-described
   interface row, which renders a screen from a description. Sources
   so far are a control-plane design essay drawing on a published
   research interface for observing and steering long-running agents,
   a vendor guide to steering a running turn, and a component
   library's run-controls component. Done when the row passes all
   quality gates. (Implemented deep editorial 2026-11-23.)

466. Add a recommendation feedback pattern row to
   `catalog/patterns.md`: where a feed recommends items, offer two
   separate controls with their effects stated in the label or
   confirmation — remove or hide this item, which tidies the current
   view only and does not change future suggestions, and not
   interested, which shapes what is suggested next — with the scope
   of each control stated (one item, a creator, a topic, or the whole
   profile), an undo for the persistent choice, and a single place
   where persistent choices can be reviewed, changed, or reset to a
   non-personalised default — and keep deliberate feedback separate
   from behaviour merely observed, so a click or a view is never read
   as a lasting preference — distinct from the personalized-content
   disclosure row, which states what signal drove an adaptation and
   offers the unadapted view, from the saved-item collection row,
   which keeps an item for a later return, and from the content
   reporting and blocking row, which reports an item rather than
   shaping suggestions. Sources so far are a published research paper
   on explicit and intentional implicit feedback in recommendation
   feeds, a platform rollout separating the two intents, and a design
   guide citing platform help centres and accessibility guidance.
   Done when the row passes all quality gates. (Implemented deep editorial 2026-11-23.)

467. Extend the smart home dashboard row in `catalog/patterns.md`
   with stale-state rules: keep the requested state separate from the
   reported state, so a tap shows a waiting state until the device
   confirms, and where no confirmation arrives within a stated
   timeout, say plainly that the change could not be confirmed rather
   than presenting it as failed, since the device may have completed
   the action while its response was lost; give old information a
   visible age on the tile, measured from the last report rather than
   the last change, so a steady reading does not read as dead; and
   mark a stale tile by more than colour. Sources so far are
   single-author guides only; a platform or standards source is still
   needed before the row is extended. Done when the extended row
   passes all quality gates.

468. Extend the parking session payment row in `catalog/patterns.md`
   with app-free checkout rules: a QR code at the lot or bay opens
   the payment page in the browser with no app download and no
   account, plate and duration entry with wallet payment in under
   thirty seconds, a live pass with a countdown, a reminder with a
   short link before expiry, and a one-tap extend from anywhere
   without returning to the vehicle — distinct from the scan-to-pay
   row, which pays at a till by scanning a code rather than starting
   a timed parking session, and from the guest checkout row, which
   covers buying without an account rather than paying for a stay.
   Sources so far are five convergent vendor pages with tightly
   matching flows; a platform or standards source is still needed
   before the row is extended. Done when the extended row passes
   all quality gates.

469. Extend the real estate property search row in
   `catalog/patterns.md` with map keyboard rules: every marker a
   real button with a roving tab stop, arrow keys with Home and End
   walking the map in reading order, Enter selecting, a cluster
   zooming into its own bounds instead of guessing which listing was
   meant, the list as one tab stop with arrow-key navigation, hover
   on a card highlighting its marker and the other way round,
   selection announced through a polite live region, and a real
   button beside load-more scrolling — distinct from the map
   comparison row, which compares places rather than searching
   listings with a map and list in step. Sources so far are a vendor
   component page implementing the rules and an accessibility guide
   grounding them in WCAG criteria 1.3.1, 2.4.3, 4.1.3, and 1.4.1;
   a platform or standards source is still needed before the row is
   extended. Done when the extended row passes all quality gates.

470. Re-check the EN 301 549 v4.1.1 Official Journal citation and
   update `trends/2026/standards-outlook.md` once it lands: the
   outlook currently records the citation date as disputed between
   trackers, one expecting 16 December 2026 and another 22 January
   2027, after the date already moved once from late November 2026.
   When the citation is published, replace the disputed-expectation
   wording with the cited version and date, state which version
   carries the presumption of conformity from that day, and re-check
   the six new criteria against the cited text. Sources so far are
   the standards trackers already recorded in
   `resources/sources.json`. Done when the updated outlook passes
   all quality gates.

- Completed this review (deep editorial 2026-11-16): two new
  pattern rows in `catalog/patterns.md` — Age assurance flow and
  Museum timed-entry ticket booking — completing roadmap action
  278; actions 252, 259, and 344 re-checked with source positions
  updated; Material Design 3 Expressive row added to
  `resources/libraries.md` with the Chakra UI row updated; three
  new improvement actions added (362 conversational companion
  safeguards for minors, 363 spending controls for minors, 364
  car wash booking and membership), ordered by coverage impact,
  each a genuine gap with its source position stated. Coverage
  matrix updated (two rows to Full, three new Gap items; 460
  pattern rows, Partial 57). 15 new source records (941 total).
  This run also carries the publish of the working tree left
  unpublished since the 2026-11-15T05:55:50Z sync, including the
  parcel locker pickup kiosk-accessibility extension, the
  phone-side fitness workout logging, digital loyalty card wallet
  pass and online therapy booking rows, the translucent control
  material row, and actions 353-361. Open actions after this
  review: 252, 259, 265, 266, 268, 277, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319,
  327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 340, 341, 342,
  343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359,
  360, 361, 362, 363, 364.


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

- Completed this review (deep editorial 2026-11-11): new Mobile
  cheque deposit and Home energy usage dashboard pattern rows in
  `catalog/patterns.md`, completing roadmap actions 276 and 271;
  coverage matrix updated (two new rows to Full, Home energy usage
  dashboard out of the Partial list); three new improvement actions
  added (279 university admissions application portal, 280 gym and
  fitness class booking, 281 job application portal); 4 new source
  records (757 total). Re-checked against deeper sources:
  drive-through and curbside pickup (252) gains platform guidance
  for the pickup point, the arrival signal, and the expected pickup
  time, with a stated wait with updates and reporting a wrong or
  missing item from the vehicle still needing a source; childcare
  booking (265) gains a single-organisation advice checklist
  covering the age-and-days-first and availability-by-day elements
  in substance, below the platform or standards bar; public library
  borrowing (266) gains single-library help pages covering queue
  place, pickup window, hold freezing, and renewal limits in
  substance, below the bar; ATM interface (268) gains no new
  platform or standards source for popular amounts first or the
  card-return order. Open actions after this review: 252, 259, 265,
  266, 268, 277, 278, 279, 280, 281.

- Completed this review (daily planning 2026-11-11): five new
  improvement actions added (282 blood donation appointment
  booking, 283 virtual court hearing, 284 proctored exam, 285
  wedding registry and gift list, 286 hot-desk and co-working
  booking), ordered by coverage impact; coverage matrix Partial
  list updated with the five new named items and with the five
  open named items from earlier reviews (277 dating app profile
  and matching, 278 museum timed-entry ticket booking, 279
  university admissions application, 280 gym and fitness class
  booking, 281 job application portal) that were missing from
  it. No new source records — the five searches (blood donation
  appointment booking, wedding registry and gift list, virtual
  court hearing, proctored exam, hot-desk and co-working booking)
  returned only single-designer case studies, app listings,
  single-service pages, vendor blogs, buyer guides, a patent, and
  single-jurisdiction court pages below the source-quality bar,
  so the five genuine gaps are recorded as actions instead of
  rows. Since the last daily run, the deep cycle completed
  actions 271 and 276; the benefits claim application row was
  also added to the working tree (local files 04:30Z, 5 new source
  records, 762 total) by a run that left no ops-log entry — noted
  here for the record, and included in this run's publish. The
  five new pattern rows are left to the deep
  cycle, pending a platform or standards source for each. Open
  actions after this review: 252, 259, 265, 266, 268, 277, 278,
  279, 280, 281, 282, 283, 284, 285, 286.

- Completed this review (deep editorial 2026-11-11): new Blood
  donation appointment booking and Virtual court hearing pattern
  rows in `catalog/patterns.md`, completing roadmap actions 282
  and 283; Visa application row cross-check corrected — it named
  a passport renewal row that does not exist; coverage matrix
  updated (two new rows to Full, two items out of the Partial
  list, three new named items added to it); three new improvement
  actions added (287 driving test booking, 288 home broadband
  installation and router setup, 289 public transport season
  ticket purchase); 6 new source records (768 total). Re-checked
  against deeper sources: ATM interface (268) gains no new
  platform or standards source for popular amounts first or the
  card-return order — a single-bank guide confirms preset
  fast-cash amounts and a content-site guide covers denomination
  choice, both below the bar, and the card-return rule as written
  still needs correcting; museum timed-entry ticket booking (278)
  still rests on single-venue travel guides and a ticket-reseller
  page, with no platform or standards guidance. Open actions
  after this review: 252, 259, 265, 266, 268, 277, 278, 279, 280,
  281, 284, 285, 286, 287, 288, 289.

- Completed this review (deep editorial 2026-11-11): new Proctored
  exam and Restaurant online ordering pattern rows in
  `catalog/patterns.md`, completing roadmap action 284; coverage
  matrix updated (two new rows to Full, Proctored exam out of the
  Partial list, Passport renewal added to the Partial list where
  it was missing); three new improvement actions added (290 online
  will creation, 291 timed cart-hold, 292 digital parking permit
  application); 5 new source records (775 total). Re-checked
  against deeper sources: online will creation still rests on
  consumer-law guidance for businesses with no interface rules, a
  single-product review, and a state trustee guide; timed
  cart-hold still rests on single-vendor ticketing and storefront
  help pages; digital parking permit application still rests on
  single-vendor product pages. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 281, 285, 286, 287,
  288, 289, 290, 291, 292, 293, 294, 295.

- Completed this review (deep editorial 2026-11-11): no new
  pattern rows — the four re-checked open actions stay open for
  want of a platform or standards source; three new improvement
  actions added (293 waste collection schedule and missed bin
  reporting, 294 home cleaning service booking, 295 smart TV
  programme guide), ordered by coverage impact; coverage matrix
  Partial list updated with the three new named items. Re-checked
  against deeper sources: driving test booking (287) gains
  single-author booking guides, a driving-school blog, a
  third-party booking site, and a single-jurisdiction government
  service page that describes the booking steps without interface
  rules; public transport season ticket purchase (289) gains
  travel guides, a retailer help page, a fare-policy research
  report, and an operator app page, with no interface guidance;
  home broadband installation and router setup (288) gains
  comparison and self-install guides only, with no interface
  guidance; timed cart-hold (291) gains storefront-platform
  extension guides that add one honest-timer rule — never call a
  hold reserved unless stock is truly held, persist the countdown
  so a refresh does not restart it, and let it expire visibly —
  still single-vendor class, below the bar. No new source records
  (775 total). Open actions after this review: 252, 259, 265, 266,
  268, 277, 278, 279, 280, 281, 285, 286, 287, 288, 289, 290, 291,
  292, 293, 294, 295.

- Completed this review (daily planning 2026-11-12): five new
  improvement actions added (299 university student portal
  dashboard, 300 online course lesson player and progress, 301
  airport self-service bag drop kiosk, 302 online prize draw and
  raffle entry, 303 streaming household viewer profiles with PIN
  lock), ordered by coverage impact; coverage matrix Partial list
  updated with the five new named items. No new source records —
  the five searches (university student portal dashboard, online
  course lesson player and progress, streaming household viewer
  profiles, airport self-service bag drop kiosk, online prize draw
  and raffle entry) returned only vendor blogs, agency blogs, a
  marketing blog, single-app guides, vendor help pages, and
  content sites below the source-quality bar, with two partial
  exceptions: an accessibility-organisation baseline standard for
  e-learning that covers captions, keyboard access, and plain
  language but not the lesson-player flow, and regulator material
  for bag-drop kiosk accessibility and for prize-draw free entry
  that grounds only part of each pattern — so the five genuine
  gaps are recorded as actions instead of rows. Since the last
  daily run, the deep cycle completed actions 281, 293, and 295
  and the working tree gained the contact-a-GP-surgery-online row;
  those outcomes are already recorded in `CHANGELOG.md`. The five
  new pattern rows are left to the deep cycle, pending a platform
  or standards source for each. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287, 288,
  289, 290, 291, 292, 294, 296, 297, 298, 299, 300, 301, 302, 303.

- Completed this review (deep editorial 2026-11-12): new
  Vaccination appointment booking and digital certificate pattern
  row in `catalog/patterns.md`; kiosk layout extended with
  headset, privacy-mode, tactile-key, and non-biometric-route
  rules; coverage matrix updated with the new row; three new
  improvement actions added (304 pet adoption application, 305
  lost property reporting, 306 video doorbell visitor interface),
  ordered by coverage impact; coverage matrix Partial list updated
  with the three new named items; 5 new source records (792
  total). Re-checked against deeper sources: ATM interface (268)
  gains accessibility-standard confirmation of the half already
  recorded but no source for popular amounts first or the
  card-return order; driving test booking (287) gains a government
  consultation response with booking policy rules but no interface
  rules; public transport season ticket purchase (289) gains
  single-operator smartcard help pages only; online will creation
  (290) gains content-site and vendor pages only; timed cart-hold
  (291) gains storefront-platform extension guides repeating the
  honest-timer rules, still single-vendor class. Open actions after
  this review: 252, 259, 265, 266, 268, 277, 278, 279, 280, 285,
  286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 298, 299, 300,
  301, 302, 303, 304, 305, 306.

- Completed this review (deep editorial 2026-11-12): new
  Passport renewal, Meal planning, Online course lesson player
  and progress, Online voter registration and mail-in ballot
  tracking, and Jury duty summons response pattern rows in
  `catalog/patterns.md`, completing roadmap actions 263 and 300
  (the Passport renewal row was missing although the action was
  marked implemented — the earlier record rested on the shared
  Government document application row; the row is now written
  from the recorded government sources); the Order substitution
  choice row extended with substitution-acceptance and visible
  stock-out rules from peer-reviewed retail studies; coverage
  matrix reconciled (428 pattern rows, all in Full; Partial 30 —
  Passport renewal and the lesson player moved to Full, online
  will creation, timed cart-hold, and digital parking permit
  application added as named open actions, and the two new
  actions added); three new improvement actions added (307
  community sports league team registration, 308 vehicle
  registration renewal and car tax payment, 309 voice dictation
  entry-control distinction); 32 new source records (826 total),
  plus 7 source records restored after a faulty file restore
  removed the pre-run local records. Re-checked: online grocery
  delivery is covered in substance by existing rows, with the
  substitution findings folded into the Order substitution choice
  row; community sports league team registration stays open for
  want of a governing-body, regulator, or peer-reviewed source;
  the delivery-slot strengthening rules rest on a master's thesis
  only and are left for a later review. Open actions after this
  review: 252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286,
  287, 288, 289, 290, 291, 292, 294, 296, 297, 298, 299, 301, 302,
  303, 304, 305, 306, 307, 308, 309.

- Completed this review (deep editorial 2026-11-12): new
  Smartwatch workout tracking pattern row in
  `catalog/patterns.md`, completing roadmap action 298; the Hotel
  self check-in row extended with wallet-pass key delivery rules
  and the Electric vehicle charging session row extended with
  availability-freshness and fault-report rules; coverage matrix
  updated with the new row (429 pattern rows, all in Full;
  Partial 29); three new improvement actions added (310 council
  tax payment and discount application, 311 ferry booking, 312
  energy tariff comparison and switching); 6 new source records
  (833 total). Re-checked: pharmacy prescription refill
  eligibility is already covered in substance by the Medication
  refill request row, which shows only refillable prescriptions
  in the request list and keeps the rest in the history with the
  reason stated; the ATM interface row (268) stays open — fresh
  results are a content-site guide, a single-author post, and a
  patent, with no platform source for popular amounts first or
  the card-return order, and the card-return rule as written
  still needs correcting before the row is written; the airport
  self-service bag drop row (301) stays open — the flow still
  rests on vendor product pages and operator guides, with
  standards material covering only the common-use infrastructure;
  the vehicle registration renewal row (308) stays open —
  government service pages describe the service rather than
  design guidance. Open actions after this review: 252, 259, 265,
  266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290, 291,
  292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308,
  309.

- Completed this review (deep editorial 2026-11-13): new Flight
  search and booking pattern row in `catalog/patterns.md`,
  grounded in the flight booking research library and its 2026
  quantitative study of 3,125 shoppers; electronic ballot
  interface rules added to the Ballot row from the voting system
  guidelines — text-size choice, touch targets, no horizontal
  scrolling when enlarged, and the same functions in every
  display format with settings and selections carried across a
  format switch; coverage matrix updated with the new row (430
  pattern rows, all in Full; Partial 29); three new improvement
  actions added (313 virtual court hearing extension, 314 flight
  booking worked example, 315 remote ballot marking extension);
  5 new source records (838 total). This publish also carries
  the working-tree changes left unpublished by the 2026-11-12
  deep editorial run — the Smartwatch workout tracking row, the
  hotel wallet-pass key extension, the electric vehicle charging
  freshness and fault-report extension, and actions 310, 311 and
  312 — which that run recorded in the changelog and roadmap but
  did not push. Open actions after this review: 252, 259, 265,
  266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290, 291,
  292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308,
  309, 310, 311, 312, 313, 314, 315.

- Completed this review (daily planning 2026-11-13): five new
  improvement actions added (316 personal budgeting and expense
  tracking dashboard, 317 shared family calendar, 318 wedding
  planning app, 319 theme park virtual queue reservation, 320
  board game app interface), ordered by coverage impact;
  coverage matrix Partial list updated with the five new named
  items (Partial 34). No new source records — the five searches
  (personal budgeting and expense tracking dashboard, shared
  family calendar, theme park virtual queue reservation, wedding
  planning app, chess and board game app interface) returned
  only a design-gallery content site, a single-author article,
  an agency guide, a single-designer portfolio, a design-concept
  page, a content-site roundup, a sponsored product review, a
  personal build log, a news digest, app-store listings, a
  magazine content piece, a prompt-sharing page, two patents, a
  vendor development blog, a code-documentation page, and a
  review aggregator below the source-quality bar, so the five
  genuine gaps are recorded as actions instead of rows. Since
  the last daily run, the deep cycle completed the Flight search
  and booking pattern row and the electronic ballot interface
  rules and added actions 313, 314, and 315, and the light cycle
  added the ambient voice feedback rule to the automotive layout;
  those outcomes are already recorded in `CHANGELOG.md`. The five
  new pattern rows are left to the deep cycle, pending a platform
  or standards source for each. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317,
  318, 319, 320.

- Completed this review (deep editorial 2026-11-13): new
  Board game app interface pattern row in `catalog/patterns.md`,
  completing roadmap action 320 — the board as the primary area
  in a square ratio, both drag-and-drop and tap-to-move, legal
  moves shown on selection, a four-action action bar, compact
  player panels, time controls in plain words, high-contrast
  options, a move history and game log, and an intent-based first
  run; and a new Language learning lesson pattern row — placement
  onboarding, a labelled lesson path, one exercise frame for every
  question type, feedback on every answer, a lesson-complete
  summary, and streak and quest views. Coverage matrix updated
  (Board game app interface moved from Partial to Full, Language
  learning lesson added to Full; 433 pattern rows, Partial 32);
  three new improvement actions added (321 music streaming
  playlist and queue, 322 podcast app playback interface, 323
  digital wallet add-card and tap-to-pay setup); 5 new source
  records (847 total). Re-checked: music streaming, podcast
  playback, and digital wallet add-card stay as actions for want
  of a platform or standards source; the flight booking worked
  example (314) stays open. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 317, 318,
  319, 321, 322, 323.

- Completed this review (deep editorial 2026-11-13): new
  Music streaming playlist and queue pattern row in
  `catalog/patterns.md`, completing roadmap action 321 — a
  now-playing view with large artwork, a progress bar with elapsed
  and remaining time, and transport controls in the thumb zone; a
  queue in three labelled parts — now playing, next, and played —
  with a visible indicator on the current item; primary controls in
  the order queue, previous, play or pause, next, with further
  actions behind an overflow control; drag handles and a remove
  control on every queued track, with shuffle and repeat states
  kept across the session; a mini player pinned above the tab bar
  while browsing; and per-track menus with add to playlist, add to
  queue, and save to library as one action each; and the Digital
  wallet add-card and tap-to-pay setup row extended with the
  pass-display element, completing roadmap action 323 — a pass
  style chosen to match the use, essential information kept
  visible where the pass is collapsed, a contactless-compatible
  pass preferred with a barcode or QR code where one is needed,
  the pass designed to look right on every device, and text kept
  in pass fields rather than inside images. Coverage matrix
  updated (Music streaming playlist and queue moved to Full,
  Podcast app playback interface added to Partial, correcting an
  earlier omission; 435 pattern rows, Partial 36); three new
  improvement actions added (324 banking fraud alert, 325 digital
  health record patient portal, 326 audiobook library app); 4 new
  source records (853 total). Re-checked: shared family calendar,
  wedding planning app, theme park virtual queue reservation, and
  podcast app playback interface stay as actions for want of a
  platform or standards source; the flight booking worked example
  (314) stays open. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 317, 318,
  319, 322, 324, 325, 326.

- Completed this review (deep editorial 2026-11-13): new
  Digital health record patient portal pattern row in
  `catalog/patterns.md`, completing roadmap action 325 — a
  task-separated home, results with a plain-language sentence
  and a clinician route, release preferences honoured rather
  than defaulting to immediate alerts, scoped and revocable
  proxy access with plain-language consent, records shared as an
  agreed short summary, and a session-timeout warning at least 2
  minutes before the end; and a Banking fraud alert pattern row,
  completing roadmap action 324 — an instant multi-channel
  alert naming the exact transaction, a plain statement that a
  restriction may relate to suspected fraud, a reply path inside
  the alert, immediate acknowledgement with a reference number,
  immediate steps to prevent further transactions, and a
  close-loop response within a stated window of no longer than 30
  days, with a rule never to reveal that a report exists. The
  row is narrower than the action as written: the three-way
  confirm, deny, and unsure-freeze choice, keeping recurring
  payments flowing while frozen, and merchant-name enrichment
  have no platform or standards source and are not in the row.
  Coverage matrix updated (Banking fraud alert and Digital
  health record patient portal moved to Full; Pet grooming
  appointment booking, School lunch ordering, and Home solar
  energy monitoring added to Partial; 437 pattern rows, Partial
  37); three new improvement actions added (327 pet grooming
  appointment booking, 328 school lunch ordering, 329 home solar
  energy monitoring); 6 new source records (860 total).
  Re-checked: audiobook library app (326) stays open — the
  platform sources found cover the generic player, chapter
  navigation, and single-device resume, but the sleep timer,
  speed steps, bookmarks, downloads, cross-device resume, and
  library organisation have no platform or standards source;
  shared family calendar, wedding planning app, theme park
  virtual queue reservation, and podcast app playback interface
  stay as actions for want of a platform or standards source;
  the flight booking worked example (314) stays open. Open
  actions after this review: 252, 259, 265, 266, 268, 277, 278,
  279, 280, 285, 286, 287, 288, 289, 290, 291, 292, 294, 296,
  297, 299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310,
  311, 312, 313, 314, 315, 317, 318, 319, 322, 326, 327, 328, 329.

- Completed this review (deep editorial 2026-11-14): new
  Podcast app playback interface pattern row in
  `catalog/patterns.md`, completing roadmap action 322 — a
  now-playing view with chapter marks and a chapter list that
  follows playback, a synced transcript with a search, skip
  back and forward in stated seconds, speed in steps of a
  tenth, a sleep timer with an end-of-episode or end-of-chapter
  choice, a mini player pinned above the tab bar, a resume
  position kept across sessions, and playback controllable
  from the lock screen, notification shade, headset buttons,
  and keyboard media keys; a new Audiobook library app pattern
  row, completing roadmap action 326 — a library organised by
  book with the listening position kept per title, a chapter
  list with durations taken from the table of contents, and a
  player with skip, speed, and a sleep timer with an
  end-of-chapter choice; and a new Student accommodation
  booking pattern row — term-time search with the term total
  beside the rent, the full cost stated on the room before
  booking starts, accreditation under the recognised national
  code of practice shown on the listing, contract terms,
  deposit protection, guarantor requirement, and a named
  complaints route with independent review. Coverage matrix
  updated (Podcast app playback interface and Audiobook
  library app moved from Partial to Full, Student accommodation
  booking added to Full; 440 pattern rows, Partial 35); three
  new improvement actions added (330 meal kit delivery
  subscription, 331 online ticket resale transfer extension,
  332 volunteer shift signup); 7 new source records (867
  total). Re-checked: shared family calendar, wedding planning
  app, theme park virtual queue reservation, pet grooming
  appointment booking, school lunch ordering, and home solar
  energy monitoring stay as actions for want of a platform or
  standards source; the flight booking worked example (314)
  stays open. Open actions after this review: 252, 259, 265,
  266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290,
  291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306,
  307, 308, 309, 310, 311, 312, 313, 314, 315, 317, 318, 319,
  327, 328, 329, 330, 331, 332.

- Completed this review (daily planning 2026-11-14): four new
  improvement actions added (333 peer-to-peer payment, 334 parcel
  sending and courier booking, 335 smart home security camera,
  336 food rescue and surplus food pickup), ordered by coverage
  impact; coverage matrix Partial list updated with the four new
  named items and corrected with five open named gaps that were
  missing from it (310 council tax payment and discount
  application, 311 ferry booking, 312 energy tariff comparison
  and switching, 330 meal kit delivery subscription, 332 volunteer
  shift signup) (Partial 44). No new source records — the five
  searches (peer-to-peer payment, parcel sending and courier
  booking, smart home security camera live view and event
  timeline, babysitter and nanny booking, food rescue and surplus
  food pickup) returned only a UI-kit vendor guide, an agency
  article, a single-designer case study, a personal post, an
  agency portfolio, an agency guide, single-operator help pages
  and a blog, app-store listings, a vendor user guide, a carrier
  guide, an open-source project documentation site, a listing
  site, a content site, a vendor product page, a single-author
  review, app-review content sites, a download listing, and a
  news site below the source-quality bar, so the four genuine gaps
  are recorded as actions instead of rows. Babysitter and nanny
  booking was probed and stays a future-cycle candidate: its
  substance overlaps open action 265 (childcare booking). Since
  the last daily run, the light cycle completed the Personal
  budgeting dashboard and Digital wallet add-card and tap-to-pay
  setup pattern rows, the deep cycle completed the Board game app
  interface, Music streaming playlist and queue, Banking fraud
  alert, and Digital health record patient portal pattern rows,
  and the deep editorial review added the Podcast app playback
  interface, Audiobook library app, and Student accommodation
  booking pattern rows with actions 330, 331, and 332; those
  outcomes are already recorded in `CHANGELOG.md`. The four new
  pattern rows are left to the deep cycle, pending a platform or
  standards source for each. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 317, 318,
  319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336.

- Completed this review (deep editorial 2026-11-14): new Train
  ticket booking pattern row in `catalog/patterns.md` — fares,
  times, and class shown before traveller details, the lowest
  fare highlighted, seat or berth stated as preference,
  allocation, or confirmed choice, fare and seat held to payment
  with the expiry shown and the price fixed, live service status,
  and change and cancel routes with fees stated in advance; a new
  Public transport ticket purchase pattern row — ticket type, fare
  class, zones, and dates before payment, activation kept separate
  from purchase, a three-group ticket wallet, a scannable code at
  full brightness, offline display of an activated ticket, and
  one-tap repurchase; and a new Mental health journaling and mood
  tracking pattern row — a one-screen check-in in three taps or
  fewer, feelings in plain words with text labels, optional
  private journaling, progress that never punishes a gap, privacy
  on by default, a fixed support button on every screen, one
  suggested next step after saving, and the limits of the app
  stated plainly. Coverage matrix updated (three rows added to
  Full; 446 pattern rows, Partial 44); three new improvement
  actions added (337 period and fertility tracking, 338 airport
  lounge access, 339 smart thermostat heating schedule); 8 new
  source records (886 total). The action 316 marker was corrected: the Personal
  budgeting dashboard row already existed in
  `catalog/patterns.md` and is now marked implemented. The
  publish was attempted twice and both attempts were interrupted
  by service restarts; the remote head is still 9a6e720d, so this
  run's rows and the working-tree changes left unpublished by the
  2026-11-14 02:12Z deep editorial run — the Podcast app playback
  interface, Audiobook library app, and Student accommodation
  booking pattern rows, the passkey autofill extension, and
  actions 330-336 — remain in the working tree for the next
  cycle to push. Open actions after
  this review: 252, 259, 265, 266, 268, 277, 278, 279, 280, 285,
  286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302,
  303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315,
  317, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336,
  337, 338, 339.

- Completed this review (deep editorial 2026-11-14): new Shared
  family calendar pattern row in `catalog/patterns.md` — a
  week-at-a-glance default view, one colour per person that never
  changes, the owner named in each event title, claiming over
  assigning, preparation reminders tied to a specific action, and
  a wall display mode that opens on today — completing roadmap
  action 317; a new Peer-to-peer marketplace selling pattern row
  — a short photo-first sell flow, structured condition and
  attribute fields, a pricing suggestion from comparable sales,
  every fee stated before publishing, listing states with reasons
  for holds, trust signals on the item page, and a seller
  dashboard; and a new Site-registered agent tools section in
  `trends/2026/agentic-ux.md` — script registration on the
  document object, the entry-point move from the navigator object,
  the dropped form-based form, behaviour where the entry point
  is absent, and a checkpoint for anything irreversible, costly,
  or privacy-sensitive. Coverage matrix updated (Shared family
  calendar moved from Partial to Full, Peer-to-peer marketplace
  selling added to Full; 448 pattern rows, Partial 43); three new
  improvement actions added (343 crypto wallet app, 344 drone and
  robot delivery tracking, 345 smart door lock and keyless entry);
  15 new source records (901 total). The previous review note's
  figures were corrected to the verified state (446 pattern rows,
  Partial 44, 8 new source records, 886 total). This run also
  carries the publish of the working tree left unpublished by the
  2026-11-14 13:52Z deep editorial run, including the Train ticket
  booking, Public transport ticket purchase, and Mental health
  journaling and mood tracking rows, actions 337-339, and the
  earlier Podcast app playback interface, Audiobook library app,
  and Student accommodation booking rows and the passkey autofill
  extension. Actions 330-336 stay open: no rows exist for them
  yet. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287, 288,
  289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305,
  306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 327,
  328, 329, 330, 331, 332, 333, 334, 335, 336, 343, 344, 345.

- Completed this review (deep editorial 2026-11-15): three
  genuine gaps re-checked against fresh sources — video
  streaming player interface, government citizen services
  portal, and weather app interface — all still below the source
  bar for a pattern row, with no platform or standards source
  for the interface itself, so no new rows this review; three
  new improvement actions added (346 video streaming player
  interface, 347 government citizen services portal, 348
  weather app interface), ordered by coverage impact, each a
  genuine gap with its source position stated. Coverage matrix
  updated (three new Gap items; 448 pattern rows, Partial 43).
  0 new source records (901 total). This run also carries the
  publish of the working tree left unpublished by the 2026-11-14
  deep editorial runs, including the Shared family calendar and
  Peer-to-peer marketplace selling rows, the site-registered
  agent tools section, and actions 337-345. Open actions after
  this review: 252, 259, 265, 266, 268, 277, 278, 279, 280, 285,
  286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302,
  303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315,
  318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336,
  343, 344, 345, 346, 347, 348.

- Completed this review (daily planning 2026-11-15): four new
  improvement actions added (349 neighbourhood noticeboard, 350
  digital business card sharing, 351 carpool coordination, 352
  home EV charger scheduling), ordered by coverage impact, each a
  genuine gap with its source position stated. Coverage matrix
  updated (four new Gap items; 448 pattern rows, Partial 43).
  0 new source records (901 total). No new pattern rows this
  review — all four candidates stay below the source bar for want
  of a platform or standards source. Since the last daily run,
  the deep cycle completed the Shared family calendar,
  Peer-to-peer marketplace selling, Train ticket booking, Public
  transport ticket purchase, Mental health journaling and mood
  tracking, Podcast app playback interface, Audiobook library
  app, and Student accommodation booking pattern rows and the
  site-registered agent tools section, and the light cycles
  completed the Personal budgeting dashboard and Digital wallet
  add-card and tap-to-pay setup rows; those outcomes are already
  recorded in `CHANGELOG.md`. The four new pattern rows are left
  to the deep cycle, pending a platform or standards source for
  each. This run also carries the publish of the working tree left
  unpublished by the 2026-11-14 and 2026-11-15 deep editorial
  runs, including the Train ticket booking, Public transport
  ticket purchase, Mental health journaling and mood tracking,
  Podcast app playback interface, Audiobook library app, and
  Student accommodation booking rows, the passkey autofill
  extension, and actions 337-348. Open actions after this review:
  252, 259, 265, 266, 268, 277, 278, 279, 280, 285, 286, 287,
  288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304,
  305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319,
  327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 343, 344, 345,
  346, 347, 348, 349, 350, 351, 352.

- Completed this review (deep editorial 2026-11-15): six new
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 345 (smart door lock and keyless entry) and 351
  (carpool coordination); the other four rows close genuine gaps
  named by recent light cycles with no open action of their own.
  Self-service food ordering kiosk — reach band, one-hand
  operation, target size, contrast, and calorie disclosure rules
  grounded in the access standard, menu-labelling rules, and the
  content-accessibility guidelines; the screen-count and
  items-per-screen figures rest on vendor practice only, so the
  row states them as practical limits. Personalised news feed —
  transparency, in-feed preference control, and a non-personalised
  ordering grounded in the recommender-transparency regulation.
  Kids' launcher / curated home screen — approved-app list, age
  profiles, guardian approval, time allowances, schedules, and
  monitoring disclosure grounded in platform parental-controls
  guidance and the children's design code. Real estate property
  search — total price, material facts, and provenance labels
  grounded in the unfair-commercial-practices guidance; the
  search mechanics are stated as practice. Smart lock guest access
  — per-person codes, stay windows, instant revoke, entry record,
  and unique changeable codes grounded in the connected-home lock
  standard, the consumer IoT baseline, and product-security
  rules. Carpool coordination — identity and vehicle checks,
  no-extra-passenger rule, live trip sharing, route-deviation
  alerts, cost-share with no profit, and a stated cancellation
  cap grounded in the transport-safety guidelines, the aggregator
  rules, and the state aggregator policy; the guidelines text was
  verified through a verbatim reproduction with press
  corroboration, as the issuing body's own site copy was not
  located in search. Three new improvement actions added (353
  phone-side fitness workout logging, 354 digital loyalty card
  wallet pass presentation, 355 online discussion forum /
  community board), ordered by coverage impact, each a genuine gap
  with its source position stated. Coverage matrix updated (six
  rows to Full; 455 pattern rows, Partial 49). 13 new source
  records (916 total). Matrix reconciliation this review: measured
  counts correct two stale figures carried in earlier notes
  (pattern rows 449, not 448; Partial 50, not 43, before this
  run); no duplicate or overlapping matrix entries; every pattern
  row present in Full. Open actions after this review: 252, 259,
  265, 266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290,
  291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307,
  308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 327, 328, 329,
  330, 331, 332, 333, 334, 335, 336, 343, 344, 346, 347, 348, 349,
  350, 352, 353, 354, 355.

- Completed this review (deep editorial 2026-11-15): three new
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 353 (phone-side fitness workout logging) and 354
  (digital loyalty card wallet pass); the third row closes a
  genuine gap named by recent light cycles with no open action of
  its own. Phone-side fitness workout logging — three-second
  countdown, glance-readable live figures, lock-screen and
  voice-assistant controls without unlocking, heart rate only
  from a paired sensor, and session restore after a crash,
  grounded in the platform workout session guidance. Digital
  loyalty card wallet pass — the reward itself in the primary
  field, balance, tier, and expiry on the pass face, and pass
  updates that change only the fields that moved, grounded in
  the wallet loyalty pass documentation. Online therapy booking
  — self-referral online, a choice of phone, video, messaging,
  or a guided programme, online booking of first and follow-up
  appointments, and a stated privacy and drop-out rule, grounded
  in the national talking-therapies service guidance; the
  booking-online rule rests on the same service's digital-access
  page. Three new improvement actions added (356 smart fridge
  and food inventory, 357 smart baby monitor, 358 smart garden
  and plant care), ordered by coverage impact, each a genuine gap
  with its source position stated. Coverage matrix updated
  (three rows to Full; 458 pattern rows, Partial 52). 5 new
  source records (922 total). This run also publishes the working
  tree left unpublished by the 2026-11-15 deep editorial runs
  (six pattern rows, the translucent control material row, and 13
  source records). Open actions after this review: 252, 259,
  265, 266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290,
  291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307,
  308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 327, 328, 329,
  330, 331, 332, 333, 334, 335, 336, 343, 344, 346, 347, 348, 349,
  350, 352, 355, 356, 357, 358.

- Completed this review (deep editorial 2026-11-15): Parcel
  locker pickup row in `catalog/patterns.md` extended with
  kiosk accessibility rules — every function in visual text and
  audible speech, a tactile start for spoken guidance with
  private listening, a tactile keypad alternative, and spoken
  guidance to the compartment door — grounded in a peer-reviewed
  locker accessibility study and public kiosk accessibility
  guidance. Three new improvement actions added (359 salon and
  spa appointment booking, 360 meditation and mindfulness app,
  361 smartwatch sensitive-notification reveal), ordered by
  coverage impact, each a genuine gap with its source position
  stated. Home solar energy monitoring action 329 source
  position updated with two corroborating homeowner guides; the
  gap stays open for want of a platform or standards source.
  Coverage matrix updated (three new Gap items; 458 pattern
  rows, Partial 52). 4 new source records (926 total). This run
  publishes the working tree left unpublished by the 2026-11-15
  deep editorial runs (ten pattern rows, the translucent control
  material row, and 21 source records, plus the four records in
  this review). Open actions after this review: 252, 259,
  265, 266, 268, 277, 278, 279, 280, 285, 286, 287, 288, 289, 290,
  291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307,
  308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 327, 328, 329,
  330, 331, 332, 333, 334, 335, 336, 343, 344, 346, 347, 348, 349,
  350, 352, 355, 356, 357, 358, 359, 360, 361.


- Completed this review (daily planning 2026-11-16): five new
  improvement actions added (365 fantasy sports app, 366 house
  moving and removals booking, 367 baby feeding and sleep
  tracking, 368 children's pocket money and allowance, 369
  tradesperson and plumber booking), ordered by coverage impact,
  each a genuine gap with its source position stated; no new
  pattern rows for these five this review — all stay below the
  source bar for want of a platform or standards source, so no
  row was implemented in this run and implementation stays with
  the deep cycle. Coverage matrix updated (five new Gap items;
  460 pattern rows, Partial 57). No new source records. Open
  actions after this review: 252, 259, 265, 266, 268, 277, 279,
  280, 285, 286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 299,
  301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,
  314, 315, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335,
  336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355,
  356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368,
  369.

- Completed this review (deep editorial 2026-11-16): one new
  pattern row in `catalog/patterns.md` — Appliance remote
  control — grounded in the appliance safety standard through a
  standards-anchored explainer and corroborated by a manufacturer
  manual: remote start armed locally at the appliance and
  cancelled when the door opens, remote stop and pause always
  available, heat sources most restricted, live status with
  remaining time, cycle-end and fault notices, finish-by
  scheduling, and a stated support period with full local
  operation kept. Three new improvement actions added (370
  restaurant table reservation, 371 food delivery courier/driver
  app, 372 wedding invitation RSVP), ordered by coverage impact,
  each a genuine gap with its source position stated; no new
  pattern rows for these three this review — all stay below the
  source bar for want of a platform or standards source. Matrix
  reconciliation this review: measured counts correct a stale
  figure carried in earlier notes (pattern rows 460 confirmed;
  Partial 62 measured, not 57, before this run). Coverage matrix
  updated (one row to Full; three new Gap items; 461 pattern
  rows, Partial 65). 3 new source records (944 total). This run
  publishes the working tree left unpublished since the
  2026-11-15T05:55:50Z sync, including the parcel locker pickup
  kiosk-accessibility extension, the phone-side fitness workout
  logging, digital loyalty card wallet pass, online therapy
  booking, age assurance flow and museum timed-entry ticket
  booking rows, the translucent control material row, the Material
  Design 3 Expressive row, and actions 353-369. Open actions
  after this review: 252, 259, 265, 266, 268, 277, 279, 280, 285,
  286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302,
  303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315,
  318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 340,
  341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357,
  358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370,
  371, 372.


- Completed this review (deep editorial 2026-11-16): five new
  pattern rows in `catalog/patterns.md` — Civic issue reporting
  (standard category list with category-specific questions,
  location in one of three forms, reference number with open or
  closed status, no mandatory account); Freelancer invoicing
  (mandatory invoice fields, payment means and terms, deposit and
  milestone billing through defined invoice processes, credit
  notes, hybrid PDF output); Stock trading and investing
  (prescribed risk warning kept prominent, 24-hour cooling-off,
  personalised risk warning, appropriateness checks that genuinely
  test understanding, positive friction before high-risk trades,
  order review and confirm); Food delivery courier/driver app
  (offer facts before acceptance, earnings net of fees, in-motion
  lockout, report-issue route at every stage, no undue pressure
  from timers or incentives) — completing roadmap action 371; and
  Grocery price comparison (selling price and unit price for every
  product, one unit per category, like-for-like matching, barcode
  scan by product number, cheapest-store split). Three new
  improvement actions added (373 water utility bill payment, 374
  pregnancy tracking, 375 restaurant waitlist management), ordered
  by coverage impact, each a genuine gap with its source position
  stated; no new pattern rows for these three this review — all
  stay below the source bar for want of a platform or standards
  source. Coverage matrix updated (five rows to Full; 466 pattern
  rows, Partial 67). 19 new source records (963 total). This run
  publishes the working tree left unpublished since the
  2026-11-15T05:55:50Z sync, including the parcel locker pickup
  kiosk-accessibility extension, the phone-side fitness workout
  logging, digital loyalty card wallet pass, online therapy
  booking, age assurance flow and museum timed-entry ticket
  booking rows, the translucent control material row, the Material
  Design 3 Expressive row, and actions 353-372. Open actions
  after this review: 252, 259, 265, 266, 268, 277, 279, 280, 285, 286, 287, 288, 289, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375.

- Completed this review (deep editorial 2026-11-16): extended
  the Electric vehicle charging session pattern row in
  `catalog/patterns.md` with advance-reservation rules — a
  future-availability query, a named charger booked for a stated
  window with the price shown before commitment, a check-in code
  or token presented at the charge point, a countdown to the
  window end, release-and-rebook when arrival slips, and no-show
  terms stated at booking — grounded in the open protocol
  specification for EV charging networks, which carries
  reservation details in its session records and a bounded
  authorisation token in its confirm step; the dentist
  appointment booking, concert and festival ticket booking, and
  online tutoring live class candidates were re-checked against
  fresh sources and all three stay below the source bar for want
  of a platform or standards source. Coverage matrix re-verified
  against the catalogue (466 pattern rows, all in Full; Full 476
  = 466 rows plus 10 layout-level items; Partial 67; no
  duplicates, no overlap). Three new improvement actions added
  (376 concert and festival ticket booking, 377 dentist
  appointment booking, 378 online tutoring live class), ordered
  by coverage impact, each a genuine gap with its source position
  stated; no new pattern rows for these three this review. 2 new
  source records (965 total). Held items from earlier reviews
  remain unpublished for want of a platform or standards source.
  Open actions after this review: 252, 259, 265, 266, 268, 277,
  279, 280, 285, 286, 287, 288, 289, 290, 291, 292, 294, 296, 297,
  299, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
  313, 314, 315, 318, 319, 327, 328, 329, 330, 331, 332, 333, 334,
  335, 336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352,
  355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367,
  368, 369, 370, 372, 373, 374, 375, 376, 377, 378.

- Completed this review (deep editorial 2026-11-17): source
  records restored and refreshed — the working copy of
  `resources/sources.json` was rebuilt from the published branch
  (963 records) after a local loss, the 10 records added since
  that publish were re-derived from fresh searches on the same
  grounding topics (2 open-protocol records for EV charging
  reservation, 2 season-ticket records, 2 peer-to-peer payment
  records, 2 driving-test booking records, 2 bag-drop records),
  and 2 new records added (EN 301 549 v4.1.1 final text; Modern
  Web Guidance 1.0), bringing the total to 975. The standards
  outlook was refreshed: EN 301 549 v4.1.1 citation in the
  Official Journal is now expected 22 January 2027, with the new
  user-preference clause, the rewritten information-about-products
  clause, and total-conversation real-time communication noted.
  Duplicate actions reconciled: 306 merged into 381, 311 into
  379, 319 into 380, with each pair's substance combined into the
  surviving action. Three new improvement actions added (382
  tiered permission gates and batch approval for the Agent
  checkpoint row, 383 appliance and device repair booking, 384
  home care visit booking), ordered by coverage impact, each a
  genuine gap with its source position stated; no new pattern rows
  for these three this review. Coverage matrix re-checked against
  the catalogue (468 pattern rows, all in Full; Full 478; Partial
  65; no duplicates, no overlap) and unchanged by this review.
  Open actions after this review: 252, 259, 265, 266, 268, 277,
  279, 280, 285, 286, 287, 288, 290, 291, 292, 294, 296, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 312,
  313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 334,
  335, 336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352,
  355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367,
  368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380,
  381, 382, 383, 384.

- Completed this review (deep editorial 2026-11-17): four new
  pattern rows in `catalog/patterns.md` — Smart-display voice screen,
  Hotel room service ordering, Concert and festival ticket booking,
  and Appliance and device repair booking — completing roadmap actions
  376 and 383; the smart-display and room-service rows had no action
  number, both were deep-cycle candidates. The fee-credit clause in
  action 383 was dropped as ungrounded. 13 new source records (989
  total). Duplicate actions reconciled: 266 merged into 341 (public
  library borrowing), 268 into 340 (ATM interface), 312 into 342
  (energy tariff comparison and switching), with each pair's substance
  combined into the surviving action; the card-return rule from 268
  was not carried over, since single-bank evidence contradicts it.
  Three new improvement actions added (385 ticket resale listing, 386
  repair information form, 387 recurring scheduled grocery order),
  ordered by coverage impact, each a genuine gap with its source
  position stated. Re-checked: dentist appointment booking (377)
  stays open — sector-association material covers fragments only,
  with no platform or standards source for the dental flow itself;
  grocery delivery-slot booking and weekly-basket reorder are already
  covered by the delivery slot picker, reorder past order, and
  subscribe-and-save rows, so no new row and no new action. Coverage
  matrix updated with the four new rows (472 pattern rows, all in
  Full; Full 482; Partial 65). This run also carries the publish of
  the working tree left unpublished since the 2026-11-17T08:20:00Z
  sync, including the agent-operable component library row and its
  source record. Open actions after this review: 252, 259, 265, 277, 279, 280, 285, 286, 287, 288, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 334, 335, 336, 340, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387.

- Completed this review (deep editorial 2026-11-17): one new
  pattern row in `catalog/patterns.md` — ATM interface — completing
  roadmap action 340; the row carries one-transaction-at-a-time
  confirmation with the fee shown, speech output and tactile keys
  for every step, multi-sense session warnings with an extension,
  and headphone privacy with the screen blanked, from the standards
  and design sources already recorded plus one new standards
  explainer. Actions 252, 259, and 265 re-checked with source
  positions updated; all three stay open. Four new source records
  (994 total). Three new improvement actions added (388 smartwatch
  sensitive-notification reveal, 389 pickup wait-time rules for the
  order tracking row, 390 multi-person, multi-day booking for the
  appointment management row), ordered by coverage impact, each a
  genuine gap with its source position stated. Coverage matrix
  updated (one row to Full; 473 pattern rows, all in Full; Full 483;
  Gap 64). This run also carries the publish of the working tree
  left unpublished since the 2026-11-17T14:49:19Z sync, including
  the server-supplied interfaces section in
  `trends/2026/agentic-ux.md` and its source record. Open actions
  after this review: 252, 259, 265, 277, 279, 280, 285, 286, 287,
  288, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305,
  307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331,
  332, 334, 335, 336, 341, 342, 343, 344, 346, 347, 348, 349, 350,
  352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
  367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380, 381,
  382, 384, 385, 386, 387, 388, 389, 390.

- Completed this review (deep editorial 2026-11-19): three new
  pattern rows in `catalog/patterns.md` — Laundry pickup and delivery,
  Dating app profile and matching, and Hot-desk and co-working booking
  — completing roadmap actions 395, 400, and 401. The laundry row
  rests on three corroborating guides (a laundry-app feature guide,
  a customer, driver, and admin feature guide, and a booking case
  study); the dating row on a design guide, a matching and chat
  guide, and a 2026 pattern roundup; the hot-desk row on a government
  booking design-patterns document plus two case studies. Three new
  improvement actions added (403 ferry booking, 404 volunteer shift
  signup, 405 weather app interface), ordered by coverage impact,
  each a genuine gap with its source position stated. Coverage
  matrix updated (three rows to Full; 476 pattern rows, all in Full;
  Full 486; Gap 61). 15 new source records (1040 total). Open actions
  after this review: 252, 259, 265, 277, 279, 280, 285, 286, 287, 288, 290, 291, 292, 294, 296, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 334, 335, 336, 341, 342, 343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 402, 403, 404, 405.

- Completed this review (daily planning 2026-11-19): three new
  improvement actions added (406 government citizen services
  portal, 407 smart home security camera, 408 theme park virtual
  queue reservation), ordered by coverage impact, each a genuine
  gap with its source position stated. Implementation is left to
  the deep cycle: the top action needs a full pattern row and a
  platform or standards source. Coverage matrix unchanged (476
  pattern rows, all in Full; Full 486; Gap 61). 9 new source
  records (1050 total). Open actions after this review: 252, 259,
  265, 277, 279, 280, 285, 286, 287, 288, 290, 291, 292, 294, 296,
  297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314,
  315, 318, 327, 328, 329, 330, 331, 332, 334, 335, 336, 341, 342,
  343, 344, 346, 347, 348, 349, 350, 352, 355, 356, 357, 358, 359,
  360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373,
  374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388,
  389, 390, 391, 392, 393, 402, 403, 404, 405, 406, 407, 408.

- Completed this review (deep editorial 2026-11-19): three new
  pattern rows in `catalog/patterns.md` — Drive-through and curbside pickup,
  Government citizen services portal, and Weather app interface —
  completing roadmap actions 252, 347, and 348, and the duplicate actions
  405 and 406 with them. The drive-through row rests on two pickup-process
  guides and drive-through ordering assistance legislation, with the
  non-voice exception route on already-recorded guidance; the portal row
  on a cross-government service-patterns specification, a local-service
  pattern taxonomy, and a citizen-portal planning guide; the weather row
  on the international alert standard, its national weather-service
  documentation, and a professional-body guide to forecast presentation.
  Reconciliation: eleven further open actions already had rows in
  `catalog/patterns.md` and are marked implemented this review (259
  laundry, 265 childcare, 277 dating, 280 gym, 286 hot-desk, 292 parking
  permit, 296 school admissions, 334 parcel sending, 341 library
  borrowing, 342 energy tariff, 346 video streaming player); the rows
  were added under later action numbers or without an action number and
  the original numbers were never marked. Action 290 (online will
  creation) carried an incorrect implemented marker although no row
  exists; the marker was removed and the action stays open. Three new improvement actions
  added (409 road toll and congestion charge payment, 410 student loan
  application, 411 travel insurance purchase), ordered by coverage
  impact, each a genuine gap with its source position stated. Coverage
  matrix updated (three rows to Full; 488 pattern rows; Full 498; Gap
  51). The counts in the two 2026-11-19 notes above were stale (476
  rows, Full 486, Gap 61); a recount this review gives 488 rows, Full
  498, Gap 51. 9 new source records (1059 total). Open actions after
  this review: 279, 285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 335, 336, 343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 402, 403, 404, 407, 408, 409, 410, 411.

- Completed this review (deep editorial 2026-11-19): four new
  pattern rows in `catalog/patterns.md` — Smart home security
  camera, Theme park virtual queue reservation, Road toll and
  congestion charge payment, and Agent-described interface —
  completing roadmap actions 407, 408, and 409. The camera row rests
  on a home-security app concept, a security dashboard case study, a
  privacy-focused surveillance redesign, and regulator guidance on
  domestic cameras; the virtual queue row on a theme-park app audit, a
  virtual queue feature case study, a park visit planning concept, the
  operator's own virtual queue page, and a visitor guide; the road
  toll row on an official city transport authority payment guide and
  two consumer payment guides; the agent-described row on the stable
  open protocol for agent-described screens and its project site. The
  held adaptive-quality item is resolved: the platform's developer
  blog post and the Tier 3 guideline page are recorded, a
  standards-outlook paragraph states the April and August 2027
  enforcement dates, and the tablet layout records the Tier 3 baseline
  as the testable bar. Three new improvement actions added (412 cinema
  ticket booking, 413 cruise booking, 414 driving licence renewal),
  ordered by coverage impact, each a genuine gap with its source
  position stated. Bag drop, home cleaning booking, and driving test
  booking were checked and already carry open actions (301, 402, 287),
  so no duplicate actions were created. Coverage matrix updated (four
  rows to Full; 492 pattern rows; Full 502; Gap 52). 16 new source
  records (1075 total). Open actions after this review: 279, 285, 287,
  288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309,
  310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 335, 336,
  343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363,
  364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379,
  380, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 402,
  403, 404, 410, 411, 412, 413, 414.

- Completed this review (deep editorial 2026-11-19): five new
  pattern rows in `catalog/patterns.md` — Cinema ticket booking,
  Driving licence renewal, Ferry booking, Student loan application,
  and Travel insurance purchase — completing roadmap actions 403,
  410, 411, 412, and 414. The cinema row rests on a live-event
  pricing rule, an accessible-seating ticketing rule, and venue
  accessibility guidance; the licence row on the national renewal
  service, the Northern Ireland renewal service, identity-checking
  guidance, and wallet documentation; the ferry row on a maritime
  passenger-rights regulation, the national enforcement-body guide,
  and corroborated operator booking conditions; the student loan row
  on government application and repayment-plan guidance from two
  countries; the travel insurance row on government guidance, a
  regulator's product-information guidance, statutory disclosure
  duties, and trade-body medical-conditions guidance. The cruise
  booking row stays open (413): no regulator, platform, or
  industry-body guidance specific to cruise booking interfaces was
  found. Three new improvement actions added (415 university
  admissions application, 416 council tax payment and discount
  application, 417 meal kit delivery subscription), ordered by
  coverage impact, each a genuine gap with its source position
  stated. Coverage matrix updated (five rows to Full; 497 pattern
  rows; Full 507; Gap 49). 33 new source records (1109 total). Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 335, 336, 343, 344, 349,
  350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365,
  366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380,
  381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 402,
  404, 413, 415, 416, 417.

- Completed this review (daily planning 2026-11-20): this run
  also carries the publish of the status-announcement rule left
  unpublished after the 2026-11-20T04:05Z light cycle, when the push
  was interrupted twice by a service restart — prefer the platform
  announcement call for one-off messages, match normal and high
  priority to polite and assertive live regions, and combine several
  updates into one message, with the live region kept as the
  fallback. No new pattern rows in this run: the top improvement
  (418 restaurant table reservation) is a pattern row that still
  needs a platform or standards source before it is written, so
  implementation stays with the deep cycle. Five new improvement
  actions added (418 restaurant table reservation, 419 tradesperson
  and plumber booking, 420 salon and spa appointment booking, 421
  wedding invitation RSVP, 422 water utility bill payment), ordered
  by coverage impact, each a genuine gap with its source position
  stated; the restaurant table reservation action rests on
  corroborated vendor reservation guides, the wedding invitation
  RSVP action on vendor invitation guides, and the water utility
  bill payment action on single-designer case studies and
  content-site guides. Duplicate meal kit delivery subscription
  actions consolidated: 417 superseded by 330, which carries the
  fuller specification. Driving test booking (287) re-checked: the
  national booking-rules consultation is still the latest government
  source and states booking policy only, with no interface rules,
  so the row stays open. Interface design patterns November 2026:
  agency trend roundups restate covered material (prompt bars,
  trust states for generated output, liquid glass control layers,
  progressive blur, expressive shapes, physics-based motion,
  command palettes, dark-first tokens, accessibility-first
  component states; the third-party iOS 27 guide restates platform
  guidance) — no new rule, no new source record. Coverage matrix
  unchanged (the five names already sit in the Gap column; 497
  pattern rows; Full 507; Gap 49). No new source records. Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 335, 336, 343, 344, 349,
  350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365,
  366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 379, 380,
  381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 402,
  404, 413, 415, 416, 418, 419, 420, 421, 422.

- Completed this review (deep editorial 2026-11-20): no new pattern
  rows — the five searches (home cleaning service booking, pet
  grooming appointment booking, restaurant waitlist management, car
  wash booking and membership, school lunch ordering) returned only
  single-designer concept case studies, agency blogs, content-site
  guides, a single-vendor marketplace case study, a shipped-product
  portfolio piece, and an app-store listing, all below the
  source-quality bar, so no new rule and no new source record.
  Duplicate-action audit: 22 pairs of pattern-row actions specify the
  same row twice; nine both-open pairs consolidated into the fuller
  original action with the distinctive rules carried across (402 into
  294, 418 into 370, 420 into 359, 419 into 369, 415 into 279, 404
  into 332, 422 into 373, 421 into 372, 416 into 310); three stale
  open actions closed as implemented through their duplicate numbers
  (335 through 407, 379 through 403, 380 through 408), with the camera
  and theme park rows extended to carry the consolidated rules; nine
  pairs already closed on both numbers and one pair already superseded
  (417 by 330), so no change there. Three new improvement actions
  added (423 service-provider booking intake, 424 multi-role
  availability, 425 book on behalf), ordered by coverage impact, each
  a genuine gap with its source position stated; the provider intake
  action rests on a single-designer concept case study and a
  single-vendor marketplace case study, the multi-role availability
  action on a single-vendor marketplace case study, and the
  book-on-behalf action on a shipped-product portfolio piece,
  single-designer concepts, and an app-store listing. Coverage matrix
  updated (three new Gap items; 497 pattern rows; Full 507; Gap 52).
  No new source records. Open actions after this review: 279, 285,
  287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307,
  308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332,
  333, 336, 343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360,
  361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374,
  375, 377, 378, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391,
  392, 393, 413, 423, 424, 425.

- Completed this review (deep editorial 2026-11-20): no new pattern
  rows — the six searches (university admissions application, home
  cleaning service booking, cruise booking, driving test booking,
  volunteer shift signup, pregnancy tracking) returned only agency
  and content-site guides, vendor booking-platform pages, travel
  guides and operator content, single-vendor scheduling products,
  single-designer case studies and portfolios, and an app-store
  listing, all below the source-quality bar, so no new rule and no
  new source record. Re-checks: driving test booking (287) gains new
  government sources — the national booking platform trial of July
  2026 and the 12 November 2026 booking-rules update — but both state
  booking policy and trial process with no interface rules, so the
  row stays open; cruise booking (413), university admissions
  application (279), volunteer shift signup (332), and pregnancy
  tracking (374) re-checked with their source positions updated and
  no new rule. Three new improvement actions added (426 volunteer
  shift cover and substitute request, 427 cruise embarkation and
  onboard check-in, 428 sensitive lifecycle change in a health
  tracker), ordered by coverage impact, each a genuine gap with its
  source position stated; the cover action rests on four
  corroborating single-vendor scheduling products, the embarkation
  action on travel guides and operator content, and the
  lifecycle-change action on a single-designer case study. Coverage
  matrix updated (three new Gap items; 497 pattern rows; Full 507;
  Gap 55). No new source records. Open actions after this review:
  279, 285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304,
  305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330,
  331, 332, 333, 336, 343, 344, 349, 350, 352, 355, 356, 357, 358,
  359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372,
  373, 374, 375, 377, 378, 381, 382, 384, 385, 386, 387, 388, 389,
  390, 391, 392, 393, 413, 423, 424, 425, 426, 427, 428.

- Completed this review (deep editorial 2026-11-20): no new pattern
  rows — the eight searches (split button, video doorbell visitor
  interface, school homework assignment tracking, neighbourhood
  noticeboard, digital business card sharing, food rescue and surplus
  food pickup, smart fridge food inventory, home EV charger
  scheduling) returned two design systems, an accessibility guide
  citing published success criteria, an agency article, and a pattern
  guide for the split button, single-designer case studies and a
  vendor school-management product page for the guardian alert, and a
  single-author development log, a single-vendor product page, and
  vendor blog posts for the bounded noticeboard; the video doorbell
  sources are a patent, vendor product pages, and retailer listings,
  the digital business card sources are single-vendor product pages
  only, the food rescue sources are hackathon projects and a
  single-designer portfolio, the smart fridge sources are a hackathon
  project, repository documentation, a single-designer portfolio, and
  a student project, and the home EV charger sources are vendor
  product pages, a vendor support page, an app-store listing, and a
  content site — all below the source-quality bar, so no new rule
  there and no new source record. The split-button gap noted by an
  earlier light cycle as a single agency piece is now corroborated by
  two design systems and the accessibility guide, so it crosses the
  bar. Three new improvement actions added (429 split button, 430
  guardian falling-behind alert, 431 bounded neighbourhood
  noticeboard), ordered by coverage impact, each a genuine gap with
  its source position stated; the split-button action rests on two
  design systems and an accessibility guide, the guardian alert on
  single-designer case studies and a vendor product page, and the
  bounded noticeboard on a single-author development log and vendor
  pages. Coverage matrix updated (two new Gap items; 505 pattern rows;
  Full 507; Gap 57; one new primitives gap: split button). No new
  source records. Open actions after this review: 279, 285, 287, 288,
  290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310,
  313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344,
  349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365,
  366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381, 382, 384,
  385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424, 425, 426,
  427, 428, 429, 430, 431.

- Completed this review (deep editorial 2026-11-21): one new section
  in `trends/2026/agentic-ux.md` — Show the track record before
  delegating — closing the held finding from the 2026-11-21 light
  cycle: before a kind of task is handed to an agent, show how often
  "done" was verified for that kind of task, measured from what
  happened rather than the agent's own report; permissions are earned
  one kind of action at a time, only a person raises the level,
  irreversible actions always ask, and an incident sends the rule
  back to asking. The section rests on two corroborating sources: a
  six-pattern guide (v1, updated November 2026) and a trust-ladder
  guide with the same earned-permission rule. 2 new source records
  (1115 total). Three new improvement actions added (432
  recipient-side agent action, 433 free-agent pool placement, 434
  multi-pet appointment booking), ordered by coverage impact, each a
  genuine new gap with its source position stated; the recipient-side
  action rests on the same six-pattern guide, the free-agent pool on
  vendor league-registration guides, and the multi-pet booking on
  vendor scheduling product pages. Coverage matrix updated (three
  new Gap items; 505 pattern rows; Full 507; Gap 60). Re-checked:
  community sports league team registration (307) stays open — fresh
  sources are vendor league-registration guides only; vehicle
  registration renewal and car tax payment (308) stays open — a
  government online-services page now corroborates the renewal flow
  (enter plate and reference, confirm vehicle details, fee shown
  before payment, receipt, reminder signup), but a second platform
  or standards source is still needed; pet grooming appointment
  booking (327) stays open — fresh sources are vendor scheduling
  product pages only; home solar energy monitoring (329) stays open
  — fresh sources are a community forum post, a content-site review,
  an agency case study, and a vendor page, the same insufficient
  class already recorded; volunteer shift signup (332) stays open —
  fresh sources are vendor scheduling pages and an open-source
  signup guide citing a university event-planning guide, the same
  insufficient class already recorded, and the substitute-request
  material already belongs to action 426. The held findings stay
  held; no new evidence surfaced in this run's searches. Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344, 349, 350,
  352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
  367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381, 382, 384,
  385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424, 425,
  426, 427, 428, 429, 430, 431, 432, 433, 434.

- Completed this review (daily planning 2026-11-21): no new pattern
  rows — the four searches (new interface types and UI updates
  November 2026, design-system component library releases November
  2026, driving test booking, children's pocket money and allowance)
  returned only material already assessed, held, or below the
  source-quality bar, so no new rule and no new source record. The
  November 2026 desktop operating-system update stays held pending a
  primary platform source, with secondary tech-news reports only;
  the single-vendor dashboard release and the single-developer
  game-authoring tool release are already assessed as covered
  classes with no new pattern rule; the design-system changelogs
  are already assessed as single-vendor releases of covered
  component classes with no new pattern rule, and the component
  library whose free components went open source on 21 November
  stays held as beta. Three new improvement actions added (435
  user-customizable menu rules, 436 booking change-allowance rules,
  437 discreet decline for supervised payments), ordered by coverage
  impact, each a genuine gap with its source position stated; the
  menu action rests on secondary reports of the November 2026
  operating-system update, the change-allowance action on the 2026
  government booking-rules update, and the discreet-decline action
  on shipped-product case studies of one family-finance product
  plus a vendor product page. The top improvement (435) is an
  extension that rests on secondary sources only, so implementation
  stays with the deep cycle. Re-checked: driving test booking (287)
  stays open — the booking-rules update and the official social
  posts state booking policy only, with no interface rules, and the
  student redesign adds notification and multi-centre search pain
  from a single-designer project only; children's pocket money and
  allowance (368) stays open — shipped-product case studies now
  corroborate parent authority, money-by-purpose rails, goal
  release on parental approval, and a quiet decline at the till,
  and a vendor product page corroborates schedule, category, and
  rollover controls, but the material is still one product plus a
  vendor page, below the bar. Coverage matrix unchanged (the three
  actions extend existing Full rows; 505 pattern rows; Full 507;
  Gap 60). No new source records. Open actions after this review:
  279, 285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304,
  305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330,
  331, 332, 333, 336, 343, 344, 349, 350, 352, 355, 356, 357, 358,
  359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372,
  373, 374, 375, 377, 378, 381, 382, 384, 385, 386, 387, 388, 389,
  390, 391, 392, 393, 413, 423, 424, 425, 426, 427, 428, 429, 430,
  431, 432, 433, 434, 435, 436, 437.

- Completed this review (deep editorial 2026-11-21): one open action
  implemented — 435 user-customisable menu rules, now in the Overflow
  menu row in `catalog/patterns.md`, grounded in the platform release
  notes for the October 2026 preview update (included in the November
  2026 security update) and a hands-on test of the November 2026
  update; the November update is now shipped, so the held item on it
  is resolved. The one-action restore of the default layout has no
  platform source and is not in the row. The single-vendor dashboard
  release, the single-developer game-authoring tool release, and the
  design-system changelogs are already assessed as covered classes
  with no new pattern rule, and the component library whose free
  components went open source on 21 November stays held as beta.
  Three new improvement actions added (438 per-display magnification
  rules, 439 connected-device prompt, 440 cloud device recovery),
  ordered by coverage impact, each a genuine gap with its source
  position stated; the per-display action rests on the same platform
  release notes, and the other two on those notes only, with a second
  independent source still needed before either row is written.
  Coverage matrix updated (two new Gap items; 505 pattern rows; Full
  508; Gap 61; the previous review note's Full 507 and Gap 60 counts
  were stale — the matrix itself already held Full 508 and Gap 59
  after the food-rescue move). Re-checked: driving test booking (287)
  and booking change-allowance rules (436) — the government
  booking-rules guidance page now states the change-counting rules in
  full and the ten-full-working-day refund cutoff, recorded as a new
  source record; the refund cutoff is corrected from three working
  days; both stay open, since no platform or standards source with
  interface rules has been found. The harmonised ICT accessibility
  standard citation stays held: trackers still disagree, one expecting
  16 December 2026 and another 22 January 2027, and the
  standards-outlook sentence now names both dates precisely. Five new
  source records (1120 total). Open actions after this review: 279,
  285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307,
  308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333,
  336, 343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362,
  363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378,
  381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423,
  424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438,
  439, 440.


- Completed this review (deep editorial 2026-11-21): one new rule
  in `catalog/states.md` — reserve the fully disabled presentation
  for actions that cannot be attempted at all, and keep a control
  reachable by keyboard with the reason beside it where the person
  needs to learn why it is unavailable; the comparison across eight
  design systems that grounds the rule is recorded as a new source
  record. The two near-duplicate Personalised news feed entries in
  `CHANGELOG.md` [Unreleased] are merged into one entry stating the
  rule, the row extension, and the source record once. Three new
  improvement actions added (441 energy supplier account, 442 car
  insurance quote and purchase, 443 water utility bill payment),
  ordered by coverage impact, each a genuine gap with its source
  position stated; the energy supplier action rests on a supplier app
  page, an agency guide, and two case studies, and the car insurance
  action on two corroborating redesign case studies, with a platform
  or standards source still needed before either row is written.
  Coverage matrix updated (two new Gap items; 505 pattern rows; Full
  508; Gap 63). One new source record (1122 total). Checked and left
  as covered or held: the platform design guidance page updated 6
  November 2026 (live-activity kits and new product bezels) and the
  touch-input guidance for desktop systems added 28 October 2026 both
  restate rules already in `layouts/desktop.md` and
  `catalog/patterns.md`, so no new rule and no new source record; the
  November 2026 component library changelogs already assessed are
  single-vendor releases of covered component classes with no new
  pattern rule, and the component library whose free components went
  open source on 21 November stays held as beta. The harmonised ICT
  accessibility standard citation stays held: trackers still
  disagree, one expecting 16 December 2026 and another 22 January
  2027. Open actions after this review: 279, 285, 287, 288, 290, 291,
  294, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313,
  314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344,
  349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364,
  365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381,
  382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423,
  424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437,
  438, 439, 440, 441, 442, 443.

- Completed this review (deep editorial 2026-11-21): no new pattern
  rows — the eight searches (driving test booking rules, pharmacy
  prescription refill, pet grooming appointment booking, home
  cleaning service booking, new interface types and design system
  releases, online will creation, online prize draw and raffle entry,
  smart baby monitor) all restate material already recorded or stay
  below the bar, so no new row and no new pattern rule. Three new
  improvement actions added (444 medication refill eligibility, 445
  smart baby monitor alert triage, 446 prize draw transparency),
  ordered by coverage impact, each a genuine gap with its source
  position stated; the medication refill action refines the request
  list so a blocked prescription stays visible with its eligibility
  state and secondary actions, the baby monitor action adds
  urgent-at-once and routine-to-digest alert triage, and the prize
  draw action adds a published entry list, a stated draw method with
  a verifiable trail, and a named winner-contact fallback. Driving
  test booking (287) re-checked: the transport department bulletin
  announcing the new rules now in effect adds that booking through a
  third party is against the law and that online access can be
  restricted where licence details are misused, recorded as a new
  source record; the row stays open. Coverage matrix unchanged (505
  pattern rows; Full 508; Gap 63). One new source record (1123
  total). Checked and left as covered or held: the November 2026
  platform update already assessed and closed as covered, with its
  context-menu rule already published; the November 2026 single-vendor
  release guides and design system changelogs already assessed are
  releases of covered component classes with no new pattern rule;
  pet grooming (327), home cleaning (294), and online will creation
  (290) already carry the substance of the fresh sources, and the
  prize draw free-route rules are already carried by action 302, so
  no new action for those; the harmonised ICT accessibility standard
  citation stays held, trackers still disagreeing on 16 December
  2026 and 22 January 2027. Open actions after this review: 279,
  285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305,
  307, 308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331,
  332, 333, 336, 343, 344, 349, 350, 352, 355, 356, 357, 358, 359,
  360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 372, 373,
  374, 375, 377, 378, 381, 382, 384, 385, 386, 387, 388, 389, 390,
  391, 392, 393, 413, 423, 424, 425, 426, 427, 428, 429, 430, 431,
  432, 433, 434, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445,
  446.

- Completed this review (deep editorial 2026-11-22): one new pattern
  row in `catalog/patterns.md` — Multiplayer game lobby and
  matchmaking — grounded in platform multiplayer documentation with
  two corroborating guides; three new source records (1126 total).
  The Loyalty rewards row in `catalog/patterns.md` was missing its
  closing table cell and is fixed. Three new improvement actions
  added (447 university admissions application, 448 airport
  self-service bag drop, 449 home broadband installation and router
  setup), ordered by coverage impact, each a genuine gap with its
  source position stated. Coverage matrix updated (one row to Full;
  pattern rows re-based on a direct count of table data rows: 498
  after this review, where earlier notes carried 505; Full 509; Gap
  62). Checked and left as covered or held: the November 2026
  platform update already assessed and closed as covered, with its
  context-menu rule already published; the November 2026
  single-vendor release guides and design system changelogs already
  assessed are releases of covered component classes with no new
  pattern rule; the university admissions, bag drop, and broadband
  topics stay below the bar for a row (single-designer case study,
  agency guides, vendor pages, and content blogs only) and are
  recorded as actions instead; the harmonised ICT accessibility
  standard citation stays held, trackers still disagreeing on 16
  December 2026 and 22 January 2027. Open actions after this
  review: 279, 285, 287, 288, 290, 291, 294, 297, 299, 301, 302,
  303, 304, 305, 307, 308, 309, 310, 313, 314, 315, 318, 327, 328,
  329, 330, 331, 332, 333, 336, 343, 344, 349, 350, 352, 355, 356,
  357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369,
  370, 372, 373, 374, 375, 377, 378, 381, 382, 384, 385, 386, 387,
  388, 389, 390, 391, 392, 393, 413, 423, 424, 425, 426, 427, 428,
  429, 430, 431, 432, 433, 434, 436, 437, 438, 439, 440, 441, 442,
  443, 444, 445, 446, 447, 448, 449.

- Completed this review (daily planning 2026-11-22): no new pattern
  rows — the five searches (new interface types and UI updates
  November 2026, design-system component library releases November
  2026, wedding registry and gift list, council tax payment and
  discount application, pet adoption application) returned only
  material already assessed, held, or below the source-quality bar
  for a row, so no new rule. The November 2026 desktop
  operating-system update stays closed as covered, with its
  context-menu rule already published; the single-vendor dashboard
  release and the single-developer game-authoring tool release are
  already assessed as covered classes with no new pattern rule; the
  design-system changelogs are already assessed as single-vendor
  releases of covered component classes with no new pattern rule.
  Three new improvement actions added (450 council tax payment and
  discount application, 451 wedding registry and gift list, 452 pet
  adoption application), ordered by coverage impact, each a genuine
  gap with its source position stated; the council tax action rests
  on council service pages, the registry action on a vendor
  tutorial, an agency case study of one registry service, and a
  single-designer project, and the pet adoption action on
  single-designer case studies. The top improvement (450) still
  needs a platform or standards source before the row is written,
  so implementation stays with the deep cycle. 7 new source records
  (1133 total). Coverage matrix unchanged (the three names already
  sit in the Gap column; 498 pattern rows; Full 509; Gap 62). Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344, 349, 350,
  352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
  367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381, 382, 384,
  385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424, 425,
  426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438, 439,
  440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452.


- Completed this review (deep editorial 2026-11-22): no new pattern
  rows — the six searches (smartwatch fall detection and emergency
  SOS, digital wallet add-card and tap-to-pay setup, home EV charger
  scheduling, smart fridge and food inventory, pregnancy tracking,
  book on behalf) returned only material already covered, held, or
  below the source-quality bar for a row, so no new rule. The fall
  detection and wallet topics are already published as pattern rows
  (Smartwatch fall detection and emergency SOS; Digital wallet
  add-card and tap-to-pay setup), and the charger, fridge, and
  pregnancy topics rest on single-designer case studies, agency
  guides, vendor pages, and an open-source user guide only, with no
  platform or standards source. Three new improvement actions added
  (453 book on behalf, 454 tablet worked example, 455 landing worked
  example), ordered by coverage impact, each a genuine gap with its
  source position stated; the book on behalf action rests on vendor
  help pages and a vendor proxy-booking guide, and the two worked
  example actions close the tablet and landing example gaps. Duplicate
  actions consolidated: 447 superseded by 279, 450 superseded by 310,
  451 superseded by 285, 452 superseded by 304, and 443 superseded by
  373, with each twin's unique points folded into the surviving
  action so no substance is lost. Coverage matrix unchanged (the book
  on behalf name already sits in the Gap column and the worked
  examples close example gaps rather than pattern gaps; 498 pattern
  rows; Full 509; Gap 62). 9 new source records (1142 total). Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307,
  308, 309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333,
  336, 343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362,
  363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378,
  381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423,
  424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438,
  439, 440, 441, 442, 444, 445, 446, 448, 449, 453, 454, 455.

- Completed this review (deep editorial 2026-11-22): no new pattern rows
  — the six searches (cruise booking, pet grooming appointment booking,
  volunteer shift signup, home broadband installation and router setup,
  online will creation, timed cart-hold) returned only material already
  covered, held, or below the source-quality bar for a row, so no new
  rule; the broadband, will, and cart-hold topics rest on provider help
  pages, commissioned comparisons, a vendor builder page, and a platform
  support doc only, with no platform or standards source. Two worked
  examples added (`examples/tablet/` and `examples/landing/`), closing
  roadmap actions 454 and 455. Three new improvement actions added (456
  cruise booking, 457 pet grooming appointment booking, 458 volunteer
  shift signup), ordered by coverage impact, each a genuine gap with its
  source position stated. Coverage matrix updated (worked-examples row
  gains tablet and landing; 498 pattern rows; Full 509; Gap 62). 9 new
  source records (1152 total). Open actions after this review: 279, 285,
  287, 288, 290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307, 308,
  309, 310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 336,
  343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363,
  364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381,
  382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424,
  425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438, 439,
  440, 441, 442, 444, 445, 446, 448, 449, 453, 456, 457, 458.

- Completed this review (deep editorial 2026-11-23): no new pattern
  rows — the six searches (connected-device prompt, smartwatch
  sensitive-notification reveal, multi-pet appointment booking, device
  authorisation grant, smart baby monitor, salon and spa appointment
  booking) returned only material already covered, held, or below the
  source-quality bar for a row, so no new rule. The connected-device
  prompt rests on the device authorisation standard with convergent
  vendor help pages, and the multi-pet booking rests on four
  booking-platform help pages with tightly convergent rules; both are
  genuine gaps recorded as actions below. The smartwatch topic was
  already open as action 388, so the prepared duplicate was not added
  as a new action: its substance was folded into 388 with a
  source-position update, and the re-check confirms the rules 388
  already states. The baby monitor topic rests on vendor pages only
  and the salon topic on a booking-app template and agency guides
  only, with no platform or standards source for either. Three new
  improvement actions added (459 connected-device prompt, 460
  multi-pet appointment booking, 461 smart baby monitor), ordered by
  coverage impact, each a genuine gap with its source position stated.
  Coverage matrix unchanged (the three names already sit in the Gap
  column; 499 pattern rows; Full 510; Gap 62). 13 new source records
  (1166 total). Open actions after this review: 279, 285, 287, 288,
  290, 291, 294, 297, 299, 301, 302, 303, 304, 305, 307, 308, 309,
  310, 313, 314, 315, 318, 327, 328, 329, 330, 331, 332, 333, 336,
  343, 344, 349, 350, 352, 355, 356, 357, 358, 359, 360, 361, 362,
  363, 364, 365, 366, 367, 368, 369, 370, 372, 373, 374, 375, 377,
  378, 381, 382, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393,
  413, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434,
  436, 437, 438, 439, 440, 441, 442, 444, 445, 446, 448, 449, 453,
  456, 457, 458, 459, 460, 461.

- Completed this review (deep editorial 2026-11-23): no new pattern
  rows — the five searches (agent run controls, disabled-button
  reason, smart home stale state, two-intent recommendation
  dismissal, university admissions application) returned no new rule
  for a row: the run-controls and two-intent dismissal topics are
  genuine gaps recorded as actions below, and the stale-state topic
  extends the smart home dashboard row as action 467. The
  disabled-button reason rests on a design-system guide and two
  practitioner pieces that restate the disabled-state rules already
  in `catalog/states.md` (keep the control focusable, place the
  reason beside it in helper text, never carry the reason by dimming
  alone), so it stays held with no new rule. The university
  admissions topic rests on vendor platform help pages only, with no
  platform or standards source, so it stays held. The EN 301 549
  citation date was re-checked against the light-cycle record and
  stays disputed between trackers. Three new improvement actions
  added (465 agent run controls, 466 recommendation feedback with
  two-intent dismissal, 467 smart home stale-state rules), ordered by
  coverage impact, each a genuine gap with its source position
  stated. Coverage matrix updated (two new Gap items; 499 pattern
  rows; Full 510; Gap 65). 12 new source records (1187 total). Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344, 349, 350,
  352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
  367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381, 382, 384,
  385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424, 425,
  426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438, 439,
  440, 441, 442, 444, 445, 446, 448, 449, 453, 456, 457, 458, 459,
  460, 461, 462, 463, 464, 465, 466, 467.

- Completed this review (deep editorial 2026-11-23): four new
  pattern rows in `catalog/patterns.md` — Agent run controls,
  Recommendation feedback, Note-taking app, and Job search discovery
  — completing roadmap actions 465 and 466; the overflow menu row
  extended with the restore-earlier-layout rule, completing action
  463; the automotive worked example added under
  `examples/automotive/`, completing action 464; the electric
  vehicle charging session row extended with plug-and-charge rules
  and the audiobook library app row extended with cross-device
  position sync, with the podcast app playback interface row
  pointing to the same rules; the Section 504 paragraph in
  `trends/2026/standards-outlook.md` refreshed to record that the
  comment period closed 6 July 2026 and the extension faces a court
  challenge. Three new improvement actions added (468 app-free
  parking checkout, 469 real-estate map keyboard rules, 470 EN 301
  549 citation re-check), ordered by coverage impact, each a genuine
  gap with its source position stated. The EN 301 549 citation date
  was re-checked against fresh tracker results and stays disputed
  between 16 December 2026 and 22 January 2027; the Title II dates
  were re-checked against the published regulation text and match
  the outlook as written. Actions 462 and 467 stay open, still
  waiting on a platform or standards source. Corrected the previous
  review's source count from 11 to 12 records (1187 total) — the
  count in the pending entry was one short. Coverage matrix updated
  (two Gap items to Full and two further new rows; 503 pattern rows;
  Full 514; Gap 63). 14 new source records (1201 total). Open
  actions after this review: 279, 285, 287, 288, 290, 291, 294, 297,
  299, 301, 302, 303, 304, 305, 307, 308, 309, 310, 313, 314, 315,
  318, 327, 328, 329, 330, 331, 332, 333, 336, 343, 344, 349, 350,
  352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
  367, 368, 369, 370, 372, 373, 374, 375, 377, 378, 381, 382, 384,
  385, 386, 387, 388, 389, 390, 391, 392, 393, 413, 423, 424, 425,
  426, 427, 428, 429, 430, 431, 432, 433, 434, 436, 437, 438, 439,
  440, 441, 442, 444, 445, 446, 448, 449, 453, 456, 457, 458, 459,
  460, 461, 462, 467, 468, 469, 470.
