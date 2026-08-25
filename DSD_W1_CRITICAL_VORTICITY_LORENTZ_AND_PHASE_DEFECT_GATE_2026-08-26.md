# DSD W1 Critical-Vorticity Lorentz Endpoint and Phase-Defect Gate

Date: 2026-08-26

Status: **W1 => UNIFORM CRITICAL VORTICITY L^{3/2,∞} PROVED / STRONG L^q FOR ALL q>3/2 PROVED / 2026 LOG-BMO DIRECTION RESULT ADDED ONLY AS AN EXTERNAL CONDITIONAL GATE / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Work on the current pure `W1` corridor.  The imported shell hypotheses are:

- bounded relative Campanato on dyadic enlarged annuli,
  \[
  \mathfrak C_k
  :=R_k^{-1}\|f_k\|_2^2\le C_C,
  \]
  where `f_k` is the compact solenoidal Bogovskii localization of the normalized velocity;
- bounded shell derivative ratio
  \[
  \Gamma_k
  :=\frac{R_k\|\nabla f_k\|_2}{\|f_k\|_2}
  \le \Gamma_*;
  \]
- bounded overlap of the enlarged annuli;
- first-hitting smoothness/analyticity and bounded normalized enstrophy.

The shell radii are geometric,
\[
R_k=R_0\Lambda^k,\qquad \Lambda>1.
\]

The aim is to determine the exact vorticity-critical function space forced by the non-`H` shell geometry.

---

## 2. Critical shell enstrophy upper bound

From Campanato and the derivative ratio,
\[
\|f_k\|_2^2\le C_C R_k,
\]
and
\[
\|\nabla f_k\|_2^2
\le \frac{\Gamma_*^2}{R_k^2}\|f_k\|_2^2
\le \frac{C_C\Gamma_*^2}{R_k}.
\]

On the retained shell core `f_k=U`.  Since
\[
|\Omega|^2=|\nabla\times U|^2\le 2|\nabla U|^2,
\]
we obtain, after harmless fixed localization-overlap constants,
\[
\boxed{
 m_k^\omega
 :=\int_{A_k}|\Omega|^2dy
 \le \frac{C_\omega}{R_k},
}
\]
where `C_omega` depends only on the fixed Campanato/frequency/localization data.

This is the exact critical `R^{-1}` shell-enstrophy law of a `1/R` velocity / `1/R^2` vorticity tail.

**Status: PROVED.**

---

## 3. Strong L^q vorticity for every q>3/2

### 3.1 Range 3/2<q<2

On a shell of volume `|A_k|~R_k^3`, finite-volume embedding gives
\[
\|\Omega\|_{L^q(A_k)}
\le |A_k|^{1/q-1/2}\|\Omega\|_{L^2(A_k)}.
\]
Hence
\[
\int_{A_k}|\Omega|^qdy
\lesssim
R_k^{3(1-q/2)}
\left(R_k^{-1/2}\right)^q
=
R_k^{3-2q}.
\]
Since `q>3/2`,
\[
3-2q<0,
\]
and the geometric shell sum converges:
\[
\sum_kR_k^{3-2q}<\infty.
\]
Thus
\[
\boxed{
\Omega\in L^q(\mathbb R^3)
\qquad(3/2<q<2).
}
\]

### 3.2 Range q>=2

The first-hitting normalized amplitude/analytic corridor gives a finite `L^∞` vorticity ceiling on the smooth normalized track.  Interpolating `L^2` with `L^∞`,
\[
\boxed{
\Omega\in L^q(\mathbb R^3)
\qquad(2\le q\le\infty)
}
\]
for every fixed normalized time in the W1 corridor, with uniform bounds on the recurrent compact set.

Combining,
\[
\boxed{
\Omega\in L^q(\mathbb R^3)
\quad\text{for every }q>3/2.
}
\]

The endpoint `q=3/2` remains critical and is not obtained strongly.

**Status: PROVED.**

---

## 4. Weak-L^{3/2} endpoint from shell mass alone

Fix `lambda>0` and let
\[
E_\lambda:=\{y:|\Omega(y)|>\lambda\}.
\]
On shell `A_k`, Chebyshev gives
\[
|E_\lambda\cap A_k|
\le \frac{m_k^\omega}{\lambda^2}
\le \frac{C_\omega}{R_k\lambda^2}.
\]
Trivially,
\[
|E_\lambda\cap A_k|\le C_VR_k^3.
\]
Therefore
\[
|E_\lambda\cap A_k|
\le
C\min\left\{R_k^3,\frac1{R_k\lambda^2}\right\}.
\]

Choose the crossover radius `R_lambda` by
\[
R_\lambda^3
\asymp
\frac1{R_\lambda\lambda^2},
\]
so
\[
\boxed{R_\lambda\asymp\lambda^{-1/2}.}
\]

For shells `R_k\lesssim R_lambda`, sum the volume bound:
\[
\sum_{R_k\lesssim R_\lambda}|E_\lambda\cap A_k|
\lesssim R_\lambda^3
\lesssim \lambda^{-3/2}.
\]

For shells `R_k\gtrsim R_lambda`, sum the L2-Chebyshev bound:
\[
\sum_{R_k\gtrsim R_\lambda}|E_\lambda\cap A_k|
\lesssim
\lambda^{-2}\sum_{R_k\gtrsim R_\lambda}R_k^{-1}
\lesssim
\lambda^{-2}R_\lambda^{-1}
\lesssim
\lambda^{-3/2}.
\]
Thus
\[
\boxed{
|\{ |\Omega|>\lambda\}|
\le C\lambda^{-3/2}.
}
\]
Equivalently,
\[
\boxed{
\Omega\in L^{3/2,\infty}(\mathbb R^3),
\qquad
\|\Omega\|_{L^{3/2,\infty}}\le C_{\Omega,w}.
}
\]

This is the vorticity analogue of the velocity `L^{3,∞}` endpoint already isolated in W1.

**Status: PROVED.**

---

## 5. Scaling back to the physical solution

Use the viscosity-restored first-hitting scaling
\[
y=\frac{x-X(t)}{r(t)},
\qquad
\Omega(y,s)=\frac{r(t)^2}{\nu}\omega(x,t).
\]
The Lorentz `L^{3/2,∞}` norm is scale critical:
\[
\|\Omega\|_{L^{3/2,\infty}_y}
=
\nu^{-1}\|\omega\|_{L^{3/2,\infty}_x}.
\]
Therefore the W1 corridor implies
\[
\boxed{
\sup_{t\in(T^*-\epsilon,T^*)}
\|\omega(t)\|_{L^{3/2,\infty}(\mathbb R^3)}
\le
\nu C_{\Omega,w}<\infty.
}
\]

Hence W1 is not merely velocity-critical.  It lies simultaneously at the critical Lorentz endpoints
\[
\boxed{
 u\in L_t^\infty L_x^{3,\infty},
 \qquad
 \omega\in L_t^\infty L_x^{3/2,\infty}.
}
\]

**Status: PROVED.**

---

## 6. Why this does not by itself prove regularity

The model critical tail
\[
U\sim R^{-1},
\qquad
\Omega\sim R^{-2}
\]
satisfies exactly
\[
U\in L^{3,\infty}\setminus L^3,
\qquad
\Omega\in L^{3/2,\infty}\setminus L^{3/2},
\]
while belonging strongly to every super-endpoint space
\[
U\in L^p\quad(p>3),
\qquad
\Omega\in L^q\quad(q>3/2).
\]
Thus the new Lorentz bound confirms rather than removes the critical endpoint nature of W1.

---

## 7. External 2026 logarithmic-direction gate

A July 2026 preprint by Z. Grujic, `Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations` (arXiv:2607.08866), states a conditional regularity theorem for a first possible singular time under
\[
\omega\in L_t^\infty L_x^{3/2,\infty}
\]
and the vorticity-direction condition
\[
\xi:=\frac{\omega}{|\omega|}
\in
L_t^\infty\mathrm{bmo}_{1/|\log r|}.
\]
The stated conclusion is that the first possible singular time is regular.

This note does **not** promote that recent preprint to an unconditional repository input.  It is recorded as an external conditional gate to be independently audited before any mainline use.

Conditional on that theorem, the W1 endpoint would satisfy
\[
\boxed{
W1+\text{singularity}
\Longrightarrow
\xi\notin
L_t^\infty\mathrm{bmo}_{1/|\log r|}.
}
\]
Equivalently, any surviving W1 candidate must exhibit a logarithmically non-VMO phase defect:
\[
\boxed{
\sup_{t\uparrow T^*}
\sup_{x,0<r<1/2}
|\log r|\,
\fint_{B_r(x)}
|\xi-\xi_{B_r(x)}|\,dx
=\infty
}
\]
(or otherwise fail one of the precise hypotheses/definitions of the external theorem).

**Status: CONDITIONAL EXTERNAL ROUTING ONLY.**

---

## 8. DSD interpretation

The pure W1 survivor is now forced into an even narrower critical class:
\[
\boxed{
\begin{gathered}
U\in L^{3,\infty}\cap\bigcap_{p>3}L^p,\\
\Omega\in L^{3/2,\infty}\cap\bigcap_{q>3/2}L^q,\\
\sup_R\mathfrak C_R<\infty,\qquad
\sup_R\Gamma_R<\infty,\\
\text{global }L^p\text{-precompact recurrent orbit},\\
\text{persistent passive critical log-memory}.
\end{gathered}
}
\]

If the recent logarithmic-direction criterion is accepted after audit, the survivor additionally requires
\[
\boxed{
\text{critical logarithmic vorticity-direction phase roughness}.
}
\]

This is useful because it identifies the exact spatial phase defect that a future DSD rigidity lemma would have to price.  It does not yet show that such a defect necessarily pays an existing `H/T/projective` budget.

---

## 9. Next target

The next proof-producing target is one of:

1. audit the 2026 logarithmic-direction theorem and determine whether its phase condition can be weakened to a vorticity-amplitude-weighted version naturally controlled by DSD;
2. prove directly that a compact recurrent W1 Leray orbit with bounded shell frequency cannot sustain a logarithmically non-VMO direction defect without entering the projective/derivative-frequency/turnover ledgers;
3. for the long-period DSS subbranch, exploit time periodicity together with the new critical vorticity Lorentz structure to seek a periodic-vorticity Liouville theorem at the weak `L^{3/2}` endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
