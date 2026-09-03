# DSD M5-605 — Residual finite-core negative-kappa budget extracts a coherent fixed-flux sink packet

Date: 2026-09-03

Status: **RESIDUAL-SINK EXTRACTION / AFTER M5-604 THE STRICT NEGATIVE CE-H BUDGET IS CONFINED TO ONE FIXED SIMILARITY CORE / SPLITTING THAT CORE INTO THE CURRENT PERSISTENT-LINEAGE CARRIER NEIGHBORHOODS AND THEIR RESIDUAL, ANY FIXED NEGATIVE RESIDUAL SHARE FORCES A POINT WHERE `G=-kappa|W|^2=-W·Delta W` IS UNIFORMLY POSITIVE / COMPACT C3 BOUNDS THICKEN THIS TO A FIXED BALL WITH NONZERO VORTICITY AND STRICTLY NEGATIVE KAPPA / DIRECTION COHERENCE THEN EXTRACTS A FIXED DIRECTED VORTICITY-FLUX PATCH / HENCE A RECURRENT RESIDUAL NEGATIVE-KAPPA PAYER IS A COHERENT FIXED-FLUX GENEALOGICAL OBJECT, NOT AN ARBITRARY DIFFUSE BACKGROUND / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Finite-core negative budget

M5-604 gives a fixed radius `R_kappa` and `c_kappa>0` such that on the marked CE-H component

\[
\boxed{
\int_{B_{R_\kappa}} -\kappa|W|^2dy
\ge c_\kappa>0.
}
\]

Define

\[
\boxed{G(y,\theta):=-\kappa|W|^2=-W\cdot\Delta W.}
\]

The second equality is valid globally on CE-H.

---

## 2. Persistent carrier / residual split

Let

\[
\mathcal C(\theta)
=
\bigcup_{j=1}^{N}C_j(\theta)
\]

be fixed-size coherent neighborhoods representing the finite persistent lineage network inside `B_{R_kappa}`.

Write

\[
\int_{B_{R_\kappa}}G
=
\int_{\mathcal C}G
+
\int_{B_{R_\kappa}\setminus\mathcal C}G.
\]

At every time with total negative budget at least `c_kappa`, either

\[
\boxed{
\int_{\mathcal C}G\ge\frac12c_\kappa
}
\]

or

\[
\boxed{
\int_{B_{R_\kappa}\setminus\mathcal C}G
\ge\frac12c_\kappa.
}
\]

The first branch is already represented by the persistent network in enstrophy weighting.

The second is the residual sink branch.

---

## 3. Positive residual integral gives a pointwise sink

The residual domain has volume bounded by `|B_{R_kappa}|`.

Therefore if

\[
\int_{B_{R_\kappa}\setminus\mathcal C}G
\ge\frac12c_\kappa,
\]

there exists `y_*` with

\[
\boxed{
G(y_*)\ge
\frac{c_\kappa}{2|B_{R_\kappa}|}
=:g_*>0.
}
\]

Since

\[
G=-W\cdot\Delta W,
\]

and compact smoothness gives

\[
\|\Delta W\|_{L^\infty(B_{R_\kappa})}
\le M_2,
\]

we have

\[
g_*
\le |W(y_*)|M_2.
\]

Hence

\[
\boxed{
|W(y_*)|
\ge w_*:=g_*/M_2>0.
}
\]

Also compactness gives

\[
|W(y_*)|\le M_0.
\]

Since

\[
G=-\kappa|W|^2,
\]

we obtain

\[
\boxed{
\kappa(y_*)
\le
-\kappa_*:= -g_*/M_0^2<0.
}
\]

---

## 4. Uniform spatial thickening

The function

\[
G=-W\cdot\Delta W
\]

has a uniform gradient bound on the compact smooth core:

\[
\|\nabla G\|_\infty
\le
\|\nabla W\|_\infty\|\Delta W\|_\infty
+
\|W\|_\infty\|\nabla\Delta W\|_\infty
\le M_G.
\]

Choose

\[
r_G:=g_*/(4M_G).
\]

Then on `B_{r_G}(y_*)`,

\[
G\ge g_*/2.
\]

After possibly shrinking by a fixed factor using the `C1` bound on `W`,

\[
\boxed{|W|\ge w_*/2}
\]

and the vorticity direction stays inside one fixed angular cone.

Because `|W|` is bounded above, the same ball also has

\[
\boxed{\kappa\le-\kappa_{**}<0}
\]

for a fixed `kappa_{**}`.

---

## 5. Fixed directed flux extraction

Let

\[
e_*:=W(y_*)/|W(y_*)|.
\]

On a sufficiently small fixed disk `D_*` normal to `e_*` inside the thickened ball, direction coherence gives

\[
W\cdot e_*\ge c_w w_*>0.
\]

Therefore

\[
\boxed{
\Phi_{sink}
:=
\int_{D_*}W\cdot e_*\,dA
\ge\phi_{sink}>0.
}
\]

Thus a fixed residual negative-kappa share produces a coherent scale-critical flux packet with

\[
\boxed{
|W|\ge c>0,
\qquad
\kappa\le-c<0,
\qquad
|\Phi_{sink}|\ge c>0.
}
\]

---

## 6. Genealogical status

Trace the material ancestry/descendancy of `D_*` through the already audited flux-genealogy framework.

A recurrent sink packet must either

1. be absorbed into an existing persistent material-flux lineage;
2. create/replace a fixed-flux label;
3. pay an already typed viscous-flux/projective/export exit.

On the compact CE-H branch, remote export is excluded by M5-604 and projective motion is absent on CE-H (`D_B xi=0`).

Therefore the genuine remaining mechanisms are persistent-lineage absorption or viscous fixed-flux replacement/change.

---

## 7. Consequence

The residual finite-core negative-kappa budget cannot remain an untracked diffuse reservoir.

It generates a genealogically trackable packet:

\[
\boxed{
\text{residual negative kappa budget}
\Longrightarrow
\text{coherent negative-kappa fixed-flux sink packet}.
}
\]

The next finite-memory audit must determine whether recurrent sink packets saturate into the same finite persistent lineage network or force positive-density viscous-flux replacement.

---

## 8. Firewall

This note does not yet prove that the eventual persistent lineage has negative **time-mean** flux-weighted `kappa`.

A material descendant may later pass through regions with positive `kappa`, compensating its negative sink episodes while preserving bounded recurrent flux.

Thus packet extraction is a measure-bridge step, not yet the final contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
