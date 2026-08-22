# Localized Solenoidal Phase-Space Trichotomy — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — LOW-FREQUENCY ESCAPE IS ELIMINATED FOR A COMPACT SOLENOIDAL SHELL PACKET; NON-HIGH-DERIVATIVE PACKETS HAVE FORCED NATURAL-FREQUENCY OCCUPANCY — GLOBAL REGULARITY NOT PROVED.**

This note attacks the sole bottleneck recorded in `FRONTIER_HISTORICAL_SHELL_AFTER_HARDY_DUHAMEL_2026-08-23.md`.

The goal is to turn a physical historical shell into a compactly supported divergence-free packet and then prove a quantitative frequency trichotomy. The main new observation is that compact support plus solenoidality automatically gives zero spatial mean, which suppresses the very-low-frequency branch.

---

## 1. Radial shell and cutoff geometry

Fix a smooth solution `u` with

\[
\nabla\cdot u=0
\]

and a center `X`.

Let the retained shell core be

\[
A_r
=\{a_1r<|x-X|<a_2r\},
\]

with fixed

\[
0<a_0<a_1<a_2<a_3<\infty.
\]

Choose a smooth radial cutoff

\[
\chi_r(x)=\chi(|x-X|/r)
\]

such that

\[
\chi_r=1\quad\text{on }A_r,
\]

\[
\operatorname{supp}\chi_r
\subset
A_r^+
:=\{a_0r<|x-X|<a_3r\},
\]

and

\[
|\nabla\chi_r|\le C_\chi r^{-1},
\qquad
|\nabla^2\chi_r|\le C_\chi r^{-2}.
\]

Then

\[
\nabla\cdot(\chi_ru)
=\nabla\chi_r\cdot u
=:g_r.
\]

The support of `g_r` lies only in the two transition annuli.

---

## 2. Each radial transition source has zero mean

Because `u` is smooth and divergence free, the flux through every sphere centered at `X` is zero:

\[
\int_{|x-X|=\rho}u\cdot n\,dS
=0.
\]

Indeed this is the divergence theorem on `B_\rho(X)`.

On either radial transition annulus,

\[
g_r=\chi_r'(\rho)u\cdot n,
\]

so coarea gives

\[
\int g_rdx
=
\int \chi_r'(\rho)
\left(
\int_{|x-X|=\rho}u\cdot n\,dS
\right)d\rho
=0.
\]

Thus each transition source separately has the compatibility condition required for a Bogovskii divergence correction.

---

## 3. Compact solenoidal shell packet

Apply the Bogovskii operator separately on the inner and outer transition annuli. Let `b_r` be the sum of the two corrections, chosen so that

\[
\nabla\cdot b_r=g_r,
\]

with `b_r` supported only in the transition regions.

Define

\[
\boxed{
f_r:=\chi_ru-b_r.
}
\]

Then

\[
\boxed{
\nabla\cdot f_r=0,
\qquad
\operatorname{supp}f_r\subset A_r^+,
\qquad
f_r=u\quad\text{on }A_r.
}
\]

By scale-invariant Bogovskii estimates on the fixed-shape annuli,

\[
\boxed{
\|b_r\|_2
\le
C_B\|u\|_{L^2(\operatorname{trans})},
}
\]

and

\[
\boxed{
\|\nabla b_r\|_2
\le
C_Br^{-1}
\|u\|_{L^2(\operatorname{trans})}.
}
\]

Hence

\[
\boxed{
\|\nabla f_r\|_2
\le
C
\left[
\|\nabla u\|_{L^2(A_r^+)}
+r^{-1}\|u\|_{L^2(A_r^+)}
\right].
}
\]

The correction therefore costs only the natural derivative scale unless the original shell already carries excess derivative mass.

---

## 4. A compact divergence-free field has zero spatial mean

Since `f_r` is compactly supported and divergence free, for each component `i`,

\[
\nabla\cdot\big((x_i-X_i)f_r\big)
=(f_r)_i.
\]

Integrating over `R^3` gives

\[
\boxed{
\int_{\mathbb R^3}f_r(x)dx=0.
}
\]

This cancellation is the key low-frequency fact.

---

## 5. Quantitative low-frequency suppression

Use the Fourier transform centered at `X`. Since the mean vanishes,

\[
\widehat f_r(\xi)
=
\int
\left(e^{-i\xi\cdot(x-X)}-1\right)
f_r(x)dx.
\]

Because `|x-X|<=a_3r` on the support,

\[
|\widehat f_r(\xi)|
\le
|\xi|
\int |x-X||f_r(x)|dx.
\]

Cauchy--Schwarz and the support volume `O(r^3)` give

\[
\int |x-X||f_r|dx
\le
C_sr^{5/2}\|f_r\|_2.
\]

Therefore

\[
|\widehat f_r(\xi)|
\le
C_s|\xi|r^{5/2}\|f_r\|_2.
\]

Integrating over the ball `|xi|<=a/r` gives

\[
\boxed{
\|P_{\le a/r}f_r\|_2^2
\le
C_La^5\|f_r\|_2^2.
}
\]

Equivalently,

\[
\boxed{
\|P_{\le a/r}f_r\|_2
\le
C_L^{1/2}a^{5/2}\|f_r\|_2.
}
\]

Thus for every desired `delta_L>0` one may choose a fixed sufficiently small `a=a(delta_L,a_3)` such that

\[
\boxed{
\|P_{\le a/r}f_r\|_2
\le
\delta_L\|f_r\|_2
}
\]

uniformly in the shell radius `r`.

So a compact solenoidal historical packet cannot place an order-one fraction of its `L2` mass at arbitrarily sub-natural frequencies.

The previously listed branch

\[
\text{low-frequency escape}
\]

is therefore eliminated at packet level rather than merely relabeled as drift.

---

## 6. Quantitative high-frequency alternative

By Plancherel,

\[
\int_{|\xi|\ge b/r}|\widehat f_r(\xi)|^2d\xi
\le
\frac{r^2}{b^2}
\int |\xi|^2|\widehat f_r(\xi)|^2d\xi.
\]

Hence

\[
\boxed{
\|P_{\ge b/r}f_r\|_2
\le
\frac1b
\frac{r\|\nabla f_r\|_2}{\|f_r\|_2}
\|f_r\|_2.
}
\]

Define the dimensionless shell derivative ratio

\[
\boxed{
\Gamma_r(f_r)
:=
\frac{r\|\nabla f_r\|_2}{\|f_r\|_2}.
}
\]

If

\[
\|P_{\ge b/r}f_r\|_2
\ge
\delta_H\|f_r\|_2,
\]

then necessarily

\[
\boxed{
\Gamma_r(f_r)
\ge
b\delta_H.
}
\]

Thus high-frequency escape is exactly a large normalized derivative-frequency event.

For a compact divergence-free packet,

\[
\|\nabla f_r\|_2^2
=
\|\nabla\times f_r\|_2^2,
\]

so this can equally be read as a localized vorticity/enstrophy cost.

If the shell has natural kinetic mass `||f_r||_2^2 \gtrsim r`, then high-frequency occupancy at frequency `b/r` implies

\[
r\|\nabla\times f_r\|_2^2
\gtrsim
b^2,
\]

a scale-invariant derivative cost. For sufficiently large fixed `b`, this is the intended `H`/derivative-frequency branch.

---

## 7. Forced middle-band occupancy on a non-H packet

Assume the non-high-derivative corridor gives

\[
\Gamma_r(f_r)
\le
\Gamma_*
\]

with a scale-independent constant `Gamma_*`.

Choose `a` so that

\[
C_La^5\le\frac1{16},
\]

and choose

\[
b\ge4\Gamma_*.
\]

Then

\[
\|P_{\le a/r}f_r\|_2
\le
\frac14\|f_r\|_2,
\]

and

\[
\|P_{\ge b/r}f_r\|_2
\le
\frac14\|f_r\|_2.
\]

For orthogonal sharp Fourier regions this yields

\[
\boxed{
\|P_{a/r<|\xi|<b/r}f_r\|_2^2
\ge
\frac78\|f_r\|_2^2.
}
\]

In particular

\[
\boxed{
\|P_{a/r<|\xi|<b/r}f_r\|_2
\ge
\sqrt{\frac78}\,\|f_r\|_2.
}
\]

The constants are not important; the structural conclusion is:

\[
\boxed{
\text{compact solenoidal shell}
+
\text{bounded normalized derivative ratio}
\Longrightarrow
\text{fixed natural-frequency occupancy}.
}
\]

Thus the natural-frequency hypothesis in `SLIDING_HISTORY_DUHAMEL_FORGETTING_TAX_2026-08-23.md` is no longer an independent assumption once the packet localization and non-H derivative bound are available.

---

## 8. Shell L3 occupancy supplies nondegenerate packet L2 mass

The historical tower is measured naturally by cubic shell occupancy. Let

\[
m_r
:=
\int_{A_r}|u|^3dx.
\]

Assume the Type-I envelope

\[
|u(x)|\le\frac{A}{r}
\qquad
\text{on }A_r.
\]

Then

\[
|u|^3
\le
\frac{A}{r}|u|^2,
\]

and hence

\[
\boxed{
\int_{A_r}|u|^2dx
\ge
\frac rA m_r.
}
\]

Because `f_r=u` on `A_r`,

\[
\boxed{
\|f_r\|_2^2
\ge
\frac rA m_r.
}
\]

Therefore every shell with a fixed cubic occupancy floor

\[
m_r\ge\mu>0
\]

has the natural kinetic packet size

\[
\boxed{
\|f_r\|_2
\ge
\sqrt{\mu/A}\,r^{1/2}.
}
\]

This prevents the Duhamel forgetting normalization from degenerating on an occupied historical shell.

---

## 9. Positive-density selection of genuinely occupied shells

Suppose a historical tower contains `N` geometric shells with

\[
\sum_{n=1}^Nm_n
\ge
c_0N.
\]

The Type-I envelope gives a uniform shell upper bound

\[
m_n\le M_A,
\]

where `M_A=O(A^3)` depends only on the fixed shell aspect ratio and the envelope constant.

Let

\[
G_N
:=
\{n:m_n\ge c_0/2\}.
\]

If `g_N=|G_N|`, then

\[
c_0N
\le
g_NM_A+(N-g_N)c_0/2.
\]

Thus

\[
\boxed{
\frac{g_N}{N}
\ge
\frac{c_0}{2M_A-c_0}
=:\rho_*>0.
}
\]

So logarithmic total `L3` occupancy is not allowed to hide in an ever-growing collection of infinitesimal shells: a fixed positive density of shells carries fixed order-one cubic mass.

Every such good shell has natural `L2` packet mass by the previous section.

---

## 10. Updated phase-space routing

For every good occupied historical shell, form `f_r` as above.

Then exactly one of the following occurs.

### Route 1: large normalized derivative ratio

\[
\Gamma_r(f_r)>\Gamma_*.
\]

This is a direct derivative-frequency event and is routed to `H` once the `H` threshold is expressed in the same localized normalized derivative ledger.

### Route 2: bounded normalized derivative ratio

\[
\Gamma_r(f_r)\le\Gamma_*.
\]

Then low frequencies are suppressed by compact solenoidal cancellation and high frequencies are suppressed by the derivative bound. Therefore a fixed fraction of `f_r` lies in the natural band

\[
\frac a r<|\xi|<\frac b r.
\]

If this historical shell is later forgotten, `SLIDING_HISTORY_DUHAMEL_FORGETTING_TAX_2026-08-23.md` forces an order-one scale-invariant nonlinear forgetting action.

This is routed to `T`, modulo the localization evolution commutators.

Thus the former three-way frequency escape has collapsed to the two existing typed branches

\[
\boxed{
\text{good historical shell}
\Longrightarrow
H
\quad\text{or}\quad
(\text{natural band and forgetting }\Rightarrow T).
}
\]

There is no independent low-frequency survivor for a compact solenoidal packet.

---

## 11. What remains technically unresolved

The spatial-frequency geometry is now quantitative. The remaining issue is dynamical rather than kinematic.

The time-dependent packet

\[
f_r(t)=\chi_r(t)u(t)-b_r(t)
\]

does not satisfy the free Navier--Stokes mild equation. Its evolution contains

- cutoff motion `partial_t chi_r`;
- material crossing `u dot grad chi_r`;
- viscous commutators `2 grad chi_r dot grad u + Delta chi_r u`;
- the time derivative and diffusion of the Bogovskii correction;
- Leray/pressure nonlocality;
- moving-center terms.

The next step is to write the exact packet equation and show the following:

\[
\boxed{
\text{if all localization commutator actions are below the existing H/T thresholds,}
}
\]

then the middle-band Duhamel forgetting lower bound survives with a positive constant.

If any commutator is not small, it must itself be assigned quantitatively to `H`, `T`, pressure routing, or coherent drift.

---

## 12. Current status

The phase-space bottleneck has been materially narrowed:

1. a compact divergence-free shell packet can be constructed by radial cutoff plus Bogovskii correction;
2. it has zero spatial mean automatically;
3. zero mean plus `O(r)` support suppresses frequencies `<<r^{-1}` by `O(a^(5/2))`;
4. frequencies `>>r^{-1}` are controlled by the normalized derivative ratio;
5. hence every non-H occupied shell has a fixed natural-frequency component;
6. logarithmic historical `L3` mass supplies a positive density of such genuinely occupied shells;
7. every forgotten non-H good shell is therefore eligible for the Duhamel turnover tax.

Status: **THE LOW-FREQUENCY ESCAPE BRANCH IS KINEMATICALLY CLOSED FOR COMPACT SOLENOIDAL PACKETS. THE HISTORICAL RECYCLING SURVIVOR IS NOW REDUCED TO AN EXACT TIME-DEPENDENT LOCALIZATION-COMMUTATOR AUDIT. GLOBAL REGULARITY IS NOT PROVED.**
