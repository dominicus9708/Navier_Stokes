# M19 Current Frontier

**Date:** 2026-09-14  
**Current tip:** **M19-252**  
**Status:** ACTIVE CALCULATION / APERIODIC SIGNED-INVARIANT FRONTIER + BOUNDED-PERIOD CAVITY CORE + SHELL DECOMPACTIFICATION/VARIABLE-COEFFICIENT RESOLVENT FRONTIER / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active new-calculation/closure family. Historical modules remain authoritative for detailed derivations; this file records the latest theorem obligations and scope firewalls.

## 2. Aperiodic recurrent hard frontier

The certified recurrent hard machinery still forces

\[
\overline P_U\ge\mathcal P_*>0,
\qquad
\left\langle(K\Gamma W)^{3/2}\right\rangle\ge c_0\nu\mathcal P_*>0
\]

on the retained simultaneous W1 lane. M19-196--201 show that this does not yet yield an unsigned global contradiction. Therefore

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

remains OPEN.

## 3. Finite hard resonance and physical-adjoint reduction — M19-211--230

On the complete hard bundle,

\[
B(q,\omega)=\sum_j e^{i\kappa_jq}b_j(\omega),
\qquad
\kappa L+\vartheta-m\alpha=2\pi n,
\]

with finite bounds

\[
|\kappa_j|\le K_q^*,
\qquad
|n|\le N_{res}.
\]

M19-211--223 establish parity/skew-crossing/Pfaffian/phase-gap reductions and the zero-q invariant-section firewalls. M19-224--228 identify the critical primal/adjoint homogeneities and the exact Green flux, while M19-226 records the Fredholm-circularity firewall for arbitrary nonorthogonal adjoint realization.

M19-229--230 localize the physical adjoint extension problem to the finite-spectator cavity equation

\[
(I-\mathcal M_R^{ad})z_0=h_R,
\]

where \(\mathcal M_R^{ad}\) is compact and \(I-\mathcal M_R^{ad}\) is Fredholm of index zero. Large-R Poincare contraction is unavailable.

## 4. Expanding-cavity dichotomy and escape currency — M19-231--237

Normalized cavity unit modes satisfy

\[
\boxed{
\text{nonzero whole-space relative-periodic core limit}
\quad\lor\quad
\text{escape of all L2 mass from every fixed compact set}.}
\]

On the escape branch,

\[
\boxed{
\int_0^{S_j}\|\nabla w_j\|_2^2ds
\to\frac1{4\nu},
\qquad
\int_0^{S_j}\|\eta_j\|_2^2ds
\to\frac1{4\nu}.}
\]

Localized vorticity identities force the vorticity-energy measure to the relative boundary and give the shear payer

\[
\boxed{
\liminf_j\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2dSds
\ge\frac1{8\nu^2}.}
\]

The natural no-slip inner coordinate

\[
z=\frac{R}{2\nu}(R-r)
\]

gives

\[
f_{zz}+f_z=0,
\qquad
f=1-e^{-z},
\qquad
d_{BL}\asymp\nu/R.
\]

This local layer is asymptotically consistent and therefore not itself a contradiction.

## 5. Regular macroscopic bulk and scale separation — M19-238--240

With

\[
x=y/R_j,
\qquad
V_j=R_j^{3/2}w_j(R_jx),
\]

any regular macroscopic curl limit satisfies

\[
\partial_sZ+\frac12x\cdot\nabla Z+Z=0,
\]

and relative periodicity forces \(Z=0\). The inherited H(div) zero-normal trace then forces every regular curl-free/divergence-free macroscopic weak limit to vanish.

Thus every nonzero regular macroscopic weak bulk is excluded.

The no-slip shell inequality

\[
\int_{R-D<|y|<R}|w|^2
\le CD^2\int|\nabla w|^2
\]

also shows that velocity mass cannot collapse into the inner \(\nu/R\) vorticity layer. Any escape requires a thicker velocity reservoir plus the thinner no-slip/vorticity payer.

## 6. Bare toroidal and Gaussian full-operator audit — M19-241--243

For \(U=0\), the toroidal pressure-free operator

\[
A_0=\nu\Delta-\frac12y\cdot\nabla-\frac12
\]

satisfies

\[
e^{-|y|^2/(8\nu)}A_0e^{|y|^2/(8\nu)}
=
\nu\Delta+\frac14-\frac{|y|^2}{16\nu},
\]

so

\[
\boxed{\sup\sigma\le-1/2.}
\]

Hence no bare toroidal relative unit multiplier exists.

For the full equation, the Gaussian identity is

\[
\begin{aligned}
\frac12\frac d{ds}\int\rho|w|^2
+\nu\int\rho|\nabla w|^2
+\frac12\int\rho|w|^2
={}&-\frac1{4\nu}\int\rho(U\cdot y)|w|^2\\
&-\int\rho w^TS_Uw
-\frac1{2\nu}\int\rho\pi(y\cdot w),
\end{aligned}
\]

with \(\rho=e^{-|y|^2/(4\nu)}\). The pressure obeys

\[
\boxed{\Delta\pi=-2\partial_iU_j\partial_jw_i,}
\]

but boundary pressure can still be driven by no-slip derivatives. M19-243 therefore compressed the full Gaussian defects to critical radial transport plus radial/poloidal boundary response.

## 7. Radial-free reduction and passive boundary impedance — M19-244--245

At critical order

\[
U=r^{-1}(A_r\omega+A_T)+\cdots,
\]

incompressibility gives

\[
(\partial_q+1)A_r+\operatorname{div}_{S^2}A_T=0.
\]

If \(A_r=0\), the leading tangential background is toroidal and the Gaussian transport defect vanishes at critical order.

The inner layer has the leading Dirichlet-to-Neumann law

\[
\boxed{
\partial_nw_T|_{S_R}
=-\frac{R}{2\nu}a_T,
}
\]

and viscous dissipation

\[
\boxed{
\mathcal D_{BL}^{(0)}
=\frac R4\int_{S_R}|a_T|^2dS.
}
\]

Thus the \(\nu/R\) layer is a passive dissipative impedance, not an energy source.

## 8. Distance-to-wall pressure currency and its exact local saturation — M19-246--247

Using

\[
a_D(d)=D(1-e^{-d/D}),
\qquad d=R-r,
\]

the one-period weighted energy identity forces, for a shell carrying positive detected mass \(M_D\),

\[
\boxed{
\mathcal W_{P,D}(R)
:=-\int e^{-d/D}\pi w_r
\gtrsim\frac R4M_D
}
\]

up to lower-order terms.

This is not a contradiction. At fixed physical shell distance, the canonical leading scaling

\[
w_T=R^{-1}v_T,
\qquad
w_r=R^{-2}v_r,
\qquad
\pi=Rp_0
\]

gives

\[
\partial_dp_0=0,
\qquad
\frac12\partial_dv_T=\nabla_{S^2}p_0,
\qquad
v_T(0)=0,
\]

hence

\[
\boxed{
v_T=2d\nabla_{S^2}p_0,
\qquad
v_r=d^2\Delta_{S^2}p_0.
}
\]

This profile exactly saturates

\[
\boxed{
\mathcal W_{P,D}
=\frac R4M_D+o(R).
}
\]

Thus linear pressure-work growth is the leading poloidal shell balance, not a closure theorem.

## 9. Half-line rigidity excludes every regular single-scale sublinear shell — M19-248--250

The local profile above grows linearly in boundary distance and is not in half-line \(L^2\) unless \(\nabla_{S^2}p_0=0\). Therefore a nonzero regular fixed-thickness tight shell is impossible.

M19-249 extends this to every single sublinear shell scale \(D=o(R)\). With

\[
\xi=\frac{R-r}{D},
\qquad
V_T=R\sqrt D\,w_T,
\qquad
V_r=\frac{R^2}{\sqrt D}w_r,
\qquad
P=\frac{D^{3/2}}R\pi,
\]

the universal regular leading equations are

\[
\partial_\xi P_0=0,
\qquad
\frac12\partial_\xi V_T=\nabla_{S^2}P_0,
\qquad
V_T(0)=0.
\]

Hence

\[
V_T=2\xi\nabla_{S^2}P_0,
\]

and scale-tight half-line \(L^2\) again forces \(V_T=V_r=0\).

M19-250 removes the radial-free restriction. In physical shell coordinates

\[
\boxed{
\frac{|U_r\partial_dw|}{|(R/2)\partial_dw|}=O(R^{-2}),
}
\]

so the critical radial background is subleading in the local shell PDE even though \(U\cdot y\) is order one in the Gaussian weighted energy.

Permanent correction:

\[
\boxed{
U\cdot y=O(1)\text{ in Gaussian energy}
\neq
U_r\partial_r\text{ is leading in physical shell dynamics}.
}
\]

Therefore **no regular single-scale sublinear shell survives for a general critical background**. Any escape survivor must lose scaled compactness or become macroscopic; the regular macroscopic limit was already closed by M19-238--239.

## 10. Frozen full shell determinant — M19-251

Flatten the remote boundary and freeze the bare similarity drift. For tangential Fourier magnitude \(k\), a homogeneous viscous exponent \(\alpha\) obeys

\[
F(\alpha)
=
\lambda-
u(\alpha^2-k^2)+\frac R2\alpha+\frac12=0.
\]

The pressure harmonic has exponent \(k\). In the poloidal sector, simultaneous normal and tangential no-slip matching requires \(\alpha=k\), hence \(F(k)=0\).

For a unit/Floquet mode \(\operatorname{Re}\lambda=0\),

\[
\boxed{
\operatorname{Re}F(k)
=\frac12+rac{Rk}{2}>0.
}
\]

Therefore no bare frozen half-space poloidal unit mode exists. Combined with M19-241, both toroidal and poloidal bare local unit shell modes are excluded.

## 11. High angular/Floquet frequency strengthens the frozen gap — M19-252

For \(\lambda=i\omega\),

\[
\boxed{
|F(k)|^2
=
\left(\frac12+rac{Rk}{2}\right)^2+\omega^2.
}
\]

The viscous-root discriminant is

\[
\Delta_\alpha
=
\frac{R^2}{4}+4\nu\left(\nu k^2+\frac12+i\omega\right),
\]

and has exactly one decaying viscous root for every \(k\ge0\), \(\omega\in\mathbb R\).

Thus large tangential/angular frequency and large Floquet frequency move the frozen boundary determinant farther from zero, not closer. Frequency blow-up alone is not a local resonance mechanism.

The remaining shell danger is therefore variable-coefficient curvature/mode conversion, global multiscale coupling, or failure of a uniform localization/resolvent comparison between the true cavity and the frozen shell model.

## 12. Current bounded-period frontier

The M19-230 cavity obstruction is now sharpened to two live families.

### B1. Core branch

\[
\boxed{
\mathcal T_{cav}^{core}:
\text{classify/exclude nonzero whole-space relative-periodic core limits and establish the needed hard-bundle membership bridge}.}
\]

### B2. Decompactifying/variable-coefficient escape branch

The regular pressure-supported shell branch is no longer independent. Any escape survivor must violate the compact shell hypotheses used above or exploit global variable-coefficient coupling:

\[
\boxed{
\mathcal T_{cav}^{decomp}:
\begin{array}{l}
\text{control scaled radial/angular/time/pressure/profile decompactification,}\\
\text{and prove the frozen no-unit determinant survives localization to the actual variable-coefficient cavity.}
\end{array}}
\]

At theorem-obligation level,

\[
\boxed{
\mathcal T_{cav}^{comp}
\subset
\mathcal T_{cav}^{core}
\cup
\mathcal T_{cav}^{decomp}.
}
\]

The previous standalone \(\mathcal T_{shell}^{rad-pol}\) is superseded by this reduction.

## 13. Live theorem complex

Aperiodic:

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

OPEN.

Bounded period:

\[
\boxed{
\mathcal T_{cav}^{core}
\cup
\mathcal T_{cav}^{decomp}}
\]

OPEN.

Long period conditionally merges into the above or compactness loss by M19-205.

## 14. Final proof-chain certification remains open

Even if the live M19 theorem complex closes, global regularity still requires:

1. arbitrary-singularity entry certification (`ROOT-CERT`);
2. historical non-CE-H branches `CP-E`, `CP-S`, `CE-T`, `Migration`;
3. parent-to-late-branch alignment/nonreuse checks;
4. full beginning-to-end independent audit.

## 15. Permanent firewalls through M19-252

\[
\boxed{\text{cavity core limit}\neq\text{certified hard kernel without a membership bridge}},
\]
\[
\boxed{\text{relative vorticity boundary localization}\neq\text{velocity mass in the same thin layer}},
\]
\[
\boxed{\text{local }\nu/R\text{ layer consistency}\neq\text{global unit multiplier existence}},
\]
\[
\boxed{\text{zero regular macroscopic weak limit}\neq\text{strong L2 compactness}},
\]
\[
\boxed{\text{Gaussian weighted gap}\neq\text{unweighted boundary-shell exclusion}},
\]
\[
\boxed{\text{passive boundary impedance}\neq\text{global unit-multiplier exclusion}},
\]
\[
\boxed{\text{linear-in-R pressure-work requirement}\neq\text{shell contradiction}},
\]
\[
\boxed{\text{leading poloidal shell normal form}\neq\text{global relative-periodic eigenmode}},
\]
\[
\boxed{\text{no regular single-scale shell survivor}\neq\text{control of decompactification}},
\]
\[
\boxed{U\cdot y=O(1)\text{ in Gaussian energy}\neq U_r\partial_r\text{ leading in physical shell dynamics}},
\]
\[
\boxed{\text{frozen half-space determinant gap}\neq\text{uniform full-cavity resolvent gap}},
\]
\[
\boxed{\text{high-frequency frozen gap}\neq\text{full variable-coefficient high-frequency exclusion without localization control}},
\]
\[
\boxed{\text{root-class merger}\neq\text{analytic closure}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-252.}}
\]
