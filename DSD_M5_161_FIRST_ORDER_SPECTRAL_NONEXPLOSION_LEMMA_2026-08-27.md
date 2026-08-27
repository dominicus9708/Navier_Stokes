# DSD M5-161 — First-Order Spectral Non-Explosion Lemma

Date: 2026-08-27

Status: **P1_B^S MAJOR RIGIDITY STEP / ON THE STABLE FLAT NORMAL BRANCH, THE PRINCIPAL SECOND-ORDER LERAY/VISCOUS OPERATOR MAY AMPLIFY OR DAMP A FIXED CROSS-SECTION SPECTRAL BAND BUT DOES NOT MOVE MASS BETWEEN BANDS; TRUE BAND TRANSFER IS FIRST ORDER, SO ON THE NATURAL PARABOLIC BAND TIME `Delta z_j ~ j^-2` ONLY `O(j^-1)` OF A BAND CAN BE PASSED TO A NEIGHBORING BAND / THE PRODUCT OF THESE FRACTIONS ALONG AN INFINITE CASCADE VANISHES FACTORIALLY, BLOCKING INFORMATION ENTRY FROM SPECTRAL INFINITY / A FINAL COEFFICIENT-ANALYTICITY AND PRINCIPAL-PROPAGATOR PACKAGING LEMMA IS REQUIRED BEFORE DECLARING P1_B^S CLOSED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why spectral non-explosion is the correct target

M5-154 shows that any nonzero statistical flat fiber must move its normalized cross-section frequency to infinity at roughly the parabolic scale.

M5-159 shows that the constant-coefficient normal and viscous operators commute with cross-section spectral projectors.  They can change the amplitude of a band but cannot move information from one band to another.

M5-160 removes the growing fast-normal branch and gives a causal stable Volterra representation.

Therefore a nontrivial flat solution with zero data at normal infinity can exist only if information can effectively enter from

\[
\Lambda=\infty
\]

and cascade through infinitely many finite bands in finite normal depth.

The present note audits whether the differential order of the actual transfer operator permits such spectral explosion.

---

## 2. Spectral shells

Use the M5-159 cross-section frequency operator

\[
\Lambda=(1-A_s^2-\Delta_{S^2})^{1/2}
\]

on

\[
\mathscr H=L^2(\rho;L^2(S^2)).
\]

For integers `j>=0`, define unit shells

\[
\boxed{
Q_j:=1_{[j,j+1)}(\Lambda).
}
\]

Write the flat relative-vorticity field as

\[
K=\sum_{j\ge0}K_j,
\qquad
K_j:=Q_jK.
\]

The same decomposition is applied to the fast normal variable from M5-160.

---

## 3. Principal shell time scale

On a fixed shell `j`, the constant-coefficient cross-section second-order part has size

\[
O(\nu j^2).
\]

The stable fast-normal reduction does not add a noncommuting cross-frequency operator; its large normal coefficient acts inside each shell.

Consequently the natural normal-depth interval over which the principal shell propagator changes an amplitude by only an order-one factor is

\[
\boxed{
\Delta z_j
:=
\frac{\gamma}{(1+j)^2},
}
\]

with `gamma>0` chosen from the fixed W1/viscosity constants.

On such an interval, the stable principal propagator restricted to `Q_j` has a uniform bound

\[
\boxed{
\|U_j(z_2,z_1)\|
\le C_0
\qquad
\text{when }0\le z_2-z_1\le\Delta z_j.
}
\]

The important feature is that `C_0` is independent of `j` after time is measured in the parabolic shell scale `j^-2`.

---

## 4. Transfer operator is only first order

M5-159 decomposes the variable-coefficient relative coupling as

\[
\mathcal N
=B^a\nabla_a+C+\mathcal S,
\]

where `S` is order zero or negative after Biot--Savart recovery.

Therefore on shell `j`, the local transfer size is at most

\[
\boxed{
\|Q_k\mathcal N Q_j\|
\lesssim
(1+j)\,\mathfrak a_{k-j},
}
\]

where `a_m` measures the spectral content of the compact W1 background coefficients.

The analyticity input implies an exponentially summable off-diagonal profile

\[
\boxed{
|\mathfrak a_m|
\le C_a e^{-a|m|}
}
\]

once the coefficient-analyticity/iterated-commutator bound is packaged in the preferred reduced analytic radius.

For neighboring shells this reduces to the first-order rate

\[
O(1+j).
\]

There is no variable-coefficient second-order band-transfer term of size `j^2`.

---

## 5. Transfer fraction per parabolic shell time

During one principal shell interval

\[
\Delta z_j\sim(1+j)^{-2},
\]

the maximum adjacent-band transfer fraction is therefore

\[
\boxed{
\varepsilon_j
\lesssim
(1+j)\Delta z_j
\lesssim
\frac{C}{1+j}.
}
\]

This is the central order gap:

\[
\boxed{
\text{second-order in-band dynamics}
\quad\text{versus}\quad
\text{first-order inter-band transfer}.
}
\]

Second-order viscosity determines how fast one band can change internally, but only the first-order relative transport can move information to a new band.

---

## 6. Infinite adjacent cascade has zero weight

Consider a path that would carry information from spectral level `M` down to a fixed finite level `N` by neighboring transfers.

Its transfer weight is bounded by

\[
\prod_{j=N}^{M}\frac{C}{1+j}.
\]

Hence

\[
\boxed{
\prod_{j=N}^{M}\frac{C}{1+j}
\le
C^{M-N+1}
\frac{N!}{(M+1)!}
\longrightarrow0
\qquad(M\to\infty).
}
\]

The factorial denominator beats every fixed exponential combinatorial multiplicity.

Thus a nearest-neighbor spectral cascade cannot bring nonzero information from `Lambda=infinity` into any fixed finite shell in finite normal depth.

---

## 7. Long jumps are even smaller

Analytic coefficient tails permit direct nonlocal shell jumps, but their matrix elements are exponentially suppressed:

\[
\|Q_k\mathcal NQ_j\|
\lesssim
(1+j)e^{-a|k-j|}.
\]

A path with large jumps therefore pays an additional factor

\[
\exp\left[-a\sum |k_{m+1}-k_m|\right].
\]

For any path arriving from spectral infinity at finite `N`, the total spectral distance diverges.

Hence long jumps cannot repair the vanishing factorial weight of the adjacent cascade.

The direct analytic tail creates arbitrarily high frequencies of exponentially tiny amplitude, but it cannot transport an order-one fraction of a surviving mode through infinitely many parabolic shells in finite normal depth.

---

## 8. Non-explosion interpretation

The mechanism is analogous to a pure-birth cascade with transfer rate proportional to spectral level:

\[
\lambda_j\sim j.
\]

The characteristic transfer times obey

\[
\sum_{j=1}^{\infty}\frac1{\lambda_j}
\sim
\sum_{j=1}^{\infty}\frac1j
=\infty.
\]

Therefore the first-order transfer process is non-explosive.

A genuinely second-order variable-coefficient transfer rate `lambda_j~j^2` would be dangerous because

\[
\sum j^{-2}<\infty.
\]

M5-159 explicitly excludes such a hidden second-order transfer channel: the only second-order operator is constant-coefficient viscosity and commutes with the spectral projectors.

---

## 9. Consequence for flat zero-boundary data

The flat boundary supplies

\[
Q_jK(0)=0
\qquad\text{for every fixed finite }j.
\]

If a nonzero solution existed at `z>0`, some fixed finite band would have to receive information through an infinite chain originating at spectral infinity.

Sections 5--8 show that the total weight of every such chain is zero, provided two already-identified quantitative packages are made explicit:

1. a shell-uniform stable principal-propagator bound on intervals `Delta z_j~j^-2`;
2. the analytic off-diagonal coefficient estimate for the first-order transfer operator.

Under those packages,

\[
\boxed{
Q_jK(z)=0
\quad\forall j<\infty,
}
\]

hence

\[
\boxed{K(z)=0}
\]

in the statistical pair Hilbert space for sufficiently small positive `z`.

---

## 10. From tail-neighborhood vanishing to pair equality

If `K=0` on a nonempty exterior normal neighborhood, the relative vorticity vanishes on a nonempty open spatial exterior set for almost every pair in the invariant measure.

Biot--Savart plus the already fixed decay/gauge conditions removes a harmonic velocity difference, giving `V=W` there.

For each fixed Leray time the W1 velocity fields are spatially real analytic.  Vanishing on a nonempty open set therefore extends to the connected whole space:

\[
\boxed{V=W.}
\]

Thus the off-diagonal invariant pair measure would collapse onto the diagonal, contradicting the definition of `P1_B^S`.

This final implication is conditional only on the two packaging lemmas in Section 9.

---

## 11. DSD four-chain audit

### Formation — GREEN

The cascade is formed from actual spectral projectors of the invariant pair Hilbert space; no discrete Koopman spectrum is assumed.

### Axis — GREEN

Normal parabolic scale `j^-2` and cross-section spectral level `j` remain separate.

### Static aggregation — GREEN

Second-order viscous amplification/damping is not counted as transfer.  Only projector-noncommuting terms contribute to the cascade weight.

### Dynamics — GREEN / YELLOW

The differential-order non-explosion mechanism is GREEN.

Full closure is YELLOW until the two quantitative packaging lemmas are written with constants and domains.

### Cross-audit — GREEN

No finite critical budget is used.  The contradiction, if completed, is uniqueness/non-explosion of spectral information rather than accumulation of repeated positive costs.

---

## 12. Next two packaging lemmas

The remaining work before `P1_B^S` can be marked closed is now finite and explicit:

### Lemma A — stable principal shell propagator

Prove uniformly for shell `j` that the flat-selected principal `(K,R)` system has

\[
\|U_j(z_2,z_1)\|\le C_0
\]

on

\[
0\le z_2-z_1\le\gamma(1+j)^{-2}.
\]

### Lemma B — analytic transfer off-diagonal bound

From the M5-155 time analyticity and the uniform scaled-shell spatial analyticity, prove

\[
\boxed{
\|Q_k\mathcal NQ_j\|
\le
C(1+j)e^{-a|k-j|}.
}
\]

Once A and B are GREEN, the factorial path estimate closes the statistical flat branch.

`P1_B^P` remains separate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
