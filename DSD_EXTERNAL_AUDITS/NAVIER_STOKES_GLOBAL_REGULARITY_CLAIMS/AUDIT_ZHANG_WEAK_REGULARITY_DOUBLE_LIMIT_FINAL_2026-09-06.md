# DSD Final Deep Audit — Zhang Weak-Regularity / Mollifier–Galerkin Double-Limit Framework

Date: 2026-09-06
Source: Jia Hong Zhang, *Global Smooth Solutions to the 3D Incompressible Navier-Stokes Equations: Weakly Regular Framework and Multi-Scenario Adaptation*, Preprints.org, 2026-01-14, DOI 10.20944/preprints202601.0992.v1.

## Final status

**FAIL_ROOT.**

Several independent displayed steps fail. The verdict applies to this manuscript/version, not to the author.

---

# Claim

The manuscript claims unique global smooth solutions for initial data as weak as

\[
u_0\in L^2(\mathbb R^3)\cap\mathcal V,
\]

including \(u_0\notin H^1\), and forcing only

\[
f\in L^2([0,\infty);L^2(\mathbb R^3)).
\]

The proposed route is compactly supported mollification + Galerkin approximation + double-limit energy estimates + high-order induction.

---

# Root failure 1 — impossible uniform H1 initialization for arbitrary L2 data

Section 3.1 publicly states for the approximate initial data

\[
\|u_{N,\varepsilon}(0)\|_{H^1}
\le C\|u_0\|_{L^2},
\]

with \(C\) independent of \(N,\varepsilon\).

But the paper explicitly includes data

\[
u_0\in L^2\setminus H^1.
\]

If \(u_{N,\varepsilon}(0)\to u_0\) strongly in \(L^2\) and the sequence is uniformly bounded in \(H^1\), Banach–Alaoglu gives a subsequence weakly convergent in \(H^1\). The strong \(L^2\) limit identifies that weak \(H^1\) limit with \(u_0\). Therefore

\[
\boxed{u_0\in H^1,}
\]

contradicting the permitted \(L^2\setminus H^1\) class.

Equivalently, for ordinary frequency truncations the \(H^1\) norm necessarily grows with the cutoff for generic \(L^2\setminus H^1\) data.

Thus the claimed parameter-independent initialization estimate cannot hold on the manuscript's stated data class.

---

# Root failure 2 — the high-order induction differentiates an L2 force that has no derivatives

Section 4.1.1 states that to obtain arbitrary

\[
\partial_t^m\nabla^k u\in L^\infty([\delta,T];L^2)
\]

one applies

\[
\partial_t^M\nabla^K
\]

to both sides of NSE and says the external-force term is directly bounded by the assumed \(L^2\) condition.

But for \(K>0\) or \(M>0\), this creates

\[
\partial_t^M\nabla^K f.
\]

The declared hypothesis

\[
f\in L^2_tL^2_x
\]

does not define, much less bound, these derivatives.

Therefore the induction cannot even be formulated under the advertised forcing class.

This alone breaks the claimed \(C^\infty\) result for rough forcing.

---

# Root failure 3 — the induction base changes norm type

The stated target is an \(L^\infty_t L^2_x\) derivative bound.

For the purported \(k=1\) base, however, the manuscript cites only the energy estimate

\[
\int_0^T\|\nabla u(t)\|_2^2\,dt<\infty,
\]

i.e. an \(L^2_t H^1_x\) bound.

But

\[
L^2_t\not\subset L^\infty_t.
\]

Hence the displayed \(k=1\) basis does not establish the norm required by the induction hypothesis.

A parabolic smoothing theorem could potentially provide a positive-time \(L^\infty_tH^1\) bound under suitable hypotheses, but that would be a separate theorem and must control the nonlinear Duhamel term. It is not supplied by the basic energy inequality.

---

# Root failure 4 — misuse of the linear Stokes semigroup as nonlinear global control

For smooth initial data the manuscript invokes the linear estimate

\[
\|\nabla^k e^{-tA}u_0\|_2
\le C_k\|\nabla^k u_0\|_2
\]

and exports global high-order smoothness of the full NSE solution.

But the mild NSE solution is

\[
u(t)=e^{-tA}u_0
-\int_0^t e^{-(t-s)A}\mathbb P\nabla\cdot(u\otimes u)(s)\,ds
+\int_0^t e^{-(t-s)A}\mathbb Pf(s)\,ds.
\]

The linear homogeneous estimate controls only the first term. The unresolved 3D regularity difficulty is precisely the nonlinear Duhamel term.

Thus

\[
\boxed{
\text{global Stokes smoothing of }e^{-tA}u_0
\not\Rightarrow
\text{global NSE smoothing of }u.
}
\]

The manuscript's Section 5 inference skips the nonlinear continuation estimate that must be proved.

---

# Root failure 5 — false Sobolev embedding statement

The manuscript states

\[
H^s(\mathbb R^3)\subset C^\infty(\mathbb R^3)
\quad\text{for }s>3/2.
\]

This is false.

For fixed finite \(s>3/2\), Sobolev embedding yields finite Hölder/continuous regularity depending on \(s\), not \(C^\infty\).

Only control in sufficiently high Sobolev spaces for every derivative order can imply smoothness. But those high-order bounds are exactly what the preceding invalid induction was intended to establish.

---

# Additional algebraic error — pressure Poisson sign

With the manuscript's convention

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad \nabla\cdot u=0,
\]

taking divergence gives

\[
\boxed{
\Delta p
=\nabla\cdot f-\nabla\cdot((u\cdot\nabla)u).
}
\]

The manuscript displays the opposite sign ordering. This sign error is not by itself the main regularity failure, but is an independent displayed algebra mistake.

---

# What the valid double-limit estimates actually give

The manuscript's uniform estimates

\[
\sup_{N,\varepsilon}\sup_{t\le T}\|u_{N,\varepsilon}(t)\|_2^2<\infty,
\]

\[
\sup_{N,\varepsilon}\int_0^T\|\nabla u_{N,\varepsilon}\|_2^2dt<\infty,
\]

and a time-derivative bound in \(L^2_tH^{-1}_x\) are of the standard compactness type used to extract a Leray-class weak solution.

Aubin–Lions then yields local strong \(L^2\) compactness, but it does **not** upgrade this limit to global smoothness.

The missing upgrade is exactly a uniform critical/higher regularity estimate.

---

# Survivor

The Galerkin/Aubin–Lions portion is structurally compatible with standard weak-solution construction. It should be separated from the invalid smoothness upgrade rather than discarded.

---

# DSD regression tests

1. **Uniform approximation firewall**: if a uniform stronger-norm bound holds and approximants converge in a weaker norm, check whether it would force the original data into the stronger space.
2. **Derivative-of-data audit**: differentiating a PDE requires corresponding regularity of forcing unless parabolic maximal-regularity machinery replaces the operation.
3. **Norm-type inheritance**: \(L^2_t\) control cannot be silently used as \(L^\infty_t\) control.
4. **Linear/nonlinear semigroup firewall**: a homogeneous linear smoothing bound never controls the nonlinear Duhamel term for free.
5. **Fixed Sobolev order != C-infinity**.

## Verdict

\[
\boxed{
\text{the displayed double-limit framework does not prove global smoothness of 3D NSE.}
}
\]

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
