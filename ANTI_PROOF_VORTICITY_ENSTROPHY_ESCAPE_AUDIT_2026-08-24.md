# Anti-Proof Audit — Normalized Enstrophy Escape — 2026-08-24

Status: **LOGICAL GAP IDENTIFIED AND QUANTITATIVELY CONSTRAINED / GLOBAL REGULARITY NOT PROVED.**

This note is deliberately adversarial. It asks whether the current DSD-guided proof tree may have removed a genuine Navier--Stokes escape by assuming a vorticity-tight corridor before proving that every non-tight corridor is already H/T/turnover.

The answer is: **yes, there is a distinct logical gap unless normalized enstrophy escape is routed explicitly.** The gap is narrower than a generic new branch because first-hitting dynamics impose a quantitative persistence and energy-dissipation budget.

---

## 1. Fixed first-hitting scaling

Let `t_j` be a first-hitting time for

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\]

and use the fixed-center inertial scaling

\[
U_j(y,\tau)
=r_ju(X_*+r_jy,t_j+r_j^2\tau),
\]

\[
\Omega_j=\nabla\times U_j,
\qquad
\Sigma_j=\operatorname{sym}\nabla U_j.
\]

For every earlier time in the first-hitting history,

\[
\boxed{\|\Omega_j(\tau)\|_\infty\le1.}
\]

Define normalized enstrophy and palinstrophy

\[
Z_j(\tau)=\|\Omega_j(\tau)\|_2^2,
\qquad
Q_j(\tau)=\|\nabla\Omega_j(\tau)\|_2^2.
\]

---

## 2. Exact fixed-scale enstrophy identity

The fixed inertial rescaling satisfies ordinary Navier--Stokes, so

\[
\frac12 Z_j'(\tau)+\nu Q_j(\tau)
=
\int \Omega_j^T\Sigma_j\Omega_j\,dy.
\]

For divergence-free whole-space fields,

\[
\|\Sigma_j\|_2^2=\frac12Z_j.
\]

Using the first-hitting cap,

\[
\|\Omega_j\|_4^4
\le
\|\Omega_j\|_\infty^2\|\Omega_j\|_2^2
\le Z_j.
\]

Hence

\[
\left|\int \Omega_j^T\Sigma_j\Omega_j\right|
\le
\|\Sigma_j\|_2\|\Omega_j\|_4^2
\le
\frac1{\sqrt2}Z_j.
\]

Therefore

\[
\boxed{Z_j'(\tau)\le\sqrt2\,Z_j(\tau).}
\]

This estimate is unconditional on the first-hitting window: it does **not** require vorticity tightness, a global strain L-infinity bound, or a projective hypothesis.

---

## 3. Endpoint enstrophy cannot be an instantaneous flash

For `-delta <= tau <= 0`, Gronwall gives

\[
\boxed{
Z_j(\tau)
\ge
 e^{-\sqrt2\delta}Z_j(0).
}
\]

Thus if endpoint normalized enstrophy is large, a fixed fraction of it was already present for a fixed amount of endpoint-normalized backward time.

The stage-length corridor gives a scale-independent positive endpoint-normalized subinterval. To avoid index-convention dependence, choose any fixed

\[
0<\delta_0<c(q)L_-
\]

contained in every sufficiently late stage; for example one may take a conservative constant proportional to `L_-/q`.

Then

\[
\boxed{
\int_{-\delta_0}^0Z_j(\tau)d\tau
\ge
c_Z Z_j(0),
\qquad
c_Z=\frac{1-e^{-\sqrt2\delta_0}}{\sqrt2}>0.
}
\]

---

## 4. Physical energy dissipation gives a weighted summability law

The scaling relations are

\[
\|\omega(t)\|_2^2
=W_j^{1/2}Z_j(\tau),
\qquad
dt=W_j^{-1}d\tau.
\]

Therefore the physical viscous energy dissipation on the terminal subinterval obeys

\[
\nu\int\|\omega(t)\|_2^2dt
=
\nu W_j^{-1/2}
\int Z_j(\tau)d\tau
\ge
\nu c_ZW_j^{-1/2}Z_j(0).
\]

Choose these terminal subintervals inside disjoint first-hitting stages. The global kinetic-energy identity then implies

\[
\boxed{
\sum_j W_j^{-1/2}Z_j(0)<\infty.
}
\]

Consequently

\[
\boxed{Z_j(0)=o(W_j^{1/2}).}
\]

This is a genuine new restriction on any non-tight enstrophy branch.

---

## 5. Why this does not yet give uniform normalized enstrophy

The weighted summability law still allows, for example,

\[
Z_j\to\infty
\]

very slowly while

\[
W_j^{-1/2}Z_j
\]

is summable.

Hence it is **not legitimate** to replace the weighted law by

\[
\sup_j Z_j<\infty
\]

without an additional argument.

This is exactly where the current vorticity-tight ancient-compactness route has narrower scope than the entire first-hitting proof tree.

---

## 6. Enstrophy blow-up forces spatial non-tightness

Let `R_{1/2,j}` be a half-enstrophy radius:

\[
\int_{B_{R_{1/2,j}}}|\Omega_j|^2dy
\ge\frac12Z_j(0).
\]

Since `|Omega_j|<=1`,

\[
\frac12Z_j(0)
\le
|B_{R_{1/2,j}}|
=
\frac{4\pi}{3}R_{1/2,j}^3.
\]

Therefore

\[
\boxed{
R_{1/2,j}
\ge
\left(\frac{3Z_j(0)}{8\pi}\right)^{1/3}.
}
\]

Thus

\[
\boxed{
Z_j(0)\to\infty
\Longrightarrow
R_{1/2,j}\to\infty.
}
\]

So the missing branch is not a new local singular core. It is necessarily a **large-normalized-radius vorticity/enstrophy escape**.

---

## 7. Correct anti-proof split

The proof tree must therefore distinguish

\[
\boxed{
\text{first-hitting blow-up sequence}
\Longrightarrow
\begin{cases}
\sup_j Z_j<\infty,\\
Z_j\to\infty\text{ along a subsequence}.
\end{cases}
}
\]

### Branch A: bounded normalized enstrophy

This branch can use

`ANCIENT_LOCAL_COMPACTNESS_FROM_ENSTROPHY_TIGHTNESS_2026-08-24.md`

once the required local derivative compactness and center nesting are available. The subsequent problem is ancient/recurrent rigidity plus the critical tail.

### Branch B: normalized enstrophy escape

This branch satisfies

\[
\boxed{
R_{1/2,j}\to\infty,
\qquad
\sum_jW_j^{-1/2}Z_j<\infty.
}
\]

It must be routed separately to one or more of

\[
\boxed{
H_{remote}
\lor
T
\lor
\text{critical multiscale tail/genealogy}.
}
\]

At present that routing is not complete.

---

## 8. Relation to existing shell machinery

The existing localized solenoidal shell construction gives, for a compact shell packet `f_R`,

\[
\|P_{\le a/R}f_R\|_2
\lesssim a^{5/2}\|f_R\|_2.
\]

Hence a non-high-derivative remote packet cannot hide most of its kinetic mass at frequencies much lower than its shell radius. It must either

1. pay a high derivative-frequency cost, or
2. carry natural-frequency packet mass.

The historical-shell Duhamel machinery then routes persistent/forgotten natural-frequency packets toward H/T.

However, the present enstrophy-escape branch may consist of **low-amplitude diffuse vorticity** rather than the previously assumed fixed cubic-occupancy historical packet. Therefore a new amplitude-sensitive shell genealogy lemma is still required before one may identify Branch B completely with the old historical recycling branch.

This is the precise anti-proof correction.

---

## 9. Next theorem target

A sufficient bridge would be an amplitude-sensitive statement of the form

\[
\boxed{
\begin{aligned}
&Z_j\to\infty,
\quad \|\Omega_j\|_\infty\le1,
\quad \text{no local derivative blow-up}
\\
&\Longrightarrow
\text{remote natural-frequency packet population}
\\
&\Longrightarrow
H_{remote}\lor T\lor\text{historical/rebuild action}.
\end{aligned}
}
\]

Equivalently, prove that diffuse enstrophy cannot occupy more and more normalized volume without either developing remote frequency, requiring repeated packet creation/replacement, or reproducing a critical historical tail already covered by the existing shell ledgers.

---

## 10. Corrected frontier

Until the preceding bridge is proved, the honest final frontier is **not** a single recurrent ancient survivor. It is

\[
\boxed{
\begin{aligned}
\text{hypothetical blow-up}
\Longrightarrow{}&
\text{bounded-}Z\text{ recurrent ancient/tail branch}
\\
&\lor
\text{unbounded-}Z\text{ remote enstrophy-escape branch}
\\
&\lor
\text{already typed H/T/residual exits}.
\end{aligned}
}
\]

The new branch is strongly constrained by

\[
\sum_jW_j^{-1/2}Z_j<\infty,
\]

but it is not yet eliminated.

Status: **ANTI-PROOF AUDIT FOUND A REAL SCOPE GAP: VORTICITY-TIGHTNESS / UNIFORM NORMALIZED ENSTROPHY IS NOT YET AN EXHAUSTIVE CONSEQUENCE OF NO-H/T. FIRST-HITTING ENSTROPHY GROWTH AND GLOBAL ENERGY DISSIPATION FORCE THE NEW ESCAPE TO BE PERSISTENT FOR O(1) NORMALIZED TIME, SPATIALLY NON-TIGHT, AND WEIGHTED-SUMMABLE. THE NEXT TARGET IS AN AMPLITUDE-SENSITIVE SHELL GENEALOGY ROUTING THIS ESCAPE TO H/T/CRITICAL TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**