# Agentic Interfaces

Interfaces where a person briefs an automated agent, watches it work, interrupts it, and reviews what it did. The agent assists visibly and can always be paused; it never acts invisibly or beyond the scope it was given.

## Classification

- Category: trends / 2026 / agentic-interfaces

When to use:

- Products where agents carry out multi-step work on the user's behalf: gathering, drafting, scheduling, filing, configuring.

When to avoid:

- Adding supervision panels around trivial single-step actions, where a plain control is clearer.
- Letting an agent run unattended where a deterministic path is faster and less ambiguous.

## Elements and components

A briefing panel stating the request, the constraints, and the allowed scope before any work starts; a live activity view showing the current step, the queued steps, and a pause control that stays reachable; a preview-before-commit gate for irreversible or externally visible actions; an activity log with undo for completed actions; visible markers for what the agent is unsure about; and a manual path to do every agent task by hand.

## Step trace and tool output

Show what the agent did as a structured list of steps — a step trace —
rather than a wall of text or an open log:

- One line per step, each with an icon, a short title, an optional
  description, and a status. Every step looks and behaves the same.
- Statuses: running, error, pending. While a step runs, show a shimmer;
  never leave a running step silent.
- Lines expand to show more detail: a summary line expands into its
  sub-steps, and a step expands into its output.
- A line can link to a page or open a dialog, sheet, drawer, or popover —
  detail stays off-screen until asked for.
- Keyboard and screen-reader support on every expandable line; the trace
  is navigable, not decorative.

For technical output — code, terminal output, logs, diffs — use a
dedicated code block, never plain text:

- A header with a title and actions, such as copy or wrap.
- Line numbers, wrapping, diff styling, and highlighted lines, so a reader
  can point at the exact lines that matter.
- A small size when the block sits inside a step trace; full size only
  when the output is the main content.

## Layout and responsive rules

- Briefing and supervision live in one view; the person never hunts for the stop control.
- The pause control is reachable at every step, including during long unattended runs.
- Pausing never loses completed steps; resuming continues from the last confirmed one.
- Irreversible actions are previewed: the agent states exactly what it will do and waits for approval.
- Planned steps appear as an editable list; reordering or removing a step never restarts the whole run.
- The agent's working context — what it knows and what it is working on — is visible and editable.
- Suggestions appear alongside the content they affect; the user's own work stays untouched until accepted.
- On compact surfaces, supervision collapses to status, pause, and log, with detail expanding on demand.
- Completed work lands in a review queue with accept, edit, and undo before anything becomes final.

## Supervision patterns

Three habits keep agent-driven work trustworthy:

- **Suggest, do not replace.** Automated suggestions sit next to the content they affect. Nothing changes until the person accepts.
- **Interrupt at any point.** Long runs expose checkpoints at each step boundary. Stopping is cheap and reversible.
- **Show the working surface.** Sources, assumptions, and uncertainty are labelled in plain words, not hidden behind confidence alone.

Where an agent command applies to something already selected — a row, a
range of text, an item on a canvas — use the inline assistant-action
pattern from `catalog/patterns.md`: the command appears as a verb on the
selection itself rather than in a separate conversation surface.

## System-initiated surfaces

Sometimes the system starts the exchange instead of the person: it
notices a condition, prepares a next step, and offers it. The person
confirms, redirects, or dismisses — the system never completes a
consequential action on its own say-so.

- Surface only when the proposal is worth an interruption: a deadline,
  a blocked task, or a change the person would act on now. Everything
  else waits in a quiet summary the person checks on their own schedule.
- Never interrupt work in progress for a low-stakes proposal; queue it
  until the current task ends or pauses.
- Every proposal states what triggered it, what will happen if
  accepted, and what it costs to accept — in plain words, before any
  action.
- Offer confirm, redirect, and dismiss on the proposal itself;
  dismissal is a real answer, not a snooze that returns the same
  proposal unchanged.
- Dismissing a kind of proposal quiets that kind: repeated dismissal
  of the same class stops further proposals of that class until the
  person re-enables them.
- Background work reports back where the person will see it, with the
  same receipt as completed work: what changed, what was assumed, and
  what can still be undone — never a bare badge count.
- Keep a visible history of system-initiated proposals and their
  outcomes, so a dismissed or accepted proposal can be found and
  revisited.

## Six trust patterns across the action lifecycle

Structure every agent-driven flow around the same six patterns; treat them
as structural, not optional:

- **Pre-action: intent preview.** Show the plan before acting, with
  approve, edit, and do-it-myself options on the table.
- **Pre-action: autonomy dial.** Offer a per-context spectrum of
  independence with progressive authorisation, not a binary on/off switch.
- **In-action: explainable rationale.** State the plain-language why plus
  the confidence behind the current step.
- **In-action: confidence signal.** Carry badges, percentages, or
  qualitative labels that travel with the work.
- **Post-action: action audit and undo.** Keep a chronological log with
  per-action reversal as a first-class surface, not a hidden page.
- **Post-action: escalation pathway.** Defer to a person on low confidence
  or high stakes.

## Orchestration surface and post-action receipts

- The plan lives on screen with editable steps and a choice of approving
  the full sequence or each step; tool-use disclosure shows which external
  system was called and what it returned at the decision moment, not in a
  collapsed log.
- Memory corrections are surfaced visibly: "you changed the suggested time
  from 9am to 2pm — afternoons will be preferred for this contact going
  forward."
- After completion, issue a post-action receipt: what changed, which
  systems were touched, what assumptions were used, and what can still be
  undone.
- Scale the surface to the stakes: the full orchestration surface for
  multi-step, high-stakes tasks; lighter disclosure (a confidence signal
  only) for low-stakes single steps.

## Trust gradient and partial work

Graduate autonomy with evidence, and report partial results honestly:

- Start in preview mode: show the plan and confirm every action. Move to
  supervised mode — low-stakes steps run on their own, high-stakes steps
  still ask — only after repeated success; full autonomy comes last and
  is reversible.
- Rollback is a first-class feature: one-click undo for every reversible
  action, as fast and easy to reach as the original command.
- Partial completion shows per-step status: which steps succeeded, which
  failed, which were never attempted. Never present partial success as
  full success or as total failure.
- Long runs show richer progress than a spinner: the current step, what
  finished, and what is queued, with the pause control always reachable.
- Inline overrides let the person redirect mid-task — change a target or
  a constraint — without starting the run over.

## Show the track record before delegating

Before a person hands a kind of task to an agent, show how often "done"
was verified for that kind of task — measured from what actually
happened, not from the agent's own report of its work:

- Show the record at the moment of delegation, per kind of task, as
  counts: how many runs completed and were verified, and how many ended
  in an incident, a rejection, or a failure. A single overall score
  hides the difference — a good record at drafting says nothing about
  paying an invoice.
- Permissions are earned one kind of action at a time. A new agent
  starts read-only: every write asks first. After a run of clean runs —
  runs that completed with no incident traced to them — the person may
  widen what runs without asking. Only a person raises the level; the
  agent never raises its own trust.
- Irreversible actions always ask, whatever the record says: deleting
  data, spending money, or changing something that cannot be undone.
- When an incident is traced to an action a rule allowed, that rule goes
  back to asking, and the person is told what changed and why.
- Keep the record visible after delegation too: what ran without asking
  and how each run ended, so the record stays honest and the person can
  narrow it again at any time.

## Accessibility gate for generated interfaces

When an agent produces interface markup, require a release-day accessibility pass before shipping. Generators optimise for visual density and fail accessibility in predictable ways: missing names, divs used as buttons, shrunken targets, and focus hidden under sticky layers.

- Freeze the generated output first; do not keep regenerating while you measure.
- Run an automated scan first (contrast, missing names, invalid roles), then a manual pass: a keyboard-only walk of every primary journey plus screen-reader spot checks on icon buttons and dialogs.
- Apply the WCAG 2.2 additions as explicit checks: focus is never fully hidden by sticky or fixed layers, every drag gesture has a single-pointer alternative, icon buttons meet the 24 px target size, help is offered consistently, users are never asked to re-enter the same information, and authentication never depends on memory or transcription alone.
- Prefer native elements over patched-up roles: replace clickable divs with buttons or links, give every icon button a real name, and treat every generated ARIA attribute as a claim to verify.
- Record what the scanner cannot see as residual risk with an owner and a follow-up date; a clean scanner score is not proof of conformance.
- Re-run the same checklist every time the interface is regenerated — accessibility debt in generated UI is a loop, not a one-time project.

## Agent-described screens

An agent can answer with a screen instead of text: a form to confirm, a chart, a choice between options. The agent describes the screen; the app draws it with its own native components.

- The agent sends a structured description of the surface — its components, text, and values — and the app renders it, so the result keeps the app's look, behaviour, and accessibility support instead of inheriting whatever the agent would have drawn.
- The agent may only place components the app has registered in advance. Anything outside that catalogue is refused, never rendered as a fallback.
- Values that must stay private are bound on the server, so they reach the screen without passing through the agent's description.
- A screen that needs live facts — availability, prices, open slots — checks them on the spot through a two-way call before it is shown, instead of showing figures that may already be stale.
- Stream the screen in as the work progresses, but keep its layout stable: reserve space for each part so nothing shifts when the next part arrives.
- The same rules as any other agent surface apply: a composed block is labelled as composed, a consequential action waits at a checkpoint, and the accessibility gate in the section above runs before the screen ships.
- The A2UI protocol is one open implementation of this pattern; its first stable version shipped in November 2026, with renderers for the web, mobile, and desktop.

## Site-registered agent tools

A page can register named tools that an agent running in the browser can discover and call, instead of the agent guessing which control to press. Treat this as a draft capability, not a settled pattern: the proposal lives as a community-group draft, not a standard, and is not on the standards track. One browser runs a public trial from version 149 to 162; a second browser has trialled it since version 150; other browsers have not committed to it.

- Register a tool from script, on the document object, with a name, a plain-language description, and an input schema; the tools belong to the page that registers them, and a page can restrict registration to its own origin.
- The entry point moved from the navigator object to the document object in mid-2026, and one browser removed the old entry point in version 152, so code written for the early preview registers nothing on current builds; detect both entry points and prefer the document form.
- The form-based declarative form was dropped from the draft in October 2026, so script registration is the only form the draft defines.
- Where the entry point is absent, the page behaves as if the proposal never existed: no error, no dead control, and no change to the task the person came to do.
- Register only tools that are safe to call without a person present. Anything irreversible, costly, or privacy-sensitive waits at a checkpoint, under the trust patterns above, and appears in the step trace and the post-action receipt.
- Keep each tool description short, plain, and honest about what the tool does and what it needs; a tool that claims more than it does will be called for the wrong job.
- Some storefront platforms switch the tools on by default for their stores, and a desktop chat application also reads the registered tools — the page still owns what it exposes, and nothing about the listing changes for people who never use an agent.

## Server-supplied interfaces in the conversation

A connected server can answer a tool call with an interactive interface — a form, a chart, a table, a dashboard — that the host renders inside the conversation, instead of plain text. The server supplies the interface as a document; the host renders it in a sandboxed frame and mediates every message between the interface and the host. The open protocol extension that defines this is MCP Apps; its stable version shipped in January 2026.

- Treat the supplied interface as untrusted content from the connected server, not as host interface: it runs in a sandbox with a deny-by-default content policy, and it reaches tools, resources, and the conversation only through the host-controlled channel.
- Label the surface with its origin — which connected server supplied it — so a person can tell host controls from server-supplied controls at a glance.
- Keep the tool useful where the host cannot render the interface: the same tool returns a plain result that works on its own, and the interface is an enhancement, never the only way to complete the task.
- A consequential action taken inside the supplied interface waits at a checkpoint, under the trust patterns above, and appears in the step trace and the post-action receipt, exactly as if it had been taken in the host interface.
- Anything the interface writes back into the conversation — a message, a value, a change to what the agent carries forward — is shown to the person as coming from that server, and is recorded in the step trace.
- Distinct from agent-described screens above, where the agent describes the surface and the app draws it with its own native components: here the server draws the surface itself, and the host only contains it.

## States

Every screen in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | Briefing panel with the request, scope, and constraints stated; agent idle. | Ready to receive a brief; scope is visible before work begins. |
| Hover | Pointer-only highlight on controls and step list items. | No change on touch devices; hover never carries essential information alone. |
| Active | Agent working; current step marked, progress by step, pause control visible in the same view. | Feedback appears within 100 ms of input; the stop control never moves away. |
| Disabled | Agent cannot run — missing permission or scope — with the reason stated and the fix named. | Explain why it is unavailable nearby and offer the path to enable it. |
| Loading | Awaiting the first step; skeleton of the planned steps in place. | Keep layout dimensions stable so content does not shift when the plan arrives. |
| Empty | No tasks yet; one example brief shown with a single clear start action. | Offer one next action and a way to dismiss the example. |
| Error | A failed step states what failed, what was rolled back, and offers retry from that step or manual completion. | Keep the entered brief, place the message next to the failed step, and never lose completed steps. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Trust patterns and the orchestration-surface rules are documented.
- [ ] Inline assistant actions link to the pattern in catalog/patterns.md.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
