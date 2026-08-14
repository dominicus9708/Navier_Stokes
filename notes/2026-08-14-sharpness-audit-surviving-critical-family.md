# Sharpness audit: a surviving critical scaling family

Date: 2026-08-14

Status: **CURRENT SOURCE/ENERGY/RADIUS/DISSIPATION LEDGERS DO NOT YET CONTRADICT EVERY SURVIVING BOUNDED-AFFINE SCALING. AN ADDITIONAL STRUCTURAL THEOREM IS NECESSARY. GLOBAL REGULARITY NOT PROVED.**

## 1. Purpose

After closing homogeneous precursor inheritance, the strict-mesoscopic quadratic-core trace lane, and small-radius Kelvin localization, the remaining bounded-affine pulse is asymptotically nonlinear.

Before claiming closure, we must test whether the existing inequalities themselves already contradict every possible scaling. They do not.

## 2. Candidate family

Choose

\[
\Lambda=W^\beta,
\qquad
0<\beta<\frac{2}{15}-2\varepsilon,
\]

with also \(\beta<1/3\). Define

\[
\boxed{
m=W^{-1/3}\Lambda=W^{-1/3+\beta},
}
\]

and

\[
\boxed{
R=W^{1/6-\beta/2}.
}
\]

Then

\[
\Lambda\to\infty,
\qquad
m\to0.
\]

## 3. The family remains strictly mesoscopic

The lower mesoscopic threshold is

\[
R_* = W^{1/10+\varepsilon}.
\]

Our choice satisfies

\[
\frac16-\frac\beta2
>
\frac1{10}+\varepsilon
\]

precisely when

\[
\beta<\frac{2}{15}-2\varepsilon.
\]

Hence

\[
\boxed{
R\gg W^{1/10+\varepsilon}.
}
\]

## 4. Parabolic-time source action is critical

The natural parabolic block length is

\[
\Delta t\asymp R^2
=W^{1/3-\beta}.
\]

For an order-\(m\) stretching source,

\[
\boxed{
mR^2=1.}
\]

Thus a source of the maximal allowed pulse size can accumulate an order-one endpoint action over one natural parabolic block without violating any present pointwise source bound.

## 5. Finite-energy Hermite ridge is comfortably satisfied

The established low-curvature ridge is

\[
BR^5\lesssim W^{1/2}.
\]

At \(B\sim m\),

\[
\frac{mR^5}{W^{1/2}}
=
W^{-1/3+\beta}
W^{5/6-(5/2)\beta}
W^{-1/2}
=
W^{-3\beta/2}.
\]

Therefore

\[
\boxed{
\frac{mR^5}{W^{1/2}}
=
\Lambda^{-3/2}
\to0.
}
\]

So the candidate lies well inside, not merely on, the finite-energy Hermite ridge.

## 6. Per-step physical dissipation can vanish

If \(B\sim m\) during one parabolic block of length \(R^2\), the Gaussian-volume lower-bound scaling gives normalized gradient-energy cost of order

\[
R^3mR^2=mR^5.
\]

Returning to physical variables introduces the factor \(W^{-1/2}\). Hence

\[
D_{\rm phys,step}
\sim
W^{-1/2}mR^5
=
\boxed{\Lambda^{-3/2}}.
\]

Thus the per-step dissipation tends to zero. Along a sufficiently rapidly growing sequence of first-hitting levels, these costs are not excluded from being summable by the current ledger.

## 7. Current survival conditions can all be met

Take, for example, a stretching/projective branch with

\[
\Theta\asymp1.
\]

Then

\[
\Lambda^{3/5}\Theta\to\infty,
\]

so the strengthened quadratic-core/projective survival condition is satisfied.

Likewise the universal typed condition

\[
\Lambda\Theta^{5/6}\to\infty
\]

is satisfied.

If the high-Hermite curvature share is negligible, this does not create a contradiction because the degree-one projective lane remains available. If instead curvature is present, the current high-Hermite stretching condition only requires

\[
\Lambda^{3/5}\delta\to\infty
\]

on the portion where that lane carries the fixed action; suitable non-vanishing \(\delta\) also passes this condition.

## 8. Homogeneous precursor inheritance remains negligible

The full-affine BMO smoothing theorem gives

\[
B_{\rm inh}(R)\lesssim_KR^2q^{-3},
\qquad
q=W^{1/3+2\varepsilon}.
\]

For the present \(R\),

\[
B_{\rm inh}
\lesssim_K
W^{1/3-\beta}W^{-1-6\varepsilon}
=
W^{-2/3-\beta-6\varepsilon}.
\]

Dividing by

\[
m=W^{-1/3+\beta},
\]

gives

\[
\boxed{
\frac{B_{\rm inh}}m
\lesssim_K
W^{-1/3-2\beta-6\varepsilon}
\to0.
}
\]

Thus this family is genuinely nonlinear; it does not reopen the precursor/Kelvin lane.

## 9. Interpretation

The critical relations

\[
\boxed{mR^2\asymp1}
\]

and

\[
\boxed{D_{\rm phys,step}\asymp\Lambda^{-3/2}}
\]

show why the existing estimates stop short of closure.

The current framework can prove that a surviving pulse must be newly generated and must pay a typed structural cost. But an order-\(m\) nonlinear stretching source acting coherently for its own parabolic lifetime \(R^2\sim m^{-1}\) remains compatible with all existing scalar ledgers.

Therefore no further algebraic recombination of only the already-established inequalities can by itself complete the regularity proof.

## 10. Exact missing structural input

At least one genuinely new theorem is required. Natural options are:

1. **projective stretching cancellation/packing:** show that the degree-one projective source cannot remain coherent for a full \(R^2\sim m^{-1}\) lifetime on infinitely many disjoint first-hitting steps;
2. **adjoint-kernel tightness/mixing control:** show that the exact advection--diffusion kernel cannot deform so as to repeatedly sustain the required stretching action without an additional finite spacetime cost;
3. **critical velocity gain:** improve the current ridge
   \[
   BR^5\lesssim W^{1/2}
   \]
   to a scale-critical estimate comparable to
   \[
   BR^4\lesssim C,
   \]
   which would feed the ancient \(L^3\) rigidity gate;
4. **a simultaneous-saturation rigidity theorem** excluding a state that simultaneously realizes \(mR^2\asymp1\), projective source efficiency, bounded affine strain, finite energy, and finite dissipation.

## 11. Audit conclusion

The current frontier has been substantially narrowed, but it is not algebraically closed.

\[
\boxed{
\text{surviving critical family: }
 m=W^{-1/3+\beta},
\quad
R=W^{1/6-\beta/2},
\quad
0<\beta<2/15-2\varepsilon.
}
\]

This family passes the present mesoscopic, energy, source, precursor, and per-step dissipation tests.

Status: **A NEW STRUCTURAL ESTIMATE, NOT A REARRANGEMENT OF THE CURRENT LEDGERS, IS NECESSARY / GLOBAL REGULARITY NOT PROVED.**
