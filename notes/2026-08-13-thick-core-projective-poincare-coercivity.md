# Thick-core projective Poincare coercivity

Date: 2026-08-13

Status: **DERIVED LOCAL GEOMETRIC COERCIVITY / OPEN ADJOINT-WINDOW SOURCE DOMINANCE**.

This note quantifies the cost of the residual `thick + projectively rough` intense-vorticity branch.

If vorticity magnitude is uniformly comparable to its local maximum on a ball, then a non-small projective covariance defect forces direction-gradient palinstrophy at the same scale.

## 1. Intense ball

Let

\[
B=B_r(x_0)
\]

and assume

\[
\boxed{
aW\le|\omega(x)|\le W\quad\text{for }x\in B}
\]

with `0<a<1`.

Write

\[
\omega=\rho\xi,
\qquad
|\xi|=1.
\]

Define

\[
E_B=\int_B\rho^2dx,
\]

\[
C_B
=\frac{\int_B\rho^2\xi\otimes\xi dx}{E_B},
\]

\[
J_B=1-\operatorname{tr}(C_B^2),
\qquad
D_B=E_BJ_B.
\]

## 2. Compare weighted and unweighted projective pair variance

Define

\[
V_B
=\frac1{|B|^2}
\iint_{B\times B}
[1-(\xi(x)\cdot\xi(y))^2]dxdy.
\]

The weighted covariance identity gives

\[
J_B
=\frac1{E_B^2}
\iint_{B\times B}
\rho(x)^2\rho(y)^2
[1-(\xi(x)\cdot\xi(y))^2]dxdy.
\]

Using

\[
a^2W^2|B|\le E_B\le W^2|B|,
\]

we obtain both comparisons

\[
\boxed{
a^4V_B\le J_B\le a^{-4}V_B.}
\]

In particular,

\[
\boxed{V_B\ge a^4J_B.}
\]

## 3. Projector variance

Let

\[
P_\xi=\xi\otimes\xi.
\]

Then

\[
\|P_\xi(x)-P_\xi(y)\|_F^2
=2[1-(\xi(x)\cdot\xi(y))^2].
\]

The standard pair-variance identity yields

\[
\boxed{
V_B
=
\fint_B
\|P_\xi-(P_\xi)_B\|_F^2dx.
}
\]

## 4. Poincare inequality forces direction-gradient energy

The ball Poincare inequality gives

\[
\fint_B
\|P_\xi-(P_\xi)_B\|_F^2
\le
C_Pr^2
\fint_B|\nabla P_\xi|_F^2.
\]

Since `|xi|=1`,

\[
|\nabla P_\xi|_F^2
=2|\nabla\xi|^2.
\]

Therefore

\[
\fint_B|\nabla\xi|^2
\ge
c\frac{V_B}{r^2}
\ge
c a^4\frac{J_B}{r^2}.
\]

Multiply by the lower intensity bound:

\[
\begin{aligned}
\int_B\rho^2|\nabla\xi|^2dx
&\ge
 a^2W^2|B|
\fint_B|\nabla\xi|^2\\
&\ge
c a^6 W^2|B|
\frac{J_B}{r^2}.
\end{aligned}
\]

Because

\[
E_B\le W^2|B|,
\]

we finally obtain

\[
\boxed{
\int_B|\omega|^2|\nabla\xi|^2dx
\ge
c a^6\frac{E_BJ_B}{r^2}
=
c a^6\frac{D_B}{r^2}.
}
\]

## 5. Direction-gradient term is part of palinstrophy

Where `omega != 0`,

\[
|\nabla\omega|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
\]

Hence the local palinstrophy satisfies

\[
\boxed{
P_B
:=\int_B|\nabla\omega|^2dx
\ge
c a^6\frac{E_BJ_B}{r^2}.
}
\]

Thus a thick intense core cannot keep a non-small projective defect without paying a scale-critical gradient cost.

## 6. Consequence for projective viscous dissipation

The energy-weighted projective equation dissipates schematically through

\[
\nu P_BJ_B^2.
\]

The thick-core lower bound implies

\[
\boxed{
\nu P_BJ_B^2
\ge
c\nu a^6
\frac{E_BJ_B^3}{r^2}.
}
\]

Thus the rough branch has a cubic projective penalty at fixed local energy and physical scale.

This does not by itself dominate the nonlinear stretching source; that comparison remains the active problem.

## 7. Natural vorticity scale

At the geometric natural scale

\[
r\sim W^{-1/2},
\]

the direction-gradient lower bound becomes

\[
\boxed{
P_B
\gtrsim
 a^6E_BWJ_B.
}
\]

If the ball is genuinely intense throughout, then

\[
E_B\sim W^2r^3\sim W^{1/2}
\]

up to intensity/volume constants, and hence

\[
P_B\gtrsim W^{3/2}J_B.
\]

This is exactly the critical Navier--Stokes scaling; no supercritical gain appears automatically.

The absence of an automatic gain is itself important: a proof must exploit either further projective depletion, spatial sparseness, or a dynamical incompatibility among the equality/saturation regimes.

## 8. Relation to Campanato coherence

The two local branches now have complementary estimates.

### Coherent branch

If

\[
J_r\lesssim r^{2\alpha}
\]

uniformly on a thick intense core, the projective Campanato bridge upgrades the covariance to pointwise projective Holder coherence.

### Rough branch

If that decay fails, then `J_r/r^(2 alpha)` remains large on dangerous scales. The present Poincare estimate converts the non-small projective defect into direction-gradient palinstrophy.

Thus

\[
\boxed{
\text{projective decay}
\Rightarrow
\text{coherence},
}

while

\[
\boxed{
\text{projective non-decay}
\Rightarrow
\text{direction-gradient cost}.
}

## 9. Remaining local source comparison

The adjoint-window projective inequality is

\[
\dot D_\phi
+\frac{3\nu}{4}P_\phi J_\phi^2
\le
2\sqrt5\sqrt{D_\phi}F_\phi.
\]

The present estimate supplies a lower bound on the left side in a thick intense region.

The missing step is to prove that the same projective roughness/occupancy information also prevents

\[
F_\phi
=\left(\int\phi|S\omega|^2\right)^{1/2}
\]

from growing fast enough to dominate the enhanced viscous term on every dangerous adjoint window.

Status: **OPEN THICK-ROUGH SOURCE/DISSIPATION COMPARISON**.
