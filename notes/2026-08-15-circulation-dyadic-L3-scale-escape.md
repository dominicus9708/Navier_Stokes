# Persistent circulation across reset scales forces critical L3 mass escape

Date: 2026-08-15

Status: **DERIVED DYADIC CIRCULATION-TO-L3 LOWER BOUND / ZENO ROUTED TO CRITICAL L3 ESCAPE OR INTERMEDIATE FLUX RESET.**

This note connects the repeated material-flux endgame to the repository's ancient `L3` Liouville/non-tightness route.

The key fact is that circulation is critical for velocity `L3`: a robust signed circulation persisting through one dyadic three-dimensional tube block costs an order-one amount of `L3` mass relative to the circulation amplitude, independent of the block radius.

---

## 1. Circulation on a transverse circle

Let a straight local axis be `e`, with cylindrical coordinates `(rho,theta,z)`.

Suppose for radii in a dyadic band

\[
r\le\rho\le2r
\]

and axial positions in an interval of length comparable to `r`, the signed vorticity flux through the transverse disk obeys

\[
\boxed{
|\Phi_\rho(z)|
\ge\Phi_0>0.
}
\]

By Stokes' theorem,

\[
\Phi_\rho(z)
=\oint_{C_{\rho,z}}u\cdot d\ell.
\]

Hence

\[
|\Phi_\rho(z)|
\le
\oint_{C_{\rho,z}}|u|d\ell.
\]

---

## 2. Holder lower bound on each circle

Holder on a circle of length `2 pi rho` gives

\[
\left(\oint|u|d\ell\right)^3
\le
(2\pi\rho)^2
\oint|u|^3d\ell.
\]

Therefore

\[
\boxed{
\oint_{C_{\rho,z}}|u|^3d\ell
\ge
\frac{\Phi_0^3}{(2\pi\rho)^2}.
}
\]

---

## 3. Integrate one dyadic tube block

Integrate over

\[
r\le\rho\le2r
\]

and over an axial interval of length

\[
L\ge c_Lr.
\]

Using cylindrical coarea,

\[
\begin{aligned}
\int_{\rm block}|u|^3dx
&=
\int dz\int d\rho
\oint_{C_{\rho,z}}|u|^3d\ell\\
&\ge
c
\Phi_0^3
\int_0^{c_Lr}dz
\int_r^{2r}\rho^{-2}d\rho.
\end{aligned}
\]

Since

\[
\int_r^{2r}\rho^{-2}d\rho
\asymp r^{-1},
\]

we obtain the scale-independent critical lower bound

\[
\boxed{
\int_{\rm block}|u|^3dx
\gtrsim
\Phi_0^3.
}
\]

This is exactly scale invariant under Navier--Stokes scaling because circulation is scale invariant and `L3` velocity mass is critical.

---

## 4. Dyadic radial persistence ladder

Suppose a comparable signed circulation survives through radii

\[
r_k=2^kr_0,
\qquad k=0,\ldots,N-1,
\]

with an `O(r_k)` axial tube block available at each scale.

Choose the corresponding radial/axial blocks with bounded overlap. Summing the previous estimate gives

\[
\boxed{
\int |u|^3dx
\gtrsim
N\Phi_0^3.
}
\]

If the circulation persists from a current core scale `ell` to a parent scale `ell sqrt(q)`, then

\[
N\asymp\log_2\sqrt q
\asymp\frac12\log q.
\]

Hence

\[
\boxed{
\|u\|_3^3
\gtrsim
\Phi_0^3\log q.
}
\]

---

## 5. Coherent crossing specialization

For the coherent Reynolds-one crossing,

\[
\Phi_0\asymp R^2.
\]

Therefore persistent circulation across the full reset scale gap forces

\[
\boxed{
\|u\|_3^3
\gtrsim
R^6\log q.
}
\]

Since

\[
R\to\infty,
\]

this is a strongly diverging critical `L3` requirement.

This is compatible with a hypothetical singular route; it is not a contradiction.

---

## 6. Shielding alternative

The dyadic lower bound assumes robust signed circulation survives through each intermediate radial band.

If this fails, then at some scale the inner circulation must be reduced by one or more of

- opposite-polarity axial vorticity;
- off-axis side flux;
- viscous material-flux change;
- strong geometric bending of the local tube.

These are exactly the already typed polarity/projective/material-reset/derivative channels.

Thus the reset scale ladder obeys

\[
\boxed{
\text{persistent signed circulation across scales}
\Longrightarrow
\text{critical }L^3\text{ mass accumulation},
}
\]

or

\[
\boxed{
\text{failure of persistence}
\Longrightarrow
\text{intermediate-scale flux reset / shielding}.
}
\]

---

## 7. Connection to the ancient Liouville branch

The repository's ancient-limit audit uses the external Liouville gate: a nontrivial mild ancient solution with uniformly bounded `L3` norm along a sequence of times tending to `-infinity` is excluded by the Albritton--Barker theorem under its stated hypotheses.

The present dyadic estimate identifies a concrete way the surviving flux-reset Zeno can avoid backward `L3` tightness:

\[
\boxed{
\text{circulation survives over a growing scale ladder}
\Rightarrow
\text{critical }L^3\text{ mass fills/escapes through those scales}.
}
\]

If it does not do so, it must repeatedly reset or shield the flux at intermediate scales, returning to the quantitative reset-cost hierarchy.

Hence the two previously separate endgames are now aligned:

\[
\boxed{
\text{parabolic flux-reset Zeno}
\Longrightarrow
\text{critical }L^3\text{ scale escape}
\lor
\text{repeated intermediate-scale reset}.
}
\]

---

## 8. Claim boundary

No boundedness of `||u||_3` near a hypothetical singular time is assumed or proved. In fact a singular solution is allowed to have diverging critical `L3` norm.

The result therefore does not prove regularity.

It shows that a surviving Zeno cascade cannot remain simultaneously

- circulation-persistent across a growing scale range;
- `L3`-tight;
- and free of intermediate-scale reset/shielding.

Status: **FINAL ZENO ROUTED TO ANCIENT CRITICAL-L3 NON-TIGHTNESS OR MORE FREQUENT QUANTITATIVE FLUX RESET.**