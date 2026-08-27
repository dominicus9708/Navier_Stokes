# DSD M5-170 — Exact Dirichlet Quotient and Volterra Covariance Gate

Date: 2026-08-27

Status: **P1_B^S EXACT FREQUENCY REDUCTION / USING `R=z F_z`, THE CROSS-SECTION DIRICHLET QUOTIENT HAS AN EXACT DERIVATIVE FORMULA; INSERTING THE M5-169 STABLE KERNEL SHOWS THAT THE LAST FAST-NORMAL COMPATIBILITY EDGE IS A SINGLE VOLTERRA COVARIANCE SIGN/ERROR ESTIMATE / THE SAME-POINT PRINCIPAL TERM IS A NONNEGATIVE SPECTRAL VARIANCE AND THE VARIABLE RELATIVE COUPLING ENTERS WITH AN EXTRA FACTOR `z` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frequency objects

Use the invariant pair Hilbert space and define

\[
A:=I-4G^2-\Delta_{S^2}>0.
\]

Let

\[
E(z):=\|F(z)\|^2,
\qquad
H(z):=\langle AF(z),F(z)\rangle.
\]

Whenever `E(z)>0`, define

\[
\boxed{
\mathcal N(z):=\frac{H(z)}{E(z)}.
}
\]

This is equivalent to the square of the audited cross-section frequency up to harmless fixed constants.

---

## 2. Exact quotient derivative

M5-168 gives

\[
F_z=\frac Rz.
\]

Therefore

\[
E'
=
\frac2z\operatorname{Re}\langle R,F\rangle
\]

and, because `A` is `z`-independent,

\[
H'
=
\frac2z\operatorname{Re}\langle AF,R\rangle.
\]

Hence

\[
\boxed{
\mathcal N_z
=
\frac{2}{zE}
\operatorname{Re}
\langle
(A-\mathcal N)F,
R
\rangle.
}
\]

No slow approximation is used.

---

## 3. Insert the exact stable kernel

M5-169 gives

\[
R(z)
=
\int_0^z
\mathcal K(z,\zeta)
\left[
LF(\zeta)
+\zeta\mathcal N_{rel}(\zeta)F(\zeta)
\right]d\zeta.
\]

Therefore

\[
\boxed{
\mathcal N_z
=
\mathcal V_{pr}(z)
+\mathcal V_{rel}(z),
}
\]

where

\[
\mathcal V_{pr}
:=
\frac2{zE}
\operatorname{Re}
\left\langle
(A-\mathcal N)F(z),
\int_0^z\mathcal K(z,\zeta)LF(\zeta)d\zeta
\right\rangle
\]

and

\[
\mathcal V_{rel}
:=
\frac2{zE}
\operatorname{Re}
\left\langle
(A-\mathcal N)F(z),
\int_0^z\mathcal K(z,\zeta)\zeta\mathcal N_{rel}F(\zeta)d\zeta
\right\rangle.
\]

The entire fast-normal compatibility question is now contained in these two explicit terms.

---

## 4. Same-point principal covariance

If the kernel were replaced by its leading mass `z delta_zeta=z`, then

\[
R_{pr}=zLF.
\]

Recall

\[
L
=
\nu A_0
-6\nu G
-2\nu I,
\]

with `A=I+A_0`.

The skew term `G` commutes with `A`, and the scalar term cancels from the quotient covariance.  Thus

\[
\operatorname{Re}\langle(A-\mathcal N)F,LF\rangle
=
\nu
\left[
\|A F\|^2
-\frac{\langle AF,F\rangle^2}{E}
\right]
\]

up to the harmless shift convention in `A`.

Therefore

\[
\boxed{
\mathcal V_{pr}^{same}
=
\frac{2\nu}{E}
\left[
\|AF\|^2
-\mathcal N^2E
\right]
\ge0.
}
\]

This is exactly the Agmon--Nirenberg / Dirichlet-quotient variance sign in the backward-`z` orientation.

Equivalently, in the forward `tau=-log z` direction the same term is nonpositive.

---

## 5. Relative coupling has the correct small factor

The nonlinear relative term enters the fast source as

\[
\zeta\mathcal N_{rel}F.
\]

The M5-169 kernel has total mass at most `z`. Hence the relative part of `R` contains two small normal factors in the crude graph estimate:

\[
\boxed{
\|R_{rel}(z)\|
\le
z^2
\sup_{\zeta\le z}
\|\mathcal N_{rel}F(\zeta)\|.
}
\]

After division by the `z` in the quotient derivative, its natural scale is therefore

\[
\boxed{
O(z)\times\text{first-order cross-frequency transfer}.
}
\]

This matches M5-154/M5-166 exactly.

The M5-163 commutator estimate then predicts

\[
\mathcal V_{rel}
\ge
-Cz(1+\mathcal N)
\]

once the kernel-local future envelope is converted into the quotient energy form.

---

## 6. The one remaining principal kernel question

The only nontrivial issue not resolved by the same-point calculation is that

\[
\mathcal K(z,\zeta)LF(\zeta)
\]

uses nearby smaller normal depths and includes a unitary genealogical shift.

Thus one must prove a lower bound of the form

\[
\boxed{
\mathcal V_{pr}(z)
\ge
- C z(1+\mathcal N(z)).
}
\]

The positive same-point spectral variance may be discarded; only the negative error caused by Volterra lag must be estimated.

If this and the corresponding relative estimate hold, then

\[
\boxed{
\mathcal N_z
\ge
-Cz(1+\mathcal N).
}
\]

Equivalently, since `z=e^-tau`,

\[
\boxed{
\mathcal N_\tau
\le
Cz^2(1+\mathcal N)
}
\]

under this normalization convention; with the unshifted M5-166 time scaling the equivalent bound is at worst `C e^-tau(1+N)`.  Either form is integrable and forbids parabolic frequency escape.

The precise power of `z` is secondary; integrability is the structural requirement.

---

## 7. Kernel localization data available for the lag estimate

From M5-169, after

\[
t=\zeta^{-1}-z^{-1},
\]

the scalar kernel measure is proportional to

\[
e^{-t/(4\nu)}(1+zt)^{-5/2}dt.
\]

Thus the normalized kernel is exponentially localized at bounded `t`, which means

\[
\boxed{
|z-\zeta|=O(z^2),
\qquad
|\log(\zeta/z)|=O(z)
}
\]

in every finite kernel moment.

Consequently:

- normal lag costs one factor `z^2 F_z`;
- genealogical unitary lag costs one factor `z G`;
- coefficient variation costs at least one factor `z`.

These are the exact small parameters available to prove the Section-6 lower bound.

---

## 8. DSD four-chain audit

### Formation — GREEN

The quotient derivative and kernel decomposition are exact.

### Axis — GREEN

Normal lag, genealogical shift, and cross spectral frequency are represented by distinct terms.

### Static aggregation — GREEN

The positive principal variance is not counted as transfer; only the Volterra-lag error can reduce it.

### Dynamics — GREEN / ONE YELLOW LEMMA

All remaining dynamics are isolated in the principal Volterra covariance lower bound plus the already-first-order relative commutator estimate.

### Cross-audit — GREEN

No Gaussian envelope, finite critical budget, or same-norm analytic derivative estimate is used.

---

## 9. Next calculation

Prove the kernel-lag estimate

\[
\boxed{
\mathcal V_{pr}(z)
\ge
-Cz(1+\mathcal N(z))
}
\]

using the exact kernel moments and the stable graph-norm slaving, then combine it with

\[
\mathcal V_{rel}(z)
\ge-Cz(1+\mathcal N(z)).
\]

This is now the single explicit compatibility gate between M5-166 and the exact M5-168/M5-169 system.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
