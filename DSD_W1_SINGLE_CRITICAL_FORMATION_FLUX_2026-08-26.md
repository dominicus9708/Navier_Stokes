# DSD W1 Single Critical Formation Flux

Date: 2026-08-26

Status: **CRITICAL SHELL DENSITY, LOG-RADIUS CONVEYOR RATE, AND THE `R3/6` GAUSSIAN ENDPOINT RESIDUE IDENTIFIED AS ONE FLUX CONSTANT / FINITE-ENERGY COST KERNEL EXPLAINS WHY THIS FLUX IS NOT EXCLUDED BY L2 ENERGY / GLOBAL REGULARITY UNPROVED.**

## 1. Critical log-shell density

The invariant W1 endpoint has

\[
M_{crit}>0
\]

and the Abelian density

\[
\boxed{
\mathscr R_3
=
\frac{M_{crit}}{\log2}.
}
\]

Interpret `R3` as the asymptotic cubic mass per unit logarithmic radius.

---

## 2. The far-tail conveyor has speed one half

In log-radius coordinates

\[
\rho=\log|Y|,
\]

the leading far transport obeys

\[
\partial_s+rac12\partial_\rho.
\]

Hence the critical memory moves at velocity

\[
\boxed{
v_\rho=\frac12.
}
\]

Therefore a log-radius density `R3` carries cubic mass across scales at the rate

\[
\boxed{
J_{3,mass}
=
\frac12\mathscr R_3.
}
\]

---

## 3. Why the endpoint residue is `R3/6`

The `p=3` energy ledger uses

\[
\frac13\frac d{ds}\int |U|^3.
\]

Therefore the cubic-energy flux corresponding to the mass conveyor is

\[
\boxed{
\mathfrak J_c
:=
\frac13J_{3,mass}
=
\frac{\mathscr R_3}{6}.
}
\]

This is exactly the residue that appeared independently in the endpoint `p downarrow 3` balance and in the Gaussian scale-chain identity.

Thus the three earlier quantities are one structural object:

\[
\boxed{
\text{critical shell density}
\longleftrightarrow
\text{log-radius transport rate}
\longleftrightarrow
\text{endpoint residue }\mathscr R_3/6.
}
\]

The natural DSD name for this common object is the **critical formation flux** `J_c`.

---

## 4. Relation to prelimit `L3` growth

If the actual prelimit shell corridor realizes the invariant asymptotic density in Cesaro form, the number of newly populated logarithmic shells grows at speed `1/2` in Leray time.

Accordingly the cubic mass has the asymptotic rate

\[
\frac d{ds}\|U(s)\|_3^3
\sim
\frac{\mathscr R_3}{2},
\]

or at the level of Cesaro growth,

\[
\boxed{
\frac1S\|U(S)\|_3^3
\to
\frac{\mathscr R_3}{2}
}
\]

when the required prelimit-to-invariant transport is available.

Then

\[
\frac13\frac d{ds}\|U\|_3^3
\sim
\mathfrak J_c.
\]

The equality of constants is not accidental: it is the same log-scale flux seen in a time ledger.

Where a full prelimit Cesaro limit has not been proved, this paragraph is an interpretation/target rather than an additional theorem. The invariant flux identity `J_c=R3/6` remains exact.

---

## 5. Minimum kinetic-energy price of one critical shell

Suppose on a physical logarithmic shell of radius `r` the cubic mass satisfies

\[
\int_{A_r}|u|^3dx\ge m_0>0
\]

and the Type-I envelope gives

\[
\|u\|_{L^\infty(A_r)}
\le
\frac{A_0}{r}.
\]

Then

\[
\int_{A_r}|u|^3dx
\le
\|u\|_\infty
\int_{A_r}|u|^2dx,
\]

so

\[
\boxed{
\int_{A_r}|u|^2dx
\ge
\frac{m_0}{A_0}r.
}
\]

Thus one order-one critical cubic shell costs only order `r` kinetic energy.

---

## 6. Why finite energy does not stop infinitely many emitted shells

For geometric radii

\[
r_j=r_0\lambda^{-j},
\qquad \lambda>1,
\]

the minimum total kinetic-energy cost is

\[
\sum_j
\frac{m_0}{A_0}r_j
<\infty.
\]

Therefore an infinite critical memory ladder can have

\[
\text{order-one cubic mass per log shell}
\]

while paying only finite total `L2` energy.

This is precisely the integrability of the physical `1/r` trace in `L2_loc`.

It also explains the repeated half-power barrier encountered in the turnover and parent-energy ledgers.

---

## 7. DSD source-chain

The current endpoint can be written with one flux symbol:

\[
\boxed{
\text{recurrent nonlinear core}
\longrightarrow
\mathfrak J_c>0
\longrightarrow
\text{outward log-scale critical memory}
\longrightarrow
\text{positive-density }1/r\text{ shell corridor}.
}
\]

The far tail is the stored historical record of the same flux; it is not a second independent source.

The finite-energy parent does not kill `J_c` because its energy price has positive scaling exponent `beta=1`.

A final contradiction therefore requires a scale-critical or scale-breaking theorem that forces

\[
\boxed{
\mathfrak J_c=0.
}
\]

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
