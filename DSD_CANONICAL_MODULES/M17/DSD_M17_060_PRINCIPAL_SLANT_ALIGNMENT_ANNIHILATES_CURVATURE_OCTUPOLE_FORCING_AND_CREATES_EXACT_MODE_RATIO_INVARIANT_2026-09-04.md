# DSD M17-060 — Principal-slant alignment annihilates curvature-octupole forcing and creates an exact mode-ratio invariant

Date: 2026-09-04
Canonical ID: **M17-060**

Status: **INTERNAL PRINCIPAL-SLANT SOURCE ALIGNMENT CLOSURE / M17-059 REDUCES THE PRINCIPAL-SLANT LOCAL CURVATURE OCTUPOLE TO TWO MODES `X_-` AND `X_+` FORCED BY `phi_112`, `phi_123`, AND `phi_233`. M17-025'S TRACE-FREE SLANTED ALIGNMENT, IN THE PRINCIPAL FRAME, FORCES THE OFF-DIAGONAL SLANT-DIRECTION THIRD-PHI JET `phi_112=0`. THE EXACT RECONSTRUCTION IDENTITY `partial_3 nabla_h^2 phi=(G_q-1)Q` FORCES `phi_123=0` BECAUSE Q IS DIAGONAL. FINALLY `q=U_3-partial_3phi`, `q_23=0`, AND `U_3=G(q,x_3)` GIVE `U_{3,23}=0` AND HENCE `phi_233=0`. THEREFORE BOTH M17-059 SOURCE TERMS VANISH EXACTLY: `S_-=S_+=0`. THE TWO MODES OBEY PURE MULTIPLIER LAWS `D_BX_-=mu_-X_-`, `D_BX_+=mu_+X_+`, WITH `mu_+-mu_-=6lambda`. BECAUSE `D_B log P=3lambda`, THE RATIO `I_oct=X_+/(P^2X_-)` IS AN EXACT MATERIAL INVARIANT WHEN BOTH MODES ARE NONZERO; THE ZERO-MODE SUBMANIFOLDS ARE ALSO MATERIAL INVARIANT. A UNIFORMLY RECURRENT NONZERO MODE FORCES `mean G_3=-1/2` USING `mean kappa=3/2` AND `mean lambda=0`. THIS CONDITION IS CONSISTENT WITH THE LABEL-FLOW DIVERGENCE: IT GIVES `mean K_3=0` AND `mean H_q=3/2`, SO IT IS A RIGIDITY LAW RATHER THAN A CONTRADICTION. IF BOTH MODES VANISH, THE ENTIRE LOCAL PRINCIPAL-SLANT PAYER OCTUPOLE VANISHES AND ANY L=3 PRESSURE LOCK MUST BE SUPPLIED BY MESOSCOPIC/GLOBAL SOURCE MOMENTS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-059

On the principal-slant nonconformal branch, choose

\[
Q=\operatorname{diag}(q_1,q_2),
\qquad
p=(P,0),
\qquad
P\ne0.
\]

M17-059 defines

\[
\boxed{
X_-=(8q_1+7q_2)H_{112}
}
\]

and

\[
\boxed{
X_+=2Pq_1H_{123}+2q_2H_{233}.
}
\]

The visible local curvature-octupole scalar is

\[
\boxed{\Xi=X_-+X_+.}
\]

The two mode equations are

\[
D_BX_-=\mu_-X_-+\mathcal S_-,
\]

\[
D_BX_+=\mu_+X_++\mathcal S_+,
\]

with

\[
\boxed{
\mu_-=2\kappa-G_3-\frac72-3\lambda,
\qquad
\mu_+=2\kappa-G_3-\frac72+3\lambda.
}
\]

The source terms are built from

\[
\phi_{112},\qquad\phi_{123},\qquad\phi_{233}.
\]

---

## 2. M17-025 kills phi112

M17-025 gives the exact slanted-core trace-free alignment

\[
\boxed{
C_p
:=TF[(p\cdot\nabla_h)H_\phi]
=-(G_q-1)Q_0,
}
\]

where

\[
H_\phi=\nabla_h^2\phi.
\]

In the principal frame,

\[
p=(P,0)
\]

and

\[
Q_0
\]

is diagonal.

The off-diagonal component of the left side is simply

\[
P\phi_{112}.
\]

The right side has zero off-diagonal component.
Since

\[
P\ne0,
\]

we obtain

\[
\boxed{\phi_{112}=0.}
\]

The diagonal component also gives the scalar compensation relation

\[
\boxed{
P(\phi_{111}-\phi_{122})
=-(G_q-1)(q_1-q_2),
}
\]

which remains available but is not needed for the source cancellation below.

---

## 3. The vertical reconstruction law kills phi123

M17-025 derives at every regular nodal core

\[
\boxed{
\partial_3H_\phi
=(G_q-1)Q.
}
\]

Take its off-diagonal `(1,2)` component.
Because `Q` is diagonal in the principal frame,

\[
(G_q-1)Q_{12}=0.
\]

Therefore

\[
\boxed{
\phi_{123}=0.
}
\]

This cancellation is independent of whether `G_q-1` vanishes.

---

## 4. The q reconstruction law kills phi233

The great-circle reconstruction is

\[
\boxed{
q=U_3-\partial_3\phi.
}
\]

Take derivatives `partial_2 partial_3`:

\[
q_{23}=U_{3,23}-\phi_{233}.
\]

Principal slant gives

\[
q_{h3}=-Qp=(-q_1P,0),
\]

so

\[
\boxed{q_{23}=0.
}
\]

Also

\[
U_3=G(q,x_3,\theta).
\]

In the nodal gauge used in M17-059,

\[
q_2=q_3=0.
\]

Therefore

\[
U_{3,23}
=G_q q_{23}
+G_{qq}q_2q_3
+G_{q3}q_2
=0.
\]

Hence

\[
\boxed{\phi_{233}=0.
}
\]

---

## 5. Both M17-059 forcing terms vanish

M17-059 gives

\[
\mathcal F_{112}
=-(2q_1+q_2)\phi_{112},
\]

\[
\mathcal F_{123}
=q_1P\phi_{112}-(q_1+q_2)\phi_{123},
\]

\[
\mathcal F_{233}
=2q_1P\phi_{123}-q_2\phi_{233}.
\]

Sections 2--4 imply

\[
\boxed{
\mathcal F_{112}
=\mathcal F_{123}
=\mathcal F_{233}
=0.
}
\]

Therefore

\[
\boxed{\mathcal S_-=\mathcal S_+=0.}
\]

The principal-slant curvature octupole is not merely low dimensional; its two internal modes are **unforced exact material multiplier modes**.

---

## 6. Exact multiplier laws

The mode equations reduce to

\[
\boxed{
D_BX_-
=\left(
2\kappa-G_3-\frac72-3\lambda
\right)X_-,
}
\]

\[
\boxed{
D_BX_+
=\left(
2\kappa-G_3-\frac72+3\lambda
\right)X_+.
}
\]

Thus each zero set

\[
\boxed{X_-=0}
\]

and

\[
\boxed{X_+=0}
\]

is materially invariant as long as the regular principal-slant chart persists.

No additive source can regenerate a mode once it vanishes.

---

## 7. Exact ratio invariant

When both modes are nonzero,

\[
D_B\log\left|\frac{X_+}{X_-}\right|
=6\lambda.
\]

M17-024 gives

\[
D_B\log P=3\lambda.
\]

Therefore

\[
D_B\log P^2=6\lambda.
\]

Subtracting,

\[
\boxed{
D_B\log\left|
\frac{X_+}{P^2X_-}
\right|
=0.
}
\]

Hence

\[
\boxed{
\mathcal I_{oct}
:=\frac{X_+}{P^2X_-}
}
\]

is an exact signed material invariant wherever both modes are nonzero.

This is a new higher-jet analogue of the frozen normalized nodal shape and frozen slant azimuth.

---

## 8. Mode product law

The product has

\[
\begin{aligned}
D_B\log|X_+X_-|
&=\mu_++\mu_-\\
&=4\kappa-2G_3-7.
\end{aligned}
\]

Thus

\[
\boxed{
D_B\log|X_+X_-|
=4\kappa-2G_3-7,
}
\]

with **all lambda dependence cancelling exactly**.

This gives a scalar higher-jet volume-like ledger independent of the instantaneous repeated-plane strain splitting.

---

## 9. Recurrent nonzero mode forces mean G3 = -1/2

Assume at least one mode remains uniformly bounded above and below away from zero along a recurrent marked principal-slant filament.

For `X_-`, zero logarithmic drift gives

\[
0
=
2\langle\kappa\rangle
-\langle G_3\rangle
-\frac72
-3\langle\lambda\rangle.
\]

For `X_+`, the last sign is reversed.

M17-010 gives

\[
\boxed{\langle\kappa\rangle=\frac32}
\]

on the uniformly recurrent regular nodal branch, and M17-024 gives

\[
\boxed{\langle\lambda\rangle=0}
\]

for uniformly recurrent nonzero slant.

Therefore either recurrent nonzero mode yields

\[
\boxed{
\langle G_3\rangle=-\frac12.
}
\]

If both modes are recurrent and nonzero, the two conditions agree exactly.

---

## 10. Label-flow interpretation of the new mean law

M17-013 defines

\[
K=G+\frac12x_3
\]

and

\[
\mathscr H_q
=\kappa-G_3-\frac12.
\]

Hence

\[
K_3=G_3+\frac12.
\]

The new mean law gives

\[
\boxed{\langle K_3\rangle=0.}
\]

Also

\[
\begin{aligned}
\langle\mathscr H_q\rangle
&=\frac32-\left(-\frac12\right)-\frac12\\
&=\frac32.
\end{aligned}
\]

Thus

\[
\boxed{
\langle\mathscr H_q\rangle=\frac32,
\qquad
\langle K_3\rangle=0,
}
\]

which is exactly consistent with

\[
\mathscr H_q+K_3=\kappa,
\qquad
\langle\kappa\rangle=\frac32.
\]

Therefore this is a rigidity law, not a contradiction.

---

## 11. Double-zero local octupole subbranch

If

\[
\boxed{X_-=X_+=0,}
\]

then

\[
\boxed{\Xi=0.}
\]

M17-058 already gives on principal slant

\[
\mathfrak o_\kappa=0.
\]

Therefore the entire local payer-octupole mismatch vanishes:

\[
\boxed{\mathfrak o_{loc}=0.}
\]

This is a genuine invariant subbranch because both zero modes are preserved by the homogeneous laws.

Any persistent DSAIG l=3 screening on this subbranch must therefore come from

1. the explicit local pressure-source-gradient tensor of M17-051 that is not the payer-octupole scalar itself;
2. mesoscopic/global l=3 pressure-source moments of M17-052--054;
3. viscous higher-jet forcing;
4. turnover or branch/interface events.

The local payer octupole cannot be regenerated while the principal regular branch remains intact.

---

## 12. Exceptional Hessian-shape resonance

The definition

\[
X_-=(8q_1+7q_2)H_{112}
\]

has an algebraic resonance when

\[
\boxed{8q_1+7q_2=0.}
\]

Because the ratio `q_1/q_2` is materially frozen, this is itself an invariant nodal-shape class.

On that class `X_-=0` regardless of `H_112`.
This does not invalidate the multiplier law; it simply places the solution directly on the invariant `X_-=0` submanifold.

No contradiction is claimed from this resonance.

---

## 13. DSD analysis

The previously visible scalar `Xi` hides two distinct material channels.
PSSAG shows that the apparent source terms were not independent data at all: they are removed by compatibility relations already required elsewhere in the CE-H structure.

The resulting hierarchy is

\[
\boxed{
(Qhat,phat)
\to
(X_-,X_+)
\to
\mathcal I_{oct}.
}
\]

All three levels carry material shape information that scalar kappa hysteresis alone does not see.

---

## 14. DSD audit

### Audit A — treating phi112 as independent
Rejected by M17-025 principal-frame alignment.

### Audit B — treating phi123 as independent
Rejected by `partial_3 H_phi=(G_q-1)Q` and diagonal Q.

### Audit C — treating phi233 as independent
Rejected by the reconstruction law plus `q_23=U_{3,23}=0` in the principal nodal gauge.

### Audit D — declaring the new mean G3 condition contradictory
Rejected. It exactly respects the label-flow divergence law.

### Audit E — dividing by a vanishing mode
Avoided. `I_oct` is defined only on the nonzero/nonzero subbranch; zero-mode classes are handled separately.

### Audit F — claiming local octupole zero means total l=3 pressure zero
Rejected. Global/mesoscopic source moments remain distinct descriptors.

### Audit G — proof status
Principal slant is substantially more rigid but survives the present audit.

---

## 15. Updated principal-slant frontier

\[
\boxed{
R_{principal}^{H_3}
\Longrightarrow
R_{++}^{\mathcal I_{oct}}
\ \lor\
R_{+0}
\ \lor\
R_{0+}
\ \lor\
R_{00}^{local-oct=0}
\ \lor\
T_{nodal/rank}.
}
\]

Any uniformly recurrent subbranch with at least one nonzero curvature-octupole mode additionally satisfies

\[
\boxed{\langle G_3\rangle=-\frac12.}
\]

---

## 16. Next target — global l=3 lock on an unforced local mode

The local principal-slant octupole no longer has arbitrary additive forcing.
The next question is therefore sharper:

\[
\boxed{
\text{Can the global pressure }l=3\text{ moment remain DSAIG-locked to an unforced, materially rigid local octupole mode?}
}
\]

The relevant equations are M17-053--054 for the pressure moment and the exact multiplier laws above.
The `R_00` subbranch is especially sharp because it requires the global/mesoscopic l=3 pressure architecture to maintain the lock with **zero local payer-octupole contribution**.

This is the **Principal Global-Octupole Lock Gate (PGOLG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
