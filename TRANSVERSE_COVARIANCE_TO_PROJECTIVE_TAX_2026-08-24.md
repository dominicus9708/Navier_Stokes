# Transverse Covariance -> Projective Tax — 2026-08-24

Status: **MULTISTAGE DEFORMATION-CONTROL BRIDGE WITH EXPLICIT REMOTE/FULL-STRAIN TRANSFER CONDITION / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `TRANSVERSE_REMOTE_STRAIN_COVARIANCE_GATE_2026-08-24.md`,
- `POSITIVE_MIDDLE_TRANSVERSE_RIBBON_GATE_2026-08-21.md`, and
- `SMOOTH_PROJECTIVE_ACTION_VISCOUS_TAX_CLOSURE_2026-08-21.md`.

A scope correction is essential: the covariance equation below is driven by the **remote** transverse affine strain `D_rem`, whereas the positive-middle eigenvalue relations and the existing projective-speed ledger concern the **full** strain. These are not automatically identical. The transfer between them is therefore made an explicit branch condition rather than assumed.

---

## 1. Remote transverse covariance equation

Use the exact transverse shape identity

\[
\boxed{
E_\perp'=2q_\perp D_{\rm rem}+\mathcal R_\perp.
}
\]

Here

\[
q_\perp=\frac12\operatorname{tr}(PQP),
\]

`E_perp` is the transverse trace-free covariance, `D_rem` is the transverse symmetric trace-free **remote affine strain**, and `R_perp` contains axis motion, non-affine remote remainder, local compensation not placed into the affine remote tensor, cutoff/material leakage, source imbalance, and lower-order couplings.

Define on a stage `I_j`

\[
A_{{D,rem},j}=\int_{I_j}|D_{\rm rem}|_Fds,
\qquad
A_{R,j}=\int_{I_j}|\mathcal R_\perp|_Fds.
\]

The active remote-transverse branch supplies its own action floor

\[
\boxed{
A_{{D,rem},j}\ge a_{D,rem}>0.
}
\]

This floor comes from the definition/quantitative threshold of the active remote channel. It is **not** inferred from `log q` without an additional dominance statement.

---

## 2. Full positive-middle strain is a separate specialization

Let `D_full` denote the transverse trace-free part of the **full** strain relative to `xi`. On the aligned positive-middle lane,

\[
s_1<0\le s_2\le s_3,
\qquad
\xi\simeq e_3,
\]

and

\[
\boxed{
|D_{\rm full}|_F
=\frac{s_2-s_1}{\sqrt2}
\ge\frac{s_3}{\sqrt2}.
}
\]

Therefore, if the full positive-middle stretching action satisfies

\[
\int_{I_j}s_3ds\ge a_3,
\]

then

\[
\boxed{
A_{{D,full},j}
\ge\frac{a_3}{\sqrt2}.
}
\]

For an ideal `q=2` flux-preserving **full-strain** stage,

\[
a_3\simeq\log2,
\qquad
A_{{D,full},j}
\gtrsim\frac{\log2}{\sqrt2}.
\]

This numerical value may be used for `D_rem` only on a remote-dominant lane where the near/local transverse component cannot cancel a fixed fraction of the remote action. Otherwise that cancellation is itself a local-compensation/residual branch.

---

## 3. Explicit remote-to-full dominance split

Write

\[
\boxed{
D_{\rm full}=D_{\rm rem}+D_{\rm near}.
}
\]

Fix `0 <= epsilon_D < 1/2`. The remote-dominant lane is

\[
\boxed{
|D_{\rm near}(s)|_F
\le\varepsilon_D|D_{\rm rem}(s)|_F
}
\]

on the action-carrying set.

If this fails on a set carrying a fixed fraction of the remote action, that set is typed as **near/local compensation action** and leaves the pure remote lane.

On the dominance lane,

\[
|D_{\rm full}|
\ge(1-\varepsilon_D)|D_{\rm rem}|.
\]

Moreover the angle between the two transverse trace-free tensor directions satisfies

\[
\boxed{
\angle(\widehat D_{\rm full},\widehat D_{\rm rem})
\le
\delta_D
:=
\arctan\frac{\varepsilon_D}{1-\varepsilon_D}.
}
\]

Thus remote tensor-direction changes transfer quantitatively to the full transverse eigenframe unless the near field pays a comparable cancellation action.

---

## 4. Covariance anisotropy and RMS aspect ratio

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
|E_\perp|_F=\sqrt2\,q_\perp\eta,
}
\]

and the covariance/RMS aspect ratio is

\[
\boxed{
\mathrm{AR}_Q
=\sqrt{\frac{1+\eta}{1-\eta}}.
}
\]

In particular

\[
\mathrm{AR}_Q=2
\quad\Longleftrightarrow\quad
\frac{|E_\perp|_F}{q_\perp}
=\frac{3\sqrt2}{5}
\approx0.8485281374.
\]

---

## 5. Remote coherence-block inequality

Assume on a long pure corridor

\[
\boxed{
q_\perp(s)\ge q_->0,
\qquad
|E_\perp(s)|_F\le E_+<\infty.
}
\]

Whenever `D_rem != 0`, define

\[
\widehat D_{\rm rem}=D_{\rm rem}/|D_{\rm rem}|_F.
\]

Fix

\[
0<\alpha<\frac\pi2.
\]

Partition the corridor into maximal **cap-exit coherence blocks**: on each block the remote direction remains within angular distance `alpha` of its direction at the block entrance, and a completed block ends when that angular displacement reaches `alpha`.

On one such block there is a fixed entrance direction `D_hat_*` with

\[
\langle D_{\rm rem},\widehat D_*\rangle_F
\ge
\cos\alpha\,|D_{\rm rem}|_F.
\]

Integrating the covariance equation gives

\[
2q_-\cos\alpha
\sum_{j\in B}A_{{D,rem},j}
\le
2E_+
+
\sum_{j\in B}A_{R,j}.
\]

Using

\[
A_{{D,rem},j}\ge a_{D,rem},
\]

we obtain

\[
\boxed{
2q_-a_{D,rem}\cos\alpha\,N_B
\le
2E_++R_B.
}
\]

This is the exact multistage deformation-control inequality for the remote transverse channel.

---

## 6. Density of remote direction exits

Suppose over the first `N` stages

\[
\sum_{j=1}^NA_{R,j}
\le r_0N+o(N).
\]

Let `B_N` be the number of completed cap-exit blocks. Summing the preceding inequality gives, whenever

\[
2q_-a_{D,rem}\cos\alpha>r_0,
\]

that

\[
\boxed{
\liminf_{N\to\infty}\frac{B_N}{N}
\ge
\frac{2q_-a_{D,rem}\cos\alpha-r_0}{2E_+}.
}
\]

Therefore bounded transverse covariance plus positive remote `D` action plus subcritical residual action forces remote tensor-direction exits at positive stage density.

This statement does not yet invoke the full-strain projective ledger.

---

## 7. Transfer each remote exit to a full eigenaxis excursion

On the remote-dominant lane, the full and remote transverse tensor directions differ by at most `delta_D` at each block endpoint.

A completed remote block has endpoint separation `alpha`, so the corresponding full transverse tensor direction changes by at least

\[
\boxed{
(\alpha-2\delta_D)_+.
}
\]

For a nondegenerate symmetric trace-free `2 x 2` tensor, the tensor-direction angle is twice the physical transverse eigenaxis angle. Hence every completed block forces full transverse eigenaxis excursion at least

\[
\boxed{
\frac12(\alpha-2\delta_D)_+.
}
\]

If `D_full` becomes degenerate, or if `xi` tilts enough that the transverse plane itself ceases to be coherent, the stage exits to the already typed spectral-degeneracy / tilt / turnover branch.

Consequently the asymptotic full-eigenaxis action per stage obeys

\[
\boxed{
a_\theta(\alpha,\varepsilon_D)
:=
\frac{(\alpha-2\delta_D)_+}{4E_+}
\left(
2q_-a_{D,rem}\cos\alpha-r_0
\right)_+.
}
\]

Now the existing full-strain anti-ribbon ledger may legitimately be used:

\[
\operatorname{TV}(\theta_e)
\le
\int c_V(s)ds.
\]

Thus

\[
\boxed{
\liminf_{N\to\infty}
\frac1N\sum_{j=1}^N\int_{I_j}c_Vds
\ge
a_\theta(\alpha,\varepsilon_D).
}
\]

If remote dominance fails, the cost is instead placed in the near/local compensation branch; it is not silently converted into projective action.

---

## 8. Zero-compensation benchmark

If

\[
\varepsilon_D=0,
\qquad
r_0=0,
\]

then

\[
a_\theta(\alpha,0)
=
\frac{\alpha q_-a_{D,rem}\cos\alpha}{2E_+}.
\]

The maximizing angle solves

\[
\tan\alpha=\frac1\alpha,
\]

with

\[
\alpha_*\approx0.8603335890,
\qquad
\alpha_*\cos\alpha_*\approx0.5610963382.
\]

Therefore

\[
\boxed{
a_\theta^{opt}
\ge
0.2805481691\,
\frac{q_-a_{D,rem}}{E_+}.
}
\]

The further numerical substitution

\[
a_{D,rem}=\frac{\log2}{\sqrt2}
\]

is valid only in the **full-D / exactly remote-dominant benchmark**, not for a generic active remote transverse field.

---

## 9. Full projective action -> frequency tax

The existing full-strain projective-speed estimate is

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

Over many stages, the corrected covariance bridge supplies full projective action at least `N a_theta` on the remote-dominant lane. Hence

\[
\boxed{
\liminf_{N\to\infty}\frac1N
\sum_{j=1}^N\int_{I_j}\lambda ds
\ge
K_P^{-4/3}Z_+^{-2/3}L_+^{-1/3}
(a_\theta-c_0L_+)_+^{4/3}.
}
\]

This tax is available only after the remote-to-full transfer in Section 7 has been paid for.

---

## 10. H1 telescoping closure test

On the bounded pure corridor,

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

an infinite remote-dominant transverse corridor is S-closed whenever

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

A failure of remote dominance is not a survivor of this test; it is a separate local-compensation/residual branch that must be budgeted directly.

---

## 11. Corrected bottleneck

The remote transverse branch is now reduced to the explicit quantities

\[
\boxed{
q_-,\ E_+,\ a_{D,rem},\ r_0,\ \varepsilon_D,\ L_+,\ Z_+,\ B_+.
}
\]

The new obligations are:

1. obtain thick-core covariance bounds `q_-`, `E_+` on the times carrying remote `D` action;
2. quantify the active remote action floor `a_D,rem` from the remote source threshold;
3. either prove a remote-dominance fraction `epsilon_D<1/2`, or charge comparable near/local cancellation as residual/turnover;
4. then use the existing projective-speed/H1 tax.

The positive-middle `log 2 / sqrt(2)` floor belongs to the **full transverse strain** and is only a special case after Item 3, not an unconditional property of `D_rem`.

Status: **THE COVARIANCE DEFORMATION LEMMA SURVIVES THE REMOTE/FULL-STRAIN AUDIT, BUT THE TRANSFER IS CONDITIONAL AND NOW EXPLICIT. A GENERIC ACTIVE REMOTE TRANSVERSE STRAIN CANNOT BE ASSIGNED THE FULL POSITIVE-MIDDLE `log 2 / sqrt(2)` ACTION FLOOR WITHOUT A DOMINANCE/CANCELLATION ARGUMENT. GLOBAL REGULARITY REMAINS UNPROVED.**