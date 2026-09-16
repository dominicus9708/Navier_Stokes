# M19-333 — The marked dilation hull inherits uniform spectral variance, so ratchet events already occur on nonmonochromatic cells

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / M19-321 TO M5-485 BRIDGE / SAME-GENERATION COUPLING / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Two structures live on the same retained generation sequence

M5-485 constructs the marked dilation hull from the retained generation sequence

\[
Z_j=(\mathcal V_j,\mathcal P_j,\mathcal O_j,\lambda_j,a_j),
\]

where

\[
a_j\in\{0,1\}
\]

is the positive-density ratchet indicator and

\[
\liminf_{N\to\infty}\frac1N\sum_{j=1}^Na_j\ge\delta_0>0.
\]

M19-319--321 apply to the same sufficiently late retained record cells and give

\[
q_{0,j}\asymp q_{1,j}\asymp q_{2,j}\asymp1,
\]

and the uniform spectral-variance gap

\[
\boxed{
\mathcal V_j
:=
q_{2,j}-\frac{q_{1,j}^2}{q_{0,j}}
\ge c_{var}>0.
}
\]

Thus the ratchet-marked sequence and the nonmonochromatic spectral sequence are not two independently selected subsequences.

## 2. No separate density-overlap theorem is needed at generation level

Because M19-321 holds for every sufficiently late retained record cell,

\[
\boxed{
a_j=1\quad\Longrightarrow\quad\mathcal V_j\ge c_{var}}
\]

for every sufficiently late marked generation.

Therefore

\[
\boxed{
\text{positive-density ratchet generations}
\subset
\text{uniformly nonmonochromatic generations}.
}
\]

This is stronger than having two positive-density event families and then seeking an ergodic overlap.

## 3. Passage to the compact marked hull

Let

\[
(\mathfrak H,\sigma,\mu,a)
\]

be the M5-485 compact marked shift hull.

On the no-defect/tight passage, the fixed-window quantities \(q_0,q_1,q_2\) pass continuously under the local smooth convergence plus the retained global tail control used in M19-319--321. Hence define the central spectral-width observable

\[
\mathcal V(\mathbf Y)
:=
q_2(\mathbf Y)-\frac{q_1(\mathbf Y)^2}{q_0(\mathbf Y)}.
\]

Then

\[
\boxed{
\mathcal V(\mathbf Y)\ge c_{var}>0
}
\]

on the retained hull component.

If this passage loses a fixed derivative/enstrophy amount at infinity, that failure is not hidden: it is routed to the already typed remote/frequency/representation compactness-defect branch.

## 4. Invariant-measure consequence

Since

\[
\int a\,d\mu\ge\delta_0>0
\]

and \(\mathcal V\ge c_{var}\) pointwise on the retained no-defect hull,

\[
\boxed{
\int a\,\mathcal V\,d\mu
\ge
c_{var}\delta_0>0.
}
\]

Thus the invariant marked hull has a strictly positive mean **joint ratchet–spectral-width observable**.

This is not merely a same-lag overlap: every marked state is already spectrally broad.

## 5. Exact CE-H refinement

On an exact CE-H compact lane,

\[
\Delta\Omega=\kappa\Omega.
\]

M19-322 gives

\[
\operatorname{Var}_\Omega(\kappa)
=
\frac{\mathcal V}{q_0}.
\]

Since \(q_0\le q_0^*<\infty\),

\[
\boxed{
\operatorname{Var}_\Omega(\kappa)
\ge c_\kappa>0
}
\]

on every retained hull state.

Hence

\[
\boxed{
\int a\,\operatorname{Var}_\Omega(\kappa)\,d\mu
\ge
c_\kappa\delta_0>0.
}
\]

Therefore every positive-mean ratchet component of the exact CE-H marked dilation hull is simultaneously a positive-mean coefficient-heterogeneity component.

## 6. Spatial/temporal variance split on ratchet-marked states

For each marked state,

\[
\operatorname{Var}_\Omega(\kappa)
=
\mathbb E_\nu[\operatorname{Var}_{\pi_s}(\kappa)]
+
\operatorname{Var}_\nu(\bar\kappa(s)).
\]

Multiplying by \(a\) and averaging gives

\[
\boxed{
\langle aV_{sp}\rangle
+
\langle aV_{tm}\rangle
\ge c_\kappa\delta_0.
}
\]

Thus at least one branch satisfies

\[
\boxed{
\langle aV_{sp}\rangle
\ge \frac12c_\kappa\delta_0
}
\]

or

\[
\boxed{
\langle aV_{tm}\rangle
\ge \frac12c_\kappa\delta_0.
}
\]

The ratchet channel must therefore coexist in invariant mean with either transverse coefficient-line segregation or effective-frequency breathing.

## 7. What this does and does not solve

This removes one possible incidence gap:

\[
\boxed{
\text{ratchet recurrence}
\not\perp
\text{spectral/coefficient heterogeneity at generation level}.
}
\]

However it does **not** prove that the material trajectory paying the ratchet lies spatially inside the coefficient-transition region at the same physical instant.

The remaining spatial-incidence question is finer:

\[
\boxed{
\text{same retained generation}
\neq
\text{same local carrier point/tube}.
}
\]

Thus one must not convert the joint mean into a local product of projective ratchet action and \(|\nabla\kappa|^2\) without an additional carrier-incidence theorem.

## 8. Relation to M19-324--332

If the joint branch is spatial, M19-324--332 reduce coefficient heterogeneity to

\[
\text{transverse line populations}
\to
\text{log-kappa diffusion / typed exits}
\to
\text{critical derivative balance}
\oplus
\text{relative-amplitude reweighting current}.
\]

M19-333 shows that this entire coefficient-current architecture is present on the same log-scale hull component that carries positive mean ratchet action.

If the joint branch is temporal, the ratchet hull simultaneously carries the M19-325 effective-frequency breathing channel.

Thus the terminal hard core now carries **two coupled recurrent critical structures on one invariant component**, not two unrelated survivor families.

## 9. New immediate target

The next useful theorem is not another density-overlap lemma. It is a **same-carrier incidence or cocycle theorem**:

1. spatial branch: force the ratchet-paying material lineage to intersect or control the transverse coefficient-segregation current;
2. temporal branch: couple the ratchet mark to the effective-frequency phase current;
3. or construct a bounded log-scale cocycle from their joint action.

Any strict bounded cocycle

\[
\Phi\circ\sigma-\Phi
\ge c\,a
\]

would contradict M5-485 invariance immediately.

## 10. Conclusion

The M5-485 marked dilation hull and the M19-321 spectral-width gap are properties of the same retained generation sequence. Therefore the positive-density ratchet cannot hide on asymptotically monochromatic cells.

\[
\boxed{
\int a\,\mathcal V\,d\mu>0,
}
\]

and on exact CE-H

\[
\boxed{
\int a\,\operatorname{Var}_\Omega(\kappa)\,d\mu>0.
}
\]

\[
\boxed{
\text{M19-333 COMPLETE; THE REMAINING GAP IS LOCAL SAME-CARRIER INCIDENCE OR A JOINT STRICT COCYCLE.}
}
\]
