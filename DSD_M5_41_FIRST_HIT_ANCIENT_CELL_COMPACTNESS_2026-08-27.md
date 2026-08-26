# DSD M5-41 — First-Hit Ancient Cell Compactness

Date: 2026-08-27

Status: **W1-SPECIFIC ANCIENT-CELL EXTRACTION / COMPLETE W1 ORBIT REPRESENTATION DERIVED / FIRST-HIT HISTORY PASSES FOR NEGATIVE TIMES / TERMINAL TRACE REQUIRES THE EXISTING PHASE-CELL COMPACTNESS / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

Let `L_j -> infinity` be a sequence of physical velocity thresholds at which the W1 critical tail produces a fixed positive normalized excess. Choose first-hit times `t_j < T_*` so that a fixed positive excess level is first reached at `t_j`.

Write

\[
\tau_j:=T_*-t_j,
\qquad
\lambda_j:=L_j\sqrt{\tau_j}.
\]

The W1 boundary-defect regime corresponds to the joint limit

\[
\boxed{L_j\to\infty,\qquad \lambda_j\to0.}
\]

Define the physical parabolic blow-up around `(X_*,t_j)` by

\[
\boxed{
V_j(z,\sigma)
:=
L_j^{-1}
 u\!\left(
 X_*+\frac z{L_j},
 t_j+\frac{\sigma}{L_j^2}
 \right).
}
\]

Each `V_j` solves the 3D incompressible Navier--Stokes equations with the same viscosity `nu` on its lifespan.

The original singular time `T_*` becomes

\[
\sigma_j^*
=L_j^2(T_*-t_j)
=\lambda_j^2\to0.
\]

Hence every fixed negative interval `[-S,0]` lies in the smooth lifespan of `V_j` for large `j`, while the positive forward horizon collapses to zero.

---

## 2. Exact relation to Leray variables

Let

\[
s=-\log(T_*-t),
\qquad
U(Y,s)=\sqrt{T_*-t}\,u(x,t),
\qquad
Y=\frac{x-X_*}{\sqrt{T_*-t}}.
\]

Set

\[
a_j:=2\log L_j,
\qquad
U_j^\#(Y,\eta):=U(Y,a_j+\eta).
\]

For

\[
t=t_j+\frac\sigma{L_j^2},
\]

one has

\[
T_*-t
=\frac{\lambda_j^2-\sigma}{L_j^2},
\]

and therefore exactly

\[
\boxed{
V_j(z,\sigma)
=
(\lambda_j^2-\sigma)^{-1/2}
U_j^\#\!\left(
\frac z{\sqrt{\lambda_j^2-\sigma}},
-\log(\lambda_j^2-\sigma)
\right).
}
\]

This formula is the key W1-specific bridge.

---

## 3. Complete W1 orbit extraction

The W1 late orbit is precompact in the local smooth topology used throughout the recurrent reduction. Since

\[
a_j=2\log L_j\to\infty,
\]

a subsequence of the time translates `U_j^#` converges on compact subsets of `(Y,eta)` to a complete W1 trajectory

\[
U^\#(Y,\eta),
\qquad \eta\in\mathbb R.
\]

Thus for every fixed `sigma<0`,

\[
\lambda_j^2-\sigma\to-\sigma,
\]

and the preceding exact relation gives

\[
\boxed{
V_j(z,\sigma)
\longrightarrow
V_*(z,\sigma)
:=
(-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{-\sigma}},
-\log(-\sigma)
\right)
}
\]

locally smoothly away from any terminal singular point.

Therefore `V_*` is a one-sided ancient Navier--Stokes solution on

\[
\boxed{\mathbb R^3\times(-\infty,0).}
\]

It is not an arbitrary ancient profile: it is exactly the inverse-Leray image of one complete recurrent W1 orbit.

---

## 4. First-hit history

Use the quadratic excess functional

\[
\mathcal G(V)
:=
\frac12\int_{\mathbb R^3}(|V|-1)_+^2\,dz.
\]

Choose the first-hit normalization so that

\[
\mathcal G(V_j(0))=g_0>0
\]

and

\[
\mathcal G(V_j(\sigma))<g_0
\qquad(\sigma<0)
\]

for every preterminal time in the corresponding first-hit interval.

For a fixed `sigma<0`, the threshold `|V_j|>1` corresponds in Leray variables to

\[
|U_j^#|>\sqrt{\lambda_j^2-\sigma}.
\]

Since this threshold stays strictly positive and W1 has the `1/|Y|` tail envelope, the active set is contained in a fixed finite Leray ball. Hence local convergence is sufficient to pass the excess functional, giving

\[
\boxed{
\mathcal G(V_*(\sigma))\le g_0
\qquad\forall\sigma<0.
}
\]

Strict inequality may be lost in the subsequential limit and is not claimed.

---

## 5. Terminal mark

At `sigma=0`,

\[
V_j(z,0)
=\lambda_j^{-1}
U\!\left(\frac z{\lambda_j},s_j\right),
\]

so the terminal slice is exactly the W1 joint boundary blow-down

\[
\lambda_j\downarrow0,
\qquad
|Y|\sim\lambda_j^{-1}.
\]

The M5-21--29 fixed phase-cell compactness and the uniform `1/|z|` envelope give local compactness of this terminal family. After a further subsequence, one obtains a terminal trace `V_0` satisfying

\[
\boxed{
\mathcal G(V_0)=g_0>0.
}
\]

The suitable/local-energy compactness needed to identify `V_0` as the terminal trace of `V_*` is the same Type-I ancient compactness mechanism used in standard blow-up extraction. Under the retained W1 local compactness hypotheses, this is the natural terminal object.

What is **not** claimed is smooth extendibility through `sigma=0`.

---

## 6. Type-I / weak-critical character

For every fixed `sigma<0`, `V_*` is smooth and bounded locally. At spatial infinity it retains the W1 critical `1/|z|` tail. Therefore the ancient cell is naturally in the weak critical class

\[
V_*(\sigma)\in L^{3,\infty}_{loc/global\;weak\;sense},
\]

while strong global `L^3` may fail logarithmically.

This is precisely why the standard Liouville theorem requiring bounded strong `L^3` along a backward sequence is not automatically applicable.

---

## 7. Literature anchor

Albritton--Barker prove that local Type-I singularities are equivalent to the existence of nontrivial bounded mild ancient solutions satisfying Type-I decay, and they prove a Liouville theorem when an ancient solution is bounded in strong `L^3` along a backward sequence.

The present W1 ancient cell lies on the weak-critical side of that frontier because the inherited `1/r` tail is compatible with `L^{3,\infty}` but not with global strong `L^3`.

Thus the ancient extraction itself does not close M5; it relocates the endpoint into a sharper same-trajectory ancient-cell problem.

---

## 8. DSD interpretation

The first-hit ancient cell separates three layers:

1. **prelimit physical history:** smooth finite-energy solution before `T_*`;
2. **complete recurrent W1 orbit:** the normalized internal dynamics;
3. **terminal projective boundary:** `lambda -> 0`, `|Y| -> infinity`, `lambda|Y|=O(1)`.

The ancient cell is the exact spacetime object obtained by gluing layers 2 and 3 through the physical parabolic scaling.

Hence the final endpoint cannot be dismissed as a static boundary artifact. It has a same-trajectory ancient Navier--Stokes ancestry.

---

## 9. Updated target

A successful continuation from M5-41 must now rule out a nonzero one-sided ancient cell satisfying simultaneously:

- inverse-Leray representation by a complete recurrent W1 orbit;
- first-hit history `G(sigma)<=g_0` for all `sigma<0`;
- nonzero terminal excess `G(V_0)=g_0`;
- weak-critical `1/r` far-field ancestry;
- the M5-23--40 threshold-Hodge / direction-compression / strict pressure-tail formation constraints at the terminal hit.

No contradiction is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
