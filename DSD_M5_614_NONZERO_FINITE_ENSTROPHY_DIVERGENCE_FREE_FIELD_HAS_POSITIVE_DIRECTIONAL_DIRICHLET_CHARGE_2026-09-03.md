# DSD M5-614 — A nonzero finite-enstrophy divergence-free field has positive directional Dirichlet charge

Date: 2026-09-03

Status: **DIRECTION-CHANNEL NONDEGENERACY / FOR A SMOOTH NONZERO `L2(R3)` DIVERGENCE-FREE VORTICITY FIELD, THE ORIENTATION DIRICHLET ENERGY `P_dir=int rho^2|nabla xi|^2` CANNOT VANISH / IF IT VANISHED, THE VORTICITY DIRECTION WOULD BE CONSTANT ON EACH CONNECTED POSITIVITY COMPONENT, SO `W=rho e`; DIVERGENCE-FREE THEN MAKES RHO CONSTANT ALONG THE ENTIRE e-DIRECTION / A POSITIVE LINE CANNOT EXIT THE POSITIVITY COMPONENT AT FINITE DISTANCE AND THEREFORE EXTENDS WITH FIXED POSITIVE AMPLITUDE TO INFINITE LENGTH, CONTRADICTING L2 / COMPACTNESS AND THE NONZERO MARK GIVE A UNIFORM POSITIVE P_DIR FLOOR / COMBINED WITH M5-613, EVERY CE-H SURVIVOR MUST CARRY BOTH MAGNITUDE AND DIRECTION GRADIENT CHANNELS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Magnitude-direction decomposition

For

\[
W=\rho\xi,
\qquad
\rho=|W|,
\qquad
|\xi|=1
\]

on the active set,

\[
|\nabla W|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
\]

Define

\[
P_{mag}=\int|\nabla\rho|^2,
\]

and

\[
\boxed{
P_{dir}=\int\rho^2|\nabla\xi|^2.
}
\]

This note concerns the equality case `P_dir=0`.

---

## 2. Vanishing P_dir fixes direction on positivity components

Assume

\[
P_{dir}=0.
\]

Because the integrand is nonnegative,

\[
\rho\nabla\xi=0
\]

almost everywhere.

On every connected open component

\[
\Omega\subset\{\rho>0\},
\]

smoothness gives

\[
\nabla\xi=0.
\]

Hence there exists one constant unit vector `e_Omega` such that

\[
\boxed{
W=\rho e_\Omega
\qquad\text{on }\Omega.
}
\]

---

## 3. Divergence-free condition freezes amplitude along e

Since

\[
\nabla\cdot W=0,
\]

we obtain on `Omega`

\[
0=\nabla\cdot(\rho e_\Omega)
=e_\Omega\cdot\nabla\rho.
\]

Therefore `rho` is constant along every line parallel to `e_Omega` while the line remains inside `Omega`.

Choose `x0 in Omega`. Since `rho(x0)>0`, continuity gives a positive value

\[
\rho(x_0)=a_0>0.
\]

Along

\[
x(t)=x_0+t e_\Omega,
\]

we have

\[
\rho(x(t))=a_0
\]

for every interval on which the line lies in `Omega`.

---

## 4. The positive line cannot terminate at finite distance

Suppose the line exited `Omega` at a finite endpoint `t_*`.

By continuity of the smooth field `W`, a boundary point of the positivity component has

\[
\rho(x(t_*))=0.
\]

But the linewise constancy gives

\[
\rho(x(t))=a_0>0
\]

as `t -> t_*` from inside `Omega`, a contradiction.

Therefore the entire line

\[
\{x_0+t e_\Omega:t\in\mathbb R\}
\]

remains inside `Omega` with amplitude `a0`.

By continuity, a fixed small transverse neighborhood around a finite segment has amplitude bounded below. Repeating along arbitrarily long line segments gives infinite `L2` mass.

Thus

\[
W\notin L^2(\mathbb R^3),
\]

contradicting finite enstrophy.

Hence no nonempty positivity component can exist.

Therefore

\[
\boxed{
P_{dir}=0
\Longrightarrow
W=0.
}
\]

---

## 5. Strict positivity for every nonzero finite-enstrophy field

For every smooth divergence-free

\[
W\in L^2(\mathbb R^3),
\]

we therefore have

\[
\boxed{
W\neq0
\Longrightarrow
P_{dir}>0.
}
\]

This conclusion does not require CE-H; CE-H is where it becomes especially useful because the direction field also obeys the weighted harmonic equation.

---

## 6. Uniform floor on the compact marked hull

Suppose a sequence of marked compact-hull states had

\[
P_{dir}(W_n)\to0.
\]

Use the all-order local smooth compactness and global `H1` tightness to extract a strong limit `W_infty`.

On every compact subset of the nonzero set of `W_infty`, the direction fields converge smoothly and the vanishing directional energies force the limiting direction to be constant on each positivity component.

Hence

\[
P_{dir}(W_\infty)=0.
\]

By the previous argument,

\[
W_\infty=0.
\]

But the persistent carrier mark is stable under the compact extraction and excludes the zero state.

Contradiction.

Therefore there exists

\[
p_{dir,*}>0
\]

with

\[
\boxed{
P_{dir}\ge p_{dir,*}>0
}
\]

throughout the marked compact hard component.

---

## 7. Combination with M5-613

M5-613 gave

\[
P_{mag}\ge p_{mag,*}>0.
\]

M5-614 gives

\[
P_{dir}\ge p_{dir,*}>0.
\]

Thus every nonzero compact CE-H survivor must simultaneously carry

\[
\boxed{
P=P_{mag}+P_{dir},
\qquad
P_{mag}>0,
\qquad
P_{dir}>0.
}
\]

The magnitude/direction split is therefore no longer an either/or alternative on the global CE-H hard core.

Both channels are mandatory.

---

## 8. Consequence for earlier directional firewall

M5-487 correctly showed that

\[
P_{dir}>0
\not\Rightarrow
\int\rho^2|\mathcal D_\xi|^2>0
\]

in general.

There is no conflict: CE-H has zero projected tension by exact strain-diffusion cancellation while maintaining strictly positive orientation Dirichlet energy.

Thus the surviving CE-H structure is precisely a nontrivial weighted-harmonic direction field with positive weighted Dirichlet energy.

---

## 9. Next target

The combination

\[
\nabla\cdot(\rho^2\nabla\xi)
+ho^2|\nabla\xi|^2\xi=0,
\]

\[
P_{dir}\ge p_{dir,*}>0,
\]

and the virial identity

\[
\int(1+2y\cdot\nabla\log\rho)
\rho^2|\nabla\xi|^2=0
\]

now defines a genuinely nonconstant finite-energy weighted harmonic-map branch.

A natural next audit is whether the divergence-free coupling

\[
\xi\cdot\nabla\log\rho=-\nabla\cdot\xi
\]

plus the critical terminal decay is compatible with such a recurrent weighted harmonic map.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
