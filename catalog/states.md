# States

A shared definition of the seven states every element and page must specify. A state is complete only when appearance, behaviour, and recovery are all defined.

## Classification

- Category: states

When to use:

- Specifying any element, pattern, or page.
- Reviewing work before release; missing states are the most common defect.

When to avoid:

- Treating a state as decoration; each state changes behaviour, not only colour.

## Elements and components

| State | Trigger | Must define |
| --- | --- | --- |
| Default | No interaction yet | Resting appearance, label, and affordance |
| Hover | Pointer rests on the element | Pointer-only feedback; no essential information revealed only here |
| Active | Press, tap, or selection in progress | Immediate feedback and the result of completing the action |
| Disabled | Action unavailable | Reason, where it is explained, and how it becomes available |
| Loading | Data or action in progress | Indicator type, expected layout, timeout and failure path |
| Empty | No content to show | Reason, illustration-free explanation, and one next action |
| Error | Action or load failed | What failed, what is preserved, and the retry or exit path |

Supporting states worth defining where relevant: focused, selected, expanded,
read-only, offline, and permission-denied. They extend this scheme; they do
not replace any of the seven above.

| Supporting state | Appearance | Behaviour and recovery |
| --- | --- | --- |
| Offline | A persistent banner or badge states that the connection is lost; the layout does not rearrange. | Cached content stays usable; actions that need the network queue visibly and sync when the connection returns; nothing silently fails. |
| Read-only | Controls are replaced or dimmed with a short reason, for example "View only". | Data is fully legible; the reason for read-only is stated once; the path to request access sits next to it. |
| Permission-denied | The blocked area explains which access is missing, why it is needed, and who can grant it. | Offer a retry after granting, or an alternative path that works without the permission; never show a dead end. For the flow that earns the permission in the first place, see the permission-request pattern in `catalog/patterns.md`. |
| Focused | A visible indicator marks the focused element — an outline, a background shift, or both — distinct from hover and selection. | Never remove the platform default without a designed replacement that stays visible in every theme; closing a dialog returns focus to the control that opened it; scrolling keeps the focused control clear of fixed chrome. |
| Selected | Selection is marked in text or shape as well as colour: a check, a label, or a persistent highlight. | State the selection count where multiple selection is possible; selection survives sorting, filtering, and paging; a clear-all action is always reachable. |
| Expanded | Disclosed content appears directly below or beside the trigger; the trigger label names the state, for example "Show more" and "Show less". | Expanded content holds its place when the layout reflows; collapsing returns focus to the trigger; the expanded region keeps its heading level in the page outline. |
| Warning | A caution presentation distinct from error: it signals a consequence to consider, not a failure that happened. | State the consequence in plain words before the irreversible step; require an explicit confirm action; never pre-check the confirmation or auto-advance past it. |

## Layout and responsive rules

- State changes never move surrounding content; reserve space in the layout.
- Loading longer than about 10 seconds needs a progress statement or a cancel action.
- Long operations name their steps, for example "Searching your documents", instead of a generic spinner.
- Optimistic updates apply the change at once and revert quietly on failure, with a clear undo path.
- Empty and error states keep the page structure: navigation, title, and search stay in place.
- On touch devices there is no hover; every hover affordance has a tap equivalent.
- In a scrollable composite control such as a carousel, activating a scroll button returns focus to that button once scrolling completes, and paging never moves keyboard focus outside the control.
- Group an action's visual states in one component: one component owns the
  idle, loading, and success presentations and moves between them, instead
  of scattering state logic across icons, labels, and handlers. Each
  transition announces itself to assistive technology, dimensions stay
  fixed while loading, and focus returns to the action once its success
  presentation clears.
- Reduced-motion settings replace animated indicators with static ones.
- Keyboard focus is never hidden behind page chrome: sticky headers,
  consent controls, chat launchers, and banners must not cover the focused
  control. When scrolling brings a control into focus, it lands fully clear
  of any fixed overlay.
- Focus indicators carry at least 3:1 contrast against adjacent colours;
  never suppress the platform default without a designed replacement that
  stays visible and themeable.
- In forced-colours mode the author palette is replaced by user colours,
  so the indicator rides on an outline in system colours rather than a
  shadow, which gets suppressed.
- Set scroll padding on the root element to match fixed chrome, so a
  focused control is never entirely hidden behind a sticky header, banner,
  or launcher when it scrolls into view.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | Any element at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Explain the absence in one short sentence and offer one action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Name the failure in plain language, preserve input, and place retry next to the message. | Keep entered data, place the message next to the problem, and offer a retry. |

## Error-state groups

Group error presentations by what the person can do next, not by the
failure's cause.

- Input rejected: an inline message at the field, other values kept, and
  focus moved to the first error.
- Session or permission lost: re-authenticate in place and resend, so the
  work survives; explain who can grant the access when permission is the
  blocker.
- Conflict or gone: show both versions, or say plainly where to go
  instead.
- Rate-limited or overloaded: show the wait, count it down, and retry
  automatically.
- Server error: retry once, then show a reference identifier.
- Unknown outcome: the request timed out and the result is unconfirmed — treat it as unknown, not failed. Preserve all entered values, verify whether the action already succeeded before enabling retry, and show a distinct checking status ("checking whether your save went through") so a retry can never create a duplicate.
- Offline or timeout: keep the action visibly queued, say it will be sent
  when the connection returns, and never present it as saved until the
  save is confirmed.

## Copy rules for states

- Loading: state what is being prepared, for example "Loading results".
- Empty: state the cause when known, for example "No results for this filter".
- Error: state the problem and the next step, for example "Results could not
  be loaded. Check the connection and try again."
- Disabled: where the reason is not obvious, place it in helper text beside
  the element, not only in a tooltip.

## Loading-state rules

A skeleton previews the shape of arriving content; it is not decoration.
Pick the indicator from the wait, not the layout.

- Reserve skeletons for waits of roughly 1 to 10 seconds. Under 1 second
  show nothing — a flickering skeleton reads as noise. Past 10 seconds
  switch to a percent-done indicator.
- Match the final layout box for box. When the post-loading layout cannot
  be predicted, use a spinner instead to avoid layout whiplash.
- Replace each placeholder the instant its content arrives; never hold
  finished content hostage to the slowest element on the page.
- Never show an empty state during a fetch — users read "no data" as
  final. Zero results after loading completes is an empty state; a
  failure is an error state with retry. Never leave the skeleton visible
  after an error.
- Skeleton shape communicates loading without motion. Ship a static
  reduced-motion variant, keep skeleton fills at readable contrast, and
  announce loading status to assistive technology: mark loading regions
  busy and announce with a polite live region when content replaces the
  skeleton.

## Empty-state variants

Four kinds of "empty" need different words and different next steps. Do
not infer the state from an item count; the data layer returns an explicit
status alongside the items.

- First-use. Nothing has been created yet. Goal: teach and start. Copy
  states the situation and the one action that begins, for example "No
  projects yet. Create your first project."
- Naturally empty. The user is caught up, cleared the list, or nothing is
  scheduled right now. Goal: confirm, not alarm. Say so plainly and, when
  known, say when to come back, for example "You are all caught up. New
  items appear here as they arrive."
- Restricted or failed. Content exists but cannot be shown, or loading
  failed. Goal: explain and recover. Name the cause honestly and give the
  matching next step: a permission request for restricted content, a retry
  for a failure. Never show a blank area that reads as broken. A
  restricted message never implies a workaround where none exists — a
  retry or a request path that can never succeed reads as broken too.
- Pre-populated. The area is technically empty, but available context
  suggests what the user is likely to want. Goal: offer a starting point
  instead of a blank screen. Show suggestions as suggestions — visually
  distinct from real items, easy to dismiss, and never stored as the user's
  data. Never present suggested content as if it already existed; a user
  must be able to tell suggestion from fact at a glance. A worked example —
  a pre-filled sample clearly marked as an example, with one action to make
  it real — teaches the shape of the result before the user commits; where a
  sample is impossible, show a faded preview of the populated state behind
  the call to action.

Rules:

- One short sentence of explanation, then one clear action; a second link
  (help, settings) is allowed but never a second action of equal weight.
- A load failure never reuses the genuinely-empty message: "nothing
  here" and "nothing loaded" are different states with different words,
  and the failure message names the failure. The same visual treatment
  must not appear in both cases, since the person cannot tell them apart.
- Keep the visual treatment calm: no error styling for first-use or
  natural empty states; error styling only for failures.
- Keep layout dimensions stable so the populated view does not shift.

## Theme preference states

Appearance mode (light, dark, automatic) is a persistent state, not a
one-time read. Resolve it carefully at every load.

- In automatic mode, re-read the live system preference on every page
  load. Never store the resolved value as if the user had chosen it —
  a frozen snapshot stops tracking the system setting.
- The configured theme is authoritative over stored leftovers. A value
  from an older version, another app on the same host, or a stale cookie
  must not override the theme the app declares; ignore or repair foreign
  and outdated values instead of applying them.
- Keep the visible label, the stored value, and the applied theme in
  agreement before the first paint, so the page never flashes the wrong
  mode while the preference resolves.

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The seven-state table and the supporting-state table are complete and consistent.
- [ ] Loading-state, empty-state, and error-state-group sections agree on wording.
- [ ] Copy-rule examples read naturally in one line each.
