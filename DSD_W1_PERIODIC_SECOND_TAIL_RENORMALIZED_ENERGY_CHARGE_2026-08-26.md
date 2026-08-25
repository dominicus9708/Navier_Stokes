# DSD W1 Periodic Second Tail: Renormalized Energy Charge

Date: 2026-08-26

Status: **CANONICAL SECOND-TAIL COEFFICIENT CONVERTED INTO AN EXPLICIT R^-1 RENORMALIZED SHELL-ENERGY ASYMPTOTIC / THE FORMER O(R^-1/3) INTERFACE BOUND IS SHARPENED TO A CANONICAL DUAL-PAIRING COEFFICIENT / SIGN NOT YET CONTROLLED / GLOBAL REGULARITY UNPROVED.**

## 1. Input

On the H2-coherent periodic W1 branch, use one canonical same-phase far cell of physical radius scale `R` and write

\[
w_R=F_\infty+e_R.
\]

The preceding second-tail theorem gives

\[
\boxed{
R^2e_R
\to
-\mathcal N[F_\infty]
\quad\text{in }H^{-1}(cell).
}
\]

Also

\[
F_\infty\in H^1(cell)
\]

and the improved strong estimate gives

\[
\|e_R\|_2=O(R^{-4/3}).
\]

## 2. Define the second-tail energy charge

The natural dual pairing is

\[
\boxed{
\mathfrak A_F
:=
\langle
F_\infty,
\mathcal N[F_\infty]
\rangle_{H^1,H^{-1}}.
}
\]

Because `F_infty` is fixed on a canonical phase cell and `N[F_infty]` is its projected viscous/nonlinear residual, `A_F` is a finite scalar determined entirely by the leading critical trace.

No sign is assumed.

## 3. Fixed-cell cross term

The H^-1 asymptotic and `F_infty in H1` give

\[
\begin{aligned}
\langle F_\infty,e_R\rangle
&=
-R^{-2}
\langle F_\infty,\mathcal N[F_\infty]\rangle
+o(R^{-2})\\
&=
\boxed{-R^{-2}\mathfrak A_F+o(R^{-2}).}
\end{aligned}
\]

The square remainder satisfies

\[
\boxed{
\|e_R\|_2^2
=O(R^{-8/3})
=o(R^{-2}).
}
\]

Thus the cross term is the leading renormalized L2 contribution.

## 4. Return to the physical Leray annulus

On the radius-R annular cell,

\[
T(Y)=R^{-1}F_\infty(z),
\qquad
U(Y)-T(Y)=R^{-1}e_R(z),
\qquad
Y=Rz,
\]

and

\[
dY=R^3dz.
\]

Therefore

\[
\begin{aligned}
\int_{C_R}
(|U|^2-|T|^2)dY
&=
R
\left[
2\langle F_\infty,e_R\rangle
+\|e_R\|_2^2
\right]\\
&=
\boxed{
-\frac{2\mathfrak A_F}{R}
+o(R^{-1}).
}
\end{aligned}
\]

This improves the previous coarse estimate `O(R^-1/3)` to a canonical asymptotic coefficient.

## 5. Consequence for the similarity-radial boundary term

The local Leray L2 ledger contains

\[
-\frac r4\int_{|Y|=r}|U|^2dS.
\]

Subtract the canonical-tail term and average in logarithmic radius over one DSS cell `[R,lambda R]` with `L=log lambda`:

\[
\begin{aligned}
&\frac1L
\int_R^{\lambda R}
\frac{dr}{r}
\left[
\frac r4
\int_{|Y|=r}
(|U|^2-|T|^2)dS
\right]\\
&=
\frac1{4L}
\int_{C_R}(|U|^2-|T|^2)dY.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal A_{log,R}
\left[
\frac r4
\int_{|Y|=r}(|U|^2-|T|^2)dS
\right]
=
-\frac{\mathfrak A_F}{2LR}
+o(R^{-1}).
}
\]

Thus the renormalized infinity dilation flux not only vanishes; its first surviving coefficient is completely determined by the canonical second-tail charge.

## 6. Renormalized energy approach to its finite limit

Let the canonical geometric radii be

\[
R_k=R_0\lambda^k.
\]

The shell asymptotic gives

\[
\Delta\mathcal E_{ren,k}
:=
\int_{C_{R_k}}(|U|^2-|T|^2)dY
=
-2\mathfrak A_F R_k^{-1}+o(R_k^{-1}).
\]

Since

\[
\sum_{j=k}^\infty R_j^{-1}
=
\frac{R_k^{-1}}{1-\lambda^{-1}},
\]

the finite renormalized exterior-energy limit satisfies

\[
\boxed{
\mathcal E_{ren,\infty}
-\mathcal E_{ren}(R_k)
=
-\frac{2\mathfrak A_F}{1-\lambda^{-1}}R_k^{-1}
+o(R_k^{-1}).
}
\]

Thus `A_F` is the leading rate at which the actual periodic orbit approaches the finite renormalized energy of its canonical critical memory.

## 7. Relation to the tail residual action

The fixed-cell operator `N[F_infty]` is precisely the coefficient of the physical `R^-3` projected viscous/nonlinear residual of the leading tail.  Pairing that residual with the leading `R^-1` tail over one radius-R cell has scale `R^-1` and coefficient `A_F`:

\[
\boxed{
\langle T,\mathcal R_T\rangle_{C_R}
=
\frac{\mathfrak A_F}{R}
}
\]

up to the fixed-cell convention used in the projected operator.

The second-tail relation

\[
G=-\mathcal N[F_\infty]
\]

therefore implies the structural coefficient relation

\[
\boxed{
\Delta\mathcal E_{ren}(C_R)
\sim
-2\langle T,\mathcal R_T\rangle_{C_R}.
}
\]

This is the energy imprint of the nonresonant response: the leading residual generates the first correction, and the cross energy with that correction records the same scalar charge.

## 8. New scalar split

The H2-coherent periodic branch can now be split by

\[
\boxed{
\mathfrak A_F=0
\quad\lor\quad
\mathfrak A_F\ne0.
}
\]

If `A_F=0`, the first renormalized energy correction vanishes and the exterior energy approaches its limit faster than `R^-1` at this order.

If `A_F!=0`, the sign of `A_F` fixes the direction of the `R^-1` approach to the renormalized limit.

Neither case is a contradiction by itself.  In particular, no sign-definite formula for `A_F` has yet been proved because the fixed log-cell viscous/nonlinear residual contains boundary/scale-transfer contributions.

The next meaningful target is therefore an exact identity or sign decomposition for

\[
\boxed{
\mathfrak A_F
=
\langle F_\infty,\mathcal N[F_\infty]\rangle.
}
\]

## 9. DSD audit

This note does not identify `A_F` with pressure work, material turnover, or viscous dissipation alone.  It is a projected full residual charge of the leading critical tail.

The distinction between a vanishing infinity flux and a nonzero finite asymptotic coefficient is maintained.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
