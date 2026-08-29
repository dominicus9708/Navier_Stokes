# DSD M5-227 — Stationary Critical-Tail Point-Force Extension and Zero-Torque Reduction

Date: 2026-08-30

Parent: `DSD_M5_226_STATIONARY_CRITICAL_TAIL_DILATION_POHOZAEV_AND_TORQUE_FLUX_FIREWALL_2026-08-30.md`

Status: **EXACT DISTRIBUTIONAL REDUCTION / AN O(1/r) STATIONARY PUNCTURED TAIL WITH O(1/r^2) STRESS EXTENDS TO ALL OF R3 AS A STATIONARY NAVIER--STOKES DISTRIBUTION WITH ONE AND ONLY ONE POINT-SUPPORTED DEFECT `b delta_0` / DERIVATIVES OF DELTA ARE EXCLUDED DIRECTLY BY THE STRESS GROWTH / THE CONSTANT TORQUE CHARGE FROM M5-226 IS FORCED TO BE EXACTLY ZERO / ZERO FORCE REMOVES THE DISTRIBUTIONAL DEFECT BUT DOES NOT BY ITSELF PROVE CLASSICAL REMOVABILITY AT THE CRITICAL 1/r SIZE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Stationary stress and pointwise growth

Use the symmetric momentum stress

\[
\mathbb S
=
-\nu(\nabla T+\nabla T^T)
+T\otimes T
+PI.
\]

On `R3\{0}`,

\[
\nabla\cdot\mathbb S=0.
\]

The W1 stationary critical-tail bounds give

\[
|T(x)|\le C|x|^{-1},
\]

\[
|\nabla T(x)|+|P(x)|\le C|x|^{-2},
\]

and therefore

\[
\boxed{|\mathbb S(x)|\le C|x|^{-2}.}
\]

In particular `mathbb S` is locally integrable across the origin:

\[
\int_{B_1}|\mathbb S|dx
\lesssim
\int_0^1dr<\infty.
\]

---

## 2. Define the distributional defect on all of R3

Extend `mathbb S` as the same locally integrable tensor across the single point `0`.

Define

\[
\mathcal F:=\nabla\cdot\mathbb S
\]

as a distribution on all of `R3`.

Since the classical divergence vanishes away from the origin,

\[
\boxed{\operatorname{supp}\mathcal F\subset\{0\}.}
\]

A priori a point-supported distribution could contain `delta_0` and derivatives of `delta_0`.

The critical stress growth removes the derivative terms.

---

## 3. Direct cutoff computation

Let

\[
\varphi\in C_c^\infty(\mathbb R^3;\mathbb R^3).
\]

For `epsilon>0`, integrate on

\[
\Omega_\varepsilon
:=\mathbb R^3\setminus\overline{B_\varepsilon}.
\]

Because `div mathbb S=0` there and `varphi` has compact support,

\[
-\int_{\Omega_\varepsilon}
\mathbb S:\nabla\varphi\,dx
=
\int_{|x|=\varepsilon}
(\mathbb S n)\cdot\varphi\,dS,
\]

where `n=x/|x|` is the outward radial normal from the origin; the sign is consistent with the inner boundary orientation after moving it to the displayed side.

Write

\[
\varphi(x)=\varphi(0)+[\varphi(x)-\varphi(0)].
\]

The first term gives

\[
\varphi(0)\cdot
\int_{|x|=\varepsilon}
\mathbb S n\,dS
=
\varphi(0)\cdot b,
\]

where `b` is the radius-independent stress charge from M5-226.

For the error,

\[
|\varphi(x)-\varphi(0)|
\le C_\varphi\varepsilon,
\]

and

\[
\int_{|x|=\varepsilon}
|\mathbb S n|dS
\le C.
\]

Hence

\[
\left|
\int_{|x|=\varepsilon}
(\mathbb S n)\cdot
[\varphi(x)-\varphi(0)]dS
\right|
\le C C_\varphi\varepsilon
\to0.
\]

Letting `epsilon->0` gives

\[
\boxed{
\langle\nabla\cdot\mathbb S,\varphi\rangle
=b\cdot\varphi(0).
}
\]

Therefore

\[
\boxed{
\nabla\cdot\mathbb S
=b\delta_0.
}
\]

---

## 4. No derivative-delta multipoles

The preceding formula depends only on the value

\[
\varphi(0),
\]

not on

\[
\nabla\varphi(0),
\quad
\nabla^2\varphi(0),
\ldots
\]

Thus every derivative-Dirac coefficient is exactly zero.

This is stronger than merely saying the defect is supported at the origin:

\[
\boxed{
\mathcal F
=b\delta_0
\text{ and nothing else.}
}
\]

The reason is precisely the critical `r^-2` stress bound. A dipole-type distribution would require a stronger singular moment.

---

## 5. Navier--Stokes equation with one point force

Unpacking the stress divergence gives the global distributional equation

\[
\boxed{
-\nu\Delta T
+(T\cdot\nabla)T
+\nabla P
=b\delta_0,
\qquad
\nabla\cdot T=0
}
\]

on all of `R3`.

Thus the large stationary W1 endpoint is no longer merely an exterior/punctured-space solution.

It is a whole-space stationary solution driven by one scale-critical point force.

Landau solutions are the exactly degree-`-1` members of this point-force class.

---

## 6. Torque charge is exactly zero

M5-226 showed that

\[
\tau(r)
:=
\int_{|x|=r}
x\times(\mathbb S n)dS
\]

is independent of `r`.

But the critical stress estimate gives

\[
\begin{aligned}
|\tau(r)|
&\le
r
\int_{|x|=r}|\mathbb S n|dS\\
&\le Cr.
\end{aligned}
\]

Therefore

\[
\tau(r)\to0
\qquad(r\downarrow0).
\]

Since it is constant,

\[
\boxed{\tau(r)\equiv0.}
\]

So the stationary endpoint carries a force monopole but no torque monopole/dipole.

---

## 7. Every dilation has the same point-force coefficient

For the Navier--Stokes dilation

\[
(D_hT)(x)
=e^{-h/2}T(e^{-h/2}x),
\]

the stationary operator scales critically and

\[
\delta_0(e^{-h/2}x)
=e^{3h/2}\delta_0(x).
\]

The velocity/stationary-operator prefactor cancels this exactly.

Hence

\[
\boxed{
-\nu\Delta(D_hT)
+(D_hT\cdot\nabla)(D_hT)
+\nabla(D_hP)
=b\delta_0
}
\]

with the **same** vector `b` for every `h`.

Therefore the entire compact minimal dilation hull of a stationary survivor lies inside one fixed point-force fiber.

---

## 8. Zero-force subbranch

If

\[
\boxed{b=0,}
\]

then

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=0
\]

holds distributionally on all of `R3`, not merely away from the origin.

This agrees with isolated-singularity results: zero stress flux together with the critical `O(1/r)` bound is sufficient to remove the point-supported defect at the **distributional-equation** level.

However this does not imply

\[
T\in C^\infty(\mathbb R^3)
\]

under the borderline `O(1/r)` size.

The classical removable criteria require a strict improvement such as

\[
r|T(x)|\to0
\]

or critical strong integrability such as `L3` near the point.

Thus

\[
\boxed{
b=0
\Longrightarrow
\text{distributionally unforced}
\not\Longrightarrow
\text{classically removable}
}
\]

is retained as a firewall.

---

## 9. Literature match

The 3D isolated-singularity literature identifies Landau solutions as stationary `1/r` fields satisfying a point-force equation

\[
\text{stationary NS}=\kappa\delta_0.
\]

It also records that if the stress flux vanishes and the field has the present `O(1/r)` size, the punctured solution extends as a distributional solution across the point.

These results match the direct stress calculation above but do not classify arbitrary-amplitude nonhomogeneous point-force solutions.

---

## 10. Updated stationary endpoint

The remaining large stationary branch is now

\[
\boxed{
S_{point,large}^{nonhom}:
\begin{cases}
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=b\delta_0,\\
\nabla\cdot T=0,\\
|T(x)|\lesssim A_*/|x|,\quad A_*>\varepsilon_{KS},\\
\tau=0,\\
\underline{\mathscr R}_H>0,\\
\text{all dilations solve the same }b\delta_0\text{ problem},\\
\text{compact minimal dilation hull.}
\end{cases}}
\]

This is substantially narrower than a generic stationary exterior solution.

---

## 11. Next target

The next stationary question is now a **fixed-point-force uniqueness/rigidity** problem:

> Can one fixed `b delta_0` support a nontrivial compact minimal family of arbitrary-amplitude stationary `O(1/r)` solutions related by dilation, other than the homogeneous Landau fixed point?

Small amplitude is already excluded by M5-221.

For large amplitude, existing homogeneous classification and perturbative exterior uniqueness do not yet answer this question.

A useful next audit is to compare two dilates of the same stationary tail, which solve the same point-force equation, and derive the exact stationary relative-energy identity for their difference.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]