# Temporal-concentration gate from the localized enstrophy budget

Date: 2026-08-13

Status: **DERIVED LOCAL TEMPORAL-NONCOLLAPSE LEMMA / SOURCE-OR-SHELL CONCENTRATION ALTERNATIVE**.

The compactness route must not infer a persistent spacetime core merely from the terminal normalization `|Omega(0,0)|=1`.  A dangerous state could in principle appear only in an increasingly thin normalized time layer.  This note shows that such temporal collapse is not free: a fixed terminal local enstrophy rise over a vanishing time layer forces concentration of the localized stretching/transport/buffer source.

---

## 1. Fixed normalized cutoff

Work in a naturally rescaled window and choose a time-independent cutoff

\[
\chi\in C_c^\infty(B_R),
\qquad
0\le\chi\le1,
\]

with `chi=1` on the core ball.

Define

\[
\boxed{
E_\chi(s)
=\int\chi^2|\Omega(s)|^2dy.
}
\]

The normalized vorticity equation is

\[
\partial_s\Omega
+(U\cdot\nabla)\Omega
=(\Omega\cdot\nabla)U
+\nu\Delta\Omega.
\]

---

## 2. Exact localized enstrophy identity

Multiply by `chi^2 Omega` and integrate.  Since `div U=0`,

\[
\boxed{
\frac12E_\chi'(s)
+\nu D_\chi(s)
=
Q_\chi(s)+T_\chi(s)+B_\chi(s),
}
\]

where

\[
D_\chi
=\int\chi^2|\nabla\Omega|^2,
\]

\[
Q_\chi
=\int\chi^2\Omega\cdot S_U\Omega,
\]

\[
T_\chi
=\frac12\int|\Omega|^2U\cdot\nabla(\chi^2),
\]

and

\[
B_\chi
=\frac\nu2\int|\Omega|^2\Delta(\chi^2).
\]

Define the total local growth channel

\[
\boxed{
G_\chi=Q_\chi+T_\chi+B_\chi.
}
\]

The nonnegative dissipation gives the one-sided inequality

\[
\boxed{
\frac12E_\chi'(s)\le G_\chi(s).
}
\]

---

## 3. Abstract time-width lower bound

Suppose at an earlier time `s_*<0`,

\[
E_\chi(s_*)\le e_-,
\]

while at the checkpoint

\[
E_\chi(0)\ge e_+>e_-.
\]

Let

\[
\Delta e=e_+-e_->0.
\]

Integrating the one-sided identity,

\[
\frac{\Delta e}{2}
\le
\int_{s_*}^{0}|G_\chi(s)|ds.
\]

If

\[
G_\chi\in L^p(s_*,0),
\qquad p>1,
\]

then Holder gives

\[
\frac{\Delta e}{2}
\le
|s_*|^{1-1/p}
\|G_\chi\|_{L^p(s_*,0)}.
\]

Therefore

\[
\boxed{
|s_*|
\ge
\left(
\frac{\Delta e}
{2\|G_\chi\|_{L^p}}
\right)^{p/(p-1)}.
}
\]

Thus a fixed local-enstrophy rise cannot be compressed into arbitrarily small normalized time if the local growth channel is uniformly bounded in any `L^p`, `p>1`.

---

## 4. Natural `p=4/3` bookkeeping

The critical energy class naturally produces the time exponent `4/3` for the standard stretching estimate.  Schematically,

\[
|Q_\chi|
\lesssim
E_{\rm buf}^{3/4}P_{\rm buf}^{3/4}
+\text{typed far-strain terms}.
\]

When

\[
E_{\rm buf}\in L_s^\infty,
\qquad
P_{\rm buf}\in L_s^1,
\]

the near part belongs uniformly to `L_s^(4/3)`.

The transport buffer term can be estimated by

\[
|T_\chi|
\lesssim
\|U\|_6\|\Omega\|_{12/5}^2
\lesssim
\|\nabla U\|_2
E_\Omega^{3/4}P_\Omega^{1/4}
\]

up to fixed cutoff/localization terms.  With

\[
\nabla U\in L_s^2L_y^2,
\qquad
P_\Omega\in L_s^1,
\]

this is also `L_s^(4/3)` by Holder in time.

The cutoff diffusion term `B_chi` is lower order under the local `L_s^infinity L_y^2` vorticity bound.

Hence, on the bounded normalized branch and with the already-typed far-strain/localization channel controlled,

\[
\boxed{
\|G_\chi\|_{L_s^{4/3}}
\le M_G
}
\]

is the natural target bound.

For `p=4/3`,

\[
\boxed{
|s_*|
\ge
\left(
\frac{\Delta e}{2M_G}
\right)^4.
}
\]

---

## 5. Thick terminal core supplies `e_+>0`

If the residual branch is non-sparse at the terminal checkpoint, for example

\[
\left|
\{y\in B_1:|\Omega(y,0)|\ge b\}
\right|
\ge\theta>0,
\]

and `chi=1` on `B1`, then

\[
\boxed{
E_\chi(0)
\ge b^2\theta.
}
\]

Thus the terminal nontriviality is a robust `L2` quantity, not merely the pointwise normalization at one center.

If the intense set is sparse instead, the route returns to the existing sparseness/geometric regularity branch.

---

## 6. Temporal-concentration dichotomy

Suppose a sequence of normalized dangerous windows has the same fixed terminal thick-core lower bound.

Then either:

### P — persistent spacetime danger

There exist fixed `delta,c0>0` such that

\[
\int_{-\delta}^{0}E_{\chi,j}(s)ds
\ge c_0
\]

along a subsequence.  This supports a nontrivial compactness limit.

### T — temporal concentration

The local danger rises from a small state to the fixed terminal state over widths `m_j->0`.

Then the time-width inequality forces

\[
\boxed{
\|G_{\chi,j}\|_{L^p}
\to\infty
}
\]

for every uniformly chosen `p>1` bound one tries to impose; in particular the natural `L^(4/3)` source/shell channel must become unbounded.

Thus temporal intermittency is not an untyped escape.  It is routed into

1. stretching-source concentration;
2. moving/buffer transport concentration;
3. far-strain concentration;
4. or loss of the local critical energy/palinstrophy bounds used to control those terms.

---

## 7. Relation to the compactness-rigidity gap

The compactness-interpolation rigidity lemma required a persistent nontrivial time slice/subsequence.  The present result supplies the missing logical alternative:

\[
\boxed{
\text{bounded normalized source/shell block}
\Longrightarrow
\text{positive normalized persistence time}.
}
\]

Therefore, on the fully bounded channel branch, the temporal-concentration escape is closed and one may seek times with both

- strong spatial compactness;
- nontrivial local vorticity mass.

If that compactness is strong enough in `H1`, the magnitude-heterogeneity saturation `chi_mag->0` is impossible.

Status: **TEMPORAL COLLAPSE TYPED / BOUNDED-BRANCH PERSISTENCE DERIVED**.
