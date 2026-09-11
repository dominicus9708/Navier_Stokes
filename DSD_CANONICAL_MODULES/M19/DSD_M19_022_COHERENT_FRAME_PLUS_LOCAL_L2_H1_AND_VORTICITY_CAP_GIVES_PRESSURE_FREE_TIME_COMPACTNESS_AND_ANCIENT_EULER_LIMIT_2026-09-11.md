# M19-022 — Coherent frame plus local L2/H1 and vorticity cap gives pressure-free time compactness and an ancient Euler limit

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE EULER COMPACTNESS / PRESSURE-FREE WEAK FORM / AUBIN--LIONS STEP

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-021

Work with the Euler-scaled remote-source sequence

\[
\partial_\tau V_j+(V_j\cdot\nabla)V_j=-\nabla P_j+\varepsilon_j\Delta V_j,
\qquad
\nabla\cdot V_j=0,
\qquad
\varepsilon_j=K_j^{-2}\to0.
\]

M19-021 gives, in the nondegenerate or otherwise locally velocity-compact regime, uniform local spatial control modulo constants. The remaining issue is to turn this into spacetime compactness.

Fix

\[
T>0,
\qquad
D'\Subset D\Subset\mathbb R^3.
\]

Assume a **coherent source frame** has been chosen on \([-T,0]\) so that one sequence of velocity fields \(V_j\) is defined on the same fixed source coordinates and obeys

\[
\boxed{
\sup_{\tau\in[-T,0]}
\|V_j(\tau)\|_{L^2(D)}
\le C_D,
}
\]

and

\[
\boxed{
\sup_{\tau\in[-T,0]}
\|\nabla V_j(\tau)\|_{L^2(D)}
\le C_D.
}
\]

The local gradient bound may be obtained from M19-021 using the Euler-scaled vorticity cap and interior div--curl once the coherent frame has fixed the Galilean mode.

No pointwise pressure estimate is assumed.

## 2. Divergence-free weak formulation removes pressure

Let

\[
\varphi\in C_c^\infty(D;\mathbb R^3),
\qquad
\nabla\cdot\varphi=0.
\]

Then

\[
\left\langle\partial_\tau V_j,\varphi\right\rangle
=
\int_D(V_j\otimes V_j):\nabla\varphi\,dy
-
\varepsilon_j\int_D\nabla V_j:\nabla\varphi\,dy.
\]

The pressure term vanishes exactly.

Hence

\[
\left|
\left\langle\partial_\tau V_j,\varphi\right\rangle
\right|
\le
\|V_j\|_2^2\|\nabla\varphi\|_\infty
+
\varepsilon_j\|\nabla V_j\|_2\|\nabla\varphi\|_2.
\]

In three dimensions,

\[
H^4_0(D)\hookrightarrow W^{1,\infty}(D).
\]

Therefore

\[
\boxed{
\|\partial_\tau V_j\|_{H^{-4}_\sigma(D)}
\le C_D
}
\]

uniformly on \([-T,0]\), where \(H^{-4}_\sigma\) denotes the dual of divergence-free \(H^4_0\) test fields.

The precise negative index is not important; any sufficiently negative fixed Sobolev space works.

## 3. Uniform time equicontinuity in a negative norm

For

\[
-T\le\tau_1<\tau_2\le0,
\]

integration gives

\[
\boxed{
\|V_j(\tau_2)-V_j(\tau_1)\|_{H^{-4}_\sigma(D)}
\le
C_D|\tau_2-\tau_1|.
}
\]

Thus the sequence is uniformly Lipschitz in material/source time with values in a fixed negative Sobolev space.

This estimate is obtained without solving for pressure.

## 4. Local Aubin--Lions / Simon compactness

Use the compact-continuous chain

\[
H^1(D')
\Subset
L^2(D')
\hookrightarrow
H^{-4}(D').
\]

The uniform bounds

\[
V_j\in L^\infty(-T,0;H^1(D')),
\]

and

\[
\partial_\tau V_j
\in L^\infty(-T,0;H^{-4}(D'))
\]

imply, after extraction,

\[
\boxed{
V_j\to V
\quad\text{strongly in }L^2((-T,0)\times D').
}
\]

By interpolation with the uniform local \(H^1\) bound,

\[
\boxed{
V_j\to V
\quad\text{strongly in }L^p_{loc}
\text{ for every }2\le p<\frac{10}{3}
}
\]

in spacetime, and in particular

\[
\boxed{
V_j\otimes V_j
\to
V\otimes V
\quad\text{strongly in }L^1_{loc}.
}
\]

The exponent \(10/3\) is only one convenient spacetime interpolation ceiling; the nonlinear passage requires only strong local \(L^2\).

## 5. Vanishing viscosity

For every compactly supported divergence-free test field \(\phi(y,\tau)\),

\[
\left|
\varepsilon_j
\int\!\!\int
\nabla V_j:\nabla\phi
\right|
\le
\varepsilon_j
C_{\phi,T,D}
\to0.
\]

Hence the viscous term disappears in the limit.

## 6. Passage to Euler in pressure-free form

The strong convergence of the quadratic term and weak convergence of the time derivative give

\[
\boxed{
\int\!\!\int
\left[
V\cdot\partial_\tau\phi
+(V\otimes V):\nabla\phi
\right]\,dy\,d\tau
=0
}
\]

for every divergence-free compactly supported test field \(\phi\).

Thus \(V\) is a local distributional incompressible Euler solution.

A local pressure can subsequently be reconstructed in the usual distributional way; pressure compactness is not needed to obtain the velocity limit.

## 7. Spatial regularity inherited by the Euler limit

The uniform local bounds yield

\[
V\in L^\infty_{loc}((-\infty,0];H^1_{loc}),
\]

on every interval for which the coherent-frame bounds hold after diagonal extraction.

The Euler-scaled vorticity bound passes weak-* as

\[
\boxed{
\|\nabla\times V\|_{L^\infty_{loc}}
\le q.
}
\]

No higher derivative compactness is claimed.

## 8. Ancient-time diagonal extraction

The physical source time scale is

\[
T_j^E=\frac{r_j^2}{\nu}\to0.
\]

For every fixed \(T>0\), the interval

\[
[-T,0]
\]

corresponds to a physical interval of length \(TT_j^E\), which lies before the first-hitting time for all sufficiently large \(j\).

The first-hitting vorticity cap therefore persists on each fixed backward Euler-time window.

If the coherent-frame and local velocity bounds hold uniformly on every fixed \([-T,0]\), a diagonal extraction gives

\[
\boxed{
V:\mathbb R^3\times(-\infty,0]\to\mathbb R^3
}
\]

as an ancient Euler solution.

## 9. Nontriviality

M5-443 supplies a fixed source-scale oscillation lower bound at the marked time:

\[
\inf_c
\|V_j(\cdot,0)-c\|_{L^2(D_1)}
\ge c_0>0.
\]

At \(\tau=0\), M19-021 gives snapshot \(H^1_{loc}\) compactness modulo the same coherent frame. Extract the subsequence so that

\[
V_j(\cdot,0)\to V(\cdot,0)
\quad\text{strongly in }L^2(D_1).
\]

Then

\[
\boxed{
\inf_c
\|V(\cdot,0)-c\|_{L^2(D_1)}
\ge c_0.
}
\]

Hence the ancient Euler limit is nontrivial modulo Galilean constants.

## 10. What is now closed in the compact branch

Under a coherent source frame and uniform local velocity variance on fixed Euler-time windows,

\[
\boxed{
\text{spatial compactness}
+
\text{time compactness}
+
\text{nonlinear passage}
}
\]

are all available.

Thus the old broad branch

\[
G_{time\ compactness/pressure\ defect}
\]

is reduced substantially:

\[
\boxed{
G_{Euler\ compactness\ failure}
\Longrightarrow
G_{coherent\ frame/mean\ drift}
\lor
G_{local\ velocity\ variance\ noncompact}
\lor
G_{source\ tail/domain\ loss}.
}
\]

Pressure is no longer an independent compactness root on the controlled local branch.

## 11. Remaining Euler-compact root

The compact branch now produces a nontrivial ancient Euler solution satisfying at least

\[
\boxed{
V\in L^\infty_{loc}(H^1_{loc}),
\qquad
\omega_V\in L^\infty_{loc},
}
\]

with the source normalization inherited from the Type-II construction.

This is not yet a contradiction. Broad classes of nontrivial ancient Euler solutions exist.

The remaining question is whether the first-hitting/source ancestry supplies an additional condition -- decay, finite energy, one-sided strain, pressure growth, circulation, or source localization -- placing this profile in a rigidity class.

## 12. Next calculation

M19-023 should attack the **coherent frame / mean-drift defect** itself.

A useful route is to derive the time variation of the local mean velocity on a source ball directly from the weak momentum equation. If the mean drift is bounded in source units, one obtains the coherent frame required here. If it is unbounded, identify the exact boundary momentum-flux / pressure-harmonic quantity that pays for it and route that failure to remote/tail noncompactness.

---

\[
\boxed{\text{M19-022 COMPLETE AS A CONDITIONAL EULER COMPACTNESS STEP; THE COHERENT-FRAME DEFECT IS NOW THE PRIMARY COMPACTNESS FRONTIER.}}
\]
