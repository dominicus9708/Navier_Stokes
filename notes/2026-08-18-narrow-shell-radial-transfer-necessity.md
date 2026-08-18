# Narrow-shell radial-transfer necessity for critical charge growth

Date: 2026-08-18

Status: **EXACT NARROW-ANNULUS MOMENT IDENTITY. PURE ANGULAR REDISTRIBUTION ON AN EXACT FREQUENCY SPHERE CANNOT GROW ENSTROPHY OR H^(1/2) CHARGE; IN A THIN ANNULUS, NONLINEAR GROWTH OF THESE MOMENTS IS THE SHELL ENERGY FLUX TIMES THE CENTRAL FREQUENCY WEIGHT PLUS AN `O(delta)` RADIAL-SPREAD ERROR. GLOBAL REGULARITY NOT PROVED.**

## 1. Narrow radial shell

Let `P_{K,delta}` be a smooth radial Fourier projection to

\[
A_{K,\delta}
=
\{\xi:(1-\delta)K\le|\xi|\le(1+\delta)K\},
\qquad
0<\delta<1/4.
\]

Write

\[
u_A=P_{K,\delta}u.
\]

Define shell kinetic energy, critical charge, and shell enstrophy

\[
E_A=\frac12\|u_A\|_2^2,
\]

\[
H_A=\frac12\|\Lambda^{1/2}u_A\|_2^2,
\]

\[
Z_A=\frac12\|\Lambda u_A\|_2^2.
\]

On the shell,

\[
\boxed{
H_A
=K E_A+O(\delta K E_A),
}
\]

and

\[
\boxed{
Z_A
=K^2E_A+O(\delta K^2E_A).
}
\]

## 2. Nonlinear shell sources

Let

\[
B(u,u)=\mathbb P(u\cdot\nabla u).
\]

The nonlinear kinetic-energy input to the shell is

\[
\mathcal T_E
=-\langle u_A,P_A B(u,u)\rangle.
\]

The nonlinear critical-charge and enstrophy inputs are

\[
\mathcal T_H
=-\langle\Lambda u_A,P_A B(u,u)\rangle,
\]

\[
\mathcal T_Z
=-\langle\Lambda^2u_A,P_A B(u,u)\rangle.
\]

Subtract the central radial weights:

\[
\boxed{
\mathcal T_H-K\mathcal T_E
=-\langle(\Lambda-K)u_A,P_A B(u,u)\rangle,
}
\]

\[
\boxed{
\mathcal T_Z-K^2\mathcal T_E
=-\langle(\Lambda^2-K^2)u_A,P_A B(u,u)\rangle.
}
\]

Since

\[
\|(\Lambda-K)u_A\|_2
\lesssim\delta K\|u_A\|_2,
\]

and

\[
\|(\Lambda^2-K^2)u_A\|_2
\lesssim\delta K^2\|u_A\|_2,
\]

we obtain

\[
\boxed{
|\mathcal T_H-K\mathcal T_E|
\lesssim
\delta K\|u_A\|_2\|P_AB(u,u)\|_2,
}
\]

and

\[
\boxed{
|\mathcal T_Z-K^2\mathcal T_E|
\lesssim
\delta K^2\|u_A\|_2\|P_AB(u,u)\|_2.
}
\]

## 3. Exact frequency-sphere limit

Formally set `delta=0`, so every participating mode has exactly `|xi|=K`.  Then

\[
H_A=K E_A,
\qquad
Z_A=K^2E_A,
\]

and exactly

\[
\boxed{
\mathcal T_H=K\mathcal T_E,
\qquad
\mathcal T_Z=K^2\mathcal T_E.
}
\]

A closed nonlinear interaction that merely redistributes kinetic energy among modes on the same radius has

\[
\mathcal T_E=0
\]

and therefore also

\[
\boxed{
\mathcal T_H=\mathcal T_Z=0.
}
\]

Thus pure angular redistribution on one Fourier sphere cannot generate either enstrophy or positive `H^(1/2)` critical charge.

## 4. Thin-shell interpretation

For small but nonzero `delta`, an efficient positive source for `H_A` or `Z_A` requires at least one of

\[
\boxed{
\text{nontrivial shell kinetic-energy input }\mathcal T_E
}
\]

or

\[
\boxed{
\text{non-negligible radial spread }\delta
\text{ times a large nonlinear amplitude}.
}
\]

Hence the previous phrase `same-scale high--high interaction` is still too broad.  A source-active interaction must possess a **radial-transfer component**; angular rearrangement alone is insufficient.

## 5. Relation to the helical filter

The helical calculation gives another independent requirement: pure homochiral fixed-shell interactions do not grow the positive `H^(1/2)` charge.  Combining the two statements, an efficient narrow-shell critical source must be both

\[
\boxed{
\text{heterochiral}
}

and

\[
\boxed{
\text{radially transferring / shell-flux active}
}
\]

unless it escapes through a broad radial support or derivative/cross-scale concentration.

Thus the irreducible spectral motif sharpens to

\[
\boxed{
\textbf{heterochiral radial-transfer high--high interaction}.
}
\]

## 6. Why this still does not close

Energy can in principle cross an infinite sequence of higher radial shells while the natural parabolic transfer times shrink like `K^-2`, producing a Zeno-type cascade compatible with the scaling of the equation.  The present identity therefore does not by itself forbid singularity.

Its role is structural: it removes a large class of same-radius angular interactions from the source-active endgame and identifies radial energy transfer as mandatory.

Status: **PURE SAME-RADIUS ANGULAR HIGH--HIGH SOURCE REMOVED / SURVIVING UNIT NETWORK MUST SUPPORT HETEROCHIRAL RADIAL ENERGY TRANSFER OR A BROAD/CROSS-SCALE DERIVATIVE ESCAPE.**