# DSD M5-573 — Stationary Terminal Branch / Stress-Defect Split

Date: 2026-09-02

Status: **THE CONTINUOUSLY HOMOGENEOUS STATIONARY SUBBRANCH REDUCES TO LANDAU-TYPE TERMINAL DEFECTS. LOG-RADIUS-DEPENDENT STATIONARY CRITICAL PROFILES REMAIN A SEPARATE OPEN CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-572

The first terminal jet is

\[
u(x,s)
=
r^{-1}A(q,\omega)
+(-s)r^{-3}C(q,\omega)+\cdots,
\]

with

\[
C=\mathcal R_{stat}[A,P].
\]

The stationary terminal branch is

\[
\boxed{C=0.}
\]

Then the leading critical field

\[
v(x)=r^{-1}A(\log r,\omega)
\]

solves the stationary incompressible Navier-Stokes equations on the exterior asymptotic domain.

This note separates the continuously homogeneous case from genuinely log-radius-dependent stationary profiles.

---

## 2. Stationary momentum-stress flux

For a stationary unforced smooth solution, define the momentum-stress tensor with the sign convention

\[
\mathbb T
:=
\nabla v+(\nabla v)^T
-v\otimes v-pI.
\]

The stationary equation implies

\[
\nabla\cdot\mathbb T=0
\]

away from singularities.

Hence the sphere flux

\[
\boxed{
\mathcal F(R)
:=
\int_{|x|=R}\mathbb T n\,dS
}
\]

is independent of \(R\) on any smooth exterior annulus:

\[
\boxed{
\mathcal F(R_2)=\mathcal F(R_1).
}
\]

For a critical \(1/r\) field,

\[
\mathbb T=O(r^{-2}),
\]

so the flux is scale-critical:

\[
\mathcal F(R)=O(1).
\]

Thus a stationary critical terminal trace carries a radius-independent vector defect candidate

\[
\boxed{\kappa:=\mathcal F.}
\]

---

## 3. Continuously homogeneous subbranch

Assume in addition

\[
\boxed{\partial_qA=0.}
\]

Then

\[
v(\lambda x)=\lambda^{-1}v(x)
\]

for every \(\lambda>0\): the stationary critical field is exactly \((-1)\)-homogeneous.

Known classification results state that smooth \((-1)\)-homogeneous stationary Navier-Stokes solutions in \(\mathbb R^3\setminus\{0\}\) are Landau solutions.

Therefore

\[
\boxed{
C=0,
\quad \partial_qA=0
\Longrightarrow
v=U_{Landau,\kappa}.
}
\]

The zero parameter gives the trivial solution, while nontrivial Landau solutions correspond distributionally to a point-force defect at the origin:

\[
\boxed{
-\Delta v+(v\cdot\nabla)v+\nabla p
=\kappa\,\delta_0.
}
\]

Equivalently, \(\kappa\) is encoded by the constant momentum-stress flux through spheres.

Thus a nontrivial continuously homogeneous stationary terminal survivor requires

\[
\boxed{\kappa\neq0.}
\]

---

## 4. Why the Landau defect is not yet a contradiction

The ancient Navier-Stokes solution is unforced and smooth for every \(s<0\).

However, the terminal trace at \(s=0\) is allowed to be singular at the blow-up core. Passing to the singular terminal limit can in principle create a distributional defect supported at that point.

Therefore one may **not** infer

\[
\text{unforced for }s<0
\Longrightarrow
\kappa=0\text{ at }s=0
\]

without a separate terminal momentum-defect compactness theorem.

The correct remaining question on this subbranch is

\[
\boxed{
\text{Can a smooth unforced Type-I ancient solution generate a nonzero Landau stress defect in its terminal trace?}
}
\]

This is a sharper question than the previous generic \(1/r\)-tail problem.

---

## 5. Log-radius-dependent stationary branch

If

\[
C=0,
\qquad
\partial_qA\neq0,
\]

then the terminal trace is stationary in physical time but not continuously homogeneous.

Examples of possible symmetry classes include:

- discretely scale-periodic/log-periodic profiles;
- aperiodic recurrent log-radius stationary profiles.

For every such stationary exterior profile, the stress flux still obeys

\[
\boxed{
\mathcal F(R)\equiv\kappa.
}
\]

Thus log-radius oscillation cannot make the total stationary momentum defect vary from shell to shell.

However, general classification of all smooth scale-critical stationary fields with

\[
|v(x)|\lesssim |x|^{-1}
\]

and nontrivial log-radius dependence is not available at the level needed here.

In particular, numerical/no-bifurcation evidence near Landau solutions in restricted axisymmetric DSS classes must not be promoted to a general theorem.

---

## 6. Stationary-branch refinement

The correct split is

\[
\boxed{
E_{stat}^{terminal}
=
E_{Landau\ defect}^{hom}
\lor
E_{stationary\ log}^{nonhom}.
}
\]

where

\[
E_{Landau\ defect}^{hom}:
\quad
\partial_qA=0,
\quad
\kappa\neq0,
\]

and

\[
E_{stationary\ log}^{nonhom}:
\quad
\partial_qA\neq0,
\quad
\mathcal F(R)\equiv\kappa.
\]

The first branch is classified but not yet dynamically excluded; the second remains a classification problem.

---

## 7. Literature firewall

- V. Sverak, *On Landau's solutions of the Navier-Stokes equations*: classification of smooth \((-1)\)-homogeneous stationary solutions in \(\mathbb R^3\setminus\{0\}\) as Landau solutions.
- Kwon-Tsai, *On bifurcation of self-similar solutions of the stationary Navier-Stokes equations*: any smooth continuously self-similar stationary solution is Landau; restricted axisymmetric DSS bifurcation analysis does not provide a general nonexistence theorem.
- Modern isolated-singularity literature confirms that nontrivial Landau solutions correspond to a Dirac-force/stress-flux defect at the isolated singularity.

Status: **THE HOMOGENEOUS C=0 SURVIVOR IS NO LONGER AN UNCLASSIFIED PROFILE: IT IS A LANDAU-TYPE TERMINAL POINT-DEFECT BRANCH. THE REQUIRED NEW CLOSURE IS A THEOREM EXCLUDING CREATION OF THAT DEFECT FROM A SMOOTH UNFORCED TYPE-I ANCIENT FLOW. GLOBAL REGULARITY REMAINS UNPROVED.**