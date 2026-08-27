# DSD M5-139 — Physical Terminal Smoothness Eliminates Half-Integer Sectors

Date: 2026-08-27

Status: **DYNAMICAL COMPLETION OF M5-138 / THE FUCHSIAN VARIABLE `z=r_L^-2` IS EXACTLY TERMINAL TIME DIVIDED BY FIXED PHYSICAL RADIUS SQUARED, WHILE `eta` IS PHYSICAL LOG-RADIUS / THE AUDITED SMOOTH TERMINAL EXTENSION ON EVERY PUNCTURED ANNULUS THEREFORE EXCLUDES ALL NONINTEGER PUiseux POWERS OF `z` / EVEN-SPHERICAL PRESSURE MULTIPOLES ARE POISSON-ADMISSIBLE BUT NOT REALIZABLE IN THE SMOOTH PUNCTURED W1 TERMINAL EXPANSION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inverse Leray variables

Let

\[
\tau:=T_*-t,
\qquad
s=-\log\tau
\]

up to the harmless fixed normalization used in the repository, and

\[
Y=\frac{x-x_*}{\sqrt\tau}.
\]

Then the Leray radius is

\[
r_L=|Y|
=\frac{|x-x_*|}{\sqrt\tau}.
\]

M5-136 defined

\[
z=r_L^{-2},
\qquad
\eta=\log r_L-\frac s2.
\]

Therefore

\[
\boxed{
z
=\frac{\tau}{|x-x_*|^2}.
}
\]

Also

\[
\begin{aligned}
\eta
&=\log|x-x_*|-\frac12\log\tau
-\frac12(-\log\tau)\\
&=\log|x-x_*|,
\end{aligned}
\]

again up to the fixed normalization constant.

Hence

\[
\boxed{
\eta=\log|x-x_*|+\text{constant}.
}
\]

This is a major interpretation: the Fuchsian coordinates are simply terminal-time depth relative to physical radius and physical logarithmic radius.

---

## 2. Meaning of `z -> 0`

At any fixed punctured physical point

\[
x\ne x_*,
\]

we have

\[
z\to0
\quad\Longleftrightarrow\quad
\tau\to0.
\]

Thus expansion in `z` at fixed `eta` is exactly terminal-time expansion at fixed nonzero physical radius, modulo powers of the constant spatial factor `|x-x_*|^-2`.

This identifies the M5-135 Fuchsian hierarchy with the punctured terminal Taylor hierarchy from the earlier physical audit.

---

## 3. Audited punctured terminal regularity

The existing W1 terminal-trace audit proved that on every compact annulus

\[
0<r_1\le|x-x_*|\le r_2<\infty,
\]

the physical W1 realization extends smoothly to

\[
t=T_*.
\]

In particular, for every finite integer `N` justified by local parabolic bootstrapping, velocity and pressure gradient possess finite one-sided terminal derivatives through order `N`.

Since `N` can be taken arbitrarily large on a fixed punctured compact set, the terminal fields are `C^infinity` in time there in the audited sense.

---

## 4. Half-integer Fuchsian terms contradict finite differentiability

Suppose a physical field contains a nonzero Fuchsian term

\[
z^{m+1/2}F(\eta,\theta),
\qquad m\ge0.
\]

At fixed physical `x != x_*`,

\[
z^{m+1/2}
=
\frac{\tau^{m+1/2}}
{|x-x_*|^{2m+1}}.
\]

A nonzero coefficient therefore produces a terminal-time dependence

\[
\tau^{m+1/2}.
\]

This fails to possess a finite derivative of sufficiently high integer order at `tau=0`.

For example,

\[
\tau^{1/2}
\]

already fails `C^1`, while

\[
\tau^{3/2}
\]

fails `C^2`, etc.

Because the punctured W1 solution has arbitrarily high finite terminal differentiability, every such coefficient must vanish.

Hence

\[
\boxed{
\text{all half-integer powers of }z\text{ vanish in the realized punctured terminal expansion.}
}
\]

The same argument excludes any noninteger algebraic Puiseux exponent.

---

## 5. Consequence for pressure multipoles

M5-138 showed an `ell`th decaying harmonic pressure multipole has relative Fuchsian power

\[
z^{(\ell-1)/2}.
\]

### Even `ell`

If `ell=2k`, then

\[
\frac{\ell-1}{2}=k-\frac12
\]

is half-integer.

Therefore every even-degree harmonic pressure multipole

\[
\boxed{\ell=2,4,6,\ldots}
\]

is excluded from the smooth realized punctured W1 terminal expansion.

### Odd `ell`

If `ell=2k+1`, then

\[
\frac{\ell-1}{2}=k
\]

is integer.

Thus

\[
\boxed{\ell=1,3,5,7,\ldots}
\]

remain compatible with terminal smoothness.

This restores the M5-137 odd tower, now with the correct **dynamical** justification rather than an unjustified restriction to integer powers.

---

## 6. Velocity corrections

A pressure multipole of degree `ell` has gradient of order

\[
r_L^{-(\ell+2)}.
\]

The corresponding passive velocity correction has the same radial order, which relative to the leading `r_L^-1` velocity gives

\[
z^{(\ell+1)/2}.
\]

For even `ell`, this is again half-integer and is excluded by punctured terminal smoothness.

For odd `ell`, it is integer and belongs to the ordinary terminal Taylor hierarchy.

---

## 7. What smoothness does not eliminate

A function may be `C^infinity` at `z=0` while vanishing faster than every algebraic power, e.g. schematically

\[
e^{-1/z}.
\]

Therefore punctured terminal smoothness eliminates noninteger algebraic sectors but does **not** prove uniqueness of the Fuchsian extension.

A same-tail difference could still be:

1. an integer-power strong Taylor hierarchy carrying admissible odd pressure multipoles; or
2. a Fuchsian-flat remainder invisible to every finite asymptotic order.

The second case is precisely a backward-uniqueness / infinite-order-vanishing problem.

---

## 8. DSD four-chain audit

### Formation — GREEN

The elimination uses the already proved physical terminal extension, not an imposed analyticity assumption.

### Axis — GREEN

Fuchsian scale depth `z`, physical terminal time `tau`, and physical radius are related exactly rather than conflated.

### Static aggregation — GREEN

M5-138's even multipoles remain valid solutions of the punctured Poisson equation; they are removed only from the dynamically realized smooth terminal branch.

### Dynamics — GREEN

The decisive input is terminal differentiability at fixed physical position.

### Cross-audit — GREEN

M5-137 is restored as the realized algebraic sector only after M5-138 exposed the missing half-integer possibilities and the present note eliminated them dynamically.

---

## 9. Revised P1 split

The same-tail fiber now has two genuinely different possibilities:

\[
\boxed{
P1_A:
\text{integer Taylor/multipole fiber with odd }\ell=3,5,7,\ldots
}
\]

or

\[
\boxed{
P1_B:
\text{Fuchsian-flat fiber, vanishing to every algebraic order at }z=0.
}
\]

The leading `ell=1` dipole is already factor-fixed by M5-134.

---

## 10. Next gate

`P1_A` should be audited against the local terminal NSE Taylor recursion and pressure normalization to determine whether the higher odd multipole coefficients are uniquely fixed.

`P1_B` is a genuine critical-background backward-uniqueness problem and cannot be settled by finite-order asymptotics.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]