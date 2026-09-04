# DSD M17-121 — Dyadic Biot–Savart/Herz bridge converts the M5 Dirichlet tail to a vorticity critical stack

Date: 2026-09-05
Canonical ID: **M17-121**

Status: **EXACT DYADIC NORM BRIDGE / THE M5 NON-L3 OBSTRUCTION `sum (R_k e_k)^(3/2)=infinity`, ORIGINALLY WRITTEN WITH FULL DIRICHLET SHELL ENERGY `e_k=int |grad U|^2`, IS EQUIVALENT AT THE DYADIC SEQUENCE LEVEL TO DIVERGENCE OF THE CORRESPONDING VORTICITY STACK. LOCAL SHELL IDENTITIES DO HAVE BOUNDARY/HARMONIC LEAKAGE, BUT THE GLOBAL BIOT–SAVART OPERATOR HAS SUMMABLE OFF-DIAGONAL DYADIC DECAY, WHICH GIVES AN `ell^3` CONVOLUTION BOUND. THIS REMOVES THE LOCAL HODGE-BOUNDARY FIREWALL FROM THE FLUX-CAPTURE PROBLEM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. M5 critical shell number

Let

\[
A_k=\{R_k<|y|<2R_k\},
\qquad R_k=2^kR_0,
\]

and define

\[
e_k^\nabla:=\int_{A_k}|\nabla U|^2dy,
\qquad
 e_k^\omega:=\int_{A_k}|\Omega|^2dy,
\qquad
\Omega=\nabla\times U.
\]

The enlarged-annulus version used by M5 differs only by a uniformly finite neighboring sum, so it is equivalent for the `ell^{3/2}` stack.

Set

\[
\boxed{
a_k:=R_k^{1/2}\|\nabla U\|_{L^2(A_k)},
\qquad
b_k:=R_k^{1/2}\|\Omega\|_{L^2(A_k)}.
}
\]

Then

\[
(a_k)^3=(R_ke_k^\nabla)^{3/2},
\qquad
(b_k)^3=(R_ke_k^\omega)^{3/2}.
\]

---

## 2. Easy direction

Pointwise,

\[
|\Omega|^2\le 2|\nabla U|^2.
\]

Therefore

\[
\boxed{b_k\le\sqrt2\,a_k}
\]

and hence

\[
\boxed{
\|b\|_{\ell^3}\le\sqrt2\,\|a\|_{\ell^3}.
}
\]

---

## 3. Biot–Savart representation

For the retained decaying/global-L6 ancient profile, no nonzero harmonic addendum survives at infinity, and

\[
\nabla U=T\Omega
\]

with `T` a zero-order Calderon–Zygmund/Biot–Savart operator whose kernel satisfies

\[
|K(x-y)|\lesssim |x-y|^{-3}.
\]

Decompose

\[
\Omega=\sum_\ell \Omega_\ell,
\qquad
\Omega_\ell:=\Omega\mathbf 1_{A_\ell}.
\]

---

## 4. Outer-to-inner dyadic interaction

If `ell >= k+3`, then for `x in A_k`, `y in A_ell`,

\[
|x-y|\asymp R_\ell.
\]

Cauchy–Schwarz gives

\[
\|T\Omega_\ell\|_{L^2(A_k)}
\lesssim
\left(\frac{R_k}{R_\ell}\right)^{3/2}
\|\Omega_\ell\|_2.
\]

Multiplying by `R_k^{1/2}` and using

\[
\|\Omega_\ell\|_2=R_\ell^{-1/2}b_\ell
\]

gives

\[
\boxed{
R_k^{1/2}\|T\Omega_\ell\|_{L^2(A_k)}
\lesssim
2^{-2(\ell-k)}b_\ell.
}
\]

---

## 5. Inner-to-outer dyadic interaction

If `ell <= k-3`, then

\[
|x-y|\asymp R_k,
\]

and similarly

\[
\|T\Omega_\ell\|_{L^2(A_k)}
\lesssim
\left(\frac{R_\ell}{R_k}\right)^{3/2}
\|\Omega_\ell\|_2.
\]

Hence

\[
\boxed{
R_k^{1/2}\|T\Omega_\ell\|_{L^2(A_k)}
\lesssim
2^{-(k-\ell)}b_\ell.
}
\]

---

## 6. Near-diagonal interaction

For

\[
|\ell-k|\le2,
\]

the global `L^2` boundedness of the Calderon–Zygmund operator gives

\[
\boxed{
R_k^{1/2}\|T\Omega_\ell\|_{L^2(A_k)}
\lesssim b_\ell,
}
\]

because `R_k/R_ell` is bounded above and below by universal constants.

---

## 7. Summable discrete kernel

Combining the three regimes,

\[
\boxed{
 a_k
\lesssim
\sum_{\ell\le k-3}2^{-(k-\ell)}b_\ell
+
\sum_{|\ell-k|\le2}b_\ell
+
\sum_{\ell\ge k+3}2^{-2(\ell-k)}b_\ell.
}
\]

The coefficient sequence is in `ell^1(Z)`. Discrete Young therefore gives

\[
\boxed{
\|a\|_{\ell^3}
\le C\|b\|_{\ell^3}.
}
\]

Together with Section 2,

\[
\boxed{
\|a\|_{\ell^3}\asymp\|b\|_{\ell^3}.
}
\]

Equivalently,

\[
\boxed{
\sum_k(R_ke_k^\nabla)^{3/2}<\infty
\iff
\sum_k(R_ke_k^\omega)^{3/2}<\infty.
}
\]

---

## 8. Consequence for the M5 non-L3 survivor

M5 proves on the retained ancient non-L3 branch

\[
\sum_k(R_ke_k^\nabla)^{3/2}=\infty.
\]

Hence M17-121 upgrades this to

\[
\boxed{
\sum_k
\left(
R_k\int_{A_k}|\Omega|^2dy
\right)^{3/2}
=\infty.
}
\]

Thus the critical tail cannot be carried purely by local irrotational/harmonic strain leakage. It has a genuinely vortical dyadic critical stack.

---

## 9. DSD audit

### Audit A — local equality of strain and vorticity shell energies

Rejected. On a bounded annulus,

\[
\int|\nabla U|^2
\]

and

\[
\int|\Omega|^2
\]

differ by a boundary divergence term.

### Audit B — discarding the boundary term shell by shell

Rejected. The bridge is not a local shell identity; it is a global dyadic operator estimate.

### Audit C — hidden harmonic velocity field

Excluded by the retained global decay/L6 class used for the ancient profile. A separate nondecaying harmonic addendum would invalidate the simple Biot–Savart reconstruction and is outside this branch.

### Audit D — enlarged-annulus mismatch

Harmless for this sequence statement: each enlarged shell is a finite sum of neighboring dyadic shells, and finite-neighbor convolution preserves `ell^3` finiteness/divergence equivalence.

### Audit E — proof status

This converts the critical stack to vorticity form. It does not yet prove that Rank-2 ribbons carry a definite fraction of that stack.

---

## 10. Updated flux-capture target

Define the vorticity critical shell number

\[
\boxed{
J_k^\omega
:=
R_k\int_{A_k}|\Omega|^2dy.
}
\]

The retained non-L3 branch forces

\[
\boxed{
\sum_k(J_k^\omega)^{3/2}=\infty.
}
\]

The Rank-2 ribbon problem can therefore be posed directly in the same quantity carried by the ribbon amplitude:

\[
\boxed{
J_{k,\mathrm{ribbon}}^\omega
\stackrel{?}{\lesssim}
K_k\Phi_k.
}
\]

The next module derives the exact flux-coordinate disintegration and identifies the precise nondegeneracy needed for this comparison.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
