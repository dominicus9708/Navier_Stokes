# M17 Frontier Index — M17-209 through M17-218

Date: 2026-09-06  
Coverage: **M17-209 -- M17-218**

This is a non-destructive continuation index after the main `M17/INDEX.md` recompression at M17-208.
It records only the new corrected frontier and does not replace the detailed derivations or the earlier index.

---

## 1. M17-209 — positive unbounded kappa is not a free packet exit

CE-H gives

\[
\frac12\Delta\rho^2=|\nabla W|^2+\kappa\rho^2.
\]

At positive `kappa=K`, persistence of `kappa>=K/2` on the intrinsic scale `K^{-1/2}` forces spherical-mean amplitude growth.
If a relative-thick/near-peak packet cannot support that growth, then

\[
|\nabla\kappa|\gtrsim K^{3/2}
\]

somewhere on the same intrinsic scale.

Thus

\[
G_{\kappa,+\infty}
\Longrightarrow
G_{amplitude\ growth/thin}
\lor
G_{\nabla\kappa\ concentration}.
\]

---

## 2. M17-210 — kappa infinity is reparametrized as H2/L2 spectral concentration

On the active CE-H set,

\[
\Delta W=\kappa W
\]

implies exactly

\[
\boxed{|\Delta W|^2=\kappa^2\rho^2.}
\]

For a shell `C_R`,

\[
\boxed{
\Lambda_R^2
:=\frac{\int_{C_R}|\Delta W|^2}
{\int_{C_R}|W|^2}
=\frac{\int_{C_R}\kappa^2\rho^2}
{\int_{C_R}\rho^2}.
}
\]

Hence enstrophy-dominant high-`|kappa|` forces `Lambda_R->infinity`; pointwise spikes with negligible enstrophy do not independently carry the hard shell.

---

## 3. M17-211 — pointwise bounded kappa removed from OU closure

For a material set `A(theta)`, define

\[
\Lambda_A^2
=\frac{\int_A\kappa^2\rho^2}{\int_A\rho^2}.
\]

If `Lambda_A<=Lambda_*` on a fixed-lag corridor and the compact strain hull is bounded, then material enstrophy obeys fixed-lag Gronwall comparability.
The same RMS bound gives the normalized `H2/L2` and interpolated `H1/L2` control required by the OU Liouville contradiction.

Therefore the corrected regular Rank-2 OU lane is

\[
R_2^{relative\text{-}thick,\ quiet,\ tempered,\ bounded\ RMS\ spectral}
\Longrightarrow\bot.
\]

The true spectral exit is

\[
\boxed{\Lambda_R\to\infty.}
\]

---

## 4. M17-212 — spectral concentration splits into amplitude curvature or director metric

Writing

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

CE-H gives

\[
\boxed{
\kappa
=\frac{\Delta\rho}{\rho}-|\nabla\xi|^2
}
\]

and

\[
\boxed{
\kappa^2\rho^2
=(\Delta\rho-\rho|\nabla\xi|^2)^2.
}
\]

Therefore

\[
G_{H2/L2\ spectral}
\Longrightarrow
G_{amplitude\ curvature}
\lor
G_{director\ metric^2}.
\]

---

## 5. M17-213 — director metric splits into area magnitude or anisotropy

For the two positive singular values `s1>=s2>0` of `grad xi`,

\[
|J_\xi|=s_1s_2,
\qquad
|\nabla\xi|^2=s_1^2+s_2^2.
\]

Define

\[
\mathcal A_\xi
=\frac{s_1^2+s_2^2}{2s_1s_2}\ge1.
\]

Then

\[
\boxed{
|\nabla\xi|^2
=2|J_\xi|\mathcal A_\xi.
}
\]

Hence large director metric requires director-area concentration or large condition number / relative Rank-1 degeneration.

---

## 6. M17-214 — enstrophy-dominant director-area concentration closed on compact relative-thick packets

Director-flux coordinates give

\[
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.
\]

Under bounded total director flux, bounded fiber length, amplitude-to-shell comparability, and fixed-fraction carrier mass, a lower bound `|J_xi|>=J0` implies a uniform upper bound for `J0`.

Thus large director-area magnitude can survive only through explicit exits:

\[
G_{J_\xi,\infty}
\Longrightarrow
G_{amplitude\ concentration/thin}
\lor
G_{director\ flux\ decompactification}
\lor
G_{fiber\ length\ decompactification}
\lor
G_{carrier\ fraction\ loss}.
\]

---

## 7. M17-215 / M17-216 — anisotropy is inherited or paid by strain spectral gap

Material frozenness gives

\[
D_B\xi=0.
\]

M17-216 integrates the director-gradient law exactly:

\[
\boxed{
\nabla\xi(\theta)
=\nabla\xi(\theta_0)F^{-1}(\theta,\theta_0),
}
\]

where `F` is the material deformation gradient.

For

\[
K_\xi:=\operatorname{cond}_+(\nabla\xi)
\]

and

\[
\Gamma_\Sigma
:=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma),
\]

\[
\boxed{
\left|
\log\frac{K_\xi(\theta)}{K_\xi(\theta_0)}
\right|
\le
\int_{\theta_0}^{\theta}\Gamma_\Sigma d\tau.
}
\]

The similarity dilation `+I/2` cancels exactly from the spectral gap.

Thus

\[
G_{anisotropy}
\Longrightarrow
G_{ancestor\ anisotropy/rank\ interface}
\lor
H_{accumulated\ strain\ spectral\ gap}.
\]

---

## 8. M17-217 — Eulerian high-anisotropy mass gets a material ancestry split

For fixed lag `T` and action threshold `L`,

\[
K_+\ge K_0
\Longrightarrow
K_-\ge K_0e^{-L}
\lor
I_T\ge L,
\]

where

\[
I_T=\int_{\theta-T}^{\theta}\Gamma_\Sigma d\tau.
\]

Using M17-205 material enstrophy transfer and M17-207 tempered shell control, a fixed-fraction current high-anisotropy packet pulls back to a fixed ancestor mass in one of those two branches on a pointwise bounded-`kappa` corridor.

M17-217 is retained as a valid specialized lemma.

---

## 9. M17-218 — RMS upgrade; pointwise bounded kappa no longer required

M17-218 performs the ancestry split **before** any material-mass comparison.
For the selected ancestor subfamily `S`, define its own material RMS spectral ratio

\[
\Lambda_S^2
=\frac{\int_S\kappa^2\rho^2}{\int_S\rho^2}.
\]

Then a current fixed-fraction high-anisotropy carrier satisfies

\[
\boxed{
G_{Eulerian\ high\ anisotropy\ mass}
\Longrightarrow
G_{ancestor\ anisotropy}
\lor
H_{strain\ spectral\ gap\ action}
\lor
G_{carrier\text{-}local\ H2/L2\ spectral\ concentration}.
}
\]

If `Lambda_S` is bounded, M17-211 gives the genuine ancestor-enstrophy lower bound.
If it is unbounded, the failure is exactly the already-canonical spectral branch.

No parent-shell-to-subset RMS inheritance is assumed.

---

# 10. Corrected dependency graph after M17-218

The current Rank-2 spectral/director chain is

\[
\boxed{
G_{H2/L2\ spectral}
\Longrightarrow
G_{amplitude\ curvature}
\lor
G_{director\ metric^2}
}
\]

and

\[
\boxed{
G_{director\ metric^2}
\Longrightarrow
G_{director\ area}
\lor
G_{director\ anisotropy}.
}
\]

The compact relative-thick director-area route is reduced by M17-214.
The anisotropy route is reduced by M17-218 to

\[
\boxed{
G_{director\ anisotropy}
\Longrightarrow
G_{ancestor\ anisotropy}
\lor
H_{strain\ gap\ action}
\lor
G_{H2/L2\ spectral}.
}
\]

Therefore there is an explicit possible recycling loop

\[
\boxed{
G_{H2/L2\ spectral}
\to
G_{director\ metric}
\to
G_{anisotropy}
\to
G_{H2/L2\ spectral}.
}
\]

This loop is **not counted as closure**.
A further argument must either:

1. assign a strictly decreasing/consumed quantity to each traversal;
2. show repeated traversal forces a nonrecyclable strain-gap or amplitude-curvature payment;
3. or extract an ancient limiting ancestry object and contradict an existing Liouville/firewall theorem.

---

# 11. Current corrected Rank-2 frontier

After M17-218, the hard Rank-2 branch is best recorded as

\[
\boxed{
R_2^{hard}
\Longrightarrow
G_{relative\text{-}thin/nodal}
\lor
G_{amplitude\ curvature/concentration}
\lor
H_{strain\ spectral\ gap\ action}
\lor
G_{ancestor\ anisotropy/rank\ reassignment}
\lor
G_{spectral/director\ recycling}
\lor
G_{flux/fiber\ decompactification}
\lor
G_{component/interface/domain}.
}
\]

The `spectral/director recycling` term is a bookkeeping warning, not a new physical payer.

---

# 12. DSD audit status

1. Pointwise `kappa` divergence is no longer treated as the primary hard-shell variable; the normalized RMS `H2/L2` spectral ratio is canonical.
2. Parent-shell RMS control is not transferred to selected subsets without proof.
3. Eulerian high-anisotropy sets are materialized before material identities are applied.
4. Director anisotropy and literal Rank loss remain distinct.
5. Similarity dilation does not pay director condition-number growth.
6. Director-area concentration is closed only on the stated compact relative-thick fixed-fraction lane.
7. The spectral/director cycle is explicitly retained and is not falsely counted as progress.
8. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
