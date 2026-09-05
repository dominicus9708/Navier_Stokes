# M17 — Material director geometry, weighted-harmonic rank, and nodal topology

Canonical continuation split from M16 after M16-023.

Recompressed at **M17-184**. Detailed derivations, corrections, provenance, and DSD audits remain in the individual canonical modules.

---

# 1. Canonical split

\[
\boxed{
B_{dir}
\Longrightarrow
R_1^{great-circle/winding}
\ \lor\
R_2^{director-area}.
}
\]

Canonical reassignment:

- **M17-001** = provisional M16-024
- **M17-002** = provisional M16-025
- **M17-003** = provisional M16-026
- **M17-004** = provisional M16-027
- **M17-005** = provisional M16-028

The axisymmetric no-swirl class remains an explicit known-regular Rank-1 firewall.

---

# 2. M17-006 — M17-096: foundational Rank-1/Rank-2 geometry

## Rank-1 great-circle system

\[
W_h=J\nabla_hq,
\qquad
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q.
\]

The reduced material label flow is

\[
(q',x_3')=(\mathscr H,K),
\qquad
\partial_q\mathscr H+\partial_3K=\kappa,
\]

and its Jacobian equals the M5 amplification factor

\[
\boxed{J_L=a=\exp\int\kappa.}
\]

## Rank-2 pure-kernel system

\[
J_\xi=|J_\xi|k,
\qquad
D_k\xi=0.
\]

Same-marker comparable recurrence forces

\[
(\langle\sigma\rangle,\langle\sigma_k\rangle,\langle\sigma_n\rangle)
=(-1/2,1,-1/2),
\]

and, with comparable normalized amplitude,

\[
\langle\kappa\rangle=3/2.
\]

## Vertical Rank-1 pressure lock

The vertical branch is independent of the slant limit and yields

\[
G_q=1,
\qquad
\partial_3\lambda=0,
\]

\[
\boxed{
V_V:=\Delta(\partial_3\lambda_h)
=-\frac12H_V,
\qquad
H_V:=\mathcal H_{333}.
}
\]

with

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel},
\qquad
\boxed{\langle\Pi_V^{prod}+\Pi_V^{rel}\rangle=0}
\]

on a compact recurrent vertical core.

At the vertical nodal filament,

\[
\boxed{
O_V=-\frac15|Q|_F^2\kappa_3,
\qquad
h_{nodal}=(B_3-v_0)\kappa_3.
}
\]

These are valid nodal identities, but the later direct M5 flux-label substitution is corrected below.

---

# 3. M17-097 — M17-163: Rank-2 carrier, ribbon, tail, and OU/Liouville frontier

Peak sheets inherit frozen director-area flux. Tangency/type switching is mostly signed-flux recyclable.

Same-material compact critical-ribbon recurrence is excluded, but fresh-carrier Eulerian recurrence survives.

Remote critical tails reduce to a low-amplitude strong-director skeleton

\[
\rho\to0,
\qquad
|J_\xi|\gtrsim1,
\qquad
\Phi_J\gtrsim1.
\]

On quiet critical spacetime blocks, positive-fraction strain recharge is excluded; dominant carriers must undergo geometry/type transition within bounded log-radius distance.

The relative-thick low-amplitude bounded-`kappa` packet branch has an OU limit

\[
\partial_\tau V+\frac12z\cdot\nabla V=\Delta V-V.
\]

Bounded CE-H potential plus finite fixed-lag normalized mass is incompatible with a nonzero eternal OU packet. Remaining Rank-2 exits are thin/nodal, unbounded-`kappa`, ancestor concentration, critical multiplicity/occupancy, or interface/domain exits.

---

# 4. M17-164 — M17-171: valid nodal local/global pressure architecture

These results remain valid independently of any M5 flux-label bridge.

## Small-core reproducing coefficient

For radial cutoff `chi_R`,

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac67m_\chi R^2O_V+O(R^3).
}
\]

For a sharp ball,

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac37R^2O_V+O(R^3).
}
\]

## Radial scale current

With

\[
P(R)=-\int_{|z|<R}\kappa\rho^2K_{333}dz,
\qquad
A(R)=R^{-2}P(R),
\]

one has

\[
A(0)=\frac37O_V,
\qquad
A(\infty)=0,
\]

and therefore

\[
\boxed{
O_V=-\frac73\int_{-\infty}^{\infty}\partial_sA(e^s)ds.
}
\]

## Positive-palinstrophy representation

\[
\kappa\rho^2
=\frac12\Delta\rho^2-|\nabla W|^2.
\]

At the vertical nodal filament,

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=\langle|\nabla W|^2,K_{333}\rangle.
}
\]

Outer sign reversal requires positive weighted palinstrophy occupancy.

## Semilinear Hessian architecture

In the nodal gauge,

\[
\boxed{H_V=F_{33},}
\qquad
\boxed{O_V=-\frac15|Q|_F^2F_{q3}.}
\]

Define

\[
\mathbf J_F=(F_{33},-F_{q3})=\nabla^\perp F_3.
\]

Then

\[
\nabla\cdot\mathbf J_F=0
\]

and on a regular `kappa=0` curve

\[
\mathbf J_F\cdot n_\kappa
=\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}{|\nabla\kappa|}.
\]

The corresponding closed-loop identity is the periodicity of `F_3`, not a second independent conserved charge.

---

# 5. M17-172 — M17-177: conditional zero-worldsheet / variance branch

These modules developed a useful conditional geometry, but their **M5-forced sign/variance statements are not unconditional** after the M17-178--183 audit.

The `(kappa,F_3)` hodograph has Jacobian

\[
\boxed{
J_\Xi
=F_{qq}H_V-25O_V^2/|Q|_F^4.
}
\]

A reduced-label countermodel shows that uniform hodograph nondegeneracy and M5-type hysteresis are kinematically compatible.

Conditional on an additional M5-to-nodal localization/pushforward hypothesis, one may obtain zero-loop pressure variance and tangential higher-jet occupancy. M17-182 shows that even then the exact moving-loop variance transport is signed and noncoercive.

---

# 6. M17-178 — M17-183: corrective Rank-1 measure/support audit

## M17-178 — M5 transverse-flux labels do not live on the nodal filament

M5-647 defines `dmu_0` on regular vortex-line flow boxes with `W != 0`; the analytic zero set carries zero vorticity-flux density.

M17-090's `O_V` is defined on the vertical nodal filament with `W=0`.

Therefore M17-095's label-by-label substitution requires an additional regular-label-to-nodal-core map and is not an unconditional identity.

## M17-179 — exact regular great-circle flux coordinates

On a regular great-circle transverse chart

\[
X(q,z)=(x_h(q,z),z),
\qquad
\partial_qx_h=\frac{\nabla_hq}{|\nabla_hq|^2},
\]

one has

\[
\boxed{|W\cdot(X_q\times X_z)|=1.}
\]

Hence

\[
\boxed{|d\Phi_W|=dq\,dz.}
\]

Since `J_L=a`,

\[
\boxed{a\,d\mu_0=dq\,dx_3}
\]

on adapted regular great-circle charts.

Thus the regular M5 current has the exact coarea form

\[
\boxed{
G_\Phi(0)
=\int_{\Gamma_0^{reg}}
\frac{h}{|\nabla_{(q,x_3)}\kappa|}ds.
}
\]

The nodal critical level remains a boundary trace rather than an ordinary regular flux label.

## M17-180 — global current sign does not fix nodal boundary trace

An explicit reduced-label model with

\[
\kappa=z,
\qquad
V_L=(0,j(q)+z^2/2)
\]

satisfies

\[
\nabla\cdot V_L=\kappa,
\qquad
h|_{\kappa=0}=j(q).
\]

One may have

\[
G_\Phi(0)=\int j(q)dq<0
\]

while

\[
j(0^+)>0.
\]

Therefore the global M5 sign cannot determine the nodal trace without a PDE-specific localization theorem.

## M17-181 — regular M5 crossing local `l=3` tensor

At a regular positive-vorticity `kappa=0` crossing, with `R=rho^2`,

\[
\boxed{
\mathcal O_{reg}^{(3)}
=-STF_3\!\left[
\frac16\operatorname{sym}(\nabla\kappa\otimes\nabla^2R
+\nabla R\otimes\nabla^2\kappa)
+\frac{R}{6}\nabla^3\kappa
\right].
}
\]

M5-682 controls only

\[
\boxed{
L_\rho\kappa
=\operatorname{tr}\nabla^2\kappa
+\frac{\nabla R\cdot\nabla\kappa}{R},
}
\]

plus strain/geometric channels. It does not fix the STF second jet or third `kappa` jet, so `h` does not determine the regular local `l=3` orientation.

## M17-182 — zero-loop pressure variance is not a new dissipation budget

For

\[
W_\Gamma
=V_L-\frac{h}{|\nabla\kappa|}n_\kappa,
\]

one has

\[
D_\Gamma H_V
=\Pi_V^{prod}+\Pi_V^{rel}
-\frac{h}{|\nabla\kappa|}\partial_nH_V.
\]

The coarea measure evolves by

\[
\Lambda_\Gamma
=-\nabla\cdot\left(\frac{h}{|\nabla\kappa|}n_\kappa\right).
\]

Thus for `u=H_V-bar H`,

\[
\boxed{
V_H'
=2\int u\left(\Pi_V^{prod}+\Pi_V^{rel}
-\frac{h}{|\nabla\kappa|}\partial_nH_V\right)d\nu
+\int u^2\Lambda_\Gamma d\nu.
}
\]

Every term is signed. Pressure variance/higher-jet occupancy is not by itself a monotone temporal cost.

## M17-183 — high-amplitude M5 labels and nodal cores are disjoint material strata

M5-681 uses a retained high-amplitude positive-vorticity material ensemble.

CE-H gives

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\]

so

\[
\boxed{\{\rho>0\}\text{ and }\{\rho=0\}}
\]

are disjoint material-invariant strata on every finite regular interval.

Therefore a same-material M5-label-to-nodal-core bridge is impossible. M17-095 is retracted in that interpretation.

Any valid coupling must be Eulerian/spatial and explicitly control localization, multiplicity, and sign transfer.

---

# 7. M17-184: exact regular M5 flux/enstrophy joint kinetics

For a regular closed great-circle vortex loop,

\[
\boxed{
L_\rho(q,x_3)
=\oint\rho\,ds
=\oint|\nabla_hq|ds.
}
\]

M5-684 gives

\[
L_\rho'
=\left(\kappa-\frac12+2\bar\sigma_\rho\right)L_\rho.
\]

Lift the current flux population to the joint state `(kappa,L_rho)`:

\[
P(k,\ell,\theta)
=\int\delta(k-\kappa)\delta(\ell-L_\rho)d\Phi.
\]

Then

\[
\boxed{
\partial_\theta P
+\partial_kG_k
+\partial_\ell G_\ell
=kP.
}
\]

Its first `L_rho` moment gives the exact enstrophy-current law

\[
\boxed{
\partial_\theta F_E
+\partial_kG_E
=\left(2k-\frac12\right)F_E
+2S_\rho,
}
\]

where

\[
S_\rho(k)
=\int\bar\sigma_\rho L_\rho\delta(k-\kappa)d\Phi.
\]

Combined with M5-683, this converts the old flux/enstrophy measure mismatch into one explicit three-way balance among

\[
\boxed{
\nabla\kappa,
\qquad
\nabla\sigma,
\qquad
\bar\sigma_\rho L_\rho.
}
\]

No sign contradiction follows yet.

---

# 8. Current corrected Rank-1 frontier

The Rank-1 problem now splits into two disjoint material blocks:

\[
\boxed{
R_{1,V}
\Longrightarrow
R_V^{regular\ M5\ conveyor}
\ \oplus\
R_V^{nodal\ pressure/octet}.
}
\]

### Regular M5 block

Exact facts:

\[
a\,d\mu_0=dq\,dx_3,
\]

\[
\partial_\theta P+\partial_kG_k+\partial_\ell G_\ell=kP,
\]

and M5-683 supplies the `kappa`-space diffusion/mixed-gradient constitutive current.

Highest-value open question:

\[
\boxed{
\text{control the weighted line strain }
\bar\sigma_\rho
\text{ on closed winding loops.}
}
\]

### Nodal pressure/octet block

Exact facts:

\[
O_V=-\frac15|Q|^2\kappa_3,
\qquad
H_V=F_{33},
\]

plus the local/global pressure-production and palinstrophy identities.

Highest-value open question:

\[
\boxed{
\text{find an Eulerian localization/covariance theorem coupling regular flux labels to nodal geometry,}
}
\]

or close the nodal pressure block independently.

---

# 9. Current Rank-2 frontier

\[
\boxed{
R_{2,ribbon}^{remote}
\Longrightarrow
H_{1,crit}^{spacetime}
\lor
G_{thin/nodal}
\lor
G_{\kappa,\infty}
\lor
G_{ancestor\ concentration}
\lor
G_{critical\ multiplicity/occupancy}
\lor
G_{domain/interface}.
}
\]

The relative-thick quiet bounded-`kappa` finite-lag packet branch is closed by the OU/Liouville mechanism.

---

# 10. DSD audit state

The following shortcuts are explicitly rejected:

1. winding is not itself singular;
2. scalar `kappa` payer cannot replace global `l=3` pressure architecture;
3. label, spatial, coarea, director-flux, and enstrophy measures are not interchangeable;
4. moving maxima are not material markers;
5. Rank-1 and Rank-2 material carrier strata do not convert on a finite regular interval;
6. same-material compact ribbon recurrence is excluded, fresh-carrier Eulerian recurrence is not;
7. the earlier `K^2` historical turnover-count inference is retracted;
8. blind higher differentiation does not close normalized-jet branches;
9. OU/Liouville closure requires amplitude-relative compactness and bounded `kappa`;
10. pure volume packing does not close critical multiplicity;
11. M17-095's direct same-material M5-to-nodal octupole bridge is retracted;
12. M5-685's negative weighted zero-current is a kinematic source-balance fact, not by itself a new PDE burden;
13. M17-165 and the M5-forced parts of M17-172--177 are conditional on an additional nodal localization/trace theorem;
14. positive spatial pressure variance is not automatically a temporal dissipation cost;
15. global regularity remains unproved.

---

# 11. Highest-value next gates

## 1. Regular Rank-1 line-strain gate

Use the great-circle strain-eigenline equations to constrain

\[
\boxed{
\bar\sigma_\rho
=\frac{\oint\sigma|\nabla_hq|ds}
{\oint|\nabla_hq|ds}.
}
\]

A sign, recurrence law, or coercive identity for this quantity would directly couple M5-681 to the M5-683 diffusion current.

## 2. Eulerian regular-to-nodal localization

Determine whether a controlled portion of the regular `kappa=0` current must concentrate near a winding nodal critical level. Without such a theorem, M5 cannot force the nodal `O_V` sign.

## 3. Rank-2 critical multiplicity/occupancy

Return to the M5 growing-window Hardy/packet packing frontier if the independent Rank-1 routes do not close.

---

# Proof status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
