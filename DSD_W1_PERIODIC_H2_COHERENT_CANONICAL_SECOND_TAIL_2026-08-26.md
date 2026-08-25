# DSD W1 Periodic H2-Coherent Canonical Second Tail

Date: 2026-08-26

Status: **ON THE H2-COHERENT PERIODIC W1 BRANCH, STRONG H1 CONVERGENCE TO THE CANONICAL CRITICAL TRACE IS OBTAINED / THE FIRST NONRESONANT R^-3 VELOCITY CORRECTION IS CANONICAL IN H^-1 AND EQUALS MINUS THE FULL PROJECTED RESIDUAL OF THE LEADING TRACE / NO FREE SECOND-TAIL MODE REMAINS AT THIS ORDER / GLOBAL REGULARITY UNPROVED.**

## 1. Inputs

Assume the periodic W1 branch with Leray period `S`, log-period

\[
L=S/2,
\qquad
\lambda=e^L,
\]

and canonical critical-amplitude trace

\[
F_\infty(\theta,\rho,s)
=\Phi(\theta,\rho-s/2),
\qquad
F_\infty(\rho+L,s)=F_\infty(\rho,s).
\]

Write

\[
U(Y,s)=e^{-\rho}w(\rho,\theta,s),
\qquad
\rho=\log|Y|.
\]

The exact far equation is written in projected fixed-cell form as

\[
\boxed{
D w
=e^{-2\rho}\mathcal N[w],
\qquad
D:=\partial_s+\frac12\partial_\rho,
}
\]

where `N` contains the fixed-cell representation of

\[
\nu\Delta U-\mathbb P\nabla\cdot(U\otimes U)
\]

after removal of the critical homogeneity factors.

The preceding H2-tail dichotomy assumes the coherent branch

\[
\sup_{R,s}
R^3\int_{A_R^*}|\nabla^2U|^2<\infty.
\]

## 2. Strong H1 convergence on same-phase cells

The one-period scale defect satisfies

\[
\|\delta_\rho\|_{H^{-1}}
\le Ce^{-2\rho},
\qquad
\delta_\rho:=w(\rho+L)-w(\rho).
\]

The H2-coherent branch gives

\[
\|\delta_\rho\|_{H^2}\le C.
\]

Interpolation at `H1` gives

\[
\|f\|_{H^1}
\le
C
\|f\|_{H^{-1}}^{1/3}
\|f\|_{H^2}^{2/3}.
\]

Hence

\[
\boxed{
\|\delta_\rho\|_{H^1}
\le Ce^{-2\rho/3}.
}
\]

Telescoping over geometric same-phase cells gives

\[
\boxed{
\|w(\rho_k)-F_\infty\|_{H^1(cell)}
\le C e^{-2\rho_k/3}.
}
\]

All estimates are uniform in the periodic phase `s`.

Thus

\[
\boxed{w\to F_\infty\quad\text{strongly in }H^1\text{ on fixed far cells}.}
\]

## 3. Continuity of the projected residual into H^-1

On a fixed three-dimensional annular cell,

\[
H^1\hookrightarrow L^q
\qquad(2\le q\le6).
\]

Strong H1 convergence implies strong L4 convergence. Therefore

\[
w\otimes w\to F_\infty\otimes F_\infty
\quad\text{strongly in }L^2.
\]

Hence

\[
\mathbb P\nabla\cdot(w\otimes w)
\to
\mathbb P\nabla\cdot(F_\infty\otimes F_\infty)
\quad\text{in }H^{-1}.
\]

Also

\[
\Delta w\to\Delta F_\infty
\quad\text{in }H^{-1}
\]

because the Laplacian is continuous `H1 -> H^-1`.

Consequently

\[
\boxed{
\mathcal N[w]
\to
\mathcal N[F_\infty]
\quad\text{strongly in }H^{-1}(cell).
}
\]

The convergence is uniform over one compact periodic time interval.

## 4. Exact one-period defect coefficient

Integrate the transport equation along one dilation characteristic

\[
\rho(\tau)=\rho+\tau/2,
\qquad
s(\tau)=s+\tau,
\qquad
0\le\tau\le S.
\]

Periodicity gives

\[
\begin{aligned}
&w(\rho+L,s)-w(\rho,s)\\
&=e^{-2\rho}
\int_0^S
 e^{-\tau}
\mathcal N[w](\rho+\tau/2,s+\tau)d\tau.
\end{aligned}
\]

Along the characteristic the leading profile has constant co-moving phase

\[
\eta=\rho-s/2.
\]

Therefore `N[F_infty]` is constant with respect to this characteristic time after the fixed-cell geometric representation is used.  Strong H1 convergence yields

\[
\boxed{
A_\rho
:=
\int_0^S e^{-\tau}\mathcal N[w](\rho+\tau/2,s+\tau)d\tau
\to
(1-e^{-S})\mathcal N[F_\infty]
}
\]

in `H^-1`.

Thus

\[
\boxed{
w(\rho+L)-w(\rho)
=e^{-2\rho}
\left[(1-e^{-S})\mathcal N[F_\infty]+o_{H^{-1}}(1)\right].
}
\]

## 5. Telescoping identifies the second tail

Fix one same-phase sequence

\[
\rho_k=\rho_0+kL.
\]

Since

\[
w(\rho_k)\to F_\infty,
\]

we have

\[
F_\infty-w(\rho_k)
=
\sum_{j=k}^\infty
\left[w(\rho_{j+1})-w(\rho_j)\right].
\]

Use

\[
e^{-2\rho_j}
=e^{-2\rho_k}e^{-S(j-k)}.
\]

Then, in `H^-1`,

\[
\begin{aligned}
e^{2\rho_k}(F_\infty-w(\rho_k))
&\to
(1-e^{-S})\mathcal N[F_\infty]
\sum_{n=0}^\infty e^{-Sn}\\
&=
\mathcal N[F_\infty].
\end{aligned}
\]

Therefore

\[
\boxed{
e^{2\rho}
\left(w-F_\infty\right)
\to
-\mathcal N[F_\infty]
\quad\text{in }H^{-1}
}
\]

along every canonical same-phase far sequence.

Equivalently,

\[
\boxed{
w
=F_\infty
-e^{-2\rho}\mathcal N[F_\infty]
+o_{H^{-1}}(e^{-2\rho}).
}
\]

This is the canonical nonresonant second-tail expansion.

## 6. Why the coefficient is unique

Suppose one writes a formal second term

\[
w=F_\infty+e^{-2\rho}G+\cdots.
\]

Because

\[
D F_\infty=0
\]

and, along the co-moving phase,

\[
D(e^{-2\rho}G)=-e^{-2\rho}G,
\]

the order-`e^-2rho` equation is

\[
-G=\mathcal N[F_\infty].
\]

Hence

\[
\boxed{G=-\mathcal N[F_\infty].}
\]

The eigenvalue `-1` of the dilation characteristic at this order is nonzero.  There is therefore no resonance and no freely selectable homogeneous second-tail coefficient compatible with the canonical far limit.

## 7. Leray-velocity expansion

Since

\[
U=e^{-\rho}w,
\]

the expansion becomes

\[
\boxed{
U(Y,s)
=
|Y|^{-1}F_\infty
-|Y|^{-3}\mathcal N[F_\infty]
+o_{H^{-1}_{cell}}(|Y|^{-3}).
}
\]

The first term is the passive critical memory.  The first dynamic correction is two powers lower and is completely forced by the full Navier--Stokes residual of that memory.

## 8. Physical-variable interpretation

Let

\[
\tau=T^*-t,
\qquad
Y=(x-X_*)/\sqrt\tau.
\]

The leading term becomes the static critical trace

\[
t_*(x)
=
\frac1{|x-X_*|}
\Phi\!\left(\widehat{x-X_*},\log|x-X_*|\right).
\]

The `|Y|^-3` correction becomes

\[
\tau^{-1/2}|Y|^{-3}
=
\frac{\tau}{|x-X_*|^3}.
\]

Therefore, away from the singular point and in the corresponding local weak topology,

\[
\boxed{
u(x,t)
=t_*(x)
-\frac{T^*-t}{|x-X_*|^3}
\mathcal N[F_\infty]
+o(T^*-t).
}
\]

Thus a vanishing first-order-in-time correction carries exactly the order-`r^-3` time derivative needed to balance the nonlinear/viscous residual of the static `1/r` trace.

This confirms and sharpens the earlier anti-proof statement: the physical critical trace need not solve stationary Navier--Stokes.

## 9. Updated periodic coherent frontier

On the H2-coherent periodic W1 branch, the far field is no longer described only by an unspecified `1/r + remainder` structure.  It has the canonical hierarchy

\[
\boxed{
U
=
T_{-1}
+T_{-3}
+o_{H^{-1}}(r^{-3}),
}
\]

with

\[
T_{-1}=r^{-1}F_\infty,
\qquad
T_{-3}=-r^{-3}\mathcal N[F_\infty].
\]

The order `-3` field is not an independent tail channel.  It is the forced response to the leading critical memory.

The remaining open issue is whether the resulting finite renormalized core plus this fully forced exterior asymptotic hierarchy can support a nontrivial recurrent Leray orbit.  No sign-definite renormalized Lyapunov functional is derived here.

## 10. DSD audit

The calculation distinguishes:

- the linear-dilation leading trace from the full Navier--Stokes residual;
- weak `H^-1` asymptotic coefficients from pointwise asymptotic expansions;
- a forced nonresonant correction from a free new degree of freedom;
- a time-independent limiting trace from a stationary Navier--Stokes solution.

The `r^-3` statement is made in the fixed-cell `H^-1` asymptotic topology unless stronger regularity is separately proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
