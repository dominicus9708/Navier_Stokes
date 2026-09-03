# DSD M16-023 — Resolve axial strain heterogeneity into strain-derivative or vorticity-helicity channels

Date: 2026-09-03
Canonical ID: **M16-023**

Status: **INTERNAL CE-H CONSTITUTIVE REFINEMENT / THE SAME-TUBE AXIAL STRAIN HETEROGENEITY FORCED IN M16-022 IS NOT AN ABSTRACT GRADIENT CHARGE. UNDER `Sigma W = sigma W`, ITS VORTEX-LINE DERIVATIVE SATISFIES AN EXACT IDENTITY INVOLVING ONLY THE STRAIN--VORTICITY DERIVATIVE CONTRACTION AND THE SELF-HELICITY DENSITY `W dot curl W`. HENCE THE RESIDENCE-COVARIANCE BRANCH REQUIRES POSITIVE-DENSITY ACTIVITY IN AT LEAST ONE OF THESE TWO CONCRETE PDE CHANNELS, OR ELSE MARKER/SHEATH TURNOVER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H eigenline input

In the CE-H branch,

\[
\Sigma W=\sigma W.
\]

Because the antisymmetric part of `grad U` annihilates `W`, this is equivalent to

\[
\boxed{
(W\cdot\nabla)U=\sigma W.
}
\]

We now differentiate this identity in a way that preserves the vortex-line geometry.

---

## 2. Divergence of the eigenline equation

Take divergence:

\[
\nabla\cdot\big((W\cdot\nabla)U\big)
=\nabla\cdot(\sigma W).
\]

Since

\[
\nabla\cdot U=0,
\qquad
\nabla\cdot W=0,
\]

we obtain

\[
\boxed{
W\cdot\nabla\sigma
=
\partial_iW_j\,\partial_jU_i.
}
\]

Decompose

\[
\partial_jU_i
=\Sigma_{ij}+\mathcal R_{ij},
\]

where

\[
\mathcal R_{ij}
=-\frac12\varepsilon_{ijk}W_k.
\]

Therefore

\[
\partial_iW_j\,\mathcal R_{ij}
=-\frac12W\cdot(\nabla\times W).
\]

Hence the exact identity is

\[
\boxed{
W\cdot\nabla\sigma
=
\Sigma:\nabla W
-\frac12W\cdot(\nabla\times W).
}
\]

On the active set `W = rho xi`,

\[
\boxed{
\rho\,(\xi\cdot\nabla\sigma)
=
\Sigma:\nabla W
-\frac12W\cdot(\nabla\times W).
}
\]

---

## 3. M16-022 gives a linewise derivative floor

M16-022 shows that on the same-marker recycling branch, with positive time density, one has two points `Y,Z` on the same material vortex tube for which

\[
\sigma(Y)-\sigma(Z)\ge c_{\rm het}>0.
\]

Along the vortex-line arclength segment joining them,

\[
\sigma(Y)-\sigma(Z)
=\int_Z^Y(\xi\cdot\nabla\sigma)\,ds.
\]

Therefore

\[
\boxed{
\int_Z^Y|\xi\cdot\nabla\sigma|\,ds
\ge c_{\rm het}.
}
\]

On the coherent active segment, `rho >= rho_* > 0` after restricting to the fixed high-amplitude subsegment. Thus

\[
\boxed{
\int_Z^Y|W\cdot\nabla\sigma|\,ds
\ge \rho_*c_{\rm het}
}
\]

up to the usual fixed-segment restriction/thickening.

---

## 4. Exact two-channel payer split

Using the identity of Section 2,

\[
|W\cdot\nabla\sigma|
\le
|\Sigma:\nabla W|
+\frac12|W\cdot\nabla\times W|.
\]

Therefore the positive linewise strain-variation charge from M16-022 forces at least one of

\[
\boxed{
\int_{\Gamma_*}|\Sigma:\nabla W|\,ds
\ge c_{SD}>0
}
\]

or

\[
\boxed{
\int_{\Gamma_*}|W\cdot\nabla\times W|\,ds
\ge c_H>0.
}
\]

Uniform smoothness and time thickening turn one of these into a positive-density coherent spacetime event family.

Define

\[
\boxed{C_{SD}^{axial}}
\]

for the first channel and

\[
\boxed{C_{H_W}^{axial}}
\]

for the second.

Thus

\[
\boxed{
P_1^{\rm axial\ het}
\Longrightarrow
C_{SD}^{axial}
\ \lor\ 
C_{H_W}^{axial}.
}
\]

---

## 5. Relation to previous canonical modules

The `C_SD` channel is a signed strain--vorticity-derivative interaction. It is more specific than the unsigned P4 packet of M16-014.

The `C_H_W` channel uses

\[
W\cdot\nabla\times W,
\]

which is the helicity density of the vorticity field `W`, not the ordinary fluid helicity `U dot W`.

This distinction is important: the Nadirashvili/Beltrami audit in M12--M13 concerns alignment of `W` with `curl W`; a large scalar `W dot curl W` does not by itself imply Beltrami alignment because the transverse component may remain nonzero.

Hence neither channel may be silently identified with a previously closed branch.

---

## 6. Integrated consistency check

Using

\[
\nabla\cdot\Sigma=-\frac12\nabla\times W
\]

and `Sigma W = sigma W`,

\[
\Sigma:\nabla W
=
\nabla\cdot(\Sigma W)
-(\nabla\cdot\Sigma)\cdot W
=
W\cdot\nabla\sigma
+\frac12W\cdot\nabla\times W.
\]

This reproduces the identity above and checks the sign.

Over all space,

\[
\int W\cdot\nabla\sigma\,dy
=\int\nabla\cdot(\sigma W)\,dy=0
\]

under the established decay. Hence

\[
\boxed{
\int\Sigma:\nabla W\,dy
=
\frac12\int W\cdot\nabla\times W\,dy.
}
\]

This is a signed global balance, not a positivity statement.

---

## 7. Updated branch

Combining M16-021, M16-022, and this note gives

\[
\boxed{
\text{negative enstrophy-weighted `kappa`}
\Longrightarrow
B_{\rm flux}^{-}
\ \lor\ 
T_{\rm marker/sheath}
\ \lor\ 
C_{SD}^{axial}
\ \lor\ 
C_{H_W}^{axial}.
}
\]

The first two alternatives are already genuine material-resource/turnover mechanisms.

The last two are the remaining same-tube PDE channels. They must now be audited for whether a compact recurrent CE-H state can support them indefinitely without forcing either Beltrami collapse, strain-sheet turnover, or another signed resource drift.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
