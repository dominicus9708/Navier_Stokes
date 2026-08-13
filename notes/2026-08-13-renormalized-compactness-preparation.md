# Renormalized dangerous-window compactness preparation

Date: 2026-08-13

Status: **CONDITIONAL COMPACTNESS PREPARATION / NO RIGIDITY THEOREM CLAIMED**.

The natural-window renormalization converts each dangerous checkpoint to a fixed unit-scale Navier--Stokes window.  The next question is not yet whether the limit is regular, but whether a bounded sequence of such normalized windows has a subsequence with enough strong convergence to preserve the DSD danger channels.

This note states the sufficient compactness block conservatively.  If any required normalized bound fails, that failure is itself retained as a typed concentration branch rather than hidden inside the compactness argument.

---

## 1. Fixed normalized cylinder

After natural rescaling, work on a fixed interior cylinder

\[
Q_R=B_R\times(-T_0,0),
\qquad R>1,
\qquad T_0>0.
\]

Use the normalized velocity, pressure, and vorticity

\[
U_j,\qquad P_j,\qquad \Omega_j=\nabla\times U_j.
\]

The amplification-time noncollapse lemma supplies a common positive time length on the branch where the tracked normalized I/V/deformation channels remain bounded.

---

## 2. Velocity compactness block

Assume on every smaller interior cylinder `Q_R` the uniform bounds

\[
\boxed{
\sup_j\left[
\|U_j\|_{L_t^\infty L_x^2(Q_R)}
+\|\nabla U_j\|_{L_{t,x}^2(Q_R)}
+\|P_j-(P_j)_{B_R}\|_{L_{t,x}^{3/2}(Q_R)}
\right]<\infty.
}
\]

The energy bounds give the standard interpolation

\[
U_j\in L_t^4L_x^3(Q_R)
\]

uniformly.  Consequently

\[
U_j\otimes U_j\in L_t^2L_x^{3/2}(Q_R).
\]

Using the Navier--Stokes equation in distributions on a strictly smaller interior ball, the time derivative is bounded in a negative Sobolev space such as

\[
\boxed{
\partial_sU_j
\text{ bounded in }
L_t^{3/2}W_x^{-1,3/2}.
}
\]

The diffusion and quadratic terms have at least this local negative-space regularity; the normalized pressure term is included explicitly in the compactness block.

Since

\[
H^1(B_R)\Subset L^2(B_R)
\hookrightarrow W^{-1,3/2}(B_R),
\]

an Aubin--Lions--Simon compactness argument gives, after passing to a subsequence and shrinking the spatial cylinder slightly,

\[
\boxed{
U_j\to U_\infty
\quad\text{strongly in }L^2_{\rm loc}(Q_R).
}
\]

This is a conditional standard compactness step, not a new theorem.

---

## 3. Why velocity compactness alone is insufficient

The normalization

\[
|\Omega_j(0,0)|=1
\]

is a pointwise statement.  Strong `L^2` convergence of the velocities does **not** by itself preserve this pointwise vorticity normalization.

Similarly, a sequence of vorticity fields may retain large instantaneous maxima while converging weakly to a trivial or less singular limit through spatial oscillation/concentration.

Therefore the DSD route must not claim nontriviality of the limiting vorticity from the single center value.

---

## 4. Vorticity compactness block

To preserve directional/occupancy channels, require a stronger normalized vorticity block on an interior cylinder:

\[
\boxed{
\sup_j\left[
\|\Omega_j\|_{L_t^\infty L_x^2}
+\|\nabla\Omega_j\|_{L_{t,x}^2}
\right]<\infty.
}
\]

From the vorticity equation

\[
\partial_s\Omega_j
+(U_j\cdot\nabla)\Omega_j
=(\Omega_j\cdot\nabla)U_j
+\nu\Delta\Omega_j,
\]

and the local `H^1` bounds, one obtains a time-derivative bound in a sufficiently weak negative Sobolev space, schematically

\[
\boxed{
\partial_s\Omega_j
\text{ bounded in }
L_t^1W_x^{-1,3/2}
+L_t^2H_x^{-1}.
}
\]

A Simon-type compactness argument then yields, after another subsequence,

\[
\boxed{
\Omega_j\to\Omega_\infty
\quad\text{strongly in }L^2_{\rm loc}(Q_R).
}
\]

A bounded normalized V2 channel

\[
\int_{Q_R}|\Delta\Omega_j|^2
\]

provides an even stronger derivative reserve, but is not declared automatic.

---

## 5. Nontriviality must be a spacetime channel

A pointwise maximum at the terminal time is not a robust compactness invariant.  Instead introduce a fixed normalized spacetime nontriviality channel, for example

\[
\boxed{
\mathcal N_{b,\delta}
=
\int_{-\delta}^{0}
\int_{B_1}
|\Omega_j|^2\,dy\,ds.
}
\]

A stronger occupancy-resolved version is

\[
\boxed{
\mathcal O_{b,\delta}
=
\int_{-\delta}^{0}
\left|
\{y\in B_1:|\Omega_j(y,s)|\ge b\}
\right|ds.
}
\]

If, along the compact subsequence,

\[
\mathcal N_{b,\delta}\ge c_0>0
\]

uniformly, strong local `L^2` convergence of vorticity gives

\[
\boxed{
\Omega_\infty\not\equiv0.
}
\]

For threshold-set occupancy itself, strong `L^2` convergence gives convergence in measure and permits stable lower-threshold statements after replacing `b` by `b-\varepsilon`; exact threshold equality sets must not be assumed harmless without a measure-zero condition.

---

## 6. New dichotomy: persistent core versus temporal concentration

The final-time dangerous core may fail to persist through any fixed normalized time slab.  Therefore retain two branches:

### P — persistent normalized danger

There exist fixed

\[
\delta>0,
\qquad c_0>0
\]

such that

\[
\mathcal N_{b,\delta}\ge c_0
\]

along a subsequence.

This branch is compatible with a nontrivial compactness limit.

### T — temporal concentration

For every fixed `delta>0`, the spacetime vorticity occupancy/nontriviality channel tends to zero even though the terminal checkpoint has normalized maximum one.

Then the danger collapses into an increasingly thin time layer near the checkpoint.  This is **not** treated as compactness success; it becomes a separate fast temporal concentration branch to be intersected with the amplification-time I/V costs and the derivative hierarchy.

Thus

\[
\boxed{
\text{nontrivial compact limit}
\quad\text{or}\quad
\text{typed temporal concentration}.
}
\]

---

## 7. Projective channels under strong vorticity compactness

If the vorticity converges strongly in `L^2` and its local enstrophy does not vanish, then the smoothed covariance numerators and denominators at any fixed positive normalized scale pass to the limit after standard truncation/localization arguments.

Hence the following fixed-scale DSD channels are natural candidates to survive compactness:

\[
E_r,
\qquad
C_r,
\qquad
J_r,
\qquad
\Pi_r,
\]

provided the denominator `E_r` stays uniformly away from zero on the region where the normalized channel is evaluated.

The singular `r\to0` limit is **not** passed automatically; compactness is taken first at fixed normalized scale.

---

## 8. Suitable-limit target

Under the velocity/pressure compactness block and the usual local-energy bounds, the target is a nontrivial limiting suitable weak solution on a fixed cylinder (or, after extending the checkpoint sequence backward, an ancient/local-ancient limit).

This note does not assert that all the hypotheses are available from the current route.  Instead it makes the proof logic explicit:

\[
\boxed{
\begin{array}{c}
\text{normalized channel sequence}\\
\downarrow\\
\text{some compactness channel unbounded}
\quad\text{or}\quad
\text{strong local subsequence}
\end{array}}
\]

and then

\[
\boxed{
\text{strong subsequence}
\Rightarrow
\text{nontrivial persistent limit}
\quad\text{or}\quad
\text{temporal concentration branch}.
}
\]

---

## 9. Rigidity target after compactness

If a nontrivial unit-scale limit exists and all current regularity gates are still avoided, it must inherit an unusually restrictive simultaneous saturation pattern:

1. non-sparse intense vorticity;
2. failure of projective Campanato coherence;
3. critical projective Poincare/palinstrophy cost but no strict dissipation gain;
4. I-lane directional strain and/or V-lane viscous rewrite at critical strength;
5. off-axis self-stretching strong enough to match projective viscosity;
6. derivative covariance chain remaining active without entering the high-order anisotropic regularity gate.

The new proof-producing question is therefore a **rigidity/gap problem on one normalized cylinder**, not a search over all of `R^3`:

\[
\boxed{
\text{Does any nontrivial normalized Navier--Stokes state satisfy all residual saturation requirements simultaneously?}
}
\]

A quantitative negative answer would supply the strict gain missing from all previous critical power-counting arguments.

Status: **OPEN CONDITIONAL COMPACTNESS + SIMULTANEOUS-SATURATION RIGIDITY**.
