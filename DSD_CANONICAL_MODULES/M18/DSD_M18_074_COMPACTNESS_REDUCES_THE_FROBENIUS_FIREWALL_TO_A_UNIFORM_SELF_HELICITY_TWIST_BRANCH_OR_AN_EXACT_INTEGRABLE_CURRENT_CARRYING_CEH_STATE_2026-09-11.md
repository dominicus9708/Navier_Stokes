# M18-074 — Compactness reduces the Frobenius firewall to a uniform self-helicity/twist branch or an exact integrable current-carrying CE-H state

**Date:** 2026-09-11  
**Status:** COMPACTNESS DICHOTOMY / SELF-HELICITY ABSORPTION / EXACT FROBENIUS-LIMIT EXTRACTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-073 corrects the finite-cross-section shortcut.

The algebraic transverse current

\[
\mathcal J_\perp
=(\nabla\times W)\times\xi
\]

is always defined on the active set, but it is an actual current on a vortex-orthogonal material surface only where the Frobenius condition

\[
\tau_\xi
:=
\xi\cdot\nabla\times\xi
=0
\]

holds on an open patch.

The present module uses compactness of the marked CE-H hull to avoid an unstable `almost integrable => surface` argument.

The exact dichotomy is:

\[
\boxed{
\text{uniform active director twist/self-helicity}
\quad\lor\quad
\text{an exact Frobenius-integrable current-carrying state in the hull}.
}
\]

The first branch is absorbed into the existing M16-023 self-helicity channel.

The second branch admits an actual vortex-transverse material patch, but recurrence of that same material patch remains a genealogy question.

## 2. Twist is exactly normalized vorticity self-helicity

M18-073 gives

\[
\xi\cdot\nabla\times W
=
\rho\tau_\xi.
\]

Multiplying by \(\rho\),

\[
\boxed{
W\cdot(\nabla\times W)
=
\rho^2\tau_\xi.
}
\]

Therefore the Frobenius obstruction is precisely the vorticity self-helicity density normalized by \(\rho^2\):

\[
\boxed{
\tau_\xi
=
\frac{W\cdot\nabla\times W}{\rho^2}
}
\]

on \(\rho>0\).

Also

\[
\boxed{
\rho^2\tau_\xi^2
=
\frac{(W\cdot\nabla\times W)^2}{\rho^2}.
}
\]

Thus the director-twist branch is not a new independent endpoint; it is a quadratic active-amplitude refinement of the M16-023 self-helicity channel.

## 3. Smooth active cutoff

M18-072 gives a fixed amplitude threshold \(a_B>0\) such that every marked CE-H state satisfies

\[
\int_{\{\rho\ge a_B\}}
|J_B|^2dy
\ge c_B>0
\]

for a fixed \(c_B>0\), where

\[
J_B=W\times(\nabla\times W).
\]

Choose a fixed smooth cutoff

\[
\chi:[0,\infty)\to[0,1]
\]

such that

\[
\chi(r)=0
\quad\text{for }r\le a_B/2,
\]

and

\[
\chi(r)=1
\quad\text{for }r\ge a_B.
\]

Define the active current observable

\[
\boxed{
\mathfrak J(Y)
:=
\int\chi(\rho_Y)|J_{B,Y}|^2dy.
}
\]

Then uniformly on the marked hull,

\[
\boxed{
\mathfrak J(Y)
\ge c_B>0.
}
\]

## 4. Smooth active twist observable

On the support of \(\chi\), the amplitude is bounded below by \(a_B/2\), so \(\xi=W/\rho\) and all finite derivatives are smooth functions of the state.

Define

\[
\boxed{
\mathfrak T(Y)
:=
\int
\chi(\rho_Y)
\rho_Y^2
\tau_{\xi_Y}^2dy.
}
\]

Equivalently,

\[
\mathfrak T(Y)
=
\int
\chi(\rho_Y)
\frac{(W_Y\cdot\nabla\times W_Y)^2}{\rho_Y^2}dy.
\]

The marked hull is strongly compact in sufficiently high Sobolev topology, so \(\mathfrak T\) is a continuous nonnegative state observable.

## 5. Compactness dichotomy

Because \(\mathfrak T\ge0\) is continuous on a compact hull, exactly one of the following occurs.

### Branch T — uniform active twist

\[
\boxed{
\inf_{Y\in\mathfrak H}
\mathfrak T(Y)
=:t_*>0.
}
\]

Then every marked state carries a fixed positive active self-helicity/twist charge.

### Branch F — zero-twist hull state

Otherwise

\[
\inf_{Y\in\mathfrak H}\mathfrak T(Y)=0.
\]

Choose \(Y_n\in\mathfrak H\) with

\[
\mathfrak T(Y_n)\to0.
\]

By compactness, after a subsequence

\[
Y_n\to Y_\infty\in\mathfrak H.
\]

Continuity gives

\[
\boxed{
\mathfrak T(Y_\infty)=0.
}
\]

Since the integrand is nonnegative and smooth on \(\{\chi>0\}\),

\[
\boxed{
\tau_{\xi_\infty}=0
\quad\text{on every connected open subset of }\{\chi(\rho_\infty)>0\}.
}
\]

At the same time the active current lower bound passes to the limit:

\[
\boxed{
\mathfrak J(Y_\infty)
\ge c_B>0.
}
\]

Thus \(Y_\infty\) is an exact Frobenius-integrable **and** current-carrying CE-H state on its active cutoff region.

## 6. Branch T is the existing self-helicity channel

On the support of \(\chi\),

\[
\rho\le M_*.
\]

Since

\[
W\cdot\nabla\times W
=
\rho^2\tau_\xi,
\]

Cauchy--Schwarz and the active amplitude bounds relate \(\mathfrak T\) to a quadratic self-helicity charge.

In particular, a uniform lower bound

\[
\mathfrak T\ge t_*>0
\]

means that \(W\cdot\operatorname{curl}W\) cannot vanish identically on the active recurrent population.

This is precisely the geometric quantity already isolated in M16-023 as

\[
C_{H_W}^{axial}.
\]

Therefore

\[
\boxed{
G_{uniform\ twist}
\subset
G_{vorticity\ self\text{-}helicity/director}.
}
\]

No new top-level branch is introduced.

## 7. Exact Frobenius state carries a nonzero integrable current patch

On Branch F, \(\mathfrak J(Y_\infty)>0\).

Hence there exists a point

\[
y_*
\]

inside the active cutoff region with

\[
J_B(y_*)\ne0.
\]

Because

\[
J_B=-\rho\mathcal J_\perp
\]

and \(\rho(y_*)>a_B/2\),

\[
\boxed{
\mathcal J_\perp(y_*)\ne0.
}
\]

Continuity gives an open neighborhood \(U_*\) on which

\[
|\mathcal J_\perp|\ge j_*>0
\]

after shrinking the neighborhood.

But Branch F also gives

\[
\tau_\xi=0
\]

through the active connected component containing \(y_*\).

Frobenius therefore supplies a local surface patch

\[
\Sigma_*
i y_*
\]

with

\[
n=\xi.
\]

On that patch,

\[
\boxed{
J_{\Sigma_*}
=\mathcal J_\perp.
}
\]

Hence after shrinking to a positive-area disk,

\[
\boxed{
\int_{\Sigma_*}|J_{\Sigma_*}|^2dA
\ge j_{surf}>0.
}
\]

This obtains a genuine M5-520 surface-current state without any bulk-to-surface trace inequality.

It uses exact Frobenius integrability plus pointwise continuity instead.

## 8. Short-time material thickening

Use \(\Sigma_*\) as an initial material patch at the state time \(\theta_*\).

On CE-H,

\[
D_B\xi=0
\]

and, as audited in M18-073,

\[
(\nabla B)^T\xi
=(\sigma+\tfrac12)\xi.
\]

Therefore the material normal initialized by

\[
n(\theta_*)=\xi(\theta_*)
\]

remains aligned with \(\xi\) while the patch remains smooth and active.

Uniform smoothness then gives a short interval

\[
I_*=[\theta_* -\delta_*,\theta_*+\delta_*]
\]

on which either

1. the material patch remains controlled and
   \[
   \int_{I_*}\int_{\Sigma(\theta)}|J_\Sigma|^2dA\,d\theta
   \ge c_{surf}>0,
   \]
   or
2. the patch loses the active/integrable/material geometry, which is a typed
   \[
   G_{surface/domain/marker\ turnover}
   \]
   event.

Thus an exact integrable current-carrying state immediately gives a finite surface-current action event or a geometric turnover event.

## 9. Why this still does not give recurrent migration

M5-521 prices a **change of a material-label flux moment** by surface-current action.

A nonzero surface current by itself does not imply that a fixed signed flux amount migrates across a fixed label distance.

The current may circulate locally and reverse.

Likewise the compact hull may return near the Eulerian state \(Y_\infty\) while the particular material patch \(\Sigma_*\) does not return as the same label set.

Therefore

\[
\boxed{
\text{surface-current event}
\not\Rightarrow
\text{recurrent material-label migration}
}
\]

without a genealogy/label bridge.

This is the remaining material firewall.

## 10. Relation to the earlier proposed coarea route

A coarea/foliation theorem could still organize a family of current-carrying surfaces on Branch F.

But it is not required to prove existence of at least one nontrivial surface-current patch.

The compactness/Frobenius argument gives the more economical route:

\[
\boxed{
\text{no uniform twist floor}
\to
\text{exact zero-twist hull state}
\to
\text{nonzero current point}
\to
\text{local transverse surface}
\to
\text{surface-current action or turnover}.
}
\]

## 11. Audit verdict

### Certified

1. The Frobenius twist is exactly normalized vorticity self-helicity:
   \[
   W\cdot\operatorname{curl}W=\rho^2\tau_\xi.
   \]
2. A smooth cutoff makes the active twist charge a continuous observable on the compact hull.
3. Compactness gives the exhaustive dichotomy
   \[
   \text{uniform active twist floor}
   \lor
   \text{exact zero-twist hull state}.
   \]
4. The uniform twist branch is absorbed into the existing M16-023 self-helicity/director channel.
5. The zero-twist hull state still carries the M18-072 non-Beltrami current floor.
6. Therefore it contains a genuine local vortex-transverse surface patch with nonzero M5-520 surface current.
7. Smooth material evolution gives a finite surface-current action event unless the patch undergoes active/domain/marker turnover.

### Not certified

- recurrent return of the same material surface labels;
- fixed signed-flux migration across labels;
- a one-sign material-flux drift;
- ancestry closure of the resulting derivative/current payment;
- exclusion of the uniform self-helicity branch;
- remote/critical closure;
- global regularity.

## 12. Next target

The current signed route is now reduced to a material-label question.

M18-075 should ask whether the exact CE-H relations and the finite persistent-lineage architecture allow a current-carrying Frobenius patch to **recur Eulerianly while indefinitely avoiding recurrence of its material labels**.

The natural split is

\[
\boxed{
\text{same-label return}
\lor
\text{label replacement/migration}
\lor
\text{surface export/domain loss}.
}
\]

The latter two are already costed turnover branches.

The first would allow M5-521 to compare material-label moments over a completed return and may expose whether the surface current is a reversible oscillation or a net flux redistribution.
