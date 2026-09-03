# DSD M5-680 — Audit toy: a nested finite-flux cascade exactly saturates the 3/2 late-activation gate

Date: 2026-09-03

Status: **DSD ANTI-SHORTCUT COUNTERMODEL / A COUNTABLE FAMILY OF MATERIAL LABELS WITH BASE FLUX `phi_n(0)=exp(-3 n T/2)` CAN BE GIVEN A PRE-ACTIVATION MULTIPLIER `kappa_n=3/2` SO THAT THE `n`TH LABEL REACHES ORDER-ONE RETAINED FLUX AND ORDER-ONE NORMALIZED CURVATURE AT TIME `theta_n=nT`; THE TOTAL BASE FLUX IS FINITE AND THE M5-621 `-3/2` RATIO LAW IS SATURATED EXACTLY / PAST LABELS CAN BE SWITCHED TO A NEGATIVE PHASE SO THE INSTANTANEOUS TOTAL FLUX STAYS FINITE / THEREFORE M5-647 + M5-621 + M5-677 + M5-678 DO NOT BY THEMSELVES CONTRADICT AN INFINITE REPLACEMENT CASCADE / THE MODEL DELIBERATELY OMITS `Delta W=kappa W`, BETCHOV/STRAIN COUPLING, AND THE CE-H ELLIPTIC SUPERLEVEL IDENTITIES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-677 forces a fixed-strength curvature packet at every recurrent CE-H state.
M5-621 gives each retained material label a finite normalized curvature lifetime.
M5-678 then forces labels activated at late times to originate from exponentially small base flux and to accumulate mean `kappa` at least `3/2`.

Before treating this as a contradiction, construct an abstract cascade that realizes exactly those scalings with a finite base resource.

Any final proof must use an ingredient absent from this toy.

---

## 2. Discrete activation times

Fix a generation spacing

\[
T>0
\]

and define

\[
\boxed{\theta_n=nT.}
\]

For each `n>=1` introduce one abstract material flux population `L_n`.

Its base flux is

\[
\boxed{
\phi_n(0)=e^{-3nT/2}.
}
\]

The total base resource is finite:

\[
\boxed{
\sum_{n=1}^\infty\phi_n(0)
=
\sum_{n=1}^\infty e^{-3nT/2}
<\infty.
}
\]

Thus the M5-647 type finite transverse resource does not prohibit the family.

---

## 3. Critical positive-kappa amplification

For `0<=theta<=theta_n`, set

\[
\boxed{\kappa_n(\theta)=\frac32.}
\]

Let the material flux satisfy

\[
\frac d{d\theta}\log\phi_n=\kappa_n.
\]

Then

\[
\phi_n(\theta)
=e^{-3nT/2}e^{3\theta/2}.
\]

At its activation time,

\[
\boxed{
\phi_n(\theta_n)=1.
}
\]

Hence every generation starts from an exponentially smaller base population but reaches the same retained order-one flux.

Moreover

\[
\frac1{\theta_n}\int_0^{\theta_n}\kappa_n d\theta
=\frac32,
\]

which exactly saturates the M5-678 lower gate.

---

## 4. Saturating the curvature/flux ratio law

Let

\[
R_n(\theta)
:=
\frac{Z_n(\theta)}{\phi_n(\theta)}
\]

and impose the M5-621 law

\[
R_n(\theta)=R_n(0)e^{-3\theta/2}.
\]

Choose

\[
Z_n(0)=1.
\]

Since

\[
\phi_n(0)=e^{-3nT/2},
\]

we have

\[
R_n(0)=e^{3nT/2}.
\]

Therefore at activation

\[
R_n(\theta_n)=1.
\]

Because

\[
\phi_n(\theta_n)=1,
\]

we obtain

\[
\boxed{Z_n(\theta_n)=1.}
\]

Thus every activation carries an order-one normalized curvature-amplitude packet while respecting the strict M5-621 cocycle exactly.

---

## 5. Keeping the instantaneous flux resource finite

If every previously activated label remained at order-one flux forever, the current total flux would grow with the number of generations.
That is not necessary.

After activation, for example set

\[
\kappa_n(\theta)=-1
\qquad
(\theta>\theta_n).
\]

Then

\[
\phi_n(\theta)
=e^{-(\theta-\theta_n)}
\]

for the retired label.

At a time `theta` the sum of not-yet-activated and retired populations is bounded by geometric series on both sides of the current generation.
Thus one can arrange

\[
\boxed{
\sup_\theta\sum_n\phi_n(\theta)<\infty.
}
\]

So finite base flux and finite instantaneous flux are both compatible with infinitely many order-one activation events.

---

## 6. Adding a compensating negative payer at the abstract level

The real CE-H branch has negative enstrophy-weighted `kappa` budget.
The toy can imitate this kinematically by assigning separate high-amplitude payer populations with negative `kappa` during each generation.

Because their weights and phase biases can be chosen independently in the abstract model, one can enforce qualitative constraints of the form

\[
\langle\kappa E\rangle<0
\]

while retaining the critical positive amplification on the small future labels.

Therefore the global sign budget alone is also insufficient unless its **elliptic spatial coupling** to the positive labels is used.

---

## 7. What the toy deliberately does not satisfy

The construction is not a Navier–Stokes solution.
It does not produce spatial vector fields satisfying

\[
\boxed{\Delta W=\kappa W,}
\]

\[
\boxed{\Sigma W=\sigma W,}
\]

or the Biot–Savart relation between `Sigma` and `W`.

It does not satisfy the exact component/superlevel deficits

\[
\int \kappa\rho(\rho-a)<0,
\]

the Miller strain-vorticity compatibility M5-671, or the Betchov middle-strain obligation M5-674--676.

Those are precisely the ingredients a valid final closure must exploit.

---

## 8. Audit verdict

The following chain is **not** a contradiction by itself:

\[
\boxed{
\text{finite base flux}
+\text{curvature mandatory}
+\text{finite label curvature lifetime}
+\text{positive-rate replacement}.
}
\]

The critical nested family above realizes all four abstractly.

Hence any proof step that closes the remaining branch while also applying to this toy is missing essential Navier–Stokes structure.

---

## 9. Sharpened final target

The last hard question is now genuinely PDE-specific:

\[
\boxed{
\text{Can the elliptic eigenfield system }\Delta W=\kappa W
\text{ support a sequence of vortex-line populations whose material flux amplification}\
\text{asymptotically saturates the critical rate }\langle\kappa\rangle=3/2,
\text{ while Betchov/strain and superlevel deficit identities remain recurrently bounded?}
}
\]

A negative answer to this question would close the nested-replacement mechanism.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
