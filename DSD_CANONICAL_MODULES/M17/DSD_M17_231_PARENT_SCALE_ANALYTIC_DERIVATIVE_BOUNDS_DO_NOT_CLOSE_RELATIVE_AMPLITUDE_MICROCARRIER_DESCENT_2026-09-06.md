# DSD M17-231 — Parent-scale analytic derivative bounds do not close relative-amplitude microcarrier descent

Date: 2026-09-06  
Canonical ID: **M17-231**

Status: **ANALYTICITY-SCOPE AUDIT / M5-392 REMOVES PARENT-SCALE POINTWISE VORTICITY-DERIVATIVE BLOWUP BY GIVING UNIFORM GLOBAL BOUNDS FOR EVERY FIXED NORMALIZED DERIVATIVE ON EACH FIRST-HITTING STAGE. IF THOSE FIXED-ORDER BOUNDS ARE INHERITED BY THE M17 REMOTE PACKET REPRESENTATION, THEY DO NOT TERMINATE THE M17-229 SCALE LADDER. A PACKET OF RADIUS `O(ell)` WITH `||Delta W||_infinity<=C_2` HAS RAW `H2` MASS AT MOST `C ell^3`; SINCE THE INTRINSIC DEFINITION IS `ell^4=M/H`, ITS `L2` MASS MAY BE AS SMALL AS `O(ell^7)`. THE PALINSTROPHY IS SIMILARLY COMPATIBLE WITH THE FIXED `C_1` DERIVATIVE CEILING. THUS THE MICROCarrier ESCAPE IS NOT A POINTWISE DERIVATIVE EXPLOSION; IT IS A RELATIVE-AMPLITUDE / OCCUPANCY DEGENERATION IN WHICH THE ACTIVE MASS VANISHES FASTER THAN THE SCALE. IF THE M17 SATELLITE REPRESENTATION DOES NOT INHERIT THE PARENT SCALE DIRECTLY, M5-392 CANNOT BE APPLIED WITHOUT AN EXPLICIT SCALE MAP. IN NEITHER CASE DOES ANALYTICITY SUPPLY THE SCALE-RETURN GATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-392

On the original first-hitting parent normalization,

\[
y=\frac{x-X_j}{r_j},
\qquad
\Omega_j=\frac{\omega}{W_j},
\]

M5-392 gives, for every fixed derivative order `m`,

\[
\boxed{
\sup_j\sup_{t\in[t_j,t_{j+1})}
\|\nabla_y^m\Omega_j\|_\infty
\le C_m<\infty.
}
\]

In particular,

\[
\|\nabla\Omega_j\|_\infty\le C_1,
\qquad
\|\Delta\Omega_j\|_\infty\le C_2.
\]

M5-392 explicitly warns that a later satellite/similarity representation must be scale-audited before these bounds are transferred.

---

## 2. Case A — the fixed-order bounds are inherited by the M17 packet

Assume the M17 packet field `W` is being read in a representation for which the inherited fixed-order bounds give

\[
\boxed{
\|\nabla W\|_\infty\le C_1,
\qquad
\|\Delta W\|_\infty\le C_2.
}
\]

Let a microcarrier packet be supported in a region of diameter

\[
O(\ell),
\qquad
\ell\to0.
\]

Its volume is

\[
O(\ell^3).
\]

Therefore its raw Laplacian mass satisfies

\[
\boxed{
H
:=\int|\Delta W|^2dy
\le C\,C_2^2\ell^3.
}
\]

---

## 3. Intrinsic relation permits even faster mass decay

By definition of the intrinsic spectral scale,

\[
\boxed{
\ell^4=\frac{M}{H},
}
\]

or equivalently

\[
\boxed{M=\ell^4H.}
\]

Using the absolute `H2` upper bound from Section 2,

\[
M
\le
C C_2^2\ell^7.
\]

Thus

\[
\boxed{
M=O(\ell^7)
}
\]

is fully compatible with a uniformly bounded pointwise Laplacian.

There is no contradiction as `ell->0` because the carrier amplitude/mass can vanish even faster.

---

## 4. Palinstrophy is also compatible

The fixed first-derivative ceiling gives

\[
\boxed{
P
:=\int|\nabla W|^2dy
\le C C_1^2\ell^3.
}
\]

The mean-zero Poincare lower bound for a fluctuation of mass `M` is only

\[
P
\gtrsim
\frac{M}{\ell^2}.
\]

With

\[
M\lesssim\ell^7,
\]

this lower floor is

\[
\boxed{
P\gtrsim O(\ell^5),
}
\]

which is entirely compatible with the upper bound `O(ell^3)`.

Hence the analytic derivative ceilings do not force a mismatch.

---

## 5. Correct interpretation of the surviving branch

Under inherited parent-scale analyticity, the M17 microcarrier branch cannot be described as

\[
\text{pointwise derivative blowup}.
\]

Instead it has the form

\[
\boxed{
\text{bounded absolute derivatives}
+\text{rapidly vanishing carrier mass}
+\text{divergent derivative-to-mass ratio}.
}
\]

That is a **relative-amplitude concentration** or **occupancy degeneration**.

This agrees with the M5-392 warning that the remaining remote H frontier is a relative-scale/mass phenomenon rather than a parent-scale derivative singularity.

---

## 6. Case B — the M17 representation is not parent-scale equivalent

If the M17 remote/satellite field has undergone an additional amplitude, spatial, or time normalization so that the M5-392 parent derivative bounds do not transfer unchanged, then one must write the explicit scale map

\[
(x,t,\omega)
\longleftrightarrow
(y,\theta,W)
\]

before importing any `C_m` estimate.

Without that map,

\[
\boxed{
\text{M5-392 cannot be used to close the M17 satellite branch.}
}
\]

The failure to inherit a bound is not itself a contradiction; it is a representation/scale-audit obligation.

---

## 7. Consequence for the Scale-Return Gate

In either case, stage-wide analyticity does not provide SRG.

### If inherited

It allows the mass law

\[
M\lesssim\ell^7,
\]

which makes lower-order costs smaller, not larger.

### If not inherited

The estimate cannot be invoked until the scale map is supplied.

Therefore

\[
\boxed{
\text{parent-scale analyticity}
\not\Rightarrow
\text{microcarrier scale return}.
}
\]

---

## 8. Stronger statement that would actually help

A useful SRG input would require a **relative-amplitude lower bound**, for example

\[
\boxed{
M\ge c\ell^\alpha
}
\]

with an exponent/constant strong enough that the induced lower-order action cannot be geometrically summable across scale depth.

Alternatively one could seek

\[
\boxed{
\frac{\ell^m\|\nabla^mW\|}{\|W\|_{local}}
\le C_m
}
\]

for an amplitude-normalized local norm.

M5-392 supplies absolute normalized derivative bounds, not this relative-amplitude estimate.

M17-155 obtained such amplitude-normalized compactness only on the bounded-`kappa`, relative-thick branch; the present spectral microcarrier branch is precisely outside that corridor.

---

## 9. Updated microcarrier frontier

The residual scale ladder may therefore be sharpened to

\[
\boxed{
G_{microcarrier\ ladder}
=
G_{relative\text{-}amplitude\ degeneration}
\lor
G_{representation\ scale\ mismatch}
\lor
H_{palinstrophy/nodal/coefficient\ return}.
}
\]

On the canonical inherited smooth-hull reading, the first label is the main survivor.

---

## 10. DSD audit

- M5-392 is respected in its parent-scale scope.
- No pointwise derivative infinity is reintroduced.
- Absolute derivative bounds are not confused with derivative-to-amplitude bounds.
- The mass estimate `M<=C ell^7` is an upper compatibility estimate, not a lower occupancy theorem.
- Representation changes must be mapped explicitly before importing analytic constants.
- The SRG remains unproved.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
