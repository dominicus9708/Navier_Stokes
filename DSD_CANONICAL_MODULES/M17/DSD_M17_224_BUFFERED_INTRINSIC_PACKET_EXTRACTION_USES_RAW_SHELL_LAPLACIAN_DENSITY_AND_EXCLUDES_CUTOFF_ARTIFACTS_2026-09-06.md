# DSD M17-224 — Buffered intrinsic packet extraction uses raw shell Laplacian density and excludes cutoff artifacts

Date: 2026-09-06  
Canonical ID: **M17-224**

Status: **BUFFERED EXTRACTION STRENGTHENING / M17-222/223 EXTRACT COMPACT HIGH-`H2/L2` PACKETS, BUT A DSD AUDIT SHOULD DISTINGUISH TRUE `Delta W` CONCENTRATION FROM DERIVATIVES OF THE LOCALIZING CUTOFF. START DIRECTLY FROM A TEMPERED CORE SHELL WITH `H_R/E_R -> infinity`, COVER THE CORE BY INTRINSIC-SCALE CELLS, AND ASSIGN TO EACH CELL THE RAW NUMERATOR `h_m=int chi_m^2 |Delta W|^2` WHILE ASSIGNING AS DENOMINATOR THE `L2` MASS OF A LARGER BUFFER CUTOFF `zeta_m W` THAT EQUALS `W` ON THE ENTIRE NUMERATOR CELL. THE RAW NUMERATORS SUM EXACTLY TO `H_R`; THE BUFFER DENOMINATORS HAVE UNIFORMLY FINITE OVERLAP AND SUM TO AT MOST A FIXED MULTIPLE OF THE TEMPERED ENLARGED-SHELL MASS `<=C E_R`. PIGEONHOLING THEREFORE PRODUCES A BUFFERED CELL WITH `||Delta(zeta_m W)||_2^2/||zeta_m W||_2^2 >= c H_R/E_R`, AND THE LOWER BOUND COMES FROM THE REGION WHERE `zeta_m=1`, SO NO CUTOFF DERIVATIVE CAN CREATE IT. THE PACKET RADIUS MAY BE CHOSEN `A ell_R`, `ell_R=(E_R/H_R)^(1/4)`, GIVING A TRUE RAW-VORTICITY INTRINSIC-SCALE WITNESS WITH ITS TRANSITION-REGION MASS ALREADY INCLUDED IN THE NORMALIZATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Core spectral shell

Let `C_R` be a globally tempered remote shell and `C_R^*` a fixed finite-neighbor enlargement.

Define

\[
E_R:=\int_{C_R}|W|^2dy,
\qquad
H_R:=\int_{C_R}|\Delta W|^2dy.
\]

Assume

\[
\boxed{
\frac{H_R}{E_R}\to\infty.
}
\]

M17-207 temperedness gives

\[
\boxed{
E_R^*:=\int_{C_R^*}|W|^2dy
\le C_*E_R.
}
\]

Define

\[
\boxed{
\ell_R:=\left(\frac{E_R}{H_R}\right)^{1/4}\to0.
}
\]

---

## 2. Intrinsic cells and buffers

Fix a large constant `A>1` and set

\[
\boxed{r_R:=A\ell_R.}
\]

For sufficiently large `R`,

\[
r_R\ll R,
\]

so every cell meeting the core shell admits a fixed-factor buffer contained in `C_R^*`.

Choose smooth core weights `chi_m` such that on `C_R`

\[
\boxed{
\sum_m\chi_m^2=1,
}
\]

with each `chi_m` supported in a ball/cube of diameter `O(r_R)` and uniformly finite overlap.

For each core weight choose a buffer cutoff `zeta_m` satisfying

\[
0\le\zeta_m\le1,
\qquad
\boxed{\zeta_m\equiv1\text{ on a neighborhood of }\operatorname{supp}\chi_m,}
\]

with

\[
\operatorname{diam}(\operatorname{supp}\zeta_m)
\le C_A\ell_R.
\]

The buffers may be chosen with uniformly finite overlap:

\[
\boxed{
\sum_m\mathbf 1_{\operatorname{supp}\zeta_m}
\le N_A<\infty.
}
\]

---

## 3. Raw numerator and buffered denominator

Define the raw shell Laplacian charge

\[
\boxed{
h_m
:=\int_{C_R}\chi_m^2|\Delta W|^2dy.
}
\]

Because the core weights square-sum to one,

\[
\boxed{
\sum_mh_m=H_R.
}
\]

Define the buffered `L2` denominator

\[
\boxed{
e_m
:=\|\zeta_mW\|_2^2.
}
\]

Finite overlap and support inside `C_R^*` give

\[
\begin{aligned}
\sum_me_m
&=\int\left(\sum_m\zeta_m^2\right)|W|^2dy\\
&\le N_A\int_{C_R^*}|W|^2dy\\
&\le N_AC_*E_R.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_me_m\le C_BE_R.
}
\]

---

## 4. Buffered pigeonhole

If every active cell satisfied

\[
h_m<c\frac{H_R}{E_R}e_m
\]

with `c<C_B^-1`, then summing would give

\[
H_R
<c\frac{H_R}{E_R}C_BE_R
=cC_BH_R
<H_R,
\]

a contradiction.

Therefore there exists `m_R` such that

\[
\boxed{
\frac{h_{m_R}}{e_{m_R}}
\ge c_B\frac{H_R}{E_R}
=c_B\ell_R^{-4}.
}
\]

Set

\[
\boxed{G_R:=\zeta_{m_R}W.}
\]

Then

\[
\|G_R\|_2^2=e_{m_R}.
\]

---

## 5. The H2 lower bound is genuine raw `Delta W`, not a cutoff artifact

On a neighborhood of `supp chi_{m_R}`,

\[
\zeta_{m_R}\equiv1.
\]

Therefore there

\[
\boxed{
\Delta G_R=\Delta W.
}
\]

Consequently

\[
\begin{aligned}
\|\Delta G_R\|_2^2
&\ge
\int_{\operatorname{supp}\chi_{m_R}}|\Delta W|^2dy\\
&\ge
\int\chi_{m_R}^2|\Delta W|^2dy\\
&=h_{m_R}.
\end{aligned}
\]

Combining with Section 4,

\[
\boxed{
\frac{\|\Delta G_R\|_2^2}{\|G_R\|_2^2}
\ge
c_B\frac{H_R}{E_R}
=c_B\ell_R^{-4}.
}
\]

The lower bound is generated inside a region on which the cutoff is exactly constant.
No derivative of `zeta_m` contributes to the lower bound.

---

## 6. Spatial scale and remote location

The selected packet satisfies

\[
\boxed{
\operatorname{diam}(\operatorname{supp}G_R)
\le C_A\ell_R.
}
\]

Its center `q_R` lies within `O(ell_R)` of the core shell, so

\[
\boxed{
|q_R|\asymp R\to\infty.
}
\]

Hence

\[
\boxed{
\frac{\operatorname{diam}(\operatorname{supp}G_R)}{|q_R|}
\to0.
}
\]

This is a true remote intrinsic-scale packet.

---

## 7. The transition-region mass is already budgeted

A dynamic localization will differentiate `zeta_m` only in its transition region.

That region is contained in `supp zeta_m`, and its vorticity mass is bounded by

\[
\boxed{
\int_{\operatorname{supp}\nabla\zeta_m}|W|^2dy
\le e_{m_R}
=\|G_R\|_2^2.
}
\]

Thus the initial transition-region `L2` mass cannot exceed the packet normalization by an uncontrolled factor.

This is the main advantage over selecting a tiny unbuffered core first and only afterward asking how much background mass its cutoff encounters.

---

## 8. Relation to M17-223

M17-223 showed by scale-matched commutator absorption that an intrinsic-scale compact packet exists.

M17-224 strengthens the extraction in two ways:

1. the large numerator is the raw shell density `|Delta W|^2` before localization;
2. the denominator already contains the full cutoff buffer mass.

Therefore M17-223 remains valid, but M17-224 is the preferred input for the next dynamic packet-persistence calculation.

---

## 9. Dynamic frontier after buffered extraction

The current spectral hard core may now be stated as

\[
\boxed{
G_{tempered\ whole\text{-}shell\ H2/L2\ spectral}
\Longrightarrow
H_{buffered\ intrinsic\ remote\ packet}.
}
\]

The remaining task is to move `zeta_m` with a material center and control, over a time interval comparable to the packet's own parabolic scale, the terms generated by

\[
D_B\zeta_m,
\qquad
\nabla\zeta_m,
\qquad
\Delta\zeta_m.
\]

Because the buffer radius is `O(ell_R)`, these terms live exactly at the expected parabolic scaling and must be included rather than declared negligible.

---

## 10. DSD analysis

### 10.1 Numerator/denominator separation

The numerator is sampled in an inner core.
The denominator is sampled on a larger buffer.
This prevents high derivative density from being paired with an artificially tiny normalization that ignores the cutoff transition region.

### 10.2 Why finite overlap is sufficient

No lower bound on the mass of one cell is needed.
Only

\[
\sum h_m=H_R
\]

and

\[
\sum e_m\le C_BE_R
\]

are required.

### 10.3 No cutoff-generated high frequency

The final H2 lower bound is taken where the cutoff equals one.
Thus the localization cannot manufacture the spectral concentration being proved.

---

## 11. DSD audit

- The core shell and enlarged shell are kept distinct.
- Temperedness is used only for the enlarged-shell `L2` denominator.
- Raw `Delta W` density is partitioned before any intrinsic cutoff is differentiated.
- Transition-region `L2` mass is included in the selected denominator.
- Dynamic persistence is still open and is not inferred from one-time localization.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
