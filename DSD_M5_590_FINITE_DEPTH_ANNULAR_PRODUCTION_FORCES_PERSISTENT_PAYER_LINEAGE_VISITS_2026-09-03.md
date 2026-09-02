# DSD M5-590 — Finite-depth annular production forces persistent payer-lineage visits

Date: 2026-09-03

Status: **M5-589'S POSITIVE-DENSITY ANNULAR PRODUCTION CAN BE RUN THROUGH THE M5-497 LOCAL-PAYER SATURATION INSIDE THE SAME FIXED FINITE-DEPTH REGION. ON THE QUIET COMPACT BRANCH, AFTER FINITELY MANY POSSIBLE NEW-LABEL ADDITIONS, ONE FIXED PERSISTENT MATERIAL-FLUX LINEAGE MUST PAY A FIXED POSITIVE SHARE OF THE ANNULAR STRETCHING PRODUCTION AT POSITIVE FREQUENCY. THUS THE EULERIAN PRODUCTION REGION AND MATERIAL GENEALOGY ARE NOW LINKED AT THE SINGLE-LINEAGE LEVEL. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-589

There is a fixed annulus

\[
\mathcal A_*
=
\{\rho_* -\delta_r<|y|<\rho_*+\delta_r\}
\]

and a positive-density set of fixed-length similarity-time windows on which

\[
\boxed{
Q_{ann}(\theta)
:=
\int_{\mathcal A_*}W\cdot\Sigma W\,dy
\ge q_{ann}>0.
}
\]

All relevant derivatives are uniformly bounded on a fixed enlargement of this annulus by the smooth compact-hull bounds.

## 2. Restrict the M5-497 represented/residual split to the annulus

Let

\[
\mathcal L(\theta)=\{L_1,\ldots,L_N\},
\qquad N\le N_{max},
\]

be the current persistent material-flux lineage family, with coherent carrier neighborhoods \(C_i(\theta)\).

Set

\[
\mathcal C(\theta)
=
\bigcup_i C_i(\theta).
\]

Split

\[
Q_{ann}=Q_{rep}^{ann}+Q_{res}^{ann},
\]

where

\[
Q_{rep}^{ann}
=
\int_{\mathcal A_*\cap\mathcal C(\theta)}W\cdot\Sigma W\,dy,
\]

and

\[
Q_{res}^{ann}
=
\int_{\mathcal A_*\setminus\mathcal C(\theta)}W\cdot\Sigma W\,dy.
\]

At every annular production event,

\[
Q_{rep}^{ann}\ge \frac12q_{ann}
\quad\lor\quad
Q_{res}^{ann}\ge \frac12q_{ann}.
\]

## 3. A residual annular payer creates a fixed coherent flux packet

On the fixed enlarged annulus,

\[
\|\Sigma\|_\infty\le S_*<\infty.
\]

Hence

\[
Q_{res}^{ann}\ge\frac12q_{ann}
\]

implies

\[
\boxed{
\int_{\mathcal A_*\setminus\mathcal C}|W|^2dy
\ge
\frac{q_{ann}}{2S_*}
=:e_{ann}>0.
}
\]

Because \(\mathcal A_*\) has finite volume, there is a point with fixed vorticity amplitude.

The uniform \(C^1\) bound then thickens it to a fixed-radius ball carrying a fixed lower vorticity amplitude; after the usual angular-sector shrinking, that ball contains a coherent directed vorticity packet with

\[
\boxed{|\Phi_{new}|\ge\phi_{ann}>0.}
\]

The packet may protrude slightly across the original annular boundary. Define once and for all a fixed enlargement

\[
\mathcal A_*^+
:=
\{\operatorname{dist}(y,\mathcal A_*)<r_{pay}\},
\]

where \(r_{pay}\) is the uniform payer-packet radius.

Then the entire extracted packet lies inside \(\mathcal A_*^+\).

## 4. Genealogy of the residual packet

Exactly as in M5-497, the fixed-flux packet has only the following quiet options:

\[
\boxed{
\text{existing-lineage absorption}
\lor
\text{new/replacement fixed-flux label}
\lor
\text{already typed costed exit}.
}
\]

The current hard branch excludes the costed exit alternatives.

M5-488 bounds the number of quietly stored fixed-flux labels by

\[
N\le N_{max}.
\]

Therefore recurrent annular residual production cannot create genuinely new labels indefinitely.

After finitely many additions, every recurrent fixed-share annular payer is absorbed into a saturated finite persistent family

\[
\mathcal L_{sat}
=
\{L_1,\ldots,L_{N_{sat}}\},
\qquad
N_{sat}\le N_{max}.
\]

## 5. Positive annular production is eventually represented by the persistent family

On the saturated no-exit branch, after decreasing constants harmlessly if needed,

\[
\boxed{
\sum_{i=1}^{N_{sat}}Q_i^{ann}(\theta)
\ge q_{rep}>0
}
\]

on a positive-density subset of the M5-589 annular production windows, where a bounded-overlap partition of unity subordinate to the coherent carrier neighborhoods defines

\[
Q_i^{ann}
:=
\int_{\mathcal A_*^+}
\chi_i W\cdot\Sigma W\,dy.
\]

Since only finitely many labels exist, at least one fixed lineage \(L_{\alpha_*}\) satisfies

\[
\boxed{
Q_{\alpha_*}^{ann}(\theta)
\ge
q_{pay}:=
\frac{q_{rep}}{N_{sat}}>0
}
\]

on a positive-density subsequence of annular production events.

Equivalently, the coherent carrier of one fixed persistent lineage intersects \(\mathcal A_*^+\) and pays positive local production with positive similarity-time frequency.

## 6. Quantitative lineage-visit mark

Define the marked event

\[
a_{ann,\alpha_*}(\theta)=1
\]

when both

1. the carrier of \(L_{\alpha_*}\) intersects \(\mathcal A_*^+\), and
2. its localized production contribution is at least \(q_{pay}\).

Then on the inherited invariant component,

\[
\boxed{
\langle a_{ann,\alpha_*}\rangle>0.
}
\]

This is the desired single-lineage Eulerian/material overlap.

## 7. What has now been proved

The M5-588 firewall

\[
\text{Eulerian production shell}
\quad\text{vs.}\quad
\text{material lineage}
\]

has been crossed at the payer-lineage level:

\[
\boxed{
\text{finite-depth production}
\Longrightarrow
\text{positive-frequency visits of a fixed persistent production-paying lineage}
}
\]

unless an already typed replacement/export/costed exit occurs.

## 8. What remains

This note does not yet show that the **same persistent dual pair** from M5-490 occupies the annulus.

However M5-455 is precisely a local formation theorem: a productive principal carrier on a quiet bounded block forces a transverse companion unless a strong exit occurs.

Therefore the next step is to apply M5-455 at the recurrent annular payer events of \(L_{\alpha_*}\), then use the finite label set to extract a fixed companion \(L_{\beta_*}\).

Status: **A FIXED PERSISTENT MATERIAL-FLUX LINEAGE NOW PAYS THE FINITE-DEPTH ANNULAR PRODUCTION AT POSITIVE FREQUENCY. THE REMAINING BRIDGE IS ONLY FROM THIS PRODUCTIVE LINEAGE TO ITS RECURRENT DUAL COMPANION, NOT FROM AN ARBITRARY MATERIAL GENEALOGY TO AN EULERIAN SPHERE. GLOBAL REGULARITY REMAINS UNPROVED.**