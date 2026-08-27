# DSD M5-163 — Analytic Off-Diagonal First-Order Transfer Bound

Date: 2026-08-27

Status: **M5-161 LEMMA B CLOSED / UNIFORM W1 TIME ANALYTICITY PLUS UNIFORM SCALED-SHELL SPATIAL ANALYTICITY GIVE FACTORIAL ITERATED COMMUTATOR BOUNDS FOR THE VARIABLE RELATIVE TRANSPORT/STRETCHING COEFFICIENTS; SPECTRAL SEPARATION THEN YIELDS EXPONENTIAL OFF-DIAGONAL DECAY, AND THE DIFFERENTIAL ORDER OF THE RELATIVE COUPLING CONTRIBUTES ONLY ONE INPUT-SHELL FACTOR `1+j`: `||Q_k N Q_j|| <= C(1+j)e^{-a|k-j|}` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input analytic scales

Use the statistical same-tail pair Hilbert space

\[
\mathscr H=L^2(\rho;L^2(S^2))
\]

and cross-section frequency operator

\[
\Lambda=(1-A_s^2-\Delta_{S^2})^{1/2}.
\]

M5-155 supplies a uniform positive analytic radius in the pair-flow/Leray-time direction, with derivative estimates valid after a fixed radius loss.

The previously audited W1 local/shell analyticity supplies a uniform positive analytic radius in the scaled angular/spatial directions on the unit shell.

After fixing reduced radii once and for all, the background coefficients appearing in the relative vorticity operator have factorial derivative bounds of the form

\[
\boxed{
\|\nabla_{cross}^m B\|_{\infty}
\le
M_B\,m!\,r_B^{-m}
}
\]

uniformly over the compact W1 class.

The same statement holds for the lower-order stretching and Biot--Savart coefficient tensors.

---

## 2. Relative transfer operator has order at most one

From M5-159,

\[
\mathcal N
=B^a\nabla_a+C+\mathcal S,
\]

where `S` has order zero or negative after recovering the velocity difference from vorticity.

Thus, for input restricted to shell `j`,

\[
\boxed{
\|\mathcal NQ_j f\|
\le
C_N(1+j)\|Q_jf\|
}
\]

before any off-diagonal gain is used.

There is no variable-coefficient second-order term.

---

## 3. Iterated commutator bound

For a multiplication/lower-order coefficient operator `B`, standard analytic pseudodifferential commutator bookkeeping for

\[
\Lambda=(1-A_s^2-\Delta_{S^2})^{1/2}
\]

gives

\[
\boxed{
\|\operatorname{ad}_\Lambda^m(B)\|_{\mathscr H\to\mathscr H}
\le
C_0 C_1^m m!
}
\]

for every integer `m>=0`.

Here

\[
\operatorname{ad}_\Lambda(B)
=[\Lambda,B],
\]

and the constants depend only on the fixed reduced analytic radii and the compact W1 coefficient ceilings.

The factorial growth is exactly the operator form of the uniform analytic derivative bounds.

For the first-order operator `N`, the same argument after placing the derivative on the input shell yields

\[
\boxed{
\|\operatorname{ad}_\Lambda^m(\mathcal N)Q_j\|
\le
C_0 C_1^m m!(1+j).
}
\]

---

## 4. Spectral separation identity

Let

\[
Q_j=1_{[j,j+1)}(\Lambda),
\qquad
Q_k=1_{[k,k+1)}(\Lambda).
\]

If the two shells are separated by

\[
d:=\max\{0,|j-k|-1\},
\]

then repeated use of the spectral theorem gives the standard separation estimate

\[
\boxed{
 d^m
\|Q_k\mathcal NQ_j\|
\le
\|Q_k\operatorname{ad}_\Lambda^m(\mathcal N)Q_j\|.
}
\]

Hence

\[
\|Q_k\mathcal NQ_j\|
\le
C_0(1+j)
\frac{C_1^m m!}{d^m}.
\]

---

## 5. Optimize the commutator order

For large `d`, choose

\[
m=\left\lfloor\frac{d}{eC_1}\right\rfloor.
\]

Using Stirling's bound

\[
m!\le C\sqrt m\,(m/e)^m,
\]

we obtain

\[
\frac{C_1^m m!}{d^m}
\le
C'e^{-a d}
\]

for some uniform `a>0`.

The finitely many small-separation cases are absorbed into the constant.

Therefore

\[
\boxed{
\|Q_k\mathcal NQ_j\|_{\mathscr H\to\mathscr H}
\le
C_{tr}(1+j)e^{-a|k-j|}.
}
\]

This is M5-161 Lemma B.

---

## 6. Interpretation

The estimate has two independent pieces:

\[
\boxed{
1+j
}
\]

is the differential-order cost of the first-order relative transport/stretching operator, while

\[
\boxed{
e^{-a|k-j|}
}

is the analytic suppression of a long spectral jump.

Thus direct excitation of a very distant frequency is allowed but exponentially tiny, and repeated neighboring transfer carries only one power of spectral level per step.

No hidden `j^2` transfer factor is present.

---

## 7. Biot--Savart audit

The velocity-difference terms do not spoil the order count.

Relative velocity is recovered from relative vorticity by an order `-1` operator.

Hence

\[
(Z\cdot\nabla)\Omega_V
\]

and

\[
(\Omega_V\cdot\nabla)Z
\]

are respectively order `-1` plus a fixed background derivative and order `0` in the relative vorticity.

They therefore satisfy the same or better off-diagonal estimate and cannot create a second-order transfer channel.

---

## 8. DSD audit

### Formation — GREEN

The operator coefficients come from the actual two W1 backgrounds in the same-tail relation.

### Axis — GREEN

Analyticity along the pair-flow axis and angular/spatial analyticity are used only to control cross-section spectral separation.

### Static aggregation — GREEN

The input-shell derivative factor and off-diagonal coefficient decay are kept separate; they are not multiplied into a fictitious second-order transfer cost.

### Dynamics — GREEN

The estimate is instantaneous in normal depth and does not assume recurrence beyond the invariant measure already defining Branch S.

### Cross-audit — GREEN

M5-152 remains respected because all derivative estimates are obtained after fixed analytic-radius loss, not by same-norm compactness.

---

## 9. M5-161 update

Both packaging lemmas are now GREEN:

\[
\boxed{
\text{Lemma A: stable principal shell time }\Delta z_j\sim j^{-2}
}
\]

and

\[
\boxed{
\text{Lemma B: transfer }\|Q_k\mathcal NQ_j\|
\le C(1+j)e^{-a|k-j|}.
}
\]

The next calculation is the full path summation / non-explosion closure: sum all possible adjacent and long-jump transfer histories and determine whether any nonzero spectral mass can enter from `Lambda=infinity` while every finite shell has zero flat boundary data.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
