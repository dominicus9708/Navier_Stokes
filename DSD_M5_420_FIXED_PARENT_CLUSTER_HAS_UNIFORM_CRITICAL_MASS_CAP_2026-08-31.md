# DSD M5-420 — Every fixed parent-natural cluster has a uniform critical-mass cap

Date: 2026-08-31

Status: **THE FIRST-HITTING VORTICITY CAP IMPLIES THAT VORTICITY INSIDE ANY FIXED MULTIPLE OF THE PARENT NATURAL BALL HAS UNIFORMLY BOUNDED `dot H^{-1/2}` NORM, EQUIVALENTLY UNIFORMLY BOUNDED LOCAL CRITICAL `dot H^{1/2}` VELOCITY CONTENT AFTER SOLENOIDAL LOCALIZATION / THEREFORE THE M5-419 CRITICAL-MASS-ACCUMULATION BRANCH CANNOT BE REALIZED BY ONE OR FINITELY MANY FIXED-SIZE PARENT-NATURAL CLUSTERS BECOMING ARBITRARILY STRONG / CRITICAL MASS DIVERGENCE MUST ESCAPE TO GROWING NORMALIZED WINDOWS, REMOTE/RELATIVE SCALES, OR INCREASING PHASE-SPACE MULTIPLICITY / THIS REDUCES `C_mass accum` TO DELOCALIZATION/MULTIPLICITY RATHER THAN A SINGLE COMPACT AMPLIFIER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-419 splits the late critical-throughput problem into

\[
C_{mass\,accum}
\lor
C_{bal}
\]

outside already-typed strong strain/interface exits.

One apparent interpretation of `C_mass accum` would be that the same compact natural cluster simply accumulates arbitrarily large critical norm.

The first-hitting amplitude cap rules out that interpretation.

---

## 2. Parent natural scale and amplitude cap

At stage `j`, let

\[
W_j=\|\omega(t_j)\|_\infty
\]

and

\[
\boxed{
r_j^2=\frac{\nu}{W_j}.
}
\]

Throughout the stage before the next first hitting,

\[
\boxed{
\|\omega(t)\|_\infty
\le qW_j.
}
\]

Fix once and for all a normalized radius `C>1` and a smooth cutoff

\[
\chi_j(x)
=
\chi\left(\frac{x-X_j}{Cr_j}\right)
\]

supported in a fixed multiple of `B_{Cr_j}(X_j)`.

---

## 3. Dual Sobolev embedding

The critical Sobolev embedding

\[
\dot H^{1/2}(\mathbb R^3)
\hookrightarrow
L^3(\mathbb R^3)
\]

has the dual form

\[
\boxed{
L^{3/2}(\mathbb R^3)
\hookrightarrow
\dot H^{-1/2}(\mathbb R^3).
}
\]

Therefore

\[
\boxed{
\|\chi_j\omega(t)\|_{\dot H^{-1/2}}
\lesssim
\|\chi_j\omega(t)\|_{L^{3/2}}.
}
\]

---

## 4. Fixed natural ball has order-one critical vorticity norm

The support volume is

\[
|\operatorname{supp}\chi_j|
\lesssim
C^3r_j^3.
\]

Hence

\[
\begin{aligned}
\|\chi_j\omega\|_{L^{3/2}}
&\le
\|\omega\|_\infty
|\operatorname{supp}\chi_j|^{2/3}\\
&\lesssim
qW_j\,(Cr_j)^2.
\end{aligned}
\]

Using `W_jr_j^2=nu`,

\[
\boxed{
\|\chi_j\omega(t)\|_{L^{3/2}}
\lesssim
C^2q\nu.
}
\]

Therefore

\[
\boxed{
\|\chi_j\omega(t)\|_{\dot H^{-1/2}}
\le
C_{crit}(C,q)\nu
}
\]

uniformly in the late stage index.

Squaring,

\[
\boxed{
\|\chi_j\omega(t)\|_{\dot H^{-1/2}}^2
\le
C_{crit}(C,q)^2\nu^2.
}
\]

This is exactly scale invariant.

---

## 5. Velocity interpretation

For a global divergence-free field,

\[
\|u\|_{\dot H^{1/2}}
\asymp
\|\omega\|_{\dot H^{-1/2}}.
\]

A literal multiplication `chi_j u` is not divergence free, so the clean local velocity statement uses the standard solenoidal cutoff/Bogovskii correction.

Up to that fixed localization operator,

\[
\boxed{
\text{critical velocity content of one fixed parent-natural cluster}
\lesssim
C\nu^2.
}
\]

The vorticity statement above is the primary estimate and avoids hiding a divergence correction.

---

## 6. Consequence for global critical norm growth

Let

\[
X(t)=\|u(t)\|_{\dot H^{1/2}}^2
\asymp
\|\omega(t)\|_{\dot H^{-1/2}}^2.
\]

Write

\[
\omega
=
\chi_j\omega
+
(1-\chi_j)\omega.
\]

By the triangle inequality,

\[
\|\omega\|_{\dot H^{-1/2}}
\le
C_{crit}(C,q)\nu
+
\|(1-\chi_j)\omega\|_{\dot H^{-1/2}}.
\]

Therefore if

\[
X(t_j)\to\infty,
\]

then for every fixed normalized radius `C`,

\[
\boxed{
\|(1-\chi_j)\omega(t_j)\|_{\dot H^{-1/2}}
\to\infty
}
\]

along the corresponding divergent subsequence.

Thus critical-mass divergence cannot remain inside any fixed multiple of the parent natural core.

---

## 7. Finite number of compact natural clusters is also insufficient

The same estimate applies to each of finitely many parent-natural balls with uniformly bounded radii and bounded overlap.

For any fixed `N`, the sum of `N` localized pieces has

\[
\boxed{
\left\|
\sum_{m=1}^N\chi_{j,m}\omega
\right\|_{\dot H^{-1/2}}
\lesssim
C(N,C,q)\nu.
}
\]

Hence a fixed finite collection of compact natural clusters cannot carry unbounded global critical mass either.

The accumulation branch must increase at least one of:

1. the number of relevant phase-space clusters;
2. the normalized spatial radius needed to contain them;
3. the range of relative internal scales/frequencies;
4. a diffuse critical background not captured by finitely many formed clusters.

---

## 8. Relation to M5-408 and M5-416

M5-408 gives a Bessel lower bound when many formed critical carriers are phase-space separated:

\[
N\nu^2
\lesssim
X.
\]

The present note gives the complementary upper statement:

\[
\boxed{
\text{one fixed parent-natural cluster}
\lesssim
C\nu^2.
}
\]

Thus if `X` grows, it cannot be explained by an ever-stronger single bounded cluster under the first-hitting cap.

M5-416 further says that sources far outside the natural phase-space window are inefficient at stretching the current target.

Therefore accumulated remote critical mass is not an efficient replacement for the local M5-394 companion; it is additional throughput content that must itself be formed, transported, or later selected as a new target.

---

## 9. Updated mass-accumulation branch

The M5-419 branch

\[
C_{mass\,accum}
\]

can now be sharpened to

\[
\boxed{
C_{mass\,accum}
\Longrightarrow
C_{multiplicity}
\lor
C_{growing\ window}
\lor
C_{relative\ scale}
\lor
C_{diffuse}.
}
\]

A single compact natural critical element with fixed first-hitting amplitude cannot carry the divergent mass by itself.

This is a structural reduction, not an exclusion of the four remaining delocalized forms.

---

## 10. Important firewall

The estimate does not say that the global critical norm is bounded.

The complement `(1-chi_j)omega` may contain large remote or multiscale critical mass even though the physical kinetic energy is finite.

Nor does the result imply that all remote mass decomposes into fixed-flux carriers. A diffuse shell/frequency distribution remains possible and is explicitly retained.

Finally, the estimate is at one fixed normalized radius `C`; allowing `C=C_j->infinity` is exactly the growing-window problem and cannot be hidden inside the local bound.

---

## 11. Consequence for the critical-element strategy

A prospective minimal/recurrent object should not be sought as an arbitrarily high-amplitude compact parent packet: first-hitting normalization and the critical local cap prevent that.

The genuine compact critical-element candidate is instead the **near-balanced natural main/companion cluster of M5-419**, while critical-norm divergence must live in an exterior/delocalized component.

Thus a future rigidity theorem may try to decouple:

\[
\boxed{
\text{compact near-balanced active element}
+
\text{inefficient delocalized critical reservoir}.
}
\]

If the exterior reservoir can be shown not to feed the compact element efficiently (M5-416) without repeated new source formation, the near-balanced branch becomes substantially more rigid.

---

## 12. Audit verdict

### DERIVED

For every fixed parent-normalized radius,

\[
\boxed{
\|\chi_{Cr_j}\omega\|_{\dot H^{-1/2}}
\lesssim
C(C,q)\nu.
}
\]

Therefore critical-norm divergence forces exterior/delocalized mass.

### REMOVED INTERPRETATION

`C_mass accum` cannot mean one/finitely many fixed parent-natural clusters simply becoming arbitrarily large in critical norm.

### REMAINING

- increasing phase-space multiplicity;
- growing normalized windows;
- relative-scale spread;
- diffuse critical mass;
- near-balanced compact critical element;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
