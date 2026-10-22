# Modular Card Grids

Dashboard and home surfaces arranged as a grid of self-contained cards of a few fixed sizes, each with one topic, one summary, and one link to detail.

## Classification

- Category: trends / 2026 / modular-card-grids

When to use:

- Overview surfaces that combine many content types and must reflow across devices.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.

## Elements and components

Cards in two or three fixed sizes; a grid with consistent gaps; card header with title and one action; summary content; a detail link.

## Layout and responsive rules

- Cards keep a fixed internal order: title, summary, action.
- The grid reflows by moving whole cards, never by resizing text inside a card.
- Compact: one card per row, ordered by importance.
- Tile markup is written in priority order; named placement areas rearrange tiles at each breakpoint without changing source order, so assistive technology and keyboard focus follow the same sequence at every size.
- Empty cards are replaced by a single placeholder card with one next action, not a blank space.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The pattern in use at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show a neutral starting prompt or placeholder with one example action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | State what could not be completed and offer the structured fallback or a retry. | Keep entered data, place the message next to the problem, and offer a retry. |

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
