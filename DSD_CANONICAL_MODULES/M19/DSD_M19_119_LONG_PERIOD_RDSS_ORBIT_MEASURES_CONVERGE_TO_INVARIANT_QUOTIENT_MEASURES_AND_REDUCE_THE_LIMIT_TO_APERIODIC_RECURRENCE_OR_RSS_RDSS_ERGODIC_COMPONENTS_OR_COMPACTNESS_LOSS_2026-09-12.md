# DSD M19-119 — Long-period RDSS orbit measures converge to invariant quotient measures and reduce the limit to aperiodic recurrence or RSS/RDSS ergodic components or compactness loss

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / LONG-PERIOD RDSS REFORMULATED BY PERIODIC-ORBIT INVARIANT MEASURES ON THE ROTATION QUOTIENT / THIS AVOIDS MISLEADING POINTWISE HETEROCLINIC LIMITS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Long-period RDSS sequence

Consider a sequence of RDSS similarity solutions

\[
U_n(s+S_n)=Q_n\cdot U_n(s),
\qquad
S_n\to\infty,
\qquad
Q_n\in SO(3).
\]

Assume first that the sequence remains inside one retained compact smooth Type-I corridor.

If this compactness fails, record immediately the already-typed branch

\[
\boxed{G_{compactness\ loss}.}
\]

The rest of this module works on the compact branch.

---

## 2. Pass to the rotation quotient

Let

\[
\mathcal X
\]

be the retained compact phase space and let

\[
\widehat{\mathcal X}:=\mathcal X/SO(3)
\]

be the rotation quotient.

Because the similarity Navier--Stokes flow is rotation-equivariant, it induces a continuous quotient flow

\[
\widehat\Phi_t:\widehat{\mathcal X}\to\widehat{\mathcal X}.
\]

Write

\[
\widehat U_n(s):=[U_n(s)].
\]

The RDSS relation becomes ordinary periodicity in the quotient:

\[
\boxed{
\widehat U_n(s+S_n)=\widehat U_n(s).
}
\]

The actual least quotient period may divide `S_n`; this does not affect the orbit-measure construction.

---

## 3. Periodic-orbit probability measure

Define

\[
\boxed{
\mu_n
:=
\frac1{S_n}
\int_0^{S_n}\delta_{\widehat U_n(s)}\,ds.
}
\]

For every continuous observable `f` on the compact quotient and every time shift `tau`, periodicity gives exactly

\[
\begin{aligned}
\int f\circ\widehat\Phi_\tau\,d\mu_n
&=
\frac1{S_n}
\int_0^{S_n}
 f(\widehat U_n(s+\tau))\,ds\\
&=
\frac1{S_n}
\int_0^{S_n}
 f(\widehat U_n(s))\,ds.
\end{aligned}
\]

Hence

\[
\boxed{
(\widehat\Phi_\tau)_*\mu_n=\mu_n
\qquad\forall\tau\in\mathbb R.
}
\]

Thus every long-period RDSS orbit already defines an **exact invariant probability measure** on the rotation quotient.

---

## 4. Compactness gives an invariant limiting measure

Since the quotient corridor is compact, the family of probability measures is weak-* compact.

After passing to a subsequence,

\[
\boxed{
\mu_n\stackrel{*}{\rightharpoonup}\mu.
}
\]

For continuous `f`, invariance passes to the limit:

\[
\int f\circ\widehat\Phi_\tau\,d\mu
=
\int f\,d\mu.
\]

Therefore

\[
\boxed{
\mu\text{ is an invariant probability measure of the quotient NS flow.}
}
\]

This conclusion is more robust than extracting one pointwise orbit limit.

---

## 5. Ergodic decomposition

Apply the ergodic decomposition theorem:

\[
\boxed{
\mu
=
\int\mu_\xi\,d\pi(\xi),
}
\]

where each `mu_xi` is an ergodic invariant probability measure.

By Poincare recurrence, for every ergodic component

\[
\mu_\xi\text{-a.e. state is recurrent}.
\]

Therefore the long-period problem reduces to recurrent ergodic components rather than arbitrary pointwise complete limits.

---

## 6. Atom implies quotient equilibrium

Suppose an ergodic invariant component has an atom at a state `x` with positive mass.

Invariance gives the same positive atomic mass to every point on the continuous orbit

\[
\{\widehat\Phi_t x:t\in\mathbb R\}.
\]

A nonstationary continuous orbit contains uncountably many distinct points, which is impossible for a probability measure carrying the same positive atomic mass at each point.

Hence an atomic ergodic component must satisfy

\[
\boxed{
\widehat\Phi_t x=x
\qquad\forall t.
}
\]

Thus

\[
\boxed{
\text{atomic quotient ergodic component}
\Longrightarrow
\text{relative equilibrium / RSS in the full flow}.
}
\]

---

## 7. Non-atomic ergodic components

A non-atomic ergodic invariant measure has two relevant possibilities:

1. it is the invariant orbit measure on a finite-period quotient orbit;
2. it is supported on genuinely aperiodic recurrent quotient dynamics.

The first lifts to RDSS.

The second returns exactly to the live aperiodic recurrent theorem frontier.

Hence

\[
\boxed{
\text{non-atomic ergodic component}
\Longrightarrow
\mathcal R_{RDSS}^{finite\ period}
\lor
\mathcal R_{aperiodic}^{recurrent}.
}
\]

No claim is made that every non-atomic ergodic measure is supported on one periodic orbit; that is precisely why the aperiodic alternative is retained.

---

## 8. Long period does not automatically imply an aperiodic limit

Even though

\[
S_n\to\infty,
\]

the invariant measures `mu_n` may converge to:

- an RSS Dirac measure;
- a finite-period RDSS orbit measure;
- a convex mixture of several invariant ergodic components;
- or a genuinely aperiodic invariant measure.

A long periodic orbit may spend increasingly long epochs near several shorter recurrent objects while transition times occupy negligible asymptotic fraction.

Therefore

\[
\boxed{
S_n\to\infty
\not\Rightarrow
\text{aperiodic recurrent limit}.
}
\]

This is an important firewall.

---

## 9. Correct classification of the compact long-period branch

Combining the preceding steps gives

\[
\boxed{
\begin{aligned}
\mathcal R_{S\to\infty}
\Longrightarrow{}&
G_{compactness\ loss}\\
&\lor G_{RSS\ ergodic}\\
&\lor G_{finite\text{-}period\ RDSS\ ergodic}\\
&\lor G_{aperiodic\ recurrent\ ergodic}.
\end{aligned}
}
\]

The last branch returns to the finite-dimensional extra-center theorem of M19-102.

The first two structured branches return to the RSS/RDSS Liouville hard cores of M19-104--118.

Thus long-period RDSS is **not a new independent solution class** once invariant measures are used.

---

## 10. Why the measure method is preferable to a pointwise limit

A pointwise sequence of long-period orbits can converge locally to a heteroclinic or other nonrecurrent complete orbit.

That is not the right object for recurrence-based classification.

The period-average measure removes this ambiguity:

- transition segments whose relative duration tends to zero disappear from the measure;
- the limit remains invariant;
- ergodic decomposition automatically extracts recurrent components.

Therefore

\[
\boxed{
\text{long-period RDSS}
\to
\text{invariant-measure genealogy}
}
\]

is the representation-safe route.

---

## 11. Conditional consequence of the extra-center theorem

If M19-102's live theorem

\[
E^c_{extra}=0
\]

and the center-manifold bridge of M19-103 are established on every ergodic recurrent component in the compact corridor, then the genuinely aperiodic alternative disappears.

Every ergodic component of `mu` is then RSS or finite-period RDSS.

Thus

\[
\boxed{
E^c_{extra}=0
\Longrightarrow
\mu\text{ is a barycenter of RSS/RDSS invariant measures}
}

on the retained compact long-period branch.

This still does **not** imply that the original long-period orbit itself equals one of those shorter objects.

---

## 12. Next target

The remaining question becomes a transition/shadowing problem:

can one periodic orbit of period

\[
S_n\to\infty
\]

spend almost all of its time near a finite collection or distribution of isolated RSS/RDSS invariant sets while connecting them through increasingly negligible transition windows?

The next module should determine what such switching requires in terms of:

- stable/unstable manifolds of the finite-dimensional recurrent core;
- extra unit/zero exponents;
- or loss of a uniform hyperbolicity/compactness gap.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
