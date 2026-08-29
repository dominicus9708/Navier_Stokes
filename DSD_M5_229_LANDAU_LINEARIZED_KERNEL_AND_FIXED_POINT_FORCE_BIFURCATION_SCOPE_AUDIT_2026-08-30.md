# DSD M5-229 — Landau Linearized Kernel and Fixed-Point-Force Bifurcation Scope Audit

Date: 2026-08-30

Parent: `DSD_M5_228_SAME_POINT_FORCE_DILATE_DIFFERENCE_RELATIVE_STATIONARY_ENERGY_GATE_2026-08-30.md`

Status: **LITERATURE/SPECTRAL SCOPE AUDIT / AXISYMMETRIC DSS LINEARIZATION AROUND LANDAU HAS STRONG PARTIAL NONDEGENERACY: SWIRL ZERO/PURE-IMAGINARY MODES ARE EXCLUDED ANALYTICALLY AND THE RADIAL-FOURIER-ZERO STREAM KERNEL IS ONLY THE LANDAU-FAMILY PARAMETER DIRECTION / FIXING THE POINT-FORCE VECTOR REMOVES THAT FAMILY DIRECTION / NONZERO STREAM FOURIER MODES HAVE NUMERICAL NO-BIFURCATION EVIDENCE RATHER THAN A GENERAL ANALYTIC THEOREM / NONE OF THESE RESULTS COVERS AN ARBITRARY LARGE NONAXISYMMETRIC FIXED-FORCE STATIONARY TAIL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Current stationary spectral target

M5-228 reduces the large stationary endpoint to a nonzero critical dilation zero-mode

\[
\mathcal H_T
:=T+x\cdot\nabla T
\]

solving

\[
\boxed{
-\nu\Delta\mathcal H_T
+(T\cdot\nabla)\mathcal H_T
+(\mathcal H_T\cdot\nabla)T
+\nabla\pi_H
=0.
}
\]

The background itself solves

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P
=b\delta_0
\]

with one fixed vector `b`, and all dilates solve the same point-force problem.

The question is whether known Landau linearized nondegeneracy eliminates such a mode.

---

## 2. Kwon--Tsai setting

Kwon--Tsai study possible bifurcation from a Landau solution within the class of **axisymmetric discretely self-similar stationary solutions** satisfying the critical pointwise bound.

They rewrite radial scaling by a periodic log-radius variable and decompose the linearization into Fourier modes of that variable.

The perturbation separates into

- a stream-function sector;
- a swirl sector.

This is much narrower than the present arbitrary W1 stationary endpoint, but it is directly relevant to the possible dilation zero-mode near a Landau state.

---

## 3. Analytic swirl nondegeneracy

For the swirl operator, Kwon--Tsai prove analytically that for every Landau parameter `a>1` and every positive DSS log-frequency parameter, the relevant Fourier-mode operator has

\[
\boxed{
\text{no zero eigenvalue and no purely imaginary eigenvalue}.
}
\]

Thus inclusion of an axisymmetric swirl component does not create the missing bifurcation direction.

This is a genuine theorem, not numerical evidence.

Consequently a local axisymmetric fixed-force dilation kernel cannot hide purely in the swirl sector.

---

## 4. Zero radial-Fourier stream kernel

For the stream operator at radial Fourier mode `n=0`, Kwon--Tsai prove that the kernel is one dimensional:

\[
\boxed{
\ker\mathfrak L_0
=\operatorname{span}\{\partial_a\Psi^a\}.
}
\]

Here `Psi^a` is the Landau stream function and `a` is the parameter of the Landau family.

Thus in this restricted sector there is no additional zero mode beyond movement along the existing Landau family.

---

## 5. Fixed point force removes the Landau-family direction

Landau solutions are uniquely parameterized by their point-force vector:

\[
\boxed{
b\longmapsto U^b}
\]

within the smooth degree-`-1` homogeneous class.

The tangent

\[
\partial_aU^a
\]

moves along this family and therefore changes the associated point-force parameter rather than preserving one fixed `b` fiber.

The current M5-227/M5-228 endpoint is constrained by

\[
\boxed{b\text{ fixed under every dilation}.}
\]

Hence the Landau-family parameter mode is not an admissible fixed-force nonhomogeneity direction.

At the linearized source level, varying the Landau parameter produces a corresponding variation of the coefficient of `delta_0`, whereas the dilation mode `mathcal H_T` derived in M5-228 has **zero source variation**.

Thus the one analytically known `n=0` stream kernel does not match the present fixed-force kernel.

---

## 6. Nonzero radial Fourier stream modes are not fully closed analytically

For the remaining stream Fourier modes, Kwon--Tsai numerically study the eigenvalue problem.

Their computations provide evidence that no bifurcation occurs in the investigated Landau parameter range, in particular for the reported `a>=1.01` regime.

However the paper explicitly presents this part as numerical evidence/conjectural no-bifurcation information rather than a complete analytic theorem for all stream modes.

Therefore

\[
\boxed{
\text{Kwon--Tsai numerics}
\not\Rightarrow
\ker\mathcal L_{U^b}^{stat}=\{\text{family modes}\}
}
\]

in the full function class.

---

## 7. Nonaxisymmetric modes remain outside the theorem

The Kwon--Tsai bifurcation problem is axisymmetric.

The present stationary W1 tail is not known to be axisymmetric.

Hence even a complete axisymmetric no-kernel theorem would still leave possible nonaxisymmetric critical kernel directions.

Similarly, asymptotic stability results for Landau solutions under `L2` perturbations concern the time-dependent Navier--Stokes evolution and do not by themselves prove stationary fixed-force kernel triviality in the scale-critical `1/r` class.

---

## 8. Why the current survivor is actually farther from the perturbative Landau problem

M5-221 already proves that if a stationary W1 tail enters the small critical-amplitude exterior regime where Landau asymptotics are available, minimality forces the entire tail hull to collapse to the Landau fixed point.

Therefore the surviving branch is

\[
\boxed{
\text{large critical amplitude and not captured by the perturbative Landau asymptotic basin}.
}
\]

A local spectral theorem around Landau, even if strengthened, would need an additional bridge showing that the large recurrent stationary tail enters a controlled neighborhood of a Landau solution.

No such bridge is currently available.

---

## 9. Spectral interpretation of fixed-force minimal recurrence

For a nonhomogeneous stationary tail, the exact dilation family

\[
T_h=D_hT
\]

is a continuum of solutions to the same point-force equation.

Its infinitesimal tangent is

\[
-\frac12\mathcal H_T.
\]

Thus a surviving stationary minimal hull would exhibit an actual **fixed-force neutral scaling orbit**.

This is stronger than a hypothetical isolated kernel eigenfunction: the zero mode integrates globally to a complete compact dilation orbit of nonlinear stationary solutions.

Therefore the correct large-data rigidity target is

\[
\boxed{
\text{exclude nontrivial fixed-force scaling orbits of stationary }O(1/r)\text{ solutions},
}
\]

not merely compute the Landau linearized spectrum.

---

## 10. DSD verdict

### GREEN imported partial results

- Landau homogeneous profiles are the only smooth degree-`-1` profiles.
- axisymmetric swirl modes do not create zero/pure-imaginary bifurcation modes in the Kwon--Tsai setting.
- the `n=0` axisymmetric stream kernel is only the Landau-family parameter direction.

### GREEN internal fixed-force refinement

- the Landau-family parameter direction changes the point-force parameter and is therefore excluded from the fixed-`b` tangent problem.

### YELLOW/OPEN

- nonzero stream Fourier modes beyond numerical evidence;
- nonaxisymmetric critical modes;
- arbitrary-large backgrounds far from the Landau perturbative regime.

---

## 11. Updated stationary frontier

The remaining stationary endpoint cannot use the only analytically known Landau-family zero mode.

It must instead realize a genuinely new fixed-force critical neutral direction:

\[
\boxed{
\mathcal H_T\ne0,
\qquad
\mathcal L_T^{stat}\mathcal H_T=0,
\qquad
\delta b=0,
\qquad
\underline{\mathscr R}_H>0,
}
\]

on a large-amplitude, potentially nonaxisymmetric background.

This is considerably narrower than the original stationary-tail escape.

---

## 12. Next target

The next internal audit should use the fact that the zero mode **integrates to an exact nonlinear dilation orbit with the same point force**.

A promising quantity is the difference between two finite dilates

\[
W_h=D_hT-T
\]

combined with minimal recurrence and the relative stationary energy form from M5-228.

The goal is to determine whether repeated finite-dilate separation forces a negative direction of the Hardy-critical quadratic form on a positive logarithmic density of scales, thereby converting nonhomogeneity into a genuine large-data instability certificate.

No such sign conclusion is assumed yet.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]