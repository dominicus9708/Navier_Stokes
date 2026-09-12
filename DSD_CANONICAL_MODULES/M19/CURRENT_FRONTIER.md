# M19 Current Frontier

**Date:** 2026-09-12  
**Current tip:** **M19-101**  
**Status:** ACTIVE CALCULATION / FINITE-DIMENSIONAL INTERIOR CENTER + EXACT DSS LOG-PERIODIC HARD CORE / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 remains frozen as the analysis/audit family.
M19 is the active calculation/closure family.

\[
\boxed{
\text{M18 certified analysis}
\Longrightarrow
\text{M19 calculation}
\Longrightarrow
\text{closure or explicit theorem frontier}.
}
\]

## 2. Earlier reductions retained

M19-001--054 reduced the quiet CE-H/current, remote, and cubic ancestry-conversion survivors into the weak-critical recurrent scattering complex at their certified scope.

On the controlled passive spectator branch,

\[
U(y,s)=\frac1rA(q,\omega)+O(r^{-3}),
\qquad
q=\log r-s/2,
\]

with

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

M19-055--074 showed that local conservation laws, pressure convolution, ordinary compact recurrence, almost periods, and fixed finite-codimensional quotients do not by themselves remove an aperiodic q-history.

## 3. Exact symmetry center — M19-075--086

The exact neutral symmetry space is

\[
E^c_{sym}
=\operatorname{span}\{\partial_sU\}
\oplus T_U(SO(3)\cdot U).
\]

Rotation can be modulated without weighted-energy loss in the retained radial Hilbert geometry.

Zero Lyapunov growth is not low temporal frequency. Weighted velocity norms alone are not spatially tight; normalized mass may escape annularly or diffuse over log-radius shells.

## 4. Pressure-free vorticity quarter-gap — M19-087

For linearized vorticity `eta=curl W`,

\[
\boxed{
\frac12\frac d{ds}\|\eta\|_2^2
+\nu\|\nabla\eta\|_2^2
+\frac14\|\eta\|_2^2
=\mathcal C_U[W].
}
\]

A zero center therefore requires

\[
\boxed{
\left\langle
\frac{\mathcal C_U[W]}{\|\eta\|_2^2}
\right\rangle
=
\frac14+
u
\left\langle
\frac{\|\nabla\eta\|_2^2}{\|\eta\|_2^2}
\right\rangle.
}
\]

Passive far-field vorticity escape cannot supply this compensation because the critical background coefficients decay at infinity.

## 5. Quasi-compact interior cocycle — M19-088 and M19-095

The bare similarity-vorticity generator

\[
\mathcal L_0=\nu\Delta-1-\frac12y\cdot\nabla
\]

satisfies

\[
\|e^{T\mathcal L_0}\|\le e^{-T/4}.
\]

Under the retained smooth critical-tail bounds

\[
U=O(r^{-1}),\qquad
\nabla U,\Omega=O(r^{-2}),\qquad
\nabla\Omega=O(r^{-3}),
\]

the full linearized background is relatively compact with respect to the bare generator. Hence

\[
\boxed{
\mathcal U(s+T,s)-e^{T\mathcal L_0}
\text{ is compact},
}
\]

and

\[
\boxed{
\lambda_{ess}\le-1/4<0.
}
\]

Therefore

\[
\boxed{
\dim E^{\ge0}<\infty,
\qquad
\dim E^c<\infty.
}
\]

This is the main new positive reduction: the infinite formal scattering center becomes a finite-dimensional interior-realizable center.

## 6. Extra-center quarter-gap budget — M19-089--094

After rotational quotient,

\[
E_q^c
=\operatorname{span}\{\partial_sU\}
\oplus E^c_{extra}.
\]

If `m=dim E_extra`, an orthonormal vorticity frame must satisfy the Ky-Fan compensation budget

\[
\boxed{
\left\langle\sum_{j=1}^m\mathfrak k_U(\eta_j)\right\rangle
\ge m/4.
}
\]

The constant-vorticity part of the nonlocal commutator cancels exactly, leaving the sharpened compensation currency

\[
\boxed{
\nu^{-1}\|\Omega\|_3^2+\|\nabla\Omega\|_3.
}
\]

Interpolation descends this to palinstrophy/raw-H2 activity, but M19-094 shows the corresponding physical-parent costs remain geometrically summable. Unsigned P/H ancestry ledgers therefore do not close the extra center.

The live aperiodic theorem remains

\[
\boxed{
\mathcal T_{extra-center}: E^c_{extra}=0.
}
\]

It now concerns a finite-dimensional compact-core spectral object, not an infinite-dimensional tail center.

## 7. One-slice Type-I external gate — M19-096--097

Pineau--Vicol (2026) prove that Type-I plus the stated pressure-annulus hypothesis and one sufficiently late approximately self-similar time slice implies regularity.

Consequently, on a singular branch satisfying their application gate,

\[
\boxed{
\mathcal V_G(s)
:=\int |\partial_sU|(1+|y|)e^{-|y|^2/8}dy
\ge v_*>0
}
\]

for every sufficiently late `s`.

For exact DSS, if

\[
A_*:=\sup_s\|\partial_s^2U\|_{X_G}<\infty,
\]

periodicity gives

\[
\boxed{
S\ge2v_*/A_*,
\qquad
\lambda=e^{S/2}\ge e^{v_*/A_*}>1.
}
\]

Thus arbitrarily small DSS periods are excluded on this certified lane, but arbitrary DSS is not.

## 8. Exact DSS hard core — M19-092 and M19-098--101

M5-566 did **not** eliminate DSS. It left the nonzero log-periodic critical tail

\[
\boxed{
U(y,s)
=\frac1r a(\log r-s/2,\omega)+O(r^{-3}),
\qquad
a(q+L)=a(q),
\qquad
a\ne0.
}
\]

Barker--Prange quantitative DSS concentration gives, when its hypotheses apply,

\[
\boxed{
\frac1L
\int_0^L\int_{S^2}|a|^3d\omega dq
\ge2c_M>0.
}
\]

Exact DSS symmetry Floquet multipliers are

\[
\boxed{
\begin{array}{c|c}
\text{mode}&\mu\\
\hline
\text{space translation}&\lambda\\
\text{blowup-time shift}&\lambda^2\\
\text{scaling/time phase}&1\\
\text{rotation}&1\\
\text{Galilean boost}&\lambda^{-1}.
\end{array}}
\]

For the one-period vorticity monodromy,

\[
\boxed{
r_{ess}(\mathcal M_S)\le e^{-S/4}<1.}
\]

Hence every unit Floquet multiplier is discrete and finite-multiplicity. After symmetry modulation, any extra unit multiplier is a finite-dimensional Fredholm-kernel problem.

However

\[
\boxed{
\text{DSS nondegeneracy}\neq\text{DSS nonexistence}.
}
\]

The nonlinear periodic orbit itself remains a genuine hard branch.

## 9. Boundary-history interpretation — M19-100

At fixed spectator radius `R_spec=e^{rho_spec}`,

\[
q=\rho_{spec}-\theta_{cross}/2.
\]

After M19-095, the long q-history is best viewed as a long observation of a finite-dimensional interior center flow, not as an independent infinite-dimensional degree of freedom.

Thus the weak-critical problem has separated into two live analytic tasks:

\[
\boxed{
\mathcal T_{extra-center}: E^c_{extra}=0
}
\]

and

\[
\boxed{
\mathcal T_{DSS}^{critical}:
\text{exclude the nonzero exact log-periodic DSS orbit for arbitrary admissible }\lambda.
}
\]

## 10. Current immediate targets after M19-101

1. **Extra-center spectral ordering:** exploit sign/orientation or a compact-core index beyond unsigned derivative magnitude to prove the top symmetry-transverse center exponent is negative.
2. **DSS nonlinear return-map rigidity:** use the finite-dimensional Fredholm reduction together with the period floor, nonzero cubic tail floor, and exact symmetry multipliers; do not confuse nondegeneracy with nonexistence.
3. **External theorem applicability audit:** certify Type-I and physical pressure-annulus hypotheses before using the Pineau--Vicol one-slice gate in the global root chain.

## 11. Final proof-chain certification remains open

Even if both live analytic tasks close, global regularity still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness and remaining alignment/nonreuse checks;
3. full beginning-to-end independent audit.

\[
\boxed{
\text{M19 ACTIVE TIP = M19-101.}
}
\]
