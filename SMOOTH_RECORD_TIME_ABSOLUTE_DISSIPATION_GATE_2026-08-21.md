# Smooth Record-Time Absolute Dissipation Gate — 2026-08-21

Status: **SMOOTH-ONLY FINITE-STAGE NECESSARY CONDITION / GLOBAL REGULARITY NOT PROVED.**

This note stays on the original smooth first-hitting solution. It adds an absolute local dissipation cost on the set of record-growth times and does not use an ancient limit.

## 1. Running-record times

Let

\[
M(t)=\sup_{\tau\le t}\|\omega(\tau)\|_\infty,
\qquad
b=(\log M)_s\ge0,
\qquad
\int_{I_j}b\,ds=\log q.
\]

At almost every time in

\[
\mathcal R_j=\{s\in I_j:b(s)>0\},
\]

the current vorticity maximum equals the running record. In normalized variables,

\[
\|\Omega(s)\|_\infty=1.
\]

Let

\[
B_S:=\sup_{I_j}\|\Sigma\|_{L^\infty}.
\]

The record-point growth inequality gives

\[
b\le \xi^T\Sigma\xi\le B_S.
\]

Therefore

\[
\boxed{
|\mathcal R_j|\ge \frac{\log q}{B_S}.
}
\]

This avoids any assumption that one fixed endpoint core must persist for an entire stage.

## 2. Taylor record ball at every record-growth time

Assume a stage-uniform second derivative bound

\[
K_2(s)\le K_{2,+}.
\]

At a record point `y_*`, let

\[
\xi=\Omega(y_*),\qquad g(y)=\xi\cdot\Omega(y).
\]

Then

\[
g(y_*)=1,
\qquad
\nabla g(y_*)=0.
\]

If `K_2` bounds all directional second derivatives of `Omega`, Taylor's theorem gives on

\[
r_0=K_{2,+}^{-1/2}
\]

that

\[
g(y)\ge 1-\frac12 K_{2,+}|y-y_*|^2.
\]

Hence

\[
\begin{aligned}
\int_{B_{r_0}(y_*)}|\Omega|^2dy
&\ge
4\pi\int_0^{r_0}
\left(1-\frac12K_{2,+}r^2\right)^2r^2dr\\
&=
\boxed{
\frac{71\pi}{105}K_{2,+}^{-3/2}
}.
\end{aligned}
\]

Since pointwise

\[
|\nabla U|^2=|\Sigma|^2+\frac12|\Omega|^2,
\]

we obtain the record-ball dissipation floor

\[
\boxed{
D_{\rm rec}
:=\int_{B_{r_0}}|\nabla U|^2
\ge
\frac{71\pi}{210}K_{2,+}^{-3/2}.
}
\]

## 3. Record-ball velocity variance ceiling

Let

\[
B_1:=\sup_{I_j}\|\nabla U\|_{L^\infty}.
\]

For the ball mean `U_B`, use the exact pairwise variance identity

\[
\int_{B_r}|U-U_B|^2
=
\frac1{2|B_r|}
\int_{B_r}\int_{B_r}|U(x)-U(y)|^2dxdy.
\]

The Lipschitz bound gives

\[
|U(x)-U(y)|\le B_1|x-y|.
\]

For a uniform ball in three dimensions,

\[
\frac1{|B_r|^2}
\int_{B_r}\int_{B_r}|x-y|^2dxdy
=\frac65r^2.
\]

Therefore

\[
\boxed{
V_{\rm rec}
:=\int_{B_{r_0}}|U-U_B|^2
\le
\frac{4\pi}{5}
B_1^2K_{2,+}^{-5/2}.
}
\]

Combining with the dissipation floor,

\[
\boxed{
\frac{D_{\rm rec}}{V_{\rm rec}}
\ge
\frac{71}{168}
\frac{K_{2,+}}{B_1^2}.
}
\]

## 4. Record-centered moving-ball ledger

On a non-turnover lane, choose a coherent absolutely continuous record-core path and use a moving ball of radius `r_0` around that path. If no such path exists, the stage is already in the core-turnover branch.

The smooth moving-ball variance identity has the form

\[
\frac12V'+\nu D
=\frac a2V+\mathcal F,
\qquad
b=2a,
\qquad
\int_{I_j}a\,ds=\frac12\log q.
\]

The scale-input term is active only where `b>0`. Therefore

\[
\frac12\int_{I_j}aV\,ds
\le
\frac14(\log q)V_{\rm rec,+}.
\]

Assume the boundary/material flux is subdominant in the typed sense

\[
\left|\int_{I_j}\mathcal Fds\right|
\le
\eta\nu\int_{I_j}Dds+F_0,
\qquad
0\le\eta<1,
\]

and the endpoint variance change obeys

\[
|V(s_1)-V(s_0)|\le\kappa_V.
\]

Using only the record-time portion of the dissipation integral,

\[
\int_{I_j}Dds
\ge
D_{\rm rec}|\mathcal R_j|
\ge
D_{\rm rec}\frac{\log q}{B_S}.
\]

Hence a necessary condition for survival is

\[
(1-\eta)\nu D_{\rm rec}
\frac{\log q}{B_S}
\le
\frac14(\log q)V_{\rm rec,+}
+F_0+\frac12\kappa_V.
\]

Define dimensionless leakage allowances relative to the record-ball variance scale:

\[
\widehat f
=\frac{F_0}{(\log q)V_{\rm rec,+}},
\qquad
\widehat\kappa
=\frac{\kappa_V}{2(\log q)V_{\rm rec,+}}.
\]

Then

\[
\boxed{
\frac{71}{168}(1-\eta)
\frac{\nu K_{2,+}}
{B_S B_1^2}
\le
\frac14+\widehat f+\widehat\kappa.
}
\]

If the reverse strict inequality holds, the smooth record-centered pure lane is S-closed.

## 5. Remove `B_1`

Pointwise

\[
|\nabla U|^2
=|\Sigma|^2+\frac12|\Omega|^2
\]

and the first-hitting cap gives `|Omega|<=1`. Thus

\[
\boxed{
B_1^2\le B_S^2+\frac12.
}
\]

A convenient sufficient S-closure condition is therefore

\[
\boxed{
\frac{71}{168}(1-\eta)
\frac{\nu K_{2,+}}
{B_S(B_S^2+1/2)}
>
\frac14+\widehat f+\widehat\kappa.
}
\]

The notable feature is that this criterion is independent of the large common-core radius once `B_S` and `K_{2,+}` are fixed.

## 6. Branch interpretation

Failure of the assumptions has a typed meaning:

- no coherent record-core path -> core turnover `T`;
- large moving-boundary/material flux -> `T`;
- loss of the analytic Hessian ceiling -> derivative escape `H`;
- failure of the first-hitting cap -> outside the normalized stage;
- otherwise the displayed inequality is a direct smooth S-closure certificate.

Status: **A LARGE ANALYTIC-SCALE CORE CANNOT ESCAPE THE PROOF MERELY BY INCREASING ITS RADIUS. ON EVERY RECORD-GROWTH TIME A SMALL TAYLOR RECORD BALL IS RECREATED, AND ITS ABSOLUTE DISSIPATION/VECTOR-VARIANCE RATIO GIVES THE RADIUS-INDEPENDENT NECESSARY CONDITION ABOVE.**