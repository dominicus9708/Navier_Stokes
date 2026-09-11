# M19-021 — Nondegenerate K^5 r gives source-snapshot H1 compactness modulo constants, while energy dilution is the precise L2 noncompactness channel

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE EULER COMPACTNESS / SNAPSHOT H1 MODULO GALILEAN CONSTANTS / ENERGY-DILUTION FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-020 and M5-443

The source-scale Euler normalization is

\[
V_j(y,\tau)
=\frac{u(x_j^s+R_jy,t_j+T_j^E\tau)-c_j}{U_j^E},
\]

with

\[
R_j=K_jr_j,
\qquad
U_j^E=\frac{\nu K_j}{r_j},
\qquad
T_j^E=\frac{r_j^2}{\nu},
\qquad
\varepsilon_j=K_j^{-2}.
\]

Define

\[
\boxed{\Lambda_j:=K_j^5r_j.}
\]

M19-020 proves

\[
\Lambda_j\lesssim C_E
\]

from finite physical kinetic energy and the fixed normalized source-oscillation lower bound.

M5-443 also gives on the first-hitting stage

\[
\boxed{\|\Omega_j^E\|_{L^\infty}\le q.}
\]

The purpose here is to calculate exactly what spatial compactness follows when \(\Lambda_j\) does not collapse.

## 2. Local velocity variance scales by Lambda^{-1}

Fix a bounded source-scale domain \(D\subset\mathbb R^3\).

At any retained physical time, define the local oscillation variance

\[
\mathcal V_u(D_{R_j})
:=
\inf_{c\in\mathbb R^3}
\int_{x_j^s+R_jD}|u(x,t)-c|^2dx.
\]

Since choosing \(c=0\) is admissible,

\[
\mathcal V_u(D_{R_j})
\le
\|u(t)\|_2^2
\le E_0.
\]

After Euler normalization,

\[
\inf_b\int_D|V_j-b|^2dy
=
\frac{\mathcal V_u(D_{R_j})}
{(U_j^E)^2R_j^3}.
\]

But

\[
(U_j^E)^2R_j^3
=\nu^2K_j^5r_j
=\nu^2\Lambda_j.
\]

Therefore

\[
\boxed{
\inf_b\|V_j-b\|_{L^2(D)}^2
\le
\frac{E_0}{\nu^2\Lambda_j}.
}
\]

## 3. Nondegenerate Lambda gives uniform local L2 modulo constants

Suppose

\[
\boxed{\Lambda_j\ge\Lambda_->0.}
\]

Then

\[
\boxed{
\inf_b\|V_j-b\|_{L^2(D)}
\le C(D,E_0,\nu,\Lambda_-).
}
\]

Choose one minimizing or near-minimizing constant \(b_{j,D}\) and set

\[
V_{j,D}^\circ:=V_j-b_{j,D}.
\]

The fixed nontrivial oscillation lower bound from M5-443 remains meaningful because subtraction of a constant is already built into that observable.

Thus the source does not collapse to a spatial constant.

## 4. Uniform local vorticity control

On every fixed source domain during the retained first-hitting time window,

\[
\|\Omega_j^E\|_\infty\le q.
\]

Hence for every fixed \(D\),

\[
\boxed{
\|\Omega_j^E\|_{L^2(D)}
\le q|D|^{1/2}.
}
\]

This estimate is independent of \(\Lambda_j\).

It is important that the derivative of vorticity need not be uniformly controlled: the natural first-hitting micro-scale becomes \(K_j^{-1}\), so bounds such as

\[
\|\nabla_y\Omega_j^E\|\sim K_j
\]

may diverge.

## 5. Interior div-curl estimate

Let

\[
D'\Subset D.
\]

For a divergence-free vector field, a standard interior div-curl estimate gives

\[
\boxed{
\|\nabla V_{j,D}^\circ\|_{L^2(D')}
\le
C_{D',D}
\left(
\|\Omega_j^E\|_{L^2(D)}
+
\|V_{j,D}^\circ\|_{L^2(D)}
\right).
}
\]

The constant subtraction does not change vorticity or gradients.

Under \(\Lambda_j\ge\Lambda_->0\), Sections 3--4 therefore yield

\[
\boxed{
\|V_{j,D}^\circ\|_{H^1(D')}
\le C.
}
\]

## 6. Snapshot spatial precompactness

Rellich--Kondrachov gives

\[
H^1(D')\Subset L^2(D').
\]

Therefore at every fixed retained rescaled time, after subtraction of local constants,

\[
\boxed{
V_{j,D}^\circ
\text{ is precompact in }L^2_{loc}.
}
\]

After a subsequence,

\[
V_{j,D}^\circ\to V
\]

strongly in \(L^2(D')\) and weakly in \(H^1(D')\).

Thus the nondegenerate \(K^5r\) regime already supplies the spatial compactness needed to pass the quadratic nonlinearity at a **single time slice**.

## 7. Local higher Lp compactness below L6

The uniform \(H^1\) bound gives

\[
V_{j,D}^\circ\in L^6(D')
\]

uniformly.

Strong \(L^2\) convergence plus interpolation yields strong convergence in

\[
\boxed{L^p(D')\quad\text{for every }2\le p<6.}
\]

In particular,

\[
V_j\otimes V_j
\]

is spatially compact in \(L^1_{loc}\) at a fixed time after the constant mode is handled consistently.

## 8. Why full spacetime Euler compactness is not yet proved

The constants used in Section 3 may depend on rescaled time:

\[
b_{j,D}=b_{j,D}(\tau).
\]

A time-dependent constant velocity is not merely an algebraic subtraction in the evolution equation unless it is accompanied by the corresponding moving spatial frame and pressure gauge.

An accelerating translation can absorb a uniform acceleration into pressure, but one must certify a coherent source-center/frame choice over a fixed \(\tau\)-interval.

Therefore snapshot compactness does not automatically imply

\[
V_j\to V
\quad\text{strongly in spacetime}.
\]

The remaining issues include:

- coherent Galilean/recentering control in time;
- time compactness of the mean-free velocity;
- pressure/harmonic-pressure normalization;
- spatial-tail control needed for nonlocal pressure;
- expansion to an ancient time interval.

These are genuine and must not be hidden behind the snapshot estimate.

## 9. What the equation suggests once a coherent frame is available

In a coherent frame the normalized equation is

\[
\partial_\tau V_j
+\mathbb P\nabla\cdot(V_j\otimes V_j)
=
\varepsilon_j\Delta V_j,
\qquad
\varepsilon_j\to0,
\]

in divergence-free weak form.

The spatial \(H^1_{loc}\) bound would give

\[
V_j\otimes V_j
\]

control sufficient to bound \(\partial_\tau V_j\) in a negative Sobolev space on compact sets, while the viscous term is small.

Thus the nondegenerate \(\Lambda_j\) regime is close to an Aubin--Lions Euler compactness argument; the missing step is primarily the coherent-frame/nonlocal-pressure implementation, not an absence of any spatial compactness.

No full compactness theorem is claimed here.

## 10. Energy-dilute regime

If

\[
\boxed{\Lambda_j=K_j^5r_j\to0,}
\]

then finite physical energy only gives

\[
\inf_b\|V_j-b\|_{L^2(D)}^2
\le
\frac{E_0}{\nu^2\Lambda_j}
\to\infty
\]

as an upper bound.

Thus the parent energy supplies no uniform source-scale velocity-variance control.

The vorticity cap remains

\[
\|\Omega_j^E\|_\infty\le q,
\]

but curl control alone cannot bound a large harmonic/Galilean velocity component on a source domain.

Hence

\[
\boxed{
\Lambda_j\to0
}
\]

is a precise velocity-energy noncompactness channel.

## 11. A sharper local quantity for the dilute branch

Define

\[
\boxed{
E_j^{E}(D)
:=
\inf_b\int_D|V_j-b|^2dy.
}
\]

M5-443 gives

\[
E_j^E(D_1)\ge e_*>0.
\]

There are then two subcases inside \(\Lambda_j\to0\):

\[
\boxed{
E_j^E(D)\le C
}
\]

for every fixed \(D\), in which case spatial compactness still follows despite the failure of the parent-energy upper bound; or

\[
\boxed{
E_j^E(D)\to\infty
}
\]

on some fixed domain, which is genuine Euler-scale amplitude/low-frequency noncompactness.

Thus \(\Lambda_j\to0\) identifies where finite parent energy stops helping, but actual noncompactness must still be witnessed by \(E_j^E\) or another source variable.

## 12. Updated Type-II compactness split

The strong source branch is now refined to

\[
\boxed{
\begin{aligned}
H_{remote}^{strong}
\Longrightarrow{}&
G_{Euler\ snapshot\ compact}\n\\&\lor
G_{coherent\ frame/time/pressure\ defect}\n\\&\lor
G_{Euler\ velocity\ variance\ noncompact}\n\\&\lor
G_{derivative/frequency\ noncompact}\n\\&\lor
G_{tail\ noncompact}.
\end{aligned}
}
\]

In the nondegenerate \(\Lambda_j\) regime, the spatial snapshot-compact branch is automatic modulo constants.

## 13. Next calculation

M19-022 should attack the coherent-time compactness step in divergence-free weak form, avoiding unnecessary pointwise pressure estimates.

The target is to show that if

\[
\sup_{\tau\in[-T,0]}
E_j^E(D)<\infty
\]

on every compact source domain and a coherent moving Galilean frame is available, then the vorticity cap implies enough negative-Sobolev time regularity for local Aubin--Lions compactness and passage to a nontrivial ancient Euler solution.

Failure would then be isolated specifically as frame/mean drift, source-tail, or time-compactness loss.

---

\[
\boxed{\text{M19-021 COMPLETE; NONDEGENERATE }K^5r\text{ GIVES SPATIAL EULER COMPACTNESS MODULO CONSTANTS.}}
\]
