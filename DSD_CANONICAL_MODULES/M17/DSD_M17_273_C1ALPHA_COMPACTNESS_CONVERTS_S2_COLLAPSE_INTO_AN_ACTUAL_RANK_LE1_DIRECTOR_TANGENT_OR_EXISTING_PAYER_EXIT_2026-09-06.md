# DSD M17-273 — C1-alpha compactness converts s2 collapse into an actual Rank <=1 director tangent or an existing payer exit

Date: 2026-09-06  
Canonical ID: **M17-273**

Status: **RANK-DROP COMPACTNESS GATE / AFTER M17-272, UNBOUNDED REGULAR FOLD MULTIPLICITY ON THE PAYER-FREE RAW HEAT LANE CANNOT SURVIVE WITH A UNIFORM `s2` FLOOR. THE COMPLEMENTARY EVENT `s2 -> 0` SHOULD NOT BE LEFT ONLY AS THE LABEL `ANISOTROPY`. THE SAME PARABOLIC `C1,alpha` COMPACTNESS GIVES STRONG `C1` CONVERGENCE OF THE DIRECTOR ON EVERY NONDEGENERATE ACTIVE SUBPATCH. THEREFORE A SEQUENCE OF RANK-2 DIRECTORS WITH `s2 -> 0` HAS A LIMIT DIRECTOR WHOSE DIFFERENTIAL HAS RANK AT MOST ONE AT THE DEGENERATING POINT/REGION. IF `s1` ALSO COLLAPSES, THE LIMIT IS RANK 0 THERE; IF `s1` STAYS NONDEGENERATE, THE LIMIT IS GENUINELY RANK 1. FAILURE OF THE AMPLITUDE FLOOR, LOCAL MASS/COEFFICIENT CORRIDOR, OR COMPACT ACTIVE PATCH IS RETAINED AS THE EXISTING NODAL/PALINSTROPHY/AMBIENT/INTERFACE EXIT. THIS REPLACES AN ABSTRACT INFINITE-ANISOTROPY SEQUENCE BY A CONCRETE LOWER-RANK TANGENT OBJECT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input compactness

On a payer-free compact raw heat cylinder, M17-272 gives

\[
\boxed{\|\xi_j\|_{C^{1,\alpha}(Q_{1/2})}\le C}
\]

on every subpatch where

\[
|V_j|\ge a_*>0.
\]

By Arzela--Ascoli, after passing to a subsequence,

\[
\boxed{\xi_j\to\xi_\infty\quad\text{strongly in }C^1(Q_{1/3}).}
\]

The limit remains sphere valued:

\[
|\xi_\infty|=1.
\]

---

## 2. Singular values pass to the limit

Let

\[
s_{1,j}\ge s_{2,j}\ge0
\]

be the nonzero singular values of `D xi_j` on the Rank-2 sequence.

Strong `C1` convergence implies operator-norm convergence

\[
D\xi_j\to D\xi_\infty.
\]

Singular values are continuous under matrix perturbation, so

\[
\boxed{
s_{m,j}\to s_{m,\infty}
}
\]

pointwise uniformly on compact subsets after the subsequence.

---

## 3. Rank-1 and Rank-0 alternatives

Suppose at selected points or on a retained carrier

\[
\boxed{s_{2,j}\to0.}
\]

Then

\[
\boxed{\operatorname{rank}D\xi_\infty\le1.}
\]

Two subcases remain.

### Genuine Rank 1

If

\[
\liminf s_{1,j}\ge\delta_1>0,
\]

then

\[
\boxed{\operatorname{rank}D\xi_\infty=1.}
\]

### Rank 0

If also

\[
s_{1,j}\to0,
\]

then

\[
\boxed{D\xi_\infty=0.}
\]

On a connected component this makes the limiting director spatially constant.

---

## 4. Fixed-fraction versus pointwise rank drop

A single point of `s2 -> 0` gives a pointwise lower-rank tangent statement.

If a fixed positive packet fraction satisfies

\[
s_{2,j}\le\varepsilon_j\to0,
\]

then strong `C1` convergence transfers the rank-at-most-one property to the corresponding limit carrier, modulo boundary/nodal leakage.

If the degenerating set has vanishing packet measure, retain it as

\[
G_{rank\text{-}drop\ microcarrier/strict\ subscale}.
\]

Thus the same measure firewall used throughout M17 remains active.

---

## 5. Why this is stronger than the label `anisotropy`

The ratio

\[
K_\xi=s_1/s_2
\]

may diverge merely because `s2 -> 0`.

M17-273 records the geometric limit object instead:

\[
\boxed{
G_{s_2\to0}^{compact}
\Longrightarrow
H_{Rank1\ director\ tangent}
\lor
H_{Rank0\ director\ tangent}
\lor
G_{rank\text{-}drop\ microcarrier}.
}
\]

This prevents repeated ancestry bookkeeping from obscuring that the compact limit has changed rank.

---

## 6. Existing payer exits

The lower-rank tangent conclusion assumes:

1. local normalized mass compactness;
2. bounded scaled lower-order coefficients;
3. an active amplitude floor;
4. a compact interior patch.

Failure gives one of

\[
H_{normalized\ palinstrophy/mass\ escape}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{nodal/amplitude\ degeneration}
\lor
G_{interface/domain}.
\]

No lower-rank tangent is asserted across such a failure.

---

## 7. Next target

The next canonical task is to classify the actual Rank-1 and Rank-0 raw CE-H heat tangents rather than continuing to refer to them only as rank loss.

The weighted harmonic-map equation of M17-269 is particularly rigid at Rank 1.

---

## 8. DSD audit

- Rank is passed through strong `C1`, not weak convergence.
- Pointwise and fixed-fraction rank degeneration remain distinct.
- `s2 -> 0` is not automatically called Rank 1; simultaneous `s1 -> 0` gives Rank 0.
- Amplitude/nodal failure remains explicit.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
