# Compact Recurrent Extremal Ledgers for P_V — 2026-08-20

Overall status: **DIRECT RECURRENT-ORBIT PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note removes an ambiguity in the recurrent Type-I argument. Instead of asking for a checkpoint at which several derivative signs happen to be favorable simultaneously, use extrema of continuous functionals on the compact invariant closure of the recurrent Leray orbit.

## 1. Leray L2 and H1 strain ledgers

For the backward Leray strain `Sigma(Y,s)`, define

\[
E(s)=\|\Sigma(s)\|_2^2,
\qquad
P(s)=\|\nabla\Sigma(s)\|_2^2,
\qquad
H(s)=\|\Delta\Sigma(s)\|_2^2.
\]

The H1 ledger already established is

\[
\boxed{
\frac12P_s+\frac34P+\nu H=N,
}
\]

where `N` is the exact `P_V` H1 production.

The physical strain-enstrophy identity

\[
\frac d{dt}\|S\|_2^2
+2\nu\|\nabla S\|_2^2
=-4\int\det S
\]

transforms to the backward Leray L2 ledger

\[
\boxed{
E_s+\frac12E+2\nu P
=D,
\qquad
D:=-4\int\det\Sigma.
}
\]

Thus similarity scaling supplies a positive `E/2` tax in the L2 ledger, just as it supplies a positive `3P/4` tax in the H1 ledger.

## 2. Extremal states on a compact recurrent closure

Assume the non-H/T `P_V` survivor generates a nonzero precompact recurrent Leray orbit. Let `K` denote a compact invariant recurrent closure.

The continuous functionals `E` and `P` attain maxima on `K`.

Choose a complete trajectory through an `E`-maximizing state. At the maximizing time,

\[
\boxed{E_s=0.}
\]

Hence

\[
\boxed{
D
=\frac12E+2\nu P.
}
\]

Likewise, at a `P`-maximizing state,

\[
\boxed{P_s=0,}
\]

and therefore

\[
\boxed{
N
=\frac34P+\nu H.
}
\]

The two equalities need not occur at the same point of `K`; this is not required. They are two exact necessary conditions on the same compact invariant recurrent class.

## 3. Exact determinant efficiency for positive-middle strain

Write the positive-middle spectrum as

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\qquad
x=d/m\in[0,1).
\]

Then

\[
-\det S
=2m^3(1-x^2),
\]

and

\[
|S|^3
=[2(3+x^2)]^{3/2}m^3.
\]

Relative to the sharp determinant ceiling

\[
-\det S
\le
\frac{|S|^3}{3\sqrt6},
\]

the exact spectral efficiency is

\[
\boxed{
\Theta_{det}(x)
=
\frac{3\sqrt3(1-x^2)}{(3+x^2)^{3/2}}.
}
\]

It decreases monotonically from

\[
\Theta_{det}(0)=1
\]

to

\[
\Theta_{det}(1)=0.
\]

Thus the H1 nonnormality ceiling and the L2 determinant ceiling prefer opposite spectral limits:

- H1 nonnormality efficiency increases toward `x=1`;
- determinant/enstrophy efficiency decreases to zero toward `x=1`.

## 4. Natural spectral dividing point

Use the previous double-saturation threshold

\[
\boxed{
x_*
=\frac{3(\sqrt3-1)}4
\approx0.5490381057.}
\]

At this point

\[
\boxed{
\Theta_{det}(x_*)
\approx0.605101397.
}
\]

Therefore every positive-middle point with

\[
x\ge x_*
\]

pays at least a `39.49%` determinant-production loss from the max-mid determinant ceiling.

If `s_2 <= 0`, then

\[
-\det S\le0,
\]

so such points contribute no positive determinant production at all.

## 5. Pure middle-zero-side recurrent E-max branch

Suppose that at an `E`-maximizing state every point contributing positive determinant production lies in

\[
x\ge x_*.
\]

Then, with

\[
B=\|S\|_\infty,
\qquad
C_E=\frac4{3\sqrt6},
\]

we have

\[
D=-4\int\det S
\le
C_E\Theta_{det}(x_*)
\int |S|^3
\le
C_E\Theta_{det}(x_*) B E.
\]

But the extremal L2 ledger requires

\[
D=\frac12E+2\nu P.
\]

Therefore

\[
\boxed{
\frac12+2\nu\frac PE
\le
C_E\Theta_{det}(x_*)B.
}
\]

In particular, dropping the positive viscous term gives the necessary amplitude floor

\[
\boxed{
B
\ge
B_{mz}
:=
\frac{1/2}{C_E\Theta_{det}(x_*)}
\approx1.51802435.
}
\]

Thus a recurrent compact class with a uniform strain-amplitude ceiling

\[
\boxed{\|S\|_\infty<1.51802435}
\]

cannot have its `E`-max state entirely on the middle-zero/non-normality side `x >= x_*`.

The second-order Biot--Savart bound provides an explicit way to test this condition from `K_2`, `R_Z`, and `epsilon_Z`.

## 6. Consequence if the amplitude ceiling is below B_mz

If

\[
B_K<B_{mz},
\]

then every `E`-maximizing state must contain a nontrivial determinant-producing region with

\[
\boxed{x<x_*.}
\]

Meanwhile the `P`-maximizing state is constrained by the nonnormality analysis:

- the branch `x <= x_*` pays the strict nonnormality self-consistency loss;
- approaching the universal H1 ceiling pushes derivative-active high-strain regions toward `x>x_*`.

Thus a compact recurrent orbit must either remain uniformly below the H1 ceiling or execute a genuine spectral-shape excursion between a determinant-efficient max-mid side and a nonnormality-efficient middle-zero side.

## 7. New dynamic target

The proof attempt now has a concrete dynamical alternative.

### Static closure

If the Biot--Savart/tightness constants imply

\[
B_K<B_{mz}
\]

and the strict H1 ceiling is already below the Leray `P`-maximum requirement, the recurrent orbit is eliminated directly.

### Spectral-excursion closure

Otherwise quantify the minimum projective/spectral action required for a trajectory in `K` to move between

\[
x<x_*
\]

at an `E`-efficient state and

\[
x>x_*
\]

at an H1-efficient state.

The existing `P_V` shape-speed bound and eigenaxis-rotation source identity are designed for this step.

## 8. Importance of the extremal-state method

No assumption is needed that `E_s` and `P_s` vanish simultaneously. Compact recurrence supplies two separate exact extremal states. A contradiction may therefore be obtained by showing that one compact invariant class cannot contain both required geometries without paying an excluded `H/T` or projective action cost.

Status: **A PRECOMPACT RECURRENT LERAY P_V ORBIT HAS EXACT L2- AND H1-EXTREMAL STATES. THE E-MAX STATE CANNOT LIVE ENTIRELY ON THE MIDDLE-ZERO SIDE UNLESS `||S||_infinity >= 1.51802435` (EVEN BEFORE VISCOSITY IS RETAINED). THIS CREATES A DIRECT SPECTRAL TENSION WITH THE H1 NONNORMALITY BRANCH.**