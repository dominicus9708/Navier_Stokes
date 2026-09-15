# M19-309 — M17-404 raw-H2 tail decay is exactly Type-I critical and reproduces rho^{-3} physical amplification rather than supplying base gain

**Date:** 2026-09-16  
**Status:** ACTIVE GMS BASE-GAIN AUDIT / QUANTITATIVE TAIL REIMPORTED / CRITICAL-SCALING NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Reimport the quantitative M17-404 tail

M17-404 proves more than total ancient raw-H2 finiteness. For large `T`,

\[
\boxed{
\int_{-2T}^{-T}
\|\Delta\Omega(\tau)\|_2^2d\tau
\le CT^{-3/2},
}
\]

and after dyadic summation,

\[
\boxed{
\int_{-\infty}^{-T}
\|\Delta\Omega(\tau)\|_2^2d\tau
\lesssim T^{-3/2}.
}
\]

This is the strongest explicit quantitative backward raw-H2 tail currently certified by that module.

## 2. Restore one first-hitting physical base scale

Let `r_j` be the physical first-hitting base scale.

Under the Navier--Stokes scaling from the ancient normalized solution back to the original physical solution, the spacetime raw-vorticity-H2 / velocity-H3 charge carries the factor

\[
\boxed{r_j^{-3}.}
\]

Therefore the M17-404 tail window at backward normalized age `T` gives at best

\[
\boxed{
Q_{j,T}^{phys}
\lesssim
r_j^{-3}T^{-3/2}.
}
\]

## 3. Composite physical radius

Backward age `T` has parabolic spatial blow-down factor

\[
R=\sqrt T.
\]

M19-260 identifies the represented physical radius as

\[
\boxed{
\rho=r_jR=r_j\sqrt T.
}
\]

Hence

\[
r_j^{-3}T^{-3/2}
=
(r_j\sqrt T)^{-3}.
\]

Therefore

\[
\boxed{
Q_{j,T}^{phys}
\lesssim
\rho^{-3}.
}
\]

The ancient tail decay has exactly converted into the ordinary physical H3/raw-H2 scaling at the composite physical radius.

## 4. No base-scale gain is produced

The desired GMS transfer requires a mechanism that improves on the fine-scale physical amplification.

But M17-404 supplies

\[
T^{-3/2}=R^{-3},
\]

which exactly cancels only the **backward blow-down representation factor**, not the physical small-radius singular factor.

Thus

\[
\boxed{
\text{M17-404 quantitative tail}
\not\Rightarrow
\mathcal T_{GMS}^{base-gain}.
}
\]

Equivalently,

\[
\boxed{
R^{-3}\text{ ancient decay}
\quad\leftrightarrow\quad
\rho^{-3}\text{ physical critical scaling}.
}
\]

## 5. Why the exponent 3/2 is critical

A Type-I vorticity profile has the dimensional form

\[
\Omega(x,-T)
\sim
T^{-1}\,W(x/\sqrt T).
\]

Then

\[
\Delta\Omega
\sim
T^{-2}(\Delta W)(x/\sqrt T).
\]

Therefore

\[
\|\Delta\Omega(-T)\|_2^2
\sim
T^{-4}T^{3/2}
=
T^{-5/2}.
\]

Integrating over a backward annulus of time length `O(T)` gives

\[
\boxed{T^{-3/2}.}
\]

Thus the M17-404 exponent is exactly the Type-I parabolic critical exponent for this raw-H2 spacetime charge.

It is not a hidden subcritical gain.

## 6. What would be sufficient

Suppose one could strengthen the ancient tail on a relevant sequence to

\[
\int_{-2T}^{-T}H(\tau)d\tau
\le
\varepsilon(T)T^{-3/2},
\qquad
\varepsilon(T)\to0.
\]

Then physical restoration would give

\[
Q_{j,T}^{phys}
\lesssim
\varepsilon(T)\rho^{-3}.
\]

This would supply a **coefficient gain**, but still not automatically a globally finite physical H3 budget; one would need the gain to dominate the remaining small-radius demand across the selected first-hitting sequence.

A stronger power improvement

\[
T^{-3/2-\delta}
\]

would give

\[
Q_{j,T}^{phys}
\lesssim
\rho^{-3}T^{-\delta},
\]

which is a genuine parabolic subcritical factor.

## 7. Near-singularity compatibility constraint

To use backward age while still probing the singular point, the composite radius must satisfy

\[
\rho_j=r_j\sqrt{T_j}\to0.
\]

Thus one cannot choose arbitrarily large `T_j` merely to exploit ancient integrability; necessarily

\[
T_j=o(r_j^{-2})
\]

along a near-singularity transfer.

This is the exact tradeoff between going far enough backward to gain decay and staying close enough physically to test the singularity.

## 8. Updated base-gain theorem target

The live theorem is now sharpened to

\[
\boxed{
\mathcal T_{GMS}^{subcrit-tail/base-gain}:
\text{obtain a representation-safe improvement beyond the critical }T^{-3/2}\text{ ancient raw-H2 tail on ages }T_j=o(r_j^{-2}).
}
\]

Possible forms include:

1. little-o critical tail with a quantitatively adequate rate;
2. a positive power improvement `T^{-delta}`;
3. a first-hitting/genealogy incidence theorem that converts critical tail decay into extra small physical occupation;
4. a different critical regularity endpoint requiring less than full physical H3.

## 9. Permanent firewall

The following shortcut is now explicitly excluded:

\[
\boxed{
\text{M17-404 has }T^{-3/2}\text{ tail}
\Longrightarrow
\text{physical H3 base gain}.
}
\]

The exponent is exactly critical and reproduces the physical `rho^{-3}` scaling.

---

\[
\boxed{\text{M19-309 COMPLETE; THE KNOWN ANCIENT RAW-H2 TAIL IS CRITICAL, NOT SUBCRITICAL.}}
\]