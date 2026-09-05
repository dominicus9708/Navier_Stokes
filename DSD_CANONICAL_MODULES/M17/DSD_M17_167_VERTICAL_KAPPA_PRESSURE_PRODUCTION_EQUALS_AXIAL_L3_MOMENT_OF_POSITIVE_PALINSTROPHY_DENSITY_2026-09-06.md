# DSD M17-167 — On a vertical nodal filament the global `-kappa rho^2` axial pressure-production channel equals the axial `l=3` moment of the positive palinstrophy density

Date: 2026-09-06  
Canonical ID: **M17-167**

Status: **EXACT POSITIVE-DENSITY REWRITE / THE CE-H ELLIPTIC EQUATION `Delta W=kappa W` GIVES THE POINTWISE IDENTITY `kappa rho^2=(1/2)Delta(rho^2)-|grad W|^2`. PAIRING WITH THE DISTRIBUTIONAL AXIAL STF NEWTONIAN KERNEL PRODUCES `Pi_{V,kappa}^{prod}=<|grad W|^2,K_333>-(1/2)partial_333 rho^2(Y)`. ON A VERTICAL REGULAR NODAL FILAMENT `W(Y)=0` AND `partial_3 W(Y)=0`, SO `partial_333 rho^2(Y)=0`. HENCE `Pi_{V,kappa}^{prod}(Y)=<|grad W|^2,K_333(Y-.)>` EXACTLY. THE GLOBAL KAPPA-PAYER COVARIANCE IS THEREFORE EQUIVALENT TO THE AXIAL l=3 ANGULAR DISTRIBUTION OF A POSITIVE PALINSTROPHY DENSITY. THIS DOES NOT FIX THE SIGN BECAUSE `K_333` CHANGES SIGN, BUT IT CONVERTS THE REMAINING GLOBAL ARCHITECTURE INTO A POSITIVE-MEASURE ANGULAR-ANISOTROPY PROBLEM AND OPENS COERCIVE PALINSTROPHY BOUNDS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pointwise CE-H energy identity

The scalar CE-H elliptic equation is

\[
\boxed{\Delta W=\kappa W.}
\]

Let

\[
\rho^2:=|W|^2.
\]

Then

\[
\Delta\rho^2
=2|\nabla W|^2+2W\cdot\Delta W.
\]

Using `Delta W=kappa W`,

\[
\boxed{
\kappa\rho^2
=\frac12\Delta\rho^2-|\nabla W|^2.
}
\]

This identity is exact and does not use a local Taylor expansion.

---

## 2. Pair with the global axial STF kernel

M17-089 defines

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=-\langle\kappa\rho^2,\mathcal K_{333}(Y-\cdot)\rangle.
}
\]

Insert Section 1:

\[
\Pi_{V,\kappa}^{prod}
=-\frac12\langle\Delta\rho^2,\mathcal K_{333}\rangle
+\langle|\nabla W|^2,\mathcal K_{333}\rangle.
\]

The Newtonian kernel is

\[
G(z)=\frac1{4\pi|z|},
\qquad
-\Delta G=\delta_0,
\]

and

\[
\mathcal K_{333}=\partial_{333}G.
\]

Therefore, distributionally,

\[
\Delta\mathcal K_{333}
=-\partial_{333}\delta_0.
\]

Hence

\[
\langle\Delta\rho^2,\mathcal K_{333}(Y-\cdot)\rangle
=\partial_{333}\rho^2(Y).
\]

Thus the general identity is

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=\langle|\nabla W|^2,\mathcal K_{333}(Y-\cdot)\rangle
-\frac12\partial_{333}\rho^2(Y).
}
\]

---

## 3. The local distributional correction vanishes on the vertical filament

At a regular nodal filament,

\[
W(Y)=0.
\]

On the vertical branch M17-090 also gives

\[
\boxed{\partial_3W(Y)=0}
\]

because `q_13=q_23=0` and `W_3=0`.

For a vector field,

\[
\partial_{333}|W|^2
=2\sum_a
\left(
3W_{a,3}W_{a,33}
+W_aW_{a,333}
\right).
\]

At the vertical nodal core both factors vanish:

\[
W_a(Y)=0,
\qquad
W_{a,3}(Y)=0.
\]

Therefore

\[
\boxed{
\partial_{333}\rho^2(Y)=0.
}
\]

---

## 4. Exact vertical positive-density representation

Sections 2--3 yield

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=\langle|\nabla W|^2,\mathcal K_{333}(Y-\cdot)\rangle.
}
\]

Thus the `-kappa rho^2` pressure-production channel can be represented either as

\[
\boxed{
-\langle\kappa\rho^2,K_{333}\rangle
}
\]

or exactly as

\[
\boxed{
\langle|\nabla W|^2,K_{333}\rangle
}
\]

on the vertical nodal filament.

The density

\[
\boxed{|\nabla W|^2\ge0}
\]

is positive.

---

## 5. What sign-indefiniteness remains

Positivity of the density does **not** make the moment positive because

\[
\mathcal K_{333}(z)
=\frac{3}{4\pi}
\frac{z_3(3|z|^2-5z_3^2)}{|z|^7}
\]

changes sign in angle.

Therefore the missing information is now purely geometric:

\[
\boxed{
\text{how the positive palinstrophy density is distributed among the }K_{333}\text{ angular sign sectors}.
}
\]

This is a narrower covariance problem than the original scalar payer formulation.

---

## 6. Spherical shell representation

Write `z=rn`, `n in S^2`, and define

\[
\boxed{
\mathfrak p_3(r;Y)
:=\int_{S^2}
|\nabla W(Y-rn)|^2
\,k_3(n)\,d\omega(n),
}
\]

with

\[
\boxed{
k_3(n):=\frac{3}{4\pi}n_3(3-5n_3^2).}
\]

Since

\[
\mathcal K_{333}(rn)=r^{-4}k_3(n),
\]

we obtain

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=\int_0^\infty r^{-2}\mathfrak p_3(r;Y)dr.
}
\]

The global covariance is therefore a one-dimensional radial integral of the `l=3` angular palinstrophy coefficient.

---

## 7. Local behavior of the palinstrophy shell coefficient

Smoothness and spherical-harmonic orthogonality imply that the `l=3` shell coefficient has the expansion

\[
\mathfrak p_3(r;Y)=c_{pal}O_Vr^3+O(r^4)
\]

for a universal coefficient consistent with M17-164.

Indeed M17-164 gives

\[
\int_0^Rr^{-2}\mathfrak p_3(r)dr
=\frac37R^2O_V+O(R^3),
\]

so differentiating the leading term gives

\[
\boxed{
\mathfrak p_3(r;Y)
=\frac67O_Vr^3+O(r^4).
}
\]

Thus the local octupole is equivalently

\[
\boxed{
O_V
=\frac76\lim_{r\downarrow0}r^{-3}\mathfrak p_3(r;Y).
}
\]

---

## 8. Angular-anisotropy bound by total palinstrophy

Because `k_3` is bounded on `S^2`,

\[
\boxed{
|\mathfrak p_3(r;Y)|
\le C_3
\int_{S^2}|\nabla W(Y-rn)|^2d\omega.
}
\]

Hence any mesoscopic/global cancellation of the local octupole requires actual positive palinstrophy mass in the relevant angular sectors.

This opens a coercive route that was unavailable when the source was viewed only as signed `kappa rho^2` payer mass.

---

## 9. Relation to M17-166

M17-166 defines the cumulative normalized scale current from the `kappa rho^2` representation.
M17-167 shows that the same cumulative can be represented globally through the positive palinstrophy shell coefficient.

Thus

\[
\boxed{
\text{radial }l=3\text{ scale current}
\leftrightarrow
\text{angular redistribution of positive palinstrophy density}.
}
\]

The outer cancellation is therefore a palinstrophy anisotropy architecture, not an arbitrary signed scalar source.

---

## 10. DSD audit

### Audit A — losing the distributional correction
Avoided. The general correction is `-(1/2)partial_333 rho^2(Y)`.

### Audit B — setting that correction to zero away from the vertical nodal branch
Rejected. The cancellation uses both `W(Y)=0` and `partial_3W(Y)=0`.

### Audit C — inferring a sign from positive palinstrophy density
Rejected because `K_333` changes sign angularly.

### Audit D — replacing angular palinstrophy by scalar total palinstrophy
Only the inequality in Section 8 is valid; angular covariance remains essential.

### Audit E — proof status
The global source is converted to a positive-density angular problem, not signed.

---

## 11. Updated vertical Rank-1 gate

The vertical kappa-production channel is now exactly

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=\int_0^\infty r^{-2}\mathfrak p_3(r)dr,
}
\]

with

\[
\boxed{
\mathfrak p_3(r)
=\frac67O_Vr^3+O(r^4)
}
\]

near the crossing core and positive-density bound

\[
|\mathfrak p_3(r)|
\le C_3\int_{S^2}|\nabla W|^2d\omega.
\]

The next target is to quantify the minimum palinstrophy/angular-redistribution cost required for the outer shells to reverse or neutralize the local octupole orientation under recurrent M5 crossings.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
