# Exact total-vorticity polar bridge to the Cauchy I/V split

Date: 2026-08-14

Status: **EXACT POINTWISE AMPLITUDE/DIRECTION DECOMPOSITION / RESIDUAL STRETCH-CONVERSION CHANNELS ROUTED TO INVISCID CHANGE OR VISCOUS REWRITE**.

Let `omega` solve incompressible Navier--Stokes vorticity dynamics

\[
D_t\omega=S\omega+\nu\Delta\omega.
\]

At points where `omega!=0`, write

\[
\omega=M\xi,
\qquad
M=|\omega|,
\qquad
|\xi|=1.
\]

Taking the component parallel to `xi` gives

\[
\boxed{
D_t\log M
=\xi^TS\xi
+\nu\frac{\xi\cdot\Delta\omega}{M}.
}
\]

Taking the perpendicular component gives

\[
\boxed{
D_t\xi
=(I-\xi\otimes\xi)S\xi
+\nu\frac{(I-\xi\otimes\xi)\Delta\omega}{M}.
}
\]

Define

\[
q_\xi=\xi^TS\xi,
\qquad
\chi_\xi=|(I-\xi\otimes\xi)S\xi|.
\]

Then directional stretching satisfies

\[
|q_\xi|
\le
|D_t\log M|
+\nu\frac{|\Delta\omega|}{M},
\]

while axis conversion satisfies

\[
\boxed{
\chi_\xi
\le
|D_t\xi|
+\nu\frac{|\Delta\omega|}{M}.
}
\]

Conversely, whenever either strain channel is large, at least one of two mechanisms must be large:

1. actual inviscid/material amplitude or direction change;
2. viscous second-vorticity-derivative rewrite.

Thus the geometric decomposition

\[
|S\xi|^2=q_\xi^2+\chi_\xi^2
\]

is exactly compatible with the existing Cauchy I/V causal split.

For the residual-source route developed on 2026-08-14, an efficient stretching source was already reduced to projective defect or mean-axis directional strain/conversion, modulo affine cancellation. On the projectively coherent subset where the Gaussian mean axis approximates the total vorticity direction, the present identities transfer that strain witness into the Cauchy I/V ledger. If the approximation fails, the route is already charged to the projective-defect branch.

Therefore the stretching part of the residual source has no independent causal escape:

\[
\boxed{
\text{residual stretching source}
\Rightarrow
\text{projective defect}
\ \text{or}\ 
\text{Cauchy material stretch/rotation}
\ \text{or}\ 
\text{viscous }\Delta\omega\text{ rewrite}.
}
\]

Status: STRETCH/CONVERSION SOURCE FULLY TYPED INTO PROJECTIVE OR CAUCHY I/V CHANNELS; GLOBAL PACKING OF THOSE CHANNELS REMAINS THE ISSUE.
