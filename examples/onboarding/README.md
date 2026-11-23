# Onboarding Example

A minimal, framework-free onboarding sequence: a step indicator with a
stated total, one task per step, an always-available skip, and a resume
path for skipped steps. Open `index.html` in a browser; no build step is
required.

## Classification

- Category: examples / onboarding

When to use:

- Checking the onboarding layout rules in `layouts/onboarding.md` against
  a working page.
- Testing step sequences, skip-and-return behaviour, and compact-screen
  placement of primary actions.

When to avoid:

- Production use; content is structural placeholder text.

## Elements and components

Step header with "Step 2 of 4" and a labelled progress bar; an always
visible skip action; one task per step with a smart-default prefilled
field; sticky action bar with back and continue; a resume panel for
skipped steps; inline demonstrations of every state.

## Layout and responsive rules

- The step total is stated up front ("Step 2 of 4"); the indicator
  advances on completion, not on press.
- Skip is always allowed and resumes later: skipped steps land in a
  resume panel with a one-tap return.
- One task per step with a prefilled smart default; the default stays
  editable and never skips validation once changed.
- Compact screens: the primary action bar is sticky at the bottom so it
  stays in thumb reach; vertical scrolling only.
- The layout is narrow by design, so the same markup demonstrates the
  compact-screen rules at any width.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The example page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | A variant in the markup shows the empty message with the one-tap suggested action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A variant in the markup shows an error message with a retry action. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the onboarding rules it documents.
- [ ] Run instructions work from a fresh checkout.
