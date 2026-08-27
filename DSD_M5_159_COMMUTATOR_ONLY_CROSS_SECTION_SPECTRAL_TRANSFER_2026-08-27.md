# DSD M5-159 — Commutator-Only Cross-Section Spectral Transfer

Date: 2026-08-27

Status: **P1_B^S SPECTRAL GATE / THE PARABOLIC FREQUENCY ESCAPE REQUIRED BY M5-154 CANNOT BE CREATED BY THE CONSTANT-COEFFICIENT LERAY/DIFFUSIVE/NORMAL OPERATORS THEMSELVES / TRUE CROSS-SECTION SPECTRAL FLUX COMES ONLY FROM COMMUTATORS WITH THE VARIABLE-COEFFICIENT RELATIVE TRANSPORT/STRETCHING/BIOT-SAVART OPERATOR, WHICH CARRIES THE EXPLICIT `e^{-tau}` FACTOR / A NORMAL-SLAVING ESTIMATE IS THE REMAINING TECHNICAL INPUT NEEDED TO TURN THIS DECOMPOSITION INTO A CLOSED FREQUENCY-growth inequality / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frozen input

Work only on Branch

\[
P1_B^S,
\]

so there is an invariant off-diagonal pair measure `rho` on

\[
\mathcal R=M\times_{\mathcal T}M.
\]

Let `K(tau)` denote the scaled relative vorticity cross-section from M5-154.  It satisfies

\[
\boxed{
K_s+K_\tau
=e^{-\tau}
\left[
4\nu K_{\tau\tau}
-6\nu K_\tau
+\nu(2+\Delta_{S^2})K
-\mathcal N_\tau K
\right],
}
\]

where `N_tau` is linear in the pair difference once the two W1 backgrounds are fixed and contains the relative transport, stretching and Biot--Savart-recovered velocity terms.

M5-154 proved that a nonzero flat statistical fiber requires cross-section frequency escape roughly at

\[
\Omega(\tau)\gtrsim e^{\tau/2}.
\]

The present note identifies which part of the equation can actually move spectral mass toward such frequencies.

---

## 2. Cross-section Hilbert space

Use

\[
\boxed{
\mathscr H:=L^2(\mathcal R,\rho;L^2(S^2)).
}
\]

The invariant pair flow induces a unitary group on `H`.  Let

\[
A_s
\]

be its skew-adjoint generator.

The angular Laplacian

\[
-\Delta_{S^2}
\]

is nonnegative self-adjoint and commutes with the pair-flow generator because flow translation acts on the state variable, not on the angular coordinate.

Define the nonnegative cross-section frequency operator

\[
\boxed{
\Lambda
:=
(1-A_s^2-\Delta_{S^2})^{1/2}.
}
\]

For a spectral cutoff `L`, write

\[
P_{\le L}:=1_{[0,L]}(\Lambda),
\qquad
P_{>L}:=1-P_{\le L}.
\]

---

## 3. Operators that do not transfer cross-section frequency

The following operators commute with every spectral projector of `Lambda`:

1. pair-flow translation `A_s`;
2. the normal derivatives `partial_tau`, `partial_tau^2`;
3. the spherical Laplacian `Delta_{S^2}`;
4. scalar multiplication by functions of `tau` only, including `e^{-tau}`.

Hence the constant-coefficient principal operator

\[
\mathcal P_0
:=
A_s+\partial_\tau
-e^{-\tau}
\left[
4\nu\partial_{\tau\tau}
-6\nu\partial_\tau
+\nu(2+\Delta_{S^2})
\right]
\]

satisfies

\[
\boxed{
[P_{\le L},\mathcal P_0]=0.
}
\]

This statement is independent of whether the normal diffusion changes the amplitude of one already-existing mode.  It says only that it cannot move that mode into a different `Lambda` spectral band.

---

## 4. Exact source of spectral flux

Project the equation to `P_{>L}`.  Because the principal operator commutes with the projector,

\[
\boxed{
\mathcal P_0(P_{>L}K)
=
-e^{-\tau}P_{>L}(\mathcal N_\tau K).
}
\]

If one compares this with the equation obtained by applying `N_tau` to `P_{>L}K`, the inter-band forcing is exactly

\[
\boxed{
\mathfrak F_L
:=
-e^{-\tau}
[P_{>L},\mathcal N_\tau]K.
}
\]

Therefore

\[
\boxed{
\text{cross-section spectral transfer}
=
\text{variable-coefficient commutator flux only}.
}
\]

The viscous terms can damp different frequencies at different rates, but they do not create higher spectral bands from lower ones.

---

## 5. Differential order of the relative coupling

The relative vorticity nonlinearity has the schematic form

\[
(U\cdot\nabla)\delta\Omega
-(\delta\Omega\cdot\nabla)U
+(Z\cdot\nabla)\Omega_V
-(\Omega_V\cdot\nabla)Z.
\]

At fixed scaled shell:

- the first term is first order in `K`;
- the second is zeroth order in `K` after the background derivative is fixed;
- `Z` is recovered from relative vorticity by Biot--Savart, one derivative smoother;
- the last two terms are therefore at most first-order operators on the relative vorticity.

Thus

\[
\boxed{
\mathcal N_\tau
= B^a_\tau\nabla_a + C_\tau + \mathcal S_\tau,
}
\]

where `S_tau` is order zero or negative after Biot--Savart recovery.

No new second-order variable-coefficient frequency-transfer operator is hidden in `N_tau`.

---

## 6. Commutator scale

For a smooth/analytic compact W1 shell class, standard first-order pseudodifferential commutator bookkeeping gives schematically

\[
\boxed{
\|[\Lambda,\mathcal N_\tau]f\|_{\mathscr H}
\le
C_{tr}
\bigl(
\|\Lambda f\|_{\mathscr H}
+
\|f\|_{\mathscr H}
\bigr),
}
\]

with a class constant `C_tr` depending on the audited scaled-shell coefficient bounds.

Equivalently, after a spectral cutoff, the instantaneous band-transfer rate carries the explicit factor

\[
\boxed{
 e^{-\tau} C_{tr}.
}
\]

The important structural point is that the coefficient is integrable:

\[
\int_{\tau_0}^{\infty}e^{-\tau}d\tau
=e^{-\tau_0}<\infty.
\]

This is the first quantitative mismatch with the required indefinitely increasing frequency scale.

---

## 7. Why this does not yet prove bounded frequency

A direct conclusion

\[
\Omega'(\tau)
\le C e^{-\tau}\Omega(\tau)
\]

would close the branch, because it would imply a finite multiplicative frequency gain after every sufficiently large `tau_0`.

However the M5-154 equation contains the fast normal terms

\[
4\nu e^{-\tau}K_{\tau\tau}
-6\nu e^{-\tau}K_\tau.
\]

Although these terms commute with every cross-section spectral projector and hence do not themselves transfer bands, a rigorous Rayleigh-quotient derivative for

\[
\Omega^2
\sim
\frac{\|\Lambda K\|^2}{\|K\|^2}
\]

must still control their effect on the denominator and numerator simultaneously.

Thus the remaining technical lemma is not another transport estimate.  It is a **normal-slaving/comparison lemma** showing that the commuting fast normal channel cannot manufacture apparent cross-frequency growth in the normalized spectral ratio.

---

## 8. Candidate normal-slaving variable

Define

\[
\boxed{
J:=K-4\nu e^{-\tau}K_\tau.
}
\]

A direct differentiation and use of the M5-154 equation yields a first-order fast/slow system in `(K,J)` in which

\[
K_\tau
=\frac{e^\tau}{4\nu}(K-J)
\]

and the difference `J-K` is driven by cross-section derivatives and the variable-coefficient coupling.

The homogeneous fast mode grows at normal infinity, consistent with M5-146/147.  Flatness therefore selects the slaved branch rather than the growing branch.

The next lemma should quantify this by proving, on the flat class and in a reduced analytic norm,

\[
\boxed{
\|J-K\|
\lesssim
 e^{-\tau}
\bigl(
\|A_sK\|
+
\|\Lambda K\|
+
\|K\|
\bigr).
}
\]

If this estimate holds with radius loss but without a same-norm analytic shortcut, the commutator estimate above can be promoted to a genuine frequency-growth inequality.

---

## 9. Consequence conditional on normal slaving

Assume the preceding slaving estimate.

Then, after the standard quotient regularization

\[
\Omega_\varepsilon^2
:=
\frac{\|\Lambda K\|^2+\varepsilon}
{\|K\|^2+\varepsilon},
\]

all commuting principal terms cancel or contribute non-increasing viscous pieces in the cross-frequency quotient, while the only positive transfer term comes from the commutator with `N_tau`.

One obtains schematically

\[
\boxed{
\frac d{d\tau}\log(1+\Omega_\varepsilon)
\le
C_* e^{-\tau}.
}
\]

Therefore for `tau>=tau_0`,

\[
\boxed{
1+\Omega_\varepsilon(\tau)
\le
(1+\Omega_\varepsilon(\tau_0))
\exp(C_*e^{-\tau_0}).
}
\]

Letting `epsilon downarrow0` would make the cross-section frequency uniformly bounded after every fixed `tau_0`.

This contradicts the M5-154 necessary escape

\[
\Omega(\tau)\gtrsim e^{\tau/2}
\]

for a nonzero flat statistical fiber.

Hence **normal slaving is sufficient to close `P1_B^S`.**

---

## 10. DSD four-chain audit

### Formation — GREEN

The spectral operator is formed on the actual invariant pair Hilbert space.  No periodicity or discrete time spectrum is assumed.

### Axis — GREEN

`Lambda` measures only cross-section frequency.  Normal depth `tau` is not folded into the same spectral coordinate.

### Static aggregation — GREEN

Viscous damping and transport commutator flux are not counted as separate positive costs; only genuine band transfer is isolated.

### Dynamics — GREEN / YELLOW

The exact commutator-only source statement is GREEN.

The promotion to a closed frequency-growth inequality is YELLOW until the normal-slaving estimate is proved.

### Cross-audit — GREEN

This note does not reuse the required frequency escape as a hypothesis for the commutator estimate.  The escape enters only after the conditional growth bound is independently derived.

---

## 11. Updated frontier

The statistical flat branch is now reduced to

\[
\boxed{
\text{prove normal slaving}
\Longrightarrow
\text{integrable commutator transfer}
\Longrightarrow
\text{bounded cross-frequency}
\Longrightarrow
P1_B^S\text{ impossible}.
}
\]

The next calculation is therefore the normal-slaving lemma for

\[
J-K=-4\nu e^{-\tau}K_\tau
\]

on the flat branch, using the growing-mode exclusion from M5-146/147 and analytic-radius loss from M5-155.

`P1_B^P` remains untouched.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
