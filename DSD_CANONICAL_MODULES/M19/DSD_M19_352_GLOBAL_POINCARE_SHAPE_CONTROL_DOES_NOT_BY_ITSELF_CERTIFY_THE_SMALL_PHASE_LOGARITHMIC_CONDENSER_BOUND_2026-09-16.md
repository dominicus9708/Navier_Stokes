# DSD M19-352 — Global Poincare shape control does not by itself certify the small-phase logarithmic condenser bound required by M19-351

Date: 2026-09-16  
Canonical ID: **M19-352**

Status: **ACTIVE CAPACITY-VERSUS-POINCARE AUDIT / LOCAL PHASE-MODULUS FIREWALL / M17-449 SEPARATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Question

M19-351 conditionally closes every fixed power sign-flux thinning law if one has a transverse condenser estimate of the schematic form

\[
(a_S-a_C)_+^2
\lesssim
\log R
\int_A|\nabla_\perp\rho|^2dA.
\]

M17-449 already tracks transverse Poincare geometry through

\[
C_P(A)=\mathfrak A(A)\Pi(A),
\]

where \(\Pi\) is scale-free under isotropic dilation.

The present audit asks whether bounded \(\Pi\) already supplies the M19-351 condenser bound.

It does not, at least not from the global Poincare inequality alone.

## 2. What M17-449 controls

The optimal global Poincare inequality is

\[
\int_A|f-\bar f_A|^2dA
\le
C_P(A)
\int_A|\nabla f|^2dA.
\]

On the canonical mesoscopic baseline

\[
\mathfrak A(A)\asymp R,
\qquad
\Pi(A)=O(1),
\]

one has

\[
\boxed{C_P(A)\asymp R.}
\]

This controls global mean-zero oscillation at the scale of the entire section.

It does not distinguish a phase occupying a vanishing fraction of the section from one occupying a fixed fraction.

## 3. Small-set variance loses the phase-size factor

Suppose a scalar takes values differing by an amount \(\Delta\) on two regions, one of which has geometric area \(m\ll |A|\), while the complementary region has area comparable to \(|A|\).

The elementary two-population variance lower bound is only

\[
\int_A|f-\bar f|^2dA
\gtrsim
m\Delta^2
\]

when \(m\) is the smaller area.

The global Poincare inequality therefore yields only

\[
\boxed{
\int_A|\nabla f|^2dA
\gtrsim
\frac{m}{C_P(A)}\Delta^2.
}
\]

On the baseline \(C_P\asymp R\), if

\[
m\asymp R^{-1},
\]

this gives

\[
\boxed{
\int_A|\nabla f|^2dA
\gtrsim
R^{-2}\Delta^2.
}
\]

This is far weaker than the logarithmic two-dimensional capacity scale

\[
\frac{\Delta^2}{\log R}.
\]

Hence the M17-449 Poincare formula cannot simply be substituted for the M19-351 capacity hypothesis.

## 4. Round annulus model

This section is a functional scaling model, not a Navier--Stokes solution.

Let

\[
A=B_L(0)\subset\mathbb R^2,
\qquad
L\asymp R^{1/2},
\]

so

\[
|A|\asymp R.
\]

Let the small phase be an inner disk

\[
S=B_r(0),
\qquad
r\asymp R^{-1/2},
\]

so

\[
|S|\asymp R^{-1}.
\]

The ambient domain is perfectly shape-regular: its scale-free Poincare factor \(\Pi(A)\) is order one.

Consider the harmonic condenser profile that equals one on \(B_r\) and zero on \(\partial B_L\). Its Dirichlet energy is

\[
\boxed{
\operatorname{Cap}(B_r,B_L)
=
\frac{2\pi}{\log(L/r)}
\asymp
\frac{1}{\log R}.
}
\]

Thus the natural small-phase interpolation cost is logarithmic even though the ambient global Poincare constant is merely \(C_P\asymp R\).

The global Poincare lower bound from Section 3 sees only \(R^{-2}\) in this configuration and is therefore highly nonsharp for the small phase.

## 5. Different geometric objects

The two quantities encode different information.

### Ambient Poincare descriptor

\[
\boxed{
\Pi(A)=\frac{C_P(A)}{|A|}
}
\]

measures scale-free global spectral/shape degeneration of the entire cross-section.

### Relative phase capacity

For two represented phase sets \(S,C\subset A\), define schematically

\[
\boxed{
\operatorname{Cap}_A(S,C)
:=
\inf
\left\{
\int_A|\nabla f|^2dA:
 f\ge1\text{ on }S,
 f\le0\text{ on }C
\right\}.
}
\]

This measures the energetic cost of separating the particular two phases inside the section.

A shape-regular ambient domain can have small subsets whose relative capacity depends logarithmically on their size. Conversely a globally bad neck may degrade both quantities.

Therefore the two gates overlap but are not identical.

## 6. Correct relation to M17-447--449

M17-447 works when the high- and low-amplitude populations each occupy fixed positive transverse measure. In that regime ordinary Poincare is enough to force an order-one transverse gradient cost.

M19-348--350 identify a different endpoint: the relevant sign phase may have vanishing material-flux and geometric participation.

For such a phase, the fixed-measure hypothesis of M17-447 is unavailable. The correct two-dimensional cost is potentially capacitary rather than variance/Poincare at fixed measure.

Thus

\[
\boxed{
\text{M19-351 is the vanishing-phase analogue of M17-447, not a restatement of M17-449.}
}
\]

## 7. What bounded scale-free Poincare does and does not say

Bounded \(\Pi(A)\) remains useful:

- it removes global thin-neck/spectral degeneration of the ambient section;
- it normalizes the mesoscopic size contribution already isolated by M17-450;
- it makes a regular condenser interpretation geometrically plausible.

But it does not by itself certify

\[
\operatorname{Cap}_A(S,C)\gtrsim1/\log R
\]

for the particular coefficient-sign/amplitude phase sets generated by the PDE.

That requires additional phase-local geometry: placement, nondegenerate separation, common-section realization, and control of phase microstructure.

## 8. Updated failure taxonomy

Failure of the M19-351 condenser estimate should not be automatically labeled only as \(\Pi\to\infty\).

The correct split is

\[
\boxed{
\begin{aligned}
G_{\rm condenser\ failure}
\Longrightarrow{}&
G_{\rm ambient\ shape/neck\ degeneration}\;(\Pi\to\infty)\\
&\lor G_{\rm sign\text{-}phase\ local\ modulus\ degeneration}\\
&\lor G_{\rm phase\ fragmentation/microstructure}\\
&\lor G_{\rm boundary\ attachment/escape}\\
&\lor G_{\rm common\ section/chart\ loss}.
\end{aligned}
}
\]

The second and third branches are phase-local and can occur conceptually even when the ambient section itself remains shape-compact.

## 9. New canonical geometry variable

The natural dimensionless small-phase geometry variable is not only \(\Pi(A)\), but a relative phase modulus such as

\[
\boxed{
\mathfrak M_{S,C}(A)
:=
\left[\operatorname{Cap}_A(S,C)ight]^{-1}
}
\]

with the expected regular two-dimensional scaling

\[
\mathfrak M_{S,C}\lesssim C\log R
\]

for a phase whose linear size differs from the mesoscopic section size by a polynomial factor in \(R\).

M19-351 can then be read as requiring a logarithmic bound on this relative phase modulus.

## 10. Audit verdict

**PASS — global Poincare compactness and local sign-phase condenser compactness are distinct.**

M17-449 removes confusion between transverse size and global shape, but it does not by itself prove the small-phase logarithmic capacity estimate needed to close the M19-348 endpoint survivor. The new obligation is genuinely phase-local.

The next target is to formulate M19-351 with explicit amplitude quantile sets and relative capacity, so that the required geometric theorem no longer depends on an abstract mean-amplitude inequality and can be tested directly against analyticity/zero-interface geometry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
