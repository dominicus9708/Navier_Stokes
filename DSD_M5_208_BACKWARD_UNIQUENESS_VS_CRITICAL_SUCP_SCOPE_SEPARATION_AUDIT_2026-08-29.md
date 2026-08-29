# DSD M5-208 — Exterior Backward Uniqueness vs Critical Spatial SUCP Scope Separation

Date: 2026-08-29

Parent: `DSD_M5_207_TRANSVERSE_METRIC_CURVATURE_FREEDOM_FIREWALL_2026-08-29.md`

Status: **LITERATURE-SCOPE CORRECTION / THE GENERIC `1/r` COMMON TAIL IS NOT ITSELF A CRITICAL OBSTRUCTION TO THE CLASSICAL ESCAURIAZA--SEREGIN--SVERAK EXTERIOR BACKWARD-UNIQUENESS THEOREM, BECAUSE ON EVERY FIXED EXTERIOR `r>=R` THE `1/r` AND `1/r^2` COEFFICIENTS ARE BOUNDED / THE ACTUAL SAME-TAIL BU GAP IS THAT THE RELATIVE VORTICITY EQUATION DOES NOT CLOSE POINTWISE IN THE VORTICITY ALONE: IT CONTAINS THE RELATIVE VELOCITY AND ITS GRADIENT THROUGH A NONLOCAL/HARMONIC HODGE COMPONENT / BY CONTRAST, THE LIN--WANG `epsilon>0` LOSS CONCERNS SPATIAL STRONG UNIQUE CONTINUATION FOR A GENERALIZED STOKES SYSTEM NEAR THE SINGULAR POINT / SCALAR PARABOLIC SUCP IS KNOWN EVEN FOR ARBITRARY CRITICAL `M/|x|^2` HARDY POTENTIAL, SO THE LIN--WANG ENDPOINT FAILURE IS NOT A UNIVERSAL CRITICAL-PARABOLIC NO-GO / THE HIGHEST-PRIORITY MISSING LEMMA RETURNS TO A BOUNDARY-CONDITION-FREE OSEEN--STOKES BACKWARD-UNIQUENESS/COUPLED HODGE PROBLEM ON A FIXED EXTERIOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two continuation problems had been mixed in the endpoint discussion

There are two mathematically distinct tasks.

### BU — terminal-time backward uniqueness

Given an exterior parabolic cylinder and exact terminal zero,

\[
U(\cdot,T)=0,
\]

propagate this zero backward in time.

### SUCP — spatial strong unique continuation

Given infinite-order spatial/parabolic vanishing near a singular spatial point, prove that the solution vanishes identically in the connected domain.

These use related Carleman ideas but are not interchangeable theorem statements.

The M5-181--183 same-tail physical-pair route is primarily a **BU** problem.

The M5-194 Lin--Wang endpoint audit is primarily a **spatial generalized-Stokes SUCP** problem.

---

## 2. Classical exterior heat-type BU does not see `1/r` as critical on a fixed exterior

Escauriaza--Seregin--Sverak prove a backward-uniqueness theorem of the schematic form

\[
|\partial_tu+\Delta u|
\le
M(|u|+|\nabla u|)
\]

on

\[
(\mathbb R^n\setminus B_R)\times[0,T],
\]

with a sub-Gaussian/Gaussian growth bound and

\[
u(x,0)=0
\]

on the exterior terminal slice, implying exterior backward vanishing.

The theorem is formulated directly on the exterior region and does not require prescribing a Dirichlet value on the artificial sphere merely in order to state the scalar/vector heat inequality.

Now the current critical tail satisfies schematically

\[
|B_T(x,t)|\lesssim |x|^{-1},
\]

\[
|\nabla B_T(x,t)|\lesssim |x|^{-2}.
\]

For every fixed

\[
|x|\ge R>0,
\]

these obey

\[
\boxed{
|B_T|\le C_R,
\qquad
|\nabla B_T|\le C_R.
}
\]

Therefore

\[
\boxed{
\text{critical scaling at }r=0
\not\Rightarrow
\text{unbounded BU coefficients on a fixed exterior}.
}
\]

The `1/r` endpoint is not the coefficient-size obstruction to ESS-type BU once the inner radius is fixed.

---

## 3. Same-tail terminal data already satisfies the easy BU-side hypotheses

From M5-145/M5-181/M5-182, for two same-tail physical realizations

\[
Z=u^V-u^W
\]

one has on every fixed exterior

\[
\boxed{Z(\cdot,T_*)=0}
\]

and in fact all terminal time derivatives vanish there.

The W1 tail gives stronger-than-Gaussian decay/growth control at infinity, and the coefficients are smooth/bounded on each fixed exterior.

Thus the remaining problem is not

- terminal zero;
- exterior coefficient boundedness;
- spatial growth.

Those are already green.

---

## 4. The relative vorticity equation is not a closed ESS inequality

Let

\[
\eta=\nabla\times Z.
\]

The relative vorticity equation is

\[
\begin{aligned}
\partial_t\eta-\nu\Delta\eta
&+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V\\
&+(Z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)Z
=0.
\end{aligned}
\]

On a fixed exterior, the coefficients multiplying `eta` and `grad eta` are bounded.

However the last two terms contain

\[
Z,
\qquad
\nabla Z.
\]

To invoke the ESS theorem directly one would need a pointwise bound of the form

\[
\boxed{
|Z|+|\nabla Z|
\le
C_R(|\eta|+|\nabla\eta|)
}
\]

or an equivalent closed local inequality.

Such a bound is false without controlling the harmonic/Hodge component of a divergence-free velocity on the exterior.

Curl does not determine the velocity locally pointwise on an artificial exterior cut.

Hence the actual BU bottleneck is

\[
\boxed{
\text{vorticity--velocity nonlocal coupling},
}
\]

not the critical magnitude of the common tail.

---

## 5. Velocity-pressure system states the missing lemma more honestly

The relative velocity solves

\[
\boxed{
\partial_tZ
-\nu\Delta Z
+A\cdot\nabla Z
+BZ
+\nabla q
=0,
\qquad
\nabla\cdot Z=0,
}
\]

with bounded smooth `A,B` on every fixed exterior and terminal zero.

The missing statement is therefore a boundary-condition-free **Oseen--Stokes backward uniqueness** theorem or an internal proof that handles the pressure/Hodge projection.

This is exactly the BU-OS target already isolated in M5-182.

M5-208 strengthens its priority by showing that the generic critical-tail coefficient size does not block this exterior route.

---

## 6. Lin--Wang addresses a different direction

Lin--Wang study the generalized nonstationary Stokes system

\[
\partial_tu-\Delta u
+A(t,x)\cdot\nabla u
+B(t,x)u
+\nabla p=0,
\qquad
\nabla\cdot u=0,
\]

under singular coefficient assumptions

\[
|A(t,x)|
\le
\lambda|x|^{-1+\varepsilon},
\]

\[
|B(t,x)|
\le
\lambda|x|^{-2+\varepsilon},
\qquad
\varepsilon>0,
\]

and prove quantitative spatial vanishing-order / strong unique-continuation results.

M5-194 correctly identified that their particular Carleman architecture consumes the strict `r^epsilon` gain and does not pass to `epsilon=0` by substitution.

But this is not the same theorem as terminal-time exterior BU.

Thus

\[
\boxed{
\text{Lin--Wang endpoint failure}
\not\Rightarrow
\text{ESS exterior BU endpoint failure}.
}
\]

---

## 7. Critical inverse-square scalar SUCP is known

There are scalar parabolic strong-unique-continuation theorems for

\[
|\Delta u-u_t|
\le
\frac{M}{|x|^2}|u|
\]

with arbitrary fixed

\[
M>0.
\]

Later work extends this to variable Lipschitz principal coefficients with the same critical Hardy-type potential.

Therefore the inverse-square zeroth-order endpoint itself is not a universal obstruction to parabolic SUCP.

The successful proofs use critical spectral/Hardy structure tailored to the scalar operator.

Hence the correct conclusion from M5-194 is narrower:

\[
\boxed{
\text{the generalized-Stokes radial Lin--Wang weight fails at the endpoint},
}
\]

not

\[
\text{all critical }|x|^{-2}\text{ continuation fails}.
\]

---

## 8. First-order critical drift remains the system-specific difficulty near the singular point

The common-tail Oseen operator has both

\[
|x|^{-1}\nabla
\]

and

\[
|x|^{-2}
\]

critical pieces, together with incompressibility and pressure.

The scalar Hardy-potential theorem does not directly cover the first-order vector drift/pressure system.

Likewise the Lin--Wang theorem is subcritical in both lower-order coefficients.

The present literature audit did not locate a theorem that can be inserted verbatim for the arbitrary-amplitude generalized Oseen--Stokes endpoint

\[
A\sim |x|^{-1},
\qquad
B\sim |x|^{-2}
\]

with pressure and no smallness/structural restriction.

This is an **audit statement about the retrieved theorem match**, not a claim that no such result can exist anywhere in the literature.

---

## 9. Boulakia-type Stokes UCP remains spatial/open-set continuation

Nonstationary Stokes unique-continuation/stability estimates are available without prescribing boundary conditions in the continuation statement.

A representative result says that if a Stokes velocity vanishes on a spacetime open subset, then it vanishes in the connected cylinder, with logarithmic stability refinements.

This is relevant to pressure handling and boundary-condition-free continuation.

But it does not by itself convert **terminal-slice zero** into backward zero for the Oseen--Stokes pair.

Thus it cannot replace BU-OS without an additional temporal bridge.

---

## 10. Revised priority of the proof tree

The current continuation front should be separated as follows.

### Route BU-OS — fixed exterior, terminal zero

Inputs already green:

\[
Z(T_*)=0,
\quad
A,B\in L^\infty(\Omega_R),
\quad
\text{sub-Gaussian growth}.
\]

Missing:

\[
\boxed{
\text{pressure/Hodge-compatible backward uniqueness for the coupled Oseen--Stokes system}.
}
\]

This route does **not** need to solve the `r=0` critical Carleman endpoint first.

### Route SUCP-critical — singular spatial point

Here the true endpoint coefficients are

\[
|x|^{-1},
\qquad
|x|^{-2},
\]

and the matrix/scalar Carleman difficulties of M5-194A--207 remain relevant.

This route is harder and should not be used when BU-OS would suffice.

---

## 11. Consequence for the local matrix program

M5-202--207 show that a universal pointwise matrix symmetrizer for the full singular critical operator has multiple independent obstructions.

M5-208 shows that this elaborate singular-point machinery may be unnecessary for the **same-tail terminal flat fiber** if BU-OS can be proved directly on one fixed exterior.

Therefore the proof priority changes:

\[
\boxed{
\text{BU-OS exterior pressure/Hodge bridge}
\quad>\quad
\text{further universal local-matrix design}
}
\]

for the same-tail flat branch.

The matrix work remains relevant for spatial critical SUCP and generic critical-tail dynamics, but no longer as the first tool for terminal backward propagation.

---

## 12. DSD firewall

The following implications are now explicitly forbidden.

1. `1/r is scale-critical => ESS exterior theorem cannot apply` — **FALSE** on fixed `r>=R`; coefficients are bounded there.
2. `Lin--Wang needs epsilon>0 => all critical parabolic SUCP fails` — **FALSE**; scalar Hardy-potential SUCP exists at `1/r^2`.
3. `terminal velocity zero => relative vorticity satisfies a closed ESS inequality` — **NOT DERIVED** because of the Hodge/harmonic velocity component.
4. `Stokes spatial UCP from an open set => terminal backward uniqueness` — **FALSE as a theorem substitution**.
5. `matrix critical-Carleman failure => same-tail BU branch survives` — **FALSE**; fixed-exterior BU-OS is a distinct route.

---

## 13. New concrete internal target

Return to the M5-183 augmented parabolic--elliptic system.

On a fixed exterior,

\[
\partial_t\eta-\nu\Delta\eta
=\mathcal L_1\eta
+
\mathcal L_2Z,
\]

while

\[
-\Delta Z
=
\nabla\times\eta,
\qquad
\nabla\cdot Z=0,
\]

modulo the exterior harmonic component/gauge.

The next calculation should perform an explicit **local Hodge decomposition with cutoff**:

\[
Z
=
\nabla\times(-\Delta)^{-1}(\chi\eta)
+
Z_{harm}
+
Z_{comm},
\]

on a slightly smaller fixed exterior annulus.

The objective is to determine whether

- the Biot--Savart part can be absorbed into an ESS-type parabolic inequality in an `L2`/Carleman norm;
- the cutoff commutator is lower order;
- terminal flatness plus decay forces the exterior harmonic part to zero or finite-dimensional form.

This attacks the actual missing coupling rather than the already-bounded critical coefficients.

---

## 14. DSD verdict

### PROVED / VERIFIED AGAINST THEOREM STATEMENTS

- ESS-type backward uniqueness is an exterior terminal-zero theorem with bounded lower-order heat inequality coefficients;
- the `1/r` and `1/r^2` common-tail coefficients are bounded on every fixed exterior;
- therefore scale criticality at the center is not the BU coefficient obstruction;
- same-tail relative vorticity fails to close because `Z` and `grad Z` remain;
- Lin--Wang is a spatial generalized-Stokes SUCP result with strict subcritical coefficient exponents;
- critical scalar Hardy-potential parabolic SUCP is known at arbitrary amplitude;
- the Lin--Wang epsilon loss is architecture/system-specific, not a universal critical-parabolic impossibility.

### OPEN

- boundary-condition-free Oseen--Stokes backward uniqueness in the exact current solution class;
- elimination/control of the exterior harmonic Hodge component;
- critical first-order generalized-Stokes SUCP at arbitrary amplitude;
- generic critical-tail backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 15. Literature checked

- Escauriaza, Seregin, Šverák, *Backward Uniqueness for Parabolic Equations*, Arch. Rational Mech. Anal. 169 (2003), 147--157, DOI 10.1007/s00205-003-0263-8.
- Lin, Wang, *Quantitative uniqueness estimates for the generalized non-stationary Stokes system*, Applicable Analysis 101 (2022), 3591--3611, DOI 10.1080/00036811.2020.1747611.
- Banerjee, Garofalo, Manna, *A Strong Unique Continuation Property for the Heat Operator with Hardy Type Potential*, J. Geom. Anal. (2021), DOI 10.1007/s12220-020-00487-y.
- Banerjee, Ganguly, Ghosh, *Strong unique continuation for variable coefficient parabolic operators with Hardy type potential*, J. Differential Equations 380 (2024), 92--145.
- Boulakia, *Quantification of the unique continuation property for the nonstationary Stokes problem*, Math. Control Relat. Fields 6 (2016), 27--52.

These are used only within their audited theorem scopes.