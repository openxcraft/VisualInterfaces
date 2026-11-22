# Tablet Example

A minimal, framework-free tablet layout using semantic markup and a single stylesheet. Open `index.html` in a browser; no build step is required. Resize the window across the 600dp and 840dp bands to see navigation change shape.

## Classification

- Category: examples / tablet

When to use:

- Checking the tablet layout rules in `layouts/tablet.md` against a working page.
- Testing width-band navigation switching, list-detail composition, and foldable posture handling.

When to avoid:

- Production use; list entries, values, and messages are structural placeholders.

## Elements and components

Adaptive navigation that switches from a bottom bar to a rail to a permanent drawer; a list beside its detail pane; a supporting pane at roughly a 70/30 split at expanded widths; a foldable posture variant with a marked crease; a continuity note for orientation changes.

## Layout and responsive rules

- Below about 600dp the navigation is a bottom bar and list and detail are separate full screens that swap.
- At or above about 600dp the navigation becomes a rail and list and detail sit side by side.
- At or above about 840dp the navigation becomes a permanent drawer and a supporting pane joins the detail at roughly a 70/30 split.
- Orientation changes preserve scroll position, entered input, and selection; the note field below keeps its value across the change.
- In the foldable posture variant, content stays clear of the marked crease; no interactive element, dialog, or text crosses it.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The example page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on navigation items and buttons: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks replace the detail pane while it loads. | Keep layout dimensions stable so content does not shift; the band switch itself never triggers a full reload. |
| Empty | The list variant shows the layout structure with an explanation and one action that adds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Navigation stays in place and the failure shows in the content area with a retry action. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the tablet layout rules it documents.
- [ ] Navigation switches bottom bar, rail, then drawer across the width bands.
- [ ] Run instructions work from a fresh checkout.
