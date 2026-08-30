# DSD M5-348 — Affine Shield / Seregin Truncated Mixed-Norm Exact `Theta^l` Identity

Date: 2026-08-30

Status: **EXACT SCALE CALCULATION AGAINST SEREGIN 2026 TYPE-II FRAMEWORK / ALL AFFINE 1/5 SPATIAL POWERS CANCEL IN `g Mbar` / NONTRIVIALITY REDUCED TO THE LOCAL CLOCK `Theta^l` / GLOBAL REGULARITY UNPROVED.**

## 1. Published Type-II quantity

Seregin 2026 introduces the truncated mixed quantity

\[
\overline M_{\kappa}^{s,l}(v,d)
:=
\frac1{d^\kappa}
\int_{-d^2f(d)}^0
\left(\int_{B_d}|v|^s dx\right)^{l/s}dt,
\]

with

\[
\kappa=2+l\left(\frac3s-1\right),
\]

and in Section 3 uses

\[
\boxed{g(d)=f(d)^{l-1}.}
\]

The potential Type-II nontriviality is

\[
\boxed{
g(d)\overline M_{\kappa}^{s,l}(v,d)\ge\varepsilon_0.
}
\]

## 2. Affine-shield scales

Let `r` be the first-hitting natural length. The saturated affine shield has physical radius

\[
\boxed{d\asymp r^{4/5}.}
\]

Its velocity is affine at leading order:

\[
|u(x,t)|\asymp r^{-2}|x|
\]

inside the shield.

Let

\[
a:=T_*-t,
\qquad
\Theta:=\frac{a}{r^2}.
\]

To make Seregin's truncated time window coincide with the available terminal time `a`, choose

\[
\boxed{
f(d)=\frac{a}{d^2}.}
\]

Since `d^2=r^{8/5}` and `a=Theta r^2`,

\[
\boxed{
f(d)=\Theta r^{2/5}.}
\]

## 3. Spatial Ls norm of the affine shield

For `|u| ~ r^{-2}|x|` on `B_d`,

\[
\int_{B_d}|u|^s dx
\asymp
r^{-2s}d^{s+3}.
\]

Therefore

\[
\left(\int_{B_d}|u|^s dx\right)^{l/s}
\asymp
r^{-2l}d^{l(1+3/s)}.
\]

Assuming the affine occupancy persists on the truncated terminal window of length

\[
d^2f(d)=a=\Theta r^2,
\]

we get

\[
\overline M_\kappa^{s,l}
\asymp
 d^{-\kappa}
 a
 r^{-2l}
 d^{l(1+3/s)}.
\]

Using

\[
\kappa=2+l(3/s-1),
\]

one has

\[
l(1+3/s)-\kappa=2l-2.
\]

Thus

\[
\overline M_\kappa^{s,l}
\asymp
 a r^{-2l}d^{2l-2}.
\]

Insert `a=Theta r^2` and `d=r^(4/5)`:

\[
\begin{aligned}
\overline M_\kappa^{s,l}
&\asymp
\Theta r^{2-2l}r^{\frac85(l-1)}\\
&=
\boxed{
\Theta r^{-\frac25(l-1)}.
}
\end{aligned}
\]

## 4. Exact cancellation with g

Because

\[
f(d)=\Theta r^{2/5},
\]

Seregin's Section-3 choice gives

\[
\boxed{
g(d)=f(d)^{l-1}
=\Theta^{l-1}r^{\frac25(l-1)}.}
\]

Multiplying,

\[
\boxed{
g(d)\overline M_\kappa^{s,l}(u,d)
\asymp
\Theta^l.
}
\]

All powers of the natural length `r` cancel exactly.

This cancellation is independent of `s`; the `s` dependence already cancels through the critical definition of `kappa`.

## 5. Structural interpretation

The Seregin truncated Type-II detector does not see the affine shield through an additional spatial power after the correct `1/5` energy radius is inserted.

It sees only the local terminal clock

\[
\boxed{\Theta=(T_*-t)r^{-2}.}
\]

Hence:

### 5.1 `Theta -> 0`

\[
g\overline M\to0.
\]

The affine shield is too temporally compressed/passive to trigger Seregin's nontriviality condition through this packet alone.

### 5.2 `Theta ~ Theta_0 > 0`

\[
g\overline M\asymp\Theta_0^l>0.
\]

The affine shield is exactly at Seregin's nontrivial truncated-mixed-norm scale.

For constant-order `Theta`,

\[
f(d)\asymp r^{2/5}=d^{1/2},
\]

so in the power notation

\[
f(d)\sim d^{\alpha-1}
\]

we recover

\[
\boxed{\alpha=3/2.}
\]

This is exactly the boundary identified in Seregin's Section 3: the simple vanishing conclusion applies for `2 alpha - 3 > 0`, while `alpha=3/2` is the borderline.

### 5.3 `Theta -> infinity`

The packet nontriviality is strongly amplified, but the weighted `A_f/E_f/D_f` bounds become harder to maintain. This is the genuine local-clock Type-II lane rather than an immediate application of the theorem.

## 6. Weighted-energy benchmark

For the affine shield, the kinetic energy inside `B_d` is order one. Therefore

\[
A(d)\sim d^{-1}.
\]

Since

\[
f^2=\Theta^2r^{4/5}
\quad\text{and}\quad d^{-1}=r^{-4/5},
\]

its affine contribution satisfies

\[
\boxed{A_f\sim\Theta^2.}
\]

Similarly, using `|grad u|~r^{-2}` on the available interval `a=Theta r^2`, the affine contribution to the weighted dissipation is of order

\[
\boxed{E_f\sim\Theta^2.}
\]

Thus `Theta=O(1)` is also the natural weighted-energy saturation regime.

The pressure contribution requires its own upper-bound audit and is not declared controlled merely from this scaling calculation.

## 7. Formation-axiom consequence

The previous descriptors

- spatial affine-shield radius `d~r^(4/5)`;
- local vorticity clock `Theta`;
- Seregin mixed-norm amplification

are not independent coordinates on the saturated branch.

They obey the exact reduced relation

\[
\boxed{
g\overline M\asymp\Theta^l.}
\]

Thus the affine branch naturally splits into

\[
\boxed{
\Theta\to0
\quad\lor\quad
\Theta\asymp1
\quad\lor\quad
\Theta\to\infty.
}
\]

These are respectively the compressed/passive, borderline Euler-scale, and local-clock Type-II regimes.

## 8. Firewall

Seregin's theorem is not claimed to exclude the `Theta~1` affine shield. It is exactly the `alpha=3/2` borderline rather than the easy `alpha>3/2` zero-limit side.

Nor does `g Mbar ~ Theta^l` by itself verify the weighted pressure/dissipation upper hypothesis (1.7).

## 9. Audit verdict

### PROVED

- exact affine-shield scaling of `Mbar_kappa`;
- exact cancellation yielding `g Mbar ~ Theta^l`;
- `Theta~1` corresponds to `f(d)~d^(1/2)` and `alpha=3/2`;
- affine contributions `A_f,E_f` are order `Theta^2`.

### OPEN

- pressure upper control in the borderline branch;
- exclusion of the `alpha=3/2` Euler-scale limit;
- fast `Theta->infinity` lane;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]