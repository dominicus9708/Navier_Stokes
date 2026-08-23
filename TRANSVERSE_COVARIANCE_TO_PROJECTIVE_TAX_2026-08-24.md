# Transverse Covariance -> Projective Tax — 2026-08-24

Status: **MULTISTAGE DEFORMATION-CONTROL BRIDGE / CONDITIONAL PURE-CORRIDOR CLOSURE TEST / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `TRANSVERSE_REMOTE_STRAIN_COVARIANCE_GATE_2026-08-24.md`,
- `POSITIVE_MIDDLE_TRANSVERSE_RIBBON_GATE_2026-08-21.md`, and
- `SMOOTH_PROJECTIVE_ACTION_VISCOUS_TAX_CLOSURE_2026-08-21.md`.

Its purpose is to replace the informal statement

\[
\text{bounded transverse aspect ratio}
\Longrightarrow
\text{projective/eigenframe action}>0
\]

by a quantitative multistage inequality.

---

## 1. Transverse covariance equation

Use the exact transverse shape identity

\[
\boxed{
E_\perp'=2q_\perp D+\mathcal R_\perp.
}
\]

Here

\[
q_\perp=\frac12\operatorname{tr}(PQP),
\]

`E_perp` is the transverse trace-free covariance, `D` is the transverse symmetric trace-free remote affine strain, and `R_perp` contains all axis motion, non-affine/local compensation, cutoff/material leakage, source imbalance, and lower-order coupling terms.

Define on a stage `I_j`

\[
A_{D,j}=\int_{I_j}|D|_Fds,
\qquad
A_{R,j}=\int_{I_j}|\mathcal R_\perp|_Fds.
\]

---

## 2. Positive-middle action floor

On the aligned positive-middle lane,

\[
s_1<0\le s_2\le s_3,
\qquad
\xi\simeq e_3.
\]

Relative to `xi`, the transverse trace-free strain has eigenvalues

\[
\pm\frac{s_2-s_1}{2},
\]

so

\[
\boxed{
|D|_F=\frac{s_2-s_1}{\sqrt2}.
}
\]

Trace freeness gives

\[
s_2-s_1=s_3+2s_2\ge s_3.
\]

Therefore

\[
\boxed{
A_{D,j}
\ge
\frac1{\sqrt2}\int_{I_j}s_3ds.
}
\]

If the flux-preserving positive-middle stage supplies logarithmic stretching action

\[
\int_{I_j}s_3ds
\ge a_3>0,
\]

then

\[
\boxed{
A_{D,j}\ge a_D:=\frac{a_3}{\sqrt2}.
}
\]

For an ideal `q=2` flux-preserving stage,

\[
a_3\simeq\log2,
\qquad
\boxed{
a_D\simeq\frac{\log2}{\sqrt2}\approx0.4901290717.
}
\]

Any deficit from `log q` is not silently discarded; it belongs to the already typed viscous-flux/tilt/residual alternatives.

---

## 3. Covariance anisotropy and RMS aspect ratio

Let the two transverse eigenvalues of `Q_perp` be

\[
\lambda_-\le\lambda_+.
\]

Write

\[
\lambda_\pm=q_\perp(1\pm\eta),
\qquad
0\le\eta<1.
\]

Then

\[
\boxed{
|E_\perp|_F=\sqrt2\,q_\perp\eta.
}
\]

The covariance/RMS aspect ratio is

\[
\boxed{
\mathrm{AR}_Q
=\sqrt{\frac{\lambda_+}{\lambda_-}}
=\sqrt{\frac{1+\eta}{1-\eta}}.
}
\]

Equivalently,

\[
\boxed{
\eta
=\frac{\mathrm{AR}_Q^2-1}{\mathrm{AR}_Q^2+1}.
}
\]

Thus `AR_Q=2` is exactly

\[
\eta=\frac35,
\]

or

\[
\boxed{
\frac{|E_\perp|_F}{q_\perp}
=\frac{3\sqrt2}{5}
\approx0.8485281374.
}
\]

This gives a tensorial version of the earlier ribbonization threshold.

---

## 4. Coherence-block inequality

Assume on a long pure corridor

\[
\boxed{
q_\perp(s)\ge q_->0,
\qquad
|E_\perp(s)|_F\le E_+<\infty.
}
\]

Whenever `D != 0`, define

\[
\widehat D=D/|D|_F.
\]

Fix

\[
0<\alpha<\frac\pi2.
\]

Partition the corridor into maximal coherence blocks on which the total variation of `D_hat` is less than `alpha`. On each such block there is a fixed unit trace-free tensor `D_hat_*` satisfying

\[
\langle D,\widehat D_*\rangle_F
\ge
\cos\alpha\,|D|_F.
\]

Integrating the covariance identity over one coherence block `B` gives

\[
2q_-\cos\alpha
\sum_{j\in B}A_{D,j}
\le
2E_+
+
\sum_{j\in B}A_{R,j}.
\]

Using the per-stage action floor `A_D,j >= a_D`,

\[
\boxed{
2q_-a_D\cos\alpha\,N_B
\le
2E_++R_B,
}
\]

where `N_B` is the number of stages in the block and

\[
R_B=\sum_{j\in B}A_{R,j}.
\]

This is the quantitative deformation-control inequality.

---

## 5. Long-corridor direction-turnover density

Consider the first `N` stages and suppose the residual action has asymptotic density at most `r_0`:

\[
\sum_{j=1}^NA_{R,j}
\le r_0N+o(N).
\]

Let `B_N` be the number of completed `alpha`-coherence blocks. Summing the preceding inequality over all blocks gives

\[
2q_-a_D\cos\alpha\,N
\le
2E_+B_N+r_0N+o(N).
\]

Hence, if

\[
\boxed{
2q_-a_D\cos\alpha>r_0,
}
\]

then

\[
\boxed{
\liminf_{N\to\infty}\frac{B_N}{N}
\ge
\frac{2q_-a_D\cos\alpha-r_0}{2E_+}.
}
\]

Every completed block costs at least `alpha` variation of `D_hat`, so

\[
\boxed{
\liminf_{N\to\infty}
\frac{\operatorname{TV}(\widehat D;1{:}N)}N
\ge
\alpha
\frac{2q_-a_D\cos\alpha-r_0}{2E_+}.
}
\]

Thus bounded transverse shape plus positive `D` action plus subcritical residual action forces **projective direction turnover with positive density in the number of stages**.

This removes `T_shape` as an independent quiet infinite-corridor escape: if the shape itself does not turn over without bound, `D` must.

---

## 6. Convert D-direction turnover to transverse eigenaxis turnover

A transverse symmetric trace-free `2 x 2` tensor can be written

\[
D=d
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix}.
\]

Therefore the tensor-direction angle is twice the physical transverse eigenaxis angle:

\[
\boxed{
\operatorname{TV}(\theta_e)
=\frac12\operatorname{TV}(\widehat D)
}
\]

as long as `D` remains nondegenerate. Degeneracy `D -> 0` removes the active transverse channel and is itself an exit from the present branch.

Consequently the asymptotic eigenaxis-turnover action per stage is bounded below by

\[
\boxed{
a_{\theta}(\alpha)
:=
\frac{\alpha}{4E_+}
\left(
2q_-a_D\cos\alpha-r_0
\right)_+.
}
\]

The existing anti-ribbon projective ledger gives

\[
\operatorname{TV}(\theta_e)
\le
\int c_V(s)ds,
\]

so the average projective action also satisfies

\[
\boxed{
\liminf_{N\to\infty}
\frac1N\sum_{j=1}^N\int_{I_j}c_Vds
\ge a_\theta(\alpha).
}
\]

This is the requested quantitative bridge from bounded transverse deformation to projective action.

---

## 7. Zero-residual optimized coherence angle

If `r_0=0`, the lower bound is proportional to

\[
\alpha\cos\alpha.
\]

The maximizing angle solves

\[
\tan\alpha=\frac1\alpha,
\]

with

\[
\boxed{
\alpha_*\approx0.8603335890\ \text{rad},
\qquad
\alpha_*\cos\alpha_*\approx0.5610963382.
}
\]

Hence

\[
\boxed{
a_{\theta}^{opt}
\ge
0.2805481691\,
\frac{q_-a_D}{E_+}
}
\]

in the residual-free benchmark.

For the ideal `q=2` positive-middle action floor,

\[
a_D=\frac{\log2}{\sqrt2},
\]

so

\[
\boxed{
a_{\theta}^{opt}
\gtrsim
0.137506\,
\frac{q_-}{E_+}
\quad\text{radians per stage}.
}
\]

This benchmark is not yet an unconditional numerical constant because the ratio `q_-/E_+` must be supplied by the thick-core geometry.

---

## 8. Projective action -> frequency tax

The existing explicit projective-speed estimate is

\[
c_V-c_0
\le
K_P\lambda^{3/4}Z^{1/2},
\]

where

\[
c_0=\frac{\sqrt2}{4},
\qquad
K_P=\frac1{3\sqrt2}S_3^{-3/4}.
\]

Assume

\[
Z\le Z_+,
\qquad
L_j\le L_+.
\]

Over `N` stages, the covariance bridge supplies asymptotic projective action at least `N a_theta`. Therefore

\[
\sum_{j=1}^N\int_{I_j}(c_V-c_0)_+ds
\ge
N(a_\theta-c_0L_+)_++o(N).
\]

Holder/Jensen over the union of the stages then gives

\[
\boxed{
\liminf_{N\to\infty}\frac1N
\sum_{j=1}^N\int_{I_j}\lambda ds
\ge
K_P^{-4/3}Z_+^{-2/3}L_+^{-1/3}
(a_\theta-c_0L_+)_+^{4/3}.
}
\]

Thus repeated tensor-shape preservation forces a positive viscous-frequency tax whenever

\[
\boxed{
a_\theta>c_0L_+.}
\]

---

## 9. H1 telescoping closure test

On the bounded pure corridor, the H1 stage ledger is

\[
\frac12\log\frac{P_{j+1}}{P_j}
+\frac34\log q
+\nu\int_{I_j}\frac HPds
=
\int_{I_j}\frac NPds.
\]

Using

\[
\frac HP\ge\lambda,
\qquad
\frac NP\le\sqrt2B_+,
\]

and telescoping the bounded endpoint `P` terms over many stages, an infinite pure transverse corridor is S-closed whenever

\[
\boxed{
\sqrt2B_+L_+
<
\frac34\log q
+
\nu K_P^{-4/3}Z_+^{-2/3}L_+^{-1/3}
(a_\theta-c_0L_+)_+^{4/3}.
}
\]

This is the direct tensor-covariance analogue of the existing anti-ribbon projective-action viscous-tax closure.

---

## 10. Remaining numerical/geometric input

The transverse branch is now reduced to explicit finite quantities:

\[
\boxed{
q_-,\quad E_+,\quad a_D,\quad r_0,\quad L_+,\quad Z_+,\quad B_+.
}
\]

Of these, `a_D`, `L_+`, `Z_+`, and `B_+` already have estimates on the existing positive-middle/tight smooth corridor.

The genuinely new geometric input is the thick-core covariance ratio and residual density:

\[
\boxed{
\Xi_\perp:=\frac{E_+}{q_-a_D},
\qquad
\rho_R:=\frac{r_0}{2q_-a_D}.
}
\]

If the core is uniformly thick enough to bound `Xi_perp` and the residual lane is quiet enough that `rho_R<cos alpha`, the transverse affine channel necessarily generates projective action at positive density.

The next target is therefore **not** another affine-strain case split. It is to derive a lower bound on `q_-` and an upper bound on `E_+` from the already tracked thick-core/non-sparseness hypotheses, or else route failure of those covariance bounds directly to geometric sparseness/turnover.

Status: **THE MAIN DEFORMATION-CONTROL OBLIGATION LEFT OPEN IN THE 2026-08-21 RIBBON NOTE NOW HAS A QUANTITATIVE MULTISTAGE FORM. A BOUNDED-SHAPE, POSITIVE-MIDDLE, RESIDUAL-QUIET TRANSVERSE CORRIDOR MUST ACCUMULATE PROJECTIVE EIGENAXIS ACTION AT POSITIVE STAGE DENSITY; THAT ACTION FEEDS THE EXISTING SOBOLEV FREQUENCY TAX AND H1 TELESCOPING LEDGER. THE NEW BOTTLENECK IS THE THICK-CORE COVARIANCE RATIO `Xi_perp`, NOT THE EXISTENCE OF THE TRANSVERSE AFFINE CHANNEL ITSELF. GLOBAL REGULARITY REMAINS UNPROVED.**