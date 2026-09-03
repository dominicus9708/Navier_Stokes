# DSD M5-656 — A productive carrier component forces a uniform strongly-negative kappa packet by a weighted superlevel identity

Date: 2026-09-03

Status: **INTERNAL SAME-AMPLITUDE-COMPONENT ATTRIBUTION / MULTIPLYING THE CE-H PARALLEL AMPLITUDE EQUATION BY `(rho-a)_+` ON ONE CONNECTED SUPERLEVEL COMPONENT REMOVES THE BOUNDARY TERM AND GIVES `int_C kappa rho(rho-a) = -int_C|nabla rho|^2 - int_C rho(rho-a)|nabla xi|^2`; THE M5-590 PRODUCTIVE PERSISTENT CARRIER CONTAINS A FIXED-AMPLITUDE BALL, SO A FIXED SUPERLEVEL COMPONENT CONTAINING THAT CARRIER HAS A UNIFORM CAPACITY/DIRICHLET FLOOR; THE WEIGHTED KAPPA MEAN ON THAT SAME COMPONENT IS THEREFORE UNIFORMLY NEGATIVE, AND THE GLOBAL `E,H` CAPS EXTRACT A FIXED HIGH-AMPLITUDE STRONGLY-NEGATIVE KAPPA PACKET INSIDE THAT VERY COMPONENT / CROSS-SHEET OUTSOURCING IS THUS FORCED TO OCCUR THROUGH PATCHING INSIDE ONE CONNECTED HIGH-AMPLITUDE REGION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Productive persistent carrier has a fixed amplitude core

M5-590 gives one fixed persistent lineage `L_alpha` paying a positive local production share

\[
Q_\alpha^{ann}\ge q_{pay}>0
\]

on positive-frequency finite-depth production windows.

On the fixed core,

\[
|\Sigma|\le S_*<\infty.
\]

Hence on every such event

\[
\int_{C_\alpha}\rho^2dy
\ge
\frac{q_{pay}}{S_*}
=:e_{pay}>0
\]

after absorbing the fixed cutoff constants.

Because the carrier has uniformly bounded volume and the compact hard hull has a uniform `C^1` cap on `W`, there exist fixed constants

\[
\boxed{
\rho_c>0,
\qquad
r_c>0
}
\]

and a point `y_c` in the productive carrier such that

\[
\boxed{
\rho(y)\ge\rho_c
\quad\text{on }B_{r_c}(y_c).
}
\]

---

## 2. Choose one fixed superlevel threshold

Set

\[
\boxed{
a_*:=\frac14\rho_c.}
\]

Let `C_*` be the connected component of

\[
\{\rho>a_*\}
\]

that contains `B_{r_c}(y_c)`.

Since `rho -> 0` at spatial infinity, `C_*` is bounded.

The ball actually satisfies

\[
\rho-a_*
\ge
\frac34\rho_c
\]

there.

---

## 3. Componentwise weighted amplitude identity

The CE-H parallel equation is

\[
\Delta\rho
=
(\kappa+|\nabla\xi|^2)\rho.
\]

On `C_*`, multiply by

\[
\rho-a_*.
\]

Because `rho=a_*` on the regular boundary of the superlevel component, the multiplier vanishes on the boundary.

Integration by parts gives

\[
\int_{C_*}(\rho-a_*)\Delta\rho
=-\int_{C_*}|\nabla\rho|^2.
\]

Therefore

\[
\boxed{
\int_{C_*}
\kappa\rho(\rho-a_*)dy
=
-
\int_{C_*}|\nabla\rho|^2dy
-
\int_{C_*}
\rho(\rho-a_*)|\nabla\xi|^2dy.
}
\]

This is stronger than the unweighted M5-651 component identity because it directly contains the magnitude Dirichlet energy and has no boundary term.

For nonregular thresholds one may approximate `a_*` by nearby regular values and pass to the limit; the proof only uses one threshold in a fixed compact interval.

---

## 4. Uniform componentwise Dirichlet floor

Let

\[
f:=(\rho-a_*)_+
\]

restricted to the connected component `C_*` and extended by zero outside.

Then

\[
f\in H_0^1(C_*),
\]

and on `B_{r_c}(y_c)`,

\[
f\ge\frac34\rho_c.
\]

The whole-space Sobolev inequality gives

\[
\|f\|_6
\le C_S\|\nabla f\|_2.
\]

Therefore

\[
\|\nabla f\|_2^2
\ge
C_S^{-2}
\left(
\frac34\rho_c
\right)^2
|B_{r_c}|^{1/3}
=:d_*>0.
\]

Since `nabla f=nabla rho` on `C_*`,

\[
\boxed{
\int_{C_*}|\nabla\rho|^2dy
\ge d_*>0.
}
\]

Thus the weighted component identity yields

\[
\boxed{
\int_{C_*}
\kappa\,w_*\,dy
\le-d_*,
\qquad
w_*:=\rho(\rho-a_*)>0.
}
\]

---

## 5. Extract a fixed strongly-negative kappa subset

On `C_*`,

\[
0<w_*\le\rho^2.
\]

Hence

\[
\int_{C_*}w_*dy
\le E\le Z_*.
\]

Also

\[
\int_{C_*}\kappa^2w_*dy
\le
\int\kappa^2\rho^2dy
=H
\le H_*.
\]

Set

\[
\boxed{
\kappa_c:=\frac{d_*}{2Z_*}>0.
}
\]

The portion with

\[
-\kappa_c<\kappa<\infty
\]

can contribute at most `kappa_c Z_*=d_*/2` to the negative magnitude.

Therefore the set

\[
A_c:=\{y\in C_*:\kappa\le-\kappa_c\}
\]

must satisfy

\[
\int_{A_c}(-\kappa)w_*dy
\ge\frac12d_*.
\]

By Cauchy--Schwarz,

\[
\frac12d_*
\le
\left(
\int_{A_c}\kappa^2w_*dy
\right)^{1/2}
\left(
\int_{A_c}w_*dy
\right)^{1/2}.
\]

Hence

\[
\boxed{
\int_{A_c}w_*dy
\ge
\frac{d_*^2}{4H_*}
=:m_c>0.
}
\]

Since `rho>a_*` throughout `C_*`, this is a fixed high-amplitude negative-multiplier population in the **same connected amplitude component as the productive persistent carrier**.

---

## 6. Coherent negative packet extraction

The component `C_*` lies in a uniformly bounded finite core for the productive event under consideration; if necessary intersect with the fixed core carrying all but an arbitrarily small enstrophy tail, which cannot absorb the fixed weighted mass `m_c`.

Finite volume and the fixed weighted mass give a point with

\[
\rho\ge a_*,
\qquad
\kappa\le-\kappa_c.
\]

On `rho>=a_*`, `kappa=(W\cdot\Delta W)/|W|^2` is smooth with uniform derivative bounds inherited from the all-order compact hull.

Therefore the point thickens to a fixed-radius subpacket on which, after reducing constants,

\[
\boxed{
\rho\ge\frac12a_*,
\qquad
\kappa\le-\frac12\kappa_c.
}
\]

A coherent subdisk carries fixed directed vorticity flux

\[
\boxed{\Phi_c\ge\phi_c>0.}
\]

---

## 7. Same-component bridge

We have proved, on every retained productive event of `L_alpha`,

\[
\boxed{
\text{productive persistent carrier}
\subset C_*
\supset
\text{fixed strongly-negative coherent kappa packet}.
}
\]

Because `C_*` is connected, there exists a path

\[
\Gamma\subset C_*
\]

from the productive carrier to the negative packet along which

\[
\rho>a_*.
\]

Thus the quotient variable `kappa` and the generalized force are nonsingular along the entire path.

---

## 8. Consequence for the M5-655 cross-sheet payer branch

The negative payer can no longer be outsourced to a completely disconnected low-amplitude or remote region.

If the path `Gamma` is covered by one common relabeling-law family, then the same-family flux-consumption machinery of M5-648--649 becomes available once the relative ordering condition is met.

If the productive reference and negative payer belong to different relabeling sheets, the sheet transition must occur **inside one connected high-amplitude component**.

Therefore the remaining outsourcing branch is sharpened to

\[
\boxed{
R_{cross-sheet\ payer}
\Longrightarrow
T_{high-amplitude\ sheet-patching}
}

inside `rho>a_*`.

This removes remote/near-zero patching as the only possible explanation for the payer separation.

---

## 9. Relation to M5-654

Along `Gamma`, `rho>=a_*>0`.

Hence the generalized force

\[
F=\rho^2\nabla\kappa
\]

faithfully represents the quotient geometry without nodal degeneracy.

A change between local scalar relabeling branches along this high-amplitude path must therefore be represented through one of:

1. nonzero cross-level force rotation
\[
F\times(D_BF+L^TF)\ne0;
\]
2. an active critical point `F=0` with force creation `D_BF!=0`;
3. a genuine disconnected-level global monodromy/patching event with both local differential defects zero.

Thus M5-654 now applies in a fixed high-amplitude region rather than only abstractly on the quotient.

---

## 10. Firewall

This note does **not** yet prove that the productive reference and the extracted negative packet satisfy one common scalar ODE.

Connectedness of the amplitude superlevel is not connectedness of a `kappa` level surface.

Therefore M5-648--649 cannot yet be invoked automatically.

The valid gain is the fixed high-amplitude spatial bridge and the forced existence of a strongly-negative payer inside it.

---

## 11. Updated highest-value target

The cross-sheet payer problem is reduced to:

\[
\boxed{
\text{Can one connected high-amplitude CE-H component repeatedly connect a persistent productive reference sheet to a strongly-negative payer sheet without a fixed generalized-force rotation/creation or topological patching cost?}
}
\]

This is the next calculation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]