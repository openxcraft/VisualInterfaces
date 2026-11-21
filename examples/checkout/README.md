# Checkout Example

A minimal, framework-free checkout page: an order summary beside a
guest checkout choice, a delivery slot picker, saved payment method
selection, and promo-code entry, with the order total recalculated at
every step. It demonstrates the ecommerce layout rules in
`../../layouts/ecommerce.md` and the checkout pattern rows in
`../../catalog/patterns.md` — guest checkout, saved payment method
selection, delivery slot picker, and promo-code entry — with all
seven states. Open `index.html` in a browser; no build step is
required.

## Classification

- Category: examples / checkout

When to use:

- Checking the ecommerce layout and the checkout pattern rows in
  `../../catalog/patterns.md` against a working page.
- Testing the order of the checkout steps, the recalculation of the
  order total, and the recovery paths for a failed payment and a
  declined promo code.

When to avoid:

- Production use; content is structural placeholder text and the
  payment controls submit nothing.
- A signed-in checkout; the guest route is the one demonstrated
  here, and the account route is covered by the guest checkout row.

## Elements and components

An order summary with one line per item and a running total; a guest
checkout choice that keeps the order when an account is created
later; a delivery slot picker offering dated windows the fulfilment
side can keep; a saved payment method list with one method chosen at
a time; a promo-code entry that shows the result as a line item
beside the recalculated total; a place-order action that stays
unavailable until the required choices are made; inline
demonstrations of every state.

## Layout and responsive rules

- The checkout runs in task order on a compact screen: order
  summary, delivery, payment, promo code, then the place-order
  action, with the running total always visible beside the action
  that changes it.
- On an expanded screen the summary sits beside the form; the total
  and the place-order action stay in view while the form is
  completed, and the summary never scrolls away from the action.
- One question per step: the delivery choice, the payment choice,
  and the promo code each own their own section, so a change in one
  never hides the state of another.
- A change recalculates at once: choosing a slot, a payment method,
  or a code updates the total in place, and the line that changed is
  named beside the new total.
- The place-order action stays unavailable until delivery, payment,
  and contact details are all chosen; the reason it is unavailable
  is stated beside it, not only in its appearance.
- A failed payment keeps the order, the chosen slot, and the entered
  code, and offers retry on the same page; a declined code names the
  reason and keeps the order total unchanged.
- An empty basket shows why the checkout is empty and offers the
  action that fills it, rather than a bare page.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The checkout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on slot, payment, and code controls. | No essential information on hover alone. |
| Active | A chosen slot or payment method is marked in text and shape, not colour alone, within 100 ms of the choice. | Feedback appears within 100 ms of input. |
| Disabled | The place-order action renders dimmed with the reason stated beside it until delivery, payment, and contact details are chosen. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | A skeleton replaces the slot list while slots load, and the place-order action shows progress while the order is sent. | Keep layout dimensions stable so content does not shift. |
| Empty | An empty basket states why it is empty and offers the action that fills it, with the checkout sections hidden until there is an order. | Offer one clear next action that sets up the order. |
| Error | A variant in the markup shows a failed payment and a declined promo code in place, each with its reason and a retry, keeping the order, the slot, and the code entered. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the checkout rows it documents.
- [ ] The total recalculates in place for every slot, payment, and code change.
- [ ] The failed-payment and declined-code variants keep the order intact.
- [ ] Run instructions work from a fresh checkout.
