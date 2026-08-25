# DSD Direct-Agmon Active-Core Survival Floor

Date: 2026-08-25

Status: **DIRECT AGMON ROUTE REMOVES K2/K3 FROM THE ACTIVE-CORE HYPERPALINSTROPHY FLOOR / EXPLICIT DYNAMIC ENSTROPHY SURVIVAL FLOOR DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

The previous curvature-thickness route derived a recurrent hyperpalinstrophy floor by combining a pointwise vorticity maximum with a third-derivative analyticity ceiling. That route left the finite constant `K_{3,+}` in the final dynamic survival threshold.

There is a shorter route. Apply the three-dimensional Agmon inequality directly to the Leray vorticity `W`.

Let

\[
M:=\|W\|_\infty,
\qquad
Z:=\|W\|_2^2,
\qquad
R:=\|\Delta W\|_2^2.
\]

The explicit Fourier-splitting Agmon constant already derived in the repository is

\[
\boxed{
C_A=\frac{2\sqrt2}{\pi 3^{7/8}}.
}
\]

Hence

\[
\boxed{
M\le C_A Z^{1/8}R^{3/8}.
}
\]

This step uses no pointwise Hessian or third derivative.

## 2. Invert on an active time

From the Agmon inequality,

\[
R^{3/8}\ge C_A^{-1}MZ^{-1/8},
\]

so

\[
\boxed{
R\ge C_A^{-8/3}M^{8/3}Z^{-1/3}.
}
\]

Suppose the recurrent active-window construction gives a set of Leray times of lower density `d_*>0` on which

\[
M\ge m_*>0.
\]

On the bounded-enstrophy recurrent branch,

\[
Z\le Z_{L,+}.
\]

Therefore on every active time,

\[
\boxed{
R\ge C_A^{-8/3}m_*^{8/3}Z_{L,+}^{-1/3}.
}
\]

Averaging gives

\[
\boxed{
\overline R
\ge
d_*C_A^{-8/3}m_*^{8/3}Z_{L,+}^{-1/3}.
}
\]

Status: **PROVED.**

## 3. Combine with the recurrent H1 hyperpalinstrophy cap

The existing recurrent H1 balance gives

\[
\boxed{
\overline R
\le
\frac{C_*^8}{16}\frac{Z_{L,+}^5}{\nu^8},
}
\]

where

\[
C_*=C_NC_A,
\qquad
C_N=\frac4{\sqrt6}.
\]

Every recurrent survivor therefore satisfies

\[
d_*C_A^{-8/3}m_*^{8/3}Z_{L,+}^{-1/3}
\le
\frac{C_*^8}{16}\frac{Z_{L,+}^5}{\nu^8}.
\]

Thus

\[
Z_{L,+}^{16/3}
\ge
16d_*C_A^{-8/3}m_*^{8/3}\nu^8C_*^{-8}.
\]

Taking the power `3/16`,

\[
\boxed{
Z_{L,+}
\ge
16^{3/16}
C_A^{-1/2}
C_*^{-3/2}
 d_*^{3/16}
 m_*^{1/2}
 \nu^{3/2}.
}
\]

Using `C_*=C_NC_A` and the explicit constants,

\[
\boxed{
16^{3/16}C_A^{-1/2}C_*^{-3/2}
=
\frac{\pi^2 3^{5/2}}{2^{9/2}}
\approx6.7993578973.
}
\]

Hence the exact explicit Leray survival floor is

\[
\boxed{
Z_{L,+}
\ge
\frac{\pi^2 3^{5/2}}{2^{9/2}}
 d_*^{3/16}
 m_*^{1/2}
 \nu^{3/2}.
}
\]

Status: **NECESSARY CONDITION FOR RECURRENT SURVIVAL.**

## 4. Convert to dynamic first-hitting variables

On the explicit terminal active windows, use

\[
\mu:=TM_D,
\qquad
\mu_-\le\mu\le\mu_+.
\]

The dynamic-to-Leray enstrophy relation is

\[
\boxed{
Z_L=\mu^{1/2}Z_D.
}
\]

Therefore a uniform dynamic ceiling `Z_{D,+}` gives

\[
Z_{L,+}\le\mu_+^{1/2}Z_{D,+}.
\]

The active-window amplitude floor may be taken as

\[
\boxed{
m_*=\frac{\mu_-}{2}.
}
\]

The active time density is

\[
\boxed{
d_*=d_L
=
\min\left\{1,\frac{\delta_D}{\mu_+G_L}\right\},
}
\]

with

\[
\delta_D=\frac1{4(2B_++3\nu K_{2,+})},
\]

\[
\mu_-=\frac{L_-}{q}e^{-B_+\delta_D},
\]

\[
\mu_+=\frac{L_+q}{q-1}+\delta_De^{B_+\delta_D},
\]

and

\[
G_L=
\log\left[
q\frac{L_+q/(q-1)}{L_-/q}
\right].
\]

Substitution yields

\[
\mu_+^{1/2}Z_{D,+}
\ge
\frac{\pi^2 3^{5/2}}{2^{9/2}}
 d_L^{3/16}
\left(\frac{\mu_-}{2}\right)^{1/2}
\nu^{3/2}.
\]

Therefore

\[
\boxed{
Z_{D,+}
\ge
Z_{D,Ag,-}
:=
\frac{\pi^2 3^{5/2}}{32}
 d_L^{3/16}
\nu^{3/2}
\left(\frac{\mu_-}{\mu_+}\right)^{1/2}.
}
\]

Numerically,

\[
\boxed{
Z_{D,Ag,-}
\approx
4.8078720769
 d_L^{3/16}
\nu^{3/2}
\left(\frac{\mu_-}{\mu_+}\right)^{1/2}.
}
\]

This contains no `K_{3,+}` and no analyticity radius.

## 5. Combine with non-T tightness

The existing non-T tightness estimate gives

\[
\boxed{
Z_{D,+}
\le
Z_{D,tight}
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Consequently the recurrent survivor is impossible whenever

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
\frac{\pi^2 3^{5/2}}{32}
 d_L^{3/16}
\nu^{3/2}
\left(\frac{\mu_-}{\mu_+}\right)^{1/2}.
}
\]

Equivalently, survival requires

\[
\boxed{
R_Z^3
\ge
\frac{3(1-\varepsilon_Z)}{4\pi}
\frac{\pi^2 3^{5/2}}{32}
 d_L^{3/16}
\nu^{3/2}
\left(\frac{\mu_-}{\mu_+}\right)^{1/2}.
}
\]

## 6. Why this is stronger structurally than the K3 route

The previous curvature route required

\[
K_{3,+}<\infty
\]

and produced a survival floor with the weak factor

\[
K_{3,+}^{-9/25}.
\]

The direct Agmon route instead uses only quantities already present in the recurrent H1 ledger:

\[
(M,Z,R).
\]

Thus the finite channel chain is

\[
\boxed{
\text{active amplitude}
\to
\text{instantaneous Agmon derivative cost}
\to
\text{mean hyperpalinstrophy floor}
\to
\text{recurrent H1 cap}
\to
\text{enstrophy survival floor}.
}
\]

No analytic derivative hierarchy is needed for this lower survival threshold.

Analyticity remains useful only for establishing a positive terminal active-window density `d_L` and amplitude floor `m_*`, not for the derivative-cost inequality itself.

## 7. Updated frontier

The strongest current finite-window comparison is now

\[
\boxed{
Z_{D,Ag,-}
\le
Z_{D,+}
\le
Z_{D,tight}.
}
\]

The remaining constants entering the lower floor are only

\[
q,L_-,L_+,B_+,K_{2,+},\nu
\]

through `d_L,mu_-,mu_+`.

Thus `K_{3,+}` has been removed from the main survival-window frontier.

The next high-leverage step is to reduce the terminal persistence constants `B_+` and `K_{2,+}` themselves, or to replace the pointwise terminal persistence construction by an averaged recurrence argument that does not require their suprema.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]