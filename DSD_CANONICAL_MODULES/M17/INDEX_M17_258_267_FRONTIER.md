# M17 continuation frontier — M17-258 through M17-267

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_250_256_FRONTIER.md` and the M17-257 addendum.

This index is additive. M17-261 explicitly corrects the fixed-`K` coherent-mean residual of M17-256; historical modules are retained for auditability.

---

# 1. M17-258 — projected caloric gradient Liouville under subexponential backward growth

For a projected ancient caloric fluctuation `F`, the spatial constant ambiguity is removed by

\[
G=\nabla F.
\]

Then

\[
\partial_\tau G=\Delta G.
\]

If

\[
\limsup_{T\to\infty}
\frac1T\log^+\|G(-T)\|_2=0,
\]

Fourier propagation forces

\[
\boxed{G\equiv0.}
\]

On the M17-253 no-H2-defect branch this contradicts the retained nonzero raw Laplacian charge.

Therefore a nonzero projected caloric survivor must have at least exponential backward Dirichlet growth or exit through existing payer/subscale channels.

---

# 2. M17-259 — finite-T smooth ancient heat existence is insufficient

The explicit Fourier example

\[
\widehat f(\xi,\tau)
=e^{-\tau|\xi|^2-|\xi|^4}
\qquad(\tau\le0)
\]

is Schwartz at every finite negative time but has backward norms growing like

\[
e^{cT^2}.
\]

A divergence-free vector version is obtained using

\[
i(\xi\times e_1).
\]

Hence

\[
\boxed{
\text{finite-}T\text{ smoothness/compactness}
\not\Rightarrow
\text{subexponential ancient growth}.
}
\]

The growth-rate input is genuinely additional.

---

# 3. M17-260 — raw heat tangent inherits CE-H temporal-direction rigidity

For the raw intrinsic field,

\[
\Delta_zV_j=K_jV_j,
\qquad
K_j=r_j^2\kappa_j.
\]

On a non-spike raw mass-compact branch this passes to

\[
\Delta V=KV.
\]

Combined with the heat tangent,

\[
\partial_\tau V=\Delta V,
\]

we obtain

\[
\boxed{\partial_\tau V=KV.}
\]

Thus on `V!=0`,

\[
\boxed{\partial_\tau(V/|V|)=0.}
\]

The raw tangent has a time-frozen director.

Mean-subtracted projected fluctuations do not automatically inherit homogeneous CE-H.

---

# 4. M17-261 — correction: fixed-K coherent-mean decompactification is impossible

The selected M17-224/251 denominator has a fixed-volume plateau on which its cutoff equals one.

If a fixed larger ball is mean dominated and normalized palinstrophy is quiet, Chebyshev makes the packet plateau mean dominated as well. Hence

\[
E_j\ge c|c_j|^2r_j^3,
\]

while

\[
M_{j,K}\le C_K|c_j|^2r_j^3.
\]

Therefore

\[
M_{j,K}/E_j\le C_K,
\]

contradicting fixed-`K` mass decompactification.

Thus

\[
\boxed{
G_{normalized\ mass\ decompactification}^{fixed\ K}
\Longrightarrow
H_{divergent\ normalized\ palinstrophy}.
}
\]

The coherent-mean residual of M17-256/M17-257 is not needed on this fixed-cylinder frontier.

---

# 5. M17-262 — Rank-2 heat tangent forces multiplier gradient into the fiber kernel

Write

\[
V=a\xi,
\qquad
\partial_\tau\xi=0.
\]

Perpendicular projection of the heat equation gives

\[
2D_{\nabla\log|a|}\xi
+P_\xi^\perp\Delta\xi=0.
\]

Time differentiation and

\[
\partial_\tau\log|a|=K
\]

give

\[
\boxed{D_{\nabla K}\xi=0.}
\]

Therefore on Rank-2,

\[
\boxed{\nabla K\parallel\ker D\xi.}
\]

All multiplier variation is confined to the one-dimensional director fiber.

---

# 6. M17-263 — K obeys exact weighted diffusion along fibers

The scalar amplitude satisfies

\[
\partial_\tau a
=\Delta a-|\nabla\xi|^2a.
\]

With

\[
K=\frac{a_\tau}{a},
\]

one obtains exactly

\[
\boxed{
\partial_\tau K
=\Delta K+2\nabla\log|a|\cdot\nabla K
=a^{-2}\nabla\cdot(a^2\nabla K).
}
\]

Using M17-262, on Rank-2 this becomes locally

\[
\boxed{
K_\tau=K_{ss}+b_fK_s
}
\]

along the director fiber.

---

# 7. M17-264 — compact closed fibers close

Assume closed fibers with

\[
0<L_-\le L\le L_+,
\]

nondegenerate active amplitude, bounded fiber drift, and bounded ancient `K`.

Uniform one-dimensional parabolic mixing gives

\[
\operatorname{osc}K(\tau+\tau_0)
\le q\operatorname{osc}K(\tau),
\qquad0<q<1.
\]

Ancient boundedness implies

\[
\boxed{\operatorname{osc}K=0.}
\]

M17-262 kills transverse derivatives as well, so `K` is spatially constant.

This contradicts the M17-233/234 critical occupancy plus sign-balance/gradient structure.

Thus the compact closed-fiber lane is closed modulo explicit hypothesis failures.

---

# 8. M17-265 — bounded open fibers are boundary/interface replenishment

On a bounded open fiber,

\[
K_\tau=K_{ss}+b_fK_s.
\]

Interior parabolic oscillation satisfies

\[
\operatorname{osc}_{int}K(t+\tau_0)
\le
q\operatorname{osc}K(t)
+C_b\mathcal B_K,
\]

where `mathcal B_K` is endpoint trace oscillation/input.

A fixed ancient interior sign-balanced oscillation cannot be maintained by remote-past initial data alone.

Therefore

\[
\boxed{
G_{bounded\ open\ fiber}
\Longrightarrow
G_{fiber\ boundary/interface\ replenishment}
}
\]

unless amplitude, drift, rank, or coefficient control fails.

---

# 9. M17-266 — long fibers force J escalation or label collapse

On a regular Rank-2 tube,

\[
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.
\]

If

\[
|J_\xi|\le J^*
\]

and active fibers have length at least `L`, then

\[
\boxed{
\Phi_J(\mathcal F_L)
\le\frac{J^*V_*}{L}.
}
\]

Hence

\[
L\to\infty
\Longrightarrow
\Phi_J(\mathcal F_L)\to0
\]

unless the director Jacobian itself escalates.

Thus pure fiber-length escape becomes

\[
G_{J\text{-}escalation}
\lor
G_{transverse\ label\ collapse}.
\]

---

# 10. M17-267 — label collapse returns to rank, anisotropy, or multiplicity

On a fixed-area transverse section,

\[
\int_\Sigma J_\xi dA
=
\int_{\xi(\Sigma)}N(\eta)dA_\eta.
\]

If multiplicity stays bounded and the director image/label area collapses, then

\[
\fint_\Sigma J_\xi\to0.
\]

Since

\[
J_\xi=s_1s_2,
\]

a fixed fraction satisfies either

\[
s_1\to0
\]

(metric/rank collapse) or

\[
s_2\to0\quad\text{with }s_1\not\to0
\]

(anisotropy divergence).

If multiplicity is not bounded, retain fold/multiplicity escalation.

Therefore

\[
\boxed{
G_{transverse\ label\ collapse}
\Longrightarrow
G_{rank/metric\ collapse}
\lor
G_{anisotropy}
\lor
G_{fold/multiplicity\ escalation}.
}
\]

---

# 11. Corrected current frontier

After the M17-261 correction and M17-262--267 fiber reductions, the raw Rank-2 spectral lane is compressed to

\[
\boxed{
R_2^{raw\ tangent}
\Longrightarrow
G_{nodal/subscale}
\lor
H_{normalized\ palinstrophy}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{fiber\ boundary/interface}
\lor
G_{director\ Jacobian/metric\ escalation}
\lor
G_{director\ anisotropy}
\lor
G_{director\ fold/multiplicity\ escalation}
\lor
G_{rank\ loss}
\lor
G_{K\text{-}spike}.
}
\]

The bounded compact-fiber heat lane itself is no longer an open endpoint.

---

# 12. Next target

The narrowest genuinely new geometric residual is

\[
\boxed{G_{director\ fold/multiplicity\ escalation}.}
\]

The next calculation should test whether repeated transverse multiplicity can be charged to

1. M17-145 multiplier-gradient fold activity;
2. M17-215/216 accumulated strain/anisotropy;
3. nodal/interface creation;
4. or an explicit multiplicity-growth budget.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
