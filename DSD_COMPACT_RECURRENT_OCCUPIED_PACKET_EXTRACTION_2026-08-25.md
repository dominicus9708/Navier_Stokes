# DSD Compact-Recurrent Occupied-Packet Extraction

Date: 2026-08-25

Status: **POSITIVE-DENSITY BOUNDED-RADIUS CRITICAL SHELLS UPGRADED TO POSITIVE-DENSITY FINITE OCCUPIED VORTICITY PACKETS ON COMPACT K / MATERIAL IDENTITY ACROSS TIMES NOT YET DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the compact RWLG closure

On the genuinely precompact fixed-center recurrent class `K`, the compact RWLG note proves that every Betchov high-enstrophy time contains a shell

\[
A_R
\subset B_{2R_T}
\]

with

\[
\boxed{
\int_{A_R}|W|^2dY
\ge m_0,
}
\]

where

\[
m_0:=\frac{m_h}{N_K}>0
\]

is independent of the selected high time.

The high-time set has positive recurrent/Leray-time density.

This note converts that `L2` shell mass into a pointwise occupied packet of fixed radius and amplitude.

---

## 2. Uniform H2 bound gives a uniform Holder modulus

The compact class satisfies a uniform `H2` bound on the strain.

Because vorticity and strain are related by order-zero Fourier multipliers,

\[
\boxed{
\sup_{K}\|W\|_{H^2}\le B_{2,K}<\infty.
}
\]

In three dimensions,

\[
H^2(\mathbb R^3)
\hookrightarrow C^{0,1/2}(\mathbb R^3).
\]

Therefore there is a fixed constant

\[
H_K:=C_{Mor}B_{2,K}
\]

such that every state in `K` obeys

\[
\boxed{
|W(Y)-W(Y')|
\le
H_K|Y-Y'|^{1/2}.
}
\]

---

## 3. Shell mass forces one pointwise amplitude witness

The selected shell lies inside the fixed ball `B_{2R_T}`. Hence its volume is at most

\[
V_T:=|B_{2R_T}|
=\frac{4\pi}{3}(2R_T)^3.
\]

Since

\[
\int_{A_R}|W|^2\ge m_0,
\]

there exists a point `Y_* in A_R` satisfying

\[
\boxed{
|W(Y_*)|
\ge
 a_K,
\qquad
 a_K:=\sqrt{\frac{m_0}{V_T}}>0.
}
\]

Otherwise `|W|<a_K` everywhere on the shell would contradict the mass lower bound.

---

## 4. Holder continuity expands the point witness into a ball

Choose

\[
\boxed{
\rho_K
:=
\min\left\{
1,
\left(\frac{a_K}{2H_K}\right)^2
\right\}>0.
}
\]

For

\[
|Y-Y_*|\le\rho_K,
\]

Holder continuity gives

\[
|W(Y)-W(Y_*)|
\le
H_K\rho_K^{1/2}
\le
\frac{a_K}{2}.
\]

Therefore

\[
\boxed{
|W(Y)|
\ge
\frac{a_K}{2}
\qquad
(Y\in B_{\rho_K}(Y_*)).
}
\]

Moreover

\[
|Y_*|\le2R_T,
\]

so the entire packet lies in the fixed ball

\[
B_{2R_T+1}.
\]

Thus every high-enstrophy time contains a uniformly sized, uniformly nonzero secondary vorticity packet in a uniformly bounded Leray region.

**Status: PROVED.**

---

## 5. Positive time density of occupied packets

Let `A_theta` be the positive-density Betchov high-enstrophy set.

The packet extraction applies at every time in `A_theta` while the orbit remains in `K`.

Hence

\[
\boxed{
\mu\left(
\left\{s:
\exists Y_*(s)\in B_{2R_T}
\text{ with }
|W(\cdot,s)|\ge a_K/2
\text{ on }B_{\rho_K}(Y_*(s))
\right\}
\right)
\ge\mu(A_\theta)>0.
}
\]

The center `Y_*(s)` may vary with time. No material identity is inferred yet.

---

## 6. Transfer to physical first-hitting variables

At a selected high time in stage `j`, let

\[
\delta=T^*-t,
\qquad
W_L(Y,s)=\delta\,\omega(x,t).
\]

The occupied Leray ball becomes a physical ball of radius

\[
\ell_K(t)=\rho_K\sqrt\delta.
\]

On the recurrent clock corridor,

\[
\delta
=\frac{\Theta_j(t)}{W_j}
=\Theta_j(t)\frac{r_j^2}{\nu}.
\]

The two-sided clock bounds give fixed positive constants `Theta_min,Theta_max` on the retained stage interior/high-time corridor, so

\[
\boxed{
 c_{r,K}r_j
\le
\ell_K(t)
\le
C_{r,K}r_j
}
\]

with class/corridor-dependent constants.

Likewise

\[
|\omega|
=\frac{|W_L|}{\delta}
\ge
\frac{a_K}{2\delta}
=
\frac{a_K}{2\Theta_j(t)}W_j.
\]

Hence

\[
\boxed{
|\omega|
\ge
 b_KW_j
}
\]

on the packet, where

\[
 b_K:=\frac{a_K}{2\Theta_+}>0.
\]

Thus the secondary packet is genuinely of the current first-hitting physical scale:

\[
\boxed{
\text{radius}\asymp r_j,
\qquad
\text{vorticity amplitude}\gtrsim W_j.
}
\]

It need not contain the global maximum.

---

## 7. Packet-generic material transport lemma

The material transport calculation used for the maximum-centered ancestor packet does not fundamentally require that the initial packet be centered at a maximum.

It requires only:

1. an initial ball of radius `a r_*`;
2. a lower vorticity amplitude `b W_*` on that ball;
3. smooth pre-singular Lagrangian flow;
4. local packet strain/diffusion and tube-deformation exposure bounds.

For the present secondary packet, the constants are supplied by Sections 4-6.

Let `A_*(t)` be its material image. Define the localized packet strain exposure

\[
\Sigma_*(I)
=
\int_I\sup_{A_*(t)}|S|dt,
\]

the normalized diffusion exposure

\[
\mathcal D_*(I)
=
\frac\nu{W_*}
\int_I\sup_{A_*(t)}|\Delta\omega|dt,
\]

and the tube deformation exposure

\[
\Lambda_*(I)
=
\int_I\sup_{H_*(t)}|\nabla u|dt.
\]

If

\[
\Sigma_*(I),\Lambda_*(I)\le L
\]

and

\[
\mathcal D_*(I)\le\frac{b}{2}e^{-L},
\]

then exactly the same integrating-factor and bi-Lipschitz arguments give a descendant occupied ball with

\[
\boxed{
\text{radius}\ge c(a,L)r_*,
\qquad
|\omega|\ge c(b,L)W_*.
}
\]

Thus the existing amplitude-location bridge is packet-generic once the initial occupied ball is formed.

**Status: PROVED by the same local Lagrangian estimates; no maximum property is used after initialization.**

---

## 8. Consequence for the genealogy frontier

On compact `K`, Eulerian positive-density high-enstrophy recurrence now implies more than a shell charge:

\[
\boxed{
\text{positive-density high state}
\Longrightarrow
\text{a finite occupied packet at current natural scale in a bounded region}.
}
\]

For each such packet, forward material evolution has the finite alternative

\[
\boxed{
\text{large local strain/tube deformation}
\lor
\text{large diffusion/fixed-derivative exposure}
\lor
\text{coherent material descendant packet}.
}
\]

This removes `Eulerian diffuseness inside the compact core` as a separate obstruction.

The only remaining issue is how descendant packets at different recurrent times are matched, replaced, or multiply occupied.

---

## 9. DSD audit

The formed finite channels are

- compact class constants `R_T,B_{2,K}`;
- one finite shell mass `m_0`;
- one pointwise witness `Y_*`;
- one occupied radius `rho_K`;
- one finite material packet;
- local packet/tube exposure integrals.

No identity between packets at different times is assumed.

The point selected by the shell average is only an initialization witness; no unique canonical material label is asserted.

---

## 10. Remaining target

The compact-class material frontier is now:

\[
\boxed{
\text{positive-density sequence of current-scale occupied packets}
\stackrel{?}{\Longrightarrow}
\text{material return / packet replacement-turnover / cumulative local exposure}.
}
\]

The next useful step is a bounded-gap recurrence argument: positive invariant measure of the occupied-packet set should produce recurrent high-state pairs separated by a bounded Leray time, after which the packet-generic material transport lemma can be applied over a scale-comparable interval.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
