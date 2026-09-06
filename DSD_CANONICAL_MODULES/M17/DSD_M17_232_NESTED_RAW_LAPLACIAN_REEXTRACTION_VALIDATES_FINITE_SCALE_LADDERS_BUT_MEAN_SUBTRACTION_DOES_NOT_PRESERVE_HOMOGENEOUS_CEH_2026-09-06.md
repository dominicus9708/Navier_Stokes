# DSD M17-232 — Nested raw-Laplacian re-extraction validates finite scale ladders, but mean subtraction does not preserve homogeneous CE-H

Date: 2026-09-06  
Canonical ID: **M17-232**

Status: **MICROCARRIER RE-EXTRACTION / SCOPE CORRECTION. M17-228 PRODUCES A SMALLER NUMERICAL FLUCTUATION SCALE `ell_fluc=(V/H)^(1/4)`, BUT A FINITE SCALE LADDER REQUIRES AN ACTUAL SMALLER PHYSICAL BUFFER AT EACH LEVEL. THE M17-224 RAW-NUMERATOR / BUFFERED-DENOMINATOR ARGUMENT CAN BE ITERATED ON THE MEAN-ZERO FLUCTUATION: PARTITION THE RETAINED RAW `|Delta W|^2` CORE AT THE NEW FLUCTUATION SCALE, USE BUFFER DENOMINATORS BUILT FROM THE FLUCTUATION `L2` MASS, AND PIGEONHOLE A NESTED BUFFER WITH THE SAME HIGH RATIO. THIS VALIDATES THE SPATIAL FINITE SCALE LADDER AFTER FIXED GEOMETRIC CONSTANTS ARE INCLUDED. HOWEVER, AFTER SUBTRACTING A MEAN `c`, THE NEW FIELD `w=W-c` SATISFIES `Delta w=kappa(w+c)`, NOT `Delta w=kappa w`. THUS THE NESTED LADDER IS A DERIVATIVE/CONCENTRATION LADDER, NOT A LADDER OF NEW HOMOGENEOUS CE-H SOLUTIONS. ANY FUTURE COEFFICIENT, DOUBLING, OR UNIQUE-CONTINUATION ARGUMENT MUST BE APPLIED TO THE ORIGINAL `W`, OR MUST RETAIN THE INHOMOGENEOUS SOURCE `kappa c` EXPLICITLY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One-level input

Let `B_n` be a physical buffer with an inner raw-Laplacian core `K_n subset B_n` and a fixed relative margin between `K_n` and `partial B_n`.

Let the current physical field be written on `B_n` as

\[
F_n=W-C_n,
\]

where `C_n` is spatially constant. Therefore

\[
\nabla F_n=\nabla W,
\qquad
\Delta F_n=\Delta W.
\]

Set

\[
M_n:=\int_{B_n}|F_n|^2dy,
\qquad
H_n:=\int_{K_n}|\Delta W|^2dy,
\]

and define

\[
\boxed{\ell_n:=\left(\frac{M_n}{H_n}\right)^{1/4}.}
\]

Assume the buffer geometry has been chosen in the M17-224 form

\[
\operatorname{diam}(B_n)\asymp A\ell_n
\]

for one fixed sufficiently large `A`.

---

## 2. Mean/fluctuation split at level n

Let

\[
c_n:=\frac1{|B_n|}\int_{B_n}F_ndy,
\qquad
g_n:=F_n-c_n.
\]

Then

\[
\int_{B_n}g_ndy=0,
\]

and

\[
\nabla g_n=\nabla W,
\qquad
\Delta g_n=\Delta W.
\]

Let

\[
V_n:=\int_{B_n}|g_n|^2dy.
\]

On the M17-228 mean-dominated branch,

\[
\boxed{V_n<\theta M_n}
\]

for a fixed `0<theta<1`.

Define the fluctuation numerical scale

\[
\boxed{
\widetilde\ell_n:=\left(\frac{V_n}{H_n}\right)^{1/4}
<\theta^{1/4}\ell_n.
}
\]

This number alone is not yet an extracted physical carrier.

---

## 3. Cover the raw core at the fluctuation scale

Cover `K_n` by smooth core weights `chi_m` of diameter

\[
O(A\widetilde\ell_n)
\]

with

\[
\sum_m\chi_m^2=1
\quad\text{on }K_n
\]

and uniformly finite overlap.

Because

\[
\widetilde\ell_n<\theta^{1/4}\ell_n,
\]

a fixed sufficiently small `theta` and the fixed core-buffer margin ensure that each core cell has a fixed-factor buffer `zeta_m` supported inside `B_n`.

Choose

\[
zeta_m\equiv1
\]

on a neighborhood of `supp chi_m`, again with uniformly finite overlap.

Define raw numerator pieces

\[
\boxed{
h_m:=\int_{K_n}\chi_m^2|\Delta W|^2dy
}
\]

and fluctuation buffer denominators

\[
\boxed{
e_m:=\int_{B_n}\zeta_m^2|g_n|^2dy.
}
\]

Then

\[
\sum_mh_m=H_n
\]

and finite overlap gives

\[
\sum_me_m\le C_BV_n.
\]

---

## 4. Nested buffered pigeonhole

If every active cell obeyed

\[
h_m<c\frac{H_n}{V_n}e_m
\]

with `c<C_B^-1`, summation would give

\[
H_n<cC_BH_n<H_n,
\]

a contradiction.

Hence there exists one selected child cell `m_n` satisfying

\[
\boxed{
\frac{h_{m_n}}{e_{m_n}}
\ge c_B\frac{H_n}{V_n}.
}
\]

Let its buffer be

\[
B_{n+1}:=\operatorname{supp}\zeta_{m_n}
\]

and define

\[
F_{n+1}:=g_n
=W-(C_n+c_n)
\quad\text{on }B_{n+1}.
\]

Set

\[
M_{n+1}:=e_{m_n},
\qquad
H_{n+1}:=h_{m_n}.
\]

Then

\[
M_{n+1}\le V_n<\theta M_n
\]

and

\[
\frac{H_{n+1}}{M_{n+1}}
\ge c_B\frac{H_n}{V_n}.
\]

Therefore

\[
\boxed{
\ell_{n+1}:=\left(\frac{M_{n+1}}{H_{n+1}}\right)^{1/4}
\le c_B^{-1/4}\widetilde\ell_n
<\left(\frac{\theta}{c_B}\right)^{1/4}\ell_n.
}
\]

Choose the fixed threshold so that

\[
\theta<c_B.
\]

Then the physical scale contracts by one fixed factor

\[
\boxed{
\ell_{n+1}\le q_*\ell_n,
\qquad0<q_*<1.
}
\]

This is the missing nested re-extraction theorem required by M17-229.

---

## 5. The raw derivative lower bound is never created by a cutoff

The child numerator is

\[
H_{n+1}
=\int_{K_n}\chi_{m_n}^2|\Delta W|^2dy.
\]

It is sampled from the original physical field before differentiating the child buffer cutoff.

Moreover on every descendant fluctuation

\[
F_n=W-C_n
\]

with `C_n` constant, so

\[
\boxed{
\Delta F_n=\Delta W
}
\]

exactly.

Thus every finite ladder level is a genuine nested raw-Laplacian concentration witness.

---

## 6. Homogeneous CE-H is not inherited by the fluctuation

The original field satisfies the CE-H elliptic relation

\[
\boxed{
\Delta W=\kappa W.
}
\]

For

\[
F_n=W-C_n,
\]

one instead has

\[
\boxed{
\Delta F_n
=\kappa(F_n+C_n)
=\kappa F_n+\kappa C_n.
}
\]

Unless

\[
C_n=0
\]

or the source is otherwise eliminated,

\[
\boxed{
\Delta F_n\neq\kappa F_n.
}
\]

Therefore a descendant fluctuation is not another homogeneous CE-H solution.

This distinction is essential.

---

## 7. Consequence for coefficient and unique-continuation arguments

The finite spatial ladder is valid because it uses only

\[
\nabla(W-C_n)=\nabla W,
\qquad
\Delta(W-C_n)=\Delta W
\]

and raw density pigeonholing.

However a theorem whose hypothesis is

\[
\Delta f=\kappa f
\]

cannot be reapplied to `F_n` without retaining the forcing term

\[
\kappa C_n.
\]

Hence future arguments must take one of two valid forms:

1. apply coefficient/doubling/unique-continuation estimates directly to the original `W` on the descendant buffer; or
2. work with the inhomogeneous descendant equation
   \[
   \Delta F_n-\kappa F_n=\kappa C_n
   \]
   and estimate the source explicitly.

Silently replacing it by the homogeneous equation is forbidden.

---

## 8. Corrected finite scale ladder

M17-229's ladder can now be made fully physical:

\[
\boxed{
B_0\supset B_1\supset\cdots\supset B_N,
}
\]

with

\[
\boxed{
\ell_{n+1}\le q_*\ell_n,
\qquad
M_{n+1}<\theta M_n,
}
\]

at every mean-dominated step and each `B_n` carrying an inner raw `|Delta W|^2` core.

The ladder consists of nested concentration witnesses of the same physical `W`, after subtraction of different constants.

It is **not** a sequence of independent CE-H solutions.

---

## 9. DSD analysis

### 9.1 Missing existence step repaired

A numerical spectral scale is not automatically a spatial object.
The raw-core / buffered-denominator re-extraction proves the existence of the physical child object.

### 9.2 Object identity preserved

All descendants refer to the same physical `W`.
Subtracting constants is a localization device for derivative concentration, not a new vorticity state.

### 9.3 Equation inheritance firewall

Derivative invariance under constants does not imply PDE invariance under constants.

This prevents the finite scale ladder from being used as an unsupported chain of homogeneous elliptic problems.

---

## 10. Updated SRG target

The Scale-Return Gate remains the correct next target, but it must be formulated on the original `W` restricted to nested buffers:

\[
\boxed{
\text{nested relative-amplitude descent of }W
\Longrightarrow
H_{lower-order}
\lor G_{coefficient/nodal/interface}.
}
\]

The most natural next test is to use

\[
\Delta W=\kappa W
\]

on a mean-dominated parent buffer while keeping the mean/fluctuation decomposition only as a geometric occupancy tool.

---

## 11. DSD audit

- The M17-228 numerical scale now has an explicit nested physical re-extraction theorem.
- The scale contraction includes fixed geometric constants; `theta` is chosen small enough that the net factor is `<1`.
- Every numerator remains raw `|Delta W|^2` from the original field.
- Mean subtraction preserves first and second spatial derivatives but not homogeneous CE-H.
- No coefficient/doubling theorem is applied to a descendant fluctuation as if it were `W`.
- Finite scale ladders remain valid; infinite completion remains unformed.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
