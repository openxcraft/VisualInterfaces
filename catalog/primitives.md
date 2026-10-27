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
| Button group | Shared container holding related buttons in one connected shape | Segmented single-select, grouped actions; horizontal, vertical | Group only related actions; one selection state visible and announced; adjacent buttons share a container edge rather than repeating borders; shape changes stay subtle enough that every target stays identifiable; under reduced motion use a simple cross-fade instead of spring or morph motion |
| Text input | Label, field, helper text, error text | Single line, multi-line, search, numeric | Label is always visible; placeholder is not a label |
| Select | Trigger, list, option, check mark | Single, multiple, searchable | Keep the list within the viewport; type-ahead for long lists |
| Checkbox | Box, label | Checked, unchecked, indeterminate | Use for independent options; apply on submit or explicitly |
| Radio group | Option list, selected ring | Vertical, horizontal | One selection; always has a default or an explicit none |
| Switch | Track, thumb, label | On, off | Applies immediately; label states the setting, not the action; keep the switch beside its label, never at the far edge of a wide row — on wide desktop columns place the switch immediately beside the label so label and control stay visible together under magnification, and on narrow columns keep the label on the left with the switch on the right so the pair stays together; never use a switch for an action that needs confirmation or cannot be undone, since a switch applies at once and offers no confirmation step |
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
| Form builder | Field palette, drag canvas, field settings panel, live preview | Inline builder, wizard-step builder | The palette shows only fields the runtime can render; settings sit beside the selected field; always offer a preview before saving; provide a keyboard path for adding and reordering fields; give every field per-part keyboard coverage, and require an explicit confirmation step for high-stakes popovers such as date entry in scheduling or financial contexts |
| Media effect | Real element kept in the DOM (visually hidden), mirrored plane on one shared full-page canvas, effect material fed by the element's texture and the live pointer | Cursor ripple, pixel blocks, lens dispersion; images and video | One shared canvas for every effect on the page; never one render context per element. The DOM element stays the source of truth for assistive technology and indexing; the effect is decorative only. Each element opts out of global effects explicitly. Disabled when reduced motion is preferred. Sync position on scroll and resize; remeasure per frame only while a transform moves the element |
| Headless behaviour primitive | Behaviour only, no visual styling: focus management, keyboard map, roles and states, portal, collision-aware positioning | Dialog, menu, popover, combobox, tooltip behaviour layers | List the behavioural guarantees (focus trap, keyboard map, state values) separately from visual styling — that is the durable half; unstyled elements carry state attributes so any visual system can bind to them; merge behaviour onto any element without wrapper markup; choose a headless behaviour layer when building a bespoke visual system, a full kit when speed beats distinctiveness |
| Markdown block | Rendered content surface: headings, paragraphs, lists, tables, images, links, code blocks | Read-only, editable source | Follows a standard Markdown specification; sanitise untrusted source input; images scale to the container; tables stay readable on narrow widths |
| Citation card | Source label, excerpt, open-source link, optional page or timestamp reference | Inline with text, stacked list, expandable panel | One card per source; the excerpt matches what the source says — never invent a quote; the link opens the cited passage; evidence sits beside the claim it supports, not in a separate tab; long excerpts collapse behind an expand control |
| Shape | Geometry definition: path coordinates, border geometry, corner treatment | Path-based coordinates, border geometry for non-rectangular outlines, corner presets (bevel, notch, scoop, squircle) | Geometry is decorative: the shape never changes the hit target, reading order, or focus order; corners stay consistent — use a system corner preset instead of hand-drawn paths when one exists; always ship a rectangular fallback for platforms without native shape support, layered as progressive enhancement so the layout never breaks |
| Date picker | Choose a calendar date or range | Typed field, calendar grid, month and year controls, presets, clear action | Choose the lightest control for the intent: a typed field for known dates, a picker when surrounding context helps the choice, a full calendar surface only for event management; each intent — single date, date-and-time, linked range, relative or recurring expression — gets its own control, never one shared control. Typed entry is a first-class path: forgiving parsing, a visible format hint, validation after input rather than during typing. Day-cell states are mutually distinguishable without colour alone: default, hover, focus, today, selected, in-range, disabled — and a disabled day hints at why, since a blocked day with no explanation reads as a bug. Ranges are their own pattern, not two single pickers: shade the span with distinct endpoint treatment, preview on hover mid-selection, guard against reversed ranges, and commit explicitly so half-finished selections never leak into the query; the closed field always shows both ends in a clear format. Unavailable dates appear as disabled states in the calendar, explained in place, not surfaced only as post-submit errors. Any time value states its timezone unambiguously and makes cross-timezone and all-day cases explicit. Presets — today, last 7 or 30 days, this month, this quarter — put the common intents one tap away and stay relative rather than freezing to absolute dates. Keyboard contract: focus moves into the grid on open and returns to the trigger on close; arrow keys move by day, page keys by month; every day cell carries a full accessible name. On mobile the native picker usually wins unless ranges or presets are required |
| Media controls | Transport bar: play/pause toggle, seek control, time readout, volume, captions toggle, speed, settings entry | Embedded inline, full player, audio-only | Ship the expected set in one reading order — play/pause, seek, time, volume, captions, speed, settings — and no control that does nothing; every control confirms it responded within 100 ms, through a pressed state, a value change, or a scrub preview. Full keyboard operation with named controls; captions stay available whenever the media carries dialogue and default to off; never auto-play with sound — playback starts on an explicit gesture or muted. Volume remembers the last setting but never reopens at full on a new page; the bar keeps a consistent order across contexts so muscle memory survives |
| Haptic feedback | Vibration pattern with three intensities and durations: confirm (short, light), alert (two taps, medium), error (long, firm) | Inline confirmations, error states, navigation cues | Map intensity to meaning and keep it consistent: light confirms, medium alerts, firm signals an error. Haptics never carry meaning alone — pair every pattern with a visual or spoken signal, since not all devices vibrate. Offer a clear user control to disable haptics, and honour reduced-motion and system accessibility settings by default. No haptic loops or continuous vibration; cap repeated patterns and stop them on navigation |
| Kinetic type | Text whose variable-font axes (weight, width, slant) or motion respond to scroll, interaction, or state | Interaction-reactive, ambient or looping, state-signalling, adaptive to environment | Motion is punctuation, not prose: use it for headlines and moments, keep body copy and core controls static. Ship on a complete static design so the text reads fully with motion disabled; honour reduced-motion settings by switching to static type. Screen readers announce whole words, never letter by letter. Animate transform and opacity only, so motion stays smooth on modest devices. Looping motion always offers a pause or stop control; never force continuous motion on the reader |
| Multimodal input bar | Text field with voice entry, media-attach entry, and send control; per-mode feedback | Text-first, voice-first, media-first | One bar serves all three modes, and the hint names every mode so nobody has to guess what is accepted ("Type, speak, or add a photo"). Voice entry shows a waveform while listening and a stop control; the transcript lands in the field as editable text before sending, never sent straight from speech, so a mishearing is corrected in place. Media attachments show as thumbnails with a remove control and a zoom view, and the bar keeps typed text and attachments when the person switches mode mid-composition. Processing states name the step ("Listening", "Reading the photo", "Ready to send") instead of a bare spinner. Every mode is reachable by keyboard and announced to assistive technology with the same labels and order as the visual layout; voice and media entries are never the only route to sending. Cross-check the voice state matrix in catalog/states.md |

## Layout and responsive rules

- Keep a 4 px spacing scale: 4, 8, 12, 16, 24, 32, 48.
- Minimum touch target: 44 px. Minimum pointer target: 24 px with clear spacing.
- Target-size audits separate the 44 px aspiration from the 24 px requirement; a finding against the requirement never presents the aspiration as the bar.
- A target-size finding records the page, viewport, target, and clickable dimensions, states the nearby controls and the exception analysis, and describes the user consequence.
- Remediation picks one path: enlarge the hit area, increase spacing, or change the shared component. Retesting happens after the change ships, including responsive states.
- Focus ring is always visible on keyboard focus and never removed without a replacement.
- Text scales to 200% without loss of content or function.
- Colour is never the only signal; pair it with text, shape, or position.
- Material qualities carry meaning, not decoration: a reflective surface suggests importance, a soft surface approachability, a firm high-contrast control stability or authority. Never apply material treatment without a purpose, and keep affordances legible — users must still tell what they can tap, drag, open, or change.

## Internationalization

Interfaces travel across writing directions and locales. These rules keep
every primitive correct when it does.

- Mirroring: in right-to-left layouts, mirror the reading flow — navigation
  order, back and forward controls, breadcrumb separators, progress bars
  filling from the inline start, carousel direction, and drawer side.
- Never mirror: media controls, clocks, logos, brand marks, non-directional
  icons, numbers, code, untranslated text, and graphs that are not read
  directionally.
- Directional icons: mirror an icon only when it communicates
  left-versus-right movement; keep the accessible label unchanged when the
  icon flips. Icons that carry text or indentation inside them are mirrored
  with the text.
- Logical properties: express spacing and placement as relationships to the
  writing direction (inline-start, inline-end, block-start, block-end),
  never as physical left and right, so one stylesheet serves both
  directions.
- Text expansion: budget roughly 40% extra room for short labels and 30%
  for paragraphs; never fix a container to the source-language label;
  truncation is a last resort and the full text stays reachable.
- Locale-aware formatting: render dates, times, numbers, and currency with
  the locale's separators and conventions; state the timezone on every time
  value; sort lists with locale-aware collation rather than raw code order.
- Mixed-direction text: runs that mix scripts follow the Unicode
  bidirectional algorithm so each run reads in the right order; joining
  scripts are rendered through a shaping engine, never as disconnected
  letters.
- Testing: review every screen in each target direction and confirm that
  focus order, reading order, and visual order still agree.

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

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Every primitive entry gives anatomy, variants, and usage rules.
- [ ] Sheet, step-trace, and code-block entries match the release notes they cite.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
