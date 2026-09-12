# DSD M19-123 — Long-period RDSS and aperiodic recurrence share the same transverse-stability obstruction after the M19-120 correction

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-119 INVARIANT-MEASURE LIMIT RECOMBINED WITH THE AUTHORITATIVE M19-120 TRANSVERSE-STABILITY CORRECTION / LONG-PERIOD RELATIVE-PERIODIC COMPLEXITY IS NOT A THIRD INDEPENDENT HARD ROOT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

M19-119 associates to every compact long-period RDSS sequence

\[
U_n(s+S_n)=Q_nU_n(s),
\qquad
S_n\to\infty,
\]

an invariant quotient probability measure

\[
\mu_n
=
\frac1{S_n}\int_0^{S_n}\delta_{[U_n(s)]}\,ds
\stackrel{*}{\rightharpoonup}\mu.
\]

Ergodic components of `mu` are recurrent.

M19-120 corrects the earlier center-only reduction: genuinely aperiodic recurrent dynamics may exist even when the flow tangent is the only zero exponent if positive transverse exponents are present.

The correct theorem target is

\[
\boxed{
\mathcal T_{transverse}:E^{\ge0}_\perp=\{0\}
}
\]

or equivalently

\[
\lambda_{top}^\perp<0.
\]

---

## 2. Consequence of uniform transverse stability

Assume the compact recurrent quotient corridor admits a uniform dominated splitting

\[
T\mathcal X_{quot}
=E^c\oplus E^s,
\]

with

\[
E^c=\operatorname{span}\{X\},
\qquad
\|D\widehat\Phi_t|_{E^s}\|
\le Ce^{-\gamma t}
\]

for some

\[
\gamma>0,
\]

and no unstable bundle.

Under the standard normally-hyperbolic/local-center-foliation hypotheses, recurrent dynamics in a sufficiently small invariant neighborhood is confined to the one-dimensional flow center after stable fibers contract.

An ergodic recurrent component is then:

- a quotient equilibrium; or
- a periodic quotient orbit.

Lifting gives RSS or RDSS.

Thus under the **strong transverse-stability theorem**, M19-119 strengthens to

\[
\boxed{
\mu
\text{ is a barycenter of RSS/RDSS ergodic invariant measures}
}
\]

on the compact branch.

---

## 3. Contrapositive interpretation

Suppose instead that the long-period invariant-measure limit has a genuinely aperiodic ergodic component.

Then the quotient recurrent set cannot have all transverse directions uniformly contracting.

Therefore at least one of the following must occur:

\[
\boxed{
\lambda_{top}^\perp\ge0
\quad\lor\quad
\text{failure of the uniform dominated/compact corridor}.
}
\]

The first branch is exactly the finite-dimensional spectral obstruction of M19-121--122.

The second is an already explicit compactness/strong-exit branch.

Hence

\[
\boxed{
\text{aperiodic long-period limit}
\Longrightarrow
\mathcal T_{transverse}\text{ failure}
\lor
G_{compactness\ loss}.
}
\]

---

## 4. Hyperbolic periodic proliferation

A sequence of periodic orbits with

\[
S_n\to\infty
\]

is entirely compatible with a compact uniformly hyperbolic recurrent set having one flow-center direction and nontrivial stable/unstable bundles.

Indeed such sets typically contain infinitely many periodic orbits of increasing period.

Therefore

\[
\boxed{
\text{unbounded RDSS periods}
\text{ can be a signature of the same transverse unstable dynamics that supports aperiodic recurrence}.
}
\]

This is precisely why M19-120 was necessary.

---

## 5. No new independent long-period theorem if transverse stability is closed

If M19-121--122 are upgraded to a proof of

\[
E^{\ge0}_\perp=0
\]

uniformly on the retained recurrent corridor, then the long-period branch no longer requires a separate chaotic-limit theorem.

Its invariant measures reduce to structured RSS/RDSS measures or compactness loss.

The remaining periodic problem is then the existence/nonexistence of the structured RSS/RDSS orbits themselves.

Thus

\[
\boxed{
\mathcal R_{S\to\infty}
\text{ and }\mathcal R_{aperiodic}
\text{ share the same transverse-stability obstruction.}
}

---

## 6. What still remains after transverse stability

Even if all aperiodic/hyperbolic recurrence is removed, isolated RSS/RDSS orbits may remain.

M19-113--114 make clear that their intrinsic period/holonomy moduli do not become free external parameters, and augmented nondegeneracy does not imply nonexistence.

Therefore the global recurrent critical branch still has two conceptually distinct tasks:

\[
\boxed{
\begin{aligned}
&\textbf{A. }\mathcal T_{transverse}:\ E^{\ge0}_\perp=0,\\
&\textbf{B. }\mathcal T_{relative\text{-}periodic}:\ \text{exclude the remaining finite-amplitude RSS/RDSS orbits.}
\end{aligned}
}
\]

The long-period measure bridge does not add a third independent analytic root.

---

## 7. Revised frontier compression

Under compactness, the recurrent critical problem is now best organized as

\[
\boxed{
\text{recurrent critical survivor}
\Longrightarrow
\begin{cases}
\text{transverse nonnegative dynamics},\\
\text{or structured RSS/RDSS orbit}.
\end{cases}
}
\]

The first is the finite-dimensional Lyapunov/Ky-Fan theorem.

The second is the nonlinear relative-periodic Liouville theorem.

---

## 8. Firewall

Uniform negative transverse Lyapunov exponents plus the required dominated/invariant-manifold structure is stronger than merely knowing that each individual transverse exponent is negative almost everywhere for one invariant measure.

Therefore later modules must distinguish:

\[
\boxed{
\text{measurewise negativity}
\neq
\text{uniform normal contraction}.
}
\]

The latter is what supports the clean RSS/RDSS reduction used here.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
