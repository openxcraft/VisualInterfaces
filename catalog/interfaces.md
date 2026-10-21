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
- Wearable surfaces follow glanceable rules: one glance per screen, at most two actions, text short enough to read in seconds; design ambient (always-on) and active display states separately. Where hands are busy, a voice action covers the same two options; every voice action states what it understood before confirming.
- Design for states, not devices, on folding surfaces: closed, half-open, fully open, and tent. The fold is a seam, not a wall — content flows across it while interactive elements reposition away from the hinge; transitions never reload and restore scroll and focus exactly.
- Across surfaces, one task continues where it stopped: navigation migrates from bottom bars on compact surfaces to side rails on expanded ones without changing order, and components morph from terse to detailed while the underlying action stays the same.

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
