# M19-379 — The weighted CE-H geometric remainder is controlled by epsilon D_kappa plus palinstrophy

**Date:** 2026-09-18  
**Status:** NEW M19 SYNTHESIS / M17-194--195 + COMPACT CUTOFF + PALINSTROPHY CLASSIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-195

Under the M5-688 weight

\[
w=\chi(\rho)e^{2\kappa}\rho^2,
\]

M17-194--195 reduce the weighted CE-H geometric remainder to

\[
\boxed{
|\mathfrak R_{geom}^{(2)}|
\le
\varepsilon D_\kappa
+C_1(\varepsilon)D_\rho
+C_2 B_\rho
+C_3 P_\xi,
}
\]

where

\[
D_\kappa
=
\int\chi e^{2\kappa}\rho^2|\nabla\kappa|^2dy,
\]

\[
D_\rho
=
\int\chi e^{2\kappa}|\nabla\rho|^2dy,
\]

\[
P_\xi
=
\int\chi e^{2\kappa}\rho^2|\nabla\xi|^2dy,
\]

and

\[
B_\rho
=
\int\chi'(\rho)e^{2\kappa}\rho|\nabla\rho|^2dy.
\]

## 2. Amplitude and director charges are palinstrophy pieces

For

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

we have the exact identity

\[
\boxed{
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Let

\[
P:=\int|\nabla W|^2dy.
\]

On compact multiplier support

\[
|\kappa|\le K_*.
\]

Since \(0\le\chi\le1\),

\[
D_\rho
\le e^{2K_*}P,
\]

and

\[
P_\xi
\le e^{2K_*}P.
\]

## 3. The cutoff collar is also palinstrophy-order

The cutoff \(\chi\) is fixed and smooth. On its compact transition interval,

\[
0\le\chi'(\rho)\le C_\chi,
\qquad
0\le\rho\le\rho_*.
\]

Therefore

\[
\begin{aligned}
B_\rho
&\le
C_\chi\rho_*e^{2K_*}
\int_{\operatorname{supp}\chi'}|\nabla\rho|^2dy\\
&\le
C_{B,P}P.
\end{aligned}
\]

Thus every non-\(D_\kappa\) term in the M17-195 bound is palinstrophy-order.

## 4. Master geometric estimate

Substituting Sections 2--3 into M17-195 gives, for every \(\varepsilon>0\),

\[
\boxed{
|\mathfrak R_{geom}^{(2)}|
\le
\varepsilon D_\kappa
+
C_{\varepsilon,P}P.
}
\]

The same estimate holds after recurrent averaging:

\[
\boxed{
|\mathcal R|
\le
\varepsilon D_\kappa
+
C_{\varepsilon,P}\langle P\rangle,
}
\]

where \(\mathcal R\) denotes the recurrent exponentially weighted geometric remainder in the M5-688 cycle-work.

## 5. Consequence

The explicit CE-H geometric remainder cannot be an independent order-one payer of the M5-687 multiplier-diffusion floor while palinstrophy tends to zero.

If it pays an order-one part of \(D_\kappa\), then after absorbing an arbitrarily small fraction of \(D_\kappa\), it forces a corresponding palinstrophy-order occupancy.

Thus

\[
\boxed{
\text{geometric payment}
\subset
\varepsilon D_\kappa
+
\text{palinstrophy currency}.
}
\]

## 6. Relation to M19-375

M19-375 showed

\[
D_\sigma\le C P.
\]

The present module shows the same resource classification for the full weighted CE-H geometric remainder.

Hence both

\[
D_\sigma
\quad\text{and}\quad
\mathcal R_{geom}^{(2)}
\]

are not new derivative currencies beyond the critical palinstrophy architecture, modulo an absorbable fraction of \(D_\kappa\).

## 7. Scaling firewall

M17-307 and M19-314--315 show that physical spacetime palinstrophy is exactly critical under parent/physical restoration.

Therefore the estimate does not create a GMS base gain or a finite cumulative similarity-time resource by itself.

A contradiction still requires bounded reuse, annular incidence, supercritical multiplicity, or another nonrecyclable resource.

## 8. Verdict

\[
\boxed{
|\mathfrak R_{geom}^{(2)}|
\le
\varepsilon D_\kappa+C_\varepsilon P.
}
\]

The M5-688 geometric remainder is completely reduced, at the integrated compact-hull level, to the already exposed multiplier-diffusion and critical palinstrophy currencies.

---

\[
\boxed{\text{M19-379 COMPLETE; THE WEIGHTED GEOMETRIC PAYER IS NOT AN INDEPENDENT RESOURCE.}}
\]
