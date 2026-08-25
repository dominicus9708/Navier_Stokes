# DSD Permanent Export: Fixed \(L^3\) Shell Mass and Logarithmic Blow-up

Date: 2026-08-25

Status: **CONDITIONAL COHERENT-EXPORT LEMMA / FIXED CRITICAL \(L^3\) MASS PER GEOMETRIC SHELL / POSITIVE-FREQUENCY EXPORT FORCES LINEAR LERAY-TIME \(L^3^3\) GROWTH / NO GLOBAL CONTRADICTION YET.**

## 1. Purpose

The log-radius conveyor note shows that ordinary enstrophy weights old shells by \(R^{-1}\), whereas \(L^3\) counts them without radial decay.

This note makes that statement quantitative on the coherent permanent-export branch by deriving a fixed positive \(L^3\) mass from one exported fixed-flux population.

## 2. Coherent exported population at radius \(R\)

Work at one late normalized time.

Assume an exported population occupies a geometrically regular cross-sectional region at radius scale \(R\), with

\[
\operatorname{Area}(E_R)\le A_0R^2,
\]

and carries same-sign directed vorticity flux

\[
\boxed{
\int_{E_R}\Omega\cdot e\,dA
\ge \phi_0>0.
}
\]

Assume also the already used ancestor-scale analyticity/derivative corridor gives

\[
\boxed{
|\nabla\Omega|
\le \frac{K_1}{R^3}
}
\]

through a fixed geometric neighborhood of the population.

Failure of cross-sectional regularity, same-sign direction, or the derivative corridor is routed to the existing projective/noncoherent/H complement and is not silently included here.

## 3. Flux gives a critical vorticity point

By the area bound,

\[
\sup_{E_R}\Omega\cdot e
\ge
\frac{\phi_0}{A_0R^2}.
\]

Choose a point \(Y_R\) where this lower bound is attained up to the harmless supremum limit.

Define

\[
\delta
:=
\min\left\{
\delta_{geom},
\frac{\phi_0}{2A_0K_1}
\right\}>0,
\qquad
a=\delta R,
\]

where \(\delta_{geom}\) is a fixed fraction ensuring that the local cylinder remains inside the coherent shell neighborhood.

The derivative bound yields on that cylinder

\[
\boxed{
\Omega\cdot e
\ge
m_R
:=
\frac{\phi_0}{2A_0R^2}.
}
\]

Thus a fixed flux population contains a fixed-fraction critical vorticity patch.

## 4. Circulation gives a velocity-variance lower bound

Use coordinates with cylinder axis \(e\), radius \(a\), and half-height \(a\).

Let

\[
v=U-\bar U_C,
\]

where \(\bar U_C\) is the cylinder mean.

For every transverse disk of radius \(r\le a\), Stokes' theorem gives

\[
\oint_{\partial D_r}v\cdot t\,dl
=
\int_{D_r}\Omega\cdot e\,dA
\ge
m_R\pi r^2.
\]

Cauchy--Schwarz on the circle yields

\[
\oint_{\partial D_r}|v|^2dl
\ge
\frac{(m_R\pi r^2)^2}{2\pi r}
=
\frac{\pi}{2}m_R^2r^3.
\]

Integrating in radius and axial coordinate therefore gives a bound of the form

\[
\boxed{
\int_C|v|^2dY
\ge
c_2m_R^2a^5
}
\]

with an absolute positive geometric constant \(c_2\). A conservative choice is sufficient; no sharp constant is needed downstream.

Since

\[
m_R\sim R^{-2},
\qquad a\sim R,
\]

this has the critical scaling

\[
\boxed{
\int_C|U-\bar U_C|^2dY
\ge c_V R
}
\]

with

\[
c_V=c_V(\phi_0,A_0,K_1,\delta_{geom})>0.
\]

## 5. Variance gives fixed \(L^3\) mass

The cylinder volume satisfies

\[
|C|=c_CR^3.
\]

By Hölder,

\[
\int_C|v|^3dY
\ge
\frac{\left(\int_C|v|^2dY\right)^{3/2}}
{|C|^{1/2}}.
\]

Using the critical variance lower bound,

\[
\int_C|v|^3dY
\ge c_3>0.
\]

Moreover the mean projection obeys

\[
\|U-\bar U_C\|_{L^3(C)}
\le2\|U\|_{L^3(C)},
\]

so

\[
\boxed{
\int_C|U|^3dY
\ge
c_{flux}>0,
}
\]

where \(c_{flux}\) depends only on the fixed coherent-flux and analyticity constants, not on \(R\) or the stage.

This is the desired fixed critical shell charge.

Status: **PROVED UNDER THE STATED COHERENT EXPORT HYPOTHESES.**

## 6. Positive-frequency export gives many disjoint charged shells

Suppose permanent export occurs with lower Leray-time event frequency

\[
\underline\rho_{exp}>0.
\]

The passive dilation conveyor carries an export born at \(s_e\) to

\[
R(s)\propto e^{(s-s_e)/2}.
\]

Thin the export event set by a fixed factor so that consecutive retained event times differ enough for their late-time shell neighborhoods to be disjoint.

Because the thinning factor is fixed, the retained event frequency remains positive.

At a sufficiently late observation time \(s\), the number \(N(s)\) of disjoint permanent-export shell populations then satisfies

\[
\boxed{
N(s)
\ge
c_{sep}\,\underline\rho_{exp}\,s-o(s)
}
\]

after choosing an origin in Leray time.

Summing the disjoint \(L^3\) charges gives

\[
\boxed{
\|U(s)\|_3^3
\ge
c_{flux}N(s)
\ge
c_*s-o(s).
}
\]

## 7. First-hitting stage form

At the first-hitting times,

\[
s_j=j\log q+O(1).
\]

Therefore permanent coherent positive-frequency export implies

\[
\boxed{
\|U(s_j)\|_3^3
\ge
c_*j\log q-O(1).
}
\]

Equivalently, using

\[
W_j(T^*-t_j)\asymp1,
\]

one has

\[
\boxed{
\|U(s_j)\|_3^3
\gtrsim
\log\frac1{T^*-t_j}
}
\]

up to fixed additive/multiplicative constants on the corridor.

## 8. Physical \(L^3\) form

Under the first-hitting normalization

\[
u(x,t_j)
=\sqrt{\nu W_j}\,U(Y,s_j),
\qquad
Y=\frac{x-X_j}{r_j},
\qquad
r_j=\sqrt{\frac\nu{W_j}},
\]

one has the exact scale-critical identity

\[
\boxed{
\|u(t_j)\|_{L^3_x}^3
=\nu^3\|U(s_j)\|_{L^3_Y}^3.
}
\]

Hence the permanent coherent export branch forces

\[
\boxed{
\|u(t_j)\|_3
\gtrsim
\nu\left(\log\frac1{T^*-t_j}\right)^{1/3}.
}
\]

The dimensional factor is tied to the normalization used throughout this repository.

## 9. Why this is not yet a contradiction

The Navier--Stokes regularity theory excludes blow-up under a uniform strong \(L^3\) bound, but a hypothetical singular solution is allowed to have \(\|u(t)\|_3\to\infty\).

The lower bound above therefore strengthens the description of the survivor without closing it.

It shows that positive-frequency permanent export is exactly a strong-\(L^3\) stacking mechanism.

At the same time the corresponding critical enstrophy shell costs are geometrically summable.

## 10. Lorentz endpoint interpretation

For an ideal critical conveyor \(U\sim R^{-1}\) over an increasing number of logarithmic shells:

- strong \(L^3\) counts each shell and grows with the number of shells;
- finite Lorentz \(L^{3,q}\), \(q<\infty\), also detects accumulation across scales;
- weak \(L^{3,\infty}\) can remain order one because the amplitude-volume relation stays exactly critical.

Thus the permanent-export survivor lands on the weak-\(L^3\) endpoint rather than contradicting the known strong critical criteria.

## 11. Audit verdict

### PROVED UNDER COHERENT EXPORT HYPOTHESES

- fixed directed flux + ancestor-scale derivative control gives a critical vorticity patch;
- circulation gives local variance \(\gtrsim R\);
- Hölder gives a scale-independent positive \(L^3\) shell charge;
- positive-frequency permanent export gives linearly many disjoint charged shells in Leray time;
- therefore \(\|U(s_j)\|_3^3\gtrsim s_j\sim j\log q\).

### ROUTED COMPLEMENTS

Failure of coherent cross-section geometry, direction, or derivative control is sent to the existing projective/noncoherent/H branch rather than counted as a quiet export.

### OPEN

The resulting logarithmic strong-\(L^3\) growth is compatible with a hypothetical singularity and does not by itself prove regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
