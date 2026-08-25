# DSD Sup-Free Recurrent Betchov Frequency Window

Date: 2026-08-25

Status: **COARSE `K_I` SUPREMUM REMOVED FROM THE EXACT INVARIANT-MEASURE WINDOW / Z-WEIGHTED TYPE-I AMPLITUDE IDENTIFIED AS THE TRUE SCALAR / EXACT ROOT-LOCATION CLOSURE TESTS DERIVED / NO NUMERIC CLOSURE WITHOUT A NEW CORRELATION BOUND / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

`DSD_RECURRENT_BETCHOV_FREQUENCY_WINDOW_2026-08-25.md` used

\[
\langle M_LZ\rangle
\le K_I\langle Z\rangle,
\]

where

\[
K_I=\sup_sM_L(s),
\qquad
M_L(s)=\|W(s)\|_\infty.
\]

The first-hitting tower only supplies the coarse continuous backward bound

\[
K_I\le\frac{L_+q^2}{q-1}.
\]

This can be much larger than the actual recurrent amplitude sampled when enstrophy is present. Since the invariant enstrophy balance contains `M_L Z`, not `M_L` alone, the supremum should not be introduced unless necessary.

---

## 2. Define the exact Z-weighted amplitude

On a nonzero invariant recurrent measure, define

\[
\boxed{
\overline M_Z
:=
\frac{\langle M_LZ\rangle}
{\langle Z\rangle}.
}
\]

Since

\[
0<\langle Z\rangle<\infty,
\]

this is well-defined, and trivially

\[
0\le\overline M_Z\le K_I.
\]

It is the `Z`-weighted average Leray vorticity amplitude, not a worst-time ceiling.

Status: **DEFINITION / EXACT FOR THE INVARIANT BALANCE.**

---

## 3. Exact recurrent residual lower bound without `K_I`

The invariant Leray enstrophy identity is

\[
\frac14\langle Z\rangle
+\nu\langle Q\rangle
=\langle P\rangle.
\]

The positive-middle/Betchov production split is

\[
P(s)
\le
\frac12M_L(s)Z(s)+\mathcal R_B(s).
\]

Averaging gives

\[
\frac14\langle Z\rangle
+\nu\langle Q\rangle
\le
\frac12\langle M_LZ\rangle
+\langle\mathcal R_B\rangle.
\]

Divide by `⟨Z⟩` and define

\[
\bar\lambda:=\frac{\langle Q\rangle}{\langle Z\rangle}.
\]

Then exactly

\[
\boxed{
\frac{\langle\mathcal R_B\rangle}{\langle Z\rangle}
\ge
\frac14-\frac{\overline M_Z}{2}
+\nu\bar\lambda.
}
\]

No first-hitting supremum has entered.

Status: **PROVED.**

---

## 4. Combine with the Young-free residual upper bound

The existing global Betchov interpolation gives

\[
\frac{\langle\mathcal R_B\rangle}{\langle Z\rangle}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4},
\]

with

\[
\boxed{
C_B=\frac8{\pi3^{9/4}}
\approx0.21498952055.
}
\]

Therefore every recurrent survivor must satisfy the **sup-free scalar window**

\[
\boxed{
\nu\bar\lambda
+\frac14-\frac{\overline M_Z}{2}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

Let

\[
x:=\bar\lambda^{1/4},
\qquad
b:=C_BZ_+^{1/2},
\qquad
a_Z:=\frac14-\frac{\overline M_Z}{2}.
\]

Then

\[
\boxed{
F_Z(x):=\nu x^4-bx^3+a_Z\le0.
}
\]

Status: **PROVED.**

---

## 5. Exact empty-window criterion

The positive minimum is at

\[
x_*=rac{3b}{4\nu}
=\frac{3C_BZ_+^{1/2}}{4\nu}.
\]

At that point

\[
F_Z(x_*)
=
\frac14-\frac{\overline M_Z}{2}
-
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
\]

Thus **no recurrent frequency at all** is possible if

\[
\boxed{
\overline M_Z
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<\frac12.
}
\]

This is strictly sharper than the old sufficient condition obtained by replacing `overline M_Z` by `K_I`.

Status: **PROVED.**

---

## 6. Add the active-core frequency floor

Let

\[
\bar\lambda\ge c_{core}>0
\]

be any proved recurrent active-core frequency floor. The repository currently supplies, on the localized active-core branch,

\[
\boxed{
 c_{core}
\ge
\frac{2}{C_\phi^4}
\left(\frac{z_*}{Z_*}\right)^3
}
\]

when the fixed core enstrophy is bounded below by `z_*` and global enstrophy by `Z_*`.

Every recurrent survivor must therefore have

\[
x\ge x_0:=c_{core}^{1/4}.
\]

There are two cases.

### Case A: the floor begins to the right of the polynomial minimum

If

\[
\boxed{x_0\ge x_*}
\]

then `F_Z` is increasing on `[x0,infinity)`. Consequently recurrence is impossible exactly when

\[
\boxed{F_Z(x_0)>0.}
\]

Equivalently,

\[
\boxed{
\nu c_{core}
+\frac14-\frac{\overline M_Z}{2}
>
C_BZ_+^{1/2}c_{core}^{3/4}.
}
\]

### Case B: the floor begins to the left of the minimum

If

\[
x_0<x_*,
\]

then a positive value `F_Z(x0)>0` is not enough; the polynomial may dip negative later. In that case the exact closure remains the empty-window condition or requires locating the upper root and proving `x0` lies above it.

Status: **PROVED.**

---

## 7. Coarse first-hitting constant audit

The continuous backward first-hitting estimate gives

\[
K_I(q)=\frac{L_+(q)q^2}{q-1}.
\]

If one temporarily holds the stage ceiling `L_+` fixed while varying only the geometric prefactor, then

\[
\frac{q^2}{q-1}
\]

has its minimum at

\[
q=2,
\]

with value `4`.

Thus for the standard `q=2` ladder,

\[
\boxed{K_I=4L_+.}
\]

The old strong condition `K_I<1/2` would require

\[
\boxed{L_+<1/8.}
\]

This shows why the supremum-based Betchov condition is quantitatively demanding.

Important audit: `L_+` itself may depend on the choice of `q`; therefore the statement `q=2 is globally optimal` is **not** claimed. Only the explicit geometric prefactor is minimized at `q=2` for fixed stage data.

---

## 8. What must be estimated next

The true remaining scalar is no longer the coarse `K_I` but

\[
\boxed{
\overline M_Z
=
\frac{\langle M_LZ\rangle}{\langle Z\rangle}.
}
\]

Three possibilities can close the window:

1. **anti-correlation:** high enstrophy occurs preferentially when `M_L` is below its sup, lowering `overline M_Z`;
2. **high active-core frequency:** `c_core` lies above the upper Betchov root;
3. **small bounded-Z ceiling:** the residual capacity `C_B Z_+^{1/2}` is too small.

The first-hitting clock by itself gives only `overline M_Z<=K_I`; it does not prove the required anti-correlation.

---

## 9. DSD interpretation

The previous scalar channel `K_I` mixed two distinct technical descriptions:

- worst-time Type-I amplitude;
- enstrophy-weighted recurrent production amplitude.

The sup-free formulation separates them.

The correct formed recurrent variables are now

\[
\boxed{
\overline M_Z,
\quad
\bar\lambda,
\quad
Z_+,
\quad
\overline{\mathcal R}_B.
}
\]

and the exact compatibility condition is one quartic inequality.

---

## 10. Audit verdict

### PROVED

- the Betchov frequency window can be written without `K_I`;
- the exact amplitude entering it is `overline M_Z`;
- exact empty-window and frequency-floor closure tests are available;
- the old `K_I` criterion is only a coarse corollary.

### NOT DERIVED

- a strict upper bound on `overline M_Z` strong enough to empty the window;
- a current active-core frequency floor above the upper root for all surviving constants;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
