# Dynamic first-hitting scale and frozen-profile gate

Date: 2026-08-19

Status: **DERIVED DYNAMIC RESCALING + CONDITIONAL COMPACTNESS/LIOUVILLE GATE + GLOBAL REGULARITY NOT PROVED**.

This note separates the previously implicit assumption of repeated O(1) projective reorganization from the distinct possibility of a nearly shape-frozen blow-up profile.

---

## 1. Dynamic vorticity-max normalization

Let

\[
W(t)=\|\omega(t)\|_\infty,
\qquad
\lambda(t)=W(t)^{1/2}.
\]

Choose a center `X(t)` and define

\[
y=\lambda(t)(x-X(t)),
\qquad
\frac{ds}{dt}=\lambda(t)^2=W(t),
\]

\[
U(y,s)=\lambda(t)^{-1}u(x,t),
\qquad
\Omega(y,s)=\lambda(t)^{-2}\omega(x,t)=\frac{\omega(x,t)}{W(t)}.
\]

Then

\[
\|\Omega(s)\|_\infty=1.
\]

Define the dimensionless scale-rate and center drift

\[
\boxed{
a(s)=\frac{\lambda'}{\lambda^3}=\frac{W'}{2W^2},
\qquad
c(s)=\frac{X'}{\lambda}.}
\]

The rescaled velocity equation is

\[
\boxed{
\partial_sU
+a(U+y\cdot\nabla U)
+(U-c)\cdot\nabla U
=-\nabla P+\nu\Delta U,
\qquad
\nabla\cdot U=0.
}
\]

The rescaled vorticity equation is

\[
\boxed{
\partial_s\Omega
=S_U\Omega-(U-c)\cdot\nabla\Omega+\nu\Delta\Omega
-a(2\Omega+y\cdot\nabla\Omega).
}
\]

These identities are exact wherever `W(t)` is differentiable.

---

## 2. Exact scale-growth ledger

Since

\[
\frac{d}{ds}\log W
=\frac{W'}{W^2}=2a,
\]

any stage during which `W` grows from `W_j` to `q W_j`, with fixed `q>1`, satisfies

\[
\boxed{
\int_{I_j}a(s)\,ds
=\frac12\log q.}
\]

Thus the scale-rate action per geometric first-hitting step is exactly fixed.

If `L_j=|I_j|` denotes the rescaled-time length and

\[
\bar a_j=\frac1{L_j}\int_{I_j}a(s)ds,
\]

then

\[
\boxed{
L_j=\frac{\frac12\log q}{\bar a_j}.}
\]

---

## 3. Maximum-point scale-rate gate

The normalized vorticity magnitude `R=|Omega|` obeys

\[
\partial_sR+(U-c+a y)\cdot\nabla R-\nu\Delta R
=R\left(\gamma-\nu|\nabla\xi|^2-2a\right),
\]

where `xi=Omega/|Omega|` and `gamma=xi^T S_U xi`.

At a differentiable tracked point where `R=1` attains its spatial maximum,

\[
\nabla R=0,
\qquad
\Delta R\le0,
\]

and the normalization keeps the maximum equal to one. Therefore

\[
\boxed{
2a
\le
\gamma-\nu|\nabla\xi|^2
\le
\gamma.
}
\]

Thus rapid scale growth is not a kinematic free parameter; it must be supported by local stretching at the normalized maximum.

---

## 4. Global energy-dissipation packing in dynamic variables

The normalized enstrophy is

\[
E_\Omega(s)=\|\Omega(s)\|_2^2.
\]

Scaling gives

\[
\boxed{
E_\Omega=W^{-1/2}E_\omega,
\qquad
E_\omega\,dt=E_\Omega W^{-1/2}ds.
}
\]

The physical energy inequality/equality gives

\[
\int_0^{T^*}E_\omega(t)dt<\infty.
\]

Suppose that on each geometric first-hitting stage `I_j`, while `W in [W_j,qW_j]`, the normalized survivor has a uniform occupancy floor

\[
\boxed{E_\Omega(s)\ge e_0>0.}
\]

Then

\[
\int_{t_j}^{t_{j+1}}E_\omega dt
\ge
\frac{e_0}{\sqrt q}\,W_j^{-1/2}L_j.
\]

Hence

\[
\boxed{
\sum_jW_j^{-1/2}L_j<\infty.}
\]

Using the exact scale action,

\[
\boxed{
\sum_j\frac{W_j^{-1/2}}{\bar a_j}<\infty.}
\]

In particular,

\[
\boxed{
\sqrt{W_j}\,\bar a_j\to\infty.}
\]

Thus a tight/nontrivial normalized profile cannot repeatedly cross geometric vorticity levels with an average scale-rate of order `W_j^(-1/2)` or smaller.

---

## 5. Power-law interpretation

For a model blow-up rate

\[
W(t)\asymp(T^*-t)^{-p},
\qquad p>1,
\]

one has

\[
a(t)\asymp W^{-(p-1)/p}.
\]

The necessary packing condition

\[
\sqrt W\,a\to\infty
\]

requires

\[
\boxed{p<2.}
\]

Therefore, under the occupancy hypothesis, shape-persistent Type-II power laws with `p>=2` are incompatible with finite physical energy dissipation.

This does not exclude all Type-II growth; `1<p<2` and irregular scale-rates remain possible.

---

## 6. Why a positive occupancy floor is natural on the surviving tight branches

The occupancy assumption is not automatic for arbitrary normalized sequences. However it is forced on several already-reduced branches.

For example, on an advection-saturated derivative episode, previous work gives schematically

\[
\|\Delta S\|_2
\lesssim
\nu^{-2/3}P_S^{5/6}\mathfrak A_{\nabla S}^{1/3}.
\]

Since `0<=A_{nabla S}<=2/3`, derivative Plancherel identities transfer this to

\[
H_\Omega^{1/2}\lesssim P_\Omega^{5/6},
\]

up to fixed constants and powers of `nu`.

The first-hitting normalization `||Omega||_infty=1`, Gagliardo--Nirenberg

\[
1\lesssim E_\Omega^{1/8}H_\Omega^{3/8},
\]

and interpolation

\[
P_\Omega\le E_\Omega^{1/2}H_\Omega^{1/2}
\]

then imply a fixed lower bound

\[
\boxed{E_\Omega\ge e_0(\nu,c)>0}
\]

on a genuinely advection-saturated, non-derivative-escape branch.

Similarly, a bounded-radius critical middle-strain mass gives a local `L^2` strain/enstrophy occupancy floor by finite-volume norm comparison.

Thus the stage-packing condition is naturally attached to the remaining tight `M*/AH*` branches.

---

## 7. Shape-frozen compactness split

The projective covariance can remain nearly unchanged without the full profile being stationary. Therefore one must distinguish:

1. projective reorganization;
2. covariance-invisible profile motion;
3. genuinely shape-frozen compact profiles.

Suppose a dangerous normalized sequence avoids `H` and `T` strongly enough to provide compactness, and after allowed recentering has

\[
U_j(\cdot,s)\to U_*
\]

strongly enough on the relevant rescaled interval, with vanishing profile time derivative and

\[
a_j\to a_*.
\]

### Positive limiting scale-rate

If

\[
a_*>0,
\]

the limiting stationary equation is a translated/rescaled Leray backward self-similar profile equation. Classical and later Liouville results exclude nontrivial backward self-similar profiles under broad integrability/local-energy hypotheses.

### Zero limiting scale-rate

If

\[
a_*=0,
\]

the limiting equation becomes the steady whole-space Navier--Stokes equation, modulo any removable constant drift. Under finite Dirichlet integral and far-field decay, the steady Liouville theorem of Xin--Xu forces the profile to be trivial.

Thus a genuinely frozen, compact, decaying, finite-Dirichlet nonzero profile is excluded at both `a_*>0` and `a_*=0`, provided the hypotheses needed to pass to the respective Liouville theorem are verified.

This is a conditional compactness-rigidity gate, not a new Liouville theorem.

---

## 8. Remaining covariance-invisible motions

The low-order covariance can remain fixed while the profile moves by:

- rotations commuting with the covariance;
- finite-dimensional phase motion among modes with the same covariance;
- discretely or rotated self-similar motion;
- higher-Hermite redistribution;
- profile drift without strong compactness.

Recent work on rotated backward self-similar solutions rules out some Type-I rotated self-similar and rotated discretely self-similar profiles for extreme rotation parameters, but not all such motions.

Therefore the next internal task is to augment the covariance channel with a finite Hermite/low-mode shape descriptor. If all low modes settle while the high-Hermite tail is controlled by the existing derivative defect, compactness should force the frozen-profile Liouville gate; otherwise the motion is charged to finite-mode turnover or high-Hermite `H`.

---

## External anchors

- J. Necas, M. Ruzicka, V. Sverak, *On Leray's self-similar solutions of the Navier-Stokes equations*, Acta Math. 176 (1996), 283--294.
- T.-P. Tsai, *On Leray's Self-Similar Solutions of the Navier-Stokes Equations Satisfying Local Energy Estimates*, Arch. Rational Mech. Anal. 143 (1998), 29--51.
- T. Y. Hou, R. Li, *Nonexistence of Local Self-Similar Blow-up for the 3D Incompressible Navier-Stokes Equations*, 2006.
- Z. Xin, D. Xu, *Liouville type theorems on the steady Navier-Stokes equations in R3*, 2017.
- B. Pineau, V. Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, 2026.

Status: **DYNAMIC SCALE ACTION EXACT; TIGHT OCCUPIED TYPE-II STAGES SATISFY A NEW FINITE-ENERGY PACKING CONDITION; GENUINELY FROZEN COMPACT PROFILES ROUTED TO EXISTING LIOUVILLE THEOREMS; COVARIANCE-INVISIBLE LOW-MODE/HIGH-HERMITE MOTION REMAINS OPEN.**