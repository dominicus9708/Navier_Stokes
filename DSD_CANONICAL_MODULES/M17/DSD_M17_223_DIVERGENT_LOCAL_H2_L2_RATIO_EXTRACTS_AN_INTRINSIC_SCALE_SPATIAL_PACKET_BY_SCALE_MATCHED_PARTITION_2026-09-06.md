# DSD M17-223 — Divergent local H2/L2 ratio extracts an intrinsic-scale spatial packet by a scale-matched partition

Date: 2026-09-06  
Canonical ID: **M17-223**

Status: **INTRINSIC-SCALE PACKET EXTRACTION / M17-222 PRODUCES A BOUNDED-SIZE REMOTE COMPACT FIELD `f_j` WITH `H_j/E_j = ||Delta f_j||_2^2/||f_j||_2^2 -> infinity`. DEFINE `ell_j=(E_j/H_j)^(1/4)`. A PARTITION INTO CELLS OF SIZE `r_j=A ell_j` HAS DERIVATIVE COMMUTATORS OF SIZE `r_j^-2 ||grad f_j||_2^2 + r_j^-4 ||f_j||_2^2`. FOURIER INTERPOLATION `||grad f_j||_2^2 <= sqrt(E_j H_j)` MAKES THESE EXACTLY `O(A^-2)H_j + O(A^-4)H_j`. CHOOSING ONE LARGE FIXED `A` ABSORBS THE COMMUTATORS, SO THE SUM OF CELLWISE H2 MASSES RETAINS A FIXED FRACTION OF `H_j`. PIGEONHOLING AGAINST THE EXACT L2 PARTITION THEN SELECTS ONE CELL OF DIAMETER `O(ell_j)` WITH H2/L2 RATIO `gtrsim ell_j^-4`. AFTER RESCALING BY `ell_j`, THE PACKET HAS FIXED SPATIAL DIAMETER. THUS THE REMOTE SPECTRAL EXIT ADMITS A TRUE INTRINSIC-SCALE SPATIAL WITNESS, NOT MERELY A UNIT-SCALE HIGH-FREQUENCY BOX. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input packet from M17-222

Let `f_j` be the compact remote packet extracted by M17-222.

Set

\[
E_j:=\|f_j\|_2^2>0,
\qquad
H_j:=\|\Delta f_j\|_2^2.
\]

Assume

\[
\boxed{
\frac{H_j}{E_j}\to\infty.
}
\]

Define the intrinsic Laplacian length

\[
\boxed{
\ell_j
:=\left(\frac{E_j}{H_j}\right)^{1/4}.
}
\]

Then

\[
\boxed{
H_j=\ell_j^{-4}E_j,
\qquad
\ell_j\to0.
}
\]

The support of `f_j` has bounded diameter independent of `j`, and its center `p_j` satisfies `|p_j|->infinity`.

---

## 2. First derivative is at most the geometric mean

Because `f_j` is compactly supported and belongs to `H2`, Fourier Cauchy-Schwarz gives

\[
\boxed{
Z_j:=\|\nabla f_j\|_2^2
\le
E_j^{1/2}H_j^{1/2}.
}
\]

Using `H_j=ell_j^-4 E_j`,

\[
\boxed{
Z_j\le\ell_j^{-2}E_j
=\ell_j^2H_j.
}
\]

This is the scale relation that makes a matched spatial partition possible.

---

## 3. Partition at the intrinsic scale

Fix a large constant

\[
A>1
\]

to be chosen once and for all.

Set the cell scale

\[
\boxed{r_j:=A\ell_j.}
\]

Choose a smooth partition of unity

\[
\sum_m\chi_{j,m}^2\equiv1
\]

with uniformly finite overlap, each `chi_{j,m}` supported in a cell of diameter `O(r_j)`, and

\[
\boxed{
\|\nabla\chi_{j,m}\|_\infty
\le C r_j^{-1},
\qquad
\|\Delta\chi_{j,m}\|_\infty
\le C r_j^{-2}.
}
\]

Define

\[
\boxed{g_{j,m}:=\chi_{j,m}f_j.}
\]

Then

\[
\boxed{
\sum_m\|g_{j,m}\|_2^2
=E_j.
}
\]

---

## 4. Scale-matched commutator estimate

The identity

\[
\chi_{j,m}\Delta f_j
=
\Delta g_{j,m}
-2\nabla\chi_{j,m}\cdot\nabla f_j
-(\Delta\chi_{j,m})f_j
\]

implies, after squaring, summing, and using finite overlap,

\[
\boxed{
H_j
\le
3\sum_m\|\Delta g_{j,m}\|_2^2
+C r_j^{-2}Z_j
+C r_j^{-4}E_j.
}
\]

Now

\[
r_j^{-2}Z_j
\le
A^{-2}\ell_j^{-2}\cdot\ell_j^2H_j
=A^{-2}H_j,
\]

and

\[
r_j^{-4}E_j
=A^{-4}\ell_j^{-4}E_j
=A^{-4}H_j.
\]

Therefore

\[
\boxed{
H_j
\le
3\sum_m\|\Delta g_{j,m}\|_2^2
+C(A^{-2}+A^{-4})H_j.
}
\]

Choose `A` sufficiently large that

\[
C(A^{-2}+A^{-4})\le\frac12.
\]

Then

\[
\boxed{
\sum_m\|\Delta g_{j,m}\|_2^2
\ge c_0H_j
}
\]

with a fixed `c_0>0` independent of `j`.

---

## 5. Intrinsic-cell pigeonhole

Since

\[
\sum_m\|g_{j,m}\|_2^2=E_j
\]

and

\[
\sum_m\|\Delta g_{j,m}\|_2^2\ge c_0H_j,
\]

there exists at least one cell index `m_j` such that

\[
\boxed{
\frac{\|\Delta g_{j,m_j}\|_2^2}
{\|g_{j,m_j}\|_2^2}
\ge
c_0\frac{H_j}{E_j}
=c_0\ell_j^{-4}.
}
\]

Write

\[
\boxed{G_j:=g_{j,m_j}.}
\]

Then

\[
\boxed{
\operatorname{diam}(\operatorname{supp}G_j)
\le C_A\ell_j
}
\]

and

\[
\boxed{
\frac{\|\Delta G_j\|_2^2}{\|G_j\|_2^2}
\ge c_0\ell_j^{-4}.
}
\]

Thus the spectral ratio is carried by a true spatial packet at its own intrinsic scale.

---

## 6. The selected packet has a comparable or smaller intrinsic length

Define

\[
\widetilde\ell_j
:=
\left(
\frac{\|G_j\|_2^2}{\|\Delta G_j\|_2^2}
\right)^{1/4}.
\]

Then

\[
\boxed{
\widetilde\ell_j
\le c_0^{-1/4}\ell_j.
}
\]

Hence

\[
\boxed{
\widetilde\ell_j\to0,
\qquad
\operatorname{diam}(\operatorname{supp}G_j)
\le C\widetilde\ell_j
}
\]

after harmless adjustment of the fixed constant.

So spatial diameter and spectral length are now comparable up to fixed constants.

---

## 7. Remote character survives the second localization

M17-222 places `f_j` in a bounded-size box whose center `p_j` satisfies

\[
|p_j|\asymp R_j\to\infty.
\]

The new packet `G_j` lies inside that box and has diameter `o(1)`.
Therefore its center `q_j` satisfies

\[
\boxed{
|q_j|\asymp R_j\to\infty.
}
\]

Moreover

\[
\boxed{
\frac{\widetilde\ell_j}{R_j}\to0.
}
\]

This is a genuine remote two-scale packet.

---

## 8. Parabolic normalization is now spatially tight

Let

\[
A_j:=\|G_j\|_2>0.
\]

Define the spatially rescaled packet at the observation time by

\[
\boxed{
V_j(z,0)
:=
\frac{\widetilde\ell_j^{3/2}}
{A_j}
G_j(q_j+\widetilde\ell_j z).
}
\]

Then

\[
\boxed{\|V_j(\cdot,0)\|_2=1.}
\]

Its support has uniformly bounded diameter, and

\[
\boxed{
\|\Delta_zV_j(\cdot,0)\|_2^2
=1
}
\]

if `widetilde ell_j` is defined exactly by the packet quotient.

Thus both spatial support and the zero/second derivative normalization are tight at time zero.

This is the correct starting point for a parabolic dynamic extraction.

---

## 9. What is still missing

The packet `G_j` is built using a spatial cutoff at one observation time.
It is not itself an exact solution of the vorticity equation.

The next theorem must choose a moving intrinsic-scale cutoff or another localized observable and prove the dichotomy

\[
\boxed{
\text{intrinsic packet at }t=0
\Longrightarrow
\text{mass persists for }|\tau|\lesssim\widetilde\ell_j^2
\lor
\text{localized flux/turnover/forcing cost}.
}
\]

Only on the persistence branch may one pass to a nonzero parabolically rescaled dynamic limit.

---

## 10. DSD analysis

### 10.1 Why the scale is `A ell`

At a generic cell size `r`, the localization errors are

\[
r^{-2}Z_j+r^{-4}E_j.
\]

With

\[
Z_j\le\ell_j^{-2}E_j,
\qquad
H_j=\ell_j^{-4}E_j,
\]

choosing `r=A ell_j` converts both errors into fixed small multiples of `H_j`.

### 10.2 Multiplicity cannot hide the ratio

The number of intrinsic cells may diverge like a power of `ell_j^-1`, but both `L2` and localized `H2` are summed before pigeonholing.
Therefore the number of cells does not enter the final constant.

### 10.3 One-time statement only

Spatial extraction does not imply temporal persistence.
That boundary is left explicit.

---

## 11. DSD audit

- The partition scale is derived from the norm quotient rather than chosen arbitrarily.
- Cutoff derivative blowup as `ell_j->0` is accounted for quantitatively and absorbed by the large fixed factor `A`.
- No fixed lower bound on the selected packet's share of the parent `L2` mass is required; the packet is normalized by its own mass.
- A nonzero dynamic heat tangent is not yet claimed.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
