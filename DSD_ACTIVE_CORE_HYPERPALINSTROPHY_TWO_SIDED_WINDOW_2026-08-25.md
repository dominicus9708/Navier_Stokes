# DSD Active-Core Hyperpalinstrophy Two-Sided Window

Date: 2026-08-25

Status: **POSITIVE-DENSITY ACTIVE CORE FORCES A MEAN HYPERPALINSTROPHY LOWER BOUND / COMBINED WITH THE RECURRENT H1 CAP TO GIVE A NECESSARY LERAY ENSTROPHY FLOOR / EXACTLY CONVERTED TO A DYNAMIC FIRST-HITTING ENSTROPHY FLOOR / NORMALIZATION AUDIT CORRECTED / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the correlation-sensitive curvature gate

The preceding note proved the pointwise Leray inequality

\[
\boxed{
M
\le
C_{CR}
K_{3,L}^{9/35}
R^{3/35}
Z_L^{2/7},
}
\]

where

\[
M=\|W\|_\infty,
\qquad
Z_L=\|W\|_2^2,
\qquad
R=\|\Delta W\|_2^2,
\]

and

\[
C_{CR}
=
C_T^{-2/7}
\left(\frac{24}{\pi}\right)^{3/35},
\qquad
C_T=\frac{64\sqrt2\pi}{105}.
\]

Numerically,

\[
C_{CR}\approx0.8955196181.
\]

The no-`H` analytic corridor supplies a finite Leray third-derivative ceiling

\[
K_{3,L}<\infty.
\]

---

## 2. Invert the amplitude inequality

Raise the amplitude inequality to the power `35/3`:

\[
M^{35/3}
\le
C_{CR}^{35/3}
K_{3,L}^3
R
Z_L^{10/3}.
\]

Therefore

\[
\boxed{
R
\ge
C_{CR}^{-35/3}
K_{3,L}^{-3}
M^{35/3}
Z_L^{-10/3}.
}
\]

The constant simplifies exactly:

\[
\boxed{
C_{CR}^{-35/3}
=
\frac{\pi}{24}C_T^{10/3}
=:C_R^{act}.
}
\]

Numerically,

\[
\boxed{C_R^{act}\approx3.6234625949.}
\]

Thus

\[
\boxed{
R
\ge
C_R^{act}
K_{3,L}^{-3}
M^{35/3}
Z_L^{-10/3}.
}
\]

Status: **PROVED.**

---

## 3. Positive-density active terminal windows

The explicit terminal-window conversion gives a Leray-time set of lower density

\[
\boxed{d_L>0}
\]

on which

\[
\boxed{M(s)\ge m_L>0.}
\]

One may take

\[
\boxed{m_L=w_L=\frac{\mu_-}{2}.}
\]

Let the global Leray enstrophy ceiling be denoted explicitly by

\[
\boxed{Z_{L,+}:=\sup_s Z_L(s).}
\]

Then every active time satisfies

\[
\boxed{
R(s)
\ge
C_R^{act}
K_{3,L}^{-3}
 m_L^{35/3}
 Z_{L,+}^{-10/3}.
}
\]

Averaging gives

\[
\boxed{
\overline R
\ge
R_{act,-}
:=
d_L
C_R^{act}
K_{3,L}^{-3}
 m_L^{35/3}
 Z_{L,+}^{-10/3}.
}
\]

Status: **PROVED.**

---

## 4. Combine with the recurrent H1 upper cap

The recurrent H1/Agmon balance gives

\[
\boxed{
\overline R
\le
R_{cap}
:=
\frac{C_*^8}{16}
\frac{Z_{L,+}^5}{\nu^8}.
}
\]

Hence every recurrent survivor must satisfy

\[
\boxed{
R_{act,-}
\le
\overline R
\le
R_{cap}.
}
\]

Equivalently,

\[
Z_{L,+}^{25/3}
\ge
\frac{16d_LC_R^{act}}{C_*^8}
\nu^8
K_{3,L}^{-3}
 m_L^{35/3}.
\]

Therefore

\[
\boxed{
Z_{L,+}
\ge
Z_{L,surv,-}
:=
\left(
\frac{16d_LC_R^{act}}{C_*^8}
\right)^{3/25}
\nu^{24/25}
K_{3,L}^{-9/25}
 m_L^{7/5}.
}
\]

Numerically,

\[
(16C_R^{act})^{3/25}
\approx1.6277558012,
\]

so

\[
\boxed{
Z_{L,surv,-}
\approx
1.6277558012\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,L}^{-9/25}
 m_L^{7/5}.
}
\]

Status: **NECESSARY LERAY-ENSTROPHY CONDITION FOR RECURRENT SURVIVAL.**

---

## 5. Correct dynamic-to-Leray conversion

The recurrent tightness ceiling in `PV_TIGHTNESS_ANALYTICITY_PARAMETER_REDUCTION_2026-08-20.md` is naturally stated in the dynamic first-hitting coordinates. Therefore it must not be identified directly with `Z_{L,+}`.

Let

\[
Z_D:=\|\widetilde\Omega\|_2^2,
\qquad
Z_{D,+}:=\sup Z_D.
\]

The exact coordinate conversion from `DSD_DYNAMIC_TO_LERAY_BETCHOV_CONSTANT_COLLAPSE_2026-08-25.md` is

\[
\boxed{Z_L=\mu^{1/2}Z_D.}
\]

Thus

\[
\boxed{Z_{L,+}\le\mu_+^{1/2}Z_{D,+}.}
\]

Similarly, because

\[
W(Y)=\mu\widetilde\Omega(\sqrt\mu Y),
\]

three derivatives give

\[
\boxed{
K_{3,L}
\le
\mu_+^{5/2}K_{3,+},
}
\]

where

\[
K_{3,+}:=\sup\|\nabla_z^3\widetilde\Omega\|_\infty.
\]

Insert the latter into the Leray survival floor. Since the exponent of `K3_L` is negative, using its upper bound gives the safe weaker lower estimate

\[
Z_{L,+}
\ge
1.6277558012\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 \mu_+^{-9/10}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{2}\right)^{7/5}.
\]

Since `Z_{L,+}<=mu_+^(1/2) Z_{D,+}`, recurrence therefore requires

\[
\boxed{
Z_{D,+}
\ge
Z_{D,surv,-},
}
\]

where

\[
\boxed{
Z_{D,surv,-}
:=
0.6168041085\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5}.
}
\]

The power simplification is exact:

\[
\mu_+^{-1/2}\mu_+^{-9/10}
\mu_-^{7/5}
=
\left(\frac{\mu_-}{\mu_+}\right)^{7/5}.
\]

This is the correctly normalized dynamic first-hitting survival floor.

Status: **PROVED AFTER NORMALIZATION CORRECTION.**

---

## 6. Dynamic tightness upper bound and direct contradiction

The non-`T` dynamic enstrophy-tightness condition gives

\[
\int_{B_{R_Z}}|\widetilde\Omega|^2
\ge
(1-\varepsilon_Z)Z_D.
\]

Because `|widetilde Omega|<=1`,

\[
\boxed{
Z_{D,+}
\le
Z_{D,tight}
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Combining with the dynamic survival floor, the recurrent branch is impossible whenever

\[
\boxed{
Z_{D,tight}<Z_{D,surv,-}.
}
\]

Explicitly,

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
0.6168041085\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5}
\Longrightarrow
\text{no recurrent survivor}.
}
\]

This is now a comparison entirely inside the same dynamic/tightness parameter system.

---

## 7. Explicit active-window clock constants

The repository supplies

\[
\boxed{
\delta_D
=
\frac1{4(2B_++3\nu K_{2,+})},
}
\]

\[
\boxed{
\mu_-
=
\frac{L_-}{q}e^{-B_+\delta_D},
}
\]

\[
\boxed{
\mu_+
=
\frac{L_+q}{q-1}
+
\delta_De^{B_+\delta_D},
}
\]

and

\[
\boxed{
G_L
=
\log\left[
q\frac{L_+q/(q-1)}{L_-/q}
\right],
}
\]

with active-window lower density

\[
\boxed{
 d_L
=
\min\left\{
1,
\frac{\delta_D}{\mu_+G_L}
\right\}.
}
\]

Thus the dynamic survival threshold depends only on

\[
\boxed{
q,
L_-,
L_+,
B_+,
K_{2,+},
K_{3,+},
R_Z,
\varepsilon_Z,
\nu,
C_*.
}
\]

The first-derivative analytic ceiling `K1,+` drops out of this particular two-sided `R` window.

---

## 8. Interpretation

A nonzero recurrent active core cannot simultaneously have

1. too little dynamic global enstrophy;
2. bounded third derivative;
3. positive-density terminal amplitude;
4. and the existing finite recurrent H1 derivative budget.

The active amplitude forces a lower derivative cost, while the H1 identity caps the mean derivative cost. The only way to reconcile them is for the dynamic enstrophy ceiling to remain above

\[
Z_{D,surv,-}.
\]

Thus the non-`T` recurrent class is confined to the finite interval

\[
\boxed{
Z_{D,surv,-}
\le
Z_{D,+}
\le
Z_{D,tight}.
}
\]

If this interval is empty, the recurrent branch closes.

---

## 9. DSD audit

The normalization error in the previous version is removed explicitly: dynamic and Leray enstrophy are never identified without the factor `mu^(1/2)`.

The finite formed channels are

\[
(M,Z_L,Z_D,R,K_{3,L},K_{3,+},d_L,\mu_-,\mu_+).
\]

The standard PDE logic is

\[
\boxed{
\text{persistent active amplitude}
\to
\text{curvature/hyperpalinstrophy floor}
\to
\text{mean }R\text{ lower bound}
\to
\text{H1 mean }R\text{ upper bound}
\to
\text{dynamic enstrophy survival interval}.
}
\]

DSD is only bookkeeping for the finite channels.

---

## 10. Updated frontier

The next remaining universal constant in this route is the Agmon factor

\[
C_*=C_NC_A,
\qquad
C_N=\frac4{\sqrt6}.
\]

An explicit admissible whole-space `R3` Agmon constant can be derived directly by Fourier splitting. Doing so will remove `C_A` as a free symbolic constant and leave the main unresolved quantities as the first-hitting analytic/tightness parameters themselves.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
