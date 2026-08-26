# DSD M5-26 — Simultaneous Two-Hodge-Channel First-Hit Cell

Date: 2026-08-26

Status: **DERIVED UNDER THE RETAINED W1 PHASE-CELL COMPACTNESS / THE FIRST FIXED POSITIVE HIGH-AMPLITUDE EXCESS EVENT ALREADY CONTAINS BOTH A PRESSURE-COUPLED GRADIENT/DIRECTION-COMPRESSION FLOOR AND A SOLENOIDAL `k ~ L` CRITICAL FLOOR / NO SEPARATE Q-TO-P CONVERSION DELAY IS NEEDED / GLOBAL REGULARITY UNPROVED.**

## 1. Apparent gap after M5-25

M5-23 proves that first creation of a positive high-amplitude excess requires the pressure-coupled Hodge-gradient channel.

M5-25 proves that every mature positive compact defect cell has a nonzero solenoidal component.

This leaves an apparent temporal question:

\[
\text{does the defect first appear in }\mathbb QW
\text{ and only later convert into }\mathbb PW?
\]

M5-26 removes this artificial gap.

## 2. Fixed positive first-hitting class

Use the normalized high-amplitude excess

\[
W
=\left(1-\frac1{|V|}\right)_+V
\]

and its convex excess energy

\[
\mathcal G
=\frac12\|W\|_2^2.
\]

M5-23 chooses one fixed

\[
g_0>0
\]

and the first normalized time `sigma_*` satisfying

\[
\mathcal G(\sigma_*)=g_0.
\]

Therefore at that first hitting

\[
\boxed{
\|W(\sigma_*)\|_2^2=2g_0.
}
\]

The W1 Type-I envelope confines the active excess to one fixed normalized ball, independently of the physical threshold `L` along the late defect corridor.

Thus the collection of first-hitting cells with `G=g0` is itself a fixed positive compact phase-cell class of exactly the type used in M5-25.

## 3. Gradient/Hodge floor at first hitting

M5-23 gives, at the first hitting,

\[
\boxed{
\|\operatorname{div}W\|_2
=\|
\mathbf1_{\{|V|>1\}}\operatorname{div}n
\|_2
\ge d_*>0.
}
\]

Equivalently,

\[
\boxed{
\|\mathbb QW\|_{\dot H^0,\,\mathrm{high/active}}
\text{ has a fixed nontrivial Hodge-direction content.}
}
\]

The exact source identity is

\[
\mathcal G'
+\nu\mathcal D_{exc}
=\int \Pi\,\operatorname{div}W.
\]

Hence this gradient component is the pressure-coupled formation channel.

## 4. Solenoidal floor at the same first hitting

Now apply the M5-25 no-pure-gradient compactness argument not to a later mature defect class, but directly to the fixed first-hitting class

\[
\mathcal C_{g_0}
:=
\{V:\mathcal G(V)=g_0,
\text{ W1 phase-cell bounds hold}\}.
\]

Suppose no uniform solenoidal floor existed. Then there would be a sequence of first-hitting cells with

\[
\|\mathbb PW_n\|_2\to0.
\]

Compactness gives a nonzero limit `W_infty` with

\[
\mathbb PW_\infty=0.
\]

Thus `W_infty` is a pure gradient.

But its associated limit velocity `V_infty` is divergence free and

\[
V_\infty\cdot W_\infty
=|V_\infty|(|V_\infty|-1)_+>0
\]

on a set of positive measure because

\[
\|W_\infty\|_2^2=2g_0>0.
\]

On the other hand a gradient `W_infty=grad phi` gives

\[
\int V_\infty\cdot W_\infty
=0
\]

by `div V_infty=0`.

Contradiction.

Therefore there exists

\[
c_P(g_0)>0
\]

such that already at every first hitting,

\[
\boxed{
\|\mathbb PW\|_2
\ge c_P>0.
}
\]

## 5. Same-scale high-frequency solenoidal floor

As in M5-25, the original excess `W` has fixed support and a uniform `L1` bound. Therefore low frequencies of `mathbb P W` satisfy

\[
\|P_{\le q}\mathbb PW\|_2^2
\le Cq^3.
\]

Choose one fixed `q_P>0` small enough relative to the solenoidal floor. Then at the same first hitting

\[
\boxed{
\|P_{>q_P}\mathbb PW\|_2
\ge c_P'>0.
}
\]

Hence

\[
\boxed{
\|\mathbb PW\|_{\dot H^{1/2}}^2
\ge q_P(c_P')^2
=:c_H>0.
}
\]

Since `z=L(x-X_*)`, this is a physical wavenumber floor

\[
\boxed{|k|\gtrsim L}
\]

at the same formation event.

## 6. Simultaneous two-channel cell

The first-hitting defect cell therefore satisfies simultaneously

\[
\boxed{
\|\mathbf1_{\{|V|>1\}}\operatorname{div}n\|_2
\ge d_*>0
}
\]

and

\[
\boxed{
\|P_{>q_P}\mathbb PW\|_2
\ge c_P'>0.
}
\]

Thus the correct formation picture is not a delayed conversion chain

\[
\mathbb Q\to\mathbb P,
\]

but a simultaneous typed cell:

\[
\boxed{
\begin{array}{c}
\text{first fixed positive high-amplitude excess}\\
\Downarrow\\
\text{pressure-coupled direction/Hodge source}\quad(\mathbb Q)\\
+\\
\text{divergence-free critical high-frequency content}\quad(\mathbb P).
\end{array}
}
\]

The two Hodge sectors have different logical roles but occupy the same normalized scale and first-hitting event.

## 7. Physical-scale interpretation

At physical threshold `L`, the cell is localized to

\[
|u|\sim L,
\qquad
|x-X_*|\sim L^{-1},
\qquad
|k|\sim L.
\]

The `Q` channel supplies the pressure-driven amplitude-state formation.

The `P` channel supplies genuine divergence-free critical content that can be decomposed into the two helical sectors.

Hence the phase-space cell is now simultaneously localized in

- amplitude;
- physical space;
- frequency;
- Hodge type.

## 8. Remaining freedom

After M5-26, the largest unresolved internal freedom of the first-hit cell is the polarization of the solenoidal sector.

Write

\[
\widehat{\mathbb PW}
=w_+h_+ +w_-h_-.
\]

The total critical solenoidal content has a fixed floor, but M5-26 does not yet force

\[
\min\{X_+^W,X_-^W\}>0
\]

uniformly.

Therefore the next reduction should split the solenoidal content into

1. a genuinely two-helicity mixed branch; or
2. a nearly homochiral branch.

The latter must then be compared with the simultaneous direction-compression floor already forced by the `Q` channel.

This is the M5-27 target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
