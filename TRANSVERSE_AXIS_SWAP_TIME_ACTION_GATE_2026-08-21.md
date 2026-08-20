# Transverse Axis-Swap Time / Projective-Action Gate — 2026-08-21

Status: **SMOOTH KINEMATIC LOWER BOUND FOR THE ANTI-RIBBON BRANCH / GLOBAL REGULARITY NOT PROVED.**

This note quantifies the eigenframe reorganization required by `POSITIVE_MIDDLE_TRANSVERSE_RIBBON_GATE_2026-08-21.md`.

## 1. Relative transverse angle equation

Consider a coherent material transverse line and let \(\theta(s)\) be its angle relative to the instantaneous transverse extensional strain eigenvector \(e_2(s)\).

On the positive-middle lane

\[
s_1<0\le s_2,
\]

and define

\[
\gamma=\frac{s_2-s_1}{2}>0.
\]

The two-dimensional velocity-gradient restriction is the sum of

- the symmetric strain with eigenvalues \(s_1,s_2\);
- the local fluid spin about the vortex/\(e_3\) direction;
- the rotation of the instantaneous strain eigenframe itself.

The standard material-line angle equation is

\[
\boxed{
\theta'
=
\varpi
-\theta_e'
-\gamma\sin2\theta,
}
\]

where

\[
\varpi=\frac12\Omega\cdot e_3
\]

in dynamically normalized first-hitting variables, and \(\theta_e\) is the transverse strain-eigenframe angle.

The isotropic scaling drift does not enter this angle equation.

## 2. Positive-middle strain cannot help a transverse-axis swap

Suppose a material direction has to pass from the transverse extensional direction to the transverse compressive direction. In relative coordinates this requires net angle change

\[
\Delta\theta=\frac\pi2.
\]

For

\[
0\le\theta\le\frac\pi2,
\]

the strain term satisfies

\[
-\gamma\sin2\theta\le0.
\]

Thus positive-middle strain itself resists positive rotation from \(e_2\) toward \(e_1\). Consequently the positive variation needed for the crossing obeys

\[
\frac\pi2
\le
\int_I |\varpi|\,ds
+
\int_I|\theta_e'|\,ds.
\]

At first-hitting normalization

\[
\|\Omega\|_\infty\le1,
\]

so

\[
|\varpi|\le\frac12.
\]

Therefore every complete transverse-axis swap satisfies the exact kinematic lower bound

\[
\boxed{
\frac{L_I}{2}
+
\operatorname{TV}_I(\theta_e)
\ge
\frac\pi2.
}
\]

Equivalently,

\[
\boxed{
L_I+2\operatorname{TV}_I(\theta_e)\ge\pi.
}
\]

This uses only the actual smooth material-line equation and the first-hitting vorticity cap.

## 3. Pure-spin benchmark

If the strain eigenframe is fixed,

\[
\operatorname{TV}(\theta_e)=0,
\]

then a transverse-axis swap requires

\[
\boxed{L_I\ge\pi.}
\]

This is much stronger than the mere area-contraction action \(\int s_3ds\gtrsim\log q\). It states that the bounded normalized fluid spin cannot rotate a material line through 90 degrees arbitrarily quickly against the positive-middle alignment tendency.

## 4. Eigenframe rotation is projective strain-shape action

For

\[
S=m\,\mathrm{diag}(-2,1-x,1+x),
\]

a transverse rotation \(\theta_e\) about \(e_3\) changes the normalized strain tensor by conjugation.

At fixed spectrum,

\[
\left|
\frac{d}{d\theta_e}
\frac{S}{|S|_F}
\right|_F
=
\frac{\sqrt2|s_2-s_1|}{|S|_F}
=
\frac{3-x}{\sqrt{3+x^2}}.
\]

On the remaining middle-zero-side spectral interval

\[
x\in[x_*,1],
\qquad
x_*=\frac{3(\sqrt3-1)}4,
\]

we have

\[
\boxed{
\frac{3-x}{\sqrt{3+x^2}}\ge1.
}
\]

The spectral-variation component is Frobenius-orthogonal to the pure rotational component. Hence the full normalized strain-shape path length \(\mathscr A_{shape}\) satisfies

\[
\boxed{
\mathscr A_{shape}
\ge
\operatorname{TV}(\theta_e)
}
\]

on this spectral lane.

Combining with the angle gate,

\[
\boxed{
\frac{L_I}{2}
+
\mathscr A_{shape}
\ge
\frac\pi2.
}
\]

## 5. Projective-speed consequence

Suppose the stage remains on the pure projective branch so that all nonprojective shape-speed channels are subdominant and the existing projective-speed estimate applies:

\[
\mathscr A_{shape}
\le
C_VL_I.
\]

Then

\[
\frac{L_I}{2}+C_VL_I\ge\frac\pi2,
\]

hence

\[
\boxed{
L_I
\ge
L_{swap}
:=
\frac{\pi}{1+2C_V}.
}
\]

Therefore if the actual smooth moving-variance ceiling obeys

\[
\boxed{
L_{var}<\frac{\pi}{1+2C_V},
}
\]

then the pure coherent positive-middle anti-ribbon/projective-swap branch is **S-closed**.

If the total strain-shape motion exceeds the `P_V` speed model because advection, derivative escape, non-affine deformation, or spatial eigenaxis bending dominates, the stage is routed to the existing \(H/T\) channels rather than being counted as a pure `P_V` survivor.

## 6. Relation to q=2 thick-core replacement

For \(q=2\), the previous ribbon gate showed that a coherent affine cross-section with no transverse-axis reorganization leaves at least

\[
\frac12-\frac1\pi
\approx0.1816901138
\]

of the next round thick disk uncovered by the old material image.

Thus a stage avoiding this fixed-fraction transverse replacement must perform the anti-ribbon reorganization. On the pure projective lane, that reorganization now has the explicit stage-length floor \(L_{swap}\).

## 7. Current branch structure

The analytic-scale thick positive-middle stage is reduced to

\[
\boxed{
\begin{aligned}
&\text{robust material-flux change}
&&\to L_I\ge L_{\Phi,min},\\
&\text{coherent anti-ribbon projective swap}
&&\to L_I\ge \pi/(1+2C_V),\\
&\text{fixed-fraction/non-affine transverse replacement}
&&\to T,\\
&\text{large derivative/eigenaxis-bending speed}
&&\to H/T.
\end{aligned}
}
\]

Both of the first two branches now have literal finite-smooth-stage minimum durations which can be compared to the already explicit moving-variance maximum duration.

Status: **A TRANSVERSE-AXIS SWAP AGAINST POSITIVE-MIDDLE STRAIN COSTS `L/2 + projective eigenframe action >= pi/2`. ON A PURE PROJECTIVE STAGE THIS GIVES THE NEW S-LEVEL DURATION FLOOR `L >= pi/(1+2 C_V)`.**