# Global terminal trace collapse

Date: 2026-08-14

Status: **DERIVED ON THE BOUNDED-CONDITION, BOUNDED-ACCUMULATED-AFFINE GAUSSIAN BRANCH. THE QUADRATIC-CORE DEGREE-TWO TRACE SOURCE CANNOT CARRY ORDER-ONE TERMINAL MEAN-VORTICITY CREATION EVEN BELOW THE PREVIOUS `W^(1/10)` MESOSCOPIC THRESHOLD. GLOBAL REGULARITY NOT PROVED.**

## 1. Natural terminal mean-creation interval

Let

\[
B(\tau)\le m,
\qquad
m\to0,
\]

on the surviving bounded-affine branch, where backward time is

\[
\tau=-t\ge0.
\]

The co-affine mean-vorticity source satisfies

\[
|J|\lesssim_K B\le C_Km.
\]

Since terminal first hitting requires an order-one mean change, its natural minimum creation time is

\[
\tau_m\asymp m^{-1}.
\]

On the matched Gaussian branch,

\[
R(\tau)^2\asymp_K\tau.
\]

## 2. Degree-two coefficient equation

Let `Y_2(t)` be the moving Gaussian degree-two vorticity coefficient, and let `ell_t` recover the quadratic-core trace source. As in the earlier telescoping calculation,

\[
Y_2'+\mathcal A_2Y_2=F_2,
\qquad
J_{\rm tr}=\ell_tF_2,
\]

with

\[
\|\mathcal A_2(t)\|+\|\ell_t'(t)\|
\lesssim_K
R(t)^{-2}+|S(t)|.
\]

Thus

\[
\boxed{
\int_IJ_{\rm tr}dt
=
[\ell_tY_2]_{\partial I}
+
\int_I(\ell_t\mathcal A_2-\ell_t')Y_2dt.
}
\]

## 3. Terminal collapse of the degree-two state

The established terminal residual-collapse estimate gives, for sufficiently small backward time,

\[
B(\tau)\lesssim_K\tau.
\]

Globally on the responsible branch we also have `B<=m`. Hence

\[
\boxed{
B(\tau)
\lesssim_K
\min\{m,\tau\}.
}
\]

Since `Y_2` is a component of the residual-vorticity variance,

\[
\boxed{
|Y_2(\tau)|
\lesssim_K
\sqrt{\min\{m,\tau\}}.
}
\]

In particular the terminal coefficient tends to zero rather than merely remaining bounded by `sqrt(m)`.

## 4. The scale term is globally integrable and vanishes

Because

\[
R(\tau)^{-2}\asymp_K\tau^{-1},
\]

the potentially singular scale contribution is

\[
I_m
:=
\int_0^{c/m}
\tau^{-1}|Y_2(\tau)|d\tau.
\]

Using the terminal-collapse envelope and splitting at `tau=m`,

\[
\begin{aligned}
I_m
&\lesssim_K
\int_0^m\tau^{-1/2}d\tau
+
\sqrt m\int_m^{c/m}\frac{d\tau}{\tau}\\
&\lesssim_K
2\sqrt m
+
\sqrt m\log\frac{c}{m^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
I_m
\lesssim_K
\sqrt m\,(1+|\log m|)
\to0.
}
\]

This is the key improvement over the earlier strict-mesoscopic estimate: no positive lower radius is required.

## 5. Boundary and affine-strain terms

At both endpoints of the natural terminal interval,

\[
|Y_2|\lesssim_K\sqrt m,
\]

and at the terminal endpoint it actually vanishes. Hence

\[
\boxed{
|[\ell_tY_2]_{\partial I}|
\lesssim_K\sqrt m
\to0.
}
\]

The affine representation term satisfies

\[
\int_I|S(t)|\,|Y_2(t)|dt
\le
\sqrt m\int_I|S(t)|dt.
\]

On the bounded accumulated-affine branch,

\[
\int_I|S(t)|dt\le K,
\]

so

\[
\boxed{
\int_I|S|\,|Y_2|dt
\lesssim_K\sqrt m
\to0.
}
\]

## 6. Global trace-action collapse

Combining the exact telescoping identity with the three estimates above gives

\[
\boxed{
\left|
\int_0^{c/m}J_{\rm tr}(\tau)d\tau
\right|
\lesssim_K
\sqrt m\,(1+|\log m|)
\to0.
}
\]

Therefore the quadratic-core degree-two trace lane cannot carry any fixed positive fraction of the order-one terminal co-affine mean-vorticity creation.

This conclusion holds throughout the full natural terminal creation interval, including radii

\[
R<W^{1/10}.
\]

## 7. Revised low-Hermite endgame

The exact quadratic-core source decomposition is

\[
J_{\rm core}=J_{\rm tr}+J_{Ab}.
\]

The present result removes `J_tr` as an order-one terminal-creation mechanism on the entire bounded-affine natural interval.

Hence a low-Hermite surviving terminal mean-vorticity episode must satisfy

\[
\boxed{
\int J_{Ab}\,dt
=O(1)
}
\]

up to high-Hermite/remainder terms.

The remaining degree-one core is therefore genuinely projective. Its amplitude-producing part can be sharpened further relative to the mean-vorticity axis.

Status: **QUADRATIC-CORE TRACE LANE CLOSED ON THE FULL TERMINAL MEAN-CREATION INTERVAL / NO `W^(1/10)` LOWER-RADIUS CONDITION REMAINS / LOW-HERMITE ENDGAME = PROJECTIVE `Ab` AMPLITUDE OR HIGH-HERMITE ESCAPE / GLOBAL REGULARITY NOT PROVED.**
