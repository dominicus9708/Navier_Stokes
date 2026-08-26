# DSD M5-21 — W1 Phase-Space Linear Frequency Bridge

Date: 2026-08-26

Status: **DERIVED W1-SPECIFIC PHASE-SPACE LOCALIZATION LEMMA / POSITIVE `K` DEFECT FORCES ORDER-ONE FREQUENCY CONTENT IN THE RESCALED HIGH-AMPLITUDE EXCESS FIELD / THIS IS A LINEAR `k ~ L` SCALE MATCH FOR THE EXCESS FIELD, NOT YET FOR THE FULL VELOCITY FOURIER TAIL / GLOBAL REGULARITY UNPROVED.**

## 1. Physical threshold rescaling

Fix a physical velocity threshold `L>0` and a candidate singular point `X_*`.

Define the scale-normalized spatial variable and normalized velocity

\[
z=L(x-X_*),
\qquad
V_L(z,t)=L^{-1}u(X_*+z/L,t).
\]

Then

\[
dz=L^3dx,
\]

and the physical truncated critical tail

\[
K_L^{phys}(t)
:=
\frac L2\int (|u|^2-L^2)_+dx
\]

becomes exactly

\[
\boxed{
K_L^{phys}(t)
=
\frac12\int_{
\mathbb R^3}
(|V_L(z,t)|^2-1)_+dz.
}
\]

Thus the velocity threshold is normalized to amplitude `1`, while the natural physical length scale `L^{-1}` becomes order one in `z`.

## 2. Relation to the W1 Leray tail

If

\[
\lambda=L\sqrt{T_*-t},
\]

and

\[
U(Y,s)=\sqrt{T_*-t}\,u(x,t),
\qquad
Y=\frac{x-X_*}{\sqrt{T_*-t}},
\]

then

\[
z=\lambda Y,
\qquad
V_L(z,t)=\lambda^{-1}U(z/\lambda,s).
\]

Hence this is exactly the joint blow-down used to resolve the projective boundary

\[
\lambda|Y|\sim1.
\]

Assume the retained W1 corridor has the uniform far-field Type-I envelope

\[
|U(Y,s)|\le \frac{A_0}{|Y|}
\qquad
(|Y|\ge R_0).
\]

Then for

\[
|z|\ge \lambda R_0,
\]

\[
\boxed{
|V_L(z,t)|
\le
\frac{A_0}{|z|}.
}
\]

## 3. Positive `K` defect localizes in a fixed `z`-annulus

Suppose along a defect sequence

\[
\lambda_n\downarrow0,
\qquad
K_{L_n}^{phys}(t_n)\ge\delta>0.
\]

Write

\[
V_n(z)=V_{L_n}(z,t_n).
\]

### Core contribution

On

\[
|z|\le \lambda_nR_0,
\]

change variables back to `Y`:

\[
\int_{|z|\le \lambda_nR_0}|V_n|^2dz
=
\lambda_n
\int_{|Y|\le R_0}|U(Y,s_n)|^2dY.
\]

The compact W1 core has a uniform local `L2` bound, so this is

\[
O(\lambda_n)\to0.
\]

Hence the fixed positive defect cannot be paid by the finite Leray core after the `z=lambda Y` blow-down.

### Small-`z` tail contribution

For

\[
\lambda_nR_0<|z|<\varepsilon,
\]

the Type-I envelope gives

\[
(|V_n|^2-1)_+
\le
\frac{A_0^2}{|z|^2}.
\]

Therefore

\[
\int_{\lambda_nR_0<|z|<\varepsilon}
(|V_n|^2-1)_+dz
\le
C A_0^2\varepsilon.
\]

Thus this contribution can be made uniformly small by choosing `epsilon` small.

### Large-`z` region

If

\[
|z|>A_0,
\]

then the Type-I envelope gives

\[
|V_n(z)|<1,
\]

for all sufficiently large `n` in the tail region, so the truncated integrand vanishes there.

Consequently there exist fixed

\[
0<\varepsilon_*<R_*<\infty
\]

depending only on the W1 constants and `delta`, such that for all sufficiently large `n`,

\[
\boxed{
\frac12
\int_{\varepsilon_*<|z|<R_*}
(|V_n|^2-1)_+dz
\ge
\frac\delta2.
}
\]

This is a genuine phase-space localization of the `K` defect.

## 4. Natural high-amplitude excess field

Define the radial Lipschitz truncation

\[
\mathcal T(v)
:=
\left(1-\frac1{|v|}\right)_+v,
\]

with `T(0)=0`, and set

\[
W_n(z):=\mathcal T(V_n(z)).
\]

Then

\[
|W_n|=(|V_n|-1)_+.
\]

No artificial spatial cutoff is introduced: `W_n` is supported exactly where the normalized velocity exceeds the physical threshold.

The far Type-I envelope implies

\[
\operatorname{supp}W_n
\subset B_{R_*}
\]

for a fixed `R_*` once `n` is large.

On the fixed annulus carrying at least `delta/2` of the truncated mass, the Type-I bound also provides a uniform amplitude ceiling

\[
|V_n|\le M_*
\]

with

\[
M_*<\infty.
\]

Since

\[
|V_n|^2-1
=(|V_n|-1)(|V_n|+1),
\]

we obtain

\[
\int (|V_n|-1)_+dz
\ge
c(\delta,M_*)>0.
\]

Because the active region lies in a fixed finite-volume ball, Cauchy--Schwarz gives

\[
\boxed{
\|W_n\|_2
\ge
c_W(\delta,A_0,R_0)>0.
}
\]

## 5. Fixed rescaled frequency floor

Because `W_n` has uniformly bounded support,

\[
\|W_n\|_1
\le
|B_{R_*}|^{1/2}\|W_n\|_2.
\]

For a Fourier cutoff `P_{<=q}`, Plancherel and

\[
\|\widehat W_n\|_\infty\le \|W_n\|_1
\]

give

\[
\|P_{\le q}W_n\|_2^2
\le
C q^3 R_*^3\|W_n\|_2^2.
\]

Choose a fixed

\[
q_*=q_*(R_*)>0
\]

so small that

\[
Cq_*^3R_*^3\le\frac14.
\]

Then

\[
\boxed{
\|P_{>q_*}W_n\|_2^2
\ge
\frac34\|W_n\|_2^2
\ge
c_*>0.
}
\]

Thus the normalized high-amplitude excess carries a fixed amount of frequency above one fixed order-one `z`-wavenumber.

## 6. Return to physical frequency

Since

\[
z=L_n(x-X_*),
\]

one unit of `z`-frequency corresponds to physical frequency of order `L_n`.

Therefore the previous estimate is the phase-space statement

\[
\boxed{
K_{L_n}^{phys}(t_n)\ge\delta
\Longrightarrow
\text{the normalized excess field has nontrivial spectral content at }
|k|\gtrsim L_n.
}
\]

This is the W1-specific linear amplitude--frequency scale match

\[
\boxed{L\longleftrightarrow k\sim L}
\]

for the **high-amplitude excess observable**.

It is stronger in scale than the generic energy/Bernstein bridge

\[
L\longmapsto \kappa_L\sim L^{2/3},
\]

because it uses the additional W1 projective localization and `1/r` tail envelope.

## 7. Important audit boundary

This result does **not** yet prove

\[
\|P_{>cL}u(t)\|_2^2\ge c/L
\]

for the full velocity itself.

The map

\[
u\mapsto
\left(1-\frac L{|u|}\right)_+u
\]

is nonlinear. Its Fourier content is therefore not identical to the Fourier content of `u` under a linear projector.

Hence the linear `k~L` bridge has been proved for the **natural nonlinear high-amplitude excess field**, not for the whole-velocity Fourier tail.

Promoting it to a whole-velocity spectral statement requires a composition/localization commutator estimate that does not simply reintroduce the open critical-tail problem.

## 8. DSD interpretation

The `K` defect is now localized in both state amplitude and physical scale:

\[
\boxed{
\text{amplitude }|u|\sim L
\quad\leftrightarrow\quad
\text{space }|x-X_*|\sim L^{-1}
\quad\leftrightarrow\quad
\text{excess-field frequency }|k|\sim L.
}
\]

Thus the former joint boundary

\[
\lambda|Y|\sim1
\]

has an equivalent physical phase-space representation.

The remaining issue is not the scale match itself. The missing step is to transfer this localized excess-field frequency information into a divergence-free critical dynamics channel of the original velocity.

## 9. Next target

Use the Hodge decomposition

\[
W_n=\mathbb PW_n+\mathbb QW_n.
\]

Because `P` and `Q` commute with Fourier cutoffs, the high-frequency excess must satisfy a dichotomy:

\[
\boxed{
\text{solenoidal high-frequency excess}
\quad\lor\quad
\text{gradient/amplitude-transport high-frequency excess}.
}
\]

The first branch can be compared with localized helical mixing; the second branch can be expressed through the divergence of the amplitude truncation and connected back to the amplitude-direction/Hodge channel.

This is the natural M5-22 continuation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
