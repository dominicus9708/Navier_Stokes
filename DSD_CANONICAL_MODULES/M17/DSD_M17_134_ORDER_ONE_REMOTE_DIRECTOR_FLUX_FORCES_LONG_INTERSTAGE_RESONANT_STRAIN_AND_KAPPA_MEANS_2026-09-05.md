# DSD M17-134 — Order-one remote director flux forces long inter-stage resonant strain and kappa means

Date: 2026-09-05
Canonical ID: **M17-134**

Status: **EXACT CONDITIONAL MATERIAL-EXPONENT RIGIDITY / M17-133 REPLACES THE FIXED-FRACTION NONDEGENERATE `Phi_k~K_k^-1` MODEL BY A LOW-AMPLITUDE, ORDER-ONE DIRECTOR-FLUX SKELETON. TRACKING ONE PURE-KERNEL CARRIER OVER `Delta theta=2 log K_k`, THE EXACT LAW `D_B log|J_xi|=sigma_k-1` SHOWS THAT ORDER-ONE DIRECTOR AREA AT BOTH ENDS FORCES `mean sigma_k -> 1`. IF THE TWO INDEPENDENT PURE-KERNEL DIRECTOR JETS ALSO HAVE COMPARABLE ENDPOINT MAGNITUDES, THEIR EXACT MATERIAL LAWS FORCE `mean sigma -> -1/2` AND `mean sigma_n -> -1/2`. IF THE SIMILARITY VORTICITY AMPLITUDE RATIO IS ALSO BOUNDED, `D_B log rho=sigma+kappa-1` THEN FORCES `mean kappa -> 3/2`. THUS THE SURVIVING NONDEGENERATE REMOTE SKELETON MUST APPROACH THE FULL RESONANT MEAN FRAME `(-1/2,1,-1/2;kappa=3/2)` OVER ARBITRARILY LONG INTER-STAGE INTERVALS. THIS IS A STRONG RIGIDITY REQUIREMENT BUT NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Long inter-stage interval

For first-hitting generations separated by age `k`,

\[
\boxed{
\Delta\theta_k
:=\theta_j-\theta_{j-k}
=2\log K_k.
}
\]

Hence

\[
\Delta\theta_k\to\infty
\]

as the remote age tends to infinity.

---

## 2. Director-area exponent

On the regular pure-kernel branch,

\[
\boxed{
D_B\log|J_\xi|=\sigma_k-1.
}
\]

Integrating,

\[
\log\frac{|J_\xi|_j}{|J_\xi|_{j-k}}
=
\int_{\theta_{j-k}}^{\theta_j}(\sigma_k-1)d\theta.
\]

Assume endpoint compactness/nondegeneracy

\[
0<c_J
\le
|J_\xi|_{j-k},|J_\xi|_j
\le C_J.
\]

Then

\[
\left|
\log\frac{|J_\xi|_j}{|J_\xi|_{j-k}}
\right|
\le
\log(C_J/c_J)
=:C_J^*.
\]

Therefore

\[
\boxed{
\left|
\langle\sigma_k\rangle_{j-k:j}-1
\right|
\le
\frac{C_J^*}{2\log K_k}.
}
\]

In particular,

\[
\boxed{
\langle\sigma_k\rangle\to1.
}
\]

---

## 3. Two pure-kernel director jets

Use the M17-033 frame and define

\[
b=(\xi\cdot\nabla)\xi,
\qquad
a=(n\cdot\nabla)\xi,
\]

with magnitudes

\[
B:=|b|,
\qquad
A:=|a|.
\]

Their exact material laws are

\[
\boxed{
D_B\log B
=-\sigma-\frac12,
}
\]

and

\[
\boxed{
D_B\log A
=-\sigma_n-\frac12.
}
\]

Assume both endpoint ratios remain bounded above and below independently of `k`:

\[
0<c_A\le A_{j-k},A_j\le C_A,
\]

\[
0<c_B\le B_{j-k},B_j\le C_B.
\]

Then

\[
\boxed{
\langle\sigma\rangle
=-\frac12+O((\log K_k)^{-1}),
}
\]

and

\[
\boxed{
\langle\sigma_n\rangle
=-\frac12+O((\log K_k)^{-1}).
}
\]

These agree with trace-free strain and the Section 2 result.

---

## 4. Vorticity-amplitude exponent

CE-H gives

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1.
}
\]

If the endpoint similarity-amplitude ratio is bounded,

\[
\left|
\log\frac{\rho_j}{\rho_{j-k}}
\right|
\le C_\rho^*,
\]

then

\[
\langle\sigma+\kappa-1\rangle
=O((\log K_k)^{-1}).
\]

Using

\[
\langle\sigma\rangle
=-\frac12+O((\log K_k)^{-1}),
\]

we obtain

\[
\boxed{
\langle\kappa\rangle
=rac32+O((\log K_k)^{-1}).
}
\]

---

## 5. Full resonant mean frame

Under the endpoint compactness assumptions of Sections 2–4,

\[
\boxed{
\begin{aligned}
\langle\sigma\rangle
&=-\frac12+O((\log K_k)^{-1}),\\
\langle\sigma_k\rangle
&=1+O((\log K_k)^{-1}),\\
\langle\sigma_n\rangle
&=-\frac12+O((\log K_k)^{-1}),\\
\langle\kappa\rangle
&=\frac32+O((\log K_k)^{-1}).
\end{aligned}
}
\]

Hence the long-age limit requires

\[
\boxed{
(-1/2,1,-1/2;\,3/2)
}
\]

for `(sigma,sigma_k,sigma_n;kappa)` in time mean along the material genealogy.

---

## 6. Relation to earlier local recurrence

The strain triple

\[
(-1/2,1,-1/2)
\]

already appeared in M17-033/M17-041 as the resonant mean frame supporting recurrent pure-kernel director jets.

M17-134 shows that the same frame is not merely a local recurrence curiosity: it is forced asymptotically on any long inter-stage material genealogy that preserves nondegenerate director area and both independent director jets.

The additional amplitude-retention condition forces the matching mean

\[
\boxed{\langle\kappa\rangle\to3/2.}
\]

---

## 7. Why this is not yet a contradiction

The global CE-H elliptic identity is signed/weighted:

\[
\int\kappa\rho^2dy
=-\int|\nabla W|^2dy\le0.
\]

A positive material mean

\[
\langle\kappa\rangle\approx3/2
\]

along a low-amplitude skeleton does not force a positive global `rho^2`-weighted mean, because

\[
\rho\to0
\]

on the remote skeleton and negative-kappa regions elsewhere may carry larger amplitude weight.

Thus one must not substitute the material time mean for the global spatial weighted identity.

---

## 8. Exact exits from the resonant conclusion

If the long resonant frame does not occur, at least one endpoint compactness condition must fail:

\[
\boxed{
\begin{aligned}
&|J_\xi|\to0
&&\text{Rank-1/rank-deficient accumulation},\\
&A\to0\text{ or }\infty
&&\text{director-jet degeneration/unboundedness},\\
&B\to0\text{ or }\infty
&&\text{director-jet degeneration/unboundedness},\\
&\rho_j/\rho_{j-k}\to0\text{ or }\infty
&&\text{large CE-H amplitude exposure}.
\end{aligned}
}
\]

Each is already a typed branch rather than an unclassified failure.

---

## 9. DSD audit

### Audit A — endpoint compactness implies pointwise strain resonance

Rejected. The conclusion is a long-time material mean only.

### Audit B — material mean kappa equals spatial weighted mean kappa

Rejected. These use different measures and different averaging variables.

### Audit C — low amplitude makes the material mean irrelevant

Rejected as a geometric statement: the material director laws remain exact at every positive amplitude. But low amplitude does make the global energetic cost small.

### Audit D — resonance proves impossibility

Rejected. The resonant frame is algebraically compatible with the known pure-kernel material laws.

### Audit E — proof status

The survivor is substantially more rigid but remains open.

---

## 10. Updated realization target

The fixed-fraction nondegenerate low-amplitude ribbon skeleton must now satisfy simultaneously

\[
\boxed{
\rho\to0,
\qquad
\Phi\gtrsim1,
\qquad
|J_\xi|\gtrsim1,
}
\]

and, under inter-stage endpoint compactness,

\[
\boxed{
\langle\sigma,\sigma_k,\sigma_n,\kappa\rangle
\to
(-1/2,1,-1/2,3/2).
}
\]

The next high-value gate is to test whether this long resonant material mean can coexist with the spatial tail decay / pressure architecture of a finite-energy ancient solution, without replacing material-time averages by spatial averages.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
