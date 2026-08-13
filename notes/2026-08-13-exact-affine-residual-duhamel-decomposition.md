# Exact affine/residual Duhamel decomposition for the full vorticity equation

Date: 2026-08-13

Status: **EXACT NONAUTONOMOUS AFFINE DUHAMEL IDENTITY + RESIDUAL DEFECT CHANNEL / DEFECT-TO-EXISTING-BUDGET CLOSURE OPEN**.

The previous frontier asked for a perturbative theorem comparing the nonlinear first-hitting window with an optimal affine model.  A more precise starting point is available: for **any** chosen trace-free matrix path `L(t)`, the full vorticity equation splits exactly into a solvable affine advection--stretch--diffusion propagator plus a residual nonlinear Duhamel term.

Thus the phrase “the affine approximation breaks down” can be replaced by a quantitative residual-defect norm.

The remaining task is to bound this defect by the already typed Cauchy-V, BMO residual, shell, pressure, and derivative channels.

---

## 1. Choose an affine matrix path

Let

\[
L(t)\in\mathbb R^{3\times3},
\qquad
\operatorname{tr}L(t)=0.
\]

For DSD/local work, the preferred choice is the optimal local affine representative

\[
L=L_\phi(t)
=\frac{\int\phi\nabla u}{\int\phi},
\]

but the algebra below is valid for any trace-free `L(t)`.

Define the residual velocity

\[
\boxed{
v(x,t)=u(x,t)-L(t)x.
}
\]

Since

\[
\nabla\cdot u=0
\]

and

\[
\operatorname{tr}L=0,
\]

we have

\[
\boxed{\nabla\cdot v=0.}
\]

Although `v` grows linearly at spatial infinity when `L !=0`, the decomposition is algebraically exact on the smooth lifespan; for rapidly decaying vorticity the residual fluxes below are interpreted in the natural weighted/distributional sense.

---

## 2. Exact split of the vorticity equation

The full equation is

\[
\partial_t\omega
+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u
+\nu\Delta\omega.
\]

Insert

\[
u=Lx+v.
\]

Because

\[
(\omega\cdot\nabla)(Lx)=L\omega,
\]

we obtain

\[
\boxed{
\partial_t\omega
+(Lx)\cdot\nabla\omega
=L\omega+\nu\Delta\omega
+f_{\rm res},
}
\]

where

\[
\boxed{
f_{\rm res}
=(\omega\cdot\nabla)v-(v\cdot\nabla)\omega.}
\]

This is exact; no smallness or locality approximation has been made.

---

## 3. Residual source as curl/divergence of a flux

Since

\[
\nabla\cdot v=0,
\qquad
\nabla\cdot\omega=0,
\]

the standard vector identity gives

\[
\boxed{
f_{\rm res}=\nabla\times(v\times\omega).}
\]

Equivalently,

\[
\boxed{
f_{\rm res}
=\nabla\cdot(v\otimes\omega-\omega\otimes v).}
\]

Thus the non-affine defect is a conservative residual vorticity-flux channel.

This is useful because derivative heat-kernel estimates may be applied directly to the residual flux tensor rather than to `grad omega` and `grad v` separately.

---

## 4. Nonautonomous affine propagator

Let

\[
F_L(t,s)
\]

solve

\[
\partial_tF_L(t,s)=L(t)F_L(t,s),
\qquad
F_L(s,s)=I.
\]

Because `tr L=0`,

\[
\det F_L(t,s)=1.
\]

Define the accumulated heat matrix in the `s`-reference coordinates

\[
\boxed{
C_L(t,s)
=\int_s^t
F_L(\tau,s)^{-1}
F_L(\tau,s)^{-T}d\tau.
}
\]

The homogeneous affine propagator is

\[
\boxed{
(\mathcal U_L(t,s)f)(x)
=F_L(t,s)
\left[
 e^{\nu C_L(t,s):D^2}f
\right]
(F_L(t,s)^{-1}x).
}
\]

This solves

\[
\partial_t w+(Lx)\cdot\nabla w
=Lw+\nu\Delta w.
\]

---

## 5. Exact Duhamel formula

The full vorticity therefore satisfies

\[
\boxed{
\omega(t_1)
=\mathcal U_L(t_1,t_0)\omega(t_0)
+\int_{t_0}^{t_1}
\mathcal U_L(t_1,s)f_{\rm res}(s)ds.
}
\]

Define

\[
\boxed{
H_L
=\|\mathcal U_L(t_1,t_0)\omega(t_0)\|_\infty
}
\]

and

\[
\boxed{
\mathfrak R_L
=\left\|
\int_{t_0}^{t_1}
\mathcal U_L(t_1,s)f_{\rm res}(s)ds
\right\|_\infty.
}
\]

Then exactly

\[
\boxed{
\|\omega(t_1)\|_\infty
\le H_L+\mathfrak R_L.
}
\]

---

## 6. Exact first-hitting half-split

Suppose

\[
\|\omega(t_1)\|_\infty=qW_0,
\qquad
W_0=\|\omega(t_0)\|_\infty.
\]

Then at least one of

\[
\boxed{
H_L\ge\frac{qW_0}{2}
}
\]

or

\[
\boxed{
\mathfrak R_L\ge\frac{qW_0}{2}
}
\]

must hold.

This is the exact nonlinear affine/residual dichotomy.

There is no need to say informally that the affine approximation is “good” or “bad”: the residual defect is an explicit term.

---

## 7. Homogeneous affine branch and the strain-energy/reservoir capacity

Let

\[
q_L=\|F_L(t_1,t_0)\|_{op}.
\]

The homogeneous affine heat estimate gives, schematically for `q_L>=2`,

\[
H_L
\lesssim
q_L^{1/2}
(J_L/\nu)^{1/2}
M_{\Pi,L},
\]

where

\[
J_L
=\int_{t_0}^{t_1}
\|\operatorname{sym}L(t)\|_{op}^2dt
\]

and

\[
M_{\Pi,L}
=\|\omega(t_0)\|_{L^\infty L^2_{\rm two\ strong\ heat\ directions}}.
\]

If

\[
H_L\ge qW_0/2,
\]

then

\[
\boxed{
q_LJ_LM_{\Pi,L}^2
\gtrsim
\nu q^2W_0^2.
}
\]

Thus the exact endpoint dichotomy may be written

\[
\boxed{
\mathfrak R_L
\ge\frac{qW_0}{2}
\quad\text{or}\quad
q_LJ_LM_{\Pi,L}^2
\gtrsim
\nu q^2W_0^2.
}
\]

The second alternative is the **affine capacity** branch.

For `q_L<2`, the elementary heat contraction gives

\[
H_L\le q_LW_0<2W_0,
\]

so for large target `q` the residual branch is automatic.

---

## 8. Trace reduction of the affine capacity

The precursor mixed norm satisfies

\[
M_{\Pi,L}^4
\le4E_0P_{e_1}.
\]

Therefore the affine-capacity branch implies

\[
\boxed{
q_LJ_L(E_0P_{e_1})^{1/2}
\gtrsim
\nu q^2W_0^2.
}
\]

If the affine stretch `q_L`, affine strain-energy `J_L`, and initial derivative/enstrophy reservoir all remain bounded relative to the chosen normalization, then adaptive selection of a sufficiently large target `q` forces the residual Duhamel branch.

---

## 9. Residual Duhamel defect as the new primary nonlinear channel

The exact source is

\[
f_{\rm res}
=\nabla\cdot
(v\otimes\omega-\omega\otimes v).
\]

Thus

\[
\boxed{
\mathfrak R_L
=\left\|
\int
\mathcal U_L
\nabla\cdot
(v\otimes\omega-\omega\otimes v)
\right\|_\infty.
}
\]

The next proof-producing task is to dominate this quantity by a small number of already typed residual channels.

Candidates include

- mean-free strain/BMO source;
- weighted residual-velocity oscillation;
- shell/buffer flux;
- pressure-difference coupling after localization;
- Cauchy-V/high-derivative events;
- material deformation not represented by `L`;
- weighted spatial moments such as `|x| omega`, which arise because `v=u-Lx` has linear growth at infinity.

---

## 10. Relation to Cauchy I/V

The affine/residual Duhamel decomposition and the Cauchy I/V decomposition are **different exact decompositions** of the same amplification.

Cauchy I/V:

\[
\text{full material deformation}
+\text{viscous rewrite}.
\]

Affine Duhamel:

\[
\text{chosen coherent affine evolution}
+\text{non-affine Eulerian residual flux}.
\]

Intersecting them is useful:

- large affine capacity can be compared with the full material I-lane;
- large residual Duhamel defect must arise from non-affine deformation/transport or viscous activity and can be cross-typed with the Cauchy decomposition.

Neither decomposition replaces the other.

---

## 11. DSD interpretation

The new exact state block is

\[
\boxed{
(H_L,\mathfrak R_L;
q_L,J_L,M_{\Pi,L}).
}
\]

The affine part is the low-dimensional structural representative.  Everything it fails to explain is not discarded; it appears exactly as the residual Duhamel defect.

This is a cleaner realization of adaptive describability than postulating a perturbation threshold before writing the exact remainder.

---

## 12. Current target

The frontier is no longer “prove an affine perturbation theorem” in the abstract.

It is now the more concrete estimate

\[
\boxed{
\mathfrak R_L
\le
\mathcal F(
\text{BMO residual},
\text{shell flux},
\text{pressure},
\text{Cauchy-V},
\text{deformation},
\text{moments}
),
}
\]

and then show that a residual defect of order `q W0` forces one of those channels into a previously excluded/expensive regime.

Status: **EXACT NONLINEAR AFFINE/RESIDUAL DICHOTOMY CLOSED / RESIDUAL DUHAMEL DEFECT ESTIMATE IS THE ACTIVE FRONTIER**.
