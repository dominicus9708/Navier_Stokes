# DSD Divergence-Free Directional Defect Floor

Date: 2026-08-25

Status: **NEW COMPACTNESS/RIGIDITY LEMMA / GLOBAL ONE-AXIS VORTICITY ALIGNMENT EXCLUDED ON A TIGHT H2-BOUNDED NONTRIVIAL CORRIDOR / EVENT-COST CONVERSION STILL OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

The permanent-export branch carries coherent directed vorticity flux populations. A possible escape picture would be that, at late recurrent times, essentially all dynamically relevant vorticity aligns with one export axis and is transported outward in a nearly one-directional critical conveyor.

For a divergence-free vorticity field with finite global enstrophy this limit is much more rigid than it first appears.

This note proves that global near-one-axis alignment is impossible if the enstrophy remains spatially tight and a global second-derivative bound is available at the selected times.

## 2. Setup

Let

\[
\Omega\in H^2(\mathbb R^3),
\qquad
\nabla\cdot\Omega=0.
\]

Fix a unit vector \(e\in S^2\) and decompose

\[
\boxed{
\Omega=\alpha e+\beta,
\qquad
\beta\cdot e=0.
}
\]

Then

\[
\boxed{
\partial_e\alpha
=-\nabla_\perp\cdot\beta.
}
\]

If \(\beta\equiv0\), then \(\partial_e\alpha=0\). A nonzero function independent of the \(e\)-coordinate cannot lie in \(L^2(\mathbb R^3)\). Hence an exactly one-directional divergence-free \(L^2\) vorticity field is necessarily zero.

The goal is a quantitative compactness version of this observation.

## 3. Cutoff-Poincare estimate

Rotate coordinates so that \(e=e_3\).

Let \(\chi_R\) satisfy

\[
\chi_R=1\text{ on }B_R,
\qquad
\operatorname{supp}\chi_R\subset B_{2R},
\qquad
|\nabla\chi_R|\le C_\chi R^{-1}.
\]

For each fixed transverse coordinate \(x_\perp\), the function

\[
x_3\mapsto \chi_R\alpha(x_\perp,x_3)
\]

has compact support in an interval of length \(O(R)\). The one-dimensional Dirichlet Poincare inequality gives

\[
\|\chi_R\alpha\|_2
\le
C_PR\|\partial_3(\chi_R\alpha)\|_2.
\]

Using

\[
\partial_3\alpha=-\nabla_\perp\cdot\beta,
\]

we obtain

\[
\partial_3(\chi_R\alpha)
=
-\chi_R\nabla_\perp\cdot\beta
+(\partial_3\chi_R)\alpha.
\]

Therefore

\[
\boxed{
\|\chi_R\alpha\|_2
\le
C R\|\nabla\beta\|_2
+C\|\Omega\|_{L^2(B_{2R}\setminus B_R)}.
}
\]

A harmless \(C\|\beta\|_2\) term may be retained if one rewrites the first term in divergence form with \(\chi_R\beta\); it does not change the argument below.

## 4. Interpolation turns small transverse enstrophy into small transverse derivative

Fourier interpolation gives

\[
\boxed{
\|\nabla\beta\|_2^2
\le
\|\beta\|_2\|\Delta\beta\|_2
\le
\|\beta\|_2\|\Delta\Omega\|_2.
}
\]

Hence, if

\[
\|\Delta\Omega\|_2\le H_2,
\]

then

\[
\|\nabla\beta\|_2
\le
H_2^{1/2}\|\beta\|_2^{1/2}.
\]

Substitution gives

\[
\boxed{
\|\Omega\cdot e\|_{L^2(B_R)}
\le
C R H_2^{1/2}
\|P_{e^\perp}\Omega\|_2^{1/2}
+C\|\Omega\|_{L^2(B_{2R}\setminus B_R)}.
}
\]

## 5. Qualitative directional-rigidity lemma

Consider a sequence \(\Omega_n\) satisfying

\[
\nabla\cdot\Omega_n=0,
\]

\[
0<m_0\le\|\Omega_n\|_2\le M_0,
\]

\[
\|\Delta\Omega_n\|_2\le H_0,
\]

and global enstrophy tightness:

\[
\forall\varepsilon>0\ \exists R<\infty:
\quad
\sup_n
\int_{|Y|>R}|\Omega_n|^2dY
<\varepsilon^2.
\]

Then

\[
\boxed{
\inf_n\inf_{e\in S^2}
\|P_{e^\perp}\Omega_n\|_2
>0.
}
\]

### Proof

Assume otherwise. Choose \(e_n\) with

\[
\|P_{e_n^\perp}\Omega_n\|_2\to0.
\]

After rotations and a subsequence, take \(e_n=e_3\).

Fix \(\varepsilon>0\) and then choose \(R\) from tightness. For this fixed \(R\), the cutoff-Poincare estimate and interpolation imply

\[
\|\Omega_n\cdot e_3\|_{L^2(B_R)}
\to O(\varepsilon).
\]

The transverse component tends to zero globally, and the tail outside \(B_R\) is \(O(\varepsilon)\). Therefore

\[
\limsup_n\|\Omega_n\|_2
\le C\varepsilon.
\]

Let \(\varepsilon\downarrow0\). This contradicts \(\|\Omega_n\|_2\ge m_0\).

Status: **PROVED.**

## 6. Quantitative corridor version

Suppose at selected recurrent times one has:

1. a nontrivial enstrophy floor
   \[
   \|\Omega\|_2\ge m_0>0;
   \]
2. an H2/hyperpalinstrophy ceiling
   \[
   \|\Delta\Omega\|_2\le H_0;
   \]
3. a tightness radius \(R_Z\) for which the transition-shell/tail norm is at most \(\varepsilon_{tail}\).

Then the preceding estimate yields

\[
m_0
\lesssim
\|P_{e^\perp}\Omega\|_2
+R_ZH_0^{1/2}
\|P_{e^\perp}\Omega\|_2^{1/2}
+\varepsilon_{tail}.
\]

Whenever \(\varepsilon_{tail}\) is a sufficiently small fixed fraction of \(m_0\), this implies an explicit positive root bound

\[
\boxed{
\|P_{e^\perp}\Omega\|_2
\ge
\delta_{dir}(m_0,H_0,R_Z,\varepsilon_{tail})>0
}
\]

uniformly for every axis \(e\).

No sharp formula is required at this stage; the important point is that the lower bound is fixed on the tight H2-bounded corridor.

## 7. Application to permanent export

Let \(e_{exp}\) be the coherent direction of one exported fixed-flux population.

The lemma gives, at every selected tight H2-bounded recurrent time,

\[
\boxed{
\|P_{e_{exp}^\perp}\Omega\|_2
\ge\delta_{dir}>0.
}
\]

Therefore a nontrivial permanent-export survivor cannot consist of a single globally one-directional vorticity conveyor.

A fixed amount of transverse vorticity must coexist with every such axis.

This is a genuine structural restriction.

## 8. Why this is not yet an event charge

The transverse residual may be the same persistent background structure reused through many export events.

Thus the estimate

\[
\|P_{e_{exp}^\perp}\Omega\|_2\ge\delta_{dir}
\]

is not by itself additive in time and cannot yet be summed over positive-frequency export events.

The next bridge must show at least one of:

1. changing export axes forces repeated projective/directional action;
2. a fixed export axis plus persistent transverse residual forces multiflux/Betchov/H activity;
3. the transverse residual must itself be exported/recycled and therefore enters the finite-memory turnover ledger.

## 9. Relation to known Type-I frontier

The result removes a particularly simple one-axis critical conveyor but does not exclude general backward DSS/Type-I weak-critical structures. Those remain known difficult classes.

## 10. Audit verdict

### PROVED

A nonzero, globally enstrophy-tight, uniformly H2-bounded divergence-free vorticity sequence cannot converge globally to a one-axis direction field.

### NEW NECESSARY CONDITION FOR THE SURVIVOR

Every coherent export axis must coexist with a fixed positive transverse-enstrophy defect on the tight H2-bounded recurrent corridor.

### OPEN

Convert this persistent transverse defect into an additive projective/H/export cost.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
