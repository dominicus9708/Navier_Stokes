# Source-sensitive affine transverse half-power compensation

Date: 2026-08-16

Status: **DERIVED POINTWISE-IN-SOURCE-TIME AFFINE DUHAMEL ESTIMATE. AN INCOMPRESSIBLE TRANSITION STRETCH `q` CANNOT MULTIPLY A GAUSSIAN RESIDUAL SOURCE BY `q` WITHOUT ALSO EXPOSING THAT SOURCE TO TRANSVERSE AFFINE-HEAT SCORE SMOOTHING; IN BALANCED GEOMETRY THE NET EXPLICIT STRETCH FACTOR IS REDUCED TO `q^(1/2)` UP TO THE SECOND-SINGULAR-VALUE ANISOTROPY. GLOBAL REGULARITY NOT PROVED.**

## 1. Source-time SVD

Fix a residual-source time `s<T` and write the affine transition

\[
F(T,s)=U\,\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)V^T,
\]

with

\[
\sigma_1=q\ge\sigma_2\ge\sigma_3>0,
\qquad
\sigma_1\sigma_2\sigma_3=1.
\]

Let `u_i` and `v_i` be the left and right singular vectors.

The terminal contribution of the Gaussian residual mean source is

\[
F(T,s)J(s).
\]

Along the maximally amplified output direction,

\[
\boxed{
 u_1\cdot F(T,s)J(s)
=q\,v_1\cdot J(s).
}
\]

## 2. Exact transverse score form of the source

The Gaussian residual-source identity gives

\[
J
=\mathbb E_\gamma
\left[s_\gamma\times(\delta\Omega\times r)\right],
\]

where

\[
s_\gamma=\nabla\log\gamma.
\]

Therefore

\[
\boxed{
 v_1\cdot J
=
\mathbb E_\gamma
\left[
(v_1\times s_\gamma)\cdot(\delta\Omega\times r)
\right].
}
\]

Set

\[
\mathcal H(s)
:=
\left(
\mathbb E_\gamma
|\delta\Omega\times r|^2
\right)^{1/2}.
\]

Then

\[
|v_1\cdot J|
\le
\left(
\mathbb E_\gamma|v_1\times s_\gamma|^2
\right)^{1/2}
\mathcal H(s).
\]

## 3. Affine heat covariance lower bound

Let

\[
C(T,s)
=\int_s^T
F(\tau,s)^{-1}F(\tau,s)^{-T}d\tau,
\]

and

\[
\Sigma(s)=2\nu C(T,s).
\]

Define the remaining affine strain-energy action

\[
\mathcal J_S(s,T)
:=
\int_s^T
\|S_L(\tau)\|_{op}^2d\tau,
\qquad
S_L=\operatorname{sym}L.
\]

The rotation-independent affine deformation--diffusion estimate gives

\[
\boxed{
C(T,s)
\succeq
\frac{(1-q^{-1})^2}{\mathcal J_S(s,T)}
F(T,s)^{-1}F(T,s)^{-T}.
}
\]

Hence

\[
\Sigma^{-1}
\preceq
\frac{\mathcal J_S(s,T)}{2\nu(1-q^{-1})^2}
V\,\operatorname{diag}(q^2,\sigma_2^2,\sigma_3^2)V^T.
\]

Because for a Gaussian

\[
\mathbb E_\gamma[s_\gamma\otimes s_\gamma]=\Sigma^{-1},
\]

we have

\[
\begin{aligned}
\mathbb E|v_1\times s_\gamma|^2
&=
\operatorname{tr}(P_{v_1^\perp}\Sigma^{-1})\\
&\le
\frac{\mathcal J_S(s,T)}{2\nu(1-q^{-1})^2}
(\sigma_2^2+\sigma_3^2).
\end{aligned}
\]

Therefore

\[
\boxed{
|u_1\cdot FJ|
\le
\frac{q}{1-q^{-1}}
\left(\frac{\mathcal J_S}{2\nu}\right)^{1/2}
(\sigma_2^2+\sigma_3^2)^{1/2}
\mathcal H.
}
\]

This is a source-sensitive affine Duhamel estimate at one injection time.

## 4. Anisotropy parameterization

Write

\[
\boxed{
\sigma_2=q^{-1/2}\chi,
\qquad
\sigma_3=q^{-1/2}\chi^{-1},
\qquad
\chi\ge1.
}
\]

Then

\[
\boxed{
|u_1\cdot FJ|
\le
\frac{q^{1/2}}{1-q^{-1}}
\left(\frac{\mathcal J_S}{2\nu}\right)^{1/2}
(\chi^2+\chi^{-2})^{1/2}
\mathcal H.
}
\]

Thus the naive explicit `q` amplification has been reduced to

\[
\boxed{q^{1/2}\times\text{anisotropy factor}.}
\]

For balanced transverse compression `chi=O(1)`, this is the clean half-power compensation.

## 5. Geometric meaning of chi

The second singular value is

\[
\sigma_2=q^{-1/2}\chi.
\]

Hence:

- `chi=O(1)`: both transverse directions are compressed comparably, and the half-power gain is effective;
- `1<<chi<<q^(1/2)`: one transverse direction is much less compressed, but both are still contracting;
- `chi>=q^(1/2)`: `sigma2>=1`, so two singular directions are noncontracting/extending. This is the biaxial-extensional-plane geometry identified previously as the hard affine branch.

At the exact threshold `chi=q^(1/2)`, the explicit factor returns to order `q`; this is not a failure of the estimate but the signal that transverse two-direction smoothing has degenerated to essentially one strong compressed direction.

## 6. Large-q source times really carry terminal contribution

Let

\[
\left|
\int_I F(T,s)J(s)ds
\right|
\ge c_0
\]

and

\[
\mathcal J=\int_I|J(s)|ds.
\]

Set

\[
Q=\frac{c_0}{2\mathcal J}.
\]

On the set

\[
A_<:=\{s:\|F(T,s)\|<Q\},
\]

\[
\left|
\int_{A_<}FJds
\right|
\le
Q\mathcal J
=\frac{c_0}{2}.
\]

Therefore its complement

\[
A_>:=\{s:\|F(T,s)\|\ge Q\}
\]

must carry

\[
\boxed{
\left|
\int_{A_>}FJds
\right|
\ge\frac{c_0}{2}.
}
\]

Thus the large transition obtained from the small-seed lemma is not merely attained at an irrelevant time. A fixed fraction of the terminal source contribution must come from source times with

\[
\boxed{
q(s)\gtrsim\mathcal J^{-1}.
}
\]

If `|J|lesssim B` and

\[
\int_I Bds\le R^{-\gamma},
\]

then the active source set satisfies

\[
\boxed{q(s)\gtrsim R^\gamma.}
\]

## 7. Resulting small-seed geometry

On the very-small-seed branch, a fixed fraction of the endpoint source must therefore be supplied by times that satisfy both

\[
q(s)\gg1
\]

and the transverse-score estimate of Section 4.

The branch splits sharply:

\[
\boxed{
\text{balanced / uniaxial-like transition}
\quad\lor\quad
\text{biaxial anisotropy }\chi\gtrsim q^{1/2}.
}
\]

The first receives a genuine affine-heat half-power reduction in the explicit deformation factor. The second is the pre-existing biaxial compression-diffusion / long-reservoir geometry.

## 8. What is still missing

The quantity

\[
\mathcal H^2
=
\mathbb E_\gamma|\delta\Omega\times r|^2
\]

is a residual velocity/vorticity reservoir. Under the first-hitting cap it obeys

\[
\mathcal H^2
\lesssim
\mathbb E_\gamma|r|^2
\le
\lambda_{\max}(\Sigma)B_\gamma,
\]

but `lambda_max(Sigma)` can grow under strong affine deformation.

Therefore the half-power estimate alone does not close the balanced branch. A complete closure requires either

1. a core-scale covariance ceiling, giving a direct residual-velocity action bound;
2. or treating `lambda_max(Sigma)>>R^2` as Gaussian spatial escape;
3. plus the reverse-Girsanov bridge to transfer the resulting affine geometry to the nonlinear path law when the Gaussian residual action is very small.

Status: **SOURCE-TIME AFFINE STRETCH IS HALF-COMPENSATED BY TRANSVERSE HEAT IN BALANCED GEOMETRY / LARGE-Q TIMES CARRY A FIXED FRACTION OF THE TERMINAL SOURCE / REMAINING ESCAPES = BIAxIAL ANISOTROPY, GAUSSIAN SPATIAL ESCAPE, OR RESIDUAL VELOCITY/DERIVATIVE RESERVOIR.**
