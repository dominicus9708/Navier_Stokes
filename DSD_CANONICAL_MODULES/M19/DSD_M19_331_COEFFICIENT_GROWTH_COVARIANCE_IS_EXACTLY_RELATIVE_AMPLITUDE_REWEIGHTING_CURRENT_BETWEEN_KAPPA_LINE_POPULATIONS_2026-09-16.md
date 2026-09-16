# M19-331 — Coefficient-growth covariance is exactly relative-amplitude reweighting current between kappa-line populations

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / EXACT SELECTION-REWEIGHTING IDENTITY / JOINT AMPLITUDE-COEFFICIENT FACTOR / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from CE-H amplitude dynamics

On the physical exact CE-H branch,

\[
D_t\rho=(\sigma+\kappa)\rho.
\]

Set

\[
g:=\sigma+\kappa=D_t\log\rho.
\]

For the material packet probability from M19-328,

\[
d\pi_t=rac{\chi\rho^2}{M(t)}dx,
\qquad
M(t)=\int\chi\rho^2dx,
\]

we have

\[
\frac12\frac{M'}M
=
\langle g\rangle_\pi.
\]

## 2. Relative amplitude coordinate

Define

\[
\boxed{
b(x,t)
:=
\log\rho(x,t)-\frac12\log M(t).
}
\]

Because \(M\) depends only on time,

\[
D_t b
=
g-rac12\frac{M'}M.
\]

Therefore

\[
\boxed{
D_t b
=
g-\langle g\rangle_\pi.
}
\]

Thus \(b\) measures a material line's logarithmic amplitude relative to the packet-wide RMS growth.

## 3. Exact covariance identity

Let

\[
z:=\log|\kappa|,
\qquad
h:=\langle z\rangle_\pi.
\]

Then

\[
\begin{aligned}
\operatorname{Cov}_\pi(g,z)
&=
\langle(g-\langle g\rangle_\pi)(z-h)\rangle_\pi\\
&=
\boxed{
\langle D_t b\,(z-h)\rangle_\pi.
}
\end{aligned}
\]

Hence the signed coefficient-growth covariance is exactly the correlation between relative material amplitude change and coefficient phase.

## 4. Probability-reweighting law

Because the material volume measure is incompressible while the packet probability uses weight \(\rho^2\),

\[
\partial_t d\pi_t
\quad\text{along material labels}
\]

satisfies

\[
\boxed{
D_t(d\pi_t)
=2(g-\langle g\rangle_\pi)d\pi_t
=2D_tb\,d\pi_t.
}
\]

Therefore regions with

\[
D_tb>0
\]

gain probability weight, while regions with

\[
D_tb<0
\]

lose probability weight.

The covariance

\[
C_{gz}
=
\langle D_tb(z-h)\rangle_\pi
\]

is exactly the signed coefficient bias of that reweighting current.

## 5. Selection-versus-material-evolution decomposition

For any material observable \(f\),

\[
\boxed{
\frac d{dt}\langle f\rangle_\pi
=
\langle D_tf\rangle_\pi
+2\operatorname{Cov}_\pi(g,f).
}
\]

Apply this to \(f=z\):

\[
\boxed{
h'
=
\langle D_tz\rangle_\pi
+2C_{gz}.
}
\]

Thus

- \(\langle D_tz\rangle_\pi\) is genuine material coefficient evolution;
- \(2C_{gz}\) is change of the observed mean coefficient phase caused purely by differential amplitude reweighting of existing material populations.

This separates material migration from population selection exactly.

## 6. Relation to M17-394

M17-394 gives

\[
D_tz
=
L_\rho z
+|\nabla z|^2
+\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\]

After packet averaging, the material-evolution part contains the positive log-diffusion and typed forcing/interface terms.

M19-331 shows that the remaining covariance part is not another derivative source. It is a **selection/reweighting current among coefficient-labeled material populations**.

## 7. Sign interpretation

If

\[
C_{gz}<0,
\]

then, on average, higher-than-mean \(z=\log|\kappa|\) populations lose relative amplitude weight while lower-than-mean coefficient populations gain it, or equivalently the reweighting current is biased toward smaller \(|\kappa|\).

If

\[
C_{gz}>0,
\]

the amplitude competition favors larger-\(|\kappa|\) populations.

On the negative-kappa branch, M19-329 identifies one intrinsic reason for negative bias: the coefficient reaction term itself contributes negative self-covariance.

## 8. Recurrent-factor interpretation

A compact recurrent state can sustain nonzero reweighting currents indefinitely while the packet probability distribution returns in law. Therefore

\[
\boxed{
C_{gz}\ne0
\not\Rightarrow
\text{monotone exhaustion}.
}
\]

The coefficient-growth covariance is structurally a population-current/hysteresis quantity.

A closure theorem would need to show that this current is incompatible with one of:

- exact CE-H line constancy;
- finite flux-line population architecture;
- coefficient-scale ancestry;
- normalized entropy return;
- or a finite signed budget.

## 9. Updated spatial branch architecture

The current spatial CE-H chain is

\[
\boxed{
\begin{aligned}
\text{spectral variance}
&\to
\text{kappa line segregation}\\
&\to
\text{log-kappa diffusion or zero/interface/geometry exit}\\
&\to
\text{critical derivative source balance}\\
&\qquad\oplus
\text{relative-amplitude reweighting current}.
\end{aligned}
}
\]

Thus the remaining genuinely dynamical degree of freedom is not an unidentified local norm. It is the joint amplitude--coefficient population current.

## 10. Conclusion

The signed covariance of M19-328--330 has an exact population-dynamical meaning:

\[
\boxed{
\operatorname{Cov}_\pi(\sigma+\kappa,\log|\kappa|)
=
\langle D_tb(\log|\kappa|-\langle\log|\kappa|\rangle)\rangle_\pi.
}
\]

It measures differential material amplitude selection between coefficient-labeled vortex-line populations.

\[
\boxed{
\text{M19-331 COMPLETE; NEXT TARGET: TEST WHETHER FINITE FLUX-LINE POPULATION CONSERVATION CONSTRAINS THIS REWEIGHTING CURRENT BEYOND ORDINARY RECURRENT HYSTERESIS.}
}
\]
