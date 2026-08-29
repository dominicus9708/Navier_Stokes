# DSD M5-271 — Residual Stress-Force Charge and Angular-Mean Split

Date: 2026-08-30

Parent: `DSD_M5_270_RESIDUAL_TERMINAL_DERIVATIVE_CRITICAL_SUMMABILITY_FIREWALL_2026-08-30.md`

Status: **EXACT MOMENT AUDIT / THE CRITICAL RESIDUAL OF A CANONICAL TAIL IS THE DIVERGENCE OF THE STATIONARY MOMENTUM STRESS / AFTER CRITICAL NORMALIZATION, THE SPHERICAL MEAN OF THE DEGREE-`-3` RESIDUAL IS EXACTLY THE LOG-RADIUS DERIVATIVE OF THE NET FORCE-CHARGE VECTOR / ON A COMPACT RECURRENT TAIL HULL ITS INVARIANT MEAN MUST VANISH / A UNIFORM RESIDUAL GAP THEREFORE SPLITS INTO EITHER NONTRIVIAL RECURRENT FORCE-CHARGE OSCILLATION OR A SPHERICALLY MEAN-FREE RESIDUAL WITH A FIXED ANGULAR-DERIVATIVE FLOOR / NEITHER IS YET A CONTRADICTION, BUT THE RESIDUAL-ACTIVE ENDPOINT IS ROUTED FROM A GENERIC `H^-1` DEFECT INTO TWO EXPLICIT NAVIER--STOKES STRUCTURAL MOMENTS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Unprojected residual and momentum stress

Let the canonical critical tail be

\[
T(x)=r^{-1}\Phi(y,\theta),
\qquad
y=\log r,
\]

with canonical pressure

\[
P(x)=r^{-2}\Pi(y,\theta).
\]

Choose the pressure so that the projected residual is represented by the ordinary stationary residual

\[
\boxed{
F_T
=\nu\Delta T
-(T\cdot\nabla)T
-\nabla P.
}
\]

Since `div T=0`, define the stationary momentum stress

\[
\boxed{
\mathbb S_T
:=2\nu D(T)-T\otimes T-P I.
}
\]

Then

\[
\boxed{
\nabla\cdot\mathbb S_T=F_T.
}
\]

For a stationary tail `F_T=0`, the corresponding spherical stress flux was the fixed point-force charge studied in M5-227--236.

Here `F_T` is nonzero by M5-268/M5-269.

---

## 2. Critical log-cylinder normalization

The critical degrees are

\[
\mathbb S_T(x)=r^{-2}\mathscr S(y,\theta),
\]

and

\[
F_T(x)=r^{-3}\mathcal R(y,\theta).
\]

Define the net force-charge vector through the sphere `S_r`:

\[
\boxed{
\mathcal B(y)
:=\int_{|x|=r}\mathbb S_T n\,dS.
}
\]

Because `mathbb S_T~r^-2` and `dS~r^2`, `mathcal B` is dimensionless and depends only on the log-radius phase `y`.

---

## 3. Exact force-charge evolution

Apply the divergence theorem to the shell

\[
A(r_1,r_2)=\{r_1<|x|<r_2\}.
\]

Then

\[
\mathcal B(\log r_2)-\mathcal B(\log r_1)
=
\int_{A(r_1,r_2)}F_T(x)\,dx.
\]

Using

\[
F_T=r^{-3}\mathcal R(y,\theta),
\qquad
dx=r^2drd\theta,
\qquad
dr/r=dy,
\]

we obtain

\[
\boxed{
\mathcal B(y_2)-\mathcal B(y_1)
=
\int_{y_1}^{y_2}
\int_{S^2}\mathcal R(y,\theta)d\theta\,dy.
}
\]

Therefore, in the classical/distributional log-cylinder sense,

\[
\boxed{
\mathcal B_y(y)
=\overline{\mathcal R}(y),
\qquad
\overline{\mathcal R}(y)
:=\int_{S^2}\mathcal R(y,\theta)d\theta.
}
\]

This is the residual-active replacement of the constant-force law `B_y=0` on the stationary branch.

---

## 4. Recurrent invariant mean of the force source is zero

On the retained compact smooth tail hull, the critical stress coefficient is bounded on each fixed log cell. Hence

\[
\sup_y|\mathcal B(y)|<\infty
\]

along every recurrent phase orbit.

For any long interval `[0,L]`,

\[
\frac1L\int_0^L\overline{\mathcal R}(y)dy
=
\frac{\mathcal B(L)-\mathcal B(0)}L.
\]

Thus

\[
\boxed{
\lim_{L\to\infty}
\frac1L\int_0^L\overline{\mathcal R}(y)dy
=0.
}
\]

Equivalently, for every invariant measure on the minimal translation hull,

\[
\boxed{
\langle\overline{\mathcal R}\rangle=0.
}
\]

Therefore a residual-active minimal tail cannot sustain a nonzero **mean** net-force source in log radius. Its force source must oscillate/cancel over recurrent phases.

---

## 5. Orthogonal spherical decomposition of the residual

Decompose componentwise

\[
\mathcal R(y,\theta)
=
\mathcal R_0(y)
+\mathcal R_\perp(y,\theta),
\]

where

\[
\mathcal R_0(y)
:=\frac1{4\pi}\overline{\mathcal R}(y),
\qquad
\int_{S^2}\mathcal R_\perp d\theta=0.
\]

Then

\[
\boxed{
\|\mathcal R(y,\cdot)\|_{L^2(S^2)}^2
=4\pi|\mathcal R_0(y)|^2
+\|\mathcal R_\perp(y,\cdot)\|_2^2.
}
\]

Thus any fixed `L2` residual lower bound on a selected log cell must be paid either by the force/source mode or by the angular mean-free mode.

---

## 6. How the global residual gap supplies a fixed local `L2` event

M5-238 gives a compact-hull residual gap in a countable local residual metric:

\[
\mathbf F(T)\ge\varepsilon_{glob}>0.
\]

By compactness and the finite-cover argument already used in M5-220/M5-238, one may select finitely many fixed enlarged cells whose local `H^-1` residual seminorms detect this gap.

On the retained smooth local class,

\[
\|F\|_{H^{-1}(K)}
\le C_K\|F\|_{L^2(K)}.
\]

Therefore, after a finite phase/cell partition, there is a fixed cell and a positive recurrent subset on which

\[
\boxed{
\|\mathcal R\|_{L^2(C_*)}
\ge r_*>0.
}
\]

No claim is made that the same cell works at every unshifted log phase; minimal translation is used only to select a finite recurrent family.

---

## 7. Finite residual-moment dichotomy

Using Section 5 on the selected cell, choose a harmless fixed split, e.g. half of the squared residual mass.

Then on a positive recurrent subset at least one of the following holds:

### F — force-charge source branch

\[
\boxed{
\int_I|\mathcal R_0(y)|^2dy
\ge c_F r_*^2.
}
\]

Since

\[
\mathcal B_y=4\pi\mathcal R_0,
\]

this is exactly a fixed `L2` log-action of the net force charge:

\[
\boxed{
\int_I|\mathcal B_y|^2dy
\ge c'_F r_*^2.
}
\]

### A — angular residual branch

\[
\boxed{
\int_I\|\mathcal R_\perp(y)\|_2^2dy
\ge c_A r_*^2.
}
\]

These are ordinary finite-dimensional/orthogonal alternatives; no sign is imposed.

---

## 8. Angular branch forces a higher spherical derivative

For every mean-free scalar component on `S2`, the first nonzero spherical Laplacian eigenvalue is `2`. Hence Poincare gives

\[
\int_{S^2}|\nabla_{S^2}f|^2d\theta
\ge2\int_{S^2}|f|^2d\theta.
\]

Applying this componentwise to `mathcal R_perp`,

\[
\boxed{
\|\nabla_{S^2}\mathcal R_\perp\|_2^2
\ge2\|\mathcal R_\perp\|_2^2.
}
\]

Therefore Branch A gives

\[
\boxed{
\int_I
\|\nabla_{S^2}\mathcal R_\perp\|_2^2dy
\ge2c_A r_*^2.
}
\]

Since `mathcal R` is the critical stationary NS residual, this is a genuine higher angular-derivative/nonlinear-pressure certificate, not a generic norm restatement.

However it is still critical in scaling and no global finite third-derivative budget is presently available.

---

## 9. Force branch is a recurrent charge oscillation, not a contradiction

Branch F says the bounded observable `mathcal B(y)` has nontrivial derivative action on a positive-density family of cells.

This is compatible with compact recurrent dynamics: a bounded periodic or quasiperiodic function may satisfy

\[
\langle\mathcal B_y\rangle=0
\]

while

\[
\langle|\mathcal B_y|^2\rangle>0.
\]

Therefore

\[
\boxed{
\mathcal B_y\ne0
\not\Rightarrow
\text{force-charge contradiction}.
}
\]

A closure would need either a monotonicity/sign law for `mathcal B`, a finite total-variation budget, or a coupling of `mathcal B_y` to a previously bounded physical turnover action.

---

## 10. DSD verdict

The residual-active endpoint has been reduced from a generic critical defect to the exact moment fork

\[
\boxed{
R_{gap}
\Longrightarrow
F_{charge}
\lor
A_{res},
}
\]

where

\[
F_{charge}:
\text{positive recurrent }L^2\text{ action of the net stress-force charge},
\]

and

\[
A_{res}:
\text{positive recurrent angular derivative action of the mean-free residual}.
\]

Both are Navier--Stokes-specific formed channels.

Neither is yet excluded, and neither is silently identified with the older `H/T` branches without a threshold comparison.

The next high-leverage audit is to pair `F_T` with the dilation/homogeneity tangent

\[
\mathcal H_T=T+x\cdot\nabla T,
\]

because the viscous part has a strict log-average sign. The nonlinear and pressure contributions must be computed exactly before any Lyapunov conclusion is made.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
