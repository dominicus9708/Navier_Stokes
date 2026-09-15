# DSD M19-271 — A finite-lag bounded-observable coboundary cannot absorb the positive-mean signed energy event

Date: 2026-09-15  
Canonical ID: **M19-271**  
Status: **ACTIVE FINITE-LAG AUDIT / COBoundary NO-GO / LAG-COUPLING MUST CARRY A NON-COBoundary DEFECT OR FINITE CRITICAL BUDGET / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-270

On the residual terminal-payer branch there is a positive-measure signed energy-event set \(\mathcal E_E\) and a positive-measure production-linked persistent-lineage event set \(\mathcal E_{pd}\).

Ergodicity produces one fixed finite lag \(h_*\) such that

\[
\mu\bigl(\mathcal E_{pd}\cap\sigma_{-h_*}\mathcal E_E\bigr)>0.
\]

Thus arbitrary scale separation has been removed.

A natural next attempt is to transport the signed energy event across this fixed lag using a bounded state observable.

The present module audits that strategy abstractly before constructing a candidate observable.

---

## 2. Finite-lag coboundaries have exactly zero invariant mean

Let \((\mathfrak H,\sigma_t,\mu)\) be any invariant probability flow and let

\[
\mathcal O:\mathfrak H\to\mathbb R
\]

be any integrable bounded state observable.

For fixed finite \(h_*\), define the lag coboundary

\[
\boxed{
\Delta_{h_*}\mathcal O(Y)
:=
\mathcal O(\sigma_{h_*}Y)-\mathcal O(Y).
}
\]

Invariance of \(\mu\) gives

\[
\int\mathcal O(\sigma_{h_*}Y)d\mu(Y)
=
\int\mathcal O(Y)d\mu(Y).
\]

Therefore

\[
\boxed{
\left\langle\Delta_{h_*}\mathcal O\right\rangle_\mu=0.
}
\]

This is exact and does not require ergodicity; invariance alone is enough.

---

## 3. The signed energy event has strictly positive invariant mean

M19-269 defines the finite-depth observable

\[
\Gamma_E(Y)
=
\left.
\frac d{dz}
\left(
\sqrt z
\int_{S^2}\mathcal J_{r,Y}(z,\omega)d\omega
\right)
\right|_{z=z_E}.
\]

Its invariant mean obeys

\[
\boxed{
\langle\Gamma_E\rangle_\mu
=
\mathscr G'(z_E)
>
\gamma_*>0.
}
\]

Hence

\[
\boxed{
\Gamma_E
\neq
\Delta_{h_*}\mathcal O
}
\]

for every bounded/integrable state observable \(\mathcal O\), even in invariant-mean equality.

A positive-mean signed energy event cannot be hidden inside a pure finite-lag coboundary.

---

## 4. Any lag representation must contain a non-coboundary remainder

Suppose a proposed lag-coupling theorem has the form

\[
\boxed{
\Gamma_E
=
\Delta_{h_*}\mathcal O
+
\mathcal R.
}
\]

Taking invariant means gives

\[
\boxed{
\langle\mathcal R\rangle_\mu
=
\langle\Gamma_E\rangle_\mu
>\gamma_*>0.
}
\]

Thus the entire positive mean survives in the remainder.

The lag coboundary itself pays none of it.

Consequently every valid fixed-lag transport identity must expose an explicit non-coboundary payer/defect \(\mathcal R\).

---

## 5. Why another unsigned remainder is not enough

If \(\mathcal R\) is merely another nonnegative recurrent local quantity with a fixed normalized lower mean, then the argument returns to the M5-598 accumulation firewall.

At geometric Type-I generations a fixed normalized cost can acquire a summable physical scale factor.

Therefore

\[
\boxed{
\langle\mathcal R\rangle>0
\not\Rightarrow
\text{physical contradiction}
}
\]

unless \(\mathcal R\) belongs to one of the genuinely nonreplenishable categories:

1. a scale-invariant signed/monotone critical resource;
2. a finite original-variable total with nonsummable mapped demand;
3. a finite label/index resource;
4. a terminal defect forbidden by an external/internal theorem;
5. an exact PDE incompatibility or Liouville obstruction.

Thus finite-lag overlap does not weaken the M5-598 standard; it only localizes where the decisive non-coboundary object must appear.

---

## 6. Application to bounded local energy observables

For example, take any fixed finite-depth local/spherical energy observable

\[
\mathcal O_E(Y)
=
\int \chi |F_Y|^2
\]

with a fixed compact cutoff. Compact-hull regularity makes \(\mathcal O_E\) bounded.

Then

\[
\left\langle
\mathcal O_E(\sigma_{h_*}Y)-\mathcal O_E(Y)
\right\rangle=0.
\]

Hence repeated positive signed energy-transport events cannot be converted into a contradiction merely by saying that a bounded local energy must increase across each production-to-energy lag.

Any such local-energy increment identity necessarily contains compensating flux, pressure work, diffusion, or moving-boundary terms whose invariant mean carries the positive balance.

This is the finite-lag version of the same compensation already visible in M5-583 and M19-269.

---

## 7. Relation to material amplitude observables

The same firewall applies to material/CE-H amplitude observables.

A bounded recurrent quantity such as a truncated \(M_p\), flux label weight, or logarithmic amplitude coordinate has zero invariant mean finite-lag increment whenever it is an honest integrable state function.

Therefore a fixed-lag material exposure identity can close only if the integrated source term has an independently forbidden sign/budget.

M18-060 already exhibits the typical compensation mechanism on CE-H:

\[
\langle A_p\rangle
=
\langle D_p\rangle
+c_p\langle M_p\rangle,
\]

so recurrent amplitude maintenance is strain-paid but not monotone contradictory.

M19-271 shows that this is not an accident of that particular observable; it is the generic invariant-measure constraint on bounded finite-lag state differences.

---

## 8. Refined lag-coupling target

M19-270 introduced

\[
\mathcal T_{tail}^{lag-coupling}.
\]

The present audit refines it to

\[
\boxed{
\mathcal T_{tail}^{lag-defect}:
\text{derive, on the fixed-lag production/energy block, a non-coboundary remainder whose positive mean is independently impossible or finite-budgeted.}
}
\]

A pure bounded-observable lag increment is permanently excluded as a closure mechanism.

The strongest candidates are now:

- terminal local-energy defect exclusion;
- a topological/index quantity not representable as an ordinary scalar coboundary;
- a genuinely critical monotone quantity;
- exact PDE rigidity coupling the production-linked anchored/projective state to the later energy-transport state.

---

## 9. Updated hard-core reduction

The terminal hard branch is now reduced to

\[
\boxed{
\mathcal T_{tail}^{energy-defect}
\lor
\mathcal T_{tail}^{lag-defect}
\lor
\mathcal T_{aper}^{signed/index}.
}
\]

Here `signed/index` emphasizes that an ordinary bounded scalar coboundary cannot work; the surviving recurrent mechanism must carry genuinely nontrivial signed, topological, index, or nonreplenishable critical content.

---

## 10. Verdict

M19-270 proves a fixed finite-lag correlation between the productive material subsystem and the signed energy subsystem.

M19-271 proves that this cannot be closed by transporting a bounded scalar state observable across that lag:

\[
\boxed{
\langle O\circ\sigma_{h_*}-O\rangle=0
\quad\text{while}\quad
\langle\Gamma_E\rangle>0.
}
\]

Therefore the next successful theorem must reveal a **non-coboundary defect/resource**, not another bounded recurrent state difference.

Global 3D Navier--Stokes regularity remains unproved.
