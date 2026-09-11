# M18-090 — Jordan decomposition of population edge diffusion: multi-p reweighting controls one-sign sectors but not the net cycle current without a noncancellation or ordering gap

**Date:** 2026-09-11  
**Status:** SIGNED-EDGE MEASURE / MULTI-P REWEIGHTING AUDIT / FALSE CYCLE-MONOTONICITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-089 realizes the population boundary defect as the explicit antisymmetric edge current

\[
\boxed{
e_{ij}^{(p)}
=
\int_{S_{ij}}
\rho^{p-1}\partial_{n_i}\rho\,dS,
\qquad
 e_{ji}^{(p)}=-e_{ij}^{(p)}.
}
\]

For \(q>p\),

\[
e_{ij}^{(q)}
=
\int_{S_{ij}}
\rho^{q-p}
\rho^{p-1}\partial_{n_i}\rho\,dS.
\]

Because the normal-gradient measure is signed, the positive change-of-measure/covariance machinery of M18-062 does not apply directly.

The present module performs the exact Jordan decomposition.

The result is:

- each one-sign interface sector has a clean positive amplitude reweighting law;
- the **net** edge current may change magnitude or sign under higher-amplitude weighting because positive and negative sectors are reweighted differently;
- therefore multi-\(p\) edge consistency alone does not exclude a conservative directed cycle.

A new obstruction requires either a sign-definite interface, a quantitative noncancellation gap, or a genuine scalar ordering/conductance law.

---

## 2. Signed normal-diffusion measure

Fix one oriented interface

\[
S_{ij}
\]

with normal \(n_i\) pointing outward from population \(i\).

Define the signed measure

\[
\boxed{
d\mu_{ij}
:=
\partial_{n_i}\rho\,dS.
}
\]

Then

\[
\boxed{
e_{ij}^{(p)}
=
\int\rho^{p-1}d\mu_{ij}.
}
\]

Take its Jordan decomposition

\[
\boxed{
\mu_{ij}=\mu_{ij}^+-\mu_{ij}^-.
}
\]

The positive and negative measures are supported on

\[
S_{ij}^+
:=
\{\partial_{n_i}\rho>0\},
\]

and

\[
S_{ij}^-
:=
\{\partial_{n_i}\rho<0\}
\]

up to null sets.

---

## 3. Positive and negative edge contributions

Define

\[
\boxed{
e_{ij,+}^{(p)}
:=
\int\rho^{p-1}d\mu_{ij}^+
\ge0,
}
\]

\[
\boxed{
e_{ij,-}^{(p)}
:=
\int\rho^{p-1}d\mu_{ij}^-
\ge0.
}
\]

Then

\[
\boxed{
e_{ij}^{(p)}
=
e_{ij,+}^{(p)}-e_{ij,-}^{(p)}.
}
\]

The total variation current is

\[
\boxed{
|e|_{TV}^{(p)}
:=
e_{ij,+}^{(p)}+e_{ij,-}^{(p)}.
}
\]

Large total variation can coexist with small net current when the two sectors nearly cancel.

---

## 4. Exact multi-p reweighting on each Jordan sector

Let

\[
q>p\ge2.
\]

On the positive sector, whenever

\[
e_{ij,+}^{(p)}>0,
\]

define the probability measure

\[
\boxed{
d\pi_{ij,+}^{(p)}
:=
\frac{
\rho^{p-1}d\mu_{ij}^+
}{
e_{ij,+}^{(p)}
}.
}
\]

Then

\[
\boxed{
\frac{e_{ij,+}^{(q)}}{e_{ij,+}^{(p)}}
=
\mathbb E_{\pi_{ij,+}^{(p)}}
[\rho^{q-p}].
}
\]

Similarly, on the negative sector,

\[
\boxed{
\frac{e_{ij,-}^{(q)}}{e_{ij,-}^{(p)}}
=
\mathbb E_{\pi_{ij,-}^{(p)}}
[\rho^{q-p}].
}
\]

Thus each sign sector has an exact positive change-of-measure law.

---

## 5. Net current formula

Set

\[
R_+
:=
\mathbb E_{\pi_{ij,+}^{(p)}}[\rho^{q-p}],
\]

\[
R_-
:=
\mathbb E_{\pi_{ij,-}^{(p)}}[\rho^{q-p}].
\]

Then

\[
\boxed{
e_{ij}^{(q)}
=
R_+e_{ij,+}^{(p)}
-
R_-e_{ij,-}^{(p)}.
}
\]

Compare with

\[
e_{ij}^{(p)}
=
e_{ij,+}^{(p)}-e_{ij,-}^{(p)}.
\]

The two exponents differ only because the positive and negative normal-gradient sectors see different amplitude moments.

---

## 6. Exact sign-flip criterion

Suppose

\[
e_{ij,+}^{(p)}>0,
\qquad
e_{ij,-}^{(p)}>0.
\]

Define the cancellation ratio

\[
\boxed{
r_p
:=
\frac{e_{ij,-}^{(p)}}{e_{ij,+}^{(p)}}.
}
\]

Then

\[
e_{ij}^{(p)}>0
\iff
r_p<1.
\]

At exponent \(q\),

\[
e_{ij}^{(q)}>0
\iff
r_p<\frac{R_+}{R_-}.
\]

Therefore a sign flip between \(p\) and \(q\) occurs exactly when the cancellation ratio crosses the amplitude-reweighting threshold.

For example,

\[
\boxed{
e_{ij}^{(p)}>0,
\quad
e_{ij}^{(q)}<0
}
\]

is possible whenever

\[
\boxed{
\frac{R_+}{R_-}<r_p<1.
}
\]

Thus the net edge orientation is not exponent-invariant.

---

## 7. Explicit two-sector toy witness

Take two interface sectors of equal geometric measure.

On the positive normal-gradient sector set

\[
\rho=a,
\qquad
\partial_n\rho=+g_+,
\]

and on the negative sector set

\[
\rho=b>a,
\qquad
\partial_n\rho=-g_-.
\]

Then

\[
e^{(p)}
\propto
 a^{p-1}g_+
-
b^{p-1}g_-.
\]

Choose \(g_-/g_+\) so that

\[
\left(\frac ab\right)^{q-1}
<
\frac{g_-}{g_+}
<
\left(\frac ab\right)^{p-1}.
\]

Then

\[
\boxed{
e^{(p)}>0,
\qquad
e^{(q)}<0.
}
\]

Therefore even a smooth two-sector interface can reverse its net diffusive exchange direction under higher-amplitude weighting.

No exotic geometry is needed.

---

## 8. Interface amplitude bounds control sectors, not cancellation

Suppose on one controlled interface

\[
0<a\le\rho\le b<\infty.
\]

Then on each Jordan sector,

\[
\boxed{
a^{q-p}e_+^{(p)}
\le
e_+^{(q)}
\le
b^{q-p}e_+^{(p)},
}
\]

and

\[
\boxed{
a^{q-p}e_-^{(p)}
\le
e_-^{(q)}
\le
b^{q-p}e_-^{(p)}.
}
\]

But no comparable two-sided bound for the **net** current follows when

\[
e_+^{(p)}\approx e_-^{(p)}.
\]

Near cancellation, a small change of amplitude weighting can produce a large relative change of net current.

This is the edge-current analogue of the re-recording/noncancellation firewall.

---

## 9. Quantitative noncancellation gap

Define

\[
\boxed{
\chi_{ij}^{(p)}
:=
\frac{|e_{ij}^{(p)}|}
{e_{ij,+}^{(p)}+e_{ij,-}^{(p)}}
\in[0,1].
}
\]

If

\[
\chi_{ij}^{(p)}\ge\chi_0>0,
\]

then the edge has a fixed fractional orientation bias at exponent \(p\).

Under an additional bound controlling the relative reweighting

\[
R_+/R_-
\]

near one, this bias can propagate to nearby exponents.

Without such a gap, sign persistence is not robust.

Therefore the correct extra hypothesis is not merely nonzero net current, but **noncancellation plus controlled amplitude contrast between the two normal-gradient sectors**.

---

## 10. One-sign interface branch

If

\[
\boxed{
\partial_{n_i}\rho\ge0
\quad\text{a.e. on }S_{ij},
}
\]

then

\[
e_{ij,-}^{(p)}=0
\]

and hence

\[
\boxed{
e_{ij}^{(p)}\ge0
\qquad\forall p\ge2.
}
\]

If the positive sector has nonzero measure and \(\rho>0\), the inequality is strict.

Likewise a one-sign negative interface preserves negative orientation for every exponent.

Thus exponent-invariant edge direction is guaranteed on a one-sign normal-gradient interface.

---

## 11. One-sign edges still do not automatically kill a directed cycle

Suppose every edge in a graph cycle has one-sign normal gradient in the chosen cycle orientation.

This does **not** by itself give a contradiction.

The edge statement is local:

\[
\partial_{n_i}\rho>0
\]

at the interface from \(i\) to \(j\).

It does not supply one scalar vertex value \(\rho_i\) satisfying

\[
\rho_j>\rho_i
\]

for the entire populations.

A single population may have different amplitude ranges on different boundary components.

Therefore a directed cycle of locally outward-increasing interfaces is not ruled out by scalar transitivity unless a **population ordering theorem** is added.

This blocks another tempting shortcut.

---

## 12. Gradient-field exactness does not directly imply graph-gradient exactness

At exponent \(p\),

\[
\rho^{p-1}\nabla\rho
=
\frac1p\nabla(\rho^p).
\]

Thus the continuum diffusive flux is a gradient field.

However the graph edge variable is a **surface flux integral**

\[
e_{ij}^{(p)}
=
\frac1p
\int_{S_{ij}}\partial_{n_i}(\rho^p)dS,
\]

not a line integral of \(d(\rho^p)\) between two scalar vertex potentials.

Without a conductance/Dirichlet-to-Neumann reduction proving

\[
e_{ij}^{(p)}
=G_{ij}(V_j-V_i),
\qquad G_{ij}>0,
\]

one cannot place the edge current in the graph-gradient subspace \(\operatorname{im}B^T\).

Therefore

\[
\boxed{
\text{continuum gradient flux}
\not\Rightarrow
\text{graph-gradient edge current}
}

under coarse population integration alone.

---

## 13. Multi-p cycle consistency theorem that is actually valid

For a fixed directed graph cycle \(C\), if every edge satisfies

1. a uniform noncancellation gap
   \[
   \chi_{ij}^{(p)}\ge\chi_0>0;
   \]
2. a controlled Jordan-sector amplitude contrast preserving the edge sign from \(p\) to \(q\);

then the directed cycle orientation persists at exponent \(q\).

This is only a **sign-persistence theorem**.

It does not make the cycle impossible.

The surviving cycle then becomes a stronger object:

\[
\boxed{
\text{same oriented diffusive population cycle across multiple amplitude exponents}.
}
\]

Such a branch is more rigid but still requires a graph-potential or dissipation theorem for closure.

---

## 14. Cancellation-dominated branch

If the noncancellation condition fails repeatedly, then

\[
\chi_{ij}^{(p)}\to0
\]

on recurrent current edges.

Thus

\[
\boxed{
|e_{ij}^{(p)}|
\ll
|e|_{TV}^{(p)}.
}
\]

The interface carries large opposing inward/outward diffusive fluxes with small net transfer.

This is a genuine **reversible interface-mixing branch**.

It is structurally aligned with

- M18-077 zero-mean reversible lineage activity;
- M18-082 fixed-metric redistribution oscillation;
- M18-070 core/sheath coexistence.

Hence cancellation is not an untyped escape.

---

## 15. Updated finite-network split

The explicit population exchange network now splits as

\[
\boxed{
G_{edge\ exchange}
\Longrightarrow
\begin{cases}
G_{one\text{-}sign/noncanceling\ edge\ cycle},\\
G_{cancellation\text{-}dominated\ reversible\ interface},\\
G_{interface\ geometry/realization\ loss},\\
G_{external\ export/import}.
\end{cases}
}
\]

The second branch is already in the recurrent reversible architecture.

The first branch is the natural place to seek a conductance or population-ordering theorem.

---

## 16. Highest-value next target

M18-091 should test whether the one-sign/noncanceling branch admits a **Dirichlet-to-Neumann graph reduction**.

On each material population solve or characterize the scalar amplitude field \(u_p:=\rho^p/p\).

The edge current is

\[
e_{ij}^{(p)}
=
\int_{S_{ij}}\partial_{n_i}u_p\,dS.
\]

The question is whether, after eliminating the interior fields at one time, the interface flux vector is generated by a symmetric positive Dirichlet-to-Neumann operator on boundary traces.

Such an operator exists at the continuum boundary level, but collapsing it to one scalar per population is nontrivial.

A successful finite-dimensional reduction could kill an unconstrained graph cycle; failure would identify precisely which within-population boundary modes carry the cycle.

---

## 17. Audit verdict

### Certified

1. Every population edge current has an exact Jordan decomposition into positive and negative normal-gradient sectors.
2. Each sector obeys a positive multi-p amplitude reweighting law.
3. The net edge current can change sign between exponents because the two sectors are reweighted differently.
4. A smooth two-sector toy interface explicitly realizes this sign flip.
5. Interface amplitude bounds control sector magnitudes but not near-cancelled net current.
6. A quantitative noncancellation gap is the correct condition for robust edge orientation.
7. One-sign normal gradients preserve orientation across all p, but do not alone produce a global population ordering.
8. Continuum gradient exactness does not automatically reduce to graph-gradient exactness after surface integration.
9. Cancellation-dominated interfaces realize the already known reversible-current architecture.

### Still open

- graph conductance/Dirichlet-to-Neumann reduction on the noncanceling branch;
- exclusion of persistent multi-p directed cycles;
- reversible interface-mixing rigidity;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 18. Next target

M18-091 should determine the strongest exact finite-dimensional graph structure obtainable from the continuum Dirichlet-to-Neumann map without assuming each population is approximately constant in amplitude.
