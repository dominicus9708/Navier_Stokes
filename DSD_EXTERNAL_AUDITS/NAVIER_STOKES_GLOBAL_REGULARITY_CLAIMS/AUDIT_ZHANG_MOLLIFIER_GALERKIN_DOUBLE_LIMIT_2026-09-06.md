# DSD Audit — Zhang Weak-Regularity / Mollifier–Galerkin Double-Limit Framework

Date: 2026-09-06
Source: JiaHong Zhang, *Global Smooth Solutions to the 3D Incompressible Navier-Stokes Equations: Weakly Regular Framework and Multi-Scenario Adaptation*, Preprints 202601.0992.v1, Jan 2026.
Audit status: **HIGH-ORDER UNIFORMITY GATE OPEN / WEAK-COMPACTNESS DOES NOT IMPLY GLOBAL SMOOTHNESS**

## 1. Public claim

The abstract claims global smoothness and uniqueness for initial data ranging from high Sobolev regularity down to merely `L^2` and locally weakly singular data, using:

- compactly supported mollifier regularization;
- “uniform double-limit energy estimates”;
- Galerkin iteration;
- instantaneous smoothing for `t>0`.

## 2. What standard approximation theory already gives

For regularized or Galerkin systems, fixed approximation parameters yield smooth finite-dimensional/regularized solutions.

The classical Leray program provides approximation-uniform energy bounds such as

\[
\sup_{t\le T}\|u_n(t)\|_2^2
+
2\nu\int_0^T\|\nabla u_n\|_2^2dt
\le \|u_0\|_2^2+\cdots.
\]

Aubin–Lions/weak compactness then yields a global Leray–Hopf weak solution.

This part is not the open problem.

## 3. Missing upgrade obligation

To conclude

\[
u\in C^\infty((0,\infty);H^\infty)
\]

for arbitrary large 3D data, one needs approximation-independent estimates in norms strong enough to prevent concentration.

For example one would need, on every `[\tau,T]` with `\tau>0`, a hierarchy such as

\[
\sup_n\sup_{t\in[\tau,T]}\|u_n(t)\|_{H^m}\le C_{m,\tau,T}
\]

for all `m`, with constants independent of both Galerkin dimension and mollifier scale.

If the constants behave like

\[
C_{m,\tau,T}(\varepsilon)\to\infty
\quad\text{as }\varepsilon\to0,
\]

the smoothness disappears in the double limit.

## 4. Instantaneous smoothing audit

The Stokes/heat semigroup smooths linear equations instantly. For the nonlinear 3D NSE, mild solutions are smooth for a short time while the strong solution exists. Linear heat smoothing does **not** by itself prevent later nonlinear blow-up.

Thus the implication

\[
\text{mollified initial singularity disappears for }t>0
\Rightarrow
\text{solution remains smooth for all later time}
\]

requires a global nonlinear a priori bound.

## 5. Double-limit order audit

Two approximation parameters may be involved, e.g. mollification `ε` and Galerkin dimension `N`. Statements of the form

\[
\lim_{\varepsilon\to0}\lim_{N\to\infty}u_{N,\varepsilon}
\]

and

\[
\lim_{N\to\infty}\lim_{\varepsilon\to0}u_{N,\varepsilon}
\]

need not have the same strong regularity. A “uniform double limit” must specify:

- the norm;
- the constants;
- the order or joint convergence;
- nonlinear-term convergence;
- preservation of the high-order estimate.

Energy-level uniformity alone is insufficient.

## 6. Uniqueness audit

Global uniqueness is known in a strong class but not for arbitrary Leray weak solutions. Therefore a uniqueness conclusion after the limit cannot be obtained merely because every approximate Galerkin system is unique.

\[
\forall n:\text{ unique approximate solution}
\not\Rightarrow
\text{unique weak limit}.
\]

One must first prove the limit lies in a strong/weak–strong uniqueness class.

## 7. Current verdict

The public abstract does not expose the detailed higher-order estimates needed to decide whether the paper actually proves the required parameter-uniform bounds. Therefore the fair classification is not an immediate falsehood verdict but:

\[
\boxed{
\text{OPEN DEEP AUDIT — uniform higher-Sobolev double-limit closure is the decisive gate.}
}
\]

If only standard energy estimates are uniform, the argument reaches global weak existence rather than global smoothness.

Global regularity remains unproved.
