# M19-320 — Three-level record saturation forces a uniform nontrivial normalized Fourier annulus and excludes total UV or IR escape of the interior carrier

**Date:** 2026-09-16  
**Status:** NEW SPECTRAL ANNULUS THEOREM / OWN-SCALE FREQUENCY OCCUPANCY / NOT A GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-319

On every sufficiently late retained second-generation record cell over a fixed normalized time interval `I`, M19-319 gives

\[
0<c_0\le q_{0,m}\le C_0,
\]

\[
0<c_1\le q_{1,m}\le C_1,
\]

and

\[
0<c_2\le q_{2,m}\le C_2,
\]

where

\[
q_{0,m}
=\int_I\|\Omega_m(s)\|_2^2ds,
\]

\[
q_{1,m}
=\int_I\|\nabla\Omega_m(s)\|_2^2ds,
\]

and

\[
q_{2,m}
=\int_I\|\Delta\Omega_m(s)\|_2^2ds.
\]

We now convert these moment bounds into a fixed spectral-annulus occupation theorem.

## 2. Spacetime Fourier measure

Define the positive measure

\[
\boxed{
 d\mu_m(\xi,s)
 :=
 |\widehat{\Omega_m}(\xi,s)|^2
 d\xi ds
}
\]

on `R^3_xi x I`.

By Plancherel,

\[
q_{0,m}=\int d\mu_m,
\]

\[
q_{1,m}=\int |\xi|^2d\mu_m,
\]

and

\[
q_{2,m}=\int |\xi|^4d\mu_m.
\]

Thus the first two spectral moments are uniformly bounded above, while the first derivative moment is uniformly bounded below.

## 3. Low-frequency part cannot carry all palinstrophy

For any `a>0`,

\[
\int_{|\xi|<a}|\xi|^2d\mu_m
\le
a^2\int d\mu_m
\le
a^2C_0.
\]

Choose a fixed `a>0` so small that

\[
\boxed{a^2C_0\le\frac{c_1}{4}.}
\]

Then uniformly in all sufficiently late records,

\[
\boxed{
\int_{|\xi|<a}|\xi|^2d\mu_m
\le\frac{c_1}{4}.
}
\]

Thus the palinstrophy lower bound cannot be paid entirely by normalized frequencies tending to zero.

## 4. High-frequency part cannot carry all palinstrophy

For any `b>0`, on `|xi|>b`,

\[
|\xi|^2
\le
b^{-2}|\xi|^4.
\]

Therefore

\[
\int_{|\xi|>b}|\xi|^2d\mu_m
\le
b^{-2}q_{2,m}
\le
b^{-2}C_2.
\]

Choose a fixed finite `b` so large that

\[
\boxed{b^{-2}C_2\le\frac{c_1}{4}.}
\]

Then

\[
\boxed{
\int_{|\xi|>b}|\xi|^2d\mu_m
\le\frac{c_1}{4}.
}
\]

Thus the palinstrophy lower bound cannot be paid entirely by normalized frequencies escaping to infinity.

## 5. Uniform middle-frequency palinstrophy

Since

\[
q_{1,m}\ge c_1,
\]

subtract Sections 3 and 4:

\[
\boxed{
\int_{a\le|\xi|\le b}
|\xi|^2d\mu_m
\ge
\frac{c_1}{2}.
}
\]

This is a fixed normalized Fourier annulus independent of the record index.

Hence every sufficiently late record contains a nontrivial own-scale frequency population.

## 6. Enstrophy and raw-H2 are also nontrivial on the same annulus

On the annulus `a <= |xi| <= b`,

\[
|\xi|^2\le b^2,
\]

so

\[
\int_{a\le|\xi|\le b}d\mu_m
\ge
b^{-2}
\int_{a\le|\xi|\le b}|\xi|^2d\mu_m.
\]

Therefore

\[
\boxed{
\int_{a\le|\xi|\le b}
d\mu_m
\ge
\frac{c_1}{2b^2}>0.
}
\]

Likewise, since `|xi|^4 >= a^2 |xi|^2` on the annulus,

\[
\boxed{
\int_{a\le|\xi|\le b}
|\xi|^4d\mu_m
\ge
\frac{a^2c_1}{2}>0.
}
\]

Thus one fixed Fourier annulus carries simultaneous positive spacetime enstrophy, palinstrophy, and raw-H2 charge.

## 7. Spectral own-scale conclusion

There exist constants

\[
0<a<b<\infty
\]

and

\[
c_{band}>0
\]

such that for all sufficiently late retained records,

\[
\boxed{
\int_I
\int_{a\le|\xi|\le b}
|\xi|^2
|\widehat{\Omega_m}(\xi,s)|^2
\,d\xi ds
\ge c_{band}.
}
\]

Therefore the canonical interior carrier cannot become purely infrared or purely ultraviolet in the second-generation normalization.

It necessarily retains an order-one population at frequencies of order one.

## 8. Physical first-ancient interpretation

The second-generation blow-down is

\[
\Omega_m(y,s)=R_m^2\Omega(R_my,R_m^2s).
\]

A normalized frequency `|xi| ~ 1` corresponds to a first-ancient physical frequency

\[
|\eta|\sim R_m^{-1}.
\]

Thus the fixed normalized Fourier annulus becomes

\[
\boxed{
\frac{a}{R_m}
\lesssim
|\eta|
\lesssim
\frac{b}{R_m}
}
\]

in the first ancient element.

The associated physical length scale is therefore

\[
\boxed{\ell_m\asymp R_m\asymp\sqrt{T_m}.}
\]

This is exactly the backward Type-I parabolic scale.

## 9. Consequence for derivative decompactification

M18-057 routes large raw-H2/D3 escalation to derivative-tail decompactification / remote / critical exits.

M19-319 already showed that `q_2` remains order one on the selected canonical record sequence.

M19-320 strengthens this: a fixed share of the derivative charge stays in a fixed normalized frequency annulus.

Therefore the canonical interior carrier itself does not require total UV frequency escape.

Additional UV microstructure may coexist, but it cannot replace the order-one own-scale spectral population.

Likewise any remote/critical tail may coexist, but it cannot absorb the entire carrier into an IR mode.

## 10. Relation to critical-tail rigidity

The record carrier now has both

1. fixed spatial local nontriviality from M5-478/M19-318;
2. fixed normalized spectral-annulus nontriviality from M19-320.

This makes the surviving compact object a genuinely own-scale nontrivial ancient packet rather than a normalization artifact caused solely by low- or high-frequency leakage.

The remaining obstruction is global tail/phase/rigidity, not basic frequency placement.

## 11. Firewall

The spectral annulus theorem does not imply exact self-similarity or a unique profile.

It also does not exclude additional IR or UV charge outside the annulus.

Most importantly, it does not repair the unsigned original-parent budget mismatch of M18-058--059.

Therefore

\[
\boxed{
\text{fixed normalized spectral annulus}
\not\Rightarrow
\text{global regularity contradiction}.
}
\]

## 12. Next target

The next useful calculation should combine the fixed spatial carrier and fixed spectral annulus with the critical terminal-tail process.

A natural question is whether an ancient packet that remains own-scale nontrivial at every backward record can have a terminal `1/r` scattering tail whose log-radius process is fully decoupled from the interior packet, or whether Biot--Savart/nonlocal pressure necessarily transfers a fixed correlation between the interior spectral band and the terminal tail.

That would attack the critical-tail rigidity/factor frontier without returning to unsigned additive accumulation.

---

\[
\boxed{\text{M19-320 COMPLETE; THE CANONICAL INTERIOR CARRIER HAS A UNIFORM NONTRIVIAL OWN-SCALE FOURIER BAND.}}
\]