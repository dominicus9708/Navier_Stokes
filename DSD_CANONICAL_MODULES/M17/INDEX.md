# M17 — Material director geometry, weighted-harmonic rank, and nodal topology

Canonical continuation split from M16 after M16-023.

Recompressed at **M17-193**. Detailed derivations, corrections, provenance, and DSD audits remain in the individual canonical modules.

---

# 1. Canonical split

\[
\boxed{
B_{dir}\Longrightarrow R_1^{great-circle/winding}\ \lor\ R_2^{director-area}.
}
\]

The axisymmetric no-swirl class remains an explicit known-regular Rank-1 firewall.

---

# 2. Foundational systems — M17-006 through M17-096

## Rank-1 great-circle system

\[
W_h=J\nabla_hq,\qquad \Delta q=F(q,x_3,\theta),\qquad \kappa=F_q.
\]

Reduced material labels satisfy

\[
(q',x_3')=(\mathscr H,K),\qquad \partial_q\mathscr H+\partial_3K=\kappa,
\]

with Jacobian

\[
\boxed{J_L=a=\exp\int\kappa.}
\]

## Rank-2 pure-kernel system

\[
J_\xi=|J_\xi|k,\qquad D_k\xi=0.
\]

Same-marker comparable recurrence forces

\[
(\langle\sigma\rangle,\langle\sigma_k\rangle,\langle\sigma_n\rangle)=(-1/2,1,-1/2),
\]

and, with comparable normalized amplitude,

\[
\langle\kappa\rangle=3/2.
\]

## Vertical Rank-1 nodal pressure block

\[
G_q=1,\qquad \partial_3\lambda=0,
\]

\[
V_V=-\frac12H_V,\qquad H_V=\mathcal H_{333},
\]

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel}.
\]

At the nodal filament

\[
\boxed{O_V=-\frac15|Q|_F^2\kappa_3.}
\]

These nodal identities remain valid, but direct same-material substitution into the M5 positive-vorticity flux ensemble is retracted below.

---

# 3. Rank-2 carrier/ribbon frontier — M17-097 through M17-163

Peak/tangency/type changes are mostly signed-director-flux recyclable. Same-material compact critical-ribbon recurrence is excluded, but fresh-carrier Eulerian recurrence survives.

Remote critical tails reduce to

\[
\rho\to0,\qquad |J_\xi|\gtrsim1,\qquad \Phi_J\gtrsim1.
\]

Relative-thick bounded-\(\kappa\) packets on quiet remote corridors have the OU limit

\[
\partial_\tau V+\frac12z\cdot\nabla V=\Delta V-V,
\]

and nonzero eternal finite-lag packets are excluded. Remaining Rank-2 exits are thin/nodal, unbounded-\(\kappa\), ancestor concentration, critical multiplicity/occupancy, or interface/domain exits.

---

# 4. Valid nodal local/global pressure architecture — M17-164 through M17-171

These results are independent of any M5 flux-label bridge.

For a radial small-core cutoff,

\[
\boxed{\Pi_{V,\kappa}^{core}(R)=\frac67m_\chi R^2O_V+O(R^3),}
\]

and for a sharp ball the coefficient is \(3R^2O_V/7\).

CE-H gives

\[
\kappa\rho^2=\frac12\Delta\rho^2-|\nabla W|^2,
\]

so at the vertical nodal filament the global \(\kappa\)-production is the axial \(l=3\) angular moment of positive palinstrophy density.

In nodal semilinear gauge,

\[
H_V=F_{33},\qquad O_V=-\frac15|Q|_F^2F_{q3}.
\]

The current

\[
\mathbf J_F=(F_{33},-F_{q3})=\nabla^\perp F_3
\]

is divergence free. Its closed-loop flux identity is the periodicity of \(F_3\), not an independent conserved charge.

---

# 5. Conditional zero-worldsheet branch — M17-172 through M17-177

The hodograph

\[
(q,x_3)\mapsto(\kappa,F_3)
\]

has Jacobian

\[
J_\Xi=F_{qq}H_V-25O_V^2/|Q|_F^4.
\]

Uniform hodograph nondegeneracy is kinematically compatible with M5-type hysteresis. Any pressure-variance/higher-jet conclusion from M17-172--177 remains **conditional** on an additional regular-flux-to-nodal Eulerian localization theorem.

The exact moving-zero-loop variance law is signed and noncoercive; pressure variance is not a new monotone dissipation budget.

---

# 6. Corrective Rank-1 support/measure audit — M17-178 through M17-183

M5 transverse-flux labels live on regular \(W\neq0\) vortex-line flow boxes, while \(O_V\) lives on \(W=0\). Because

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\]

\(\rho>0\) and \(\rho=0\) are disjoint material strata on finite regular intervals. Thus M17-095's same-material M5-to-nodal identification is retracted.

On regular great-circle charts, however, the flux measure is exact:

\[
\boxed{|d\Phi_W|=dq\,dx_3,\qquad a\,d\mu_0=dq\,dx_3.}
\]

Hence

\[
\boxed{G_\Phi(0)=\int_{\Gamma_0^{reg}}\frac{h}{|\nabla_{(q,x_3)}\kappa|}\,ds.}
\]

An explicit reduced-label firewall shows the global sign of this current does not determine a nodal boundary trace.

At a regular positive-vorticity \(\kappa=0\) crossing, the local \(l=3\) tensor is

\[
\mathcal O_{reg}^{(3)}=-STF_3\!\left[\frac16\operatorname{sym}(\nabla\kappa\otimes\nabla^2\rho^2+\nabla\rho^2\otimes\nabla^2\kappa)+\frac{\rho^2}{6}\nabla^3\kappa\right].
\]

Thus the scalar crossing rate \(h\) does not determine regular local \(l=3\) orientation.

---

# 7. Exact regular flux/enstrophy joint kinetics — M17-184

For a regular closed winding loop,

\[
\boxed{L_\rho=\oint\rho\,ds=\oint|\nabla_hq|ds.}
\]

Its material law is

\[
L_\rho'=\left(\kappa-\frac12+2\bar\sigma_\rho\right)L_\rho.
\]

With joint distribution

\[
P(k,\ell,\theta)=\int\delta(k-\kappa)\delta(\ell-L_\rho)d\Phi,
\]

one has

\[
\boxed{\partial_\theta P+\partial_kG_k+\partial_\ell G_\ell=kP.}
\]

The first \(L_\rho\)-moment is

\[
\boxed{\partial_\theta F_E+\partial_kG_E=(2k-\tfrac12)F_E+2S_\rho.}
\]

Thus the M5 flux/enstrophy measure mismatch is an explicit line-strain residence channel.

---

# 8. Quarter-strain / regular payer structure — M17-185 through M17-193

## M17-185 — exact \(1/4\)-strain balance

With

\[
E=\int\rho^2dy=\int L_\rho d\Phi,\qquad D=\int|\nabla W|^2dy,
\]

CE-H gives

\[
\boxed{\int\kappa L_\rho d\Phi=-D<0,}
\]

and

\[
\boxed{\int(\bar\sigma_\rho-\tfrac14)L_\rho d\Phi=D+\tfrac12E'.}
\]

Hence on a recurrent mean

\[
\boxed{\overline{\int(\bar\sigma_\rho-\tfrac14)L_\rho d\Phi}=\overline D>0.}
\]

## M17-186 — M5-688 cycle-work in quarter-strain form

The exponential payer identity becomes

\[
\boxed{D_\kappa+X_{\kappa\sigma}=\frac12Q_\sigma^{(2)}+\frac14\mathcal C+\frac12\mathcal R,}
\]

where

\[
Q_\sigma^{(2)}=\int e^{2k}(\bar S_\sigma-\tfrac14\bar F)dk.
\]

## M17-187 — exponential phase segregation

Although the unweighted quarter-strain excess is positive, the \(e^{2\kappa}\)-tilted excess can be small only by placing a definite amount of quarter-strain deficit in an opposing \(\kappa\)-phase.

## M17-188 / 190 — recurrent closed-loop covariance forces strain-gradient occupancy

If a same-material compact high-amplitude closed winding loop recurrently restores its length, enstrophy line weight, and flux, then

\[
\langle\bar\sigma_{ds}\rangle=-\frac12,\qquad \langle\bar\sigma_\rho\rangle=\frac14,
\]

so the \(\rho\)-weighted and arclength-weighted strain averages differ by \(3/4\). This forces positive strain/amplitude line covariance and, under compact derivative bounds and positive flux mass,

\[
\boxed{D_\sigma>0.}
\]

## M17-189 — high-amplitude ledger has a nodal-label gap

Near a nondegenerate definite winding node,

\[
\rho\asymp |q|^{1/2},\qquad L_\rho(q)\asymp |q|.
\]

Thus a fixed cutoff \(\rho\ge a_0\) enforces

\[
\boxed{|q|\ge c_*a_0^2.}
\]

The high-amplitude M5-683/688 ledger does not approach the nodal trace.

## M17-191 — unweighted cutoff-transition escape is closed

For monotone high-amplitude cutoff \(\chi'\ge0\), M5-668 gives

\[
\boxed{\overline{C_\chi^{tot}}=-\frac32\int\chi'(a)a^2\overline{V_a}\,da\le0.}
\]

Therefore

\[
\boxed{Q_\sigma^{(0)}=\overline{D_\chi+B_\chi}+\frac34\int\chi'(a)a^2\overline{V_a}\,da>0}
\]

on the nontrivial retained branch.

## M17-192 — exponentially positive cutoff payer requires replenishment phase segregation

If the \(e^{2\kappa}\)-weighted cutoff term is nonnegative despite the negative unweighted threshold turnover, then a fixed positive amount of upward/replenishing threshold turnover must be concentrated in sufficiently high-\(\kappa\) phases.

## M17-193 — connected phase segregation returns to \(D_\sigma\)

On a connected high-amplitude component with uniform weighted Poincare constant, simultaneous positive and negative masses of

\[
f=\sigma-\frac14
\]

force

\[
\boxed{\int\chi\rho^2|\nabla\sigma|^2dy\ge c>0.}
\]

Thus quarter-strain phase segregation is not an independent escape on connected compact components; it returns to the strain-gradient payer. A genuinely distinct escape requires component/interface segregation.

---

# 9. Current corrected Rank-1 payer frontier

M5-687 already gives a uniform positive multiplier-diffusion charge

\[
\boxed{D_\kappa\ge d_\kappa>0.}
\]

The regular Rank-1 conveyor must pay it through

\[
\boxed{
D_\sigma
\ \lor\
Q_\sigma^{(2)}\text{ phase architecture}
\ \lor\
\text{high-}\kappa\text{ threshold replenishment}
\ \lor\
\mathcal R_{geom}
\ \lor\
\text{component/interface segregation}.
}
\]

M17-191 closes the unweighted cutoff-sign escape; M17-193 folds connected quarter-strain phase segregation back into \(D_\sigma\).

The highest-value next calculation is therefore to decompose the explicit CE-H geometric remainder \(\mathcal R_{geom}\) under the same \(e^{2\kappa}\chi\rho^2\) weight and determine whether it is genuinely independent or collapses into the already exposed gradient/threshold/director charges.

---

# 10. Current Rank-2 frontier

\[
\boxed{
R_{2,ribbon}^{remote}
\Longrightarrow
H_{1,crit}^{spacetime}
\lor G_{thin/nodal}
\lor G_{\kappa,\infty}
\lor G_{ancestor\ concentration}
\lor G_{critical\ multiplicity/occupancy}
\lor G_{interface/domain}.
}
\]

The relative-thick bounded-\(\kappa\) quiet packet lane is closed by the OU/Liouville reduction; the critical multiplicity/occupancy lane remains a major global firewall.

---

# 11. DSD audit status

1. Local and global descriptors are not equated without an explicit kernel/localization theorem.
2. Regular positive-vorticity flux labels and nodal \(W=0\) filaments are distinct material strata.
3. M5's negative zero-crossing current is kinematic source-balance data, not an independent PDE burden.
4. High-amplitude regular great-circle flux measure is exactly \(dq\,dx_3\).
5. Signed occupancy is not called irreversible dissipation without a separate monotone budget.
6. Known regular firewalls, including axisymmetric no-swirl, remain explicit.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
