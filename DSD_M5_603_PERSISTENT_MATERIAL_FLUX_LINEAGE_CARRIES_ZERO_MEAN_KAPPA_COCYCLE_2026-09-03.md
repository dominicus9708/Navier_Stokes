# DSD M5-603 — Persistent material-flux lineage carries an exact zero-mean kappa cocycle

Date: 2026-09-03

Status: **CE-H SIGNED-COCYCLE LIFT / M5-488 ALREADY DEFINES A PERSISTENT LINEAGE THROUGH A FIXED MATERIAL SURFACE PATCH, SO M5-602 DOES NOT NEED THE STRONGER UNPROVED IDENTIFICATION OF A LINEAGE WITH ONE INFINITESIMAL VORTEX-TUBE ELEMENT / ON THE GLOBAL CE-H BRANCH `Delta W = kappa W`, THE EXACT M5-489 MATERIAL-FLUX LAW BECOMES `Phi' = int_S kappa W·n`, HENCE `d log|Phi|/dtheta = kappa_bar_Phi`, THE INSTANTANEOUS FLUX-WEIGHTED MEAN OF KAPPA / A PERSISTENT FIXED-FLUX LINEAGE HAS FLUX BOUNDED ABOVE AND AWAY FROM ZERO, SO ITS RECURRENT TIME AVERAGE SATISFIES `mean(kappa_bar_Phi)=0` / THIS IS A SCALE-INVARIANT SIGNED COCYCLE ON THE ACTUAL AUDITED LINEAGE OBJECT / THE REMAINING GAP IS TO COMPARE THIS FLUX-WEIGHTED ZERO MEAN WITH THE GLOBAL ENSTROPHY-WEIGHTED NEGATIVE IDENTITY `int kappa |W|^2 = -P < 0` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why an infinitesimal-tube identification is unnecessary

M5-602 derived, for an infinitesimal CE-H vortex tube,

\[
D_B\log |\phi|=\kappa.
\]

A potential firewall remained: M5-518 had already shown that a persistent coherent lineage need not preserve one distinguished active marker or one distinguished infinitesimal tube element.

However, M5-488 gives a weaker but already audited material object that is sufficient here.

For a persistent material-flux lineage, select the same transported material surface patch

\[
S(\theta)
\]

through the lineage, and define its signed similarity vorticity flux

\[
\boxed{
\Phi(\theta)
:=
\int_{S(\theta)}W\cdot n\,dA.
}
\]

The lineage construction retains a fixed directed flux threshold and a compact upper bound, so on the persistent fixed-sign branch

\[
\boxed{
0<\Phi_-\le |\Phi(\theta)|\le \Phi_+<\infty.
}
\]

Thus no identification with a single material marker is needed.

---

## 2. Exact similarity material-flux law

M5-489 gives

\[
\boxed{
\frac{d}{d\theta}\Phi(\theta)
=
\int_{S(\theta)}\Delta W\cdot n\,dA.
}
\]

The similarity stretching and material-area deformation cancel exactly.

On the CE-H branch, M5-599--600 give globally

\[
\boxed{
\Delta W=\kappa W.
}
\]

Therefore

\[
\boxed{
\Phi'(\theta)
=
\int_{S(\theta)}\kappa\,W\cdot n\,dA.
}
\]

---

## 3. Flux-weighted kappa observable

Whenever `Phi != 0`, define

\[
\boxed{
\bar\kappa_\Phi(\theta)
:=
\frac{
\int_{S(\theta)}\kappa\,W\cdot n\,dA
}{
\int_{S(\theta)}W\cdot n\,dA
}.
}
\]

Then the exact flux law becomes

\[
\boxed{
\frac{d}{d\theta}\log|\Phi(\theta)|
=
\bar\kappa_\Phi(\theta).
}
\]

This is the finite-material-surface analogue of M5-602's infinitesimal tube law.

No sign is assigned to `kappa` pointwise.

---

## 4. Recurrent zero-mean cocycle

Integrating from `theta_0` to `theta_T`,

\[
\int_{\theta_0}^{\theta_T}\bar\kappa_\Phi(\theta)\,d\theta
=
\log\frac{|\Phi(\theta_T)|}{|\Phi(\theta_0)|}.
\]

Using

\[
\Phi_-\le |\Phi|\le\Phi_+,
\]

the right side is uniformly bounded independently of `T`.

Hence along every recurrent/Cesaro average on the persistent lineage,

\[
\boxed{
\langle\bar\kappa_\Phi\rangle=0.
}
\]

This is a true bounded-coboundary identity on the material-flux lineage itself.

---

## 5. Scale invariance

Similarity vorticity flux is invariant under Navier--Stokes parabolic scaling.

Therefore `log|Phi|` is a bounded scale-invariant state observable on the fixed-flux lineage and

\[
\bar\kappa_\Phi
\]

is its signed similarity-time drift.

This is qualitatively different from the positive dimensionless charges audited in M5-598 whose physical energy cost shrinks geometrically with scale.

---

## 6. Compare with the global CE-H sign identity

M5-600 gives

\[
\boxed{
\int_{\mathbb R^3}\kappa|W|^2dy
=
\int W\cdot\Delta W\,dy
=
-P<0
}
\]

for every nonzero state.

Thus the same scalar field `kappa` has

\[
\boxed{
\text{persistent material-flux average: }
\langle\bar\kappa_\Phi\rangle=0,
}
\]

but

\[
\boxed{
\text{global enstrophy-weighted spatial average: }
\int\kappa|W|^2=-P<0.
}
\]

These are different measures and therefore are not yet contradictory.

---

## 7. Exact remaining gap

To close CE-H one needs a bridge showing that the negative enstrophy-weighted `kappa` mass cannot live permanently outside the finite persistent material-flux network that carries the recurrent production.

The desired statement is schematically

\[
\boxed{
\int \kappa|W|^2<0
\quad\text{and finite persistent production network}
\Longrightarrow
\text{some persistent lineage has }
\langle\bar\kappa_\Phi\rangle<0,
}
\]

which would contradict the exact cocycle above.

This implication is **not yet proved**.

The next audit should therefore decompose the global negative measure

\[
-\kappa|W|^2
\]

into

1. persistent-lineage carrier neighborhoods;
2. residual finite-core vorticity;
3. spectator/remote tail,

and test whether the latter two can carry the entire negative `kappa` budget without becoming new persistent/replacement lineages or typed exits.

---

## 8. DSD audit firewall

This note does **not** claim

\[
\bar\kappa_\Phi
=
\frac{\int \kappa|W|^2}{\int|W|^2}.
\]

Flux weighting and enstrophy weighting are different.

It also does not require one material marker or one infinitesimal tube element to survive forever.

The exact object is the already audited material surface patch of the persistent material-flux lineage.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
