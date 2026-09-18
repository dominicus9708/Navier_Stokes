# M19-413 — M19-412 removes the stationary-all minimal hull and promotes the uniform residual gap to the mandatory terminal frontier

Date: 2026-09-19  
Canonical ID: **M19-413**  
Status: **CANONICAL REBASE / STATIONARY-ALL MINIMAL HULL EXCLUDED ON THE REALIZED OFF-ORIGIN-SMOOTH WEDGE / UNIFORM GLOBAL RESIDUAL GAP IS NOW MANDATORY ON EVERY NONTRIVIAL RETAINED HARD MINIMAL HULL / M5-270--272 FIREWALLS REACTIVATED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs that must now be read together

M5-238 gives a compact-minimal terminal-tail dichotomy.

Let \(\mathcal T\) be the compact minimal canonical terminal-tail hull and
\[
\mathcal S_{stat}
=
\{T\in\mathcal T:\mathcal F(T)=0\}
\]
the stationary set.

Because \(\mathcal S_{stat}\) is closed and dilation invariant, minimality gives
\[
\boxed{
\mathcal T\subset\mathcal S_{stat}
\quad\lor\quad
\mathcal T\cap\mathcal S_{stat}=\varnothing.
}
\]

On the second branch M5-238 defines a continuous global residual metric \(\mathbf F\) and proves
\[
\boxed{
\mathbf F(T)\ge\varepsilon_{glob}>0
\qquad\forall T\in\mathcal T.
}
\]

M19-412 now supplies the missing realized-wedge correction. On the retained isolated-center off-origin-smooth wedge,
\[
C=0
\]
means that the terminal trace is stationary on \(\mathbb R^3\setminus\{0\}\), and the M5-268/269 RG-flatness + Oseen-Carleman mechanism forces that stationary trace to extend smoothly and then vanish.

Hence on the realized hard branch
\[
\boxed{
C=0
\Longrightarrow
T\equiv0.
}
\]

M5-571 independently gives nontrivial hard-component terminal densities
\[
c_3>0,
\qquad
c_\omega>0,
\]
so the retained hard minimal hull is not the zero hull.

## 2. The stationary-all alternative is impossible

Assume for contradiction that
\[
\mathcal T\subset\mathcal S_{stat}.
\]

Every state in the realized hard minimal hull would then have
\[
C=0.
\]

By M19-412 every such realized stationary terminal trace is trivial:
\[
T\equiv0.
\]

Therefore the whole minimal hull would reduce to the zero state, contradicting the retained hard nontriviality
\[
c_3>0,
\qquad
c_\omega>0.
\]

Thus
\[
\boxed{
\mathcal T\cap\mathcal S_{stat}=\varnothing.
}
\]

The all-or-none dichotomy of M5-238 therefore collapses to the residual-active side only.

## 3. Mandatory uniform global residual gap

Compactness and continuity from M5-238 now apply without a remaining stationary alternative:

\[
\boxed{
\varepsilon_{glob}
:=
\min_{T\in\mathcal T}\mathbf F(T)
>0.
}
\]

Hence
\[
\boxed{
\mathbf F(T)
\ge
\varepsilon_{glob}
\qquad
\forall T\in\mathcal T.
}
\]

This is strictly stronger than merely saying that one ergodic trajectory has
\[
\langle |C|^2\rangle>0.
\]

The retained minimal hull has no globally residual-quiet state and no stationary cluster point inside the realized hard class.

Up to the sign convention between the projected stationary residual \(\mathcal F(T)\) and the first terminal coefficient \(C\), they are the same first terminal-time obstruction. Norm statements are unaffected by that sign convention.

## 4. Finite normalized windows carry recurrent residual events

M5-238 reduces the global metric to finitely many punctured normalized windows.

Therefore there exist

- finitely many normalized annular cells \(K_1,\ldots,K_M\);
- a fixed threshold \(\varepsilon_{fin}>0\);

such that every hull state has at least one cell satisfying
\[
\|\mathcal F(T)\|_{H^{-1}(K_m)}
\ge
\varepsilon_{fin}.
\]

Under an ergodic invariant measure, a deterministic finite-cell selection gives at least one cell index \(m_*\) occurring with positive invariant density.

Thus the residual-active hard branch contains a positive-density recurrent family of fixed normalized residual events.

On the retained smooth compact class, local
\[
H^{-1}\to L^2
\]
comparison yields a fixed positive local \(L^2\) residual event after the finite partition.

## 5. Exact Navier--Stokes structural fork is now mandatory

M5-271 decomposes the degree-\(-3\) first residual into its spherical mean and mean-free parts.

Using the first-jet notation,
\[
C(q,\omega)
=
\overline C(q)+C^\perp(q,\omega),
\qquad
\int_{S^2}C^\perp d\omega=0.
\]

The spherical-mean part is exactly the derivative of the critical stress-force charge:
\[
\boxed{
4\pi\overline C
=
-\mathcal F_A'(q).
}
\]

The mean-free part satisfies the spherical Poincare inequality
\[
\boxed{
\|\nabla_{S^2}C^\perp\|_2^2
\ge
2\|C^\perp\|_2^2.
}
\]

Therefore the mandatory residual gap produces, on a positive-density recurrent family of normalized cells, at least one of

\[
\boxed{
F_{charge}:
\text{ nontrivial }L^2\text{ log-action of }\mathcal F_A'
}
\]

or

\[
\boxed{
A_{res}:
\text{ nontrivial angular-derivative action of }C^\perp.
}
\]

This fork is no longer an optional subbranch of a residual-active scenario. After M19-412 it is part of the mandatory retained terminal frontier.

## 6. Two old shortcuts remain invalid

M5-270 remains fully active.

The critical residual
\[
F_T\sim r^{-3}
\]
with natural inner scale
\[
r\sim\sqrt{T^*-t}
\]
is compatible with the standard weak time-derivative and kinetic-energy budgets.

In particular the model sizes
\[
\|u_t\|_{H^{-1}}
\lesssim
(T^*-t)^{-1/4},
\]
and
\[
\|\nabla u\|_2^2
\lesssim
(T^*-t)^{-1/2}
\]
remain time-integrable.

Therefore
\[
\boxed{
\text{uniform residual gap}
\not\Rightarrow
\text{standard energy-budget contradiction}.
}
\]

M5-272 also remains active.

Pairing the residual with the dilation tangent produces a strictly negative viscous contribution, but nonlinear and pressure correlations have no universal sign. Hence
\[
\boxed{
\text{residual gap}
\not\Rightarrow
\text{dilation Lyapunov sign}.
}
\]

The M19-267--308 wedge-energy and hysteresis audits likewise show that finite-depth positive transport events can be compensated inside the full wedge and do not automatically yield a one-way recurrent drift.

## 7. Correct post-M19-412 frontier

The realized stationary terminal branch is closed.

The retained hard minimal terminal hull is therefore forced into
\[
\boxed{
R_{gap}
}
\]
with
\[
\boxed{
R_{gap}
\Longrightarrow
F_{charge}
\lor
A_{res}.
}
\]

The immediate high-value task is no longer to classify a stationary zero-force tail.

It is to determine whether either mandatory residual channel can be coupled to a genuinely noncritical resource:

1. **Force-charge route:** convert recurrent stress-flux oscillation into a finite-total-variation, signed, or export obstruction.
2. **Angular-residual route:** test whether the fixed angular derivative activity can be placed into the later M17 raw-\(H^2\)/higher-derivative ancestry with enough multiplicity or gain to defeat critical summability.
3. **Cross-channel rigidity:** couple the residual moment fork to the wedge energy/enstrophy production events so that compensation cannot occur on disjoint phases/depths.

The next calculation should first audit item 2, because the later M17 ancestry resources were not available when M5-271 originally classified the angular branch.

\[
\boxed{\text{M19-413 COMPLETE; THE UNIFORM RESIDUAL GAP IS NOW THE MANDATORY TERMINAL-HULL FRONTIER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
