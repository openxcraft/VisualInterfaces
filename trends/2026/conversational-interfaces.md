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

## When chat is the wrong surface

Chat is linear and ephemeral; it fails for multi-step workflows where context
gets lost, precise structured input and output, high-frequency repetitive
actions, and persistent collaborative context. Use this decision rule:

- Open-ended exploration and lookup: chat.
- Well-defined tasks with fixed fields: structured forms or wizards.
- Spatial or comparative work: visual surfaces.
- Frequent repeat actions: shortcuts, not another conversation.
- Hybrids let the person switch mode without losing context; a conversational
  layer beside a conventional interface routes each request to words, to the
  right screen, or to both, and states which one was chosen.

## Voice interaction states

Design the voice flow as if no screen existed, then add a visual layer that
confirms what was heard and shows what speech handles poorly, such as lists
and comparisons.

- One step at a time: confirm each step before moving on; state every change
  explicitly, since there is no visual to glance at.
- Offer at most about three spoken options at a time; keep responses short.
- Repair asks only for the missing piece, never restarts the whole exchange.
- Support barge-in: the person can interrupt and be understood.
- Interruption works the same everywhere: cut-ins are accepted at any point,
  including mid-prompt, and the flow resumes from the last confirmed step
  when no meaningful speech followed the interruption.
- Keep system utterances short enough to be interrupted safely at any point;
  long readings are broken into chunks with pauses.
- Timeouts are generous and adjustable: the person can ask for more time,
  and a silent response earns a simpler, more explanatory reprompt rather
  than a restart of the whole exchange.
- In noisy settings, confirm costly actions explicitly and offer a
  structured alternative, such as buttons or a keypad path, that works
  without speech.
- Set a loop limit: after repeated failures to understand, the system hands
  off or ends safely instead of asking the same question again.
- When recognition fails, say what was heard and what is needed, then retry
  the single step.
- Give every state its own timeout: silence after a question earns one
  re-prompt, then an alternative input such as a keypad, then a polite end;
  a system that is thinking too long speaks a short filler and gives up at
  a hard limit; a whole-conversation limit caps stuck loops and cost.
- Barge-in responds fast: aim to stop output within about 300 ms of speech
  start; on interruption, cancel playback, clear the audio buffer, and mark
  the context as interrupted so the system knows its answer was incomplete.
- Ignore backchannel words: "mm-hm" and "right" during system speech do not
  count as interruptions; require a minimum word count before a cut-in
  counts as one.
- Let the person interrupt routine speech, but never let an interruption
  block a mandatory disclosure from completing; a stop request always wins
  over whatever the system planned to do next.

## Voice-plus-screen pairing

When voice is paired with a screen, the voice flow must complete on its
own and the screen carries what speech handles poorly. No information
exists in one channel only.

- Channel assignment: voice carries commands, navigation, and quick
  answers; the screen carries lists, maps, and comparisons — anything the
  person needs to compare, review, edit, or confirm in detail.
- The visual layer confirms what was heard, shows detail that would take
  too long to read aloud, and highlights the field the system is
  currently asking about.
- The voice response never repeats the screen and never depends on
  screen-only information: the voice says "I found three nearby", while
  the screen shows the photos, ratings, and distances.
- A synchronised transcript of spoken output is always available; there
  is no fixed limit on response time, and the person can switch input
  methods mid-dialogue.
- After two failed understanding attempts, the third turn offers an exit —
  a handoff or a screen fallback — instead of repeating the same apology.
- When intent is uncertain, ask one focused clarification question rather
  than guessing.

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
