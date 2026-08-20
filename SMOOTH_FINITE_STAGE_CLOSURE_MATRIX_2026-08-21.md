# Smooth Finite-Stage Closure Matrix — 2026-08-21

Status: **MAINLINE SMOOTH FIRST-HITTING CLOSURE MATRIX / GLOBAL REGULARITY NOT PROVED.**

This note consolidates the current proof attempt after moving the mainline back to actual smooth finite first-hitting stages. Limit/ancient arguments are not used in the closure tests below.

## 1. One geometric stage

Consider

\[
M_j\to qM_j,
\qquad q>1,
\]

with dynamically normalized stage length

\[
L_j=|I_j|.
\]

The candidate survivor is the analytic-scale, vorticity/derivative-tight, positive-middle, low-turnover projective lane.

## 2. Smooth moving-variance upper time

For a persistent low-shell-flux core of normalized radius \(R_V\), the exact moving-variance estimate gives

\[
\boxed{
L_j\le L_{var}
:=
\frac{C_{var}R_V^2}{(1-\eta)\nu V_-}
\left(
\frac14(\log q)V_+
+F_0+
\frac12\kappa_V
\right).
}
\]

Write this schematically as

\[
L_{var}=\Pi_V\frac{R_V^2}{\nu}.
\]

Every pure tight-core branch must fit below this ceiling. Failure of the hypotheses is already a shell/material-turnover or local-energy branch.

## 3. Cross-order production minimum time

The smooth multistage tightrope ledger yields, on a uniform frequency corridor,

\[
(X_+-\nu G_-)L_+
\ge
\frac12\log q.
\]

Thus a persistent cross-order projective stage requires

\[
\boxed{
L_j\ge L_{cross}
:=
\frac{\log q}{2(X_+-\nu G_-)}
}
\]

whenever \(X_+>\nu G_-\). If \(X_+\le\nu G_-\), the lane is S-closed immediately.

## 4. Record/deformation minimum time

The strain amplitude ceiling from first-hitting analyticity/tightness is

\[
B_+
\le
C_B2^{1/5}M_0
\left[
\frac{4\pi}{3(1-\varepsilon_Q)}
\right]^{2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5},
\]

where

\[
C_B=\frac{15\sqrt2}{8}\pi^{-2/5}.
\]

A coherent flux-preserving material cross-section must contract its area by the geometric scale factor \(q^{-1}\). Since

\[
\int_I\|\Sigma\|_\infty ds
\le B_+L_j,
\]

while an area contraction by \(q^{-1}\) needs strain action at least \(\log q\), the coherent deformation branch requires

\[
\boxed{
L_j\ge L_{def}
:=
\frac{\log q}{B_+}.
}
\]

This is the same scale as the independently derived record-growth common-core radius floor.

## 5. Robust material-flux-change minimum time

For the endpoint Taylor cylinder with

\[
r_0=K_{2,+}^{-1/2},
\]

define

\[
Z_-=
\frac{64\sqrt2\pi}{105}K_{2,+}^{-3/2},
\]

\[
Z_+=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
\]

If a fraction \(\beta\) of the material disk family changes a fraction \(\eta\) of its natural signed flux under deformation \(M_F\le K\), the flux/enstrophy gate gives

\[
L_j\ge L_{\Phi,min},
\]

with

\[
A=Z_+/\sqrt2,
\]

\[
B=\frac12(Z_+-Z_-)-\frac14Z_-\log q,
\]

\[
D=
\frac{9\pi}{2048\sqrt q}
\frac{\beta\eta^2r_0^5}{\nu K^2},
\]

and

\[
\boxed{
L_{\Phi,min}
=
\frac{-B+\sqrt{B^2+4AD}}{2A}.
}
\]

Thus robust viscous flux reorganization cannot occur on a stage shorter than \(L_{\Phi,min}\).

## 6. Anti-ribbon transverse-swap minimum time

Positive-middle coherent stretching ribbonizes a transverse material disk. Avoiding fixed-axis ribbonization while keeping the core thick requires transverse-axis reorganization.

The exact material-line angle gate is

\[
\frac{L_j}{2}
+\operatorname{TV}(\theta_e)
\ge
\frac\pi2.
\]

On the pure projective branch, if normalized strain-shape action has speed

\[
\mathscr A_{shape}\le C_VL_j
\]

and \(\mathscr A_{shape}\ge\operatorname{TV}(\theta_e)\), then

\[
\boxed{
L_j\ge L_{swap}
:=
\frac{\pi}{1+2C_V}.
}
\]

If the swap is supplied by local residual, viscous derivative action, or a harmonic parent pressure tail instead, those terms are routed by the exact strain-eigenframe equation into residual/H/finite parent escalation.

## 7. Pure P_V S-closure test

A smooth finite stage that simultaneously avoids

- material/shell turnover;
- derivative escape;
- spectral-gap collapse;
- large local non-affine residual;
- unresolved parent-pressure escalation;

must satisfy the upper time ceiling and whichever lower-time mechanism supplies the scale transition.

In particular, any pure coherent projective stage must have

\[
\boxed{
L_{var}
\ge
\min\{L_{cross},L_{def},L_{\Phi,min},L_{swap}\}
}
\]

for at least one allowed continuation mode, while a mode-by-mode closure is obtained whenever

\[
L_{var}<L_{mode}.
\]

If all admissible continuation modes satisfy

\[
\boxed{
L_{var}
<
\min\{L_{cross},L_{def},L_{\Phi,min},L_{swap}\},
}
\]

then the entire pure analytic-scale positive-middle P_V stage is S-closed.

## 8. What remains outside the matrix

The closure matrix deliberately does not call the following branches solved:

1. fixed-fraction material/transverse turnover;
2. large derivative or eigenaxis-bending action;
3. spectral transition out of the positive-middle lane;
4. local residual/non-affine shape action;
5. parent-pressure action before the finite escalation gate resolves it.

Those are typed exits from the pure smooth P_V corridor, not hidden assumptions.

## 9. Principal next numerical target

The strongest remaining unknowns in the pure corridor are now constants rather than mechanisms:

\[
C_V,
\quad
\Pi_V,
\quad
M_*,
\quad
\text{and quantitative residual/turnover thresholds}.
\]

The next useful calculation is to replace the abstract projective-speed constant \(C_V\) by an explicit smooth first-hitting bound, or to show that any attempt to exceed a chosen explicit \(C_V\) necessarily activates the already typed derivative/residual/pressure branches.

Status: **THE PURE SMOOTH POSITIVE-MIDDLE PROJECTIVE SURVIVOR IS NOW CONFINED BETWEEN ONE EXPLICIT STAGE-LENGTH CEILING AND FOUR INDEPENDENT MECHANISM-SPECIFIC STAGE-LENGTH FLOORS. CLOSURE IS REDUCED TO QUANTITATIVE CONSTANT COMPARISON OR ESCAPE INTO THE ALREADY TYPED H/T/RESIDUAL BRANCHES.**