# DSD M5-225 — Tail-Core Graph Differentiability Firewall and Orbit-Tangent Linearized Gate

Date: 2026-08-30

Parent: `DSD_M5_222_RESIDUAL_ACTIVE_TAIL_FORCING_WORK_ALIGNMENT_FIREWALL_2026-08-30.md`

Status: **CORRECTION + POSITIVE TANGENT REDUCTION / M5-217 CARLEMAN INJECTIVITY AND M5-218 HOMEOMORPHIC CONJUGACY DO NOT PROVIDE A FRECHET-DIFFERENTIABLE OR LIPSCHITZ TAIL-TO-CORE INVERSE / EXISTING STOKES/NAVIER--STOKES CARLEMAN LITERATURE GIVES HÖLDER OR LOGARITHMIC CONTINUATION STABILITY, NOT THE COERCIVE DIFFERENTIAL RESPONSE REQUIRED BY M5-222 / HOWEVER THE ACTUAL W1 FLOW HAS AN EXACT ORBIT TANGENT `Z=V_s` SOLVING THE HOMOGENEOUS LINEARIZED LERAY EQUATION, WITH PASSIVE-TAIL TANGENT `T_s=-1/2(T+Y dot grad T)` / GLOBAL L2 DIFFERENTIABILITY OF THE QUOTIENT GRAPH IS NOT ASSUMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Topological result already proved

M5-217 gives injectivity of the canonical tail code on the audited compact W1 minimal class:

\[
T_V=T_W
\Longrightarrow
V=W.
\]

M5-114 gives continuity, and compactness therefore upgrades the tail map to a homeomorphism:

\[
\boxed{
\mathfrak T:M\overset{\cong}{\longrightarrow}\mathcal T.
}
\]

Consequently the inverse

\[
\mathfrak T^{-1}:\mathcal T\to M
\]

is uniformly continuous.

This is exactly the input used safely in M5-219.

---

## 2. Homeomorphism does not imply a differential coercivity estimate

The residual-work idea of M5-222 would become much stronger if one could differentiate a tail-to-core graph and obtain a bound such as

\[
\|D\mathfrak T^{-1}_T[\dot T]\|_X
\ge c\|\dot T\|_Y.
\]

Nothing proved so far gives such an estimate.

Even in one dimension the compact homeomorphism

\[
f(x)=x^3,
\qquad x\in[-1,1],
\]

has a continuous inverse but

\[
(f^{-1})'(0)
\]

is unbounded/non-Lipschitz.

Conversely a homeomorphism can have derivative zero at a point while remaining globally injective.

Therefore

\[
\boxed{
\text{continuous injective compact code}
\not\Rightarrow
\text{Lipschitz, differentiable, or tangent-coercive inverse}.
}
\]

---

## 3. Carleman stability literature does not supply the missing derivative

The Carleman theorem used in M5-217 is compatible with quantitative continuation results, but the recovered literature gives weak moduli rather than a uniform differential inverse.

Bellassoued--Imanuvilov--Yamamoto prove Hölder-type conditional stability for a lateral Cauchy problem for the linearized Navier--Stokes system.

Boulakia proves logarithmic stability estimates for the nonstationary Stokes unique-continuation problem without prescribed boundary conditions.

Such estimates are of schematic type

\[
\|z\|_{interior}
\le
C\,\Psi(\|\text{Cauchy data}\|),
\]

with `Psi` Hölder or logarithmic and with a priori norm bounds.

They do not imply a uniform lower tangent estimate for the inverse tail code.

Hence the shortcut

\[
\boxed{
\text{M5-217 injectivity}
\Longrightarrow
D\mathfrak T^{-1}\text{ exists and is coercive}
}
\]

is RED.

---

## 4. The compact minimal set is not an open Banach manifold

There is an even more basic geometric issue.

The domain of the inverse code is the compact tail hull

\[
\mathcal T,
\]

not an open subset of a Banach space.

A Fréchet derivative of

\[
\mathfrak T^{-1}
\]

is therefore not intrinsically defined without first proving that the hull sits in a differentiable invariant manifold and extending the inverse to an open neighborhood.

No such manifold theorem has been established.

Thus a generic notation

\[
D\mathcal Q_T
\]

for the tail-to-quotient graph is presently only formal.

---

## 5. The actual orbit direction is different and is well defined

The preceding firewall does **not** remove the genuine time derivative along an actual smooth W1 orbit.

Let

\[
V(s)=S(s)V_0.
\]

Define

\[
\boxed{Z(s):=V_s(s).}
\]

The W1 smooth compact corridor gives this derivative locally in all finite spatial norms used in the proof.

Differentiate the autonomous Leray equation

\[
V_s
-\nu\Delta V
+\frac12V
+\frac12Y\cdot\nabla V
+(V\cdot\nabla)V
+\nabla P
=0.
\]

Then `Z` satisfies the exact homogeneous linearized Leray system

\[
\boxed{
Z_s
-\nu\Delta Z
+\frac12Z
+\frac12Y\cdot\nabla Z
+(V\cdot\nabla)Z
+(Z\cdot\nabla)V
+\nabla P_s
=0,
}
\]

with

\[
\boxed{\nabla\cdot Z=0.}
\]

Thus perpetual W1 motion is itself a nonzero complete solution of the linearized equation along the recurrent background.

---

## 6. Tail tangent is exact from covariance

Along the same orbit the canonical tail satisfies

\[
T(s)=D_sT_0.
\]

Therefore

\[
\boxed{
T_s
=-\frac12
\left(T+Y\cdot\nabla T\right)
=-\frac12\mathcal H_T.
}
\]

In log-radius coordinates,

\[
\boxed{
T_s(r\theta,s)
=-\frac1{2r}\partial_y\Phi_s(y,\theta).
}
\]

M5-224 then gives the strictly positive critical tangent residue

\[
\boxed{
\underline{\mathscr R}_H(T)>0
}
\]

on every nontrivial minimal scale-motion branch.

Hence the orbit tangent is not tail-flat.

---

## 7. Fixed tail cutoff gives a local orbit quotient derivative

The divergence-free tail cutoff is constructed by one fixed linear operator

\[
\mathcal B:T\mapsto B_T
\]

consisting of multiplication by a fixed cutoff plus a fixed Bogovskii correction on the transition annulus.

Therefore along the actual orbit,

\[
\boxed{
(B_T)_s
=
\mathcal B[T_s]
}
\]

in every local topology where `T_s` is controlled.

With

\[
Q=V-B_T,
\]

one has locally

\[
\boxed{
Q_s
=Z-\mathcal B[T_s].
}
\]

This is an exact orbit-direction identity and requires no derivative of the abstract inverse tail map.

---

## 8. Global L2 derivative is a separate issue

Although each state satisfies

\[
Q(s)\in L^2\cap L^3
\]

uniformly on the compact W1 class, this alone does not imply

\[
Q_s(s)\in L^2
\]

with a uniform bound.

A bounded differentiable curve in local topologies can have a derivative whose global tail norm is not controlled by the uniform norm of the curve itself.

To use `Q_s` in a global energy pairing one needs a differentiated far-tail approximation or another global derivative-tightness lemma.

Therefore

\[
\boxed{
Q\in L_s^\infty L_x^2
\not\Rightarrow
Q_s\in L_s^\infty L_x^2.
}
\]

This distinction is retained explicitly.

---

## 9. Tangent equation does not by itself yield a contradiction

A periodic orbit provides the standard counterexample to any purely abstract claim:

its nonzero tangent `Z=V_s` is a bounded complete solution of the linearized equation and is the neutral Floquet direction generated by time translation.

An aperiodic minimal trajectory likewise possesses its flow tangent.

Therefore

\[
\boxed{
Z\ne0
+\text{bounded recurrent linearized tangent}
\not\Rightarrow
\text{instability or contradiction}.
}
\]

Navier--Stokes-specific coercivity must use more than existence of the tangent.

---

## 10. Corrected residual-work target

M5-222 suggested differentiating a tail-to-core graph.

The corrected target is narrower:

1. use only the actual orbit tangent `Z=V_s`;
2. use the exact passive tangent `T_s=-mathcal H_T/2`;
3. derive a **global** quotient-tangent estimate only if differentiated tail tightness is proved;
4. then compare the linearized tangent equation with the derivative of the tail residual.

Until step 3 is established, no global tangent work identity is counted.

---

## 11. DSD verdict

### CLOSED shortcut

\[
\boxed{
\text{tail injectivity/homeomorphism}
\not\Rightarrow
\text{differentiable coercive tail-to-core graph}.
}
\]

### POSITIVE replacement

\[
\boxed{
Z=V_s
\text{ solves the homogeneous linearized Leray system},
\qquad
T_s=-\frac12\mathcal H_T.
}
\]

### OPEN

- global `L2/H1` tightness of the orbit quotient derivative `Q_s`;
- a coercive relation between the critical tail tangent and the finite-energy tangent response;
- large-amplitude stationary critical-tail rigidity.

---

## 12. Updated frontier

The final residual route should no longer be phrased as an abstract inverse-function problem.

It is the concrete PDE question

\[
\boxed{
\text{Can a compact recurrent W1 orbit support a nonzero complete linearized flow tangent}
\ Z=V_s
\text{ whose canonical tail tangent has }
\underline{\mathscr R}_H>0,
}
\]

while the strong-critical quotient remains finite-energy and all derivative/turnover exits stay bounded?

That is the correct tangent formulation of the remaining dynamic endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]