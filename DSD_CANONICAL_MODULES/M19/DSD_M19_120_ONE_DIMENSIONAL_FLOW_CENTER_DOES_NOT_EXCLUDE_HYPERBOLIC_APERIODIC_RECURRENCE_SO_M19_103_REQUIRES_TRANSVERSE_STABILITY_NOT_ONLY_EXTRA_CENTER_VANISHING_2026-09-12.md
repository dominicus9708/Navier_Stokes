# DSD M19-120 — One-dimensional flow center does not exclude hyperbolic aperiodic recurrence, so M19-103 requires transverse stability, not only extra-center vanishing

Date: 2026-09-12

Status: **AUTHORITATIVE M19 DYNAMICAL CORRECTION / THE CLAIM THAT A ONE-DIMENSIONAL CENTER GENERATED ONLY BY THE FLOW TANGENT FORCES A RECURRENT COMPONENT TO BE EQUILIBRIUM OR PERIODIC IS FALSE WITHOUT CONTROL OF UNSTABLE DIRECTIONS / APERIODIC HYPERBOLIC FLOWS HAVE EXACTLY ONE CENTER DIRECTION AND NONTRIVIAL STABLE/UNSTABLE BUNDLES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The overstrong step in M19-103

M19-103 argued conditionally that, after quotienting rotations,

\[
E^c_{quot}=\operatorname{span}\{\partial_sU\}
\]

would reduce a compact recurrent component to a one-dimensional center manifold and hence to equilibrium or a periodic orbit.

That implication is not valid for a general invariant recurrent set.

The missing issue is the possible presence of nontrivial stable and **unstable** directions.

---

## 2. Standard dynamical counterexample pattern

A uniformly hyperbolic flow may have a splitting

\[
\boxed{
T\mathcal K
=E^s\oplus E^c\oplus E^u,
\qquad
E^c=\operatorname{span}\{X\},
}
\]

where `X` is the flow vector field and

\[
\dim E^c=1.
\]

Nevertheless the invariant set may support:

- aperiodic recurrent orbits;
- positive topological entropy;
- infinitely many periodic orbits;
- ergodic invariant measures with positive Lyapunov exponents.

Anosov flows are the canonical example.

Thus

\[
\boxed{
\dim E^c=1
\not\Rightarrow
\text{one-dimensional recurrent dynamics}.
}
\]

The local center manifold does not contain the whole hyperbolic recurrent set; stable and unstable directions generate the surrounding invariant geometry.

---

## 3. Correct implication

To force a recurrent quotient component onto a one-dimensional flow curve, one needs more than

\[
E^c_{extra}=0.
\]

A sufficient spectral form would be

\[
\boxed{
E^u=\{0\},
\qquad
E^c=\operatorname{span}\{\partial_sU\},
}
\]

after symmetry quotient, together with the usual local invariant-manifold hypotheses.

Then every complete orbit remaining forever in a sufficiently small compact neighborhood is constrained to the one-dimensional center manifold because there is no unstable direction and stable directions contract toward it.

In that stronger setting, recurrent dynamics on the center manifold is equilibrium or periodic.

---

## 4. Revised live spectral theorem

The aperiodic theorem must therefore be strengthened from

\[
\mathcal T_{extra-center}:E^c_{extra}=0
\]

to a **transverse stability theorem**:

\[
\boxed{
\mathcal T_{transverse}:
\lambda_{top}^{\perp}<0
}
\]

for every symmetry-transverse direction, where the quotient removes time phase and rotations in the appropriate way.

Equivalently, after the symmetry-safe quotient,

\[
\boxed{
E^{\ge0}_{\perp}=\{0\}.
}
\]

This excludes both:

- extra zero-growth center directions;
- positive Lyapunov/unstable directions capable of hyperbolic aperiodic recurrence.

---

## 5. Relation to M19-095 and M19-102

M19-095 already proves

\[
\dim E^{\ge0}<\infty.
\]

Therefore the correction does **not** restore an infinite-dimensional problem.

It changes the finite-dimensional target from

\[
\text{remove extra zero eigenchannels}
\]

to

\[
\boxed{
\text{remove every positive or zero symmetry-transverse Lyapunov channel}.
}
\]

M19-102's Ky-Fan quarter-gap budget remains useful as a necessary condition for zero-growth directions, but a complete transverse-stability proof must also control positive exponents.

---

## 6. Vorticity quarter-gap formulation for positive exponents

For a normalized linearized vorticity trajectory,

\[
\frac12\frac d{ds}\log\|\eta\|_2^2
=
-\frac14
-\nu\frac{\|\nabla\eta\|_2^2}{\|\eta\|_2^2}
+rac{\mathcal C_U[W]}{\|\eta\|_2^2}.
\]

Hence a transverse Lyapunov exponent `lambda` satisfies schematically

\[
\boxed{
\lambda
=
-\frac14
-\nu\left\langle\frac{\|\nabla\eta\|_2^2}{\|\eta\|_2^2}\right\rangle
+\left\langle\frac{\mathcal C_U[W]}{\|\eta\|_2^2}\right\rangle.
}
\]

The true target is therefore the strict bound

\[
\boxed{
\left\langle\frac{\mathcal C_U[W]}{\|\eta\|_2^2}\right\rangle
<
\frac14
+\nu\left\langle\frac{\|\nabla\eta\|_2^2}{\|\eta\|_2^2}\right\rangle
}
\]

for every symmetry-transverse invariant projective trajectory.

This is exactly the strong form of the earlier projective-coercivity target.

---

## 7. Correction to M19-103 and M19-119

The following earlier conditional statement must be weakened:

\[
E^c_{extra}=0
\not\Rightarrow
\text{all recurrent ergodic components are RSS/RDSS}.
\]

Instead,

\[
\boxed{
E^{\ge0}_{\perp}=0
\Longrightarrow
\text{local recurrent quotient dynamics reduces to the flow center}
}
\]

under the retained invariant-manifold hypotheses.

Therefore the conditional sentence in M19-119 Section 11 that invokes only `E_extra^c=0` is not sufficient; it should be read with the stronger transverse-stability hypothesis supplied here.

---

## 8. Consequence for long-period RDSS measures

M19-119's invariant-measure reduction remains valid.

Its aperiodic ergodic alternative may arise from:

- extra zero center directions;
- or hyperbolic dynamics with positive transverse Lyapunov exponents.

Hence the long-period bridge now points to

\[
\boxed{
\mathcal T_{transverse}
\text{ rather than merely }\mathcal T_{extra-center}.
}
\]

---

## 9. Updated central analytic frontier

The dominant finite-dimensional analytic theorem is now

\[
\boxed{
\mathcal T_{transverse}:
\sup_{\text{symmetry-transverse projective trajectories}}
\lambda_{Lyap}<0.
}
\]

If proved uniformly on the compact recurrent corridor, it simultaneously eliminates:

1. extra neutral center channels;
2. hyperbolic unstable channels;
3. genuinely aperiodic recurrent quotient dynamics supported by those channels.

Periodic/RDSS isolated orbits remain a separate nonlinear Liouville problem, as corrected by M19-113--114.

---

## 10. Permanent firewall

\[
\boxed{
\text{symmetry-only center}
\neq
\text{symmetry-only recurrent dynamics}
}
\]

unless all transverse unstable directions are also excluded.

This correction is authoritative for all later M19 modules.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
