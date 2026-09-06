# DSD M17-261 — Fixed-K packet plateau excludes coherent-mean normalized mass decompactification

Date: 2026-09-06  
Canonical ID: **M17-261**

Status: **CORRECTION / STRENGTHENING OF M17-256. THE M17-256 FIXED-`K` MASS-DECOMPACTIFICATION AUDIT USED POINCARE TO SHOW THAT A PALINSTROPHY-QUIET LARGE SURROUNDING MASS MUST BE MEAN DOMINATED, BUT IT DID NOT REUSE A CRUCIAL PROPERTY OF THE SELECTED M17-224/251 PACKET: ITS DENOMINATOR CUTOFF IS IDENTICALLY ONE ON A FIXED-VOLUME PLATEAU OF SIZE `~r_j^3`. IF THE FIXED LARGER BALL IS MEAN DOMINATED, CHEBYSHEV SHOWS THAT THIS PLATEAU IS ALSO MEAN DOMINATED EXCEPT on `o(r_j^3)` VOLUME. THE PACKET DENOMINATOR THEN SATISFIES `E_j >= c |c_j|^2 r_j^3`, WHILE THE ENTIRE FIXED-`K` BALL HAS MASS only `<= C_K |c_j|^2 r_j^3`. CONSEQUENTLY `M_{j,K}/E_j` IS BOUNDED, CONTRADICTING NORMALIZED MASS DECOMPACTIFICATION. THEREFORE AT FIXED `K`, DECOMPACTIFICATION CANNOT SURVIVE AS A COHERENT-MEAN BRANCH: IT FORCES DIVERGENT NORMALIZED PALINSTROPHY. THE M17-257 COHERENT-MEAN PROJECTED BRANCH IS NOT NEEDED FOR THIS FIXED-`K` FRONTIER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Packet plateau inherited from M17-224/251

Let the selected packet denominator be

\[
\boxed{
E_j:=\int \zeta_j^2|W_j|^2dy.
}
\]

The M17-224 buffered construction gives a fixed plateau region `P_j` such that

\[
\boxed{
\zeta_j\equiv1\quad\text{on }P_j,
\qquad
|P_j|\ge v_0r_j^3
}
\]

for one fixed `v_0>0` independent of `j`.

Hence

\[
\boxed{
E_j\ge\int_{P_j}|W_j|^2dy.
}
\]

This lower-support property was not used in the M17-256 coherent-mean residual.

---

## 2. Fixed-K surrounding mass

Fix one finite `K>1` large enough that the packet support lies inside

\[
B_{Kr_j}(q_j).
\]

Define

\[
M_{j,K}:=\int_{B_{Kr_j}(q_j)}|W_j|^2dy
\]

and

\[
L_{j,K}:=\frac{M_{j,K}}{E_j}.
\]

The M17-255 decompactification branch is

\[
\boxed{L_{j,K}\to\infty}
\]

for some fixed `K`.

---

## 3. Mean/fluctuation split

Let

\[
c_{j,K}:=\fint_{B_{Kr_j}}W_jdy,
\qquad
w_{j,K}:=W_j-c_{j,K}.
\]

Set

\[
F_{j,K}:=\int_{B_{Kr_j}}|w_{j,K}|^2dy.
\]

Orthogonality gives

\[
\boxed{
M_{j,K}
=F_{j,K}+|B_{Kr_j}|\,|c_{j,K}|^2.
}
\]

---

## 4. Fluctuation-dominated case already forces normalized palinstrophy

If for some fixed `theta>0`

\[
F_{j,K}\ge\theta M_{j,K},
\]

mean-zero Poincare gives

\[
F_{j,K}
\le C(Kr_j)^2
\int_{B_{Kr_j}}|\nabla W_j|^2dy.
\]

Therefore

\[
\boxed{
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\ge c_{K,\theta}\frac{M_{j,K}}{E_j}
=c_{K,\theta}L_{j,K}.
}
\]

Thus if `L_{j,K}->infinity`, this branch has divergent normalized palinstrophy.

The only possible quiet branch would have

\[
\boxed{
\frac{F_{j,K}}{M_{j,K}}\to0.
}
\]

---

## 5. Quiet mean dominance propagates to the packet plateau

Assume the quiet mean-dominated branch.

Then

\[
M_{j,K}\sim |B_{Kr_j}|\,|c_{j,K}|^2.
\]

Define the cancellation set

\[
A_j
:=
\left\{
|w_{j,K}|>\frac12|c_{j,K}|
\right\}.
\]

Chebyshev gives

\[
|A_j|
\le
\frac{4F_{j,K}}{|c_{j,K}|^2}.
\]

Because

\[
|c_{j,K}|^2
\sim
\frac{M_{j,K}}{|B_{Kr_j}|},
\]

we obtain

\[
\boxed{
|A_j|
\le
C|B_{Kr_j}|
\frac{F_{j,K}}{M_{j,K}}
=o(r_j^3)
}
\]

since `K` is fixed.

The plateau satisfies

\[
|P_j|\ge v_0r_j^3.
\]

Hence for sufficiently large `j`,

\[
\boxed{
|P_j\setminus A_j|
\ge\frac{v_0}{2}r_j^3.
}
\]

On this good portion,

\[
|W_j|
=|c_{j,K}+w_{j,K}|
\ge\frac12|c_{j,K}|.
\]

---

## 6. The denominator captures the coherent mean

Because `zeta_j=1` on `P_j`, Section 5 gives

\[
\begin{aligned}
E_j
&\ge
\int_{P_j\setminus A_j}|W_j|^2dy\\
&\ge
\frac14|c_{j,K}|^2
|P_j\setminus A_j|.
\end{aligned}
\]

Therefore

\[
\boxed{
E_j
\ge c_0|c_{j,K}|^2r_j^3
}
\]

with fixed `c_0>0`.

On the other hand,

\[
M_{j,K}
\sim
|B_{Kr_j}|\,|c_{j,K}|^2
=C_3K^3|c_{j,K}|^2r_j^3.
\]

Hence

\[
\boxed{
\frac{M_{j,K}}{E_j}
\le C_K<\infty.
}
\]

This contradicts

\[
L_{j,K}\to\infty.
\]

Thus the quiet coherent-mean decompactification alternative is impossible at fixed `K`.

---

## 7. Strengthened fixed-K gate

The corrected result is

\[
\boxed{
G_{normalized\ mass\ decompactification}^{fixed\ K}
\Longrightarrow
H_{divergent\ normalized\ palinstrophy}.
}
\]

There is no additional coherent-mean terminal branch at fixed `K`.

Equivalently, on a normalized-palinstrophy-bounded branch, for every fixed `K`,

\[
\boxed{
\sup_j
\frac{1}{E_j}
\int_{B_{Kr_j}}|W_j|^2dy
<\infty.
}
\]

This is exactly the surrounding-mass compactness needed in M17-255.

---

## 8. Consequence for M17-257, M17-258, and M17-260

M17-257 was introduced to treat the coherent-mean residual of M17-256.

M17-261 shows that this residual cannot occur in the actual **fixed-`K` normalized-mass-decompactification gate** once the packet plateau is retained.

Therefore the current fixed-`K` frontier does not require

\[
G_{coherent\ ambient\ mean}
\]

or its projected mean-shear descendant.

M17-258 and the projected half of M17-260 remain mathematically correct conditional statements and may still be useful in other mean-renormalized settings, but they are not required to resolve the fixed-`K` M17-255 mass-compactness branch.

The raw mass-compact heat tangent is now the canonical branch.

---

## 9. Scope firewall

This correction uses `K` fixed before `j->infinity`.

It does **not** say that mass on balls with

\[
K=K_j\to\infty
\]

is uniformly controlled by the packet denominator.

Such expanding-radius mass growth is a separate global-spatial-tightness issue and must not be conflated with the fixed-cylinder compactness needed for local tangent extraction.

---

## 10. Updated narrow frontier

At fixed intrinsic cylinders,

\[
\boxed{
H_{scale\text{-}comparable\ packet}
\Longrightarrow
G_{nodal/subscale}
\lor
H_{normalized\ palinstrophy}
\lor
G_{scaled\ ambient/coefficient}
\lor
H_{raw\ mass\text{-}compact\ tangent}.
}
\]

On the last branch, M17-260 supplies CE-H temporal-direction rigidity when the scaled multiplier is non-spiking.

---

## 11. DSD audit

1. The packet denominator is not treated as an arbitrary subset mass; its fixed plateau is essential.
2. Poincare is used only on the fixed larger ball.
3. Mean dominance is converted into a denominator lower bound before any dynamic claim.
4. The correction supersedes only the coherent-mean residual of M17-256 at fixed `K`.
5. Expanding `K_j->infinity` remains open as a global tightness issue.
6. M17-257 is retained as a mathematically valid conditional module, not deleted.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
