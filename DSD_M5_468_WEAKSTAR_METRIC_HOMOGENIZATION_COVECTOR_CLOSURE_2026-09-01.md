# DSD M5-468 — Weak-* metric homogenization closes in the covector formulation

Date: 2026-09-01

Status: **RAPID PARABOLIC ZOOM-OUT OSCILLATION OF THE TIME-DEPENDENT METRIC DOES NOT DESTROY THE ALGEBRAIC PDE CLASS AT THE WEAK-EQUATION LEVEL / IF THE COVECTORS ARE STRONGLY COMPACT LOCALLY, WEAK-* COEFFICIENT CONVERGENCE IS ENOUGH TO PASS BOTH THE NONLINEAR TRANSPORT AND DIFFUSION TERMS, PRODUCING AN EFFECTIVE SYMMETRIC UNIFORMLY ELLIPTIC METRIC `G_BAR` / THE EFFECTIVE DETERMINANT SATISFIES `det G_BAR >= 1` / THE REMAINING ZOOM-OUT GAP IS STRONG COVECTOR COMPACTNESS WITHOUT A COEFFICIENT-DERIVATIVE BOUND / GLOBAL REGULARITY REMAINS UNPROVED.**

Consider a parabolically zoomed metric sequence on a fixed time interval:

\[
G_k(t)=G(\lambda_k^2t),
\qquad
\lambda_k\to\infty.
\]

Uniform ellipticity gives, after a subsequence,

\[
\boxed{
G_k\stackrel{*}{\rightharpoonup}\bar G
\quad\text{in }L^\infty_t.
}
\]

Let `m_k` solve the covector equation in the pressure-absorbed form

\[
\partial_t m_k
+\nabla\cdot(w_k\otimes m_k)
=-\nabla p_k
+\nabla\cdot(G_k\nabla m_k),
\]

with

\[
w_k=G_km_k,
\qquad
\nabla\cdot w_k=0.
\]

Assume for this note that

\[
\boxed{
m_k\to m
\quad\text{strongly in }L^2_{loc}(space\text{-}time).
}
\]

## 1. Constitutive/transport limit

Since

\[
m_k\otimes m_k\to m\otimes m
\]

strongly in local `L1`, multiplication by the time-only weak-* coefficient gives

\[
\boxed{
G_k(m_k\otimes m_k)
\rightharpoonup
\bar G(m\otimes m)
}
\]

distributionally.

Equivalently

\[
w_k\otimes m_k
\rightharpoonup
(\bar Gm)\otimes m.
\]

Define

\[
\boxed{w:=\bar Gm.}
\]

The divergence constraint passes to

\[
\boxed{\nabla\cdot w=\nabla\cdot(\bar Gm)=0.}
\]

## 2. Diffusion limit without weak-times-weak gradients

For a smooth compact test field `phi`, spatial constancy of `G_k` gives

\[
\int G_k\nabla m_k:\nabla\phi
=-\int m_k\cdot(G_k:D^2\phi).
\]

The first factor converges strongly and the coefficient converges weak-* in time. Therefore

\[
\boxed{
\int G_k\nabla m_k:\nabla\phi
\to
\int \bar G\nabla m:\nabla\phi.
}
\]

Thus no product of a weak coefficient with a weak solution gradient needs to be identified.

## 3. Effective weak equation

Passing to the limit against divergence-free test fields gives

\[
\boxed{
\partial_t m
+\nabla\cdot((\bar Gm)\otimes m)
=-\nabla p
+\nabla\cdot(\bar G\nabla m),
}
\]

\[
\boxed{
\nabla\cdot(\bar Gm)=0.
}
\]

Since `bar G` is symmetric positive definite, one may again set

\[
C_{eff}:=\bar G^{-1}
\]

and recover the same metric covector class.

## 4. Effective determinant is not below one

At almost every time, weak-* limits can be represented through the associated Young-measure barycenter of the matrices `G_k`. The function

\[
G\mapsto\log\det G
\]

is concave on positive definite matrices. Since every original metric satisfies

\[
\det G_k=1,
\]

Jensen gives

\[
\log\det\bar G
\ge
\overline{\log\det G_k}=0.
\]

Hence

\[
\boxed{\det\bar G\ge1.}
\]

Rapid temporal oscillation therefore cannot produce an effective metric with smaller determinant-volume diffusion than the determinant-one inputs.

## 5. Exact remaining gap

M5-467's coefficient-dilation problem is now reduced from `coefficient convergence` to one concrete estimate:

\[
\boxed{
\text{obtain strong local compactness of the zoomed covectors }m_k
\text{ with constants independent of }\|G_k'\|.
}
\]

The M5-464 energy estimate is insufficient for this purpose because its metric-energy Gronwall constant uses coefficient time variation. A derivative-free compactness/energy mechanism or a compensated argument is still required.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]