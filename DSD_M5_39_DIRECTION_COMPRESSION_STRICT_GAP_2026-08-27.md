# DSD M5-39 — Direction Compression Supplies the Strict Pressure-Tail Gap

Date: 2026-08-27

Status: **DERIVED W1-SPECIFIC REFINEMENT / THE ADDITIVE PRESSURE-TAIL MARGIN AT A POSITIVE FIRST HIT CAN BE CHARGED DIRECTLY TO THE NONDEGENERATE DIRECTION-COMPRESSION FLOOR / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the first-hit formation audit

M5-23 proves that a fixed positive high-amplitude defect first hit requires

\[
\boxed{
\|\mathbf1_{a>1}\operatorname{div}n\|_{L^2}
\ge d_*>0,
}
\]

where

\[
a=|V|,
\qquad n=V/a.
\]

This is the gauge-free direction-compression source required by the threshold pressure work.

## 2. Nonsmooth threshold dissipation sees direction without collar degeneracy

For the nonsmooth entropy

\[
\Phi_*(a)=\frac12(a^2-1)_+,
\]

M5-31 gives the active bulk viscous term

\[
A
=
\int_{a>1}|\nabla V|^2dz.
\]

Decompose

\[
|\nabla V|^2
=|\nabla a|^2+a^2|\nabla n|^2.
\]

Define

\[
A_n^*
:=
\int_{a>1}a^2|\nabla n|^2dz.
\]

Since `a>1` and `|div n|<=C|grad n|` pointwise up to the fixed dimensional tensor constant,

\[
\boxed{
A_n^*
\ge c\n\|\mathbf1_{a>1}\operatorname{div}n\|_2^2
\ge c d_*^2.
}
\]

Absorb the dimensional constant into the floor and write

\[
\boxed{A_n^*\ge d_n^*>0.}
\]

Unlike the smooth quadratic direction term `a(a-1)|grad n|^2`, this floor does not vanish as `a downarrow 1`.

## 3. Insert the direction floor into the M5-37 estimate

M5-37 gives

\[
\lambda[-Q_P'(\lambda)]
\ge
\nu^2D_\lambda^{surf}
+
\nu^2A(\lambda)
\]

at a fixed positive first hit.

Since

\[
A(\lambda)
\ge
A_n^*(\lambda),
\]

we obtain

\[
\boxed{
\lambda[-Q_P'(\lambda)]
\ge
\nu^2D_\lambda^{surf}
+
\nu^2d_n^*.
}
\]

Thus the strict additive pressure-tail margin may be charged directly to the mandatory direction-compression content.

## 4. DSD interpretation

The formation chain is now typed as

\[
\boxed{
\text{positive defect first hit}
\Longrightarrow
\text{direction compression}
\Longrightarrow
\text{nondegenerate direction dissipation}
\Longrightarrow
\text{strict pressure-tail overpay}.
}
\]

The first and last objects are not independent payers. They are input and output constraints in the same threshold formation cell.

The significance of the nonsmooth entropy is that it prevents the direction floor from hiding in the smooth threshold collar.

## 5. What remains

The pressure-tail density is scale critical. Hence a fixed additive normalized margin at infinitely many nested thresholds does not contradict the ordinary finite-energy/dissipation budget.

A closing theorem must provide a finite or subcritical spacetime budget for the strict pressure-tail margin, or prove that the pressure-Poisson geometry cannot realize the required margin at arbitrarily large physical thresholds.

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
