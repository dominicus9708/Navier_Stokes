# Combined source/dissipation certificate from angular and magnitude deficits

Date: 2026-08-13

Status: **DERIVED DIMENSIONLESS ENSTROPHY-GROWTH CERTIFICATE / CONSTANT-DEPENDENT BUT EXACT GIVEN SOURCE BOUND**.

The magnitude-direction palinstrophy split and the magnitude-heterogeneity interpolation gap can be combined into one dimensionless certificate that is necessary for nondecreasing global enstrophy.

---

## 1. Refined source bound

Let

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\]

\[
\eta_{\rm ang}
=\frac{P_{\rm ang}}P
\in[0,1]
\]

when `P>0`, and let

\[
\chi_{\rm mag}\ge0
\]

be the enstrophy-weighted magnitude coefficient of variation.

The refined source estimate is

\[
\boxed{
|Q|
\le
C_*E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4}
(1+\chi_{\rm mag})^{-1/2}.
}
\]

The global enstrophy identity is

\[
\frac12\dot E+\nu P=Q.
\]

---

## 2. Dimensionless certificate

For `E,P>0` and `eta_ang<1`, define

\[
\boxed{
\mathfrak D
=
\frac{\nu^4P}{C_*^4E^3}
\frac{(1+\chi_{\rm mag})^2}
{(1-\eta_{\rm ang})^3}.
}
\]

The fourth power of the source/dissipation ratio obeys

\[
\left(
\frac{|Q|}{\nu P}
\right)^4
\le
\frac1{\mathfrak D}.
\]

Therefore

\[
\boxed{
\mathfrak D>1
\Longrightarrow
|Q|<\nu P.
}
\]

Consequently

\[
\boxed{
\mathfrak D>1
\Longrightarrow
\dot E<0.
}
\]

---

## 3. Necessary condition for enstrophy growth

If

\[
\dot E\ge0,
\]

then

\[
Q\ge\nu P>0.
\]

Hence necessarily

\[
\boxed{
\mathfrak D\le1.
}
\]

Equivalently,

\[
\boxed{
\nu^4P(1+\chi_{\rm mag})^2
\le
C_*^4E^3(1-\eta_{\rm ang})^3.
}
\]

This is a combined compatibility condition among

- total palinstrophy;
- angular/directional palinstrophy fraction;
- enstrophy-weighted magnitude heterogeneity;
- viscosity;
- total enstrophy.

---

## 4. DSD interpretation

Keep the underlying channel block

\[
\boxed{
(E,P,\eta_{\rm ang},\chi_{\rm mag})
}
\]

as primary data.  The scalar

\[
\mathfrak D
\]

is a **derived certificate**, not a replacement for those channels.

- `D>1`: guaranteed dissipative side of the derived bound;
- `D<=1`: potentially source-active, but not guaranteed to grow;
- `D near 1`: candidate near-saturation state requiring further equality/geometry checks.

Thus no information-loss claim is made from the single aggregate value.

---

## 5. Equality/saturation stack

A sequence with

\[
\dot E\ge0
\]

and

\[
\mathfrak D\to1
\]

must approach equality in several separate estimates, including

1. the strain/vorticity `L3` singular-integral bound;
2. the critical `L2-L3-L6` interpolation;
3. scalar Sobolev for `rho=|omega|`;
4. the angular-palinstrophy split with the required total-palinstrophy ratio;
5. any localization/far-field decompositions used in the local version.

The previously derived compactness-rigidity gap shows that one of these equality requirements (`chi_mag -> 0`) is impossible on a strongly `H1`-compact nontrivial cutoff family.

---

## 6. Scale invariance

Under Navier--Stokes scaling,

\[
E\mapsto\lambda E,
\qquad
P\mapsto\lambda^3P,
\]

while

\[
\eta_{\rm ang},
\qquad
\chi_{\rm mag}
\]

are invariant.

Therefore

\[
\frac{P}{E^3}
\]

and hence

\[
\boxed{\mathfrak D}
\]

are scale invariant.

This makes `mathfrak D` suitable for comparison across the natural-window amplification checkpoints.

---

## 7. Claim boundary

The certificate uses the analytical constant `C_*` from the singular-integral/interpolation/Sobolev chain.  It does not prove that `mathfrak D>1` for arbitrary data.  Its role is to define the exact channel inequality that any enstrophy-growing residual state must satisfy.

A local moving-window version also requires the already-typed shell, near/far strain, and cutoff terms.

Status: **GLOBAL CERTIFICATE DERIVED / LOCAL CERTIFICATE WITH REMAINDERS STILL TO CLOSE**.
