# DSD M17-254 — Every fixed rescaled backward corridor follows by finite iteration or exhibits a local payment

Date: 2026-09-06  
Canonical ID: **M17-254**

Status: **BACKWARD-LIFETIME AUDIT / M17-226 GIVES TWO-SIDED MASS COMPARABILITY ON ONE FIXED OWN-SCALE PARABOLIC WINDOW `O(r_j^2)` UNLESS PALINSTROPHY, INTERFACE/REPLENISHMENT, OR A COEFFICIENT EXIT OCCURS. FOR AN ANCIENT/RECURRENT CE-H ORBIT, A FIXED RESCALED BACKWARD TIME `T` CORRESPONDS TO ONLY `T r_j^2` OF ORIGINAL SIMILARITY TIME. PARTITION THIS INTO FINITELY MANY M17-226 WINDOWS. IF ANY WINDOW HAS A FIXED NORMALIZED PAYMENT OR A SCALED COEFFICIENT EXIT, RECORD THAT PAYER. OTHERWISE FINITE ITERATION GIVES `C_T^- M_j(0) <= M_j(theta) <= C_T^+ M_j(0)` ON THE WHOLE `[-T r_j^2,0]` CORRIDOR. A DIAGONAL SUBSEQUENCE OVER INTEGER `T` THEREFORE REMOVES 'BACKWARD LIFETIME' AS AN INDEPENDENT FRONTIER: THE REAL REMAINING ISSUE IS PAYER-FREE SPACETIME COMPACTNESS ON ALL FIXED PARABOLIC CYLINDERS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One-window input from M17-226

Let

\[
M_j(\theta)
=\int\zeta_j(\theta)^2|W|^2dy
\]

be the moving localized enstrophy of a scale-`r_j` packet.

M17-226 proves that on one window of length

\[
2c_pr_j^2
\]

centered at an observation time, either

1. a normalized palinstrophy/interface/replenishment payment occurs;
2. a coefficient corridor fails;
3. or the packet mass stays comparable to its value at the center of the window.

Schematically,

\[
\boxed{
H_{one\ parabolic\ window}
\Longrightarrow
H_{mass\ comparability}
\lor H_{payment}
\lor G_{coefficient}.
}
\]

No backward heat inequality is used; every backward statement is read in the physical forward time direction.

---

## 2. Fixed rescaled backward horizon

Fix once and for all

\[
T>0.
\]

The desired original-time interval is

\[
\boxed{
I_{j,T}
=[\theta_j-Tr_j^2,\theta_j].
}
\]

Choose

\[
N_T:=\left\lceil\frac{T}{c_p}\right\rceil.
\]

Then `I_{j,T}` can be partitioned into at most `N_T` adjacent intervals, each of length at most

\[
c_pr_j^2.
\]

For fixed `T`, `N_T` is finite and independent of `j`.

---

## 3. Scale-normalized payment on a subwindow

For a subwindow `J`, define the normalized localized payment

\[
\boxed{
\mathfrak P_j(J)
:=
\frac{1}{M_j(\theta_J)}
\left[
\int_JD_jd\theta
+r_j^{-2}\int_JN_jd\theta
\right],
}
\]

where `theta_J` is one chosen endpoint or center whose mass is comparable on the previously accepted windows.

A fixed lower bound

\[
\mathfrak P_j(J)\ge\varepsilon_*>0
\]

is recorded as the corresponding local palinstrophy/interface payment branch.

For coefficient terms define a dimensionless own-scale corridor size

\[
\boxed{
\mathfrak C_j(J)
:=
 r_j^2
 \sup_{\theta\in J}
 \sup_{B_{Cr_j}(q_j(\theta))}
 \left(|\nabla B|+|\Sigma|+1\right).
}
\]

A fixed large or nonvanishing `mathfrak C_j` is retained as a scaled coefficient/ambient branch when the heat-tangent line requires `mathfrak C_j->0`.

---

## 4. Finite induction when no subwindow pays

Assume no subwindow in the partition has a fixed payment and the coefficient corridor remains within the constants required by the one-window estimate.

Let the one-window mass ratio satisfy

\[
\boxed{
 c_*M_j(\theta_k)
 \le
 M_j(\theta)
 \le
 C_*M_j(\theta_k)
}
\]

on the `k`-th accepted subwindow, for fixed `0<c_*<=1<=C_*<infinity`.

After `m` windows,

\[
 c_*^mM_j(\theta_j)
 \le
 M_j(\theta)
 \le
 C_*^mM_j(\theta_j).
\]

Since

\[
m\le N_T<\infty,
\]

define

\[
\boxed{
C_T^-:=c_*^{N_T}>0,
\qquad
C_T^+:=C_*^{N_T}<\infty.
}
\]

Then

\[
\boxed{
C_T^-M_j(\theta_j)
\le
M_j(\theta)
\le
C_T^+M_j(\theta_j)
\qquad
(\theta\in I_{j,T}).
}
\]

The constants may depend on `T` but not on `j`.

This is sufficient for fixed-cylinder tangent extraction.

---

## 5. Exhaustive fixed-T gate

For every fixed `T>0`, after passing to a subsequence if necessary,

\[
\boxed{
H_{packet\ at\ theta_j}
\Longrightarrow
H_{T\text{-}backward\ mass\ corridor}
\lor H_{payment\ before\ T}
\lor G_{scaled\ coefficient/ambient\ before\ T}.
}
\]

The first alternative means

\[
\boxed{
C_T^-
\le
\frac{M_j(\theta_j+r_j^2\tau)}{M_j(\theta_j)}
\le
C_T^+
\qquad
(-T\le\tau\le0).
}
\]

Thus the normalized packet neither vanishes nor explodes on that fixed backward cylinder.

---

## 6. Why ancient existence is not the obstacle

The recurrent CE-H branch being analyzed is already an ancient similarity orbit.

For fixed `T`, the required original-time lookback is only

\[
Tr_j^2\to0.
\]

Hence for sufficiently large `j` the solution exists throughout `I_{j,T}`.

The difficulty is not PDE existence on that short physical interval.

It is whether the selected packet remains in the payer-free compactness corridor.

Therefore

\[
\boxed{
\text{backward existence}
\neq
\text{backward normalized packet persistence}.
}
\]

M17-254 handles the latter by a finite gate.

---

## 7. Diagonal extraction over all fixed T

Take integer horizons

\[
T=1,2,3,\dots.
\]

Suppose the payment/coefficient alternatives are absent along a nested subsequence for every finite integer horizon.

For `T=1`, extract a subsequence with the corridor.

From it extract a further subsequence for `T=2`, and continue.

The diagonal subsequence has, for every fixed finite `T`,

\[
\boxed{
C_T^-
\le
\frac{M_j(\theta_j+r_j^2\tau)}{M_j(\theta_j)}
\le
C_T^+
\qquad
(-T\le\tau\le0).
}
\]

Thus the mass-normalization part of an ancient tangent is available on every compact backward time interval.

---

## 8. What remains after the diagonal mass corridor

M17-254 does not provide spacetime derivative compactness.

To obtain an ancient heat tangent one still needs, for every fixed `K,T`, uniform control on

\[
B_K\times[-T,0]
\]

sufficient to pass the rescaled PDE to the limit.

In particular the following remain:

1. local parabolic `H2/H1` estimates on the whole cylinder;
2. vanishing scaled drift/strain on the no-payer branch;
3. spatial normalized mass tightness/growth control;
4. exclusion or classification of renewed strict subscale defects at earlier times.

Hence the corrected next target is **finite-cylinder spacetime compactness**, not backward lifespan.

---

## 9. DSD audit

- Only finitely many one-window estimates are iterated for each fixed `T`.
- Constants are allowed to depend on `T`; no false uniform-in-`T` estimate is claimed.
- Backward information is never obtained by reversing diffusion.
- A payment on any subwindow terminates the payer-free induction and is recorded explicitly.
- The coefficient/ambient corridor is made dimensionless at the packet scale.
- Ancient solution existence is separated from normalized packet persistence.
- Diagonal extraction is used only after every finite horizon has its own valid estimate.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
