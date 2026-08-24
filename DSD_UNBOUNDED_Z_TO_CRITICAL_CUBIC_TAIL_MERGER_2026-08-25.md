# DSD Unbounded-Z -> Critical Cubic-Tail Merger

Date: 2026-08-25

Status: **AMPLITUDE-SENSITIVE UNBOUNDED-Z / CUBIC-TAIL MERGER DERIVED / H-ALTERNATIVE RETAINED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Continue the unbounded normalized enstrophy branch

\[
Z=\|\Omega\|_2^2\to\infty,
\qquad
\|\Omega\|_\infty\le1.
\]

`DSD_UNBOUNDED_Z_WEIGHTED_MOMENT_KINETIC_DICHOTOMY_2026-08-25.md` showed that a remote shell with vorticity mass

\[
m_k:=\int_{A_k}|\Omega|^2dy
\]

obeys the dichotomy

\[
\Gamma_k>\Gamma_*
\quad\Longrightarrow\quad H_{remote},
\]

or, on the non-H lane,

\[
\|f_k\|_2^2
\ge
c_0R_k^2m_k,
\]

for the compact divergence-free Bogovskii velocity packet `f_k` supported in a fixed-factor enlarged annulus `A_k^+` of radius `R_k`.

The present note converts this kinetic reservoir into critical velocity `L3` mass without any fixed shell-amplitude hypothesis.

---

## 2. Compact-support reverse Hölder estimate

Because `f_k` is supported in a fixed-shape annulus of volume

\[
|A_k^+|\le C_A R_k^3,
\]

Hölder gives

\[
\|f_k\|_2
\le
|A_k^+|^{1/6}\|f_k\|_3
\le
C_A^{1/6}R_k^{1/2}\|f_k\|_3.
\]

Hence

\[
\boxed{
\|f_k\|_3^3
\ge
C_A^{-1/2}R_k^{-3/2}\|f_k\|_2^3.
}
\]

Insert the non-H kinetic lower bound:

\[
\|f_k\|_2^3
\ge
c_0^{3/2}R_k^3m_k^{3/2}.
\]

Therefore

\[
\boxed{
\|f_k\|_3^3
\ge
c_1(R_km_k)^{3/2}.
}
\]

This is exactly a scale-critical cubic shell quantity.

---

## 3. Transfer from the corrected packet back to the physical velocity

The packet is

\[
f_k=\chi_kU-b_k,
\]

where `b_k` is the Bogovskii correction on the fixed-shape transition annuli.

The standard scale-invariant Bogovskii estimate on `L3` gives

\[
\|b_k\|_3
\le
C_B\,R_k\|\nabla\chi_k\cdot U\|_3
\le
C_B'\|U\|_{L^3(\operatorname{trans}_k)}.
\]

Thus

\[
\|f_k\|_3
\le
\|\chi_kU\|_3+\|b_k\|_3
\le
C_{loc,3}\|U\|_{L^3(A_k^+)}.
\]

Consequently

\[
\boxed{
\int_{A_k^+}|U|^3dy
\ge
c_2(R_km_k)^{3/2}
}
\]

for every non-H shell.

No fixed lower bound on `m_k` is assumed.

---

## 4. Aggregate shell inequality

Choose dyadic shells

\[
R_k=2^kR_0.
\]

The enlarged annuli have uniformly bounded overlap. After passing to one of finitely many disjoint color classes if necessary,

\[
\int_{|y|>cR_0}|U|^3dy
\ge
c_3
\sum_{k\in NH}(R_km_k)^{3/2}.
\]

Thus

\[
\boxed{
\text{non-H remote enstrophy mass}
\Longrightarrow
\text{critical cubic velocity tail mass}.
}
\]

---

## 5. Lower bound in terms of total remote enstrophy

Let

\[
Z_{ext}:=\sum_{k\in NH}m_k.
\]

Set

\[
a_k:=(R_km_k)^{3/2}.
\]

Then

\[
m_k=a_k^{2/3}R_k^{-1}.
\]

Hölder with exponents `3/2` and `3` gives

\[
\begin{aligned}
Z_{ext}
&=\sum_ka_k^{2/3}R_k^{-1}\\
&\le
\left(\sum_ka_k\right)^{2/3}
\left(\sum_kR_k^{-3}\right)^{1/3}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_k(R_km_k)^{3/2}
\ge
\frac{Z_{ext}^{3/2}}
{\left(\sum_kR_k^{-3}\right)^{1/2}}.
}
\]

For `R_k=2^kR_0`,

\[
\sum_{k=0}^\infty R_k^{-3}
=
\frac{8}{7}R_0^{-3}.
\]

Hence

\[
\boxed{
\sum_k(R_km_k)^{3/2}
\ge
\sqrt{\frac78}\,
R_0^{3/2}Z_{ext}^{3/2}.
}
\]

Combining with Section 4,

\[
\boxed{
\int_{|y|>cR_0}|U|^3dy
\ge
c_4R_0^{3/2}Z_{ext}^{3/2}
}
\]

on the non-H remote shell lane.

---

## 6. Consequence for unbounded normalized enstrophy

First-hitting analyticity bounds the vorticity mass on every fixed normalized ball. Therefore if

\[
Z_j\to\infty,
\]

then for each fixed sufficiently large `R_0`,

\[
Z_{ext,j}
=Z_j-O_{R_0}(1)
\to\infty.
\]

Hence, unless a positive weighted portion is routed to `H_remote`,

\[
\boxed{
\|U_j\|_3^3
\gtrsim
Z_j^{3/2}
}
\]

up to fixed shell-localization constants.

Equivalently,

\[
\boxed{
\|U_j\|_3
\gtrsim
Z_j^{1/2}.
}
\]

The physical `L3` norm is scale invariant under the first-hitting normalization:

\[
U_j(y)=\frac{r_j}{\nu}u(X_j+r_jy,t_j),
\]

so

\[
\boxed{
\|u(t_j)\|_3
=\nu\|U_j\|_3.
}
\]

Therefore

\[
\boxed{
Z_j\to\infty,
\quad\text{no }H_{remote}
\Longrightarrow
\|u(t_j)\|_3\to\infty.
}
\]

This is consistent with known critical regularity theory and is not itself a contradiction.

---

## 7. Branch merger

The important conclusion is structural rather than contradictory.

Previously the proof map contained two apparently separate escapes:

1. bounded-`Z` / non-`L3` critical velocity tail;
2. unbounded-`Z` diffuse normalized enstrophy escape.

The present amplitude-sensitive shell estimate shows

\[
\boxed{
\text{unbounded-}Z
\Longrightarrow
H_{remote}
\lor
\text{critical cubic velocity-tail escalation}.
}
\]

Thus the non-H part of the unbounded-`Z` branch is no longer an independent low-frequency diffuse escape. It joins the same critical cubic-tail/genealogy family already present on the bounded-`Z` route.

The distinction that remains is the strength of the cubic tail:

- bounded-`Z` survivor may have a logarithmically divergent or diffuse critical tail;
- unbounded-`Z` non-H survivor forces the critical `L3` mass itself to grow at least like `Z_j^{3/2}` in cubic mass.

---

## 8. DSD audit

For every finite shell truncation, the formed channels are

- shell radius `R_k`;
- shell enstrophy mass `m_k`;
- finite derivative ratio `Gamma_k`;
- compact solenoidal packet `f_k`;
- cubic shell charge `(R_km_k)^(3/2)`.

The infinite tail is introduced only after the finite-shell estimates are established and aggregated.

No infinite derivative hierarchy is used.

---

## 9. Updated frontier

The global proof tree can now be sharpened to

\[
\boxed{
\begin{aligned}
\text{hypothetical singular branch}
\Longrightarrow{}&
\text{recurrent/core critical cubic-tail branch}\\
&\lor H_{remote}\\
&\lor T/turnover/residual.
\end{aligned}
}
\]

The old `unbounded-Z diffuse escape` is absorbed into the first two alternatives rather than retained as a fourth independent branch.

The next genuine question is therefore the same on both bounded- and unbounded-`Z` routes:

\[
\boxed{
\text{Can a critical cubic velocity tail remain dynamically passive/persistent}
\text{ while the active recurrent core continues first-hitting amplification,}
}
\]

without paying `H_remote` or `T`?

That is now the common core-tail/genealogy frontier.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
