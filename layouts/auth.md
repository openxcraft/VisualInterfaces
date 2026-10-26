# Authentication Layout

Screens for sign-in, registration, recovery, and verification. The goal is a short, predictable path with clear recovery at every step.

## Classification

- Category: layouts / auth

When to use:

- Any flow that verifies identity before granting access.

When to avoid:

- Using this layout for a task it does not serve, such as a long reading page or a focused single-step form.

## Elements and components

Identifier field; credential field with show and hide control; primary submit action; secondary links for recovery and registration; verification code fields where used; plain security notes in short sentences.

## Layout and responsive rules

- Centered card on expanded screens, full-width form on compact screens; maximum form width about 400 px.
- One column, one primary action; secondary actions are text links below the form.
- Labels stay visible; autocomplete attributes are set for identifier and credential fields.
- Verification uses separate fields or a single field with clear grouping; paste is allowed.
- Session and lockout messages state the wait time and the next step; they never reveal whether an account exists.
- Prefer passkey-first sign-in: put passkeys in the username autofill dropdown via conditional mediation so the browser offers them inline, rather than building a standalone sign-in-with-passkey button.
- Keep a visible fallback chain and never hide options: after the primary passkey step, keep app push, email magic link, email one-time code, and SMS fallbacks immediately visible below the primary action; hiding fallbacks raises frustration when passkey sign-in fails without raising passkey use.
- Time the passkey enrollment once: repeated enrollment prompts are linked to authentication abandonment; a workable hybrid is first visit via magic link, then one immediate passkey-creation prompt, with return visits authenticating single-tap via autofill.
- For cross-device sign-in via QR, label the context explicitly ("use your phone to sign in on this new device") before the code appears; a bare code reads as something broken.
- Offer a credential management page: name each passkey with device metadata, let the person rename and revoke them, and issue one-time recovery codes at setup.
- Offer device biometric sign-in only after a first successful sign-in, never during registration: the prompt lands once the person already trusts the account, and registration stays short.
- The operating system owns the biometric prompt; design the timing, framing, and fallback around it rather than building a replacement prompt screen.
- Show the biometric option only where the device can actually use it; where it cannot, fall back to the other methods without comment.
- Always keep a password or PIN fallback visible beside the biometric option: face and fingerprint checks fail in poor light, with wet hands, or when sensors miss, and the person must never be stranded.
- Treat dismissal of the biometric prompt as a return, not an error: show no error message when the person cancels. On a genuine failure, state the plain cause, offer a retry, and keep the fallback beside it.

## States

Every element and page in this group defines all seven states. Missing states are treated as incomplete work.

| State | Appearance | Behaviour |
| --- | --- | --- |
| Default | The auth layout at rest, with full contrast and a clear label. | Ready for input or selection. |
| Hover | Pointer-only highlight: subtle background or border change. | No change on touch devices; hover never carries essential information alone. |
| Active | Pressed or selected appearance while interaction is in progress. | Feedback appears within 100 ms of input. |
| Disabled | Reduced contrast, no pointer response, still readable. | Explain why it is unavailable nearby when the reason is not obvious. |
| Loading | Skeleton blocks or a progress indicator replace live content. | Keep layout dimensions stable so content does not shift. |
| Empty | Show the layout structure with an explanation and one action that adds or finds content. | Offer one clear next action and, where relevant, a reset for filters. |
| Error | Keep navigation in place, show the failure in the content area, and offer retry. | Keep entered data, place the message next to the problem, and offer a retry. |

## Pre-publish checklist

The canonical publishing checklist lives in `../CONTRIBUTING.md`; the checks below are specific to this file.

- [ ] Passkey-first flow, the visible fallback chain, and one-time enrollment are all documented.
- [ ] Biometric sign-in timing, prompt ownership, fallback, and cancellation handling are documented.
- [ ] QR cross-device labelling and credential-management rules are present.
- [ ] All seven states appear by name: default, hover, active, disabled, loading, empty, error.
