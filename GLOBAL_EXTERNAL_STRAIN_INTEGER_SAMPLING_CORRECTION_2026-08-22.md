# Global External-Strain Sampling: Mandatory One-Cell Correction — 2026-08-22

Status: **GLOBAL FINITE-ENERGY FREQUENCY-LOCALITY REDUCTION / GLOBAL REGULARITY NOT PROVED.**

This note sharpens the earlier packet-multiplicity external-strain sampling estimate by retaining the trivial but important integer constraint that at least one responsible strain cell is required whenever even one active packet is stretched.

## 1. Terminal scale

Let

\[
K=\sqrt W,
\qquad
\ell=K^{-1}
\]

be the physical first-hitting frequency and natural packet radius.

Suppose a lower-frequency velocity field

\[
v=u_{\le L}
\]

supplies a fixed fraction of the required order-`K^2` extensional strain to at least one natural active packet.

Write

\[
\boxed{L=K/R},
\qquad R\ge1.
\]

The physical strain-cell radius is `R/K`.

## 2. Bandlimited gradient sampling

For an `L`-bandlimited field and an `L^{-1}`-separated set of responsible strain-cell centers,

\[
\sum_{i=1}^{M}|\nabla v(x_i)|^2
\lesssim
L^5\|v\|_2^2.
\]

If every responsible cell supplies

\[
|\nabla v(x_i)|\gtrsim cK^2,
\]

then

\[
MK^4\lesssim L^5\|u\|_2^2,
\]

so

\[
\boxed{
\|u\|_2^2
\gtrsim
M\frac{R^5}{K}.
}
\]

## 3. Mandatory integer correction

If at least one packet is being stretched by this lower-frequency field, then there is at least one responsible strain cell:

\[
\boxed{M\ge1.}
\]

Therefore, independently of packet multiplicity,

\[
\boxed{
\|u\|_2^2
\gtrsim
\frac{R^5}{K}.
}
\]

Since the physical kinetic energy is uniformly bounded by the initial energy,

\[
\|u(t)\|_2^2\le E_0,
\]

we obtain

\[
\boxed{
R
\lesssim
C_EK^{1/5}.
}
\]

Equivalently,

\[
\boxed{
L=K/R
\gtrsim
c_EK^{4/5}.
}
\]

Since `K=sqrt(W)`, this is

\[
\boxed{
R_{freq}\lesssim W^{1/10},
\qquad
L_{responsible}\gtrsim W^{2/5}.
}
\]

Thus a genuinely low-frequency common amplifier separated from the terminal scale by more than `K^(1/5)` cannot supply order-one normalized strain even to a single active natural packet without violating finite kinetic energy.

## 4. Multiplicity-aware piecewise bound

If `N` bounded-overlap natural packets are served, one strain cell of radius `R/K` can cover at most `O(R^3)` natural packet cells. Hence

\[
\boxed{
M\gtrsim\max\left\{1,\frac{N}{R^3}\right\}.
}
\]

Substituting into the energy sampling bound gives two regimes.

### Regime A: `N <= R^3`

Then the integer floor dominates:

\[
M\gtrsim1,
\]

and

\[
\boxed{R\lesssim C_EK^{1/5}.}
\]

### Regime B: `N >= R^3`

Then

\[
M\gtrsim N/R^3,
\]

so

\[
\|u\|_2^2
\gtrsim
\frac{NR^2}{K},
\]

and therefore

\[
\boxed{
R\lesssim C_E\sqrt{K/N}.
}
\]

The two regimes meet when

\[
N\sim R^3,
\qquad
R\sim K^{1/5},
\]

which gives

\[
\boxed{
N\sim K^{3/5},
\qquad
R\sim K^{1/5},
\qquad
L\sim K^{4/5}.
}
\]

Thus the previously identified `3/5-1/5-4/5` ridge remains the transition point, but the corrected result adds a universal one-packet bound `R <= O(K^(1/5))` on the low-multiplicity side.

## 5. Combined interpretation with the remote-action gate

The new remote-action packing note gives a spatial condition for infinitely recurring bounded-time active halos:

\[
R_{space}=o(W^{5/14})
\]

or, physically,

\[
d=o(W^{-1/7}).
\]

The present sampling correction gives an independent frequency condition on a lower-frequency responsible amplifier:

\[
R_{freq}\lesssim W^{1/10}.
\]

These are different notions of scale separation and must not be identified. Together they say that a surviving external-stretching mechanism must become both

1. spatially concentrated toward the singular center; and
2. frequency-local relative to the terminal first-hitting scale.

The unresolved survivor is therefore not a cheap large-scale common amplifier. It is a near-field, high-frequency, same-scale or nearly same-scale interaction cascade.

## 6. Scope

This sampling result applies when a fixed fraction of the packet stretching is supplied by a genuinely lower-frequency field `u_{<=L}`. If the required strain instead comes from frequencies above `L`, that contribution is routed to the same-scale/high-high interaction branch.

It does not by itself exclude a near-field high-frequency packet cascade.

Status: **FINITE KINETIC ENERGY FORCES ANY LOWER-FREQUENCY FIELD THAT SUPPLIES ORDER-ONE TERMINAL STRAIN TO OBEY `R_freq <= O(K^(1/5))`, EVEN FOR A SINGLE ACTIVE PACKET. WITH MULTIPLICITY, THE OLD `3/5-1/5-4/5` RIDGE IS RECOVERED. THE GLOBAL SURVIVOR IS FORCED TOWARD SPATIALLY NEAR, FREQUENCY-LOCAL HIGH-HIGH INTERACTION.**