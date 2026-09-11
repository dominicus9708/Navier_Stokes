# M19-053 — Translation invariance of local kinetic and palinstrophy resources proves the J^{1/4} gap is positional, not derivative

**Date:** 2026-09-11  
**Status:** CALCULATION / ANTI-PROOF FIREWALL / MIXED-RESOURCE CENTER-COHERENCE AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-050 gives, on the first-hitting center-proximity branch,

\[
\mathcal M^{com}
\gtrsim
J^{5/4}
\]

rather than the own-scale charge \(J\).

M19-052 adds the simultaneous scale-matched palinstrophy floor

\[
P
\gtrsim
J/\rho^3.
\]

A natural hope is that a mixed kinetic-palinstrophy interpolation might restore the missing factor \(J^{1/4}\).

The present module shows that no purely translation-invariant local resource combination can do so.

The gap is positional: it measures distance from the chosen common center, while kinetic energy and palinstrophy are unchanged by spatial translation.

## 2. Use the M19-051 packet family

Let \((u_{J,\rho},\omega_{J,\rho})\) be the smooth divergence-free packet of M19-051, centered at the origin.

It satisfies

\[
\boxed{
\|u\|_2^2\asymp J\rho,
}
\]

\[
\boxed{
\|\omega\|_2^2\asymp J/\rho,
}
\]

and

\[
\boxed{
\|\nabla\omega\|_2^2\asymp J/\rho^3.
}
\]

The own-scale kinetic Morrey charge is

\[
\boxed{
\rho^{-1}\|u\|_2^2\asymp J.
}
\]

The amplitude-natural scale is

\[
\boxed{
r_A\asymp\rho J^{-1/4}.}
\]

## 3. Translate the packet without changing its local resources

For a displacement vector \(z\in\mathbb R^3\), define

\[
u_z(x):=u(x-z),
\qquad
\omega_z(x):=\omega(x-z).
\]

Then exactly

\[
\boxed{
\|u_z\|_2=\|u\|_2,
}
\]

\[
\boxed{
\|\omega_z\|_2=\|\omega\|_2,
}
\]

and

\[
\boxed{
\|\nabla\omega_z\|_2
=\|\nabla\omega\|_2.
}
\]

Likewise every translation-invariant Sobolev/Lorentz norm or algebraic combination of these norms remains unchanged.

Therefore local kinetic, enstrophy, palinstrophy, higher derivative, and weak-\(L^3\) magnitudes contain no information about \(|z|\).

## 4. Common-center Morrey charge does depend on z

Choose the common center to be the origin and translate the packet to distance

\[
|z|=d.
\]

A ball centered at the origin that contains the packet must have radius

\[
R_{com}\asymp d+\rho.
\]

Its kinetic Morrey charge satisfies

\[
\mathcal M^{com}
\asymp
\frac{\|u\|_2^2}{d+\rho}
\asymp
\frac{J\rho}{d+\rho}.
\]

Take specifically

\[
\boxed{d\asymp r_A=\rho J^{-1/4}.}
\]

For \(J\ll1\),

\[
d\gg\rho,
\]

and therefore

\[
\boxed{
\mathcal M^{com}
\asymp
\frac{J\rho}{\rho J^{-1/4}}
=J^{5/4}.}
\]

This exactly saturates the M19-050 center-nesting lower scale.

## 5. Palinstrophy does not repair the loss

The translated packet still has

\[
P\asymp J/\rho^3.
\]

Thus the pair of scale-invariant own-packet charges

\[
\boxed{
\rho^{-1}\|u\|_2^2\asymp J,
\qquad
\rho^3P\asymp J
}
\]

is identical before and after translation.

Yet the common-center kinetic charge has changed from order \(J\) to order \(J^{5/4}\).

Therefore no inequality of the form

\[
\boxed{
\mathcal M^{com}
\ge
F\left(
\rho^{-1}\|u\|_2^2,
\rho^3P,
\ldots
\right)
}
\]

with \(F\gtrsim J\) can hold universally if the arguments of \(F\) consist only of translation-invariant local magnitude resources and no center-position variable.

## 6. Mixed homogeneous combinations are not positional observables

At the larger radius \(r_A\), the two normalized charges scale as

\[
\frac{\|u\|_2^2}{r_A}
\asymp
J^{5/4},
\]

and

\[
r_A^3P
\asymp
J^{1/4}.
\]

One can algebraically form, for example,

\[
\left(J^{5/4}\right)^{3/4}
\left(J^{1/4}\right)^{1/4}
=J.
\]

But this algebraic recovery of exponent \(J\) does not yield a lower bound on common-center kinetic mass.

The mixed number is still unchanged by translating the packet, whereas the common-center Morrey charge is not.

Thus exponent matching is not enough.

\[
\boxed{
\text{homogeneity matching}
\neq
\text{center-coherence control}.
}
\]

## 7. Relation to local interpolation identities

The whole-space interpolation

\[
\|\omega\|_2^2
\lesssim
\|u\|_2\|\nabla\omega\|_2
\]

and its localized cutoff analogues are also translation invariant.

The M19-051 packet essentially saturates the scale:

\[
\frac J\rho
\asymp
(J\rho)^{1/2}
(J/\rho^3)^{1/2}.
\]

Therefore interpolation between kinetic and derivative resources cannot encode where the packet sits relative to the terminal center.

No additional derivative order fixes this conceptual issue unless the derivative estimate is coupled to an explicitly centered weight/moment.

## 8. What kind of observable could close the gap

To control eccentricity one needs a genuinely positional quantity, for example a weighted moment such as

\[
\int |x-X_*|^\alpha |\omega|^2dx,
\]

or a center-cocycle / transport identity involving

\[
X_{j+1}-X_j,
\]

or an interaction with a fixed parent boundary/pressure field that distinguishes translations.

Ordinary unweighted Sobolev norms cannot provide this information.

Thus the next theorem must use **spatial transport/coherence**, not another unweighted derivative interpolation.

## 9. Consequence for the R-AC strategy

M19-046 retired return count as the primary closure mechanism.

M19-047--052 exposed simultaneous kinetic and derivative concentration.

M19-053 now proves that those local magnitude resources alone cannot remove the remaining spatial center loss.

Hence the current hard endpoint is

\[
\boxed{
\mathcal T_{center}^{pos}:
\text{control the position/eccentricity of cubic-mass-bearing terminal packets relative to one first-hitting center genealogy}.
}
\]

Equivalently, one needs either

\[
\boxed{
\eta_k=O(1)
}

on a cubic-mass-divergent subset, or a positional/transport cost for

\[
\eta_k\to\infty.
\]

## 10. Off-center packet is not automatically a formed remote satellite

The translated anti-model also clarifies a scope issue.

A packet of radius \(\rho\) placed at distance \(r_A\) from the main center has distance-to-packet-size ratio

\[
\frac{r_A}{\rho}
\asymp
J^{-1/4}\to\infty.
\]

But its flux and critical norm shrink with \(J\):

\[
\Phi_{packet}\sim J^{1/2},
\qquad
\|u\|_{L^{3,\infty}}\sim J^{1/2}.
\]

Therefore it need not satisfy the fixed-strength active-source hypotheses used by the formed-remote theorem.

This is why the sub-natural off-center branch cannot simply be relabeled as a strong remote satellite.

## 11. Next target

The next calculation should build the lowest-order positional observable available from the equations.

The natural candidates are:

1. vorticity-enstrophy barycenter relative to the first-hitting center;
2. a truncated first spatial moment
   \[
   \int \chi_R(x)|x-X_*||\omega|^2dx;
   \]
3. the exact center-cocycle increments \(X_{j+1}-X_j\) from first-hitting normalization;
4. pressure/nonlocal-strain coupling between an off-center packet and the main core.

The observable must be audited for translation/Galilean covariance and for whether its time derivative introduces a finite or signed parent budget.

---

\[
\boxed{\text{M19-053 COMPLETE; THE REMAINING J^{1/4} LOSS IS A POSITIONAL COHERENCE PROBLEM, NOT A MISSING DERIVATIVE ESTIMATE.}}
\]