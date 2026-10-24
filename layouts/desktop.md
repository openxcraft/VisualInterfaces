# Desktop Layout

Pointer-and-keyboard-first application surfaces for large screens:
multiple windows, menu bars, deep keyboard support, and density that
honours long working sessions.

## Classification

- Category: layouts / desktop

When to use:

- Productivity tools, creative software, developer tools, and any
  application used for hours at a time on a large display.

When to avoid:

- Touch-first consumption, single-task kiosk flows, and any surface
  where the person never has a keyboard.

## Elements and components

Window chrome with title bar; menu bar; toolbars; status bar; context
menus; multiple document windows or tabs; a searchable command list as
a complement to — not a replacement for — the menu bar; a shortcut
reference reachable in the product.

## Layout and responsive rules

- Menu bars: every command stays reachable by keyboard. Group commands
  by task and keep the order people expect (application, file, edit,
  view, window, help, and their equivalents). The platform modifier
  plus the underlined letter opens a top-level menu; arrow keys move
  between items; Enter or Space opens a submenu; Escape collapses it
  and returns focus to the trigger.
- Mnemonics: keep access keys unique within each menu level; reuse
  across levels is allowed. Use the first letter of the first or
  second word for frequent items; use numbers for dynamic lists such
  as recent files.
- Keyboard shortcuts: reserve single-modifier shortcuts for the dozen
  most frequent actions; show the shortcut next to the menu label so
  it is learned in place; never steal shortcuts from text editing;
  keep a shortcut reference discoverable inside the product. For the
  keyboard-first command surface, see the Command palette pattern in
  ../catalog/patterns.md.
- Context menus: appear at the pointer or on the focused element;
  contain only actions valid for the current selection; duplicate the
  most relevant menu-bar items rather than hiding them exclusively in
  the context menu.
- Drag and drop: a progressive enhancement layered on an already
  keyboard-usable flow. Always provide a non-drag path (buttons or
  menu commands) for reordering, moving, and organising. Handle
  pointer, touch, and stylus through one input approach; avoid heavy
  layout work during move events; validate drag behaviour across
  pointer and touch inputs.
- Multi-window management: windows remember position and size;
  support edge and corner tiling zones; offer saved layouts for
  recurring task sets; keep one window per document with a clear
  active window; keep menu access reachable in full-screen mode.
- Density: honour the platform density setting — compact density for
  data-heavy work, comfortable density for mixed content. Keep text
  selectable at every density.
- Window and screen size bands: treat narrow windows like compact
  layouts — collapse toolbars into overflow, switch multi-pane views
  to single-pane with back navigation, and keep primary actions
  visible.
- Container-query responsiveness: components adapt to the size of
  their container, not only to the viewport, so the same component
  works in a full page, a sidebar, a modal, and a dense dashboard
  grid. Declare the container on the parent (inline-size containment
  for width-driven layout, named where several containers nest), then
  query that container for the component's breakpoints. Verify every
  reusable component in all four contexts — full page, sidebar, modal,
  and dense grid — because a component tuned only to the viewport
  breaks the moment it lands in a narrow panel. Keep viewport queries
  for page-level bands and container queries for component behaviour;
  remember that size containment needs a contextual or explicit size
  from the parent, or the container collapses. Use container-relative
  units sparingly, for fluid type and spacing inside the component,
  never to smuggle a viewport breakpoint back in.

## States

Full state definitions live in `../catalog/states.md`. The desktop
layout's additions are below.

| State | Desktop-specific note |
| --- | --- |
| Default | Menu bar, toolbars, and the active window all render at rest with full contrast. |
| Hover | Pointer-only highlight on menu items and toolbar controls; no essential information on hover alone. |
| Active | Pressed menu items and toolbar buttons show feedback within 100 ms; the active window is visually distinct from inactive ones. |
| Disabled | Unavailable menu items render dimmed with the reason discoverable; disabled drag targets reject drops with an explanation. |
| Loading | Window content skeletonises in place; the menu bar and chrome never block on content loading. |
| Empty | A new document or window opens with a template gallery or a clear first action, never a blank void. |
| Error | Keep the document and its undo history intact; place the message next to the failed action with retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Menu-bar, mnemonic, shortcut, context-menu, drag-and-drop, and multi-window rules are all documented.
- [ ] The non-drag path is stated as a requirement, not an option.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
