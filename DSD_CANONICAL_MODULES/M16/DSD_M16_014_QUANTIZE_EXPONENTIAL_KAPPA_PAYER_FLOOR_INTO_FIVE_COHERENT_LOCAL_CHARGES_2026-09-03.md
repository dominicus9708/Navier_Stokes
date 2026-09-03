# DSD M16-014 — Quantize the exponential-kappa payer floor into five coherent local charges

Date: 2026-09-03
Canonical ID: **M16-014**

Status: **INTERNAL PAYER CONSOLIDATION / COMBINING M16-012 WITH THE EXACT REMAINDER COLLAPSE OF M16-013 REMOVES THE OPAQUE `R_geom` BRANCH: A NONZERO COMPACT CE-H SURVIVOR MUST CARRY A UNIFORM POSITIVE LOWER BOUND IN AT LEAST ONE OF FIVE FINITE-CORE LOCAL CHARGES — STRAIN-EIGENVALUE GRADIENT, STRAIN RESIDENCE, AMPLITUDE-TRANSITION ACTIVITY, STRAIN/VORTICITY-DERIVATIVE-GRAM OVERLAP, OR MAGNITUDE-GRADIENT ACTIVITY / EACH CHARGE LIVES WHERE `rho` IS BOUNDED AWAY FROM ZERO AND THE GLOBAL SMOOTH HULL GIVES UNIFORM DERIVATIVE CAPS, SO A POSITIVE INVARIANT FLOOR THICKENS TO A FIXED-RADIUS COHERENT EVENT; THUS THE LAST PDE CONSTITUTIVE PROBLEM IS RECONNECTED TO FINITE MATERIAL/VORTICITY GENEALOGY RATHER THAN AN ABSTRACT KAPPA-SPACE CURRENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M16-012

M16-012 (Legacy M5-688) gives a fixed number

\[
\boxed{d_*>0}
\]

coming from the uniform nonzero `kappa`-gradient diffusion charge of M16-011.

Its exponential-kappa ledger implies the following coarse dichotomy:

\[
\boxed{
D_\sigma\ge \frac14d_*
\quad\lor\quad
\max\{|\mathcal S|,|\mathcal C|,|\mathcal R|\}
\ge \frac25d_*.
}
\]

Here

\[
D_\sigma
:=
\int e^{2\kappa}\chi\rho^2|\nabla\sigma|^2dy
\]

is the aligned-strain gradient charge, `S` is the exponential-weighted strain-residence term, `C` is supported in the amplitude cutoff/threshold transition, and `R` was the explicit CE-H geometric remainder.

---

## 2. Replace the geometric remainder using M16-013

M16-013 gives

\[
\boxed{
\mathcal R
=2\mathfrak T_{\Sigma W}
+4\mathfrak X_{\kappa\rho}
+\mathfrak C_{\rm geom}^{\chi},
}
\]

where

\[
\mathfrak T_{\Sigma W}
=
\int e^{2\kappa}\chi\,\Sigma:\mathsf G_Wdy,
\]

\[
\mathsf G_W{}_{ij}
=\partial_iW\cdot\partial_jW,
\]

and

\[
\mathfrak X_{\kappa\rho}
=
\int e^{2\kappa}\chi\rho\,
\Sigma\nabla\kappa\cdot\nabla\rho\,dy.
\]

The term `C_geom^chi` is supported only where `chi' != 0`; merge it with the existing amplitude-transition family and define

\[
\boxed{
\mathcal C_{\rm tot}
:=
\mathcal C+\mathfrak C_{\rm geom}^{\chi}.
}
\]

---

## 3. Uniform upper caps

On the compact CE-H hull and the fixed high-amplitude core there are finite constants

\[
\|\Sigma\|_\infty\le S_*,
\qquad
D_\kappa\le D_\kappa^*,
\]

with

\[
D_\kappa
=
\int e^{2\kappa}\chi\rho^2|\nabla\kappa|^2dy.
\]

M16-011 also gives

\[
D_\kappa\ge d_\kappa>0.
\]

Put

\[
M_\rho
:=
\int e^{2\kappa}\chi|\nabla\rho|^2dy.
\]

M16-013 gives

\[
|\mathfrak X_{\kappa\rho}|
\le
S_*\sqrt{D_\kappa^*}\sqrt{M_\rho}.
\]

Therefore any fixed lower bound

\[
|\mathfrak X_{\kappa\rho}|\ge x_*>0
\]

forces

\[
\boxed{
M_\rho
\ge
\frac{x_*^2}{S_*^2D_\kappa^*}
=:m_*>0.
}
\]

Thus the cross term is not a new branch: it is a quantitative magnitude-gradient payer.

---

## 4. Five canonical payer charges

By the triangle inequality in the decomposition of `R`, the M16-012 floor yields constants depending only on the compact-hull caps and `d_*` such that at least one of the following has a fixed positive lower bound:

### P1 — aligned-strain gradient

\[
\boxed{
D_\sigma
=
\int e^{2\kappa}\chi\rho^2|\nabla\sigma|^2dy
\ge c_1>0.
}
\]

### P2 — aligned-strain residence

\[
\boxed{
|\mathcal S|
\ge c_2>0.
}
\]

### P3 — amplitude-transition activity

\[
\boxed{
|\mathcal C_{\rm tot}|
\ge c_3>0.
}
\]

### P4 — strain / derivative-Gram overlap

\[
\boxed{
|\mathfrak T_{\Sigma W}|
\ge c_4>0.
}
\]

### P5 — magnitude-gradient activity

\[
\boxed{
M_\rho
\ge c_5>0.
}
\]

The exact numerical constants are inessential; what matters is that all `c_j` are uniform and strictly positive on the retained nonzero CE-H component.

Hence

\[
\boxed{
E_{CEH}^{hard}
\Longrightarrow
P_1\lor P_2\lor P_3\lor P_4\lor P_5.
}
\]

---

## 5. P4 forces simultaneous strain and vorticity-derivative activity

Because `G_W` is positive semidefinite,

\[
|\Sigma:\mathsf G_W|
\le
|\Sigma|\,|\nabla W|^2.
\]

Therefore

\[
|\mathfrak T_{\Sigma W}|
\le
\int e^{2\kappa}\chi
|\Sigma|\,|\nabla W|^2dy.
\]

If P4 holds, then

\[
\boxed{
\int e^{2\kappa}\chi
|\Sigma|\,|\nabla W|^2dy
\ge c_4.
}
\]

The cutoff support lies in one fixed finite core, while `Sigma`, `grad W`, `kappa`, and all their derivatives have uniform upper caps.

Consequently there exist fixed constants

\[
s_4>0,
\qquad
g_4>0,
\qquad\ r_4>0
\]

and a positive-frequency family of balls `B_{r_4}` on which

\[
\boxed{
|\Sigma|\ge s_4,
\qquad
|\nabla W|\ge g_4.
}
\]

Since `chi != 0` there, vorticity amplitude is also bounded away from zero after restricting to the interior part of the cutoff or assigning the transition part to P3.

Thus P4 is a genuine coherent high-amplitude strain/derivative packet.

---

## 6. P1 and P5 also thicken to coherent events

For P1,

\[
D_\sigma\ge c_1
\]

inside a fixed core with uniform `C^2` bounds implies a positive-frequency fixed-radius event where

\[
\boxed{
\rho\ge a_1>0,
\qquad
|\nabla\sigma|\ge s_{\nabla,*}>0.
}
\]

For P5,

\[
M_\rho\ge c_5
\]

similarly yields a fixed-radius event with

\[
\boxed{
\rho\ge a_5>0,
\qquad
|\nabla\rho|\ge r_{\rho,*}>0.
}
\]

Thus both are eligible for the finite-core coherent-packet / material-genealogy machinery of M13--M15.

---

## 7. P2 sign firewall

A large absolute strain-residence term does not by itself say whether the active population is stretching or compressing.

Therefore P2 must be split as

\[
\boxed{
P_2^+:
\mathcal S\ge c_2
\qquad\lor\qquad
P_2^-:
\mathcal S\le-c_2.
}
\]

The positive branch is compatible with the mandatory production / positive-middle-strain mechanism of M15.

The negative branch is a genuine compressive payer and must be kept separately; it cannot be silently counted as positive production.

---

## 8. P3 firewall

P3 is supported in a fixed amplitude transition layer. It proves recurrent order-one threshold-layer activity, but by itself it does **not** determine the sign of material crossing.

To call it sheath turnover one must combine it with the signed moving-level current of M15/M14.

Thus the correct statement is

\[
\boxed{
P_3
\Rightarrow
\text{coherent amplitude-transition activity},
}
\]

with material turnover as the next signed audit.

---

## 9. Finite pigeonhole in invariant time

There are only five canonical payer types.

If every recurrent state satisfies at least one payer alternative with a uniform floor, then along an ergodic invariant component at least one payer type occurs with positive asymptotic time density.

After the usual uniform time thickening,

\[
\boxed{
\exists j\in\{1,2,3,4,5\}:
\quad
P_j\text{ is a positive-density coherent event family.}
}
\]

Hence the constitutive `kappa`-space problem has been returned to finite spacetime genealogy.

---

## 10. Updated frontier

The last survivor no longer has an abstract choice

\[
\text{`strain or geometry somehow pays kappa diffusion.'}
\]

It must realize recurrently one of five concrete local structures:

\[
\boxed{
\begin{array}{ll}
P_1:&\nabla\sigma\text{ packet},\\
P_2:&\sigma\text{-residence packet},\\
P_3:&\text{amplitude-transition packet},\\
P_4:&\Sigma\text{--}\nabla W\text{ overlap packet},\\
P_5:&\nabla\rho\text{ packet}.
\end{array}
}
\]

The next target is to determine which of these can persist on the same finite material source network without forcing one of the already audited M13--M15 turnover/replacement mechanisms.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
