# DSD M17-146 — Quiet low-amplitude `kappa`-gradient recharge collapses to the scale-free director/weighted-Laplacian commutator

Date: 2026-09-05  
Canonical ID: **M17-146**

Status: **FORCING RECOMPRESSION / M17-145 GIVES `D_B K_xi=L_rho K_xi-(sigma+3/2)K_xi+F_xi`, `K_xi=D_xi kappa`, WITH `F_xi=L_rho(D_xi sigma)+C_xi[kappa+sigma]+D_xi R_geom`. ON THE QUIET LOW-AMPLITUDE COMPACT-HARD-HULL BRANCH, IF THE STRAIN JET ONE ORDER ABOVE THE TERMS USED IS UNIFORMLY BOUNDED AND THE NORMALIZED `log rho`, DIRECTOR, AND `kappa` JETS ARE UNIFORMLY BOUNDED, THEN `L_rho(D_xi sigma)->0`, `C_xi[sigma]->0`, AND `D_xi R_geom->0`. THE CURL-W PART OF `R_geom` SIMPLIFIES EXACTLY TO `rho (curl xi)·grad log rho`, SO IT VANISHES WITH AMPLITUDE. CONSEQUENTLY THE LEADING QUIET FOLD-DRIVER LAW BECOMES `D_BK_xi=L_rho K_xi-(3/2)K_xi+C_xi[kappa]+o(1)`. THE ONLY ORDER-ONE RECHARGE LEFT BY THIS AUDIT IS THE SCALE-FREE NONCOMMUTATIVITY OF THE MATERIAL DIRECTOR DERIVATIVE WITH THE WEIGHTED CE-H DIFFUSION OPERATOR. THIS TERM CONTAINS TRANSVERSE `kappa` HESSIAN AND DIRECTOR/LOG-AMPLITUDE GEOMETRY AND HAS NO CURRENT SIGN. THEREFORE THE FREQUENT GENERIC-FOLD SURVIVOR IS NOW A SPECIFIC NORMALIZED COMMUTATOR-RECHARGE PROBLEM RATHER THAN AN UNSTRUCTURED HIGH-JET BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-145

Define

\[
\boxed{K_\xi:=D_\xi\kappa.}
\]

M17-145 gives the exact active-set equation

\[
\boxed{
D_BK_\xi
=
L_\rho K_\xi
-\left(\sigma+\frac32\right)K_\xi
+\mathcal F_\xi,
}
\]

with

\[
\boxed{
\mathcal F_\xi
=
L_\rho(D_\xi\sigma)
+\mathcal C_\xi[\kappa+\sigma]
+D_\xi\mathcal R_{geom},
}
\]

and

\[
\boxed{
\mathcal C_\xi[f]
:=D_\xi(L_\rho f)-L_\rho(D_\xi f).
}
\]

The goal is to identify which pieces of `F_xi` can remain order one on the M17-133/142 low-amplitude quiet remote skeleton.

---

## 2. Explicit compact-hard-hull hypotheses for this reduction

Retain a fixed-width remote ribbon/fold neighborhood and assume:

1. quiet shell Dirichlet control

\[
R\int_{C_R}|\nabla U|^2dy\le J_*;
\]

2. sufficiently high uniform strain-jet bounds to apply the M17-144 interpolation hierarchy through the derivatives appearing in `L_rho(D_xi sigma)`;

3. uniform bounds on the required normalized jets of

\[
\psi:=\log\rho,
\qquad
\xi,
\qquad
\kappa;
\]

4. the low-amplitude strong-director regime

\[
\rho\to0,
\qquad
|J_\xi|\asymp1
\]

on the selected remote geometry.

Failure of any of these assumptions is retained as a separate high-jet/potential/unbounded-geometry exit.

---

## 3. Strain-derivative forcing vanishes

M17-144 gives the general local interpolation hierarchy

\[
\|\nabla^m\Sigma\|_\infty
=O\left(R^{-1/(2m+5)}\right)
\]

whenever one additional strain derivative is uniformly bounded.

The scalar

\[
D_\xi\sigma
\]

contains one derivative of `Sigma` plus lower terms.
Applying `L_rho`, whose coefficients are bounded by the normalized `psi` hard hull, introduces at most two additional spatial derivatives.

Thus, with a uniform fourth strain derivative available,

\[
\boxed{
L_\rho(D_\xi\sigma)
=o(1).
}
\]

A representative rate from the same interpolation ladder is controlled by the slowest third-strain-derivative decay,

\[
O(R^{-1/11}),
\]

up to lower-order terms. The exact exponent is not important; strict decay is.

---

## 4. The strain part of the commutator also vanishes

The exact commutator is

\[
\boxed{
\begin{aligned}
\mathcal C_\xi[f]
={}&
-(\Delta\xi)\cdot\nabla f
-2(\partial_i\xi_j)\partial_{ij}f\\
&+2\left(D_\xi\nabla\psi-D_{\nabla\psi}\xi\right)\cdot\nabla f.
\end{aligned}
}
\]

Set `f=sigma`.
Every coefficient involving `xi` and `psi` is uniformly bounded on the normalized hard hull, while

\[
\nabla\sigma\to0,
\qquad
\nabla^2\sigma\to0
\]

under the corresponding higher strain-jet assumptions.

Therefore

\[
\boxed{
\mathcal C_\xi[\sigma]
=o(1).
}
\]

---

## 5. Rewrite the geometric remainder in scale-separated form

M5-682 gives

\[
\mathcal R_{geom}
=-\frac2\rho\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+(\nabla\times W)\cdot\nabla\psi.
\]

Use

\[
\frac{\nabla^2\rho}{\rho}
=
\nabla^2\psi+\nabla\psi\otimes\nabla\psi.
\]

Thus the first term is

\[
-2\Sigma:
\left(
\nabla^2\psi+\nabla\psi\otimes\nabla\psi
\right),
\]

which is strain times bounded normalized geometry.

For the curl term,

\[
\nabla\times W
=\nabla\times(\rho\xi)
=\nabla\rho\times\xi+\rho\nabla\times\xi
=\rho\left(\nabla\psi\times\xi+\nabla\times\xi\right).
\]

Dot with `grad psi`:

\[
(\nabla\psi\times\xi)\cdot\nabla\psi=0.
\]

Therefore the curl contribution simplifies **exactly** to

\[
\boxed{
(\nabla\times W)\cdot\nabla\psi
=
\rho(\nabla\times\xi)\cdot\nabla\psi.
}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal R_{geom}
={}&
-2\Sigma:
\left(
\nabla^2\psi+\nabla\psi\otimes\nabla\psi
\right)\\
&+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi\\
&+\rho(\nabla\times\xi)\cdot\nabla\psi.
\end{aligned}
}
\]

This form cleanly separates strain-weighted and amplitude-weighted pieces.

---

## 6. `D_xi R_geom` vanishes on the quiet low-amplitude hard hull

Differentiate the representation above along `xi`.

The first two groups contain either `Sigma` or `nabla Sigma` multiplied by bounded normalized `psi`/director jets.
They therefore vanish by the quiet high-jet strain decay.

The last group contains an explicit factor `rho`.
Since

\[
D_\xi\rho
=\rho D_\xi\log\rho
=\rho g,
\]

and `g` is bounded on the retained hard hull, its `xi` derivative remains `O(rho)` after differentiating the bounded normalized factors.
At the peak/fold itself `g=0`, so the amplitude derivative term is even simpler.

Consequently

\[
\boxed{
D_\xi\mathcal R_{geom}
=o(1).
}
\]

---

## 7. Leading quiet forcing

Combine Sections 3, 4, and 6:

\[
\mathcal F_\xi
=
\mathcal C_\xi[\kappa]
+o(1).
\]

Therefore the quiet low-amplitude fold-driver law becomes

\[
\boxed{
D_BK_\xi
=
L_\rho K_\xi
-\frac32K_\xi
+\mathcal C_\xi[\kappa]
+o(1),
}
\]

because

\[
\sigma=o(1).
\]

This is the main reduction of M17-146.

---

## 8. The surviving commutator is fully scale-free

Explicitly,

\[
\boxed{
\begin{aligned}
\mathcal C_\xi[\kappa]
={}&
-(\Delta\xi)\cdot\nabla\kappa
-2(\partial_i\xi_j)\partial_{ij}\kappa\\
&+2\left(D_\xi\nabla\psi-D_{\nabla\psi}\xi\right)\cdot\nabla\kappa.
\end{aligned}
}
\]

Every quantity here is invariant under constant amplitude rescaling

\[
\rho\mapsto\varepsilon\rho
\]

at the fixed-time CE-H/director level:

- `xi` is unchanged;
- spatial derivatives of `psi=log rho` are unchanged;
- `kappa` and its derivatives are unchanged.

Hence `C_xi[kappa]` is exactly the kind of normalized recharge that survives every quadratic low-amplitude ledger used so far.

---

## 9. Why this is not merely a generic high-jet escape

The surviving forcing uses only a finite explicit set of jets:

\[
\nabla\xi,
\quad
\nabla^2\xi,
\quad
\nabla\psi,
\quad
\nabla^2\psi,
\quad
\nabla\kappa,
\quad
\nabla^2\kappa.
\]

Thus, under finite analytic hard-hull control, the fold survivor is not hidden in uncontrolled arbitrarily high derivatives.
It is a concrete finite-dimensional local jet mechanism.

The hard question becomes whether this finite normalized geometry can repeatedly overcome the `3/2` damping on almost all director-flux carriers.

---

## 10. Principal diffusion versus commutator recharge

The leading equation is

\[
D_BK_\xi
=
L_\rho K_\xi
-\frac32K_\xi
+\mathcal C_\xi[\kappa]
+o(1).
\]

There are now only three leading mechanisms:

1. weighted diffusion/transport of existing `K_xi` through `L_rho K_xi`;
2. universal similarity damping `-3K_xi/2`;
3. scale-free director/multiplier commutator recharge `C_xi[kappa]`.

Ordinary strain recharge and explicit amplitude-weighted geometric forcing have disappeared from the leading quiet limit under the stated compactness assumptions.

---

## 11. Persistent ribbon comparison

M17-144 gives, on a persistent quiet critical ribbon,

\[
K_\xi=D_\xi\kappa\to0.
\]

The reduced law then implies that persistence of this small `K_xi` also requires the leading source balance

\[
\boxed{
L_\rho K_\xi
+\mathcal C_\xi[\kappa]
=o(1)
}
\]

along the ribbon.

Thus the persistent-ribbon branch is not only `xi`-flat in `kappa`; it asymptotically lies on a weighted-diffusion/commutator balance manifold.

No contradiction follows yet because the two terms are signed and can cancel.

---

## 12. DSD audit

### Audit A — all of `F_xi` vanishes because strain vanishes

Rejected.
`C_xi[kappa]` is independent of strain amplitude and survives.

### Audit B — the curl-W remainder is scale-free

Rejected after exact simplification:

\[
(\nabla\times W)\cdot\nabla\log\rho
=
\rho(\nabla\times\xi)\cdot\nabla\log\rho.
\]

It carries an explicit amplitude factor.

### Audit C — `C_xi[kappa]` is an uncontrolled infinite-order term

Rejected.
It uses only finite first/second normalized jets.

### Audit D — the `-3/2` damping closes the branch by itself

Rejected.
`L_rho K_xi` and `C_xi[kappa]` can be order one and have no established sign.

### Audit E — the reduced equation proves repeated folds are realizable

Rejected.
It identifies the only leading quiet normalized recharge mechanism; full compatibility and recurrence remain to be proved or excluded.

---

## 13. Updated frontier

The quiet frequent-fold firewall has now been sharpened to

\[
\boxed{
D_B(D_\xi\kappa)
=
L_\rho(D_\xi\kappa)
-\frac32D_\xi\kappa
+[D_\xi,L_\rho]\kappa
+o(1).
}
\]

Therefore the next highest-value gate is:

\[
\boxed{
\text{Can }[D_\xi,L_\rho]\kappa
\text{ recurrently supply order-one recharge on asymptotically full }d\Phi_J\text{ measure?}
}
\]

The next calculation should project this commutator into the pure-kernel frame `(xi,k,n)` and test whether the tangency/ribbon flatness identities remove any of its Hessian components or force a signed finite-jet balance.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
