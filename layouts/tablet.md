# Tablet Layout

The middle zone between compact phone layouts and expanded desktop layouts: medium and expanded window sizes where content gains a second pane and navigation changes shape. The layout adapts to width bands and fold postures, not to device names.

## Classification

- Category: layouts / tablet

When to use:

- Products used on tablets, foldables, and large phones in landscape — anywhere the window is wider than a phone in portrait but the input is still primarily touch.

When to avoid:

- Treating width as a device label; the same person rotates, resizes, and folds the same device, so bands must be handled live.
- Copying the desktop layout down; the middle zone has its own navigation and pane rules.

## Elements and components

Window size bands as the layout switch; adaptive navigation (bottom bar, rail, drawer); list-detail and supporting-pane compositions; posture-aware foldable arrangements; orientation-change continuity.

## Layout and responsive rules

- Base layout changes on width bands, not device names: compact is under about 600dp, medium is about 600–840dp, expanded is about 840–1200dp, with larger bands beyond.
- Navigation switches with the width band: compact width gets bottom navigation, medium width gets a navigation rail, expanded width gets a permanent navigation drawer; the rail appears around 600dp and the persistent drawer around 840dp.
- List-detail switches at roughly 600dp of width: below it, list and detail are separate full screens that swap; at or above it they sit side by side.
- Supporting-pane layouts follow roughly a 70/30 main/secondary split at expanded widths and 50/50 at medium; at compact widths the secondary content stacks or moves into a bottom sheet.
- Feed and grid layouts adjust column counts as space grows; card content order stays fixed so comparable values align across breakpoints.
- Orientation changes are continuity events, not resets: preserve scroll position, entered input, and selection when the band changes.
- Foldables need posture-aware layout, not just responsive layout: fully open behaves like a tablet with multi-pane layouts; half-open with a horizontal fold puts viewing content on the upper half and controls on the lower half; half-open with a vertical fold treats the halves as left and right pages with content kept clear of the crease; never place interactive elements, dialogs, pop-ups, or text across the fold; preserve in-progress state (for example mid-form input) when the device folds or unfolds so the task continues.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The tablet layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift; the band switch itself never triggers a full reload. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Window size bands, navigation switching, and two-pane thresholds are documented.
- [ ] Foldable posture rules are present.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
