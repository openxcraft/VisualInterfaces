# Interface Types

A taxonomy of interface types by platform, input method, and viewing distance. Choose the type first; layout and density follow from it.

## Classification

- Category: interfaces

When to use:

- Selecting a primary surface for a product or feature.
- Checking whether a pattern fits the input method and screen size in use.

When to avoid:

- Copying a pattern from a different input method without adapting targets, focus order, and density.

## Elements and components

| Interface type | Primary input | Viewing distance | Density | Key constraints |
| --- | --- | --- | --- | --- |
| Web application | Pointer, keyboard | Arm's length | Medium to high | Browser chrome, variable window sizes |
| Mobile application | Touch | Handheld | Low to medium | One-handed reach, interruptions, variable connectivity |
| Tablet application | Touch, pointer | Handheld to arm's length | Medium | Split views, orientation change |
| Desktop application | Pointer, keyboard | Arm's length | High | Multiple windows, shortcuts, context menus — see `layouts/desktop.md` |
| Kiosk | Touch | Standing distance | Low | Large targets, idle timeout, session reset, no personal data retained |
| Wearable | Touch, voice, crown or bezel | Glanceable | Very low | Two actions per screen at most, short text |
| Television | Remote, voice | Room distance | Low | Focus-based navigation, 10-foot legibility, overscan margins |
| Conversational | Text, voice | Varies | Low | Turn-taking, repair of misunderstood input, fallback to structured controls |
| Spatial | Gesture, gaze, voice | Room scale | Low | Depth cues, physical comfort, clear exit to a flat view |
| Embedded display | Touch, physical controls | Arm's length | Low | Fixed size, offline operation, high contrast in bright light |
| Email and message view | Pointer, touch | Varies | Low | Narrow column, limited interactivity, plain-text fallback |

## Layout and responsive rules

- Design for the primary input first; add secondary input without breaking the primary flow.
- Set density by distance: glanceable and room-distance interfaces use larger type and fewer items.
- Compact screens show one task per view; expanded screens may combine a list and a detail view.
- Every interface type defines keyboard or focus order, even when touch is primary.
- Respect safe areas, overscan margins, and physical control placement on fixed devices.
- Wearable surfaces follow glanceable rules: one glance per screen, at most two actions, text short enough to read in seconds; design ambient (always-on) and active display states separately. Where hands are busy, a voice action covers the same two options; every voice action states what it understood before confirming. For voice paired with a screen, follow the channel-assignment rules in `trends/2026/conversational-interfaces.md`.
- Design for states, not devices, on folding surfaces: closed, half-open, fully open, and tent. The fold is a seam, not a wall — content flows across it while interactive elements reposition away from the hinge; transitions never reload and restore scroll and focus exactly.
- Across surfaces, one task continues where it stopped: navigation migrates from bottom bars on compact surfaces to side rails on expanded ones without changing order, and components morph from terse to detailed while the underlying action stays the same.

## Gesture-only input

For surfaces where gestures are the only input — gesture-first screens,
motion sensing, and gesture-first wearables — gestures replace buttons, so
the design must teach them and tolerate mistakes.

- Keep the gesture set small: a few consistent gestures across the whole
  surface, each with one meaning everywhere it appears.
- Teach without a manual: pair every essential gesture with a visual hint,
  an animated affordance, or a visible button alternative until it is
  learned.
- Tolerate variation: accept gestures performed at different speeds and
  angles; set clear thresholds — minimum movement for a drag, minimum hold
  for a long press, clear velocity cutoffs for a fling — and never treat a
  near miss as a command.
- Give immediate feedback when a gesture is recognised: highlight, motion,
  or a haptic pulse that matches the action.
- Make errors cheap: every gesture is reversible or confirmable; an
  unrecognised gesture states what was seen and how to retry, never a dead
  end.
- Respect the body: avoid gestures that tire quickly or demand precision
  repeated many times; offer a non-gesture alternative for every essential
  task.
- Every multipoint or path-based gesture (pinch, swipe, drag) is also
  operable with a single pointer — tap or click — unless the gesture itself
  is essential; never restrict a task to one input modality.

### Worked example: swipe-to-archive in a gesture-first list

One surface, one worked example, to show how the rules compose.

- Discoverability: the row edge shows a drag handle and the next row peeks
  from the side; the first time the list appears, a one-time coach mark
  points at a row and says "swipe to archive"; archive also appears as a
  visible control in the row's detail view.
- Progressive teaching: swiping a few pixels reveals the archive action
  beneath the row, teaching the gesture through the interaction itself.
- Thresholds: movement under about 8 px is a tap, not a drag; around 24 px
  begins revealing the row action; a drag commits to a direction after
  about 10 px of hysteresis, then tracks the finger one-to-one.
- Feedback: the row highlights on touch-down instantly; the gesture is
  tracked continuously so the archive tint deepens as the swipe extends —
  the surface never waits for the gesture to finish before responding.
- Recovery: committing happens on lift-off, not on touch-down; dragging
  away and back cancels; after commit, an inline undo stays available, and
  a swiped-near-miss is never treated as a command.
- Seven states for the example: default shows the list with the hint
  affordance; hover has no pointer equivalent and is not used; active
  tracks the finger with the archive tint; disabled dims archive where
  items cannot be archived, with the reason stated; loading is not
  gestured — a spinner row replaces nothing; empty shows the list empty
  state from `catalog/states.md` with the first-use variant; error keeps
  the item in place and states what failed with a retry.

## Remote-control input

For room-distance screens where a remote is the primary control: design
directional-pad first, then enhance. For display-side television rules —
type minimums, safe margins, and focus drawing — see `layouts/tv.md`.

- Treat the directional pad (up, down, left, right, select, back) as the
  common denominator: every task must be completable with it alone.
- Pointer remotes add a cursor on top of focus order; never require a
  precise pointer action that the directional pad cannot perform.
- Touch-surface remotes send velocity, not position: keep the underlying
  focus behaviour so the same navigation works, and keep focus movement
  predictable per flick rather than per pixel.
- Scroll-wheel remotes map to one-dimensional focus movement; horizontal
  wheels move within the current row, vertical wheels move between rows.
- Keep remote fatigue low: predictable focus order, short paths to the
  most-used content, no focus traps, and focus memory that survives
  back-and-forth navigation.

## Spatial interfaces

For head-worn and room-scale surfaces: content placed in depth, read at
room distances, and always escapable back to a flat view. For the full
treatment — comfort zones by gaze angle, distance tiers, panel choice, and
capability tiers with two-dimensional fallbacks — see
`trends/2026/spatial-interfaces.md`.

- Three depth arrangements cover most surfaces: flat (all content on one plane
  at a comfortable distance — dashboards and reference panels), layered
  (gentle near/mid/far stacking — glanceable context with drill-down
  detail), deep (nested rooms or portals — guided focus through a
  sequence).
- Place primary actions closer than supporting content; depth contrast
  creates the focal order, so distance is never decorative.
- Comfort zone: content lives between roughly 1.25 m and 5 m. Detailed,
  frequent interaction sits at arm's length; general viewing between 1
  and 3 m; beyond 3 m is ambient information only. Closer invades personal
  space and risks collisions; farther is hard to read.
- Keep content inside the central field of view so the neck and body do
  not rotate to read it; never fully obscure the environment, and keep
  peripheral zones for large, simple supplementary content.
- Scale windows so type stays legible at any distance (dynamic scaling);
  use fixed scaling only for objects that should behave like physical
  things and appear smaller when farther away.
- Always offer a home zone at body-centre height so the user can reorient
  when spatial memory fails; back off-screen targets with positional audio
  cues and time-limited gaze rays.
- Every spatial surface offers a clear exit to a flat two-dimensional
  view; the exit control is reachable without navigating depth.
- Seven states for spatial: default is the home zone with content at its
  assigned depths; hover is replaced by a gaze or focus highlight with a
  dwell confirmation, never motion alone; active confirms selection
  within 100 ms; disabled dims with the reason stated; loading anchors a
  progress indicator at a readable distance and never moves placed
  content; empty shows the first-use or naturally-empty variant in place;
  error brings a plain-language panel to the primary zone with retry and
  a flat-view exit.

## Embedded displays

For fixed panels in appliances, machinery, and wall-mounted controls,
see `layouts/embedded.md`: fixed-size canvases, bright-light contrast
rules, offline-first operation, and refresh constraints.

## Extension interfaces

For browser extensions and other add-on surfaces that act on host pages:
the classic click-the-icon, see-a-dropdown, interact, click-away flow is
giving way to the inline overlay: a floating panel anchored to the cursor
or to the page element being acted on, behaving as part of the page's own
interface rather than a separate layer.

- Anchor the overlay to the cursor position or the target element, not to
  the toolbar; keep the user inside their current task and context.
- Show results next to their source: translated text beside the original
  sentence, highlights on the text they annotate, previews where the change
  will apply. Closing the overlay never forces reorientation — the
  underlying page stays exactly where it was.
- Dismissal is cheap: one action closes the overlay and returns focus to
  the anchor; focus never leaks into the host page underneath.
- Build the overlay as a web component with a closed shadow root for style
  isolation. Avoid iframes: they complicate focus management and keyboard
  navigation.
- Defend against the host page deliberately: handle shadow DOM, z-index
  conflicts, and scroll events so the overlay behaves on arbitrary pages.
- Size to content, not to the toolbar: the old narrow dropdown panels
  forced squinting; give the overlay room up to sensible maximum bounds.
- Full keyboard access to every overlay control, in a documented order;
  never require pointer-only interaction.

## Assistant-rendered interactive components

Conversational interfaces increasingly answer with interactive components
rendered in place — buttons that act, calculators tuned to the question,
charts the reader can adjust, forms that capture the structured reply —
instead of flat text alone. The component is the answer, not a decoration.

- Render one component per idea; never stack several competing widgets in
  a single response.
- Match the component to the task: a diagram for how a mechanism works, a
  calculator for a planning question, a map for a route — never a widget
  for a question plain text already answers.
- Keep every rendered component fully operable by keyboard and by
  assistive technology: named controls, exposed states, documented focus
  order.
- Supply a text equivalent for anything shown only inside a widget — chart
  values, calculator inputs and results — so the response still reads on
  a screen reader or a text-only surface.
- Announce the arrival of a component politely; never steal focus
  mid-conversation.
- Prefer platform-native controls over bespoke widgets; when a custom
  control is unavoidable, own its focus behaviour on activation and
  dismissal.
- Size the component to the task, not to spectacle: it must earn its space
  by shortening the path to the answer.

## Wearable interfaces

For wrist-worn and other tiny screens: glanceable, single-action surfaces
with the phone app as the overflow.

- Glanceability is a structural constraint, not a style choice: design for
  a 2–5 second task window; put one primary piece of information per
  screen; move anything requiring more than two taps to the paired phone
  app.
- Treat information surfaces such as tiles as non-scrollable: they are
  meant to be read in a glance, with a tap leading to more detail on
  another surface.
- Size touch targets and gestures to the finger: minimum targets around
  38–48dp spaced at least 8pt apart; favour full-screen swipes for
  navigation, long-press for context menus, edge-based gestures, and
  rotating bezels or crowns as the primary scroll mechanism over fine
  swipe scrolling.
- Confirm actions with haptic feedback first, so the person gets
  confirmation without needing to look at the screen.
- Design for the round case first with larger margins: round displays
  offer roughly 22% less usable space than square ones.
- Ship a simplified ambient, always-on state alongside the active state:
  low brightness, no animation, critical data visible; prefer dark
  interfaces and minimal background work to protect battery life.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | An interface surface at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the purpose of the surface and one starting action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | State what failed, what is preserved, and how to retry or exit. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Every interface type in the table has a primary input, viewing distance, density, and constraints.
- [ ] The remote-control input section covers directional-pad, pointer, touch-surface, and scroll-wheel variants.
- [ ] Wearable, spatial, and embedded sections link to their full treatments.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
