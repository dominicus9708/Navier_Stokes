# M19-319 — The interior carrier forces simultaneous enstrophy, palinstrophy, and raw-H2 saturation on record cells, making the ancient tail rates sharp along the record subsequence

**Date:** 2026-09-16  
**Status:** NEW THREE-LEVEL RECORD SATURATION THEOREM / SPECTRAL OWN-SCALE CLASSIFICATION / NO GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-318 proves that the M5-478 second-generation interior carrier automatically supplies a fixed annular palinstrophy payment.

The existing ancient estimates already give matching upper bounds on enstrophy, palinstrophy, and raw-H2 after the same record blow-down.

Combining these facts with spacetime Sobolev log-convexity shows that all three derivative levels are simultaneously order one in every sufficiently late retained record cell.

## 2. Record notation

Let

\[
T_m=-\tau_m,
\qquad
R_m=\sqrt{T_m}\to\infty,
\]

and

\[
\Omega_m(y,s)=R_m^2\Omega(R_my,R_m^2s).
\]

Fix a compact normalized interval

\[
I=[-b,-a]\Subset(-\infty,0)
\]

containing the M5-478 carrier neighborhood around `s=-1`.

Define

\[
q_{0,m}:=
\int_I\|\Omega_m(s)\|_2^2ds,
\]

\[
q_{1,m}:=
\int_I\|\nabla\Omega_m(s)\|_2^2ds,
\]

and

\[
q_{2,m}:=
\int_I\|\Delta\Omega_m(s)\|_2^2ds.
\]

## 3. Enstrophy lower and upper bounds

M19-318 thickens the M5-478 local carrier so that on a fixed subinterval `I_0 subset I`,

\[
\int_{B_{\rho_0}}|\Omega_m(y,s)|^2dy\ge c_E>0.
\]

Hence

\[
\boxed{q_{0,m}\ge c_0>0.}
\]

On the other hand M5-475 Type-I decay is invariant under the record blow-down:

\[
\|\Omega_m(s)\|_2^2
\le C|s|^{-1/2}
\]

uniformly on fixed `I`.

Therefore

\[
\boxed{q_{0,m}\le C_0<\infty.}
\]

Thus

\[
\boxed{q_{0,m}\asymp1.}
\]

## 4. Palinstrophy lower and upper bounds

M19-318 gives directly

\[
\boxed{q_{1,m}\ge c_1>0.}
\]

M5-477 gives the quantitative backward palinstrophy tail

\[
\int_{-\infty}^{-T}\|\nabla\Omega(t)\|_2^2dt
\lesssim T^{-1/2}.
\]

The exact record scaling is

\[
R_m^{-1}q_{1,m}
=
\int_{R_m^2I}\|\nabla\Omega(t)\|_2^2dt.
\]

Since `R_m^2 I` lies at backward time comparable to `T_m=R_m^2`,

\[
\int_{R_m^2I}P(t)dt
\lesssim R_m^{-1}.
\]

Therefore

\[
\boxed{q_{1,m}\le C_1<\infty.}
\]

Thus

\[
\boxed{q_{1,m}\asymp1.}
\]

## 5. Raw-H2 upper bound

M17-404 proves

\[
\int_{-\infty}^{-T}
\|\Delta\Omega(t)\|_2^2dt
\lesssim T^{-3/2}.
\]

The exact record scaling is

\[
R_m^{-3}q_{2,m}
=
\int_{R_m^2I}
\|\Delta\Omega(t)\|_2^2dt.
\]

Hence

\[
\int_{R_m^2I}H(t)dt
\lesssim R_m^{-3},
\]

and therefore

\[
\boxed{q_{2,m}\le C_2<\infty.}
\]

## 6. Raw-H2 lower bound from spacetime log-convexity

At each time,

\[
\|\nabla\Omega\|_2^2
\le
\|\Omega\|_2\,\|D^2\Omega\|_2
\]

in the standard homogeneous Fourier interpolation sense.

Integrating in time and applying Cauchy--Schwarz gives

\[
\boxed{
q_{1,m}^2
\le
q_{0,m}q_{2,m}.
}
\]

Using

\[
q_{1,m}\ge c_1,
\qquad
q_{0,m}\le C_0,
\]

we obtain

\[
\boxed{
q_{2,m}
\ge
\frac{c_1^2}{C_0}
=:c_2>0.
}
\]

Therefore

\[
\boxed{q_{2,m}\asymp1.}
\]

This lower bound did not require a CE-H coefficient identity.

## 7. Simultaneous three-level saturation

Combining Sections 3--6,

\[
\boxed{
0<c_k
\le
q_{k,m}
\le
C_k<\infty,
\qquad
k=0,1,2,
}
\]

for every sufficiently late retained record.

Thus the canonical second-generation interior carrier is neither

- enstrophy-vanishing,
- palinstrophy-vanishing,
- nor raw-H2-vanishing.

It carries simultaneous order-one charge at all three levels.

## 8. Sharp first-ancient tail rates on record windows

Undo the second-generation scaling.

For `k=0`,

\[
q_{0,m}
=
R_m^{-1}
\int_{R_m^2I}E(t)dt,
\]

so

\[
\boxed{
\int_{R_m^2I}E(t)dt
\asymp
R_m
=
T_m^{1/2}.
}
\]

For palinstrophy,

\[
R_m^{-1}q_{1,m}
=
\int_{R_m^2I}P(t)dt,
\]

so

\[
\boxed{
\int_{R_m^2I}P(t)dt
\asymp
R_m^{-1}
=
T_m^{-1/2}.
}
\]

For raw-H2,

\[
R_m^{-3}q_{2,m}
=
\int_{R_m^2I}H(t)dt,
\]

so

\[
\boxed{
\int_{R_m^2I}H(t)dt
\asymp
R_m^{-3}
=
T_m^{-3/2}.
}
\]

Therefore the previously known upper tail exponents are saturated on the retained record subsequence.

## 9. Effective spectral scale

Since

\[
q_{0,m}\asymp q_{1,m}\asymp q_{2,m}\asymp1,
\]

the integrated effective derivative ratios satisfy

\[
\boxed{
\frac{q_{1,m}}{q_{0,m}}\asymp1,
\qquad
\frac{q_{2,m}}{q_{1,m}}\asymp1.
}
\]

Thus the interior carrier is spectrally own-scale in the coarse `L2` derivative sense.

It does not require an H/raw-H2 escalation to remain nontrivial on the selected record cells.

In first-ancient coordinates the corresponding effective length is of order `R_m`, exactly the backward Type-I scale.

## 10. Consequence for the M18-056--057 escape interpretation

M18-056 says a fixed palinstrophy payer can avoid lower-order descent by escalating raw-H2.

For the canonical M5-478 interior carrier, M19-319 shows instead

\[
q_{1,m}\asymp1,
\qquad
q_{2,m}\asymp1.
\]

Hence the `q_H -> infinity` escape is absent on this selected record subsequence.

This improves classification but does not create a global contradiction because M18-058 remains decisive: the standard-energy cost obtained after full physical composition still carries the summable chronological factor `r_n`.

## 11. Physical interpretation

The canonical record cell is a genuinely self-similar derivative packet in the weak integrated sense:

- vorticity mass is order one;
- one derivative costs order one;
- two derivatives cost order one;
- undoing the blow-down reproduces exactly the Type-I powers of the backward scale.

This is stronger than merely saying the tail estimates are finite.

The old upper bounds are sharp along the first-hitting record sequence.

## 12. Firewall

The simultaneous saturation does **not** imply exact self-similarity, periodicity, or profile convergence without subsequence.

It also does not supply a finite original-parent total for palinstrophy/raw-H2.

Therefore

\[
\boxed{
\text{three-level record saturation}
\not\Rightarrow
\text{global regularity contradiction}.
}
\]

## 13. Next target

The high-value next question is no longer whether the canonical interior carrier pays palinstrophy or raw-H2. Both are now certified at order one.

Instead test whether the simultaneous ratios

\[
q_0\asymp q_1\asymp q_2
\]

plus compact recurrence and the M18-062 multi-p segregation force a **rigidity or nontrivial scale-critical tail condition** strong enough to escape the unsigned budget firewall.

---

\[
\boxed{\text{M19-319 COMPLETE; THE CANONICAL RECORD CELL SATURATES THE TYPE-I ENSTROPHY, PALINSTROPHY, AND RAW-H2 RATES SIMULTANEOUSLY.}}
\]