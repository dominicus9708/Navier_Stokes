# DSD M5-496 — Production payer splits into a local dual-core payer or remote critical-enstrophy tail

Date: 2026-09-01

Status: **PAYER CONCENTRATION-COMPACTNESS / THE POSITIVE MEAN PRODUCTION REQUIRED BY M5-493--495 CAN BE SPATIALLY SPLIT INTO A FIXED DUAL-CORE BALL AND ITS EXTERIOR / USING GLOBAL `L2` CALDERON--ZYGMUND CONTROL OF STRAIN, THE TYPE-I `L-infinity` VORTICITY CAP, AND THE BOUNDED CRITICAL ENSTROPHY `E <= Z_*`, THE EXTERIOR PRODUCTION IS CONTROLLED BY THE SQUARE ROOT OF THE EXTERIOR ENSTROPHY MASS / HENCE UNIFORM `L2` TIGHTNESS OF THE SIMILARITY HULL FORCES THE REQUIRED PRODUCTION TO BE PAID LOCALLY IN A SUFFICIENTLY LARGE FIXED BALL; FAILURE OF TIGHTNESS PRODUCES A GENUINE REMOTE CRITICAL-ENSTROPHY TAIL/ESCAPE BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Required mean production

M5-486 gives

\[
\frac14\langle E\rangle
+
\langle P\rangle
=
\langle Q\rangle.
\]

M5-493 sharpens

\[
\langle P\rangle
\ge p_{mean}>0.
\]

Therefore

\[
\boxed{
\langle Q\rangle
\ge p_{mean}>0.
}
\]

The question is where this positive production is paid.

---

## 2. Spatial payer split

Fix a ball `B_R` centered at the marked similarity core and write

\[
Q
=
Q_{loc}(R)+Q_{ext}(R),
\]

where

\[
Q_{loc}(R)
:=
\int_{|y|\le R}
W\cdot\Sigma W\,dy,
\]

and

\[
Q_{ext}(R)
:=
\int_{|y|>R}
W\cdot\Sigma W\,dy.
\]

M5-496 estimates the exterior payer using only quantities already controlled on the compact bounded lane.

---

## 3. Global strain `L2` bound

Calderon--Zygmund gives

\[
\|\Sigma\|_2
\le C_{CZ,2}\|W\|_2.
\]

Since

\[
E=\|W\|_2^2\le Z_*,
\]

we have

\[
\boxed{
\|\Sigma\|_2
\le C Z_*^{1/2}.
}
\]

The Type-I similarity bound also gives a uniform vorticity-amplitude cap

\[
\boxed{
\|W\|_\infty
\le M_*<\infty.
}
\]

---

## 4. Exterior production is controlled by exterior enstrophy

By Holder,

\[
|Q_{ext}(R)|
\le
\|\Sigma\|_{L^2(|y|>R)}
\|W\|_{L^4(|y|>R)}^2.
\]

Bound the first factor by the global strain norm:

\[
\|\Sigma\|_{L^2(|y|>R)}
\le C Z_*^{1/2}.
\]

For the second factor,

\[
\begin{aligned}
\|W\|_{L^4(|y|>R)}^4
&=
\int_{|y|>R}|W|^4dy\\
&\le
M_*^2
\int_{|y|>R}|W|^2dy.
\end{aligned}
\]

Therefore

\[
\|W\|_{L^4(|y|>R)}^2
\le
M_*
\left(
\int_{|y|>R}|W|^2dy
\right)^{1/2}.
\]

Hence

\[
\boxed{
|Q_{ext}(R)|
\le
C Z_*^{1/2}M_*
\left(
E_{ext}(R)
\right)^{1/2},
}
\]

where

\[
E_{ext}(R)
:=
\int_{|y|>R}|W|^2dy.
\]

---

## 5. Uniform-tightness branch

Suppose the invariant compact hull is uniformly enstrophy-tight:

\[
\boxed{
\lim_{R\to\infty}
\sup_{\mathbf Y\in\mathfrak H}
E_{ext}^{\mathbf Y}(R)
=0.
}
\]

Choose `R=R_*` sufficiently large that

\[
C Z_*^{1/2}M_*
\sup_{\mathfrak H}E_{ext}(R_*)^{1/2}
\le
\frac14p_{mean}.
\]

Then pointwise on the hull

\[
|Q_{ext}(R_*)|
\le\frac14p_{mean}.
\]

Averaging,

\[
\langle Q_{loc}(R_*)\rangle
=
\langle Q\rangle-\langle Q_{ext}(R_*)\rangle.
\]

Since

\[
\langle Q\rangle\ge p_{mean},
\]

we obtain

\[
\boxed{
\langle Q_{loc}(R_*)\rangle
\ge
\frac34p_{mean}>0.
}
\]

Thus a uniformly tight recurrent hull must pay a fixed positive fraction of its production inside one fixed bounded similarity region containing the dual core.

---

## 6. Positive-frequency local payer on the compact branch

Inside the fixed ball `B_{R_*}`, local smooth compactness gives a uniform bound

\[
|Q_{loc}(R_*)|
\le Q_*<\infty.
\]

Since its invariant mean is positive, there exist fixed constants

\[
q_0>0,
\qquad
\delta_q>0
\]

such that the set

\[
\boxed{
\{\theta:Q_{loc}(R_*,\theta)\ge q_0\}
}
\]

has positive invariant time measure at least `delta_q`.

Therefore the tight branch contains recurrent local productive-strain episodes in the same bounded similarity region as the persistent dual-source geometry.

---

## 7. Failure of tightness

If uniform tightness fails, then there exists

\[
\varepsilon_{tail}>0
\]

such that for every `R>0` there is a hull state with

\[
\boxed{
\int_{|y|>R}|W|^2dy
\ge\varepsilon_{tail}.
}
\]

Thus a fixed amount of critical enstrophy remains capable of occupying arbitrarily remote similarity shells.

This is not a pointwise derivative blowup. It is a genuine concentration-compactness failure through translation/radial escape of critical vorticity mass.

Define

\[
\boxed{
H_{tail}^{remote-E}
:
\quad
\exists\varepsilon_{tail}>0
\text{ with remote }L^2\text{ mass at arbitrarily large normalized radii}.
}
\]

Then

\[
\boxed{
\text{failure of enstrophy tightness}
\Longrightarrow
H_{tail}^{remote-E}.
}
\]

---

## 8. Relation to the terminal critical tail

The M5-479--483 chain already forced a critical terminal velocity/Dirichlet tail on the compact bounded corridor.

M5-496 distinguishes two different notions:

1. a **terminal critical spatial tail** required at the blow-down boundary; and
2. **non-tight similarity enstrophy mass** at recurrent interior similarity times.

They may be related, but they are not identical and must not be silently conflated.

A future argument may show that recurrent interior remote enstrophy necessarily feeds the terminal dilation tail. That implication is not yet proved here.

---

## 9. Exact payer dichotomy

The current compact survivor therefore satisfies

\[
\boxed{
E_{dual}^{marked}
\Longrightarrow
H_{tail}^{remote-E}
\lor
L_{payer}^{local}.
}
\]

Here

\[
L_{payer}^{local}
:
\quad
\exists R_*,q_0,\delta_q>0
\]

such that local positive production

\[
Q_{loc}(R_*)\ge q_0
\]

occurs with positive similarity-time frequency.

---

## 10. DSD interpretation

The M5-493 dual geometry creates a recurrent local structural cost.

The global equation does not require the payment to occur at the same point as the cost.

M5-496 therefore performs a describability separation of payer location:

### Nonlocal payment

The system keeps a fixed critical enstrophy reserve at arbitrarily remote normalized scales.

### Local payment

The required stretching production repeatedly appears in the bounded region containing the recurrent dual geometry.

The ambiguity is no longer hidden inside the global scalar `Q`.

---

## 11. Highest-value next targets

### Route L — local payer

On the tight branch, combine

\[
Q_{loc}(R_*)\ge q_0
\]

with the M5-492 bridge/separator split.

The goal is to determine whether positive local axial production can repeatedly coexist with the same finite material-flux lineages without causing replacement, export, or projective flux loss.

### Route R — remote tail

On the non-tight branch, determine whether

\[
H_{tail}^{remote-E}
\]

forces one of

\[
\text{unbounded critical shell occupancy},
\quad
\text{terminal-tail strengthening},
\quad
\text{remote-source genealogy},
\]

and reconnect this to the older W1/remote-payer machinery.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
