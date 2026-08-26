# DSD M5-02 — Temporal persistence scaling lock

Date: 2026-08-26

Status: **SCALING AUDIT / PURELY SCALE-INVARIANT LOCAL PERSISTENCE CAN ONLY PRODUCE THE PARABOLIC `L^{-2}` TIME SCALE, WHICH IS FAR TOO SHORT TO CONTRADICT THE M5-01 `L^{-1/3}` TIME-MEASURE BOUND / ANY SUCCESSFUL PERSISTENCE ROUTE NEEDS A SCALE-BREAKING GLOBAL ANCHOR / GLOBAL REGULARITY UNPROVED.**

## 0. Input from M5-01

For the physical critical tail coordinate

\[
K_L^{phys}(t)=\frac L2\int (|u|^2-L^2)_+dx,
\]

M5-01 proved

\[
\left|\{t:K_L^{phys}(t)\ge\kappa\}\right|
\le
C_{E,D,\kappa}L^{-1/3}.
\]

It also showed that a critical K event at amplitude `L` is compatible with the standard energy/dissipation budgets if its duration is of parabolic order `L^{-2}`.

The present file asks whether exact Navier--Stokes temporal persistence can close this gap.

---

## 1. Normalize one K event

Suppose at time `t0`,

\[
K_L^{phys}(t_0)\ge\kappa>0.
\]

Use the Navier--Stokes rescaling centered at an arbitrary spatial point `x0`:

\[
v(y,\sigma)
:=
L^{-1}
 u\left(x_0+\frac yL,
 t_0+\frac\sigma{L^2}\right).
\]

Then `v` again solves Navier--Stokes with the same viscosity and the threshold `L` is normalized to threshold `1`.

The critical K quantity is invariant under this normalization:

\[
\boxed{
K_1^{phys}[v](0)
=K_L^{phys}[u](t_0).
}
\]

Therefore any persistence theorem whose hypotheses and constants use only scale-invariant local quantities must give a normalized time interval

\[
|\sigma|\le c(\kappa,\text{dimensionless data}),
\]

which in physical variables is

\[
\boxed{
|t-t_0|
\le
c L^{-2}.
}
\]

Thus `L^{-2}` is the unavoidable persistence scale for a purely critical/local theorem.

---

## 2. Compare with the global time-measure upper bound

M5-01 permits

\[
|\{t:K_L\ge\kappa\}|
\lesssim L^{-1/3}.
\]

But

\[
L^{-2}=o(L^{-1/3}).
\]

Hence even if every order-one K event persists for its full natural parabolic lifetime,

\[
\boxed{
\Delta t_{event}\gtrsim cL^{-2},
}
\]

there is no contradiction with the global energy-class estimate.

The upper budget allows a much larger amount of event time than one parabolic packet requires.

---

## 3. Required persistence exponent

Suppose a hypothetical theorem gave

\[
\Delta t_{event}\gtrsim cL^{-\gamma}.
\]

To contradict an upper bound of order `L^{-1/3}` from a single event uniformly at large `L`, one would need, schematically,

\[
\gamma<\frac13
\]

(or an endpoint `gamma=1/3` estimate with sufficiently strong quantitative constants).

This is dramatically longer than the parabolic value

\[
\gamma=2.
\]

Therefore no scale-invariant local persistence mechanism can bridge M5-01 to uniform tail tightness.

---

## 4. DSD interpretation

The state `K_L>=kappa` is critical under Navier--Stokes scaling.

A local dynamical law that is itself critical has no dimensional quantity with which to generate a lifetime longer than `L^{-2}`.

Thus a successful temporal-persistence proof must contain a genuinely scale-breaking input, for example

- global finite energy `E0` used in a nontrivial way;
- a fixed physical length/time anchor inherited from the parent solution;
- a nonlocal compactness constraint;
- or a pressure/geometry mechanism whose estimate is not reducible to critical local scaling.

Without such an anchor, temporal persistence is only a reformulation of the parabolic packet picture already shown compatible with finite total dissipation.

---

## 5. Dimensional form of a possible global anchor

Under Navier--Stokes scaling,

\[
E_0=\|u\|_2^2
\mapsto
\lambda^{-1}E_0,
\qquad
L\mapsto\lambda L,
\qquad
t\mapsto\lambda^{-2}t.
\]

Therefore a scale-consistent persistence time using global energy can have the form

\[
\Delta t
\gtrsim
E_0^aL^{-b},
\qquad
a+b=2.
\]

To reach the `L^{-1/3}` scale would require

\[
(a,b)=\left(\frac53,\frac13\right).
\]

No such Navier--Stokes persistence estimate is proved here.

This calculation is only a dimensional target showing exactly how strong a global-anchor improvement would need to be.

---

## 6. Consequence for the M5 search

The route

\[
\text{order-one K event}
\Longrightarrow
\text{parabolic-time persistence}
\Longrightarrow
\text{contradiction with M5-01}
\]

is closed as insufficient.

A persistence route remains viable only if it proves a genuinely super-parabolic lifetime using scale-breaking parent information.

Therefore the next higher-priority M5 route is not ordinary temporal continuity. It is either

1. **defect-aware critical compactness**, or
2. **pressure-pump / amplitude-state absorption**, where the Navier--Stokes pressure Poisson structure may supply information not present in the energy budget.

---

## 7. External context

Existing velocity-profile regularity criteria also show that sufficiently rapid shrinkage of the large-velocity region can imply regularity, but they do not supply the missing theorem that arbitrary finite-energy solutions must satisfy the required uniform high-tail shrinkage near a candidate singular time.

Thus the present M5 target remains a genuine endpoint issue rather than a consequence already available from a generic profile criterion.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]