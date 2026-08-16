# Frontier: fast spectral branch closed on the tight bounded-derivative track; productive strain becomes the universal source ledger

Date: 2026-08-16

Overall status: **THE PARABOLIC RENORMALIZATION LOOP HAS BEEN REDUCED FURTHER. PURE SKEW ROTATION COMMUTES WITH THE ISOTROPIC GAUSSIAN; TIGHT COMPACT-FREQUENCY UNIFORMLY-FAST NEAR RESONANCE IS DEPLETED EVEN IN THE PRESENCE OF VAN-HOVE CRITICAL POINTS; LOW FREQUENCY IS UNCERTAINTY-DEPLETED; HIGH FREQUENCY IS A DERIVATIVE ESCAPE; WEIGHTED PRESSURE-HESSIAN FORCING IS ABSORBED BY KERNEL-WEIGHTED ENSTROPHY. EVERY CLEAN-TO-COHERENT EPISODE PAYS A LOGARITHMIC ENSTROPHY-WEIGHTED POSITIVE-MIDDLE-STRAIN ACTION. GLOBAL REGULARITY NOT PROVED.**

---

## 1. Starting renormalization loop

The previous frontier had

\[
\text{coherent critical crossing}
\to
\text{fresh parabolic source}
\to
\begin{cases}
\text{supercritical residual pulse},\\
\text{thin V2/pressure pulse},\\
\log R\text{ symmetric strain}.
\end{cases}
\]

The supercritical residual pulse returned to another Reynolds-one crossing. Scalar energy/time estimates were critically saturated and could not stop this recursion.

The remaining question was whether the fast-rotation resonant realization of the returned crossing had a spatially tight low-cost survivor.

---

## 2. Pure skew rotation creates no Gaussian localization commutator

For `A^T=-A` and radial Gaussian `gamma_R`,

\[
(Ay)\cdot\nabla\gamma_R=0,
\qquad
\nabla\cdot(Ay)=0.
\]

Therefore

\[
\boxed{
\int\gamma_R(Ay\cdot\nabla f)=0.
}
\]

Also for the orthogonal flow `Q'=AQ`,

\[
\gamma_R(Qy)=\gamma_R(y).
\]

Thus the large coherent rigid-rotation coefficient does not multiply an observation-window commutator. Localization errors come only from symmetric affine deformation, axis/covariance variation, or extra compact cutoffs, all already typed by other ledgers.

---

## 3. Uniformly-fast near resonance on a compact turnover band

On a fixed annulus

\[
c_0\le |p|,|q|,|p+q|\le C_0,
\]

the inertial-wave phase

\[
\Phi(p,q)
=
 s_p\frac{p_\parallel}{|p|}
+s_q\frac{q_\parallel}{|q|}
-s_k\frac{(p+q)_\parallel}{|p+q|}
\]

is a nonzero real-analytic function of the pair frequency.

No uniform coarea transversality is assumed. Group-velocity critical / Van-Hove resonances can occur.

Nevertheless, compact real-analytic sublevel control yields some

\[
\alpha_*>0
\]

such that

\[
\big|\{|\Phi|\le\delta\}\big|
\lesssim
\delta^{\alpha_*}
\]

on the fixed block.

For a spatially tight packet, `L1` controls Fourier `Linfinity`, converting this sublevel measure into the same positive-power source gain.

A secular interaction over the `R` fast-rotation turnovers requires

\[
\delta\lesssim R^{-1}.
\]

Since the residual-gradient source has basic size `R^-2`,

\[
\boxed{
|J_{\rm near}|
\lesssim
R^{-2-\alpha_*},
\qquad
\int_0^{cR^2}|J_{\rm near}|dt
\lesssim R^{-\alpha_*}\to0.
}
\]

Hence compact-frequency spatially tight uniformly-fast near resonance is depleted, including the effect of Van-Hove critical points through a degraded but positive exponent.

---

## 4. Frequency endpoints

For a spatially tight turnover packet `G`,

\[
\|\widehat G\|_\infty
\lesssim
\|G\|_2.
\]

Therefore

\[
\boxed{
\|P_{\le\lambda}G\|_2
\lesssim
\lambda^{3/2}\|G\|_2.
}
\]

Any low-frequency escape `lambda_R->0` is negligible in the full `R^2` source interval.

For high frequencies,

\[
\boxed{
\|P_{\ge\Lambda}G\|_2
\le
\Lambda^{-1}\|\nabla G\|_2.
}
\]

Thus `Lambda_R->infinity` either becomes negligible or forces one further derivative of the residual packet to diverge.

Combined with the earlier near-slow uncertainty estimate, there is no remaining purely spectral source which is simultaneously

- spatially tight,
- turnover-frequency compact,
- derivative/modulation bounded.

---

## 5. Spatial escape from the returned crossing is not independent

If the returned fast-rotation crossing abandons spatial tightness, the previously derived material-vorticity-flux argument applies.

Spatial non-tightness is routed to

\[
\boxed{
\text{palinstrophy/derivative concentration}
\quad\lor\quad
\text{strain-driven material deformation}.
}
\]

Hence the former unpaid recursion

\[
\text{crossing}\to\text{residual pulse}\to\text{crossing}
\]

can no longer remain on a tight, bounded-derivative resonant track. Every return must now pay derivative/modulation growth, spatial-material deformation, or symmetric strain.

---

## 6. Pressure-Hessian is absorbed by kernel-weighted enstrophy

Pressure satisfies

\[
-\Delta P=\partial_iU_j\partial_jU_i.
\]

Calderon--Zygmund and the first-hitting cap `||Omega||_infinity<=1` imply

\[
\boxed{
\|\nabla^2P\|_2^2
\lesssim E.
}
\]

For an age-`tau` bounded-condition Gaussian,

\[
\Pi_P(\tau)^2
\lesssim
\tau^{-3/2}E(\tau).
\]

Therefore the exact pressure weight appearing in residual-variance dynamics obeys

\[
\boxed{
\int\tau\Pi_P^2d\tau
\lesssim
\int\tau^{-1/2}E(\tau)d\tau
=\mathfrak Z_K.
}
\]

The pressure-Hessian branch is thus absorbed into the already established mesoscopic-enstrophy / terminal-enstrophy-concentration routing.

---

## 7. Universal productive positive-middle-strain action

From the exact enstrophy identity

\[
\frac12E'+\nu P=Q,
\qquad
Q=\int\Omega\cdot S\Omega,
\]

dividing by `E` gives

\[
\int_{s_m}^{s_c}\frac QE ds
\ge
\frac12\log\frac{E_c}{E_m}.
\]

Global Betchov gives

\[
Q=-4\int\det S.
\]

If `lambda_1>=lambda_2>=lambda_3`, then

\[
Q
\le
2\int\lambda_2^+|S|^2.
\]

Hence

\[
\boxed{
\int_{s_m}^{s_c}
\frac{\int\lambda_2^+|S|^2dx}{E(s)}ds
\ge
\frac14\log\frac{E_c}{E_m}.
}
\]

Using

\[
E_m\lesssim R^\beta/\sqrt W,
\qquad
E_c\gtrsim R^3,
\qquad
\sqrt W\gtrsim R^5(\log R)^{5/2},
\]

one obtains

\[
\boxed{
\int
\frac{\int\lambda_2^+|S|^2}{E}ds
\gtrsim
\frac{8-\beta}{4}\log R
+\frac58\log\log R-O(1).
}
\]

Thus every coherent episode pays logarithmically diverging **enstrophy-weighted productive middle-strain action**.

Derivative pulses cannot replace this production because viscosity enters the enstrophy balance with the opposite sign. They can only localize/modulate the productive strain and increase the required nonlinear production.

---

## 8. Revised proof graph

The source-active endgame is now better represented as

\[
\boxed{
\text{clean precursor}
\to
\text{fresh parabolic generation}
\to
\text{productive }\lambda_2^+\text{ strain}
}
\]

with attempts to hide/localize that productive action routed into

\[
\boxed{
\text{spatial/material concentration}
\quad\lor\quad
\text{higher derivative/modulation}
\quad\lor\quad
\text{symmetric affine deformation}.
}
\]

The previously separate pure fast-resonant and weighted-pressure escape routes have been removed on the stated branches.

---

## 9. What remains genuinely open

The remaining wall is no longer a scalar source-size estimate and no longer a generic resonance classification.

A proof requires a cross-scale theorem excluding infinite repetition of the following organized event:

\[
\boxed{
\begin{gathered}
\text{a clean low-enstrophy precursor is rebuilt into an }R^3\text{ coherent core},\\
\text{the episode pays }c\log R\text{ enstrophy-weighted positive-middle-strain action},\\
\text{and any concentration needed to realize that action is pushed into}\\
\text{spatial/material deformation or higher-derivative/modulation channels.}
\end{gathered}
}
\]

The action is scale critical and may diverge at a hypothetical singularity, so its divergence alone is not a contradiction.

The missing theorem is therefore a **structured productive-strain nonrepeatability theorem**, likely requiring cross-scale geometric or derivative packing rather than another one-scale scalar inequality.

Overall status: **PURE ROTATION LOCALIZATION ERROR CLOSED / TIGHT FAST SPECTRAL RESONANCE CLOSED ON COMPACT BOUNDED-DERIVATIVE BLOCKS / FREQUENCY ENDPOINTS ROUTED / PRESSURE-HESSIAN ABSORBED / PRODUCTIVE POSITIVE-MIDDLE STRAIN IS THE UNIVERSAL SOURCE LEDGER / CROSS-SCALE NONREPEATABILITY OPEN / GLOBAL REGULARITY NOT PROVED.**