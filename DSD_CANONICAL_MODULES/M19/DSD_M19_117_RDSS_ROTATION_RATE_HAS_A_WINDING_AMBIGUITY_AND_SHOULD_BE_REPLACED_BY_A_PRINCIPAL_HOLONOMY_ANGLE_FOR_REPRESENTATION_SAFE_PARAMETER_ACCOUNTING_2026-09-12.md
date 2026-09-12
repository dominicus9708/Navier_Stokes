# DSD M19-117 — RDSS rotation rate has a winding ambiguity and should be replaced by a principal holonomy angle for representation-safe parameter accounting

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION/AUDIT / EXACT GROUP-PARAMETER DICTIONARY FOR RDSS / RAW ALPHA IS NOT AN INTRINSIC DISCRETE-HOLONOMY PARAMETER BECAUSE ALPHA -> ALPHA + 2PI K/S PRODUCES THE SAME ONE-PERIOD ROTATION / USE A PRINCIPAL ANGLE BETA INSTEAD WHEN COMPARING REPRESENTATION-INVARIANT BRANCHES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RDSS holonomy

For a rotated discretely self-similar orbit with similarity period

\[
S=2\log\lambda,
\]

the one-period rotation is

\[
\boxed{
Q_*=R(\alpha S).
}
\]

The physical discrete symmetry only sees the matrix `Q_*`, not the chosen real number `alpha` separately.

---

## 2. Winding ambiguity

Because

\[
R(\vartheta+2\pi k)=R(\vartheta),
\qquad k\in\mathbb Z,
\]

we have

\[
R\left(\left(\alpha+\frac{2\pi k}{S}\right)S\right)
=R(\alpha S).
\]

Hence

\[
\boxed{
\alpha
\sim
\alpha+\frac{2\pi k}{S}.
}
\]

Different rotating-frame representations may therefore assign different angular speeds to the same discrete rotation holonomy.

This is a representation issue, not a new physical branch.

---

## 3. Principal holonomy angle

Choose the principal axis-angle representative

\[
\beta\in[-\pi,\pi]
\]

such that

\[
Q_*=R(\beta).
\]

Define the principal angular rate

\[
\boxed{
\alpha_{pr}:=\frac\beta S.
}
\]

Then

\[
\boxed{
|\alpha_{pr}|\le\frac\pi S.
}
\]

Every other representation is

\[
\alpha_k
=\alpha_{pr}+\frac{2\pi k}{S}.
\]

Thus the representation-safe intrinsic RDSS moduli are more naturally

\[
\boxed{(S,Q_*)}
\]

or, after an axis is fixed by the global rotation quotient,

\[
\boxed{(S,\beta)}.
\]

---

## 4. Rewriting the M19-116 joint floor

M19-116 gives, in the representation used by the weighted RDSS theorem,

\[
S+|\alpha|\ge c_*.
\]

For representation-invariant branch bookkeeping, choose the principal representative whenever the external estimate is valid in that gauge.

Then the floor becomes

\[
\boxed{
S+\frac{|\beta|}{S}
\ge c_*.
}
\]

This shows that a simultaneously tiny period and tiny principal holonomy angle are excluded.

It does not exclude large `S`, and it does not by itself exclude an order-one principal angle.

---

## 5. Interpretation of the large-alpha/small-period external regime

Pineau--Vicol's large-rotation RDSS argument uses a condition schematically of the form

\[
(1+\alpha^2)S\ll1
\]

in addition to large `|alpha|`.

In principal holonomy variables this reads

\[
\boxed{
S+\frac{\beta^2}{S}\ll1.
}
\]

Hence

\[
S\ll1,
\qquad
|\beta|\ll\sqrt S.
\]

So the theorem's rapid-rotation RDSS regime is still a **near-identity one-period holonomy regime**: the angular speed may be large because the period is extremely short, while the actual rotation angle per discrete scale step remains small.

This explains why the theorem does not automatically settle RDSS with an order-one holonomy angle.

---

## 6. Small-alpha regime in principal variables

If both

\[
S\ll1,
\qquad
|\alpha|\ll1,
\]

then

\[
|\beta|=|\alpha|S\ll S.
\]

Thus the small-alpha RDSS theorem also lies near the identity in the combined time/rotation group step.

Both extreme-rate RDSS theorems should therefore be interpreted as strong exclusions of particular **near-identity relative-periodic steps**, not as arbitrary-holonomy Liouville theorems.

---

## 7. New firewall

\[
\boxed{
\text{raw RDSS }\alpha
\neq
\text{intrinsic rotation holonomy}.
}
\]

When comparing different RDSS branches or estimating parameter compactness, use

\[
(S,Q_*)
\]

or principal

\[
(S,\beta),
\]

unless a theorem explicitly fixes a rotating-frame representation.

---

## 8. Updated hard core

The representation-safe unresolved RDSS class contains relative-periodic orbits for which the group-time step is not in the certified near-identity exclusion regimes.

Schematic hard variables are therefore

\[
\boxed{
S
\quad\text{and}\quad
\beta=\operatorname{Angle}(Q_*),
}
\]

with

\[
S+|\beta|/S\gtrsim1
\]

at the theorem-dependent scale of M19-116.

The next useful module should rewrite the periodic/RDSS frontier entirely in these intrinsic variables and separate small-step, finite-holonomy, and long-period escape.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
