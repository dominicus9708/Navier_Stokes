# M19-023 — Nondegenerate K^5 r removes the coherent-frame defect by using the original physical inertial frame

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE FRAME CLOSURE / DIRECT LOCAL L2 / EULER-COMPACT BRANCH SHARPENING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why the M19-021 frame defect can be avoided

M19-021 estimated

\[
\inf_b\|V_j-b\|_{L^2(D)}
\]

and therefore left a possible time-dependent Galilean-mode defect.

On the nondegenerate energy branch this is unnecessary.

The original finite-energy Navier--Stokes solution already lives in one fixed physical inertial frame with

\[
\|u(t)\|_2^2\le E_0
\]

for all pre-singular times.

Use that same frame in the Euler source normalization:

\[
\boxed{
V_j(y,\tau)
:=
\frac{u(x_j^s+R_jy,t_j+T_j^E\tau)}{U_j^E}.
}
\]

No Galilean subtraction is made.

## 2. Exact local L2 scaling

For every fixed bounded source domain \(D\),

\[
\int_D|V_j(y,\tau)|^2dy
=
\frac{1}{(U_j^E)^2R_j^3}
\int_{x_j^s+R_jD}
|u(x,t_j+T_j^E\tau)|^2dx.
\]

Since

\[
(U_j^E)^2R_j^3
=
\nu^2K_j^5r_j
=
\nu^2\Lambda_j,
\]

we obtain

\[
\boxed{
\|V_j(\tau)\|_{L^2(D)}^2
\le
\frac{E_0}{\nu^2\Lambda_j}.
}
\]

Therefore if

\[
\boxed{
\Lambda_j\ge\Lambda_->0,
}
\]

then

\[
\boxed{
\sup_{\tau\in[-T,0]}
\|V_j(\tau)\|_{L^2(D)}
\le C(E_0,\nu,\Lambda_-)
}
\]

on every fixed backward Euler-time interval \([-T,0]\).

This is a direct bound, not a bound modulo constants.

## 3. Nontriviality is preserved without subtracting a constant

M5-443 gives the Galilean-invariant oscillation lower bound

\[
\inf_c
\|V_j(\cdot,0)-c\|_{L^2(D_1)}
\ge c_0>0.
\]

For the particular choice \(c=0\),

\[
\boxed{
\|V_j(\cdot,0)\|_{L^2(D_1)}
\ge c_0.
}
\]

Hence using the original inertial frame does not destroy source nontriviality.

## 4. Uniform local H1 in the inertial frame

The Euler-scaled vorticity satisfies

\[
\|\Omega_j^E\|_\infty\le q
\]

on every fixed backward first-hitting window.

For

\[
D'\Subset D,
\]

the interior div--curl estimate gives

\[
\|\nabla V_j\|_{L^2(D')}
\le
C_{D',D}
\left(
\|\Omega_j^E\|_{L^2(D)}
+
\|V_j\|_{L^2(D)}
\right).
\]

Thus under \(\Lambda_j\ge\Lambda_->0\),

\[
\boxed{
\sup_{\tau\in[-T,0]}
\|V_j(\tau)\|_{H^1(D')}
\le C.
}
\]

No mean subtraction and no moving frame are needed.

## 5. M19-022 now applies unconditionally inside the nondegenerate Lambda branch

M19-022 requires a coherent fixed source frame with uniform local \(L^2\) and \(H^1\) control.

Sections 1--4 provide exactly that frame: it is simply the inherited original physical inertial frame.

Therefore for every fixed \(T>0\), after subsequence extraction,

\[
\boxed{
V_j\to V
\quad\text{strongly in }L^2_{loc}(\mathbb R^3\times[-T,0]).
}
\]

The nonlinear term converges strongly in \(L^1_{loc}\), viscosity vanishes because \(\varepsilon_j=K_j^{-2}\to0\), and the limit solves Euler in divergence-free weak form.

Diagonal extraction over \(T=1,2,3,\dots\) gives a nontrivial ancient Euler solution

\[
\boxed{
V:\mathbb R^3\times(-\infty,0]\to\mathbb R^3.
}
\]

## 6. The frame defect is not independent

The previous provisional split

\[
G_{coherent\ frame/mean\ drift}
\]

is therefore removed from the nondegenerate energy branch.

A large apparent local constant velocity in source units would itself contribute to the left side of

\[
\|V_j\|_{L^2(D)}^2
\le
\frac{E_0}{\nu^2\Lambda_-},
\]

so it is already bounded by the physical kinetic-energy budget.

Thus

\[
\boxed{
\Lambda_j\gtrsim1
\Longrightarrow
\text{fixed inertial frame + spacetime Euler compactness}.
}
\]

More generally only a fixed positive lower bound on \(\Lambda_j\) is needed.

## 7. What happens when Lambda collapses

If

\[
\Lambda_j\to0,
\]

then

\[
\frac{E_0}{\nu^2\Lambda_j}\to\infty,
\]

so the original inertial-frame energy bound no longer gives source-scale local \(L^2\) compactness.

Hence apparent Galilean/mean drift and genuine source-scale low-frequency amplitude growth are not separate roots there. They are both contained in

\[
\boxed{
G_{Euler\ velocity/low\text{-}frequency\ noncompactness}
}
\]

on the energy-dilute branch.

## 8. Updated remote split

The strong remote source route is now

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
\begin{cases}
\Lambda_j\ge\Lambda_->0
\Rightarrow
E_{ancient}^{Euler,compact},\\[1mm]
\Lambda_j\to0
\Rightarrow
G_{Euler\ velocity/low\text{-}frequency\ noncompact},\\[1mm]
G_{source\ tail/domain\ noncompact},\\
G_{higher\ derivative/frequency\ noncompact}.
\end{cases}
}
\]

The first line now has actual spacetime compactness, not merely snapshot compactness.

## 9. Remaining compact-Euler problem

The compact branch gives a nonzero ancient Euler solution with

\[
V\in L^\infty_{loc}H^1_{loc},
\qquad
\omega_V\in L^\infty_{loc},
\]

and a source-scale normalization inherited from the remote Type-II construction.

No contradiction follows from these properties alone.

The next useful calculation is to determine what additional **global/source-scale energy information** survives in the limit when \(\Lambda_j\) has a positive limit or subsequential limit.

In particular, M19-024 should test whether the normalized total kinetic energy

\[
\frac{\|u(t)\|_2^2}{\nu^2\Lambda_j}
\]

produces a finite-energy ancient Euler profile, or whether energy can escape to source-space infinity during the limit. This is the next compact-Euler rigidity gate.

---

\[
\boxed{\text{M19-023 REMOVES THE COHERENT-FRAME DEFECT ON THE NONDEGENERATE }K^5r\text{ BRANCH.}}
\]
