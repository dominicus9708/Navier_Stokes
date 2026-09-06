# DSD M17-247 — Quiet strain-cancelled scale-comparable cells cannot carry a fixed fraction of the nonsummable shell spectral charge

Date: 2026-09-06  
Canonical ID: **M17-247**

Status: **SHELL-LEVEL AGGREGATION / M17-224'S RAW-NUMERATOR BUFFER PARTITION MAY BE KEPT AS A FAMILY INSTEAD OF PIGEONHOLING ONLY ONE CELL. CELLS WHOSE LOCAL `H2/L2` RATIO IS COMPARABLE TO THE PARENT SHELL RATIO CARRY EITHER A FIXED FRACTION OF THE SHELL `H2` CHARGE OR ELSE A FIXED FRACTION ALREADY LIES IN STRICTLY HIGHER-RATIO SUBSCALE CELLS. ON THE SCALE-COMPARABLE FAMILY, M17-244 SHOWS THAT EVERY QUIET ORDER-ONE STRAIN-CANCELLATION CELL REQUIRES `ell<=C/R` AND AT LEAST `c ell` OF SPACETIME STRAIN-SQUARED ACTION. FINITE OVERLAP PLUS THE QUIET SHELL BUDGET `C/R` BOUNDS THE NUMBER OF SUCH CELLS BY `C/(R ell)`. A UNIFORM COMPACT-HULL `|Delta W|` CEILING THEN BOUNDS THEIR TOTAL RAW `H2` CHARGE BY `C ell^2/R`, HENCE BY `C/R^3`. IF THEY CARRIED A FIXED FRACTION OF THE PARENT SPECTRAL CHARGE, THE PARENT CRITICAL COST `b=RE` WOULD DECAY AT LEAST LIKE `R^-6`, CONTRADICTING NONSUMMABILITY OF `sum b^(3/2)` ON THAT SUBFAMILY. THUS QUIET STRAIN CANCELLATION CANNOT BE THE DOMINANT SCALE-COMPARABLE SPECTRAL PAYER; DOMINANT CHARGE MUST MOVE TO STRICT SUBSCALE DESCENT OR ANOTHER ARG EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parent shell quantities

Let a globally tempered remote shell have

\[
E_R:=\int_{C_R}|W|^2dy,
\qquad
H_R:=\int_{C_R}|\Delta W|^2dy,
\]

with

\[
\Lambda_R^2:=\frac{H_R}{E_R}\to\infty.
\]

Define the shell intrinsic scale

\[
\boxed{
\ell_R:=\left(\frac{E_R}{H_R}\right)^{1/4}
=\Lambda_R^{-1/2}.
}
\]

The scale-critical shell mass is

\[
\boxed{b_R:=R E_R.}
\]

On the M17-207 selected family,

\[
\sum b_R^{3/2}=\infty.
\]

---

## 2. Keep the entire raw M17-224 cell family

Partition the shell raw numerator at spatial scale \(A\ell_R\) exactly as in M17-224.

For each cell \(i\), let

\[
h_i:=\int_{C_R}\chi_i^2|\Delta W|^2dy
\]

and let

\[
e_i:=\|\zeta_iW\|_2^2
\]

be the buffered denominator.

Then

\[
\boxed{
\sum_i h_i=H_R,
\qquad
\sum_i e_i\le C_B E_R.
}
\]

---

## 3. Spectral-good cells carry a fixed H2 fraction

Fix

\[
\alpha:=\frac1{4C_B}.
\]

Call a cell spectral-good if

\[
\frac{h_i}{e_i}
\ge
\alpha\frac{H_R}{E_R}
=\alpha\Lambda_R^2.
\]

The bad cells satisfy

\[
\sum_{bad}h_i
<
\alpha\Lambda_R^2\sum_i e_i
\le
\frac14H_R.
\]

Hence

\[
\boxed{
\sum_{good}h_i\ge\frac34H_R.
}
\]

Thus most raw Laplacian charge lies in cells whose local spectral ratio is at least a fixed fraction of the shell ratio.

---

## 4. Scale-comparable versus strict-subscale cells

Fix a large constant \(Q>1\).

Split the good cells into

\[
G_{comp}
:=
\left\{i:
\alpha\Lambda_R^2
\le\frac{h_i}{e_i}
\le Q\Lambda_R^2
\right\}
\]

and

\[
G_{sub}
:=
\left\{i:
\frac{h_i}{e_i}>Q\Lambda_R^2
\right\}.
\]

If

\[
\sum_{i\in G_{sub}}h_i\ge\frac14H_R,
\]

then a fixed fraction of the shell raw spectral charge has already entered a strictly shorter local intrinsic scale. Retain this as

\[
\boxed{G_{strict\ subscale\ spectral}.}
\]

Otherwise

\[
\boxed{
\sum_{i\in G_{comp}}h_i\ge\frac12H_R.
}
\]

For every scale-comparable cell,

\[
\ell_i
:=\left(\frac{e_i}{h_i}\right)^{1/4}
\asymp\ell_R.
\]

---

## 5. Assume quiet strain cancellation carries a fixed fraction of the comparable charge

Let \(S_R\subset G_{comp}\) be the cells entering the M17-239 strain-cancellation branch.

Suppose for contradiction that

\[
\boxed{
\sum_{i\in S_R}h_i
\ge\eta H_R
}
\]

for a fixed \(\eta>0\) along a remote shell subfamily.

Because \(\ell_i\asymp\ell_R\), M17-244 applies at the common scale up to fixed constants.

Every strain-cancelled cell requires

\[
\boxed{
\int_{Q_i}|\Sigma|^2dyd\tau
\ge c\ell_R
}
\]

on its parabolic packet corridor \(Q_i\), and on the quiet shell

\[
\boxed{
\ell_R\le\frac{C}{R}.
}
\]

---

## 6. Finite overlap bounds the number of strain-cancelled cells

The spatial cell family has fixed finite overlap, and over the \(O(\ell_R^2)\) interval a bounded-deformation corridor preserves overlap up to another fixed factor. Failure is a deformation/nonquiet exit.

If \(N_S:=|S_R|\), summing the cell lower bounds gives

\[
N_S c\ell_R
\le
C
\int_{-T}^{T}
\int_{C_R^*}|\Sigma|^2dy\,d\tau.
\]

M17-155 gives

\[
\int_{-T}^{T}
\int_{C_R^*}|\Sigma|^2dy\,d\tau
\le\frac{C_T}{R}.
\]

Therefore

\[
\boxed{
N_S
\le
\frac{C}{R\ell_R}.
}
\]

---

## 7. Uniform C2 ceiling bounds raw H2 per cell

On the retained smooth compact CE-H hull, fixed-order compactness gives a uniform second-derivative pointwise ceiling. Write

\[
\boxed{\|\Delta W\|_\infty\le C_2.}
\]

If this ceiling is not available in a different representation, retain a pointwise derivative-amplitude exit instead of importing it.

Each cell has volume \(O(\ell_R^3)\), so

\[
\boxed{h_i\le C C_2^2\ell_R^3.}
\]

Hence

\[
\begin{aligned}
\sum_{i\in S_R}h_i
&\le
C N_S\ell_R^3\\
&\le
C\frac{\ell_R^2}{R}.
\end{aligned}
\]

Using \(\ell_R\le C/R\),

\[
\boxed{
\sum_{i\in S_R}h_i
\le\frac{C}{R^3}.
}
\]

---

## 8. Fixed-fraction dominance would force summable critical shell mass

If

\[
\sum_{i\in S_R}h_i\ge\eta H_R,
\]

then

\[
\boxed{H_R\le\frac{C}{R^3}.}
\]

Since

\[
E_R=H_R\ell_R^4
\]

and

\[
\ell_R\le\frac{C}{R},
\]

we obtain

\[
\boxed{
E_R\le\frac{C}{R^7}.
}
\]

Therefore

\[
\boxed{
b_R=R E_R\le\frac{C}{R^6}.}
\]

On dyadic radii,

\[
\sum_R b_R^{3/2}
\le
C\sum_R R^{-9}
<\infty.
\]

This contradicts the M17-207 nonsummable cubic packing if the strain-dominant subfamily were responsible for a nonsummable portion of that packing.

---

## 9. Shell-level strain conclusion

Thus on the globally tempered nonsummable spectral branch,

\[
\boxed{
\text{quiet strain-cancelled scale-comparable cells}
}
\]

cannot carry a fixed fraction of the shell raw \(H^2\) charge throughout the nonsummable subfamily.

The shell must instead route a fixed spectral fraction through at least one of

\[
\boxed{
G_{strict\ subscale\ spectral}
\lor
H_{kappa\ turnover/reformation}
\lor
H_{relative\ variance/palinstrophy}
\lor
G_{interface/deformation/nonquiet}
\lor
G_{pointwise\ derivative\ ceiling\ failure}.
}
\]

---

## 10. DSD audit

- The proof keeps the full M17-224 cell family instead of promoting one selected cell to the whole shell.
- A fixed H2 fraction on higher-ratio cells is retained as strict subscale descent rather than ignored.
- Scale comparability is imposed explicitly before using one common `ell_R`.
- Spacetime finite overlap is conditional on bounded deformation; failure remains an exit.
- The uniform `Delta W` ceiling is imported only on the retained compact smooth CE-H representation.
- The argument excludes dominant quiet strain cancellation; it does not close the other ARG branches.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
