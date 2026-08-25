# DSD Critical Flux-Loop Cascade Countermodel

Date: 2026-08-25

Status: **KINEMATIC/ASYMPTOTIC FALSIFICATION MODEL / DIVERGENCE-FREE, ZERO TOTAL VORTICITY, FINITE ENSTROPHY, FIXED FLUX, FIXED \(L^3\) SHELL CHARGE, AND PASSIVE LERAY TRANSPORT ARE SIMULTANEOUSLY COMPATIBLE / NOT AN EXACT NAVIER--STOKES SOLUTION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current survivor is

\[
\text{asymptotically fixed-axis critical export conveyor}
+
\text{persistent transverse enstrophy anchor}.
\]

Before seeking another coercive inequality, one must test whether divergence-free topology, zero total vorticity, finite enstrophy, and remote nonlinear interaction already contradict a permanent export cascade.

They do not.

This note constructs a scaled flux-loop family that simultaneously saturates all of these kinematic budgets.

## 2. One compact divergence-free flux-loop template

Choose a smooth compactly supported divergence-free velocity template

\[
U_0\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
\nabla\cdot U_0=0,
\]

with vorticity

\[
\Omega_0=\nabla\times U_0
\]

containing a closed flux-tube loop.

Choose the geometry so that one local leg of the loop has a prescribed directed cross-sectional vorticity flux

\[
\int_{E_0}\Omega_0\cdot e\,dA=\phi_0>0.
\]

The return leg closes the tube and supplies the compensating opposite projection without returning to the recurrent core.

Because \(\Omega_0\) is compactly supported and divergence-free,

\[
\Omega_{0,i}
=\partial_j(x_i\Omega_{0,j}),
\]

so integration by parts gives

\[
\boxed{
\int_{\mathbb R^3}\Omega_0\,dY=0.
}
\]

Thus one closed loop already satisfies the whole-space zero-total-vorticity condition internally.

## 3. Critical scaling

For \(R>0\), define

\[
\boxed{
U_R(Y)=R^{-1}U_0(Y/R),
\qquad
\Omega_R(Y)=R^{-2}\Omega_0(Y/R).
}
\]

Then the directed flux is scale invariant:

\[
\boxed{
\int_{RE_0}\Omega_R\cdot e\,dA
=\phi_0.
}
\]

The total vorticity remains zero:

\[
\int\Omega_RdY
=R\int\Omega_0dY=0.
\]

The critical norms scale as

\[
\boxed{
\|\Omega_R\|_2^2
=R^{-1}\|\Omega_0\|_2^2,
}
\]

\[
\boxed{
\|U_R\|_3^3
=\|U_0\|_3^3,
}
\]

\[
\boxed{
\|U_R\|_2^2
=R\|U_0\|_2^2,
}
\]

and

\[
\boxed{
\int |Y||\Omega_R|^2dY
\asymp 1
}
\]

if the support is placed at radius comparable with \(R\).

These are exactly the scalings isolated in the permanent-export calculation.

## 4. Geometric shell cascade

Choose

\[
R_k=R_0\lambda^k,
\qquad \lambda>1,
\]

and place scaled copies in mutually disjoint annular neighborhoods.

Then

\[
\sum_{k\ge0}\|\Omega_{R_k}\|_2^2
=\|\Omega_0\|_2^2
\sum_{k\ge0}R_k^{-1}<\infty.
\]

At the same time every shell carries the same directed local flux and the same strong \(L^3\) charge.

Hence an infinite family can satisfy finite global enstrophy while producing

\[
\sum_{k<N}\|U_{R_k}\|_{L^3(\text{shell }k)}^3
\sim N.
\]

This is the exact strong-\(L^3\)/weak-critical separation already found dynamically.

## 5. The transverse anchor can decouple from remote loops

Let \(\Omega_{core}\) be a fixed tight core/anchor in \(B_M\), and let a remote loop lie at radius \(R\gg M\).

The existing far-field decoupling estimate gives

\[
\|S_R\|_{L^\infty(B_M)}
\lesssim
Z_R^{1/2}R^{-3/2}
\]

at the level needed here.

Therefore the core stretching cross term obeys

\[
\boxed{
\left|
\int_{B_M}
\Omega_{core}\cdot S_R\Omega_{core}dY
\right|
\lesssim
\|\Omega_{core}\|_2^2
Z_R^{1/2}R^{-3/2}
\to0.
}
\]

Thus the persistent transverse anchor does not force a uniform nonlinear/Betchov interaction with a shell that has escaped to similarity infinity.

The same principle applies to higher remote derivatives with even faster decay.

## 6. Passive Leray transport of one loop

Let \(\Delta=s-s_e\ge0\) and set

\[
\boxed{
U^{(e)}(Y,s)
=e^{-\Delta/2}
U_0(e^{-\Delta/2}Y).
}
\]

Then

\[
U_s^{(e)}
+\frac12U^{(e)}
+\frac12Y\cdot\nabla U^{(e)}=0
\]

exactly.

Its scale is

\[
R=e^{\Delta/2}.
\]

Hence a compact flux loop is an exact pulse solution of the **linear Leray dilation equation**.

## 7. Navier--Stokes residual becomes small

For the scaled pulse,

\[
U_R\cdot\nabla U_R
\sim R^{-3},
\qquad
\nu\Delta U_R\sim R^{-3}.
\]

After applying the Leray projector to absorb the pressure gradient, write the nonlinear-viscous residual as \(\mathcal R_R\).

Its \(L^{6/5}\) norm scales as

\[
\|\mathcal R_R\|_{6/5}
\lesssim
R^{-3}R^{5/2}
=
CR^{-1/2}.
\]

Since

\[
L^{6/5}(\mathbb R^3)\hookrightarrow \dot H^{-1}(\mathbb R^3),
\]

one gets

\[
\boxed{
\|\mathcal R_R\|_{\dot H^{-1}}
\lesssim R^{-1/2}\to0.
}
\]

Thus an exported loop becomes increasingly close, in a natural weak equation norm, to a passive Leray pulse as it moves to similarity infinity.

For geometric radii,

\[
\sum_kR_k^{-1/2}<\infty,
\]

so even the asymptotic residual scale is summable across a geometric tail.

This does **not** construct an exact nonlinear solution, but it shows why a perturbative-looking remote tail is not ruled out by the existing local ledgers.

## 8. Physical-scale interpretation

A pulse emitted at physical natural scale \(r_n\) appears at later first-hitting stage \(j\) at normalized radius

\[
R_{j,n}=\frac{r_n}{r_j}.
\]

Its physical size remains comparable to \(r_n\) while the blow-up core scale \(r_j\) shrinks.

Thus similarity-space escape need not mean literal physical motion to spatial infinity. It can mean that an old finite-scale structure is left behind while the active core zooms to smaller scales.

This is exactly the topology represented by the passive conveyor.

## 9. Consequence for proof strategy

The following implication is false as a purely kinematic statement:

\[
\text{fixed same-sign local export flux}
+
\nabla\cdot\Omega=0
+
\int\Omega=0
+
\sup\|\Omega\|_2<\infty
\Rightarrow
\text{contradiction}.
\]

A closed scaled flux loop internally supplies the compensating vorticity and obeys all critical norm scalings.

Likewise, the persistent transverse anchor need not interact coercively with loops that have already escaped.

## 10. What a successful closure must use

Any successful final step must use genuinely nonlinear/global-in-time information beyond the static constraints above, such as:

1. an exact radiation/return theorem for repeated loop emission;
2. a scale-critical monotone quantity not saturated by the loop family;
3. a quantitative incompatibility between recurrent core regeneration and repeated emission;
4. a new ancient/Type-I rigidity theorem in the weak-critical endpoint class.

## 11. Audit verdict

### PROVED AS A KINEMATIC/ASYMPTOTIC MODEL

- one closed divergence-free loop has zero total vorticity internally;
- critical scaling gives enstrophy \(R^{-1}\), fixed \(L^3\) charge, energy \(R\), and fixed weighted-enstrophy charge;
- geometric loops are enstrophy summable;
- remote-loop/core Betchov interaction vanishes with separation;
- each scaled loop exactly solves the passive Leray dilation equation;
- its nonlinear-viscous residual is \(O(R^{-1/2})\) in \(\dot H^{-1}\).

### IMPORTANT LIMITATION

This is **not** an exact Navier--Stokes solution or a blow-up construction. It is a falsification model showing that the currently used kinematic and critical norm ledgers alone cannot eliminate the survivor.

### OPEN

The exact nonlinear recurrent-core / repeated-radiation coupling.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
