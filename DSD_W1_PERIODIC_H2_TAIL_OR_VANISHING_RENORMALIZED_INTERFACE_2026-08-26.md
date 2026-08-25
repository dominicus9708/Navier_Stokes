# DSD W1 Periodic Tail: H2 Escape or Vanishing Renormalized Interface

Date: 2026-08-26

Status: **PERIODIC CORE-TAIL INTERFACE SPLIT SHARPENED / IF CRITICAL H2 TAIL ESCALATES IT IS THE EXISTING H2_TAIL BRANCH / IF CRITICAL H2 STAYS BOUNDED, THE CANONICAL TAIL DEFECT IMPROVES FROM L2 RATE R^-1 TO R^-4/3 ON FIXED CELLS / RENORMALIZED L2 RADIAL INTERFACE VANISHES / EXTERIOR ENERGY AND GRADIENT-ENERGY DIFFERENCES ARE SUMMABLE ACROSS DSS CELLS / NO CONTRADICTION YET / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The periodic W1 canonical-tail note constructs

\[
U(Y,s)=T(Y,s)+R(Y,s)
\]

on the far field, where

\[
T(Y,s)=|Y|^{-1}\Phi\!\left(\widehat Y,\log|Y|-\frac s2\right)
\]

is the canonical log-periodic critical tail and the fixed-cell one-period defect obeys

\[
\|\delta_\rho\|_{H^{-1}}
\le Ce^{-2\rho}.
\]

Using only a uniform fixed-cell `H1` bound previously gave

\[
\|\delta_\rho\|_2\lesssim e^{-\rho},
\]

which leaves an order-one possible correction to the order-R dilation-interface energy pairing.

The present note determines exactly what happens if one includes the already existing critical `H2_tail` frontier.

## 2. Critical H2 quantity on a far annulus

On an enlarged annulus `A_R^*`, define

\[
\boxed{
\mathfrak E_2(R,s)
:=
R^3\int_{A_R^*}|\nabla^2U(Y,s)|^2dY.
}
\]

Under the critical rescaling

\[
f_R(z,s):=R U(Rz,s),
\]

this is equivalent, up to fixed-annulus constants, to

\[
\|\nabla_z^2 f_R\|_{L^2(A_1^*)}^2.
\]

Hence the exact dichotomy is

\[
\boxed{
\sup_{R,s}\mathfrak E_2(R,s)<\infty
\quad\lor\quad
H_{2,crit}^{tail}.
}
\]

The second alternative is precisely the existing remote derivative-subscale H branch; it is not renamed or silently excluded here.

## 3. H2-coherent branch gives a uniform fixed-cell H2 bound

Assume

\[
\sup_{R,s}\mathfrak E_2(R,s)\le H_{2,*}<\infty.
\]

The W1 Type-I/Campanato/H1 bounds control the lower fixed-cell norms, so the same-phase cell profiles `w(rho)` satisfy

\[
\boxed{
\|w(\rho,\cdot,s)\|_{H^2(cell)}\le C_{2,*}
}
\]

uniformly for large `rho` and periodic time `s`.

Therefore the one-period difference

\[
\delta_\rho=w(\rho+L)-w(\rho)
\]

also satisfies

\[
\|\delta_\rho\|_{H^2(cell)}\le2C_{2,*}.
\]

## 4. Improved H^-1--H2 interpolation

On a fixed smooth cell, real interpolation gives

\[
\|f\|_{L^2}
\le
C
\|f\|_{H^{-1}}^{2/3}
\|f\|_{H^2}^{1/3}.
\]

Using

\[
\|\delta_\rho\|_{H^{-1}}\le Ce^{-2\rho}
\]

and the uniform H2 ceiling yields

\[
\boxed{
\|\delta_\rho\|_{L^2(cell)}
\le
C e^{-4\rho/3}.
}
\]

Along same-phase cells

\[
R_k=e^{\rho_k}=R_0\lambda^k,
\]

the geometric telescoping series gives

\[
\boxed{
\|w(\rho_k)-F_\infty\|_{L^2(cell)}
\le
C R_k^{-4/3}.
}
\]

This strictly improves the previous `R^-1` fixed-cell L2 rate.

## 5. Physical annular L2 remainder

On the kth physical annular cell `C_k` of radius scale `R_k`,

\[
R(Y,s):=U(Y,s)-T(Y,s)
=R_k^{-1}\bigl(w-F_\infty\bigr)
\]

after identification with the fixed cell.

Critical scaling gives

\[
\|R\|_{L^2(C_k)}^2
=
R_k
\|w-F_\infty\|_{L^2(cell)}^2.
\]

Hence

\[
\boxed{
\|U-T\|_{L^2(C_k)}^2
\le
C R_k^{-5/3}.
}
\]

Equivalently,

\[
\boxed{
\|U-T\|_{L^2(C_k)}
\le
C R_k^{-5/6}.
}
\]

The canonical tail itself satisfies

\[
\|T\|_{L^2(C_k)}^2\asymp R_k
\]

on a nontrivial phase cell, and in any case

\[
\|T\|_{L^2(C_k)}\le C R_k^{1/2}.
\]

Therefore

\[
\boxed{
\left|\int_{C_k}T\cdot(U-T)dY\right|
\le
C R_k^{-1/3}.
}
\]

## 6. Renormalized shell energy tends to zero

Expand

\[
|U|^2-|T|^2
=2T\cdot(U-T)+|U-T|^2.
\]

The previous estimates give

\[
\boxed{
\left|
\int_{C_k}(|U|^2-|T|^2)dY
\right|
\le
C R_k^{-1/3}+C R_k^{-5/3}
\le C R_k^{-1/3}.
}
\]

Thus

\[
\boxed{
\int_{C_k}(|U|^2-|T|^2)dY
\to0.
}
\]

More strongly, because `R_k` grows geometrically,

\[
\boxed{
\sum_{k\ge k_0}
\left|
\int_{C_k}(|U|^2-|T|^2)dY
\right|
<\infty.
}
\]

Therefore the exterior renormalized energy

\[
\boxed{
\mathcal E_{ren}(R)
:=
\int_{R_0<|Y|<R}
(|U|^2-|T|^2)dY
}
\]

has a finite limit along the canonical geometric radii:

\[
\boxed{
\mathcal E_{ren}(R_k)\to\mathcal E_{ren,\infty}(s).
}
\]

Periodic smoothness makes this limit periodic in `s`.

## 7. Vanishing renormalized similarity-radial flux in log-radius mean

The local Leray L2 identity contains the dilation boundary term

\[
-\frac r4\int_{|Y|=r}|U|^2dS.
\]

Subtract the corresponding canonical-tail term.  Its logarithmic radial average on a cell is

\[
\begin{aligned}
&\frac1L
\int_{R_k}^{\lambda R_k}
\frac{dr}{r}
\left[
\frac r4\int_{|Y|=r}(|U|^2-|T|^2)dS
\right]\\
&=\frac1{4L}
\int_{C_k}(|U|^2-|T|^2)dY.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal A_{log,k}
\left[
\frac r4\int_{|Y|=r}(|U|^2-|T|^2)dS
\right]
=O(R_k^{-1/3})\to0.
}
\]

Thus, after subtracting the universal passive dilation flux of the canonical `1/r` memory, there is **no nonzero infinity-scale L2 dilation payer** left on the H2-coherent periodic branch.

## 8. Other L2 boundary mechanisms vanish already at critical scale

The remaining local L2 boundary terms have lower critical order.

### Advective boundary term

Using log averaging and the bounded critical cubic shell mass,

\[
\begin{aligned}
\mathcal A_{log,k}
\left[
\frac12\int_{|Y|=r}|U|^2U\cdot n\,dS
\right]
&\lesssim
\frac1{R_k}
\int_{C_k}|U|^3dY\\
&=O(R_k^{-1}).
\end{aligned}
\]

### Viscous boundary term

By coarea and Cauchy-Schwarz,

\[
\mathcal A_{log,k}
\left[
\nu\int_{|Y|=r}\partial_nU\cdot U\,dS
\right]
\lesssim
\frac\nu{R_k}
\|\nabla U\|_{L^2(C_k)}
\|U\|_{L^2(C_k)}.
\]

The W1 shell bounds give

\[
\|\nabla U\|_2=O(R_k^{-1/2}),
\qquad
\|U\|_2=O(R_k^{1/2}),
\]

so

\[
\boxed{\text{viscous boundary average}=O(R_k^{-1}).}
\]

### Pressure boundary term

After the already repaired global pressure gauge,

\[
\|P\|_{L^2(C_k)}=O(R_k^{-1/2}).
\]

Thus

\[
\mathcal A_{log,k}
\left[
\int_{|Y|=r}P U\cdot n\,dS
\right]
\lesssim
\frac1{R_k}
\|P\|_2\|U\|_2
=O(R_k^{-1}).
\]

Hence every non-dilation boundary mechanism vanishes in the far log-radius mean.

## 9. Gradient-energy renormalization is also summable

Interpolation between `H^-1` and `H2` at the `H1` level gives

\[
\|f\|_{H^1}
\le
C
\|f\|_{H^{-1}}^{1/3}
\|f\|_{H^2}^{2/3}.
\]

Therefore

\[
\boxed{
\|w-F_\infty\|_{H^1(cell)}
\le C R_k^{-2/3}.
}
\]

Critical scaling then yields

\[
\|\nabla(U-T)\|_{L^2(C_k)}^2
\le
C R_k^{-7/3}.
\]

Since

\[
\|\nabla T\|_{L^2(C_k)}=O(R_k^{-1/2}),
\]

we obtain

\[
\left|
\int_{C_k}
\bigl(|\nabla U|^2-|\nabla T|^2\bigr)dY
\right|
\le
C R_k^{-5/3}+C R_k^{-7/3}.
\]

Thus

\[
\boxed{
\sum_k
\left|
\int_{C_k}
(|\nabla U|^2-|\nabla T|^2)dY
\right|
<\infty.
}
\]

The periodic coherent branch therefore also possesses a finite exterior renormalized gradient-energy limit.

## 10. Tail residual action is finite

The canonical tail satisfies only the linear dilation equation.  Its full viscous/nonlinear projected residual has critical size

\[
\mathcal R_T
:=-\nu\Delta T+\mathbb P\nabla\cdot(T\otimes T)
=O(r^{-3}).
\]

On a shell,

\[
\|\mathcal R_T\|_{L^2(C_k)}=O(R_k^{-3/2}).
\]

Hence

\[
|\langle\mathcal R_T,T\rangle_{C_k}|
\le
O(R_k^{-1})
\]

and, on the H2-coherent branch,

\[
|\langle\mathcal R_T,U-T\rangle_{C_k}|
\le
O(R_k^{-7/3}).
\]

Both are geometrically summable.  Thus the genuine nonlinear/viscous tail residual carries only a finite total exterior action; it cannot replace the removed order-R dilation payer.

## 11. Sharpened periodic W1 frontier

The periodic branch now obeys the exact alternative

\[
\boxed{
P_{DSS}^{long}
\Longrightarrow
H_{2,crit}^{tail}
\quad\lor\quad
P_{ren}^{core},
}
\]

where `P_ren^core` denotes the H2-coherent periodic branch with

1. a canonical nonzero `1/r` passive tail;
2. summable exterior differences in L2 energy and gradient energy;
3. vanishing renormalized infinity dilation flux;
4. vanishing advective, viscous, and pressure boundary fluxes at infinity in log-radius mean;
5. only finite total action from the nonlinear/viscous residual of the canonical tail.

Thus a coherent periodic survivor can no longer appeal to an independent nonzero infinity interface payer after the passive critical dilation flux has been subtracted.  Any remaining recurrent production must be represented by the finite renormalized core/tail problem.

This is a reduction, not a contradiction: the finite renormalized core can still exchange energy with the canonical background through finite cross terms of indefinite sign.

## 12. DSD audit

The following distinctions are retained:

- passive similarity dilation versus material turnover;
- genuine tail residual versus artificial cutoff commutator;
- bounded critical H2 versus H2 tail escalation;
- vanishing infinity flux versus absence of all finite core-tail coupling;
- finite renormalized energy versus positive Lyapunov energy.

No sign is assigned to the finite renormalized core interaction without an additional identity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
