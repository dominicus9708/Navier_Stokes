# DSD M19-102 — Finite-dimensional extra center obeys a compact-core Ky-Fan eigenvalue budget

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-095 QUASI-COMPACTNESS TURNED INTO A SHARP NECESSARY SPECTRAL BUDGET FOR EVERY EXTRA ZERO-GROWTH CENTER DIRECTION / THIS DOES NOT YET FORCE THE EXTRA CENTER TO VANISH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting point

M19-087--095 reduce the symmetry-transverse linearized vorticity problem to

\[
\partial_s\eta
=\mathcal L_0\eta+\mathcal K(s)\eta,
\]

where

\[
\mathcal L_0=\nu\Delta-1-\frac12y\cdot\nabla
\]

has the exact unweighted `L2` energy gap

\[
\langle \eta,\mathcal L_0\eta\rangle
=-\nu\|\nabla\eta\|_2^2-\frac14\|\eta\|_2^2,
\]

and, on the controlled critical-tail corridor,

\[
\mathcal K(s)
\]

is a relatively compact background perturbation of the bare generator.

Let

\[
\mathcal K_s^{sym}:=\frac12(\mathcal K(s)+\mathcal K(s)^*)
\]

be its symmetric part on the retained vorticity Hilbert space.

---

## 2. Assume an `m`-dimensional extra center

After quotienting the certified rotational symmetry directions and separating the time tangent, suppose that there is an extra zero-growth center bundle

\[
E_{extra}^c(s)
\]

of dimension

\[
m\ge1.
\]

Choose an orthonormal moving frame

\[
\eta_1(s),\ldots,\eta_m(s)
\]

for this bundle in vorticity `L2`.

For the induced `m`-volume, the logarithmic derivative is the trace of the symmetric generator restricted to the moving center space. Therefore

\[
\frac d{ds}\log\operatorname{Vol}_m
=
-\nu\sum_{j=1}^m\|\nabla\eta_j\|_2^2
-\frac m4
+\sum_{j=1}^m
\langle\eta_j,\mathcal K_s^{sym}\eta_j\rangle.
\]

If all `m` Lyapunov exponents are zero, the long-time mean of the left side is zero.

Hence

\[
\boxed{
\left\langle
\sum_{j=1}^m
\langle\eta_j,\mathcal K_s^{sym}\eta_j\rangle
\right\rangle
=
\frac m4
+\nu
\left\langle
\sum_{j=1}^m\|\nabla\eta_j\|_2^2
\right\rangle.
}
\]

In particular,

\[
\boxed{
\left\langle
\operatorname{Tr}
\bigl(P_{E_{extra}^c(s)}\mathcal K_s^{sym}P_{E_{extra}^c(s)}\bigr)
\right\rangle
\ge\frac m4.
}
\]

This is stronger than the single-vector quarter-gap statement.

---

## 3. Ky-Fan domination

Let

\[
\lambda_1^+(s)\ge\lambda_2^+(s)\ge\cdots\ge0
\]

be the positive eigenvalues of the compact self-adjoint operator

\[
(\mathcal K_s^{sym})_+.
\]

The Ky-Fan maximum principle gives, for every `m`-dimensional subspace,

\[
\operatorname{Tr}
\bigl(P_E\mathcal K_s^{sym}P_E\bigr)
\le
\sum_{j=1}^m\lambda_j^+(s).
\]

Therefore every `m`-dimensional zero center must satisfy

\[
\boxed{
\frac m4
\le
\left\langle
\sum_{j=1}^m\lambda_j^+(s)
\right\rangle.
}
\]

Equivalently, the compact background coupling must supply at least one quarter unit of positive symmetric spectral weight per extra neutral dimension.

---

## 4. Uniform compactness over the recurrent hull

M19-095 places the background on a compact recurrent hull and identifies `K(s)` as a compact perturbation depending continuously on the background in the retained smooth topology.

Hence the set

\[
\{\mathcal K_s^{sym}:s\in\mathbb R\}
\]

has compact closure in the compact-operator norm on the retained corridor.

Therefore its singular/eigenvalue tails vanish uniformly:

for every

\[
\varepsilon>0
\]

there exists a finite

\[
N_\varepsilon
\]

such that

\[
\boxed{
\sup_s\lambda_{N_\varepsilon+1}^+(s)
\le\varepsilon.
}
\]

Choose

\[
0<\varepsilon<\frac14.
\]

Define the finite core spectral budget

\[
C_\varepsilon
:=
\sup_s
\sum_{j=1}^{N_\varepsilon}\lambda_j^+(s).
\]

Then for any `m>N_epsilon`,

\[
\sum_{j=1}^m\lambda_j^+(s)
\le
C_\varepsilon
+\varepsilon(m-N_\varepsilon).
\]

Combining with the zero-center requirement yields

\[
\frac m4
\le
C_\varepsilon
+\varepsilon(m-N_\varepsilon).
\]

Thus

\[
\boxed{
 m
\le
\frac{C_\varepsilon-\varepsilon N_\varepsilon}
{\frac14-\varepsilon}
}
\]

whenever the numerator is positive, with the obvious finite bound obtained by replacing the numerator by its positive part and adjoining `N_epsilon` when needed.

The exact numerical expression is less important than the structural conclusion:

\[
\boxed{
\dim E_{extra}^c
\text{ is controlled entirely by finitely many positive compact-core eigenchannels.}
}
\]

---

## 5. Sharp closure criterion

The same argument gives an immediate sufficient condition for **no** extra center:

if

\[
\boxed{
\left\langle\lambda_1^+(s)\right\rangle<\frac14,
}
\]

then no symmetry-transverse zero-growth center direction can exist.

More generally, if for every `m>=1`

\[
\boxed{
\left\langle
\sum_{j=1}^m\lambda_j^+(s)
\right\rangle
<\frac m4,
}
\]

then

\[
\boxed{E_{extra}^c=\{0\}.}
\]

This is the finite-dimensional spectral form of the live theorem.

---

## 6. What this calculation achieves

The unresolved center problem no longer needs to control the full infinite-dimensional scattering boundary space.

It is enough to understand the finitely many positive eigenchannels of

\[
\mathcal K_s^{sym}
\]

inside the compact core.

Thus the live theorem becomes

\[
\boxed{
\mathcal T_{core\text{-}KyFan}:
\text{show that the recurrent compact-core Ky-Fan averages stay below }m/4
\text{ on every symmetry-transverse }m\text{-plane}.
}
\]

---

## 7. Firewall

This module does **not** prove the required strict inequality.

A compact operator may possess finitely many sufficiently large positive eigenvalues, and M19-093--094 already show that the known unsigned derivative budgets do not automatically rule them out.

Therefore

\[
\boxed{
\text{finite-dimensional center}
\neq
\text{symmetry-only center}.
}
\]

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
