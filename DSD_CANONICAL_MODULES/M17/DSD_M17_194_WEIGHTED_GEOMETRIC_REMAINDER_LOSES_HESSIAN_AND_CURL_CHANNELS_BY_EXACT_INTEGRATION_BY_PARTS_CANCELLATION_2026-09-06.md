# DSD M17-194 — Weighted CE-H geometric remainder loses its Hessian and curl channels by exact integration-by-parts cancellation

Date: 2026-09-06  
Canonical ID: **M17-194**

Status: **EXACT GEOMETRIC-REMAINDER COLLAPSE / UNDER THE M5-688 WEIGHT `chi(rho) exp(2 kappa) rho^2`, THE APPARENTLY SECOND-ORDER AMPLITUDE-HESSIAN TERM IN `R_geom` CAN BE INTEGRATED BY PARTS. INCOMPRESSIBILITY GIVES `div Sigma = -(1/2) curl W`, AND THE RESULTING CURL-W TERM CANCELS THE EXPLICIT `(curl W) dot grad log rho` TERM EXACTLY. THE WEIGHTED GEOMETRIC REMAINDER THEREFORE REDUCES TO FOUR FIRST-GRADIENT/THRESHOLD CHANNELS: STRAIN AGAINST `grad rho tensor grad rho`, A MIXED `grad kappa`--`grad rho` TERM, THE AMPLITUDE-CUTOFF COLLAR, AND STRAIN AGAINST THE DIRECTOR METRIC `partial_i xi dot partial_j xi`. NO NEW AMPLITUDE-HESSIAN OR CURL PAYMENT SURVIVES. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input remainder

M5-682 gives on the active set `rho=|W|>0`

\[
\boxed{
\mathcal R_{geom}
=-\frac2\rho\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+(\nabla\times W)\cdot\nabla\log\rho.
}
\]

Use the M5-688 spatial weight

\[
\boxed{
w:=\chi(\rho)e^{2\kappa}\rho^2,
}
\]

where `chi` is the fixed monotone high-amplitude cutoff.

Define

\[
\boxed{
\mathfrak R_{geom}^{(2)}
:=\int w\,\mathcal R_{geom}\,dy.
}
\]

All calculations below are at one fixed similarity time; recurrent averaging may be applied afterwards.

---

## 2. Integrate the amplitude-Hessian term by parts

The first contribution is

\[
I_H
=-2\int \chi e^{2\kappa}\rho\,\Sigma_{ij}\partial_{ij}\rho\,dy.
\]

Integrating in `x_i`,

\[
I_H
=2\int
\partial_i(\chi e^{2\kappa}\rho\Sigma_{ij})
\,\partial_j\rho\,dy.
\]

Expand the derivative:

\[
\boxed{
\begin{aligned}
I_H
={}&2\int\chi e^{2\kappa}\Sigma(\nabla\rho,\nabla\rho)\,dy\\
&+4\int\chi e^{2\kappa}\rho\,\Sigma(\nabla\kappa,\nabla\rho)\,dy\\
&+2\int\chi'(\rho)e^{2\kappa}\rho\,\Sigma(\nabla\rho,\nabla\rho)\,dy\\
&+2\int\chi e^{2\kappa}\rho\,(\nabla\cdot\Sigma)\cdot\nabla\rho\,dy.
\end{aligned}
}
\]

No boundary term is retained; this is the same whole-space/high-amplitude compact-support integration convention already used in M5-683/688.

---

## 3. Exact incompressible identity for `div Sigma`

For incompressible `U`,

\[
\Sigma_{ij}=\frac12(\partial_iU_j+\partial_jU_i),
\qquad
\nabla\cdot U=0.
\]

Therefore

\[
\partial_i\Sigma_{ij}
=\frac12\Delta U_j.
\]

Since

\[
W=\nabla\times U,
\qquad
\nabla\times W
=\nabla(\nabla\cdot U)-\Delta U
=-\Delta U,
\]

we obtain

\[
\boxed{
\nabla\cdot\Sigma
=-\frac12\nabla\times W.
}
\]

Hence the last term in `I_H` is

\[
2\int\chi e^{2\kappa}\rho(\nabla\cdot\Sigma)\cdot\nabla\rho
=-\int\chi e^{2\kappa}\rho(\nabla\times W)\cdot\nabla\rho.
\]

But

\[
\rho\nabla\rho=\rho^2\nabla\log\rho,
\]

so this equals

\[
-\int\chi e^{2\kappa}\rho^2
(\nabla\times W)\cdot\nabla\log\rho\,dy.
\]

This cancels the explicit curl term in `w R_geom` **exactly**.

---

## 4. Exact collapsed formula

After the cancellation, only four channels remain:

\[
\boxed{
\begin{aligned}
\mathfrak R_{geom}^{(2)}
={}&2\int\chi e^{2\kappa}
\Sigma(\nabla\rho,\nabla\rho)\,dy\\
&+4\int\chi e^{2\kappa}\rho\,
\Sigma(\nabla\kappa,\nabla\rho)\,dy\\
&+2\int\chi'e^{2\kappa}\rho\,
\Sigma(\nabla\rho,\nabla\rho)\,dy\\
&+2\int\chi e^{2\kappa}\rho^2
\Sigma_{ij}(\partial_i\xi\cdot\partial_j\xi)\,dy.
\end{aligned}
}
\]

Thus the original three-term pointwise remainder

\[
\text{amplitude Hessian}
+\text{director metric}
+\text{curl-amplitude transport}
\]

becomes, after the exact M5-688 weighting,

\[
\boxed{
\text{amplitude-gradient/strain}
+\text{kappa-amplitude mixed gradient}
+\text{threshold collar}
+\text{director-gradient/strain}.
}
\]

---

## 5. Consequence for the M5-688 payer tree

The geometric remainder is therefore **not an independent higher-derivative payer** at the integrated cycle-work level.

It introduces no new `nabla^2 rho` charge and no independent `curl W` charge.

The surviving quantities are all already adjacent to known positive/fixed-order ledgers:

1. `|grad rho|^2` — amplitude-gradient / palinstrophy sector;
2. `rho |grad kappa| |grad rho|` — mixed multiplier-amplitude sector;
3. `chi' rho |grad rho|^2` — amplitude-threshold collar;
4. `rho^2 |grad xi|^2` — director-gradient / palinstrophy sector.

The next module should quantify this by Cauchy--Schwarz/compact-hull bounds and identify whether `R_geom` can pay the M5-687 positive `D_kappa` charge without forcing one of these already exposed positive occupancies.

---

## 6. DSD audit

### Audit A — pointwise versus integrated identity
The cancellation is an **integrated weighted identity**. Pointwise `R_geom` still contains the Hessian and curl terms.

### Audit B — boundary terms
The integration convention is the same whole-space/high-amplitude localized convention used in M5-683/688. Any finite artificial spatial cutoff would carry an additional shell term and must be retained until the complementary partition is restored.

### Audit C — calling the surviving terms sign-definite
Rejected. Every surviving contraction with `Sigma` is signed. The result is a structural reduction, not yet a sign contradiction.

### Audit D — proof status
A formerly independent-looking geometric payer has been reduced to fixed-order gradient/threshold/director channels, but their recurrent recyclability is not yet excluded.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
