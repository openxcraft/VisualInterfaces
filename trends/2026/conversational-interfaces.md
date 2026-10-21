# Conversational Interfaces

Task completion through short text or voice exchanges, paired with structured controls for choices, corrections, and confirmation.

## Classification

- Category: trends / 2026 / conversational-interfaces

When to use:

- Tasks that are hard to express as a form, lookups, and guided multi-step requests.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.

## Elements and components

Message list with clear turn order; composer with send action; suggestion chips for common replies; structured cards for choices and confirmations; a visible way to restart or switch to a form.

## Rendered interface answers

A newer direction: instead of answering with text, the system answers with a
compact interface program composed from the product's registered components,
which the client renders progressively as it streams.

- Only components in the registered set can appear; anything outside the set
  never renders, so the registered set is the effective control on the answer.
- The instruction set that teaches the syntax must match the client runtime
  version; mismatched versions render nothing.
- A cut-off stream renders blank rather than a partial tree, so an incomplete
  answer is never presented as finished.
- Rendered programs remain inspectable: they are built from the product's own
  components and run on the shipped client.

## Layout and responsive rules

- Every conversational step offers a structured fallback: buttons, a list, or a form.
- Confirmations for costly actions are shown as a summary card, not only as text.
- Long answers are chunked with headings; actions sit with the chunk they affect.
- Compact and expanded layouts keep the composer fixed at the bottom of the view.

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
