# Critical H1 Tail -> Relative Campanato Escalation or Critical H2 Tail — 2026-08-24

Status: **ONE ANTI-PROOF TAIL BRANCH REDUCED / GLOBAL REGULARITY NOT PROVED.**

`ANTI_PROOF_TAIL_ENDPOINT_SCOPE_CORRECTION_2026-08-24.md` restores two honest annular tail failures:

\[
H_{1,crit}^{tail}:
\sup_R R\int_{A_R}|\nabla V|^2=\infty,
\]

and

\[
H_{2,crit}^{tail}:
\sup_R R^3\int_{A_R}|\nabla^2V|^2=\infty.
\]

This note shows that the first is **not independent**. If the critical H2 quantity remains bounded, unbounded critical H1 shell energy forces unbounded Galilean-invariant relative Campanato energy.

---

## 1. Scale to a unit annulus

Let

\[
A_R=\{R<|Y|<2R\},
\]

and let `A_R^*` be a fixed enlargement.

Define the critical rescaling

\[
f_R(z)=R V(Rz),
\]

on the corresponding fixed annulus `A_1^*`.

Let

\[
\bar f_R=\fint_{A_1^*}f_Rdz.
\]

The scale-invariant quantities become

\[
\boxed{
\|\nabla f_R\|_{L^2(A_1^*)}^2
\asymp
R\int_{A_R^*}|\nabla V|^2
=:\mathfrak E_1(R),
}
\]

\[
\boxed{
\|\nabla^2f_R\|_{L^2(A_1^*)}^2
\asymp
R^3\int_{A_R^*}|\nabla^2V|^2
=:\mathfrak E_2(R),
}
\]

and

\[
\boxed{
\|f_R-\bar f_R\|_{L^2(A_1^*)}^2
\asymp
R^{-1}
\int_{A_R^*}|V-(V)_{A_R^*}|^2dY
=:\mathfrak C_A(R).
}
\]

Thus `E1`, `E2`, and annular relative Campanato energy are all dimensionless on the unit annulus.

---

## 2. Fixed-domain H2 interpolation

On a fixed smooth annulus, standard interior/extension interpolation gives

\[
\boxed{
\|\nabla f\|_2
\le
C
\|f-\bar f\|_2^{1/2}
\|\nabla^2f\|_2^{1/2}
+C\|f-\bar f\|_2.
}
\]

Squaring and absorbing harmless constants,

\[
\boxed{
\mathfrak E_1(R)
\le
C
\left[
\mathfrak C_A(R)^{1/2}
\mathfrak E_2(R)^{1/2}
+
\mathfrak C_A(R)
\right].
}
\]

This is purely local functional analysis; no Navier--Stokes dynamics is used yet.

---

## 3. Quantitative converse

Suppose

\[
\mathfrak E_2(R)\le H_*
\]

on a shell. Then

\[
\mathfrak E_1(R)
\le
C\left[
H_*^{1/2}\mathfrak C_A(R)^{1/2}
+\mathfrak C_A(R)
\right].
\]

Writing `x=sqrt(C_A)` and solving the quadratic inequality gives the lower bound

\[
\boxed{
\mathfrak C_A(R)
\ge
c
\frac{\mathfrak E_1(R)^2}
{H_*+\mathfrak E_1(R)}
}
\]

for a universal fixed-annulus constant `c>0`.

Consequently

\[
\boxed{
\mathfrak E_1(R_n)\to\infty,
\quad
\sup_n\mathfrak E_2(R_n)<\infty
\Longrightarrow
\mathfrak C_A(R_n)\to\infty.
}
\]

---

## 4. Annular variance forces ball relative Campanato escalation

Let `B_{4R}` contain `A_R^*`. The ball mean minimizes the full-ball squared deviation, but on the shell

\[
\int_{A_R^*}|V-(V)_{B_{4R}}|^2
\ge
\int_{A_R^*}|V-(V)_{A_R^*}|^2.
\]

Therefore

\[
\int_{B_{4R}}|V-(V)_{B_{4R}}|^2
\ge
\int_{A_R^*}|V-(V)_{A_R^*}|^2.
\]

Hence the ball relative Campanato quantity

\[
\mathcal C_{4R}
=(4R)^{-1}
\int_{B_{4R}}|V-(V)_{B_{4R}}|^2
\]

satisfies

\[
\boxed{
\mathcal C_{4R}
\ge c\,\mathfrak C_A(R).
}
\]

Thus

\[
\boxed{
H_{1,crit}^{tail}
\Longrightarrow
\text{relative-Campanato escalation}
\ \lor\ 
H_{2,crit}^{tail}.
}
\]

---

## 5. Structural interpretation

The two ways to make a shell carry much more than the `1/R` critical amount of first-derivative energy are now explicit.

### A. Large shell-scale velocity variance

If second derivatives remain at critical size, then the large first-derivative shell must be supported by a genuinely large shell-scale velocity variation:

\[
\mathcal C_R\to\infty.
\]

This is precisely the Galilean-invariant relative-energy / affine-strain obstruction already exposed by

`RELATIVE_CAMPANATO_REMOTE_STRAIN_GATE_2026-08-23.md`

and

`MOVING_RELATIVE_VARIANCE_TURNOVER_LEDGER_2026-08-23.md`.

### B. Fine oscillation / derivative concentration

If the velocity variance does not escalate, then the shell can carry large `E1` only by increasing

\[
R^3\int_{A_R}|\nabla^2V|^2,
\]

which is the critical H2 derivative-tail branch.

There is no third quiet mechanism.

---

## 6. Revised bounded-Z tail frontier

The previous trichotomy

\[
\text{spatial Type-I}
\lor H_{1,crit}^{tail}
\lor H_{2,crit}^{tail}
\]

reduces to

\[
\boxed{
\text{spatial Type-I / borderline tail}
\quad\lor\quad
\text{relative-Campanato escalation}
\quad\lor\quad
H_{2,crit}^{tail}.
}
\]

This is a genuine reduction because the middle branch is already a pre-existing local-energy/turnover frontier rather than a new tail-specific category.

---

## 7. Remaining tasks

Two bridges remain:

1. prove that persistent relative-Campanato escalation either activates the exact turnover ledger or reduces to a coherent affine corridor with an explicit finite-stage tax;
2. transfer `H2crit_tail` to the prelimit remote derivative/H branch or rule it out directly by recurrent/dissipative dynamics.

If both succeed, the only bounded-Z ancient tail survivor with no H/T is the spatial Type-I / borderline `1/R` corridor.

Status: **THE CRITICAL H1/ENSTROPHY TAIL IS NOT AN INDEPENDENT FINAL ESCAPE. STANDARD SCALE-INVARIANT H2 INTERPOLATION FORCES IT INTO EITHER RELATIVE-CAMPANATO ESCALATION OR THE CRITICAL H2 DERIVATIVE TAIL. THE BOUNDED-Z TAIL FRONTIER IS NOW SPATIAL TYPE-I, CAMPANATO/TURNOVER, OR H2CRIT. GLOBAL REGULARITY REMAINS UNPROVED.**