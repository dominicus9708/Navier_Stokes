# DSD M17-359 — Exact CE-H material flow preserves regular vortex-line identity and collapses true replacement to nodal, interface, or domain exit

Date: 2026-09-08  
Canonical ID: **M17-359**

Status: **ACTIVE MATERIAL-GENEALOGY REDUCTION / M17-238 AND M17-357--358 CONNECTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. CE-H regular material flow

Work in similarity variables on an exact regular CE-H component with

\[
W=\rho\xi,
\qquad
\rho>0,
\qquad
|\xi|=1.
\]

Let

\[
B=U+\frac12 y
\]

be the similarity material velocity and let `X(theta;theta0,x)` be its flow map:

\[
\frac d{d\theta}X(\theta)=B(X(\theta),\theta).
\]

On every finite compact regular interval, smoothness makes `X` a diffeomorphism onto its image.

## 2. Vortex direction is materially fixed on CE-H

The CE-H alignment conditions give

\[
\Sigma\xi=\sigma\xi
\]

and the directional diffusion is parallel to `W`:

\[
\Delta W=\kappa W.
\]

Hence the transverse direction equation has no forcing and

\[
\boxed{D_B\xi=0.}
\]

This is the same material-line property used in M5-681 and audited in M17-238.

Moreover the antisymmetric part of `nabla U` annihilates the vorticity direction because it is proportional to cross product with `W` itself. Therefore

\[
\nabla B\,\xi
=
\left(\sigma+\frac12\right)\xi.
\]

## 3. Material image of a vortex line remains a vortex line

Let `gamma_0(alpha)` be a regular vortex line at time `theta_0`, so

\[
\partial_\alpha\gamma_0
=c_0(\alpha)\xi(\gamma_0,\theta_0)
\]

for a nonzero scalar speed `c_0`.

Transport the curve materially:

\[
\Gamma(\alpha,\theta)
:=X(\theta;\theta_0,\gamma_0(\alpha)).
\]

Its tangent

\[
q:=\partial_\alpha\Gamma
\]

obeys the standard variational equation

\[
D_B q=(\nabla B)q.
\]

If

\[
q=c\xi,
\]

then using Section 2,

\[
D_B(c\xi)
=c'\xi
\]

while

\[
(\nabla B)(c\xi)
=c\left(\sigma+\frac12\right)\xi.
\]

Thus

\[
\boxed{
D_B c=\left(\sigma+\frac12\right)c
}
\]

and the tangent remains parallel to `xi` for the full regular interval.

Therefore

\[
\boxed{
X(\theta;\theta_0,\gamma_0)
\text{ is again a vortex line at time }\theta.
}
\]

## 4. Line identity and closed-loop topology are preserved

Because `X` is a diffeomorphism on the regular finite-time interval:

1. two distinct material vortex lines cannot merge;
2. one regular material vortex line cannot split into two;
3. a closed material vortex loop remains a closed embedded loop;
4. an open material line remains the material image of that same line until it exits the represented domain or encounters a point where the active vortex-line description fails.

Thus exact CE-H supplies a genuine vortex-line genealogy, not merely a sequence of Eulerian snapshots.

## 5. Consequence for the M17-355 replacement branch

M17-355 retained

\[
G_{loop\ replacement/interface/genealogy}
\]

as one possible escape from compact same-loop recurrence.

On the present exact regular CE-H branch, **true material vortex-line replacement cannot occur internally**.

If the currently selected active segment changes from one location to another on the same line, M17-238 already says this is not lineage replacement.

If a different line becomes the active representative while the old line still exists, this is active-set/selection turnover, not destruction of the original genealogy.

Hence any genuine failure of the line genealogy must pass through an explicit loss of the hypotheses used above.

## 6. Exact replacement exits

The legitimate exits are

\[
\boxed{G_{nodal\ crossing}},
\]

where `rho=0` and `xi` is undefined;

\[
\boxed{G_{amplitude\ cutoff/active\ segment\ interface}},
\]

where the selected high-amplitude subsegment leaves the retained capture set while the underlying material line may survive;

\[
\boxed{G_{CEH/rank\ loss}},
\]

where the exact aligned-eigenline structure fails;

or

\[
\boxed{G_{flow/domain\ decompactification}},
\]

where the finite coherent material representation cannot be continued in the required compact domain.

Therefore

\[
\boxed{
T_{true\ material/vortex\ line\ replacement}
\Longrightarrow
G_{nodal}
\lor G_{cutoff/interface}
\lor G_{CEH/rank\ loss}
\lor G_{flow/domain\ exit}.
}
\]

## 7. Interaction with flux fragmentation

M17-358 shows that subdivision of the material flux measure is neutral for the flux-linear currents as long as the underlying material-label family remains coherent.

The present module supplies exactly that coherence on the regular CE-H branch.

Thus an increasing number of small active tube bands cannot by itself be called genealogy replacement. It is only a finer partition of a persistent material foliation unless one of the exits in Section 6 occurs.

## 8. Closed-loop branch becomes sharper

For a closed regular material loop, the flow preserves the same loop identity. Hence failure of same-loop recurrence cannot be blamed on spontaneous loop replacement while the loop remains in the compact CE-H component.

It must instead occur through

\[
\boxed{
G_{loop\ state\ decompactification}
\lor G_{nodal/cutoff/interface}
\lor G_{CEH/rank\ loss}.
}
\]

If none occurs and the loop state is recurrent, M17-188 applies to the same material loop.

## 9. DSD-theory role

The useful heuristic is the strict separation between `active representative replacement` and `material lineage replacement`. The proof is standard ODE flow-map and tangent-transport mathematics.

No DSD axiom is used as a PDE assumption.

## 10. Audit verdict

**PASS as a genealogy reduction.**

On exact regular CE-H, true vortex-line replacement is not an independent internal mechanism. It is routed to nodal, cutoff/interface, CE-H/rank, or flow/domain failure.

The surviving bounded/winding branch is therefore substantially narrower than in M17-355--356.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
