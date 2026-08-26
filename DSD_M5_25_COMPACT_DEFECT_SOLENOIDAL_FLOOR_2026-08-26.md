# DSD M5-25 — Compact-Defect Solenoidal Floor

Date: 2026-08-26

Status: **DERIVED UNDER THE RETAINED W1 PHASE-CELL COMPACTNESS / A NONTRIVIAL HIGH-AMPLITUDE EXCESS CANNOT APPROACH A PURE HODGE-GRADIENT STATE / THE COMPACT DEFECT CLASS HAS A UNIFORM SOLENOIDAL `k ~ L` FLOOR / COMBINED WITH M5-23, DEFECT FORMATION REQUIRES BOTH A PRESSURE-COUPLED GRADIENT SOURCE AND A MATURE SOLENOIDAL CRITICAL COMPONENT / GLOBAL REGULARITY UNPROVED.**

## 1. Question left by M5-22--24

M5-22 gives a Hodge split of the normalized high-amplitude excess

\[
W
=\left(1-\frac1{|V|}\right)_+V
=\mathbb PW+\mathbb QW.
\]

M5-23 then shows that at first creation of a fixed positive excess, the pressure-coupled gradient branch `mathbb Q W` is mandatory.

A remaining possibility is that a mature defect could stay arbitrarily close to a pure gradient state, with its solenoidal component tending to zero.

M5-25 excludes that possibility on the retained compact W1 defect class.

## 2. Defect-cell compactness used here

The W1 tail construction already retains fixed-cell local compactness/analyticity and a uniform Type-I envelope. M5-21 turns a positive `K` defect into a fixed normalized phase cell:

\[
K\ge\delta>0
\]

implies that the active excess is supported in one fixed `z`-ball and carries a fixed `L2` floor.

Accordingly consider a defect sequence `(V_n,W_n)` satisfying

\[
\nabla\cdot V_n=0,
\]

\[
W_n=\mathcal T(V_n)
=\left(1-\frac1{|V_n|}\right)_+V_n,
\]

\[
\|W_n\|_2\ge c_W(\delta)>0,
\]

with uniform active support and the retained W1 local compactness.

After passing to a subsequence,

\[
V_n\to V_\infty
\]

locally strongly on the active phase cell and

\[
W_n\to W_\infty
\]

strongly in `L2` on the fixed support.

The Lipschitz truncation is continuous under this convergence, so

\[
\boxed{
W_\infty
=\left(1-\frac1{|V_\infty|}\right)_+V_\infty.
}
\]

Also

\[
\nabla\cdot V_\infty=0
\]

distributionally, and

\[
\|W_\infty\|_2\ge c_W>0.
\]

## 3. No-pure-gradient lemma

Assume for contradiction that the solenoidal component can vanish along a defect sequence:

\[
\|\mathbb PW_n\|_2\to0.
\]

The Leray projector is bounded on `L2`, hence strong convergence gives

\[
\mathbb PW_\infty=0.
\]

Therefore

\[
W_\infty=\mathbb QW_\infty
\]

is a gradient field. Write

\[
W_\infty=\nabla\phi
\]

in the weak Hodge sense. Because `W_infty` is compactly supported in the fixed active ball, the potential may be chosen constant at infinity, and the pairing below is legitimate by approximation.

Since `V_infty` is divergence free,

\[
\int V_\infty\cdot W_\infty dz
=
\int V_\infty\cdot\nabla\phi dz
=0.
\]

But the amplitude truncation is pointwise parallel to `V_infty`:

\[
V_\infty\cdot W_\infty
=
|V_\infty|(|V_\infty|-1)_+.
\]

Thus

\[
\int V_\infty\cdot W_\infty dz
=
\int_{|V_\infty|>1}
|V_\infty|(|V_\infty|-1)dz.
\]

The integrand is nonnegative and vanishes only where the excess vanishes. Since

\[
\|W_\infty\|_2>0,
\]

this integral is strictly positive.

Contradiction.

Therefore no nontrivial compact W1 defect cell can be purely gradient.

## 4. Uniform solenoidal floor by compactness

The preceding contradiction is qualitative for one limit. Compactness upgrades it to a quantitative floor.

If no uniform constant existed, one could choose a sequence of defect cells with

\[
\|\mathbb PW_n\|_2\downarrow0,
\]

and the compactness argument would produce the forbidden pure-gradient nonzero limit.

Hence there exists

\[
c_{sol}=c_{sol}(\delta,\text{W1 cell constants})>0
\]

such that every cell in the compact positive-defect class satisfies

\[
\boxed{
\|\mathbb PW\|_2
\ge c_{sol}>0.
}
\]

This collapses the static M5-22 dichotomy further: a positive mature defect always contains a nontrivial solenoidal component.

## 5. Upgrade to an order-one frequency floor

Although `mathbb P W` is nonlocal and need not be compactly supported, its Fourier transform obeys

\[
|\widehat{\mathbb PW}(q)|
\le
|\widehat W(q)|
\le
\|W\|_1.
\]

The defect class has fixed support and uniform `L2` control for `W`, hence

\[
\|W\|_1\le C_*.
\]

Therefore for a low-frequency ball

\[
\|P_{\le q}\mathbb PW\|_2^2
\le
C q^3C_*^2.
\]

Choose a fixed `q_sol>0` such that

\[
Cq_{sol}^3C_*^2
\le
\frac14c_{sol}^2.
\]

Then

\[
\boxed{
\|P_{>q_{sol}}\mathbb PW\|_2
\ge
\frac12c_{sol}>0.
}
\]

Thus the solenoidal component is not merely nonzero; it carries an order-one normalized frequency floor.

In physical variables this again corresponds to

\[
\boxed{|k|\gtrsim L.}
\]

## 6. Critical Sobolev/helical consequence

Because the solenoidal high-frequency component lies above `q_sol`,

\[
\|\mathbb PW\|_{\dot H^{1/2}}^2
\ge
q_{sol}
\|P_{>q_{sol}}\mathbb PW\|_2^2.
\]

Hence

\[
\boxed{
\|\mathbb PW\|_{\dot H^{1/2}}^2
\ge c_{H}>0.
}
\]

The helical split

\[
\widehat{\mathbb PW}
=w_+h_+ +w_-h_-
\]

therefore has

\[
\int |q|(|w_+|^2+|w_-|^2)dq
\ge c_H.
\]

At least one helical sector carries a critical floor. M5-25 alone does not yet force a minority-helicity floor for the excess.

## 7. Formation-cell synthesis with M5-23

M5-23 proves

\[
\boxed{
\text{first creation of positive excess}
\Longrightarrow
\|\mathbb QW\|_{\text{direction/Hodge channel}}
\ge c_Q>0.
}
\]

M5-25 proves

\[
\boxed{
\text{every mature positive defect cell}
\Longrightarrow
\|\mathbb PW\|_{\text{critical solenoidal channel}}
\ge c_P>0.
}
\]

Thus a surviving W1 high-amplitude defect cannot be described by only one Hodge sector.

The DSD formation cell has the structure

\[
\boxed{
\text{pressure-coupled gradient/Hodge source}
\quad\longrightarrow\quad
\text{positive high-amplitude excess}
\quad\longrightarrow\quad
\text{solenoidal critical content at }k\sim L.
}
\]

The arrow denotes a logical formation requirement, not yet a proved monotone temporal conversion law.

## 8. Why this is stronger than a generic Hodge split

For an arbitrary vector field, one Hodge component may be arbitrarily small.

The positive lower bound here uses three W1-specific facts simultaneously:

1. the excess is pointwise parallel to a divergence-free velocity;
2. the positive `K` defect prevents the excess from vanishing;
3. the defect class is compact after phase-space normalization.

Without compactness, the contradiction for one pure-gradient limit would not automatically yield a uniform floor.

## 9. Remaining gap

M5-25 does not yet show that the first-hitting gradient floor and the mature solenoidal floor occur at the same instant or that their conversion has an extra non-reusable physical cost.

It also does not yet transfer the helical sector structure of `mathbb P W` into a quantitative two-helicity floor for the original Navier--Stokes velocity.

Thus the next question is:

\[
\boxed{
\text{what dynamics converts the mandatory first-hitting }\mathbb QW
\text{ source into the mandatory mature }\mathbb PW
\text{ content?}
}
\]

A useful answer must either

- force a two-helicity critical transfer at the same phase-space scale, or
- produce an additional critical action that cannot be reused across all nested thresholds.

This is the M5-26 target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
