# Authentication Example

A minimal, framework-free sign-in page: an identifier and credential
form with a show-and-hide control, a passkey-first route with a
visible fallback chain, a second-factor code step, and an account
recovery route, with all seven states. It demonstrates the
authentication layout rules in `../../layouts/auth.md` and the
sign-in pattern rows in `../../catalog/patterns.md` — passkey
sign-in, second-factor sign-in, verification-code entry, and
account recovery. Open `index.html` in a browser; no build step is
required.

## Classification

- Category: examples / auth

When to use:

- Checking the authentication layout and the sign-in pattern rows
  in `../../catalog/patterns.md` against a working page.
- Testing the passkey-first route, the fallback chain, the
  second-factor step, and the recovery path for a lost credential.

When to avoid:

- Production use; content is structural placeholder text and no
  credential is checked or sent anywhere.
- A registration flow; the sign-up route is the one named here,
  and the full registration sequence is covered by the identity
  verification onboarding row.

## Elements and components

A centred sign-in card with an identifier field and a credential
field with a show-and-hide control; a primary sign-in action; a
passkey route offered beside a visible fallback chain of app push,
email link, email code, and text-message code; a second-factor code
step with a resend control and a backup-code route; a recovery link
that never reveals whether an account exists; inline
demonstrations of every state.

## Layout and responsive rules

- The card is centred on expanded screens with a maximum form
  width of about 400 px, and full-width on compact screens.
- One column, one primary action; secondary actions are text links
  below the form.
- Labels stay visible; the identifier and credential fields carry
  autocomplete attributes.
- The passkey route sits beside the primary action with the
  fallback chain immediately visible below it, never hidden behind
  a failed attempt.
- The second-factor step is a separate card: one code field that
  accepts a pasted code, a resend control that states the wait,
  and a backup-code route that stays visible at all times.
- A lockout message states the wait time and the next step, and
  never reveals whether an account exists.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The sign-in card at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight on the sign-in action and the fallback links. | No essential information on hover alone. |
| Active | The chosen fallback route is marked in text and shape, not colour alone, within 100 ms of the choice. | Feedback appears within 100 ms of input. |
| Disabled | The sign-in action renders dimmed with the reason stated beside it until the identifier and credential are entered. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | A skeleton replaces the fallback list while methods load, and the sign-in action shows progress while the sign-in is checked. | Keep layout dimensions stable so content does not shift. |
| Empty | A variant in the markup shows no saved credential on this device, with the fallback chain as the one clear next action. | Offer one clear next action that sets up sign-in. |
| Error | Variants in the markup show a wrong code with the attempts remaining, and a lockout that states the wait time and the next step, each keeping the entered identifier and offering a retry or another route. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] The example HTML parses with no unclosed tags.
- [ ] The example demonstrates the authentication layout rules it documents.
- [ ] The passkey route, the visible fallback chain, and the second-factor step are all present.
- [ ] The wrong-code and lockout variants keep the entered identifier and offer another route.
- [ ] Run instructions work from a fresh checkout.
