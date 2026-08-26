# DSD M5-38 — Direction Dissipation as a Pressure Overpay Tax

Date: 2026-08-27

Status: **DERIVED CHANNEL-SEPARATED LOWER BOUND / THE QUADRATIC THRESHOLD PRESSURE SOURCE COUPLES DIRECTLY TO THE LONGITUDINAL AMPLITUDE CHANNEL WHILE VISCOSITY ALSO PAYS DIRECTION DEFORMATION / ANY DIRECTION DISSIPATION FORCES EXTRA WEIGHTED PRESSURE TAIL / GLOBAL REGULARITY UNPROVED.**

## 1. Quadratic threshold entropy

Return to the continuous quadratic excess

\[
\Phi_2(a)=\frac12(a-1)_+^2,
\qquad
W=(a-1)_+n,
\qquad a=|V|.
\]

The exact first-hit ledger is

\[
T_{form}
=\mathcal G'+\nu D_{exc}.
\]

At a fixed positive first hit,

\[
\boxed{T_{form}\ge\nu D_{exc}.}
\]

Split

\[
\boxed{
D_{exc}=D_a+D_n,
}
\]

where

\[
D_a
:=
\int_{a>1}|\nabla a|^2dz,
\]

and

\[
D_n
:=
\int_{a>1}a(a-1)|\nabla n|^2dz.
\]

## 2. Pressure source uses the longitudinal amplitude channel

For the quadratic multiplier,

\[
\operatorname{div}W
=-\operatorname{div}n.
\]

Incompressibility gives

\[
\boxed{
\operatorname{div}n
=-\frac{n\cdot\nabla a}{a}.
}
\]

Hence

\[
T_{form}
=-\int_{a>1}\Pi\,\operatorname{div}n\,dz.
\]

The source is therefore directly paired with the streamline/longitudinal amplitude derivative.

## 3. Weighted pressure Cauchy estimate

Write

\[
\begin{aligned}
|T_{form}|^2
&\le
\left(
\int_{a>1}a|\Pi|^2dz
\right)
\left(
\int_{a>1}
\frac{|\operatorname{div}n|^2}{a}dz
\right).
\end{aligned}
\]

Since

\[
\frac{|\operatorname{div}n|^2}{a}
=
\frac{|n\cdot\nabla a|^2}{a^3}
\le
|\nabla a|^2
\qquad(a\ge1),
\]

we obtain

\[
\boxed{
|T_{form}|^2
\le
\left(
\int_{a>1}a|\Pi|^2dz
\right)D_a.
}
\]

## 4. First-hit pressure overpay

At the positive first hit,

\[
\nu^2(D_a+D_n)^2
\le
\left(
\int_{a>1}a|\Pi|^2dz
\right)D_a.
\]

Therefore

\[
\boxed{
\int_{a>1}a|\Pi|^2dz
\ge
\nu^2
\frac{(D_a+D_n)^2}{D_a}.
}
\]

Expand the ratio:

\[
\frac{(D_a+D_n)^2}{D_a}
=D_a+2D_n+\frac{D_n^2}{D_a}
\ge
D_a+2D_n.
\]

Since `D_exc=D_a+D_n`,

\[
\boxed{
\int_{a>1}a|\Pi|^2dz
\ge
\nu^2(D_{exc}+D_n).
}
\]

Thus direction dissipation creates an additive pressure-tail overpay beyond the baseline viscous amount.

## 5. DSD channel interpretation

The first-hit formation process has distinct typed roles:

- **pressure source channel:** longitudinal amplitude compression/transport through `div n = -(n·grad a)/a`;
- **amplitude viscous channel:** `D_a`;
- **direction viscous channel:** `D_n`.

Pressure work can correlate directly with the first channel, but viscosity charges both amplitude and direction deformation. Hence direction deformation is an additional tax that pressure must overcompensate for a first hit to occur.

This is not a second independent physical source; it is a strict inequality inside the one threshold-Hodge formation ledger.

## 6. Relation to the helical/twist split

M5-27 decomposes the mandatory solenoidal geometry into a two-helicity mixed branch or a direction-twist branch.

Whenever either branch supplies a quantitative lower bound

\[
D_n\ge d_n>0,
\]

M5-38 immediately yields

\[
\boxed{
\int_{a>1}a|\Pi|^2dz
\ge
\nu^2D_{exc}+\nu^2d_n.
}
\]

Thus any independent direction/twist floor translates into a strict weighted-pressure correlation requirement.

## 7. Limitation

The smooth quadratic direction weight `a(a-1)` still degenerates at the threshold, as audited in M5-30. Therefore a generic lower bound on `div n` does not automatically imply a uniform lower bound on `D_n` unless the direction activity is known to occur away from the collar or is weighted by the excess itself.

Consequently this estimate strengthens the twist/deep-direction branches but does not by itself close the mixed/collar branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
