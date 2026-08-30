# DSD M5-339 — Same-Sector Positive-Middle/Compressive Axis / Quiescent-Affine No-Go

Date: 2026-08-30

Status: **THE EXACT STATIONARY AFFINE ANTI-MODEL EXISTS ONLY ON THE NEUTRAL-MIDDLE (`lambda_2=0`) GEOMETRY / TWO-POSITIVE/ONE-NEGATIVE SAME-SECTOR ATOM+PRODUCTIVE STRAIN CANNOT REMAIN A QUIESCENT CONSTANT-GRADIENT ROTOR / IT MUST PAY VORTICITY AMPLIFICATION, PROJECTIVE CHANGE, DIFFUSION, OR STRAIN/PRESSURE REFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Same-sector hard branch

After M5-334--338, the remaining local atom geometry not already routed through a middle-eigenvalue sign/interface event is the sector

\[
\lambda_2\ge\delta|S|>0,
\]

where

- `lambda_2^+` supplies productive strain,
- the unique compressive eigen-direction `e_3` supplies the atom-selected negative spectral part `S_-`.

All three strain eigenvalues have critical size in this sector.

## 2. Oseen production selects the compressive axis

Let

\[
A_H=(\nabla H)(\nabla H)^T\ge0.
\]

In the strain eigenframe,

\[
- S:A_H
=|\lambda_3|a_3-\lambda_1a_1-\lambda_2a_2,
\]

where

\[
a_i=e_i^TA_He_i\ge0.
\]

Positive atom Oseen production therefore requires a nontrivial fraction of the Oseen-gradient quadratic form to occupy the compressive `e_3` direction.

This is an auxiliary orientation condition, not yet a contradiction.

## 3. Vorticity production selects the extensional plane

For the physical vorticity direction

\[
\xi=\sum_i\xi_ie_i,
\]

\[
\frac{\omega\cdot S\omega}{|\omega|^2}
=\lambda_1\xi_1^2+\lambda_2\xi_2^2+\lambda_3\xi_3^2.
\]

Positive enstrophy production in a sector where the eigenvalues are comparable requires a fixed amount of vorticity direction in the extensional plane `span(e_1,e_2)` unless compensated elsewhere.

Thus the same-sector atom geometry naturally carries a dual-axis organization:

\[
\boxed{
\text{Oseen gradient biased toward }e_3,
\qquad
\text{physical vorticity biased away from }e_3.
}
\]

## 4. Constant-gradient affine test

Consider an affine velocity

\[
u(x,t)=M(t)x,
\qquad
M=S+W,
\qquad
\operatorname{tr}M=0.
\]

For a stationary constant-gradient solution, viscosity vanishes and the pressure Hessian is symmetric. Hence the antisymmetric part of

\[
M^2+\nabla^2p=0
\]

requires

\[
\boxed{SW+WS=0.}
\]

Suppose the vorticity/rotation axis is `e_2`. Then `W` acts in the `e_1-e_3` plane. In the diagonal strain frame,

\[
SW+WS=(\lambda_1+\lambda_3)W.
\]

Trace-freeness gives

\[
\lambda_1+\lambda_3=-\lambda_2.
\]

Therefore

\[
\boxed{
SW+WS=-\lambda_2W.
}
\]

If

\[
\lambda_2>0,
\qquad W\ne0,
\]

then

\[
SW+WS\ne0.
\]

Hence no stationary constant-gradient affine rotor of this type exists.

The exact affine anti-model from the previous audits occurs precisely at

\[
\boxed{\lambda_2=0.}
\]

## 5. Dynamic affine equation

For a time-dependent affine solution, the antisymmetric part of the matrix equation gives

\[
\boxed{
W'+SW+WS=0.
}
\]

When the rotation axis remains `e_2`, this becomes

\[
W'=\lambda_2W.
\]

Equivalently the vorticity amplitude obeys the affine version of the exact vorticity law

\[
\boxed{
\frac d{dt}|\omega|=\lambda_2|\omega|.
}
\]

Thus a coherent positive-middle affine-like core is not quiescent: it amplifies vorticity on the critical clock.

## 6. Same-sector dynamic fork

Therefore the same-sector branch has the exact qualitative alternatives

\[
\boxed{
C_{same-sector}
\Longrightarrow
\begin{cases}
H_{stretch}:&\text{persistent positive-middle vorticity amplification},\\
H_{proj}:&\text{vorticity/eigenframe axis change},\\
H_{diff}:&\text{viscous vorticity-direction/amplitude correction},\\
H_p/T:&\text{strain/pressure reformation or spatial replacement}.
\end{cases}
}
\]

Unlike the neutral-planar branch, there is no zero-cost stationary affine fixed point inside this sector.

## 7. What is and is not closed

This no-go removes only the **quiescent affine escape**.
It does not exclude a genuinely dynamic restricted-Euler-like positive-middle core; such a core is precisely a plausible local blow-up mechanism and must be controlled by viscosity, pressure, or global organization.

The next target is therefore the persistent `H_stretch` lane and its balance against diffusion/pressure-induced strain reformation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
