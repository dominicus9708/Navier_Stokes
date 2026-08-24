# DSD Unbounded-Z Weighted-Moment / Kinetic Dichotomy

Date: 2026-08-25

Status: **AMPLITUDE-SENSITIVE STATIC ROUTING DERIVED / UNBOUNDED-Z GROWTH IMPROVED ON NON-H LANE / DYNAMIC GENEALOGY CLOSURE NOT YET DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

This note attacks the normalized-enstrophy escape branch

\[
Z_j:=\|\Omega_j\|_2^2\to\infty,
\qquad
\|\Omega_j\|_\infty\le1,
\]

identified in `ANTI_PROOF_VORTICITY_ENSTROPHY_ESCAPE_AUDIT_2026-08-24.md`.

The previous audit proved only

\[
\sum_j r_j Z_j<\infty
\]

in viscosity-normalized notation, and therefore allowed slow unbounded growth.

The aim here is to exploit the spatial moment forced by large `Z_j` and the existing localized-solenoidal phase-space machinery.

---

## 2. Minimal second moment under the first-hitting amplitude cap

Let

\[
\rho(y):=|\Omega(y)|^2.
\]

The first-hitting cap gives

\[
0\le\rho\le1,
\qquad
\int_{\mathbb R^3}\rho\,dy=Z.
\]

Among all densities satisfying these constraints, the radially decreasing rearrangement minimizing

\[
I_2:=\int |y|^2\rho(y)dy
\]

is the indicator of a ball of volume `Z`.

Let

\[
R_Z:=\left(\frac{3Z}{4\pi}\right)^{1/3}.
\]

Then

\[
I_2
\ge
\int_{B_{R_Z}}|y|^2dy
=
\frac{4\pi}{5}R_Z^5.
\]

Therefore

\[
\boxed{
I_2
\ge
C_{mom}Z^{5/3},
}
\]

with

\[
\boxed{
C_{mom}
=
\frac{3^{5/3}}{5(4\pi)^{2/3}}
\approx0.23090083894.
}
\]

Thus large normalized enstrophy necessarily carries a large normalized radius-squared moment even if it is arbitrarily diffuse.

---

## 3. Dyadic shell decomposition

Fix a finite core radius `R_0` and decompose the exterior into fixed-shape dyadic annuli

\[
A_k
=
\{2^kR_0<|y|<2^{k+1}R_0\},
\qquad
R_k:=2^kR_0.
\]

Define shell enstrophy

\[
\boxed{
m_k:=\int_{A_k}|\Omega|^2dy.}
\]

Up to fixed geometric constants,

\[
\boxed{
I_{2,ext}
\asymp
\sum_kR_k^2m_k.
}
\]

Hence unbounded `Z` eventually forces a large weighted shell ledger unless the entire growth is confined to the fixed core, which is excluded by the uniform first-hitting analytic bound on every fixed normalized ball.

---

## 4. Localized solenoidal velocity packet

Use the existing Bogovskii shell localization on the normalized velocity `U`.

For each shell construct

\[
f_k=\chi_kU-b_k,
\]

so that

\[
\nabla\cdot f_k=0,
\qquad
\operatorname{supp}f_k\subset A_k^+,
\qquad
f_k=U\quad\text{on }A_k,
\]

where the enlarged shells `A_k^+` have uniformly bounded overlap.

The localization estimate gives

\[
\boxed{
\|f_k\|_2
\le
C_{loc}\|U\|_{L^2(A_k^+)}.
}
\]

Pointwise,

\[
|\nabla\times U|^2
\le2|\nabla U|^2.
\]

Since `f_k=U` on `A_k`,

\[
\|\nabla f_k\|_2^2
\ge
\int_{A_k}|\nabla U|^2dy
\ge
\frac12m_k.
\]

Thus

\[
\boxed{
\|\nabla f_k\|_2^2\ge\frac12m_k.
}
\]

---

## 5. Shell derivative ratio and non-H conversion

Define the dimensionless packet derivative ratio

\[
\Gamma_k
:=
\frac{R_k\|\nabla f_k\|_2}{\|f_k\|_2}.
\]

Fix a finite threshold `Gamma_*`.

### High derivative alternative

If

\[
\Gamma_k>\Gamma_*,
\]

the shell is a scale-normalized derivative-frequency event and is routed to `H_remote`.

### Non-H alternative

If

\[
\Gamma_k\le\Gamma_*,
\]

then

\[
\|f_k\|_2^2
\ge
\frac{R_k^2}{\Gamma_*^2}
\|\nabla f_k\|_2^2
\ge
\frac{R_k^2m_k}{2\Gamma_*^2}.
\]

Using the localization upper bound,

\[
C_{loc}^2
\|U\|_{L^2(A_k^+)}^2
\ge
\|f_k\|_2^2,
\]

we obtain

\[
\boxed{
\|U\|_{L^2(A_k^+)}^2
\ge
\frac{R_k^2m_k}
{2C_{loc}^2\Gamma_*^2}.
}
\]

Thus a non-H shell carrying remote vorticity mass necessarily carries a large local kinetic reservoir.

This is amplitude-sensitive: no fixed `L3` shell occupancy floor is required.

---

## 6. Aggregate weighted-moment dichotomy

Because the enlarged dyadic shells have bounded overlap `N_ov`, summing the non-H estimate gives

\[
N_{ov}\|U\|_2^2
\ge
\sum_{k\in NH}
\|U\|_{L^2(A_k^+)}^2
\ge
\frac1{2C_{loc}^2\Gamma_*^2}
\sum_{k\in NH}R_k^2m_k.
\]

Therefore

\[
\boxed{
\sum_{k\in NH}R_k^2m_k
\le
C_{kin}\Gamma_*^2\|U\|_2^2,
}
\]

with

\[
C_{kin}:=2N_{ov}C_{loc}^2.
\]

Hence one of two things must occur:

\[
\boxed{
\text{a positive fraction of the weighted vorticity moment lies in }H_{remote}
}
\]

or

\[
\boxed{
I_{2,ext}
\lesssim
\Gamma_*^2\|U\|_2^2.
}
\]

This is the desired amplitude-sensitive remote-enstrophy routing.

---

## 7. First-hitting kinetic-energy ceiling

Use the viscosity-restored normalized variables

\[
y=\frac{x-X_j}{r_j},
\qquad
U_j(y)=\frac{r_j}{\nu}u(x,t_j),
\qquad
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
\]

Then

\[
\|u(t_j)\|_2^2
=
\nu^2r_j\|U_j\|_2^2.
\]

The physical energy inequality yields

\[
\boxed{
\|U_j\|_2^2
\le
\frac{\|u_0\|_2^2}{\nu^2r_j}.
}
\]

Therefore on the non-H weighted-moment lane,

\[
I_{2,j}
\lesssim
\Gamma_*^2
\frac{\|u_0\|_2^2}{\nu^2r_j}
\]

up to the fixed core contribution and localization constants.

---

## 8. Improved growth bound for unbounded normalized enstrophy

Combine the moment lower bound

\[
C_{mom}Z_j^{5/3}
\le I_{2,j}
\]

with the non-H kinetic ceiling.

Then

\[
Z_j^{5/3}
\lesssim
\Gamma_*^2
\frac{\|u_0\|_2^2}{\nu^2r_j}.
\]

Thus

\[
\boxed{
Z_j
\lesssim
\left(
\Gamma_*^2
\frac{\|u_0\|_2^2}{\nu^2r_j}
\right)^{3/5}
}
\]

on the no-`H_remote` lane.

In particular,

\[
\boxed{
Z_j=O(r_j^{-3/5})
}
\]

rather than the much weaker energy-dissipation allowance `o(r_j^{-1})` from the previous audit.

Therefore an unbounded-`Z` survivor that avoids remote derivative-frequency activity has a sharply restricted growth exponent.

---

## 9. Radius consequence

The minimal half-mass/filled-ball scale satisfies schematically

\[
R_{Z,j}\gtrsim Z_j^{1/3}.
\]

The improved bound gives

\[
R_{Z,j}\lesssim r_j^{-1/5}
\]

at the extremal growth scale on the non-H lane.

Hence the corresponding physical halo radius obeys

\[
\boxed{
r_jR_{Z,j}\lesssim r_j^{4/5}\to0.}
\]

So the unbounded normalized halo is remote only in the shrinking first-hitting coordinates; in physical coordinates it still collapses toward the candidate singular point.

Its own parabolic time, however, is larger than the current-core remaining time by the factor

\[
R_{Z,j}^2\to\infty.
\]

This is precisely the regime where the repository's remaining-time compression / historical-shell forgetting machinery becomes relevant.

---

## 10. DSD audit

The unbounded-`Z` escape is now reduced to finite typed alternatives:

\[
\boxed{
Z_j\to\infty
\Longrightarrow
H_{remote}^{weighted}
\lor
\text{large finite kinetic/relative-variance reservoir}.
}
\]

On the second lane,

\[
Z_j=O(r_j^{-3/5}).
\]

No infinite shell population is treated as one formed DSD object. The dyadic argument is performed on arbitrary finite shell truncations; the weighted-moment conclusion is then passed through the ordinary aggregation/limit layer.

---

## 11. Remaining dynamic gate

The remaining task is no longer to prove that diffuse unbounded enstrophy has a packet structure at fixed cubic amplitude.

The amplitude-sensitive result already gives either derivative-frequency activity or a large local kinetic reservoir.

The next gate is:

\[
\boxed{
\text{Can the large non-H kinetic reservoir at normalized radius }R_j\to\infty
\text{ persist/relabel across shrinking first-hitting scales without paying }T?
}
\]

Because the time remaining after stage `j` is only `O(r_j^2/nu)` while the reservoir's own natural time is `O(r_j^2R_j^2/nu)`, quiet rebuilding/forgetting has only an `O(R_j^{-2})` fraction of a natural time available.

This should be combined next with `MOVING_RELATIVE_VARIANCE_TURNOVER_LEDGER_2026-08-23.md` and `SLIDING_HISTORY_REMAINING_TIME_CLOSURE_2026-08-23.md`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
