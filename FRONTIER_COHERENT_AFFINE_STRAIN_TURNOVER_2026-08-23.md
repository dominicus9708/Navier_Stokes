# Frontier — Coherent Affine-Strain Turnover — 2026-08-23

Overall status: **ACTIVE FRONTIER — GLOBAL REGULARITY NOT PROVED.**

This note is the continuation pointer after the historical-shell and active-remote-halo reductions.

---

## 1. Current reduction

The remote-strain functional now satisfies the Galilean-invariant estimate

\[
\boxed{
|\mathcal S_R|
\le
C R^{-2}
\sum_{k\ge0}4^{-k}
\mathcal C_{2^{k+1}R}^{1/2},
}
\]

where

\[
\mathcal C_\rho
=
\rho^{-1}
\int_{B_\rho}|U-(U)_{B_\rho}|^2.
\]

Thus

\[
\boxed{
|\mathcal S_R|\ge s_0
\Longrightarrow
\exists\rho\ge R:
\mathcal C_\rho\gtrsim s_0^2R^4.
}
\]

Uniform relative Campanato control therefore removes active remote influence at normalized radius infinity.

The `R^4` escalation is saturated by a coherent affine field `U ~ A y`. Hence the surviving active obstruction is no longer best described as diffuse `H_remote`; it is a coherent affine-strain / relative-energy reservoir.

---

## 2. Physical-radius compression

Global kinetic energy gives

\[
\boxed{
R\lesssim W^{1/10},
\qquad
\ell=RW^{-1/2}\lesssim W^{-2/5}.
}
\]

For `W_j=q^jW_0`, a persistently active source therefore has total logarithmic physical-radius contraction at least

\[
\frac25J\log q-O(1)
\]

through stage `J`.

Consequently infinitely many stages satisfy

\[
\boxed{
\left[\log\frac{\ell_j}{\ell_{j+1}}\right]_+
\ge
\frac15\log q.
}
\]

This contraction cannot automatically be identified with material-line shortening unless the tracked center is itself material.

---

## 3. Exact turnover ledger

For a moving cutoff

\[
\phi(x,t)=\Phi\!\left(\frac{x-X(t)}{\ell(t)}\right),
\]

weighted mean `bar u_phi`, relative velocity `v=u-bar u_phi`, and

\[
V_\phi=\frac12\int\phi|v|^2,
\]

the exact identity is

\[
\boxed{
V_\phi'+\nu D_\phi
=
\mathcal T_{mat}
+\mathcal T_{rad}
+\mathcal T_{vis}
+\mathcal T_{pres}.
}
\]

The four terms are respectively material boundary crossing, radius motion, viscous boundary leakage, and pressure work.

Therefore a coherent relative-energy reservoir can change only through an explicitly listed turnover payer or interior viscous dissipation.

---

## 4. Safe current trichotomy

The active remote branch is now

\[
\boxed{
\text{active remote influence}
\Longrightarrow
\text{coherent relative-energy escalation}
\Longrightarrow
\begin{cases}
\text{same material source contracts},\\
\text{tracked center drifts},\\
\text{active source is replaced},\\
\text{pressure/viscous boundary action pays}.
\end{cases}
}
\]

In the same-material + material-center subcase, if

\[
\|\Sigma\|_\infty\le B_+,
\]

the infinitely recurring strong-contraction stages obey

\[
\boxed{
L_j\ge\frac{\log q}{5B_+}.
}
\]

The other cases must be closed by the relative-variance ledger rather than a material-line inequality.

---

## 5. Relation to the ancient compactness gap

For an affine field,

\[
A(R)=R^{-1}\int_{B_R}|U|^2\sim R^4.
\]

Thus the coherent affine-strain corridor is exactly the obstruction to an expanding-radius uniform Type-I local-energy bound in the first-hitting compactness bridge.

This unifies two previously separate gaps:

\[
\boxed{
\text{active }H_{remote}
\quad\text{and}\quad
\text{failure of expanding-tower local-energy compactness}
}
\]

are now the same relative-Campanato/affine obstruction at the present level of the proof.

---

## 6. Next exact proof obligation

The next target is no longer a generic remote-derivative estimate. It is the finite-stage lemma

\[
\boxed{
\text{relative Campanato escalation or coherent-reservoir replacement}
\Longrightarrow
\mathcal T_j\ge \tau_*>0,
}
\]

where `T_j` is built from the normalized time integral of

\[
|\mathcal T_{mat}|,
\quad
|\mathcal T_{rad}|,
\quad
|\mathcal T_{vis}|,
\quad
|\mathcal T_{pres}|,
\quad
\nu D_\phi.
\]

An equivalent acceptable closure is to prove directly that avoiding this turnover action implies

\[
\boxed{
\sup_j\sup_{1\le\rho\le R_j^{max}}
\mathcal C_{j,\rho}<\infty,
\qquad
R_j^{max}\to\infty.
}
\]

That statement would simultaneously:

1. eliminate dynamically active `H_remote` at normalized infinity by the `R^{-2}` gate;
2. supply the relative-energy part of the expanding Type-I compactness bridge;
3. leave only bounded-radius compact dynamics / turnover alternatives.

---

## 7. Caution

Ordinary global kinetic energy and dissipation do **not** by themselves close the affine corridor. For `U ~ A y`,

\[
\int_{B_R}|\nabla U|^2\sim R^3,
\]

and the corresponding physical stage cost is

\[
W^{-1/2}R^3,
\]

which can remain summable for sufficiently slowly growing `R`. Therefore the remaining step genuinely requires the moving relative-energy/turnover structure or an external rigidity theorem; it cannot be replaced by a naive energy-budget argument.

Status: **THE PROOF TREE HAS BEEN REDUCED TO A COHERENT AFFINE-STRAIN / RELATIVE-CAMPANATO TURNOVER CLOSURE PLUS THE BOUNDED-RADIUS ANCIENT-LIMIT RIGIDITY PROBLEM. NO GLOBAL REGULARITY PROOF IS CLAIMED.**