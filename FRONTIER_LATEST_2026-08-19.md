# Latest Frontier — 2026-08-19

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier continues `FRONTIER_LATE_2026-08-19.md` after introducing dynamic first-hitting normalization, finite-energy stage packing, Hermite compactness, a local-variance Type-II gate, and the left/right covariance decomposition of the vorticity-gradient source.

---

## 1. Dynamic first-hitting scale

Let

\[
W=\|\omega\|_\infty,
\qquad
\lambda=W^{1/2},
\qquad
\frac{ds}{dt}=W,
\]

\[
U=\lambda^{-1}u,
\qquad
\Omega=\lambda^{-2}\omega,
\qquad
\|\Omega\|_\infty=1,
\]

and

\[
\boxed{a=\frac{W'}{2W^2}.}
\]

Then

\[
\boxed{
\partial_s\Omega
=S_U\Omega-(U-c)\cdot\nabla\Omega+\nu\Delta\Omega
-a(2\Omega+y\cdot\nabla\Omega).
}
\]

A geometric first-hitting step `W_j -> q W_j` satisfies exactly

\[
\boxed{
\int_{I_j}a(s)ds=\frac12\log q.
}
\]

---

## 2. Finite-energy stage packing

The normalized enstrophy obeys

\[
E_\Omega=W^{-1/2}E_\omega.
\]

If a tight survivor has `E_Omega >= e0>0` throughout geometric stages, physical energy dissipation gives

\[
\boxed{
\sum_j W_j^{-1/2}L_j<\infty,
}
\]

where `L_j` is the rescaled-time stage length. Since

\[
L_j=\frac{\frac12\log q}{\bar a_j},
\]

one gets

\[
\boxed{
\sum_j\frac{W_j^{-1/2}}{\bar a_j}<\infty,
\qquad
\sqrt{W_j}\,\bar a_j\to\infty.
}
\]

Under the occupancy hypothesis, power-law Type-II growth `W~(T-t)^(-p)` with `p>=2` is excluded.

---

## 3. Tight Type-II persistence routes to T/H

For a bounded normalized velocity-variance core of radius `R`, the dynamic local-energy/variance equation has the typed form

\[
\frac12V_R'+\nu D_R
=\frac a2V_R+\mathcal F_R,
\]

where `F_R` is shell/material turnover. Weighted Poincare gives

\[
V_R\le C_PR^2D_R.
\]

If the core is recurrent and `F_R` is subdominant,

\[
\boxed{
L_j\lesssim R^2/\nu,
\qquad
\bar a_j\gtrsim\nu/R^2.
}
\]

Hence `a -> 0` cannot coexist with bounded-radius shape persistence and low turnover. A Type-II persistent core must activate `T`, `H`, or lose recurrence.

---

## 4. Frozen compact profile gate

If a tight/non-derivative-escape normalized sequence is compact enough that the full profile freezes, then:

- positive limiting `a_*` gives a backward self-similar Leray profile;
- zero limiting `a_*` gives a steady whole-space Navier--Stokes profile, modulo removable drift.

Existing Liouville theorems exclude nontrivial profiles under their respective integrability/local-energy/decay hypotheses.

Therefore the genuinely new compact survivor is not an exactly frozen profile but a nonstationary recurrent/phase-moving normalized orbit.

---

## 5. Finite-Hermite compactness

For Gaussian Hermite projection `Pi_n`,

\[
\boxed{
\|\Pi_{\ge N}f\|_{L^2_\gamma}^2
\le\frac1N\|\nabla f\|_{L^2_\gamma}^2.
}
\]

Thus a sequence avoiding high-Hermite/derivative escape cannot hide arbitrary profile motion exclusively in the infinite tail. After a diagonal subsequence, either:

1. the profile is compact in the Gaussian core;
2. a finite number of low modes carries O(1) phase motion;
3. high-Hermite control fails (`H`).

Covariance-invisible motion is therefore typed as finite-dimensional low-mode action or high-Hermite escape.

---

## 6. Dynamic middle-strain scale damping

The normalized enstrophy ledger is

\[
\boxed{
\frac12E_\Omega'
+\frac a2E_\Omega
+4\|\Lambda_2^+\|_3^3
\le
\left(C_S\|\Lambda_2^+\|_{3/2}-\nu\right)P_\Omega.
}
\]

For `E_Omega>=e0`, each geometric scale step pays the fixed scale-damping cost

\[
\boxed{
\frac12\int aE_\Omega ds
\ge\frac{e_0}{4}\log q.
}
\]

Hence a recurrent normalized profile must replenish a fixed amount of critical middle-strain/palinstrophy production per scale step.

---

## 7. Vorticity-gradient left/right covariance

Let

\[
G=\nabla\Omega.
\]

Then

\[
\boxed{
(\partial_s+(U-c+a y)\cdot\nabla)G
=SG-GS-GW+(\nabla S)\Omega+\nu\Delta G-3aG.
}
\]

Define

\[
L_G=GG^T/|G|^2,
\qquad
C_G=G^TG/|G|^2.
\]

Then

\[
\boxed{
G:(SG-GS)=|G|^2S:(L_G-C_G).
}
\]

Thus homogeneous strain amplifies palinstrophy only through left/right covariance mismatch, equivalently nonnormality of the gradient matrix.

Rigid rotation satisfies

\[
\boxed{G:GW=0.}
\]

The inhomogeneous source `B=(nabla S)Omega` obeys, under `||Omega||_infty=1`,

\[
\boxed{
\|B\|_2^2\le\frac12P,
\qquad
\left|\int G:B\right|\le P/\sqrt2.
}
\]

Consequently

\[
\boxed{
\frac12(\log P)'
+\frac32a
+\nu H/P
\le
\mathcal L_{LR}+1/\sqrt2,
}
\]

where `L_LR` is the weighted left/right nonnormal strain action.

Short recurrent scale steps therefore require genuine gradient nonnormality or hyperpalinstrophy; long steps are constrained by the Type-II/finite-energy packing gates.

---

## 8. Current active survivor classes

The earlier broad `M/H/T` tree is now reduced to the following forms.

### R1 — finite-mode / projective reorganization

The normalized profile changes by O(1) in a finite set of low Hermite/projective channels. Each such change has a typed source/turnover/viscous/scale action.

### R2 — compact positive-rate recurrent orbit

The profile remains tight and derivative-controlled, with average `a` bounded away from zero, but does not converge to a stationary self-similar profile. Periodic/discretely self-similar and rotated periodic subcases are externally constrained; a general aperiodic recurrent orbit remains open.

### R3 — short fast scale steps

The normalized stage length is too short for the universal inhomogeneous gradient source to supply the palinstrophy-scale damping, forcing left/right gradient nonnormality or hyperpalinstrophy.

### R4 — transport/high-derivative escape

Long Type-II persistence, weak connectivity, far/multicore turnover, or high-Hermite escape routes to `T` or `H` and is no longer untyped.

### M* — critical middle-strain replenishment

Every occupied geometric scale step pays a fixed dynamic scale-damping amount that must be replenished through critical middle-strain/palinstrophy production.

---

## 9. Principal next theorem target

The remaining core problem is now a compact-recurrence packing theorem:

\[
\boxed{
\begin{gathered}
\text{Can a bounded-radius, derivative-controlled normalized orbit cross infinitely many}\
\text{geometric vorticity levels while repeatedly paying the fixed scale-damping action,}\
\text{yet avoid both finite-mode projective turnover and the left/right nonnormal/hyper}\
\text{palinstrophy costs strongly enough to stay compatible with finite physical energy?}
\end{gathered}
}
\]

A complete proof still requires a new monotonicity, rigidity, or summability estimate for the compact positive-rate recurrent orbit.

Status: **FROZEN COMPACT AND LONG TYPE-II PERSISTENCE SUBBRANCHES REDUCED; HIGH-HERMITE HIDDEN MOTION TYPED; SHORT-STAGE DERIVATIVE SOURCE REFINED BY GRADIENT NONNORMALITY; ACTIVE ENDGAME = COMPACT POSITIVE-RATE RECURRENCE / FINITE-MODE ACTION PACKING — GLOBAL REGULARITY NOT PROVED.**