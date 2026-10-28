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
- Add an author-side gate: validate each interface tree against the
  registered set before it ships, so unknown components are caught when
  the tree is produced, not when it renders.
- Gate rules: every node must resolve to a registered component; a form
  may submit only to an approved destination; the check stays cheap
  enough to run on every tree.
- Live visuals inside a conversation are controls, not pictures: a visual
  that shows a quantity, a diagram, or a chart stays manipulable in
  place, so changing a control updates the linked values and
  explanations in that same visual, and selecting a part of a diagram
  swaps in the explanation for that part.
- Keep the visual usable after the conversation moves on: a person
  returning to an earlier visual can still change its controls and read
  the updated result, rather than finding a frozen snapshot.
- When a visual cannot update, say so in place and offer the same result
  as plain text or a structured form, never a picture that looks
  interactive but does nothing.
- Fix the answer shapes in advance: give each intent one shape — a
  side-by-side comparison for comparing options, a diagram for
  explaining a principle, a map for a route, a calculator for a
  calculation, and plain text where text suffices — and keep every
  answer inside that menu. Letting each answer invent its own shape
  makes one conversation feel like several different products.
- Offer a control to show fewer visuals, so a person who finds visuals
  in the way can return to text without leaving the conversation.

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
- Disclose automation before collecting anything sensitive: at the start
  of the interaction, in the caller's own language, state that they are
  speaking with an automated assistant — before any sensitive or
  decision-relevant information is collected. The disclosure covers
  identity, purpose, recording or transcription notice, an opt-out, and a
  path to a person. Repeat it after any transfer. Never claim to be human
  when asked.
- Recover from false interruptions cleanly: a cough, noise, or short
  non-speech sound is recorded as a candidate and the flow resumes from
  the last confirmed-played boundary instead of restarting; stale
  in-progress results are discarded, not spoken.
- Treat a genuine correction as a full stop, not a pause: when the
  person corrects the system mid-flow, stop playback, cancel any
  pending action that has not yet happened, keep the correction as the
  current instruction, and never resume the old answer.
- After a dropped connection, treat playback as unknown: never claim
  the person heard a sentence unless a receipt proves it; if the
  missing part affects the next action, ask a short confirmation
  before continuing.
- Make a reconnected request safe to repeat: reconcile what already
  happened before retrying, so reconnecting never books, sends, or
  charges twice for one request.

## Interruption budget and turn-taking rhythm

The interruption budget is separate from the response-latency budget:
people forgive a slow answer but not an assistant that keeps talking after
being cut off. Treat continued speech after an interruption as rudeness,
not slowness.

- Budget the stop pipeline, not just the answer: detect user speech, stop
  audio output, cancel in-progress generation, re-enter listening — target
  200–300 ms total; design an explicit "interrupted" state with an abort
  visual under 300 ms.
- Prefer learned turn-taking (acoustic plus semantic plus conversational
  context, landing end-of-turn around 200–250 ms) over bare silence
  thresholds; distinguish backchannel ("mm-hm") from true barge-in through
  turn classification, not word counts alone.
- Keep a turn-taking rhythm: break responses into digestible chunks, pause
  intentionally, and never fire long paragraphs at once.
- Fuse channels in voice-plus-screen contexts: speech with visual context,
  gestures, and camera input (look at an object, ask about it, receive an
  overlay); confirmations can arrive as haptic pulses and spatial audio,
  not only speech.
- Recover from errors by rephrasing the prompt, offering tappable options,
  or handing to support; in voice-only contexts never rely on buttons —
  design spoken fallbacks.

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

## Voice hybrid flows

Voice initiates, another channel confirms. Voice is fast for starting a
task and poor for verifying detail, so the flow splits the work: speak
to begin, then confirm on a channel that shows the detail.

- Voice-to-initiate with physical confirmation: for sensitive actions
  such as payments, sending, or sharing, the spoken request prepares
  the action and a tap or biometric confirmation completes it. The
  confirmation surface shows the full detail — amount, recipient, and
  effect — and the spoken request alone never completes the action.
- Visual mishearing repair: when the screen is available, show what was
  heard as editable text, with low-confidence words marked. Tapping a
  marked word offers likely alternatives, and re-speaking replaces only
  that part; never silently autocorrect a mishearing into a different
  action.
- Confirmation by stakes: low-stakes requests get an implicit echo in
  the reply ("Setting a timer for ten minutes"); high-stakes requests
  get an explicit confirmation naming the action and its effect before
  anything happens.
- Repair without a dead end: after a failed understanding, narrow the
  choice instead of repeating the same question — offer two or three
  options, or switch to typed or tapped input for the uncertain part.
  After two failed attempts, offer the screen fallback or a handoff
  rather than a third identical prompt.
- Cross-check the voice state matrix in ../../catalog/states.md and the
  voice-plus-screen pairing section above.

## Voice command discovery

Commands in a voice surface are invisible, so discovery has to happen
in context, not in a tour or a help page nobody opens.

- Suggested prompts on first use: show two or three example requests
  that work on the current screen, as tappable chips that fill the
  input rather than running at once, so the person can edit before
  sending.
- Example utterances for the current screen: the suggestions change
  with the screen — on a list, offer filtering and sorting requests;
  on a detail view, offer actions on that item. A suggestion that
  cannot run here teaches the person not to trust the next one.
- A browsable capability list: a "What can I say?" entry opens a
  short, grouped list of capabilities in plain words, searchable by
  typing, with one example utterance per capability. The list stays
  reachable from any screen, not only from first use.
- Teach inside replies: after a successful request, the reply may
  name one follow-up the person can try next ("You can also ask for
  the weekly summary"), never a catalogue of features.
- Progressive introduction: introduce advanced capabilities only
  after the basics are used, one at a time, and retire suggestions
  the person already uses regularly.
- Recovery as discovery: after a failed understanding, offer two or
  three things that can be said here instead of repeating the same
  question, and keep a typed or tapped path open for the uncertain
  part.
- Cross-check the voice-plus-screen pairing section above and the
  voice state matrix in ../../catalog/states.md.

## States

Canonical state definitions live in `../../catalog/states.md`. Notes specific to conversational interfaces:

| State | Conversational note |
| --- | --- |
| Default | The conversation surface at rest; input ready, history readable. |
| Hover | Pointer-only highlight on tappable turns and suggestions. |
| Active | The turn in progress; typing, speaking, or waiting shown within 100 ms. |
| Disabled | Input unavailable with the reason stated; history stays readable. |
| Loading | A named-step indicator, for example "Searching your documents"; no silent waits. |
| Empty | First-use prompt with one example request. |
| Error | Say what failed, keep the conversation intact, offer retry or another channel. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Interruption budget, barge-in, backchannel, and disclosure rules are current.
- [ ] Voice-plus-screen pairing cross-links to catalog/interfaces.md.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
