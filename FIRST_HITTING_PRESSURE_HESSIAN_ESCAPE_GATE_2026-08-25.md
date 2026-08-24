# First-hitting pressure-Hessian escape gate

Date: 2026-08-25

Status: **ACTIVE CALCULATION — GLOBAL REGULARITY NOT PROVED**

## 1. Setup

Let

\[
A=\nabla u,
\qquad
M(t)=\|A(t)\|_{L^\infty(\mathbb R^3)}.
\]

Work on a compact pre-singular interval on which the smooth solution exists.  Use the running maximum

\[
\overline M(t)=\max_{0\le s\le t}M(s).
\]

Fix `q>1` and first-hitting levels

\[
M_j=q^jM_0,
\qquad
r_j=\left(\frac{\nu}{M_j}\right)^{1/2},
\]

with hitting times

\[
t_j=\inf\{t:\overline M(t)=M_j\}.
\]

On `I_j=(t_{j-1},t_j)` one has

\[
M_{j-1}\le \overline M(t)\le M_j.
\]

The running maximum is used to avoid a false assumption that the raw norm `M(t)` remains above `M_{j-1}` after its first hit.

---

## 2. Exact gradient equation and maximum-norm inequality

Differentiating Navier-Stokes gives

\[
\partial_tA+u\cdot\nabla A+A^2=-\nabla^2p+\nu\Delta A.
\]

For

\[
\Phi=\frac12|A|^2,
\]

one obtains

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\Phi
=-A:A^2-A:\nabla^2p-\nu|\nabla A|^2.
\]

At a spatial maximum of `|A|^2`, the transport term vanishes and the scalar Laplacian has the favorable sign.  Hence, in upper-Dini/a.e. norm-derivative form,

\[
\boxed{
D^+M(t)
\le
M(t)^2+\|\nabla^2p(t)\|_\infty.
}
\]

The viscosity contribution does **not** create a positive high-derivative escape at this maximum-norm level; it is favorable.

On the contact set where `\overline M=M` and `\overline M'>0`, therefore,

\[
\boxed{
\frac{\overline M'}{\overline M^2}
\le
1+\Pi_M(t),
\qquad
\Pi_M(t):=rac{\|\nabla^2p(t)\|_\infty}{M(t)^2}.
}
\]

Status: **PROVED for smooth pre-singular solutions, with the standard running-maximum/Dini interpretation.**

---

## 3. Correct first-hitting time normalization

Since

\[
\frac{d}{dt}\frac1{\overline M}
=-\frac{\overline M'}{\overline M^2},
\]

integration over one hitting epoch gives

\[
\int_{I_j}
\frac{\overline M'}{\overline M^2}\,dt
=
\frac1{M_{j-1}}-\frac1{M_j}
=
\frac{1-q^{-1}}{M_{j-1}}.
\]

Define the dimensionless parabolic epoch length

\[
\boxed{
\Theta_j
:=M_{j-1}(t_j-t_{j-1})
=\frac{\nu(t_j-t_{j-1})}{r_{j-1}^2}.
}
\]

Then

\[
\boxed{
1-q^{-1}
\le
\Theta_j
+M_{j-1}\int_{I_j\cap\{\overline M=M\}}\Pi_M(t)\,dt.
}
\]

Thus a strongly compressed hitting epoch, `Theta_j << 1`, requires a fixed normalized time-integrated pressure-Hessian burden.

This corrects the dimensional bookkeeping of the informal `r^2` first-hitting formula: with viscosity retained, the natural time is `r^2/nu`.

---

## 4. Pointwise pressure-Hessian decomposition

The pressure obeys

\[
-\Delta p
=\partial_i u_j\,\partial_j u_i
=:f,
\qquad
|f|\le |A|^2.
\]

A second derivative of the Newtonian potential has the Calderon-Zygmund representation

\[
\nabla^2p
=c\,f+\operatorname{p.v.}K*f,
\qquad
|K(z)|\lesssim |z|^{-3},
\]

with angular mean zero for the principal-value kernel.

At any point `x`, split at radius `r>0`.

### 4.1 Near field

Using kernel cancellation,

\[
\left|
\operatorname{p.v.}\int_{|z|<r}K(z)f(x-z)\,dz
\right|
\lesssim
r\|\nabla f\|_\infty.
\]

Because

\[
\|\nabla f\|_\infty
\lesssim
M\,\|\nabla A\|_\infty,
\]

we obtain

\[
|P_{\rm near}|
\lesssim
M^2+rM\|\nabla A\|_\infty.
\]

Choose the natural radius

\[
r(t)=\left(\frac\nu{M(t)}\right)^{1/2}.
\]

Define

\[
\boxed{
H_{2,r}
:=
\frac{r\|\nabla A\|_\infty}{M}
=
\frac{r^3}{\nu}\|\nabla^2u\|_\infty.
}
\]

Then

\[
\frac{|P_{\rm near}|}{M^2}
\lesssim
1+H_{2,r}.
\]

### 4.2 Far field

Let

\[
R_\ell=2^\ell r,
\qquad
\mathcal A_\ell=\{R_\ell<|z|<2R_\ell\},
\]

and define the critical shell gradient cost

\[
\boxed{
J_\ell(r,t)
:=
\frac{R_\ell}{\nu^2}
\int_{x-\mathcal A_\ell}|\nabla u(y,t)|^2\,dy.
}
\]

Then

\[
\frac{|P_{\rm far}(x,t)|}{M^2}
\lesssim
\sum_{\ell\ge0}2^{-4\ell}J_\ell(r,t).
\]

Indeed,

\[
R_\ell^{-3}
\int_{x-\mathcal A_\ell}|A|^2
\cdot\frac{r^4}{\nu^2}
=
2^{-4\ell}
\frac{R_\ell}{\nu^2}
\int_{x-\mathcal A_\ell}|A|^2.
\]

Define

\[
\boxed{
\mathcal T_r(t)
:=
\sup_x\sum_{\ell\ge0}2^{-4\ell}J_\ell(r,t;x).
}
\]

Therefore

\[
\boxed{
\Pi_M(t)
\lesssim
1+H_{2,r(t)}(t)+\mathcal T_{r(t)}(t).
}
\]

The `2^{-4 ell}` weight is the same physical decay order that appears in the existing affine-free remote-pressure track.

Status: **PROVED as a smooth pointwise Calderon-Zygmund near/far estimate.**

---

## 5. Compressed-epoch dichotomy

On contact times in `I_j`, `M(t)` differs from `M_{j-1}` by at most the fixed factor `q`, hence `r(t)` is comparable with `r_{j-1}`.

Combining the previous sections gives

\[
\boxed{
1-q^{-1}
\lesssim
\Theta_j
+
M_{j-1}\int_{I_j\cap\{\overline M=M\}}
\left[H_{2,r(t)}+\mathcal T_{r(t)}\right]dt.
}
\]

Consequently, if `Theta_j` is sufficiently small, at least one of the following must carry a fixed normalized time occupancy:

1. local normalized velocity-Hessian concentration `H_{2,r}`;
2. remote dyadic shell-gradient pressure tail `mathcal T_r`.

In particular,

\[
\boxed{
\Theta_j\to0
\Longrightarrow
\text{time-integrated }H_{2,r}\text{ escape}
\ \lor\ 
\text{time-integrated remote shell-tail escape}.
}
\]

The direct positive viscosity/higher-derivative branch is pruned at this stage.

---

## 6. Crude energy tax of the remote branch

Using only total gradient energy,

\[
\mathcal T_r(t)
\lesssim
\frac{r}{\nu^2}\|\nabla u(t)\|_2^2.
\]

Therefore a fixed remote-tail burden over a compressed epoch forces

\[
\boxed{
\nu\int_{I_j}\|\nabla u(t)\|_2^2dt
\gtrsim
\nu^2r_{j-1},
}
\]

up to constants depending on the fixed compression threshold and `q`.

This is a real first-order energy cost, but for geometrically shrinking `r_j` the series `sum_j r_j` converges.  Hence this estimate **does not by itself contradict the global energy inequality**.

Status: **PROVED CONDITIONAL ENERGY TAX; NO GLOBAL CONTRADICTION.**

---

## 7. Audit verdict

- gradient maximum equation: **PROVED**;
- viscosity is favorable at the maximum: **PROVED**;
- compressed gradient first-hitting implies pressure-Hessian occupancy: **PROVED**;
- pressure Hessian splits into normalized local `nabla^2 u` concentration or `2^{-4 ell}` remote shell tail: **PROVED**;
- remote branch pays `O(nu^2 r_j)` energy per occupied epoch: **PROVED CONDITIONAL**;
- geometric sum of those costs diverges: **FALSE**;
- compressed epochs are thereby excluded: **NOT DERIVED**;
- global regularity: **UNPROVED**.

## 8. Next use

The pressure route should now be compared with the pressure-free vorticity first-hitting route.  The latter is potentially stronger because the far strain field can be controlled by an `L^2` vorticity/enstrophy window, which is directly connected to the global energy dissipation ledger.
