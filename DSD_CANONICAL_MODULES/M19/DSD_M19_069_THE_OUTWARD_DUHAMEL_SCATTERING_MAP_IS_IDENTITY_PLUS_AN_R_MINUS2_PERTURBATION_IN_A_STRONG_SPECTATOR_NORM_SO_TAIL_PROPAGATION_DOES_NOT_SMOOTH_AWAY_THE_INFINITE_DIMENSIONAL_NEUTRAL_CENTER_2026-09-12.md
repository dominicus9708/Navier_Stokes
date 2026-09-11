# M19-069 — The outward Duhamel scattering map is identity plus an R^-2 perturbation in a strong spectator norm, so tail propagation does not smooth away the infinite-dimensional neutral center

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / LINEARIZED SCATTERING MAP / CONDITIONAL LOCAL BI-LIPSCHITZ THEOREM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-068 showed that the formal critical scattering sector has infinitely many neutral leading modes.  A possible rescue would be that the **outward scattering map** from a finite spectator boundary to infinity strongly smooths or compactifies those modes, leaving only the time-translation tangent realizable.

The exact M5-563/M5-567 dilation-characteristic equation shows the opposite structure.

Along a sufficiently remote quiet spectator characteristic, the scattering datum is the finite-radius critical profile plus an integrable \(O(R_0^{-2})\) Duhamel correction.  Under a strong spectator norm in which the residual map is uniformly locally Lipschitz, the linearized scattering map is

\[
\boxed{D\mathscr S_{R_0}=I+O(R_0^{-2}).}
\]

For large enough \(R_0\), it is locally invertible and bi-Lipschitz.  Hence outward tail propagation does not remove the infinite-dimensional neutral boundary degrees of freedom.

The remaining realizability restriction, if any, must already act on the **finite spectator-boundary history supplied by the interior solution**.

## 2. Exact outward characteristic equation

M5-563 defines

\[
R(\tau)=R_0e^{\tau/2},
\qquad
V(\xi,\tau)
=R(\tau)U(R(\tau)\xi,\theta_0+\tau),
\]

and derives the exact equation

\[
\boxed{
\partial_\tau V
=R_0^{-2}e^{-\tau}\mathcal R[V,P],
}
\]

where

\[
\mathcal R[V,P]
:=
\nu\Delta_\xi V
-(V\cdot\nabla_\xi)V
-\nabla_\xi P
\]

with the appropriate viscosity normalization.

The key structural fact is the exponentially integrable coefficient

\[
\boxed{R_0^{-2}e^{-\tau}.}
\]

## 3. Exact nonlinear scattering representation

Integrating from \(0\) to \(\tau\),

\[
V(\tau)
=
V(0)
+R_0^{-2}
\int_0^\tau e^{-s}\mathcal R[V(s),P(s)]ds.
\]

M5-567 shows that \(V(\tau)\) converges in the fixed-annulus spectator norm as \(\tau\to\infty\).  Therefore

\[
\boxed{
A
=
V(0)
+R_0^{-2}
\int_0^\infty e^{-s}\mathcal R[V(s),P(s)]ds.
}
\]

Thus the scattering map from one spectator-boundary characteristic profile to its asymptotic datum has the form

\[
\boxed{
\mathscr S_{R_0}=I+\mathcal K_{R_0},
}
\]

with a nonlinear correction whose size is \(O(R_0^{-2})\) on the quiet spectator corridor.

## 4. Strong spectator norm needed for linearization

M5-563 certifies a uniform residual bound in a strong fixed-annulus norm after derivative/pressure exits have been removed.

For the present linearized statement, use a Banach norm \(X\) strong enough that on the retained compact spectator family

\[
\boxed{
\|D\mathcal R[V,P]H\|_X
\le L_{spec}\|H\|_X
}
\]

for all admissible divergence-free perturbations \(H\), with pressure variation estimated in the same enlarged-annulus framework.

This uniform Frechet-derivative bound is slightly stronger than the residual-size bound alone.  It is the explicit hypothesis under which the local bi-Lipschitz conclusion below is certified.

Failure of such a strong linearized spectator bound is itself a derivative/pressure compactness failure and must not be silently discarded.

## 5. Linearized outward equation

Let \(V_\varepsilon\) be a smooth one-parameter family of spectator solutions and set

\[
H(\tau)
:=
\left.\frac d{d\varepsilon}\right|_{\varepsilon=0}V_\varepsilon(\tau).
\]

Then

\[
\boxed{
\partial_\tau H
=R_0^{-2}e^{-\tau}
D\mathcal R_{V(\tau)}H.
}
\]

Hence

\[
\frac d{d\tau}\|H(\tau)\|_X
\le
L_{spec}R_0^{-2}e^{-\tau}
\|H(\tau)\|_X.
\]

Gronwall gives

\[
\boxed{
\|H(\tau)\|_X
\le
\exp\left(L_{spec}R_0^{-2}\right)
\|H(0)\|_X
}
\]

uniformly for all \(\tau\ge0\).

## 6. Derivative of the scattering map is near identity

Differentiate the Duhamel scattering formula:

\[
D\mathscr S_{R_0}H(0)
=
H(0)
+R_0^{-2}
\int_0^\infty e^{-s}
D\mathcal R_{V(s)}H(s)ds.
\]

Therefore

\[
\begin{aligned}
\|D\mathscr S_{R_0}H(0)-H(0)\|_X
&\le
L_{spec}R_0^{-2}
\int_0^\infty e^{-s}\|H(s)\|_Xds\\
&\le
L_{spec}R_0^{-2}
 e^{L_{spec}R_0^{-2}}
\|H(0)\|_X.
\end{aligned}
\]

Define

\[
\boxed{
\varepsilon_{R_0}
:=
L_{spec}R_0^{-2}
 e^{L_{spec}R_0^{-2}}.
}
\]

Then

\[
\boxed{
\|D\mathscr S_{R_0}-I\|_{X\to X}
\le
\varepsilon_{R_0}
=O(R_0^{-2}).
}
\]

## 7. Local invertibility for a sufficiently remote spectator boundary

Choose \(R_0\) so large that

\[
\varepsilon_{R_0}<1.
\]

Then

\[
D\mathscr S_{R_0}
=I+K,
\qquad
\|K\|<1.
\]

The Neumann-series theorem gives invertibility, with

\[
\boxed{
(1-\varepsilon_{R_0})\|H\|_X
\le
\|D\mathscr S_{R_0}H\|_X
\le
(1+\varepsilon_{R_0})\|H\|_X.
}
\]

Therefore the scattering map is locally bi-Lipschitz in this strong spectator topology.

In particular it is not a compact smoothing map there.

## 8. Boundary-history version

At a fixed spectator radius \(R_{spec}\), the characteristic label satisfies

\[
q=\log R_{spec}-\frac{\theta_{cross}}2.
\]

Thus the full scattering function \(A(q,\omega)\) is the finite-radius boundary history reparameterized by \(q\), plus the uniformly small outward Duhamel correction.

Schematically,

\[
\boxed{
A(q)
=
\mathcal B(\theta=2(\log R_{spec}-q))
+O_X(R_{spec}^{-2}),
}
\]

where \(\mathcal B\) is the critical rescaled profile crossing the spectator annulus.

Hence high-frequency, quasiperiodic, or other infinite-dimensional time dependence present in the spectator-boundary history is not filtered out merely by outward propagation.

## 9. Consequence for center simplicity

M19-068 exposed infinitely many formal neutral scattering modes.  M19-069 shows that, conditional on strong spectator linearized control, the outward map from the spectator boundary to infinity is locally invertible and near identity.

Therefore

\[
\boxed{
\text{tail propagation does not reduce the neutral center dimension.}
}
\]

Any theorem reducing the realizable center to the single time-translation mode must act **before** the outward spectator conveyor, namely on the finite-radius boundary histories that can be generated by a complete recurrent Navier--Stokes interior.

The frontier is therefore sharpened to

\[
\boxed{
\mathcal T_{boundary}^{real}:
\text{classify recurrent finite-spectator-boundary histories realizable by the retained interior dynamics}.}
\]

## 10. Important firewall

The result does not say that an arbitrary boundary history can be prescribed independently for Navier--Stokes.  The spectator boundary is not an external boundary condition; it is an observation surface inside the whole-space solution.

The local bi-Lipschitz statement concerns

\[
\text{already realizable spectator perturbations}
\longleftrightarrow
\text{their scattering perturbations}.
\]

Thus

\[
\boxed{
\text{near-identity outward scattering}
\neq
\text{surjectivity of arbitrary boundary data from the core}.}
\]

The latter is exactly the remaining global realizability problem.

## 11. Certified / conditional / not certified

### Certified from the exact M5-563/567 conveyor

1. The scattering datum equals the spectator profile plus an exponentially integrable \(O(R_0^{-2})\) Duhamel correction.
2. Outward tail propagation carries no large dissipative coefficient; all PDE correction is weighted by \(R_0^{-2}e^{-\tau}\).

### Conditional on uniform strong linearized spectator control

1. \(D\mathscr S_{R_0}=I+O(R_0^{-2})\) in the chosen strong norm.
2. For sufficiently large \(R_0\), the derivative is invertible and near-isometric.
3. Thus the outward scattering map does not compactify/smooth the neutral center in that topology.

### Not certified

1. Surjectivity of arbitrary spectator-boundary histories from the interior.
2. One-dimensionality of the realizable boundary center.
3. Global weak-critical factor rigidity.
4. Global 3D Navier--Stokes regularity.

## 12. Next target

M19-070 should attack the finite spectator-boundary history itself.

The exact boundary-history relation suggests working with one fixed finite radius and asking whether the trace

\[
\theta\mapsto U(R_{spec}\omega,\theta)
\]

of a compact recurrent ancient whole-space solution can support an aperiodic quasiperiodic component.

Spatial parabolic smoothing alone is unlikely to forbid this because the observation surface is finite and the dynamics are autonomous.  The next calculation should therefore examine the **temporal frequency response** of the linearized interior similarity operator to a boundary-history mode \(e^{i\lambda\theta}\), and determine whether nonzero real temporal frequencies can remain bounded/regular in the whole-space interior.

If the interior resolvent has no imaginary-axis modes except the time tangent, center simplicity becomes plausible.  If imaginary-axis modes exist at the linearized level, the realizability frontier remains genuinely nonlinear/spectral.

---

\[
\boxed{\text{M19-069 COMPLETE; OUTWARD SCATTERING IS NEAR IDENTITY, SO THE LAST CENTER-SELECTION PROBLEM LIVES AT THE FINITE SPECTATOR BOUNDARY/INTERIOR INTERFACE.}}
\]
