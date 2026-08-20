# Threshold Maximizer and First-Hitting KKT Contact Equation — 2026-08-20

Overall status: **COMPACTNESS/KKT REDUCTION — GLOBAL REGULARITY NOT PROVED.**

This note refines the variational threshold problem by separating two facts:

1. on a quantitative non-H/non-T class, the threshold supremum is attained after excluding translation, vanishing, and multicore splitting;
2. a positive maximizer necessarily saturates the first-hitting vorticity cap, so the exact Euler--Lagrange equation contains an additional KKT multiplier supported on the maximum-vorticity contact set.

---

## 1. Quantitative compact threshold class

Consider a sequence of strain fields `S_n in L^2_st cap H^2` satisfying the first-hitting cap

\[
\|\omega_n\|_\infty\le1,
\qquad
\omega_n=\mathcal B S_n,
\]

where

\[
\mathcal B S
=\nabla\times[-2\operatorname{div}(-\Delta)^{-1}S].
\]

Assume the quantitative non-H/non-T conditions:

- a fixed center, removing translation escape;
- uniform upper bounds on `E_n=||S_n||_2^2`, the second moment `M_n`, and `H_n=||Delta S_n||_2^2`;
- derivative-tail tightness, excluding escape of the H1/H2 packet to infinity;
- no splitting into two separated comparable threshold cells (classified as multicore turnover `T`).

If additionally

\[
\eta(S_n)=\frac{N(S_n)}{H(S_n)}\ge\nu>0,
\]

the mass--radius lemma gives a uniform positive lower bound on `E_n`. Thus vanishing is excluded.

---

## 2. Compactness of a maximizing sequence

Uniform `H^2` control gives weak compactness in `H^2` and strong local compactness in `H^1`. Tightness upgrades the latter to the global strong convergence needed for the cubic functional:

\[
S_n\to S_*\quad\text{strongly in }H^1
\]

along a subsequence, while

\[
S_n\rightharpoonup S_*\quad\text{weakly in }H^2.
\]

The strain constraint space is closed, hence

\[
S_*\in L^2_{st}.
\]

The strong `H^1` convergence together with the uniform `H^2` bound implies convergence of

\[
N(S_n)
=-\int
\left[
S_{k\ell}\partial_kS:\partial_\ell S
+2\operatorname{tr}(S(\partial_kS)^2)
\right].
\]

After taking a subsequence with `H(S_n)` convergent, weak lower semicontinuity gives

\[
H(S_*)\le\liminf H(S_n).
\]

For a positive maximizing sequence this can only improve the quotient. Hence the non-H/non-T compact class admits a nonzero maximizer `S_*` for the threshold quotient.

This statement is conditional on the quantitative derivative-tail tightness/no-splitting formulation of non-H/non-T. Its purpose is to identify precisely the remaining concentration-compactness obligation.

---

## 3. The first-hitting cap must be active

The quotient is homogeneous under pure amplitude scaling:

\[
N(cS)=c^3N(S),
\qquad
H(cS)=c^2H(S),
\]

so

\[
\eta(cS)=c\eta(S).
\]

The vorticity operator is linear:

\[
\|\mathcal B(cS)\|_\infty
=c\|\omega\|_\infty.
\]

Therefore any positive maximizer subject to

\[
\|\omega\|_\infty\le1
\]

must satisfy

\[
\boxed{\|\omega_*\|_\infty=1.}
\]

If the cap were strict, the field could be amplified slightly and the quotient would increase.

---

## 4. Smooth p-surrogate for the L-infinity constraint

To formulate the stationarity equation rigorously, replace the nonsmooth cap temporarily by

\[
G_p(S)=\frac1p\int|\omega|^pdx=\text{constant},
\qquad p<\infty.
\]

Then

\[
\delta G_p
=
\int |\omega|^{p-2}\omega\cdot \mathcal B(\delta S)dx
\]

and hence the functional derivative is

\[
\boxed{
\nabla G_p
=
\mathcal B^*(|\omega|^{p-2}\omega).
}
\]

On a fixed-energy/fixed-moment slice, a smooth p-maximizer therefore satisfies

\[
\boxed{
P_{st}\left[
\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta|x|^2S
\right]
=\mu_p\,\mathcal B^*(|\omega|^{p-2}\omega).
}
\]

Here `mathcal E_N` is the local first-variation operator derived in the previous variational note.

---

## 5. Formal p -> infinity KKT limit

As `p -> infinity`, the normalized measures

\[
|\omega|^{p-2}\omega\,dx
\]

concentrate on the contact set

\[
\mathcal M
=\{x:|\omega(x)|=1\}.
\]

The expected limiting KKT equation is therefore

\[
\boxed{
P_{st}\left[
\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta|x|^2S
\right]
=\mathcal B^*\boldsymbol\mu,
}
\]

where `boldsymbol mu` is a vector Radon measure supported on `mathcal M` and aligned with the active vorticity constraint in the usual KKT sense.

This limiting measure statement is a variational roadmap; a rigorous passage from finite p to infinity remains to be proved.

---

## 6. Equation away from the contact set

On every open set disjoint from `mathcal M`, the KKT source vanishes. Thus the maximizer solves the homogeneous constrained fourth-order equation

\[
\boxed{
P_{st}\left[
\mathcal E_N
-2\Lambda\Delta^2S
-2\alpha S
-2\beta|x|^2S
\right]=0
}
\]

away from the maximum-vorticity set.

Therefore all first-hitting nonsmoothness is localized to the contact set. The rest of the threshold core is governed by a smooth strain-compatible nonlinear eigenproblem.

---

## 7. Relation to the Pohozaev balance

For variations that preserve the active first-hitting constraint to first order, the amplitude/moment Pohozaev calculation from the smooth slice remains the natural candidate balance. However, because the `L^infinity` cap is active, one must include the KKT multiplier contribution in unrestricted amplitude variations.

Accordingly, the earlier identity

\[
\alpha E=\beta M=N/4
\]

should be regarded as exact on the smooth fixed-amplitude slice and as a guide for the full first-hitting problem, not yet as an unconditional identity for the KKT maximizer.

This distinction is essential.

---

## 8. Current reduced target

If the dangerous threshold value satisfies

\[
\Lambda_{\mathcal K}\ge\nu,
\]

then, modulo quantitative non-H/non-T compactness, there exists a nonzero first-hitting maximizer satisfying

\[
\|\omega_*\|_\infty=1
\]

and the KKT fourth-order strain equation above.

Thus the final local contradiction can be sought by combining:

1. the maximum-vorticity contact geometry;
2. the first-hitting pointwise stretching inequality;
3. the sharp trace-free H1 efficiency bound;
4. the strain compatibility projection;
5. the fourth-order KKT equation away from the contact set.

Status: **A DANGEROUS NON-H/NON-T THRESHOLD SEQUENCE CAN BE REDUCED TO A NONZERO COMPACT MAXIMIZER. ANY POSITIVE MAXIMIZER SATURATES THE VORTICITY L-INFINITY CAP, SO THE TRUE VARIATIONAL EQUATION IS A FOURTH-ORDER STRAIN-COMPATIBLE KKT SYSTEM WITH A MULTIPLIER SUPPORTED ON THE MAXIMUM-VORTICITY CONTACT SET. GLOBAL REGULARITY REMAINS UNPROVED.**