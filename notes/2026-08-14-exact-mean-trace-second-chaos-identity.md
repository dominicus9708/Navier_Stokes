# Exact mean-trace versus second-chaos identity for the quadratic vorticity core

Date: 2026-08-14

Status: **EXACT FINITE-DIMENSIONAL IDENTITY AND EXPLICIT COERCIVE DICHOTOMY / NO GLOBAL CLOSURE CLAIM**.

This note gives an explicit quantitative statement that does not require extracting a full Groebner coercivity certificate.

## 1. Setup

In whitened Gaussian coordinates let

\[
w=Q-b,
\qquad
Q_i(z)=\frac12T_{i,jk}z_jz_k,
\qquad
b=E_\gamma Q,
\]

with `div Q=0`.

Let

\[
\eta=\nabla\times Q=Az.
\]

Define the homogeneous quadratic bracket

\[
P=(Az\cdot\nabla)Q-AQ.
\]

Since `w=Q-b` and `grad eta=A`, the genuine residual-residual vorticity source is

\[
N_\omega
=(\eta\cdot\nabla)w-(w\cdot\nabla)\eta
=P+Ab.
\]

Write its Hermite decomposition as

\[
N_\omega=J+N_{\omega,2},
\qquad
J=E_\gamma N_\omega.
\]

## 2. Exact mean identity

Because `P` is homogeneous quadratic,

\[
E_\gamma P=\frac12\Delta P.
\]

Therefore

\[
\boxed{
J
=E_\gamma P+Ab
=\frac12\Delta P+Ab.
}
\]

The centered second-chaos source is

\[
\boxed{
N_{\omega,2}
=P-E_\gamma P.
}
\]

Thus the part of the mean source not carried by the constant-shift term `Ab` is literally the Euclidean trace of the same quadratic coefficient tensor that generates the second Hermite chaos.

## 3. Exact identity for b

The divergence-free vector identity gives

\[
\Delta Q
=-\nabla\times(\nabla\times Q)
=-\nabla\times(Az).
\]

Hence

\[
\boxed{
b=-\frac12c,
\qquad
c:=\nabla\times(Az).
}
\]

Therefore

\[
Ab=-\frac12Ac.
\]

## 4. Trace is controlled by the centered second chaos

Write each component of `P` as

\[
P_i(z)=z^TM_i z,
\]

with `M_i` symmetric.

Then

\[
E_\gamma P_i=\operatorname{tr}M_i,
\]

and

\[
\|P_i-E_\gamma P_i\|_{L^2(\gamma)}^2
=2\|M_i\|_F^2.
\]

Since

\[
|\operatorname{tr}M_i|^2
\le3\|M_i\|_F^2,
\]

summing components gives

\[
\boxed{
|E_\gamma P|
\le
\sqrt{\frac32}\,
\|N_{\omega,2}\|_{L^2(\gamma)}.
}
\]

Also

\[
|c|^2
=2\|\operatorname{skew}A\|_F^2
\le2\|A\|_F^2.
\]

Hence

\[
|Ab|
\le
\frac1{\sqrt2}\|A\|_F^2.
\]

Since

\[
V_\omega=\|Az\|_{L^2(\gamma)}^2=\|A\|_F^2,
\]

we obtain

\[
\boxed{
|Ab|
\le
\frac1{\sqrt2}V_\omega.
}
\]

## 5. Explicit mean-to-second-chaos dichotomy

Combining the exact mean identity with the two bounds,

\[
\boxed{
|J|
\le
\sqrt{\frac32}\,
\|N_{\omega,2}\|_2
+
\frac1{\sqrt2}V_\omega.
}
\]

Equivalently,

\[
\boxed{
\|N_{\omega,2}\|_2
\ge
\sqrt{\frac23}
\left(
|J|-\frac1{\sqrt2}V_\omega
\right)_+.
}
\]

This is a completely explicit quantitative replacement for part of the previously conjectured finite-dimensional coercivity.

## 6. Insert source efficiency and vorticity share

Let

\[
B=\mathcal B_\gamma,
\qquad
\Theta=\frac{V_\omega}{B},
\]

and define the pointwise source efficiency

\[
\mathcal E
:=
\frac{|J|}{\sqrt{BV_\omega}}
=
\frac{|J|}{B\sqrt\Theta}.
\]

Then

\[
|J|=\mathcal E B\sqrt\Theta,
\qquad
V_\omega=\Theta B.
\]

Therefore

\[
\boxed{
\|N_{\omega,2}\|_2
\ge
\sqrt{\frac23}\,
B\sqrt\Theta
\left(
\mathcal E-rac1{\sqrt2}\sqrt\Theta
\right)_+.
}
\]

In particular, whenever

\[
\boxed{
\mathcal E\ge C_0\sqrt\Theta
}
\]

for any fixed `C0>1/sqrt(2)`, the second-chaos source is comparable to the mean-source scale:

\[
\boxed{
\|N_{\omega,2}\|_2
\gtrsim_{C_0}
\mathcal E B\sqrt\Theta.
}
\]

Thus a source-efficient quadratic core cannot create mean vorticity without producing a quantitatively comparable degree-two vorticity source.

## 7. Complementary low-efficiency relative to vorticity branch

If instead

\[
\mathcal E\lesssim\sqrt\Theta,
\]

the source-efficiency dissipation lemma gives a stronger survival condition.

Recall

\[
H=\Lambda\Theta^{5/6},
\qquad
\mathcal E H^{3/5}\to\infty.
\]

Using `E <= C sqrt(Theta)`, a surviving sequence must satisfy

\[
\sqrt\Theta H^{3/5}\to\infty.
\]

But

\[
\sqrt\Theta H^{3/5}
=
\Lambda^{3/5}\Theta.
\]

Hence the complementary branch obeys

\[
\boxed{
\Lambda^{3/5}\Theta\to\infty.
}
\]

So the quadratic-core source is now split into two quantitatively typed alternatives:

### A. Efficient relative to vorticity share

\[
\mathcal E\gg\sqrt\Theta.
\]

Then an order-comparable second-chaos vorticity source is forced.

### B. Inefficient relative to vorticity share

\[
\mathcal E\lesssim\sqrt\Theta.
\]

Then survival requires the stronger vorticity-share growth

\[
\Lambda^{3/5}\Theta\to\infty.
\]

## 8. Curl-free boundary case

When `A -> 0`, the quadratic core tends to a curl-free divergence-free field `Q0=grad h` with `h` harmonic cubic. Then `b=0` and the exact identity reduces to

\[
\boxed{
J=\frac12\Delta P.
}
\]

Therefore

\[
P=0\Longrightarrow J=0
\]

without any computer algebra. This closes the linearized boundary case needed for compactness arguments at vanishing vorticity.

## 9. Relation to the exact Groebner zero-set lemma

The explicit trace estimate does not subsume the stronger exact statement

\[
N_{\omega,2}=0\Longrightarrow J=0.
\]

Indeed the trace estimate alone leaves the `Ab` term. The Groebner zero-set calculation proves that when the entire second-chaos source vanishes, the self-consistency conditions force `Ac=0` as well.

The two results are complementary:

- the trace identity gives explicit quantitative control when the mean source dominates `V_omega`;
- the Groebner lemma removes the exact mean-only zero set even when `Ab` is important.

Status: **EXPLICIT EFFICIENT-SOURCE COERCIVITY PROVED / COMPLEMENTARY BRANCH FORCED TO `Lambda^(3/5) Theta -> infinity` / NEXT TARGET = PRICE THE FORCED SECOND-CHAOS SOURCE OR THE ENHANCED VORTICITY-SHARE BRANCH.**
