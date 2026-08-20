# Global P_V Action Link — 2026-08-20

Overall status: **ACTIVE PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note connects the remaining full-Navier--Stokes projective branch `P_V*` to the global enstrophy-time occupancy budget derived in `GLOBAL_STAGE_PACKING_BARRIER_2026-08-20.md`.

---

## 1. Normalized algebraic projective residual

In first-hitting variables let

\[
\Sigma=S_U,
\qquad
\Omega=W^{-1}\omega,
\qquad
\|\Omega\|_\infty=1,
\]

and define

\[
\mathcal V
=P_{st}\left(\frac13\Sigma^2+\frac14\Omega\otimes\Omega\right).
\]

The strain/vorticity `L^2` identity gives

\[
\boxed{
\|\Sigma\|_2^2=\frac12\|\Omega\|_2^2=\frac12E_\Omega.
}
\]

---

## 2. Universal L4 control from the first-hitting cap

Since strain is a zero-order singular integral of vorticity, for `1<p<infinity`,

\[
\|\Sigma\|_p\le C_p\|\Omega\|_p.
\]

At `p=4`, the cap `||Omega||_infty=1` gives

\[
\|\Omega\|_4^4
\le
\|\Omega\|_\infty^2\|\Omega\|_2^2
=E_\Omega.
\]

Hence

\[
\boxed{
\|\Omega\|_4^2\le E_\Omega^{1/2},
\qquad
\|\Sigma\|_4^2\le C E_\Omega^{1/2}.
}
\]

Because orthogonal projection does not increase `L2` norm,

\[
\begin{aligned}
\|\mathcal V\|_2
&\le
\frac13\|\Sigma^2\|_2
+\frac14\|\Omega\otimes\Omega\|_2\\
&\le C E_\Omega^{1/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\frac{\|\mathcal V\|_2}{\|\Sigma\|_2}
\le C_V,
}
\]

where `C_V` is universal up to the Riesz-transform constants.

Interpretation: under first-hitting normalization, the algebraic full-NS projective residual cannot rotate the normalized strain shape at arbitrarily large speed without additional derivative/advection action.

---

## 3. Fixed projective action forces a minimum normalized stage duration

Define the normalized projective action

\[
\boxed{
\mathscr A_{V,j}
=
\int_{I_j}
\frac{\|\mathcal V(s)\|_2}{\|\Sigma(s)\|_2}\,ds.
}
\]

If the `P_V` branch is required to carry a fixed amount of projective reorganization on a geometric first-hitting stage,

\[
\mathscr A_{V,j}\ge a_V>0,
\]

then the universal speed bound implies

\[
\boxed{
L_j:=|I_j|\ge\frac{a_V}{C_V}=:L_V>0.
}
\]

Thus a pure `P_V` survivor cannot cross infinitely many geometric vorticity levels through arbitrarily short normalized-time impulses.

---

## 4. Action--occupancy uncertainty estimate

The weaker estimate without dividing by `||Sigma||_2` is

\[
\int_{I_j}\|\mathcal V\|_2ds
\le
C\int_{I_j}E_\Omega^{1/2}ds
\le
C(L_j\mathcal C_j)^{1/2},
\]

where

\[
\mathcal C_j=\int_{I_j}E_\Omega ds.
\]

Therefore if a branch requires

\[
\int_{I_j}\|\mathcal V\|_2ds\ge v_0,
\]

then

\[
\boxed{
\mathcal C_jL_j\ge c v_0^2.
}
\]

Equivalently,

\[
\boxed{
\mathcal C_j\gtrsim \frac1{L_j}.
}
\]

If the tracked core also has a fixed normalized enstrophy occupancy `E_Omega >= e0`, then

\[
\mathcal C_j\gtrsim L_j.
\]

Combining both,

\[
\boxed{
\mathcal C_j\gtrsim \max\{L_j,L_j^{-1}\}\gtrsim1.
}
\]

This prevents the projective branch from becoming simultaneously arbitrarily short and arbitrarily cheap in normalized occupancy.

---

## 5. Why this still does not close global regularity

Physical dissipation on stage `j` is weighted by `W_j^{-1/2}`:

\[
D_j^{phys}\asymp W_j^{-1/2}\mathcal C_j.
\]

The preceding lower bound gives only

\[
D_j^{phys}\gtrsim W_j^{-1/2},
\]

at its optimum `L_j~1`. Since `W_j=q^jW_0`,

\[
\sum_jW_j^{-1/2}<\infty.
\]

Therefore a fixed amount of `P_V` projective action per geometric stage is still compatible with finite global energy.

This confirms the half-power scaling barrier: the `P_V` action-to-enstrophy link is real, but it supplies only `O(1)` normalized occupancy rather than the `O(W^(1/2))` occupancy required for an energy contradiction.

---

## 6. New precise global requirement for P_V

A successful energy-based closure of `P_V*` must strengthen the above estimate to something of the form

\[
\boxed{
\mathcal C_j
\gtrsim
W_j^{1/2}\,\Phi(\mathscr A_{V,j})
}
\]

with `Phi(a_V)>0`, or else identify a different scale-critical globally finite functional that directly controls the sum of `A_{V,j}`.

Status: **P_V PROJECTIVE SPEED IS UNIVERSALLY BOUNDED IN FIRST-HITTING VARIABLES; FIXED PROJECTIVE ACTION FORCES O(1) NORMALIZED TIME/OCCUPANCY, BUT THIS REMAINS BELOW THE W^(1/2) GLOBAL ENERGY-PACKING THRESHOLD.**