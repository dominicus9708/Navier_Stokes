# M19-395 — Extremal kappa phases force opposite-sign strain/geometric CE-H payers

Date: 2026-09-18

Status: **NEW EXTREMAL CONSTITUTIVE RIGIDITY / ON THE REGULAR COMPACT CE-H ENDPOINT BRANCH OF M19-394, AN ATTAINED GLOBAL POSITIVE KAPPA EXTREMUM IS SIMULTANEOUSLY A MATERIAL-TIME TURNING POINT AND A SPATIAL MAXIMUM. THEREFORE `h=0`, `grad kappa=0`, AND `L_rho kappa=Delta kappa<=0`. THE M5-682 CONSTITUTIVE LAW THEN FORCES `L_rho sigma+R_geom >= K_+>0`. AT AN ATTAINED GLOBAL NEGATIVE EXTREMUM, `L_rho kappa>=0` AND THE SAME LAW FORCES `L_rho sigma+R_geom <= K_-<0`. THUS A NONTRIVIAL COMPACT RECURRENT KAPPA CONVEYOR MUST SUPPORT FIXED OPPOSITE-SIGN STRAIN/GEOMETRIC FORCING AT ITS TWO EXTREME COEFFICIENT PHASES. THIS IS A PDE-SPECIFIC TWO-SIDED PAYER CONDITION, NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular attained endpoint branch

Let the retained nontrivial compact CE-H hull have coefficient range

\[
K_-<0<K_+.
\]

Work first on the regular branch where the extrema are attained on the retained high-amplitude active core.

Thus there exist marked material states/points with

\[
\kappa=K_+
\]

and

\[
\kappa=K_-.
\]

If an endpoint is not attained because of nodal, remote, sheet, or disintegration loss, that remains the explicit endpoint-exit branch of M19-394.

---

## 2. Material-time condition at the global positive extremum

Take a material label at a state where

\[
\kappa=K_+.
\]

Because \(K_+\) is the global supremum on the invariant compact hull, the material trajectory cannot increase \(\kappa\) through that value.

The trajectory is differentiable and belongs to the complete recurrent hull, so at the attained extremum

\[
\boxed{
h=D_B\kappa=0.
}
\]

This is the temporal turning-point condition.

---

## 3. Spatial maximum condition

At the same state, \(K_+\) is also the maximal spatial coefficient value on the retained active core.

Hence

\[
\boxed{
\nabla\kappa=0,
\qquad
\Delta\kappa\le0.
}
\]

The weighted operator is

\[
L_\rho\kappa
=
\Delta\kappa
+
2\nabla\log\rho\cdot\nabla\kappa.
\]

Since \(\nabla\kappa=0\),

\[
\boxed{
L_\rho\kappa
=
\Delta\kappa
\le0.
}
\]

---

## 4. Positive-edge payer

M5-682 gives

\[
h
=
L_\rho\kappa
+
L_\rho\sigma
-
\kappa
+
\mathcal R_{geom}.
\]

At the positive extremum,

\[
h=0,
\qquad
\kappa=K_+.
\]

Therefore

\[
L_\rho\sigma
+
\mathcal R_{geom}
=
K_+
-
L_\rho\kappa.
\]

Since \(L_\rho\kappa\le0\),

\[
\boxed{
L_\rho\sigma
+
\mathcal R_{geom}
\ge
K_+>0.
}
\]

Thus pure multiplier diffusion cannot hold the upper endpoint in place. The strain-diffusion plus explicit geometric forcing must supply at least the full positive coefficient value, and possibly more if the kappa maximum is strictly curved.

---

## 5. Negative-edge payer

At an attained global negative extremum,

\[
\kappa=K_-<0,
\]

the same complete-orbit argument gives

\[
\boxed{
h=0.
}
\]

Spatially this is a minimum, so

\[
\boxed{
\nabla\kappa=0,
\qquad
\Delta\kappa\ge0,
}
\]

and hence

\[
\boxed{
L_\rho\kappa\ge0.
}
\]

The constitutive law gives

\[
L_\rho\sigma
+
\mathcal R_{geom}
=
K_-
-
L_\rho\kappa.
\]

Therefore

\[
\boxed{
L_\rho\sigma
+
\mathcal R_{geom}
\le
K_-<0.
}
\]

The lower endpoint requires a fixed negative strain/geometric forcing.

---

## 6. Two-sided constitutive sign gap

Combining the two extrema,

\[
\boxed{
\left.
L_\rho\sigma+\mathcal R_{geom}
\right|_{\kappa=K_+}
\ge K_+>0,
}
\]

while

\[
\boxed{
\left.
L_\rho\sigma+\mathcal R_{geom}
\right|_{\kappa=K_-}
\le K_-<0.
}
\]

Hence the compact recurrent conveyor requires a genuine sign change in the non-kappa-diffusion CE-H forcing between its positive and negative coefficient extremes.

If the retained away-zero branches of M19-355 give

\[
K_+\ge\delta_+>0,
\qquad
-K_-\ge\delta_->0,
\]

then the endpoint payer gap is uniformly nonzero.

---

## 7. Relation to M19-394 stagnation

M19-394 derives conditional drift stagnation near compact coefficient edges:

\[
\overline h_\Phi(k)\to0
\]

along regular endpoint sequences.

M19-395 identifies the pointwise PDE geometry at an actually attained endpoint:

\[
\boxed{
h=0
\quad\text{and}\quad
L_\rho\sigma+\mathcal R_{geom}
\text{ exactly balances }\kappa-L_\rho\kappa.
}
\]

Thus the endpoint stagnation is not free phase-space slowing. It is maintained by a definite spatial strain/geometric balance.

---

## 8. Immediate branch split

Define

\[
Q_{sg}
:=
L_\rho\sigma+\mathcal R_{geom}.
\]

The regular compact endpoint branch forces

\[
Q_{sg}(Y_+)\ge K_+>0,
\]

\[
Q_{sg}(Y_-)\le K_-<0.
\]

Therefore either

1. the opposite-sign endpoint states lie in one connected regular space/state corridor, forcing a transition in \(Q_{sg}\); or
2. they are separated by component/sheet/time-phase structure; or
3. an endpoint fails regular attainment and routes to the M19-394 singular/disintegration exit.

This refines the next target to the **transition mechanism of the strain/geometric endpoint payer**, rather than another search for a sign at the endpoints themselves.

---

## 9. Firewall

The two endpoint inequalities are not additive dissipation costs.

A recurrent orbit may revisit the same positive and negative endpoint phases indefinitely.

The result is therefore a structural PDE constraint:

\[
\boxed{
\text{compact two-sided kappa recurrence}
\Rightarrow
\text{opposite-sign strain/geometric extremal payer}.
}
\]

A closure still needs a nonreuse, connected-gradient, or finite-resource theorem for the transition between those endpoint payer phases.

---

\[
\boxed{\text{M19-395 COMPLETE; THE TWO KAPPA EDGES REQUIRE OPPOSITE-SIGN STRAIN/GEOMETRIC FORCING.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
