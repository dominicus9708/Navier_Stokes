# First-hitting blow-up scaling gives an ancient horizon automatically, but not a Liouville closure

Date: 2026-08-13

Status: **DERIVED ANCIENT-HORIZON FACT + LITERATURE-ANCHORED CLAIM BOUNDARY / ANCIENT LIOUVILLE CLOSURE OPEN**.

This note corrects two possible overstatements in the compactness route.

1. A noncollapsing sequence of adjacent amplification windows is **not needed** merely to obtain an arbitrarily long backward normalized time horizon.
2. A bounded nontrivial ancient 3D Navier--Stokes limit is **not by itself contradictory**.  General three-dimensional bounded-ancient Liouville rigidity is not available without extra hypotheses.

---

## 1. First-hitting blow-up sequence

Let

\[
W_j=\|\omega(t_j)\|_\infty\to\infty
\]

and choose each `t_j` as the first hitting time of the level `W_j`.
Assume a hypothetical finite singular time

\[
0<T^*<\infty,
\qquad
t_j\uparrow T^*.
\]

Use the vorticity-natural scaling

\[
r_j=W_j^{-1/2},
\]

\[
y=\frac{x-x_j}{r_j},
\qquad
s=W_j(t-t_j),
\]

\[
U_j(y,s)=r_j u(x_j+r_jy,t_j+r_j^2s),
\]

\[
\Omega_j(y,s)=r_j^2\omega(x_j+r_jy,t_j+r_j^2s).
\]

Because `t_j` is a first hitting time,

\[
\boxed{
\|\Omega_j(s)\|_\infty\le1
\qquad
-W_jt_j\le s\le0.
}
\]

At the selected maximum point,

\[
|\Omega_j(0,0)|=1.
\]

---

## 2. The backward normalized horizon diverges without using adjacent-window noncollapse

The physical initial time `t=0` becomes

\[
\boxed{s=-W_jt_j.}
\]

Since

\[
t_j\to T^*>0
\]

and

\[
W_j\to\infty,
\]

we have immediately

\[
\boxed{W_jt_j\to\infty.}
\]

Therefore for every fixed `S>0`, all sufficiently large `j` are defined on

\[
[-S,0].
\]

Hence a local compactness theorem uniform on every fixed backward cylinder can be diagonalized to produce a candidate ancient limit on

\[
\boxed{\mathbb R^3\times(-\infty,0].}
\]

This fact does **not** require the previously derived lower bound on each adjacent dimensionless duration

\[
\sigma_k=W_k(t_{k+1}-t_k).
\]

The `sigma` noncollapse result remains useful for comparing consecutive amplification windows and for preventing a single-step temporal concentration escape, but it is not logically needed for the existence of a long blow-up-scaled past horizon.

---

## 3. What first-hitting gives for free

The ancient candidate inherits, locally and before any affine-frame issue,

\[
\boxed{\|\Omega_\infty\|_\infty\le1}
\]

in the vorticity variable, provided strong enough local compactness is available.

The terminal normalization/thick-core mechanism can preserve nontriviality, schematically

\[
\boxed{|\Omega_\infty(0,0)|=1}
\]

or a robust local `L2` substitute.

Thus the blow-up route naturally aims at a **nontrivial ancient bounded-vorticity profile**.

---

## 4. This is not yet a contradiction in three dimensions

Koch--Nadirashvili--Seregin--Sverak, *Liouville theorems for the Navier--Stokes equations and applications*, Acta Mathematica 203 (2009), study bounded ancient solutions and explicitly identify the unrestricted three-dimensional Liouville problem as out of reach, while proving two-dimensional and axisymmetric partial results.

Albritton--Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, Journal of Mathematical Fluid Mechanics 21 (2019), prove stronger ancient rigidity under additional critical assumptions; in particular their abstract records a Liouville theorem for ancient solutions whose `L3` norm is bounded along a backward sequence of times.

Therefore the implication

\[
\boxed{
\text{bounded nontrivial ancient 3D solution}
\Longrightarrow\bot
}
\]

is **not available**.

The present project must first derive an additional hypothesis matching a valid Liouville theorem or prove a new rigidity statement.

---

## 5. Existing DSD `L3` bridge does not automatically supply the required global ancient hypothesis

The material-oscillation bridge controls a **local, mean-centered** critical cubic quantity,

\[
\int_{\Omega_s}|u-\bar U|^3dx,
\]

under local oscillation/dissipation/deformation assumptions.

This is useful for one-scale epsilon regularity, but it is not the same as a uniform whole-space bound

\[
\boxed{
\|U(s_k)\|_{L^3(\mathbb R^3)}\le C
}
\]

along a backward sequence, which is the kind of condition appearing in the Albritton--Barker Liouville result.

Thus no global `L3` Liouville closure may be inferred from the existing local cubic gate.

---

## 6. Affine-background issue makes the ancient limit still more delicate

The local DSD compression writes

\[
U(y,s)=L(s)y+v(y,s).
\]

When the affine deformation condition number is uniformly bounded, the transformation

\[
y=F(s)z,
\qquad
F'=LF,
\]

produces a uniformly parabolic local equation with time-dependent anisotropic diffusion

\[
A(s)=F^{-1}F^{-T}.
\]

This is excellent for local compactness, but the transformed limiting equation is not literally the standard isotropic Navier--Stokes system unless the affine background also converges in a compatible way.

Conversely, staying in the original coordinates preserves standard Navier--Stokes but leaves the affine drift/stretching coefficients visible.

Therefore a standard ancient-Navier--Stokes Liouville theorem cannot be imported after affine removal without checking the limiting equation.

---

## 7. Correct ancient-limit fork

The ancient route should be typed as follows.

### A. Standard-frame compact ancient branch

Obtain local compactness without losing the standard Navier--Stokes form and derive an extra valid critical/decay condition, such as a theorem-compatible global `L3` bound along backward times.

Then an existing Liouville theorem may close the branch.

### B. Affine-frame compact ancient branch

Obtain an ancient limit for

\[
\partial_sW+\widetilde v\cdot\nabla W
=W\cdot\nabla\widetilde v
+\nu\nabla\cdot(A(s)\nabla W).
\]

This requires a Liouville/rigidity theorem for the time-dependent uniformly elliptic affine-frame system, or a further argument reducing it back to standard Navier--Stokes.

### C. Noncompact deformation branch

If the affine/material/residual deformation factors lose compactness, return to the deformation ledger

\[
H=FG
\]

rather than claiming an ancient limit.

---

## 8. Updated role of amplification-time noncollapse

The lower bound

\[
\sigma_j\ge\sigma_*>0
\]

on bounded-channel consecutive amplification steps remains valuable because it says a fixed amplification cannot occur in vanishing natural time without a normalized cost blowing up.

Its role is therefore

\[
\boxed{
\text{one-step temporal rigidity},
}
\]

not

\[
\boxed{
\text{existence of the ancient backward horizon}.
}
\]

The latter follows directly from first-hitting blow-up scaling.

---

## 9. Current proof target

The ancient route becomes proof-producing only after establishing one of:

1. a theorem-compatible critical norm/decay condition for the standard-frame ancient limit;
2. a new Liouville theorem for the affine-frame uniformly parabolic limit;
3. or a contradiction before taking the ancient limit, using the local source/deformation/projective channels.

For now, option 3 remains the safer primary route.

Status: **ANCIENT HORIZON AUTOMATIC / GENERAL 3D ANCIENT LIOUVILLE NOT AVAILABLE / EXTRA RIGIDITY CONDITION STILL REQUIRED**.
