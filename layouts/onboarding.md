# Onboarding Layout

A first-use sequence that gets a person to their first meaningful
success as fast as possible, then gets out of the way.

## Classification

- Category: layouts / onboarding

When to use:

- First-run experience, new-feature introduction, or account setup where
  the person must configure something before value appears.

When to avoid:

- As a tour of every feature, or as a gate in front of value — defer
  sign-in and configuration wherever the product can deliver value
  without them.

## Elements and components

Step indicator, one task per step, skip action, progress persistence,
smart defaults, sample or template content, a success marker for the
first completed action, and a measurable activation event.

## Layout and responsive rules

- Lead with the success action: identify the one task that delivers
  the first value and design the sequence to push the person toward
  completing it.
- Cut the welcome modal: a greeting screen that only says hello is a
  tax on attention. Replace it with the first real action, or remove
  it.
- One question at a time; no more than three input fields in a single
  step. Anything beyond that defers to settings.
- Defer authentication where possible: let the person experience value
  before sign-in when the product allows it.
- Skip-and-return: skipping is always allowed and resumes later.
  Progress persists across interruptions and devices, and a returning
  person lands exactly where they left off.
- Smart defaults and prefill: prefill with the most likely value from
  location, common choice, or past behaviour; detect and prefill
  language and region with a one-tap correction affordance; use
  standard autocomplete tokens so saved values can fill in; every
  default stays editable and skips validation until the person changes
  it; never set defaults for decisions needing deliberation, such as
  consent or legal acceptance; explain why each field is asked.
- Sample data over blank slates: pre-filled templates or example
  content the person can react to, keep, or delete beat an empty page
  every time.
- Progressive disclosure with intent: hide complexity that depends on
  context; surface complexity the person is asking for. Show one path
  on day one and reveal the rest after the person has done something.
- Mechanism-agnostic: checklists, contextual tips, guided actions, or
  a prefilled workspace all work — choose whichever the audience
  responds to. A checklist works when its items map to outcome events,
  not when it is a feature tour in disguise; in-app tips work when
  they appear next to the next action, not as a wall of hints on
  sign-up.
- Make activation measurable: define the activation event so it can be
  counted, and instrument completion, time to first value, and
  drop-off per step.
- Compact screens: keep the primary action in thumb reach, allow
  swipe or tap progression, prefer vertical scrolling, and keep the
  flow light for slow connections.

## States

Full state definitions live in `../catalog/states.md`. The onboarding
layout's additions are below.

| State | Onboarding-specific note |
| --- | --- |
| Default | One task visible; the next step and the skip affordance are both clear. |
| Hover | Pointer-only highlight on step actions; no information carried by hover alone. |
| Active | The pressed step shows feedback within 100 ms; progress indicator advances on completion, not on press. |
| Disabled | A step blocked by a missing prerequisite explains what is missing and links to it. |
| Loading | Skeleton blocks hold the step layout; never gate progress on content that can load lazily. |
| Empty | Before setup starts, the sequence offers the prefilled path; after completion, it resolves to the product home with a resume link for skipped steps. |
| Error | Keep entered data, explain the failure next to the field or step, and offer retry without losing progress. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The sequence names a success action, a measurable activation event, and the skip-and-return rule.
- [ ] Smart-default and prefill rules match `../catalog/patterns.md`.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
