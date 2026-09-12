# DSD M19-150 — Every unit Floquet mode must pay the exact quarter-gap from a compact core; tail escape cannot support kernel or elliptic neutrality

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / COMMON KERNEL-ELLIPTIC COERCIVITY / FOR EVERY TWISTED FLOQUET MULTIPLIER OF MODULUS ONE THE PERIOD-AVERAGED VORTICITY IDENTITY REQUIRES EXACT OU-PLUS-VISCOUS COMPENSATION / CRITICAL TAIL COEFFICIENTS VANISH AT INFINITY, SO A UNIT MODE CANNOT MAINTAIN NEUTRALITY BY ESCAPING TO LARGE RADIUS / ALL NONSYMMETRY UNIT MODES ARE GENUINE COMPACT-CORE SPECTRAL OBJECTS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Linearized vorticity identity

Let

\[
W_s=L_U(s)W
\]

be a linearized velocity perturbation and

\[
\eta:=\nabla\times W.
\]

M19-087 gives

\[
\boxed{
\frac12\frac d{ds}\|\eta\|_2^2
+\nu\|\nabla\eta\|_2^2
+\frac14\|\eta\|_2^2
=\mathcal C_U[W].
}
\]

The right side contains only background-dependent transport/strain/nonlocal coupling.

---

## 2. Unit twisted Floquet mode

Let the base orbit be RDSS/DSS,

\[
U(s+S)=Q_*U(s),
\]

and suppose

\[
\mathcal M_S^{tw}v=\mu v,
\qquad
|\mu|=1.
\]

Then after one physical similarity period,

\[
W(s+S)=\mu Q_*W(s)
\]

in the complexified linearized space.

Since `Q_*` is orthogonal and `|mu|=1`,

\[
\boxed{
\|\eta(s+S)\|_2=\|\eta(s)\|_2.
}
\]

This is independent of whether

\[
\mu=1
\]

or

\[
\mu=e^{i\vartheta}\ne1.
\]

---

## 3. Exact one-period neutralization identity

Integrating the vorticity identity over one period yields

\[
\boxed{
\nu\int_s^{s+S}\|\nabla\eta\|_2^2d\tau
+\frac14\int_s^{s+S}\|\eta\|_2^2d\tau
=
\int_s^{s+S}\mathcal C_U[W]d\tau.
}
\]

Thus every unit mode must exactly neutralize the bare quarter-gap and viscosity.

The Floquet phase does not weaken this payment.

---

## 4. Split core and tail

Fix a large similarity radius `R` and write schematically

\[
\mathcal C_U
=\mathcal C_U^{core,R}
+\mathcal C_U^{tail,R}.
\]

On the passive critical-tail lane,

\[
U=O(r^{-1}),
\qquad
\nabla U,\Omega=O(r^{-2}),
\qquad
\nabla\Omega=O(r^{-3}).
\]

The sharpened M19-091 commutator structure removes the constant-vorticity piece and prices the remaining coupling by decaying background derivatives.

Therefore the tail quadratic form is relatively form-small with respect to the bare vorticity energy:

\[
\boxed{
|\mathcal C_U^{tail,R}[W]|
\le
\varepsilon_R
\left(
\nu\|\nabla\eta\|_2^2+\|\eta\|_2^2
\right),
\qquad
\varepsilon_R\to0
}
\]

on the retained hard-domain class.

This is the form-level content behind the relative compactness/quasi-compactness established in M19-095.

---

## 5. Choose a universal spectator core

Choose `R=R_c` large enough that

\[
\varepsilon_{R_c}\le\frac18
\]

and, after the viscosity normalization in the form estimate, small enough to absorb one half of the gradient term.

Then the one-period identity implies

\[
\boxed{
\int_s^{s+S}
\mathcal C_U^{core,R_c}[W]d\tau
\ge
c_0
\int_s^{s+S}
\left(
\|\eta\|_2^2+
u\|\nabla\eta\|_2^2
\right)d\tau
}
\]

for some

\[
c_0>0
\]

uniform on a compact controlled corridor.

Thus the entire neutralization budget cannot migrate to infinity.

---

## 6. No radial-escape unit sequence

Normalize a sequence of unit Floquet modes by

\[
\frac1S\int_0^S\|\eta_j\|_2^2ds=1.
\]

If their vorticity mass and graph norm escaped every fixed compact core, then by local compactness and the tail form-smallness,

\[
\int_0^S\mathcal C_U^{core,R}[W_j]ds\to0
\]

for every fixed `R`, while

\[
\int_0^S\mathcal C_U^{tail,R}[W_j]ds
\]

could be made arbitrarily small uniformly by first choosing `R` large.

This contradicts the exact payment

\[
\frac14\int_0^S\|\eta_j\|_2^2ds
\]

required by neutrality.

Hence

\[
\boxed{
\text{unit Floquet mode}
\Longrightarrow
\text{nonvanishing compact-core activity}.
}
\]

---

## 7. Quantitative compact-core floor

On a compact background corridor and finite unit spectral bundle, continuity upgrades nonvanishing to a uniform floor.

For normalized unit modes,

\[
\boxed{
\int_0^S
\|\chi_{R_c}\eta(s)\|_2^2ds
\ge c_{core}>0
}
\]

for a fixed cutoff `chi_Rc`, after possibly enlarging the controlled graph norm if required by the nonlocal commutator.

Equivalently, every kernel or elliptic hard mode is detectable in the same finite compact region.

---

## 8. Relation to scattering observability

M19-131--133 already show that finite hard modes are uniformly observable at the spectator boundary and in scattering coordinates.

M19-150 adds the complementary fact that unit modes also cannot be supported only by a remote scattering tail.

Thus the hard unit spectrum is pinned simultaneously by

\[
\boxed{
\text{compact-core quarter-gap compensation}
\quad\text{and}\quad
\text{finite-radius/tail observability}.
}
\]

This removes radial delocalization as an explanation for zero growth.

---

## 9. What this does not prove

A compact-core quadratic form can still possess finitely many eigenchannels strong enough to neutralize the quarter-gap.

Therefore

\[
\text{compact-core floor}
\not\Rightarrow
\text{absence of unit spectrum}.
\]

The remaining problem is finite-dimensional orientation/index rigidity inside this compact core.

---

## 10. Revised unit-spectrum frontier

After M19-147--150, every nonsymmetry unit mode is

1. finite-dimensional;
2. semisimple in the scattering pullback metric;
3. uniformly observable;
4. quantitatively supported by a common compact core;
5. either a finite-iterate kernel mode or an irrational elliptic rotation block.

The live theorem is therefore no longer a compactness problem:

\[
\boxed{
\mathcal T_{unit}^{nsym}:
\text{exclude finitely many compact-core neutral channels by a sign/index theorem}.
}
\]

---

## 11. Audit verdict

### Certified on the retained smooth hard lane

- exact one-period quarter-gap payment for every unit multiplier;
- tail form-smallness from critical coefficient decay;
- impossibility of a purely remote unit mode;
- uniform compact-core activity floor on a compact finite unit bundle.

### Not certified

- sign/index exclusion of compact-core unit channels;
- kernel triviality;
- irrational elliptic-block exclusion;
- RSS/RDSS nonexistence;
- global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
