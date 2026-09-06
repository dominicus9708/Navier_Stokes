# DSD M17-282 — A bounded stationary nodal domain of the raw heat tangent is a principal positive mode and cannot carry sign-balanced K

Date: 2026-09-06  
Canonical ID: **M17-282**

Status: **BOUNDED NODAL-DOMAIN CLOSURE / THE NODAL EXIT SURVIVED M17-280--281 AS AN EXPLICIT PLACE WHERE THE DIRECTOR/AMPLITUDE FLOOR FAILS. ON EVERY ACTIVE RAW HEAT-TANGENT NODAL DOMAIN, THE TIME-FROZEN DIRECTOR GIVES THE EXACT AMPLITUDE EQUATION `a_tau=Delta a-|grad xi|^2 a`, WITH A TIME-INDEPENDENT NONNEGATIVE POTENTIAL `q=|grad xi|^2`. IF A CONNECTED NODAL DOMAIN IS BOUNDED, REGULAR, AND STATIONARY IN TIME, `a>0` INSIDE AND `a=0` ON ITS BOUNDARY, SO `a` IS A GLOBALLY POSITIVE DIRICHLET SOLUTION OF AN AUTONOMOUS LINEAR PARABOLIC EQUATION. POSITIVITY-IMPROVING DIRICHLET PARABOLIC THEORY (E.G. Mierczynski, arXiv:1708.06813, ON UNIQUENESS UP TO POSITIVE MULTIPLES OF GLOBALLY POSITIVE SOLUTIONS) REDUCES THE AUTONOMOUS CASE TO THE PRINCIPAL POSITIVE EIGENMODE: `a=e^{lambda_1 tau} phi_1`. CONSEQUENTLY `K=a_tau/a=lambda_1` IS SPATIALLY CONSTANT ON THE DOMAIN, INCOMPATIBLE WITH THE CRITICAL SIGN-BALANCED K SURVIVOR. MOVING NODAL DOMAINS, UNBOUNDED DOMAINS, IRREGULAR BOUNDARIES, OR FAILURE OF THE POTENTIAL/AMPLITUDE CORRIDOR REMAIN EXPLICIT INTERFACE/DECOMPACTIFICATION EXITS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Amplitude equation on a nodal domain

On the raw CE-H heat tangent write

\[
V=a\xi,
\qquad a=|V|.
\]

M17-260 gives

\[
\partial_\tau\xi=0.
\]

The parallel component of the heat equation gives

\[
\boxed{
\partial_\tau a
=\Delta a-a|\nabla\xi|^2.
}
\]

Define the time-independent potential

\[
\boxed{q(x):=|\nabla\xi(x)|^2\ge0.}
\]

Then

\[
\boxed{
\partial_\tau a=(\Delta-q)a.
}
\]

---

## 2. Stationary bounded nodal-domain corridor

Let `D` be a connected component on which

\[
\boxed{a(x,\tau)>0}
\]

for all ancient times under consideration.

Assume:

1. `D` is bounded and connected;
2. `partial D` is regular enough for the Dirichlet parabolic theory;
3. the domain is stationary in `tau`;
4. `a` extends continuously to
   \[
   \boxed{a=0\quad\text{on }\partial D;}
   \]
5. `q` is bounded/regular enough on `D` for the autonomous operator
   \[
   L:=\Delta-q
   \]
   to generate the usual positivity-improving Dirichlet semigroup.

Failure of these assumptions is retained as an explicit nodal-interface/geometry exit.

---

## 3. Positive global Dirichlet solution

On `D`,

\[
\partial_\tau a=La,
\qquad
a>0,
\qquad
a|_{\partial D}=0.
\]

The ancient solution at time `0` has a unique forward Dirichlet evolution, which remains positive by the strong maximum principle.
Thus the ancient solution extends to a globally positive entire-time Dirichlet solution of the same autonomous linear parabolic equation.

For strongly positive Dirichlet parabolic equations on bounded domains, the globally positive solution is unique up to multiplication by a positive constant.

A relevant general reference is:

J. Mierczynski, *Globally positive solutions of linear parabolic partial differential equations of second order with Dirichlet boundary conditions*, arXiv:`1708.06813`.

---

## 4. Autonomous reduction to the principal mode

Because `L=Delta-q` is time independent, let

\[
\lambda_1
\]

be its principal Dirichlet eigenvalue and

\[
\varphi_1>0
\]

the corresponding principal eigenfunction:

\[
L\varphi_1=\lambda_1\varphi_1,
\qquad
\varphi_1|_{\partial D}=0.
\]

Then

\[
e^{\lambda_1\tau}\varphi_1
\]

is a globally positive solution.
Uniqueness up to positive scalar multiples forces

\[
\boxed{
a(x,\tau)=C e^{\lambda_1\tau}\varphi_1(x)}
\]

for some `C>0`.

---

## 5. Constant multiplier on the nodal domain

The raw tangent multiplier is

\[
K=\partial_\tau\log a.
\]

For the principal mode,

\[
\boxed{K\equiv\lambda_1}
\]

throughout `D`.

Thus a bounded stationary positive nodal domain cannot carry both positive and negative multiplier populations.

This contradicts the retained bounded-spike critical sign-balanced `K` branch from M17-233/234/239.

Hence

\[
\boxed{
H_{bounded\ stationary\ nodal\ domain}
\Longrightarrow\bot
}
\]

on that survivor.

---

## 6. Remaining nodal exits

M17-282 does not close:

\[
\boxed{
G_{moving\ nodal\ interface}
\lor
G_{unbounded\ nodal\ domain}
\lor
G_{irregular\ nodal\ geometry}
\lor
G_{potential/coefficient\ failure}.
}
\]

Those are genuine geometry/interface/decompactification problems and must not be identified with the bounded stationary case.

---

## 7. Relation to Rank 0

M17-280 shows that a local open Rank-0 patch extends to a global fixed target line unless it encounters a node.
M17-282 now additionally closes any bounded stationary positive scalar nodal domain produced after such a node, again leaving only moving/unbounded/interface geometry.

The theorem also applies to higher-rank raw tangents at the amplitude level because the potential is always

\[
q=|\nabla\xi|^2
\]

and is time independent on the raw heat tangent.

---

## 8. DSD audit

- The nodal domain is assumed stationary; moving boundaries are not suppressed.
- The external positive-parabolic uniqueness theorem is invoked only on bounded Dirichlet domains under its positivity/regularity corridor.
- The autonomous principal-mode reduction is separated from the general time-dependent parabolic theorem.
- A constant `K` on one nodal domain is not claimed to be constant across different nodal domains.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
