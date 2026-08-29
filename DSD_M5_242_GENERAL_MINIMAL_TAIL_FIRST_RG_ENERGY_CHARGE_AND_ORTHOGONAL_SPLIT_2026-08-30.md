# DSD M5-242 — General Minimal-Tail First RG Energy Charge and Orthogonal Split

Date: 2026-08-30

Parent: `DSD_M5_241_LINEAR_BACKWARD_RG_APERIODIC_MINIMAL_ANTIMODEL_FIREWALL_2026-08-30.md`

Status: **GENERALIZATION OF THE PERIODIC SECOND-TAIL CHARGE / THE FIRST RG RESIDUAL PRODUCES AN `R^{-1}` RENORMALIZED SHELL-ENERGY CORRECTION FOR EACH PHASE STATE OF A GENERAL COMPACT MINIMAL TAIL HULL / THE CHARGE IS A CONTINUOUS SCALAR OBSERVABLE BUT HAS NO UNIVERSAL SIGN / THE RESIDUAL-ACTIVE HULL SPLITS INTO AN ENERGY-VISIBLE SUBBRANCH OR A RESIDUAL THAT IS EVERYWHERE ORTHOGONAL TO THE LEADING TAIL AT FIRST ORDER / STRICT LYAPUNOV MONOTONICITY IS NOT OBTAINED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from the exact RG correction

M5-237 gives, on every fixed punctured cell,

\[
\boxed{
\mathscr R_\rho(T)
=T-\rho F_T+o(\rho),
\qquad
\rho=R^{-2}.
}
\]

Here

\[
F_T
=\nu\Delta T
-\mathbb P\nabla\cdot(T\otimes T).
\]

This statement does not require periodicity.

---

## 2. Fixed-cell normalized fields

On a unit annular/log cell `C`, write the leading critical profile as

\[
F_T^{cell}.
\]

The first descendant correction is

\[
-\rho\,\mathcal N[F_T^{cell}],
\]

where `mathcal N` denotes the fixed-cell representative of the projected stationary residual.

Define the first RG energy charge

\[
\boxed{
\mathfrak A(T)
:=
\left\langle
F_T^{cell},
\mathcal N[F_T^{cell}]
\right\rangle_{H^1,H^{-1}}.
}
\]

Equivalently, suppressing the cell normalization notation,

\[
\boxed{
\mathfrak A(T)
=\langle T,F_T\rangle_{cell}.
}
\]

This is the same scalar that appeared on the periodic second-tail branch, now evaluated phase by phase on the general tail hull.

---

## 3. First shell-energy correction

Let

\[
U_R(Y)
\]

be the actual W1 field on a radius-`R` normalized annulus and `T_R` its canonical-tail leading term at the corresponding ancestor phase.

The RG asymptotic gives on the fixed rescaled cell

\[
R(U_R-T_R)
=
-R^{-2}\mathcal N[F_T^{cell}]
+o(R^{-2}).
\]

Therefore the cross term is

\[
\left\langle
F_T^{cell},
R(U_R-T_R)
\right\rangle
=
-R^{-2}\mathfrak A(T)
+o(R^{-2}).
\]

After restoring physical annulus volume, exactly as in the previous periodic calculation,

\[
\boxed{
\int_{C_R}
\bigl(|U_R|^2-|T_R|^2\bigr)dY
=
-\frac{2\mathfrak A(T)}{R}
+o(R^{-1}).
}
\]

The only change from the periodic formula is that `mathfrak A(T)` now depends on the current point of the compact tail hull.

---

## 4. Continuity of the charge

The tail map is compact in local punctured topology and the residual is continuous in local `H^-1` under the retained derivative compactness.

Therefore

\[
\boxed{
\mathfrak A:\mathcal T\to\mathbb R
\text{ is continuous}.
}
\]

Along tail dilation, `A` becomes a continuous recurrent scalar observable on the minimal hull.

No sign is implied by continuity or minimality.

---

## 5. Why the charge is not a Lyapunov functional

For finite-energy whole-space velocity fields one would have, formally,

\[
\langle U,
\nu\Delta U-\mathbb P\nabla\cdot(U\otimes U)angle
=-\nu\|\nabla U\|_2^2.
\]

The critical tail is not in global `L2`; cell renormalization leaves radial/pressure/scale-transfer boundary terms.

The earlier periodic audit already showed that these terms destroy a universal sign for `mathfrak A`.

M5-237 gives the dynamical explanation: `mathfrak A` is the cross energy between the tail boundary data and the first **backward-RG** correction.

Thus

\[
\boxed{
\mathfrak A(T)
\text{ need not be nonpositive or nonnegative.}
}
\]

Therefore the route

\[
\text{renormalized energy}
\Rightarrow
\text{strict Lyapunov on }\mathcal T
\]

remains RED.

---

## 6. Energy-visible residual branch

Suppose

\[
\mathfrak A
\not\equiv0
\quad\text{on }\mathcal T.
\]

Then there is some tail state `T0` with

\[
|\mathfrak A(T_0)|>0.
\]

By continuity, an open neighborhood has

\[
|\mathfrak A(T)|\ge a_*>0.
\]

Minimality makes returns to this open set syndetic/topologically recurrent; under an invariant ergodic measure one obtains a positive-density visit set.

Hence the residual-active branch contains a positive-density family of cells with a fixed nonzero `R^-1` renormalized-energy coefficient:

\[
\boxed{
|\Delta E_{ren}(C_R)|
\ge
\frac{2a_*}{R}
+o(R^{-1}).
}
\]

This is an **energy-visible residual**.

Its sign may alternate between different recurrent regions, so no monotonicity is inferred.

---

## 7. First-order energy-orthogonal branch

The only way to avoid all first-order renormalized-energy visibility is

\[
\boxed{
\mathfrak A(T)=0
\quad\forall T\in\mathcal T.
}
\]

On the `R-gap` branch of M5-238 we simultaneously have

\[
\mathbf F(T)\ge\varepsilon_{glob}>0.
\]

Thus the residual is nonzero but first-order energy orthogonal to the leading tail:

\[
\boxed{
F_T\ne0,
\qquad
\langle T,F_T\rangle_{cell}=0
\quad\forall T\in\mathcal T.
}
\]

This is a genuine **transverse RG branch**.

It is analogous in kinematic spirit to a flow moving along a constant-energy surface, although no actual isometric dynamics is asserted.

---

## 8. Second-order coefficient in the orthogonal branch

From M5-240,

\[
\mathscr R_\rho
=
T-\rho F_T
+\frac12\rho^2D\mathcal F_T[F_T]
+O_{formal}(\rho^3).
\]

Therefore

\[
\begin{aligned}
\|\mathscr R_\rho\|^2-
\|T\|^2
&=
-2\rho\langle T,F_T\rangle\\
&\quad+
\rho^2
\left(
\|F_T\|^2
+
\langle T,D\mathcal F_T[F_T]\rangle
\right)
+O_{formal}(\rho^3).
\end{aligned}
\]

If `A(T)=0`, the next scalar charge is therefore

\[
\boxed{
\mathfrak A_2(T)
:=
\|F_T\|^2
+
\langle T,D\mathcal F_T[F_T]\rangle.
}
\]

No sign is claimed for `A2` either.

This defines a possible hierarchy of renormalized-energy visibility charges, but the hierarchy is not yet a Lyapunov hierarchy.

---

## 9. DSD verdict

The residual-active branch now splits into

\[
\boxed{
R_{gap}
\Longrightarrow
R_{E1}
\lor
R_{\perp1},
}
\]

where

\[
R_{E1}:
\mathfrak A\not\equiv0
\text{ and first RG correction is energy-visible},
\]

and

\[
R_{\perp1}:
F_T\ne0
\text{ but }
\langle T,F_T\rangle=0
\text{ throughout the hull}.
\]

### Important limitation

Neither branch is presently contradictory because the `R^-1` shell corrections are geometrically summable and the charge has no fixed sign.

---

## 10. Next target

The transverse branch is more rigid and therefore higher leverage.

Audit whether

\[
\langle T,F_T\rangle=0
\quad\forall T\in\mathcal T
\]

combined with the exact scale covariance of `F_T` forces the residual to lie in a rotational/projective tangent direction, or whether a genuinely shape-changing energy-orthogonal residual anti-model exists.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]