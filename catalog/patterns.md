# Patterns

Composite patterns assembled from primitives. Each pattern solves a recurring task and inherits the state rules of its parts.

## Classification

- Category: patterns

When to use:

- Composing a screen for a recurring task such as finding, filtering, or editing information.
- Checking a flow for missing steps, exits, or recovery paths.

When to avoid:

- Inventing a one-off arrangement for a task a pattern already covers.

## Elements and components

| Pattern | Purpose | Core elements | Rules |
| --- | --- | --- | --- |
| Primary navigation | Move between top-level sections | Nav list, current indicator, badge | Current section is marked in text or shape, not colour alone |
| Search | Find content by query | Search input, suggestions, results list, clear action | Show recent and suggested queries only where appropriate; results state the query |
| Filtering and sorting | Narrow a list | Filter controls, active filter tags, sort menu, result count | Result count updates with filters; one action clears all filters |
| Data table | Compare structured rows | Header row, sort controls, pagination or load-more, row actions | Sticky header on long tables; density is a user choice where feasible; bulk selection uses a selection column with a select-all that states its scope; keep loading state per section (grouped headers, expanded rows) rather than whole-table only, and keep expanded-row content aligned with the visible viewport during horizontal scroll; cell-level actions combine one link with one or two adjacent button or link actions |
| Data table density | Fit more rows without losing legibility | Compact, comfortable, and spacious density options; sticky column headers | Density is a per-user choice stored with preferences; row height never drops below the minimum target size |
| Bulk selection | Act on many rows at once | Selection checkboxes, selection count, action bar with the available actions | Selection survives sorting and paging; actions apply to the stated scope and confirm before destructive ones |
| Onboarding | Teach the essential path on first use | Step indicator, one task per step, skip action, progress persistence | Steps focus on what the person must do, not on features; skipping is always allowed and returns later; progress resumes after interruption; detect and prefill language and region with a one-tap correction affordance; never pre-select sensitive fields, and question whether they are needed at all; prefill with the most likely value from location, common choice, or past behaviour; every default stays editable and skips validation until the person changes it; use standard autocomplete tokens so saved values can fill; never set defaults for decisions needing deliberation such as consent or legal acceptance; explain why each field is asked; show one question at a time |
| Inline assistant actions | Apply automated help to the thing already selected | Contextual command on a selection or row, scope statement, inline preview, undo | Commands appear as verbs on the existing surface — selection menus, row actions, inline toolbars — not as a separate chat surface; inline wins when the target is visible, the task is short, and the result lands where the person already is, while chat wins for open-ended or multi-step exploration; every command states its scope before acting and is reversible, graded by consequence: trivial changes apply with a plain undo, costly ones preview the effect and wait for approval; capabilities are discovered in place, as a suggestion on the selection itself, never through a tour; loading names the running step and error keeps the selection intact |
| Form flow | Collect structured input | Grouped fields, inline validation, summary of errors, submit | Validate on submit and on correction; errors are listed and linked to fields |
| Wizard | Complete a multi-step task | Step indicator, back and next, save and resume | Steps can be revisited; progress is preserved on interruption |
| Detail view | Inspect one item | Title, key facts, actions, related items | Primary action stays reachable while scrolling on compact screens |
| Notification list | Review updates | Grouped items, read state, mark-all action | Unread state uses shape or text in addition to colour |
| Confirmation | Prevent a costly mistake | Plain statement of effect, confirm and cancel actions | Destructive actions name the item and the effect; no pre-selected confirm; grade every action by reversibility: free actions (read-only or trivially reversible) need no interruption, reversible writes get a lightweight inline check with a before-and-after statement, and irreversible actions (pay, send, delete, publish) get the full confirmation ceremony; support standing permissions such as "always draft, never send"; never gate trivial actions or confirmations stop being read |
| Comparison | Choose between options | Option columns or tier cards, criterion rows in a fixed order, difference toggle, decision row | Fix the criterion order across options so rows line up; three to four columns is the workable range; label tiers by audience in plain words, not abstract names; each higher tier opens with "everything in the previous tier, plus…" so readers scan only what is new; a differences-only toggle hides identical rows; mark each row's winner gently with shading plus a text or icon cue, never colour alone; do the arithmetic for the reader ("+$40/month buys 3 extra seats and single sign-on"); state the metric direction explicitly where ambiguous ("lower is better"); keep option labels and a decision row with one action per option sticky on long matrices; spell out annual savings next to the billing toggle; choose the container by difference count — cards when only a few real differences separate the options, tabs or accordions or a grouped collapsible matrix when the feature list is long |
| Permission request | Earn access without losing trust | Pre-permission rationale screen, system dialog, graceful denial path, settings route | Never request on first launch just in case; trigger when the person taps the feature that needs the access; stage one is a custom pre-permission screen stating the concrete value ("to scan receipts and auto-categorise expenses"); if the person taps "not now", do not fire the system dialog; stage two is the system dialog only after a positive pre-prompt response; request one permission at a time — batched prompts produce combined denials; on denial, degrade gracefully into a feature-limited experience, never a dead end; for permanent denial, explain the limitations plainly and route to the app settings; ask once, then only in context; never nag within the same session after a denial; consider a single in-app screen listing all requested permissions with one-tap revocation |
| Search results | Recover from finding nothing | Query echo, carried filter chips, ordered recovery actions, facet panel | Keep the division of labour simple: search narrows by intent, filters narrow by attribute; the two controls sit close together since people loop between them; on empty results, say the combination matched nothing and echo it exactly ("no invoices match X with Status: Paid"), keep the query and filters visible, and never silently clear choices; offer recovery in order: a clickable spelling suggestion rather than silent autocorrect, a one-action scope broadening, carried filters as removable chips (an old filter is the most common hidden cause), and a create action where user content is accepted; label each widening action by what it changes; mirror applied filters as chips next to the query echo; a single reset clears filters but leaves the query intact; facet panels sit left on expanded screens and in a bottom sheet on compact ones, with live result counts per facet |
| Paywall and upgrade prompt | Explain a limit and an option | Limit statement, option summary, dismiss action | Dismiss is always present and equally easy to find |
| Consent choice | Record a preference | Plain description, accept and decline, link to detail | Decline is as prominent as accept; choice is changeable later |
| Media viewer | Inspect visual content | Stage, previous and next, caption, close | Keyboard and swipe both work; captions are text, not embedded in the visual |
| Simplified view | Reduce cognitive load on demand | Simplified-mode toggle, reading view, critical-region markers | Offer a simplified version that hides non-essential features and shortens text; keep it available, easy to enter, and easy to leave; mark content on critical paths for simplification (data-simplification attribute) so personalization tools can reduce it; extra features stay discoverable when wanted, never permanently removed |

## Layout and responsive rules

- One pattern owns the primary action of a screen; supporting patterns stay visually quieter.
- On compact screens, patterns stack in task order: search, filters, results, actions.
- On expanded screens, filters may sit beside results; the result count stays with the results.
- Keep the path back: every pattern that opens a detail or a step offers a clear return.
- Do not nest dialogs; use a new view when a second layer of decisions appears.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A pattern at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | State why the area is empty and offer the action that fills it, or a reset when filters cause it. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep the pattern's structure, show the failure in place, and offer retry without losing input. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Every pattern names its purpose, anatomy, and practical rules.
- [ ] Permission-request, comparison, search-results, and onboarding rows reflect the latest rules.
- [ ] Cross-links to catalog/states.md resolve.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
