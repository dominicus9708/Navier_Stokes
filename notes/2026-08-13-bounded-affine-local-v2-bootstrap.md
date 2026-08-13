# Bounded affine-background strain gives a local terminal `H1/V2` bootstrap without global normalized enstrophy

Date: 2026-08-13

Status: **DERIVED NESTED-CUTOFF LOCAL DERIVATIVE BOOTSTRAP / AFFINE-STRAIN `L1_t` CONTROL**.

The first-hitting normalization gives a global amplitude cap `||Omega||_infinity<=1`.  This alone bounds vorticity on every fixed normalized ball, even when global normalized enstrophy is large.  The remaining nonlocal influence of distant/intermediate scales is split into a common affine velocity gradient plus a small spatial-difference remainder.

The present lemma shows that if the **symmetric affine strain** has bounded time integral, then a terminal local `H1` bound and a local spacetime `V2` bound follow on nested fixed balls.  No global normalized-enstrophy bound is required.

---

## 1. First-hitting local block

Work on a normalized backward interval

\[
I=[-2\delta,0],
\qquad
\delta>0,
\]

with

\[
\boxed{\|\Omega(s)\|_{L^\infty(\mathbb R^3)}\le1.}
\]

Fix nested balls

\[
B_{R_0}\Subset B_{R_1}\Subset B_{R_2}
\]

with fixed positive gaps between radii.

Then automatically

\[
\|\Omega(s)\|_{L^p(B_{R_2})}
\le |B_{R_2}|^{1/p}
\]

for every finite `p>=1`.

---

## 2. Local velocity-gradient decomposition

After subtracting a spatially constant translation, write on `B_R2`

\[
\boxed{
U(y,s)=L(s)y+v(y,s),
\qquad
\nabla U=L(s)+\nabla v.
}
\]

Here `L(s)` is the common affine gradient supplied by the remote/intermediate field at the tracked center, while `v` contains

1. the local/near Biot--Savart contribution;
2. the non-affine remote difference;
3. harmless cutoff/frame remainders.

Decompose

\[
\boxed{
L=A_0+S_0,
\qquad
A_0^T=-A_0,
\qquad
S_0^T=S_0,
\qquad
\operatorname{tr}S_0=0.
}
\]

The antisymmetric `A0` is a common rigid rotation.  Use an orthogonal time-dependent frame to remove it.  Orthogonal rotation preserves the isotropic Laplacian and all Euclidean `L2/H1` norms.

Hence below one may assume, after this frame change,

\[
L=S_0.
\]

Define the affine-strain accumulation

\[
\boxed{
K_S
=\int_{-2\delta}^{0}|S_0(s)|\,ds.
}
\]

Assume

\[
\boxed{K_S\le K<\infty.}
\]

---

## 3. Residual local coefficient bounds

Choose one fixed `p>3`.  The near-field singular-integral relation and the amplitude cap give, on the buffered ball, a bound of the form

\[
\boxed{
\|\nabla v(s)\|_{L^p(B_{R_1})}
\le M_{p,R_1,R_2}
}
\]

uniformly in the amplification index, after the far non-affine remainder has been made small by the chosen buffer.

Poincare--Morrey, after subtracting the local mean of `v`, gives

\[
\boxed{
\|v(s)\|_{L^\infty(B_{R_1})}
\le M_{v}.
}
\]

When one spatial derivative of `grad v` is needed after a good `H1` slice has been found, local Calderon--Zygmund on nested balls gives schematically

\[
\boxed{
\|\nabla^2v\|_{L^2(B_{R_0})}
\le
C\left(
\|\nabla\Omega\|_{L^2(B_{R_1})}+1
\right),
}
\]

with the constant absorbing fixed cutoff and remote-difference errors.

These are standard nested-ball singular-integral estimates; no global `L2` vorticity norm enters.

---

## 4. Local enstrophy gives a good `H1` time slice

Let `chi1` be one on `B_R1` and supported in `B_R2`.  Define

\[
E_1(s)=\int\chi_1^2|\Omega|^2,
\qquad
P_1(s)=\int\chi_1^2|\nabla\Omega|^2.
\]

The localized vorticity-enstrophy identity has the schematic form

\[
\frac12E_1'(s)+\nu P_1(s)
\le
C_0
+C_1|S_0(s)|.
\]

Reason:

- `|Omega|<=1` bounds all fixed-volume lower-order terms;
- the residual local strain/source is bounded in finite `Lp`;
- the affine source `Omega.S0.Omega` is bounded by `|S0| E1`;
- affine transport through the cutoff is bounded by `C |S0|` because `|y|` is fixed on the support;
- the rigid-rotation part has already been removed.

Since `E1(s)<=|B_R2|`, integrate over `[-2delta,-delta]`:

\[
\boxed{
\nu\int_{-2\delta}^{-\delta}P_1(s)ds
\le
C(R_2,\delta,K,\nu,M_v).
}
\]

Therefore there exists

\[
s_0\in[-2\delta,-\delta]
\]

such that

\[
\boxed{
P_1(s_0)
\le C_{\rm good}(R_2,\delta,K,\nu,M_v).
}
\]

---

## 5. Affine terms are linear in `|S0| P`, not quadratic

This is the key point.

For the affine advection field

\[
b(y,s)=S_0(s)y,
\qquad\nabla\cdot b=0,
\]

the derivative-energy contribution satisfies, after integration by parts,

\[
\left|
\int
(b\cdot\nabla\Omega)(-\Delta\Omega)
\right|
\le
C|S_0(s)|\,P.
\]

One does **not** estimate it by

\[
\|b\|_\infty P^{1/2}Z^{1/2},
\]

which would unnecessarily produce `|S0|^2` after Young's inequality.

Likewise, because `S0` is spatially constant,

\[
\left|
\int
(S_0\Omega)\cdot(-\Delta\Omega)
\right|
=
\left|
\int
S_0\nabla\Omega:\nabla\Omega
\right|
\le
C|S_0(s)|P.
\]

Thus only the **time integral** of `|S0|` is needed.

---

## 6. Local derivative-energy inequality

Let `chi0` be one on `B_R0` and supported in `B_R1`.  Define

\[
P_0(s)=\int\chi_0^2|\nabla\Omega|^2,
\]

\[
Z_0(s)=\int\chi_0^2|\Delta\Omega|^2.
\]

Multiply the vorticity equation by `-chi0^2 Delta Omega` and use nested-cutoff integration by parts.

For the residual advection term,

\[
\int |\nabla v||\nabla\Omega|^2
\le
\|\nabla v\|_3
\|\nabla\Omega\|_3^2.
\]

Interpolate

\[
\|\nabla\Omega\|_3^2
\le
C P_1^{1/2}Z_1^{1/2},
\]

so Young gives

\[
\le
\frac\nu8Z_1
+C_{\nu,M}P_1.
\]

For residual stretching, differentiation produces terms involving

\[
\nabla v\,\nabla\Omega
\]

and

\[
\Omega\,\nabla^2v.
\]

The first is estimated as above; the second uses `|Omega|<=1` and the buffered Calderon--Zygmund estimate

\[
\|\nabla^2v\|_2
\lesssim P_1^{1/2}+1.
\]

All cutoff terms are bounded by fixed multiples of `1+P1+|S0|P1` on the nested buffer.

After absorbing the `Z` fractions, one obtains

\[
\boxed{
P_0'(s)
+\frac\nu2 Z_0(s)
\le
C_2
+
C_3\,[1+|S_0(s)|]\,P_1(s).
}
\]

Using a standard finite nested-cutoff iteration (or choosing a slightly larger derivative-energy functional covering `B_R1`) yields the closed comparison form

\[
\boxed{
\mathcal P'(s)
+c_\nu\mathcal Z(s)
\le
C
+[C+ C|S_0(s)|]\mathcal P(s),
}
\]

for a derivative-energy functional `mathcal P` that controls `P0` and is controlled by the chosen buffered `H1` norm.

---

## 7. Gronwall with `L1_t` affine strain

Start at the good slice `s0`.  Since

\[
\int_{s_0}^{0}|S_0(s)|ds\le K,
\]

Gronwall gives

\[
\boxed{
\sup_{-\delta\le s\le0}
\|\nabla\Omega(s)\|_{L^2(B_{R_0})}^2
\le
C(R_i,\delta,K,\nu).
}
\]

Integrating the same inequality gives

\[
\boxed{
\int_{-\delta}^{0}
\|\Delta\Omega(s)\|_{L^2(B_{R_0})}^2ds
\le
C(R_i,\delta,K,\nu).
}
\]

Thus the terminal local V2 reserve follows from

\[
\boxed{
\|\Omega\|_\infty\le1
\quad+\quad
\int|S_0|dt\le K
}
\]

plus the fixed-buffer local singular-integral bounds.

---

## 8. Local strong compactness

On a still smaller cylinder, the V2 reserve gives

\[
\Omega_j\text{ bounded in }L_s^2H_y^2.
\]

The vorticity equation and bounded local drift/strain coefficients give a time-derivative bound in a negative Sobolev space.  Therefore Aubin--Lions--Simon yields

\[
\boxed{
\Omega_j\to\Omega_\infty
\quad\text{strongly in }L_s^2H_{y,\rm loc}^1.
}
\]

This compactness is entirely local to the tracked route.  Distant vorticity mass enters only through the bounded common affine strain and the small difference remainder.

---

## 9. Refined proof dichotomy

The main compactness split is now

\[
\boxed{
\mathcal K_S
=\int|S_0(s)|ds\to\infty
}
\]

or

\[
\boxed{
\mathcal K_S\le K
\Longrightarrow
\text{terminal local }H^1/V2\text{ bounds and strong compactness}.
}
\]

Thus global normalized enstrophy is not a necessary local compactness assumption.

The unbounded branch is a genuine **affine-strain cascade** from the shrinking mesoscopic interaction neighborhood into the tracked core.

---

## 10. Claim boundary

The lemma uses a fixed-buffer near/far decomposition and standard local singular-integral/nested-cutoff estimates.  It does not claim that `K_S` is automatically bounded along an arbitrary hypothetical blowup sequence.

Nor does local compactness by itself prove regularity; it supplies the compact branch on which the source-rigidity gaps can be applied.

Status: **LOCAL V2/COMPACTNESS CLOSED ON THE BOUNDED-AFFINE FIRST-HITTING BRANCH / AFFINE-STRAIN CASCADE REMAINS**.
