# M18-075 — Material-surface current splits orthogonally into label redistribution and label-invisible circulation

**Date:** 2026-09-11  
**Status:** MATERIAL-LABEL MOMENT AUDIT / SURFACE HODGE SPLIT / CURRENT-TO-MIGRATION ANTI-SHORTCUT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-074 shows that, unless the active director-twist/self-helicity channel has a uniform positive floor, the compact CE-H hull contains an exact Frobenius-integrable state with a local vortex-transverse material patch carrying nonzero surface current.

M5-521 proves that material-label moments satisfy

\[
\frac d{d\theta}M_\psi
=
\int_{\Sigma(\theta)}
\nabla_\Sigma\psi\cdot J_\Sigma\,dA
\]

for materially transported scalar label functions \(\psi\), up to the explicitly retained boundary term.

A tempting converse is

\[
J_\Sigma\ne0
\Longrightarrow
\text{material-label redistribution}.
\]

That converse is false.

Only the component of \(J_\Sigma\) lying in the closure of surface gradients is visible to scalar material-label moments.

The orthogonal component may circulate tangentially while leaving every such scalar moment unchanged instantaneously.

The present module records the exact Hilbert-space split and makes the remaining signed route precise.

## 2. Controlled material patch and boundary firewall

Let \(\Sigma\) be one smooth compact material surface patch in the integrable branch of M18-074.

Work first with the test space

\[
\mathcal H_0
:=
H_0^1(\Sigma),
\]

or equivalently with smooth scalar labels compactly supported away from \(\partial\Sigma\).

This removes the boundary-current term from the weak identity.

If a fixed fraction of the current is trapped arbitrarily close to \(\partial\Sigma\) so that no interior cutoff retains it, record that separately as

\[
\boxed{G_{surface\ boundary/export}.}
\]

The analysis below concerns the retained interior current.

## 3. Gradient subspace

Define the closed gradient subspace of tangent \(L^2\) vector fields

\[
\boxed{
\mathcal G_\Sigma
:=
\overline{
\{\nabla_\Sigma\psi:\psi\in H_0^1(\Sigma)\}
}^{L^2(T\Sigma)}.
}
\]

Let

\[
\Pi_G
:
L^2(T\Sigma)
\to
\mathcal G_\Sigma
\]

be the orthogonal projection.

Decompose

\[
\boxed{
J_\Sigma
=J_G+J_C,
}
\]

where

\[
J_G:=\Pi_GJ_\Sigma,
\qquad
J_C:=(I-\Pi_G)J_\Sigma.
\]

Then

\[
\boxed{
\|J_\Sigma\|_{L^2(\Sigma)}^2
=
\|J_G\|_2^2+
\|J_C\|_2^2.
}
\]

No coordinate choice is involved.

## 4. Scalar material-label moments see exactly the gradient component

For every \(\psi\in H_0^1(\Sigma)\),

\[
\nabla_\Sigma\psi
\in\mathcal G_\Sigma.
\]

Therefore orthogonality gives

\[
\int_\Sigma
\nabla_\Sigma\psi\cdot J_C\,dA
=0.
\]

The M5-521 moment identity becomes

\[
\boxed{
\frac d{d\theta}M_\psi
=
\int_\Sigma
\nabla_\Sigma\psi\cdot J_G\,dA.
}
\]

Thus

\[
\boxed{
J_G
=
\text{scalar-label-redistributive current},
}
\]

while

\[
\boxed{
J_C
=
\text{scalar-label-invisible circulation current}.
}
\]

The second name is operational: it is invisible to all scalar test-label moments in the chosen zero-boundary test class.

## 5. Distributional divergence interpretation

By the weak definition of surface divergence,

\[
\int_\Sigma
\nabla_\Sigma\psi\cdot J_\Sigma\,dA
=
-\langle\operatorname{div}_\Sigma J_\Sigma,\psi\rangle
\]

for \(\psi\in H_0^1(\Sigma)\).

Hence

\[
\boxed{
J_C\perp\mathcal G_\Sigma
\Longleftrightarrow
\operatorname{div}_\Sigma J_C=0
}
\]

in the interior distributional sense.

Therefore the split may also be read as

\[
\boxed{
\text{surface current}
=
\text{divergent/redistributive part}
+
\text{surface-divergence-free circulation part}.
}
\]

Boundary topology may add harmonic circulation modes; they are contained in \(J_C\) and are not silently discarded.

## 6. Quantitative current split

Suppose M18-074 gives on a controlled material event

\[
\int_\Sigma|J_\Sigma|^2dA
\ge j_*>0.
\]

Then orthogonality yields the exhaustive alternative

\[
\boxed{
\|J_G\|_2^2
\ge\frac{j_*}{2}
\quad\lor\quad
\|J_C\|_2^2
\ge\frac{j_*}{2}.
}
\]

Call the branches

\[
\boxed{G_{label\ redistribution}}
\]

and

\[
\boxed{G_{surface\ circulation}}
\]

respectively.

Thus nonzero surface-current action does not automatically imply marker migration; it implies redistribution **or** circulation.

## 7. Redistributive branch produces a material-label moment derivative

By definition of orthogonal projection,

\[
\|J_G\|_2
=
\sup_{
 g\in\mathcal G_\Sigma,
 \|g\|_2\le1
}
\left|
\int_\Sigma g\cdot J_\Sigma\,dA
\right|.
\]

Because gradients of \(H_0^1\) functions are dense in \(\mathcal G_\Sigma\), for every fixed \(0<\varepsilon<1\) there exists \(\psi\in H_0^1(\Sigma)\) with

\[
\|\nabla_\Sigma\psi\|_2=1
\]

and

\[
\left|
\int_\Sigma
\nabla_\Sigma\psi\cdot J_\Sigma\,dA
\right|
\ge
(1-\varepsilon)\|J_G\|_2.
\]

Hence on the redistributive branch,

\[
\boxed{
|M_\psi'|
\ge
(1-\varepsilon)\sqrt{j_*/2}.
}
\]

At one smooth event time the sign of \(M_\psi'\) is fixed after choosing the sign of \(\psi\).

Uniform time continuity then gives a short interval on which either

\[
\boxed{
|\Delta M_\psi|
\ge m_*>0
}
\]

or the material patch/test geometry loses control, which is a surface/label turnover event.

Therefore

\[
\boxed{
G_{label\ redistribution}
\Longrightarrow
\text{fixed material-label moment change}
\lor
G_{surface/label\ turnover}.
}
\]

## 8. Why the moment change is still reversible

The material-label moment \(M_\psi\) is bounded on a controlled finite-flux patch.

A recurrent system may therefore execute

\[
M_\psi:
\text{low}\to\text{high}\to\text{low}
\]

indefinitely.

Thus

\[
\boxed{
\text{fixed local material-label redistribution}
\not\Rightarrow
\text{one-sign global drift}.
}
\]

M5-521 prices each migration but does not forbid reverse migration.

This is the same path-functional firewall encountered in M16-016 and M18-066.

## 9. Circulation branch

On

\[
G_{surface\ circulation},
\]

we have a fixed nonzero current satisfying

\[
\operatorname{div}_\Sigma J_C=0
\]

in the interior weak sense.

On a simply connected smooth disk, after the standard two-dimensional Hodge representation and with suitable boundary conditions, one may write schematically

\[
J_C
=\star_\Sigma\nabla_\Sigma\chi
\]

for a stream function \(\chi\), up to the boundary/harmonic sector.

On multiply connected patches an additional harmonic circulation may remain.

The present module does not differentiate this representation and does not introduce a higher-derivative payer by fiat.

The valid conclusion is only

\[
\boxed{
\text{nonzero label-invisible surface circulation}
}
\]

or a boundary/topology contribution.

## 10. Relation to flux-density evolution

M5-520 gives

\[
D_Bf+(1-\sigma_n)f
+
\operatorname{div}_\Sigma J_\Sigma
=0,
\]

where

\[
f=W\cdot n.
\]

On the circulation component alone,

\[
\operatorname{div}_\Sigma J_C=0.
\]

Therefore \(J_C\) does not directly alter the local signed flux density through the divergence term.

It is a tangential circulation of the viscous surface current rather than a scalar flux-density redistribution.

This explains exactly why surface-current action and marker migration are not equivalent.

## 11. Finite-lineage interpretation

The Frobenius patch from M18-074 has

\[
n=\xi,
\qquad
\rho\ge a_0>0
\]

after shrinking.

Hence its directed flux satisfies

\[
\Phi_*
=
\int_{\Sigma_*}\rho\,dA
>0.
\]

It is therefore a coherent positive-flux packet eligible for the M5-397/M5-497 material-lineage genealogy.

If the patch cannot be absorbed into an existing persistent lineage, then its persistence produces a new/replacement flux label or an already typed export/flux-loss event.

Consequently both surface branches live inside the finite material-lineage architecture rather than outside it.

However, the Hodge split is internal to one surface and does not by itself decide whether the label is old or new.

## 12. Updated signed-route tree

Combining M18-073--075 gives

\[
\boxed{
\text{mandatory CE-H transverse current}
\Longrightarrow
\begin{cases}
G_{self\text{-}helicity/twist},\\
G_{surface\ boundary/export},\\
G_{label\ redistribution},\\
G_{surface\ circulation}.
\end{cases}
}
\]

The redistributive branch is priced by M5-521.

The circulation branch is genuinely different and must not be relabeled as migration.

## 13. Audit verdict

### Certified

1. On a controlled material surface, the current has the exact orthogonal split
   \[
   J_\Sigma=J_G+J_C.
   \]
2. Scalar material-label moments see exactly \(J_G\).
3. \(J_C\) is interior surface-divergence-free and may circulate without changing any scalar label moment.
4. A fixed surface-current action forces either a fixed redistributive current or a fixed circulation current.
5. The redistributive branch gives a fixed short-time material-label moment change unless surface/label geometry turns over.
6. A material-label moment change remains reversible and is not a monotone contradiction.
7. The Frobenius patch is a positive-flux packet and belongs to the existing finite-lineage genealogy.

### Not certified

- exclusion of surface-divergence-free recurrent circulation;
- a one-sign drift of material-label moments;
- return of the same material patch after an Eulerian recurrent cycle;
- ancestry closure of the surface-current/palinstrophy payment;
- remote/critical closure;
- global regularity.

## 14. Next target

The new sharp survivor is

\[
\boxed{G_{surface\ circulation}.}
\]

M18-076 should test whether this circulation can remain nonzero on a vortex-transverse CE-H material disk while

\[
\Delta W=\kappa W,
\qquad
W\cdot\nabla\kappa=0,
\qquad
n=\xi,
\]

without producing either

- boundary current/export;
- nontrivial surface vorticity of \(J_C\), which may connect to coefficient/director gradients;
- or harmonic circulation tied to nontrivial surface topology.

The calculation should first use the existing CE-H identities and surface Stokes formulas before differentiating further.
