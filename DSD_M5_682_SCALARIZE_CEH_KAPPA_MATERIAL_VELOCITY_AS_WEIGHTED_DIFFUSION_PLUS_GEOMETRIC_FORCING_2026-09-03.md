# DSD M5-682 — Scalarize the CE-H kappa material velocity as weighted kappa diffusion plus explicit geometric forcing

Date: 2026-09-03

Status: **INTERNAL CONSTITUTIVE REDUCTION / DOT-PROJECTING THE M5-601 MATERIAL-LAPLACIAN COMMUTATOR AND USING `W=rho xi`, `Sigma W=sigma W`, `Delta W=kappa W` GIVES AN EXACT SCALAR FORMULA FOR `h=D_B kappa`; ITS PRINCIPAL PART IS THE WEIGHTED LAPLACIAN `rho^{-2} div(rho^2 grad kappa)`, ACCOMPANIED BY THE SAME WEIGHTED OPERATOR ON `sigma`, THE LINEAR TERM `-kappa`, AND AN EXPLICIT GEOMETRIC REMAINDER INVOLVING THE STRAIN-HESSIAN AMPLITUDE COUPLING, THE DIRECTION METRIC, AND `curl W · grad log rho` / THE ANTISYMMETRIC PART OF `grad U` CANCELS FROM THE SECOND-DERIVATIVE CONTRACTION / THIS IS THE PDE CONSTITUTIVE LAW ABSENT FROM THE M5-653/680 TOY OSCILLATORS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-601

On CE-H,

\[
\Delta W=\kappa W,
\qquad
D_BW=\gamma W,
\qquad
\gamma=\sigma+\kappa-1.
\]

M5-601 gives

\[
\boxed{
(h-\Delta\gamma+\kappa)W
=
2\nabla\gamma\cdot\nabla W
-2\partial_iU_j\partial_{ij}W
+(\nabla\times W)\cdot\nabla W,
}
\]

where

\[
\boxed{h:=D_B\kappa.}
\]

Work first on the active set `rho=|W|>0`.

---

## 2. Parallel projection

Dot the identity with `W/rho^2`.
Because

\[
W\cdot\partial_jW
=\rho\partial_j\rho,
\]

we have

\[
\frac{2}{\rho^2}
W\cdot(\nabla\gamma\cdot\nabla W)
=
2\nabla\gamma\cdot\nabla\log\rho.
\]

Therefore

\[
\boxed{
\begin{aligned}
h
={}&
\Delta\gamma-\kappa
+2\nabla\gamma\cdot\nabla\log\rho\\
&-
\frac{2}{\rho^2}
W\cdot(\partial_iU_j\partial_{ij}W)
+
\frac1{\rho^2}
W\cdot((\nabla\times W)\cdot\nabla W).
\end{aligned}
}
\]

---

## 3. Simplify the second-derivative velocity-gradient term

For `W=rho xi`, `|xi|=1`,

\[
\partial_iW\cdot\partial_jW
=
\partial_i\rho\,\partial_j\rho
+\rho^2\partial_i\xi\cdot\partial_j\xi.
\]

Also

\[
W\cdot\partial_{ij}W
=
\partial_{ij}\frac{\rho^2}{2}
-
\partial_iW\cdot\partial_jW.
\]

Hence

\[
\boxed{
W\cdot\partial_{ij}W
=
\rho\partial_{ij}\rho
-
\rho^2\partial_i\xi\cdot\partial_j\xi.
}
\]

Thus

\[
-
\frac2{\rho^2}
W\cdot(\partial_iU_j\partial_{ij}W)
=
-
2\partial_iU_j
\left[
\frac{\partial_{ij}\rho}{\rho}
-
\partial_i\xi\cdot\partial_j\xi
\right].
\]

The tensor in square brackets is symmetric in `i,j`.
Therefore the antisymmetric part of `grad U` drops out and only the strain remains:

\[
\boxed{
-
\frac2{\rho^2}
W\cdot(\partial_iU_j\partial_{ij}W)
=
-
\frac2\rho\Sigma:\nabla^2\rho
+
2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi.
}
\]

---

## 4. Simplify the curl-W transport term

Let

\[
C:=\nabla\times W.
\]

Then

\[
W\cdot(C\cdot\nabla W)
=
C_jW\cdot\partial_jW
=
\rho C\cdot\nabla\rho.
\]

Therefore

\[
\boxed{
\frac1{\rho^2}
W\cdot((\nabla\times W)\cdot\nabla W)
=
(\nabla\times W)\cdot\nabla\log\rho.
}
\]

---

## 5. Weighted-divergence principal part

Since

\[
\gamma=\sigma+\kappa-1,
\]

we have

\[
\Delta\gamma
+2\nabla\gamma\cdot\nabla\log\rho
=
\rho^{-2}\nabla\cdot(\rho^2\nabla\gamma).
\]

Split `gamma` into `sigma+kappa-1`:

\[
\boxed{
\rho^{-2}\nabla\cdot(\rho^2\nabla\gamma)
=
\rho^{-2}\nabla\cdot(\rho^2\nabla\kappa)
+
\rho^{-2}\nabla\cdot(\rho^2\nabla\sigma).
}
\]

Hence the exact constitutive equation is

\[
\boxed{
\begin{aligned}
D_B\kappa
={}&
\rho^{-2}\nabla\cdot(\rho^2\nabla\kappa)
+
\rho^{-2}\nabla\cdot(\rho^2\nabla\sigma)
-
\kappa\\
&-
\frac2\rho\Sigma:\nabla^2\rho
+
2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+
(\nabla\times W)\cdot\nabla\log\rho.
\end{aligned}
}
\]

Define

\[
\boxed{
\mathcal R_{geom}
:=-
\frac2\rho\Sigma:\nabla^2\rho
+
2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+
(\nabla\times W)\cdot\nabla\log\rho.
}
\]

Then compactly

\[
\boxed{
h
=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom},
}
\]

where

\[
\boxed{
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f).
}
\]

---

## 6. Structural interpretation

The multi-sheet current velocity `h` of M5-681 is not arbitrary.
Its principal scalar part is a weighted diffusion operator on `kappa`:

\[
L_\rho\kappa.
\]

The remaining terms are

1. weighted strain-eigenvalue diffusion `L_rho sigma`;
2. linear relaxation `-kappa`;
3. an explicit CE-H geometric remainder `R_geom`.

The abstract oscillators M5-653 and M5-680 specify `h` freely and therefore do not encode this constitutive law.

---

## 7. Zero-set firewall

The quotient expression uses `rho^{-1}` and `rho^{-2}`, so it is interpreted on `rho>0`.
The original vector commutator identity of M5-601 is smooth across `W=0` and remains the canonical global formulation.

All kappa-space applications below are restricted to retained high-amplitude populations with

\[
\rho\ge a_0>0,
\]

where the scalar formula is uniformly regular.

---

## 8. Next push-forward target

For a spatial/enstrophy-weighted kappa distribution the principal term has a clean integration-by-parts form:

\[
\rho^2 L_\rho\kappa
=\nabla\cdot(\rho^2\nabla\kappa).
\]

Pushing this to `kappa`-space yields a derivative of the nonnegative level diffusion density

\[
\int\delta(k-\kappa)\rho^2|\nabla\kappa|^2dy.
\]

The next step is to compute that push-forward exactly and audit whether the `sigma` and `R_geom` terms can sustain the strict directed current of M5-681.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
