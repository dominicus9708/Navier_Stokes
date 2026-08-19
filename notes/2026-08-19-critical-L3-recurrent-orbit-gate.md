# Critical L3 gate for compact recurrent normalized profiles

Date: 2026-08-19

Status: **DERIVED SCALE-CRITICAL COMPACTNESS GATE + EXTERNAL L3 REGULARITY ANCHOR / GLOBAL REGULARITY NOT PROVED**.

This note continues `FRONTIER_LATEST_2026-08-19.md` and targets the remaining compact positive-rate recurrent normalized orbit.

---

## 1. Dynamic normalization and the critical L3 channel

Let

\[
W=\|\omega(t)\|_\infty,\qquad \lambda=W^{1/2},\qquad ds=W\,dt,
\]

\[
U(y,s)=\lambda^{-1}u(x,t),\qquad \Omega(y,s)=\lambda^{-2}\omega(x,t).
\]

The velocity critical norm is exactly invariant:

\[
\boxed{\|U(s)\|_{L^3_y}=\|u(t)\|_{L^3_x}.}
\]

The whole-space identity

\[
\frac{d}{dt}\int|u|^3+3\nu D_3=3\Pi_3
\]

has the same form in dynamic normalized time:

\[
\boxed{
\frac{d}{ds}\int|U|^3+3\nu D_3[U]=3\Pi_3[U].
}
\]

There is no scale-damping term because `L^3` is Navier--Stokes critical.

The Escauriaza--Seregin--Sverak critical regularity theory, and Tao's quantitative refinement, imply that a finite-time singular solution cannot remain uniformly bounded in the global `L^3` velocity norm. Thus along a singular sequence

\[
\boxed{\|U(s_j)\|_3\to\infty.}
\]

Tao's quantitative version gives a very slow but explicit lower growth rate along a sequence approaching the singular time.

---

## 2. Critical vorticity norm must also diverge

By the Biot--Savart / Hardy--Littlewood--Sobolev estimate,

\[
\boxed{
\|U\|_3\le C_H\|\Omega\|_{3/2}.
}
\]

Hence every singular sequence satisfying the critical velocity divergence also satisfies

\[
\boxed{
\|\Omega(s_j)\|_{3/2}\to\infty.
}
\]

Therefore a globally precompact/recurrent normalized vorticity profile in `L^(3/2)` cannot represent a singular critical element.

---

## 3. Scale-critical Gagliardo--Nirenberg gate

For divergence-free `U`,

\[
\Omega=\nabla\times U.
\]

The three-dimensional Gagliardo--Nirenberg inequality with one derivative between `U in L2` and `D^2 U in L2` gives

\[
\|\Omega\|_{3/2}
\lesssim
\|U\|_2^{3/4}\|D^2U\|_2^{1/4}.
\]

On the whole space, Fourier equivalence gives

\[
\|D^2U\|_2\asymp\|\nabla\Omega\|_2.
\]

Define

\[
K_U=\|U\|_2^2,
\qquad
P_\Omega=\|\nabla\Omega\|_2^2.
\]

Raising the interpolation inequality to the eighth power yields the exact scale-critical gate

\[
\boxed{
\|\Omega\|_{3/2}^{8}
\lesssim
K_U^3P_\Omega.
}
\]

Combining with the HLS estimate gives

\[
\boxed{
\|U\|_3^8
\lesssim
K_U^3P_\Omega.
}
\]

If

\[
X=\max\{K_U,P_\Omega\},
\]

then `K_U^3 P_Omega <= X^4`, so

\[
\boxed{
\max\{K_U,P_\Omega\}
\gtrsim
\|U\|_3^2.
}
\]

Thus critical-norm blow-up forces at least one of normalized kinetic-energy escape or normalized palinstrophy escape.

---

## 4. Recurrent-core consequence

Suppose the tracked normalized core is locally recurrent/tight and its bounded-radius velocity variance is uniformly controlled.

If

\[
P_\Omega(s_j)\to\infty,
\]

this is a derivative/palinstrophy escape and is routed to `H`.

If instead

\[
K_U(s_j)\to\infty,
\]

while every fixed-radius recurrent core carries only bounded kinetic energy/variance, the excess kinetic energy must leave every fixed normalized ball. This is a low-frequency / large-spatial-scale non-tightness certificate and is routed to `T`.

Consequently

\[
\boxed{
\text{compact recurrent critical profile}
\Longrightarrow
H\ \text{or}\ T.
}
\]

The previously listed `compact positive-rate recurrent orbit` is therefore not an independent derivative-controlled/tight survivor once the external critical `L^3` theorem is imposed.

---

## 5. Remote-tail influence gate

Let `A_j` be dyadic annuli of radius `R_j` outside a fixed normalized core. The strain generated at the core by remote vorticity satisfies schematically

\[
\|S_{\rm far}\|_{L^\infty(B_{R_0})}
\lesssim
\sum_{j\ge J}R_j^{-2}
\|\Omega\|_{L^{3/2}(A_j)}.
\]

Using finite-volume comparison on each annulus,

\[
\|\Omega\|_{3/2,A_j}
\lesssim
R_j^{1/2}\|\Omega\|_{2,A_j},
\]

hence

\[
\|S_{\rm far}\|_{L^\infty(B_{R_0})}
\lesssim
\sum_{j\ge J}R_j^{-3/2}E_j^{1/2}
\lesssim
R_J^{-3/2}E_\Omega^{1/2}.
\]

Therefore if normalized enstrophy remains bounded, a critical `L^(3/2)` halo can diverge while becoming dynamically weak at the tracked core. To have order-one remote strain influence from arbitrarily distant scales, normalized enstrophy itself must grow or the critical mass must remain at bounded normalized radius.

Thus the critical tail splits into:

1. **passive far halo** -- required by global critical-norm divergence but negligible in the local core equation;
2. **active bounded-radius turnover** -- routed to `T`;
3. **active far tail with growing enstrophy** -- routed to `H/T`.

This prevents the global critical tail from being counted automatically as a free local production mechanism.

---

## 6. Critical pressure-action consequence

Because the dynamic normalization leaves the `L^3` identity unchanged,

\[
T_3(s_1)-T_3(s_0)
+3\nu\int_{s_0}^{s_1}D_3\,ds
=
3\int_{s_0}^{s_1}\Pi_3\,ds.
\]

If a singular sequence has `T3 -> infinity`, then necessarily

\[
\boxed{
\int^{s_j}\Pi_3\,ds\to+\infty
}
\]

along a corresponding sequence. Thus global critical-norm escape requires unbounded cumulative positive pressure correlation. If the tracked recurrent core keeps bounded `L^3`, this pressure action must increasingly reside in the critical tail / turnover sector.

The next pressure target is therefore not monotonicity of `T3`, which is known to fail as a general route, but a local-to-tail packing estimate for the positive pressure action.

---

## External anchors

- Escauriaza, Seregin, Sverak: endpoint `L^infinity_t L^3_x` regularity for 3D Navier--Stokes.
- T. Tao, *Quantitative bounds for critically bounded solutions to the Navier-Stokes equations*, arXiv:1908.04958.
- N. C. Phuc, *The Navier-Stokes equations in nonendpoint borderline Lorentz spaces*, arXiv:1407.5129.

Status: **COMPACT POSITIVE-RATE RECURRENT CRITICAL ELEMENT REDUCED TO DERIVATIVE ESCAPE OR CRITICAL LARGE-SCALE/TAIL ESCAPE; GLOBAL CLOSURE STILL OPEN.**