# Material total-curvature evolution routing

Date: 2026-08-16

Status: **EXACT CURVE-EVOLUTION INEQUALITY ON THE SMOOTH LIFESPAN / STOCHASTIC ADDITIVE-NOISE VERSION PATHWISE / GLOBAL REGULARITY NOT PROVED**.

## 1. Purpose

The stochastic ancestor geometry has been reduced to

\[
\boxed{
N_D\mathcal K_-
\gtrsim R,
}
\]

where

- `N_D` is the ancestor diameter in earlier natural-radius units;
- `mathcal K_-` is the total curvature of the ancestor loop;
- `R -> infinity` is the coherent crossing radius.

This note shows that divergent total curvature is not a new independent causal branch.  Its evolution is supported only by strain acting on existing curvature or by velocity-Hessian forcing.

---

## 2. Moving curve geometry

Let a smooth curve move with the incompressible velocity field:

\[
\partial_tX(a,t)=U(X(a,t),t).
\]

For the Constantin--Iyer stochastic flow the same spatial derivative formulas hold pathwise because the Brownian term is additive and spatially constant; derivatives with respect to the curve label do not see a direct noise derivative.

Parameterize the instantaneous curve by arclength `s` and define

\[
T=\partial_sX,
\qquad |T|=1,
\]

\[
K=\partial_sT,
\qquad
\kappa=|K|.
\]

Write

\[
a=T^TST,
\qquad
S=\frac12(\nabla U+\nabla U^T).
\]

The arclength element evolves by

\[
\boxed{
D_t(ds)=a\,ds.
}
\]

Consequently

\[
\boxed{
[D_t,\partial_s]
=-a\partial_s.
}
\]

---

## 3. Tangent equation

Differentiate the flow along the curve.  After normalizing to unit length,

\[
\boxed{
D_tT
=(\nabla U)T-aT.
}
\]

The antisymmetric part of `grad U` rotates the tangent but does not change line length.

---

## 4. Curvature-vector equation

Using the commutator,

\[
\begin{aligned}
D_tK
&=D_t(\partial_sT)\\
&=\partial_s(D_tT)-aK\\
&=(\nabla_T\nabla U)T
+(\nabla U)K
-(\partial_sa)T
-2aK.
\end{aligned}
\]

Thus

\[
\boxed{
D_tK
=(\nabla_T\nabla U)T
+(\nabla U)K
-(\partial_sa)T
-2aK.
}
\]

Since `K perpendicular T`, the `partial_s a` term drops out of the norm derivative.

For `kappa>0`, with `N_K=K/kappa`,

\[
D_t\kappa
=
N_K\cdot(\nabla_T\nabla U)T
+\kappa N_K^TSN_K
-2a\kappa.
\]

Therefore

\[
D_t\kappa
\le
|\nabla^2U|
+\big(\|S\|_{op}+2|a|\big)\kappa.
\]

---

## 5. Total-curvature inequality

Define

\[
\boxed{
\mathcal K(t)
=\int_{C_t}\kappa\,ds.
}
\]

Using `D_t ds=a ds`,

\[
\frac d{dt}\mathcal K
=
\int_{C_t}
\big(D_t\kappa+a\kappa\big)ds.
\]

At the exact quadratic-form level,

\[
N_K^TSN_K-a
\]

has magnitude at most `2||S||_op`.  Hence

\[
\boxed{
\frac d{dt}\mathcal K(t)
\le
2\|S(t)\|_\infty\mathcal K(t)
+
\int_{C_t}|\nabla^2U|\,ds.
}
\]

The same absolute-value inequality applies when following a smooth stochastic-flow realization backward or forward over a compact smooth time interval.

---

## 6. Gronwall routing

Let

\[
K_S
:=
\int_{t_-}^{t_c}\|S(t)\|_\infty dt
\]

and

\[
H_C
:=
\int_{t_-}^{t_c}
\int_{C_t}|\nabla^2U|\,ds\,dt.
\]

Up to harmless orientation of the time integration, the absolute differential inequality gives

\[
\boxed{
\mathcal K_-
\lesssim
\exp(2K_S)
\big(\mathcal K_c+H_C\big).
}
\]

At the final coherent crossing the selected reference loop is geometrically simple, so

\[
\mathcal K_c=O(1).
\]

Therefore if

\[
\mathcal K_-\to\infty,
\]

then at least one of

\[
\boxed{K_S\to\infty}
\]

or

\[
\boxed{H_C\to\infty}
\]

must occur.

More quantitatively, if `mathcal K_- = K >> 1`, then either

\[
\boxed{
K_S
\ge
\frac14\log K-O(1)
}
\]

or

\[
\boxed{
H_C
\gtrsim
K^{1/2}.
}
\]

Indeed, if `K_S < (1/4) log K - C`, the exponential factor is at most a fixed multiple of `K^(1/2)`, forcing the bracket to be at least a fixed multiple of `K^(1/2)`.

---

## 7. Combine with the diameter--curvature product

Using the symmetric split

\[
N_D\gtrsim\sqrt R
\quad\text{or}\quad
\mathcal K_-\gtrsim\sqrt R,
\]

the curvature side gives

\[
\boxed{
K_S
\gtrsim
\frac18\log R
}
\]

or

\[
\boxed{
H_C
\gtrsim
R^{1/4}.
}
\]

Thus every late coherent crossing satisfies the three-way routed alternative

\[
\boxed{
\begin{cases}
\text{ancestor diameter spans }\gtrsim\sqrt R\text{ earlier natural radii},\\
\text{or accumulated }L^\infty\text{ strain carries a divergent }\log R\text{ action},\\
\text{or line-integrated velocity-Hessian forcing grows at least like }R^{1/4}.
\end{cases}
}
\]

Constants and the symmetric exponent `1/2` are not claimed optimal; the structural dichotomy is the point.

---

## 8. DSD / proof-tree interpretation

The stochastic-ancestor total-curvature channel is not retained as a new endpoint.

It maps to existing state variables:

\[
\boxed{
\mathcal K
\to
\text{strain-action channel}
\oplus
\text{higher-derivative/Hessian channel}.
}
\]

Therefore the late stochastic ancestry tree is now

\[
\boxed{
\text{critical spatial escape}
\quad\lor\quad
\text{critical strain action}
\quad\lor\quad
\text{higher derivative forcing}.
}
\]

This is the same core trichotomy reached earlier by independent Gaussian/Hermite/material arguments, now obtained from the exact stochastic Kelvin ancestry of the final circulation.

---

## 9. Claim boundary

The line quantity

\[
\int_{C_t}|\nabla^2U|ds
\]

is not controlled directly by the global `L2` palinstrophy budget without a thickness/trace argument.  Thus the Hessian branch is not closed here.

Likewise the divergent strain action is compatible with the BKM-critical signature of a hypothetical singularity.

The gain is causal classification: no stochastic-ancestor curvature growth remains unexplained outside the already active strain/derivative channels.

Overall status: **TOTAL-CURVATURE ESCAPE ROUTED EXACTLY TO STRAIN OR HESSIAN FORCING / STOCHASTIC ANCESTRY INTRODUCES NO NEW CAUSAL BRANCH / GLOBAL REGULARITY NOT PROVED.**
