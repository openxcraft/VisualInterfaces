# Landing Example

A minimal, framework-free landing page using semantic markup and a single stylesheet. Open `index.html` in a browser; no build step is required.

## Classification

- Category: examples / landing

When to use:

- Checking the landing layout rules in `layouts/landing.md` against a working page.
- Testing the outcome-first hero, section order, lead-form friction, and the compact sticky action bar.

When to avoid:

- Production use; numbers, statements, and form entries are structural placeholders.

## Elements and components

Header with navigation and primary action; outcome-first hero with one primary action and a proof point; social-proof strip; benefit blocks; how it works; deeper proof; objection handling; closing action; a three-field lead form; a compact sticky action bar.

## Layout and responsive rules

- The hero names the audience and a measurable outcome, carries exactly one primary action, and places a proof point before the first scroll.
- Sections mirror the decision: hero, social proof, benefit blocks, how it works, deeper proof, objection handling, then a closing action.
- The lead form keeps to three fields.
- On compact screens a sticky action bar appears only after the hero action scrolls away; in this static demo the bar is shown pinned below the hero so its placement can be inspected.
- Hero motion honours the reduced-motion preference: looping hero media pauses or fades for people who asked for less movement, and the offer stays readable with motion off.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The example page at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on the primary action and links: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks replace the proof numbers while they load. | Keep layout dimensions stable so content does not shift. |
| Empty | A search of the questions with no match shows the page structure with an explanation and one action that shows all questions. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A failed form submission keeps the entered values, states the problem next to the form, and offers a retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the landing layout rules it documents.
- [ ] The hero carries one primary action with a proof point before the first scroll.
- [ ] Run instructions work from a fresh checkout.
