# Smooth Positive-Middle Determinant Producer Obligation — 2026-08-22

Status: **EXACT SMOOTH ENSTROPHY/DETERMINANT OBLIGATION + GEOMETRIC-STAGE LOWER LIMSUP / GLOBAL REGULARITY NOT PROVED.**

This note addresses the complement in which the vorticity record core leaves the positive-middle strain geometry. The key point is that a singular first-hitting cascade cannot eliminate positive-middle strain everywhere: the exact physical enstrophy identity forces positive-middle determinant production to recur at order-one normalized strength.

## 1. Determinant sign and the middle strain eigenvalue

Let

\[
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0
\]

be the strain eigenvalues.

If `s2>0`, then

\[
s_1<0<s_2\le s_3
\]

and

\[
\det S<0.
\]

If `s2<0`, then

\[
s_1\le s_2<0<s_3
\]

and

\[
\det S>0.
\]

At `s2=0`, the determinant is zero.

Thus

\[
\boxed{
(-\det S)_+
=(-\det S)\,\mathbf 1_{\{s_2>0\}}.
}
\]

Positive determinant production is exactly the positive-middle strain sector.

## 2. Exact physical enstrophy identity

For a smooth rapidly decaying incompressible solution,

\[
\frac12\frac d{dt}\|\omega\|_2^2
+\nu\|\nabla\omega\|_2^2
=
\int S:(\omega\otimes\omega)\,dx.
\]

The global strain-vorticity determinant identity is

\[
\boxed{
\int S:(\omega\otimes\omega)\,dx
=-4\int\det S\,dx.
}
\]

Hence

\[
\boxed{
\frac12\|\omega(t)\|_2^2
+\nu\int_0^t\|\nabla\omega\|_2^2d\tau
=
\frac12\|\omega_0\|_2^2
+4\int_0^t\int(-\det S)\,dx\,d\tau.
}
\]

Split

\[
\mathcal D_+(t)
:=
\int_0^t\int_{\{s_2>0\}}(-\det S)\,dx\,d\tau,
\]

\[
\mathcal D_-(t)
:=
\int_0^t\int_{\{s_2<0\}}\det S\,dx\,d\tau.
\]

Both are nonnegative, and

\[
\int_0^t\int(-\det S)
=
\mathcal D_+(t)-\mathcal D_-(t).
\]

Therefore the exact balance is

\[
\boxed{
\mathcal D_+(t)
=
\mathcal D_-(t)
+\frac18\left(
\|\omega(t)\|_2^2-\|\omega_0\|_2^2
\right)
+\frac\nu4\int_0^t\|\nabla\omega\|_2^2d\tau.
}
\]

In particular,

\[
\boxed{
\mathcal D_+(t)
\ge
\frac18\left(
\|\omega(t)\|_2^2-\|\omega_0\|_2^2
\right).
}
\]

Thus unbounded physical enstrophy forces unbounded cumulative positive-middle determinant action.

## 3. First-hitting endpoint enstrophy floor

At a normalized first-hitting endpoint,

\[
\|\Omega\|_\infty=1.
\]

The record-point second-Taylor mass floor gives

\[
\|\Omega\|_2^2
\ge
C_ZK_{2,+}^{-3/2},
\qquad
C_Z=\frac{64\sqrt2\pi}{105}.
\]

Use

\[
K_{2,+}=\frac4{\rho_0^2}.
\]

Then

\[
\boxed{
\|\Omega\|_2^2
\ge
z_*:=\frac{8\sqrt2\pi}{105}\rho_0^3.
}
\]

If the physical vorticity maximum at the endpoint is `M_j`, the parabolic first-hitting scaling gives

\[
\boxed{
\|\omega(t_j)\|_2^2
=M_j^{1/2}\|\Omega_j\|_2^2
\ge
z_*M_j^{1/2}.
}
\]

Therefore along any hypothetical singular first-hitting sequence `M_j -> infinity`,

\[
\boxed{
\|\omega(t_j)\|_2^2\to\infty.
}
\]

This conclusion uses only the actual smooth endpoint and the analytic Hessian ceiling; no ancient limit is involved.

## 4. Cumulative positive-middle action must grow at least like `M_j^(1/2)`

Insert the endpoint floor into the exact determinant balance:

\[
\mathcal D_+(t_j)
\ge
\frac18
\left(
 z_*M_j^{1/2}-\|\omega_0\|_2^2
\right).
\]

Hence

\[
\boxed{
\liminf_{j\to\infty}
\frac{\mathcal D_+(t_j)}{M_j^{1/2}}
\ge
\frac{z_*}{8}
=
\frac{\sqrt2\pi}{105}\rho_0^3.
}
\]

So a negative-middle-only cascade is impossible. Even if the record point itself is negative-middle, positive-middle determinant producers must occur elsewhere in spacetime with cumulative critical-scale strength.

## 5. Geometric-stage normalized producer action

Let

\[
M_{j+1}=qM_j,
\qquad q>1,
\]

and use the running normalized variables on stage `I_j`. Define the normalized positive-middle determinant action

\[
\boxed{
A_{+,j}
:=
\int_{I_j}
\int_{\{s_2(\Sigma)>0\}}
(-\det\Sigma)\,dy\,ds.
}
\]

Under the running parabolic normalization,

\[
S=M\Sigma,
\qquad
 dx=M^{-3/2}dy,
\qquad
 dt=M^{-1}ds.
\]

Therefore

\[
(-\det S)\,dx\,dt
=M^{1/2}(-\det\Sigma)\,dy\,ds.
\]

Since `M_j <= M(s) <= qM_j` on the stage,

\[
\boxed{
M_j^{1/2}A_{+,j}
\le
\mathcal D_{+,j}^{phys}
\le
q^{1/2}M_j^{1/2}A_{+,j}.
}
\]

## 6. Positive limsup on geometric stages

Suppose for contradiction that

\[
\limsup_{j\to\infty}A_{+,j}=L
\]

is arbitrarily small. The geometric sum satisfies

\[
\sum_{j=0}^{N-1}M_j^{1/2}
=
M_N^{1/2}
\frac{1-q^{-N/2}}{\sqrt q-1}.
\]

Using the upper stage conversion,

\[
\limsup_{N\to\infty}
\frac{\mathcal D_+(t_N)}{M_N^{1/2}}
\le
\frac{\sqrt q}{\sqrt q-1}L.
\]

But Section 4 gives the lower limit `z_*/8`. Hence

\[
\boxed{
\limsup_{j\to\infty}A_{+,j}
\ge
\frac{\sqrt q-1}{\sqrt q}\frac{z_*}{8}.
}
\]

For `q=2`,

\[
\frac{\sqrt2-1}{\sqrt2}\frac{z_*}{8}
=
\boxed{
\frac{(\sqrt2-1)\pi}{105}\rho_0^3
}.
\]

Numerically,

\[
\boxed{
\frac{(\sqrt2-1)\pi}{105}
\approx0.0123932408054.
}
\]

Therefore infinitely many late smooth geometric stages obey

\[
\boxed{
A_{+,j}
\ge
\frac{(\sqrt2-1)\pi}{105}\rho_0^3-o(1).
}
\]

This is an order-one normalized positive-middle determinant-producer obligation.

## 7. Proof-tree consequence

The record core can no longer escape the positive-middle local closure simply by becoming negative-middle everywhere.

A hypothetical singular cascade must repeatedly realize one of two configurations:

1. **record-centered positive-middle producer** — then the adaptive Taylor-ball pure-local closure applies unless a typed complement is activated;
2. **spatially or structurally separate positive-middle producer** — the record core is negative-middle or otherwise non-producing, while a distinct region carries the mandatory determinant action `A_{+,j}`.

The second case is not a free `P_V` survivor. It is an explicit producer-separation problem: the proof must account for how order-one positive-middle determinant action is supplied away from the record-centered local lane.

Possible realizations are already typed as

- bounded-radius spectral/shape turnover;
- a separate active producer core;
- active outer/parent strain;
- boundary/material transport;
- derivative/high-frequency escape;
- distributed producer action requiring a new packing estimate.

## 8. Significance

The combination of this note with the adaptive Taylor-ball closure changes the `P_V` frontier:

\[
\boxed{
\text{positive-middle record core}
\to
\text{local S-closure or typed complement},
}

while

\[
\boxed{
\text{negative-middle record core}
\to
\text{mandatory separate positive-middle determinant producer}.
}

Thus an autonomous, single-core, low-turnover `P_V` mechanism is no longer available simply by switching the sign of the middle strain eigenvalue.

The next target is to localize the producer action relative to the adaptive record ball and prove a quantitative dichotomy:

\[
\boxed{
\text{producer overlaps record neighborhood}
\quad\text{or}\quad
\text{order-one producer action is spatially separated}.
}
\]

The overlap branch should feed the local closure; the separated branch is the remaining `T/H` packing problem.

Status: **A SINGULAR FIRST-HITTING CASCADE FORCES ORDER-ONE NORMALIZED POSITIVE-MIDDLE DETERMINANT ACTION ON INFINITELY MANY STAGES. NEGATIVE-MIDDLE-ONLY CASCADES ARE EXCLUDED, BUT THE SPATIALLY SEPARATED PRODUCER BRANCH REMAINS OPEN.**