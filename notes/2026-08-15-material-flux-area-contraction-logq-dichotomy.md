# Material-flux area-contraction `log q` dichotomy

Date: 2026-08-15

Status: **DERIVED ON THE COHERENT CRITICAL-CROSSING TRACK. IF A ROBUST MATERIAL VORTICITY FLUX IS NOT CREATED/DESTROYED VISCOUSLY BETWEEN THE PREVIOUS FIRST-HITTING CHECKPOINT AND THE COHERENT CROSSING, THEN THE MATERIAL CROSS-SECTION CARRYING THAT FLUX MUST CONTRACT IN AREA BY A FACTOR COMPARABLE TO THE AMPLIFICATION RATIO `q`, FORCING `log q` OF SURFACE-AVERAGED NORMAL STRAIN AND AT LEAST `log q` OF `L^infinity` STRAIN ACTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Previous checkpoint and coherent crossing

Work in terminal normalization. Let the previous adaptive first-hitting checkpoint be `t_-`, so

\[
\boxed{\|\Omega(t_-)\|_\infty\le q^{-1}.}
\]

Let `t_c` be the coherent Reynolds-one crossing. On a robust family of cross-sections inside the coherent core there is a fixed `kappa>0` such that

\[
\boxed{
|\Phi_c|
:=
\left|
\int_{S_c}\Omega(t_c)\cdot n_c\,dA
\right|
\ge \kappa R_c^2,
}
\]

while

\[
\boxed{|S_c|\le C_0R_c^2.}
\]

Here `S_c` is understood as a terminal member of the material family identified by the coherent-core construction.

Trace the same material surface backward to `t_-` and denote it by `S_-`.

## 2. Flux-change / flux-retention dichotomy

Fix

\[
0<\eta<1.
\]

There are two alternatives.

### A. Material-flux change

\[
\boxed{
|\Phi_c-\Phi_-|
\ge\eta|\Phi_c|.
}
\]

By the exact material vorticity-flux identity,

\[
\Phi_c-\Phi_-
=-\nu\int_{t_-}^{t_c}
\oint_{\partial S(t)}
(\nabla\times\Omega)\cdot d\ell\,dt.
\]

For a robust nested material family, the established material-tube coarea lemma routes this alternative to

\[
\boxed{
\text{bulk palinstrophy / derivative concentration}
\quad\lor\quad
\text{large Lagrangian deformation}.
}
\]

Thus Alternative A is already Branch 1 or Branch 3.

### B. Material-flux retention

Otherwise

\[
|\Phi_c-\Phi_-|
<\eta|\Phi_c|.
\]

Hence

\[
\boxed{
|\Phi_-|
\ge(1-\eta)|\Phi_c|
\ge (1-\eta)\kappa R_c^2.
}
\]

The first-hitting cap at `t_-` gives

\[
|\Phi_-|
\le
\|\Omega(t_-)\|_\infty |S_-|
\le q^{-1}|S_-|.
\]

Therefore

\[
\boxed{
|S_-|
\ge
(1-\eta)\kappa qR_c^2.
}
\]

Compared with the current area,

\[
|S_c|\le C_0R_c^2,
\]

we obtain

\[
\boxed{
\frac{|S_-|}{|S_c|}
\ge c_{\eta,\kappa,C_0}q.
}
\]

Thus retained flux requires a material area contraction by a factor proportional to `q`.

## 3. Exact area evolution of a material surface

Let `S(t)` be a material surface with unit normal `n(x,t)`. The area element satisfies

\[
\frac{D}{Dt}dA
=
\left(\nabla\cdot u-n^T(\nabla u)n\right)dA.
\]

Since the flow is incompressible and the antisymmetric part of `grad u` contributes nothing to `n^T grad u n`,

\[
\boxed{
\frac{D}{Dt}dA
=-n^TSn\,dA.
}
\]

Hence the total area obeys

\[
\boxed{
A'(t)
=-\int_{S(t)}n^TSn\,dA.
}
\]

When `A(t)>0`, define the surface probability measure

\[
d\mu_{S,t}=A(t)^{-1}dA.
\]

Then

\[
\boxed{
\frac d{dt}\log A(t)
=-\int_{S(t)}n^TSn\,d\mu_{S,t}.
}
\]

This is exact.

## 4. `log q` surface-strain action

Integrating from `t_-` to `t_c`,

\[
\log\frac{A_-}{A_c}
=
\int_{t_-}^{t_c}
\int_{S(t)}n^TSn\,d\mu_{S,t}\,dt.
\]

On the flux-retention branch,

\[
A_-/A_c\ge cq.
\]

Therefore

\[
\boxed{
\int_{t_-}^{t_c}
\int_{S(t)}n^TSn\,d\mu_{S,t}\,dt
\ge
\log q-O(1).
}
\]

In particular,

\[
\boxed{
\int_{t_-}^{t_c}
\frac1{A(t)}
\int_{S(t)}|n^TSn|\,dA\,dt
\ge
\log q-O(1).
}
\]

Since

\[
|n^TSn|\le\|S(t)\|_{L^\infty},
\]

we also obtain the global endpoint

\[
\boxed{
\int_{t_-}^{t_c}\|S(t)\|_\infty dt
\ge
\log q-O(1).
}
\]

This recovers a BKM-scale logarithmic action, but with stronger geometric localization: the action is required on the actual material surfaces carrying the coherent vorticity flux.

## 5. Relation to the earlier maximum-vorticity `log q` routing

The earlier maximum-vorticity identity gave

\[
\log q
\le
\int \Lambda_{2,M}dt
+
\int \mathcal E_3dt,
\]

routing pointwise maximum growth to middle-strain or extensional-alignment channels.

The present result is complementary rather than duplicate:

- the earlier statement follows one maximum-vorticity point/direction;
- the present statement follows a positive-area material flux carrier;
- flux retention forces area compression regardless of where the instantaneous maximum lies on the surface;
- flux change is routed to palinstrophy through the material-flux identity.

Thus a coherent crossing has the stronger dichotomy

\[
\boxed{
\text{viscous material-flux change}
\quad\lor\quad
\text{material area contraction }\gtrsim q.
}
\]

## 6. Robust family form

The coherent crossing supplies not merely one cross-section but a positive-measure family of axial labels carrying flux `~R_c^2`.

For every member of a retained subfamily, the same dichotomy applies.

If a fixed fraction of this family lies in the flux-change lane, nested material coarea charges bulk palinstrophy or deformation.

If a fixed fraction lies in the flux-retention lane, a positive family of material surfaces must each carry `log q` normal-strain action.

Thus the coherent-core strain requirement is not confined to one exceptional material label.

A full spacetime volume lower bound for this family-weighted strain action would require an additional coarea/Jacobian estimate and is not asserted here.

## 7. Consequence for the final branch tree

After Branch 2 has been reduced by material-flux tracking, the remaining singular survivor must satisfy, on every sufficiently late adaptive first-hitting step,

\[
\boxed{
\text{derivative/palinstrophy concentration}
\quad\lor\quad
\int_{I_j}\|S\|_\infty dt
\ge\log q_j-O(1).
}
\]

The second alternative is the genuine Branch 3 critical-strain saturation lane.

Since `q_j` may be chosen adaptively large from a smooth checkpoint, this says that any late singular survivor must repeatedly produce correspondingly large material-surface contraction action unless it repeatedly activates the derivative concentration lane.

This is a necessary condition, not yet a contradiction: BKM-type blowup itself requires divergent strain/vorticity action.

Status: **MATERIAL FLUX RETENTION FORCES `q`-FACTOR AREA CONTRACTION AND `log q` SURFACE-NORMAL STRAIN ACTION / FLUX CHANGE RETURNS TO DERIVATIVE-PALINSTROPHY / BRANCH 3 REDUCED TO REPEATED MATERIAL-AREA-CONTRACTION STRAIN SATURATION / GLOBAL REGULARITY NOT PROVED.**
