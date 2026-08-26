# DSD W1 Projective Amplitude--Spatial Boundary

Date: 2026-08-26

Status: **THE WEAK-L3 DEFECT IS LOCATED ON THE JOINT LIMIT `LAMBDA*R=O(1)` RATHER THAN ON AMPLITUDE ZERO OR SPATIAL INFINITY SEPARATELY / FAR BLOW-DOWN TURNS THE DEFECT INTO A NONTRIVIAL UNIT-LEVEL DISTRIBUTION FOR A LINEAR-DILATION BOUNDARY FIELD / GLOBAL REGULARITY UNPROVED.**

## 1. Joint scaling

For a small normalized amplitude `lambda>0`, define the spatial blow-down

\[
\boxed{
V_\lambda(z,s)
:=
\lambda^{-1}U(z/\lambda,s).
}
\]

The spatial variable is

\[
z=\lambda Y.
\]

Thus fixed `z` probes Leray radius

\[
|Y|\asymp\lambda^{-1}.
\]

The weak-L3 low-amplitude boundary and spatial infinity are therefore coupled by

\[
\boxed{\lambda |Y|=O(1).}
\]

## 2. Defect coefficient becomes a fixed-level volume

By the change of variables `z=lambda Y`,

\[
\begin{aligned}
\lambda^3|\{Y:|U(Y,s)|>\lambda\}|
&=
|\{z:|V_\lambda(z,s)|>1\}|.
\end{aligned}
\]

Hence

\[
\boxed{
\mathscr C_{WL3}
=
\lim_{\lambda\downarrow0}
|\{|V_\lambda|>1\}|
}
\]

whenever the defect limit exists.

The low-amplitude distribution anomaly is thus an ordinary unit-amplitude mass of the far blow-down field.

## 3. Blow-down equation

Write the backward Leray equation as

\[
U_s+\frac12U+\frac12Y\cdot\nabla U
-\nu\Delta U
+(U\cdot\nabla)U+\nabla P=0.
\]

Under

\[
U(Y,s)=\lambda V_\lambda(\lambda Y,s),
\]

the linear dilation terms are order `lambda`, whereas viscosity and nonlinearity are order `lambda^3`. After division by `lambda`,

\[
\boxed{
\partial_sV_\lambda
+\frac12V_\lambda
+\frac12z\cdot\nabla V_\lambda
+\lambda^2\mathcal N[V_\lambda,Q_\lambda]
=0.
}
\]

Therefore any compact blow-down limit satisfies

\[
\boxed{
\partial_sV
+\frac12V
+\frac12z\cdot\nabla V
=0.
}
\]

This is the same linear-dilation boundary equation obtained from the log-tail hull.

## 4. DSD boundary geometry

The critical defect is not naturally assigned to either coordinate boundary separately:

- `lambda=0` at fixed `Y` sees the interior state;
- `|Y|=infinity` at fixed amplitude loses the matched critical level;
- the defect lives on the projective boundary `lambda|Y|~1`.

Thus the correct compactification must retain the product coordinate

\[
\boxed{z=\lambda Y.}
\]

In DSD language, amplitude resolution and spatial resolution must be refined jointly.

## 5. Physical interpretation

Since

\[
\lambda=L\sqrt{T_*-t},
\qquad
|Y|=r/\sqrt{T_*-t},
\]

one has

\[
\boxed{\lambda|Y|=Lr.}
\]

Therefore the joint boundary is physically

\[
\boxed{Lr=O(1),}
\]

i.e. velocity amplitude grows like inverse physical radius.

This is exactly the `1/r` critical geometry.

## 6. Consequence

Uniform no-defect is equivalent to triviality of all such projective blow-down limits. The W1 survivor instead requires a nontrivial projective boundary field with positive unit-level volume.

The leading boundary equation is linear and permits nontrivial `-1` degree / log-translation structures, so linear boundary dynamics alone do not yield a contradiction. Any closure must use how this boundary field is attached to the finite-amplitude nonlinear interior at the next scale-sensitive level.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
