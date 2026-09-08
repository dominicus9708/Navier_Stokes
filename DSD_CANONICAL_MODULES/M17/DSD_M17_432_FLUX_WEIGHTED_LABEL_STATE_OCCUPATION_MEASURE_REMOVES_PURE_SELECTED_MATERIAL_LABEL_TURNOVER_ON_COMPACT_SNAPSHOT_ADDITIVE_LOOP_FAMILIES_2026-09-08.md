# DSD M17-432 — Flux-weighted label-state occupation measure removes pure selected-material-label turnover on compact snapshot-additive loop families

Date: 2026-09-08  
Canonical ID: **M17-432**

Status: **ACTIVE LABEL-TURNOVER REDUCTION / FLUX-WEIGHTED OCCUPATION-MEASURE EXTENSION OF M17-358 AND M17-420**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Problem

M17-359 preserves true material vortex-line genealogy on regular exact CE-H.

M17-358 proves that snapshot fragmentation of a coherent material-flux family does not change flux-linear additive currencies.

M17-420 proves that time turnover among finite-jet states on one compact loop orbit cannot evade a snapshot raw-`H2` payer: an occupation measure forces one fixed finite-jet class to carry positive asymptotic time mass.

After M17-424--431, one remaining apparent escape is that the proof-selected active loop/tube label changes with time, so no single material label has positive time density.

The present module shows that **pure label turnover is not an independent escape** when the whole positive-flux label-state bundle remains compact and the payer is snapshot-additive in flux.

## 2. Material label space and positive flux measure

Let `Lambda` be a coherent material label space for regular CE-H vortex loops/tubes.

At similarity time `theta`, let

\[
d\Phi_\theta(\lambda)\ge0
\]

be the oriented positive flux measure on the retained label family.

Assume

\[
\boxed{
0<\Phi_*
\le
\Phi_{tot}(\theta)
:=
\int_\Lambda d\Phi_\theta
<\infty
}
\]

on the retained interval.

The measure need not be materially conserved; viscosity may change `dPhi_theta` through the exact CE-H flux law. Only positivity, finite total mass, and the retained lower total flux are used.

Normalize it at each time:

\[
\boxed{
dp_\theta(\lambda)
:=
\frac{d\Phi_\theta(\lambda)}{\Phi_{tot}(\theta)}.
}
\]

Then `p_theta` is a probability measure on the material label space.

## 3. Compact label-state bundle

Let

\[
Z_\lambda(\theta)
\]

denote the represented loop/tube state of material label `lambda`.

Assume the retained label-state pairs

\[
(\lambda,Z_\lambda(\theta))
\]

remain in a compact metric space `K`.

This compactness includes whichever geometric, amplitude, coefficient-jet, tubular-chart, and domain bounds are required by the snapshot payer under consideration.

If this compactness fails, the module does not hide the loss; it returns the corresponding decompactification/interface/domain exit.

## 4. Flux-weighted spacetime occupation probability

Define the empirical probability measure on the compact label-state space by

\[
\boxed{
\mu_T
:=
\frac1T
\int_0^T
(\lambda,Z_\lambda(\theta))_\#p_\theta\,d\theta.
}
\]

For a Borel set `A subset K`,

\[
\mu_T(A)
=
\frac1T
\int_0^T
\int_\Lambda
\mathbf 1_A(\lambda,Z_\lambda(\theta))
\,dp_\theta(\lambda)d\theta.
\]

Each `mu_T` is a probability measure.

By compactness of `K`, a sequence `T_j -> infinity` has

\[
\boxed{
\mu_{T_j}\rightharpoonup^*\mu
}
\]

for some probability measure `mu` on `K`.

## 5. Countable robust payer classes

Suppose the retained regular compact state bundle is covered by countably many open robust classes

\[
\boxed{
K=\bigcup_{n\ge1}\mathcal G_n.
}
\]

For the M17-416--419 application, the classes may be chosen from finite coefficient-jet order and fixed nondegeneracy thresholds, with the analytic infinite-flat state removed by M17-419.

Assume every state in `G_n` carries a uniform nonnegative snapshot payer

\[
q(Z)\ge q_n>0
\]

in a currency that is additive under the material flux measure.

Because `mu(K)=1`, countable subadditivity implies that at least one fixed class `G_n*` has

\[
\boxed{
\mu(\mathcal G_{n_*})=\beta_*>0.
}
\]

Since `G_n*` is open, Portmanteau gives

\[
\boxed{
\liminf_{j\to\infty}
\mu_{T_j}(\mathcal G_{n_*})
\ge\beta_*>0.
}
\]

Thus a fixed robust payer class has positive **flux-weighted time-label occupation**, even if every individual label has zero asymptotic time density.

## 6. Return to the unnormalized positive flux

By definition,

\[
\int_\Lambda
\mathbf1_{\mathcal G_{n_*}}
\,d\Phi_\theta
=
\Phi_{tot}(\theta)
\int_\Lambda
\mathbf1_{\mathcal G_{n_*}}
\,dp_\theta.
\]

Since

\[
\Phi_{tot}(\theta)\ge\Phi_*,
\]

we obtain

\[
\boxed{
\liminf_{j\to\infty}
\frac1{T_j}
\int_0^{T_j}
\int_\Lambda
\mathbf1_{\mathcal G_{n_*}}
\,d\Phi_\theta d\theta
\ge
\Phi_*\beta_*.
}
\]

Therefore the class carries a fixed positive amount of unnormalized flux-time occupation.

## 7. Additive snapshot payer survives arbitrary label turnover

If the snapshot payer is flux-linear/additive, then on `G_n*`

\[
Q(\theta)
\ge
q_{n_*}
\int_\Lambda
\mathbf1_{\mathcal G_{n_*}}
\,d\Phi_\theta.
\]

Hence

\[
\boxed{
\liminf_{j\to\infty}
\frac1{T_j}
\int_0^{T_j}Q(\theta)d\theta
\ge
q_{n_*}\Phi_*\beta_*>0.
}
\]

No single material label recurrence is required.

The active label may change at every time.

What matters is compactness of the whole label-state bundle, positive total retained flux, and pointwise flux-additivity of the payer.

## 8. Application to the M17-420 finite-jet raw-H2 mechanism

M17-416--419 supply countable robust finite-jet classes on the retained analytic regular loop branch.

M17-420 converts positive time occupation of one such class into a pointwise-in-time raw-`H2` packet lower bound and then uses the M17-413--414 spatial/time packet factorization.

The present module extends the occupation step from one loop orbit to a compact positive-flux family of material labels.

Therefore

\[
\boxed{
G_{pure\ selected\ label\ turnover}
}

is not an independent way to remove the M17-420 snapshot-additive finite-jet payer as long as the label-state bundle stays compact and the flux measure stays retained.

The label identity may rotate; the integrated payer does not disappear.

## 9. Important scope firewall: history-dependent payers

This theorem applies to **snapshot-additive** payer classes.

It does not automatically apply to a history-dependent one-label quantity such as the M17-188 recurrent covariance identity, because that identity compares logarithmic changes along the same material history.

Thus M17-429--431 remain necessary for the decompactifying covariance branch.

The present theorem may be used directly for snapshot raw-`H2`, zero-corridor, or other nonnegative flux-linear pointwise currencies whose uniform lower bounds are already certified.

## 10. Exact surviving exits

Pure label turnover is reduced to failures of the hypotheses above:

\[
\boxed{
\begin{aligned}
G_{selected\ label\ turnover}
\Longrightarrow{}&
G_{label/state\ noncompactness}\\
&\lor G_{positive\ total\ flux\ thinning/loss}\\
&\lor G_{payer\ class\ nonuniformity/scale\ mismatch}\\
&\lor G_{flux\ measure\ nonadditivity/sign\ cancellation}\\
&\lor G_{material\ genealogy/interface/CEH/domain\ loss}.
\end{aligned}
}
\]

On the retained positive-flux compact regular snapshot-additive branch, turnover alone is bookkeeping rather than a PDE escape.

## 11. Relation to parent-to-record closure

This module is a second-generation/late-CE-H occupation theorem.

To generate a first-generation contradiction from its positive flux-time payer, one still needs the representation-safe parent-to-record map, bounded overlap, and the appropriate M17-307 or M17-405 ancestral scaling.

Those upstream scale/genealogy dependencies remain OPEN.

## 12. DSD role

DSD is used only to distinguish `which label is selected` from `how much additive positive measure is present`.

The proof is ordinary normalization of finite positive measures, weak-* compactness of probability measures, Portmanteau, and countable additivity.

## 13. Audit verdict

**PASS as a pure selected-label-turnover reduction for compact snapshot-additive positive-flux families.**

Individual-label recurrence is not necessary for an additive payer; a joint flux-weighted label-state occupation measure is sufficient.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
