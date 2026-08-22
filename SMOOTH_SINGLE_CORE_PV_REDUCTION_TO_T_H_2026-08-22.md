# Smooth Autonomous Single-Core P_V Reduction to T/H Complements — 2026-08-22

Status: **SMOOTH PROOF-TREE REDUCTION: AUTONOMOUS SINGLE-CORE P_V REMOVED MODULO REPEATED T/H COMPLEMENTS / GLOBAL REGULARITY NOT PROVED.**

This note combines two independent smooth results:

1. the adaptive Taylor-ball S-closure of the pure coherent positive-middle record-centered lane;
2. the exact positive-middle determinant-producer obligation forced by first-hitting endpoint enstrophy growth.

The combination removes the possibility that a single coherent `P_V` core escapes merely by switching the sign of the middle strain eigenvalue.

## 1. Positive-middle record-centered lane

From `SMOOTH_ADAPTIVE_TAYLOR_BALL_AMPLITUDE_FREE_CLOSURE_2026-08-22.md`, a completed `q=2` smooth stage is impossible if all of the following hold:

- the tracked current vorticity maximum is followed by an adaptive Taylor ball;
- the record neighborhood remains coherent positive-middle;
- outer/parent strain at the analytic split is below the chosen inactive threshold;
- normalized moving-ball boundary/material/pressure/center-motion flux is low;
- transverse eigenframe action is modest;
- fixed-fraction transverse material replacement is absent.

The contradiction is radius-free:

\[
L_I\le0.5377803706
<
\pi/5
\le L_I.
\]

Thus a positive-middle record-centered stage can survive only by activating a typed complement.

## 2. Positive-middle determinant production cannot disappear globally

From `SMOOTH_POSITIVE_MIDDLE_PRODUCER_OBLIGATION_2026-08-22.md`, any hypothetical singular first-hitting cascade forces

\[
\boxed{
\limsup_{j\to\infty}A_{+,j}
\ge
 a_*
:=
\frac{(\sqrt2-1)\pi}{105}\rho_0^3
>0,
}
\]

where

\[
A_{+,j}
=
\int_{I_j}
\int_{\{s_2(\Sigma)>0\}}
(-\det\Sigma)\,dy\,ds.
\]

Hence for every sufficiently small `epsilon>0`, infinitely many late stages satisfy

\[
A_{+,j}\ge a_*-\epsilon.
\]

Call these **producer stages**.

## 3. Record-centered near/far producer split

On a producer stage, let `B_j(s)` be the adaptive Taylor ball centered at the current tracked vorticity maximum. Split

\[
A_{+,j}=A_{+,j}^{near}+A_{+,j}^{far},
\]

with

\[
A_{+,j}^{near}
:=
\int_{I_j}
\int_{B_j(s)\cap\{s_2>0\}}
(-\det\Sigma),
\]

and

\[
A_{+,j}^{far}
:=
\int_{I_j}
\int_{B_j(s)^c\cap\{s_2>0\}}
(-\det\Sigma).
\]

For a late producer stage with, say,

\[
A_{+,j}\ge\frac34a_*,
\]

one of the two pieces satisfies

\[
\boxed{
A_{+,j}^{near}\ge\frac38a_*
\quad\text{or}\quad
A_{+,j}^{far}\ge\frac38a_*.
}
\]

Thus every late producer stage carries a fixed order-one normalized positive-middle packet either inside the record neighborhood or outside it.

## 4. Far producer = spatially separate active producer branch

If

\[
A_{+,j}^{far}\ge\frac38a_*,
\]

then a fixed amount of the determinant source needed to sustain endpoint enstrophy growth lies outside the adaptive record neighborhood.

This is not an autonomous single-core `P_V` stage. The record-centered core and the determinant-producing positive-middle sector are spatially distinct at the analytic observation scale.

This branch is typed as

\[
\boxed{
T_{producer-separation}
}
\]

or, if the producer moves to increasing normalized radii / derivative scales, into the existing `H_remote`/active-halo hierarchy.

The present note does not yet prove that repeated producer separation is impossible; it identifies it as a System-I packing/turnover problem.

## 5. Near producer with a negative-middle record center = spectral-sign turnover

Suppose instead

\[
A_{+,j}^{near}\ge\frac38a_*.
\]

If the tracked record center is negative-middle at a time contributing to the near producer action,

\[
s_2(\Sigma(y_*,s))<0,
\]

while the near producer integrand is supported on

\[
s_2(\Sigma(y,s))>0
\]

at points in the same adaptive ball.

Therefore the middle strain eigenvalue changes sign inside the record neighborhood. By continuity of the eigenvalues of a symmetric matrix, there is an intermediate location with

\[
s_2=0.
\]

Hence the stage contains an explicit local spectral reorganization

\[
\boxed{
\text{negative-middle record state}
\to
s_2=0
\to
\text{positive-middle producer state}.
}
\]

This is a bounded-radius spectral/shape-turnover event, typed as

\[
\boxed{T_{spectral-sign}.}
\]

If the transition is driven by large spatial strain derivatives rather than coherent bounded-radius reshaping, it is routed to the existing derivative/H branch instead.

## 6. If the record center itself becomes positive-middle

The remaining possibility is that the tracked record center changes from

\[
s_2\le0
\]

to

\[
s_2>0.
\]

Then either

1. the change itself is a spectral-turnover event, or
2. the stage enters the coherent positive-middle record-centered lane.

In the second case the adaptive Taylor-ball S-closure applies unless one of its explicit complement mechanisms is activated.

Thus changing the sign of the record-center middle eigenvalue does not reopen an autonomous pure `P_V` branch.

## 7. Combined single-core conclusion

Consider an infinite smooth first-hitting cascade and suppose that no System-I-style complement occurs eventually.

- If the record core is positive-middle, the radius-free local Taylor-ball contradiction closes the stage.
- If the record core is negative-middle, the producer obligation forces order-one positive-middle determinant action on infinitely many stages.
  - If that producer action is outside the record ball, producer separation occurs.
  - If it is inside, spectral-sign turnover or a positive-middle record-centered episode occurs.

Therefore an autonomous coherent single-core `P_V` recurrence cannot persist.

In proof-tree notation,

\[
\boxed{
P_V^{single,coherent,pure}
\Longrightarrow
T_{producer-separation}
\lor
T_{spectral-sign}
\lor
T_{boundary/material}
\lor
T_{replacement}
\lor
H_{derivative/remote}
\lor
P_{parent/pressure-action}.
}
\]

The last pressure/parent term is already known to escalate only finitely before returning to resolved residual, derivative, or active-parent action.

## 8. Interpretation

The original System-II question was whether a recurrent `P_V` core could sustain a singular cascade without repeatedly paying the turnover/escape costs classified in System I.

The present combination says: **not as an autonomous single coherent core.**

Positive-middle record geometry is locally S-closed on the pure lane. Negative-middle record geometry cannot remove the positive-middle determinant source required by the exact enstrophy balance; it must import that source from a spatially or spectrally distinct sector.

Therefore the unresolved mainline has shifted to repeated complement packing/nonrepeatability:

\[
\boxed{
\text{remaining singular cascade}
\Longrightarrow
\text{infinitely many typed }T/H\text{-style events}.
}
\]

This is a reduction, not yet a proof of global regularity. The next target is System-I closure: prove that the required fixed-size producer-separation / spectral-turnover / boundary-flux / derivative events cannot occur on infinitely many geometric first-hitting stages under the finite physical budgets.

Status: **AUTONOMOUS SINGLE-CORE P_V HAS BEEN REDUCED TO THE SYSTEM-I COMPLEMENT TREE. GLOBAL REGULARITY REMAINS OPEN BECAUSE REPEATED T/H COMPLEMENTS STILL NEED A NONREPEATABILITY/PACKING THEOREM.**