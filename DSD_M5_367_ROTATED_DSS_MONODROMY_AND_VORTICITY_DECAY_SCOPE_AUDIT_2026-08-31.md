# DSD M5-367 — Rotated DSS Monodromy and Vorticity-Decay Scope Audit

Date: 2026-08-31

Status: **THE EULER RDSS BRANCH IS NOT AUTOMATICALLY CLOSED BY THE 2023 ROTATED-DSS THEOREM / THE EXACT EXTERNAL DECAY HYPOTHESIS IS STRONGER THAN FINITE ENERGY PLUS BOUNDED PROFILE GRADIENT / RDSS IS REDUCED TO ORDINARY DSS, NONTRIVIAL ROTATIONAL MONODROMY, OR A SPECIFIC FAR-VORTICITY DECAY FAILURE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-365--366 close the exact non-rotated `alpha=3/2` DSS endpoint on the no-gradient-H lane.

The remaining periodic symmetry possibility is rotated discretely self-similar (RDSS) Euler dynamics.

This note audits the exact scope of the available 2023 RDSS rigidity theorem and separates what is genuinely proved from what remains.

## 2. RDSS relation

For `alpha>-1`, spatial scale `lambda>1`, and a fixed rotation `R(phi)`, an `(alpha,lambda,phi)`-RDSS Euler solution satisfies

\[
 u(x,t)
 =
 \lambda^\alpha
 R(-\phi)
 u(\lambda R(\phi)x,\lambda^{\alpha+1}t).
\]

At the current endpoint

\[
 \alpha=\frac32,
 \qquad
 \lambda=q^{2/5},
\]

and the corresponding similarity-time step is

\[
 S_0=\log q.
\]

In profile variables, the period is therefore a period **modulo rotation**.

## 3. Trivial-rotation reduction

If

\[
 \phi\in2\pi\mathbb Z,
\]

RDSS is exactly DSS and is already removed by M5-366 on the no-H gradient lane.

More generally, if the profile is invariant under the rotation used in the monodromy,

\[
 R(-\phi)V(R(\phi)y,s)=V(y,s),
\]

then the RDSS relation reduces to ordinary periodicity in `s`, again giving the DSS branch.

Thus the genuinely new case has nontrivial rotational monodromy.

## 4. Chae 2023 RDSS theorem

Dongho Chae, *Removing rotated discretely self-similar singularity for the Euler equations*, J. Differential Equations 377 (2023), 113--120, excludes RDSS singularities under an isolated-singularity hypothesis and an explicit spatial-infinity vorticity decay condition.

One formulation of the decay hypothesis is: there exist `epsilon>0` and points

\[
 |x_j|\to\infty
\]

such that

\[
 \boxed{
 \sup_{t\in(-\epsilon,0)}
 |\omega(x_j,t)|
 =
 o(|x_j|^{-\alpha-1}).
 }
\]

At

\[
 \alpha=\frac32,
\]

this is

\[
 \boxed{
 \sup_t|\omega(x_j,t)|
 =o(|x_j|^{-5/2}).
 }
\]

Under the theorem hypotheses the RDSS solution is zero.

## 5. Why finite energy does not automatically give the decay condition

The current Seregin endpoint has uniform finite kinetic energy:

\[
 V(s)\in L^2(\mathbb R^3).
\]

On the no-gradient-H branch one may also have

\[
 \|\nabla V\|_\infty<\infty.
\]

These imply a bounded/sublinear velocity profile, but they do not automatically give the quantitative vorticity decay

\[
 |\Omega(y,s)|=o(|y|^{-5/2})
\]

along a spatial sequence uniformly in time.

A bounded derivative field can still have sparse derivative/vorticity spikes at large radii while the velocity remains `L2`.

Therefore the 2023 theorem must not be invoked without an additional far-vorticity bridge.

## 6. RDSS formation split

The RDSS endpoint is now decomposed as

\[
 \boxed{
 E_{\rm RDSS}
 \Longrightarrow
 E_{\rm DSS}
 \lor
 R_{\rm mon}
 \lor
 H/T_{\omega,\infty}.
 }
\]

Here

- `E_DSS`: rotation is trivial on the actual profile and the branch is closed by M5-366;
- `R_mon`: genuine nontrivial rotational monodromy persists each similarity period;
- `H/T_{omega,infty}`: the profile evades the external RDSS theorem only through failure of the required far-vorticity decay/isolation structure.

## 7. Monodromy descriptor

Define the one-period rotational defect in a local/critical norm `X` by

\[
 \boxed{
 \mathfrak R_\phi[V](s)
 :=
 \|V(\cdot,s+S_0)
 -R(-\phi)V(R(\phi)\cdot,s)\|_X.
 }
\]

Exact RDSS means

\[
 \mathfrak R_\phi[V]\equiv0.
\]

The genuine rotational content is instead measured by the distance to the non-rotated orbit:

\[
 \boxed{
 \mathfrak M_\phi[V](s)
 :=
 \|R(-\phi)V(R(\phi)\cdot,s)-V(\cdot,s)\|_X.
 }
\]

If this vanishes, RDSS reduces to DSS.

If it stays positive, the similarity orbit has a persistent rigid group motion each period.

## 8. Irrational rotation angle

If

\[
 \phi/(2\pi)\notin\mathbb Q,
\]

then the powers `R(n phi)` are dense in the circle rotation group.

The RDSS orbit therefore has recurrent rotational returns: there exist `n_k -> infinity` with

\[
 R(n_k\phi)\to I.
\]

This gives recurrence of the shape modulo many periods, but it does **not** force rotational invariance or ordinary DSS.

Thus dense group recurrence is a dynamical observation, not a rigidity proof.

## 9. Relation to axis-property ledgers

A nontrivial rotational monodromy can appear in two ways.

1. The high-vorticity/eigenframe structure itself rotates relative to similarity coordinates. This is a projective/axis action.
2. The field is nearly rotationally symmetric, so the group motion is almost invisible to the active core. Then the profile is close to the ordinary DSS symmetry class.

The existing projective ledgers can price the first case under their bounded-shape/tightness hypotheses, but this is conditional and must not be promoted to a general RDSS nonexistence theorem.

## 10. Updated periodic endpoint

Combining M5-366 and the present scope audit,

\[
 \boxed{
 \text{periodic/modulated Euler endpoint}
 \Longrightarrow
 H_{\nabla,\infty}
 \lor
 H/T_{\omega,\infty}
 \lor
 R_{\rm mon}.
 }
\]

A pure non-rotated periodic leaf is no longer present on the no-H branch.

## 11. Firewall

Do not infer the Chae 2023 decay hypothesis from `L2 + bounded gradient` alone.

Do not infer ordinary DSS from irrational RDSS recurrence.

Do not identify a rigid global rotation with viscous/projective dissipation without an explicit bridge.

## 12. Next target

The highest-value remaining endpoint is no longer exact DSS but genuinely **shape-reforming similarity dynamics**, including rotational monodromy as a symmetry-reduced special case.

The next audit should introduce a similarity-time shape speed/one-period defect and determine whether

\[
 \text{small defect}\to\text{asymptotic DSS rigidity},
\]

whereas

\[
 \text{large defect}\to\text{persistent reformation/turnover action}.
\]

## 13. Audit verdict

### CLOSED

- trivial-rotation RDSS reduces to DSS and is closed on no-H by M5-366.

### EXTERNAL CONDITIONAL

- Chae 2023 removes genuine RDSS under isolated-singularity and far-vorticity decay hypotheses.

### OPEN

- derivation of the required far-vorticity decay from the current endpoint;
- persistent rotational monodromy without that decay;
- general aperiodic shape-reforming Euler similarity dynamics;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
