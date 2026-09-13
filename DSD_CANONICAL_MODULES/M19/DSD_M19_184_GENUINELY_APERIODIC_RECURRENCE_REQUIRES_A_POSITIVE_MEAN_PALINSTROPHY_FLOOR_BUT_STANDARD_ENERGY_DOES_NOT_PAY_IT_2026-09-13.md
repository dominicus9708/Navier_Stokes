# M19-184 — Genuinely aperiodic recurrence requires a positive mean-palinstrophy floor but standard energy does not pay it

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / BRANCH SPLIT + BUDGET FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Mean-palinstrophy parameter

Let

\[
\overline P_U:=\langle\|\nabla\Omega\|_2^2\rangle
\]

on a retained compact recurrent background.

M19-182/183 give coefficient bounds of the form

\[
A'\le C_A Z_+^{7/20}\overline P_U^{3/20},
\qquad
B'\le C_B\overline P_U^{1/2}.
\]

The exact `a=2` two-mode maximum is

\[
\Psi_2^{max}(A',B',\nu).
\]

It is monotone nondecreasing in both `A'` and `B'`.

## 2. A positive low-activity region always exists

At

\[
\overline P_U=0,
\]

both coefficients vanish and

\[
\Psi_2^{max}=0<\frac14.
\]

By continuity there exists a positive threshold

\[
\boxed{
\mathcal P_*=\mathcal P_*(\nu,Z_+,C_A,C_B)>0
}
\]

such that

\[
\boxed{
\overline P_U<\mathcal P_*
\Longrightarrow
N\le1.
}
\]

The threshold may be defined as the first value at which the algebraic M19-183 test reaches equality.

## 3. Aperiodic recurrence therefore has a derivative-activity floor

M19-173 states that `N<=1` reduces recurrent hard dynamics to relative-periodic behavior after at most a two-fold quotient return.

Hence a genuinely aperiodic recurrent survivor must satisfy

\[
\boxed{
N\ge2
\Longrightarrow
\overline P_U\ge\mathcal P_*.
}
\]

Thus the aperiodic hard branch is no longer an arbitrary compact recurrent state. It is a **high mean-palinstrophy compact-core branch**.

## 4. Physical scaling of palinstrophy

Let

\[
\tau=T_*-t=e^{-s}.
\]

Under the similarity vorticity scaling

\[
\omega(x,t)=\tau^{-1}\Omega(y,s),
\qquad
y=\frac{x-x_*}{\sqrt\tau},
\]

we have

\[
\|\nabla_x\omega(t)\|_2^2
=\tau^{-3/2}P_U(s).
\]

Since

\[
dt=\tau\,ds,
\]

physical spacetime palinstrophy scales as

\[
\boxed{
\|\nabla_x\omega\|_2^2dt
=\tau^{-1/2}P_U(s)\,ds
=e^{s/2}P_U(s)\,ds.
}
\]

Therefore persistent positive similarity mean palinstrophy is not controlled by the standard finite kinetic-energy dissipation ledger.

## 5. Why the standard energy budget cannot close this branch

The standard energy inequality controls

\[
\int\|\nabla u\|_2^2dt
=\int\|\omega\|_2^2dt,
\]

not

\[
\int\|\nabla\omega\|_2^2dt.
\]

In similarity variables the former receives the integrable weight `e^{-s/2}`, whereas palinstrophy receives the opposite singular weight `e^{s/2}`.

Hence

\[
\boxed{
\overline P_U\ge\mathcal P_*
\not\Rightarrow
\text{contradiction with finite kinetic energy}.
}
\]

## 6. Branch split

The recurrent hard branch now splits as

\[
\boxed{
\mathcal R_{hard}^{rec}
\Longrightarrow
\begin{cases}
\overline P_U<\mathcal P_*:
&N\le1\Rightarrow\text{relative-periodic after finite quotient return},\\
\overline P_U\ge\mathcal P_*:
&\text{high-activity aperiodic hard branch}.
\end{cases}
}
\]

## 7. Firewall

\[
\boxed{
\text{positive recurrent palinstrophy floor}
\neq
\text{finite-energy contradiction}.
}
\]

The high-activity branch needs a new signed/spectral/structural argument, not a return to the standard energy ledger.

---

\[
\boxed{\text{M19-184: APERIODIC RECURRENCE NOW PAYS A POSITIVE MEAN-PALINSTROPHY FLOOR.}}
\]
