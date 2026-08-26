# DSD M5-23 — First-Hitting Direction-Compression Source Lemma

Date: 2026-08-26

Status: **DERIVED W1-CONDITIONAL DYNAMIC REFINEMENT / A NEW POSITIVE HIGH-AMPLITUDE EXCESS CANNOT BE FIRST CREATED BY A PURELY SOLENOIDAL EXCESS; AT FIRST HITTING THE PRESSURE-COUPLED HODGE/DIRECTION-COMPRESSION CHANNEL HAS A FIXED NORMALIZED FLOOR / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-21 and M5-22

For a large physical threshold `L`, use the scale-normalized variables

\[
z=L(x-X_*),
\qquad
\sigma=L^2(t-t_{ref}),
\]

\[
V(z,\sigma)
=L^{-1}u(X_*+z/L,t),
\qquad
\Pi(z,\sigma)=L^{-2}p(X_*+z/L,t).
\]

Then `(V,Pi)` solves the same-viscosity Navier--Stokes system

\[
V_\sigma+(V\cdot\nabla)V+\nabla\Pi
=\nu\Delta V,
\qquad
\nabla\cdot V=0.
\]

Define

\[
a=|V|,
\qquad
W
=\left(1-\frac1a\right)_+V
=(a-1)_+n,
\qquad
n=V/a
\]

on `a>0`.

M5-21 shows that a fixed positive `K` defect localizes the normalized active region in a fixed `z`-scale and gives a fixed lower bound on the high-amplitude excess.

## 2. Convex excess energy

Define

\[
\boxed{
\mathcal G(V)
:=
\frac12\int (|V|-1)_+^2dz
=
\frac12\|W\|_2^2.
}
\]

This is the convex primitive whose derivative with respect to `V` is exactly `W`:

\[
\nabla_V\left(\frac12(|V|-1)_+^2\right)=W.
\]

The phase-space localization in M5-21 implies that if

\[
K_L^{phys}(t)\ge\delta>0,
\]

then, after choosing the fixed annulus where the defect mass is carried and using its uniform Type-I amplitude ceiling,

\[
\boxed{
\mathcal G(V)\ge g_*(\delta,A_0,R_0)>0.
}
\]

## 3. Exact excess-energy ledger

Test the rescaled Navier--Stokes equation against `W`.

### Time derivative

By convex-chain differentiation,

\[
\int V_\sigma\cdot W
=\frac{d}{d\sigma}\mathcal G(V).
\]

### Advection

Because `W` is the derivative of a scalar function of `V`,

\[
(V\cdot\nabla)V\cdot W
=
V\cdot\nabla\left(\frac12(|V|-1)_+^2\right).
\]

Since `div V=0` and the active excess is localized,

\[
\boxed{
\int (V\cdot\nabla)V\cdot W\,dz=0.
}
\]

Thus the convective nonlinearity is exactly absent from this ledger.

### Pressure

\[
\int \nabla\Pi\cdot W
=-\int \Pi\,\operatorname{div}W.
\]

### Viscosity

On `a>1`,

\[
V=an,
\qquad
W=(a-1)n.
\]

Using `n·partial_k n=0`,

\[
\nabla V:\nabla W
=|
abla a|^2+a(a-1)|\nabla n|^2.
\]

Define

\[
\boxed{
\mathcal D_{exc}
:=
\int_{a>1}
\left(
|\nabla a|^2
+a(a-1)|\nabla n|^2
\right)dz.
}
\]

Then

\[
\boxed{
\frac{d\mathcal G}{d\sigma}
+\nu\mathcal D_{exc}
=
\int \Pi\,\operatorname{div}W\,dz.
}
\]

This is the exact dynamic ledger for the high-amplitude excess.

## 4. Viscous coercivity of the excess

Again on `a>1`,

\[
|\nabla W|^2
=
|\nabla a|^2
+(a-1)^2|\nabla n|^2.
\]

Since

\[
a(a-1)\ge(a-1)^2,
\qquad a\ge1,
\]

we obtain

\[
\boxed{
\mathcal D_{exc}
\ge
\|\nabla W\|_2^2.
}
\]

The W1 Type-I envelope confines the active set to one fixed normalized ball `B_{R_*}` once the threshold is in the late defect regime. Since `W` vanishes outside the active set, `W in H_0^1(B_{R_*})` in the weak sense and Poincare gives

\[
\|\nabla W\|_2^2
\ge
c_{P,R_*}\|W\|_2^2.
\]

Therefore

\[
\boxed{
\mathcal D_{exc}
\ge
2c_{P,R_*}\mathcal G.
}
\]

## 5. Uniform normalized pressure oscillation on the defect annulus

The pressure satisfies

\[
\Pi=R_iR_j(V_iV_j)
\]

up to a scalar gauge.

We need only an `L2` oscillation bound on the fixed normalized region supporting the defect, not a global pressure norm.

Split the source into three parts.

### (i) Rescaled finite Leray core

The original finite normalized core `|Y|<=R0` becomes

\[
|z|\le\lambda R_0,
\qquad
\lambda=L\sqrt{T_*-t}.
\]

Its rescaled kinetic mass is

\[
\int_{|z|\le\lambda R_0}|V|^2dz
=
\lambda
\int_{|Y|\le R_0}|U|^2dY
=O(\lambda).
\]

For evaluation on a fixed annulus separated from zero, its pressure contribution is therefore `O(lambda)` by the degree `-3` pressure kernel.

### (ii) Near-zero tail part

For

\[
\lambda R_0<|z|<\varepsilon/2,
\]

the Type-I envelope gives

\[
|V(z)|\le A_0/|z|.
\]

Hence

\[
\int_{|z|<\varepsilon/2}|V|^2dz
\le C A_0^2\varepsilon+O(\lambda).
\]

Because this source is separated from the fixed active annulus, its pressure contribution there is uniformly bounded for fixed `epsilon`.

### (iii) Source away from zero

For

\[
|z|\ge\varepsilon/2,
\]

\[
|V|\le A_0/|z|,
\]

so

\[
\int_{|z|\ge\varepsilon/2}|V|^4dz
\le C(A_0,\varepsilon)<\infty.
\]

Thus

\[
V_iV_j\in L^2
\]

uniformly on this truncated source class, and Calderon--Zygmund boundedness gives a uniform `L2` pressure bound.

Combining the three pieces, on the fixed ball/annulus containing the active excess there exists a gauge `c(sigma)` and a constant

\[
P_*<\infty
\]

such that along the late W1 defect corridor

\[
\boxed{
\|\Pi-c(\sigma)\|_{L^2(B_{R_*})}
\le P_*.
}
\]

This is consistent with the earlier finite-parent pressure locality audit: arbitrarily remote pressure sources cannot supply fixed local pressure action.

## 6. First-hitting argument

For arbitrary smooth initial data in the retained setting, every fixed compact time interval strictly before `T_*` has a bounded velocity. Therefore for sufficiently large `L`, the normalized high-amplitude excess is initially absent before the late singular corridor.

If a later defect event satisfies

\[
\mathcal G\ge g_*,
\]

choose a first time `sigma_*` at which

\[
\mathcal G(\sigma_*)=g_0,
\qquad
0<g_0<g_*,
\]

with `g0` fixed.

At this first hitting,

\[
\mathcal G'(\sigma_*)\ge0.
\]

The exact ledger then gives

\[
\int \Pi\,\operatorname{div}W\,dz
\ge
\nu\mathcal D_{exc}.
\]

Using the coercive lower bound,

\[
\nu\mathcal D_{exc}
\ge
2\nu c_{P,R_*}g_0.
\]

Since

\[
\int\operatorname{div}W=0,
\]

subtract the pressure gauge `c(sigma_*)` and use Cauchy--Schwarz:

\[
2\nu c_{P,R_*}g_0
\le
P_*\|\operatorname{div}W\|_2.
\]

Therefore

\[
\boxed{
\|\operatorname{div}W\|_2
\ge
\frac{2\nu c_{P,R_*}g_0}{P_*}
=:d_*>0.
}
\]

## 7. Direction-compression interpretation

M5-22 gives

\[
\operatorname{div}W
=-\mathbf1_{\{|V|>1\}}\operatorname{div}n.
\]

Hence every first creation of a fixed normalized high-amplitude excess satisfies

\[
\boxed{
\|\mathbf1_{\{|V|>1\}}\operatorname{div}n\|_2
\ge d_*>0.
}
\]

Equivalently, because

\[
V\cdot\nabla|V|
=-|V|^2\operatorname{div}n,
\]

the defect-forming event has a fixed streamline-amplitude transport floor.

## 8. Dynamic collapse of the M5-22 dichotomy

M5-22 says an already existing positive excess contains either

1. solenoidal critical content, or
2. a gradient/Hodge direction-compression component.

M5-23 adds a dynamic distinction:

\[
\boxed{
\text{first creation of the excess}
\Longrightarrow
\text{gradient/Hodge pressure-coupled source is mandatory}.
}
\]

The solenoidal/helical component may participate in the mature defect, but it cannot by itself create positive `G` in this convex truncation ledger because

- advection cancels exactly;
- pressure is orthogonal to the solenoidal component;
- viscosity is dissipative.

Thus the actual formation source is the Hodge/direction-compression branch.

## 9. Physical scaling of the floor

Since

\[
z=L(x-X_*),
\qquad
\operatorname{div}_z n
=L^{-1}\operatorname{div}_x n,
\]

we have

\[
\int |\operatorname{div}_z n|^2dz
=
L
\int |\operatorname{div}_x n|^2dx.
\]

Therefore the normalized floor becomes

\[
\boxed{
\int_{\{|u|>L\}}
|\operatorname{div}_x(u/|u|)|^2dx
\ge
\frac{d_*^2}{L}
}
\]

at the corresponding first-hitting event, modulo the same localized active region.

This scaling is compatible with a critical cascade and is not by itself a contradiction.

## 10. What remains open

The new result removes a purely solenoidal creation mechanism, but it does not prove that the required sequence of direction-compression events has infinite physical cost.

Indeed the physical `L2` direction-compression floor scales like `L^{-1}` per threshold event, which is summable over geometric `L` if treated as an ordinary additive cost.

A successful continuation must therefore connect this first-hitting direction-compression floor to a genuinely critical nonintegrable quantity, for example:

- the `D3` direction term;
- the critical amplitude-transport norm;
- a Vasseur-type direction criterion at the correct spacetime exponents;
- or a recurrence/phase-space argument preventing repeated first-hitting formation across nested thresholds.

This is the M5-24 target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
