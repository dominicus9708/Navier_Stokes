# DSD Active-Core Hyperpalinstrophy Two-Sided Window

Date: 2026-08-25

Status: **POSITIVE-DENSITY ACTIVE CORE FORCES A MEAN HYPERPALINSTROPHY LOWER BOUND / COMBINED WITH THE RECURRENT H1 CAP TO GIVE A NECESSARY ENSTROPHY SURVIVAL FLOOR / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the correlation-sensitive curvature gate

The preceding note proved the pointwise inequality

\[
\boxed{
M
\le
C_{CR}
K_{3,L}^{9/35}
R^{3/35}
Z^{2/7},
}
\]

where

\[
M=\|W\|_\infty,
\qquad
Z=\|W\|_2^2,
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

The no-`H` analytic corridor supplies a uniform finite third-derivative ceiling

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
Z^{10/3}.
\]

Therefore

\[
\boxed{
R
\ge
C_{CR}^{-35/3}
K_{3,L}^{-3}
M^{35/3}
Z^{-10/3}.
}
\]

The constant simplifies exactly. Since

\[
C_{CR}
=
C_T^{-2/7}(24/\pi)^{3/35},
\]

we get

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
\boxed{
C_R^{act}
\approx3.6234625949.
}
\]

Thus

\[
\boxed{
R
\ge
C_R^{act}
K_{3,L}^{-3}
M^{35/3}
Z^{-10/3}.
}
\]

Status: **PROVED.**

---

## 3. Apply on positive-density active terminal windows

The explicit Leray active-window construction gives a set of Leray times of lower density at least

\[
\boxed{d_*>0}
\]

on which a fixed local vorticity floor is present.

In particular, on every such active time,

\[
\boxed{M(s)\ge m_*>0.}
\]

One may take the explicit terminal-window value

\[
m_*=w_L=\frac{\mu_-}{2}
\]

from the dynamic-to-Leray thick-tube conversion.

On the bounded-enstrophy branch,

\[
Z(s)\le Z_+.
\]

Therefore every active time obeys

\[
\boxed{
R(s)
\ge
C_R^{act}
K_{3,L}^{-3}
 m_*^{35/3}
 Z_+^{-10/3}.
}
\]

Averaging over Leray time yields

\[
\boxed{
\overline R
\ge
R_{act,-}
:=
d_*
C_R^{act}
K_{3,L}^{-3}
 m_*^{35/3}
 Z_+^{-10/3}.
}
\]

Thus the recurrent active core cannot have arbitrarily small mean hyperpalinstrophy.

Status: **PROVED.**

---

## 4. Combine with the existing recurrent upper cap

The recurrent H1/Agmon balance gives

\[
\boxed{
\overline R
\le
R_{cap}
:=
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

Every recurrent survivor must therefore satisfy the two-sided window

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
 d_*
C_R^{act}
K_{3,L}^{-3}
 m_*^{35/3}
 Z_+^{-10/3}
\le
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
\]

Move the powers of `Z_+` to one side:

\[
\boxed{
Z_+^{25/3}
\ge
\frac{16d_*C_R^{act}}{C_*^8}
\nu^8
K_{3,L}^{-3}
 m_*^{35/3}.
}
\]

Hence every recurrent survivor must satisfy the enstrophy floor

\[
\boxed{
Z_+
\ge
Z_{surv,-}
:=
\left(
\frac{16d_*C_R^{act}}{C_*^8}
\right)^{3/25}
\nu^{24/25}
K_{3,L}^{-9/25}
 m_*^{7/5}.
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
Z_{surv,-}
\approx
1.6277558012\,
 d_*^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,L}^{-9/25}
 m_*^{7/5}.
}
\]

Status: **NECESSARY CONDITION FOR RECURRENT SURVIVAL.**

---

## 5. Tightness upper bound gives a direct contradiction certificate

The recurrent non-`T` tightness reduction supplies an upper bound

\[
\boxed{
Z_+
\le
Z_{tight}
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Therefore the recurrent branch is impossible whenever

\[
\boxed{
Z_{tight}
<
Z_{surv,-}.
}
\]

Explicitly,

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
1.6277558012\,
 d_*^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,L}^{-9/25}
 m_*^{7/5}
\quad\Longrightarrow\quad
\text{no recurrent survivor}.
}
\]

This certificate does not use the Betchov residual decomposition at all. It comes only from

1. analytic curvature thickness;
2. positive-density active-core amplitude;
3. the recurrent H1 hyperpalinstrophy cap;
4. enstrophy tightness.

---

## 6. Interpretation

The bounded recurrent core is now trapped between two incompatible tendencies.

A nonzero active core with bounded third derivative must maintain enough curvature/hyperpalinstrophy to support its vorticity amplitude:

\[
\text{active amplitude}
\Longrightarrow
\overline R\ge R_{act,-}.
\]

But recurrent H1 balance prevents an arbitrarily large derivative background:

\[
\overline R\le R_{cap}.
\]

Consequently the survivor needs **enough total enstrophy** to dilute the curvature cost:

\[
\boxed{Z_+\ge Z_{surv,-}.}
\]

Thus small bounded enstrophy is no longer merely favorable for regularity; below the explicit survival threshold it is incompatible with the persistent active core.

---

## 7. Relation to the previous Betchov route

The previous correlation-sensitive Betchov certificate gives an upper-amplitude condition involving

\[
\overline M_Z.
\]

The present argument instead inverts the same curvature estimate and obtains a lower derivative requirement.

The two routes are complementary:

\[
\boxed{
\begin{aligned}
\text{Betchov route:}&\quad
\overline R\text{ cap}
\Rightarrow
\overline M_Z\text{ cap},\\
\text{active-core route:}&\quad
M\ge m_*\text{ on density }d_*
\Rightarrow
\overline R\text{ floor}.
\end{aligned}
}
\]

A recurrent survivor must satisfy both simultaneously.

---

## 8. DSD audit

No new escape class is introduced.

The formed finite channels are

\[
(M,Z,R,K_{3,L},d_*,m_*).
\]

The logic is

\[
\boxed{
\text{persistent formed core}
\to
\text{curvature cost}
\to
\text{mean derivative floor}
\to
\text{two-sided recurrent budget}.
}
\]

All inequalities are standard analytic/PDE estimates inside the DSD bookkeeping; DSD is not used as a substitute for the Navier--Stokes equations.

---

## 9. Updated frontier

The recurrent branch now has simultaneous necessary windows for

\[
\boxed{
Z_+,
\qquad
\overline R,
\qquad
\bar\lambda,
\qquad
\overline M_Z.
}
\]

The highest-leverage next calculation is to substitute the explicit active-window constants

\[
 d_*,
\qquad
m_*=\mu_-/2,
\]

and the dynamic-to-Leray scaling

\[
K_{3,L}\le\mu_+^{5/2}K_{3,+}
\]

into `Z_surv,-`. This will reduce the lower survival threshold to the same finite first-hitting parameter set used by the tightness upper bound, allowing a direct parameter-window comparison.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
