# DSD M19-082 — Uniform two-sided center-norm nondegeneration upgrades remote damping to an explicit fixed-window core observability and hence finite dimension

**Date:** 2026-09-12  
**Status:** CONDITIONAL TEMPORAL-BRIDGE CLOSURE / THE M19-079 TO M19-080 GAP CLOSES UNDER A UNIFORM TWO-SIDED CENTER BOUND WITH AN EXPLICIT OBSERVATION WINDOW / SYMMETRY MODES SATISFY THE REQUIRED NONDEGENERATION ON A NONSTATIONARY COMPACT MINIMAL COMPONENT OF CONSTANT SYMMETRY RANK / GLOBAL REGULARITY REMAINS UNPROVED

## 1. Starting inequality

M19-079 established, on the quiet weak-critical spectator branch and for a sufficiently large finite core \(B_R\),

\[
\boxed{
\frac12E'(\theta)
+c_*E_o(\theta)
\le
K_RE_c(\theta),
}
\tag{1}
\]

where

\[
E=E_c+E_o,
\qquad
c_*>0,
\qquad
K_R<\infty.
\]

Equivalently,

\[
\boxed{
\frac12E'
+c_*E
\le
(K_R+c_*)E_c.
}
\tag{2}
\]

M19-081 showed that long-time recurrence alone does not turn this into a fixed-window observation estimate.

The present module identifies one sufficient dynamical property that does.

## 2. Uniform two-sided center nondegeneration

Assume that a linear invariant center family \(\mathcal C\) satisfies

\[
\boxed{
 m\|W(s)\|_X
\le
\|W(t)\|_X
\le
M\|W(s)\|_X
\qquad
\forall s,t\in\mathbb R,
\quad
W\in\mathcal C,
}
\tag{UC}
\]

for constants

\[
0<m\le1\le M<\infty.
\]

Since

\[
E(\theta)=\|W(\theta)\|_X^2,
\]

this gives

\[
\boxed{
 m^2E(s)
\le
E(t)
\le
M^2E(s).
}
\tag{3}
\]

Write

\[
\mu:=m^2>0.
\]

The key input is the lower bound in (3): a true center vector cannot become arbitrarily small for arbitrarily long times and later recover while remaining inside this uniformly nondegenerate center family.

## 3. Integrate the remote damping inequality on one arbitrary window

Integrate (2) from \(s\) to \(s+T\):

\[
\frac12\bigl(E(s+T)-E(s)\bigr)
+c_*\int_s^{s+T}E(t)dt
\le
(K_R+c_*)
\int_s^{s+T}E_c(t)dt.
\]

Rearrange:

\[
\boxed{
(K_R+c_*)
\int_s^{s+T}E_c(t)dt
\ge
c_*\int_s^{s+T}E(t)dt
-\frac12E(s).
}
\tag{4}
\]

Here we used only

\[
E(s+T)\ge0.
\]

By (3),

\[
\int_s^{s+T}E(t)dt
\ge
\mu T E(s).
\]

Therefore

\[
\boxed{
\int_s^{s+T}E_c(t)dt
\ge
\frac{c_*\mu T-1/2}{K_R+c_*}
E(s).
}
\tag{5}
\]

This is positive as soon as

\[
\boxed{
T>rac1{2c_*\mu}.
}
\tag{6}
\]

## 4. Explicit observation window

Choose the convenient value

\[
\boxed{
T_*
:=
\frac1{c_*m^2}.
}
\tag{7}
\]

Then

\[
c_*m^2T_*=1,
\]

and (5) becomes

\[
\boxed{
\int_s^{s+T_*}E_c(t)dt
\ge
\frac1{2(K_R+c_*)}E(s).
}
\tag{8}
\]

Equivalently,

\[
\boxed{
E(s)
\le
2(K_R+c_*)
\int_s^{s+T_*}E_c(t)dt.
}
\tag{9}
\]

Thus every time interval of one fixed length \(T_*\) observes the center vector quantitatively in the finite core.

The return-gap issue of M19-081 disappears because long remote-only intervals would force genuine norm decay, prohibited by (UC).

## 5. Centered-window observability

To match M19-080, put

\[
s=-T_*/2.
\]

Then (9) gives

\[
E(-T_*/2)
\le
2(K_R+c_*)
\int_{-T_*/2}^{T_*/2}E_c(t)dt.
\]

By the upper half of (UC),

\[
E(0)
\le
M^2E(-T_*/2).
\]

Hence

\[
\boxed{
E(0)
\le
C_{obs}
\int_{-T_*/2}^{T_*/2}E_c(t)dt,
}
\tag{10}
\]

with the explicit constant

\[
\boxed{
C_{obs}
:=
2M^2(K_R+c_*).
}
\tag{11}
\]

Therefore the exact M19-080 hypothesis (OBS) is obtained.

## 6. Immediate finite-dimensionality consequence

M19-080 proves that fixed-window finite-core observability plus local parabolic compactness implies

\[
\boxed{
\dim\mathcal C<\infty.
}
\]

Combining M19-079, M19-080 and M19-082 yields the conditional chain

\[
\boxed{
\begin{aligned}
&\text{quiet weak-critical spectator decay}\\
&+\text{pressure-compatible }A_2\text{ gap}\\
&+\text{uniform two-sided center nondegeneration (UC)}
\end{aligned}
\Longrightarrow
\text{fixed-window core observability}
\Longrightarrow
\dim\mathcal C<\infty.
}
\]

This is stronger than the former global-compactness shortcut and avoids the remote-packet counterexample of M19-077.

## 7. Why (UC) is stronger than zero Lyapunov exponent

A zero Lyapunov exponent only states

\[
\limsup_{|t|\to\infty}
\frac1{|t|}
\log\frac{\|W(t)\|}{\|W(0)\|}=0.
\]

It permits:

- polynomial growth;
- polynomial decay;
- arbitrarily deep subexponential excursions;
- long intervals of strong decay followed by compensating growth.

By contrast, (UC) requires

\[
\boxed{
\frac{\|W(t)\|}{\|W(s)\|}
\in[m,M]
\quad\text{uniformly for all }s,t.
}
\]

Therefore

\[
\boxed{
\lambda=0
\not\Rightarrow
(UC).
}
\]

The condition is a genuine additional center-bundle rigidity statement.

## 8. Symmetry modes on a compact minimal recurrent component

The symmetry-generated modes from M19-075 provide an important calibration.

### 8.1 Time tangent

Let

\[
Z_t(Y)=\partial_\theta U_Y|_{\theta=0}.
\]

This is a continuous function of the state in a topology controlling the equation's vector field.

If a compact minimal invariant component \(\mathcal M\) is nonstationary, it contains no equilibrium state. If it contained an equilibrium, the singleton equilibrium orbit would be a nonempty closed invariant subset of \(\mathcal M\), contradicting minimality unless \(\mathcal M\) itself were that singleton.

Hence

\[
\|Z_t(Y)\|_X>0
\qquad
\forall Y\in\mathcal M.
\]

By compactness and continuity,

\[
\boxed{
0<m_t
\le
\|Z_t(Y)\|_X
\le
M_t<\infty
\qquad
Y\in\mathcal M.
}
\]

Thus the time-symmetry mode is uniformly nondegenerate on a nonstationary compact minimal component.

### 8.2 Rotation tangents

For fixed \(A\in\mathfrak{so}(3)\),

\[
Z_A(Y)=AU-(Ay)\cdot\nabla U.
\]

If \(Z_A(Y_*)=0\), then \(Y_*\) is invariant under the one-parameter rotation subgroup generated by \(A\).

Because the Navier--Stokes flow commutes with rotations, the set of states invariant under that subgroup is closed and flow-invariant.

On a minimal component, if this set is nonempty then it is the whole component.

Therefore, for a generator \(A\) which acts nontrivially on a minimal component,

\[
\boxed{
\inf_{Y\in\mathcal M}\|Z_A(Y)\|_X>0.
}
\]

The corresponding symmetry direction satisfies an individual form of (UC).

### 8.3 Full rotation bundle

If the rotational stabilizer dimension is constant on \(\mathcal M\), the nonzero symmetry tangent bundle has constant finite rank.

The Gram matrix of a continuous symmetry basis varies continuously on compact \(\mathcal M\). After quotienting the stabilizer, its smallest singular value has a positive minimum.

Hence the entire finite-dimensional symmetry bundle

\[
\boxed{
E^c_{sym}
}
\]

is uniformly norm-equivalent along the minimal component and satisfies (UC) with finite constants.

Thus (UC) is not artificial for the **known** center directions.

## 9. The real open issue

The question is whether every additional bounded center direction, if one exists, must also obey uniform two-sided nondegeneration.

At present there is no certified reason for this.

An extra center mode could in principle have

\[
\inf_t\|W(t)\|_X=0
\]

while remaining bounded and having zero exponential rate.

Such a direction would evade M19-082 exactly through deep subexponential norm excursions.

Therefore the center problem has sharpened to

\[
\boxed{
\text{extra center}
\Longrightarrow
\text{uniformly nondegenerate finite-dimensional mode}
\quad\lor\quad
\text{deep norm-degeneration mode}.
}
\]

The first branch is finite-dimensional by the present theorem.

The second is now the genuine surviving temporal-center escape.

## 10. Updated center branch tree

Within the quiet weak-critical scattering corridor:

\[
\boxed{
\mathcal C_{neutral}
\Longrightarrow
\begin{cases}
\mathcal C_{sym},\\
\mathcal C_{extra}^{UC}
\;\Rightarrow\;
\text{finite-dimensional observable center},\\
\mathcal C_{extra}^{deg}
:\ \inf_t\|W(t)\|/\|W(0)\|=0.
\end{cases}
}
\]

The last branch is compatible with zero Lyapunov exponent and is not closed here.

## 11. What is certified

M19-082 certifies:

1. under (UC), the remote damping inequality yields an explicit window length
   \[
   T_*=\frac1{c_*m^2};
   \]
2. the corresponding observability constant can be taken as
   \[
   C_{obs}=2M^2(K_R+c_*);
   \]
3. M19-080 then forces finite-dimensionality;
4. the known time/rotation symmetry bundle satisfies uniform nondegeneration on a compact nonstationary minimal component of constant symmetry rank.

## 12. What remains unproved

M19-082 does not prove:

1. (UC) for every bounded center direction;
2. absence of deep norm-degeneration neutral modes;
3. equality of the center with the symmetry bundle;
4. exclusion of relative-periodic screw states;
5. exclusion of aperiodic scattering factors;
6. global regularity.

## 13. Next target

The surviving branch has a precise signature:

\[
\boxed{
\exists W\neq0,
\qquad
\sup_t\|W(t)\|_X<\infty,
\qquad
\inf_t\|W(t)\|_X=0,
\qquad
\lambda(W)=0.
}
\]

The next calculation should test whether a bounded complete parabolic solution with arbitrarily deep norm minima can recover to order-one size without paying a quantitatively large core strain/pressure amplification integral.

If each recovery carries a positive action cost, recurrence of infinitely many deep minima may reconnect the center problem to an additive core payer rather than to compactness.

---

\[
\boxed{\text{M19-082 COMPLETE.}}
\]
