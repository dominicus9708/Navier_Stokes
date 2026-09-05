# M17 — Material director geometry, weighted-harmonic rank, and nodal topology

Canonical continuation split from M16 after M16-023.

Recompressed at **M17-208**. Detailed derivations, corrections, provenance, and DSD audits remain in the individual canonical modules.

---

# 1. Canonical split

\[
\boxed{
B_{dir}\Longrightarrow R_1^{great-circle/winding}\ \lor\ R_2^{director-area}.
}
\]

The axisymmetric no-swirl class remains an explicit known-regular Rank-1 firewall.

---

# 2. Foundational Rank-1 / Rank-2 geometry — M17-006 through M17-096

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

and with comparable normalized amplitude

\[
\langle\kappa\rangle=3/2.
\]

## Vertical nodal pressure block

\[
V_V=-\frac12H_V,\qquad H_V=\mathcal H_{333},
\]

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel},
\]

and at the vertical nodal filament

\[
\boxed{O_V=-\frac15|Q|_F^2\kappa_3.}
\]

These nodal identities remain valid, but direct same-material substitution into the M5 positive-vorticity flux ensemble is retracted by M17-178--183.

---

# 3. Rank-2 ribbon / OU frontier — M17-097 through M17-163

Peak/tangency/type changes are mostly signed-director-flux recyclable. Same-material compact critical-ribbon recurrence is excluded, but fresh-carrier Eulerian recurrence survives.

Remote critical tails reduce to

\[
\rho\to0,\qquad |J_\xi|\gtrsim1,\qquad \Phi_J\gtrsim1.
\]

Relative-thick, quiet, bounded-\(\kappa\) packets have the amplitude-normalized OU limit

\[
\partial_\tau V+\frac12z\cdot\nabla V=\Delta V-V.
\]

M17-158 shows that an eternal \(L^2\) OU packet with bounded CE-H potential must vanish. The former escape was fixed-lag normalized mass explosion, split by M17-162 into concentration or diffuse multiplicity. M17-163 showed raw volume packing alone is too weak.

---

# 4. Valid nodal local/global pressure architecture — M17-164 through M17-171

These results do not use an M5 flux-label bridge.

Small-core pressure production reproduces the nodal octupole:

\[
\boxed{\Pi_{V,\kappa}^{core}(R)=\frac67m_\chi R^2O_V+O(R^3).}
\]

For a sharp ball the coefficient is \(3R^2O_V/7\).

CE-H gives

\[
\kappa\rho^2=\frac12\Delta\rho^2-|\nabla W|^2,
\]

so the global \(\kappa\)-production is an axial \(l=3\) moment of positive palinstrophy density.

In nodal semilinear gauge,

\[
H_V=F_{33},\qquad O_V=-\frac15|Q|_F^2F_{q3},
\]

and

\[
\mathbf J_F=(F_{33},-F_{q3})=\nabla^\perp F_3.
\]

The closed-loop flux identity is periodicity of \(F_3\), not an independent conserved charge.

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

Uniform hodograph nondegeneracy is kinematically compatible with M5-type hysteresis. Any M5-forced pressure-variance/higher-jet statement in this branch is **conditional** on an additional regular-flux-to-nodal Eulerian localization theorem.

The exact moving-zero-loop pressure-variance law is signed and noncoercive.

---

# 6. Corrective Rank-1 support/measure audit — M17-178 through M17-183

M5 transverse-flux labels live on regular \(W\neq0\) vortex-line flow boxes, while \(O_V\) lives on \(W=0\). Since

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\]

\(\rho>0\) and \(\rho=0\) are disjoint material strata on finite regular intervals. Thus M17-095's same-material M5-to-nodal identification is retracted.

On regular great-circle charts the flux measure is exact:

\[
\boxed{|d\Phi_W|=dq\,dx_3,\qquad a\,d\mu_0=dq\,dx_3.}
\]

Hence

\[
\boxed{G_\Phi(0)=\int_{\Gamma_0^{reg}}\frac{h}{|\nabla_{(q,x_3)}\kappa|}\,ds.}
\]

The global M5 zero-current sign does not determine a nodal boundary trace.

At a regular positive-vorticity \(\kappa=0\) crossing,

\[
\mathcal O_{reg}^{(3)}=-STF_3\!\left[\frac16\operatorname{sym}(\nabla\kappa\otimes\nabla^2\rho^2+\nabla\rho^2\otimes\nabla^2\kappa)+\frac{\rho^2}{6}\nabla^3\kappa\right],
\]

so the scalar crossing velocity \(h\) does not determine the local regular \(l=3\) orientation.

---

# 7. Regular M5 flux/enstrophy kinetics — M17-184 through M17-193

For a regular closed winding loop,

\[
L_\rho=\oint\rho\,ds=\oint|\nabla_hq|ds,
\]

\[
L_\rho'=\left(\kappa-\frac12+2\bar\sigma_\rho\right)L_\rho.
\]

The joint \((\kappa,L_\rho)\) distribution obeys

\[
\boxed{\partial_\theta P+\partial_kG_k+\partial_\ell G_\ell=kP,}
\]

and the first \(L_\rho\)-moment gives

\[
\boxed{\partial_\theta F_E+\partial_kG_E=(2k-\tfrac12)F_E+2S_\rho.}
\]

The exact quarter-strain balance is

\[
\boxed{\int\kappa L_\rho d\Phi=-\int|\nabla W|^2dy,}
\]

\[
\boxed{\int(\bar\sigma_\rho-\tfrac14)L_\rho d\Phi=\int|\nabla W|^2dy+\tfrac12E'.}
\]

On recurrent mean, the quarter-strain excess equals palinstrophy.

M17-191 closes the unweighted cutoff-sign escape. M17-192 shows an exponentially positive cutoff payer requires upward amplitude replenishment concentrated in high \(\kappa\). M17-193 sends connected quarter-strain phase segregation back to strain-gradient occupancy; disconnected component/interface segregation remains explicit.

---

# 8. Geometric-remainder and payer collapse — M17-194 through M17-200

## M17-194 — exact weighted cancellation

For weight \(w=\chi e^{2\kappa}\rho^2\), integration by parts and

\[
\nabla\cdot\Sigma=-\frac12\nabla\times W
\]

cancel the amplitude-Hessian-generated curl term against the explicit curl term in \(\mathcal R_{geom}\).

The integrated remainder reduces to amplitude-gradient/strain, \(\kappa\)-amplitude mixed gradient, threshold collar, and director-gradient/strain channels.

## M17-195 / 196 — quantitative domination

With

\[
D_\rho=\int\chi e^{2\kappa}|\nabla\rho|^2,
\qquad
P_\xi=\int\chi e^{2\kappa}\rho^2|\nabla\xi|^2,
\]

and threshold charges \(B_\rho,B_\kappa,B_\sigma\),

\[
|\mathcal R^{(2)}|
\lesssim
D_\rho+B_\rho+P_\xi
+\sqrt{D_\kappa D_\rho}
+\sqrt{B_\rho B_\kappa}
+\sqrt{B_\rho B_\sigma}.
\]

Thus no independent geometric-remainder payer survives.

## M17-197 / 198 — bulk payer compression and double-counting firewall

For the simple strain eigenvalue,

\[
|\nabla\sigma|^2\le|\nabla\Sigma|^2,
\]

and globally

\[
\boxed{\|\nabla\Sigma\|_2^2=\frac12\|\nabla W\|_2^2.}
\]

Together with

\[
|\nabla W|^2=|\nabla\rho|^2+\rho^2|\nabla\xi|^2,
\]

bulk fixed-order payers collapse to palinstrophy occupancy. Palinstrophy and unweighted quarter-strain excess are one enstrophy cycle and must not be counted as independent payments.

## M17-199 — amplitude/kappa joint state

For \(r=\rho,k=\kappa\),

\[
\boxed{\partial_\theta\mathcal P+\partial_r\mathcal J_r+\partial_k\mathcal J_k=\frac32\mathcal P.}
\]

M5-668 threshold turnover is the \(r\)-current; the M5 constitutive multiplier transport is the \(k\)-current. The exponentially tilted cutoff payer is only a \(\kappa\)-weighted moment of the same amplitude current.

## M17-200 — threshold multiplier-gradient descent

If a child cutoff's threshold charge is

\[
B_\kappa[\chi]=\int\chi'e^{2\kappa}\rho^3|\nabla\kappa|^2,
\]

choose a lower-amplitude parent cutoff \(\tilde\chi=1\) on \(\operatorname{supp}\chi'\). Then

\[
\boxed{B_\kappa[\chi]\le C D_\kappa[\tilde\chi].}
\]

Thus threshold \(\nabla\kappa\) payment is the same multiplier-diffusion charge in a lower amplitude layer and descends toward bulk/replenishment/interface or low-amplitude/nodal exits.

---

# 9. High-kappa replenishment / return current — M17-201 through M17-204

For the stationary joint \((\rho,\kappa)\) state and quadrant \(\{r>a,k>k_0\}\),

\[
\boxed{
\int_{k>k_0}\bar{\mathcal J}_r(a,k)dk
+\int_{r>a}\bar{\mathcal J}_k(r,k_0)dr
=-\frac32M_{a,k_0}.
}
\]

Thus high-\(\kappa\) upward amplitude replenishment forces a stronger downward multiplier return current.

On a retained amplitude band \(a\le\rho\le M_0\), a negative volume return current \(-A\) either transfers a fixed negative fraction to the enstrophy measure or forces quantitative positive \(h\) counterflow. On a connected regular \(\kappa\)-level, counterflow forces

\[
\boxed{\int|\nabla_T h|^2d\nu\ge cA^2.}
\]

At \(k_0=0\), the negative return direction is coherent with the existing M5-686 zero-current conveyor; it is not a new sign contradiction. The regular Rank-1 frontier is therefore recyclability/budget, not further local sign chasing.

---

# 10. Rank-2 global multiplicity closure — M17-205 through M17-208

## M17-205 — fixed-lag material shell transfer

For any material set,

\[
\boxed{
\int_{\Phi_T(A_-)}\rho_+^2dy
=\int_{A_-}\rho_-^2
\exp\int(2\sigma+2\kappa-\tfrac12)d\tau\,dy.
}
\]

On compact bounded-\(\kappa\) corridors, fixed-lag material enstrophy is uniformly comparable. Remote Type-I velocity gives

\[
|y(\theta)|^2=e^T|y(\theta-T)|^2+O_T(1),
\]

so one ancestor dyadic shell maps into finitely many current dyadic neighbors. Hence

\[
\boxed{E_j(-T)\le C_T\sum_{|m|\le M_T}E_{j+s_T+m}(0).}
\]

## M17-206 / 207 — good and globally tempered shell extraction

For the bounded critical sequence \(b_k=R_kE_k\), cubic divergence survives on a globally tempered subfamily. Choose \(A>1\), \(A^{3/2}>3\), and define

\[
\boxed{b_{k+m}\le A^{|m|}b_k\qquad\forall m.}
\]

Then

\[
\boxed{
\sum_kb_k^{3/2}\le C_A\sum_{k\in G_{temp}}b_k^{3/2}.
}
\]

Thus the nonsummable M5-526 defect cannot avoid shells that control **every fixed finite neighborhood simultaneously**.

## M17-208 — tempered Rank-2 multiplicity lane closed

On a tempered shell remaining in the M17-155 relative-thick, quiet, bounded-\(\kappa\) Rank-2 lane,

\[
a_j^2\ge c_*E_{k_j}(0).
\]

M17-205 plus global temperedness gives, for every fixed \(T\),

\[
\boxed{\sup_{|\tau|\le T}\frac{E_j(\tau)}{a_j^2}\le C_T.}
\]

M17-158 therefore produces a nonzero eternal \(L^2\) OU packet with bounded CE-H potential, which is impossible.

Hence

\[
\boxed{
R_{2,ribbon}^{relative\text{-}thick,\ quiet,\ bounded\text{-}\kappa,\ tempered}
\Longrightarrow\bot.
}
\]

The previous diffuse multiplicity escape is not terminal on this lane. If the M17-207 charging lands on shells where the Rank-2 hypotheses fail, that is explicit rank reassignment / thin / unbounded-\(\kappa\) / nonquiet / interface exit.

---

# 11. Current corrected frontiers

## Regular Rank-1

\[
\boxed{
R_1^{regular}
\Longrightarrow
G_{M5\text{-}688\ enstrophy/palinstrophy\ cycle}
\lor
G_{\nabla_T h}
\lor
G_{component/interface}
\lor
G_{low\ amplitude/nodal}.
}
\]

The catch-all geometric remainder has been removed as an independent payer. The hard issue is nonrecyclable cumulative control, not another scalar sign.

## Rank-2 hard tail

\[
\boxed{
R_2^{hard}
\Longrightarrow
G_{relative\text{-}thin/nodal}
\lor
G_{\kappa,\infty}
\lor
H_{1,crit}^{spacetime}
\lor
G_{rank\ reassignment/concentration}
\lor
G_{component/interface/domain}.
}
\]

The relative-thick quiet bounded-\(\kappa\) diffuse-multiplicity lane is closed on the globally tempered hard-shell subfamily.

---

# 12. DSD audit status

1. Local/global descriptors are not equated without explicit localization/kernel control.
2. Regular positive-vorticity flux labels and nodal \(W=0\) filaments are distinct material strata.
3. M5's negative zero-crossing current is kinematic source-balance data, not an independent PDE burden.
4. High-amplitude regular great-circle flux measure is exactly \(dq\,dx_3\).
5. Palinstrophy and quarter-strain excess are one enstrophy cycle and are not double counted.
6. Geometric-remainder and threshold-gradient payers are reduced to explicit fixed-order/nested-layer charges.
7. Rank-2 multiplicity is closed only on the stated tempered relative-thick quiet bounded-\(\kappa\) lane; rank reassignment and other hard exits remain.
8. Known regular firewalls, including axisymmetric no-swirl, remain explicit.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
