# DSD M17-259 — Finite-time smooth ancient heat existence does not control backward Dirichlet growth

Date: 2026-09-06  
Canonical ID: **M17-259**

Status: **ANTI-SHORTCUT / M17-258 PROVES A GRADIENT LIOUVILLE THEOREM UNDER SUBEXPONENTIAL BACKWARD DIRICHLET GROWTH. THIS CONDITION CANNOT BE INFERRED FROM THE FACT THAT AN ANCIENT HEAT TANGENT IS SMOOTH AND HAS FINITE SOBOLEV NORM AT EVERY FINITE NEGATIVE TIME. AN EXPLICIT FOURIER-GAUSSIAN-OF-FOURTH-ORDER EXAMPLE IS NONZERO, ANCIENT, SCHWARTZ AT EVERY FINITE TIME, AND YET ITS BACKWARD `L2`/DIRICHLET NORMS GROW SUPEREXPONENTIALLY LIKE `exp(c T^2)`. A DIVERGENCE-FREE VECTOR VERSION IS OBTAINED BY MULTIPLYING BY `i xi cross e_1`. THEREFORE M17-254 FINITE-`T` CORRIDORS AND M17-255 FINITE-CYLINDER COMPACTNESS DO NOT BY THEMSELVES CLOSE THE PROJECTED CALORIC BRANCH. THE MISSING INPUT IS A TRUE BACKWARD GROWTH-RATE/GLOBAL-FREQUENCY RESTRICTION OR A RETURN OF THAT GROWTH TO AN EXISTING NAVIER--STOKES PAYER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scalar ancient heat example

Define at time `tau=0`

\[
\boxed{
\widehat f_0(\xi)=e^{-|\xi|^4}.
}
\]

For every `tau<=0`, set

\[
\boxed{
\widehat f(\xi,\tau)
=e^{-\tau|\xi|^2}\widehat f_0(\xi)
=e^{|\tau||\xi|^2-|\xi|^4}.
}
\]

Then

\[
\partial_\tau f=\Delta f
\]

for all finite negative times.

---

## 2. Every finite-time Sobolev norm is finite

Fix `T>0`. At `tau=-T`,

\[
|\widehat f(\xi,-T)|^2
=e^{2T|\xi|^2-2|\xi|^4}.
\]

Complete the square in `s=|xi|^2`:

\[
-2s^2+2Ts
=-2\left(s-\frac T2\right)^2+\frac{T^2}{2}.
\]

Hence for every finite derivative order `m`,

\[
\int_{\mathbb R^3}
(1+|\xi|^2)^m
 e^{2T|\xi|^2-2|\xi|^4}d\xi
<\infty.
\]

Therefore

\[
\boxed{
f(\cdot,-T)\in H^m(\mathbb R^3)
\quad\forall m<\infty,
\quad\forall T<\infty.
}
\]

Indeed `f` is Schwartz at every finite time.

---

## 3. Backward norm grows faster than exponentially

The exponent is maximized near

\[
|\xi|^2=\frac T2.
\]

There

\[
2T|\xi|^2-2|\xi|^4
=\frac{T^2}{2}.
\]

A fixed-width annular neighborhood of this maximizing radius therefore gives, up to polynomial factors in `T`,

\[
\boxed{
\|f(-T)\|_2^2
\gtrsim
 e^{cT^2}
}
\]

for some `c>0` and all sufficiently large `T`.

The same is true for the Dirichlet norm:

\[
\boxed{
\|\nabla f(-T)\|_2^2
\gtrsim
 T\,e^{cT^2}.
}
\]

Thus

\[
\limsup_{T\to\infty}
\frac1T\log\|\nabla f(-T)\|_2
=\infty.
\]

The M17-258 subexponential hypothesis fails maximally.

---

## 4. Divergence-free vector version

To preserve the vorticity-type divergence-free constraint, fix a constant unit vector `e_1` and define

\[
\boxed{
\widehat V(\xi,\tau)
:=i(\xi\times e_1)
 e^{-\tau|\xi|^2-|\xi|^4}.
}
\]

Then

\[
\xi\cdot\widehat V=0,
\]

so

\[
\boxed{\nabla\cdot V=0.}
\]

The field is nonzero, solves

\[
\partial_\tau V=\Delta V,
\]

is Schwartz at every finite negative time, and has the same superexponential backward Sobolev growth pattern.

Thus incompressibility does not remove the firewall.

---

## 5. Consequence for the M17 tangent program

M17-254 can provide, for each fixed `T`, a normalized mass corridor unless a payer occurs.

M17-255 can provide strong local spacetime compactness on every fixed cylinder.

M17-259 shows that these statements are compatible with a perfectly smooth nonzero ancient heat solution whose global Dirichlet norm grows arbitrarily fast backward.

Therefore

\[
\boxed{
\text{finite-}T\text{ smoothness/compactness}
\not\Rightarrow
\text{M17-258 Liouville growth condition}.
}
\]

---

## 6. Frequency interpretation

For any ancient heat solution,

\[
\widehat G(-T,\xi)
=e^{T|\xi|^2}\widehat G(0,\xi).
\]

Backward growth is therefore a direct measurement of how much nonzero frequency is present at `tau=0`.

Subexponential growth forces all frequency support to collapse to `xi=0`.

Conversely, any fixed nonzero frequency component creates at least exponential backward growth.

Hence the unresolved branch after M17-258 can be read as

\[
\boxed{
\text{nonzero projected caloric tangent}
\Longrightarrow
\text{persistent nonzero-frequency content}
\Longrightarrow
\text{backward normalized derivative growth}.
}
\]

The next task is to decide whether the original Navier--Stokes genealogy can sustain that growth without triggering an already recorded palinstrophy, ambient, coefficient, interface, or nodal/subscale branch.

---

## 7. DSD audit

1. This is a counterexample to an inference, not a Navier--Stokes counterexample.
2. The example is linear heat dynamics only.
3. Every finite-time Sobolev norm is finite; the failure is exclusively in the `T->infinity` growth rate.
4. Divergence-free structure can be imposed explicitly.
5. No claim is made that this heat example satisfies the CE-H multiplier relation inherited from the nonlinear branch.
6. That last distinction is the next possible source of additional rigidity.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
