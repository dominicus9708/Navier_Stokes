# DSD M5-566 — DSS plus spectator Duhamel forces a nonzero log-periodic 1/r tail

Date: 2026-09-02

Status: **DSS TAIL ASYMPTOTICS / ON AN EXACT BACKWARD DSS SUBBRANCH, THE M5-563 OUTWARD-CHARACTERISTIC DUHAMEL LAW COMBINED WITH SIMILARITY-TIME PERIODICITY MAKES THE CRITICAL RESCALED PROFILE ASYMPTOTICALLY PERIODIC IN LOG RADIUS / THE ONE-PERIOD RADIAL DEFECT IS `O(R^-2)` IN THE FIXED-ANNULUS PROFILE NORM AND IS GEOMETRICALLY SUMMABLE / THEREFORE THE FAR FIELD HAS A LIMITING TRAVELING LOG-PERIODIC AMPLITUDE `A(LOG R - THETA/2, OMEGA)` WITH `U ~ R^-1 A` / IF THIS LIMITING AMPLITUDE VANISHES, THE SUMMABLE DEFECT IMPROVES THE TAIL TO A SUBCRITICAL RATE STRONG ENOUGH TO RECOVER GLOBAL `L3`, WHICH IS IMPOSSIBLE ON A NONTRIVIAL RECURRENT COMPONENT BY M5-562 / HENCE ANY UNRESOLVED DSS SURVIVOR MUST CARRY A NONZERO LOG-PERIODIC `1/R` TAIL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact DSS hypothesis

Assume the similarity solution is periodic:

\[
\boxed{
U(y,\theta+T)=U(y,\theta),
\qquad
\Pi(y,\theta+T)=\Pi(y,\theta)
}
\]

for some

\[
T>0.
\]

The physical solution is backward DSS with scaling factor

\[
\boxed{
\lambda=e^{T/2}>1.
}
\]

Set

\[
L:=\log\lambda=\frac T2.
\]

---

## 2. Critical log-radius profile

Write

\[
r=e^\rho,
\qquad
\omega=\frac y{|y|}\in S^2.
\]

Define

\[
\boxed{
F(\rho,\omega,\theta)
:=
e^\rho U(e^\rho\omega,\theta).
}
\]

Thus

\[
U(y,\theta)
=
\frac1rF(\log r,\omega,\theta).
\]

The critical `1/r` tail corresponds to an order-one profile `F`.

---

## 3. Exact transport equation in log radius

M5-563 proved that along

\[
R(\tau)=R_0e^{\tau/2},
\]

the scaled profile

\[
V(\xi,\tau)
=R(\tau)U(R(\tau)\xi,\theta_0+\tau)
\]

satisfies

\[
\partial_\tau V
=R(\tau)^{-2}\mathcal R[V,P].
\]

In log-radius notation this is the schematic exact equation

\[
\boxed{
\left(
\partial_\theta
+\frac12\partial_\rho
\right)F
=
e^{-2\rho}\mathcal N[F,P],
}
\]

where `mathcal N` is the fixed-annulus rescaled nonlinear/pressure/viscous operator, including angular and radial derivatives.

On the spectator analytic branch,

\[
\boxed{
\|\mathcal N[F,P]\|_X
\le C_{spec}
}
\]

in a fixed-annulus norm `X` strong enough to control the weighted Dirichlet shell profile.

Failure of this bound is already a strong derivative/pressure/active-remote exit.

---

## 4. One-period characteristic relation

Start at log radius `rho` and time `theta`.

After one DSS period `T`, the outward characteristic reaches

\[
\rho+\frac T2
=
\rho+L.
\]

Integrating the exact characteristic equation gives

\[
F(\rho+L,\omega,\theta+T)
-
F(\rho,\omega,\theta)
=
\int_0^T
 e^{-2(\rho+s/2)}
\mathcal N(s)ds.
\]

Therefore

\[
\boxed{
\|F(\rho+L,\cdot,\theta+T)
-F(\rho,\cdot,\theta)\|_X
\le
C e^{-2\rho}.
}
\]

Using DSS periodicity in `theta`,

\[
F(\rho+L,\omega,\theta+T)
=F(\rho+L,\omega,\theta),
\]

so

\[
\boxed{
\|F(\rho+L,\cdot,\theta)
-F(\rho,\cdot,\theta)\|_X
\le
C e^{-2\rho}.
}
\]

This is the key asymptotic discrete-homogeneity estimate.

---

## 5. Geometric summability of radial-period defects

Fix a phase

\[
\rho_0\in[\rho_{spec},\rho_{spec}+L).
\]

Define

\[
F_n(\omega,\theta)
:=
F(\rho_0+nL,\omega,\theta).
\]

Then

\[
\|F_{n+1}-F_n\|_X
\le
C e^{-2\rho_0}e^{-2nL}.
\]

Since

\[
\sum_{n=0}^\infty e^{-2nL}<\infty,
\]

the sequence is Cauchy in `X`.

Hence there exists

\[
\boxed{
A(\rho_0,\omega,\theta)
:=
\lim_{n\to\infty}
F(\rho_0+nL,\omega,\theta).
}
\]

Moreover

\[
\boxed{
\|F(\rho_0+nL)-A(\rho_0)\|_X
\le
C e^{-2(\rho_0+nL)}.
}
\]

---

## 6. Log-periodicity of the limiting tail

The phase variable is naturally taken modulo `L`.

Extend `A` by

\[
\boxed{
A(\zeta+L,\omega,\theta)
=A(\zeta,\omega,\theta).
}
\]

The far-field tail therefore has a limiting log-periodic critical amplitude.

Because the rescaled PDE forcing tends to zero as `rho->infinity`, the limit satisfies the homogeneous transport law

\[
\boxed{
\left(
\partial_\theta
+\frac12\partial_\zeta
\right)A=0.
}
\]

Thus there is a profile `a` such that

\[
\boxed{
A(\zeta,\omega,\theta)
=
a\left(\zeta-\frac\theta2,\omega\right).
}
\]

DSS periodicity in `theta` gives

\[
a(s-L,\omega)=a(s,\omega),
\]

so `a` is `L=log lambda` periodic.

Therefore

\[
\boxed{
U(y,\theta)
=
\frac1{|y|}
 a\left(
\log|y|-\frac\theta2,
\frac y{|y|}
\right)
+
\text{subleading tail}.
}
\]

---

## 7. Divergence-free constraint on the leading amplitude

Decompose

\[
a(s,\omega)
=a_r(s,\omega)\,\omega
+a_T(s,\omega),
\qquad
a_T\cdot\omega=0.
\]

For

\[
U=r^{-1}a(\log r-\theta/2,\omega),
\]

the leading divergence is

\[
\nabla\cdot U
=r^{-2}
\left[
\partial_s a_r
+a_r
+\operatorname{div}_{S^2}a_T
\right].
\]

Hence the limiting amplitude must satisfy

\[
\boxed{
\partial_s a_r
+a_r
+\operatorname{div}_{S^2}a_T
=0.
}
\]

This is a genuine leading-order structural constraint.

It does not force `a=0` by itself.

---

## 8. The leading nonlinear Navier--Stokes operator does not constrain `a` at order one

The critical profile equation has the form

\[
\left(\partial_\theta+\frac12\partial_\rho\right)F
=e^{-2\rho}\mathcal N[F,P].
\]

After taking `rho->infinity`, the factor `e^-2rho` kills the finite rescaled nonlinear/pressure/viscous operator.

Therefore the leading amplitude is governed by the linear transport and incompressibility constraints, while the full Navier--Stokes operator determines the subleading `O(e^-2rho)` radial correction.

Consequently there is no algebraic reason at this level for a nonzero log-periodic amplitude to vanish.

This is an important firewall against overusing the far-field Navier--Stokes equation.

---

## 9. If the limiting amplitude vanishes, the tail becomes subcritical

Suppose

\[
\boxed{a\equiv0.}
\]

Then for each radial phase, the telescoping defect estimate gives

\[
\|F(\rho,\cdot,\theta)\|_X
\le
C e^{-2\rho}
\]

at large `rho`.

Since

\[
U=r^{-1}F,
\]

this yields a strongly subcritical tail, schematically

\[
\boxed{
U=O(r^{-3})
}
\]

in the retained annular norm.

In particular the dyadic cubic tail is summable and

\[
\boxed{U(\theta)\in L^3(\mathbb R^3).}
\]

For an exact DSS orbit this gives global `L3` uniformly over one period and hence along a backward physical-time sequence.

The ancient global-`L3` Liouville theorem then yields

\[
U\equiv0.
\]

That contradicts the nontrivial hard-core mark.

Therefore any nontrivial DSS survivor must satisfy

\[
\boxed{a\not\equiv0.}
\]

---

## 10. Nonzero amplitude reproduces the critical shell stack

For a nonzero periodic amplitude, the leading gradient has size

\[
|\nabla U|\sim r^{-2}
\]

on phases where the angular/log-radial derivative does not vanish.

Hence

\[
\int_{A_R}|\nabla U|^2dy
\sim R^{-1}
\]

and

\[
\boxed{J_R\sim O(1)}
\]

along corresponding logarithmic phases.

Thus

\[
\sum_kJ_{R_k}^{3/2}=\infty
\]

while

\[
\sum_kR_k^{-1}J_{R_k}<\infty.
\]

The limiting log-periodic `1/r` tail is exactly the sharp shell geometry already isolated by the ancient tail audits.

---

## 11. Revised DSS hard core

The unresolved exact DSS branch is no longer an arbitrary periodic similarity solution.

On the passive spectator lane it must carry

\[
\boxed{
\begin{gathered}
U(y,\theta)
=
|y|^{-1}
 a(\log|y|-\theta/2,y/|y|)
+o(|y|^{-1}),\\
a(s+\log\lambda,\omega)=a(s,\omega),\\
a\not\equiv0,\\
\partial_s a_r+a_r+\operatorname{div}_{S^2}a_T=0,
\end{gathered}
}
\]

with summable `O(r^-2)` defect in the critical rescaled profile.

This is a substantially narrower boundary condition at infinity.

---

## 12. Highest-value next target

There are now two focused DSS questions.

### A. Tail-to-core matching

The leading amplitude `a` is a free critical transport datum at infinity, while the smooth core is regular at finite radius.

Determine whether matching a nonzero log-periodic `1/r` tail to the finite-enstrophy recurrent core forces a nonzero conserved or monotone boundary invariant.

### B. Periodic vorticity/shape ledger

Use exact time periodicity to combine the M5-559 determinant payer identity, M5-554 connector compression, M5-560 material-volume multiplier, and the nonzero asymptotic amplitude over one period.

No external theorem currently closes arbitrary `lambda`, so any further progress must exploit these extra inherited structures.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
