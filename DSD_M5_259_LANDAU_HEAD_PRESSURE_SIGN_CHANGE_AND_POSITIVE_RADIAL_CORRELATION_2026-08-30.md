# DSD M5-259 — Landau Head-Pressure Sign Change and Positive Radial Correlation

Date: 2026-08-30

Parent: `DSD_M5_258_STATIONARY_LOG_TAIL_HEAD_PRESSURE_IDENTITY_2026-08-30.md`

Status: **EXPLICIT LANDAU MODEL AUDIT / THE POINT-FORCE LANDAU FAMILY DOES NOT HAVE GLOBALLY NONPOSITIVE HEAD PRESSURE: THE HEAD-PRESSURE COEFFICIENT CHANGES SIGN ON THE SPHERE / NEVERTHELESS ITS SPHERICAL MEAN AND ITS RADIAL BERNOULLI CORRELATION ARE STRICTLY POSITIVE / THEREFORE THE WHOLE-SPACE MAXIMUM-PRINCIPLE SIGN ROUTE IS DEFINITIVELY INVALID FOR THE POINT-FORCE ENDPOINT, WHILE POSITIVE RADIAL BERNOULLI CORRELATION EMERGES AS THE MORE ROBUST LANDAU-COMPATIBLE SCALAR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Standard Landau formula

Use the standard Slezkin--Landau family aligned with the `x_1` axis, with parameter

\[
|c|>1.
\]

For viscosity `nu=1`, a conventional Cartesian representation is

\[
\begin{aligned}
V_{c,1}(x)
&=
\frac{2\left(c|x|^2-2x_1|x|+cx_1^2\right)}
{|x|(c|x|-x_1)^2},\\
V_{c,2}(x)
&=
\frac{2x_2(cx_1-|x|)}
{|x|(c|x|-x_1)^2},\\
V_{c,3}(x)
&=
\frac{2x_3(cx_1-|x|)}
{|x|(c|x|-x_1)^2},
\end{aligned}
\]

and

\[
\boxed{
P_c(x)
=
\frac{4(cx_1-|x|)}
{|x|(c|x|-x_1)^2}.
}
\]

Let

\[
\mu:=\frac{x_1}{|x|}\in[-1,1].
\]

Then

\[
V_c=r^{-1}\Phi_c(\mu),
\qquad
P_c=r^{-2}\Pi_c(\mu).
\]

For general viscosity, multiply velocity by `nu` and pressure by `nu^2`; all sign conclusions below are unchanged.

---

## 2. Velocity magnitude and head pressure

Direct algebra gives

\[
|\Phi_c|^2
=
\frac{4\left(3c^2\mu^2+c^2-2c\mu^3-6c\mu+3\mu^2+1\right)}
{(c-\mu)^4}.
\]

The head-pressure coefficient

\[
h_c(\mu)
:=
\Pi_c(\mu)+\frac12|\Phi_c(\mu)|^2
\]

simplifies exactly to

\[
\boxed{
 h_c(\mu)
=
\frac{2(c^2-1)(2c\mu-\mu^2-1)}
{(c-\mu)^4}.
}
\]

Thus

\[
H_c(x)=r^{-2}h_c(\mu).
\]

---

## 3. Head pressure changes sign

The sign-controlling numerator is

\[
2c\mu-\mu^2-1
=
(c^2-1)-(\mu-c)^2.
\]

For `c>1`,

\[
2c(1)-1-1=2(c-1)>0,
\]

while

\[
2c(-1)-1-1=-2(c+1)<0.
\]

Therefore

\[
\boxed{
H_c\text{ changes sign on }S^2.
}
\]

The same conclusion holds after reversing the axis for `c<-1`.

Hence the point-force Landau solution is an explicit counterexample to any attempted import of

\[
H\le0
\]

from smooth whole-space stationary Liouville theory to the punctured point-force class.

---

## 4. Spherical mean is positive

Despite the sign change,

\[
\int_{-1}^{1}h_c(\mu)d\mu
=
\boxed{
\frac{16}{3(c^2-1)}
}>0.
\]

Including the azimuthal integral gives

\[
\boxed{
\int_{S^2}h_cd\theta
=
\frac{32\pi}{3(c^2-1)}
>0.
}
\]

Thus even the weaker averaged sign

\[
\overline H_0\le0
\]

from M5-258 is not a Landau-universal property.

---

## 5. Radial velocity coefficient

The radial component simplifies to

\[
\boxed{
\Phi_{c,r}(\mu)
=
\frac{2(2c\mu-\mu^2-1)}{(c-\mu)^2}.
}
\]

Thus the radial velocity and head pressure share the same sign-changing factor.

Their product is therefore nonnegative pointwise:

\[
\boxed{
\Phi_{c,r}h_c
=
\frac{4(c^2-1)(2c\mu-\mu^2-1)^2}
{(c-\mu)^6}
\ge0.
}
\]

It is nonzero except on the zero set of the numerator.

This is stronger than positivity of the spherical mean.

---

## 6. Exact radial Bernoulli correlation

Direct integration yields

\[
\boxed{
\int_{-1}^{1}
\Phi_{c,r}(\mu)h_c(\mu)d\mu
=
\frac{32(5c^2+7)}
{15(c^2-1)^2}
>0.
}
\]

Hence

\[
\boxed{
\int_{S^2}\Phi_{c,r}h_cd\theta
=
\frac{64\pi(5c^2+7)}
{15(c^2-1)^2}
>0.
}
\]

Thus the M5-258 radial Bernoulli observable is strictly positive throughout the nonzero Landau family.

---

## 7. Compatibility with the head-pressure identity

M5-258 gives for any stationary recurrent critical tail

\[
2\nu\overline H_0+\mathcal B_r
=\nu\mathcal Z_T.
\]

For Landau, both

\[
\overline H_0>0
\]

and

\[
\mathcal B_r>0.
\]

Therefore the enstrophy term is large enough to pay both positive contributions.

There is no sign contradiction.

---

## 8. Perturbative implication

The pointwise identity

\[
\Phi_{c,r}h_c\ge0
\]

and strict positivity of its sphere integral are stable under sufficiently small perturbations in a topology controlling both the radial velocity and head pressure on `S2`.

Therefore a stationary critical profile sufficiently close to a Landau solution at fixed force has

\[
\boxed{
\mathcal B_r>0.
}
\]

This supplies a perturbative radial-flux sign gate around Landau.

However the current arbitrary-large stationary endpoint need not lie in that neighborhood.

---

## 9. Relation to fixed-force nondegeneracy

The fixed-force stationary endpoint from M5-227/228 keeps the point-force coefficient `b` fixed under dilation.

Landau's family parameter changes the force amplitude/direction. Consequently the Landau-family tangent is not the fixed-force dilation zero-mode sought in the current survivor.

The present positive radial-correlation calculation therefore does not by itself remove the non-Landau large-amplitude kernel.

---

## 10. DSD verdict

### EXPLICITLY DISPROVED AS A UNIVERSAL POINT-FORCE RULE

\[
\boxed{H\le0.}
\]

Landau head pressure changes sign and has positive spherical mean.

### POSITIVE LANDAU-COMPATIBLE OBSERVABLE

\[
\boxed{
\int_{S^2}H\,u_r\,r^3d\theta>0
}
\]

in scale-normalized form, equivalently `B_r>0`.

### PERTURBATIVE CONSEQUENCE

Positive radial Bernoulli correlation persists near the Landau family.

### OPEN

Whether fixed point force plus compact minimal log-recurrence enforces `B_r>=0` at arbitrary critical amplitude remains unknown in the present audit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
