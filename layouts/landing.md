# Landing Page Layout

A single-purpose page that presents one offer and one primary action, supported by short proof and detail sections in reading order.

## Classification

- Category: layouts / landing

When to use:

- A public entry page for a product, service, or campaign with one conversion goal.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Header with navigation and primary action; hero with headline, short supporting text, and primary action; feature grid; evidence section with numbers and short quotes paraphrased as plain statements; comparison or pricing summary; frequently asked questions; footer.

## Layout and responsive rules

- Hero fits the first viewport on expanded screens without hiding the next section's start.
- One primary action repeats at natural stopping points; wording stays identical.
- Compact: single column in reading order — headline, action, features, evidence, questions.
- Sticky action bar on compact screens appears only after the hero action scrolls away.
- Media is abstract or product-focused; decorative media never pushes the headline below the fold on compact screens.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The landing layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

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
