# DSD M19-118 — The RDSS hard core in intrinsic moduli is a moderate relative-periodic step or long-period escape, not a raw large-alpha branch

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / REPRESENTATION-SAFE SYNTHESIS OF M19-104, M19-116, AND M19-117 / NEAR-IDENTITY RELATIVE-PERIODIC STEPS ARE PARTIALLY EXCLUDED, WHILE THE GENUINE OPEN SET IS BEST DESCRIBED BY MODERATE PRINCIPAL HOLONOMY OR LONG SIMILARITY PERIOD / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Intrinsic RDSS variables

Use

\[
\boxed{
S=2\log\lambda>0
}
\]

and the principal holonomy angle

\[
\boxed{
\beta\in[-\pi,\pi],
\qquad
Q_*=R(\beta).
}
\]

When a rate is useful, use the principal rate

\[
\alpha_{pr}=\beta/S.
\]

These variables describe the one-step relative periodic symmetry without winding duplication.

---

## 2. Nontriviality floor

M19-116 gives a theorem-dependent positive lower bound of the form

\[
S+|\alpha|\ge c_*.
\]

In a principal representation this is recorded as

\[
\boxed{
S+\frac{|\beta|}{S}
\gtrsim c_*.
}
\]

Thus a nontrivial RDSS cannot have both an arbitrarily short period and an extremely small principal group displacement.

---

## 3. Small-rate near-identity exclusion

The small-rotation RDSS theorem applies when

\[
S\ll1,
\qquad
|\alpha|\ll1.
\]

In intrinsic variables,

\[
|\beta|=|\alpha|S\ll S.
\]

Thus this theorem removes a wedge near

\[
(S,\beta)=(0,0)
\]

where the group displacement is even smaller than the already short time step.

---

## 4. Rapid-rate near-identity exclusion

The large-rotation RDSS analysis uses a condition schematically equivalent to

\[
(1+\alpha^2)S\ll1.
\]

With

\[
\alpha=\beta/S,
\]

this becomes

\[
\boxed{
S+\frac{\beta^2}{S}\ll1.
}
\]

Hence

\[
S\ll1,
\qquad
|\beta|\ll\sqrt S.
\]

Even though the instantaneous angular rate may be large, the actual one-step holonomy is still close to identity.

Therefore the phrase "large-alpha RDSS" should not be interpreted as a genuinely large discrete rotation angle.

---

## 5. Geometric picture of the remaining short-period sector

For small `S`, the two external regimes remove:

- very small principal rate `|beta|/S`;
- very large principal rate for which the stronger short-period compatibility assumptions hold.

What may remain is an intermediate-rate wedge where

\[
\boxed{
|\beta|\sim S
}
\]

at theorem-dependent constants, together with any region not covered by the precise external threshold assumptions.

This is a genuine moderate relative-periodic step.

---

## 6. Long-period escape

For

\[
S\to\infty,
\]

the principal rate automatically satisfies

\[
\boxed{
|\alpha_{pr}|\le\pi/S\to0.
}
\]

Yet the principal holonomy angle

\[
\beta
\]

may remain order one.

Thus long-period RDSS is **not** a small-rotation perturbation of ordinary DSS in the sense relevant to the short-period theorems: the orbit may evolve for a very long similarity time before returning with a finite rotation.

The actual noncompact intrinsic modulus is therefore mainly

\[
\boxed{S\to\infty.}
\]

The group variable itself is compact because

\[
Q_*\in SO(3).
\]

---

## 7. Updated RDSS branch menu

Representation-safe bookkeeping gives

\[
\boxed{
\mathcal R_{RDSS}^{open}
\subset
\mathcal R_{step}^{moderate}
\lor
\mathcal R_{period\to\infty}
}
\]

plus any explicit failure of the Type-I/pressure/compactness hypotheses needed to enter the external theorems.

The raw branch

\[
|\alpha|\to\infty
\]

is not intrinsic and should not be listed separately without fixing a rotating-frame gauge.

---

## 8. Relation to augmented Floquet theory

For every finite `S`, M19-109 and M19-114 reduce the RDSS orbit to a finite-dimensional augmented unit-multiplier/Fredholm problem after the essential quarter-gap is removed.

Therefore:

- the moderate finite-`S` branch is a finite-dimensional isolated relative-periodic orbit problem;
- the `S -> infinity` branch is the only intrinsic period-modulus noncompactness not addressed by that fixed-period Fredholm reduction.

This is a substantial simplification of the periodic frontier.

---

## 9. Highest-value next target

The next target should be the long-period limit:

\[
\boxed{
S_n\to\infty,
\qquad
U_n(s+S_n)=Q_nU_n(s).
}
\]

Under compact recurrent Type-I bounds, extract an invariant-measure or complete-orbit limit and determine whether the long-period RDSS sequence necessarily creates:

1. an aperiodic recurrent component, returning to the extra-center theorem;
2. an RSS/relative equilibrium limit;
3. a heteroclinic/nonrecurrent compact orbit;
4. or loss of the retained compact corridor.

This is now the cleanest unresolved bridge between the finite-period and aperiodic problems.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
