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
| Permission-denied | The blocked area explains which access is missing and why it is needed. | Offer a retry after granting, or an alternative path that works without the permission; never show a dead end. |

## Layout and responsive rules

- State changes never move surrounding content; reserve space in the layout.
- Loading longer than about 10 seconds needs a progress statement or a cancel action.
- Long operations name their steps, for example "Searching your documents", instead of a generic spinner.
- Optimistic updates apply the change at once and revert quietly on failure, with a clear undo path.
- Empty and error states keep the page structure: navigation, title, and search stay in place.
- On touch devices there is no hover; every hover affordance has a tap equivalent.
- In a scrollable composite control such as a carousel, activating a scroll button returns focus to that button once scrolling completes, and paging never moves keyboard focus outside the control.
- Reduced-motion settings replace animated indicators with static ones.

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

## Copy rules for states

- Loading: state what is being prepared, for example "Loading results".
- Empty: state the cause when known, for example "No results for this filter".
- Error: state the problem and the next step, for example "Results could not
  be loaded. Check the connection and try again."
- Disabled: where the reason is not obvious, place it in helper text beside
  the element, not only in a tooltip.

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
