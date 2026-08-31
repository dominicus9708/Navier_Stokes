# DSD M5-371 — Similarity Gradient-H: Calderón–Zygmund Near/Middle/Far Source Decomposition

Date: 2026-08-31

Status: **THE EULER/SIMILARITY GRADIENT-TYPE-II ESCAPE IS RESOLVED INTO STANDARD VORTICITY SOURCE MECHANISMS / UNBOUNDED `||grad V||_infty` WITH FINITE ENERGY REQUIRES VORTICITY-AMPLITUDE ESCALATION, SMALL-SCALE Dini/DERIVATIVE ROUGHNESS, OR AN INCREASING MULTISCALE/REMOTE CZ RANGE / NO NEW INDEPENDENT H LEAF IS CREATED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-370 showed that the energy-bearing affine/atom escape left by the Euler endpoint theorem is exactly

\[
 H_{\nabla,\rm sim}:
 \qquad
 \sup_s\|\nabla V(s)\|_\infty=\infty.
\]

This note decomposes that gradient blow-up using the whole-space vorticity representation.

## 2. Strain from vorticity

For a divergence-free decaying whole-space field,

\[
 \nabla V
\]

is a Calderon--Zygmund singular integral of the vorticity

\[
 \Omega=\nabla\times V.
\]

For the symmetric strain one may write schematically

\[
 S[V](x)
 =\operatorname{p.v.}
 \int K(y)\Omega(x-y)\,dy,
\]

where

\[
 |K(y)|\lesssim |y|^{-3},
 \qquad
 \int_{S^2}K(r\theta)d\theta=0.
\]

The same analysis applies componentwise to the full gradient after adding the local antisymmetric vorticity part.

## 3. Near/middle/far split

Choose

\[
 0<\rho<R.
\]

Split

\[
 S=S_{<\rho}+S_{\rho,R}+S_{>R}.
\]

### Near field

By cancellation of the kernel,

\[
 S_{<\rho}(x)
 =
 \int_{|y|<\rho}
 K(y)[\Omega(x-y)-\Omega(x)]dy.
\]

Define the local modulus

\[
 \omega_\Omega(x,r)
 =\sup_{|h|\le r}|\Omega(x+h)-\Omega(x)|.
\]

Then

\[
 \boxed{
 |S_{<\rho}(x)|
 \lesssim
 \int_0^\rho
 \frac{\omega_\Omega(x,r)}{r}\,dr.
 }
\]

Thus near-field gradient escalation is a Dini/modulus-of-continuity failure of the vorticity.

## 4. Middle field

If

\[
 M_\Omega=\|\Omega\|_\infty,
\]

then

\[
 \boxed{
 |S_{\rho,R}(x)|
 \lesssim
 M_\Omega\log\frac{R}{\rho}.
 }
\]

This is the familiar critical logarithmic scale accumulation.

A bounded vorticity amplitude can therefore produce a large strain only by accumulating coherent contribution over a large number of logarithmic scales, unless the near/far terms are already large.

## 5. Far field from finite kinetic energy

The Euler endpoint has

\[
 V\in L^2(\mathbb R^3).
\]

For the far field, use

\[
 \Omega=\nabla\times V
\]

and integrate by parts with a smooth cutoff outside radius `R`. The derivative falls on the Calderon--Zygmund kernel/cutoff, producing a kernel of order `|y|^{-4}` plus a shell term of the same scaling.

Cauchy--Schwarz gives

\[
 \boxed{
 |S_{>R}(x)|
 \lesssim
 R^{-5/2}\|V\|_2
 }
\]

up to a universal cutoff constant.

Indeed

\[
 \int_{|y|>R}|y|^{-8}dy\asymp R^{-5}.
\]

Thus finite kinetic energy controls the genuinely far velocity contribution.

## 6. Master pointwise estimate

Combining the three pieces,

\[
 \boxed{
 |S(x)|
 \lesssim
 \int_0^\rho\frac{\omega_\Omega(x,r)}rdr
 +
 \|\Omega\|_\infty\log\frac{R}{\rho}
 +
 R^{-5/2}\|V\|_2.
 }
\]

This is a mechanism ledger, not an optimized global inequality.

## 7. Formation split for unbounded profile gradient

Suppose

\[
 \|\nabla V(s_j)\|_\infty\to\infty.
\]

At maximizing/near-maximizing points, the estimate implies at least one of the following.

### A. Vorticity-amplitude escalation

\[
 \boxed{
 \|\Omega(s_j)\|_\infty\to\infty.
 }
\]

This creates a smaller natural vorticity scale and returns to the high-frequency/re-point-picking `H_omega` branch.

### B. Near-field Dini/derivative roughness

For every useful fixed cutoff radius, the near integral becomes large:

\[
 \boxed{
 \int_0^\rho
 \frac{\omega_\Omega(x_j,r,s_j)}rdr
 \to\infty.
 }
\]

This is a small-scale derivative/fractional regularity failure:

\[
 \boxed{H_{\rm Dini}\lor H_{\rm high-der}.}
\]

It includes amplitude gradients and direction roughness.

### C. Multiscale critical accumulation

If vorticity amplitude and near Dini regularity remain controlled, the only way to make the middle term large is an increasing effective scale span

\[
 \boxed{
 \log(R_j/\rho_j)\to\infty.
 }
\]

This is a scale-distributed CZ strain source rather than a single local packet.

It is exactly the multiscale/critical-tail/remote-network structure already represented by the angular-source and weak-critical H/T ledgers.

### D. Far-energy failure

If the finite-energy far estimate cannot be used uniformly because the relevant center/window escapes or the decomposition loses the global `L2` ancestry, that loss is spatial/compactness turnover `T`.

## 8. Relation to the Biot--Savart angular ledger

M5-362 refined the productive longitudinal part of the strain to

\[
 \gamma(x)
 \sim
 \int
 \frac{|\Omega(x+y)|\sin\theta(x,x+y)}{|y|^3}dy.
\]

Thus the multiscale middle-field branch is not merely large scalar vorticity mass.

For the part of strain that actually amplifies first-hitting vorticity, it must contain a misaligned angular source on some scale.

Hence

\[
 \boxed{
 H_{\nabla,\rm sim}
 \subset
 H_{\omega,\infty}
 \lor
 H_{\rm Dini/dir}
 \lor
 H_{\rm angular,multiscale}
 \lor
 T_{\rm remote}.
 }
\]

## 9. No new terminal leaf

This is the main proof-tree consequence.

The Euler gradient-Type-II branch from M5-369--370 is not an independent fifth endpoint.

It decomposes back into the already familiar high-frequency, directional/projective, multiscale, or spatial-turnover mechanisms.

## 10. Firewall

The logarithmic middle-field bound does not itself contradict blow-up.

A singular solution may create an increasing number of active logarithmic scales.

Likewise Dini failure does not automatically imply an infinite `H2` budget without a capacity/occupancy bridge.

The result is exhaustive source localization, not closure.

## 11. Formation/axis interpretation

Formation analysis separates **where** the large gradient is generated:

- local amplitude;
- local roughness;
- multiscale accumulation;
- remote ancestry.

Axis-property analysis then refines the productive part by the relative direction factor `sin theta`.

This is separate from DSD auditing, which checks that no source mechanism was silently discarded.

## 12. Audit verdict

### DERIVED/STANDARD

- CZ near/middle/far split;
- Dini near-field control;
- logarithmic middle-field control by `||Omega||_infty`;
- finite-energy far-field decay after integration by parts.

### MASTER REDUCTION

\[
 \boxed{
 H_{\nabla,\rm sim}
 \Longrightarrow
 H_{\omega}
 \lor H_{\rm Dini/dir}
 \lor H_{\rm multiscale}
 \lor T_{\rm remote}.
 }
\]

### OPEN

- non-summable price for repeated multiscale/Dini events;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
