# DSD M5-401 — Unbounded normalized enstrophy forces a remote active satellite

Date: 2026-08-31

Status: **NORMALIZED ENSTROPHY ESCALATION IS NOT AN INDEPENDENT DIFFUSE MASS TERMINAL / UNDER THE FIRST-HITTING AMPLITUDE CAP, IF THE REMOTE ACTIVE-SATELLITE PARAMETER `Lambda_R = R^2 sup_{A_R}|Omega|` WERE UNIFORMLY BOUNDED ON DYADIC ANNULI, EACH ANNULAR ENSTROPHY WOULD BE `O(R^{-1})` AND THE DYADIC TAIL WOULD BE SUMMABLE / THEREFORE `||Omega||_2^2 -> infinity` FORCES `sup_R Lambda_R -> infinity`, WITH THE RESPONSIBLE RADII TENDING TO INFINITY / THE CORRESPONDING ACTIVE NATURAL SCALE IS MUCH SMALLER THAN ITS DISTANCE TO THE TRACKED CORE, EXACTLY THE M5-280 REMOTE-SATELLITE GEOMETRY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-400 proves on the original analytic first-hitting normalization that

\[
\|\Sigma_j\|_\infty\to\infty
\Longrightarrow
Z_j:=\|\Omega_j\|_2^2\to\infty.
\]

The immediate question is whether

\[
Z_j\to\infty
\]

can remain a genuinely diffuse normalized-enstrophy cloud without producing a remote active satellite.

The first-hitting amplitude cap and the critical `R^{-2}` vorticity scaling answer this directly.

---

## 2. Dyadic annuli and the satellite parameter

At one normalized stage/time write simply

\[
\Omega=\Omega_j.
\]

For dyadic radii

\[
R_k:=2^k,
\qquad k=0,1,2,\dots,
\]

define fixed-shape annuli

\[
A_k
:=
\{R_k\le |Y|<2R_k\}.
\]

Let

\[
m_k:=\|\Omega\|_{L^\infty(A_k)}
\]

and define the M5-280 remote-active parameter

\[
\boxed{
\Lambda_k:=R_k^2m_k.
}
\]

A passive critical vorticity tail has

\[
m_k\sim R_k^{-2}
\]

and therefore `Lambda_k=O(1)`.

---

## 3. Bounded satellite parameter implies summable enstrophy tail

Assume

\[
\boxed{
\sup_{k\ge0}\Lambda_k\le L<\infty.
}
\]

Then

\[
m_k\le LR_k^{-2}.
\]

The volume of `A_k` is comparable to `R_k^3`, so

\[
\begin{aligned}
\int_{A_k}|\Omega|^2dY
&\le
|A_k|m_k^2\\
&\lesssim
R_k^3L^2R_k^{-4}\\
&=
L^2R_k^{-1}.
\end{aligned}
\]

Thus

\[
\boxed{
\int_{A_k}|\Omega|^2dY
\lesssim
L^22^{-k}.
}
\]

Summing over all dyadic annuli,

\[
\boxed{
\int_{|Y|\ge1}|\Omega|^2dY
\lesssim
L^2\sum_{k=0}^\infty2^{-k}
\lesssim
L^2.
}
\]

---

## 4. The inner normalized ball is automatically bounded

On a first-hitting stage the global amplitude cap gives

\[
\|\Omega\|_\infty\le q
\]

up to the fixed endpoint convention.

Therefore

\[
\boxed{
\int_{B_1}|\Omega|^2dY
\le
|B_1|q^2.
}
\]

Combining with the dyadic tail estimate,

\[
\boxed{
Z=\|\Omega\|_2^2
\le
C(q^2+L^2).
}
\]

Thus a uniform bound on the remote-satellite parameter gives a uniform bound on normalized enstrophy.

---

## 5. Contrapositive: enstrophy escalation forces satellite escalation

The previous estimate gives the exact contrapositive

\[
\boxed{
Z_j\to\infty
\Longrightarrow
\sup_{k\ge0}\Lambda_{j,k}\to\infty.
}
\]

Choose `k_j` so that

\[
\Lambda_{j,k_j}
\ge
\frac12\sup_k\Lambda_{j,k}.
\]

Because each fixed bounded normalized annulus has

\[
\Lambda_{j,k}
\le
qR_k^2<\infty
\]

uniformly in the stage index for fixed `k`, any sequence with

\[
\Lambda_{j,k_j}\to\infty
\]

must satisfy

\[
\boxed{k_j\to\infty,
\qquad
R_{k_j}\to\infty.}
\]

Hence the escalating enstrophy is necessarily accompanied by activity escaping to larger normalized radii.

---

## 6. Extract an active point and its natural scale

Choose

\[
Y_j\in A_{k_j}
\]

with

\[
|\Omega_j(Y_j)|
\ge
\frac12m_{j,k_j}.
\]

Define its normalized vorticity-natural scale by

\[
\ell_j
:=
|\Omega_j(Y_j)|^{-1/2}.
\]

Since

\[
|Y_j|\asymp R_{k_j},
\]

we obtain

\[
\frac{|Y_j|}{\ell_j}
=
|Y_j|\sqrt{|\Omega_j(Y_j)|}
\gtrsim
R_{k_j}\sqrt{m_{j,k_j}}
=
\sqrt{\Lambda_{j,k_j}}.
\]

Therefore

\[
\boxed{
\frac{|Y_j|}{\ell_j}\to\infty.
}
\]

This is precisely the remote active-satellite scale separation of M5-280--281.

---

## 7. No assumption of one fixed high-amplitude remote packet

The argument does not assume that one shell carries order-one parent-normalized vorticity.

For example, it permits

\[
m_j\to0
\]

provided

\[
R_j^2m_j\to\infty.
\]

Then the satellite's own natural radius

\[
\ell_j=m_j^{-1/2}
\]

may grow in parent units, but still satisfies

\[
\ell_j/R_j\to0.
\]

Thus the conclusion is genuinely a **relative-scale remote satellite**, exactly matching the M5-392 correction.

---

## 8. Relation to M5-400

M5-400 gives

\[
H_{nonlocal\,strain}^{pointwise,parent}
\Longrightarrow
Z_j\to\infty.
\]

M5-401 gives

\[
Z_j\to\infty
\Longrightarrow
S_{remote}.
\]

Therefore the combined route is

\[
\boxed{
H_{nonlocal\,strain}^{pointwise,parent}
\Longrightarrow
S_{remote}.
}
\]

The intermediate enstrophy-mass label is useful analytically but is not a final independent terminal.

---

## 9. Relation to M5-281

Once

\[
|Y_j|/\ell_j\to\infty,
\]

M5-281's backward point-picking can select a satellite-centered parabolic sequence with

\[
|\widetilde\omega_j(0,0)|=1,
\qquad
|\widetilde\omega_j|\le4
\]

on expanding backward cylinders, while the original core escapes to infinity in the satellite frame.

Thus

\[
\boxed{
Z_j\to\infty
\Longrightarrow
T_{dynamic}
\lor
H_{ambient}^{sat}
\lor
A_{detached}.
}
\]

The ambient-strain and detached-limit firewalls of M5-281 remain unchanged.

---

## 10. DSD audit

### Derived

- bounded `Lambda_R` gives an `R^{-1}` dyadic enstrophy-shell bound;
- the dyadic tail is summable;
- normalized enstrophy escalation therefore forces `Lambda_R` escalation at radii tending to infinity;
- this gives remote distance/natural-scale separation.

### Firewall

- `Z_j -> infinity` is not itself a contradiction;
- the conclusion is a relative-scale satellite, not necessarily a parent-subnatural packet;
- after recentering/rescaling, the satellite's global `L2` or weak-`L3` norm is not automatically inherited;
- M5-284's restart-coherence gap remains relevant.

---

## 11. Updated frontier

After M5-399--401, three formerly separate escapes collapse into the remote-satellite lane:

\[
\boxed{
T_{center}^{unbounded}
\lor
H_{nonlocal\,strain}^{pointwise,parent}
\lor
H_{enstrophy\,mass}^{parent}
\Longrightarrow
S_{remote}.
}
\]

Thus the current hard frontier is better written as

\[
\boxed{
H_{frequency/direction/critical\ action}^{local}
\lor
S_{remote}
\lor
T_{projective/export/compactness/realization}.
}
\]

The next target is whether the satellite's ambient-strain failure can itself be iterated into another remote active scale or whether it converges to a genuinely harmonic/affine source-free limit; that split must preserve the energy-bearing versus energy-vanishing firewall.

---

## 12. Audit verdict

### REMOVED AS INDEPENDENT TERMINAL

\[
\boxed{H_{enstrophy\,mass}^{parent}.}
\]

### REPLACEMENT

\[
\boxed{
H_{enstrophy\,mass}^{parent}
\Longrightarrow
S_{remote}.
}
\]

### STILL OPEN

- satellite ambient-strain recursion/harmonic-affine limit;
- detached ancient critical restart inheritance;
- local critical frequency/direction action;
- projective/export/compactness/realization escape;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
