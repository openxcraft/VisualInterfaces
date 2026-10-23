# Component Libraries

A neutral index of component library categories and representative options.
Listings here are references, not endorsements. Check the licence and current
version of any option before use.

## Classification

- Category: resources.

When to use:

- Choosing a starting point for primitives instead of building every control.
- Comparing styled sets against unstyled, accessible building blocks.

When to avoid:

- Treating a listing as a quality guarantee; evaluate accessibility and state
  coverage against `catalog/states.md` first.

## Elements and components

| Option | Category | Notes |
| --- | --- | --- |
| Radix UI | Unstyled accessible primitives | Dialogs, menus, popovers, and form controls with keyboard and focus behaviour included; styling is supplied by the project. |
| Headless UI | Unstyled accessible components | Interactive components for common interface patterns, designed to be styled by the project. |
| shadcn/ui | Copy-in component set | Components copied into the project codebase and owned there; built on unstyled primitives and utility styling. |
| MUI | Styled component set | A comprehensive styled set for application interfaces with dense data components. The current direction pairs a stable unstyled-primitives layer — focus, keyboard, and role behaviour without styling — with token-based theming; new form controls such as a number field are built on those primitives, and the advanced data line adds grid-chart integration and server-side pivoting. Compare with the headless behaviour primitive pattern in `../catalog/primitives.md`. |
| Mantine | Styled component set | A broad set including form, date, and notification components with theming support. |
| Ant Design | Styled component set | A mature set with dense tables, trees, and forms suited to administration interfaces. |
| Chakra UI | Styled component set | Accessible components with style properties and a theming system. |
| daisyUI | Utility-class component themes | Semantic component classes added to utility styling, with built-in themes and no scripting dependency. |
| Flowbite | Utility-class component set | Components for several frameworks built on utility styling. |
| Bootstrap | Styled framework set | A long-standing responsive grid and component set for plain markup and server-rendered pages. |
| Web Awesome | Web-component library | A current web-components set succeeding an earlier one: dozens of components, multiple colour palettes, native element styles, cascade layers, and server-side rendering support, with commercial additions such as combobox, file input, date picker, video, sparklines, charts, and a data grid on the way. |
| Accessible Components Library | Accessibility-documented component set | A small v1.0.0 set (accordion, breadcrumbs, dialog, disclosure, pagination, tabs, text input, textarea) where each component ships with documented accessibility requirements mapped to WCAG 2.2 success criteria at levels A, AA, and AAA, plus working examples, test scenarios, assistive-technology compatibility notes, and usability recommendations the standard does not cover, such as high-contrast theme behaviour. Requirements are grouped into ten themes (adaptability, animation and movement, assistive technologies and semantics, colour and contrast, consistency and predictability, images and media, input assistance, keyboard, navigation, pointer and touch). Test it in your product before relying on it; it is a reference, not a production-ready design system. |
| Maz-UI | Styled Vue component set | A Vue set whose current major line ships logical direction by default: every directional prop, slot, and style hook uses `start`/`end` instead of `left`/`right`, so layouts mirror correctly under right-to-left settings without per-component fixes. The same line overhauls theming on a perceptually uniform colour scale with honest token names and per-component token overrides. Check the current version and its migration notes before adopting; a new major line may drop support for the previous one. |

## Layout and responsive rules

- Prefer options that expose every state in `catalog/states.md`.
- Check target sizes, focus behaviour, and text scaling before visual fit.
- Record the chosen option, version, and licence in the project that uses it,
  not in this file.

## States

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | A library entry at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | A category with no verified option stays listed as a gap rather than being filled with an unchecked entry. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A broken or superseded reference is corrected or removed at the next review. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Every listing points at a real, maintained library; external links are allowed in this file only.
- [ ] Entries are grouped by use case with one-line descriptions.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
