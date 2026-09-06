# DSD M17-250 — Dyadic stopping scale extracts a scale-comparable raw spectral packet or nodal concentration

Date: 2026-09-06  
Canonical ID: **M17-250**

Status: **STOPPING-SCALE EXTRACTION / M17-224 GIVES A RAW-LAPLACIAN BUFFERED PACKET OF RADIUS `O(ell)` WITH A LOWER `H2/L2` RATIO, BUT THE PACKET'S OWN INTRINSIC SCALE MAY BE STRICTLY SMALLER THAN ITS SUPPORT RADIUS. ITERATE A FIXED-RATIO DYADIC RAW-NUMERATOR / BUFFERED-DENOMINATOR SELECTION INSIDE THE ROOT BUFFER AND MONITOR `Q(B)=r(B)^4 H(B)/E(B)`. EVERY PARENT HAS A CHILD WITH `Q_child >= alpha Q_parent` FOR A FIXED `alpha>0`. IF `Q` FIRST FALLS BELOW A FIXED LARGE THRESHOLD, THE FIRST-CROSSING CHILD AUTOMATICALLY SATISFIES `alpha C <= Q <= C`, SO ITS PHYSICAL RADIUS IS COMPARABLE TO ITS OWN `H2/L2` INTRINSIC SCALE. IF NO CROSSING EVER OCCURS, THE NESTED BALLS SHRINK TO ONE POINT. THAT POINT MUST SATISFY `W=0`; OTHERWISE CONTINUITY WOULD GIVE `Q(B_r)->0`. THUS THE ONLY FAILURE OF SCALE-COMPARABLE EXTRACTION IS A GENUINE NODAL CONCENTRATION BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Root raw spectral packet

Start from an M17-224 buffered packet.

Let `B_0` be its physical buffer, with radius

\[
 r_0>0,
\]

and let `K_0\Subset B_0` be an inner raw-Laplacian core.

Define

\[
E_0:=\int_{B_0}|W|^2dy,
\qquad
H_0:=\int_{K_0}|\Delta W|^2dy.
\]

Assume `E_0>0`, `H_0>0` and define the dimensionless spectral number

\[
\boxed{
Q_0:=r_0^4\frac{H_0}{E_0}.
}
\]

M17-224 provides a root packet for which `Q_0` is bounded below by a fixed positive constant after the geometric factor between `r_0` and the shell intrinsic scale is absorbed.

The remaining issue is that `Q_0` may be arbitrarily large.

If it is, the packet support is much larger than its own derivative correlation scale.

---

## 2. One dyadic raw child selection

Fix once and for all a child scale factor

\[
0<\lambda<1,
\]

for example `lambda=1/2`.

Suppose at level `n` we have a buffer `B_n` of radius `r_n`, an inner core `K_n`, and

\[
E_n:=\int_{B_n}|W|^2dy,
\qquad
H_n:=\int_{K_n}|\Delta W|^2dy.
\]

Cover `K_n` by finitely-overlapping core cells of radius `lambda r_n` with smooth square partition

\[
\sum_m\chi_{n,m}^2=1
\quad\text{on }K_n.
\]

Assign to each core cell a slightly larger buffer cutoff `zeta_{n,m}` supported in `B_n`, equal to one on a neighborhood of the core cell, and with uniformly finite overlap.

Set

\[
h_{n,m}
:=\int_{K_n}\chi_{n,m}^2|\Delta W|^2dy,
\]

and

\[
e_{n,m}
:=\int \zeta_{n,m}^2|W|^2dy.
\]

Then

\[
\sum_m h_{n,m}=H_n,
\]

while finite overlap gives

\[
\sum_m e_{n,m}\le C_B E_n
\]

with one fixed geometric constant `C_B`.

Hence some child `m_n` satisfies

\[
\boxed{
\frac{h_{n,m_n}}{e_{n,m_n}}
\ge c_B\frac{H_n}{E_n},
\qquad
c_B:=C_B^{-1}>0.
}
\]

Let `B_{n+1}` be the selected child buffer, with radius comparable to

\[
r_{n+1}=\lambda r_n,
\]

and set

\[
E_{n+1}:=e_{n,m_n},
\qquad
H_{n+1}:=h_{n,m_n}.
\]

All `H_n` are raw `|Delta W|^2` charges; no cutoff derivative creates the numerator.

---

## 3. Dimensionless spectral number has a one-step lower transfer

Define at every level

\[
\boxed{
Q_n:=r_n^4\frac{H_n}{E_n}.
}
\]

The child estimate gives

\[
\begin{aligned}
Q_{n+1}
&=r_{n+1}^4\frac{H_{n+1}}{E_{n+1}}\\
&\ge
\lambda^4r_n^4c_B\frac{H_n}{E_n}.
\end{aligned}
\]

Therefore

\[
\boxed{
Q_{n+1}\ge\alpha Q_n,
\qquad
\alpha:=c_B\lambda^4>0.
}
\]

This lower transfer is the key stopping-time fact.

`Q` is allowed to increase or decrease, but it cannot jump downward by an arbitrarily large factor in one selected dyadic step.

---

## 4. First crossing gives scale comparability

Fix a threshold

\[
C_*>\max\{1,Q_{min}\}
\]

large enough for the root bookkeeping, where `Q_min>0` is the fixed root lower bound supplied by M17-224.

If

\[
Q_0\le C_*,
\]

then the root packet is already scale comparable.

Otherwise suppose

\[
Q_0>C_*.
\]

Choose the first index `N>=1` for which

\[
Q_N\le C_*.
\]

Then by minimality

\[
Q_{N-1}>C_*.
\]

The one-step lower transfer yields

\[
Q_N\ge\alpha Q_{N-1}>\alpha C_*.
\]

Hence

\[
\boxed{
\alpha C_*<Q_N\le C_*.
}
\]

Define the child's own intrinsic scale

\[
\ell_N
:=\left(\frac{E_N}{H_N}\right)^{1/4}.
\]

Because

\[
Q_N=r_N^4\frac{H_N}{E_N}
=\left(\frac{r_N}{\ell_N}\right)^4,
\]

we obtain

\[
\boxed{
(\alpha C_*)^{1/4}
<\frac{r_N}{\ell_N}
\le C_*^{1/4}.
}
\]

Thus

\[
\boxed{
r_N\asymp\ell_N}
\]

with constants independent of the shell radius, packet amplitude, and stopping depth.

This is the desired **scale-comparable raw spectral packet**.

---

## 5. If no crossing occurs, the nested balls converge to a nodal point

Suppose instead that

\[
\boxed{
Q_n>C_*
\qquad\forall n<\infty.
}
\]

The radii satisfy

\[
r_n=\lambda^n r_0\to0.
\]

Choose the child buffers nested, after a harmless fixed geometric shrink of the inner core if necessary, so

\[
\overline{B_{n+1}}\subset\overline{B_n}.
\]

Their intersection consists of one point

\[
\boxed{
y_*\in\bigcap_n\overline{B_n}.}
\]

Assume for contradiction that

\[
W(y_*)\ne0.
\]

By continuity there are `a_*>0` and `r_*>0` such that

\[
|W(y)|\ge a_*
\]

on `B_{r_*}(y_*)`.

Smoothness gives a finite local ceiling

\[
|\Delta W(y)|\le L_*
\]

on the same ball.

For all sufficiently large `n`, `B_n` lies inside this neighborhood, so

\[
E_n\gtrsim a_*^2r_n^3,
\qquad
H_n\lesssim L_*^2r_n^3.
\]

Therefore

\[
Q_n
=r_n^4\frac{H_n}{E_n}
\lesssim
r_n^4\frac{L_*^2}{a_*^2}
\to0,
\]

contradicting `Q_n>C_*`.

Hence

\[
\boxed{W(y_*)=0.}
\]

So nontermination of the stopping scale is not a generic scale-mismatch branch.

It is a genuine **nodal concentration** branch.

---

## 6. Canonical dichotomy

The root M17-224 packet therefore obeys

\[
\boxed{
H_{raw\ intrinsic\ spectral\ packet}
\Longrightarrow
H_{scale\text{-}comparable\ raw\ packet}
\lor
G_{nodal\ concentration}.
}
\]

On the first branch there is a physical buffer `B` with radius `r` and own intrinsic scale

\[
\ell=(E/H)^{1/4}
\]

such that

\[
\boxed{
r\asymp\ell.}
\]

On the second branch the selected raw derivative concentration collapses onto an actual zero of the original vorticity field.

---

## 7. Relation to M17-232

M17-232 proves that relative-amplitude descent can be physically re-extracted at successively smaller scales.

M17-250 uses a different stopping variable:

\[
Q(B)=r^4H/E.
\]

It does not subtract means and does not assign homogeneous CE-H to descendant fluctuations.

Every level uses the original physical field `W` and raw `Delta W`.

Thus the two modules are compatible but logically distinct:

- M17-232 validates finite concentration ladders after mean removal;
- M17-250 extracts the first physical scale at which support radius and own `H2/L2` scale are comparable, or else identifies an actual nodal point.

---

## 8. Why this matters for the linear-tangent route

For a scale-comparable packet, rescaling by its own `ell` no longer leaves an uncontrolled support ratio.

If

\[
y=q+\ell z,
\]

then the normalized spatial buffer lies in one fixed `z`-ball.

This removes one of the compactness obstructions recorded after M17-249.

It does **not** yet prove:

1. an upper compactness bound for all derivatives;
2. nonzero strong `L2` convergence;
3. backward lifetime tending to infinity;
4. vanishing ambient/nonlocal forcing;
5. vanishing interface/cutoff forcing.

Those remain separate obligations.

---

## 9. DSD audit

- A numerical intrinsic scale is not identified with a physical packet radius without the stopping argument.
- The child lower-transfer estimate is derived from raw numerator and buffered denominator finite overlap.
- First crossing gives both lower and upper control of `Q`, not only a lower spectral bound.
- Infinite dyadic descent is not declared impossible.
- If no stopping scale exists, the nested intersection is proved to lie in `W=0`.
- No finite nodal vanishing-order theorem is imported here.
- The nodal concentration branch remains open unless a separate nodal theorem applies.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
