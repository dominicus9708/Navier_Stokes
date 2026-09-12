# DSD M19-116 — Pineau--Vicol periodic enstrophy estimate gives a quantitative joint period-rotation floor for every nontrivial RDSS

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL RDSS WEIGHTED-ENSTROPHY ESTIMATE RECAST AS A NECESSARY LOWER BOUND ON S+|ALPHA| / ORDINARY DSS INHERITS A POSITIVE PERIOD FLOOR AS THE ALPHA=0 SPECIAL CASE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RDSS similarity period

Let

\[
S=2\log\lambda>0
\]

be the similarity-time period and `alpha` the rotation parameter in the Pineau--Vicol RDSS representation.

The profile is `S`-periodic in similarity time in the chosen rotating frame.

---

## 2. External local-enstrophy estimate

Under the Type-I bound with constant `C_{U,0}`, Pineau--Vicol construct a time-independent positive adjoint weight for the time-averaged drift and prove, in the small-`S`, small-`|alpha|` regime, the pointwise-in-time estimate

\[
\boxed{
\|\Omega(\cdot,s)\|_{L^2(B_{\bar R})}
\le
C''\sqrt{S+|\alpha|}
}
\]

for every

\[
s\in[0,S],
\]

where

\[
\bar R,
\qquad
C''
\]

depend only on the Type-I corridor and not on `S` or `alpha`.

The key ingredients are:

- the time-averaged adjoint-kernel weight;
- cancellation of the total `s`-derivative over one period;
- the fluctuation estimate `U-<U>_s=O(S)`;
- the angular error proportional to `|alpha|`.

---

## 3. Periodic enstrophy identity

The RDSS vorticity satisfies

\[
\partial_s\Omega
+\alpha\mathcal R\Omega
+\Omega
+\frac12y\cdot\nabla\Omega
-\Delta\Omega
+U\cdot\nabla\Omega
=
\Omega\cdot\nabla U.
\]

Taking the `L2` inner product with `Omega`, the rotation term is skew and drops out:

\[
\boxed{
\frac12\frac d{ds}\|\Omega\|_2^2
+\frac14\|\Omega\|_2^2
+\|\nabla\Omega\|_2^2
=
\int \Omega_i\partial_iU_j\Omega_j\,dy.
}
\]

Using the Type-I derivative decay outside `B_Rbar` and the local estimate inside, Pineau--Vicol obtain

\[
\frac12\frac d{ds}\|\Omega\|_2^2
+\frac18
\left(
\|\Omega\|_2^2+\|\nabla\Omega\|_2^2
\right)
\le
C_\Omega
\|\Omega\|_{L^2(B_{\bar R})}
\left(
\|\Omega\|_2^2+\|\nabla\Omega\|_2^2
\right).
\]

Insert

\[
\|\Omega\|_{L^2(B_{\bar R})}
\le C''\sqrt{S+|\alpha|}.
\]

---

## 4. Integrate over one period

Integrating from `0` to `S` and using periodicity,

\[
\|\Omega(S)\|_2^2
=
\|\Omega(0)\|_2^2,
\]

so the time derivative contributes zero.

Hence

\[
\begin{aligned}
&\int_0^S
\left(
\|\Omega\|_2^2+\|\nabla\Omega\|_2^2
\right)ds\\
&\qquad\le
8C_\Omega C''\sqrt{S+|\alpha|}
\int_0^S
\left(
\|\Omega\|_2^2+\|\nabla\Omega\|_2^2
\right)ds.
\end{aligned}
\]

Therefore if

\[
8C_\Omega C''\sqrt{S+|\alpha|}<1,
\]

the integral must vanish and

\[
\Omega\equiv0,
\]

hence the decaying divergence-free profile is trivial.

---

## 5. Joint floor for every nontrivial RDSS

Thus on the regime in which the estimate is derived, every nonzero RDSS must satisfy

\[
\boxed{
S+|\alpha|
\ge
c_{RDSS}
:=
\frac1{(8C_\Omega C'')^2}.
}
\]

If either `S` or `|alpha|` already lies outside the small-parameter normalization used in the derivation, the sum is automatically order one.

Hence one may state structurally that there is a Type-I-dependent positive constant

\[
\boxed{c_*>0}
\]

such that every nontrivial RDSS on the certified corridor obeys

\[
\boxed{S+|\alpha|\ge c_*.}
\]

---

## 6. Ordinary DSS special case

For DSS,

\[
\alpha=0.
\]

Therefore every nontrivial DSS survivor in this class must satisfy

\[
\boxed{S\ge c_*>0.}
\]

This yields a direct period floor from the periodic enstrophy argument itself, independent of the separate M19-096 one-slice speed-floor route.

---

## 7. Relation to M19-110

M19-110 says that once

\[
S\ge S_*>0,
\]

no nontrivial DSS/RDSS orbit can approach the zero profile in the retained smooth vorticity phase space.

M19-116 supplies such a positive period floor automatically for ordinary DSS, and a joint period-rotation floor for RDSS.

Thus the small-parameter corner of the periodic problem is doubly excluded:

\[
\boxed{
\text{small }S+|\alpha|
\Rightarrow
\text{trivial},
}

while any surviving branch is finite-amplitude.

---

## 8. Firewall

The inequality does not give an upper bound on `S` or `|alpha|` and therefore does not compactify the full intrinsic-moduli space.

Also the RDSS representation has a rotation-holonomy/winding convention that must be fixed before comparing numerical `alpha` values across different representations.

Hence

\[
\boxed{
S+|\alpha|\ge c_*
\neq
\text{global RDSS nonexistence}.
}
\]

---

## 9. Reference

- Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619v2, 2026, Sections 7--8.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
