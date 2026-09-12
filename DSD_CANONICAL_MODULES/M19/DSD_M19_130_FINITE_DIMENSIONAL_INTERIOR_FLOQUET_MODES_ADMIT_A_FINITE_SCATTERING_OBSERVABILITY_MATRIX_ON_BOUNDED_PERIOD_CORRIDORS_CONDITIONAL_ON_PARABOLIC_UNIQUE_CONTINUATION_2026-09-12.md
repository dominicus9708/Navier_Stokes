# DSD M19-130 — Finite-dimensional interior Floquet modes admit a finite scattering observability matrix on bounded-period corridors, conditional on parabolic unique continuation

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / FINITE-DIMENSIONAL INTERIOR-TO-TAIL MATCHING REDUCTION / M19-095 QUASI-COMPACTNESS PLUS M19-069 NEAR-IDENTITY SCATTERING AND PARABOLIC UNIQUE CONTINUATION MAKE THE FULL SCATTERING OBSERVATION INJECTIVE ON THE FINITE FLOQUET HARD CORE / FINITELY MANY TAIL FUNCTIONALS THEN SUFFICE TO DETECT ALL INTERIOR MODES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Interior finite-dimensional hard space

Fix a bounded-period DSS or RDSS orbit on the retained smooth compact corridor.

M19-101/M19-109 give

\[
r_{ess}(\mathcal M_S^{tw})<1.
\]

Hence the spectral subspace associated with unit or nonnegative relevant Floquet multipliers is finite-dimensional.

After exact phase/rotation gauge bookkeeping, let

\[
\boxed{E_F\subset X}
\]

be a finite-dimensional interior Floquet hard space of dimension

\[
N_F<\infty.
\]

A vector

\[
W_0\in E_F
\]

generates a complete linearized perturbation

\[
W(s).
\]

---

## 2. Spectator observation

Fix a sufficiently large finite spectator annulus

\[
A_{R_{spec}}.
\]

Let

\[
\mathcal O_{spec}W_0
\]

denote the complete one-period boundary/annular history of the normalized perturbation on that spectator region.

Schematically,

\[
\mathcal O_{spec}:E_F
\to
Y_{spec},
\]

where `Y_spec` is a Banach space of smooth annular histories over one period.

---

## 3. Conditional injectivity from unique continuation

Assume the standard strong unique-continuation property for the linearized parabolic Navier--Stokes system on the retained smooth background:

if a complete linearized perturbation vanishes on a nonempty open spacetime cylinder, then it vanishes identically.

Suppose

\[
\mathcal O_{spec}W_0=0.
\]

Then

\[
W(y,s)=0
\]

on the spectator annulus for all `s` in a nontrivial time interval.

Unique continuation gives

\[
W\equiv0.
\]

Hence

\[
W_0=0.
\]

Therefore

\[
\boxed{
\mathcal O_{spec}|_{E_F}
\text{ is injective}.
}
\]

This step is conditional on the stated unique-continuation theorem being available in the exact retained function class.

---

## 4. Transfer to scattering data

M19-069 gives, at sufficiently large spectator radius, a linearized scattering map

\[
D\mathscr S_{R_{spec}}
=I+\mathcal E,
\qquad
\|\mathcal E\|<1
\]

in a strong annular norm after choosing `R_spec` large enough.

Therefore

\[
D\mathscr S_{R_{spec}}
\]

is invertible by Neumann series on the spectator profile space.

Define the full linearized scattering observation

\[
\boxed{
\mathcal O_{scatt}
:=
D\mathscr S_{R_{spec}}\circ\mathcal O_{spec}.
}
\]

Then

\[
\boxed{
\mathcal O_{scatt}|_{E_F}
\text{ is injective}.
}
\]

Thus no nonzero interior Floquet hard mode can be completely invisible in the full scattering history.

---

## 5. Finite-dimensional output reduction

The domain

\[
E_F
\]

has dimension `N_F`.

Let

\[
Y_{scatt}
\]

be the scattering-history Banach space.

Because

\[
\mathcal O_{scatt}:E_F\to Y_{scatt}
\]

is injective and `E_F` is finite-dimensional, there exist finitely many continuous linear functionals

\[
\ell_1,\ldots,\ell_M\in Y_{scatt}^*,
\qquad
M\le N_F
\]

(after allowing `M=N_F` without loss) such that

\[
\boxed{
\mathbb O W
:=
\left(
\ell_1(\mathcal O_{scatt}W),\ldots,
\ell_M(\mathcal O_{scatt}W)
\right)
}
\]

is injective on `E_F`.

Equivalently, in suitable bases the interior-to-tail hard matching is represented by a finite matrix

\[
\boxed{
\mathbf O\in\mathbb C^{M\times N_F}
}
\]

of full column rank.

---

## 6. Choice of tail observables

The abstract functionals may be chosen from sufficiently rich scattering observables, for example finite combinations of:

- log-Fourier coefficients;
- vector spherical-harmonic coefficients;
- values against smooth compact q-window test functions;
- twisted Bloch coefficients in the RDSS representation of M19-128.

The finite-dimensional separation theorem guarantees that **some finite set** works once full scattering injectivity is known.

It does not yet prove that the particular low-mode set from M19-129 alone has full rank.

---

## 7. Relation to the finite low-mode tail core

M19-129 shows that the nonlinear base DSS tail has a nontrivial finite low-mode component on bounded-period corridors.

M19-130 is a linear statement: every finite-dimensional interior Floquet hard perturbation is detectable by finitely many scattering observables.

Together they give a finite-dimensional architecture on both sides:

\[
\boxed{
\text{interior Floquet hard modes}
\xrightarrow{\mathbf O}
\text{finite scattering observables}.
}
\]

The remaining issue is the rank and nonlinear compatibility of a **specific natural low-mode observation matrix**, not an infinite-dimensional tail matching problem.

---

## 8. Potential use for the extra-center theorem

If a symmetry-transverse zero/unstable interior mode existed, M19-130 forces a corresponding nonzero scattering variation in at least one finite observable.

Therefore a tail-side rigidity theorem showing that all such finite observables are exhausted by the exact time/rotation symmetries would imply

\[
E^{\ge0}_\perp=0.
\]

This gives a concrete finite-dimensional route to the transverse-stability theorem.

---

## 9. Firewall

Unique continuation gives injectivity, not a quantitative lower singular-value bound uniform over an entire parameter corridor.

For global rigidity one would need either:

\[
\boxed{
\sigma_{min}(\mathbf O)\ge c_{obs}>0
}
\]

uniformly, or a compactness argument preventing the observation matrix from losing rank along a sequence.

Thus

\[
\boxed{
\text{finite observability}
\neq
\text{uniform observability}.
}
\]

The latter is a genuine next theorem frontier.

---

## 10. Next target

On a compact bounded-period parameter/state corridor, test whether the finite observation matrices vary continuously and whether pointwise injectivity plus compactness yields

\[
\inf\sigma_{min}(\mathbf O)>0.
\]

This would turn qualitative unique continuation into a uniform tail-to-core observability inequality for the finite hard sector.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
