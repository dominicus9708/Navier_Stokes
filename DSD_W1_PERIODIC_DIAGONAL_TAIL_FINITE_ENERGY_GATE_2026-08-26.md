# DSD W1 Periodic Tail: Diagonal Inheritance and Finite-Energy Gate

Date: 2026-08-26

Status: **TEMPTING DIRECT FINITE-ENERGY CONTRADICTION REJECTED FOR THE OMEGA-LIMIT ORBIT / CONDITIONAL DIAGONAL-INHERITANCE LEMMA SHOWN TO CLOSE THE PERIODIC CRITICAL TAIL / PRELIMIT-TO-LIMIT MOVING-SHELL TRANSFER IDENTIFIED AS THE MISSING BRIDGE / GLOBAL REGULARITY UNPROVED.**

## 1. The tempting argument

The periodic W1 omega-limit orbit has a nonzero canonical physical critical trace

\[
t_*(x)
=|x-X_*|^{-1}\Phi(\widehat{x-X_*},\log|x-X_*|).
\]

A nonzero discretely homogeneous degree-`-1` field is locally `L2` near the origin but not globally `L2` at spatial infinity.  Indeed, if one canonical annular cell carries positive energy

\[
E_*:=\int_{1<|x|<\lambda}|t_*|^2dx>0,
\]

then discrete scaling gives

\[
\int_{\lambda^k<|x|<\lambda^{k+1}}|t_*|^2dx
=\lambda^kE_*.
\]

Hence

\[
\boxed{t_*\notin L^2(\mathbb R^3)}
\]

whenever it is nonzero.

The original smooth Navier--Stokes solution, however, has finite kinetic energy uniformly before the candidate singular time.  This makes a direct contradiction look possible.

## 2. Why the direct argument is invalid

The periodic W1 object `U_per` is not the original rescaled trajectory itself.  It is an omega-limit orbit obtained from a sequence of Leray time shifts

\[
U_{orig}(s_n+\cdot)\to U_{per}(\cdot)
\]

in the compact topology, in particular globally in `Lp` for the fixed `p>3` used in W1 and smoothly on bounded spatial sets.

The physical inverse transform at a fixed nonzero physical point uses the rescaled coordinate

\[
Y_n
=\frac{x-X_*}{\sqrt{T^*-t_n}}
\asymp e^{s_n/2}.
\]

Thus the point/shell relevant to the physical final trace moves to spatial infinity **at the same time as** `s_n->infinity`.

Convergence on every fixed Leray ball does not control this diagonal regime.

Even global `Lp`, `p>3`, convergence does not solve the problem, because a critical `1/R` shell has

\[
\int_{A_R}|U|^p
\sim R^{3-p}\to0
\]

while its physical critical `L2` energy after inverse scaling can remain order one on a fixed physical annulus.  The critical memory is therefore invisible to the `p>3` tail norm in precisely the moving-shell limit needed here.

Hence

\[
\boxed{
U_{orig}(s_n)\to U_{per}
\text{ in W1 topology}
\not\Rightarrow
\text{physical convergence to }t_*
\text{ on fixed spatial annuli}.
}
\]

This rejects the naive finite-energy closure.

## 3. Exact diagonal shell corresponding to a fixed physical annulus

Let

\[
\tau_n=T^*-t_n=e^{-s_n}
\]

and fix a physical annulus

\[
A^{phys}_{a,b}
=\{a<|x-X_*|<b\},
\qquad0<a<b<\infty.
\]

In Leray variables this becomes

\[
A^{Leray}_{n}
=\{a\tau_n^{-1/2}<|Y|<b\tau_n^{-1/2}\}.
\]

Thus its characteristic radius is

\[
\boxed{R_n\asymp e^{s_n/2}.}
\]

This is the **finite-energy diagonal**.

A tail theorem that is uniform for fixed `R` and then takes `R->infinity` is not automatically a theorem on `R=R_n` simultaneously with `s=s_n`.

## 4. Conditional diagonal-inheritance lemma

Suppose one could prove, along a blow-up sequence, that for every fixed physical annulus `A_phys`,

\[
\boxed{
\|u(t_n)-t_*\|_{L^2(A^{phys})}\to0.
}
\]

Equivalently in Leray variables,

\[
\boxed{
\tau_n^{1/4}
\|U_{orig}(s_n)-T_{per}(\cdot,s_n^{phase})\|_{L^2(A^{Leray}_n)}
\to0.
}
\]

This is the missing **diagonal tail inheritance** statement.

## 5. Such inheritance would immediately force the trace into global L2

The physical energy inequality gives

\[
\sup_{t<T^*}\|u(t)\|_2^2\le E_0<\infty.
\]

If the local annular convergence above holds, then for every `0<a<b<infinity`,

\[
\int_{a<|x-X_*|<b}|t_*|^2dx
=
\lim_{n\to\infty}
\int_{a<|x-X_*|<b}|u(t_n)|^2dx
\le E_0.
\]

Let `a downarrow 0` and `b upward infinity`.  Monotone convergence gives

\[
\boxed{
\|t_*\|_2^2\le E_0.
}
\]

But every nonzero discretely homogeneous degree-`-1` trace has infinite global L2 energy.  Therefore

\[
\boxed{t_*=0.}
\]

This contradicts the nonzero periodic W1 critical-shell/canonical-tail result.

Hence

\[
\boxed{
\text{DIAGONAL TAIL INHERITANCE}
\Longrightarrow
\text{NO NONZERO PERIODIC W1 SURVIVOR}.
}
\]

## 6. Why the existing exterior L2 quotient does not already prove inheritance

For the periodic omega-limit orbit itself,

\[
U_{per}-T_{per}\in L^2(\{|Y|>R_0\})
\]

uniformly in periodic phase.  If `U_per` were the actual rescaled physical solution, inverse scaling would indeed give

\[
\|u-t_*\|_{L^2(A^{phys})}
\le
\tau^{1/4}\|U_{per}-T_{per}\|_2
\to0.
\]

But `U_per` is only an omega-limit model.  The missing estimate is for

\[
U_{orig}(s_n)-U_{per}(s_n^{phase})
\]

on the moving annulus `R_n~e^{s_n/2}`, not on a fixed Leray ball.

This distinction is essential.

## 7. Relation to the all-age co-moving transport estimate

The repository has the strong all-age shell estimate

\[
\|W_R(h)-W_R(0)\|_{H^{-1}}
\le CR^{-2}
\qquad\forall h\ge0.
\]

This removes deterioration with shell age and is therefore highly relevant to the diagonal problem.

However it compares a shell to its own co-moving ancestor on the **same actual orbit**.  It does not by itself identify that ancestor with the phase of the omega-limit periodic orbit at a fixed remote base radius.

The remaining bridge can therefore be formulated as a two-step compatibility problem:

1. use all-age co-moving transport to pull the diagonal shell `R_n~e^{s_n/2}` back to one controlled remote base shell;
2. use omega-limit recurrence/convergence strongly enough on that base shell to identify the pulled-back profile with the canonical periodic phase.

A successful estimate must keep the base radius large enough for the all-age error to be small while keeping it fixed enough for omega-limit convergence to apply.

This is now a sharply posed diagonal compactness problem rather than a vague finite-energy objection.

## 8. Candidate epsilon--R order of limits

The natural safe order is:

- first choose a large but finite base radius `R0` so the all-age transport error is `O(R0^-alpha)`;
- then take the omega-limit sequence `s_n->infinity`, using compact/smooth convergence on the fixed ball containing the `R0` shell;
- only after passing `n->infinity`, send `R0->infinity`.

If the accumulated comparison error remains uniform when the co-moving age is chosen to hit the physical diagonal, this order of limits may produce the desired diagonal inheritance.

The existing all-age estimate is designed precisely to avoid an age-dependent constant, so this route is technically plausible.  It is not completed in this note.

## 9. Updated periodic closure target

The periodic branch now has two complementary endgame routes:

\[
\boxed{
P_{DSS}^{long}
\Longrightarrow
H_{2,crit}^{tail}
\lor
P_{ren}^{core},
}
\]

from the renormalized-interface audit, and independently

\[
\boxed{
P_{DSS}^{long}
+
\text{diagonal tail inheritance}
\Longrightarrow
\bot
}
\]

from the original finite-energy bound.

The second route is especially attractive because it does not require a sign-definite renormalized core functional; it requires only a sufficiently uniform prelimit/omega-limit tail-transfer lemma.

## 10. DSD audit

The following are explicitly distinguished:

- original finite-energy physical solution;
- rescaled original Leray orbit;
- omega-limit ancient orbit;
- canonical tail of the omega-limit orbit;
- fixed-Leray-radius convergence;
- moving diagonal radius `R~e^{s/2}`;
- local physical convergence versus formal inverse transformation of an infinite-energy ancient model.

The direct finite-energy contradiction is not used without the diagonal bridge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
