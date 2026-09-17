# DSD M19-371 — Analytic zero-kappa skeleton has zero enstrophy measure, so all volumetric critical and sheath structure is through-flow

Date: 2026-09-17  
Canonical ID: **M19-371**

Status: **ACTIVE VOLUMETRIC-TURNOVER REDUCTION / ANALYTICITY-DEPENDENT SKELETON-SHEATH SEPARATION / NOT A CONTRADICTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M5-639

On the CE-H analyticity corridor,

\[
Z_0:=\{W\ne0,\ \kappa=0\}
\]

satisfies

\[
\boxed{|Z_0|=0,}
\]

and hence

\[
\boxed{\int_{Z_0}|W|^2dy=0.}
\]

Thus the persistent zero-kappa relabeling survivor is at most a lower-dimensional material flux skeleton. It carries no direct three-dimensional enstrophy measure.

This step inherits the external spatial-analyticity theorem used in M5-599/M5-639.

## 2. Combine with M19-369

M19-369 decomposes the retained critical/relabeling architecture into

\[
\text{transient positive-kappa critical seed}
+
\text{persistent zero-mean/zero-kappa flux spine}
+
\text{renewing high-amplitude sheath}.
\]

M5-639 now fixes the dimensional role of the persistent spine:

\[
\boxed{\text{persistent spine carries zero volumetric enstrophy.}}
\]

Therefore every order-one three-dimensional enstrophy carrier belongs to a nonzero-kappa volumetric population outside the persistent skeleton.

## 3. Critical seed is necessarily volumetric through-flow

The M19-364--366 critical seed has positive material cross-sectional area before activation and reaches an order-one active carrier.

Since its mean multiplier is

\[
\bar\kappa\to\frac32>0,
\]

it is not contained in the persistent zero-kappa skeleton.

Hence

\[
\boxed{G_{seed}^{3/2}\subset G_{volumetric\ throughflow}}
\]

on the retained relabeling branch.

## 4. High-amplitude sheath is necessarily volumetric through-flow

M5-638 already shows that any positive-thickness material neighborhood of a persistent zero-kappa surface expands at rate \(3/2\) and cannot remain one bounded material sheath indefinitely.

M5-639 adds that the zero-kappa skeleton itself has no three-dimensional enstrophy measure.

Thus all high-amplitude/enstrophy-bearing mass around the skeleton is carried by

\[
\boxed{\kappa\ne0\text{ volumetric labels undergoing material turnover}.}
\]

## 5. Rayleigh and production budgets are entirely off the skeleton

The whole-space CE-H identity is

\[
\int\kappa|W|^2dy=-P<0.
\]

The persistent zero-level skeleton contributes zero to this integral by both \(\kappa=0\) and zero enstrophy measure.

Therefore the full volumetric Rayleigh budget and all enstrophy-weighted compensation live in the through-flow population:

\[
\boxed{
\int_{\kappa\ne0}\kappa|W|^2dy=-P<0.
}
\]

This removes the possibility that the lower-dimensional persistent skeleton itself stores a hidden volumetric covariance budget.

## 6. Stronger normal form

The relabeling survivor can now be represented as

\[
\boxed{
\text{measure-zero persistent material flux skeleton}
+
\text{three-dimensional nonzero-kappa renewal flow}.
}
\]

Within the renewal flow, the M19-369 semantic roles are:

- incoming/dormant critical seed labels;
- active positive-kappa transverse-inflation labels;
- extensional/Rayleigh compensator labels;
- high-amplitude nonpositive-kappa sheath labels;
- outgoing/decompactifying labels.

These roles may be successive phases of the same material labels; no disjointness is assumed.

## 7. Consequence for renewal accounting

M19-370's nonadditivity firewall becomes stronger.

Since all volumetric roles belong to one turnover sea around a measure-zero persistent skeleton, semantic event counting is especially unsafe:

\[
\boxed{
N_{seed}+N_{sheath}+N_{compensator}
\not\Rightarrow
N_{material\ renewals}^{sum}.
}

One material cohort may realize several roles during one passage through the active core.

A useful event must therefore be tied to an actual material/projective transversal crossing, not to a named phase.

## 8. Canonical event target

The new gate is sharpened to

\[
\boxed{
\mathcal T_{cross}^{vol}:
\text{construct a codimension-one material/projective transversal separating incoming and outgoing volumetric labels around the persistent skeleton,}
}
\]

such that every complete active renewal passage crosses it with bounded multiplicity and a fixed signed/nonrecyclable charge.

If no such transversal exists, the stationary through-flow picture remains compatible with the present exact transport laws.

## 9. Firewall

The zero-volume statement does not classify the topology or dimension of the analytic zero set beyond three-dimensional measure zero. It may contain surfaces, curves, singular strata, or combinations thereof.

Likewise, turnover of all volumetric enstrophy does not imply infinite dissipation without a nonreuse/additivity theorem.

## 10. Audit verdict

**PASS — under the inherited analyticity corridor, all three-dimensional enstrophy-bearing structure is necessarily material through-flow around a lower-dimensional persistent flux skeleton.**

This sharply identifies the object that a future renewal theorem must count, but does not by itself prohibit a stationary conveyor.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
