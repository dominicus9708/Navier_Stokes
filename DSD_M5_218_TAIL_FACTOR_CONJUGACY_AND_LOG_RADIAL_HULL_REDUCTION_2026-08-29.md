# DSD M5-218 — Tail-Factor Conjugacy and Log-Radial Hull Reduction

Date: 2026-08-29

Parent: `DSD_M5_217_LINEARIZED_NS_CARLEMAN_MATCH_AND_FLAT_FIBER_CLOSURE_2026-08-29.md`

Status: **POSITIVE TOPOLOGICAL REDUCTION / THE CONTINUOUS CANONICAL-TAIL FACTOR OF M5-114 IS NOW INJECTIVE BY M5-217, HENCE ON THE COMPACT MINIMAL W1 SET IT IS A HOMEOMORPHISM ONTO ITS COMPACT TAIL IMAGE / THE ENTIRE W1 LERAY DYNAMICS IS THEREFORE TOPOLOGICALLY CONJUGATE TO PURE DILATION OF THE CANONICAL PASSIVE TAIL / IN LOG-RADIUS VARIABLES THIS IS JUST TRANSLATION OF ONE BOUNDED LOCAL-L3 PROFILE / PERIODIC/DSS TAILS ARE ONLY ONE SUBCLASS; APERIODIC MINIMAL TRANSLATION HULLS REMAIN POSSIBLE AND ARE NOT SILENTLY EXCLUDED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Imported factor theorem

Let

\[
M
\]

be the compact minimal W1 invariant set with Leray flow

\[
S(\tau):M\to M.
\]

M5-114 constructs the canonical-tail map

\[
\boxed{
\mathfrak T:M\to\mathcal T,
\qquad
\mathfrak T(V)=T_V,
}
\]

which is continuous for local `L3` convergence on the punctured space.

Its image

\[
\mathcal T:=\mathfrak T(M)
\]

is compact.

The exact covariance is

\[
\boxed{
\mathfrak T(S(\tau)V)
=D_\tau\mathfrak T(V),
}
\]

where

\[
\boxed{
(D_\tau T)(Y)
=e^{-\tau/2}T(e^{-\tau/2}Y).
}
\]

---

## 2. Injectivity is now proved on the audited W1 class

M5-217 closes the only surviving same-tail fiber alternative:

\[
\boxed{
T_V=T_W
\Longrightarrow
V=W.
}
\]

Thus

\[
\boxed{
\mathfrak T\text{ is injective on }M.
}
\]

Since it is surjective by definition onto `mathcal T`,

\[
\mathfrak T:M\to\mathcal T
\]

is a continuous bijection.

The domain `M` is compact and the local-`L3` tail space is Hausdorff.

Therefore

\[
\boxed{
\mathfrak T:M\overset{\cong}{\longrightarrow}\mathcal T
}
\]

is a homeomorphism.

Status: **PROVED.**

---

## 3. Exact dynamical conjugacy

The covariance now becomes a conjugacy identity rather than merely a factor identity:

\[
\boxed{
D_\tau
=
\mathfrak T\circ S(\tau)\circ\mathfrak T^{-1}.
}
\]

Hence

\[
\boxed{
(M,S)
\cong
(\mathcal T,D).
}
\]

Every recurrent, periodic, aperiodic, minimal, or return property of the W1 dynamics has an equivalent tail-dilation formulation.

There is no longer any hidden strong-critical core degree of freedom above one fixed tail.

---

## 4. Log-radius representation

For a tail `T`, define the scale-neutral log-radius profile

\[
\boxed{
\Phi_T(y,\theta)
:=
e^yT(e^y\theta),
\qquad
y\in\mathbb R,
\quad
\theta\in S^2.
}
\]

Equivalently,

\[
T(r\theta)
=
\frac1r\Phi_T(\log r,\theta).
\]

Under the dilation flow,

\[
\begin{aligned}
\Phi_{D_\tau T}(y,\theta)
&=e^y(D_\tau T)(e^y\theta)\\
&=e^{y-\tau/2}T(e^{y-\tau/2}\theta)\\
&=\Phi_T(y-\tau/2,\theta).
\end{aligned}
\]

Thus

\[
\boxed{
\Phi_{D_\tau T}(y,\theta)
=\Phi_T(y-\tau/2,\theta).
}
\]

The W1 Leray-time dynamics is therefore exactly translation in the tail log-radius coordinate.

---

## 5. Minimal tail hull

Choose one state `V0 in M` and set

\[
\Phi_0:=\Phi_{T_{V_0}}.
\]

Minimality of `M` and conjugacy imply

\[
\boxed{
\mathcal H(\Phi_0)
:=
\overline{\{\Phi_0(\cdot-a,\cdot):a\in\mathbb R\}}
}
\]

in the inherited local critical topology is minimal under translations.

Moreover every tail in `mathcal T` is one element of this hull.

Thus the entire surviving W1 recurrent dynamics has been reduced to one **log-radial translation hull**.

---

## 6. Periodic case

If there exists `L>0` such that

\[
\Phi_0(y+L,\theta)=\Phi_0(y,\theta),
\]

then

\[
D_{2L}T=T.
\]

By conjugacy,

\[
\boxed{
S(2L)V=V.
}
\]

Hence a log-periodic tail is exactly a periodic Leray state, equivalently a backward DSS candidate in physical variables.

This branch is already connected to the periodic/DSS audits and their critical-tail restrictions.

---

## 7. Constant log profile

If

\[
\partial_y\Phi_0=0,
\]

then

\[
T(r\theta)=r^{-1}\Phi_0(\theta)
\]

is exactly `(-1)`-homogeneous.

The conjugate W1 orbit is stationary:

\[
D_\tau T=T
\quad\forall\tau
\Longrightarrow
S(\tau)V=V.
\]

The stationary alpha-limit/self-similar branch has already been excluded on the relevant suitable local-energy corridor.

---

## 8. Critical firewall: compact minimal translation hull need not be periodic

A compact minimal translation hull does **not** imply periodicity.

Abstract translation/shift dynamics admits aperiodic minimal hulls.

Therefore the implication

\[
\boxed{
\text{compact + minimal + injective tail factor}
\not\Rightarrow
\text{DSS/periodic}
}
\]

is RED.

The remaining nonperiodic possibility is

\[
\boxed{
\Phi_0\text{ has an aperiodic minimal log-radial hull}.
}
\]

This is now the exact tail form of the previously vague aperiodic similarity survivor.

---

## 9. What PDE information is and is not inherited by the passive tail

The canonical tail was constructed as the asymptotic passive critical part of actual W1 states.

It obeys

- divergence-free constraints;
- critical `1/r` scaling size;
- exact dilation covariance;
- compact-hull regularity inherited from W1.

However the repository has **not** proved that an arbitrary canonical tail by itself solves the stationary Navier–Stokes equation or a closed elliptic equation on the log cylinder.

Therefore one may not apply stationary homogeneous classification directly to every element of `mathcal T`.

The PDE continues to act through the unique reconstructed W1 state

\[
V=\mathfrak T^{-1}(T).
\]

---

## 10. New aperiodic rigidity target

Because the tail is now a complete code for the W1 state, the unresolved nonperiodic branch can be stated purely as:

\[
\boxed{
\begin{array}{c}
\Phi(y,\theta)\text{ generates a compact aperiodic minimal translation hull},\\
T(r\theta)=r^{-1}\Phi(\log r,\theta),\\
\mathfrak T^{-1}(T)\text{ is a smooth nontrivial recurrent W1 Leray state}
\end{array}
}
\]

Can this occur while satisfying all existing Type-I, Morrey, first-hitting, and suitable-solution constraints?

This is a substantially narrower question than arbitrary recurrent Leray motion.

---

## 11. DSD audit

### Formation — GREEN

The tail map existed and was continuous before injectivity was inserted.

### Axis — GREEN

Leray time and log radius are related by conjugacy but are not identified before the map is proved bijective.

### Static aggregation — GREEN

Fiber closure is used exactly once to upgrade factor to conjugacy.

### Dynamics — GREEN REDUCTION / APERIODIC HULL OPEN

The remaining dynamic freedom is entirely tail-log-translation freedom.

### Cross-audit — GREEN

No abstract minimal-dynamics theorem is misused to force periodicity.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]