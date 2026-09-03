# DSD M5-652 — Truncated-amplitude ledger resolves palinstrophy layer-by-layer and exactly recovers the enstrophy balance

Date: 2026-09-03

Status: **INTERNAL LAYER-CAKE LEDGER / FOR `M_a=int(rho-a)_+`, THE CE-H AMPLITUDE TRANSPORT AND THE M5-651 SUPERLEVEL ELLIPTIC IDENTITY GIVE AN EXACT TEMPORAL BALANCE WITH A STRICT SUPERLEVEL DEFICIT `D_a`; INTEGRATING `D_a` OVER ALL AMPLITUDE THRESHOLDS GIVES EXACTLY `P_mag+P_dir=P`, WHILE INTEGRATING `M_a` GIVES `E/2`, AND THE FULL FAMILY RECOMBINES TO THE ORIGINAL SIMILARITY ENSTROPHY LEDGER `E'/2+E/4+P=Q` / THEREFORE THE SUPERLEVEL INEFFICIENCY IS A TRUE LOCALIZATION OF PALINSTROPHY BUT NOT A NEW GLOBAL DISSIPATION / NEW LEVERAGE MUST COME FROM OVERLAP OF A SPECIFIC AMPLITUDE LAYER WITH REPLACEMENT/SHEET-TRANSFER DYNAMICS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Truncated amplitude functional

For every `a>0`, define

\[
\boxed{
M_a(\theta)
:=
\int_{\mathbb R^3}
(\rho(y,\theta)-a)_+\,dy.
}
\]

Because

\[
(\rho-a)_+\le\rho\mathbf1_{\rho>a}
\le\frac1a\rho^2,
\]

we have

\[
\boxed{
0\le M_a\le\frac Ea\le\frac{Z_*}{a}.
}
\]

Thus `M_a` is a bounded observable for every fixed positive threshold.

---

## 2. CE-H amplitude transport

On CE-H,

\[
D_B\rho
=
(\sigma+\kappa-1)\rho,
\]

and

\[
\nabla\cdot B=\frac32.
\]

For `F_a(rho)=(rho-a)_+`,

\[
D_BF_a
=
\mathbf1_{\rho>a}D_B\rho.
\]

Using

\[
\partial_\theta F_a
=D_BF_a-B\cdot\nabla F_a
\]

and integrating over all space gives

\[
M_a'
=
\int_{\rho>a}
(\sigma+\kappa-1)\rho\,dy
+
\frac32
\int(\rho-a)_+dy.
\]

Therefore

\[
\boxed{
M_a'
=
\int_{\rho>a}
\rho\left(\sigma+\kappa+\frac12\right)dy
-
\frac32a|\Omega_a|,
}
\]

where

\[
\Omega_a:=\{\rho>a\}.
\]

---

## 3. Insert the M5-651 superlevel kappa identity

M5-651 gives

\[
\int_{\Omega_a}\kappa\rho\,dy
=-D_a,
\]

with

\[
\boxed{
D_a
:=
\int_{\{\rho=a\}}|\nabla\rho|\,dS
+
\int_{\Omega_a}\rho|\nabla\xi|^2dy.
}
\]

Hence

\[
\boxed{
M_a'
=
\int_{\Omega_a}
\rho\left(\sigma+\frac12\right)dy
-
\frac32a|\Omega_a|
-
D_a.
}
\]

This is the exact truncated-amplitude ledger.

---

## 4. Invariant-average form

On an invariant recurrent component, the bounded observable `M_a` has zero mean derivative.

Therefore

\[
\boxed{
\langle D_a\rangle
=
\left\langle
\int_{\Omega_a}
\rho\left(\sigma+\frac12\right)dy
-
\frac32a|\Omega_a|
\right\rangle.
}
\]

Thus every positive geometric superlevel deficit is paid by an amplitude-layer axial-stretch/volume balance.

This is an amplitude-local version of the production-payer picture.

---

## 5. Layer-cake integral of the truncated mass

Pointwise in `rho>=0`,

\[
\int_0^\infty(\rho-a)_+\,da
=
\int_0^\rho(\rho-a)da
=
\frac12\rho^2.
\]

Hence

\[
\boxed{
\int_0^\infty M_a\,da
=
\frac12E.
}
\]

Consequently

\[
\int_0^\infty M_a'\,da
=
\frac12E'.
\]

---

## 6. Layer-cake integral of the superlevel deficit

For the magnitude-boundary term, the coarea formula gives

\[
\int_0^\infty
\left(
\int_{\{\rho=a\}}|\nabla\rho|\,dS
\right)da
=
\int_{\mathbb R^3}|\nabla\rho|^2dy
=P_{mag}.
\]

For the direction term,

\[
\int_0^\infty
\left(
\int_{\rho>a}\rho|\nabla\xi|^2dy
\right)da
=
\int\rho^2|\nabla\xi|^2dy
=P_{dir}.
\]

Therefore

\[
\boxed{
\int_0^\infty D_a\,da
=P_{mag}+P_{dir}
=P.
}
\]

Thus the family `D_a` is an exact amplitude-layer decomposition of palinstrophy.

---

## 7. Layer-cake integral of the stretching term

By Fubini,

\[
\int_0^\infty
\left(
\int_{\rho>a}
\rho\left(\sigma+\frac12\right)dy
\right)da
=
\int\rho^2\left(\sigma+\frac12\right)dy.
\]

Hence

\[
\boxed{
=
Q+\frac12E.
}
\]

For the threshold-volume term,

\[
\int_0^\infty a|\Omega_a|da
=
\int\left(\int_0^\rho a\,da\right)dy
=
\frac12E.
\]

Thus

\[
\boxed{
\frac32
\int_0^\infty a|\Omega_a|da
=
\frac34E.
}
\]

---

## 8. Exact recovery of M5-486

Integrate the truncated ledger over `a`:

\[
\frac12E'
=
Q+\frac12E
-
\frac34E
-P.
\]

Therefore

\[
\boxed{
\frac12E'
+
\frac14E
+
P
=Q.
}
\]

This is exactly the M5-486 similarity enstrophy ledger.

Hence the new superlevel formalism is perfectly consistent with the old global ledger.

---

## 9. Audit consequence

The strict inequality

\[
\int_{\Omega_a}\kappa\rho<0
\]

for every amplitude layer may look like a new global one-sided damping mechanism.

It is not.

When all thresholds are summed, its total is exactly the already known palinstrophy `P`.

Thus one must not claim a second independent dissipation budget from the superlevel family.

The correct interpretation is:

\[
\boxed{
P
=
\int_0^\infty
\text{superlevel geometric deficit }D_a\,da.
}
\]

---

## 10. Where new leverage can still occur

Although the total family gives no new global budget, a specific threshold can still be valuable if another mechanism is known to occupy that same amplitude band with positive frequency.

Examples include:

- high-amplitude sheet-transfer events;
- coherent replacement carriers;
- vorticity-maximum detachment events;
- non-Beltrami transverse-magnitude packets.

If one can prove that such an event forces

\[
D_{a_*}\ge d_*>0
\]

on a fixed threshold `a_*` while the available stretching payer at that same threshold is strictly smaller, a genuine contradiction would follow.

No such strict same-layer mismatch is proved here.

---

## 11. Updated target

The multi-sheet/forced problem should now be attacked **threshold-locally**, not by summing all amplitude layers.

The highest-value question is:

\[
\boxed{
\text{Does every flux-recharging sheet-transfer event cross a fixed high-amplitude layer where }D_a
\text{ has a uniform cost?}
}
\]

If yes, M5-647's finite transverse resource and the present layer-resolved dissipation may be combined.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]