# Shape-repeating octave reproduction: conditional bridge to asymptotically discrete self-similarity

Date: 2026-08-18

Status: **CONDITIONAL EXTERNAL-THEOREM BRIDGE. IF A REPRODUCING HIGH-FREQUENCY GENEALOGY IS PRECOMPACT AFTER PARABOLIC RESCALING, HAS A CONVERGENT DISCRETE SCALE/TIME SHIFT, AND RETAINS THE REQUIRED GLOBAL L3 TIGHTNESS, THEN A SHAPE-REPEATING SUBSEQUENCE FALLS INTO THE LOCALLY ASYMPTOTICALLY DISCRETELY SELF-SIMILAR SCENARIO EXCLUDED BY CHAE UNDER THE STATED PROFILE HYPOTHESES. FAILURE IS TYPED AS SPATIAL NON-TIGHTNESS, DERIVATIVE NONCOMPACTNESS, OR PERSISTENT SHAPE MODULATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Parabolic renormalization along a genealogy

Let `K_j -> infinity` be active physical frequencies, `t_j -> T*`, and `x_j` the corresponding material/packet centers.  Define the natural rescaling

\[
\boxed{
u_j(y,s)
=K_j^{-1}u\left(
x_j+\frac{y}{K_j},
t_j+\frac{s}{K_j^2}
\right).
}
\]

The viscosity is unchanged by this Navier--Stokes scaling.

A bounded unit-cell lane is designed precisely so that, after translation/rotation as needed, the `u_j` have nontrivial order-one local structure.

## 2. Shape-repeating hypothesis

Suppose along a subsequence:

1. the scale ratios converge,
   \[
   K_{j+1}/K_j\to\lambda>1;
   \]
2. the normalized time gaps and center displacements converge;
3. `u_j` is precompact in a local topology strong enough to pass Navier--Stokes, e.g. `C^2_loc` on compact subsets of the preterminal spacetime region;
4. the rescaled critical `L3` mass is tight enough that the limiting profile satisfies the global integrability condition required by the external self-similar nonexistence theorem;
5. the parent-child renormalized shape mismatch tends to zero.

Then the limiting reproduction law is a discrete parabolic recurrence in the renormalized variables.  In logarithmic self-similar time, the limit becomes a time-periodic / discretely self-similar backward profile.

## 3. External nonexistence anchor

D. Chae, *Remarks on the asymptotically discretely self-similar solutions of the Navier-Stokes and the Euler equations*, arXiv:1306.0305, proves nonexistence of locally asymptotically discretely self-similar blow-up for 3D Navier--Stokes under a time-periodic profile in

\[
C^1(\mathbb R;L^3(\mathbb R^3)\cap C^2(\mathbb R^3)).
\]

Therefore a shape-repeating genealogy satisfying the hypotheses above is not an independent surviving singular mechanism.

## 4. Exhaustive complement of this bridge

The bridge does **not** apply automatically.  Its failure is informative and already belongs to typed channels.

### Critical spatial non-tightness

If the rescaled `L3` mass escapes to larger and larger spatial radii, this is the packet-multiplicity / mesoscopic-cluster / enlarged coherent branch.

### Derivative noncompactness

If `C2_loc` precompactness fails, higher derivative / analytic-radius / V2 concentration is active.

### Persistent shape modulation

If consecutive renormalized cells do not approach one common reproduction shape, the parent-child projective/helical/residual configuration changes by an order-one amount across scales.  This is the scale-modulation branch targeted by the criticalized dynamic-radius projective forcing inequality.

### Nonconvergent scale-time geometry

If scale ratios, normalized time gaps, or centers fail to stabilize, the genealogy itself has a scale/time modulation that must be retained in the moving-band forcing rather than silently identified with a fixed point.

## 5. Claim boundary

This note does not prove that every bounded unit-cell cascade has a discretely self-similar subsequence.  Precompactness plus recurrence is not automatic, and the global `L3` profile hypothesis is substantial.

The result is a **conditional gate**:

\[
\boxed{
\text{shape repetition + tight compactness}
\Rightarrow
\text{known asymptotic-DSS nonexistence},
}
\]

while every failure is explicitly returned to one of the active noncompact/modulation channels.

Status: **SIMPLE RENORMALIZATION FIXED-POINT REPRODUCTION CONDITIONALLY EXCLUDED / SURVIVOR MUST MODULATE, DECOMPACTIFY, OR CONCENTRATE DERIVATIVES / GLOBAL REGULARITY NOT PROVED.**