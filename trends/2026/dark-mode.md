# Dark Mode Design

Dark colour schemes as a first-class theme: not an inverted palette but a
separately designed surface system with its own typography, elevation,
and accent rules.

## Classification

- Category: trends / 2026 / dark-mode

When to use:

- Products where people work at night, in low light, or on emissive
  displays — and everywhere a theme switcher is offered.

When to avoid:

- Applying the direction as decoration without the behaviour and guardrails described here.
- Simply inverting the light palette and calling it done.

## Elements and components

A semantic token set shared across themes; dark surface scale; adjusted
type scale; redesigned accents; elevation-by-lightness instead of
shadows; a theme switch with system default and user override.

## Layout and responsive rules

- Never invert the palette: use dark greys rather than pure black for
  backgrounds to avoid halation, and off-white or light grey rather than
  pure white for text — slightly reduced contrast reads more comfortably
  than maximum contrast on dark.
- Adjust type for dark: slightly heavier body weight, 1–2 px larger body
  size, about 150% line height, and a touch more letter spacing;
  grotesque sans faces hold up better than serifs on dark.
- Replace shadows with surface elevation: layers get progressively
  lighter surface tones with depth, since dark shadows are invisible on
  dark backgrounds.
- Redesign accents, do not reuse them: shift accent colours lighter or
  more saturated for legibility on dark; verify every text and
  background pair in both themes.
- Build the token contract once: the same semantic token names across
  themes with different values; respect the system colour-scheme
  preference as the default and keep a user override that persists.
- Animate the switch in about 200–300 ms and honour reduced-motion
  settings with an instant swap.
- Test on emissive, transmissive, and reflective displays: behaviour
  differs between OLED, LCD, and e-ink, especially for elevation steps
  and near-black text.

## Contrast-verification routine

Run this routine before any theme ships or changes:

- Test every text/background pair against both token sets: a pair that
  passes on one theme often fails on the other, and muted or disabled
  text is the most common dark-theme failure.
- Verify disabled and secondary text at the size it is used; a token
  value that reads fine at 16 px body can fail at 12 px caption size.
- Define forced-colours-mode behaviour: the theme must survive the
  operating-system high-contrast palette. Boundaries drawn with border
  or elevation tones need explicit forced-colour adaptations, and the
  elevation-by-lightness steps degrade to borders or outlines where
  colour is removed.
- Text over photography: place text on a scrim or a translucent panel
  rather than trusting the image; test the worst-case image brightness,
  not the curated hero shot. Where text must sit directly on imagery,
  choose the colour by sampling the actual background under each text
  run.
- Recheck the routine whenever a new surface, accent, or elevation
  step is added to either theme; contrast debt accumulates silently.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The dark theme at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Token contract, elevation, and type-adjustment rules are present.
- [ ] The contrast-verification routine covers both token sets, forced-colours mode, and text over imagery.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
