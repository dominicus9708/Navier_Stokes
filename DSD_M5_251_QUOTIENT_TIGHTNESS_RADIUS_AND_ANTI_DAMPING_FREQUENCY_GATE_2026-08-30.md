# DSD M5-251 — Quotient Tightness Radius and Anti-Damping Frequency Gate

Date: 2026-08-30

Parent: `DSD_M5_250_FINITE_ENERGY_QUOTIENT_INVARIANT_AVERAGE_BALANCE_2026-08-30.md`

Status: **SAFE SAME-QUOTIENT FREQUENCY LOWER BOUND / PRIOR DIRICHLET-FREQUENCY RESULTS FOR VORTICITY OR FLAT-PAIR CROSS-SECTIONS ARE NOT IDENTIFIED WITH THE PRESENT WHOLE-SPACE FINITE-ENERGY QUOTIENT / COMPACTNESS OF THE CANONICAL QUOTIENT HULL GIVES UNIFORM L2 TIGHTNESS; SOBOLEV THEN GIVES A DIRECT `D_Q/E_Q >= c/R_Q^2` LOWER BOUND / COMBINING WITH M5-250 CONVERTS THE ANTI-DAMPING-DOMINANT BRANCH INTO AN EXPLICIT `R_Q >= c sqrt(nu)` RADIUS FLOOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frequency-normalization firewall

M5-250 defines

\[
\boxed{
\bar\lambda_Q
:=
\frac{\langle D_Q\rangle}{\langle E_Q\rangle}
=
\frac{\langle\|\nabla Q\|_2^2\rangle}
{\langle\|Q\|_2^2\rangle}.
}
\]

Several earlier repository files contain quantities called a frequency or Dirichlet quotient. They concern, depending on the file,

- localized vorticity/enstrophy;
- a log-spherical cross-section field in an invariant pair space;
- finite moving balls;
- or genealogical flat fibers.

They are not automatically the same as `bar lambda_Q`.

Therefore no previous frequency floor is imported unless its numerator and denominator are exactly transferred to the present whole-space `Q`.

---

## 2. Compact quotient hull

Fix the canonical divergence-free tail-extension convention from M5-250.

The W1 recurrent hull `M` is compact in the audited strong local topology, the canonical tail map is continuous, and the same-tail quotient belongs to global `L2 cap H1`.

On the strong quotient corridor assume, as already required for the M5-250 invariant-energy observable, that

\[
\boxed{
V\mapsto Q[V]
\quad\text{is continuous from }M\text{ into }L^2(\mathbb R^3).
}
\]

Then

\[
\mathcal Q:=\{Q[V]:V\in M\}
\]

is compact in `L2`.

Consequently it is uniformly tight:

for every `0<epsilon<1`, there exists a finite `R_Q(epsilon)` such that

\[
\boxed{
\int_{|Y|>R_Q(\varepsilon)}|Q[V](Y)|^2dY
\le
\varepsilon\|Q[V]\|_2^2
}
\]

for every nonzero quotient state, provided the normalization is taken relative to its own `L2` mass.

If the quotient hull is uniformly separated from zero, this follows immediately from ordinary compact `L2` tightness. If zero lies in the quotient hull, that endpoint must first be treated separately as in M5-250 Section 11.

---

## 3. Same-state Sobolev frequency bound

Let `R=R_Q(epsilon)` and suppose

\[
\int_{B_R}|Q|^2
\ge
(1-\varepsilon)E_Q.
\]

Hölder on `B_R` gives

\[
\int_{B_R}|Q|^2
\le
|B_R|^{2/3}\|Q\|_6^2.
\]

Use the homogeneous Sobolev inequality

\[
\|Q\|_6
\le C_S\|\nabla Q\|_2.
\]

Since

\[
|B_R|=\frac{4\pi}{3}R^3,
\]

we obtain

\[
(1-\varepsilon)E_Q
\le
C_S^2
\left(\frac{4\pi}{3}\right)^{2/3}
R^2D_Q.
\]

Therefore every nonzero quotient state satisfying the same tightness radius obeys

\[
\boxed{
\frac{D_Q}{E_Q}
\ge
\lambda_{Q,-}(R,\varepsilon)
:=
\frac{1-\varepsilon}
{C_S^2(4\pi/3)^{2/3}R^2}.
}
\]

This is a direct whole-space estimate on exactly the M5-250 quotient.

---

## 4. Invariant-average consequence

If one radius `R_Q(epsilon)` works uniformly on the recurrent quotient hull, then pointwise

\[
D_Q(s)
\ge
\lambda_{Q,-}E_Q(s).
\]

Averaging gives

\[
\boxed{
\bar\lambda_Q
=
\frac{\langle D_Q\rangle}{\langle E_Q\rangle}
\ge
\lambda_{Q,-}(R_Q,\varepsilon).
}
\]

---

## 5. Combine with M5-250 anti-damping dominance

The anti-damping-dominant payer from M5-250 requires

\[
\boxed{
\bar\lambda_Q
\le
\frac{3}{4\nu}.
}
\]

Hence a survivor in that branch must satisfy

\[
\frac{1-\varepsilon}
{C_S^2(4\pi/3)^{2/3}R_Q^2}
\le
\frac{3}{4\nu}.
\]

Equivalently,

\[
\boxed{
R_Q
\ge
R_{Q,anti,-}(\varepsilon)
:=
\left[
\frac{4\nu(1-\varepsilon)}
{3C_S^2(4\pi/3)^{2/3}}
\right]^{1/2}.
}
\]

Thus the anti-damping payer is impossible for a sufficiently tightly concentrated finite-energy quotient.

---

## 6. Interpretation

The critical tail has already been removed. Hence `R_Q` measures the spatial extent of the **finite-energy correction/core**, not the `1/r` halo.

The branch says:

\[
\boxed{
\text{if backward-Leray anti-damping pays at least one third of mean quotient dissipation,}
\text{ the finite-energy correction must occupy a radius of order }\sqrt\nu.
}
\]

This is structurally analogous to previous enstrophy quantile-radius gates, but it is a new quotient-specific radius and must not be numerically identified with `R_Z` without an explicit comparison theorem.

---

## 7. Why compactness alone does not close the branch

Compactness gives

\[
R_Q(\varepsilon)<\infty,
\]

but it does not give a universal upper bound below `R_{Q,anti,-}`.

Thus

\[
\boxed{
\text{compact quotient hull}
\not\Rightarrow
\text{anti-damping contradiction}.
}
\]

What has been obtained is an explicit radius floor, not closure.

---

## 8. Possible next comparison

There are now two independently defined normalized radii:

1. `R_Z(epsilon_Z)` from enstrophy tightness;
2. `R_Q(epsilon)` from finite-energy quotient tightness.

A useful next lemma would be a **Biot--Savart/canonical-tail-subtraction comparison** of the form

\[
R_Q(\varepsilon_Q)
\le
C\,R_Z(\varepsilon_Z)
\]

or the reverse, with exact constants and explicit tail-error terms.

Without such a lemma their numerical thresholds must remain separate.

---

## 9. DSD verdict

### PROVED

On the same finite-energy quotient used in M5-250,

\[
\boxed{
\frac{D_Q}{E_Q}
\ge
\frac{1-\varepsilon}
{C_S^2(4\pi/3)^{2/3}R_Q(\varepsilon)^2}.
}
\]

Hence anti-damping dominance forces

\[
\boxed{
R_Q(\varepsilon)
\ge
\left[
\frac{4\nu(1-\varepsilon)}
{3C_S^2(4\pi/3)^{2/3}}
\right]^{1/2}.
}
\]

### FIREWALL

Earlier vorticity/cross-section frequency quotients are not silently identified with `bar lambda_Q`.

### OPEN

- comparison of `R_Q` with the already quantified enstrophy radius `R_Z`;
- compressive-strain payer;
- signed residual-work payer;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
