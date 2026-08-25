# DSD W1 Vorticity-Amplitude Dichotomy and Uniform Contact Order

Date: 2026-08-26

Status: **NONCONSTANT VORTICITY-SUPREMUM BRANCH ROUTED TO RECURRENT DIRECTIONAL SUPERCRITICAL STRETCHING / CONSTANT-SUPREMUM BRANCH REDUCED TO UNIFORMLY FINITE-ORDER ANALYTIC CONTACT DEGENERACY UNLESS THE SAME SUPERCRITICAL STRETCHING OCCURS / INFINITE-ORDER CONTACT ESCAPE EXCLUDED ON THE COMPACT MINIMAL W1 CLASS / GLOBAL REGULARITY UNPROVED.**

## 1. Setting

Let `M` be a nontrivial compact minimal recurrent W1 set for the autonomous Leray flow.  Write

\[
F_U(Y):=|\Omega_U(Y)|^2,
\qquad
m(U):=\|\Omega_U\|_\infty^2.
\]

The W1 tail gives uniform decay

\[
F_U(Y)=O(|Y|^{-4})
\]

on `M`, while local analyticity gives smooth compactness on every finite ball.  Hence `m:M->R` is continuous and every spatial maximum lies in one fixed finite ball.

Along an orbit write

\[
m(s):=m(U(s)).
\]

The exact Leray vorticity-magnitude equation is

\[
\frac12
\left(
\partial_s+U\cdot\nabla+\frac12Y\cdot\nabla
\right)F
+F
=
\Omega^TS\Omega
+\frac\nu2\Delta F
-\nu|\nabla\Omega|^2.
\]

At a spatial maximum of `F`,

\[
\nabla F=0,
\qquad
\Delta F\le0.
\]

Define the directional stretching rate

\[
\gamma:=\frac{\Omega^TS\Omega}{|\Omega|^2}
=\xi^TS\xi.
\]

## 2. Dichotomy of the vorticity supremum on a minimal set

Since `m` is continuous on compact `M`, either

\[
\boxed{m_{max}>m_{min}}
\]

or

\[
\boxed{m(U)\equiv m_*>0\quad(U\in M).}
\]

The zero value is impossible because it would give `Omega=0` and then the excluded equilibrium.

We call these the **oscillatory-amplitude branch** and the **isovortical-amplitude branch**.

## 3. Oscillatory amplitude forces directional supercritical stretching at a true vorticity maximum

Assume

\[
m_{max}>m_{min}.
\]

Choose

\[
0<\delta<\frac14(m_{max}-m_{min})
\]

and the nonempty open state sets

\[
\mathcal O_-:=\{U\in M:m(U)<m_{min}+\delta\},
\]

\[
\mathcal O_+:=\{U\in M:m(U)>m_{max}-\delta\}.
\]

For a compact minimal flow, returns to each nonempty open set are syndetic.  Hence there is one finite `L_+` such that, after any visit to `O_-`, the orbit reaches `O_+` within a Leray-time interval of length at most `L_+`.

Across such a low-to-high passage,

\[
\Delta m
\ge
(m_{max}-m_{min})-2\delta
=:\Delta_*>0.
\]

The smooth compact W1 class makes `m(s)` locally Lipschitz (the maximum remains in a fixed core and `partial_s F` is uniformly bounded there).  Therefore `m` is absolutely continuous on bounded intervals and at some differentiability time in each low-to-high passage,

\[
\boxed{m'(s)\ge \Delta_*/L_+>0.}
\]

At a differentiability time of a spatial maximum, the standard envelope/Danskin formula gives at least one maximizing point `Y_s` such that

\[
\partial_sF(Y_s,s)=m'(s).
\]

Evaluating the exact magnitude equation at `Y_s`, using `grad F=0` and `Delta F<=0`, gives

\[
\frac12m'(s)+m(s)
\le
\gamma(Y_s,s)m(s).
\]

Thus

\[
\boxed{
\gamma(Y_s,s)
\ge
1+\frac{m'(s)}{2m(s)}
\ge
1+\varepsilon_\gamma,
}
\]

where one may take

\[
\varepsilon_\gamma
:=
\frac{\Delta_*}{2L_+m_{max}}>0.
\]

This is stronger than a bare `lambda_3>1` event: it is supercritical extension **in the actual vorticity direction at an actual global-vorticity maximum**.

By continuity this produces a nonempty open state-space event with a slightly weakened threshold.  Minimality therefore makes such events syndetic, and local smoothness supplies a uniform short persistence time.  Hence the oscillatory-amplitude branch has positive asymptotic density of finite-core directional supercritical-stretching events.

Status: **PROVED on the compact smooth minimal W1 class.**

## 4. Constant-amplitude branch: exact contact formula

Now assume

\[
\boxed{m(U)\equiv m_*>0\quad(U\in M).}
\]

At every time `s`, `m'(s)=0`.  At a maximizing point compatible with the envelope derivative,

\[
\partial_sF=0.
\]

The exact magnitude equation gives

\[
\boxed{
\gamma
=
1
-\frac{\nu}{2m_*}\Delta F
+\frac{\nu}{m_*}|\nabla\Omega|^2
\ge1.
}
\]

Therefore every isovortical-amplitude state has at least one maximum point satisfying `gamma>=1`.

If a compact-state subsequence contains a strict gap

\[
\gamma\ge1+\epsilon
\]

at such maximum points for some fixed `epsilon>0`, then the same open-set/minimality argument again produces syndetically recurrent directional supercritical stretching.  Thus the only genuinely new branch is the equality/degenerate-contact corridor.

## 5. Equality contact is second-order flat

At a selected maximum point, if

\[
\gamma=1,
\]

then both nonnegative defect terms in the previous identity must vanish:

\[
\boxed{
\nabla\Omega=0,
\qquad
\Delta F=0.
}
\]

At a spatial maximum the Hessian of `F` is negative semidefinite.  A negative-semidefinite matrix with zero trace is zero.  Therefore

\[
\boxed{D^2F=0}
\]

at every equality-contact point.

Thus the constant-amplitude branch avoiding a strict directional-stretching gap must pass through spatially degenerate vorticity maxima whose quadratic contact jet vanishes.

## 6. Compactness plus analyticity excludes unbounded contact order

Define the compact contact set

\[
\mathcal C_M
:=
\{(U,Y):U\in M,\ Y\in B_{R_M},\ F_U(Y)=m_*\}.
\]

Compactness follows from compactness of `M`, the uniform finite-core location of maxima, and smooth local convergence.

For a nontrivial state define the contact defect

\[
h_U(Y):=m_*-F_U(Y)\ge0.
\]

Each `h_U` is real analytic in `Y`.

Suppose, contrary to the desired conclusion, that contact orders are not uniformly bounded on `C_M`.  Then there exist

\[
(U_n,Y_n)\in\mathcal C_M
\]

such that every spatial derivative of `h_{U_n}` of order at most `n` vanishes at `Y_n`.

By compactness, pass to a subsequence

\[
U_n\to U_*,
\qquad
Y_n\to Y_*.
\]

Smooth local convergence implies that for every fixed multi-index `alpha`,

\[
\partial^\alpha h_{U_*}(Y_*)=0.
\]

Hence the complete Taylor series of the analytic scalar `h_{U_*}` vanishes at `Y_*`.  Analyticity gives

\[
h_{U_*}\equiv0
\]

in a neighborhood of `Y_*`, and analytic continuation on connected `R^3` gives

\[
F_{U_*}(Y)\equiv m_*.
\]

But the W1 vorticity tail tends to zero.  Since `m_*>0`, this is impossible.

Therefore there exists a finite integer

\[
\boxed{N_M<\infty}
\]

such that every contact pair has a nonzero spatial derivative of `h_U` of order at most `N_M`.

Because a first nonzero Taylor term at a local minimum of `h_U` must have even order, the genuinely degenerate equality-contact corridor has an even order at least four and at most `N_M`.

Status: **PROVED.**

## 7. Uniform quantitative jet gap

For the finite `N_M`, define on `C_M`

\[
G_{N_M}(U,Y)
:=
\max_{1\le|\alpha|\le N_M}
|\partial^\alpha h_U(Y)|.
\]

This is continuous on compact `C_M` and is strictly positive there by the preceding argument.  Hence

\[
\boxed{
c_M
:=
\min_{(U,Y)\in\mathcal C_M}G_{N_M}(U,Y)
>0.
}
\]

Thus every maximum-vorticity contact obeys the uniform finite-jet alternative

\[
\boxed{
\max_{1\le|\alpha|\le N_M}
|\partial^\alpha(m_*-|\Omega|^2)|
\ge c_M.
}
\]

On the equality-contact corridor the first and second order jets vanish, so the nonzero derivative is of some even order in

\[
\boxed{4,6,\ldots,N_M.}
\]

This removes the historical escape in which the first nonzero analytic contact order tends to infinity along recurrent snapshots.

## 8. Updated W1 maximum-geometry split

Every nontrivial compact minimal W1 set therefore satisfies

\[
\boxed{
W1_{min}
\Longrightarrow
G_\gamma
\lor
C_{iso}^{fin-deg},
}
\]

where

\[
G_\gamma:
\text{syndetically recurrent finite-core events }
\xi^TS\xi>1+\varepsilon_\gamma
\text{ at true global-vorticity maxima},
\]

and

\[
C_{iso}^{fin-deg}:
\|\Omega(s)\|_\infty\equiv const>0
\text{ and recurrent maximum contacts are uniformly finite-order degenerate,}
\]

with contact order belonging to a finite set of even integers `>=4` unless a strict `gamma>1` gap occurs.

The second branch is much narrower than the former unspecified flat-contact escape, but it is not yet excluded.  A next route is to differentiate the contact equation through the first nonzero even jet and determine whether preservation of the constant maximum forces a fixed `partial_s S`, eigenframe-conversion, or higher-derivative/palinstrophy cost.

## 9. DSD audit

The argument preserves the distinctions:

- state-space recurrence versus pointwise spatial recurrence;
- a strict directional stretching event versus a bare principal-eigenvalue event;
- exact constant maximum amplitude versus approximate recurrence;
- finite-order contact degeneracy versus an analytic plateau;
- lower finite-jet nondegeneracy versus derivative blow-up.

No step identifies a fixed nonzero normalized derivative with an `H` escape; such a routing requires an additional scale or accumulation argument.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
