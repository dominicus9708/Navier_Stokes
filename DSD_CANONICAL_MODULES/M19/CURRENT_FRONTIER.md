# M19 Current Frontier

**Date:** 2026-09-14  
**Current tip:** **M19-253**  
**Status:** ACTIVE CALCULATION / WHOLE-SPACE TRANSPARENT MOVING-SPHERE + GALILEAN-CYLINDER FRONTIER / APERIODIC SIGNED FRONTIER OPEN / FINAL ROOT-PROOF CERTIFICATION OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active calculation/closure family. Detailed derivations remain in the numbered modules. This frontier records only the current theorem obligations, reclassifications, and permanent scope firewalls.

## 2. Global proof tree still open

The repository-wide singularity reduction still requires final certification of

\[
\text{hypothetical singularity}
\Longrightarrow
R_{remote}\lor R_{critical}\lor R_{AC}\lor\text{compact hard survivor},
\]

followed by the historical branches

\[
CP\!-\!E\lor CP\!-\!S\lor CE\!-\!T\lor Migration\lor CE\!-\!H.
\]

`ROOT-CERT`, the four non-CE-H roots, genealogy/nonreuse checks, and a beginning-to-end independent audit remain OPEN.

## 3. Aperiodic recurrent hard frontier

The certified recurrent-hard machinery still forces a positive simultaneous W1 severity mean, but M19-196--201 do not convert it into a signed/global contradiction. Therefore

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

remains OPEN.

## 4. Historical bounded-period cavity branch — M19-211--252

M19-211--230 reduced finite hard resonance and physical-adjoint realization to a compact finite-cavity Fredholm problem. M19-231--252 then analyzed the no-slip cavity in detail: core/escape, boundary vorticity concentration, shear payer, \(\nu/R\) layer, macroscopic rigidity, Gaussian pressure coupling, passive boundary impedance, sublinear-shell rigidity, and frozen toroidal/poloidal unit-mode gaps.

### 4.1 Reclassification by M19-253

Clay (A) is a whole-space problem on \(\mathbb R^3\). The spectator sphere is not a physical wall. Therefore M19-231--252 are retained as correct auxiliary cavity diagnostics under their stated hypotheses, but the no-slip-specific conclusions are no longer the canonical whole-space frontier.

In particular, the following do **not** transfer directly to a nonmaterial observation sphere:

- cavity unit-mode core/escape spectral dichotomy as a whole-space theorem;
- exact cavity normalization currency;
- wallward vorticity localization;
- boundary shear payer;
- \(\nu/R\) no-slip layer;
- zero-normal-trace H(div) closure;
- zero-trace radial Hardy use;
- passive no-slip impedance;
- pressure-supported shell normal forms tied to the wall;
- frozen no-slip half-space determinant/high-frequency gap.

The following remain potentially reusable after whole-space/cutoff rederivation:

- bulk scaling/curl ideas from M19-238;
- operator spectral information from M19-241 after domain audit;
- weighted energy bookkeeping from M19-242 with exact moving-window fluxes;
- exact pressure identities from M19-243;
- critical-background asymptotics from M19-244.

No numbered module is deleted or retracted inside its original assumptions.

## 5. M19-253 — transparent moving observation sphere

The active geometric object is

\[
\Omega_R(t)=B_R(X(t))\subset\mathbb R^3,
\qquad S_R(t)=\partial B_R(X(t)),
\]

with fixed radius \(R\), boundary velocity \(\dot X(t)\), and **no boundary condition** imposed on \(u\).

For \(e=|u|^2/2\),

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}e
+\nu\int_{\Omega_R(t)}|\nabla u|^2
=
-\int_{S_R(t)}
\left[e(u-\dot X)\cdot n+p\,u\cdot n-\nu\partial_ne\right]dS.
}
\]

Thus the sphere records real advective, pressure, and viscous exchange. It creates no wall payer.

The net relative volume flux is exactly

\[
\boxed{\int_{S_R(t)}(u-\dot X)\cdot n\,dS=0,}
\]

while local inward/outward flux generally remains nonzero.

For singular-scale work the canonical primitive is a smooth moving cutoff rather than a sharp trace:

\[
\boxed{
\frac d{dt}\int e\chi_X
+\nu\int|\nabla u|^2\chi_X
=
\int[e(u-\dot X)+pu]\cdot\nabla\chi_X
+\nu\int e\Delta\chi_X.
}
\]

For suitable weak solutions the corresponding local-energy inequality is used.

## 6. Exact Galilean-cylinder reformulation

For a spacetime point \(z_0=(x_0,t_0)\), constant tracking velocity \(V\), and scale \(r\), define

\[
Q_r^V(z_0)=
\{(x,t):t_0-r^2<t<t_0,
\ |x-x_0-V(t-t_0)|<r\}.
\]

Set

\[
C_V(r)=r^{-2}\int_{Q_r^V}|u-V|^3,
\]

\[
D_V(r)=r^{-2}\int_{Q_r^V}
|p-(p)_{B_r^V(t)}|^{3/2}.
\]

Constant Galilean transformation maps \(Q_r^V\) to a standard cylinder and preserves the Navier--Stokes system and regular/singular status. Standard one-scale epsilon regularity therefore yields, by contraposition:

\[
\boxed{
\mathcal T_{GMS}^{\varepsilon}:
\quad z_0\text{ singular}
\Longrightarrow
C_V(r)+D_V(r)\ge\varepsilon_*
}
\]

for every constant \(V\) and every sufficiently small admissible \(r\). Equivalently,

\[
\boxed{
\inf_{V\in\mathbb R^3}[C_V(r)+D_V(r)]\ge\varepsilon_*.
}
\]

This is an inherited reformulation of standard epsilon regularity, not a new epsilon-regularity theorem.

## 7. New active whole-space gate

The required new theorem is

\[
\boxed{
\mathcal T_{GMS}^{select}:
\text{every hypothetical singularity produces }r_j\downarrow0,\ V_j
\text{ with }
C_{V_j}(r_j)+D_{V_j}(r_j)<\varepsilon_*.
}
\]

If proved, it contradicts \(\mathcal T_{GMS}^{\varepsilon}\) immediately.

At present,

\[
\boxed{\mathcal T_{GMS}^{select}\text{ is OPEN}.}
\]

The next calculation must therefore use genuinely whole-space, scale-critical DSD ledgers to determine whether maintaining

\[
\inf_V(C_V+D_V)\ge\varepsilon_*
\]

at every small scale forces an incompatible payer.

## 8. Moving-center acceleration firewall

For time-dependent \(V(t)=\dot X(t)\), the translated velocity

\[
v(y,t)=u(y+X(t),t)-V(t)
\]

satisfies standard Navier--Stokes only after the pressure correction

\[
q(y,t)=p(y+X(t),t)+\dot V(t)\cdot y.
\]

Therefore constant Galilean cylinders are the rigorous first primitive; accelerated tracking is a separate extension requiring pressure audit.

## 9. Small regular celestial-sphere geometry

If \(\dot X=u(X,t)\) and the solution is smooth,

\[
[u(X+R\omega)-u(X)]\cdot\omega
=R\,\omega^TS_u(X)\omega+O(R^2).
\]

Moreover,

\[
\int_{S^2}\omega^TS_u\omega\,d\omega
=\frac{4\pi}{3}\operatorname{tr}S_u=0.
\]

Thus the leading relative radial flow consists of strain-controlled inward/outward lobes with zero spherical mean. This is kinematic geometry, not a regularity theorem.

## 10. Permanent firewalls added by M19-253

\[
\boxed{\text{no-slip cavity exclusion}\neq\text{whole-space transparent-sphere exclusion}},
\]

\[
\boxed{\text{sharp moving-sphere identity}\neq\text{singular-scale validity without trace control}},
\]

\[
\boxed{\text{constant Galilean tracking}\neq\text{accelerated tracking without pressure correction}},
\]

\[
\boxed{\text{moving-frame optimization}\neq\text{subcriticality at a singular point}},
\]

\[
\boxed{\mathcal T_{GMS}^{\varepsilon}\neq\mathcal T_{GMS}^{select}}.
\]

Previous firewalls through M19-252 remain valid inside the hypotheses of the corresponding numbered modules.

## 11. Live theorem complex after M19-253

Whole-space moving-observation branch:

\[
\boxed{\mathcal T_{GMS}^{select}}
\]

OPEN.

Aperiodic branch:

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

OPEN.

Historical cavity/Fredholm branch remains available as an auxiliary comparison/diagnostic branch, not as an automatic substitute for whole-space transparent matching.

## 12. Next calculation

1. Re-express the certified whole-space ancestry, energy, enstrophy, palinstrophy, and low-frequency ledgers on \(Q_r^V\) or smooth moving cutoffs.
2. Minimize the critical cost over \(V\) without assuming it becomes small.
3. If the epsilon floor persists, classify the scale-to-scale payer needed to sustain it.
4. Test that payer against the previously certified summability/ancestry budgets.
5. Only if an actual contradiction is obtained promote it toward `ROOT-CERT`; otherwise record the surviving payer as the next OPEN branch.

Global regularity remains unproved.