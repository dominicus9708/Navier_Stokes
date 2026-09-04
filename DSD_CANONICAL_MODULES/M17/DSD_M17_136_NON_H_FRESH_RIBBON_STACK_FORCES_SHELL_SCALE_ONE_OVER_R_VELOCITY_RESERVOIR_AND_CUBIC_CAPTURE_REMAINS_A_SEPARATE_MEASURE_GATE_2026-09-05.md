# DSD M17-136 — Non-H fresh ribbon stack forces a shell-scale `1/R` velocity reservoir; cubic capture remains a separate measure gate

Date: 2026-09-05  
Canonical ID: **M17-136**

Status: **M17/M5 BRIDGE / A FIXED-FRACTION RIBBON CONTRIBUTION TO THE CRITICAL DIRICHLET-VORTICITY STACK CANNOT REMAIN AN ISOLATED UNIT-SCALE LOW-AMPLITUDE OBJECT ON THE NON-H LANE. THE M5 NATURAL-FREQUENCY GATE FORCES A SHELL-SCALE `L2` VELOCITY RESERVOIR OF RMS SIZE `~1/R` WHEN `J_k~1`. THIS RECOVERS THE CRITICAL `1/r` VELOCITY SCALE, BUT THE RIBBON ENSTROPHY MEASURE AND THE ACTUAL CUBIC-VELOCITY MEASURE MUST STILL NOT BE IDENTIFIED WITHOUT A LOCALIZATION/PUSHFORWARD BRIDGE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The one-way M5 implication

The ancient annular-tail reduction proves

\[
\boxed{
U\notin L^3(\{|y|>R_0\})
\Longrightarrow
\sum_k J_k^{3/2}=\infty,
}
\]

where, up to the bounded-overlap enlarged-annulus convention,

\[
J_k
:=R_k\int_{C_k}|\nabla U|^2dy.
\]

M17-121 allows the critical stack to be represented equivalently at the summability level by vorticity shell energy.

The logical direction is crucial:

\[
\boxed{
\sum_kJ_k^{3/2}=\infty
\not\Rightarrow
U\notin L^3.
}
\]

Therefore M17-135's scale-consistent sparse ribbon model is not, merely from `J_k~1`, an actual realization of the non-`L3` velocity tail.

This is a DSD measure-separation point:

\[
\boxed{
\text{weighted gradient/vorticity stack}
\neq
\text{cubic velocity mass}.
}
\]

---

## 2. Reintroduce the M5 natural-frequency gate

Let `f_k` be the compact solenoidal shell packet used in the M5 localized phase-space decomposition at scale `R_k`.
Define

\[
\boxed{
\Gamma_k
:=
\frac{R_k\|\nabla f_k\|_2}{\|f_k\|_2}.
}
\]

The derivative-frequency exit is

\[
\Gamma_k>\Gamma_*.
\]

On the non-H lane,

\[
\boxed{\Gamma_k\le\Gamma_*.}
\]

Suppose a ribbon population carries a fixed fraction `theta>0` of the retained shell derivative/vorticity cost, so that the localized packet obeys

\[
\boxed{
\|\nabla f_k\|_2^2
\ge
c_\theta\frac{J_k}{R_k}.
}
\]

Then the non-H inequality gives

\[
\|f_k\|_2
\ge
\Gamma_*^{-1}R_k\|\nabla f_k\|_2,
\]

and hence

\[
\boxed{
\|f_k\|_2^2
\ge
c_\theta\Gamma_*^{-2}J_kR_k.
}
\]

This is an exact scale consequence of the non-H branch once the ribbon contribution is captured by the retained shell packet.

---

## 3. Critical `J_k~1` forces a shell-scale velocity reservoir

For the M17-135 cheap critical ribbon stack,

\[
J_k\asymp1.
\]

Then

\[
\boxed{
\|f_k\|_2^2\gtrsim R_k.
}
\]

The shell-localized packet has support volume of order

\[
|\operatorname{supp}f_k|\lesssim R_k^3.
\]

Therefore its RMS velocity scale satisfies

\[
\left(
\frac{\|f_k\|_2^2}{|\operatorname{supp}f_k|}
\right)^{1/2}
\gtrsim
R_k^{-1}.
\]

Thus

\[
\boxed{
|U|_{\rm rms,shell}
\gtrsim
R_k^{-1}
}
\]

at the shell-packet level.

This is exactly the classical scale-critical tail size.

Hence a unit-scale ribbon with

\[
\rho_k^2\asymp R_k^{-1}
\]

cannot be the entire non-H picture by itself.
It must either

1. trigger the derivative-frequency branch `H`, or
2. coexist with a shell-scale low-frequency velocity reservoir of critical `1/R` amplitude.

Symbolically,

\[
\boxed{
F_{\rm fresh}^{lowamp,strongdir}
\Longrightarrow
H_{\rm derivative-frequency}
\ \lor\
B_{1/R}^{low-frequency\ bath}.
}
\]

---

## 4. Packet cubic lower bound on the non-H lane

Finite support and Hölder give

\[
\|f_k\|_2
\le
|\operatorname{supp}f_k|^{1/6}\|f_k\|_3.
\]

Therefore

\[
\|f_k\|_3^3
\ge
|\operatorname{supp}f_k|^{-1/2}\|f_k\|_2^3.
\]

Using

\[
|\operatorname{supp}f_k|\lesssim R_k^3
\]

and the preceding non-H lower bound,

\[
\boxed{
\|f_k\|_3^3
\gtrsim
J_k^{3/2}.
}
\]

Thus, at the level of the localized solenoidal shell packet, the non-H branch converts the critical derivative cost back into critical cubic mass.

For `J_k\asymp1`,

\[
\boxed{\|f_k\|_3^3\gtrsim1.}
\]

An infinite stack therefore has an order-one cubic packet contribution per selected shell.

---

## 5. Why this is not yet an unconditional lower bound for the original `U`

The shell packet `f_k` is obtained by solenoidal localization.
It agrees with `U` on the retained core but contains cutoff/correction pieces near the localization collar.

To promote

\[
\|f_k\|_3^3\gtrsim J_k^{3/2}
\]

to

\[
\int_{C_k}|U|^3dy
\gtrsim J_k^{3/2},
\]

one needs a scale-uniform `L3` stability estimate for the exact localizer used in M5, or an explicit decomposition showing that any failure of that stability is already one of the localization/residual exits.

The required bridge has the schematic form

\[
\boxed{
\|f_k\|_3
\le
C_{loc}\|U\|_{L^3(C_k^*)}
+
\mathcal R_{loc,k},
}
\]

with bounded overlap of the enlarged annuli and a typed residual `R_loc,k`.

Until that exact localizer estimate is imported or reproved, the cubic lower bound is rigorously a statement about `f_k`, not automatically about `U`.

---

## 6. DSD interpretation: two different carriers

The fresh critical ribbon and the critical velocity bath may occupy very different geometric measures.

A representative compatible scaling is

\[
\boxed{
\begin{aligned}
\text{ribbon: }&|W|\sim R^{-1/2}
\text{ on }O(1)\text{ similarity volume},\\
\text{bath: }&|U|\sim R^{-1}
\text{ over }O(R^3)\text{ shell volume}.
\end{aligned}
}
\]

The ribbon then contributes order

\[
\int|W|^2\sim R^{-1},
\qquad
J\sim R\cdot R^{-1}\sim1,
\]

while the low-frequency bath contributes order-one cubic velocity mass

\[
R^3(R^{-1})^3\sim1.
\]

Therefore one must not say that the ribbon itself carries the cubic velocity tail.
The correct statement is that, on the non-H lane, a ribbon carrying critical derivative cost forces coexistence with a shell-scale velocity reservoir.

---

## 7. The hybrid hard survivor

The genuinely unresolved non-H Rank-2 model is now

\[
\boxed{
\text{fresh low-amplitude / strong-director ribbon skeleton}
\quad+
\text{shell-scale }1/R\text{ velocity bath}.
}
\]

The ribbon carries a fixed fraction of the critical vorticity/Dirichlet cost.
The bath supplies the low-frequency `L2/L3` size needed to keep the derivative-frequency ratio bounded.

This is more restrictive than M17-135's isolated sparse-ribbon firewall.

---

## 8. DSD audit

### Audit A — divergent `J` implies non-`L3`

Rejected. The M5 implication is one-way.

### Audit B — fixed-fraction ribbon enstrophy means the ribbon neighborhood carries fixed-fraction cubic velocity mass

Rejected. Velocity is nonlocal and the measures differ.

### Audit C — isolated unit-scale ribbon can remain non-H at radius `R>>1`

Rejected unless a large low-frequency shell velocity reservoir is also present.
The non-H ratio forces `||f_k||_2^2 \gtrsim J_k R_k`.

### Audit D — packet cubic lower bound is automatically the original velocity cubic lower bound

Not yet promoted. The exact M5 solenoidal-localizer `L3` bound/correction ledger must be imported or rederived.

### Audit E — the `1/R` bath is itself a contradiction

Rejected. It is exactly the sharp scale-critical survivor already identified in the ancient tail analysis.

---

## 9. Updated frontier

The fixed-fraction remote Rank-2 ribbon branch now satisfies

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
H
\ \lor\
T_{\rm ribbon\ geometry/carrier}
\ \lor\
\bigl(
F_{\rm fresh}^{lowamp,strongdir}
+
B_{1/R}^{low-frequency}
\bigr).
}
\]

The highest-value next calculation is to close the remaining localization gap and then test the **full CE-H coupling between the sparse high-vorticity director skeleton and the shell-scale low-frequency velocity bath**.

In particular, the next questions are:

\[
\boxed{
\text{Does the exact M5 shell localizer satisfy a scale-uniform }L^3\text{ bound?}
}
\]

and, after that,

\[
\boxed{
\text{Can a }1/R\text{ velocity bath generate the strain/pressure field required to continually create fresh order-one-}J_\xi\text{ ribbons?}
}
\]

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
