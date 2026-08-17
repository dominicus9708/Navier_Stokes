# Frontier: local Betchov buffer and cross-time band-repopulation wall

Date: 2026-08-17

Overall status: **THE CRITICAL AFFINE-RESIDUAL FIXED POINT HAS BEEN REDUCED FURTHER. PRODUCTIVE POSITIVE-MIDDLE STRAIN IS CONNECTED QUANTITATIVELY TO THE KNOWN SCALE-CRITICAL `L_t^2L_x^3` MIDDLE-EIGENVALUE CRITERION. LOW GAUSSIAN VARIANCE EXTENDS COHERENT ENSTROPHY AND CRITICAL VELOCITY `L^3` TO `R sqrt(log R)`. MOST IMPORTANTLY, THE LOCAL BETCHOV FLUX HAS BEEN RELOCALIZED: A REMOTE WHOLE-SPACE ENSTROPHY RESERVOIR CAN NO LONGER PAY THE EXTERIOR COMPENSATION COST. COMPENSATION MUST APPEAR IN THE SAME BUFFER AS LOCAL STRAIN ENERGY OR LOCAL SECOND-GRADIENT ENERGY. AFFINE CONTINUATION OF THAT BUFFER IS ALSO NOT FREE: ITS EVENTUAL LARGE-SCALE TERMINATION PAYS AN EXACT POSITIVE DYADIC GAUSSIAN BAND COST. THE REMAINING WALL IS CROSS-TIME REPOPULATION OF MOVING PHYSICAL SCALE BANDS / CRITICAL STRAIN ACTION. GLOBAL REGULARITY IS NOT PROVED.**

---

## 1. Starting fixed point

The minimally escaping coherent episode is pinned to

\[
\mathcal B_R=R^{-2+o(1)},
\qquad
q_{aff}=R^{2+o(1)},
\]

\[
\lambda_{max}\Sigma\asymp R^2,
\qquad
\mathcal J_S=R^{o(1)},
\]

with a final hyperbolic/Riccati deformation stage of normalized duration

\[
\Delta t_{ramp}=R^{1+o(1)}.
\]

A reduced affine-residual benchmark saturates all current one-scale scalar inequalities, so another fixed power gain is not expected to close the problem.

The missing information is whole-space spatial self-consistency.

---

## 2. Positive-middle strain is a standard critical norm boundary

Let

\[
M(t)=\int\lambda_2^+|S|^2dx,
\quad
E=\|\omega\|_2^2,
\quad
P=\|\nabla\omega\|_2^2.
\]

The exact enstrophy identity and global Betchov imply

\[
2\int\frac{M}{E}dt
\ge
\frac12\log\frac{E_c}{E_m}
+\nu\int\frac{P}{E}dt.
\]

Holder and interpolation give

\[
M
\lesssim
\|\lambda_2^+\|_3E^{1/2}P^{1/2}.
\]

Optimizing over

\[
D=\int P/E
\]

yields

\[
\boxed{
\int_{t_m}^{t_c}\|\lambda_2^+\|_3^2dt
\gtrsim
\nu\log(E_c/E_m)
\gtrsim c_{\nu,\beta}\log R.
}
\]

This is not a new regularity criterion. It is the `p=2,q=3` member of the known middle-eigenvalue scale-critical family (E. Miller, ARMA 2020 / arXiv:1710.05569), quantitatively attached here to the DSD clean-precursor -> coherent-crossing episode.

Therefore the productive branch is already known to be compatible with singularity only through divergence of a standard critical norm.

---

## 3. Low variance forces logarithmically enlarged coherent occupancy

At a late coherent time with

\[
|\bar\Omega|\gtrsim1,
\qquad
B\lesssim R^{-2},
\]

bounded-condition Gaussian tails and Euclidean Poincare give coherence out to

\[
L_R\asymp R\sqrt{\log R}.
\]

Consequently

\[
\boxed{
\int_{B_{L_R}}|\Omega|^2dx
\gtrsim
R^3(\log R)^{3/2},
}
\]

and the affine velocity component gives

\[
\boxed{
\|U\|_3^3
\gtrsim
R^6(\log R)^3.
}
\]

The latter is a scale-invariant velocity `L^3` escape signature.

Scale-separated enlarged coherent probes remain Bessel, so temporal overlap does not remove the strengthened occupancy ledger

\[
\boxed{
\sum_j
\frac{R_j^3(\log R_j)^{3/2}}{\sqrt{W_j}}
<\infty.
}
\]

The adversarial power-law Zeno family still passes this test.

---

## 4. Aligned `lambda_2<=0` mismatch is stable unless cubic residual strain is macroscopic

On the late aligned branch with mean maximal extension and

\[
\bar\lambda_2\le0,
\]

the affine reference Betchov mismatch is strictly positive and order one.

The quadratic Gaussian residual is negligible relative to the enlarged volume `L_R^3`. Polynomial stability then gives the dichotomy

\[
\boxed{
\int_{B_{L_R}}|S-\bar S|^3dx
\gtrsim L_R^3
}
\]

or

\[
\boxed{
\int_{B_{L_R}}
(\omega\cdot S\omega+4\det S)dx
\gtrsim L_R^3.
}
\]

Thus failure of the coherent mismatch itself is already a macroscopic cubic residual-strain concentration.

---

## 5. Localize the Betchov boundary flux

The earlier cutoff estimate used whole-space enstrophy/palinstrophy. That allowed an irrelevant remote reservoir to enlarge the right-hand side.

For any constant vector `c`, the shifted field `u-c` has the same gradient and

\[
\nabla\cdot\mathcal F_A(u-c)=\operatorname{tr}(A^3).
\]

Choose `c` as a buffer-annulus average and define

\[
e_L=\int_{A_L^*}|\nabla u|^2dx,
\qquad
p_L=\int_{A_L^*}|\nabla^2u|^2dx.
\]

Local Poincare--Sobolev gives

\[
\boxed{
\left|\int\nabla\chi_L\cdot\mathcal F_A dx\right|
\lesssim
L^{-1}e_L^{5/4}p_L^{1/4}
+
L^{-3/2}e_L^{3/2}.
}
\]

If the inner mismatch is `>=cL^3`, write

\[
z=e_L/L^3,
\qquad
w=p_L/L.
\]

Then

\[
1\lesssim z^{5/4}w^{1/4}+z^{3/2},
\]

so

\[
\boxed{
 e_L\gtrsim L^3
\quad\lor\quad
 p_L\gtrsim L.
}
\]

At the logarithmic coherent radius,

\[
\boxed{
 e_{L_R}
\gtrsim
R^3(\log R)^{3/2}
}
\]

or

\[
\boxed{
 p_{L_R}
\gtrsim
R\sqrt{\log R}.
}
\]

This removes the **remote exterior enstrophy reservoir** as an independent compensation mechanism. The compensation is genuinely local to the buffer scale.

---

## 6. Exact Gaussian mean-termination bands

A local strain reservoir can try to remain approximately affine and simply continue outward. This also has an exact scale cost.

For

\[
m_r(x_*)=(g_r*f)(x_*),
\]

with Gaussian multiplier

\[
\widehat g_r=e^{-r^2|\xi|^2/2},
\]

define

\[
\mathfrak b_r(f)
=
\int
\left(
e^{-r^2|\xi|^2/2}
-e^{-2r^2|\xi|^2}
\right)|\widehat f|^2d\xi.
\]

Weighted Cauchy--Schwarz gives

\[
\boxed{
r^3|m_r-m_{2r}|^2
\lesssim
\mathfrak b_r(f).
}
\]

For `r_k=2^kr_0`, the band weights telescope exactly:

\[
\sum_k
\left(
e^{-r_k^2|\xi|^2/2}
-e^{-r_{k+1}^2|\xi|^2/2}
\right)
=e^{-r_0^2|\xi|^2/2}.
\]

Since `f in L^2` implies `m_r->0`, weighted Cauchy over the outward scale ladder yields

\[
\boxed{
\sum_{k\ge0}\mathfrak b_{r_k}(f)
\gtrsim
r_0^3|m_{r_0}(x_*)|^2.
}
\]

For `f=S` or `f=omega`, an order-one coherent/affine mean therefore cannot continue to arbitrarily large scales and vanish for free. Its termination is recorded in the same positive Gaussian scale partition used for residual fluctuations.

---

## 7. Revised exterior-compensation graph

The previous branch

\[
\text{aligned critical ramp}
\to
\text{Betchov exterior compensation}
\]

now becomes

\[
\boxed{
\text{aligned critical ramp}
\to
\begin{cases}
\lambda_2^+\text{ critical action},\\
\text{macroscopic cubic residual strain},\\
\text{local buffer }e_L\gtrsim L^3,\\
\text{local derivative }p_L\gtrsim L.
\end{cases}
}
\]

and if the local buffer reservoir is an affine continuation,

\[
\boxed{
\text{affine continuation}
\to
\text{eventual positive dyadic mean-termination band cost}.
}
\]

Thus there is no longer an untyped `remote reservoir` leaf in the proof graph.

---

## 8. Current single wall

At a fixed time and fixed coherent episode, the exterior compensation is now scale-localized and positively packed.

The unresolved issue is temporal:

\[
\boxed{
\textbf{Can successive first-hitting episodes repopulate new, progressively higher}\
\textbf{physical scale/frequency bands quickly enough that every episode obtains}\
\textbf{its local Betchov/productive-strain compensation, while the finite}\
\textbf{kinetic-energy dissipation and all established derivative/Bessel ledgers remain finite?}
}
\]

The existing fixed-frequency theorem says any fixed physical band contributes vanishing strain action on shrinking singular-tail intervals. Hence a survivor must move its active compensation frequency to infinity.

The new mean-termination theorem says each coherent affine state also leaves a positive outward scale-band footprint before disappearing.

What is still missing is a **cross-time moving-band repopulation theorem** coupling these two facts.

A likely target statement is:

> For a geometrically increasing first-hitting sequence, the moving physical bands that carry the required local buffer/mean-termination action cannot be repopulated with the necessary amplitude on every shrinking critical ramp unless either a scale-critical middle-strain norm, a derivative norm, or the kinetic-energy dissipation measure accumulates a quantitatively non-summable amount.

No proof of this statement is currently available.

---

## 9. Status

What is now closed/typed:

- cumulative scale double counting of Gaussian residual variance;
- temporal overlap for scale-separated Gaussian mean strain/vorticity probes;
- reuse of a fixed physical strain frequency;
- arbitrarily small residual seed without large actual affine deformation;
- arbitrary affine singular-value cancellation;
- remote whole-space enstrophy reservoir in the local Betchov cutoff estimate;
- affine continuation to large spatial scales without an eventual positive band cost;
- derivative concentration as a way to remove the middle-strain critical action;
- treating the `L_t^2L_x^3` positive-middle criterion as novel (it is a known criterion; only the episode-specific quantitative attachment is used here).

What remains:

\[
\boxed{
\text{cross-time repopulation of moving scale-local compensation bands}
}
\]

plus its equivalent formulations through critical positive-middle strain and local derivative concentration.

Overall status: **EXTERIOR COMPENSATION LOCALIZED / REMOTE RESERVOIR LOOPHOLE REMOVED / AFFINE TERMINATION POSITIVELY SCALE-PACKED / FINAL WALL MOVED TO CROSS-TIME MOVING-BAND REPOPULATION / GLOBAL REGULARITY NOT PROVED.**