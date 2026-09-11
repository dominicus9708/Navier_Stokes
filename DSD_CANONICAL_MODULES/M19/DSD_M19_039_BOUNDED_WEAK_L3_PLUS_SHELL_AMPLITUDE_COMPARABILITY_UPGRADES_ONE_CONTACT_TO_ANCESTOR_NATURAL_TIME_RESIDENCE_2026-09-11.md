# M19-039 — Bounded weak-L3 plus shell-amplitude comparability upgrades one contact to ancestor-natural-time residence

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC RADIAL TRANSPORT / LORENTZ WEIGHTED-SPEED BOUND / NATURAL-TIME THICKENING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-038

On the fully quiet population branch, the only new mechanism capable of rapidly removing shell-localized material enstrophy is the relative radial current

\[
C_{rad}
=
\int (u-\dot X)\cdot\nabla\chi_R\,|\omega|^2dx,
\]

with

\[
|\nabla\chi_R|\lesssim R^{-1}.
\]

The goal is to estimate this current from the bounded weak-critical velocity corridor.

## 2. Shell-amplitude comparability hypothesis

Let \(E_R\) denote the active shell collar carrying the selected ancestry packet.

Write

\[
m_R
:=
\int_{E_R}|\omega|^2dx.
\]

On the retained shell-amplitude/comparability corridor assume

\[
\boxed{
m_R\ge c_m\frac{J}{R}}
\]

and

\[
\boxed{
\|\omega\|_{L^\infty(E_R)}
\le
C_A\frac{\sqrt J}{R^2}.
}
\]

These are scale-compatible: a shell of volume order \(R^3\) with amplitude \(\sqrt J/R^2\) has enstrophy order \(J/R\).

Failure of either condition is retained as concentration/amplitude/noncomparability exit rather than silently excluded.

## 3. Lorentz estimate for vorticity-weighted velocity

Assume

\[
\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}\le M.
\]

Let

\[
f=|\omega|^2\mathbf 1_{E_R}.
\]

Lorentz Hölder gives

\[
\int |u|f
\le
C\|u\|_{L^{3,\infty}}
\|f\|_{L^{3/2,1}}.
\]

Interpolation between \(L^1\) and \(L^\infty\) yields

\[
\|f\|_{L^{3/2,1}}
\lesssim
\|f\|_1^{2/3}\|f\|_\infty^{1/3}.
\]

Hence

\[
\int_{E_R}|u||\omega|^2dx
\lesssim
M m_R^{2/3}
\|\omega\|_\infty^{2/3}.
\]

Dividing by \(m_R\),

\[
\frac{
\int |u||\omega|^2
}{m_R}
\lesssim
M\|\omega\|_\infty^{2/3}m_R^{-1/3}.
\]

Using the shell comparability bounds,

\[
\|\omega\|_\infty^{2/3}m_R^{-1/3}
\lesssim
\left(\frac{\sqrt J}{R^2}\right)^{2/3}
\left(\frac JR\right)^{-1/3}
\lesssim
R^{-1}.
\]

Therefore

\[
\boxed{
\frac{
\int_{E_R}|u||\omega|^2dx
}{
\int_{E_R}|\omega|^2dx
}
\lesssim
\frac{M}{R}.
}
\]

The vorticity-weighted average speed is critical, not Type-II, on this corridor.

## 4. Moving-center contribution

If the shell center is \(X(t)\), then

\[
|u-\dot X|
\le |u|+|\dot X|.
\]

Assume the retained center genealogy satisfies the critical drift bound

\[
\boxed{R|\dot X(t)|\le M_X.}
\]

Failure is a center-drift/turnover/export defect already separated in the upstream genealogy audit.

Then

\[
\boxed{
U_{rad}^{weighted}
\lesssim
\frac{M+M_X}{R}.
}
\]

## 5. Radial-current rate

Since \(|\nabla\chi_R|\lesssim R^{-1}\),

\[
|C_{rad}|
\lesssim
\frac1R
\int_{E_R}|u-\dot X||\omega|^2dx.
\]

Thus

\[
\boxed{
|C_{rad}|
\lesssim
\frac{M+M_X}{R^2}m_R.
}
\]

Equivalently, as long as the localized mass remains comparable to \(m_R\),

\[
\boxed{
\left|\frac d{dt}\log M_{2}^{\chi}\right|_{rad}
\lesssim
\frac{M+M_X}{R^2}.
}
\]

## 6. Ancestor-natural-time thickening

Suppose at \(t_0\)

\[
M_2^\chi(t_0)\ge m_*.
\]

Assume the already typed stretch, bulk-diffusion, shell-diffusion and population-exchange terms contribute at most a sufficiently small fixed fraction of \(m_*\) over the candidate interval.

Then radial transport alone cannot reduce the mark below \(m_*/2\) before a time

\[
\boxed{
\tau_{res}
\gtrsim
\frac{R^2}{M+M_X}.
}
\]

Hence on the bounded weak-critical, shell-comparable, quiet-source branch,

\[
\boxed{
\tau_{res}\gtrsim cR^2.
}
\]

This is the **ancestor natural parabolic time**, not merely the current child time.

## 7. Gain over the raw age penalty

For an age ratio

\[
R=Kr,
\]

the current-epoch window has duration only

\[
r^2=K^{-2}R^2.
\]

M19-039 replaces that raw window by

\[
\tau_{res}\gtrsim R^2
\]

on the retained quiet branch.

Thus the temporal thickness gains the factor

\[
\boxed{K^2.}
\]

This removes the geometric \(K^{-2}\) **dwell-duration deficiency for one genuine material contact**.

It does not yet remove the shrinking physical-radius weight in the global Leray dissipation ledger.

## 8. Return-density consequence

The physical weighted return density is schematically

\[
\mathfrak R_k
=\frac1{R_k}
\sum_\ell \tau_{k,\ell}.
\]

For \(N_k\) selected natural-time contacts satisfying M19-039,

\[
\boxed{
\mathfrak R_k
\gtrsim
N_kR_k.
}
\]

The sufficient cubic-tail closure target

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

therefore becomes exactly

\[
\boxed{
N_kR_k\gtrsim J_k^{1/2}.
}
\]

This recovers the old physical return-count threshold, but now the **natural-time dwell per contact is derived conditionally from bounded weak-L3 and shell comparability**, rather than assumed.

## 9. What remains

The remaining R-AC problem is no longer principally the duration of one return.

It is the multiplicity/incidence theorem

\[
\boxed{
\mathcal T_{count}:
N_kR_k\gtrsim J_k^{1/2}
\quad\text{on a cubic-mass-divergent subset},
}
\]

or else a typed replacement/export/concentration/center-drift/source-exchange exit.

Thus the age penalty has been reduced from a \(K^{-2}\) time-thickness problem to a **return-count problem at shrinking physical radius**.

## 10. Firewalls

M19-039 does not claim the shell-amplitude comparability bounds automatically hold for every \(J_k\).

It does not claim the center-drift bound automatically holds.

It does not claim source/exchange terms are small; their failure is an already typed payer branch.

And it does not prove the return-count lower bound \(N_kR_k\gtrsim J_k^{1/2}\).

---

\[
\boxed{\text{M19-039 COMPLETE; ONE QUIET CONTACT NOW HAS FULL ANCESTOR-NATURAL-TIME THICKNESS.}}
\]