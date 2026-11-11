# Changelog

All notable changes are recorded here. Format: newest first, grouped by
version, with Added, Changed, and Fixed sections where they apply.

## [Unreleased]

### Added

- Patterns catalogue: Blood donation appointment booking and
  Virtual court hearing rows added to `catalog/patterns.md`: the
  blood donation row checks eligibility first with the next
  eligible date named, offers whole blood, plasma, and platelets
  before the centre, remembers a preferred centre with hours and
  directions, lets the health questionnaire be answered before
  arrival, books, moves, and cancels from one place, and reminds
  the person before the appointment and when the next donation is
  due; the court hearing row states the hearing is formal with
  the same rules as in person, sends the join link with the
  notice, offers a test call, holds the person in a waiting room
  until the court opens the hearing with name and role visible,
  keeps the microphone muted when not speaking, states the
  recording rule at joining, and gives a phone route and a
  reconnection route. Coverage matrix updated. 6 new source
  records (768 total).

- Roadmap: three new improvement actions added (287 driving test
  booking, 288 home broadband installation and router setup, 289
  public transport season ticket purchase), ordered by coverage
  impact; coverage matrix Partial list updated with the three new
  named items and with the two completed items (282 blood donation
  appointment booking, 283 virtual court hearing) moved to Full.
  ATM interface (268) and museum timed-entry ticket booking (278)
  re-checked against deeper sources and stay open — no platform or
  standards source for the remaining elements.

- Roadmap: five new improvement actions added (282 blood donation
  appointment booking, 283 virtual court hearing, 284 proctored
  exam, 285 wedding registry and gift list, 286 hot-desk and
  co-working booking), ordered by coverage impact; coverage matrix
  Partial list updated with the five new named items and with the
  five open named items from earlier reviews (277 dating app
  profile and matching, 278 museum timed-entry ticket booking, 279
  university admissions application, 280 gym and fitness class
  booking, 281 job application portal) that were missing from it.
  No new source records.

- Patterns catalogue: Benefits claim application row added to
  `catalog/patterns.md`: the row starts from the life event or
  need rather than the programme name, lets one application cover
  every programme the person may qualify for with each answer
  shared across programmes, shows eligibility as answers are
  given, lets anyone check eligibility without an account, asks
  questions in plain language a small set per screen with help
  beside the question, saves at every step, lets the application
  be sent with documents still missing where what is needed and
  its due date are named, and states the decision wait and first
  payment date before submission with tracking by named stages.
  Coverage matrix updated. 5 new source records (762 total).

- Patterns catalogue: Mobile cheque deposit and Home energy usage
  dashboard rows added to `catalog/patterns.md`: the cheque row
  asks for the restrictive endorsement before capture, gives
  capture guidance that keeps all four corners and the printed
  line legible, matches the entered amount against the amount read
  from the image, states the cut-off time before sending, and
  tells the person to keep the paper cheque until the deposit is
  confirmed; the energy row shows use over time with cost beside
  it in money as well as in units, breaks use down by appliance
  or circuit where the meter supports it, compares against a
  previous period, and alerts when use or cost passes a threshold
  the person set. Coverage matrix updated. 4 new source records
  (757 total).

- Patterns catalogue: Visa application, Parking fine payment and
  appeal, and Phone voice menu rows added to
  `catalog/patterns.md`: the visa row starts from the trip itself
  with purpose and dates before the detail that depends on them,
  gives a document checklist with what each document must show,
  offers a biometrics appointment at a stated place within a
  stated window, states the decision wait and tells the person not
  to book travel until the decision arrives, tracks by named
  stages, and states the reason and the challenge route with its
  time limit where refused; the parking fine row states the fine
  amount, the reduced amount and its deadline, and the evidence
  window at once, lets the person pay by the notice reference and
  vehicle registration without an account, keeps payment and
  appeal side by side, and states plainly that paying counts as
  an admission and closes any open challenge; the phone voice menu
  row offers a reserved digit or word that skips the menu at any
  time and names it in the first option, uses plain words with
  each option stated before its number, waits for slow speakers,
  and moves the person to a human where the menu cannot serve the
  task or an error persists. Coverage matrix updated. 9 new source
  records (750 total).

- Examples: worked examples for the authentication and settings
  layouts added under `examples/`: the authentication example
  demonstrates the sign-in form with a show-and-hide control, the
  passkey-first route with a visible fallback chain, the
  second-factor code step with a resend control and a backup-code
  route, and the recovery route, with wrong-code and lockout
  variants; the settings example demonstrates grouped preferences
  with scope labels, a stated save behaviour, settings search, and
  a danger zone for irreversible actions, with a failed-save
  variant that keeps the entered values. Roadmap actions 274 and
  275 completed.

- Roadmap: actions 252, 259, 265, 268, and 271 updated with new
  source findings — platform guidance for simplified in-car
  ordering and a confirmation step for 252, government guidance
  for the visit before committing and the child's age as a first
  factor for 265, a regulator consultation paper for denomination
  stocking and receipt-on-request in part for 268, and verification
  of the 2010 programme document as consultation proposals for
  271; 3 new source records for the re-checked actions (753
  total). Three new improvement actions added (276 mobile cheque
  deposit, 277 dating app profile and matching, 278 museum
  timed-entry ticket booking); coverage matrix updated (three new
  rows to Full; Authentication and Settings moved from
  worked-example gaps to Full).

- Patterns catalogue: Virtual try-on row added to `catalog/patterns.md`: items that can be tried on are marked, the try-on entry sits on the product view and applies the item at once, size and colour choice and the add-to-cart control stay on the try-on screen, the camera is asked for only when a try-on starts with the trade stated first and a manual-measurement or size-chart route where the camera is refused or unavailable, a store mirror keeps catalogue and fitting separate with chrome at the edges, gestures are kept low and brief with a touch or phone route beside them, the starting point is marked with short on-screen guidance, and measurement is treated as private with an at-home route. Choice items are laid out as a grid and instruction text is kept dark on a light ground. Coverage matrix updated. 2 new source records (740 total).

- Patterns catalogue: Pension dashboard row added to `catalog/patterns.md`: the total saved so far sits beside the projected retirement income stated in today's money, every income source (state, workplace, private) is combined into one total and one projection, detail is layered (total and projection first, breakdown by source second, plan specifics third), a calculator shows how changing the retirement age moves the projection with optimistic, neutral, and pessimistic outcomes and stated assumptions, lost accounts can be located, money terms are in plain words with bar charts for comparison, and a dashboard that cannot change figures says so and points to where the change is made. Coverage matrix updated. 1 new source record (741 total).

- Patterns catalogue: Government document application, Mortgage
  application, and Smartwatch fall detection and emergency SOS rows
  added to `catalog/patterns.md`: the document-application row
  states eligibility, fee, and timescale first, uses a stepped form
  with save and return, asks for documents only when the step needs
  them with capture guidance before upload, confirms identity
  through a stated route, shows a review before submission, states
  before submission that the current document becomes invalid on
  submission, and tracks by named stages with dates; the mortgage
  row gives an affordability estimate before detail with a
  rate-rise view, shows the full document checklist first,
  acknowledges complete and incomplete applications with the
  missing documents named, gives the decision within a stated time
  or the reasons and expected timeframe, gives refusal reasons in
  writing, and tracks by named stages; the fall-detection row taps
  the wrist and sounds an alarm on a hard fall, waits where the
  wearer is moving, starts a stated countdown with a large cancel
  control where the wearer stays still, calls emergency services
  on its own with location and a recorded message when the
  countdown ends, and offers a press-and-hold manual SOS that
  cancels on release. Coverage matrix updated. 15 new source
  records (738 total). Roadmap actions 263, 270, and 272 completed.

- States catalogue: four rules from the current accessibility
  standard added to `catalog/states.md`: a single-pointer route
  without dragging for every dragging movement, help entries
  keeping the same relative order across pages, no repeated entry
  of information already given in the same process, and sign-in
  steps that never require remembering a password or solving a
  puzzle without an alternative or an assisting mechanism. The
  source record for the standard is included in the 15 above.

- Roadmap: action 252 updated with a city disability office's
  drive-through guidelines now covering the exception route
  directly, and actions 264, 268, and 271 updated with new source
  findings — the shared document-application flow for 264, fee
  disclosure and receipt rules for 268, and an energy-regulator
  programme document for 271; 1 new source record for the
  drive-through guidelines. Three new improvement actions added
  (273 phone voice menu, 274 authentication worked example, 275
  settings worked example); coverage matrix updated (Cooking mode
  added to Full; Passport renewal moved from Partial to Full;
  Home energy usage dashboard and Phone voice menu added to
  Partial; Authentication and Settings added as worked-example
  gaps).

- Patterns catalogue: Cooking mode row added to `catalog/patterns.md`: one large readable step at a time with visible progress and previous and next controls that always work, quantities in the instruction or one tap away, several labelled timers at once, the screen kept awake only while cooking is in progress with the benefit stated plainly, the current step and every timer saved on the device and restored after backgrounding or sleep, and voice actions confirmed before changing a timer or moving a step with a touch route always kept. 1 new source record (722 total).

- Patterns catalogue: Temporary home access code and Car rental
  and car sharing booking rows added to `catalog/patterns.md`:
  the access-code row creates a code for one person and one door
  with the validity window stated as a date and time range or a
  recurring slot, sends the code to the person it is for with its
  limits stated, offers single-use codes for deliveries or service
  visits, keeps a list of everyone with access and their
  authorised periods, revokes at once when a code is lost or no
  longer trusted, and keeps a plain entry record; the car rental
  row states the full cost including every compulsory charge and
  the deposit and excess before payment, the fuel policy and the
  fuel or charge level at handover, the pickup window and the
  return procedure with inspection timescales, a condition check
  with a diagram and photographs at pickup and return, and a
  damage-dispute route with the right to challenge and a
  reasonable time to challenge before the charge is taken.
  Coverage matrix updated. 4 new source records (721 total).
  Roadmap actions 247 and 267 completed.

- Patterns catalogue: Passkey sign-in, Code scanner, and
  Conversation mute rows consolidated in `catalog/patterns.md`:
  the two Passkey sign-in rows, the Code scanner and Code scanning
  rows, and the Conversation mute and Mute conversation rows each
  become one row keeping the union of their rules, with
  cross-references updated in the Scan-to-pay, QR code payment at
  a till, and Mobile plan setup rows. Coverage matrix updated;
  399 unique rows remain.

- Roadmap: three new improvement actions added (270 mortgage
  application, 271 home energy usage dashboard, 272 smartwatch
  fall detection and emergency SOS), ordered by coverage impact;
  each states its done condition and the files it touches, and
  notes that a platform or standards source is still needed before
  the row is written. Coverage matrix Partial list corrected —
  the three named gaps from the last review (passport renewal,
  visa application, childcare booking) were missing and are now
  listed, and the car rental item moved to full. No new source
  records for the actions themselves. Open actions 252, 259, 263,
  264, 265, 266, 268, and 269 re-checked against deeper sources
  and still below the source-quality bar, with their source notes
  updated where partial qualifying material turned up.

- Roadmap: four new improvement actions added (266 public library
  borrowing, holds and renewals, 267 car rental and car sharing
  booking, 268 ATM interface, 269 parking fine payment and
  appeal), ordered by coverage impact; each states its done
  condition and the files it touches, and notes that a platform
  or standards source is still needed before the row is written.
  Coverage matrix Partial list updated with the four new named
  items. No new source records (717 total). Open actions 247, 252,
  259, 263, 264, and 265 re-checked against fresh searches and
  still below the source-quality bar; home insurance claim
  submission is covered by the existing Insurance claim submission
  row, so no new action for it.

- Patterns catalogue: Veterinary appointment booking, Rental
  property viewing and tenancy application, Insurance claim
  submission, and Tax filing and self-assessment rows added to
  `catalog/patterns.md`: the vet row starts from the animal's saved
  profile, offers video only for minor concerns where a care
  relationship already exists, states the fee when booking, and
  sends a history form ahead of the visit; the rental row pairs
  scannable listing cards with a step-based application that asks
  only for what the decision needs; the insurance row states what
  the claim needs, how long there is to file, and the decision and
  settlement times at notification; the tax row takes the return
  one section at a time with save-and-resume and a review step
  before sending. Coverage matrix updated. 8 new source records
  (717 total). Roadmap actions 258, 260, 261, and 262 completed.

- Patterns catalogue: Crowdfunding campaign page row in
  `catalog/patterns.md` extended: keep reward tiers few and
  comparable, treat every delivery date as an estimate, explain
  the fulfilment plan on the page, and update backers regularly
  and at the first sign of a roadblock with status, cause,
  response, new timeline, and next steps. Roadmap action 237
  completed.

- Patterns catalogue: Accessibility labels on a store listing row
  in `catalog/patterns.md` extended: one fixed set of labels with
  the same wording and order on every listing, claimed only
  against the published criteria for that feature and tested on
  every device the app supports. The source was already recorded.
  Roadmap action 244 completed.

- Worked examples: Checkout worked example added under
  `examples/`: a worked example demonstrating the ecommerce
  layout and the checkout pattern rows — guest checkout, saved
  payment method selection, delivery slot picker, and promo-code
  entry — with all seven states. Roadmap action 154 completed.

- Patterns catalogue: Document signing row in
  `catalog/patterns.md` extended: where the signature is a ticked
  box or a typed name rather than a drawn mark, state plainly
  before signing that it carries the same effect as a handwritten
  signature, ask the signer to confirm they understand that
  before the signature is applied, and place guidance about
  signing in the journey before the signing step. 1 new source
  record (709 total).

- Patterns catalogue: Pass and ticket display row in
  `catalog/patterns.md` extended: where the platform allows actions
  on the pass, at most two relevant actions appear below the pass
  face, each labelled with what it does and kept about the pass
  itself. 1 new source record (708 total).

- Patterns catalogue: Recurring donation, Indoor wayfinding,
  Hotel room controls, and University course registration rows
  added to `catalog/patterns.md`: the donation row answers what
  the work is and how donations are used on the same page, keeps
  the donation action findable, presents the recurring choice as
  an equally weighted option beside the one-time gift, and states
  the recurring terms in full at the point of commitment; the
  wayfinding row uses one name per destination across directory,
  signs, and maps, with raised characters and contracted Braille
  on room signs and visual characters sized to viewing distance;
  the room-controls row places controls within reach, operable
  with one hand and no more than 5 pounds of force, grouped by
  what they do with the state shown in words; the registration
  row plans first and registers second from a saved plan,
  surfaces clashes, missing prerequisites, and full sections
  while planning, and leads a failed step directly to its fix.
  Coverage matrix updated. 8 new source records (707 total).
  Roadmap actions 246, 250, 254, and 257 completed.

- Roadmap: improvement-actions list reconciled with the
  catalogue (roadmap action 239): 76 actions marked implemented,
  66 of them implemented in earlier runs without the marker;
  actions 120, 242, 243, 245, 248, and 253 already carried a
  variant marker and were left as written. Four partly-
  implemented actions completed: 20 (form validation timing:
  single-invalid-field focus and input retention after a failed
  submission), 21 (contextual guidance rules in the Onboarding
  row and `layouts/onboarding.md`), 22 (empty-state fallback
  rule in `catalog/states.md`), and 57 (no-results recovery rule
  in the Search row). Three new improvement actions added (260
  rental property viewing and tenancy application, 261 insurance
  claim submission, 262 tax filing and self-assessment).
  Coverage matrix updated with the new named gaps.

- Patterns catalogue: Real-time departure board row added to
  `catalog/patterns.md`: the board stays static with departures
  grouped by transport kind, shows bus and tram times as a
  countdown and train times as clock times, states delays as
  added minutes, and marks disruptions in shape and words as
  well as colour. Coverage matrix updated. 1 new source record
  (698 total).

- Patterns catalogue: Care decision card row added to
  `catalog/patterns.md`: three urgency tiers — routine, urgent,
  emergency — each with one action heading followed by a short
  symptom list, urgency stated in words rather than colour alone,
  one signposted service per heading, and cards ordered by
  likelihood and seriousness. Coverage matrix updated. 1 new source
  record (699 total).

- Patterns catalogue: Self-checkout grocery kiosk, School
  parent portal, and Live translated captions rows added to
  `catalog/patterns.md`: the kiosk keeps a running total visible
  with each scanned item priced as it is added, holds
  age-restricted items aside for a check without blocking the
  shop, warns before any time limit in more than one sense with
  a way to extend it, and offers spoken guidance with a private
  listening route and tactile keys; the portal keeps each child
  separate, reaches guardians by invitation with daily or weekly
  summaries that carry no grades, and lets a guardian unsubscribe
  or remove themselves at any time; translated captions keep the
  translated text beside the speaker's words, state the source
  and target languages, and never store caption text unless a
  transcript is asked for. Coverage matrix updated. 3 new source
  records (697 total). Roadmap actions 249, 251, and 255
  completed. Three new improvement actions added (257 university
  course registration, 258 veterinary appointment booking, 259
  laundry pickup and delivery).

- Patterns catalogue: Keyless shared-car pickup row added to
  `catalog/patterns.md`: the booking states whether the car opens
  by phone or by card before the person leaves home, check-in
  opens a stated time before the booking starts, one clear unlock
  step with a visible failure state and a retry, lock and unlock
  work without a signal, a guided condition check with a fault
  report before driving off, extra drivers activate on their own
  phones, and the trip ends with a lock confirmation and a summary
  of time, distance, and cost. Coverage matrix updated. 1 new
  source record (694 total).

- Patterns catalogue: Flight disruption compensation claim row
  added to `catalog/patterns.md`: eligibility bands with the
  fixed amount for each distance band shown before the claim is
  sent, flight and booking details carried from the booking,
  compensation, expenses, and refund kept as separate amounts,
  an evidence file the person can add to after sending, claim
  states from sent to paid, a case reference given at once, and
  a route to the national enforcement body where the carrier
  does not answer. Coverage matrix updated. 2 new source
  records (693 total). Roadmap action 256 completed.

- Patterns catalogue: Ballot row added to `catalog/patterns.md`:
  sentence case and left-aligned text, candidates in a single
  column with contests clearly separated, instructions at the
  start in plain words stating the result before the action, a
  grid or column layout for ranked choices rather than
  hand-numbered entry, a review screen before casting, a plain
  invalid-selection notice, a cast confirmation, and large-print
  and tactile options for the same ballot. Coverage matrix
  updated. 3 new source records (691 total).

- Patterns catalogue: Health record sharing and E-reader and
  reading app rows added to `catalog/patterns.md`: sharing a
  health record states the scope and the expiry before sharing,
  protects a link or code with a separately shared passcode,
  and keeps a revoke control with a record of who had access
  and when; the reading app keeps type, spacing, and margin
  choices between sessions, keeps the reading position across
  devices, and offers chapter navigation, word lookup without
  losing the page, and a low-glare mode. Coverage matrix
  updated. 5 new source records (688 total). Roadmap actions
  248 and 253 completed.

- Desktop worked example added under `examples/desktop/`: a
  menu bar, toolbar, two panes with drag-and-drop and a
  keyboard path, window strip, status bar, and all seven
  states, demonstrating the desktop layout rules. Coverage
  matrix updated. Roadmap action 245 completed.

- Roadmap: three new improvement actions added (254 hotel room
  controls, 255 school parent portal, 256 flight disruption
  compensation claim), ordered by coverage impact; each states
  its done condition and the files it touches, and notes that a
  platform or standards source is still needed before the row
  is written.

- Roadmap: five new improvement actions added (249 self-checkout
  grocery kiosk, 250 indoor wayfinding, 251 live translated
  captions, 252 drive-through and curbside pickup, 253 e-reader
  and reading app), ordered by coverage impact; each states its
  done condition and the files it touches, and notes that a
  platform or standards source is still needed before the row is
  written.

- Coverage matrix: Gap column corrected in `roadmap.md` — six
  rows implemented since the last review (transit card top-up,
  in-flight entertainment, hotel self check-in, tenant portal, QR
  table ordering, screen time dashboard) were listed as gaps
  while also listed as full; they are removed from the gap list,
  replaced by the five new named gaps (live translated captions,
  self-checkout grocery kiosk, indoor wayfinding, drive-through
  and curbside pickup, e-reader and reading app).

- Patterns catalogue: Tenant portal, QR table ordering, and
  Screen time dashboard rows added to `catalog/patterns.md`:
  the portal gathers rent payment with a stated due date and
  receipt, maintenance requests tracked from report to fix with
  a stated response time, document access, and messaging with
  the property contact; table ordering scans one code per table
  to open the menu with the table already known, keeps a
  call-staff action on the same screen, and states how to tell
  the code is genuine; the dashboard shows time spent per app or
  category over a stated period with a person-set daily limit, a
  warning before the limit, and a plain route to change or remove
  it. Coverage matrix updated. 6 new source records (683 total).
  Roadmap actions 226, 242, and 243 completed.

- Roadmap: three new improvement actions added (246 recurring
  donation, 247 temporary home access code, 248 health record
  sharing).

- Patterns catalogue: Hotel self check-in row added to
  `catalog/patterns.md`: pre-registration is invited before
  arrival with the benefit stated in plain terms, arrival
  instructions are sent on the day of arrival, document capture
  is handed to the guest's own phone by scannable code, the stay
  ends with a digital or physical key and plain directions to
  the room, and the kiosk clears the previous guest's details at
  once. Coverage matrix updated. 2 new source records (677 total).

- Patterns catalogue: Transit card top-up row added to
  `catalog/patterns.md`: the balance and the fare for the next
  journey are shown before paying, with preset and custom amounts,
  a stated smallest top-up and card limit, an auto top-up with a
  stated threshold and amount, a stated wait before the value
  reaches the card, and a receipt stating the new balance.
  Coverage matrix updated. 2 new source records. Roadmap action
  240 completed.

- Patterns catalogue: In-flight entertainment row added to
  `catalog/patterns.md`: language is set first at the welcome step,
  browse and search run over content held on board, titles are
  marked for captions, audio description, and a signed
  alternative, captions can be resized and recoloured,
  announcements appear on screen as text, a nonvisual way to work
  the controls is offered, and an alternative device is offered
  where the seatback screen cannot be used. Coverage matrix
  updated. 2 new source records (675 total). Roadmap action 241
  completed.

- Coverage matrix: reconciled with the catalogue in `roadmap.md`:
  47 pattern rows that existed in `catalog/patterns.md` without a
  matrix entry were added, and two stale entries were removed (a
  stray separator and a hyphenated duplicate of the converted-price
  display entry), so the matrix now matches the catalogue.

- Roadmap: three new improvement actions added (243 screen time
  dashboard, 244 standardised accessibility labels, 245 desktop
  worked example); actions 240 and 241 completed; action 242
  (QR table ordering) re-checked and left open — the order-and-pay
  flow still rests only on vendor guides.

- Patterns catalogue: Live auction bidding row added to
  `catalog/patterns.md`: a bid on a lot shows the current bid, the
  next step, and the exact amount before it is placed, with every
  bid stated as binding; a maximum-bid control bids in steps up to
  a stated cap and never past it; the countdown runs on the server
  clock with a stated extension rule for late bids; bid history in
  time order with an at-once outbid notice; and the outcome shown
  at once when the close passes. Coverage matrix updated. 2 new
  source records (671 total).

- Patterns catalogue: Guest mode row added to
  `catalog/patterns.md`: lend a device to someone else for a
  short session without signing in, with a stated scope of what
  the guest can and cannot reach, the owner's profile kept behind
  its own lock, everything the guest did cleared on exit, a
  visible sign-out with a stated maximum length and a warning
  before the session ends, and a named profile offered for
  regular borrowers. Coverage matrix updated. 2 new source
  records (669 total). Roadmap action 231 completed.

- Worked examples: Kiosk example added under `examples/kiosk/`:
  a single-task public surface demonstrating the reach range, one
  task per screen, glance budgets, an assistive entry point usable
  without vision, a session reset after inactivity, and all seven
  states. Roadmap action 232 completed; coverage matrix updated.

- Worked examples: Television example added under `examples/tv/`:
  a row-and-column shelf surface demonstrating visible focus,
  focus memory, Back-button behaviour, and 10-foot legibility
  with all seven states. Roadmap action 227 completed; coverage
  matrix updated.

- Primitives catalogue: Date picker row extended with a
  range-band refinement: where two months are shown side by side,
  a range band follows the pointer across both grids so the span
  under consideration stays visible while the person moves.
  Roadmap action 233 completed.

- Roadmap: three new improvement actions added (240 transit card
  top-up, 241 in-flight entertainment, 242 QR table ordering);
  two duplicate source records removed from
  `resources/sources.json` (the same URL recorded twice), leaving
  669 unique records.

- Spatial interfaces trend: audio-only and display glasses rules added
  to `trends/2026/spatial-interfaces.md`: spoken responses as the whole
  interface on audio-only glasses, with short self-contained replies,
  spoken confirmation before consequential actions, and a spoken repeat
  on request; small high-contrast visuals on display glasses that appear
  only when they carry something speech cannot and disappear once read.
  1 new source record (669 total).

- Patterns catalogue: Voice dictation input row added to
  `catalog/patterns.md`: enter text by speaking into a text
  field, with the field kept visible and editable, interim
  words shown until confirmed, microphone access asked for
  before listening starts, pause and resume while dictating,
  single-word correction of uncertain words, and a plain
  statement with captured text kept when the connection
  drops. Coverage matrix updated. 2 new source records
  (668 total).

- Patterns catalogue: Mobile plan setup (eSIM) row added to
  `catalog/patterns.md`: activate, transfer, or switch a mobile
  plan on a built-in SIM, with activation-route choice, the
  switch-versus-transfer distinction, number-porting order,
  keep-the-old-plan-until-signal rule, line labels and default
  lines, transfer confirmation on both phones, and removal
  rules. Coverage matrix updated. 2 new source records
  (666 total).

- Interfaces catalogue: Screenless sensor interfaces section added to
  `catalog/interfaces.md`: a ring or band with no screen of its own, where
  the paired phone app carries the whole interface, haptics alone carry
  alerts with one fixed meaning per pattern, daily scores pair a value with
  a plain-language reason and a next step, a short check-in pairs measured
  data with how the person feels, and on-device gestures stay minimal and
  mapped to one phone action each. 1 new source record (664 total).

- Patterns catalogue: Parcel locker pickup row added to
  `catalog/patterns.md`: collect a parcel from an unattended
  locker with a one-time code or QR, with the expiry stated in
  the notice and a reminder before it ends, single-use code
  rules, a second identity check for high-value or
  age-restricted parcels, and an easy-access compartment on
  request. Coverage matrix updated. 2 new source records
  (663 total).

- Patterns catalogue: Digital car key sharing row added to
  `catalog/patterns.md`: share a key held in a wallet with a named
  recipient, with guest, co-owner and service access levels, an
  expiry stated with the guest role, reshare control, first-use
  activation, per-recipient removal, and a stated distinction
  between a key that only unlocks and one that also starts the
  vehicle. Coverage matrix updated. 2 new source records
  (661 total).

- Watch worked example added under `examples/watch/`: a
  glance-first watch surface demonstrating the two-tap rule,
  complications-first placement, the ambient always-on variant as a
  separate layout, and all seven states. Roadmap action 225
  completed; coverage matrix updated (television worked example
  remains the gap, action 227).

- Patterns catalogue: Telehealth video consultation, Museum audio
  guide, QR code payment at a till, Crowdfunding campaign page,
  and Shared bike and scooter rental rows added to
  `catalog/patterns.md`: telehealth covers a pre-call device and
  connection check, clinician identity, privacy confirmation,
  large labelled controls, a phone fallback, and a written
  post-call summary naming the next step; museum audio guide
  covers language first, a word-for-word transcript beside each
  track, audio description and signed-language video, and short
  tracks with pause, replay, and skip; QR code payment at a till
  covers merchant- and consumer-presented modes stated in words,
  dynamic codes carrying the exact amount, printed-code placement
  and labelling, confirmation on both sides of the till, and the
  authenticated-app rule; crowdfunding covers purpose, organiser
  identity, fees disclosed before payment details, target and
  time limit; shared rental covers price before unlock,
  designated parking, end-of-ride confirmation, and assistive
  technology support. Coverage matrix updated; roadmap actions
  235 and 236 completed; three new improvement actions added to
  `roadmap.md` (237 crowdfunding reward tiers and backer updates,
  238 shared-rental interaction flow, 239 actions-list
  reconciliation). 9 new source records (659 total).

- Patterns catalogue: Device pairing row in `catalog/patterns.md`
  extended with a reconnection rule: a device that drops off the
  network and must connect again goes through the same guided flow
  as first-time setup, rather than relying on the person remembering
  the steps. 1 new source record (650 total).

- Patterns catalogue: Sleep and rest data row added to
  `catalog/patterns.md`: a morning view that leads with the
  seven-day trend rather than a single night's grade, plain words
  with no judgement language and no red grading, stated measurement
  limits, missing nights stated rather than filled in, and at most
  one suggested change tied to the pattern. Coverage matrix updated;
  roadmap action 234 completed; three new improvement actions added
  to `roadmap.md` (234 sleep and rest data, 235 telehealth video
  consultation, 236 museum audio guide). No new source records (649
  total).

- Spatial interfaces trend: glasses and on-the-move placement section
  added to `trends/2026/spatial-interfaces.md`: world-fixed and
  path-following placement for walking users, head-locked placement
  reserved for brief alerts, additive-display colour rules, depth as
  hierarchy, and three-dimensional forms for interactive elements with
  flat planes for text. 2 new source records (649 total).

- Patterns catalogue: Call forwarding, Voicemail greeting, Hotel
  booking, Electric vehicle charging session, and Smart home
  dashboard rows added to `catalog/patterns.md`: forwarding
  covers per-rule destinations with a one-action turn-off and a
  voicemail-override warning; greeting covers recording with
  playback before saving, re-recording without losing the
  previous greeting, a stated length limit, and a plain return
  to the default; hotel booking covers full-cost comparison,
  rate cards with identical attributes in identical order,
  cancellation deadlines in the rate label, sold-out and
  closed-to-arrival dates, a price hold with a stated expiry,
  and a confirmation restating the chosen rate; charging covers
  live availability and connector choice, the price per unit
  shown before the session and fixed once started, contactless
  payment without an account, a pre-authorisation hold explained
  before payment, a live session view, a stop control, a session
  summary with a receipt, and a staffed helpline; smart home
  covers room-first organisation, scenes above device controls,
  state before controls, per-tile battery, updating, error, and
  offline states, plain household language, per-context views,
  and access scoped by person. Coverage matrix updated; roadmap
  actions 220, 221, 228, 229, and 230 completed; three new
  improvement actions added to `roadmap.md` (231 guest mode, 232
  kiosk worked example, 233 date picker range band). 6 new
  source records (647 total).

- Patterns catalogue: Parking session payment, Screenshot
  markup, and Group chat administration rows added to
  `catalog/patterns.md`: parking covers zone entry by number
  or map, vehicle and duration choice, rate and total cost
  before payment, a live countdown, an expiry reminder that
  extends from the notice itself, a stated maximum stay, and
  a receipt; markup covers crop-first, at most three
  callouts in one colour, arrows that touch their target,
  numbered steps, solid or pixelated cover for private
  details before sharing, editable marks, and the original
  capture kept unchanged; group administration covers owner,
  admin, and member roles with per-permission toggles, a
  named ownership transfer, demotion back to member, and
  blocked and removed member lists with a stated route back.
  Coverage matrix updated; three new improvement actions
  added to `roadmap.md` (228 hotel booking, 229 electric
  vehicle charging session, 230 smart home dashboard). No new
  source records (641 total).

- Patterns catalogue: Cookie consent banner row added to
  `catalog/patterns.md`: the banner appears before any optional
  cookie or tracker is set, accept and reject sit on the first layer
  as real controls of equal weight and equal steps, a reject offered
  only as a faint link or with unreadable contrast does not count as
  a choice, no optional purpose is pre-ticked, no basis other than
  consent is claimed for placing or reading cookies, a category is
  labelled required only where it truly is, and withdrawal stays
  available through a permanently visible control with a record of
  each decision. Coverage matrix updated; 1 new source record
  (641 total).

- Patterns catalogue: PIN entry row added to `catalog/patterns.md`:
  a fixed telephone-layout keypad that never moves, a tactile
  alternative with a raised marker on 5, per-digit confirmation by
  count only with no digit shown or spoken, the amount stated before
  entry, and an assisted-entry mode with several activation routes,
  spoken progress and outcome, and per-transaction reset. Coverage
  matrix updated; 1 new source record (640 total).

- Patterns catalogue: Accessibility labels on a store listing row added to
  `catalog/patterns.md`: a store-listing section naming the accessibility
  features an app supports, claimed only where every common task can be
  completed with the feature on, declared per device, with an
  undeclared-support statement and a link to accessibility details.
  Coverage matrix updated; 1 new source record (639 total).
- Standards outlook: European harmonised standard note added to
  `trends/2026/standards-outlook.md`: version 4.1.1, published September
  2026, moves the web and software clauses to WCAG 2.2 Level AA, with
  citation in the Official Journal expected late November to
  mid-December 2026 and the earlier version the legal reference until
  then; the six added criteria are named in plain terms, with a build
  to 2.2 AA now as the practical stance. 1 new source record
  (638 total).
- Patterns catalogue: Deceptive design patterns row added to
  `catalog/patterns.md`: a six-trap check for any screen that asks for
  personal data — overloading, skipping, stirring, obstructing, fickle,
  and left in the dark — with neutral presentation, the least invasive
  option as the default, no re-asking after a refusal, and a plain
  route to data settings from every screen that asks. Coverage matrix
  updated; 1 new source record (637 total).
- Watch layout: complications-first placement and a quick-dismiss
  wrist gesture added to `layouts/watch.md`: the watch-face
  complication is the primary surface, offered for the most-checked
  datum with a tap into the app at that datum, and a short turn of
  the wrist away and back dismisses a notification, call, or alarm
  where the hardware supports it, always beside a visible on-screen
  dismiss. No new source record (636 total).
- Automotive layout: five safety-critical physical controls and a
  control-by-task split added to `layouts/automotive.md`: indicators,
  hazard lights, windscreen wipers, horn, and emergency call keep
  physical controls under the safety-rating protocols in force from
  2026, while urgent actions use physical controls, complex
  non-urgent tasks use voice, and touch serves the rest through
  shallow menus — voice always with a non-voice alternative and a
  visible failure with retry. 2 new source records (636 total).
- Television layout: row-and-column grid navigation and Back-button
  behaviour added to `layouts/tv.md`: left and right move within a
  row, up and down move to the neighbouring row keeping the column,
  and Back always takes the viewer one step back through the
  experience rather than acting as a second select or toggle.
  2 new source records (636 total).
- Modular card grids: independent card loading, failure, refresh,
  and stale-data age added to `trends/2026/modular-card-grids.md`:
  one card's failure never empties the grid, a failed card retries
  in place, stale data states when it was last updated, and
  refreshing one card never reloads the whole grid. No new source
  record (636 total).
- Roadmap: three new improvement actions added to `roadmap.md`
  (225 watch worked example, 226 tenant portal, 227 television
  worked example); coverage matrix updated with watch and
  television worked examples as gaps.
- Patterns catalogue: Transaction history row added to
  `catalog/patterns.md`: every movement of money in and out of an
  account as a checkable record, newest first, each entry naming the
  merchant, date, and amount with its state stated in words — pending,
  posted, reversed, or disputed — pending entries kept visibly separate
  from settled ones, search and filters for state, type, and account
  with the applied filters kept visible, a detail view showing the
  payment method, a quotable reference, and the dispute route, account
  and card numbers masked by default with a deliberate reveal action,
  and exports matching exactly the entries the current filters show.
  Coverage matrix updated; no new source record (already recorded,
  632 total).
  `catalog/patterns.md`: paying for transit by tapping a card or
  device, with a stated day or week cap, the single-ride fare charged
  per tap until the cap is reached and free rides after it, the same
  card or device required for every tap in the period, a tap-off step
  where the fare depends on the journey's end, a plainly stated
  highest fare for a missed tap-off, the full fare charged where a
  reduced fare would need another route, and a checkable payment
  history with cap progress. 2 new source records (632 total).
- Patterns catalogue: System-mediated snippet row added to
  `catalog/patterns.md`: a compact surface shown by the system for one
  quick action, with separate confirmation and result presentations,
  one clearly labelled primary action beside a cancel, no scrolling
  detail, and a route into the app where the task needs more; actions
  with effects beyond the screen always confirm first. 1 new source
  record (630 total).
- Primitives catalogue: Dialog row now states a preference for the
  platform-native dialog element where one is available, since it
  supplies focus trapping, escape handling, focus return, and an
  inert background without custom code. 1 new source record (629
  total).
- Patterns catalogue: Reading view, Add people to a live call, and
  Call history rows added to `catalog/patterns.md`, completing
  roadmap actions 215, 217, and 219: a reading view that removes
  navigation, banners, and interactive controls with text size, line
  spacing, and background controls, a fifty-to-seventy-five-character
  line measure, a kept reading position, and a one-action exit; adding
  people to a live call by dialling privately first, merging once
  connected, announcing each joiner by name, and dropping one
  participant without ending the call; a call history list grouped
  by day with call-type marks, a filter by type, one-action call
  back, grouped repeated missed calls, per-entry delete and clear-all
  with a stated retention limit, and missed calls that never clear
  themselves. Coverage matrix updated with the three new rows, and
  three new improvement actions added to `roadmap.md` (222 parking
  session payment, 223 screenshot markup, 224 group chat
  administration). No new source records (628 total).
- Patterns catalogue: Identity verification onboarding row added to
  `catalog/patterns.md`: state the step count and expected time before
  the first check, put low-friction steps first with document capture
  last, explain beside each request why it is needed, give framing and
  lighting guidance before a document photo, state the exact cause in
  plain language where a capture fails, replace indefinite waiting with
  a review status and a save-and-return path, and state the reason
  plainly where a document is rejected; 1 new source record (628 total).
- Patterns catalogue: Call screening row added to
  `catalog/patterns.md`: for an unknown caller, the phone asks
  who is calling and why before the person answers, showing the
  spoken answer as text on the incoming-call screen, with accept,
  decline, and block-and-report from the same screen, a stated rule
  that a screened call is never answered silently, and saved contacts
  ringing through without screening; 1 new source record (627 total).
- Patterns catalogue: Conference call row added to
  `catalog/patterns.md`: merge two or more live calls into
  one call, dialling each new person privately before
  merging, a participant list naming everyone on the line,
  drop-one and speak-privately controls, a stated
  participant limit, a warning where the host leaving ends
  the call for everyone, and a plain notice where merging
  is not supported; no new source records (626 total).
- Interfaces catalogue: Game interfaces section added to
  `catalog/interfaces.md`: show only what the player needs this second
  in the heads-up display, readability tested under motion with stable
  positions and background-proof text treatment, text sized for the
  viewing distance and scalable to at least twice the default, 4.5:1
  text and 3:1 large-element contrast, never colour alone, subtitles on
  by default, full control remapping with hold-versus-toggle choice,
  motion-reduction controls, and critical elements kept inside the safe
  area on room-distance screens; 2 new source records (626 total).
- Patterns catalogue: Digital identity wallet presentation row added to
  `catalog/patterns.md`: a request summary naming who asks and why,
  per-item disclosure choice with optional items unshared by default,
  explicit consent to the exact set shown, wallet unlock before sending,
  a stated outcome naming what was shared and with whom, and a scannable-code
  route for in-person presentation with a typed or staff fallback; 1 new
  source record (624 total).
- Patterns catalogue: Suspected spam call warning row added to
  `catalog/patterns.md`: a plain-words warning on the
  incoming-call screen with the reason where known, stating
  what the warning does not prove, spoken as well as shown,
  with answer, decline, silence, and block-and-report from
  the same screen, a mark-as-not-unwanted control, and a
  stated place where a blocked number's calls go; 1 new
  source record (623 total).
- Patterns catalogue: Call transfer row added to
  `catalog/patterns.md`: direct and announced transfers with
  the kind stated before the move, the caller told who they
  are being passed to and why, the caller's name, reason, and
  details already given travelling with the call, a stated
  hold with a short wait, return to the caller where the
  next person cannot take the call, and a plain failure
  notice with retry or message; 1 new source record
  (622 total).
- Patterns catalogue: Breakout rooms in video calls row added
  to `catalog/patterns.md`: host-created rooms with a stated
  size and purpose, assignment shown before joining, the
  task and return time in writing in every room, a visible
  countdown before rooms close, stated rules for who can
  move between rooms, help from inside a room, late-joiner
  handling, and a plain recording statement; 1 new source
  record (621 total).
- Patterns catalogue: Safety check-in row added to
  `catalog/patterns.md`: a timed or destination-based check-in with
  chosen trusted contacts, a stated data-sharing level, a prompt to
  confirm safety at the end of the chosen time with a short window to
  answer, an alert with the last known position if there is no answer,
  an add-time control, and a one-action stop confirmed to the contacts;
  1 new source record (620 total).
- Patterns catalogue: Live captions row in
  `catalog/patterns.md` extended: where a person brings their own
  captioning service, its captions are shown on the same call screen
  rather than on a separate screen, with size, font, position, and
  the colour and opacity of the text and its background adjustable
  without asking the host; where a person follows the call through
  sign language, the interpreter stays visible beside the speaker,
  pinned in place, with video clear enough to read the signing;
  1 new source record (619 total).
- Patterns catalogue: Visual voicemail row added to
  `catalog/patterns.md`: recorded messages shown as a list with the
  caller's identity, the time, and the length, each playable in any
  order with pause and scrub controls, a written transcript labelled
  as a transcript and never trusted for exact details without
  listening, heard marking only after play or read, one-at-a-time
  save, share, and confirmed delete, an unheard count, live-arrival
  transcription with one-action pick-up, and a plain statement where
  the list is unavailable or the mailbox is full; 1 new source record
  (618 total).
- Patterns catalogue: Data visualisation row in
  `catalog/patterns.md` extended: for a single goal-progress read,
  such as daily activity against a target, prefer a bar over a ring
  where a quick accurate read matters, and state the value and the
  target in words beside either form so progress never depends on
  judging an arc by eye; 1 new source record (617 total).
- Patterns catalogue: Notification list row in
  `catalog/patterns.md` extended: read state, triage state, and
  following are separate dimensions — reading an item says only that
  it has been seen and never removes it from the active queue, a done
  action moves it out of the active queue without changing its read
  state, and following controls whether future updates arrive, with
  the effect of stopping updates stated plainly; the badge counts one
  stated unit, unread threads in the active queue excluding items
  marked done, so several updates on one thread count once; 1 new
  source record (616 total).
- Patterns catalogue: Subscription cancellation row in
  `catalog/patterns.md` extended: where the flow asks why the person
  is leaving, it asks one short question with a small set of reasons
  and an optional comment, then matches the single alternative to the
  answer — a cheaper plan where price is the reason, a pause where
  use has dropped, a fix or a support route where something is
  broken — and shows that one alternative once, with declining it
  exactly as easy as accepting it, never repeating an offer after it
  has been declined and never showing the same generic offer
  whatever the reason given; 1 new source record (615 total).
- Patterns catalogue: In-app browser row in `catalog/patterns.md`: a
  linked page opens inside the app only where the person needs to stay
  in the task, the platform in-app browser carries pages the app does
  not control, the address and security state are stated before
  anything is entered, a close action returns to the exact place left,
  forward and back controls cover onward navigation, an open-in-browser
  action is always offered, and sign-in to another service is handed
  to the system browser; coverage matrix updated; 1 new source record
  (614 total).
- Patterns catalogue: Call waiting, Outgoing call, and Call quality
  and reconnection rows in `catalog/patterns.md`: a second call
  during a live call offers hold-and-accept, end-and-accept, and
  decline with the effect of each stated before use, a held call
  with a one-action return and a swap control, and merge only where
  the call supports it; an outgoing call states each stage —
  dialling, ringing, connected, busy, no-answer, and failed — with
  a one-action cancel while ringing and a stated cause plus retry
  or message where a call fails; a weakening connection warns
  plainly on the affected tile with an audio-only fallback, and a
  dropped connection reconnects automatically where possible with
  a plain statement of what was lost and what was kept; coverage
  matrix updated; 2 new source records (613 total).
- Patterns catalogue: Confirmation row in `catalog/patterns.md`
  extended with the heaviest confirmation rung: the highest-stakes
  irreversible actions — deleting a whole workspace, removing every
  member, closing an account with data loss — ask the person to type
  the item's name or a confirmation word, so the action cannot be
  completed by habit; 1 new source record (611 total).
- Patterns catalogue: Form flow row in `catalog/patterns.md`
  extended with mistake-prevention rules: accept the common formats
  for a field rather than one rigid shape, divide long numbers into
  chunks that autocomplete across fields, offer a reliable correction
  beside the entered value instead of silently rewriting it, and word
  errors about what the system could not recognise rather than blaming
  the person; 1 new source record (610 total).
- Patterns catalogue: Launch screen row in `catalog/patterns.md`: shown
  only as long as loading genuinely takes, with no artificial delay and
  never used to show loading progress or data; minimal content with no
  text, complex imagery, or advertising; mirrors the first screen where
  platform guidance favours it, or a centred mark on a plain background
  otherwise; dismissed only when the first screen is stable and ready,
  never shown again on a warm start, with light and dark variants that
  match the first screen; coverage matrix updated; 1 new source record
  (609 total).
- Patterns catalogue: Scan-to-pay row in `catalog/patterns.md`: two
  modes — scanning a code the seller shows, or showing a personal code
  for the seller to scan — with the recipient confirmed before any
  amount is entered, a review step showing amount, fee, and total as
  separate lines, a receipt as a distinct state after confirmation,
  large high-contrast shown codes with a full-screen option, and no
  forced sign-in before the scan where the payment needs no account;
  coverage matrix updated; 1 new source record (608 total).
- Primitives catalogue: text-scaling rules added in
  `catalog/primitives.md`: containers wrap and grow with the text and
  truncation is a deliberate choice, fixed bars keep their size with
  another way to read their text at the chosen size, fixed heights are
  avoided, every text element sits inside a scrollable region, and
  side-by-side arrangements stack at large sizes; screens are checked
  at 100%, 150%, and 200% text size; 1 new source record (607 total).
- Patterns catalogue: Call recording notice, Incoming call, and Missed
  call rows in `catalog/patterns.md`: a plain statement before
  recording starts, shown to everyone in the call with a visible
  recording state, a stated rule for who can start and stop it, and a
  stated place and retention period for the recording; an incoming
  call with the caller's identity stated plainly, accept and decline
  controls that work without unlocking the device, a quick reply for a
  declined call, and a silence control that does not decline; and a
  missed-call entry with the caller's identity and the time, a
  one-action call back, a called-back mark that keeps the entry, and a
  rule that a missed call never clears itself — completing roadmap
  actions 206, 207, and 208; coverage matrix updated; three new
  improvement actions added (209 call waiting, 210 outgoing call,
  211 call quality and reconnection); 3 new source records (606 total).
- Patterns catalogue: data-table numeric alignment and totals-row rules added in
  `catalog/patterns.md`: numbers, currency, and percentages align right with
  consistent decimals so digits line up by place value, while text stays left;
  where a column total matters, a totals row in the footer stays pinned while
  the table scrolls and stays out of the sort order so totals never sort as if
  they were a record; 1 new source record (603 total).
- Patterns catalogue: honest wizard progress rule added in
  `catalog/patterns.md`: the step indicator reflects the effort left,
  not just the screens left, and a branching path shows its
  conditional route instead of a percentage that can move backwards;
  1 new source record (602 total).
- Trends: long-output-beside-conversation rule added in
  `trends/2026/conversational-interfaces.md`: a long result opens in a
  pane beside the conversation, stays linked to the turn that produced
  it, updates in place on revision, and changes only after the person
  reviews and accepts them; 1 new source record (601 total).
- Primitives catalogue: language-detection rule added in
  `catalog/primitives.md`: choose the starting language from the saved
  preference first, then the browser or device language, never from
  place; where the detected language is unavailable, say so up front
  and offer a choice instead of silently showing another language;
  1 new source record (600 total).
- States catalogue: first-use empty-state rule added in
  `catalog/states.md`: where the first action can be undone or changed
  afterwards, say so plainly, and never imply that a wrong first choice
  carries lasting cost; where it cannot be undone, state what happens
  before the person acts; 1 new source record (599 total).
- Patterns catalogue: Checkout upsell and cross-sell offer row in
  `catalog/patterns.md`: one addition per surface, with a placement map
  from product view to post-purchase, relevance and price rules, no
  preselected paid extra, and no accept-or-reject step inside payment;
  1 new source record (598 total).
- Watch layout: proactive surfacing rule added in
  `layouts/watch.md`: when time, place, or current activity makes one
  item clearly relevant, surface it at that moment instead of waiting
  for the person to open the app and look for it; the surfaced item
  still shows one datum and one action, it appears only while it stays
  relevant and leaves when it no longer does, and the person can
  dismiss it or switch the surfacing off without losing the underlying
  content; 1 new source record (597 total).
- Automotive layout: head-up display rules added in
  `layouts/automotive.md`: projections show only speed, the next
  manoeuvre, and critical warnings; overlays that annotate the road stay
  fixed to what they mark and never cover hazards or sightlines;
  brightness adapts to ambient light; 1 new source record (596 total).
- Patterns catalogue: Screen sharing in video calls, Mute conversation,
  and Disappearing messages rows in `catalog/patterns.md`: a share
  control that states what will be visible before sharing starts, a
  choice between one window and the whole screen with a live preview,
  a visible sharing state with a one-action stop, and a stated rule
  that private content stays hidden; a mute control with a stated
  duration that silences alerts without stopping delivery, a muted
  mark in the list, and one-action unmute; and a per-conversation
  disappearing-messages timer with a visible countdown, a change
  notice, and a plain statement that a screenshot or a second device
  can keep a copy — completing roadmap actions 200, 201, and 204;
  coverage matrix updated; three new improvement actions added (206
  call recording notice, 207 incoming call, 208 missed call); 3 new
  source records (595 total).
- Desktop layout: scrolling window strip rule added in
  `layouts/desktop.md`: windows sit as columns on a horizontal strip
  wider than the screen, opening a window adds a column without
  shrinking the others, focus slides the strip to the column in use,
  column count and off-screen columns are stated, and tiling is
  preferred where every window must stay visible at once; 1 new
  source record (592 total).
- Patterns catalogue: Raise hand in video calls row in
  `catalog/patterns.md`: one control in the call controls
  and the participants panel, a raised-hand mark on the tile
  and in the list, a visible queue in the order hands were
  raised, moderator lower-one and lower-all controls,
  auto-lower on speaking with a cancel step to keep the hand
  raised, and gesture detection off by default — completing
  roadmap action 203; coverage matrix updated; three new
  improvement actions added (204 disappearing messages, 205
  breakout rooms in video calls); 3 new source records (591
  total).
- Patterns catalogue: Machine-composed content disclosure row in
  `catalog/patterns.md` extended: carry the composed label as a
  machine-readable mark attached to the content itself, so it
  survives copying, sharing, and re-posting instead of living only
  in the surrounding page; no new source record (already recorded,
  588 total).
- Tablet layout: large-screen orientation rule added in
  `layouts/tablet.md`: never depend on a fixed orientation or a
  locked aspect ratio on wide screens — the platform ignores
  those restrictions, so the layout works in both orientations
  and at any window aspect ratio, with capped content width in
  wide landscape, primary actions kept reachable, and preview
  surfaces re-measured on every orientation change; 1 new
  source record (588 total).
- Patterns catalogue: Human verification challenge row in
  `catalog/patterns.md`: a background check first, a visible challenge
  only where needed, never a puzzle as the only route, with an
  alternative path, an audio alternative, and no tight time limit;
  1 new source record (587 total).
- Patterns catalogue: Neuro-inclusive design row in
  `catalog/patterns.md`: steady placement and wording, limited
  sensory load, unhurried timing, short steps with progress
  shown, and a calmer view kept as a stored preference; no new
  source record (already recorded, 586 total).
- Mobile navigation layout: top app bar rule added in
  `layouts/mobile-nav.md`: the bar steps aside while the person
  scrolls down a long reading page and returns slimmer on the
  first upward movement; 1 new source record (586 total).
- Patterns catalogue: Page not found row in
  `catalog/patterns.md`: a plain statement that the page does
  not exist, with the address kept visible, a way back to a
  known place, and a search offer — completing roadmap action
  202; 1 new source record (585 total).
- Patterns catalogue: Paywall and upgrade prompt row in
  `catalog/patterns.md` extended with an exit-offer rule: at most
  one alternative offer follows a dismissal, shown once per
  session, and a second dismissal returns to the task; 1 new
  source record (584 total).
- Patterns catalogue: Sticker and GIF picker row in
  `catalog/patterns.md`: a searchable picker inside the
  compose view with recent and saved items first, a plain
  text description for every item announced to assistive
  technology, and a full-size animated preview before
  sending — completing roadmap action 198; actions 197
  (video-call waiting room) and 199 (focus mode schedule)
  marked implemented to match rows already in the
  catalogue; coverage matrix updated with the five rows
  added by earlier runs; three new improvement actions
  added (200 screen sharing in video calls, 201 mute
  conversation, 202 page not found); 3 new source records
  (583 total).
- Primitives catalogue: Toggle button row in
  `catalog/primitives.md`: a button that stays pressed while its
  mode is on — bold in an editor, mute in a call, a filter chip —
  with the label naming the function while the pressed state is
  announced separately, the pressed state shown by shape and
  wording as well as colour, and the choice rules against a switch
  and a segmented control; 1 new source record (580 total).
- Patterns catalogue: Multi-device handoff row in
  `catalog/patterns.md` extended with scannable-code initiation:
  a short-lived code on the first screen beside a short typed link
  and an emailed link, with its expiry stated and confirmation on
  the originating device when the second device connects; 1 new
  source record (579 total).
  `catalog/patterns.md`: named modes per activity with
  their own allowlists of people and apps, schedules by
  time, place, or app launch with days stated, a visible
  state while on with a stated end, held notifications
  returning in one grouped summary, an automatic reply,
  and sync across devices — completing roadmap action
  199; 1 new source record (578 total).

- Patterns catalogue: search suggestions made operable for assistive
  technology in `catalog/patterns.md`: focus stays in the input while
  moving through suggestions, with each highlighted suggestion
  announced as the current option, the suggestion count or a
  no-matches state announced as a status message without moving
  focus, and the panel's open or closed state exposed; 1 new source
  record (577 total).

- Authentication layout: passkey fast-path rules added to
  `layouts/auth.md`: an immediate-credential check that skips the
  account picker where sign-in intent is already clear, automatic
  passkey upgrade after a successful password sign-in, and removal
  of stale credentials from the credential manager; 1 new source
  record (576 total).

- Patterns catalogue: new Video-call waiting room row in
  `catalog/patterns.md`: people who join before the host wait
  in a holding view with a plain statement of what happens
  next, the host admits or declines each person by name, and
  nobody joins the call unannounced — completing roadmap
  action 197; 1 new source record (575 total).

- Patterns catalogue: new Expense claim submission row in
  `catalog/patterns.md`: a claim built from its items with
  amount, date, and category stated for each, receipts
  attached where required, the approval route stated before
  submission, and one plain state per claim — draft,
  submitted, approved, paid, or returned with a reason —
  completing roadmap action 180, which was marked
  implemented but had no row in the catalogue; 1 new source
  record (572 total).

- Patterns catalogue: new Read receipt row in
  `catalog/patterns.md`: sending, sent, delivered, and read
  states shown on the sender's own messages only, reader
  names on request in groups, a privacy control that stops
  sending read states with its mutual effect stated plainly,
  and a mark-as-unread control that moves the read position
  back to a chosen message; 1 new source record (573 total).

- Patterns catalogue: new Typing indicator row in
  `catalog/patterns.md`: shown only while someone is
  actually composing, named in words with an aggregated
  statement for several typers, expired at once on
  disconnect, and announced to assistive technology without
  repeating on every keystroke, with a still label under
  reduced-motion settings; 1 new source record (574 total).

- Patterns catalogue: new Broadcast emergency alert row in
  `catalog/patterns.md`: two-tier cell-broadcast safety warnings
  where the highest tier overrides silent mode and do-not-disturb
  settings and cannot be turned off, the message states what the
  emergency is, where it is, how serious it is, what action to
  take, who issued it and where to find more, the full-screen
  modal stays until acknowledged and a dismissed warning is kept
  in the notification centre, and no registration, app, or phone
  number is needed; 1 new source record (571 total).

- Conversational interfaces: new earcons section in
  `trends/2026/conversational-interfaces.md`: short non-verbal sounds
  that confirm outcomes and mark state changes, one distinct sound per
  outcome, always paired with a visual or haptic signal, a small set
  shared across the whole product, and urgency carried by pattern
  rather than loudness; 1 new source record (570 total).

- Patterns catalogue: strengthened Collaborative editing presence
  row in `catalog/patterns.md`: keep presence, cursor motion, and
  document state separate, treat the roster as uncertain after a
  disconnect and replace it from a fresh snapshot on reconnect,
  and undo only your own edits; 1 new source record (569 total).

- Patterns catalogue: new Shared whiteboard row in
  `catalog/patterns.md`: a shared infinite canvas where several
  people draw, write, and arrange ideas at the same time, with
  sticky notes, shapes and connectors, named frames, live
  cursors, follow and bring-everyone-here controls, silent
  brainstorming with a reveal, voting, templates, draw and
  view access levels, and export; 1 new source record (568 total).

- Patterns catalogue: new Lightweight app entry row in
  `catalog/patterns.md`: a single-task slice of an app that opens
  from a code, link, or tag without a full install, with a system
  entry card naming the app and the task, no account needed before
  the task, platform sign-in and payment, a one-time full-app
  install offer after the task, and nothing left behind when
  unused; 1 new source record (567 total).

- Patterns catalogue: new Product questions and answers row in
  `catalog/patterns.md`: a questions-and-answers section on a
  product page where shoppers ask about one item and read
  answers from the seller or other shoppers, with review
  before publishing, helpfulness-sorted answers, seller
  answers marked distinctly, a stated sort, and private
  questions kept private; 1 new source record (566 total).

- Patterns catalogue: new Verified account badge row in
  `catalog/patterns.md`: a badge shown beside the name only
  once a check is confirmed, stating what was checked and
  when, with levels named where they differ, never added by
  the person themselves, and removed at once when the check
  no longer holds; 1 new source record (563 total).

- Patterns catalogue: new Virtual background in video calls
  row in `catalog/patterns.md`: background blur as the plain
  default with a preview before joining, a stated limit that
  blur hides detail and not movement, a still-image
  replacement choice, a per-device setting changeable
  mid-call, and a camera-off offer where the device cannot
  run the effect; 1 new source record (564 total).

- Patterns catalogue: new World clock row in
  `catalog/patterns.md`: several places shown at once with
  local time, date, and offset in plain figures, day-or-night
  marks and working-hours bands on a shared timeline, an
  overlap finder naming the shared window, and a share
  control stating every local time for a chosen moment;
  1 new source record (565 total).

- Patterns catalogue: new Gift card purchase row in
  `catalog/patterns.md`: a purchase path of its own for buying
  stored value as a gift — format and design choice, preset or
  custom value, delivery method and scheduled date, recipient
  details kept separate from the buyer's billing, an optional
  message, a balance-check route, and a confirmation stating value,
  recipient, delivery method and date; no new source (already
  recorded).

- Authentication layout: new sign-in restoration rule in
  `layouts/auth.md`: when the person moves to a new device and
  restores their data, the app opens already signed in on first
  launch, with no sign-in screen in between; where no restore
  credential was saved or restoration fails, the ordinary sign-in
  screen appears with the visible fallback chain and a plain
  statement that sign-in is needed again; 1 new source record
  (562 total).

- Patterns catalogue: new Shared shopping list row in
  `catalog/patterns.md`: one household list shared in real time,
  per-item claiming so nobody buys the same item twice, duplicate
  warnings, bought items kept in a separate section, changes by
  others kept visible on next open with an unseen-changes count,
  per-item quantity, unit, category, note and photo detail, a
  shopping mode collapsing several lists into one trip list, and
  saved templates for repeated lists; 1 new source record
  (561 total).

- Patterns catalogue: new Group conversation participant management row
  in `catalog/patterns.md`, completing roadmap action 178: a member
  list in the conversation details with roles stated in words, add
  and remove controls shown only to those allowed to use them, a
  stated history rule for a new joiner, in-conversation
  announcements of every membership change, role changes and
  ownership transfer with confirmation, and a plain leaving flow;
  1 new source record (560 total).

- Patterns catalogue: new Message translation row in
  `catalog/patterns.md`: a per-message translate action in the
  message menu, a translation bar that translates a whole
  conversation including new messages as they arrive, the
  original kept one action away, the chosen language remembered,
  unsupported languages stated before translation is requested,
  and a check of the translated wording before a message is sent
  in another language; 1 new source record (559 total).

- Patterns catalogue: new Recurring payment setup row in
  `catalog/patterns.md`, completing roadmap action 190: a setup
  flow kept separate from a one-time payment, stating the
  amount, the date of the first charge and the repeat schedule,
  and the payment method before authorisation, with pause,
  change, and cancel from the setup itself, a plain notice
  before each charge and after a failed charge, and a stated
  rule for what happens when the payment method changes; no
  new source record (source already recorded, 558 total).

- Patterns catalogue: new Appointment preparation checklist row
  in `catalog/patterns.md`, completing roadmap action 191: one
  short list of what to bring, do, and expect before a booked
  appointment, shown with the booking and again in the reminder,
  with checkable items, time-gated items shown greyed out with
  the date they become available, a done-against-total progress
  count, a stated route where a preparation step cannot be
  completed, and completed items collapsible into a reopenable
  view; 1 new source record (558 total).

- Patterns catalogue: new Deposit refund status row in
  `catalog/patterns.md`, completing roadmap action 192: a
  plain statement of where a deposit refund stands after a
  cancellation — requested, sent, or received — with the
  amount, the method it returns to, and how long it takes to
  appear, a stated route where a refund is delayed or
  missing, a plain reason and retry where a refund fails, and
  the refund action disabled once a refund is complete; 1
  new source record (557 total).

- Patterns catalogue: new Medication refill request row in
  `catalog/patterns.md`, completing roadmap action 193: a
  request sent before the supply runs out, stating how much
  is left and when it runs out, with a choice of delivery or
  pickup and a plain state — sent, confirmed, or ready —
  for each request; 1 new source record (556 total).

- Patterns catalogue: new Booking deposit, Appointment
  standby list, and Medication reminder rows in
  `catalog/patterns.md`, completing roadmap actions 186, 187,
  and 189: a deposit stated with its amount, what it secures,
  and the refund rule for on-time cancellation, late
  cancellation, and a no-show before payment, with the
  remaining balance and its due date shown beside it; a
  standby list that states the person's place, asks for the
  details a match needs at joining, and offers a freed slot
  with a stated window and a one-action accept; and a
  medication reminder naming each dose in plain words with
  its amount and time, a flexible schedule with a snooze,
  taken-or-missed marks from the reminder itself, and a
  visible history kept when the schedule changes; coverage
  matrix updated with the three new rows and four rows added
  by earlier runs; three new roadmap actions (191 appointment
  preparation checklist, 192 deposit refund status, 193
  medication refill request); 3 new source records (555
  total).

- Patterns catalogue: new Ride booking row in
  `catalog/patterns.md`: pickup confirmation as a separate
  decision with a labelled pin and a readable description,
  one-card fare estimates carrying vehicle, arrival estimate,
  and fare with the reason stated where a fare changes,
  live driver tracking as a coordination view with named
  stages, identity confirmation on both sides with a short
  handoff code before the trip starts, and an itemised
  receipt after the trip; 1 new source record (552 total).

- Patterns catalogue: new Emergency assistance request row in
  `catalog/patterns.md`, completing roadmap action 188: a
  request sent with one action from wherever the person is,
  stating the kind of help needed and sharing location at
  once, a short cancel window for accidental requests, a
  plain receipt stating what was sent and to whom, separate
  states for sent, received, and accepted, and a route to
  add essential details after the request; coverage matrix
  updated with the new row; three new roadmap actions
  (189 medication reminder, 190 recurring payment setup);
  3 new source records (551 total).

- Patterns catalogue: new Bottom sheet choice row in
  `catalog/patterns.md`: one short task per sheet, a single
  pending-or-immediate behaviour kept everywhere, a named
  apply control for pending choices, the same discard rule
  for every closing route, a drag handle as a cue only,
  and a search field checked with the on-screen keyboard
  open; 1 new source record (548 total).

- Patterns catalogue: new Trigger-character suggestion menu row in
  `catalog/patterns.md`: a floating list opened by a typed trigger
  character, filtered by the characters after the trigger, with
  keyboard and pointer routes, Escape closing without inserting,
  and a plain no-match state that inserts nothing unasked;
  1 new source record (547 total).

- Patterns catalogue: new Shared trip itinerary row in
  `catalog/patterns.md`, completing roadmap action 185:
  per-person view-only or editable access, one live trip
  seen by every companion with changes naming affected
  bookings, proposals marked with who suggested them and
  what joining costs that person, sensitive details kept
  out of view-only links, and a stop-sharing control that
  leaves each companion with their own copy; 1 new source
  record (546 total).

- Patterns catalogue: new Travel itinerary view,
  Bill explanation, and Appointment late-cancellation
  and no-show policy rows in `catalog/patterns.md`,
  completing roadmap actions 182, 183, and 184: a trip
  shown day by day with local place times, an overnight
  stay anchoring each day, and changes naming affected
  bookings, kept reachable without a connection; one
  bill broken down line by line with each charge named
  and dated, discounts, credits, and fees as their own
  lines, and a dispute route from any line; and a
  cancellation deadline with late-cancellation and
  no-show fees stated before booking, repeated at
  confirmation, with a late-cancel route and a plain
  prepayment statement; coverage matrix updated with
  the three new rows; three new roadmap actions (185
  shared trip itinerary, 186 booking deposit, 187
  appointment standby list); 3 new source records
  (545 total).

- Patterns catalogue: new Aggregate rating display,
  Recurring appointment series, and Travel document
  checklist rows in `catalog/patterns.md`, completing
  roadmap actions 63, 177, and 179: a read-only rating
  summary stating its scale, count, and which ratings
  count, with a verified-only view where verification
  exists; a repeating booking with a stated series rule,
  an edit and cancel scope choice, changed-occurrence
  marks, and pause and end-series routes that keep past
  occurrences; and a pre-travel document list checked
  against trip dates with renewal routes and a plain
  blocking warning where a missing document blocks
  boarding; coverage matrix updated with the three new
  rows; three new roadmap actions (182 travel itinerary
  view, 183 bill explanation, 184 appointment
  late-cancellation and no-show policy); 2 new source
  records (542 total).

- Patterns catalogue: new Shared subscription plan row in
  `catalog/patterns.md`: one paying manager, stated seat limit
  with seats used and left, separate member accounts, pending
  invites with resend and withdrawal, removal or self-leaving
  that downgrades the member to the free tier without deleting
  their account, and a shared end date on plan cancellation;
  1 new source record (540 total).

- Patterns catalogue: new Back to top row in
  `catalog/patterns.md`: shown only on long pages after a
  stated scroll distance, fixed clear of content and other
  floating controls, focus moved to the top landmark on
  activation, smooth scroll honouring reduced-motion
  settings; completing roadmap action 181; 1 new source
  record (539 total).

- Patterns catalogue: new Group scheduling poll row in
  `catalog/patterns.md`: shortlist votes or a blank availability grid,
  overlap shown as a heatmap plus counts in text, best windows ranked
  by required people free, per-person zones with the organiser zone
  beside them, editable responses before close, and the chosen time
  issued as a calendar invitation; 1 new source record (538 total).

- Patterns catalogue: new Appointment check-in row in
  `catalog/patterns.md`: check-in from the booking or
  its reminder, arrival window stated separately from
  the service start, visible queue position, and plain
  early, on-time, and late arrival states with a next
  step after check-in; new Travel check-in row:
  check-in window in the trip timezone, seat and bag
  choices settled in the same flow, a pass issued at
  once with a saved copy reachable without a
  connection, and a plain bag-drop or direct-boarding
  next step; and new Stored payment method removal
  row: every affected subscription and saved checkout
  listed with its outcome stated before confirming,
  confirmation naming the method by label, and a
  replacement required where the method is the only
  method for a subscription; completing roadmap
  actions 174, 175, and 176; coverage matrix updated
  with the three new rows; three new roadmap actions
  (179 travel document checklist, 180 expense claim
  submission, 181 back-to-top control); 1 new source
  record (537 total).


- Patterns catalogue: Address entry row in
  `catalog/patterns.md` extended with post-entry
  correction rules: where a check finds a close
  standardized match, show the entered address beside
  the suggested address with changes highlighted and let
  the person accept the suggestion or keep the address as
  entered; where no close match is found, warn plainly
  that the address could not be verified without blocking
  the task; no new source (already recorded).

- Patterns catalogue: Appointment management row in
  `catalog/patterns.md` extended with booking-flow order
  rules: service, then staff, then time, then details, then
  confirmation; no account creation demanded before a first
  booking; slot picker opening on the next days holding
  slots, leading with the first available appointment and
  grouping times into morning, afternoon, and evening;
  no new source (already recorded).

- Patterns catalogue: new Shoppable video row in
  `catalog/patterns.md`: buying a product shown in a video
  without leaving the player, with tags shown only while the
  product is on screen, a card that pauses playback while open
  and resumes at the same point, in-place cart confirmation,
  sold-out handling before the add action, and a post-play
  product list; distinct from the product variant selection,
  live broadcast chat overlay, and carousel rows; coverage
  matrix updated; 1 new source record (536 total).

- Patterns catalogue: new Stored payment method label
  row in `catalog/patterns.md`: a plain name chosen by
  the person for each stored method, shown beside its
  type and last digits wherever methods are listed, so
  two methods of the same type are told apart without
  opening either; new Conversation export row: a copy
  of one conversation as a file with the scope stated
  before it starts, a media choice with a size warning,
  omitted attachments marked in place, and a plain
  warning that the exported file is a readable copy;
  and new Appointment reminder row: a reminder carrying
  time with timezone, place or join link, duration, and
  preparation, with confirm, reschedule, and cancel
  routes, quiet-hours respect, and suppression of stale
  reminders after a booking changes; completing roadmap
  actions 170, 171, and 172; coverage matrix updated
  with the three new rows; three new roadmap actions
  (176 stored payment method removal, 177 recurring
  appointment series, 178 group conversation
  participant management); 3 new source records (535
  total).

- Patterns catalogue: new Supervised usage limits row in
  `catalog/patterns.md`: daily and per-app or per-category
  limits counted inside the daily total, downtime schedules
  with a named always-allowed list, remaining-time warnings,
  a limit-reached state that keeps help and guardian routes
  open, and a scoped extension request; distinct from the
  usage allowance row and the guardian approval request row;
  1 new source record (532 total).

- Patterns catalogue: new Dual approval row in
  `catalog/patterns.md`: a sensitive change taking effect
  only after a second, different person approves it, with
  the exact change stated in the request, a pending state
  blocking any partial effect, approval bound to the
  request as written and used once, a stated expiry, and
  a decision record naming who requested and who decided;
  coverage matrix updated; three new roadmap actions
  (174 appointment check-in, 175 travel check-in);
  1 new source record (531 total).


- Patterns catalogue: new Paired handover record row in
  `catalog/patterns.md`: recording an item's condition at
  handover and again at return with the same fields and
  standard, timestamped photos, dual meter readings, and
  a countersign at each end, showing only differences as
  new with their charge effect stated before billing;
  1 new source record (530 total).

- Patterns catalogue: new In-conversation message search
  row in `catalog/patterns.md`: searching inside one
  conversation with a match count, jump-to-match controls,
  highlighted matches, and a plain route back to the
  latest message; and new Expiring payment method
  replacement row: replacing a stored method from its
  warning, carrying the replacement into every subscription
  and saved checkout that used the old method, with a
  stated effective date and a plain statement where a
  payment cannot move; coverage matrix updated with both
  rows; 2 new source records (529 total).

- Patterns catalogue: new Turn-by-turn guidance row in
  `catalog/patterns.md`: showing the current step with
  direction, distance, and plain cue text, previewing a
  close-following next step, keeping the map oriented to
  travel with travelled and remaining route in distinct
  styles, showing arrival time with time and distance
  remaining, offering overview with a single recenter
  action, stating recalculation plainly on leaving the
  route, keeping the end-navigation action visible, and
  showing lane guidance before junctions; distinct from
  the route planning row; no new source record (already
  recorded, 527 total).

- Patterns catalogue: new Receipt capture row in
  `catalog/patterns.md`: capturing a receipt in labelled
  sections where it is long or double-sided, showing
  recognised merchant, date, amount, and line items beside
  the image for review and correction before saving,
  marking uncertain fields for checking, merging duplicates
  with confirmation, and marking a checked record as
  reviewed with the image kept; 1 new source record
  (527 total).

- Patterns catalogue: extended the Contact picker row in
  `catalog/patterns.md` to cover choosing several contacts in
  the same picker, with the chosen set shown for review before
  confirming, each chosen contact removable on its own, and the
  needed field still asked for where a chosen contact holds
  several; 1 new source record (526 total).

- Mobile navigation layout: predictive back preview rule in
  `layouts/mobile-nav.md`: an edge swipe shows the destination
  before it commits, releasing before the commit threshold
  returns the current surface unchanged and releasing past it
  completes the move, with touch targets and drag handles kept
  out of the system gesture areas at the screen edges;
  1 new source record (525 total).

- Patterns catalogue: new Pinned conversation row in
  `catalog/patterns.md`, completing roadmap action
  169: keeping a few chosen conversations fixed in a
  pinned section above the chronological list, with a
  plain pinned mark, a stated small pin limit, pinning
  that changes position only and never alert behaviour,
  and a one-action unpin that returns the conversation
  to its place by latest message; distinct from the
  pinned message row and the conversation mute row;
  1 new source record (524 total).

- Patterns catalogue: new Reduced-motion preference row
  in `catalog/patterns.md`, completing roadmap action
  165: honouring a system-level preference for less
  movement on every screen, replacing large, continuous,
  or self-starting movement with instant or faded
  changes while keeping brief state feedback, never
  carrying essential information by motion alone, and
  applying the preference mid-session; and a new
  Archive conversation row, completing roadmap action
  166: moving a finished conversation out of the main
  list without deleting it, with a named archive
  location, search still finding archived conversations,
  a stated new-message rule, and a one-action restore;
  distinct from the message edit and delete row and the
  saved-item collection row. Landing layout: a
  reduced-motion rule for hero media in
  `layouts/landing.md`. Roadmap: three new improvement
  actions added (167 in-conversation message search,
  168 expiring payment method replacement, 169 pinned
  conversation); coverage matrix updated with the two
  new rows; 2 new source records (523 total).

- Patterns catalogue: new Sleep timer row in
  `catalog/patterns.md`: stopping long-form playback on its
  own after a chosen time, with fixed durations and an
  end-of-current-chapter choice, a visible remaining time,
  a fade-out rather than a cut, resume from the stop
  position, and one-action extend or cancel from the
  player; distinct from the media chapters row and the
  playback queue row; 1 new source record (521 total).

- Patterns catalogue: extended the List reorder row in
  `catalog/patterns.md` with a move-to-position control for
  long lists — a destination choice or a position number —
  so reaching a distant position never needs repeated
  single steps, and a tap-to-select then tap-to-place route
  on touch screens, so reordering never requires a
  press-hold-drag gesture; no new source record, the
  existing accessible drag-and-drop source already covers
  these rules (520 total).

- Patterns catalogue: new Recipe serving scaling row in
  `catalog/patterns.md`: changing the serving count scales
  every scalable ingredient amount by the chosen count
  divided by the original count, rounds to a usable kitchen
  measure with rounded amounts marked, keeps fixed
  quantities unchanged and marked as such, states where
  seasoning and leavening do not scale in proportion, and
  carries the chosen count into the printed list; 1 new
  source record (520 total).

- Patterns catalogue: new Conversation mute row in
  `catalog/patterns.md`, completing roadmap action 164:
  silencing one conversation without leaving it, with a
  stated mute length or until-unmuted choice, a plain
  muted mark visible in the list, messages still arriving
  without an alert, a stated rule for mentions while
  muted, and a one-action unmute from the conversation
  itself; distinct from the pinned message row and the
  notification preferences row; 1 new source record
  (519 total).

- Patterns catalogue: help-search recovery rule in the
  In-product help row, completing roadmap action 29: a
  search with no matches states plainly that nothing
  matched, suggests the nearest topics by wording, keeps
  the query editable in place with a route back to the
  full help list, and carries the failed query into the
  escalation path so it is never retyped; link-preview
  rule in the Share link row, completing roadmap action
  30: before sending, the sender sees the item title or
  description the link opens, who can open it, and when
  access ends, with an edit step for scope and expiry
  from the same screen; second-factor method-change rule
  in the Second-factor sign-in row, completing roadmap
  action 31: changing the method requires a successful
  check with the current method first, and the old method
  stays active until the new one verifies; 3 new source
  records (518 total).

- Patterns catalogue: new Conversation catch-up summary row in
  `catalog/patterns.md`: catching up on unread messages in a
  conversation with a condensed summary that states its covered
  range, links each point to its message, offers a jump to the
  first unread message, surfaces anything needing a decision or
  reply separately, and never marks the underlying messages read;
  distinct from the notification digest row and the threaded
  message reply row; 1 new source record (515 total).

- Patterns catalogue: new Shared presentation control row in
  `catalog/patterns.md`: letting another participant advance shared
  slides or operate shared content during a live share, with a
  stated grant scope, a visible holder list, session-only grants,
  per-holder or all-holder revocation, and instant take-back;
  distinct from the live call controls row and the meeting and
  event creation row; 1 new source record (514 total).

- Patterns catalogue: new Read-along narration row in
  `catalog/patterns.md`: following spoken narration in written
  text with a whole-word current-passage highlight kept in view,
  a follow control that pauses automatic scrolling, and
  play-from-word control; distinct from the voice message
  transcript row, the live captions row, and the transcript
  editing row; 1 new source record (513 total).

- Patterns catalogue: new Saved collection sharing row in
  `catalog/patterns.md`, completing roadmap action 163: sharing
  a saved collection with another person, stating the scope
  of what is shared, offering a view-only or editable choice,
  keeping sharing changes with the owner, and stating what
  happens to shared items when access is revoked; distinct
  from the saved-item collection row and the shared cart row;
  1 new source record (512 total).

- Patterns catalogue: new Return label and drop-off row in
  `catalog/patterns.md`, completing roadmap action 162: returning
  an item with a label and a drop-off route, stating where the
  label is found, how long it stays valid, what to show at
  drop-off, and the refund timing after the return is scanned;
  distinct from the return and exchange request row and the
  order tracking row; 1 new source record (511 total).

- Patterns catalogue: new Message forwarding row in
  `catalog/patterns.md`, completing roadmap action 161: forwarding
  a message to another conversation with a preview of the message
  being sent, a recipient choice that states where it will land, an
  edit route before sending, and a stated rule for forwarded media
  and links; distinct from the quote reply row and the threaded
  message reply row; 1 new source record (510 total).

- Patterns catalogue: new Group checkout, Gift receipt,
  and Store pickup rows in `catalog/patterns.md`,
  completing roadmap action 148: a group checkout where
  each participant pays a stated share with a stated
  deadline and refund route for unpaid shares; a gift
  receipt that proves a purchase for exchange without
  showing prices, discounts, or payment details; and a
  store pickup flow with per-store stock, a stated ready
  time, a check-in control, and a stated hold period for
  uncollected orders; 3 new source records (509 total).

- Roadmap: three new improvement actions (161 message
  forwarding, 162 return label and drop-off, 163 saved
  collection sharing), ordered by coverage impact;
  coverage matrix updated with the three new rows.

- Patterns catalogue: Document scanner row extended in
  `catalog/patterns.md`: capture guidance before shooting — fill
  the frame, hold the camera flat and straight, and move glare
  and shadows off the text — a short good-versus-poor example,
  a pre-submission check that names the fault to fix, and
  legibility judged rather than an exact file size; 1 new
  source record (506 total).

- Patterns catalogue: new Loyalty tier progress row in
  `catalog/patterns.md`, completing roadmap action 160: the
  current tier stated with progress toward the next tier in
  plain figures, the next tier benefits listed beside the
  gap, a stated rule for how the tier is kept or lost with a
  warning before loss, and progress never shown by shape or
  colour alone; 1 new source record (505 total).

- Patterns catalogue: new Delivery reschedule row in
  `catalog/patterns.md`, completing roadmap action 159: a
  delivery window changed from the placed order itself, with
  the cut-off stated before any change is started, only open
  windows offered and re-checked at confirmation, any fee
  difference stated before confirmation, the new window
  carried into the tracking view, and a plain statement
  where rescheduling is no longer possible rather than a
  missing control; 1 new source record (504 total).

- Patterns catalogue: new Subscription gifting row in
  `catalog/patterns.md`, completing roadmap action 157: a
  subscription given to another person for a set period, paid
  once by the giver, with the gift length and included access
  stated before purchase, acceptance by the recipient before
  access starts, a stated rule for who pays on renewal and
  for a recipient who already holds a plan, and a plain
  decline route so the giver is not charged for access never
  taken; 1 new source record (503 total).

- Patterns catalogue: new Price history display row in
  `catalog/patterns.md`, completing roadmap action 156: past
  prices for one item shown in date order with a stated
  history range, a table beside any chart, separate lines for
  different variants or conditions, and a sale label used only
  where a higher price genuinely applied before; 1 new
  source record (502 total).

- Patterns catalogue: new QR sign-in row in
  `catalog/patterns.md`, completing roadmap action 158: a
  sign-in on a screen with awkward input approved on a phone
  already signed in, with the account and the asking device
  named on the approving phone, an explicit approval before
  sign-in completes, a typed short code beside the QR code,
  a stated code expiry, and a cancel control that ends the
  attempt on both screens; 1 new source record (501 total).

- Roadmap: three new improvement actions (158 QR sign-in,
  159 delivery reschedule, 160 loyalty tier progress),
  ordered by coverage impact; coverage matrix updated with
  the QR sign-in row and the previously missing high-demand
  queue row.

- Patterns catalogue: new High-demand queue row in
  `catalog/patterns.md`, completing roadmap action 155: a
  queue entered when demand exceeds capacity, with the
  person's position stated, a wait estimate revised as the
  line moves, a place kept through a brief interruption, and
  a plain route out that releases the place at once; 1 new
  source record (500 total).


- Patterns catalogue: new Product recall notice, Account
  merge, and Loyalty points expiry warning rows in
  `catalog/patterns.md`, completing roadmap actions 149, 150,
  and 151: a recall notice stating affected items, risk, and
  remedy with a kept remedy record; a merge preview stating
  what moves, what is kept, and what is lost with an undo
  window stated; and an expiry warning stating the amount at
  risk, the exact date, and the smallest saving use with a
  use-from-warning route; 3 new source records (499 total).


- Patterns catalogue: new Download manager row in
  `catalog/patterns.md`, completing roadmap action 152: a list
  of files being fetched or already fetched, each with name,
  size, progress, and a stated state, per-item pause and
  resume that keep already-fetched progress, cancel and
  remove controls, a retry route for a failed item alone,
  and an open action for a finished download; 1 new source
  record (496 total).

- Patterns catalogue: extended Invitation response row in
  `catalog/patterns.md` with guest-count rules: the allowed
  number stated beside the reply before it is chosen, a name
  collected for each additional guest, in-place headcount
  updates on a changed count, and removal of additional guests
  on declining; 1 new source record (495 total).

- Patterns catalogue: new File preview, Search history, and
  Passkey sign-in rows in `catalog/patterns.md`, completing
  roadmap actions 48, 49, and 67: a preview shown before
  opening or downloading a file with name, type, and size
  stated, an excerpt or thumbnail where the type allows one,
  and a plain fallback where no preview exists; a list of
  past queries that can be re-run, edited, or deleted one at
  a time or all at once with a stated retention scope; and
  sign-in with a device-held credential explained before the
  device prompt, offered beside a visible fallback, with a
  cross-device route and a recovery path that never strands
  the account; coverage matrix updated; 3 new source records
  (494 total).

- Roadmap: three new improvement actions (152 download
  manager, 153 voice message transcript, 154 checkout worked
  example), ordered by coverage impact; coverage matrix updated
  with the new rows.

- Patterns catalogue: new Automation routine builder row in
  `catalog/patterns.md`: trigger, condition, and action lists kept
  separate, a plain-sentence summary of the whole rule, an
  all-or-any choice for several conditions, a test run, an
  enable switch that pauses without deleting, warnings for
  irreversible actions and self-firing loops, and a last-run
  record for diagnosis; 1 new source record (491 total).

- Patterns catalogue: new Order editing after placement row in
  `catalog/patterns.md`: editing from the order itself within a stated
  window, what can change at each stage, a full changed-order summary
  with the price difference stated before confirmation, and the change
  carried into the tracking view; 1 new source record (490 total).

- Patterns catalogue: new Profile photo upload and crop,
  Playback queue, and Security incident notice rows in
  `catalog/patterns.md`, completing roadmap actions 144,
  145, and 146: a crop preview in exactly the shape shown
  to others with a stated size and format limit and a
  keyboard-operable crop alternative; a playback list with
  the current item marked in text as well as in shape,
  shuffle that plays each item once before repeating, and
  stated repeat and end-of-queue rules; and a plain
  incident notice stating what happened, what data was
  involved, the actions matched to that data, and what is
  already being done, with a dated update route; coverage
  matrix updated; 3 new source records (489 total).

- Roadmap: three new improvement actions (149 product
  recall notice, 150 account merge, 151 loyalty points
  expiry warning), ordered by coverage impact; coverage
  matrix updated with the three new rows.

- Patterns catalogue: expanded Consent choice row in
  `catalog/patterns.md`: accept and decline on the first layer
  with equal size, weight, and steps, dismissal without choosing
  treated as no agreement, a locked required category and
  accept-all and decline-all shortcuts inside the preferences
  panel, and a persistent change route; 1 new source record
  (486 total).
- Patterns catalogue: new Donation at checkout row in
  `catalog/patterns.md`: an optional charitable contribution
  that is never preselected, with a named beneficiary, preset
  and custom amounts, a round-up choice stating the exact
  amount for the order, a separate line item and receipt
  line, and a stated change or refund route; 1 new source
  record (485 total).
- Patterns catalogue: new Recording consent row in
  `catalog/patterns.md`, completing roadmap action 147:
  consent asked before capture starts with a stated scope,
  equal accept and leave choices, a persistent indicator,
  spoken notices for audio-only participants, re-asking
  when the scope widens, and stopping over a stated
  objection; 1 new source record (484 total).
- Patterns catalogue: new Transaction dispute, Habit
  streak, and Contactless payment confirmation rows in
  `catalog/patterns.md`, completing roadmap actions 140,
  141, and 142: a dispute raised from the transaction
  detail with reason choices, evidence, a provisional state
  and a final outcome notice; a streak count shown with its
  longest run, a stated break rule, and a limited recovery
  or pause route; and a tap payment confirmed in more than
  one channel with a named failure cause and a fallback
  method; coverage matrix updated; 3 new source records
  (483 total).

- Roadmap: three new improvement actions (146 security
  incident notice, 147 recording consent, 148 group
  checkout), ordered by coverage impact; coverage matrix
  updated with the three new rows.

- Patterns catalogue: new Gated feature entry row in
  `catalog/patterns.md`: a feature beyond the current tier
  stays visible where it usually lives, marked in text as
  needing a higher tier, with an upgrade action that states
  the added entitlement and cost and a dismiss or return
  action that preserves the task in progress; 1 new source
  record (480 total).

- Patterns catalogue: new Live location sharing row in
  `catalog/patterns.md`: choosing recipients and a bounded
  duration before sharing starts, a persistent sharing
  indicator naming who can see the position and when it
  ends, stop and extend controls, and an expired view that
  states plainly that sharing has ended and shows only the
  last shared position as a static point; 1 new source
  record (479 total).

- Patterns catalogue: new App lock row in
  `catalog/patterns.md`, completing roadmap action 143:
  an opt-in lock behind the device's own check or a
  sign-in fallback after a stated period of inactivity,
  with a lock-on-leaving option, a visible fallback, a
  stated pause after repeated failed attempts without
  locking the account, hidden sensitive content in
  previews and notifications while locked, and a plain
  statement of what the lock does and does not protect;
  coverage matrix updated; no new source records — the
  biometric sign-in guidance source was already recorded
  (478 total).

- Roadmap: three new improvement actions (143 app lock,
  144 profile photo upload and crop, 145 playback queue),
  ordered by coverage impact; coverage matrix updated
  with the new app lock row.

- Primitives catalogue: extended Switch row in
  `catalog/primitives.md` with a keyboard contract, a
  track focus ring at 3:1 contrast, and disabled and
  waiting states announced to assistive technology;
  1 new source record (478 total).

- Patterns catalogue: new Shared item access row in
  `catalog/patterns.md`: inviting named people or groups to a
  single item with each role stated in plain words, inherited
  access shown plainly, pending invitations with resend and
  withdrawal, and role changes and removals that state their
  effect before they take hold; coverage matrix updated;
  1 new source record (477 total).

- Patterns catalogue: new Card freeze, Travel disruption
  rebooking, and Size guide and fit recommendation rows in
  `catalog/patterns.md`: a one-action card freeze with a
  plain statement of what stops and an unfreeze control in
  the same place; a disruption replacement judged on the
  whole journey, with the original held until the
  replacement is confirmed and a refund or later-date
  route where no suitable replacement exists; and a size
  guide beside the size selector stating whether values
  describe the garment or the body, with a recommendation
  that states what it rests on and stays editable;
  coverage matrix updated with the new rows and with
  three rows previously missing from it (saved reply,
  order receipt, subscription billing-date change); three
  new improvement actions added (140 transaction dispute,
  141 habit streak, 142 contactless payment
  confirmation); 3 new source records (476 total).

- States catalogue: new Produced-result states section in
  `catalog/states.md`: specific progress text while a result is being
  produced, answer-first presentation in short chunks with detail on
  demand, refine, undo, and retry controls beside the result,
  confirmation before consequential actions, and a manual route that
  does not depend on the produced result; 1 new source record
  (473 total).

- Patterns catalogue: new Saved reply row in
  `catalog/patterns.md`, completing roadmap action
  139: a reusable message template inserted from the
  compose view by trigger or picker as editable text,
  never sent at once, with placeholders filled from the
  current conversation or flagged when left empty, named
  by purpose and searchable by name and content, with its
  scope stated plainly; 1 new source record (472 total).

- Patterns catalogue: new Subscription billing-date change
  row in `catalog/patterns.md`, completing roadmap action
  138: moving a renewal date states whether only the next
  charge moves or the whole cycle shifts, the new
  next-charge date, and any prorated credit or extra charge
  for the lengthened or shortened current period before
  confirming, with a pending change cancellable until it
  takes effect; 1 new source record (471 total).

- Patterns catalogue: new Order receipt row in
  `catalog/patterns.md`, completing roadmap action 137: a
  receipt kept after purchase stating every item with its
  quantity and unit price, the subtotal, discounts, taxes,
  shipping, and final total, the masked payment method and
  order reference, and the delivery or pickup details, kept
  reachable from the order with print and download routes
  that match what was paid, and a correction route stating
  any refund or further charge before confirmation; 1 new
  source record (470 total).

- Patterns catalogue: new Converted price display and
  Scheduled message send rows in `catalog/patterns.md`,
  completing roadmap actions 135 and 136: a converted
  amount shown beside the original price with its rate,
  rate date, and rounding rule, every price in the view
  converted with the same rate, and the final charge
  re-stated in the charging currency before payment; and
  a message composed now and sent later, editable and
  cancellable until it sends, re-checked for stale
  recipients or content before sending, confirmed once
  when sent, and reported with a retry path when a send
  fails; coverage matrix updated with the new rows and
  three new improvement actions added (137 order receipt,
  138 subscription billing-date change, 139 saved reply);
  no new source records — the scheduled-message guidance
  source was already recorded, and the converted-price
  row is grounded in the existing locale formatting and
  checkout rules (469 total).

- Patterns catalogue: new Translated content row in
  `catalog/patterns.md`, completing roadmap action 134: a
  translated label naming the source language, the original
  reachable in one action with the reader's place kept,
  untranslated parts named rather than silently mixed, a
  stated controlling version and reviewed-version route for
  legal or safety-critical text, and language marking for
  reading tools; 1 new source record (469 total).

- Patterns catalogue: new Delivery photo proof, Warranty
  claim, and Overflow menu pattern rows in
  `catalog/patterns.md`, completing roadmap actions 126,
  131, and 62: a delivery photo attached to the delivered
  stage with a mismatch route, stated retention and
  visibility rules, and a plain no-photo statement; a
  warranty claim started from its order or item with proof
  stated up front, states matching established events,
  remedy options with timeframes, a return route, and a
  reasoned decision notice; and an overflow menu gathering
  secondary actions under a named trigger with plain
  destructive-action separation and close-on-selection,
  dismiss, and focus-leaving behaviour; coverage matrix
  updated with the new rows and with pattern rows
  previously missing from it; three new improvement
  actions added (134 translated content, 135
  converted-price display, 136 scheduled message send);
  3 new source records (468 total).

- Patterns catalogue: new Shared expense splitting row in
  `catalog/patterns.md`: per-expense split methods, per-expense
  participant choice, item-proportion shared charges, exact
  totals with stated rounding, running balances, and a
  fewest-transfer settle-up plan; 1 new source record
  (464 total).

- Patterns catalogue: new Live poll row in
  `catalog/patterns.md`: one-action voting with plain
  confirmation, labelled live results in counts and
  percentages, presenter control over result reveal, stated
  voting state and deadline, plain anonymity and
  vote-change statements, and results kept after closing;
  1 new source record (465 total).

- Patterns catalogue: new Guardian approval request row in
  `catalog/patterns.md`: a child request stating exactly what
  is asked, the requested thing blocked until the guardian
  decides on their own device, a pending state with a
  withdraw route for the child, a plain decline with no
  bypass, approval limited to what was asked, and later
  change or withdrawal from a guardian-only area; 1 new
  source record (463 total).

- Patterns catalogue: new Hands-busy step guidance row in
  `catalog/patterns.md`: one step at a time in large text
  readable at a distance, only the items for that step beside
  it, a keep-awake screen with a pause that holds the place,
  labelled timers that may run together with expiry announced
  in sound and in words, and voice, gesture, and large-control
  step movement with place and timers kept on leaving and
  return; 1 new source record (462 total).

- Patterns catalogue: new Delivery address validation row in
  `catalog/patterns.md`, completing roadmap action 133: a
  suggested correction shown beside the entered address for
  confirmation, never silently rewriting what was entered, the
  original kept where the person insists on it, a prompt for a
  missing unit or suite number, a warning rather than a block
  where the result is uncertain, and a re-check at
  confirmation; 1 new source record (461 total).

- Patterns catalogue: new Device pairing row in
  `catalog/patterns.md`: pairing-mode instruction stated in
  words with its indicator described, nearby discovery first
  with manual-entry and code fallbacks, network details asked
  once with staged progress, failure stated with its cause and
  a retry plus a different method keeping entered details,
  and a name, place, and test control after connection before
  leaving setup; 1 new source record (460 total).

- Patterns catalogue: new In-store availability check row in
  `catalog/patterns.md`, completing roadmap action 132: stock
  at nearby stores checked before a visit, with distance and
  opening times beside each store, the time the stock was
  checked stated, a hold or reserve route where offered, and
  the next nearest store or a delivery route where the nearest
  store has none; 1 new source record (459 total).

- Patterns catalogue: new Service status notice, Order
  substitution choice, and Commercial content disclosure
  pattern rows in `catalog/patterns.md`, completing roadmap
  actions 128, 129, and 130; coverage matrix updated with
  the three new rows; three new improvement actions added
  (131 warranty claim, 132 in-store availability check,
  133 delivery address validation); 1 new source record
  (458 total).

- Patterns catalogue: new Live call controls row in
  `catalog/patterns.md`: one fixed bar holding microphone,
  camera, share, participant, and leave controls, with
  worded toggle states, a leave-versus-end distinction, a
  share preview with a visible pause or stop control,
  speaker marking, connection-trouble indicators, queued
  raise-hand handling, and keyboard shortcuts with a
  pointer path for each; 1 new source record (457 total).
- Patterns catalogue: new Signed-in device management row in
  `catalog/patterns.md`, completing roadmap action 127: a
  list of every device and session signed in to the account
  with a recognisable name and last-activity statement, the
  device in use marked, per-device and sign-out-everywhere
  controls, and a direct route to change the password and
  review recent activity after an unfamiliar device is signed
  out; 3 new source records (456 total).
- Roadmap: four new improvement actions (127 signed-in
  device management, 128 service status notice, 129 order
  substitution choice, 130 commercial content disclosure),
  ordered by coverage impact; coverage matrix updated with
  the new signed-in device management row.

- Patterns catalogue: new Trial-end reminder row in
  `catalog/patterns.md`, completing roadmap action 124: a
  notice sent a few days before a trial's first charge,
  stating the charge date, the amount, and the plan that
  follows, with a cancel route that works before the charge
  and a stated rule for what access continues after
  cancelling; 1 new source record (453 total).
- Patterns catalogue: extended Data visualisation row in
  `catalog/patterns.md`: an audio rendering of a chart, where
  offered, complements the text alternative and data table,
  maps rising values to rising pitch, announces each value as
  it plays, and stays under the person's control with pause
  and stop, never starting on its own; 1 new source record
  (452 total).
- Patterns catalogue: new Tip selection row in
  `catalog/patterns.md`, completing roadmap action 125:
  preset amounts, a custom amount, and an explicit no-tip
  choice shown together, the total updated before
  confirmation, and a stated rule for whether the tip can
  change after the order is placed; 1 new source record
  (451 total).
- Patterns catalogue: new Split shipment display, Price-drop
  alert, and Guest order lookup rows in `catalog/patterns.md`,
  completing roadmap actions 121, 122, and 123; coverage
  matrix updated with the three new rows; three new
  improvement actions added (124 trial-end reminder, 125 tip
  selection, 126 delivery photo proof); 3 new source records
  (450 total).
- Patterns catalogue: extended What's-new announcement row in
  `catalog/patterns.md` — match the surface to the impact with a
  badge and unread count for ongoing news, a slim top bar with
  one action for a broad change, a corner card for a single
  feature worth discovering, and a modal only for a change that
  blocks a task or changes terms, shown once at a natural pause
  and never mid-task, each announcement shown only to the people
  it affects and at most once per person.
- Primitives catalogue: extended Tooltip row in
  `catalog/primitives.md` — use only for a short explanation tied
  to one element, with a richer anchored surface or guided flow
  where an action or several connected steps are needed, a
  trigger tied to a specific observable behaviour rather than
  unprompted display on load, dismissible and hoverable
  behaviour with keyboard-focus reachability, an explicit
  trigger for touch users rather than hover alone, and a switch
  to a richer anchored surface where the message outgrows a
  tap-triggered tip.
- Patterns catalogue: new Preorder purchase row in
  `catalog/patterns.md` — the item marked as a preorder wherever it
  appears and never presented as in stock, the release or shipping
  date beside the buy action, full-price or deposit terms with the
  balance, due date, and total stated before payment, a preorder
  order view with amount paid and amount still due, a delay notice
  stating the new date with a cancel route where one remains open,
  and cancellation with refund terms stated at the point of
  cancelling, distinct from the waitlist row and the back-in-stock
  alert request row.
- Patterns catalogue: new Guided route navigation row in
  `catalog/patterns.md` — one current step at a time with
  direction, distance, and plain instruction plus a next-step
  preview, a visible travel estimate updated on route change,
  immediate rerouting with the change stated and a plain
  calculating state, lane guidance before complex junctions,
  spoken guidance kept in step with a mute control that does
  not stop navigation, and a plain arrival message with an end
  control, distinct from the route planning row.
- Patterns catalogue: extended Order tracking row in
  `catalog/patterns.md` — where an order splits into several
  shipments, state the split as soon as it is known, never show a
  single order-level progress bar for a split order, list the
  items in each shipment beside that shipment, and keep the
  overall order state as a summary of its shipments.
- Patterns catalogue: new Household member management row in
  `catalog/patterns.md` — every member listed with a role stated
  in plain words and what that role can see and change, invites
  that state their scope and stay pending with resend and
  withdraw routes until accepted, role changes that state their
  effect before confirmation, and removal that states what is
  lost, takes effect at once, and never strands a household
  without a managing member.
- Patterns catalogue: new Checkout price-change confirmation row
  in `catalog/patterns.md` — on any price, fee, or discount change
  between cart view and payment, stop before charging, state the
  old total, the new total, and what changed line by line, and
  require a fresh confirmation of the new total, with edit-cart
  and cancel routes that keep entered details.

- Patterns catalogue: new Document scanner row in
  `catalog/patterns.md` — state what scanning will do before the
  camera opens, show detected edges in place with adjustable
  corners before a page is kept, capture automatically only when
  the document is steady and fully in view with a manual control
  beside it, keep captured pages as a reorderable, retakable list
  with a plain page count, offer a readable filter choice while
  keeping the original reachable, and keep an import-from-library
  route where camera access is refused, distinct from the code
  scanner, document signing, and file upload rows.
- Patterns catalogue: new Magic link sign-in row in
  `catalog/patterns.md` — ask only for the identifier, put the
  sign-in action first in the message with its stated validity,
  never complete sign-in on the first fetch alone but on an
  explicit confirmation, give expired or already-used links their
  own resend screen, replace an older link on a newer request,
  and keep an alternate sign-in route visible, distinct from the
  verification-code entry, passkey sign-in, and account recovery
  rows.
- Patterns catalogue: Order tracking row in `catalog/patterns.md`
  extended — a live position view kept secondary to the stage,
  delivery window, and arrival estimate stated in words, a stated
  last-updated time with a plain stale-position fallback to the
  last confirmed stage and window, a recalculated arrival estimate
  stated beside the stage when it moves, and a proof-of-delivery
  record attached to the delivered stage with a route where the
  proof does not match the order received.
- Patterns catalogue: Form flow row in `catalog/patterns.md`
  extended — never move focus automatically to a field when a
  form loads, and non-standard controls, or required fields that
  cannot be filled in from stored information, carry a short
  explanation and a worked example beside the control itself
  rather than only in help.
- Patterns catalogue: new In-app survey row in
  `catalog/patterns.md` — a short structured survey kept to a few
  essential, skippable questions, closed answers paired with an
  optional open field for the reason, container matched to length
  and disruption (inline, popover or sheet, or an opted-in full
  page), asked at the end of a process rather than
  mid-transaction or on every page, progress and back-navigation
  across steps, and in-place confirmation, distinct from the
  problem-report, rating-submission, and poll rows.
- Patterns catalogue: new Subscription pause row in
  `catalog/patterns.md` — pause start stated as at once or at the
  next billing date, exact resume date, access during the pause,
  and whether billing stops, fixed duration choices with stated
  limits on frequency and length, a paused-state label carrying
  the resume date, early resume restoring the same plan without
  a new sign-up, a warning before billing resumes, and the route
  to ending the plan kept visible from the paused view, distinct
  from the subscription cancellation row and the subscription
  plan change row.

- Patterns catalogue: new Saved search alert row in
  `catalog/patterns.md` — the exact criteria stated in the
  alert and repeated in each message, a plain check frequency,
  only new matches reported and nothing sent when nothing new
  matches, a stated rule that the alert follows the saved
  search as currently defined, and pause and stop controls from
  the alert itself and from the alert list, distinct from the
  back-in-stock alert request, saved-filter view, and
  saved-item collection rows.

- Patterns catalogue: new Data import row in
  `catalog/patterns.md` — expected and required fields stated
  before file choice, column-to-field mapping with unmapped
  and ambiguous matches flagged, a preview with create,
  update, skip, and blocked counts before anything is
  committed, errors tied to exact row and field, a stated
  commit rule so a failed import never leaves a silent
  half-import, and a reachable failure report with a
  retry-only-failed-rows route, distinct from the data
  export row and the file upload row.

- Patterns catalogue: new Meeting and event creation row in
  `catalog/patterns.md` — attendee and resource availability
  checked before confirming, conflicts stated in plain words
  with the next available time offered, the time zone stated
  beside every time shown, and a route to carry the confirmed
  event into the person's own calendar, distinct from the
  calendar and scheduling row and the invitation response row.

- Patterns catalogue: new Shared resource booking row in
  `catalog/patterns.md` — booking from availability with
  capacity and equipment stated for each choice, buffer time
  treated as blocked time, approval stated before submission
  where it applies, freed bookings released at once, and a
  stated rule for a bundled booking where one item is
  unavailable, distinct from the appointment management row.

- Patterns catalogue: new Backup payment method row in
  `catalog/patterns.md` — a second stored method chosen in
  advance and stated at checkout, charged only after a failed
  primary attempt with a plain notice, never charged alongside
  the primary method for one order, and falling back to
  payment failure recovery where no usable backup remains,
  distinct from the stored payment method expiry warning row.


- Patterns catalogue: new Referral invitation row in
  `catalog/patterns.md` — benefit stated for both sides before
  sharing, qualifying action stated plainly, share controls with
  copy confirmation, referral progress through invited, signed up,
  qualified, and rewarded states, and a history that exposes no
  more of the invited person's activity than the referral itself,
  distinct from the loyalty rewards and promo-code entry rows.

- Primitives catalogue: Slider row in `catalog/primitives.md`
  extended — use only where an approximate value is enough, current
  value always shown in text, keyboard contract of arrow keys for one
  step, page keys for a larger step, and Home and End for the ends,
  and two-thumb ranges with each thumb named for the end it controls
  and values kept in order, distinct from the filtering row's
  slider-and-typed-input pairing for facet ranges.

- Patterns catalogue: new Transcript editing row in
  `catalog/patterns.md` — audio and text kept in sync in both
  directions, spoken segments as editable units with stated start
  times, tentative wording marked and corrected in place, speaker
  labels in words, and a confirmed route to remove a sensitive
  passage, distinct from the live captions row.

- Patterns catalogue: Payment instalment plan row in
  `catalog/patterns.md` extended — where choosing the plan starts an
  eligibility or approval check, the check, its duration, and the
  no-order outcome if approval is not given are stated before the
  choice, an earlier check is offered where available, and
  pre-checkout instalment wording stays tied to the actual order
  total and conditional.

- Patterns catalogue: new Document signing row in
  `catalog/patterns.md` — a draw route with a redraw route before
  applying, drag placement with a keyboard or menu alternative, a
  review of the document name and page before confirming, a signed
  record carrying signer name and signing date, and sequential or
  parallel signing order stated plainly with each signer's status
  in words, distinct from the annotation and file upload rows.

- Patterns catalogue: new Timeline view row in
  `catalog/patterns.md` — work laid along a shared time axis with
  labelled scales, item bars for durations, milestone points,
  dependency links stated before dependents shift, a now marker
  keeping past, current, and planned work distinct, zoom that
  changes detail level, and grouping or clustering for dense
  stretches, distinct from the Activity feed and Calendar rows.

- Patterns catalogue: new View switcher row in
  `catalog/patterns.md` — switching one collection between list
  and grid presentations without changing its items, order, sort,
  or filters, with a labelled single-select control, preserved
  selection, focus, and scroll position, a remembered choice across
  sessions, and a list fallback where a grid would truncate
  essential facts, distinct from the List navigation row.

- Patterns catalogue: extended Subscription cancellation row in
  `catalog/patterns.md` — paused-subscription rules: what access
  continues during a pause, whether billing stops, and the exact
  resume date, a paused-state label carrying that date wherever
  the plan is shown, a reminder before billing resumes, a one-step
  resume without a new sign-up or setup, and a cancellation path
  kept visible from the paused view.

- Patterns catalogue: new Tree view row in
  `catalog/patterns.md` — a nested hierarchy navigated as a
  single tab stop with arrow-key expand and collapse, stated
  branch state, level, and sibling position, ancestor expansion
  on selection, and children loaded on expansion rather than
  a branch shown as empty while loading.

- Desktop layout: new touch-as-secondary-input rules in
  `layouts/desktop.md` — layout and control sizes stay unchanged
  when switching inputs, tap targets enlarged beyond visible
  bounds, temporary enlarged controls for small or closely spaced
  targets, tap-near-content reveal plus touch-and-hold context
  menu as the touch routes for hover-revealed actions, and touch
  designed for brief, intentional interactions.

- Patterns catalogue: new Product configurator row in
  `catalog/patterns.md` — guided questions that narrow options to
  those fitting the stated use, a live preview with price and
  availability updated on every choice, a running summary editable
  from the summary, and a full-build review before an order or
  quote request.

- Patterns catalogue: extended Search row in
  `catalog/patterns.md` — matched-substring highlighting inside
  each suggestion, previous rows kept on screen while new
  suggestions load so the panel never flashes empty, and a
  distinct refinement control that appends a suggestion to the
  query without running the search.

- Patterns catalogue: new Pass or ticket transfer row in
  `catalog/patterns.md` — the pass or ticket named in full
  before the offer is sent, a transfer that moves only on the
  recipient's acceptance, a pending state shown to both sides
  with its expiry, a sender cancel route before acceptance, a
  declined or expired offer returning the item at once, and
  the original invalidated once accepted. Completes roadmap
  action 115.

- Patterns catalogue: new Undo send row in
  `catalog/patterns.md` — a short configurable delay after the
  send action with a visible undo control for the whole window,
  returning the message to the compose view intact on undo, and
  a plain statement that the message can no longer be stopped
  once the window ends.

- Patterns catalogue: new Pass and ticket display row in
  `catalog/patterns.md` — a scannable code shown large on a
  plain high-contrast background with brightness raised while
  displayed, the pass stated in words beside the code, saved
  passes available without a connection, and a typed-code or
  staff route when a scan fails. Completes roadmap action
  109.

- Patterns catalogue: new Shared cart row in
  `catalog/patterns.md` — each item naming who added it, one
  stated checkout owner, a plain rule that only the owner may
  remove another person's item, and a stated outcome for a
  contributor's items when they leave. Completes roadmap
  action 110.

- Patterns catalogue: new Stored payment method expiry
  warning row in `catalog/patterns.md` — a warning ahead of
  expiry stating which method and its expiry month, a
  replacement route in the warning that keeps future orders
  and plans working, and no expired method offered at
  checkout. Completes roadmap action 111.

- Roadmap: three new improvement actions (115–117) — pass
  or ticket transfer, backup payment method, and checkout
  price-change confirmation; coverage matrix updated with
  the three new rows.

- Resources: 3 new source records (419 total): wallet pass
  display guidance, shared cart purchasing, and expired
  stored-card management.

- Patterns catalogue: new Route planning row in
  `catalog/patterns.md` — an ordered stop list kept in step with
  numbered map markers, typed, listed, and map-tap entry,
  fixed first and last stops, an optimise action that reorders
  only the stops between them, a stated distinction between a
  pause stop and a pass-through point, and totals recalculated
  after every change.

- Resources: 1 new source record (416 total): multi-stop
  route planning with ordered waypoints.

- Patterns catalogue: new Expandable table row in
  `catalog/patterns.md` — a named toggle per row that holds
  detail, short detail in a detail row beneath its parent row
  and long detail as a separate detail view, the expanded
  state stated in text and announced to assistive technology,
  focus kept on the toggle, and collapsing never discarding
  entered input inside the detail. Completes roadmap action
  112.

- Roadmap: three new improvement actions (112–114) —
  expandable table row, meeting and event creation, and
  shared resource booking — with action 112 marked
  implemented; coverage matrix updated with the new row.

- Resources: 3 new source records (415 total): data table
  expansion and column controls, add-to-calendar event
  creation, and shared room and resource booking rules.

- Patterns catalogue: Data visualisation row in
  `catalog/patterns.md` extended — a key value must never
  live only in a tooltip; values that matter belong on the
  chart or in the data table, since hover-only values are
  unreachable by keyboard and touch.
- Patterns catalogue: new Workspace switcher row in
  `catalog/patterns.md` — the current workspace stays legible
  on every screen, switching re-scopes all content to the new
  workspace, a single workspace collapses to its identity
  alone, and a long list gains search or filtering, distinct
  from the account switcher row.
- Patterns catalogue: new Payment instalment plan row in
  `catalog/patterns.md` — each plan states its number of
  payments, each payment's amount and date, and the total
  cost including any charges before confirmation, with a
  single place to view remaining payments and change the
  payment method, distinct from the split payment row.
- Patterns catalogue: new Subscribe-and-save purchase
  option row in `catalog/patterns.md` — a recurring choice
  beside the one-time purchase stating the repeat interval
  and repeat price, with pause, skip, change, and cancel
  taking effect before the next order's cutoff, distinct
  from the subscription plan change row.
- Patterns catalogue: new Pickup point selection row in
  `catalog/patterns.md` — each point states distance and
  opening hours, the holding period is stated at choice
  time and in the ready notice, and the point can be
  changed while the order can still be changed, distinct
  from the delivery slot picker row.
- Patterns catalogue: new Live captions row in
  `catalog/patterns.md` — captions stay visible and movable,
  speakers are labelled in words, uncertain wording is shown
  and corrected in place, caption preferences sit beside the
  other call settings and are remembered, and a searchable
  transcript stays beside the live view, distinct from the
  recorded-media captions toggle.
- Source record for the live-caption guidance in
  resources/sources.json.
- Source records for the instalment, recurring-purchase,
  and pickup guidance in resources/sources.json.


- Primitives catalogue: Switch row extended in
  `catalog/primitives.md` — the label stays fixed when the
  state changes, any on/off wording is separate from the
  label, the state is shown by position and shape as well as
  colour, and a compact switch without on/off wording marks
  the on state with a visible tick.
- Source record for the switch accessibility guidance in
  resources/sources.json.

- Patterns catalogue: new Quote reply row in
  `catalog/patterns.md` — a reply shown in place with a short
  preview of the quoted message, a jump back to the original,
  and a preview that stays as sent when the original is edited
  or deleted, distinct from the threaded reply row.

- Patterns catalogue: new Offline download row in
  `catalog/patterns.md` — size and storage stated before the
  download starts, progress with pause and resume that keep
  what was already fetched, expiry stated before downloading
  and re-checked when the content is opened, and removal
  that frees storage at once.

- Patterns catalogue: new Sensitive-action re-confirmation
  row in `catalog/patterns.md` — a fresh confirmation tied
  to the consequential action itself, stating plainly what
  will change and whether it can be undone, never reusing an
  earlier sign-in as silent approval, and leaving everything
  unchanged when the re-confirmation is declined.

- Patterns catalogue: new Delivery instructions row in
  `catalog/patterns.md` — a short, actionable drop-off and
  access note at checkout, carried into the delivery record
  and shown back before payment, with a plain route to
  change it while the order can still be changed and a plain
  statement when an instruction cannot be honoured.

- Roadmap: coverage matrix refreshed to match the actual
  catalogue, and three new improvement actions added (106
  pickup point selection, 107 referral invitation, 108
  household member management).


- Patterns catalogue: new Live activity row in
  `catalog/patterns.md` — one ongoing task followed from
  outside the app, with its state stated in words beside any
  progress figure or countdown, a compact presentation kept
  to one state value, fuller detail only in an expanded view,
  stale data marked in words, finished or dismissed
  activities removed from every presentation at once, and a
  tap route that always lands on the matching in-app view.

- Patterns catalogue: new Address entry row in
  `catalog/patterns.md` — only the fields actually needed, in
  locale order with locale wording for the postal code, a
  single name field, a second address line hidden behind a
  reveal control, suggestions that fill editable fields with
  a manual entry route that never depends on a suggestion,
  and the full address stated in one place for checking
  before it is used.

- Patterns catalogue: new Character count row in
  `catalog/patterns.md` — the limit is stated in words beside
  the field before typing starts, the count is shown as
  characters used or remaining and announced to assistive
  technology on entry and at thresholds rather than on every
  keystroke, over-limit text states how many characters over
  the limit were entered, and text beyond the limit is never
  discarded silently.

- Primitives catalogue: extended Inline copy row in
  `catalog/primitives.md` — the copy button is labelled with
  the payload where the context does not name it, a shortened
  display still copies the full value, confirmation is given in
  words and through a status announcement and the control
  returns to its copy state, a failed copy keeps the value
  selectable for manual copying with the failure stated
  plainly, and a copy confirmation is never presented as proof
  of a later step such as installation or verification.

- Patterns catalogue: new Follow row in
  `catalog/patterns.md` — follow a topic, source, or person
  from beside the subject itself, followed state stated in
  words as well as shape, new activity added to the update
  stream with its subject named, a single followed list with
  one-action unfollow, a per-subject notification control
  separate from following, and unavailable subjects stated
  plainly rather than dropped silently.

- Patterns catalogue: extended Wizard row in
  `catalog/patterns.md` — the current step is marked for
  assistive technology as well as in sight, its position
  stated as step two of five, the new step announced on
  moving to it, and completed steps named in text rather
  than by a check mark alone.

- Patterns catalogue: new Suggestion review row in
  `catalog/patterns.md` — a proposing mode distinct from
  direct editing, proposed additions and removals marked in
  the text, per-proposal accept and reject with a linked
  discussion thread, accept-all and reject-all previews, and
  rejected proposals kept reachable in a resolved list.

- Patterns catalogue: new Home control map row in
  `catalog/patterns.md` — device markers placed where the
  device sits and grouped by room, state shown in words or
  shape as well as colour with unreachable devices stated
  plainly, a list alternative to the map, floor and room
  switching, device-type filtering, and named scenes that
  state what they will change before running.

- Patterns catalogue: new Selecting an option from a list row in
  `catalog/patterns.md` — match the control to the length of the
  list, showing a short set as a visible checkbox or radio group
  and a long set as a select menu or searchable combobox, with a
  custom option that reveals a text field and an add-another
  control for further custom values.

- Patterns catalogue: new Seat selection row in
  `catalog/patterns.md` — a seating map labelled by row
  and number with availability, selection, and
  unavailability stated in shape or text as well as
  colour, keyboard-focusable seats, a list alternative
  to the map, a selection summary with per-seat prices
  and a running total, and a stated hold length with a
  re-check at confirmation.

- Patterns catalogue: new Setup checklist row in
  `catalog/patterns.md` — an ordered list of setup tasks
  with done, current, and remaining states stated in text
  as well as in shape, each item linking directly to the
  task it names, a resume control returning to the first
  unfinished task, and a skip path that keeps skipped
  tasks reachable. Completes roadmap action 64.

- Patterns catalogue: new Return and exchange request row in
  `catalog/patterns.md` — a request started from the order
  itself naming the item, quantity, and reason in plain
  words, only the outcomes that apply offered per item, a
  stated label cost and drop-off or pickup route with a
  send-by date, and a request status kept visible on the
  order until the outcome is settled.

- Patterns catalogue: new Back-in-stock alert request row in
  `catalog/patterns.md` — an alert offered in place of the
  buy action naming exactly the item and variant it covers,
  a single alert per restock without added promotions,
  availability re-checked at the moment the alert is opened
  rather than promised in the message, and a stop route
  from the request and from the alert.

- Patterns catalogue: new Contact picker row in
  `catalog/patterns.md` — the system picker preferred where
  one is available so only the chosen contact reaches the
  task, a named searchable list with a choice of number or
  address where a contact holds several, a plainly stated
  scope for what the contact is used for, an add-contact
  route without leaving the task, and a manual entry
  fallback.

- Patterns catalogue: new Text-selection action menu row in
  `catalog/patterns.md` — a floating menu beside the selection
  that never covers the selected text, frequent actions of copy,
  share, and define first with further actions behind one
  secondary step, handles at each end of the selection on touch
  surfaces, stepwise expansion from word to passage to all,
  dismissal by tapping elsewhere or pressing escape, and cut and
  paste offered only where the text is editable.

- Patterns catalogue: new Split payment row in
  `catalog/patterns.md` — equal, by-item, or custom shares, a
  running total that must match the order total before
  confirmation, per-share status while the order stays pending
  until every share is paid, each payer receiving only their own
  share and receipt, and separate confirmation per method where
  one person pays with several methods.

- Patterns catalogue: new Notification preferences row in
  `catalog/patterns.md` — settings grouped by topic with an
  independent switch per group, a category-by-channel matrix, a
  per-category cadence of at once, scheduled summary, or off,
  quiet hours stating their end and what still breaks through, a
  per-source mute, quiet defaults for promotional updates, a
  single reset, and a plain statement where a system-level
  permission governs a choice rather than this screen.

- Patterns catalogue: new Reorder past order row in
  `catalog/patterns.md` — a reorder control on each past order
  and its detail view plus a per-item control, a cart review
  step showing current prices before payment, unavailable items
  stated with the rest of the order still repeatable, items
  already in the cart kept, and any discount or stored value
  from the past order stated rather than assumed.

### Changed

- Patterns catalogue: Draft autosave and recovery row in
  `catalog/patterns.md` extended — where several drafts exist
  they are listed newest first with a title or opening lines,
  destination or context, and last-saved time, a draft preview
  inside a parent list is labelled as a draft, opening a draft
  returns to editing rather than sending it, and discarding one
  draft never removes the others.

- Patterns catalogue: Notification list row in
  `catalog/patterns.md` extended — a snooze on an individual
  item returns it at the stated time as unread rather than
  dropping it, a whole-list pause states its end and what
  still breaks through, held items return as a grouped
  summary when the pause ends, and clearing a snoozed item
  cancels its return.

- Patterns catalogue: Search row in
  `catalog/patterns.md` extended — recent queries sit in their own
  labelled group separate from completions and suggestions, each
  recent entry offers its own removal alongside a clear-all
  control, only queries that were actually run are shown newest
  first, and the scope is stated plainly, with recents clearing
  on sign-out on shared devices unless the person chose otherwise.

- States catalogue: Theme preference states section in
  `catalog/states.md` extended — a quick header or toolbar control
  offers only the opposite of the current appearance, the three-way
  follow-system, light, or dark choice belongs in a dedicated settings
  view, nothing is stored until the person chooses, toggling back to
  the appearance that matches the system clears the stored value, and
  a stored choice is never cleared on its own when the system
  preference later changes to match it.

- Patterns catalogue: Form flow row in
  `catalog/patterns.md` extended — a field is checked once on
  leaving it rather than while typing, then re-checked on each
  change after an invalid mark so the error clears on
  correction; inline messages stay beside their fields in text
  with an icon or label, and a submit-time summary moves focus
  to the top, states the count, and links to each field while
  the inline messages stay in place.

- Patterns catalogue: Location selection row in
  `catalog/patterns.md` extended — grouped nearby markers state
  their count and look distinct from a single place, expand to
  the individual places on zoom or on activation, and every
  grouped place stays reachable through the list.

- Patterns catalogue: Product variant selection row in
  `catalog/patterns.md` extended — each option group is a named
  single-choice group, every option is a real named control rather
  than a styled shape alone, the chosen value and selected state
  are stated in words as well as in shape, keyboard focus stays
  visible, and pale swatches keep a visible border.

### Added

- Patterns catalogue: new Reading progress indicator row in
  `catalog/patterns.md` — a slim bar or ring that tracks only
  the main reading content, is omitted on pages short enough
  to read without scrolling, stays decorative for assistive
  technology with no repeated percentage announcements,
  honours reduced-motion settings, and pairs with the section
  outline for jumping rather than replacing navigation, kept
  distinct from the long-document navigation row.

- Patterns catalogue: new Usage allowance row in
  `catalog/patterns.md` — used, allowance, and remaining shown
  together as numbers in words with unit, period, and reset
  date per meter, threshold warnings with a top-up or upgrade
  route before the limit, a plain statement of what happens at
  the limit, and freshness stated where the figure may be
  stale, kept distinct from the Billing overview row.

- Patterns catalogue: new Emoji picker row in
  `catalog/patterns.md` — a picker beside the compose input
  with search by name or keyword, word-labelled categories, a
  limited clearable recents group, a persistent skin-tone
  choice for symbols that carry variants, insertion at the
  cursor, and keyboard-operable, word-labelled symbols, kept
  distinct from the Message reaction row.

- Patterns catalogue: new Restore purchases row in
  `catalog/patterns.md` — a plainly labelled restore control in
  the paywall and the account or billing area, restoring never
  charges again, progress shown while the purchase record is
  checked, restored items stated in words on success, a plain
  nothing-found statement with a sign-in and help route on
  failure, and spent consumable items excluded from restore.

- Patterns catalogue: new Sticky section headers row in
  `catalog/patterns.md` — only the current section header is
  pinned, the next header pushes it away, the pinned header
  stays compact with an opaque background, section headers
  are labelled headings in matching visual and underlying
  order, and pinning is omitted where it would leave too
  little room for content at high zoom.

- Patterns catalogue: Second-factor sign-in row in
  `catalog/patterns.md` extended — at enrolment every method
  is offered plainly with a chosen default where several are
  enrolled, and an authenticator-app setup pairs the QR code
  with a typed secret alternative and a text description, so
  enrolment never depends on scanning alone.

- Patterns catalogue: Activity feed row in
  `catalog/patterns.md` extended — new entries arriving while
  the feed is being read are held behind a count control
  instead of shifting content under the reader, activating
  the control adds them at the top with an announcement of
  how many were added, timestamps are relative with the
  exact time available on demand, and a connecting line is
  used only where order and elapsed time carry meaning.

- Patterns catalogue: new Rating distribution summary row in
  `catalog/patterns.md` — the average shown with its scale and the
  total number of reviews, the share of reviews at each rating
  level as labelled bars with counts in words, each level usable
  as a filter for the review list, and no merging of unrelated
  scores into one unexplained number.

- Patterns catalogue: new Password strength meter row in
  `catalog/patterns.md` — strength shown as guidance while typing,
  length judged first with a check against commonly used or
  compromised values, one actionable improvement at a time, a
  text label beside any colour indicator, and stable feedback
  that does not flash on every keystroke.

- Patterns catalogue: new Billing overview row in
  `catalog/patterns.md` — the current plan, next charge amount
  and date, and payment method stated before any upgrade offer,
  past invoices listed with period, amount, status in words,
  and a document route, amounts that may still change labelled
  as estimates distinct from finalised invoices, and a plain
  route to fix a missing or failed payment method.

- Patterns catalogue: new Home-screen widget row in
  `catalog/patterns.md` — one glanceable summary per size tier
  with a tap route to the matching view, a stated refresh
  cadence and last-updated time, loading and error states that
  keep the tap route working, and personal values cleared on
  sign-out or account switch.

- Patterns catalogue: new Deep-link landing row in
  `catalog/patterns.md` — an outside link landing on the exact
  content with its owning navigation selected, a reconstructed
  back stack so back leads to the parent view and section root,
  a plain fallback surface where the content is gone, and link
  context preserved where it still applies.

- Patterns catalogue: new Progressive disclosure row in
  `catalog/patterns.md` — supporting detail behind a labelled
  expand control, the expanded state stated in text as well as
  in shape, content kept in reading order when expanded, the
  expanded state retained where returning matters, and the core
  task never hidden inside a collapsed block.


- Patterns catalogue: new Link preview row in
  `catalog/patterns.md` — a pasted link expands to one card
  showing title, short description, thumbnail where available,
  and source in words, with a plain-link fallback where no
  destination details are available, one preview per message,
  and a sender control to remove the preview without removing
  the link.

- Patterns catalogue: new Loyalty rewards row in
  `catalog/patterns.md` — an available balance shown beside its
  plain currency value, pending points kept separate from
  available points, the nearest attainable reward and the gap
  to it paired with the balance, earning rules and expiry
  stated plainly, unavailable rewards kept out of the
  redeemable list, and a history covering earned, spent,
  expired, and reversed points.

- Patterns catalogue: new Waitlist row in
  `catalog/patterns.md` — joining a queue when capacity is full, a
  confirmed place with an honest position statement, an offer
  with a stated deadline that is never treated as an enrolment
  without acceptance, expiry that releases the offer onward,
  and a leave action that removes the entry at once.

- Patterns catalogue: new Media chapters row in
  `catalog/patterns.md` — chapter markers on the seek bar and a
  named chapter list with titles, start times, and durations, a
  current chapter stated in words, a transcript kept beside the
  player so it stays available in fullscreen, and announcements
  only for confirmed playback and seek changes.

- Patterns catalogue: new Saved payment method selection row in
  `catalog/patterns.md` — a named list of saved methods identified
  by type and last few digits only, a marked default preselected
  at checkout, a plain statement of which method will be charged
  before payment, unusable methods kept out of preselection, and
  edit and removal routes that never expose full details.

- Patterns catalogue: new Gift card and stored-credit redemption row in
  `catalog/patterns.md` — a code entry at checkout kept separate
  from any discount-code entry, the applied amount shown at once
  as a payment line beside the recalculated total, the remaining
  balance stated after a partial redemption, the remainder
  charged to another payment method in the same checkout where
  the stored value covers only part of the total, a balance
  check outside checkout, and the expiry rule stated before
  the code is applied.

- Patterns catalogue: new In-product feedback and problem report row in
  `catalog/patterns.md` — a report entry reachable from every screen
  without leaving the task, a plain choice of what went wrong, an
  optional screenshot or screen capture attached with consent, the
  current screen and task carried into the report so nothing is
  retyped, and a stated follow-up route rather than a silent
  submission.

- Patterns catalogue: new Order cancellation row in
  `catalog/patterns.md` — cancellation offered from the
  order itself while it can still be stopped, a plain
  statement of whether cancellation is still possible and
  until when, partial cancellation of the unfulfilled part
  where part of the order has shipped, a confirmation
  stating what is cancelled and what refund follows and
  when, and a cancelled order kept visible with its items,
  total, and refund state rather than deleted.

- Roadmap: three new improvement actions (97–99) — order
  cancellation, in-product feedback and problem report, and
  gift card and stored-credit redemption — with action 97
  marked implemented; coverage matrix updated with the new
  row.

- Patterns catalogue: new Account recovery row in
  `catalog/patterns.md` — one plain request screen with the same
  public response whether or not an account matches, every
  reachable verification route offered instead of a dead end, a
  failed verification falling back to another route, single-use
  expiring reset links or codes with a dedicated expired-link
  screen, stated password rules before submission, a success state
  with a sign-in route and a separate account notification, and
  saved work or sessions restored with a plain statement of what
  recovery does and does not restore.

- Source record for password reset guidance in
  resources/sources.json (1 new record, 355 total).

- States catalogue: new Status announcements section in
  `catalog/states.md` — announcement regions present from first
  load, polite announcements by default with interrupting
  announcements reserved for time-critical news, whole versus
  changed-part announcements, no announcement for every progress
  tick, focus never moved to deliver an announcement, and regions
  marked busy while an update is in progress.

- Source record for screen reader live region guidance in
  resources/sources.json (1 new record, 354 total).

- Patterns catalogue: new Appointment management row in
  `catalog/patterns.md` — reschedule and cancel actions beside the
  booked time on the confirmation, the original booking kept until
  a rescheduled slot is confirmed, the cancellation policy stated
  at booking, change routes carried in every reminder, and a freed
  slot offered onward rather than left unfilled.

- Source record for booking and appointment-management guidance
  in resources/sources.json (1 new record, 353 total).

- Patterns catalogue: new Delivery slot picker row in
  `catalog/patterns.md` — a date-first choice of delivery window
  at checkout, unavailable windows marked with a reason in words,
  cut-off times stated in the person's own zone, availability
  re-checked at confirmation, and the chosen window carried into
  the order confirmation.

- Patterns catalogue: new Product variant selection row in
  `catalog/patterns.md` — one control per option group, price,
  image, and availability updated together on a complete choice,
  unavailable combinations marked in place rather than removed,
  the add action held until every group has a choice, and the
  nearest available combination offered where a choice cannot be
  supplied.

- Source records for delivery scheduling and product variation
  guidance in resources/sources.json (3 new records, 351 total).

- Patterns catalogue: new Saved address selection row in
  `catalog/patterns.md` — a named list of saved addresses with a
  clear default, a one-action choice at checkout, an edit route
  that never overwrites another saved address, and a plain
  statement of which address receives the order before payment.

- Patterns catalogue: new Master-detail row in
  `catalog/patterns.md` — a list beside its detail on wide screens,
  the selected item stated in words as well as in shape, the detail
  updating without losing the list position, a stacked
  list-then-detail route with a clear back step on narrow screens,
  and a stated empty detail placeholder before anything is selected.

- Patterns catalogue: new Threaded message reply row in
  `catalog/patterns.md` — a reply anchored to the message it
  answers, a thread view keeping the original message visible,
  reply and unread counts stated in text, replies staying in the
  thread unless explicitly shared to the main conversation, a clear
  return route to the main conversation, and shallow nesting.

- Patterns catalogue: new Gift option row in
  `catalog/patterns.md` — a gift choice offered before payment, a
  per-item choice where only some items are gifts, prices hidden
  from the recipient while the buyer still sees full totals, an
  optional gift message with a stated length limit, and a separate
  recipient address that never overwrites the buyer's own address.

- Patterns catalogue: extended Chat and messaging row in
  `catalog/patterns.md` — group mentions notifying only the members
  of that group, a mute marker suppressing a message's
  notifications, no new mention notification when a message is
  edited, and mentions distinct in shape and text as well as
  colour.

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

### Fixed

- Patterns catalogue: Visa application row cross-check corrected —
  it named a passport renewal row that does not exist; the
  reference is removed.

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
