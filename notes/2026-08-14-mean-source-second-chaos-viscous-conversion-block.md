# Mean-source split into surviving second chaos, viscous conversion, or projective defect

Date: 2026-08-14

Status: **EXACT ISOTROPIC MATCHED-HEAT BLOCK DECOMPOSITION FOR THE QUADRATIC CORE / BOUNDED-AFFINE VERSION FOLLOWS AFTER THE HOMOGENEOUS PROPAGATOR IMPLEMENTATION**.

The quadratic-core mean source has already been reduced pointwise to

\[
J=L_2N_{\omega,2}+Ab,
\]

where `L2` is the fixed finite-dimensional trace map from second Hermite chaos to the Gaussian mean contribution, and

\[
|Ab|\lesssim\sqrt{V_\omega V_\perp}.
\]

This note shows that time cancellation of the second-chaos source is not a new escape. Under matched heat propagation, the trace source splits exactly into a surviving degree-two output and a heat-erased/viscous part.

## 1. One isotropic matched block

Fix a parent covariance

\[
\Sigma_p=R_p^2I
\]

and a child covariance

\[
\Sigma_c=c\Sigma_p,
\qquad 0<c<1.
\]

Choose the block duration by the matched heat relation.

At an intermediate source time `s`, let

\[
\rho_2(s)\in[c,1]
\]

be the amplitude attenuation factor with which a second-Hermite-chaos vorticity source reaches the child state.

For pure heat, Hermite degree two is preserved and multiplied by this positive scalar factor.

## 2. Degree-two Duhamel output

Let

\[
N_2(s):=N_{\omega,2}(s).
\]

The second-chaos part of the nonlinear Duhamel contribution at the child is

\[
\boxed{
Q_2
=
\int_{t_p}^{t_c}
\rho_2(s)N_2(s)\,ds.
}
\]

Since `L2` is linear,

\[
L_2Q_2
=
\int
\rho_2(s)L_2N_2(s)\,ds.
\]

## 3. Mean trace contribution

The trace-generated part of the Gaussian mean source over the same block is

\[
M_{\rm tr}
:=
\int
L_2N_2(s)\,ds.
\]

Insert `1=rho2+(1-rho2)`:

\[
\boxed{
M_{\rm tr}
=
L_2Q_2
+
M_{\rm visc},
}
\]

where

\[
\boxed{
M_{\rm visc}
:=
\int
(1-\rho_2(s))
L_2N_2(s)\,ds.
}
\]

This identity is exact.

The first term is the trace of the degree-two nonlinear output that survives to the child scale.

The second term is precisely the portion of the trace source removed from the second-chaos child state by heat attenuation inside the block.

Therefore it is naturally a **viscous-conversion / viscous-rewrite channel**.

## 4. Add the constant-shift term

The full quadratic-core mean Duhamel contribution is

\[
M_{\rm core}
=
\int J(s)ds
=
M_{\rm tr}
+
M_{Ab},
\]

with

\[
M_{Ab}=\int Ab\,ds.
\]

Hence

\[
\boxed{
M_{\rm core}
=
L_2Q_2
+
M_{\rm visc}
+
M_{Ab}.
}
\]

The last term is already quantitatively projective:

\[
|Ab|
\lesssim
\sqrt{V_\omega V_\perp}.
\]

Thus one matched block has the exact causal routing

\[
\boxed{
\text{quadratic-core mean contribution}
\Rightarrow
\text{surviving second chaos}
\ \lor\
\text{viscous heat conversion}
\ \lor\
\text{projective defect}.
}
\]

## 5. Why temporal sign oscillation is not a fourth channel

The identity is algebraic before taking absolute values.

Any sign oscillation in `N2(s)` appears simultaneously in both

\[
Q_2=\int\rho_2N_2
\]

and

\[
M_{\rm visc}=\int(1-\rho_2)L_2N_2.
\]

Therefore cancellation that makes the surviving child second-chaos output small does not make the mean trace source disappear for free. The missing part is transferred exactly into `M_visc`.

So `temporal cancellation` is not an independent escape; it is a redistribution between surviving degree two and viscous erasure.

## 6. Relation to the Cauchy I/V split

The total-vorticity polar identities previously routed large directional strain into

- material amplitude/direction change;
- viscous `Delta omega` rewrite.

The present finite-dimensional Hermite block gives the corresponding low-mode version of the same principle.

For the quadratic core, mean production not visible as surviving degree-two vorticity must be accounted for by heat attenuation of that degree-two source, which is the Hermite manifestation of the viscous lane.

Thus the two independently derived channel systems are consistent:

\[
\boxed{
\text{quadratic-core source}
\to
\text{projective}
\ \lor\
\text{second chaos / material residual change}
\ \lor\
\text{viscous rewrite}.
}
\]

## 7. Bounded-affine extension

When the full affine/mean linear feedback is moved into the homogeneous co-deforming propagator, degree-two modes need not be multiplied by a scalar; they are acted on by a finite-dimensional matrix propagator.

The exact scalar identity above is then replaced by

\[
I=\mathcal U_2(t_c,s)+[I-\mathcal U_2(t_c,s)]
\]

inside the source integral.

Hence the same algebraic decomposition survives:

\[
M_{\rm tr}
=L_2Q_2
+
\int L_2[I-\mathcal U_2]N_2\,ds,
\]

provided the co-affine trace map is transported consistently.

The remaining technical issue is therefore not the existence of the split, but bounding the finite-dimensional affine propagator and identifying its dissipative versus rotational pieces.

Status: **TIME-CANCELLATION ESCAPE REMOVED AT THE MATCHED-HEAT BLOCK LEVEL / CORE MEAN SOURCE FULLY ROUTED TO SURVIVING SECOND CHAOS, VISCOUS CONVERSION, OR PROJECTIVE DEFECT.**
