# DSD M5-05 — Cross-Characteristic Coherence Target

Date: 2026-08-26

Status: **M5 SUBSTEP / A SINGLE FAR LERAY DILATION CHARACTERISTIC IS DYNAMICALLY HARMLESS AND CORRESPONDS TO ONE FIXED PHYSICAL RADIUS / THE LARGE-WEAK-CRITICAL SURVIVOR REQUIRES A COHERENT FAMILY OF SUCH CHARACTERISTICS DOWN TO PHYSICAL RADIUS ZERO / THIS CROSS-CHARACTERISTIC COHERENCE IS THE NEW LIVE TARGET / GLOBAL REGULARITY UNPROVED.**

## 1. Far Leray dilation mode

Consider the far-field critical profile

\[
U(Y,s)=R(s)^{-1}\phi(Y/R(s))
\]

with

\[
\frac{R'(s)}{R(s)}=\frac12.
\]

A direct differentiation gives

\[
\boxed{
\partial_sU+\frac12U+\frac12Y\cdot\nabla U=0.
}
\]

Thus the linear Leray dilation operator transports this profile exactly.

The viscous and nonlinear terms scale as

\[
\nu\Delta U=O(R^{-3}),
\qquad
(U\cdot\nabla)U+\nabla P=O(R^{-3}).
\]

Therefore at large `R` one such critical packet is an asymptotically passive far-field mode. This is consistent with the previously proved all-age comoving transport estimates.

---

## 2. Physical meaning of one characteristic

Let

\[
\tau=T_*-t=e^{-s}.
\]

The Leray/physical relation is

\[
Y=\frac{x-X_*}{\sqrt\tau},
\qquad
U=\sqrt\tau\,u.
\]

Since

\[
R(s)=Ce^{s/2},
\]

its physical radius is

\[
\boxed{
r_{phys}=\sqrt\tau\,R(s)=C.
}
\]

Hence one far Leray characteristic is simply one fixed physical radius.

If its normalized amplitude is critical,

\[
|U|\sim R^{-1},
\]

then

\[
\boxed{
|u|\sim \tau^{-1/2}R^{-1}=C^{-1}.
}
\]

This physical amplitude is also constant along that one characteristic.

Therefore a single passive packet does **not** produce the `L -> infinity` tail required for a singular M5 survivor.

---

## 3. What a genuine large-critical survivor requires

To obtain arbitrarily large physical amplitudes one needs

\[
C\downarrow0.
\]

Thus the survivor requires a whole family of characteristics

\[
\{\Gamma_C:0<C\le C_0\}
\]

such that along the family

\[
\boxed{
|u|\asymp C^{-1}
}
\]

with enough coherence to produce the critical `1/r` state across physical radii approaching the candidate singular point.

In DSD language:

- one characteristic = one admissible physical-radius channel;
- the singular endpoint = compatibility of infinitely many such channels as the channel label `C` approaches the boundary `C=0`.

The unresolved object is therefore not one packet but the **cross-characteristic coherence relation**.

---

## 4. Why finite kinetic energy does not exclude the family

The static critical geometry

\[
|u(r)|\sim r^{-1}
\]

has local kinetic energy

\[
\int_0^{r_0}|u(r)|^2r^2dr
\sim
\int_0^{r_0}dr
<\infty.
\]

Thus finite `L2` energy is compatible with a coherent `1/r` family down to `r=0`.

The same geometry is not locally `H1`:

\[
|\nabla u|\sim r^{-2},
\qquad
\int_0^{r_0}|\nabla u|^2r^2dr
\sim
\int_0^{r_0}r^{-2}dr=\infty.
\]

Hence M5 cannot be closed by kinetic energy alone; it must prevent formation of this cross-radius coherence before the endpoint.

---

## 5. Relation to earlier diagonal audit

The earlier periodic-parent audit correctly rejected automatic inheritance of a periodic omega-limit tail on a fixed physical annulus. The present formulation explains why.

Fixed Leray compactness controls one order of limits, while a physical-radius family approaching `C=0` requires a joint limit across

\[
s\to\infty,
\qquad
R\sim Ce^{s/2},
\qquad
C\downarrow0.
\]

Therefore the missing theorem is a **cross-characteristic / parent-lineage theorem**, not ordinary fixed-`R` compactness.

---

## 6. Refined M5 target

The previous M5 sufficient condition remains

\[
\lim_{L\to\infty}\sup_{t<T_*}K_L^{phys}(t)=0.
\]

The present step rewrites its dynamical meaning:

\[
\boxed{
\textbf{exclude a coherent family of critical physical-radius channels }C\downarrow0.
}
\]

Equivalent useful targets include:

1. prove that critical `1/r` amplitude cannot persist uniformly over a continuum of shrinking physical radii;
2. prove a parent-lineage decorrelation estimate between sufficiently separated physical-radius channels;
3. show that cross-radius coherence forces a strong-critical quantity (for example local `L3` or `H1`) to diverge too early / violate continuation;
4. derive a scale-breaking monotonicity in the physical radius label `C` that prevents the `1/C` family.

---

## 7. M5 ledger after this step

- M5-01: time-average `K` decay exists, but spikes fit finite energy/dissipation.
- M5-02: one-event parabolic persistence is too short.
- M5-03: instantaneous pressure-pump absorption is circular or requires new dynamic input.
- M5-04: `Lp`, `p>3`, compactness does not see the critical joint-boundary dilation mode.
- M5-05: one dilation characteristic is harmless; the actual singular survivor requires **cross-characteristic coherence down to physical radius zero**.

Thus the next step should investigate a radius-to-radius identity or monotonicity for the parent solution rather than another fixed-scale estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
