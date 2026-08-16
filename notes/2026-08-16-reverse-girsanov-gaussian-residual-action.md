# Reverse Girsanov bridge from Gaussian non-affinity to nonlinear path-law closeness

Date: 2026-08-16

Status: **DERIVED REVERSE RELATIVE-ENTROPY IDENTITY FOR THE SELF-CONSISTENT AFFINE GAUSSIAN REFERENCE. SMALL GAUSSIAN RESIDUAL ACTION IMPLIES PATH-LAW CLOSENESS UNLESS THE AFFINE GAUSSIAN COVARIANCE ITSELF ESCAPES SPATIALLY. GLOBAL REGULARITY NOT PROVED.**

## 1. Two diffusions with the same noise

Fix a smooth pre-singular interval `[t0,T]` and the self-consistent Gaussian affine frame

\[
b_{\rm aff}(x,t)=a'(t)+L(t)(x-a(t)),
\]

\[
b(x,t)=u(x,t)=b_{\rm aff}(x,t)+r(x-a(t),t).
\]

Consider the two path laws with the same diffusion coefficient `sqrt(2 nu)` and the same terminal/start specification appropriate to the backward affine-kernel construction:

\[
P_{\rm aff}:
\quad dX_t=b_{\rm aff}(X_t,t)dt+\sqrt{2\nu}\,dW_t,
\]

\[
P:
\quad dX_t=b(X_t,t)dt+\sqrt{2\nu}\,dW_t.
\]

The one-time marginals of the affine reference are exactly the self-consistent Gaussian kernels

\[
\gamma_t=N(0,\Sigma(t))
\]

in moving coordinates.

For a smooth solution on a compact pre-singular interval, one may first localize the drifts so Novikov holds globally and then remove the localization. The identities below are the standard Girsanov entropy identities in this smooth regime.

## 2. Forward and reverse relative entropy

The drift difference is exactly `r`. Therefore

\[
D_{\rm KL}(P\|P_{\rm aff})
=
\frac1{4\nu}
\mathbb E_P
\int_{t_0}^{T}|r(X_t,t)|^2dt.
\]

The equally valid reverse orientation is

\[
\boxed{
D_{\rm KL}(P_{\rm aff}\|P)
=
\frac1{4\nu}
\mathbb E_{P_{\rm aff}}
\int_{t_0}^{T}|r(X_t,t)|^2dt.
}
\]

Because the affine marginal at time `t` is `gamma_t`, Fubini gives

\[
\boxed{
D_{\rm KL}(P_{\rm aff}\|P)
=
\frac1{4\nu}
\int_{t_0}^{T}
\int\gamma_t(y)|r(y,t)|^2dy\,dt.
}
\]

This is the useful direction for the DSD Gaussian state because the expectation is under the known affine Gaussian law rather than under the unknown exact kernel.

## 3. Gaussian Poincare closes the residual velocity action

The self-consistent affine frame satisfies

\[
\int\gamma_t r=0
\]

and

\[
\boxed{
B_\gamma(t)
=\int\gamma_t|\nabla r|_F^2.
}
\]

Gaussian Poincare yields

\[
\int\gamma_t|r|^2
\le
\lambda_{\max}(\Sigma(t))
\int\gamma_t|\nabla r|^2.
\]

Hence

\[
\boxed{
D_{\rm KL}(P_{\rm aff}\|P)
\le
\frac1{4\nu}
\int_{t_0}^{T}
\lambda_{\max}(\Sigma(t))
B_\gamma(t)dt.
}
\]

This is an exact one-sided bridge from the Gaussian non-affinity ledger to path-law closeness.

## 4. Pinsker consequence

Pinsker is symmetric at the level of total variation, so

\[
\|P_{\rm aff}-P\|_{TV}
\le
\sqrt{\frac12D_{\rm KL}(P_{\rm aff}\|P)}.
\]

Therefore

\[
\boxed{
\int\lambda_{\max}(\Sigma)B_\gamma dt=o(1)
\Longrightarrow
\|P_{\rm aff}-P\|_{TV}=o(1).
}
\]

Any uniformly bounded path observable then has asymptotically the same expectation under the nonlinear and affine path laws.

The boundedness qualifier is essential: total variation alone does not transfer an unbounded deformation-gradient observable.

## 5. Parabolic critical evaluation

On the minimal recent-source branch the normalized source interval has length

\[
T_R\asymp R^2.
\]

Suppose first that the affine Gaussian remains spatially controlled in the sense

\[
\boxed{
\sup_I\lambda_{\max}(\Sigma(t))\le C R^2.
}
\]

If the accumulated Gaussian residual seed obeys

\[
\boxed{
\mathcal B_R
:=\int_I B_\gamma(t)dt
\le R^{-2-\varepsilon}
}
\]

for some fixed `epsilon>0`, then

\[
D_{\rm KL}(P_{\rm aff}\|P)
\lesssim_{\nu,C}
R^2\mathcal B_R
\lesssim R^{-\varepsilon}.
\]

Thus

\[
\boxed{
\|P_{\rm aff}-P\|_{TV}
\lesssim R^{-\varepsilon/2}\to0.
}
\]

Hence the very-small-seed branch is asymptotically affine in path law whenever its Gaussian covariance remains at the core-parabolic spatial scale.

## 6. Spatial-escape alternative

If the previous conclusion cannot be invoked because

\[
\lambda_{\max}(\Sigma)/R^2
\to\infty,
\]

then the affine observation kernel itself has left the coherent core scale.

Thus the very-small-seed branch has the exact dichotomy

\[
\boxed{
\mathcal B_R\le R^{-2-\varepsilon}
\Longrightarrow
\begin{cases}
P_{\rm aff}\text{ and }P\text{ are asymptotically close in TV},\\
\text{or }\lambda_{\max}(\Sigma)\gg R^2
\text{ (Gaussian spatial escape).}
\end{cases}
}
\]

The second branch is already an existing spatial non-tightness / large affine deformation channel.

## 7. Combine with the actual-transition-stretch lemma

The exact variation-of-constants result gives, on the same small-seed branch,

\[
q_*\gtrsim\mathcal B_R^{-1}.
\]

Therefore if

\[
\mathcal B_R\le R^{-2-\varepsilon},
\]

then

\[
\boxed{
q_*\gtrsim R^{2+\varepsilon}.
}
\]

Consequently a surviving very-small-seed episode must simultaneously satisfy

\[
\boxed{
\text{actual polynomially huge affine deformation}
+
\text{nonlinear path law close to its affine Gaussian reference}
}
\]

unless the Gaussian covariance itself becomes spatially non-tight.

This is substantially narrower than the earlier generic small-seed branch.

## 8. Claim boundary

The path-law TV closeness does not by itself control the vorticity deformation-gradient factor in a stochastic Cauchy formula, because that factor is unbounded and depends on spatial derivatives of the drift.

Therefore no regularity conclusion is claimed from Pinsker alone.

The next step is source-sensitive rather than path-event based: use the exact affine Duhamel propagator and the Gaussian residual-source curl/score identity to show that the huge transition `q_*` is offset by transverse affine heat smoothing unless the deformation is biaxially anisotropic or the residual develops a large velocity/derivative reservoir.

Status: **VERY-SMALL RESIDUAL SEED -> AFFINE PATH-LAW CLOSENESS OR GAUSSIAN SPATIAL ESCAPE / COMBINED WITH SMALL-SEED DEFORMATION LEMMA GIVES HUGE ACTUAL AFFINE STRETCH ON THE CLOSE-LAW BRANCH / SOURCE-SENSITIVE TRANSVERSE DIFFUSION REMAINS.**
