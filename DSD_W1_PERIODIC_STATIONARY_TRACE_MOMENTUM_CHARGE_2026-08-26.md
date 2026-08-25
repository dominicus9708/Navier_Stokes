# DSD W1 Periodic Stationary Trace: Momentum Point-Force Charge

Date: 2026-08-26

Status: **FULL-RESIDUAL-ZERO PERIODIC TRACE SPLIT BY A CONSERVED VECTOR MOMENTUM-STRESS CHARGE / NONZERO CHARGE IDENTIFIED DISTRIBUTIONALLY WITH A POINT-FORCE DEFECT / ZERO CHARGE REMOVES THE DELTA DEFECT BUT DOES NOT BY ITSELF PROVE REMOVABILITY AT CRITICAL WEAK-L3 SIZE / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

This note concerns only the stronger subbranch of the H2-coherent periodic W1 tail for which

\[
\boxed{\mathcal N[F_\infty]=0.}
\]

This is much stronger than the scalar condition

\[
\mathfrak A_F
=\langle F_\infty,\mathcal N[F_\infty]\rangle=0.
\]

Here the canonical `r^-3` correction vanishes at first nonresonant order and the physical leading critical trace

\[
T_*(x)
=|x|^{-1}\Phi(\widehat x,\log|x|)
\]

solves the stationary incompressible Navier--Stokes equation on the punctured space

\[
\nu\Delta T_*
-(T_*\cdot\nabla)T_*
-\nabla P_*=0,
\qquad
\nabla\cdot T_*=0,
\qquad x\ne0.
\]

The trace is discretely homogeneous:

\[
T_*(\lambda x)=\lambda^{-1}T_*(x),
\qquad
P_*(\lambda x)=\lambda^{-2}P_*(x).
\]

## 2. Momentum stress tensor

Define

\[
\boxed{
\mathbf T_{mom}
:=
\nu(\nabla T_*+\nabla T_*^T)
-T_*\otimes T_*
-P_*I.
}
\]

Since `div T_*=0`,

\[
\nabla\cdot\mathbf T_{mom}=0
\qquad\text{on }\mathbb R^3\setminus\{0\}.
\]

The symmetric viscous form is used only for the momentum flux; replacing it by `nu grad T_*` changes the tensor by a divergence-free-column term under incompressibility and does not alter the conserved force vector on closed spheres.

## 3. Conserved vector charge

For any sphere not meeting the origin define

\[
\boxed{
\mathbf b(r)
:=
\int_{|x|=r}
\mathbf T_{mom}n\,dS.
}
\]

For `0<r_1<r_2`, the divergence theorem on the annulus gives

\[
\mathbf b(r_2)-\mathbf b(r_1)
=
\int_{r_1<|x|<r_2}
\nabla\cdot\mathbf T_{mom}\,dx
=0.
\]

Hence

\[
\boxed{\mathbf b(r)=\mathbf b_*\quad\forall r>0.}
\]

This is a genuine conserved vector charge of the stationary punctured trace.

## 4. Critical scaling is exactly compatible with a nonzero charge

The trace has degree `-1`, so

\[
\nabla T_*\sim r^{-2},
\qquad
T_*\otimes T_*\sim r^{-2},
\qquad
P_*\sim r^{-2}.
\]

Thus

\[
\mathbf T_{mom}\sim r^{-2}.
\]

Since `dS~r^2`, the flux vector is scale invariant:

\[
\boxed{
\mathbf b(\lambda r)=\mathbf b(r).
}
\]

Therefore discrete homogeneity does not force `b_*` to vanish.

## 5. Distributional point-force interpretation

The stress is locally integrable near the origin because

\[
|\mathbf T_{mom}(x)|\lesssim |x|^{-2},
\qquad
\int_{B_r}|x|^{-2}dx=O(r).
\]

Take a smooth compactly supported test vector `varphi`.  Excise `B_epsilon`, integrate by parts, and let `epsilon->0`.  The bulk divergence vanishes away from the origin, while

\[
\int_{|x|=\epsilon}
\mathbf T_{mom}n\cdot\varphi(x)dS
\to
\mathbf b_*\cdot\varphi(0).
\]

Consequently, up to the sign convention fixed by the outward normal in the definition above,

\[
\boxed{
\nabla\cdot\mathbf T_{mom}
=\mathbf b_*\delta_0
}
\]

in distributions on `R3`.

Thus the only zeroth-order distributional defect detected by the conserved momentum stress is a point-force vector at the singular point.

## 6. Relation to Landau and known isolated-singularity theory

Continuously `(-1)`-homogeneous smooth stationary Navier--Stokes solutions on the punctured space are classified by the classical Landau family (up to the known rotations/parameters).  Landau solutions carry a nonzero point-force vector at the origin in the distributional equation.

Miura--Tsai's isolated-singularity theory shows, under a sufficiently small weak-`L3` hypothesis, that point singularities are characterized by a Landau component associated with this force vector plus a more regular remainder.

The present W1 trace is only known to be critical weak-`L3` and need not be small.  It is also only discretely homogeneous rather than continuously homogeneous.  Therefore neither theorem is imported as a general classification of the present trace.

## 7. Exact stationary-trace split

The full-residual-zero subbranch splits as

\[
\boxed{
\mathcal N[F_\infty]=0
\Longrightarrow
\mathbf b_*\ne0
\quad\lor\quad
\mathbf b_*=0.
}
\]

### Nonzero-force branch

If

\[
\mathbf b_*\ne0,
\]

then the static critical trace is a stationary solution only on the punctured space and represents a distributional point-force solution across the origin:

\[
\nabla\cdot\mathbf T_{mom}
=\mathbf b_*\delta_0.
\]

This is Landau-like at the level of the conserved momentum charge, but no general Landau classification is asserted for a large discretely self-similar trace.

### Zero-force branch

If

\[
\mathbf b_*=0,
\]

then the delta-type momentum defect vanishes.  The stress extends distributionally with zero force through the origin.

However this alone does **not** imply that `T_*` is bounded or smooth at the origin.  Known critical isolated-singularity regularity results require additional hypotheses such as strong `L3`, `o(r^-1)`, or sufficiently small weak-`L3`.  The present nonzero log-periodic critical trace has exactly `r^-1` size and its weak-`L3` norm is not known to be small.

Thus

\[
\boxed{
\mathbf b_*=0
\not\Rightarrow
\text{removable singularity}
}

under the present W1 data alone.

## 8. Relation to the scalar energy charge

The vector momentum charge

\[
\mathbf b_*
\]

and the scalar second-tail energy charge

\[
\mathfrak A_F
\]

encode different information.

If

\[
\mathcal N[F_\infty]=0,
\]

then automatically

\[
\mathfrak A_F=0,
\]

but the converse is false in general because a vector residual can be energy-orthogonal to `F_infty`.

Even under `N[F]=0`, the vector charge `b_*` may be nonzero because the stationary equation is solved only away from the origin.

Thus the hierarchy is

\[
\boxed{
\mathcal N[F]=0
\Longrightarrow
\mathfrak A_F=0,
}
\]

but

\[
\boxed{
\mathcal N[F]=0
\not\Longrightarrow
\mathbf b_*=0.
}
\]

## 9. Connection to the unforced prelimit requires a separate bridge

The original physical Navier--Stokes evolution is unforced before the candidate singular time.  It is tempting to infer that a final stationary trace must therefore have

\[
\mathbf b_*=0.
\]

That inference is not automatic.

The momentum equation on a fixed ball contains the time derivative of the momentum stored in the shrinking inner core.  A self-similar core of radius `sqrt(T-t)` has small instantaneous momentum but can have an order-one time derivative after rescaling.  Such a concentration can in principle converge to a point-force defect in the limiting static trace.

Therefore the missing bridge is an exact no-defect statement of the form

\[
\boxed{
\text{unforced smooth prelimit}
+\text{W1 compactness}
\Longrightarrow
\mathbf b_*=0,
}
\]

and this is **NOT DERIVED** here.

## 10. Updated periodic residual-zero frontier

The H2-coherent periodic branch now has the nested structure

\[
\boxed{
\mathcal N[F]\ne0
\quad\lor\quad
\left(
\mathcal N[F]=0,
\ \mathbf b_*\ne0
\right)
\quad\lor\quad
\left(
\mathcal N[F]=0,
\ \mathbf b_*=0
\right).
}
\]

Interpretation:

1. `N[F]!=0`: the canonical `r^-3` dynamic second tail is nonzero and fully forced;
2. `N[F]=0`, `b_*!=0`: stationary critical point-force trace;
3. `N[F]=0`, `b_*=0`: zero-force stationary critical DSS trace, whose removability at large critical amplitude remains open under current hypotheses.

This is a sharper classification of the periodic coherent tail, not a proof of nonexistence.

## 11. DSD audit

The following are kept separate:

- full vector stationary residual;
- scalar energy pairing of that residual;
- vector momentum-stress point-force charge;
- smooth unforced prelimit versus distributional final-time defect;
- continuous `(-1)` homogeneity versus discrete/log-periodic homogeneity;
- small weak-`L3` isolated-singularity theory versus the unrestricted critical W1 amplitude.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
