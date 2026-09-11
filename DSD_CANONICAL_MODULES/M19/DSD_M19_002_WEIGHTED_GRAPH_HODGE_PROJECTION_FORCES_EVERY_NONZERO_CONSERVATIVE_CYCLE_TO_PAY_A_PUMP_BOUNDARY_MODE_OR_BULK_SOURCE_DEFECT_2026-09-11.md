# M19-002 — Weighted graph Hodge projection forces every nonzero conservative cycle to pay a pump, boundary-mode, or bulk-source defect

**Date:** 2026-09-11  
**Status:** CALCULATION / QUANTITATIVE CYCLE-DEFECT FLOOR / DEFECT ROUTING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-001

On the controlled finite persistent-population graph, M19-001 gives the mean exchange current

\[
\boxed{
\bar j
=
\bar G B^T\bar V
+r,
}
\]

where

\[
\boxed{
r
:=
r^{pump}
+\bar r^{mode}
+\bar r^{src}.
}
\]

Here \(\bar G\) is a positive diagonal edge-conductance matrix with

\[
0<G_-\le \bar G_e\le G_+<\infty.
\]

The conductance-pump term is

\[
\boxed{
r^{pump}
=
\left\langle
(G-\bar G)B^T(V-\bar V)
\right\rangle.
}
\]

## 2. Conservative mean-cycle branch

The present module works on the recurrent conservative redistribution branch

\[
\boxed{B\bar j=0.}
\]

This is the cycle-space branch after node-storage drift and explicitly separated source/sink terms have zero recurrent mean or have been removed into the defect/source ledger.

No claim is made that every instantaneous current is divergence-free.

## 3. Weighted edge inner product

Define

\[
\boxed{
\langle x,y\rangle_{\bar G^{-1}}
:=
x^T\bar G^{-1}y
}
\]

and

\[
\|x\|_{\bar G^{-1}}^2
:=x^T\bar G^{-1}x.
\]

Let

\[
\mathcal C:=\ker B
\]

be the cycle space and

\[
\mathcal G
:=
\operatorname{ran}(\bar G B^T)
\]

be the fixed-conductance gradient space.

## 4. Exact weighted orthogonality

Take

\[
z\in\mathcal C,
\qquad
 g=\bar G B^TV\in\mathcal G.
\]

Then

\[
\begin{aligned}
\langle z,g\rangle_{\bar G^{-1}}
&=
z^T\bar G^{-1}\bar G B^TV\\
&=
z^TB^TV\\
&=(Bz)^TV\\
&=0.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal C
\perp_{\bar G^{-1}}
\mathcal G.
}
\]

This is the discrete weighted Hodge decomposition associated with the mean conductance.

## 5. Project the M19-001 identity onto cycle space

Let

\[
P_{\mathcal C}^{\bar G^{-1}}
\]

be the orthogonal projection onto \(\mathcal C\) in the \(\bar G^{-1}\) metric.

Because

\[
\bar j\in\mathcal C,
\]

and

\[
\bar G B^T\bar V\in\mathcal G,
\]

projecting

\[
\bar j
=
\bar G B^T\bar V+r
\]

gives

\[
\boxed{
\bar j
=
P_{\mathcal C}^{\bar G^{-1}}r.
}
\]

Therefore

\[
\boxed{
\|\bar j\|_{\bar G^{-1}}
\le
\|r\|_{\bar G^{-1}}.
}
\]

This is the quantitative cycle-defect inequality.

## 6. Three-way defect floor

Using

\[
r
=
r^{pump}+\bar r^{mode}+\bar r^{src},
\]

and the triangle inequality,

\[
\|\bar j\|_{\bar G^{-1}}
\le
\|r^{pump}\|_{\bar G^{-1}}
+
\|\bar r^{mode}\|_{\bar G^{-1}}
+
\|\bar r^{src}\|_{\bar G^{-1}}.
\]

Hence if the recurrent mean cycle has a fixed floor

\[
\boxed{
\|\bar j\|_{\bar G^{-1}}
\ge j_*>0,
}
\]

then at least one of

\[
\boxed{
\|r^{pump}\|_{\bar G^{-1}}
\ge\frac{j_*}{3},
}
\]

\[
\boxed{
\|\bar r^{mode}\|_{\bar G^{-1}}
\ge\frac{j_*}{3},
}
\]

or

\[
\boxed{
\|\bar r^{src}\|_{\bar G^{-1}}
\ge\frac{j_*}{3}
}
\]

must hold.

Thus a nonzero conservative recurrent cycle cannot be an arbitrarily small coarse-graining artifact.

## 7. Quantify the conductance-pump branch

Let

\[
\mathcal K(\theta)
:=
\bar G^{-1/2}(G(\theta)-\bar G)\bar G^{-1/2}.
\]

Then

\[
\begin{aligned}
\|r^{pump}\|_{\bar G^{-1}}
&=
\left\|
\left\langle
\bar G^{-1/2}(G-\bar G)B^T(V-\bar V)
\right\rangle
\right\|_2\\
&\le
\left\langle
\|\mathcal K\|_{op}
\,
\|\bar G^{1/2}B^T(V-\bar V)\|_2
\right\rangle.
\end{aligned}
\]

By Cauchy--Schwarz,

\[
\boxed{
\|r^{pump}\|_{\bar G^{-1}}
\le
\left\langle\|\mathcal K\|_{op}^2\right\rangle^{1/2}
\left\langle
\|\bar G^{1/2}B^T(V-\bar V)\|_2^2
\right\rangle^{1/2}.
}
\]

On the compact CE-H population branch, \(\rho\) is uniformly bounded for every fixed finite \(p\), hence the coarse \(u_p\)-potentials are bounded. The finite graph and conductance bounds then give

\[
\left\langle
\|\bar G^{1/2}B^T(V-\bar V)\|_2^2
\right\rangle^{1/2}
\le C_V<\infty.
\]

Therefore a pump floor

\[
\|r^{pump}\|_{\bar G^{-1}}\ge c_*>0
\]

forces

\[
\boxed{
\left\langle\|\mathcal K\|_{op}^2\right\rangle^{1/2}
\ge
\frac{c_*}{C_V}.
}
\]

Thus a fixed pump cycle requires a fixed amount of conductance/connector modulation unless the coarse-potential compactness itself fails.

## 8. Boundary-mode branch gives a trace-heterogeneity floor

For every controlled connector, the map

\[
\text{nonconstant endpoint trace}
\longmapsto
\text{integrated mode flux}
\]

is a bounded linear functional on the trace space, uniformly on a compact connector family.

Hence there exists \(C_{tr}<\infty\) such that

\[
\boxed{
\|r^{mode}\|
\le
C_{tr}\|g^\perp\|_{H^{1/2}(\partial C)}.
}
\]

Therefore a fixed mode-current floor forces

\[
\boxed{
\|g^\perp\|_{H^{1/2}}
\ge c_{mode}>0.
}
\]

By the Dirichlet principle / trace extension bound, nontrivial trace heterogeneity requires nontrivial interior gradient energy of the corresponding harmonic mode:

\[
\boxed{
\int_C
\nabla u^{mode}\cdot A\nabla u^{mode}
\ge c_E>0
}
\]

on a uniformly controlled connector family.

For

\[
u_p=\rho^p/p,
\]

this is a genuine weighted amplitude-gradient/interface payment, not an abstract graph artifact.

## 9. Bulk-source branch gives a source norm floor

The zero-boundary source solution satisfies the standard elliptic estimate

\[
\|u^{src}\|_{H^1_0(C)}
\le C_{ell}\|f\|_{H^{-1}(C)}.
\]

The integrated source flux is a bounded functional of \(u^{src}\), so

\[
\boxed{
\|r^{src}\|
\le C_{src}\|f\|_{H^{-1}(C)}.
}
\]

Thus a fixed source-current floor forces

\[
\boxed{
\|L_\theta u_p\|_{H^{-1}(C)}
\ge c_{src}>0.
}
\]

This returns the cycle to a concrete bulk CE-H derivative/source quantity.

No sign is claimed for this source norm at this stage.

## 10. M19-002 routing theorem

On the controlled conservative mean-cycle branch,

\[
\boxed{
\|\bar j\|_{\bar G^{-1}}
\ge j_*>0
}
\]

forces at least one of

\[
\boxed{
G_{conductance\ modulation},
}
\]

\[
\boxed{
G_{boundary\ trace/gradient\ mode},
}
\]

or

\[
\boxed{
G_{bulk\ amplitude\ source}
}
\]

with a fixed quantitative floor.

If the connector compactness required above fails, record separately

\[
\boxed{G_{connector\ geometry/topology\ degeneration}.}
\]

## 11. What has been closed

The branch

\[
\boxed{
\text{nonzero conservative finite-lineage cycle}
\text{ carried only by a fixed symmetric conductance gradient}
}
\]

is closed.

More strongly, a fixed cycle cannot be approximated by such a gradient with all defects tending to zero.

## 12. What remains in this calculation complex

The next calculation should identify the M18 ancestry of each defect:

1. conductance modulation \(\to\) controlled transverse-strain/connector-geometry work or geometry degeneration;
2. boundary trace mode \(\to\) weighted amplitude-gradient / sheath / interface payer;
3. bulk source \(\to\) CE-H coefficient/strain/diffusion source terms.

The useful question is whether all three descend to already certified M18 currencies, leaving no new independent CE-H cycle currency.

---

\[
\boxed{\text{M19-002 COMPLETE AS A CALCULATION STEP; GLOBAL REGULARITY REMAINS OPEN.}}
\]
