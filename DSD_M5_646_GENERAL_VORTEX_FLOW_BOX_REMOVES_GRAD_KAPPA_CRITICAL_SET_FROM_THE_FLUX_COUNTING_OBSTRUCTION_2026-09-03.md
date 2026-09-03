# DSD M5-646 — General vortex flow boxes remove the grad-kappa critical set from the flux-counting obstruction

Date: 2026-09-03

Status: **DSD GEOMETRIC AUDIT / M5-644--645 USED KAPPA-CLEBSCH CHARTS ON `grad kappa!=0`, BUT THE FINITE-FLUX TRANSVERSAL ARGUMENT ACTUALLY NEEDS ONLY A NONVANISHING VORTICITY VECTOR FIELD. AT EVERY POINT WITH `W!=0`, THE STANDARD FLOW-BOX THEOREM STRAIGHTENS THE ONE-DIMENSIONAL VORTEX FOLIATION AND THE GLOBAL FLUX TWO-FORM `i_W vol` DEFINES THE SAME HOLONOMY-INVARIANT TRANSVERSE MEASURE. THEREFORE ON EVERY COMPACT SUBSET OF `{W!=0}` A FINITE FLOW-BOX COVER AND FINITE-MASS COMPLETE TRANSVERSAL EXIST REGARDLESS OF WHETHER `grad kappa=0`. THE ONLY ESSENTIAL SINGULAR SET LEFT FOR THE M5-643 FLUX-RESOURCE PROBLEM IS THE VORTICITY ZERO SET `{W=0}`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Correction to the M5-645 obstruction list

M5-645 listed both

\[
\{W=0\}
\]

and

\[
\{\nabla\kappa=0\}
\]

as possible obstructions to regular flux transversals.

The second item is an obstruction only to using `kappa` itself as one Clebsch coordinate.

It is **not** an obstruction to the vortex-line foliation whenever

\[
W\ne0.
\]

---

## 2. General flow-box theorem

Let `y_0` satisfy

\[
W(y_0)\ne0.
\]

The standard flow-box theorem gives a local smooth coordinate system

\[
(s,z_1,z_2)
\]

in which the vortex trajectories are straightened into the `s` direction.

Equivalently, a local transverse disk

\[
S=\{s=0\}
\]

meets each nearby vortex line exactly once.

This construction requires only `W!=0` and smoothness.

No condition on `grad kappa` is required.

---

## 3. Transverse flux measure without Clebsch coordinates

The globally defined flux two-form is

\[
\beta:=\iota_W\,vol.
\]

Since

\[
\nabla\cdot W=0,
\]

we have

\[
\boxed{d\beta=0.}
\]

For any local transversal `S`, define

\[
\mu_{flux}(S)
:=\int_S\beta
=\int_SW\cdot n\,dA.
\]

Sliding the transversal along the same vortex-line bundle preserves this signed flux.

Thus the holonomy-invariant transverse measure exists on the entire **nonsingular vortex foliation**

\[
\{W\ne0\},
\]

not only on the regular-kappa set.

---

## 4. Compact nonsingular region has finite complete transversal

Let

\[
K\Subset\{W\ne0\}
\]

be compact.

Every point of `K` has a flow box.

Compactness gives a finite subcover

\[
\mathcal U_1,\ldots,\mathcal U_N.
\]

Choose one compact local transverse disk `S_i` in each box, enlarged/shrunk in the standard way so that the union meets every relevant local leaf segment in `K`.

Then

\[
\mathcal T_K:=\bigcup_{i=1}^NS_i
\]

has finite absolute flux mass because `W` is smooth and every disk has finite area:

\[
\boxed{
\|\mu_{flux}\|(\mathcal T_K)<\infty.
}
\]

Therefore the M5-645 finite-resource counting works on every compact set separated from the vorticity zero set.

---

## 5. Critical kappa points are harmless for flux counting

Suppose

\[
W\ne0,
\qquad
\nabla\kappa=0.
\]

The kappa-Clebsch chart degenerates, but the vortex flow box does not.

Hence a fixed-flux packet passing through such a point is still counted by an ordinary local transverse disk.

Therefore

\[
\boxed{
\{\nabla\kappa=0,\ W\ne0\}
\text{ is not a genuine escape set for transverse-flux counting.}
}
\]

This corrects the broader obstruction list in M5-645.

---

## 6. Genuine remaining singular set

The only place where the one-dimensional vortex foliation itself fails is

\[
\boxed{Z_W:=\{W=0\}.}
\]

Consequently, if infinitely many distinct past packet bundles each carrying flux at least `phi_*` evade every finite-mass complete transversal inside the fixed reservoir, their leaf representatives must accumulate essentially toward `Z_W`.

Symbolically,

\[
\boxed{
\text{infinite packet resource escape}
\Longrightarrow
\text{vortex-zero-set accumulation}.
}
\]

---

## 7. Relation to analyticity

The CE-H compact state is real analytic in space under the M5-599 external analyticity corridor.

Thus `Z_W` is a real-analytic zero set rather than an arbitrary rough singular set.

It has zero three-dimensional volume unless `W` is identically zero, but it may contain lower-dimensional analytic strata.

The next problem is therefore sharply stated:

\[
\boxed{
\text{can infinitely many disjoint fixed-flux vortex bundles accumulate on an analytic vorticity-zero set?}
}
\]

If not, the M5-643 finite-resource contradiction closes the relabeling turnover branch.

---

## 8. Firewall

A finite complete transversal is asserted only on compact subsets strictly contained in `{W!=0}`.

No claim is yet made that one can extend it across or uniformly up to `Z_W`.

The topology and local dynamics of the analytic zero set remain a genuine unresolved geometric issue.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]