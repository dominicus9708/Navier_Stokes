# M18-052 — Strong scattering continuity is not needed: measurable equivariance suffices to build the ergodic tail factor on the passive branch

**Date:** 2026-09-11  
**Status:** B-TAIL TOPOLOGY REPAIR / MEASURABLE-FACTOR CERTIFICATE / W1-RATCHET MIDDLE-BRIDGE COMPRESSION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-051 reduced the W1--ratchet middle bridge to

\[
B_{tail}:
\quad
\text{complete compact W1 hull}
\to
\text{controlled terminal critical-tail/scattering factor}
\]

or one of the three root complexes.

M5-567 correctly contains a topology firewall:

\[
\boxed{
\text{local hull compactness}
\not\Rightarrow
\text{strong continuity of }Y\mapsto A_Y
\text{ in an infinite-tail topology}.
}
\]

The present audit asks whether M5-571 actually needs that strong continuity.

It does not.
For the ergodic factor construction, **Borel measurability plus exact equivariance is enough**.

## 2. Passive spectator input from M5-563

For a complete similarity solution \(Y\), along the outward dilation characteristic

\[
R(\tau)=R_0e^{\tau/2},
\qquad
V_Y(\xi,\tau)=R(\tau)U_Y(R(\tau)\xi,\theta_0+\tau),
\]

M5-563 derives the exact equation

\[
\boxed{
\partial_\tau V_Y
=
R_0^{-2}e^{-\tau}
\mathcal R[V_Y,P_Y].
}
\]

On the passive spectator corridor,

\[
\boxed{
\|\mathcal R[V_Y(\tau),P_Y(\tau)]\|_X
\le C_{spec}
}
\]

in a fixed-annulus Banach norm \(X\), for example a separable Sobolev norm on \(A_1^+\).

M5-563 explicitly classifies failure of this bound as a strong derivative/pressure/active-remote exit.

Thus, on the no-root passive branch, this is a retained case condition rather than a new free hypothesis.

## 3. The Duhamel limit exists in X

For \(\tau_2>\tau_1\),

\[
\|V_Y(\tau_2)-V_Y(\tau_1)\|_X
\le
C_{spec}R_0^{-2}e^{-\tau_1}.
\]

Hence

\[
V_Y(\tau)
\]

is Cauchy in \(X\) and has a limit

\[
\boxed{
A_Y(q)
=
\lim_{\tau\to\infty}V_Y^{(q)}(\tau),
}
\]

where

\[
q=\log R_0-\theta_0/2
\]

labels the dilation characteristic.

The convergence rate is quantitative:

\[
\boxed{
\|V_Y^{(q)}(\tau)-A_Y(q)\|_X
\le
C_{spec}R_0^{-2}e^{-\tau}.
}
\]

## 4. Finite-time approximants are Borel observables of the local hull

Fix \(q\) and a finite \(\tau=n\in\mathbb N\).

The approximant

\[
A_Y^{(n)}(q)
:=
V_Y^{(q)}(n)
\]

is obtained by:

1. flowing the hull state by a finite similarity time;
2. evaluating the solution on one finite physical/similarity annulus;
3. applying a finite rescaling to the fixed annulus \(A_1\).

For any fixed finite radius and time, these operations are continuous in the retained local smooth hull topology, or at minimum Borel in the state topology used by the invariant measure.

Therefore

\[
\boxed{
Y\mapsto A_Y^{(n)}(q)
}
\]

is an \(X\)-valued Borel map.

## 5. The scattering value A_Y(q) is Borel measurable

Take \(X\) separable, as is the case for the standard fixed-annulus Sobolev spaces used in M5-563.

Since

\[
A_Y^{(n)}(q)	o A_Y(q)
\quad\text{in }X,
\]

and pointwise limits of Borel maps into a separable metric space are Borel,

\[
\boxed{
Y\mapsto A_Y(q)
\text{ is Borel measurable for each fixed }q.
}
\]

No strong continuity of the infinite-tail map is needed.

## 6. Measurability of the local-q scattering profile

For ergodic observables one does not need a norm controlling the entire \(q\in\mathbb R\) profile at once.

It is enough to work in a separable local profile space such as

\[
\mathcal X_{loc}
:=
L^2_{loc}(\mathbb R_q;X)
\]

or a countable product of fixed compact \(q\)-interval spaces.

The finite-time approximants are jointly measurable in \((Y,q)\), and the Duhamel limit is pointwise/local in \(q\).

Hence, after the usual separable representative choice,

\[
\boxed{
\mathcal A:
Y\mapsto A_Y
}
\]

is a Borel map into \(\mathcal X_{loc}\).

This is sufficient to define a push-forward probability measure.

## 7. Exact covariance supplies the factor relation

M5-567 proves trajectory by trajectory

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega).
}
\]

Let

\[
T_tA(q,\omega)
:=
A(q-t/2,\omega).
\]

Then

\[
\boxed{
\mathcal A\circ\sigma_t
=
T_t\circ\mathcal A.
}
\]

This is the exact measurable factor relation.

## 8. Push-forward invariance requires measurability, not continuity

Let \(\mu\) be an invariant probability measure on the compact complete hull and define

\[
\boxed{
\nu:=\mathcal A_\#\mu.
}
\]

For a Borel set \(B\subset\mathcal X_{loc}\),

\[
\begin{aligned}
\nu(T_t^{-1}B)
&=
\mu(\mathcal A^{-1}(T_t^{-1}B))\\
&=
\mu(\sigma_t^{-1}\mathcal A^{-1}(B))\\
&=
\mu(\mathcal A^{-1}(B))\\
&=
\nu(B).
\end{aligned}
\]

Therefore

\[
\boxed{\nu\text{ is translation-invariant}.}
\]

Strong continuity of \(\mathcal A\) is irrelevant to this measure-theoretic step.

## 9. Ergodicity also passes to a measurable factor

Suppose \(\mu\) is ergodic under \(\sigma_t\).

Let \(B\) be invariant under all \(T_t\).
Then

\[
\mathcal A^{-1}(B)
\]

is invariant under all \(\sigma_t\) by equivariance.

Ergodicity of \(\mu\) gives

\[
\mu(\mathcal A^{-1}(B))\in\{0,1\}.
\]

Hence

\[
\boxed{
\nu(B)\in\{0,1\}.
}
\]

Thus

\[
\boxed{
\text{an ergodic hull measure pushes forward to an ergodic log-radius scattering factor}
}
\]

under measurable equivariance alone.

This validates the measure-theoretic core of M5-571 without importing an unjustified global strong-scattering continuity claim.

## 10. What the original topology firewall still forbids

The repair above does **not** make the M5-567 warning obsolete.

Local hull convergence still does not imply

\[
\|A_{Y_n}-A_Y\|_{global\ q}\to0
\]

in a strong norm over the whole scattering cylinder.

Therefore one still may not infer:

- uniform global scattering-tail compactness;
- pointwise convergence of all remote shell coefficients from local state convergence;
- strong recurrence of the entire infinite-q profile from local topological recurrence alone.

The valid replacement is weaker and sufficient:

\[
\boxed{
\text{Borel measurable equivariant scattering factor}.}
\]

## 11. Nontriviality of the scattering factor

M5-567 identifies global \(L^3\) with unweighted \(q\)-integrability of the critical datum.

M5-562/M5-569 exclude the zero/global-\(L^3\) terminal profile on the retained nontrivial hard component.

Therefore on the retained hard passive component,

\[
\boxed{
A_Y\not\equiv0
\quad\mu\text{-a.e.}
}

and the local cubic observable

\[
C_3(A)
=
\int_0^1\int_{S^2}|A|^3
\]

has positive ergodic mean.

Likewise the terminal-vorticity coefficient is nontrivial on the retained regular critical class.

## 12. B_tail is now a branch split rather than a topology MISS

The complete W1 hull has the following alternatives.

### Passive spectator branch

Uniform fixed-annulus residual control holds.
Then M5-563/567 construct a Borel measurable equivariant scattering datum and the preceding sections justify the ergodic factor used in M5-571.

### Residual-control failure

Derivative, pressure, or active remote residual becomes unbounded.
This is

\[
\mathcal R_{remote}
\lor
\mathcal R_{AC}
\]

according to whether the failure is a genuine remote source or a boundary/ancestry payer issue.

### Critical tail/trace existence itself fails

The state does not admit the passive critical asymptotics/terminal object required by the scattering reduction.
This remains

\[
\mathcal R_{critical}.
\]

Hence

\[
\boxed{
\mathcal H_{W1}^{two-sided}
\Longrightarrow
\mathcal H_{scattering}^{ergodic}
\lor
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}.
}
\]

## 13. Revised middle-chain status

M18-050 classified B-WR as a missing middle bridge.
M18-051 certified its compact-hull half on the no-root corridor.
M18-052 repairs the strong-topology overrequirement on the tail half.

Therefore there is no longer an independent fourth middle-chain root called `B-WR failure`.

The valid route is

\[
\boxed{
\text{first-hitting compact survivor}
\Longrightarrow
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}
\lor
\text{nontrivial ergodic scattering/terminal process}.
}
\]

This remains conditional on the exact tail/trace existence assumptions already separated as \(\mathcal R_{critical}\).

## 14. Consequence for the dependency matrix

The M18-050 row

\[
B_{WR}=MISS
\]

should be replaced by two rows:

\[
\boxed{
\begin{array}{c|c}
B_{hull}&INT+STD\text{ on the no-root corridor}\\
B_{tail}&INT\text{ passive branch}\lor R1\lor R2\lor R3
\end{array}
}
\]

where the `R1/R2/R3` labels denote the three current root complexes.

The main theorem-level open work now moves back to:

1. closure of those three root complexes;
2. end-chain ancestry/rigidity D7;
3. historical completeness of the upstream case split.

## 15. Relation to M5-571

M5-571's statement

\[
\nu=\mathcal A_\#\mu
\]

and its assertion that the induced log-radius translation process is ergodic are measure-theoretically legitimate provided:

- \(\mathcal A\) is Borel measurable;
- covariance holds;
- the passive scattering datum exists \(\mu\)-almost everywhere on the selected invariant component.

Sections 4--9 provide the missing measurability justification at the audit level.

Thus the phrase “factor of an ergodic flow” need not be interpreted as requiring a continuous topological factor.

## 16. DSD lesson

This is a useful distinction between two kinds of describability requirement:

\[
\boxed{
\text{topological factor}
\quad\text{vs}\quad
\text{measurable dynamical factor}.
}
\]

Demanding the stronger object without necessity would create a false proof obligation.

For the ergodic average arguments, measurable describability is sufficient.

## 17. Audit verdict

### Certified at the current audit level

1. The passive scattering datum is an \(X\)-limit of finite-radius Borel observables.
2. In a separable fixed-annulus/local-q function space the scattering map is Borel measurable.
3. Exact M5-567 covariance makes it a measurable dynamical factor.
4. Invariance and ergodicity push forward without strong continuity.
5. The original strong-topology firewall remains valid but is not an obstruction to M5-571's ergodic-factor construction.
6. B-tail reduces to the already typed remote/critical/ancestry roots or the controlled ergodic scattering process.

### Still open

1. Closure of \(\mathcal R_{remote}\).
2. Closure of \(\mathcal R_{critical}\).
3. Closure of \(\mathcal R_{AC}\).
4. End-chain payer-to-parent contradiction D7.
5. Historical completeness outside the active indexed case split.
6. Global 3D Navier--Stokes regularity.

## 18. Next target

M18-053 should update the global canonical frontier and then focus on **which of the three remaining root complexes is mathematically weakest**.

A first comparison should score each root by:

- whether a finite parent budget already exists;
- whether a nontrivial normalized witness is guaranteed;
- whether scale conversion is favorable or summable;
- whether an external rigidity theorem applies to a substantial subbranch;
- whether the root has already been reduced to one precise missing inequality.

This will choose the next calculation rationally rather than continuing the deepest CE-H branch by habit.
