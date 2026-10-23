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

Canonical state definitions live in `../../catalog/states.md`. Notes specific to card grids:

| State | Card-grid note |
| --- | --- |
| Default | Cards at rest in the grid, full contrast, labels clear. |
| Hover | Pointer-only lift or border change on the card. |
| Active | Pressed-card feedback within 100 ms. |
| Disabled | Card dimmed but readable; the reason stated on the card. |
| Loading | Skeleton cards matching the grid's card shape. |
| Empty | One explanatory card with the single next action. |
| Error | The failed card names the problem and offers retry in place. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Grid composition and responsive card rules are complete.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
