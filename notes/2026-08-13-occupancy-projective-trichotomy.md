# Occupancy--projective trichotomy for an intense vorticity core

Date: 2026-08-13

Status: **DERIVED LOCAL PROBABILITY/COVARIANCE LEMMA / OPEN POINTWISE-COHERENCE TRANSFER**.

This note intersects the intense-vorticity occupancy channel with the local projective covariance channel.

The result is a local structural trichotomy:

1. the intense core is sparse;
2. the intense core is enstrophy-dominant and approximately one-axis in an averaged projective sense;
3. the intense core retains substantial multi-axis disorder, forcing a non-small projective defect and hence activating projective viscous cost.

No pointwise vorticity-direction regularity theorem is inferred from the averaged statement without an additional concentration argument.

## 1. Local enstrophy probability measure

Fix center `z` and scale `r`. Define

\[
E_r(z)
=\int\eta_r(z-y)|\omega(y)|^2dy.
\]

When `E_r(z)>0`, define the probability measure

\[
\boxed{
d\mu_{z,r}(y)
=
\frac{\eta_r(z-y)|\omega(y)|^2}{E_r(z)}dy.
}
\]

Let

\[
\xi(y)=\omega(y)/|\omega(y)|
\]

on the support of this measure.

Then

\[
C_r(z)
=\int\xi(y)\otimes\xi(y)d\mu_{z,r}(y).
\]

Let `n_r(z)` be a principal axis of `C_r` and

\[
\Pi_r=1-\mu_1(C_r).
\]

Exactly,

\[
\boxed{
\Pi_r
=\int|n_r\times\xi(y)|^2d\mu_{z,r}(y).
}
\]

Also

\[
\boxed{
\frac12J_r\le\Pi_r\le\frac32J_r,
\qquad
J_r=1-\operatorname{tr}(C_r^2).
}
\]

## 2. Restrict to an intense core

Let `H` be any measurable subset of the local region and define its local enstrophy mass fraction

\[
\boxed{
h=\mu_{z,r}(H).}
\]

Assume `h>0`.

Then

\[
\int_H|n_r\times\xi|^2d\mu
\le\Pi_r.
\]

After conditioning on `H`,

\[
\boxed{
\frac1h
\int_H|n_r\times\xi|^2d\mu
\le
\frac{\Pi_r}{h}
\le
\frac{3J_r}{2h}.
}
\]

Thus a core carrying nontrivial enstrophy mass cannot remain strongly off-axis when `J_r` is small.

## 3. Angular bad-set estimate inside the core

For `0<theta<=1`, define

\[
B_\theta
=\{y\in H:|n_r\times\xi(y)|\ge\theta\}.
\]

Markov/Chebyshev gives

\[
\theta^2\mu(B_\theta)
\le
\int_H|n_r\times\xi|^2d\mu
\le\Pi_r.
\]

Therefore the conditional bad-angle fraction satisfies

\[
\boxed{
\frac{\mu(B_\theta)}{h}
\le
\frac{\Pi_r}{h\theta^2}
\le
\frac{3J_r}{2h\theta^2}.
}
\]

Hence if

\[
J_r\ll h\theta^2,
\]

most of the intense-core enstrophy lies within projective angle `theta` of the local principal axis.

This is an averaged/enstrophy-weighted statement, not a pointwise Hölder coherence condition.

## 4. Pairwise projective defect inside the core

Define the conditional pairwise defect

\[
\boxed{
J_{HH}
=
\frac1{h^2}
\iint_{H\times H}
\left[
1-(\xi(y)\cdot\xi(y'))^2
\right]
d\mu(y)d\mu(y').
}
\]

The full local projective defect is

\[
J_r
=
\iint
\left[
1-(\xi(y)\cdot\xi(y'))^2
\right]
d\mu(y)d\mu(y').
\]

The integrand is nonnegative, so restricting to `H x H` gives

\[
\boxed{
J_r\ge h^2J_{HH}.
}
\]

Equivalently,

\[
\boxed{
J_{HH}\le\frac{J_r}{h^2}.
}
\]

Conversely, if the intense core has conditional pairwise disorder

\[
J_{HH}\ge\delta>0,
\]

then

\[
\boxed{
J_r\ge h^2\delta.
}
\]

## 5. Connect volume occupancy to enstrophy mass

Let

\[
W=\|\omega\|_\infty
\]

at the time under consideration and define an intense set

\[
H_a=\{|\omega|\ge aW\}
\]

with `0<a<1`.

Assume we inspect an inner ball `B_{c r}(z)` on which the positive kernel obeys

\[
\eta_r(z-y)\ge c_\eta r^{-3}.
\]

Let

\[
\rho_{\rm vol}
=\frac{|H_a\cap B_{cr}(z)|}{r^3}.
\]

Since the normalized positive kernel gives

\[
E_r(z)\le W^2,
\]

we obtain

\[
\begin{aligned}
h
&\ge
\frac{a^2W^2}{E_r(z)}
\int_{H_a\cap B_{cr}(z)}\eta_r(z-y)dy\\
&\ge
c_\eta a^2\rho_{\rm vol}.
\end{aligned}
\]

Thus

\[
\boxed{
h\gtrsim a^2\rho_{\rm vol}.}
\]

A non-sparse intense core in physical volume therefore carries a nontrivial amount of the local enstrophy probability mass.

## 6. Local trichotomy

Fix thresholds

\[
\rho_0>0,
\qquad
\theta_0>0,
\qquad
\delta_0>0.
\]

At an active natural-scale ball, one of the following must occur.

### Branch A: sparse intense core

\[
\rho_{\rm vol}<\rho_0.
\]

This feeds the existing volume-to-line-sparseness / geometric regularity track.

### Branch B: occupied but projectively aligned core

\[
\rho_{\rm vol}\ge\rho_0
\]

and `J_r` is small.

Then `h>=c a^2 rho_0`, and

\[
\frac{\mu(B_{\theta_0})}{h}
\lesssim
\frac{J_r}{a^2\rho_0\theta_0^2}.
\]

Thus most intense-core enstrophy is aligned with the local covariance axis in the averaged projective sense.

The existing local covariance-axis lemma simultaneously makes this axis spatially stable when `J_r` is sufficiently small, but an additional step is still required to upgrade the averaged alignment to a known pointwise/mixed-norm regularity criterion.

### Branch C: occupied and projectively disordered core

If the conditional core disorder remains

\[
J_{HH}\ge\delta_0,
\]

then

\[
J_r\gtrsim a^4\rho_0^2\delta_0.
\]

The covariance coercivity in the energy-weighted derivative equation then forces a projective viscous cost at least quadratic in this defect.

Schematically,

\[
\boxed{
E_{k+1}J_k^2
\gtrsim
E_{k+1}a^8\rho_0^4\delta_0^2
}
\]

when the corresponding projective defect is measured at the same typed level.

For the local physical-scale version, the exact localization/cutoff terms must still be retained before promoting this schematic consequence to a local PDE inequality.

## 7. Why this is useful

The residual singular configuration cannot freely choose both density and directional disorder.

- If the intense set becomes too sparse, the geometric sparseness gate activates.
- If it stays dense but becomes projectively aligned, the local-axis branch activates.
- If it stays dense and projectively disordered, the projective defect is quantitatively bounded below and directional viscous dissipation cannot be arbitrarily weak.

This is the first direct intersection between the occupancy and covariance channels.

## 8. Remaining gap

The aligned branch is still only an **averaged enstrophy alignment** statement.

Classical Constantin--Fefferman / Beirao da Veiga--Berselli criteria use stronger pointwise or function-space control of vorticity direction, while Miller's criterion uses the mixed norm of `n x omega` plus spatial control of the plane field.

The next target is therefore to use

\[
\mu(B_\theta)/h
\ll1
\]

together with the previously established axis-gradient estimate and intense-set sparseness information to control the exceptional misaligned set in a norm strong enough for an external regularity criterion.

Status: **OPEN EXCEPTIONAL-SET ANISOTROPY CLOSURE**.
