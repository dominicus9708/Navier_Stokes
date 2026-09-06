# DSD Deep Audit — Scale-K / Restricted-Carleson VACM: Eigen-Gap Uniformity Gate

Date: 2026-09-06
Target family: Scale-invariant resonant budgets, variable-axis conic analysis, Axis Carleson / Restricted-Carleson VACM (2025).
Status: **EARLY UNCONDITIONAL VERSION SUPERSEDED; LATEST H1 DISCHARGE OPEN_DEEP**

## 1. Version-aware status

The program has a useful self-correction history:

- an early record claimed unconditional global regularity;
- a later September 2025 record explicitly stated that H2-H4 were proved while H1, the Axis Carleson theorem, remained the single analytic barrier;
- later Restricted-Carleson/VACM work claims to discharge the active-scale H1 problem using a mollified strain axis, eigen-gap sublevel estimates, and a stop-time ledger.

Thus the earlier unconditional wording is superseded by the later explicit H1 obligation. The H2-H4 harmonic-analysis modules should be preserved conditionally if their proofs check.

## 2. Exact eigenprojector sensitivity

Let `S(x,t)` be the symmetric strain matrix after the paper's declared smoothing. Suppose its top eigenvalue is simple:

\[
\lambda_1>\lambda_2.
\]

Let `P_1` be the orthogonal projector onto the top eigenspace. Standard perturbation theory gives schematically

\[
\boxed{
|\nabla P_1|
\lesssim
\frac{|\nabla S|}{\lambda_1-\lambda_2}
}
\]

(and analogous time-derivative formulas).

Therefore a moving-axis conic multiplier cannot be uniformly smooth through eigenvalue degeneracy for free. Every commutator estimate must pay either the inverse gap or exclude/price the small-gap set.

## 3. Heat smoothing does not by itself supply a universal eigen-gap sublevel theorem

Heat mollification makes `S_r` smooth/analytic at the chosen scale. But analyticity alone does not imply a solution-independent estimate of the form

\[
|\{x:0<\lambda_1-\lambda_2<\delta\}|
\le C\delta^\alpha
\]

with universal `C,alpha`.

Even analytic matrix fields may have arbitrarily high-order eigenvalue contact. A toy family

\[
S_m(x)=\operatorname{diag}(x^{2m},0,-x^{2m})
\]

is analytic and has an eigen-gap vanishing to order `2m` at the origin. Quantitative Lojasiewicz/sublevel exponents and constants generally require nondegeneracy/complexity information beyond mere analyticity.

This does not refute a specialized NSE theorem. It identifies exactly what the proof must derive from NSE-native quantities.

## 4. Required H1 discharge ledger

A valid Restricted-Carleson proof must show a uniform alternative on every active tent:

\[
\boxed{
\text{large gap: moving-axis commutator controlled}
\quad\lor\quad
\text{small gap: the bad set pays a summable physical/Carleson cost.}
}
\]

The constants must be uniform over:

- all active dyadic scales;
- all admissible solutions;
- the smoothing scale chosen relative to the packet scale;
- eigen-gap degeneracy order.

If the proof uses a sublevel inequality, its exponent/constants must be traced back to bounds already available from the NSE rather than assumed regularity of the spectral frame.

## 5. Spectral leakage audit

The latest public description says high-low and high-high interactions are treated. This is important because a valid proof cannot use a fixed-width shell closure.

M17 regression requirement remains:

\[
\boxed{
P_jB(u,u)
\text{ receives low-high contributions from arbitrarily lower modes and high-high near-cancellation contributions.}
}
\]

Any VACM ledger must retain these interactions or prove a genuine symbol/orthogonality theorem that absorbs them.

## 6. Endpoint audit

An earlier directional-ledger version publicly described a finite spacetime integral of `||omega||_{L^1_x}` and then a regularity conclusion. `L^1_x` vorticity alone is not the BKM endpoint.

The later eigen-gap version advertises a separate endpoint inequality mapping the directional ledger to maximum vorticity. That later bridge must be judged independently; it is not automatically refuted by the earlier formulation.

## 7. DSD verdict

Current precise status:

\[
\boxed{
\begin{aligned}
&\text{early unconditional claim: SUPERSEDED},\\
&\text{H2-H4: CONDITIONAL/SURVIVOR pending proof audit},\\
&\text{latest Restricted-Carleson H1 discharge: OPEN_DEEP}.
\end{aligned}}
}
\]

Decisive remaining theorem:

\[
\boxed{
\text{uniform NSE-native control of the small eigen-gap set and its moving-axis commutator cost.}
}
\]

New regression test:

\[
\boxed{
R24:\ \text{analytic smoothing does not create universal eigen-gap transversality; inverse-gap costs must be explicitly paid.}
}
\]

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
