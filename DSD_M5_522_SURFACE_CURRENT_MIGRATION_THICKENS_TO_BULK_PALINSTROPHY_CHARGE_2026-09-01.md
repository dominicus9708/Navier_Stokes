# DSD M5-522 — Surface-current migration thickens to a bulk palinstrophy charge on the globally smooth compact branch

Date: 2026-09-01

Status: **SURFACE-TO-BULK THICKENING / M5-521 PRICES FIXED MATERIAL-LABEL MARKER MIGRATION BY A POSITIVE `L2` MATERIAL-SURFACE CURRENT CHARGE / ON THE M5-508 GLOBALLY SMOOTH COMPACT BRANCH, UNIFORM `C^2` SPACE BOUNDS AND TIME-EQUICONTINUITY TURN ANY FIXED SURFACE-CURRENT CHARGE INTO A FIXED THREE-DIMENSIONAL SPACE-TIME PALINSTROPHY CHARGE / HENCE RECURRENT MARKER MIGRATION IS NOT A NEW INDEPENDENT HARD CORE: IT FEEDS THE ALREADY EXISTING PALINSTROPHY/AXIAL-PRODUCTION LEDGER / THIS DOES NOT CREATE A CONTRADICTION BECAUSE M5-486 ALREADY ALLOWS POSITIVE RECURRENT PALINSTROPHY PAID BY POSITIVE AXIAL PRODUCTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-521

A fixed material-label migration event on a controlled material surface produces

\[
\boxed{
\int_I\int_{\Sigma(\theta)}
|J_{\Sigma}|^2\,dA\,d\theta
\ge j_*>0,
}
\]

where

\[
J_{\Sigma}
=(\nabla\times W)\times n.
\]

Assume the retained event satisfies

\[
|I|\le T_*,
\qquad
\sup_{\theta\in I}\operatorname{Area}(\Sigma(\theta))\le A_*.
\]

These are the controlled material-surface geometry bounds used in the compact finite-lineage branch.

---

## 2. Extract one point with nontrivial current amplitude

By averaging over the event cylinder,

\[
\sup_{(x,\theta)\in\Sigma(\theta)\times I}
|J_{\Sigma}(x,\theta)|^2
\ge
\frac{j_*}{T_*A_*}.
\]

Define

\[
\boxed{
a_*:=\left(\frac{j_*}{T_*A_*}\right)^{1/2}>0.}
\]

Then there exists

\[
(x_*,\theta_*)
\]

with

\[
\boxed{|J_{\Sigma}(x_*,\theta_*)|\ge a_*.}
\]

Since orthogonal projection cannot increase norm,

\[
|J_{\Sigma}|
\le
|\nabla\times W|.
\]

Hence

\[
\boxed{
|\nabla\times W(x_*,\theta_*)|
\ge a_*.
}
\]

---

## 3. Global smooth compactness supplies a uniform spatial continuity scale

M5-507--508 give uniform global bounds in every fixed Sobolev order and therefore in every fixed bounded `C^k` norm.

In particular there is

\[
M_{curl,1}<\infty
\]

such that

\[
\boxed{
\sup_{\widehat{\mathfrak H}}
\|\nabla(\nabla\times W)\|_{L^\infty}
\le M_{curl,1}.
}
\]

If `M_(curl,1)=0`, then `curl W` is spatially constant; finite enstrophy forces it to vanish, contradicting `a_*>0`.

Thus on the active branch we may define

\[
\boxed{
r_*:=\frac{a_*}{4M_{curl,1}}>0.}
\]

For every

\[
|x-x_*|\le r_*,
\]

we obtain

\[
|\nabla\times W(x,\theta_*)|
\ge
\frac34a_*
\]

and in particular

\[
\boxed{
|\nabla\times W(x,\theta_*)|
\ge
\frac12a_*.
}
\]

---

## 4. Instantaneous bulk palinstrophy lower bound

For divergence-free `W`, the whole-space identity gives

\[
\|\nabla W\|_2^2
=
\|\nabla\times W\|_2^2.
\]

Locally we only need the pointwise inequality

\[
|\nabla W|\ge c|\nabla\times W|.
\]

Therefore at the event time

\[
\begin{aligned}
P(\theta_*)
&:=
\int_{\mathbb R^3}|\nabla W|^2dy\\
&\ge
c\int_{B_{r_*}(x_*)}
|\nabla\times W|^2dy.
\end{aligned}
\]

Using the amplitude lower bound,

\[
\boxed{
P(\theta_*)
\ge
c_0a_*^2r_*^3
=:
p_{mig}>0.
}
\]

Quantitatively,

\[
p_{mig}
\asymp
\frac{a_*^5}{M_{curl,1}^3}
\]

up to universal geometric constants.

---

## 5. Time thickening

Global smooth compactness also gives uniform time-equicontinuity of fixed spatial derivatives through the similarity Navier--Stokes equation.

In particular, on the compact hull there is

\[
M_{curl,t}<\infty
\]

such that

\[
\boxed{
\|\partial_\theta(\nabla\times W)\|_{L^\infty}
\le M_{curl,t}.
}
\]

Choose

\[
\delta_*
:=
\frac{a_*}{8M_{curl,t}}
\]

when `M_(curl,t)>0`; if it vanishes, the current amplitude is already time-stationary over the event.

Then for

\[
|\theta-\theta_*|\le\delta_*,
\]

and after shrinking the spatial radius by a fixed factor if needed,

\[
|\nabla\times W(x,\theta)|
\ge
\frac14a_*
\]

on a fixed ball around `x_*`.

Hence

\[
\boxed{
\int_{\theta_*-\delta_*}^{\theta_*+\delta_*}
P(\theta)\,d\theta
\ge
c_{mig}>0.
}
\]

Thus one fixed marker-migration event carries a fixed three-dimensional spacetime palinstrophy cost.

---

## 6. Positive-frequency migration gives positive mean palinstrophy

Suppose fixed-size marker-migration events recur with positive similarity-time frequency.

Because event durations and generation roof times are uniformly controlled on the compact branch, select a disjoint positive-density subfamily of thickened event intervals.

Summing the Section 5 lower bound and dividing by long similarity time gives

\[
\boxed{
\langle P\rangle
\ge
p_{mig,mean}>0.
}
\]

Thus

\[
\boxed{
H_{marker\ migration}
\Longrightarrow
\text{positive recurrent bulk palinstrophy charge}.
}
\]

This absorbs the migration branch into a ledger already present in M5-493 and M5-486.

---

## 7. Reconnection to the similarity enstrophy budget

M5-486 gives the exact invariant average identity

\[
\boxed{
\frac14\langle E\rangle
+\langle P\rangle
=\langle Q\rangle.
}
\]

Therefore recurrent marker migration forces an additional positive payment requirement

\[
\boxed{
\langle Q\rangle
\ge
\frac14\langle E\rangle
+p_{mig,mean}.
}
\]

The migration current is not free.

It must be supported by the same positive average vortex-stretching production that maintains the rest of the compact recurrent system.

---

## 8. This is a branch absorption, not a contradiction

Positive mean palinstrophy is already compatible with the compact hard core.

M5-493 proved such a positive lower bound from recurrent noncollinear dual geometry even without the marker-migration mechanism.

Therefore M5-522 does **not** provide

\[
\langle P\rangle=\infty
\]

or any contradiction with the enstrophy balance.

It proves instead that marker migration cannot remain an independent loophole outside the existing derivative ledger.

The updated DSD interpretation is

\[
\boxed{
\text{marker migration}
\to
\text{surface current}
\to
\text{bulk palinstrophy}
\to
\text{axial production payment}.
}
\]

---

## 9. Consequence for the anchored-pair endpoint

The M5-516--519 anchored noncollinear pair had two apparent amplitude loopholes:

1. a uniformly nondegenerate marker, where the M5-517 effective-eigenvalue ledger applies;
2. marker migration across a persistent material surface.

M5-522 shows that the second case does not create a genuinely new endpoint class.

It is absorbed into the positive-palinstrophy branch.

Thus the anchored pair can now be described as

\[
\boxed{
\text{fixed noncollinear frame}
+
\tau_i=-\mathcal D_i
+
\big(
\text{effective-eigenline amplitude recurrence}
\lor
\text{recurrent palinstrophy-paid redistribution}
\big).
}
\]

---

## 10. External-theory audit

Established backward self-similar Liouville results exclude several exact self-similar profile classes under `L^p`, Morrey, decay, or Type-I hypotheses.

Recent 2026 Pineau--Vicol results further exclude specified Type-I rotated self-similar and short-factor rotated discretely self-similar regimes.

However the present compact hull may be aperiodic or long-period recurrent and M5-510 showed that global smooth compactness does not automatically provide the required spatial `1/|y|` Type-I velocity decay.

Therefore no external theorem currently imported into this proof line eliminates the full M5-522 recurrent compact class.

Unreviewed or unverified manuscripts claiming complete Navier--Stokes regularity are not used as proof dependencies.

---

## 11. Highest-value next target

After M5-522, repeatedly deriving new unsigned costs is unlikely to close the compact recurrent hull: every such cost can be paid by the positive average production `Q`.

The remaining high-value alternatives are now sharper.

### A. Rigidity of the anchored effective eigenline

Use the two fixed noncollinear directions and

\[
\Sigma W_i+\Delta W_i=\lambda_iW_i
\]

on nondegenerate markers to ask whether incompressibility and one common velocity/strain field can support both effective eigenlines recurrently without becoming an exact stationary/RSS/RDSS geometry.

### B. Spatial decay recovery

Use global all-order compactness plus persistent finite-enstrophy genealogy to determine whether the missing

\[
|U(y)|\lesssim(1+|y|)^{-1}
\]

can be recovered from the **Navier--Stokes dynamics**, not from abstract Sobolev compactness alone.

Either result would connect the survivor to existing Liouville/Type-I theorems much more directly than another unsigned ledger.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
