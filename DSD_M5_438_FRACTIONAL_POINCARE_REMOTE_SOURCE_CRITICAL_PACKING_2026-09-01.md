# DSD M5-438 — Fractional-Poincare critical packing for Galilean-invariant remote sources

Date: 2026-09-01

Status: **RIGOROUS CRITICAL LOCALIZATION WITHOUT BOGOVSKII ALMOST-ORTHOGONALITY / THE GALILEAN-INVARIANT REMOTE-SOURCE OSCILLATION LOWER BOUND OF M5-437 COMBINED WITH THE SCALE-`1/2` FRACTIONAL POINCARE INEQUALITY GIVES `||u||_{dot H^(1/2)}^2 >= c nu^2 (R/r)^4` FOR ONE FIXED-FRACTION REMOTE STRAIN SOURCE / FOR PHYSICALLY DISJOINT SOURCE ANNULI ACTING AT THE SAME TIME, THE LOCAL GAGLIARDO SEMINORMS ADD DIRECTLY AND GIVE `X(t) >= c nu^2 sum K_n^4` / NO FOURIER ORTHOGONALITY OF CUTOFF/BOGOVSKII PACKETS IS USED / THIS SOLVES THE SIMULTANEOUS-ACTIVE-SOURCE PACKING PROBLEM BUT NOT YET THE PERSISTENCE OF HISTORICAL FROZEN SOURCES / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fractional Poincare on a fixed-shape annulus

Let `D_1` be a fixed bounded connected Lipschitz annular domain in `R^3`, and let

\[
D_R=x_0+RD_1.
\]

For scalar or vector-valued `v in dot H^(1/2)(D_R)`, the fractional Poincare inequality gives

\[
\boxed{
\inf_{c\in\mathbb R^3}
\|v-c\|_{L^2(D_R)}^2
\le
C_PR
\iint_{D_R\times D_R}
\frac{|v(x)-v(y)|^2}{|x-y|^4}\,dx\,dy.
}
\]

Equivalently,

\[
\boxed{
R^{-1}
\inf_c\|v-c\|_{L^2(D_R)}^2
\le
C_P[v]_{\dot H^{1/2}(D_R)}^2.
}
\]

The factor `R` is forced by scaling: both sides of the second form scale like velocity-squared times length-squared.

The constant depends only on the fixed reference annulus.

---

## 2. One remote source forces global critical mass

At a first-hitting target scale `r`, let a fixed-fraction remote source lie at physical radius `R`.

M5-437 gives

\[
\inf_c
\|u-c\|_{L^2(D_R)}^2
\ge
c_s\nu^2\frac{R^5}{r^4}.
\]

Apply fractional Poincare:

\[
[u]_{\dot H^{1/2}(D_R)}^2
\ge
c\nu^2\frac{R^4}{r^4}.
\]

Define

\[
K:=\frac Rr.
\]

Then

\[
\boxed{
[u]_{\dot H^{1/2}(D_R)}^2
\ge
c\nu^2K^4.
}
\]

Since the local Gagliardo seminorm is bounded above by the global one,

\[
\boxed{
X(t):=\|u(t)\|_{\dot H^{1/2}(\mathbb R^3)}^2
\ge
c\nu^2K^4.
}
\]

Thus a genuinely remote fixed-fraction source is automatically a large critical object in a Galilean-invariant sense.

---

## 3. Simultaneous disjoint source annuli add exactly at the local-seminorm level

Suppose at one physical time `t` there are source domains

\[
D_n
\]

with fixed-shape geometry, radii `R_n`, and pairwise disjoint physical supports.

For each `n`, assume the source feeds a target scale `r_n` with a fixed strain fraction and set

\[
K_n:=R_n/r_n.
\]

The local seminorm is

\[
[u]^2_{\dot H^{1/2}(D_n)}
=
C\iint_{D_n\times D_n}
\frac{|u(x)-u(y)|^2}{|x-y|^4}dxdy.
\]

Because the integrand is nonnegative and the product sets `D_n x D_n` are disjoint subsets of `R^3 x R^3`, one has

\[
\boxed{
\sum_n
[u]^2_{\dot H^{1/2}(D_n)}
\le
\|u\|_{\dot H^{1/2}(\mathbb R^3)}^2.
}
\]

No cross-term estimate is needed.

Combining with the source lower bounds,

\[
\boxed{
X(t)
\ge
c\nu^2
\sum_nK_n^4.
}
\]

This is a rigorous simultaneous-source critical packing law.

---

## 4. Why this avoids the M5-435 operator gap

The first version of M5-435 tried to use compact solenoidal packets

\[
P_{R_n}(\chi_{R_n}u-b_{R_n})
\]

and Fourier separation.

That route required proving that the family of localization/Bogovskii operators is almost orthogonal in homogeneous `dot H^(1/2)`. M5-437 shows why this is delicate: local constants can be converted by cutoff geometry into artificial natural-frequency packets.

M5-438 uses neither those packet operators nor their Fourier cross terms.

Instead it uses the genuinely Galilean-invariant quantity

\[
\inf_c\int_{D_n}|u-c|^2
\]

and the positive local Gagliardo energy already contained in the global homogeneous Sobolev norm.

Thus the common-time inequality is unconditional once the remote sources themselves coexist at that time.

---

## 5. Fifth-root form

Write

\[
R_n=a_nr_n^{4/5}.
\]

Then

\[
K_n^4
=
a_n^4r_n^{-4/5}.
\]

For one remote source,

\[
\boxed{
X(t_n)
\ge
c\nu^2a_n^4r_n^{-4/5}.
}
\]

Even when the physical source energy

\[
\nu^2a_n^5
\]

tends to zero on the non-atomic sub-fifth branch, its scale-critical cost can diverge because of the factor `r_n^(-4/5)`.

This makes precise the distinction between physical-energy sub-saturation and critical-norm escalation.

---

## 6. Relation to the global L4_t dot H1/2 ledger

M5-430 gives

\[
\int_0^{T_*}X(t)^2dt<\infty.
\]

If a fixed-fraction source at separation `K_j` persists for a physical time comparable to the current first-hitting stage length `~r_j^2/nu`, then M5-438 gives

\[
\int_{I_j}X(t)^2dt
\gtrsim
\nu^3r_j^2K_j^8,
\]

recovering the individual eighth-power remote packing law of M5-430 through a fully Galilean-invariant local oscillation argument.

The new issue for the frozen historical conveyor is not the one-source bound; it is whether an old source's **oscillatory variance modulo constants** remains large after it ceases to be an active strain payer.

---

## 7. Exact remaining gap

M5-434 freezes a compact localized historical packet on the quiet corridor. M5-437 shows that raw cutoff packets can contain constant-mode localization artifacts.

Therefore the next lemma must establish persistence of

\[
\boxed{
E_{osc,n}(t)
:=
\inf_c
\int_{D_n(t)}|u(x,t)-c|^2dx
}
\]

itself, or an equivalent Galilean-invariant oscillation quantity.

If that succeeds, frozen source domains can be observed at one common time and M5-438 will give the previously conditional cumulative critical packing rigorously.

---

## 8. Audit verdict

### Proved

\[
\boxed{
\text{one fixed-fraction remote source at }K=R/r
\Longrightarrow
\|u\|_{\dot H^{1/2}}^2
\gtrsim\nu^2K^4.
}
\]

For simultaneous disjoint remote sources,

\[
\boxed{
\|u\|_{\dot H^{1/2}}^2
\gtrsim
\nu^2\sum K_n^4.
}
\]

### Corrected

No cutoff/Bogovskii almost-orthogonality theorem is required for simultaneous active-source packing.

### Open

- Galilean-invariant variance freezing for historical source shells;
- cumulative critical packing of the frozen stack;
- frozen-conveyor rigidity;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
