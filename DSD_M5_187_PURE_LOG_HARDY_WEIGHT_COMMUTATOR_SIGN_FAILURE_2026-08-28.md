# DSD M5-187 — Pure Log-Hardy Weight Commutator Sign Failure

Date: 2026-08-28

Status: **W1-CONDITIONAL / THE SCALE-COVARIANT WEIGHT `Phi=-log rho` MATCHES THE TYPE-I DIFFERENTIAL ORDERS BUT ITS STANDARD SYMMETRIC–SKEW CARLEMAN COMMUTATOR IS NOT POSITIVE: THE SPATIAL HESSIAN HAS TWO STRICTLY NEGATIVE TANGENTIAL DIRECTIONS AND A NEGATIVE RADIAL REGION INSIDE THE PARABOLIC CORE / PURE LOG-HARDY WEIGHT IS THEREFORE REJECTED AS A DIRECT STANDARD CARLEMAN CLOSURE / A PERTURBED HARDY WEIGHT OR A DIFFERENT BACKWARD-STOKES CARLEMAN STRUCTURE IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Starting conjugated operator

Use M5-186:

\[
P_s
=\partial_t-\nu\Delta
+2\nu s\nabla\Phi\cdot\nabla
+V_s,
\]

with

\[
\Phi=-\log\rho,
\qquad
\rho^2=r^2+\vartheta,
\qquad
\vartheta=T_*-t.
\]

Define

\[
W:=-s\Phi_t-\nu s^2|\nabla\Phi|^2.
\]

Then split

\[
\boxed{
S_s:=-\nu\Delta+W
}
\]

and

\[
\boxed{
A_s:=\partial_t
+2\nu s\nabla\Phi\cdot\nabla
+\nu s\Delta\Phi.
}
\]

For compactly supported spacetime test fields, `S_s` is symmetric and `A_s` is skew-adjoint up to the audited terminal/lateral boundary terms.

Thus

\[
\|P_sv\|^2
=\|S_sv\|^2+\|A_sv\|^2
+2\operatorname{Re}\langle S_sv,A_sv\rangle.
\]

---

## 2. Exact commutator structure

The standard integration-by-parts calculation gives

\[
\boxed{
\begin{aligned}
2\operatorname{Re}\langle S_sv,A_sv\rangle
={}&4\nu^2s\int \nabla^2\Phi(\nabla v,\nabla v)\\
&-\nu^2s\int (\Delta^2\Phi)|v|^2\\
&-\int\left(W_t+2\nu s\nabla\Phi\cdot\nabla W\right)|v|^2,
\end{aligned}}
\]

ignoring only explicitly separated support-boundary terms.

This is the sign object that M5-186 left open.

---

## 3. Hessian of the pure log weight

For

\[
\Phi=-\frac12\log(r^2+\vartheta),
\]

we have

\[
\boxed{
\nabla^2\Phi
=-\frac{I}{\rho^2}
+2\frac{y\otimes y}{\rho^4}.
}
\]

Hence on tangential directions to the sphere,

\[
\boxed{\lambda_T=-\rho^{-2}}
\]

with multiplicity two.

On the radial direction,

\[
\boxed{
\lambda_R
=\frac{r^2-\vartheta}{\rho^4}.
}
\]

Therefore

\[
\boxed{
\nabla^2\Phi(\nabla v,\nabla v)
=-\rho^{-2}|\nabla_Tv|^2
+\frac{r^2-\vartheta}{\rho^4}|\partial_rv|^2.
}
\]

The principal commutator gradient term contains

\[
\boxed{
-4\nu^2s\rho^{-2}|\nabla_Tv|^2
}
\]

everywhere and an additional negative radial contribution whenever

\[
r^2<\vartheta.
\]

Thus the standard commutator is not pseudoconvex in the required critical gradient channel.

---

## 4. Biharmonic weight term

A direct radial calculation gives

\[
\boxed{
\Delta\Phi
=-\frac{r^2+3\vartheta}{(r^2+\vartheta)^2}
}
\]

and

\[
\boxed{
\Delta^2\Phi
=-2\frac{r^4+10r^2\vartheta-15\vartheta^2}
{(r^2+\vartheta)^4}.
}
\]

Consequently the zeroth-order commutator contribution also changes sign across the parabolic core geometry.  It cannot repair the Hessian defect by a global pointwise sign argument.

---

## 5. The `W` transport term is likewise indefinite

With

\[
W
=-\frac{s}{2\rho^2}
-\nu s^2\frac{r^2}{\rho^4},
\]

the quantity

\[
W_t+2\nu s\nabla\Phi\cdot\nabla W
\]

contains an `s^3` contribution proportional to

\[
r^2(r^2-\vartheta)\rho^{-8},
\]

which changes sign at

\[
r^2=\vartheta.
\]

Thus the pure logarithmic weight has no hidden globally positive zeroth-order commutator capable of restoring the missing standard pseudoconvexity.

---

## 6. What is and is not rejected

### GREEN

M5-186 remains correct that `Phi=-log rho` matches the differential **orders** of the W1 Type-I coefficients:

\[
|a|\sim\rho^{-1},
\qquad
|B|\sim\rho^{-2}.
\]

### REJECTED / RED

The implication

\[
\boxed{
\text{order matching of }-\log\rho
\Rightarrow
\text{direct positive standard Carleman estimate}
}
\]

is false.

The pure weight cannot be used as the missing M5-185 Stokes-Carleman lemma without an additional mechanism.

---

## 7. Relation to known critical Hardy Carleman estimates

Known scalar inverse-square unique-continuation proofs do not rely on the unperturbed logarithmic weight alone.  They use refined/special Carleman weights and more delicate decompositions that overcome the limiting Hardy geometry.

Therefore the failure in Sections 3–5 is consistent with, rather than contradictory to, the existence of scalar critical Hardy unique continuation.

The Stokes target must likewise use either:

1. a perturbed critical Hardy weight;
2. a spherical/spectral decomposition adapted to the limiting logarithmic geometry;
3. a different backward weight of Escauriaza–Seregin–Sverak / Lei–Yang–Yuan type;
4. a direct generalized Stokes Carleman theorem whose pressure treatment is already built in.

---

## 8. DSD four-chain audit

### Formation — GREEN

All terms come from the exact conjugated heat operator.

### Axis — GREEN

Tangential, radial, and terminal-time channels are separated explicitly.

### Static aggregation — GREEN

Negative tangential terms are not hidden inside a positive radial average.

### Dynamics — RED for pure-log direct closure

The candidate weight fails the required standard pseudoconvex sign test.

### Cross-audit — GREEN

M5-185 remains a valid target theorem; only the specific naive weight candidate from M5-186 is pruned.

---

## 9. Updated next gate

Do **not** continue by forcing positivity from `Phi=-log rho`.

The next legitimate calculations are:

- audit a refined Hardy weight modeled on the critical inverse-square scalar Carleman constructions; or
- return to a pressure-compatible backward-Stokes Carleman weight with known positive pseudoconvexity and test whether the Type-I `rho^-1/rho^-2` coefficients can be absorbed.

All statements remain W1-conditional.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
