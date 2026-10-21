# Commerce Layout

Listing, product, cart, and checkout layouts for browsing and buying. Price, availability, and total cost stay visible at every step.

## Classification

- Category: layouts / ecommerce

When to use:

- Catalogues, product pages, carts, and checkout flows.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Category navigation; filter and sort controls; product grid with image area, name, price, and rating summary; product detail with options, quantity, and add action; cart summary with line items and totals; checkout steps for delivery, payment, and review.

## Layout and responsive rules

- Grid: 2 columns on compact, 3 to 4 on medium and expanded; card content order is fixed so prices align.
- Product detail on compact screens keeps the add action in a sticky bar after scrolling.
- Totals show all mandatory charges before the final step; no cost appears for the first time at payment.
- Checkout is a short wizard with a visible step indicator and an order summary that stays reachable.
- Filters collapse behind a clearly labelled control on compact screens; active filters remain visible as tags.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The ecommerce layout at rest, with full contrast and a clear label. | Ready for input or selection. |
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
