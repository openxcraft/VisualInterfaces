# Food Rescue and Surplus Food Pickup Layout

A page that lists surplus food offers from nearby places, states the pickup window and the price beside each offer, and carries one offer through reserve, collection, and confirmation without hiding a cost or a deadline.

## Classification

- Category: layouts / food rescue

When to use:

- A page where a place offers food that would otherwise go to waste, and a person reserves it for collection inside a stated window.

When to avoid:

- Using this layout for ordering a chosen meal from a menu, for planning home cooking, or for collecting an order that was already placed through a checkout.

## Elements and components

Nearby offers shown as a map and as a list that stay in step with each other; an offer card naming the place, the pickup window, the price, and the distance; a plain statement that the contents are a surprise assortment rather than a chosen meal; dietary and allergen notes for each offer; a reserve step that states the collection window and the place before any payment; a handover code or confirmation shown at pickup; a stated rule for a missed pickup window; favourites with alerts when a chosen place posts a new offer; and a receipts view listing past collections with their windows and prices.

## Layout and responsive rules

- Map and list show the same offers in the same order; choosing an offer in one view marks it in the other, and the list stays fully usable where the map cannot load.
- Order offers by pickup window first, so the offer that must be collected soonest is easiest to reach; distance and price stay visible beside each offer rather than appearing only after it is opened.
- The pickup window is the most prominent fact on the offer card after the place name: the start and end times in plain words, with the time left until the window closes stated beside them.
- State plainly that the contents are a surprise assortment, and never present an offer as a chosen meal; where the assortment has a theme or a size, state both on the card.
- The reserve step repeats the place, the window, and the full price on one screen before payment, and payment never adds a charge that was not shown on the offer card.
- The handover code appears on the confirmation screen and stays reachable from the receipts view until the window ends; the code is the proof of the reservation, so sharing the code shares the collection.
- A missed window states plainly what follows: whether the reservation lapses, whether the payment is returned, and where the next offer from the same place can be found.
- Favourites are kept per place, and an alert names the place and the new window rather than sending a bare prompt to open the page.
- Keep the page usable on a slow connection: text and prices load first, the map loads after, and a failed map load never blocks the list or the reserve step.
- Ask for location only while browsing nearby offers, and offer a typed place search as an equal route so nobody must share a precise position to see offers.
- Touch targets are at least 44 px in the smallest dimension, and the reserve action stays reachable without scrolling on compact screens once an offer is open.
- Countdown and timer motion honour the reduced-motion preference: the remaining time is always shown as text, and no offer depends on animation to be understood.

## Reserve and collection

- Reserve is one decision with one confirmation: choose the offer, check the place, window, and price, then confirm; a second confirmation screen for the same facts is not added.
- The confirmation names the place, the address, the window, the price paid, and the handover code, and states what to do when the place is closed or the offer is gone on arrival.
- Collection is confirmed in the same view that showed the code, so the person never has to search for proof after handing the food over.
- Where collection needs a step the person cannot do alone, such as carrying a large bag, the offer states that before reserve rather than at the door.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The food rescue layout at rest, with offers in window order, full contrast, and a clear label on every action. | Ready for input or selection. |
| Hover | Pointer-only highlight on an offer card or reserve control: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance on the chosen offer and the reserve control while the action is in progress. | Feedback appears within 100 ms of input. |
| Disabled | A closed window or a sold-out offer shown with reduced contrast, no pointer response, still readable, with the reason stated beside it. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks for offer cards or a progress indicator replace live content while offers refresh. | Keep layout dimensions stable so content does not shift. |
| Empty | No offers nearby shows the layout structure with an explanation, the search area in plain words, and one action to widen the search or follow a place. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | A failed refresh or a failed reserve keeps the offer list and the entered details in place, shows the failure in the content area, and offers retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Pickup window, price, and surprise-assortment statement appear on every offer card.
- [ ] Reserve repeats place, window, and full price before payment, with no charge added later.
- [ ] Missed-window rule, handover code, and favourites alerts are stated.
- [ ] Map failure never blocks the list or the reserve step.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
