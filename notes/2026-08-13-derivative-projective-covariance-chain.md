# Derivative-order projective covariance chain

Date: 2026-08-13

Status: **DERIVED HIGHER-DERIVATIVE MATRIX CHAIN / OPEN UNIFORM-k CLOSURE**.

This note extends the global vorticity projective-dispersion budget from derivative order `k=0` to every spatial derivative order.

The purpose is to connect three previously separate pieces of the active route:

1. vorticity-axis covariance;
2. palinstrophy / higher-derivative activation;
3. the factorially normalized derivative-channel Cauchy convolution.

No global regularity result is claimed.

## 1. Ordered derivative words

For exact nesting under one additional gradient, use ordered derivative words

\[
I=(i_1,\ldots,i_k)\in\{1,2,3\}^k.
\]

Define

\[
\partial_I
=\partial_{i_1}\cdots\partial_{i_k},
\qquad
w_I=\partial_I\omega.
\]

For `k=0`, the empty word gives

\[
w_\varnothing=\omega.
\]

Mixed derivatives commute for smooth solutions, so the ordered-word norm counts ordinary multi-index derivatives with their multinomial multiplicities. This is deliberate: it makes the viscous derivative chain exact.

## 2. Derivative covariance tensors

Define

\[
\boxed{
N_k
=\sum_{I\in\{1,2,3\}^k}
\int w_I\otimes w_I\,dx,
}
\]

\[
\boxed{
E_k=\operatorname{tr}N_k
=\sum_I\|w_I\|_2^2,
}
\]

and, when `E_k>0`,

\[
\boxed{
C_k=\frac{N_k}{E_k},
\qquad
J_k=1-\operatorname{tr}(C_k^2).
}
\]

Thus

\[
C_k\succeq0,
\qquad
\operatorname{tr}C_k=1,
\qquad
0\le J_k\le\frac23.
\]

At `k=0`, these reduce to the vorticity covariance and projective dispersion already used in the global axis gate.

At `k=1`,

\[
N_1
=\sum_{j=1}^3
\int(\partial_j\omega)\otimes(\partial_j\omega)dx,
\]

so

\[
C_1=C_\nabla
\]

is exactly the normalized gradient covariance introduced in the viscous mixing branch.

## 3. Differentiated vorticity equation

The vorticity equation is

\[
\partial_t\omega+(u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega.
\]

For an ordered word `I`, define the nonlinear differentiated forcing

\[
\boxed{
F_I
=\partial_I(S\omega)
-[\partial_I,u\cdot\nabla]\omega.
}
\]

Then

\[
\boxed{
\partial_t w_I
+(u\cdot\nabla)w_I
=F_I+\nu\Delta w_I.
}
\]

The transport term makes no contribution to the whole-space second-moment tensor after integration because `div u=0`.

## 4. Exact derivative-tensor evolution

Define

\[
\boxed{
A_k
=\sum_I\int F_I\otimes w_I\,dx.
}
\]

Integration by parts gives

\[
\sum_I\int
\left[
(\Delta w_I)\otimes w_I
+w_I\otimes(\Delta w_I)
\right]dx
=-2N_{k+1}.
\]

Therefore

\[
\boxed{
\dot N_k
=A_k+A_k^T-2\nu N_{k+1}.
}
\]

Taking the trace,

\[
\boxed{
\dot E_k
=2Q_k-2\nu E_{k+1},
\qquad
Q_k=\operatorname{tr}A_k.
}
\]

Thus the next derivative order appears **exactly** as the dissipative covariance tensor of the current order.

## 5. Normalized derivative covariance dynamics

Define

\[
B_k=A_k/E_k,
\qquad
q_k=Q_k/E_k,
\qquad
r_k=E_{k+1}/E_k.
\]

Then

\[
\boxed{
\dot C_k
=B_k+B_k^T
-2\nu r_k C_{k+1}
-2(q_k-\nu r_k)C_k.
}
\]

The scalar `r_k` has dimensions of inverse length squared and is the derivative-order analogue of the palinstrophy/enstrophy ratio.

## 6. Exact projective-dispersion chain

Since

\[
J_k=1-\operatorname{tr}(C_k^2),
\]

we obtain

\[
\boxed{
\frac14\dot J_k
=
\underbrace{
q_k\operatorname{tr}(C_k^2)
-\operatorname{tr}(C_kB_k)
}_{\mathcal M_{N,k}}
+
\nu r_k
\underbrace{
\left[
\operatorname{tr}(C_kC_{k+1})
-\operatorname{tr}(C_k^2)
\right]
}_{\mathcal A_{k\to k+1}}.
}
\]

Thus every derivative order has two directional-mixing mechanisms:

1. `M_N,k`: nonlinear derivative forcing;
2. `nu r_k A_{k->k+1}`: dissipative coupling to the next derivative covariance.

At `k=0`,

\[
r_0=E_1/E_0=P/E,
\qquad
C_1=C_\nabla,
\]

so this formula reproduces the previous global projective-dispersion budget exactly.

## 7. Covariance-mismatch form of the viscous chain

Define

\[
\boxed{
\Delta_k
=\|C_{k+1}-C_k\|_F.
}
\]

Then

\[
\mathcal A_{k\to k+1}
=
\operatorname{tr}[C_k(C_{k+1}-C_k)],
\]

and therefore

\[
\boxed{
|\mathcal A_{k\to k+1}|
\le
\sqrt{1-J_k}\,\Delta_k.
}
\]

Hence

\[
\boxed{
|\text{viscous directional mixing at order }k|
\le
\nu r_k\sqrt{1-J_k}\,\Delta_k.
}
\]

Large positive viscous mixing at one derivative level therefore requires both

- a large derivative ratio `r_k=E_{k+1}/E_k`, and
- a mismatch between the directional covariance of derivative orders `k` and `k+1`.

If

\[
C_{k+1}=C_k,
\]

viscosity changes the magnitude `E_k` but not the normalized directional covariance `C_k` to first order.

## 8. Generic nonlinear-mixing bound

The strain-mixing proof at `k=0` uses only the fact that `A_k` pairs a forcing family `F_I` with the current derivative family `w_I`.

Define

\[
\boxed{
L_k
=
\left(
\frac{
\sum_I\|F_I\|_2^2
}{E_k}
\right)^{1/2}.
}
\]

Repeating the covariance-eigenbasis Cauchy--Schwarz argument yields

\[
\boxed{
|\mathcal M_{N,k}|
\le
\sqrt{J_k(1-J_k)}\,L_k.
}
\]

Therefore

\[
\boxed{
\dot J_k
\le
4\sqrt{1-J_k}
\left[
\sqrt{J_k}L_k
+\nu r_k\Delta_k
\right].
}
\]

This is the derivative-order analogue of the S/V mixing closure at `k=0`.

## 9. Connection to the factorial derivative convolution

The forcing

\[
F_I
=\partial_I(S\omega)-[\partial_I,u\cdot\nabla]\omega
\]

contains the near-scale Leibniz couplings among derivative orders.

The existing factorial normalization of derivative channels removes the binomial combinatorics and reduces their aggregate bounds to Cauchy convolution form,

\[
N_k^{\rm nl}
\lesssim
\sum_{m=0}^k A_mB_{k-m}.
\]

Therefore the two-index active route can now be read as

\[
\boxed{
\text{physical scale }j
\times
\text{derivative order }k
\times
\text{directional covariance }C_k.
}
\]

The off-diagonal mechanisms are:

1. near-scale physical cascade in `j`;
2. Cauchy convolution across derivative orders;
3. covariance mismatch `C_{k+1}-C_k` across neighboring derivative levels.

## 10. Residual-class consequence

The old V-branch

\[
\nu(P/E)\Delta_\nu
\]

is not an isolated palinstrophy obstruction. It is the first element of the chain

\[
\boxed{
\nu r_k\Delta_k,
\qquad
k=0,1,2,\ldots
}
\]

A residual singular cascade that uses viscosity to regenerate directional dispersion must therefore keep activating derivative-scale covariance mismatch as the cascade proceeds.

Conversely, if the covariance chain stabilizes,

\[
\Delta_k\to0,
\]

then viscous directional regeneration weakens and the burden returns to the nonlinear derivative-forcing channel `L_k`, which is already subject to the derivative convolution / sparseness / analyticity track.

This gives a clean new target:

\[
\boxed{
\text{either derivative covariance stabilizes}
\quad\text{or}
\quad
\sum_k\text{ must sustain large }r_k\Delta_k.
}
\]

No uniform-in-`k` summability or contradiction has yet been proved.

Status: **OPEN UNIFORM DERIVATIVE-COVARIANCE CLOSURE**.
