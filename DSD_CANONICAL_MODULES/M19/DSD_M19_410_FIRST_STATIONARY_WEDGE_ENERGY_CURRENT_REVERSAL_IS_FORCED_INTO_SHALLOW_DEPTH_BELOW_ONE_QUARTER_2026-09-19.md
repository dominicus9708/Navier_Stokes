# M19-410 — The first stationary wedge energy-current reversal is forced into the shallow depth z<1/4

Date: 2026-09-19

Status: **NEW FINITE-DEPTH LOCALIZATION / M19-409 GIVES STRICTLY POSITIVE TERMINAL ENERGY CURRENT ON EVERY NONTRIVIAL BOUNDED RECURRENT STATIONARY HARD TAIL, WHILE M19-304 GIVES STRICTLY NEGATIVE DEPTH-INTEGRATED CURRENT. THEREFORE A FIRST FINITE-DEPTH CURRENT ZERO MUST OCCUR. AT THAT FIRST CROSSING, THE WEDGE ENERGY ODE AND THE EXACT DISSIPATION DECOMPOSITION OF M19-269 IMPLY THAT ANY REGULAR NONDEGENERATE CROSSING MUST LIE IN \`0<z<1/4\`. A CROSSING AT OR BEYOND \`z=1/4\` FORCES A DEGENERATE ZERO-ENERGY/ZERO-DISSIPATION STATE AND IS THEREFORE A SEPARATE NODAL/REPRESENTATION BRANCH. THUS THE STATIONARY ZERO-FORCE HARD TAIL HAS A UNIVERSALLY SHALLOW OUTWARD-TO-INWARD ENERGY-FLUX REVERSAL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal positive current

On the nontrivial stationary terminal branch, M19-409 gives

\[
\boxed{
\mathscr J(0)
=
\langle\Phi_E\rangle
>0.
}
\]

By continuity,

\[
\mathscr J(z)>0
\]

for all sufficiently small \(z>0\).

---

## 2. The depth-integrated current is negative

M19-304 gives the exact unconditioned balance

\[
\boxed{
\int_0^\infty
\mathscr J(z)\,dz
=
-\mathscr E(0)
-
\int_0^\infty
\mathscr D(z)\,dz
<0.
}
\]

Therefore \(\mathscr J\) cannot remain nonnegative.

There exists a finite depth with

\[
\mathscr J(z)<0.
\]

Define the first current reversal depth

\[
\boxed{
z_0
:=
\inf\{z>0:\mathscr J(z)\le0\}.
}
\]

Smoothness gives

\[
\boxed{
\mathscr J(z_0)=0,
\qquad
\mathscr J'(z_0)\le0.
}
\]

---

## 3. Energy derivative at the first crossing

The exact wedge energy ODE is

\[
\boxed{
\mathscr E'
+
2z\mathscr J'
+
\mathscr J
=
\mathscr D.
}
\]

At \(z=z_0\),

\[
\mathscr J(z_0)=0,
\]

so

\[
\mathscr E'(z_0)
=
\mathscr D(z_0)
-
2z_0\mathscr J'(z_0).
\]

Since

\[
\mathscr J'(z_0)\le0,
\]

we obtain

\[
\boxed{
\mathscr E'(z_0)
\ge
\mathscr D(z_0)
\ge0.
}
\]

Thus the wedge energy is nondecreasing when the radial current first changes from outward to inward.

---

## 4. Exact dissipation decomposition

M19-269 derives, for every \(z\),

\[
\boxed{
\mathscr D(z)
=
2\mathscr E(z)
+
\mathcal H(z)
+
4z\mathscr E'(z),
}
\]

where

\[
\mathcal H(z)
:=
\left\langle
\int_{S^2}
|\partial_qF-2z\partial_zF|^2
+
|\nabla_{S^2}F|^2
\,d\omega
\right\rangle_q
\ge0.
\]

At \(z_0\),

\[
\mathscr D(z_0)
\ge
2\mathscr E(z_0)
+
4z_0\mathscr E'(z_0).
\]

Using

\[
\mathscr E'(z_0)\ge\mathscr D(z_0),
\]

we obtain

\[
\mathscr D(z_0)
\ge
2\mathscr E(z_0)
+
4z_0\mathscr D(z_0).
\]

Hence

\[
\boxed{
(1-4z_0)\mathscr D(z_0)
\ge
2\mathscr E(z_0).
}
\]

---

## 5. Universal shallow-depth bound

On a regular nondegenerate crossing,

\[
\mathscr E(z_0)>0.
\]

Then the right side is strictly positive, so

\[
1-4z_0>0.
\]

Therefore

\[
\boxed{
0<z_0<\frac14.
}
\]

Moreover,

\[
\boxed{
\mathscr D(z_0)
\ge
\frac{2\mathscr E(z_0)}{1-4z_0}.
}
\]

Thus the closer the first reversal approaches \(z=1/4\), the larger the required dissipation becomes.

---

## 6. Degenerate alternative at or beyond 1/4

Suppose instead

\[
z_0\ge\frac14.
\]

Then

\[
(1-4z_0)\mathscr D(z_0)
\ge
2\mathscr E(z_0)
\]

has a nonpositive left side and nonnegative right side.

Hence necessarily

\[
\boxed{
\mathscr E(z_0)=0.
}
\]

For \(z_0>1/4\), also

\[
\boxed{
\mathscr D(z_0)=0.
}
\]

At \(z_0=1/4\), the regular nondegenerate branch still fails because \(\mathscr E(z_0)=0\).

Therefore a crossing at or beyond \(1/4\) is not an ordinary hard-tail transport event. It routes to a degenerate branch:

\[
\boxed{
G_{velocity\ nodal/zero\text{-}energy}
\lor
G_{representation/analytic\ degeneration}.
}
\]

No such branch is silently discarded.

---

## 7. Stationary zero-force implication

M19-409 applies to every nontrivial bounded recurrent stationary hard tail, including the smooth zero-force branch of M19-406--408.

Hence on the retained nondegenerate zero-force stationary branch,

\[
\boxed{
\exists z_0\in(0,1/4):
\quad
\mathscr J(z_0)=0,
\quad
\mathscr J'(z_0)\le0,
\quad
\mathscr E'(z_0)\ge\mathscr D(z_0)>0.
}
\]

The terminal outward energy supply must reverse into inward wedge transport **before** the universal depth \(z=1/4\).

---

## 8. Similarity-radius interpretation

Since

\[
z=|y|^{-2},
\]

the bound

\[
z_0<\frac14
\]

means

\[
\boxed{
|y_0|>2.
}
\]

Thus the first energy-current reversal occurs outside the normalized similarity sphere of radius \(2\).

It is therefore a terminal-to-intermediate-depth event, not a deep-center event.

---

## 9. Relation to M5-587

M5-587 independently forces a finite depth \(z_*\) where

\[
\mathscr Q_\omega(z_*)
-
\mathscr P_\omega(z_*)
=
\frac{\mathscr K_\omega(z_*)}{2z_*}
>0.
\]

M19-410 does **not** prove

\[
z_*=z_0
\]

or even \(z_*<1/4\).

It provides a new universal localization for the energy-current reversal only.

A future overlap theorem may compare the shallow energy-reversal interval with the finite-depth enstrophy-production shell.

---

## 10. Updated finite-depth target

The stationary zero-force hard branch now contains an ordered shallow transport event:

\[
\boxed{
\text{terminal outward energy flux}
\to
\text{first reversal at }z_0<1/4
\to
\text{net inward depth transport}.
}
\]

The next useful question is whether the forced enstrophy-production surplus must occur before, at, or after this reversal, and whether one ordering is incompatible with the zero-force stress law.

---

\[
\boxed{\text{M19-410 COMPLETE; THE FIRST STATIONARY ENERGY-CURRENT REVERSAL IS FORCED INTO }0<z<1/4.}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
