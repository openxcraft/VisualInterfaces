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

## Accessibility gate for generated interfaces

When an agent produces interface markup, require a release-day accessibility pass before shipping. Generators optimise for visual density and fail accessibility in predictable ways: missing names, divs used as buttons, shrunken targets, and focus hidden under sticky layers.

- Freeze the generated output first; do not keep regenerating while you measure.
- Run an automated scan first (contrast, missing names, invalid roles), then a manual pass: a keyboard-only walk of every primary journey plus screen-reader spot checks on icon buttons and dialogs.
- Apply the WCAG 2.2 additions as explicit checks: focus is never fully hidden by sticky or fixed layers, every drag gesture has a single-pointer alternative, icon buttons meet the 24 px target size, help is offered consistently, users are never asked to re-enter the same information, and authentication never depends on memory or transcription alone.
- Prefer native elements over patched-up roles: replace clickable divs with buttons or links, give every icon button a real name, and treat every generated ARIA attribute as a claim to verify.
- Record what the scanner cannot see as residual risk with an owner and a follow-up date; a clean scanner score is not proof of conformance.
- Re-run the same checklist every time the interface is regenerated — accessibility debt in generated UI is a loop, not a one-time project.

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
