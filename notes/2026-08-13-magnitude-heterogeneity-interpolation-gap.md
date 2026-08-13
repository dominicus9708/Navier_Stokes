# Magnitude-heterogeneity gap in the critical `L2-L3-L6` interpolation

Date: 2026-08-13

Status: **DERIVED MOMENT/INTERPOLATION DEFICIT + DSD MAGNITUDE-DISTRIBUTION CHANNEL / OPEN FLUX-RIGIDITY CLOSURE**.

The generic enstrophy-production estimate uses the interpolation

\[
\|\omega\|_3
\le
\|\omega\|_2^{1/2}\|\omega\|_6^{1/2}.
\]

This step is itself strictly depleted unless the vorticity magnitude is nearly constant with respect to the enstrophy-weighted distribution.  The resulting deficit is dimensionless and combines multiplicatively with the magnitude/direction palinstrophy deficit.

---

## 1. Enstrophy-weighted probability measure

Let

\[
\rho=|\omega|,
\qquad
E=\int\rho^2dx>0.
\]

Define the probability measure

\[
\boxed{
d\mu
=\frac{\rho^2}{E}dx.
}
\]

Let

\[
m_1=\mathbb E_\mu[\rho]
=\frac{\int\rho^3dx}{E},
\]

\[
m_2=\mathbb E_\mu[\rho^2]
=\frac{\int\rho^4dx}{E},
\]

\[
m_4=\mathbb E_\mu[\rho^4]
=\frac{\int\rho^6dx}{E}.
\]

Define the enstrophy-weighted magnitude variance

\[
\boxed{
v_{\rm mag}
=m_2-m_1^2
=\operatorname{Var}_\mu(\rho).
}
\]

and the dimensionless coefficient of variation

\[
\boxed{
\chi_{\rm mag}
=\frac{v_{\rm mag}}{m_1^2}
\ge0.
}
\]

---

## 2. Exact interpolation ratio

The cubed interpolation ratio is

\[
\mathcal R_{\rm int}
=\frac{
\|\rho\|_3^3
}{
\|\rho\|_2^{3/2}
\|\rho\|_6^{3/2}
}.
\]

Using the weighted moments,

\[
\|\rho\|_3^3=Em_1,
\]

and

\[
\|\rho\|_2^{3/2}\|\rho\|_6^{3/2}
=E m_4^{1/4}.
\]

Hence

\[
\boxed{
\mathcal R_{\rm int}
=\frac{m_1}{m_4^{1/4}}.
}
\]

---

## 3. Variance forces a strict interpolation deficit

Cauchy--Schwarz/Jensen gives

\[
m_4
=\mathbb E_\mu[\rho^4]
\ge
\left(\mathbb E_\mu[\rho^2]\right)^2
=m_2^2.
\]

Since

\[
m_2=m_1^2+v_{\rm mag},
\]

we obtain

\[
\boxed{
\mathcal R_{\rm int}
\le
\frac{m_1}
{(m_1^2+v_{\rm mag})^{1/2}}
=
(1+\chi_{\rm mag})^{-1/2}.
}
\]

Thus the generic interpolation constant can be approached only when

\[
\boxed{
\chi_{\rm mag}\to0.
}
\]

That is: the vorticity magnitude must become nearly constant under its own enstrophy-weighted measure.

---

## 4. Scaling

Under Navier--Stokes scaling,

\[
\rho\mapsto\lambda^2\rho.
\]

Therefore

\[
m_1\mapsto\lambda^2m_1,
\qquad
v_{\rm mag}\mapsto\lambda^4v_{\rm mag},
\]

and

\[
\boxed{
\chi_{\rm mag}\mapsto\chi_{\rm mag}.
}
\]

Hence `chi_mag` is a valid scale-invariant DSD channel for the natural-window renormalization.

---

## 5. Combine with the angular palinstrophy gap

The previous source estimate was

\[
|Q|
\le
C_*E^{3/4}
(P-P_{\rm ang})^{3/4}.
\]

Keeping the actual interpolation ratio yields the stronger bound

\[
\boxed{
|Q|
\le
C_*E^{3/4}
(P-P_{\rm ang})^{3/4}
(1+\chi_{\rm mag})^{-1/2}.
}
\]

Equivalently, with

\[
\eta_{\rm ang}=P_{\rm ang}/P,
\]

\[
\boxed{
|Q|
\le
C_*E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4}
(1+\chi_{\rm mag})^{-1/2}.
}
\]

Thus there are at least two independent coefficient-level depletion mechanisms before any additional direction-coherence theorem is used:

1. **directional heterogeneity:** `eta_ang>0`;
2. **magnitude heterogeneity:** `chi_mag>0`.

---

## 6. Saturation consequence

A residual state that attempts to saturate the generic critical source must satisfy simultaneously

\[
\boxed{
\eta_{\rm ang}\to0,
\qquad
\chi_{\rm mag}\to0.
}
\]

Interpretation:

- very little palinstrophy can be spent on changing vorticity direction;
- the enstrophy-bearing vorticity magnitude must be almost single-level.

Therefore the saturation profile is pushed toward an approximately **oriented, nearly constant-magnitude vorticity core**.

This is exactly the geometry already typed by the polarity/oriented-flux track.

---

## 7. Link back to flux geometry

If the saturation core is also projectively close to one axis, then the remaining degree of freedom is polarity.

- mixed polarity forces scalar axial variance and palinstrophy;
- one dominant polarity produces a robust signed axial flux;
- signed flux cannot terminate freely because `div omega=0`;
- material flux changes only through the viscous boundary derivative channel.

Hence the interpolation equality regime is not a new free branch.  It feeds back into the previously derived polarity/flux/material-surface geometry.

The proof-producing next question is quantitative: does small `eta_ang` and small `chi_mag` on a thick natural core force enough coherent signed flux to activate the flux-cost lemmas with a uniform coefficient?

---

## 8. New DSD static block

At each normalized dangerous window retain

\[
\boxed{
\mathsf H_{\rm mag-dir}
=
(
\eta_{\rm ang},
\chi_{\rm mag},
J,
\Pi,
\theta_+,
\theta_-,
\Phi
).
}
\]

These channels separate quantities that a single scalar enstrophy cannot distinguish:

- magnitude variability;
- directional variability;
- projective axis dispersion;
- orientation/polarity;
- signed flux.

This is a direct use of the DSD channel-resolved static aggregation discipline.

Status: **OPEN SMALL-DEFICIT -> COHERENT-FLUX RIGIDITY BRIDGE**.
