# M17 — Material director geometry, weighted-harmonic rank, and nodal topology

Canonical continuation split from M16 after M16-023.

Recompressed at **M17-177**. Detailed derivations, corrections, provenance, and DSD audits remain in the individual canonical modules.

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

# 2. Phase catalog

## M17-006 — M17-023: Rank-1 winding / nodal geometry

Material nodal filaments, finite analytic nodal order, nodal-Jacobian multiplier laws, positive-`kappa` sheath / negative-`kappa` payer separation, closed `(q,x_3)` label flow, and angular-defect dynamics.

Core semilinear structure:

\[
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q.
\]

The reduced material label flow satisfies

\[
(q',x_3')=(\mathscr H,K),
\qquad
\partial_q\mathscr H+\partial_3K=\kappa,
\]

and its Jacobian equals the M5 amplification factor

\[
\boxed{J_L=a=\exp\int\kappa.}
\]

## M17-024 — M17-042: Rank-2 director-area / pure-kernel geometry

Director-area current and the full-rank pure-transverse-kernel frame

\[
J_\xi=|J_\xi|k,
\qquad
D_k\xi=0.
\]

Same-marker comparable recurrence forces the resonant mean frame

\[
(\langle\sigma\rangle,\langle\sigma_k\rangle,\langle\sigma_n\rangle)
=(-1/2,1,-1/2),
\]

and, with comparable normalized amplitude,

\[
\langle\kappa\rangle=3/2.
\]

## M17-043 — M17-070: Rank-1 pressure / cubic STF architecture

The Rank-1 pressure branch is reduced to local payer-octupole information versus the global sign-changing `l=3` STF pressure tensor.

Principal recurrent slant local octupole modes are closed. Oblique slant remains a driven cocycle / global-lock branch.

## M17-071 — M17-096: Rank-2 compensation and vertical Rank-1 restoration

Rank-2 regular maxima require positive Riccati compensation. Finite critical-type and top-jet architectures are developed.

The vertical Rank-1 branch is restored independently of the slant limit and yields

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

The global pressure coordinate obeys

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel},
\]

and compact recurrence requires

\[
\boxed{\langle\Pi_V^{prod}+\Pi_V^{rel}\rangle=0.}
\]

At a regular vertical `kappa=0` crossing,

\[
\boxed{
O_V=-\frac15|Q|_F^2\kappa_3,
\qquad
h=(B_3-v_0)\kappa_3
=-\frac{5r_V}{|Q|_F^2}O_V.
}
\]

M5 hysteresis gives in the original base-label measure

\[
\boxed{
\overline{\int a\frac{r_VO_V}{|Q|_F^2}\delta(\kappa)d\mu_0}>0.
}
\]

## M17-097 — M17-142: Rank-2 inherited director-flux carriers / critical ribbons

Peak sheets inherit the frozen director-area flux measure. Tangency/type switching is mostly signed-flux recyclable.

Same-material complete compact critical-ribbon recurrence is excluded, but fresh-carrier Eulerian recurrence survives.

Remote critical tails reduce to a low-amplitude strong-director skeleton

\[
\rho\to0,
\qquad
|J_\xi|\gtrsim1,
\qquad
\Phi_J\gtrsim1.
\]

On a quiet critical spacetime block, positive-fraction strain recharge is excluded; dominant carriers must undergo geometry/type change within bounded log-radius distance.

## M17-143 — M17-154: fold-driver / normalized high-jet audit

The true generic fold driver is

\[
A_T=D_\xi(\sigma+\kappa).
\]

The recurrent quiet axial convexity payer is closed. Mixed/transverse payers climb a `kappa` / `log rho` jet ladder, and blind higher differentiation is explicitly stopped as non-closing.

## M17-155 — M17-163: whole-packet OU/Liouville reduction

Relative-thick low-amplitude bounded-`kappa` packets converge on quiet remote corridors to

\[
\boxed{
\partial_\tau V+\frac12z\cdot\nabla V=\Delta V-V.
}
\]

Bounded CE-H potential plus finite fixed-lag normalized packet mass is incompatible with a nonzero eternal OU packet. Strong fixed-lag forgetting also requires order-one non-OU action; comoving-dilation cutoffs remove pure similarity-dilation replenishment.

The remaining Rank-2 mass escape is concentration or critical multiplicity/occupancy. Pure volume packing is too weak.

---

# 3. M17-164 — M17-168: local octupole enters the actual global `kappa` pressure-production channel

## M17-164 — exact small-core reproducing coefficient

For a radial cutoff `chi_R`,

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac67m_\chi R^2O_V+O(R^3),
\qquad
m_\chi=\int_0^\infty\chi(s)sds.
}
\]

For a sharp ball,

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac37R^2O_V+O(R^3).
}
\]

Thus the local payer octupole is the exact first small-core coefficient of the genuine global `-kappa rho^2` axial pressure-production source.

## M17-165 — M5 hysteresis acts directly on localized pressure production

Within the original M5 label measure,

\[
\mathcal C_R
:=\int a\frac{r_V}{|Q|_F^2}
\frac{\Pi_{V,\kappa}^{core}(R)}{R^2}
\delta(\kappa)d\mu_0
\]

satisfies

\[
\boxed{\lim_{R\to0}\overline{\mathcal C_R}>0.}
\]

This removes the old local-source mismatch without replacing `dmu_0` by spatial volume.

## M17-166 — exact radial scale-current sum rule

Let

\[
P(R)=-\int_{|z|<R}\kappa\rho^2K_{333}dz,
\qquad
A(R)=R^{-2}P(R).
\]

Then

\[
A(0)=\frac37O_V,
\qquad
A(\infty)=0
\]

when the full moment is finite. Hence, with `s=log R`,

\[
\boxed{
O_V=-\frac73\int_{-\infty}^{\infty}\partial_sA(e^s)ds.
}
\]

Outer cancellation is therefore a signed radial `l=3` scale-current ledger, not arbitrary freedom.

## M17-167 — positive-palinstrophy representation

CE-H gives

\[
\kappa\rho^2
=\frac12\Delta\rho^2-|\nabla W|^2.
\]

On the vertical nodal filament, `W=0` and `partial_3W=0`, so the local distributional correction vanishes and

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=\langle|\nabla W|^2,K_{333}\rangle.
}
\]

Thus the global `kappa` production is the axial `l=3` angular moment of a **positive palinstrophy density**.

## M17-168 — outer sign reversal costs positive weighted palinstrophy

If the full global `kappa` production neutralizes or reverses the small-core octupole orientation, then for sufficiently small regular `R_0`,

\[
\boxed{
\int_{|z|>R_0}
|\nabla W|^2|z|^{-4}dz
\gtrsim R_0^2|O_V|.
}
\]

This is a positive spatial occupancy requirement, not yet a nonrecyclable temporal cost.

---

# 4. M17-169 — M17-175: semilinear Hessian / zero-worldsheet / hodograph architecture

## M17-169 — one Hessian contains both local and global descriptors

In the nodal gauge `q=0` along the vertical filament,

\[
\boxed{H_V=F_{33},}
\qquad
\boxed{O_V=-\frac15|Q|_F^2F_{q3}.}
\]

If `F_qq !=0`, the critical value along `F_q=0` satisfies

\[
\boxed{
H_V=\mathcal C_{*,33}
+\frac{25O_V^2}{|Q|_F^4F_{qq}}.
}
\]

## M17-170 — divergence-free semilinear Hessian current

Define

\[
\boxed{\mathbf J_F=(F_{33},-F_{q3}).}
\]

Then

\[
\nabla_{(q,3)}\cdot\mathbf J_F=0.
\]

On a regular `kappa=0` curve,

\[
\boxed{
\mathbf J_F\cdot n_\kappa
=\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}{|\nabla\kappa|}.
}
\]

For a closed component,

\[
\boxed{
\oint\frac{F_{qq}H_V}{|\nabla\kappa|}ds
=25\oint\frac{O_V^2}{|Q|_F^4|\nabla\kappa|}ds.
}
\]

## M17-171 — current streamfunction / no double counting

\[
\boxed{\mathbf J_F=\nabla^\perp F_3.}
\]

Hence

\[
\boxed{
\mathbf J_F\cdot n_\kappa=\partial_sF_3.
}
\]

The closed-loop identity is the periodicity of `F_3`, not a second independent conserved charge. On open zero arcs the exact missing boundary term is `F_3(end)-F_3(start)`.

## M17-172 — conditional M5 base-flux pushforward

M5's `dmu_0` is a base transverse-flux measure and is **not** automatically reduced-label area.

Conditional branch: if its restriction to the vertical/great-circle stratum pushes forward initially as

\[
(\Psi_0)_\#\mu_0=w_0(q_0,x_{3,0})dq_0dx_{3,0},
\]

then because the label-flow Jacobian is `a`, the current flux-weighted measure pushes forward as

\[
\boxed{w_\theta(q,x_3)dqdx_3,\qquad w_\theta=w_0\circ\Phi^{-1}.}
\]

Thus

\[
\boxed{
G_\Phi(0,\theta)
=\int_{\Gamma_0(\theta)}
\frac{h w_\theta}{|\nabla\kappa|}ds,
}
\]

while

\[
G_0(0,\theta)
=\int_{\Gamma_0}
\frac{h w_\theta}{a_\theta|\nabla\kappa|}ds.
\]

The absolute-continuity/bounded-density pushforward remains a **conditional theorem**, not an established consequence of M5-647.

## M17-173 — common `kappa=0` worldsheet

In `(q,x_3,theta)` define

\[
\Sigma_0=\{\kappa=0\},
\qquad
\mathbf M=(\mathscr H,K,1).
\]

Then

\[
\mathbf M\cdot\nabla_{st}\kappa=h.
\]

On the M17-172 conditional branch,

\[
\boxed{
\int_I G_\Phi(0,\theta)d\theta
=\int_{\Sigma_0\cap I}w_\theta\mathbf M\cdot N\,dA.
}
\]

Embed the Hessian current as

\[
\mathcal J_F=(F_{33},-F_{q3},0),
\qquad
\nabla_{st}\cdot\mathcal J_F=0.
\]

Its worldsheet normal flux is

\[
\boxed{
\mathcal J_F\cdot N
=\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}
{|\nabla_{st}\kappa|}.
}
\]

Thus the old cross-measure firewall becomes a same-worldsheet two-flux covariance problem.

## M17-174 — `(kappa,F_3)` hodograph

The map

\[
\Xi:(q,x_3)\mapsto(\kappa,F_3)
\]

has Jacobian matrix

\[
D\Xi=\nabla^2F
\]

and determinant

\[
\boxed{
J_\Xi=F_{qq}H_V-25O_V^2/|Q|_F^4.
}
\]

Material velocity transforms exactly:

\[
\boxed{
\begin{pmatrix}
h-\kappa_\theta\\
D_LF_3-F_{3\theta}
\end{pmatrix}
=\nabla^2F
\begin{pmatrix}\mathscr H\\K\end{pmatrix}.
}
\]

Where `J_Xi !=0`, `(kappa,F_3)` are valid local hodograph coordinates.

## M17-175 — uniform hodograph is NOT contradictory

An explicit smooth reduced-label toy model with constant nondegenerate Hessian, periodic `kappa=cos theta`, and

\[
a\propto e^{\sin\theta}
\]

realizes

\[
\overline G_0(0)=0,
\qquad
\overline G_\Phi(0)<0
\]

while `J_Xi` stays uniformly nonzero and `O_V` is nonzero.

Therefore

\[
\boxed{
\text{label-plane kinematics + hodograph nondegeneracy}
\not\Longrightarrow\bot.
}
\]

Any closure must use additional CE-H/Navier--Stokes pressure, palinstrophy, or transport structure.

---

# 5. M17-176 — M17-177: M5 hysteresis forces pressure heterogeneity / higher-jet occupancy on the closed-loop pushforward branch

## M17-176 — zero normal mean converts square balance into pressure variance

For a closed plane zero curve,

\[
\oint n_\kappa ds=0,
\]

so

\[
\boxed{\oint\frac{F_{qq}}{|\nabla\kappa|}ds=0.}
\]

Hence the M17-170 identity becomes

\[
\int F_{qq}(H_V-\bar H_\Gamma)d\nu_\Gamma
=25\int\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma,
\qquad
d\nu_\Gamma=\frac{ds}{|\nabla\kappa|}.
\]

Cauchy--Schwarz yields

\[
\boxed{
\int(H_V-\bar H_\Gamma)^2d\nu_\Gamma
\ge
625\frac{\left(\int O_V^2|Q|_F^{-4}d\nu_\Gamma\right)^2}
{\int F_{qq}^2d\nu_\Gamma}.
}
\]

On the M17-172 bounded-density branch, strict M5 hysteresis plus Cauchy--Schwarz forces a positive time-averaged `O_V^2` crossing mass and therefore a positive pressure-heterogeneity floor.

## M17-177 — pressure variance forces tangential higher-jet occupancy

Under compact regular zero-loop geometry, weighted Poincare gives

\[
\boxed{
\int|\partial_sH_V|^2d\nu_\Gamma
\gtrsim
\int(H_V-\bar H_\Gamma)^2d\nu_\Gamma.
}
\]

Exactly,

\[
\boxed{
\partial_sH_V
=\frac{-F_{q3}F_{q33}+F_{qq}F_{333}}
{|\nabla\kappa|}.
}
\]

Thus on the conditional compact closed-loop branch,

\[
\boxed{
\text{M5 hysteresis}
\Longrightarrow
\text{recurrent nonzero tangential axial-pressure higher-jet occupancy}.
}
\]

This is spatial occupancy, not yet temporal dissipation.

---

# 6. Current Rank-1 hard frontier

The old vague local/global covariance firewall has been substantially reduced.

Unconditional exact results:

\[
\boxed{
\text{local }O_V
\leftrightarrow
\text{small-core kappa pressure production}
\leftrightarrow
\text{radial }l=3\text{ scale current}
\leftrightarrow
\text{positive-palinstrophy angular moment}.
}
\]

Semilinear exact results:

\[
\boxed{
O_V\leftrightarrow F_{q3},
\qquad
H_V\leftrightarrow F_{33},
\qquad
J_\Xi=F_{qq}H_V-25O_V^2/|Q|_F^4.
}
\]

Conditional pushforward / closed-loop branch:

\[
\boxed{
\text{M5 hysteresis}
\to
O_V^2\text{ crossing mass}
\to
H_V\text{ variance}
\to
\partial_sH_V\text{ higher-jet occupancy}.
}
\]

Remaining Rank-1 exits:

\[
\boxed{
G_{pushforward\ density/coordinate\ degeneration}
\lor
G_{open\ zero\ endpoints}
\lor
G_{zero\ geometry\ degeneration}
\lor
G_{pressure\ higher\ jet/nonlocal}
\lor
G_{palinstrophy\ tail/turnover}.
}
\]

---

# 7. Current Rank-2 hard frontier

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

The relative-thick quiet bounded-`kappa` finite-lag packet branch is closed by the OU/Liouville mechanism. The remaining multiplicity branch is the old M5 critical growing-window occupancy problem in new packet language.

---

# 8. DSD audit state

Explicitly rejected shortcuts include:

1. winding is not itself singular;
2. scalar `kappa` payer cannot replace global `l=3` architecture by sign alone;
3. M5 base-label, spatial, coarea, director-flux, and reduced-label area measures are not interchangeable;
4. `a=J_L` does not imply `a dmu_0=dq dx_3` without a pushforward-density theorem;
5. moving maxima are not material markers;
6. Rank-1 and Rank-2 material carrier strata do not convert on a finite regular interval;
7. same-material compact ribbon recurrence is excluded, fresh-carrier Eulerian recurrence is not;
8. the earlier `K^2` historical turnover-count inference is retracted;
9. absolute analyticity does not give amplitude-relative `log rho` / `kappa` whole-jet bounds near `rho=0`;
10. generic folds are not charged by `D_B(D_k g)`;
11. blind repeated high-jet differentiation is not a closure principle;
12. M17-170 closed-loop flux is `d_sF_3` and must not be double-counted as an independent conservation law;
13. `F_qq=0` need not be physical zero-set degeneration when `F_q3 !=0`;
14. uniform nondegenerate hodograph geometry is compatible with M5-type hysteresis at the reduced-label level;
15. positive zero-loop pressure variance / higher-jet occupancy is not itself temporal dissipation;
16. global regularity remains unproved.

---

# 9. Highest-value next gates

## 1. Pressure-variance maintenance / global pressure transport

Combine

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel}
\]

with the M17-176/177 forced zero-loop variance and loop motion. Determine whether maintaining the required pressure heterogeneity has a scale-critical production/relative-transport budget, or merely routes into the known pressure/high-derivative firewall.

## 2. M17-172 pushforward theorem

Derive or refute absolute continuity of the M5 base transverse-flux label measure in the reduced `(q,x_3)` atlas. Until then, the strongest M5-to-zero-loop coarea statements remain conditional.

## 3. Rank-2 critical multiplicity/occupancy

Return to the M5 growing-window Hardy/packet packing frontier if the pressure-transport route yields only a recyclable higher-jet occupancy.

---

# Proof status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
