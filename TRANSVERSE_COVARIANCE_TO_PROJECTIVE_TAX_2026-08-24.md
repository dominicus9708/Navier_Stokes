# Transverse Covariance -> Projective Tax — 2026-08-24

Status: **MULTISTAGE DEFORMATION-CONTROL BRIDGE, NOW ALIGNMENT-FREE FOR THE FULL/EFFECTIVE STRAIN / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `TRANSVERSE_REMOTE_STRAIN_COVARIANCE_GATE_2026-08-24.md`,
- `POSITIVE_MIDDLE_TRANSVERSE_INTERLACING_GENERALIZATION_2026-08-24.md`,
- `RECURRENT_MAX_BETCHOV_POSITIVE_MIDDLE_ROUTING_2026-08-24.md`, and
- `SMOOTH_PROJECTIVE_ACTION_VISCOUS_TAX_CLOSURE_2026-08-21.md`.

The main correction relative to the earlier version is conceptual. The positive-middle transverse action floor is a property of the **full/effective strain seen by the core**, not of a chosen remote piece. A remote/near split remains useful diagnostically, but exact remote-near cancellation means that the remote field is not an effective core obstruction and should not be charged artificially.

---

## 1. Exact transverse covariance equation

For a localized enstrophy packet let

\[
Q=m^{-1}\int (y-c)\otimes(y-c)\,\rho(y,s)\,dy,
\]

\[
P=I-\xi\otimes\xi,
\qquad
Q_\perp=PQP=q_\perp P+E_\perp,
\]

where

\[
q_\perp=\frac12\operatorname{tr}(PQP),
\qquad
\operatorname{tr}_{\xi^\perp}E_\perp=0.
\]

Choose the affine representation actually used in the packet covariance ledger and write its symmetric part relative to `xi` as

\[
\Sigma_{eff}
=a\,\xi\otimes\xi
+\xi\otimes b+b\otimes\xi
-\frac a2P
+D_{eff},
\]

with

\[
D_{eff}=PD_{eff}P,
\qquad
\operatorname{tr}D_{eff}=0.
\]

Everything not represented by this effective affine tensor is retained in the exact residual. Then the transverse trace-free covariance equation is

\[
\boxed{
E_\perp'
=2q_\perp D_{eff}+\mathcal R_\perp.
}
\]

The bulk viscous term is isotropic and therefore disappears exactly after transverse trace-free projection:

\[
\boxed{
\operatorname{dev}_\perp(2\nu I)=0.
}
\]

Thus an effective transverse strain cannot be hidden by bulk isotropic diffusion.

---

## 2. Alignment-free positive-middle transverse action floor

Let `S` be the full physical/Leray strain at a source-active point, with ordered eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3,
\]

and let `xi` be the actual vorticity direction. Define

\[
\gamma=\xi^TS\xi.
\]

Compress `S` to the plane `xi^perp` and denote the two eigenvalues by

\[
\mu_1\le\mu_2.
\]

Trace-freeness gives

\[
\mu_1+\mu_2=-\gamma.
\]

Cauchy interlacing gives

\[
\lambda_1\le\mu_1\le\lambda_2\le\mu_2\le\lambda_3.
\]

Hence on the positive-middle sector

\[
\boxed{\lambda_2\ge0}
\]

we have

\[
\mu_2\ge0
\]

and therefore

\[
\boxed{
\mu_2-\mu_1
=\gamma+2\mu_2
\ge\gamma.
}
\]

Writing the transverse compression as

\[
PSP|_{\xi^\perp}
=-\frac\gamma2I_{\xi^\perp}+D_{full},
\]

we obtain

\[
\boxed{
|D_{full}|_F
=\frac{\mu_2-\mu_1}{\sqrt2}
\ge\frac\gamma{\sqrt2}.
}
\]

No assumption such as `xi ~= e3` appears anywhere in this estimate.

---

## 3. Source-active cell gives an explicit full-D floor

At a source-active point or cell let

\[
q=W^TSW=|W|^2\gamma.
\]

Suppose

\[
q\ge q_0>0,
\qquad
|W|\le M_+.
\]

Then

\[
\gamma\ge\frac{q_0}{M_+^2}.
\]

On the positive-middle part of the source-active cell,

\[
\boxed{
|D_{full}|_F
\ge
D_0
:=
\frac{q_0}{\sqrt2\,M_+^2}>0.
}
\]

Thus the full/effective transverse action floor is obtained directly from source activity and positive-middle strain. It is no longer tied to an eigenvector-alignment assumption or to the idealized `log 2 / sqrt(2)` benchmark.

If the packet affine representative does not capture this full local transverse strain to a fixed fraction, the discrepancy is by definition non-affine/spatially varying core action and is retained in `R_perp`; it is not silently discarded.

---

## 4. How the recurrent route supplies source-active positive-middle times

The recurrent maximum-vorticity ledger gives

\[
D^+\log M(s)\le G(s)-1,
\]

with

\[
G(s)=
\sup_{\operatorname{Argmax}|W|}
\left[
\xi^TS\xi-\nu|\nabla\xi|^2
\right].
\]

Every nonzero periodic orbit, and every genuine nonzero recurrent-return orbit, therefore satisfies the mean action floor

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^TG(s)\,ds
\ge1.
}
\]

If `G<=B_+` and `0<g_0<1`, the high-source set has positive lower time density; in the periodic case,

\[
\boxed{
d_G(g_0)
\ge
\frac{1-g_0}{B_+-g_0}.}
\]

On such times the maximum-vorticity core has strictly positive stretching. The existing source-active Betchov dichotomy says that a residual-quiet source-active cell must contain a fixed positive-middle population; otherwise it pays the already typed local Betchov buffer/Hessian/residual cost.

Consequently a nonzero recurrent **pure** lane carries positive-density full transverse action satisfying the pointwise floor in Section 3.

---

## 5. Thick covariance and bounded-shape corridor

Assume on the action-carrying recurrent packet that

\[
\boxed{
q_\perp(s)\ge q_->0,
\qquad
|E_\perp(s)|_F\le E_+<\infty.
}
\]

For an exact periodic nonzero orbit these bounds are natural consequences of uniform smoothness, nonzero vorticity amplitude, and no-`T` bounded similarity-center recurrence once the packet is chosen continuously around the recurrent core.

For a general aperiodic recurrent orbit they are a branch condition on the recurrent compact core. Their failure is a thickness/shape turnover event rather than a quiet survivor.

Let the full/effective transverse action satisfy

\[
\liminf_{T\to\infty}
\frac1T\int_0^T|D_{eff}(s)|_Fds
\ge a_D>0.
\]

The recurrent source-active/interlacing route supplies such an `a_D` on the residual-quiet lane, with a symbolic lower bound of the form

\[
\boxed{
a_D
\gtrsim
 d_{pm}\,
\frac{q_0}{\sqrt2M_+^2},}
\]

where `d_pm>0` is the lower time density of source-active positive-middle core events. The exact geometric fraction is kept symbolic because it depends on the quantitative threshold used to declare the complementary Betchov mismatch branch non-quiet.

---

## 6. Continuous-time coherence-block inequality

Whenever `D_eff != 0`, set

\[
\widehat D=D_{eff}/|D_{eff}|_F.
\]

Fix

\[
0<\alpha<\frac\pi2.
\]

Partition a long time interval into maximal cap-exit coherence blocks on which `D_hat` stays within angle `alpha` of its entrance direction. On one such block `B`, with entrance tensor `D_hat_*`,

\[
\langle D_{eff},\widehat D_*\rangle_F
\ge
\cos\alpha\,|D_{eff}|_F.
\]

Pairing

\[
E_\perp'=2q_\perp D_{eff}+\mathcal R_\perp
\]

with `D_hat_*` and integrating gives

\[
\boxed{
2q_-\cos\alpha
\int_B|D_{eff}|_Fds
\le
2E_+
+
\int_B|\mathcal R_\perp|_Fds.
}
\]

Suppose over `[0,T]`

\[
\int_0^T|\mathcal R_\perp|_Fds
\le r_0T+o(T).
\]

If

\[
2q_-a_D\cos\alpha>r_0,
\]

then the number `N_B(T)` of completed coherence blocks satisfies

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_B(T)}T
\ge
\frac{2q_-a_D\cos\alpha-r_0}{2E_+}.
}
\]

Thus a bounded-shape, thick, residual-quiet recurrent core must turn the transverse strain direction at positive rate in Leray time.

---

## 7. Convert tensor-direction exits to projective eigenaxis action

A nondegenerate transverse symmetric trace-free tensor has the form

\[
D=d
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix}.
\]

Hence tensor direction moves at twice the physical transverse eigenaxis angle. Every completed `alpha` block therefore pays at least

\[
\frac\alpha2
\]

of transverse eigenaxis variation, unless `D` crosses degeneracy. Degeneracy removes the active transverse channel and is itself a typed spectral exit.

Consequently the asymptotic eigenaxis-action density satisfies

\[
\boxed{
\liminf_{T\to\infty}
\frac{\operatorname{TV}(\theta_e;[0,T])}{T}
\ge
\frac{\alpha}{4E_+}
\left(
2q_-a_D\cos\alpha-r_0
\right)_+.
}
\]

Define

\[
\boxed{
a_\theta(\alpha)
:=
\frac{\alpha}{4E_+}
\left(
2q_-a_D\cos\alpha-r_0
\right)_+.}
\]

The existing full-strain projective-speed ledger gives

\[
\operatorname{TV}(\theta_e)
\le
\int c_V(s)ds,
\]

so

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^Tc_V(s)ds
\ge a_\theta(\alpha).
}
\]

This is the alignment-free recurrent covariance-to-projective bridge.

---

## 8. Zero-residual optimized benchmark

If `r_0=0`, the lower bound is proportional to

\[
\alpha\cos\alpha.
\]

The optimum solves

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
\frac{q_-a_D}{E_+}.}
\]

Unlike the older version, `a_D` here is the actual recurrent full/effective transverse action density. It is supplied by source-active positive-middle events through the interlacing lemma, not by inserting `log 2 / sqrt(2)` for a generic remote field.

---

## 9. Projective action -> frequency tax

The existing projective-speed estimate is

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

On a recurrent corridor with

\[
Z\le Z_+,
\]

an average projective-action density `a_theta` gives a positive frequency tax whenever

\[
\boxed{a_\theta>c_0.}
\]

Indeed Jensen/Holder gives schematically

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^T\lambda(s)ds
\ge
K_P^{-4/3}Z_+^{-2/3}
(a_\theta-c_0)_+^{4/3}.}
\]

For finite first-hitting stages the corresponding formula contains the stage-length factor already recorded in `SMOOTH_PROJECTIVE_ACTION_VISCOUS_TAX_CLOSURE_2026-08-21.md`; the present form is the continuous Leray-time density analogue.

---

## 10. H1 recurrent closure target

The finite-stage H1 ledger remains

\[
\frac12\log\frac{P_{j+1}}{P_j}
+\frac34\log q
+\nu\int_{I_j}\frac HPds
=
\int_{I_j}\frac NPds.
\]

The alignment-free recurrent route now supplies a projective/frequency tax on a positive-density subset without introducing a new eigenvector-alignment assumption.

A full numerical recurrent contradiction would require quantitative lower bounds for

\[
q_-,\quad a_D,
\]

and an upper residual density `r0` strong enough to make

\[
a_\theta>c_0
\]

or otherwise exceed the production margin in the H1 ledger.

The currently available Taylor endpoint constants and the crude source-active continuity fraction do not yet justify such a universal numerical inequality. Therefore no unsupported closure radius is claimed here.

---

## 11. Remote/full split retained only as a diagnostic subledger

If one specifically wishes to ask which spatial region produces `D_eff`, write

\[
D_{full}=D_{rem}+D_{near}.
\]

Three cases are then possible:

1. `D_rem` dominates: the remote source genuinely drives the effective transverse action;
2. `D_near` dominates: the action is local and belongs to the local/projective route;
3. `D_rem ~= -D_near`: the effective transverse action is small, so the remote field is not an independent core obstruction.

Only case 1 needs a remote-to-full transfer estimate. Exact cancellation is not declared expensive by fiat.

This diagnostic split no longer appears in the core covariance/projective theorem itself.

---

## 12. Updated bottleneck

The recurrent pure-lane reduction is now

\[
\boxed{
\begin{aligned}
\text{nonzero recurrent source-active core}
\Longrightarrow\;&
\text{positive-middle source action}\\
&\lor\ T/H/\text{Betchov residual}\\
\Longrightarrow\;&
\text{positive-density }D_{eff}\text{ action}\\
&\lor\ T/H/\text{non-affine residual}\\
\Longrightarrow\;&
\text{shape growth}\\
&\lor\text{projective eigenaxis action}\\
&\lor\ T/H/\text{residual}.
\end{aligned}
}
\]

The vorticity/strain alignment assumption has disappeared from this chain.

What remains is quantitative rather than classificatory: either obtain enough recurrent action density to beat the explicit projective-speed baseline and H1 production margin, or show that the residual/shape/turnover complements cannot recur indefinitely.

Status: **THE TRANSVERSE COVARIANCE/PROJECTIVE BRIDGE IS NOW FORMULATED FOR THE FULL/EFFECTIVE CORE STRAIN AND USES AN ALIGNMENT-FREE CAUCHY-INTERLACING ACTION FLOOR. SOURCE-ACTIVE POSITIVE-MIDDLE RECURRENCE FORCES POSITIVE-DENSITY TRANSVERSE ACTION; A THICK BOUNDED-SHAPE RESIDUAL-QUIET ORBIT MUST CONVERT THAT ACTION INTO PROJECTIVE EIGENAXIS TURNOVER. THE REMAINING GAP IS THE SIZE OF THE ACTION DENSITY, NOT VORTICITY/STRAIN ALIGNMENT. GLOBAL REGULARITY REMAINS UNPROVED.**