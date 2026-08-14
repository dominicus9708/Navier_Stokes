# Adaptive previous-checkpoint inheritance is negligible

Date: 2026-08-14

Status: derived on the bounded-condition Gaussian branch; surviving pulse must be predominantly nonlinear creation.

Let the terminal first-hitting level be `W` and the previous adaptive threshold be `W_-=W/q`, with

\[
q=W^{1/3+2\varepsilon}.
\]

At the previous first-hitting time, terminal-normalized vorticity satisfies

\[
\|\Omega\|_\infty\le q^{-1}.
\]

Calderon--Zygmund plus John--Nirenberg therefore gives, uniformly over bounded-condition Gaussian windows and all centers,

\[
\boxed{B_-\lesssim_K q^{-2}.}
\]

Consider a later pulse observed at Gaussian radius `R`. Match the actual elapsed time by a parent heat covariance. The parent radius is at least of order `sqrt(q)` on the bounded-affine long-step branch; if the elapsed time is larger, heat contraction is only stronger.

The exact scale-time heat contraction therefore gives the homogeneous inherited contribution

\[
\boxed{B_{\rm inh}\lesssim_K R^2q^{-3}.}
\]

On the surviving low-curvature corridor write

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\]

and

\[
R\lesssim W^{1/6}\Lambda^{-1/5}.
\]

Then

\[
B_{\rm inh}
\lesssim
W^{1/3}\Lambda^{-2/5}
W^{-1-6\varepsilon}
=
W^{-2/3-6\varepsilon}\Lambda^{-2/5}.
\]

Hence relative to the required pulse height,

\[
\boxed{
\frac{B_{\rm inh}}{m}
\lesssim
W^{-1/3-6\varepsilon}\Lambda^{-7/5}
\to0.
}
\]

Thus a surviving intermediate residual pulse cannot be explained by linear heat transport of the previous first-hitting residual state. Up to bounded-affine comparison constants,

\[
\boxed{B_Q\ge(1-o(1))m,}
\]

where `B_Q` is the Gaussian variance of the nonlinear Duhamel commutator over the adaptive step.

Consequently the precursor branch is asymptotically eliminated for the actual adaptive checkpoint construction: the remaining pulse must be generated predominantly by nonlinear stretching/transport/pressure-projected dynamics during the current step.

Status: PREVIOUS-CHECKPOINT LINEAR INHERITANCE NEGLIGIBLE / ACTIVE FRONTIER = NONLINEAR CREATION PACKING OR RIGIDITY.
