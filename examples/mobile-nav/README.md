# Mobile Navigation Example

A minimal, framework-free handheld layout with a top app bar, scrolling content cards, and a fixed bottom tab bar. Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / mobile-nav

When to use:

- Checking the mobile navigation rules in `layouts/mobile-nav.md` against a working page.
- Testing safe-area padding, label visibility, and badge behaviour.

When to avoid:

- Production use; content is structural placeholder text.

## Elements and components

Top app bar with title and one action; content list of cards; fixed bottom tab bar with four labelled destinations and one badge.

## Layout and responsive rules

- Tab bar height plus safe-area padding is reserved at the bottom of the content.
- Labels are always visible under each abstract mark.
- On wider screens the same destinations move to a side rail without reordering.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The example page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | A card variant in the markup shows an empty section message with one action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A card variant in the markup shows an error message with a retry action. | Keep entered data, place the message next to the problem, and offer a retry. |

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
