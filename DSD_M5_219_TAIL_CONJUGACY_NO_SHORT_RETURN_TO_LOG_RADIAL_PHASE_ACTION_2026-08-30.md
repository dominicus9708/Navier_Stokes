# DSD M5-219 — Tail-Conjugacy No-Short-Return to Log-Radial Phase-Action Gate

Date: 2026-08-30

Status: **POSITIVE REDUCTION / AFTER M5-217 INJECTIVITY AND M5-218 CONJUGACY, THE UNIFORM CORE NO-SHORT-RETURN CONE FORCES A UNIFORM NONZERO FINITE-DIFFERENCE OF THE CANONICAL TAIL UNDER ONE FIXED LOG-RADIAL TRANSLATION / A FINITE ANNULUS CARRIES THIS DEFECT ON POSITIVE TIME DENSITY / THE DEFECT YIELDS A POSITIVE LOG-RADIAL HOMOGENEITY-DERIVATIVE ACTION / NO FINITE PHYSICAL BUDGET CONTRADICTION CLAIMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs

Let `M` be the compact minimal W1 set and

\[
\mathfrak T:M\to\mathcal T,
\qquad
\mathfrak T(V)=T_V,
\]

be the canonical-tail factor.

M5-217 closes the same-tail flat fiber, so

\[
\boxed{T_V=T_W\Longrightarrow V=W.}
\]

Together with M5-114 continuity and compactness, M5-218 therefore gives a homeomorphism

\[
\boxed{
\mathfrak T:M\overset{\cong}{\longrightarrow}\mathcal T
}
\]

conjugating the Leray flow and tail dilation flow:

\[
\boxed{
\mathfrak T(S(h)V)=D_hT_V,
}
\]

where

\[
(D_hT)(Y)=e^{-h/2}T(e^{-h/2}Y).
\]

The pure singular corridor also carries the uniform local speed floor and local second-time-derivative bound. Hence the already-audited no-short-return cone gives constants

\[
h_0>0,\qquad c_{ns}>0
\]

such that for every `V in M` and every

\[
0<h\le h_0,
\]

one has on one fixed core topology/ball

\[
\boxed{
 d_M(S(h)V,V)\ge c_{ns}h.
}
\]

For the concrete local `L2` metric one may take schematically

\[
c_{ns}=\sigma_0/2.
\]

---

## 2. Fix one finite translation step

Choose once and for all

\[
\boxed{h_*:=h_0/2>0.}
\]

Then

\[
\boxed{
 d_M(S(h_*)V,V)\ge d_*:=c_{ns}h_*>0
\qquad(V\in M).
}
\]

Since `mathfrak T^{-1}` is uniformly continuous on the compact tail space, there exists

\[
\boxed{\delta_*>0}
\]

such that

\[
d_{tail}(T_1,T_2)<\delta_*
\Longrightarrow
 d_M(\mathfrak T^{-1}T_1,\mathfrak T^{-1}T_2)<d_*.
\]

Taking the contrapositive with

\[
T_1=T_V,
\qquad
T_2=D_{h_*}T_V,
\]

gives

\[
\boxed{
 d_{tail}(D_{h_*}T,T)\ge\delta_*
\qquad(T\in\mathcal T).
}
\]

This is the first quantitative use of the newly proved tail-factor injectivity.

It says that the singular W1 survivor cannot move at positive core speed while becoming invisible in its complete canonical tail code.

---

## 3. Extract a finite annulus witness

Use the M5-114 tail metric

\[
d_{tail}(T_1,T_2)
=
\sum_{m=1}^\infty
2^{-m}
\min\left(1,
\|T_1-T_2\|_{L^3(K_m)}
\right),
\]

with a fixed annular exhaustion `K_m` of the punctured space.

Choose `N_*` so large that

\[
\sum_{m>N_*}2^{-m}<\delta_*/2.
\]

Then at every state `T in mathcal T`, at least one index

\[
1\le m\le N_*
\]

satisfies

\[
\boxed{
\|D_{h_*}T-T\|_{L^3(K_m)}
\ge c_*,
}
\]

where one may take

\[
c_*:=\min\{1,\delta_*/2\}>0.
\]

Indeed otherwise the first `N_*` terms plus the metric tail would sum to less than `delta_*`.

Thus the complete infinite-dimensional code reduces at every time to one of finitely many fixed annular witnesses.

---

## 4. Positive-density fixed-annulus selection

Along any complete minimal orbit

\[
T(s)=D_sT_0,
\]

define

\[
E_m
:=
\left\{
 s:
\|D_{h_*}T(s)-T(s)\|_{L^3(K_m)}
\ge c_*
\right\}.
\]

Then

\[
\boxed{
\bigcup_{m=1}^{N_*}E_m=\mathbb R.
}
\]

Hence on every interval `I`,

\[
|I|
\le
\sum_{m=1}^{N_*}|E_m\cap I|.
\]

By finite pigeonhole, along a sequence of arbitrarily long intervals there is at least one fixed index `m_*` such that

\[
\boxed{
\underline d_*(E_{m_*})
\ge
\frac1{N_*}>0
}
\]

in the corresponding lower-density/limsup-density sense used throughout the recurrent audit.

Thus the tail motion cannot move its finite annular witness to an ever-new observable shell at every time.

---

## 5. Exact log-radius representation

Write

\[
Y=r\theta,
\qquad
y=\log r,
\]

and represent the canonical critical tail as

\[
\boxed{
T(r\theta)=\frac1r\Phi(y,\theta).
}
\]

For

\[
\ell_*:=h_*/2,
\]

the dilation action becomes the exact translation

\[
D_{h_*}T(r\theta)
=
\frac1r\Phi(y-\ell_*,\theta).
\]

Therefore on a radial annulus corresponding to a log interval `I_m`, critical `L3` scaling gives exactly

\[
\boxed{
\|D_{h_*}T-T\|_{L^3(K_m)}^3
=
\int_{I_m\times S^2}
|\Phi(y-\ell_*,\theta)-\Phi(y,\theta)|^3
\,dy\,d\theta.
}
\]

There is no power of `r` left in this identity.

Hence on the positive-density selected set `E_{m_*}`,

\[
\boxed{
\|\Phi(\cdot-\ell_*)-\Phi\|_{L^3(I_{m_*}\times S^2)}
\ge c_*.
}
\]

---

## 6. Finite difference forces log-radial derivative action

The tail has the local spatial regularity inherited from the W1 descendant construction, so `partial_y Phi` exists in the corresponding local weak/strong class.

Use

\[
\Phi(y-\ell_*)-\Phi(y)
=-\int_0^{\ell_*}
\partial_y\Phi(y-a)\,da.
\]

Minkowski followed by Holder in `a` gives

\[
\begin{aligned}
\|\Phi(\cdot-\ell_*)-\Phi\|_{L^3(I\times S^2)}
&\le
\int_0^{\ell_*}
\|\partial_y\Phi(\cdot-a)\|_{L^3(I\times S^2)}da\\
&\le
\ell_*^{2/3}
\left(
\int_0^{\ell_*}
\|\partial_y\Phi(\cdot-a)\|_{L^3(I\times S^2)}^3da
\right)^{1/3}.
\end{aligned}
\]

Therefore every annular finite-difference witness obeys

\[
\boxed{
\int_0^{\ell_*}
\|\partial_y\Phi(\cdot-a)\|_{L^3(I_{m_*}\times S^2)}^3da
\ge
\frac{c_*^3}{\ell_*^2}.
}
\]

Equivalently, on a slightly enlarged fixed log cylinder `I_{m_*}^{+}`,

\[
\boxed{
\int_{I_{m_*}^{+}\times S^2}
|\partial_y\Phi|^3
\,dy\,d\theta
\ge c_{ph}>0
}
\]

for a fixed positive constant after the corresponding translated observation is made.

---

## 7. The derivative is exactly the spatial homogeneity defect

For

\[
T(r\theta)=r^{-1}\Phi(\log r,\theta),
\]

one has

\[
r\partial_rT
=
\frac1r(-\Phi+\partial_y\Phi).
\]

Hence

\[
\boxed{
T+(Y\cdot\nabla)T
=
\frac1r\partial_y\Phi.
}
\]

Define

\[
\boxed{
\mathcal H_T
:=
T+(Y\cdot\nabla)T.
}
\]

Then the log-cylinder identity becomes

\[
\boxed{
\int_{A_R}|\mathcal H_T|^3dY
=
\int_{\log A_R\times S^2}
|\partial_y\Phi|^3dy\,d\theta.
}
\]

Thus the aperiodic/minimal W1 motion necessarily carries a genuine scale-critical **tail homogeneity-defect action**.

This is not a finite-dimensional descriptor. It is the exact tangent direction of the complete tail code.

---

## 8. Relation to tail-time speed

The passive tail equation is

\[
T_s+rac12T+rac12Y\cdot\nabla T=0.
\]

Therefore

\[
\boxed{
T_s=-\frac12\mathcal H_T.
}
\]

So the new payer may equivalently be written as tail-time motion:

\[
\boxed{
\|T_s\|_{L^3(A_R)}^3
=
\frac18
\|\mathcal H_T\|_{L^3(A_R)}^3.
}
\]

The W1 core-speed problem has therefore been converted, through injective conjugacy, into a spatial log-radial critical action of the passive tail.

---

## 9. What is new and what is not yet closed

### PROVED

\[
\boxed{
\text{uniform core no-short-return}
\Longrightarrow
\text{uniform tail finite-translation separation}
}
\]

and, after finite annulus extraction,

\[
\boxed{
\text{positive-density critical log-radial homogeneity-defect action}.
}
\]

### NOT PROVED

The quantity

\[
\int|\mathcal H_T|^3
\]

is not currently known to be controlled by a finite physical-energy or dissipation budget.

In particular, a critical cascade may pay one fixed dimensionless log-radial action per generation while its dimensional physical cost shrinks geometrically.

Therefore this note does not declare the aperiodic hull impossible.

---

## 10. Updated frontier

After M5-217--M5-219 the infinite-dimensional shape survivor has a much sharper form:

\[
\boxed{
A_{min}^{aper}
\Longrightarrow
\text{positive-density nonzero }
\mathcal H_T
=T+Y\cdot\nabla T
\text{ in critical }L^3\text{ on fixed log cells}.
}
\]

The next audit should determine whether this tail homogeneity-defect action

1. forces a nonzero critical tail residual
   \[
   F_T=\nu\Delta T-\mathbb P\nabla\cdot(T\otimes T),
   \]
   which must be paid by the finite-energy quotient; or
2. can remain large while `F_T` is small/zero, in which case stationary singular-tail solutions form a new rigidity subclass.

No implication between these two possibilities is assumed here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]