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
| Desktop application | Pointer, keyboard | Arm's length | High | Multiple windows, shortcuts, context menus |
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

## Spatial interfaces

For head-worn and room-scale surfaces: content placed in depth, read at
room distances, and always escapable back to a flat view.

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

- [ ] Title and short description are present and accurate.
- [ ] Classification and when-to-use guidance are present.
- [ ] Elements, layout, and responsive rules are complete.
- [ ] All seven states are defined: default, hover, active, disabled, loading, empty, error.
- [ ] Text is neutral, short, and free of names of persons and organisations in editorial prose.
- [ ] No references appear outside the resources files.
- [ ] No secrets, contact details, local filenames, or system paths are present.
- [ ] Visuals, if any, are abstract shapes only.
- [ ] Internal links resolve and headings follow a consistent order.
