# Primitives

The smallest reusable building blocks. A primitive has one job, a stable anatomy, and defined variants and states that composite patterns inherit.

## Classification

- Category: primitives

When to use:

- Building or reviewing any screen; primitives are the shared vocabulary.
- Auditing consistency across screens that were built at different times.

When to avoid:

- Creating a new primitive when an existing one can be extended with a variant.

## Elements and components

| Primitive | Anatomy | Variants | Rules |
| --- | --- | --- | --- |
| Button | Label, optional leading shape, focus ring | Primary, secondary, quiet, destructive; small, medium, large | One primary action per view; verb-first labels |
| Text input | Label, field, helper text, error text | Single line, multi-line, search, numeric | Label is always visible; placeholder is not a label |
| Select | Trigger, list, option, check mark | Single, multiple, searchable | Keep the list within the viewport; type-ahead for long lists |
| Checkbox | Box, label | Checked, unchecked, indeterminate | Use for independent options; apply on submit or explicitly |
| Radio group | Option list, selected ring | Vertical, horizontal | One selection; always has a default or an explicit none |
| Switch | Track, thumb, label | On, off | Applies immediately; label states the setting, not the action |
| Slider | Track, thumb, value label | Continuous, stepped | Pair with a numeric input for precise values |
| Badge | Short text, dot or count | Neutral, accent, warning, critical | Counts above a cap show the cap, for example 99+ |
| Tag | Label, optional remove control | Removable, selectable | Removable tags are reachable by keyboard |
| Tag input | Field containing chips; remove control per chip; text entry at the end | Free-form tags, recipient lists, keyword filters | Each chip is reachable and removable by keyboard; enter or a delimiter commits a chip; pasting a list splits it into chips; duplicates are rejected with a short note |
| Inline copy | Compact value text with an inline copy button | Identifiers, keys, values in dense rows | Copy shows a confirmation within 100 ms; the full value stays reachable to screen readers; the button is at least 24 px; never truncate the value without a way to reveal it |
| Layer dialog | Title, body, actions, close control | Centred dialog on wide screens, bottom drawer on narrow screens | Focus is trapped and returned to the trigger; escape closes it; scrim dismissal is optional and announced; the drawer variant keeps actions within thumb reach |
| Tooltip | Short text, pointer | Top, bottom, left, right | Supplementary only; never the sole source of essential information |
| Dialog | Title, body, actions, close control | Confirm, form, full-screen on compact | Traps focus, returns focus to the trigger, closes on escape where safe |
| Sheet | Trigger wrapper, content surface, optional header, body, footer, close parts | Slide-in from left, right, top, or bottom edge; inline panel | One overlay family covers drawers and modals; the trigger wrapper manages the interaction, a control opens it, and the component renders the content; choose the opening edge by position; compose with header, body, footer, and close parts; do not nest sheets |
| Toast | Short message, optional action | Neutral, success, warning, error | Auto-dismiss except errors; action allows undo where possible |
| Progress | Bar or ring, label | Determinate, indeterminate | Label states what is loading or progressing |
| Skeleton | Abstract blocks matching final layout | Text line, card, list row | Same dimensions as final content to prevent layout shift |
| Step trace | Line list; each line has icon, title, optional description, status | Expandable, nested, linking | One line per step of an automated task; running, error, and pending states stay visible; expand in place rather than navigating away; operable by keyboard and screen reader |
| Code block | Header with title and actions, line numbers, content body | Code, terminal output, log, diff; compact | Line numbers aid reference; wrap or scroll long lines without clipping; diff highlights stay text-readable |
| Leaderboard | Ranked entries; each entry has a start slot, a middle slot, and an end slot | Top-N lists, scores, rankings; compact and full | One entry per ranked item; keep the ranking signal (position, score, delta) separate from the identity in the middle; sort by the same key the rank claims; never reorder without re-ranking |
| Form builder | Field palette, drag canvas, field settings panel, live preview | Inline builder, wizard-step builder | The palette shows only fields the runtime can render; settings sit beside the selected field; always offer a preview before saving; provide a keyboard path for adding and reordering fields |
| Media effect | Real element kept in the DOM (visually hidden), mirrored plane on one shared full-page canvas, effect material fed by the element's texture and the live pointer | Cursor ripple, pixel blocks, lens dispersion; images and video | One shared canvas for every effect on the page; never one render context per element. The DOM element stays the source of truth for assistive technology and indexing; the effect is decorative only. Each element opts out of global effects explicitly. Disabled when reduced motion is preferred. Sync position on scroll and resize; remeasure per frame only while a transform moves the element |
| Markdown block | Rendered content surface: headings, paragraphs, lists, tables, images, links, code blocks | Read-only, editable source | Follows a standard Markdown specification; sanitise untrusted source input; images scale to the container; tables stay readable on narrow widths |
| Citation card | Source label, excerpt, open-source link, optional page or timestamp reference | Inline with text, stacked list, expandable panel | One card per source; the excerpt matches what the source says — never invent a quote; the link opens the cited passage; evidence sits beside the claim it supports, not in a separate tab; long excerpts collapse behind an expand control |

## Layout and responsive rules

- Keep a 4 px spacing scale: 4, 8, 12, 16, 24, 32, 48.
- Minimum touch target: 44 px. Minimum pointer target: 24 px with clear spacing.
- Focus ring is always visible on keyboard focus and never removed without a replacement.
- Text scales to 200% without loss of content or function.
- Colour is never the only signal; pair it with text, shape, or position.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A primitive at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Not applicable to most primitives; containers using a primitive show an empty message with one next action. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Error text sits next to the primitive, names the problem, and keeps the entered value. | Keep entered data, place the message next to the problem, and offer a retry. |

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
