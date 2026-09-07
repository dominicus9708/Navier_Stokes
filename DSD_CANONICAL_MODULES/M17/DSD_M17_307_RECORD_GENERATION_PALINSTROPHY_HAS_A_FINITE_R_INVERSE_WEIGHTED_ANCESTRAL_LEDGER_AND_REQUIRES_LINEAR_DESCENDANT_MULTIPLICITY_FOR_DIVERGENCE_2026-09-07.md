# DSD M17-307 — Record-generation palinstrophy has a finite inverse-scale ancestral ledger and needs essentially linear descendant multiplicity to diverge

Date: 2026-09-07  
Canonical ID: **M17-307**

Status: **CORRECTED TRUE-RESOURCE GATE AFTER M17-306 / THE FIRST MARKED ANCIENT ELEMENT OF M5-477 HAS FINITE TOTAL PALINSTROPHY, BUT M17-306 SHOWS THAT AN UNWEIGHTED SECOND-GENERATION PALINSTROPHY BUDGET IS NOT INHERITED THROUGH THE M5-478 RECORD BLOW-DOWN. THE EXACT BLOW-DOWN SCALING DOES, HOWEVER, GIVE A FINITE CROSS-GENERATION LEDGER AFTER INSERTING THE REQUIRED INVERSE RECORD-SCALE WEIGHT. FOR ANY FIXED CELL-TIME ANNULUS `I=[-b,-a] subset (-infinity,0)` AND A GEOMETRIC RECORD FAMILY `R_m`, THE PHYSICAL ANCESTOR WINDOWS `R_m^2 I` HAVE UNIFORMLY FINITE OVERLAP AFTER PASSING TO A FIXED-CODIMENSION SUBSEQUENCE IF NECESSARY. THEREFORE `sum_m R_m^{-1} int_I ||grad Omega_m||_2^2 ds <= C P_anc < infinity`. CONSEQUENTLY, IF EACH RECORD CELL CONTAINS `N_m` PAIRWISE DISJOINT DESCENDANT WINDOWS EACH PAYING AN ORDER-ONE CELL PALINSTROPHY CHARGE, THE ANCESTRAL BUDGET ONLY FORCES `sum_m N_m/R_m < infinity`; A CONTRADICTION WOULD REQUIRE `sum_m N_m/R_m=infinity`. POLYNOMIAL OR LOGARITHMIC MULTIPLICITY IN THE RECORD INDEX IS INSUFFICIENT WHEN `R_m` GROWS GEOMETRICALLY. THIS MAKES THE INTER-GENERATION R21 DEFICIT PRECISE AND REPLACES THE INVALID UNWEIGHTED FINITE-LEDGER CLAIM OF M17-304. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. First-generation finite palinstrophy

Let

\[
(V,\Omega)(x,t)
\]

be the first marked ancient element of M5-474--477.

M5-477 proves

\[
\boxed{
\mathscr P_{anc}
:=
\int_{-\infty}^{0}
\|\nabla_x\Omega(t)\|_2^2dt
<\infty.
}
\]

Let the backward record scales of M5-478 be

\[
\boxed{
R_m=\sqrt{T_m},
\qquad
T_m\asymp q^m,
\qquad
R_m\asymp q^{m/2},
}
\]

with `q>1` fixed.

The second-generation record cells are

\[
\boxed{
V_m(y,s)=R_mV(R_my,R_m^2s),
}
\]

and

\[
\boxed{
\Omega_m(y,s)=R_m^2\Omega(R_my,R_m^2s).
}
\]

---

## 2. Fixed normalized cell-time window

Fix once and for all

\[
\boxed{
I=[-b,-a],
\qquad
0<a<b<\infty.
}
\]

This lies a positive distance away from the second-generation terminal boundary `s=0`.

The corresponding first-generation physical time interval is

\[
\boxed{
I_m^{anc}
:=R_m^2I
=[-bR_m^2,-aR_m^2].
}
\]

The exact palinstrophy scaling from M17-306 gives

\[
\boxed{
R_m^{-1}
\int_I
\|\nabla_y\Omega_m(s)\|_2^2ds
=
\int_{I_m^{anc}}
\|\nabla_x\Omega(t)\|_2^2dt.
}
\]

Thus one fixed second-generation time window has a precisely identified ancestral cost after multiplication by `R_m^-1`.

---

## 3. Finite-overlap extraction of the physical record windows

Because

\[
R_m^2\asymp q^m,
\]

the intervals

\[
[-bR_m^2,-aR_m^2]
\]

move geometrically toward backward infinity.

If `b/a<q`, then sufficiently late consecutive intervals are already disjoint up to fixed comparability constants.

For a general fixed `a,b`, choose an integer `L>=1` such that

\[
\boxed{
q^L>b/a.
}
\]

Split the record indices into the `L` residue classes modulo `L`.

Within each residue class the time intervals are eventually pairwise disjoint up to the fixed asymptotic constants in `T_m asymp q^m`.
Equivalently, the full collection has a uniformly finite overlap number

\[
\boxed{N_I<\infty.}
\]

No dynamical assumption is used here; this is only geometric spacing of the record times.

---

## 4. The true cross-generation finite ledger

Sum the identity of Section 2 over `m`.

Finite overlap gives

\[
\begin{aligned}
\sum_m
R_m^{-1}
\int_I
\|\nabla\Omega_m(s)\|_2^2ds
&=
\sum_m
\int_{I_m^{anc}}
\|\nabla\Omega(t)\|_2^2dt\\
&\le
N_I
\int_{-\infty}^{0}
\|\nabla\Omega(t)\|_2^2dt.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_m
R_m^{-1}
\int_I
\|\nabla\Omega_m(s)\|_2^2ds
\le
N_I\mathscr P_{anc}
<\infty.
}
\]

This is the correct finite ancestral palinstrophy ledger across the second-generation record cells.

Unlike M17-304, no unweighted descendant budget is claimed.

---

## 5. Descendant payment multiplicity inside one record cell

Suppose record cell `m` contains `N_m` pairwise spacetime-disjoint descendant payment regions

\[
Q_{m,1},\dots,Q_{m,N_m}
\subset
\mathbb R^3\times I
\]

such that each pays a fixed positive **cell-variable palinstrophy** amount

\[
\boxed{
\int_{Q_{m,j}}
|\nabla\Omega_m|^2dy\,ds
\ge c_*>0.
}
\]

Then disjointness gives

\[
\int_I\|\nabla\Omega_m(s)\|_2^2ds
\ge c_*N_m.
\]

Insert this into the true ancestral ledger:

\[
\boxed{
\sum_m\frac{N_m}{R_m}
\le
\frac{N_I\mathscr P_{anc}}{c_*}
<\infty.
}
\]

Thus the first-generation finite palinstrophy constrains only the **inverse-record-scale weighted payment count**.

---

## 6. Threshold for an ancestral contradiction

A contradiction with M5-477 would follow if one could prove

\[
\boxed{
\sum_m\frac{N_m}{R_m}=\infty.
}
\]

Since

\[
R_m\asymp q^{m/2},
\]

any multiplicity satisfying only a polynomial bound or lower law in the record index,

\[
N_m\asymp m^p,
\]

or a logarithmic law in the record radius,

\[
N_m\asymp (\log R_m)^p,
\]

still gives

\[
\sum_m\frac{N_m}{R_m}<\infty.
\]

Even subexponential growth

\[
N_m\le e^{o(m)}
\]

is insufficient against a fixed geometric `R_m` unless the exponent approaches the record-scale rate strongly enough.

The natural threshold is essentially

\[
\boxed{N_m\sim R_m\times\text{nonsummable correction}.}
\]

This is the inter-generation analogue of the essentially-linear-in-remote-radius deficit found conditionally in M17-305.

The two radii must not be identified: `R_m` here is a **record blow-down factor**, while the late M17 remote shell radius is a variable inside a second-generation similarity state.

---

## 7. A stronger formulation with nonuniform event charges

Let the descendant events in cell `m` carry charges `c_{m,j}>=0` rather than one fixed `c_*`.

Then

\[
\sum_jc_{m,j}
\le
\int_I\|\nabla\Omega_m(s)\|_2^2ds
\]

for pairwise disjoint events sampled from raw palinstrophy.

The ancestral ledger gives

\[
\boxed{
\sum_m
\frac1{R_m}
\sum_jc_{m,j}
<\infty.
}
\]

Therefore a true contradiction requires a descendant theorem forcing

\[
\boxed{
\sum_m
\frac1{R_m}
\sum_jc_{m,j}
=\infty.
}
\]

This is the correct weighted endpoint for any future genealogy argument that tries to charge second-generation palinstrophy back to M5-477.

---

## 8. Relation to normalized own-scale packet payments

M17-303 concerns another internal rescaling inside one second-generation similarity state:

\[
W=a_jV_j,
\qquad
y=q_j+r_jz,
\qquad
\theta=\theta_j+r_j^2\tau.
\]

Its exact weight

\[
m_j=a_j^2r_j^3
\]

must be retained before any event is compared with second-generation palinstrophy.

If that second-generation event is then charged back across the M5-478 record blow-down, the additional record factor `R_m^-1` is still required.

Schematically, a normalized gradient-interface event cannot be assigned ancestral cost larger than its correctly mapped descendant charge; the ancestry map introduces another explicit scale weight rather than removing one.

No combined formula is asserted until the exact parent-to-M17 representation and record-cell identity are simultaneously available on the same event.

This prevents a three-level normalization shortcut.

---

## 9. What this closes and what remains

M17-307 closes the ambiguity created by the retraction of M17-304:

- there **is** a legitimate finite resource inherited from M5-477;
- it is an `R_m^-1`-weighted cross-generation palinstrophy ledger;
- it does **not** make fixed descendant payments nonsummable;
- geometric record spacing makes ordinary repeated normalized costs cheap in the ancestor.

The remaining high-value branches are therefore:

1. a descendant multiplicity/genealogy theorem strong enough to overcome `R_m^-1`;
2. a scale-critical transfer theorem avoiding the record-scale loss;
3. strict scale descent/nodal closure;
4. a signed or monotone quantity invariant under the record blow-down;
5. closure of the parallel non-CE-H roots from M5-598.

---

## 10. DSD audit

- The first and second ancient generations are never identified.
- The record scale `R_m` is distinct from every late-M17 remote shell radius.
- The finite-overlap statement is proved from geometric record spacing, not assumed from material genealogy.
- Payment regions must be disjoint or uniformly bounded-overlap before they can be summed.
- The exact `R_m^-1` ancestry weight is retained.
- Polynomial/logarithmic event counts are not promoted to a contradiction.
- No new external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
