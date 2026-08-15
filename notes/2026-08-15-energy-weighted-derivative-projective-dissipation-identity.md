# Energy-weighted derivative projective dissipation identity

Date: 2026-08-15

Status: **EXACT ENERGY-WEIGHTED DERIVATIVE-COVARIANCE IDENTITY. AFTER MULTIPLYING PROJECTIVE DISPERSION BY DERIVATIVE ENERGY, THE VISCOUS DIRECTIONAL-MIXING TERM BECOMES PURELY DISSIPATIVE: IT CHARGES BOTH NEXT-ORDER PROJECTIVE DEFECT AND NEIGHBORING COVARIANCE MISMATCH. HIGH-DERIVATIVE PROJECTIVE MIXING IS THEREFORE NOT AN INDEPENDENT POSITIVE VISCOUS SOURCE. GLOBAL REGULARITY NOT PROVED.**

## 1. Derivative covariance chain

For ordered derivative words `I` of length `k`, let

\[
w_I=\partial_I\omega,
\qquad
E_k=\sum_I\|w_I\|_2^2,
\]

and define

\[
N_k=\sum_I\int w_I\otimes w_I\,dx,
\qquad
C_k=N_k/E_k
\]

when `E_k>0`.

The normalized projective dispersion is

\[
\boxed{
J_k=1-\operatorname{tr}(C_k^2).
}
\]

Let

\[
F_I=\partial_I(S\omega)-[\partial_I,u\cdot\nabla]\omega,
\]

\[
A_k=\sum_I\int F_I\otimes w_I\,dx,
\qquad
Q_k=\operatorname{tr}A_k,
\]

\[
B_k=A_k/E_k,
\qquad
q_k=Q_k/E_k,
\qquad
r_k=E_{k+1}/E_k.
\]

The exact derivative-energy and covariance equations are

\[
\boxed{
\dot E_k=2Q_k-2\nu E_{k+1},
}
\]

and

\[
\boxed{
\frac14\dot J_k
=\mathcal M_{N,k}
+\nu r_k\mathcal A_k,
}
\]

where

\[
\mathcal M_{N,k}
=q_k\operatorname{tr}(C_k^2)-\operatorname{tr}(C_kB_k),
\]

\[
\boxed{
\mathcal A_k
=\operatorname{tr}(C_kC_{k+1})-\operatorname{tr}(C_k^2).
}
\]

## 2. Energy-weighted projective defect

Define

\[
\boxed{
D_k:=E_kJ_k.
}
\]

Differentiate:

\[
\dot D_k
=J_k\dot E_k+E_k\dot J_k.
\]

Substituting the exact equations gives

\[
\dot D_k
=2J_kQ_k+4E_k\mathcal M_{N,k}
+2\nu E_{k+1}[-J_k+2\mathcal A_k].
\]

The nonlinear part will be denoted

\[
\boxed{
\mathcal N_k
:=2J_kQ_k+4E_k\mathcal M_{N,k}.
}
\]

## 3. Exact viscous completion of squares

Using

\[
J_k=1-\operatorname{tr}(C_k^2),
\]

we have

\[
\begin{aligned}
-J_k+2\mathcal A_k
&=-1+\operatorname{tr}(C_k^2)
+2\operatorname{tr}(C_kC_{k+1})
-2\operatorname{tr}(C_k^2)\\
&=-1-\operatorname{tr}(C_k^2)
+2\operatorname{tr}(C_kC_{k+1}).
\end{aligned}
\]

On the other hand

\[
J_{k+1}
=1-\operatorname{tr}(C_{k+1}^2)
\]

and

\[
\|C_{k+1}-C_k\|_F^2
=
\operatorname{tr}(C_{k+1}^2)
+\operatorname{tr}(C_k^2)
-2\operatorname{tr}(C_kC_{k+1}).
\]

Therefore

\[
\boxed{
-J_k+2\mathcal A_k
=-J_{k+1}
-\|C_{k+1}-C_k\|_F^2.
}
\]

Hence the exact energy-weighted projective equation is

\[
\boxed{
\dot D_k
+2\nu E_{k+1}
\left[
J_{k+1}
+\|C_{k+1}-C_k\|_F^2
\right]
=\mathcal N_k.
}
\]

This is the central identity.

## 4. Consequence for the old positive-V branch

At the normalized-covariance level, viscosity could have either sign in `dot J_k`, because preferential damping may increase or decrease directional dispersion.

After multiplying by the actual derivative energy `E_k`, this ambiguity disappears completely:

\[
\boxed{
\text{viscosity cannot create }D_k=E_kJ_k.
}
\]

Instead it dissipates two nonnegative quantities:

1. next-order projective defect
   \[
   E_{k+1}J_{k+1};
   \]
2. neighboring derivative-covariance mismatch
   \[
   E_{k+1}\|C_{k+1}-C_k\|_F^2.
   \]

Thus the previously retained positive viscous projective-mixing lane is a normalization effect. In the energy-weighted ledger it is not an independent positive source.

## 5. Nonlinear source bound

Let

\[
\mathcal F_k
:=
\left(
\sum_I\|F_I\|_2^2
\right)^{1/2}.
\]

Then

\[
|Q_k|
\le
\sqrt{E_k}\,\mathcal F_k.
\]

The covariance-mixing estimate gives

\[
|\mathcal M_{N,k}|
\le
\sqrt{J_k(1-J_k)}
\frac{\mathcal F_k}{\sqrt{E_k}}.
\]

Therefore

\[
\begin{aligned}
|\mathcal N_k|
&\le
2J_k\sqrt{E_k}\mathcal F_k
+4\sqrt{E_k}\sqrt{J_k(1-J_k)}\mathcal F_k\\
&\le
6\sqrt{E_kJ_k}\,\mathcal F_k.
\end{aligned}
\]

Thus

\[
\boxed{
|\mathcal N_k|
\le6\sqrt{D_k}\,\mathcal F_k.
}
\]

No reciprocal derivative-energy factor remains.

## 6. Factorial weighted sum at a fixed radius

Fix an analytic/factorial radius `ell>0` and define

\[
a_k(\ell)=\frac{\ell^{2k}}{(k!)^2}.
\]

Set

\[
\boxed{
\mathfrak D_\ell
=\sum_{k\ge0}a_kD_k
=\sum_{k\ge0}
\frac{\ell^{2k}E_k}{(k!)^2}J_k.
}
\]

Define also the factorial forcing amplitudes

\[
\boxed{
F_k^\#
=\frac{\ell^k}{k!}\mathcal F_k.
}
\]

Multiplying the exact identity by `a_k` and summing gives

\[
\begin{aligned}
\dot{\mathfrak D}_\ell
&+2\nu\sum_{k\ge0}a_kE_{k+1}J_{k+1}\\
&+2\nu\sum_{k\ge0}a_kE_{k+1}
\|C_{k+1}-C_k\|_F^2
\le
6\sum_{k\ge0}
\sqrt{a_kD_k}\,F_k^\#.
\end{aligned}
\]

The shifted first viscous sum is exact:

\[
\begin{aligned}
\sum_{k\ge0}a_kE_{k+1}J_{k+1}
&=
\sum_{j\ge1}
\frac{\ell^{2(j-1)}}{((j-1)!)^2}D_j\\
&=
\boxed{
\frac1{\ell^2}
\sum_{j\ge1}j^2a_jD_j.
}
\end{aligned}
\]

Hence

\[
\boxed{
\begin{aligned}
\dot{\mathfrak D}_\ell
&+\frac{2\nu}{\ell^2}
\sum_{j\ge1}j^2a_jD_j\\
&+2\nu\sum_{k\ge0}a_kE_{k+1}
\|C_{k+1}-C_k\|_F^2\\
&\le
6\mathfrak D_\ell^{1/2}
\left(
\sum_{k\ge0}(F_k^\#)^2
\right)^{1/2}.
\end{aligned}
}
\]

This is a common factorial S/V ledger. The entire V contribution is coercive.

## 7. Nonincreasing dynamic radius

Let now `ell=ell(t)>0`. Since

\[
\dot a_k
=2k\frac{\dot\ell}{\ell}a_k,
\]

a nonincreasing radius `dot ell <= 0` contributes the additional nonnegative damping term

\[
\boxed{
2\frac{-\dot\ell}{\ell}
\sum_{k\ge1}k a_kD_k.
}
\]

Thus

\[
\boxed{
\begin{aligned}
\dot{\mathfrak D}_{\ell(t)}
&+2\frac{-\dot\ell}{\ell}
\sum_{k\ge1}k a_kD_k\\
&+\frac{2\nu}{\ell^2}
\sum_{j\ge1}j^2a_jD_j\\
&+2\nu\sum_{k\ge0}a_kE_{k+1}
\|C_{k+1}-C_k\|_F^2\\
&\le
6\mathfrak D_{\ell(t)}^{1/2}
\left(
\sum_{k\ge0}(F_k^\#)^2
\right)^{1/2}.
\end{aligned}
}
\]

A shrinking analytic radius therefore helps rather than hurts the projective-defect budget; the difficulty is transferred into the size of the factorial nonlinear forcing itself.

## 8. Combination with the factorial forcing majorant

The existing factorial forcing calculation gives schematically

\[
\mathcal F(z)
\lesssim
\mathcal G(z)\mathcal W(z)
+\mathcal U(z)\partial_z\mathcal W(z).
\]

In coefficient norms, Young convolution gives the schematic estimate

\[
\boxed{
\|F^\#\|_{\ell^2_k}
\lesssim
\|G\|_{\ell^1_k}\|W\|_{\ell^2_k}
+
\|U\|_{\ell^1_k}\|kW_k\|_{\ell^2_k}.
}
\]

Thus the remaining obstruction is no longer a positive viscous derivative-mixing cycle. It is one of:

1. bounded factorial forcing/analytic radius — then the coercive projective ledger is available;
2. collapse of the factorial derivative radius / explosion of the derivative generator;
3. failure of the `L^infinity` coefficient controls entering `G` or `U`, which is itself a high-derivative concentration branch.

## 9. Revised high-Hermite interpretation

Combined with the exact multiscale total-covariance source recursion:

- a high-Hermite parent source descends to child sources or becomes a positive between-scale variance increment;
- repeated descent reaches the low-Hermite terminus or endpoint derivative concentration;
- the low-Hermite material-center mean lane is closed on the stated bounded-affine hypotheses;
- between-scale increments have fixed-time scale packing;
- derivative-order viscosity is purely dissipative in the energy-weighted projective functional.

Therefore the surviving high-Hermite branch has been reduced to

\[
\boxed{
\text{scale-time regeneration of between-scale variance}
\quad\lor\quad
\text{factorial derivative-radius collapse / endpoint derivative concentration}.
}
\]

There is no independent positive viscous projective-cascade lane.

Status: **ENERGY-WEIGHTED V-BRANCH CLOSED EXACTLY / HIGH-HERMITE SURVIVOR REDUCED TO SCALE-TIME VARIANCE REGENERATION OR DERIVATIVE-RADIUS COLLAPSE / GLOBAL REGULARITY NOT PROVED.**
