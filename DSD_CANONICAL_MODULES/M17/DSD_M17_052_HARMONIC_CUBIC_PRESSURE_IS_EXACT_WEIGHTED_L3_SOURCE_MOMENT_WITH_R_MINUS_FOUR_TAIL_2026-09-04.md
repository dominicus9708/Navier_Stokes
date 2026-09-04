# DSD M17-052 — The harmonic cubic pressure is an exact weighted l=3 source moment with an R^-4 tail

Date: 2026-09-04
Canonical ID: **M17-052**

Status: **INTERNAL HARMONIC-CUBIC BOUNDARY GATE / PROJECTING `-Delta P=S_P` ONTO SPHERICAL HARMONIC DEGREE THREE AROUND THE NODAL CORE GIVES AN EXACT RADIAL ODE. IF `u_{3m}(r)` IS THE DEGREE-THREE PRESSURE COEFFICIENT AND `A_{3m}=u_{3m}/r^3`, THEN `(r^8 A'_{3m})'=-r^5 s_{3m}(r)`, WHERE `s_{3m}` IS THE DEGREE-THREE PRESSURE-SOURCE COEFFICIENT. REGULARITY AT THE CORE AND WHOLE-SPACE PRESSURE DECAY GIVE `A_{3m}(0)=(1/7) integral_0^infty r^-2 s_{3m}(r) dr`. THUS THE CENTRAL HARMONIC CUBIC IS NOT AN ARBITRARY LOCAL POISSON FREEDOM: IT IS THE EXACT WEIGHTED l=3 MOMENT OF `S_P=|Sigma|^2-rho^2/2`. THE CONTRIBUTION FROM `r>=R` IS `O(Z_* R^-4)`, CONSISTENT WITH M17-050. DSAIG HARMONIC SCREENING IS THEREFORE A FINITE-DIMENSIONAL SEVEN-COMPONENT GLOBAL SOURCE-MOMENT LEDGER, AND ITS PERPENDICULAR ALIGNMENT REQUIREMENT IS ONE LINEAR MOMENT CONSTRAINT AT EACH RETAINED TIME. THIS IS RIGID BUT NOT A SNAPSHOT CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Spherical harmonic decomposition around the marked core

Center coordinates at the regular nodal core.
Write

\[
-\Delta P=S_P,
\qquad
S_P=|\Sigma|^2-\frac12\rho^2.
\]

Let

\[
\{Y_{3m}\}_{m=1}^{7}
\]

be a real orthonormal basis of degree-three spherical harmonics on `S^2`.

Define the angular coefficients

\[
\boxed{
 u_{3m}(r)
:=\int_{S^2}P(r\omega)Y_{3m}(\omega)\,d\omega,
}
\]

and

\[
\boxed{
 s_{3m}(r)
:=\int_{S^2}S_P(r\omega)Y_{3m}(\omega)\,d\omega.
}
\]

---

## 2. Exact radial Poisson equation for l=3

For spherical harmonic degree `l`,

\[
\Delta[u_l(r)Y_l(\omega)]
=
\left(
 u_l''+\frac2r u_l'-\frac{l(l+1)}{r^2}u_l
\right)Y_l.
\]

For `l=3`, `l(l+1)=12`.
Therefore

\[
\boxed{
-\left(
 u_{3m}''
+\frac2r u_{3m}'
-\frac{12}{r^2}u_{3m}
\right)
=s_{3m}(r).
}
\]

---

## 3. Remove the regular r^3 factor

Set

\[
\boxed{
A_{3m}(r):=\frac{u_{3m}(r)}{r^3}.
}
\]

Then

\[
u_{3m}=r^3A_{3m},
\]

and direct differentiation gives

\[
 u_{3m}''
+\frac2r u_{3m}'
-\frac{12}{r^2}u_{3m}
=r^3A_{3m}''+8r^2A_{3m}'.
\]

Hence

\[
\boxed{
A_{3m}''+\frac8rA_{3m}'
=-\frac{s_{3m}(r)}{r^3}.
}
\]

Equivalently,

\[
\boxed{
\left(r^8A_{3m}'\right)'
=-r^5s_{3m}(r).
}
\]

This is the exact radial ledger for the harmonic cubic coefficient.

---

## 4. Regularity at the core

Spatial analyticity gives a regular Taylor expansion.
The degree-three pressure sector has

\[
 u_{3m}(r)
=r^3A_{3m}(0)+O(r^5).
\]

There is no `r^4 Y_3` contribution because a homogeneous degree-four polynomial contains only angular degrees `4,2,0`.

Thus

\[
\boxed{
A_{3m}(r)=A_{3m}(0)+O(r^2),
}
\]

and in particular

\[
\boxed{
r^8A_{3m}'(r)\to0
\quad(r\downarrow0).}
\]

Integrating the radial ODE gives

\[
\boxed{
A_{3m}'(r)
=-r^{-8}
\int_0^r t^5s_{3m}(t)\,dt.
}
\]

---

## 5. Finite-radius identity

Integrate once more from `0` to `R`:

\[
\boxed{
A_{3m}(R)-A_{3m}(0)
=-\frac17
\int_0^R
\left(t^{-2}-t^5R^{-7}\right)
s_{3m}(t)\,dt.
}
\]

Equivalently,

\[
\boxed{
A_{3m}(0)
=A_{3m}(R)
+\frac17\int_0^Rt^{-2}s_{3m}(t)\,dt
-\frac1{7R^7}\int_0^Rt^5s_{3m}(t)\,dt.
}
\]

This is an exact boundary/source decomposition for every degree-three component.

---

## 6. Whole-space moment formula

Under the retained whole-space pressure normalization and decay, the degree-three pressure component at large radius is decaying rather than growing.
Thus

\[
A_{3m}(R)\to0
\qquad(R\to\infty).
\]

M17-050 gives

\[
S_P\in L^1(\mathbb R^3),
\qquad
\|S_P\|_1\le Z_*.
\]

This also controls the final finite-radius correction:

\[
\left|
R^{-7}\int_0^Rt^5s_{3m}(t)dt
\right|
\le CR^{-4}Z_*
\to0.
\]

Therefore

\[
\boxed{
A_{3m}(0)
=\frac17
\int_0^\infty r^{-2}s_{3m}(r)\,dr.
}
\]

This is the exact central harmonic-cubic moment formula.

---

## 7. Why the integral converges

Near `r=0`, analyticity of `S_P` implies its `l=3` component starts at order

\[
s_{3m}(r)=O(r^3).
\]

Hence

\[
r^{-2}s_{3m}(r)=O(r),
\]

which is integrable at the origin.

At infinity,

\[
\int_1^\infty r^2|s_{3m}(r)|dr
\le C\|S_P\|_1<\infty.
\]

Since `r^-2<=r^2` for `r>=1`, the weighted moment is also absolutely convergent there.

---

## 8. R^-4 tail of the cubic moment

Define the tail contribution

\[
\boxed{
A_{3m}^{tail}(R)
:=\frac17
\int_R^\infty r^{-2}s_{3m}(r)dr.
}
\]

Then

\[
\begin{aligned}
|A_{3m}^{tail}(R)|
&\le C\int_R^\infty r^{-2}
\int_{S^2}|S_P(r\omega)|d\omega\,dr\\
&=C\int_R^\infty r^{-4}
\left[r^2\int_{S^2}|S_P(r\omega)|d\omega\right]dr\\
&\le CR^{-4}\|S_P\|_1.
\end{aligned}
\]

Thus

\[
\boxed{
|A_{3m}^{tail}(R)|
\le CZ_*R^{-4}.
}
\]

This exactly matches the direct Newtonian-kernel estimate of M17-050.

---

## 9. Relation to the local cubic decomposition of M17-051

M17-051 writes

\[
P_3
=H_3
-\frac1{10}|x|^2(s\cdot x).
\]

On a sphere `|x|=r`, the particular term

\[
|x|^2(s\cdot x)
=r^3(s\cdot\omega)
\]

has angular degree one, not degree three.

Therefore the degree-three boundary projection isolates the harmonic cubic:

\[
\boxed{
\Pi_{l=3}P(r\omega)
=r^3H_3(\omega)+O(r^5).
}
\]

Hence

\[
\boxed{
H_3(\omega)
=\lim_{r\downarrow0}
r^{-3}\Pi_{l=3}P(r\omega).
}
\]

The coefficients of `H_3` are precisely the seven numbers `A_{3m}(0)` above.

---

## 10. DSAIG harmonic screening becomes a finite-dimensional moment map

Let

\[
C^{harm}_{ijk}=\partial_{ijk}H_3.
\]

The DSAIG harmonic tensor is

\[
N_{harm}
=TF_h[p_\ell C^{harm}_{\alpha\beta\ell}].
\]

Because `H_3` is determined by the seven coefficients `A_{3m}(0)`, there is a fixed linear map

\[
\boxed{
\mathcal L_p:\mathbb R^7
\to Sym_0(2)
}
\]

such that

\[
N_{harm}=\mathcal L_p(A_3).
\]

Here

\[
\dim Sym_0(2)=2.
\]

The persistent slanted alignment condition projects this tensor onto the one-dimensional direction perpendicular to the nonzero fixed tensor `Q_0`:

\[
\boxed{
P_{Q_0}^{\perp}N_{harm}
=\text{required scalar compensation}.
}
\]

Thus at a single time this is one linear constraint on a seven-component global source-moment vector.

It is restrictive, but not algebraically contradictory.

---

## 11. DSD audit

### Audit A — calling H_3 arbitrary harmonic gauge
Rejected. Whole-space pressure selection fixes it by the exact weighted source moment.

### Audit B — identifying H_3 with the local source-gradient particular cubic
Rejected. The particular cubic is angular `l=1`; `H_3` is angular `l=3`.

### Audit C — using one alignment scalar as a seven-dimensional contradiction
Rejected. Snapshot dimension counting leaves ample algebraic freedom.

### Audit D — ignoring far-tail control
Rejected. The portion outside radius `R` is explicitly `O(Z_*R^-4)`.

### Audit E — proof status
The harmonic cubic freedom has been converted to an exact global source-moment ledger, but recurrent dynamic locking remains open.

---

## 12. Updated Rank-1 pressure frontier

The DSAIG pressure third jet now consists of

\[
\boxed{
\text{explicit local source-gradient tensor}
\quad+\quad
\mathcal L_p\left[
\frac17\int_0^\infty r^{-2}s_3(r)dr
\right].
}
\]

The remote portion of the second term is `O(R^-4)`.

Therefore the surviving slanted branch requires a **recurrent finite-dimensional l=3 source-moment lock** to the materially frozen nodal tensor `Q_0`, together with the local viscous/source-gradient cancellation.

---

## 13. Next target — l=3 moment locking dynamics

The next highest-value Rank-1 calculation is to differentiate

\[
A_{3m}(0,\theta)
=\frac17\int_0^\infty r^{-2}s_{3m}(r,\theta)dr
\]

along the moving nodal core and express its perpendicular DSAIG projection in terms of

1. pressure-source production;
2. radial/angular source transport;
3. core-center motion;
4. the already quantified `R^-4` tail.

This should be compared directly with M17-046's Newtonian cubic transport identity.

The aim is to decide whether recurrent l=3 locking is an independent viable cycle or merely another form of the existing source-turnover/hysteresis ledger.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
