# Desktop Example

A minimal, framework-free desktop surface: a menu bar, a toolbar, two
panes with drag-and-drop between them, a status bar, a command list,
and a shortcut reference. It demonstrates the desktop rules in
`../../layouts/desktop.md` with all seven states. Open `index.html`
in a browser; no build step is required.

## Classification

- Category: examples / desktop

When to use:

- Checking the desktop layout rules in `../../layouts/desktop.md`
  against a working page.
- Testing menu-bar keyboard travel, shortcut discovery, drag-and-drop
  with a keyboard path, and multi-pane layout on a large screen.

When to avoid:

- Production use; content is structural placeholder text.
- Touch-first tasks; those belong on a phone or tablet surface.

## Elements and components

A menu bar across the top with named menus; a toolbar with the dozen
most frequent actions; two panes side by side — a document list and
the open document — with drag-and-drop between them and a keyboard
path for the same moves; a command list opened from the toolbar; a
shortcut reference reachable from the menu bar; a status bar stating
the document, the selection, and the saved state; inline
demonstrations of every state.

## Layout and responsive rules

- The menu bar holds every command: groups follow the expected order
  (application, file, edit, view, window, help), and every menu opens
  from the keyboard — the platform modifier plus the underlined
  letter opens a top-level menu, arrow keys move between items,
  Enter or Space opens a submenu, and Escape collapses it and
  returns focus to the trigger.
- Access keys stay unique within each menu level; the shortcut for
  each frequent action sits beside its menu label so it is learned
  in place, and the full shortcut reference opens from the menu bar.
- Drag and drop is a progressive enhancement: every move the panes
  offer by dragging also works from a menu command or a button, so
  the same move is reachable without a pointer.
- Windows remember position and size; the window strip below the
  menu bar names each open window and which one is active, and a new
  window opens beside the one in use instead of landing on top of it.
- Density follows the platform setting: compact for data-heavy work,
  comfortable for mixed content, with text selectable at every
  density.
- A narrow window collapses like a compact layout: the toolbar folds
  into overflow, the two panes become one pane with back navigation,
  and the primary actions stay visible.
- Touch stays secondary: keyboard and pointer paths remain complete
  when touch is used, and element positions and visual sizes do not
  change when the person switches inputs.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The desktop surface at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on menu items and toolbar controls. | No essential information on hover alone. |
| Active | Pressed menu items and toolbar buttons confirm the press visibly within 100 ms; the active window is visually distinct from inactive ones. | Feedback appears within 100 ms of input. |
| Disabled | Unavailable menu items render dimmed with the reason discoverable; disabled drag targets reject drops with an explanation. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Window content skeletonises in place; the menu bar and chrome never block on content loading. | Keep layout dimensions stable so content does not shift. |
| Empty | A new document opens with a template gallery or a clear first action, never a blank void. | Offer one clear next action that sets up the document. |
| Error | A variant in the markup shows a failure note beside the failed action with retry, keeping the document and its undo history intact. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the desktop rules it documents.
- [ ] Every menu opens from the keyboard and every drag has a keyboard path.
- [ ] Run instructions work from a fresh checkout.
