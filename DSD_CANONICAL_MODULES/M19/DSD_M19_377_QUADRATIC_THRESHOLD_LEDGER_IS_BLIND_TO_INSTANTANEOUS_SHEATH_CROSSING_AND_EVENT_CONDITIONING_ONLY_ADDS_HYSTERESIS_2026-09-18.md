# DSD M19-377 — The quadratic threshold ledger is blind to instantaneous sheath crossing; event conditioning only adds hysteresis

Date: 2026-09-18

Status: **NEW STRUCTURAL NO-GO / THE M5-666 QUADRATIC TRUNCATED-AMPLITUDE OBSERVABLE `N_a=(1/2)int(rho-a)_+^2` HAS ZERO TRACE ON THE AMPLITUDE THRESHOLD. CONSEQUENTLY AN ORDER-ONE MATERIAL TURNOVER CURRENT ACROSS `rho=a` PRODUCES NO DIRECT BOUNDARY CHARGE IN `N_a`; NEWLY CROSSING MATERIAL ENTERS WITH ZERO `q_a` WEIGHT AND IS SEEN ONLY LATER THROUGH BULK AMPLITUDE/STRETCHING EVOLUTION. MULTIPLYING THE LEDGER BY AN EVENT MARKER `m` AND AVERAGING ADDS ONLY THE GENERATOR/HYSTERESIS TERM `<N_a Lm>`. THEREFORE `N_a` CANNOT BY ITSELF CONVERT THE M5-665 SHEATH-TURNOVER BRANCH INTO A FIXED IRREVERSIBLE EVENT COST. A CLOSURE MUST USE AN OBSERVABLE WITH NONZERO THRESHOLD TRACE/FLUX WEIGHT OR COUPLE TO FORCE/HIGHER-JET GEOMETRY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting ledger

M5-666, independently rederived in M19-375, gives

\[
\boxed{
\mathcal L N_a
+
A_a
=
Q_a^{(2)},
}
\]

where `mathcal L` is the similarity-time generator on the recurrent hull and

\[
A_a
:=
\frac12N_a+aM_a+D_a^{(2)}
\ge0.
\]

Explicitly,

\[
N_a=\frac12\int q_a^2dy,
\qquad
q_a=(\rho-a)_+.
\]

---

## 2. Why threshold turnover does not appear as a boundary term

At the moving amplitude boundary

\[
\Sigma_a(\theta)=\{\rho=a\},
\]

we have

\[
\boxed{q_a|_{\Sigma_a}=0.}
\]

Hence the transported density

\[
\frac12q_a^2
\]

also has zero trace on the boundary.

For a moving-domain Reynolds formula, the material crossing contribution has the schematic form

\[
\int_{\Sigma_a}
\frac12q_a^2
(B-V_a)\cdot n\,dS.
\]

It vanishes identically:

\[
\boxed{
\int_{\Sigma_a}
\frac12q_a^2
(B-V_a)\cdot n\,dS=0.
}
\]

Therefore the positive mean sheath-turnover current from M5-662/M5-665,

\[
\langle\mathcal T_a\rangle>0,
\]

does not generate a direct signed event charge in `N_a`.

---

## 3. Physical interpretation

A material element crossing from `rho<a` into `rho>a` enters at the instant when

\[
\rho=a,
\qquad
q_a=0.
\]

Thus its contribution to `N_a` begins at zero.

Only after its amplitude moves away from the threshold does it contribute positive `q_a^2`, and that subsequent evolution is already encoded in the bulk terms

\[
Q_a^{(2)},\qquad D_a^{(2)},\qquad N_a,\qquad M_a.
\]

Hence

\[
\boxed{
\text{threshold crossing rate}
\not\Rightarrow
\text{fixed instantaneous change of }N_a.
}
\]

This is structural, not an estimate failure.

---

## 4. Event-conditioned identity

Let `m` be any bounded sufficiently regular marker of a crossing/force event on the invariant hull.

Multiply

\[
\mathcal L N_a+A_a=Q_a^{(2)}
\]

by `m` and average with the invariant measure.

Since

\[
\langle\mathcal L(mN_a)\rangle=0,
\]

we have

\[
\langle m\mathcal L N_a\rangle
=-\langle N_a\mathcal L m\rangle.
\]

Therefore

\[
\boxed{
\langle mA_a\rangle
=
\langle mQ_a^{(2)}\rangle
+
\langle N_a\mathcal Lm\rangle.
}
\]

Define

\[
\boxed{
B_{m,a}:=\langle N_a\mathcal Lm\rangle.
}
\]

This is an event-boundary / phase-hysteresis term.

---

## 5. If the marker depends only on N_a, the new term vanishes

Suppose

\[
m=\chi(N_a)
\]

for a smooth scalar function `chi`.

Then

\[
N_a\mathcal Lm
=N_a\chi'(N_a)\mathcal L N_a.
\]

Choose `H` with

\[
H'(x)=x\chi'(x).
\]

Then

\[
N_a\mathcal Lm
=\mathcal L H(N_a).
\]

Invariant averaging gives

\[
\boxed{B_{m,a}=0.}
\]

Thus a marker built only from the scalar threshold state cannot create a new signed resource.

Any nonzero `B_{m,a}` requires genuine phase coupling to an additional variable such as generalized-force rotation, higher-jet creation, or sheet geometry.

---

## 6. Hysteresis is not automatically irreversible

Even when

\[
B_{m,a}\ne0,
\]

it is a bounded recurrent correlation term. It can represent circulation in a multi-variable phase plane rather than one-way resource consumption.

This is the same structural firewall encountered earlier for production/current hysteresis.

Therefore

\[
\boxed{
B_{m,a}\ne0
\not\Rightarrow
\text{finite cumulative contradiction}.
}
\]

---

## 7. Consequence for the M19-374 event family

The three positive-rate mechanisms are

\[
C_{rot}^{force}
\lor
C_{crit}^{higher-jet}
\lor
T_{sheath}^{\rho=a_0}.
\]

The present result separates them:

1. **Sheath turnover** cannot be directly priced by `N_{a0}` because the density has zero threshold trace.
2. **Force/higher-jet events** may couple to `N_{a0}` only through a nontrivial phase marker, producing hysteresis rather than automatic monotone loss.
3. A genuine finite-resource closure therefore needs either a threshold observable carrying nonzero signed flux weight, or a PDE-specific signed/finite resource tied directly to generalized-force/higher-jet activity.

---

## 8. Updated target

Do not continue trying to close `T_sheath` with the quadratic threshold mass itself.

The next high-value alternatives are:

\[
\boxed{
\mathcal T_{trace}^{threshold}:
\text{construct a bounded/finite threshold observable with nonzero material-crossing trace}
}
\]

or

\[
\boxed{
\mathcal T_{force}^{finite}:
\text{couple positive-rate force/higher-jet events to a nonrecyclable generalized-force resource.}
}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
