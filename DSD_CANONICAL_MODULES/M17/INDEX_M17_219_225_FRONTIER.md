# M17 continuation frontier — M17-219 through M17-225

Date: 2026-09-06  
Scope: continuation after `INDEX_M17_209_218_FRONTIER.md`.

This index is additive and does not replace the earlier canonical index or detailed module files.

---

# 1. Measure-theoretic correction — M17-219

M17-212 gives the director-metric second moment

\[
Q_R
:=
\frac{\int_{C_R}\rho^2|\nabla\xi|^4dy}{E_R}
\to\infty.
\]

This does **not** automatically imply that a high-metric/high-anisotropy set carries a fixed fraction of shell enstrophy.

With

\[
d\mu_R=\frac{\rho^2}{E_R}dy,
\qquad
g_R=|\nabla\xi|^2,
\]

M17-219 proves

\[
\boxed{
\int g_R^2d\mu_R\to\infty
\Longrightarrow
G_{fixed\text{-}fraction\ high\ metric}
\lor
G_{director\text{-}metric\ microcarrier}.
}
\]

On the fixed-fraction branch,

\[
g_R=2|J_\xi|\mathcal A_\xi
\]

preserves a fixed fraction under the split

\[
\boxed{
G_{fixed\text{-}fraction\ high\ metric}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ area}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}.
}
\]

M17-214 removes the high-area part on the relative-thick compact packet lane modulo the existing thin/decompactification/interface exits.

The microcarrier branch has vanishing enstrophy fraction but divergent director-metric second-moment charge and cannot be fed directly into M17-218.

---

# 2. Quiet fixed-fraction strain-gap action is closed — M17-220

For the M17-218 bounded-carrier-RMS branch, the fixed-lag strain-gap alternative gives

\[
\mathcal A_T
:=
\int_{S^-}\rho_-^2I_Tdy
\ge cE_R,
\]

where

\[
I_T=\int\Gamma_\Sigma d\theta.
\]

On the M17-155 quiet relative-thick compact corridor, bounded RMS spectral ratio gives

\[
\sup_{S^-}\rho_-^2\le C E_R,
\]

and

\[
\int_{-T}^{0}\int_{C_R(\theta)}|\Sigma|^2dy\,d\theta
\le\frac{C_T}{R}.
\]

The exact material Jacobian and Cauchy-Schwarz imply

\[
\boxed{
\mathcal A_T
\le C E_RR^{-1/2}
=o(E_R).
}
\]

Hence

\[
\boxed{
H_{fixed\text{-}fraction\ strain\ gap}^{quiet,compact,bounded\ RMS}
\Longrightarrow\bot.
}
\]

Therefore

\[
\boxed{
G_{fixed\text{-}fraction\ high\ anisotropy}^{quiet,compact}
\Longrightarrow
G_{ancestor\ high\ anisotropy}
\lor
G_{carrier\text{-}local\ spectral}
\lor
G_{thin/decompactification/interface}.
}
\]

---

# 3. Carrier-local spectral return is an intrinsic small scale — M17-221

For any spectral carrier,

\[
\Lambda_S^2
=
\frac{\int_S|\Delta W|^2}{\int_S|W|^2},
\]

define

\[
\boxed{
\ell_S
:=
\Lambda_S^{-1/2}
=
\left(
\frac{\int_S|W|^2}{\int_S|\Delta W|^2}
\right)^{1/4}.
}
\]

Then

\[
\boxed{
\Lambda_S\to\infty
\Longrightarrow
\ell_S\to0.
}
\]

On remote shells,

\[
\ell_S/R\to0.
\]

Thus the spectral return is already a remote derivative-subscale statement.
It need not be recycled through director anisotropy merely for classification.

For an arbitrary tiny carrier, failure of comparable bounded localization remains a microcarrier-fragmentation issue.

---

# 4. Whole-shell spectral concentration extracts a finite remote packet — M17-222

On an M17-207 globally tempered shell,

\[
E_R^*\le C_*E_R
\]

for every fixed enlarged neighborhood.

If

\[
\boxed{
\frac{H_R}{E_R}
:=
\frac{\int_{C_R}|\Delta W|^2}{\int_{C_R}|W|^2}
\to\infty,
}
\]

then a shell cutoff equal to one on the core has compact `H2/L2` ratio tending to infinity.

A fixed bounded-scale partition of unity and

\[
\|\nabla F\|_2^2
\le
\|F\|_2\|\Delta F\|_2
\]

show that one bounded-size remote cell inherits a divergent local ratio.

Hence

\[
\boxed{
G_{whole\text{-}shell\ H2/L2\ spectral}^{tempered}
\Longrightarrow
H_{finite\ remote\ derivative\ subscale\ packet}.
}
\]

Diffuse spatial fragmentation is not terminal at the whole-shell level.

---

# 5. Intrinsic-scale spatial extraction — M17-223

For a compact remote packet with

\[
E_j=\|f_j\|_2^2,
\qquad
H_j=\|\Delta f_j\|_2^2,
\]

define

\[
\ell_j=(E_j/H_j)^{1/4}.
\]

Partitioning at scale

\[
r_j=A\ell_j
\]

makes the derivative commutators

\[
O(A^{-2})H_j+O(A^{-4})H_j.
\]

For fixed sufficiently large `A`, these are absorbed and one cell satisfies

\[
\boxed{
\operatorname{diam}(packet_j)=O(\ell_j),
\qquad
\frac{\|\Delta packet_j\|_2^2}{\|packet_j\|_2^2}
\gtrsim\ell_j^{-4}.
}
\]

Thus the remote spectral defect has a spatial witness at its own intrinsic scale.

---

# 6. Buffered raw-density extraction — M17-224

M17-224 strengthens M17-223 to exclude cutoff-generated spectral artifacts.

Partition the **raw** core-shell density

\[
|\Delta W|^2
\]

into intrinsic cells and assign each cell a larger buffer denominator

\[
e_m=\|\zeta_mW\|_2^2,
\]

where `zeta_m=1` on the numerator cell.

Then

\[
\sum h_m=H_R,
\qquad
\sum e_m\le C_BE_R.
\]

Therefore one buffered cell satisfies

\[
\boxed{
\frac{h_m}{e_m}
\ge c_B\frac{H_R}{E_R}.
}
\]

Since `zeta_m=1` on the numerator core,

\[
\boxed{
\frac{\|\Delta(\zeta_mW)\|_2^2}
{\|\zeta_mW\|_2^2}
\ge c_B\frac{H_R}{E_R}.
}
\]

The numerator is therefore genuine raw `Delta W`, while the transition-region `L2` mass is already included in the normalization.

M17-224 is the preferred input to the dynamic stage.

---

# 7. Parabolic persistence or turnover payment — M17-225

Move the intrinsic cutoff with a material center.

For

\[
M_j(\theta)=\int\zeta_j^2|W|^2dy,
\]

the exact localized enstrophy identity is

\[
\begin{aligned}
M_j'
={}&-2\int\zeta_j^2|\nabla W|^2\\
&-4\int\zeta_jW\cdot(\nabla\zeta_j\cdot\nabla W)\\
&+2\int\zeta_j^2W\cdot\Sigma W\\
&-\frac12M_j
+2\int\zeta_j(D_B\zeta_j)|W|^2.
\end{aligned}
\]

On a bounded local coefficient corridor,

\[
M_j'
\ge
-C_DD_j
-C_Br_j^{-2}N_j
-C_0M_j,
\]

where

\[
D_j=\int\zeta_j^2|\nabla W|^2,
\qquad
N_j=\int_{supp\nabla\zeta_j}|W|^2.
\]

If a fixed fraction of packet mass is lost before time `c r_j^2`, then

\[
\boxed{
\int D_jd\theta
+r_j^{-2}\int N_jd\theta
\ge cM_j(0).
}
\]

Therefore

\[
\boxed{
H_{intrinsic\ packet}
\Longrightarrow
H_{parabolic\ persistence}
\lor
H_{local\ palinstrophy}
\lor
H_{interface/turnover}
\lor
G_{local\ coefficient\ spike}.
}
\]

On the persistence branch, the moving parabolic scaling formally reduces the vorticity equation to

\[
\partial_\tau V=\Delta V,
\]

because the similarity drift difference and the strain/reaction terms acquire factors `r_j` or `r_j^2`.

A nonzero heat tangent is **not yet proved**; compactness, cutoff forcing, and backward lifetime remain.

---

# 8. Corrected Rank-2 hard frontier after M17-225

The earlier `spectral/director recycling` label is no longer needed as an independent endpoint.

The corrected compressed frontier is

\[
\boxed{
R_2^{hard}
\Longrightarrow
G_{relative\text{-}thin/nodal}
\lor
G_{amplitude\ curvature/concentration}
\lor
H_{buffered\ intrinsic\ remote\ derivative\ packet}
\lor
H_{local\ palinstrophy/turnover}
\lor
G_{ancestor\ asymptotic\ anisotropy/rank\ boundary}
\lor
G_{flux/fiber\ decompactification}
\lor
G_{component/interface/domain}.
}
\]

On the tempered whole-shell spectral lane,

\[
\boxed{
G_{H2/L2\ spectral}
\Longrightarrow
H_{buffered\ intrinsic\ remote\ packet}
}
\]

is now the preferred nonrecycling route.

---

# 9. Current narrow next target

The next dynamical bottleneck is

\[
\boxed{
H_{parabolic\ persistence}
\Longrightarrow
\text{nonzero compact heat tangent}
\lor
\text{backward replenishment/interface payment}
\lor
\text{loss of intrinsic-scale compactness}.
}
\]

To obtain an actual heat-Liouville contradiction one must still prove:

1. compactness of the parabolically normalized moving packets on fixed `z,tau` cylinders;
2. a nonzero normalized mass surviving the limit;
3. enough backward lifetime to obtain an ancient/eternal heat solution or another coercive one-sided contradiction;
4. control of moving-cutoff forcing/interface terms under the scaling.

No one of these is assumed by M17-225.

---

# 10. DSD audit status

1. Divergent director second moment is no longer equated with fixed-fraction anisotropy without a measure gate.
2. Quiet fixed-fraction strain-gap action is closed by the `R^-1/2` mismatch.
3. Spectral return is reinterpreted directly as an intrinsic small scale.
4. Whole-shell tempered spectral concentration has a finite spatial packet witness.
5. The intrinsic packet can be extracted from raw `Delta W` with a buffered `L2` denominator, excluding cutoff artifacts.
6. Early parabolic packet loss is converted to palinstrophy/interface turnover rather than assumed impossible.
7. Heat dynamics remain a next-step limit problem, not a proved contradiction.
8. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
