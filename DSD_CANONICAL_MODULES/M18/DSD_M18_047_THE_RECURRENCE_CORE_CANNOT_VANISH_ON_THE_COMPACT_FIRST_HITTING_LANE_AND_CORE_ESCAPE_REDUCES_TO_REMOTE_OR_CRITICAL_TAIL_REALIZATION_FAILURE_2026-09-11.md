# M18-047 — The recurrence core cannot vanish on the compact first-hitting lane, and core escape reduces to remote or critical-tail realization failure

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE RECURRENT-CORE AUDIT / NONVANISHING CERTIFICATE / CORE-ESCAPE RECOMPRESSION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-046 left

\[
G_{vanishing/escaping\ recurrent\ core}
\]

as one upstream ROOT-CERT label.

That label combines two logically different questions:

1. can the normalized active core itself converge to zero?
2. can the core fail to remain represented in one compact normalized state space because its center, tail, or global realization escapes?

The first-hitting normalization and later compactness modules already answer the first question strongly. The second reduces to previously typed remote/tail/realization failures.

## 2. First-hitting normalization prevents local vanishing

At each selected first-hitting stage,

\[
W_j=\|\omega(t_j)\|_\infty,
\qquad
r_j=\sqrt{\nu/W_j},
\]

and the normalized vorticity is

\[
\Omega_j(Y,\tau)
=
\frac{r_j^2}{\nu}\,
\omega\left(X_j+r_jY,
 t_j+\frac{r_j^2}{\nu}\tau\right).
\]

At the marked first-hitting point,

\[
\boxed{|\Omega_j(0,0)|=1.}
\]

This is an exact finite-stage normalization, not a limit statement.

On the bounded critical ratchet corridor, the existing estimates give on every fixed backward time interval:

\[
\sup_j\|\Omega_j\|_{L^\infty}<\infty,
\qquad
\sup_j\|\Omega_j\|_{L^2}<\infty,
\]

and stage-wide analyticity gives uniform local derivative bounds of every fixed order.

Hence a subsequence converges locally smoothly to an ancient element \(\Omega_*\), and the marked value passes directly:

\[
\boxed{|\Omega_*(0,0)|=1.}
\]

Therefore

\[
\boxed{
\text{local smooth compactness}
+\text{ first-hitting normalization}
\Longrightarrow
\text{nonzero ancient core}.
}
\]

A vanishing ancient limit is impossible on this compact lane.

## 3. The active mark also thickens spatially

The nonzero point is not merely a measure-zero marker.

Uniform local analyticity/Lipschitz control supplies a fixed normalized radius \(r_a>0\) and amplitude \(c_a>0\) such that after shrinking constants if needed,

\[
\boxed{
|\Omega_j(Y,0)|\ge c_a
\qquad (Y\in B_{r_a})
}
\]

for all sufficiently late retained stages.

Passing to the local smooth limit gives

\[
\boxed{
|\Omega_*(Y,0)|\ge c_a
\qquad (Y\in B_{r_a}).
}
\]

Thus the nontriviality is a fixed positive-volume local witness.

This is the same kind of fixed active-core witness used in M18-044 to obtain a positive velocity-variance floor.

## 4. Backward checkpoint nontriviality cannot escape spatially on the no-turnover lane

The similarity checkpoint audit gives a stronger backward statement.

At age \(m\), the earlier first-hitting scale obeys

\[
r_{j-m}=q^{m/2}r_j.
\]

On the center-nested/two-sided-clock corridor, after conversion to backward similarity coordinates the tracked checkpoint maximizers satisfy

\[
\boxed{
\xi_{j,m}\in B_{R_*}
}
\]

for one fixed \(R_*<\infty\), independent of \(j,m\).

Moreover their similarity-vorticity amplitudes obey

\[
\boxed{
0<c_-
\le
|\Omega_{V,j}(\xi_{j,m},s_{j,m})|
\le c_+<\infty.
}
\]

After the same strong local compactness passage, there is a backward sequence

\[
\boxed{
\xi_m\in B_{R_*},
\qquad
|\Omega_V(\xi_m,s_m)|\ge c_*>0,
\qquad
s_m\to-\infty.
}
\]

Hence the tracked recurrent checkpoint core neither vanishes nor drifts to similarity infinity while center nesting and the two-sided first-hitting clock remain valid.

## 5. Center escape was already removed as an independent root

M18-043 audited adjacent first-hitting center displacement

\[
\mathfrak T_j
=
\frac{|X_{j+1}-X_j|}{r_j}.
\]

There is an exhaustive split:

\[
\boxed{
\sup_j\mathfrak T_j<\infty
\Longrightarrow
\text{one nested physical center},
}
\]

while unbounded displacement produces a fully formed remote active satellite.

Thus

\[
\boxed{
G_{center\ escape}
\Longrightarrow
\mathcal R_{remote/II}.
}
\]

Center escape is not a separate recurrent-core root.

## 6. Local compactness failure is already a strong branch

The ancient extraction uses only local information on fixed normalized parabolic cylinders:

- bounded normalized vorticity amplitude;
- bounded normalized enstrophy on compact backward intervals;
- stage-wide analyticity / local derivative control;
- time compactness from the vorticity equation.

Therefore a failure of local smooth compactness means that at least one of these controls breaks.

Those failures are already typed as

\[
\boxed{
G_{Z\text{-}escalation}
\lor
G_{high\ frequency}
\lor
G_{amplitude/Type\text{-}II}
\lor
G_{localization/turnover}.
}
\]

M18-043 and M18-046 further route these to

\[
\mathcal R_{remote/II}
\lor
G_{paid\ turnover\ ancestry}.
\]

Hence there is no independent local-compactness core-loss branch.

## 7. Spatial-tail non-tightness is not local core vanishing

A sequence may retain the fixed nonzero first-hitting core while losing global compactness through mass or critical structure at larger normalized radii.

This is exactly the distinction

\[
\boxed{
\text{local core nontriviality}
\neq
\text{global tail tightness}.
}
\]

M18-046 audited the global alternatives:

- weak-L3/frequency escalation routes to remote or paid turnover;
- bounded critical \(1/R\) tail can remain and is exactly energy-critical.

Thus spatial non-tightness of the global state routes to

\[
\boxed{
\mathcal R_{remote/II/historical}
\lor
G_{escaping\ critical\ tail/W1\ boundary}.
}
\]

It does not mean the normalized local core itself vanished.

## 8. Global realization failure is a tail/trace problem

The repository distinguishes:

1. local smooth ancient extraction;
2. global realized normalized orbit / RG reconstruction / terminal-trace package.

The first is available on the bounded compact corridor and preserves the nonzero core.

The second may fail because a required global tail, critical norm, pressure class, or terminal trace does not pass to the limit.

Such a failure is not a new local-core mechanism. It belongs to the global weak-critical/tail boundary problem:

\[
\boxed{
G_{global\ realization\ failure}
\subset
G_{escaping\ critical\ tail/W1\ boundary}
\lor
\mathcal R_{remote/historical}
}
\]

unless one of the already typed local compactness quantities first diverges.

This is a scope classification, not a claim that every global realization failure has already been analytically closed.

## 9. Stationary alpha-limit rigidity is auxiliary, not needed for nonvanishing

The checkpoint alpha-limit audit further shows that if a compact checkpoint alpha-limit exists and retains the suitable/local-energy pressure class, a stationary backward-Leray alpha-limit is excluded by the classical backward self-similar Liouville theorem together with checkpoint nontriviality.

This is a useful rigidity reduction, but the present module does not rely on it for ROOT-CERT recompression.

Dynamic periodic/aperiodic alpha-limits remain possible internal W1 realizations.

The essential certified statement here is only

\[
\boxed{
\text{compact checkpoint alpha-limit}
\Longrightarrow
\text{nonzero checkpoint core}.
}
\]

## 10. Retire the broad vanishing/escaping-core label

Combining the preceding sections:

### Vanishing core

Excluded on the compact first-hitting lane by the exact normalized mark and local smooth passage.

### Center escape

Routes to the remote-satellite complex.

### Local compactness loss

Routes to already typed amplitude/frequency/Z/turnover branches and hence to remote/II or paid turnover.

### Global/tail realization loss

Routes to the weak-critical escaping-tail/W1-boundary or remote/historical complex.

Therefore

\[
\boxed{
G_{vanishing/escaping\ recurrent\ core}
}
\]

should be retired as a primitive ROOT-CERT root.

## 11. Updated ROOT-CERT root menu

After M18-043--047, the upstream root structure compresses to four principal classes:

\[
\boxed{
\begin{aligned}
\mathcal R_1&:=\mathcal R_{remote/II/historical},\\
\mathcal R_2&:=G_{escaping\ critical\ tail/W1\ boundary/realization},\\
\mathcal R_3&:=G_{paid\ turnover\ ancestry},\\
\mathcal R_4&:=G_{temporal\ return\text{-}weight\ deficiency}.
\end{aligned}
}
\]

Everything audited so far upstream of the canonical survivor either enters one of these four or reaches the bounded compact ancient/canonical branch.

This is a major recompression, not a proof that the four roots are closed.

## 12. Relationship to downstream canonical analysis

On the complement of \(\mathcal R_1\)--\(\mathcal R_4\), the first-hitting sequence has:

- bounded normalized enstrophy;
- center nesting;
- two-sided stage clock;
- local smooth ancient compactness;
- a nonzero normalized active core;
- no weak-L3/frequency escalation;
- no quiet genealogy loss;
- no unpaid turnover escape.

This is the appropriate setting for the already-developed downstream canonical branch menu

\[
CP\!-\!E
\lor CP\!-\!S
\lor CE\!-\!T
\lor Migration
\lor CE\!-\!H.
\]

Thus the remaining global proof gap is no longer an amorphous collection of first-hitting failures. It is the explicit four-root upstream complex plus the downstream payer/ancestry endpoints.

## 13. Audit verdict

### Certified

1. First-hitting normalized ancient limits cannot vanish on the compact lane.
2. The nonzero point thickens to a fixed local active ball.
3. Backward checkpoint maxima stay in one fixed similarity ball under center nesting and two-sided clock control.
4. Center escape routes to remote active satellites.
5. Local compactness failure is already a typed strong branch.
6. Global realization failure is a tail/trace issue, not local core vanishing.
7. The broad vanishing/escaping-core label is not an independent root.

### Not certified

1. Closure of the remote/Type-II/historical root.
2. Closure of the escaping critical-tail/W1-boundary root.
3. A divergent parent budget for repeated paid turnover.
4. The needed ancestral physical return-density lower bound.
5. Global 3D Navier--Stokes regularity.

## 14. Next target

The next audit should no longer create another broad upstream branch label.

M18-048 should compare the two remaining **budget roots**

\[
G_{paid\ turnover\ ancestry}
\quad\text{and}\quad
G_{temporal\ return\text{-}weight\ deficiency}
\]

against the exact derivative-order ancestry law and the standard-energy parent ledger.

The key question is whether they are genuinely distinct or whether both are instances of one common problem:

\[
\boxed{
\text{fixed normalized event cost}
\stackrel{?}{\Longrightarrow}
\text{sufficient nonsummable parent physical charge}.
}
\]
