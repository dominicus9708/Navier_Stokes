# Critical L3 non-tightness certificate at first-hitting scale

Date: 2026-08-19

Status: **DERIVED CRITICAL COMPACTNESS REDUCTION + EXTERNAL ENDPOINT L3 ANCHOR / GLOBAL REGULARITY NOT PROVED**.

This note sharpens `2026-08-19-critical-L3-recurrent-orbit-gate.md`.

---

## 1. Endpoint critical requirement

For a finite-time singularity, the endpoint `L^infinity_t L^3_x` regularity theorem implies that the scale-invariant velocity norm cannot remain bounded. In the dynamic first-hitting normalization,

\[
\boxed{
\|U(s)\|_3=\|u(t)\|_3,
}
\]

so along a singular sequence

\[
\boxed{
\|U(s_j)\|_3\to\infty.
}
\]

---

## 2. Elementary H1 critical interpolation

Let

\[
K_U=\|U\|_2^2,
\qquad
E_\Omega=\|\Omega\|_2^2.
\]

For whole-space divergence-free velocity,

\[
\|\nabla U\|_2^2=\|\Omega\|_2^2=E_\Omega.
\]

Interpolation between `L2` and Sobolev `L6` gives

\[
\|U\|_3
\le
\|U\|_2^{1/2}\|U\|_6^{1/2}
\lesssim
K_U^{1/4}E_\Omega^{1/4}.
\]

Therefore

\[
\boxed{
\|U\|_3^4
\lesssim
K_U E_\Omega.
}
\]

If

\[
X=\max\{K_U,E_\Omega\},
\]

then

\[
\boxed{
X\gtrsim\|U\|_3^2.
}
\]

Thus endpoint critical blow-up forces normalized kinetic energy or normalized enstrophy to diverge along a sequence.

---

## 3. Enstrophy divergence is spatial non-tightness under the first-hitting cap

The first-hitting normalization satisfies

\[
\boxed{\|\Omega\|_\infty=1.}
\]

For every fixed measurable set `K` of finite volume,

\[
\int_K|\Omega|^2dy\le |K|.
\]

Hence if

\[
E_\Omega(s_j)\to\infty,
\]

then

\[
\frac{\int_K|\Omega|^2}{E_\Omega(s_j)}\to0
\]

for every fixed bounded `K`.

Therefore

\[
\boxed{
E_\Omega\to\infty
\Longrightarrow
\text{vorticity-enstrophy spatial non-tightness}.
}
\]

This is a direct `T` certificate, not merely a derivative-size statement.

---

## 4. Kinetic-energy divergence is also a T certificate for a recurrent relative core

The tracked moving-center route subtracts coherent translation and controls bounded-radius relative velocity variance.

If every fixed normalized core has uniformly bounded relative kinetic energy while

\[
K_U(s_j)\to\infty,
\]

then the excess kinetic energy must leave every fixed normalized ball or enter a coherent low-frequency/large-scale component not contained in the recurrent core.

Thus

\[
\boxed{
K_U\to\infty
+\text{bounded recurrent core variance}
\Longrightarrow
\text{large-scale / low-frequency }T.
}
\]

---

## 5. Elimination of the independent compact recurrent branch

Combining the endpoint critical theorem with the interpolation certificate gives

\[
\boxed{
\text{finite-time singularity}
+\text{locally recurrent first-hitting core}
\Longrightarrow
T.
}
\]

More precisely, a singular first-hitting sequence cannot remain globally tight simultaneously in normalized velocity energy and normalized vorticity enstrophy.

Therefore the previously listed

`R2 = compact positive-rate recurrent orbit`

is removed as an independent globally compact survivor. Any locally recurrent critical core must be accompanied by a large-scale / critical-tail non-tightness sector.

This conclusion is stronger and simpler than routing `R2` through palinstrophy first.

---

## 6. Quantitative external refinement

Tao's quantitative endpoint result gives a lower growth rate for `||u(t)||_3` along a sequence approaching a finite blow-up time. Through

\[
\max\{K_U,E_\Omega\}\gtrsim\|U\|_3^2,
\]

that result immediately transfers to a quantitative minimum growth rate of the non-tight kinetic-energy/enstrophy sector.

This quantitative rate is slow and does not by itself close the global problem, but it shows that the `T` sector is not optional in a singular recurrent-core scenario.

---

## External anchors

- Escauriaza--Seregin--Sverak endpoint `L^infinity_t L^3_x` regularity theorem.
- T. Tao, *Quantitative bounds for critically bounded solutions to the Navier-Stokes equations*, arXiv:1908.04958.

Status: **INDEPENDENT COMPACT RECURRENT R2 REMOVED; ANY SINGULAR RECURRENT CORE REQUIRES GLOBAL NON-TIGHTNESS T.**