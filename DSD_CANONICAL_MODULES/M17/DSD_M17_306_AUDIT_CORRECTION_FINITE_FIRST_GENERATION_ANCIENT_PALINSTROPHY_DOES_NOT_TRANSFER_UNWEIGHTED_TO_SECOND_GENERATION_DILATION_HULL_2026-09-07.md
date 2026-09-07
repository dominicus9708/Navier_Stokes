# DSD M17-306 — Audit correction: finite first-generation ancient palinstrophy does not transfer unweighted to the second-generation dilation hull

Date: 2026-09-07  
Canonical ID: **M17-306**

Status: **AUDIT CORRECTION / M17-304 CORRECTLY DERIVED THE SIMILARITY JACOBIANS FOR ONE GIVEN ANCIENT SOLUTION, BUT IT THEN IDENTIFIED THE RECURRENT SIMILARITY/DILATION-HULL SOLUTION USED BY M5-526 AND LATE M17 WITH THE FIRST MARKED ANCIENT ELEMENT OF M5-474--477. M5-483 SHOWS THAT THIS IS NOT THE REPOSITORY GENEALOGY: THE RECURRENT HARD CORE IS OBTAINED AFTER A SECOND BACKWARD RECORD BLOW-DOWN `V_m(y,s)=R_m V(R_m y,R_m^2 s)`. THE FIRST ANCIENT ELEMENT'S FINITE TOTAL PALINSTROPHY THEREFORE DOES NOT PASS AS AN UNWEIGHTED FINITE TOTAL PALINSTROPHY BUDGET TO THE SECOND-GENERATION CELL/HULL. IN FACT THE PALINSTROPHY SPACETIME INTEGRAL SCALES BY THE SUPERCRITICAL FACTOR `R_m`. ONLY THE SCALE-WEIGHTED QUANTITY `R_m^{-1} int |grad Omega_m|^2` IS DIRECTLY IDENTIFIED WITH THE ANCESTRAL PALINSTROPHY OVER THE CORRESPONDING PHYSICAL WINDOW. CONSEQUENTLY M17-304'S CLAIMS `int_{theta0}^infinity ||grad W||_2^2<infinity` AND `int_{theta0}^infinity ||W||_2^2<infinity` FOR THE RECURRENT SECOND-GENERATION HULL ARE RETRACTED UNLESS A NEW ANCESTRY-TRANSFER THEOREM IS PROVED. M17-303'S PACKET PHYSICALIZATION FORMULAS REMAIN VALID. M17-305'S PURE MULTIPLICITY/SPECTRAL-DEFICIT ALGEBRA REMAINS A CONDITIONAL INSUFFICIENCY CALCULATION, BUT ITS INTERPRETATION AS CONTRADICTING THE M17-304 FINITE HULL LEDGERS IS RETRACTED. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. The two ancient generations must be distinguished

M5-474 extracts a first marked ancient Navier--Stokes element, which we denote here by

\[
(V,\Omega)(x,t).
\]

M5-477 proves for this first ancient element

\[
\boxed{
\int_{-\infty}^{0}
\|\nabla_x\Omega(t)\|_2^2dt<\infty.
}
\]

However M5-483 then forms backward record-scale cells

\[
\boxed{
V_m(y,s)
:=R_mV(R_my,R_m^2s),
}
\]

and passes to a parabolic dilation hull.

Thus the recurrent/dilation hard core used by later similarity analysis is a **blow-down descendant** of the first ancient element, not simply the same solution written in logarithmic time.

The chain is

\[
\boxed{
\text{first marked ancient element}
\to
\text{record blow-down cells}
\to
\text{second-generation parabolic dilation hull}.
}
\]

Any resource transfer across this arrow requires its own scaling and compactness theorem.

---

## 2. Exact vorticity scaling of the record cells

Let

\[
\Omega_m:=\nabla_y\times V_m.
\]

Since

\[
V_m(y,s)=R_mV(R_my,R_m^2s),
\]

we have

\[
\boxed{
\Omega_m(y,s)
=R_m^2\Omega(R_my,R_m^2s).
}
\]

Differentiating once more,

\[
\boxed{
\nabla_y\Omega_m(y,s)
=R_m^3\nabla_x\Omega(R_my,R_m^2s).
}
\]

The spacetime Jacobian is

\[
dy=R_m^{-3}dx,
\qquad
ds=R_m^{-2}dt.
\]

---

## 3. Palinstrophy spacetime scaling is supercritical

For any time interval `I` in the cell variable `s`,

\[
\begin{aligned}
\int_I\int_{\mathbb R^3}
|\nabla_y\Omega_m|^2dy\,ds
&=R_m^6R_m^{-3}R_m^{-2}
\int_{R_m^2I}\int
|\nabla_x\Omega|^2dx\,dt\\
&=\boxed{
R_m
\int_{R_m^2I}
\|\nabla_x\Omega(t)\|_2^2dt.
}
\end{aligned}
\]

In particular, when the entire ancient interval is represented,

\[
\boxed{
\mathscr P_m
:=
\int_{-\infty}^{0}
\|\nabla\Omega_m(s)\|_2^2ds
=R_m\mathscr P_{anc},
}
\]

where

\[
\mathscr P_{anc}
:=
\int_{-\infty}^{0}
\|\nabla\Omega(t)\|_2^2dt<\infty.
\]

Thus finite ancestral palinstrophy becomes a budget that may grow linearly in the blow-down factor.

Therefore

\[
\boxed{
\mathscr P_{anc}<\infty
\not\Rightarrow
\sup_m\mathscr P_m<\infty.
}
\]

This is exactly why the second-generation recurrent hull can carry persistent normalized derivative activity without contradicting M5-477.

---

## 4. The scale-weighted quantity that really transfers

Rearranging the exact scaling identity gives

\[
\boxed{
R_m^{-1}
\int_I\|\nabla\Omega_m(s)\|_2^2ds
=
\int_{R_m^2I}
\|\nabla\Omega(t)\|_2^2dt.
}
\]

Hence

\[
\boxed{
R_m^{-1}\mathscr P_m
=\mathscr P_{anc}.
}
\]

The inherited currency is therefore scale weighted.

A unit-order second-generation palinstrophy event at record scale `R_m` may cost only order

\[
\boxed{R_m^{-1}}
\]

when charged back to the first ancient generation.

For geometric record scales this is summable:

\[
\sum_mR_m^{-1}<\infty.
\]

This reproduces, at the inter-generation level, the same R21 firewall seen in M5-598 and M17-303:

\[
\boxed{
\text{fixed normalized descendant cost}
\not\Rightarrow
\text{fixed ancestral physical cost}.
}
\]

---

## 5. Why M17-304's similarity Jacobians were not themselves wrong

For a single ancient solution `mathcal U` and its own logarithmic similarity transform, the formulas derived in M17-304 are algebraically correct.

The invalid step was the substitution

\[
\boxed{
\text{M5-477 finite first-generation palinstrophy}
\Longrightarrow
\text{finite forward similarity palinstrophy of the second-generation hull}.
}
\]

M5-483 inserts a nontrivial blow-down between those objects.

Therefore the following M17-304 claims are retracted for the recurrent second-generation hull unless an additional ancestry-transfer theorem is supplied:

\[
\int_{\theta_0}^{\infty}
\|\nabla W(\theta)\|_2^2d\theta<\infty,
\]

and

\[
\int_{\theta_0}^{\infty}
\|W(\theta)\|_2^2d\theta<\infty.
\]

No assertion is made that these integrals must be infinite; only that M5-477 does not prove their finiteness for the descendant hull.

---

## 6. Consequence for M17-303

M17-303's local rescaling identities are unaffected:

\[
\boxed{
\int |\nabla_yW|^2dy\,d\theta
=m_j
\int |\nabla_zV_j|^2dz\,d\tau,
}
\]

and

\[
\boxed{
\int |W|^2dy\,d\theta
=m_jr_j^2
\int |V_j|^2dz\,d\tau.
}
\]

These are within one representation and use no inter-generation resource transfer.

What is withdrawn is only the claim that the left-hand sides possess the M17-304 finite forward-tail budget by inheritance from M5-477.

Thus R21 remains fully active.

---

## 7. Consequence for M17-305

M17-305 contains two logically separable statements.

### 7.1 Surviving algebraic statement

Conditional on the unresolved M17-298 allocation theorem, bounded packet-mass overlap plus the logarithmic scale floor yields

\[
\boxed{
\Lambda_k:=\frac{H_k^{sh}}{E_k^{sh}}
\lesssim(\log R_k)^2.
}
\]

The calculation that `O(log R_k)` unit-window multiplicity and this spectral cap cannot recover the critical shell currency `b_k^(3/2)` from the currently guaranteed interface-payment floors is algebraically unchanged.

It remains a useful **insufficiency theorem for the present multiplicity strategy**.

### 7.2 Retracted interpretation

The sentence that this failure prevents contradiction with already established finite M17-304 second-generation interface ledgers is withdrawn.

Those finite ledgers are not established.

The correct conclusion is only

\[
\boxed{
\text{current log-time/geometric multiplicity does not produce the desired critical currency}.
}
\]

A future proof still needs a legitimate terminal resource or a different closing mechanism.

---

## 8. The correct new ancestry target

The useful question is now not whether the second-generation hull has finite unweighted total palinstrophy.

It is whether some **scale-critical ancestral charge** survives the record blow-down with the correct multiplicity.

The exact starting currency is

\[
\boxed{
R_m^{-1}
\int |\nabla\Omega_m|^2.
}
\]

Possible closing mechanisms must therefore do one of the following:

1. produce at least order `R_m` independent descendant payments per record scale without double counting;
2. transfer the M17-207 critical shell currency directly across generations without the `R_m^{-1}` loss;
3. produce strict physical scale descent ending at a nodal/regularity endpoint;
4. identify a scale-invariant signed/monotone quantity rather than raw palinstrophy;
5. prove a new ancestry theorem stronger than the generic record-cell scaling.

---

## 9. DSD audit

- Ancient-generation labels are now explicit.
- No finite norm of the first ancient element is assigned automatically to a blow-down limit.
- The exact scaling exponent of vorticity palinstrophy is retained.
- A scale-weighted inherited budget is not confused with an unweighted descendant budget.
- M17-303 is preserved because its rescaling is internal to one packet representation.
- M17-305 is downgraded only in interpretation, not in its conditional arithmetic.
- This correction is analogous in role to M17-302: a useful late argument is retained after removing an unsupported bridge.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
