# DSD M19-266 — Ergodic hard tail has positive log-radius density, so sublinear tail decay is not the surviving branch

Date: 2026-09-15  
Canonical ID: **M19-266**  
Status: **ACTIVE REDUCTION / M5-571 REIMPORT / POSITIVE-DENSITY HARD TAIL / SUBLINEAR-TAIL TARGET REMOVED ON ERGODIC HARD COMPONENT / PDE FLUX-SOURCE BALANCE PROMOTED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-265 showed that finite physical energy permits a normalized critical tail

\[
U_0(y,s)
=
|y|^{-1}A(\log|y|-s/2,\omega)
\]

to extend to normalized radius \(R\sim r_j^{-1}\), and proposed sublinear normalized kinetic-energy growth as a possible strengthening that would suppress such a tail.

The historical M5-567--571 chain already contains a stronger classification of the surviving hard tail.

The present module reimports that result into the M19 low-frequency frontier.

---

## 2. M5-567 scattering datum

On the passive critical spectator branch, M5-567 constructs

\[
\boxed{
U_Y(y,\theta)
=
\frac1{|y|}
A_Y\left(
\log|y|-\frac\theta2,
\frac y{|y|}
\right)
+O(|y|^{-3}).
}
\]

The scattering datum satisfies the exact covariance

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega).
}
\]

Thus similarity-time dynamics becomes translation in log radius.

M5-567 also identifies the fundamental endpoint difference:

\[
\boxed{
\begin{aligned}
\text{finite enstrophy}
&\sim
\text{exponentially weighted square control in }q,\\
\text{global strong }L^3
&\sim
A\in L^3(dq\,d\omega)
\text{ without the exponential weight}.
\end{aligned}
}
\]

Therefore finite enstrophy is compatible with a bounded nonzero recurrent tail datum.

---

## 3. M5-571 ergodic hard-tail density

On a nontrivial ergodic hard component, M5-571 defines

\[
C_3(A)
=
\int_0^1\int_{S^2}|A(q,\omega)|^3d\omega\,dq.
\]

The zero mean case would force the factor profile to vanish, contradicting the retained nontrivial hard component.

Hence

\[
\boxed{
c_3:=\int C_3\,d\nu>0.
}
\]

By Birkhoff,

\[
\boxed{
\frac1L
\int_0^L\int_{S^2}|A(q,\omega)|^3d\omega\,dq
\longrightarrow c_3>0
}
\]

for almost every profile in the ergodic hard component.

M5-571 likewise obtains positive mean terminal-vorticity density

\[
\boxed{
c_\omega>0.}
\]

---

## 4. The hard tail is not an asymptotically vanishing log-radius process

The preceding limit immediately excludes

\[
\int_0^L\int_{S^2}|A|^3=o(L).
\]

Thus

\[
\boxed{
\text{nontrivial ergodic hard tail}
\not\Rightarrow
\text{sublinear cubic tail action};
}
\]

rather,

\[
\boxed{
\int_0^L\int_{S^2}|A|^3
\sim c_3L
}
\]

in ergodic mean.

Equivalently, strong \(L^3\) fails at a definite positive log-radius density, not merely on a sparse sequence of exceptional shells.

---

## 5. Positive cubic density also yields persistent L2-active cells

The retained compact regular tail class provides a uniform local amplitude ceiling

\[
|A|\le M_A
\]

on the factor component.

Therefore pointwise

\[
|A|^3\le M_A|A|^2.
\]

Hence on any unit cell

\[
\int|A|^2
\ge
M_A^{-1}\int|A|^3.
\]

Since the long-time/log-radius average of the cubic cell action is positive, there is a positive-density family of log-radius cells with nontrivial square amplitude.

In particular there exists \(\delta_2>0\) and infinitely many cell indices \(n\) such that

\[
\boxed{
\int_n^{n+1}\int_{S^2}|A|^2d\omega\,dq
\ge\delta_2.
}
\]

Thus the finite-energy-compatible linear radial tail identified in M19-265 is genuinely active on infinitely many exponentially separated physical shells of the hard factor.

---

## 6. Consequence for the sublinear normalized-energy target

For one active cell \(q\in[n,n+1]\), the radial interval is

\[
r\in[e^n,e^{n+1}].
\]

Since

\[
|U_0|^2dx
=
|A(q,\omega)|^2dr\,d\omega
=
e^q|A(q,\omega)|^2dq\,d\omega,
\]

the cell contributes at least

\[
\gtrsim e^n\delta_2
\]

to normalized kinetic energy.

At \(R_n=e^{n+1}\),

\[
\boxed{
\frac{1}{R_n}
\int_{1<|y|<R_n}|U_0|^2dy
\gtrsim e^{-1}\delta_2
}
\]

along infinitely many active radii.

Therefore

\[
\boxed{
E_{tail}^{norm}(R)=o(R)
}
\]

cannot hold along **all** large radii on the nontrivial ergodic hard component.

This does not prove a uniform positive lower bound for every radius; arbitrarily long inactive gaps are not excluded by ergodic mean alone.

---

## 7. Why this still does not contradict finite physical energy

At first-hitting scale \(r_j\), normalized radius \(R\sim r_j^{-1}\) corresponds to fixed macroscopic physical radius.

An order-\(R\) normalized kinetic-energy tail therefore costs physical energy

\[
r_jR\sim O(1).
\]

Hence positive log-radius density of the critical tail remains compatible with finite physical kinetic energy.

The new result is not an energy contradiction.

It is a classification:

\[
\boxed{
\text{the surviving hard R-critical branch is a genuinely persistent stationary tail, not a decaying tail.}
}
\]

---

## 8. The next closure mechanism must use the PDE balance

M5-571 already proposed the correct next direction: derive a renormalized local energy/enstrophy balance on one log-radius cell and test whether a stationary positive-density terminal-vorticity process can be maintained without a nonzero mean source or flux forbidden by the available budgets.

The M19 audit now independently arrives at the same frontier.

Thus the low-frequency program should no longer prioritize proving

\[
A(q)\to0
\]

or sublinear tail energy on the retained hard component.

Instead define

\[
\boxed{
\mathcal T_{tail}^{balance}:
\text{stationary positive-density }A,B_A
\text{ are incompatible with the exact renormalized NS shell balance unless an explicit root exit occurs.}
}
\]

---

## 9. Required source/flux classification

For one log-radius cell, every nonzero mean sustaining term should be typed as one of:

1. radial/local energy flux through the cell boundaries;
2. pressure work;
3. viscous transfer/dissipation;
4. nonlinear angular transfer;
5. active core-to-tail export;
6. remote/source injection;
7. terminal realization or trace defect.

If all sustaining terms are exact coboundaries or have zero invariant mean, positive stationary tail density would be impossible.

If one has nonzero mean, that term becomes the explicit R-critical payer/root.

This avoids pretending that recurrence itself is a contradiction.

---

## 10. Relation to M19-262 epsilon-smallness

M19-262 left the alternative

\[
\mathcal T_\varepsilon^{crit}
\lor
\mathcal E_{crit-floor}.
\]

The present hard-tail result naturally belongs to the second side:

\[
\boxed{
\text{nontrivial ergodic hard tail}
\subset
\mathcal E_{crit-floor}
\text{ / persistent critical activity}.
}
\]

Hence epsilon-smallness is not expected to arise internally from decay of this specific hard factor.

Any smallness route must first leave the positive-density hard-tail factor or show that the physical singularity cannot realize it.

---

## 11. Permanent firewalls after M19-266

\[
\boxed{
\text{positive ergodic tail density}
\neq
\text{finite-energy contradiction}.
}
\]

\[
\boxed{
\text{finite enstrophy}
\text{ is compatible with nonzero stationary critical scattering data}.
}
\]

\[
\boxed{
\text{strong }L^3\text{ failure is positive-density in log radius on the hard factor}.
}
\]

\[
\boxed{
\text{sublinear tail decay is not the surviving ergodic-hard mechanism}.
}
\]

\[
\boxed{
\text{the next closure target is a renormalized PDE flux/source balance.}
}
\]

---

## 12. Immediate next target

Reopen the M5-571 post-frontier and subsequent shell-balance modules, if any, and determine whether the stationary log-radius process already has an exact one-cell energy/enstrophy identity with an invariant-mean source classification.

If such a balance exists, import its strongest audited form into M19 and identify the exact surviving nonzero mean payer.

Global 3D Navier--Stokes regularity remains unproved.
