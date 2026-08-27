# DSD M5-80 — Regular-Branch Defect Continuity under W1 Local Analytic Convergence

Date: 2026-08-27

Status: **PERSISTENT REGULAR-BRANCH CONTINUITY PROVED / M5-74--M5-76 VELOCITY-ONLY DEFECTS PASS TO W1 OMEGA LIMITS UNDER UNIFORM REGULAR-LEVEL AND CROSSING NONDEGENERACY / GLOBAL Lp PRECOMPACTNESS ALONE IS INSUFFICIENT / CRITICAL-LEVEL DEGENERATION REMAINS AN OPEN ESCAPE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-74--M5-76 introduced the velocity-derived endpoint diagnostics

\[
K_A,
\qquad
\delta_\beta,
\qquad
K_\alpha,
\qquad
\mathfrak I.
\]

A recurrent saturating sequence is useful only if these quantities survive passage to a W1 omega-limit state.

The actual W1 topology is:

- global precompactness in `Lp`, `3<p<=6`;
- local analytic compactness on every fixed bounded space-time cylinder.

The derivative-based level-set defects are therefore handled locally.

---

## 2. Convergent W1 sequence

Let

\[
U_n(Y,s)
\]

be a sequence of time-translated W1 states and suppose, after subsequence extraction, that on a fixed cylinder

\[
B_R\times[s_*-\delta,s_*+\delta]
\]

we have

\[
\boxed{
U_n\to U_*
\quad\text{in }C^4
}
\]

and the corresponding time derivatives converge to the orders required by the Navier--Stokes equation.

The `C4` assumption is deliberately stronger than the minimum needed. It is available from the already audited local analytic compactness and safely controls:

- `a=|U|`;
- `b=U dot grad log a`;
- `grad b`;
- `Delta b`;
- level-surface geometry;
- one amplitude derivative of the reconstructed coefficient `beta`.

---

## 3. Persistent amplitude branch assumptions

Fix a compact amplitude interval

\[
I=[\lambda_-,\lambda_+]
\subset(0,\infty).
\]

Assume the limit field has a smooth nested connected branch

\[
\Gamma^*_{\lambda,k}
\subset B_R,
\qquad
\lambda\in I,
\]

with

\[
\boxed{
|\nabla a_*|\ge\kappa>0
\quad\text{on all }\Gamma^*_{\lambda,k},
\ \lambda\in I.
}
\]

Then the implicit-function theorem gives, for all sufficiently large `n`, corresponding branches

\[
\Gamma^n_{\lambda,k}
\]

with the same local topology and

\[
\Gamma^n_{\lambda,k}	o\Gamma^*_{\lambda,k}
\]

in the finite `C^m` surface topology needed below, uniformly for `lambda in I`.

In particular,

\[
|\nabla a_n|\ge\frac\kappa2
\]

on these branches for large `n`.

---

## 4. Stability of coarea surface measures

The M5 functionals use

\[
\frac{dS}{|\nabla a|}.
\]

Under the preceding uniform regularity,

\[
\boxed{
\frac{dS_n}{|\nabla a_n|}
\to
\frac{dS_*}{|\nabla a_*|}
}
\]

smoothly after identifying the nearby surfaces by the normal graph supplied by the implicit-function theorem.

Therefore every level integral whose integrand converges uniformly also converges.

This includes the geometric denominators appearing in M5-75 and M5-76.

---

## 5. Continuity of the amplitude defect KA

M5-74 has

\[
F=\beta b
\]

at exact compatibility, with

\[
F
=
\nu\Delta a
-\nu\frac{|\nabla U|^2-|\nabla a|^2}{a}
-\partial_ta
-ab
-\frac{2\nu}{a}U\cdot\nabla b.
\]

On `I`, `a>=lambda_->0`, so no amplitude denominator degenerates.

The fields

\[
a_n,\ b_n,\ F_n
\]

converge uniformly on the persistent branch.

If the crossing denominator obeys the uniform nondegeneracy condition

\[
\boxed{
\langle b_n,b_n\rangle_{\Gamma^n_{\lambda,k}}
\ge\eta>0,
}
\]

then

\[
\beta_{A,n}
=
\frac{\langle F_n,b_n\rangle}
{\langle b_n,b_n\rangle}
\]

converges uniformly in `lambda` to `beta_{A,*}`.

Consequently the least-squares amplitude defect satisfies

\[
\boxed{
K_{A,n}(\lambda,k)
\to
K_{A,*}(\lambda,k)
}
\]

uniformly on compact subintervals of `I`.

---

## 6. Continuity of the elliptic recovery betaE

M5-75 gives

\[
\beta_E
=
\frac{
\displaystyle\int_{\Omega_{\lambda,k}}Q_U\,dY
-2\nu\displaystyle\int_{\Gamma_{\lambda,k}}\partial_nb\,dS
}{
\displaystyle\int_{\Gamma_{\lambda,k}}|\nabla a|\,dS
},
\]

where

\[
Q_U=\partial_iU_j\,\partial_jU_i.
\]

On a persistent regular branch:

- `Q_{U_n}->Q_{U_*}` uniformly locally;
- the nested domains converge by normal graphs;
- `partial_n b_n->partial_n b_*` uniformly;
- the denominator satisfies
  \[
  \int_{\Gamma^n}|\nabla a_n|dS
  \ge c(\kappa,\Gamma_*)>0.
  \]

Hence

\[
\boxed{
\beta_{E,n}	o\beta_{E,*}
}
\]

uniformly on compact regular branch intervals.

Therefore

\[
\boxed{
\delta_{\beta,n}
=
\beta_{E,n}-\beta_{A,n}
\to
\delta_{\beta,*}.
}
\]

The normalized scale-invariant defect

\[
\mathfrak B_n
=
\frac{\delta_{\beta,n}}{\lambda}
\]

converges as well because `lambda>=lambda_->0`.

---

## 7. Continuity of Kalpha

M5-76 uses

\[
g_1=|\nabla a|^2,
\qquad
g_2=\Delta a,
\qquad
g_3=2\nu\Delta b+Q_U.
\]

The `C4` local convergence gives uniform convergence of all these fields on the persistent branch.

Since

\[
g_1\ge\kappa^2/4
\]

for large `n`, the denominator

\[
\langle g_1,g_1\rangle_\Gamma
\]

stays uniformly positive.

Thus

\[
\alpha_{P,n}	o\alpha_{P,*}
\]

and

\[
\boxed{
K_{\alpha,n}	o K_{\alpha,*}.
}
\]

---

## 8. Continuity of the cross-level integrability defect

The final defect is

\[
\mathfrak I
=
\alpha_P-\partial_\lambda\beta.
\]

On a persistent `C4` regular nested family, the level integrals defining `beta_E` and `beta_A` depend smoothly on `lambda`.

The standard normal-variation formula for a regular level family differentiates a surface integral through one additional normal derivative and the level-set mean curvature, all controlled by the local `C4` convergence and the bound

\[
|\nabla a|\ge\kappa.
\]

Therefore

\[
\partial_\lambda\beta_n
\to
\partial_\lambda\beta_*
\]

on compact subintervals where the crossing denominator remains at least `eta`.

Hence

\[
\boxed{
\mathfrak I_n
\to
\mathfrak I_*.
}
\]

---

## 9. Closedness of the exact regular endpoint system

Under the persistent regular-crossing assumptions, if

\[
K_{A,n}\to0,
\qquad
\delta_{\beta,n}\to0,
\qquad
K_{\alpha,n}\to0,
\qquad
\mathfrak I_n\to0,
\]

then the W1 omega-limit state satisfies

\[
\boxed{
K_{A,*}=0,
\qquad
\delta_{\beta,*}=0,
\qquad
K_{\alpha,*}=0,
\qquad
\mathfrak I_*=0.
}
\]

Thus the regular crossing endpoint constraints form a closed condition in the actual local analytic topology supplied by W1.

Conversely, if for some robust limit level

\[
|\mathfrak B_*|
+K_{A,*}^{1/2}
+K_{\alpha,*}^{1/2}
+|\mathfrak I_*|
\ge d_*>0,
\]

then all sufficiently nearby W1 states retain a positive defect.

This gives the local strict-gap mechanism needed by the compactness strategy.

---

## 10. No-division variant near zeros of b

The quotient defining `beta_A` is inconvenient if `b` becomes small.

M5-76 already supplied the no-division identity

\[
\alpha g_1b+g_2F+g_3b=0.
\]

Define

\[
R=g_1b,
\qquad
H=g_2F+g_3b.
\]

Then exact compatibility requires

\[
H=-\alpha R.
\]

The associated rank-one residual can be written using only polynomial combinations of the locally convergent fields.

Therefore this no-division residual remains continuous even when `b` has isolated zeros.

Only collapse of `b` on the entire level removes the ability to recover `beta_A` itself.

---

## 11. What W1 compactness does not yet control

The preceding theorem fails to give a uniform endpoint gap if a saturating sequence can force any of the following:

1. **critical-level degeneration**
   \[
   \inf_{\Gamma_n}|\nabla a_n|\to0;
   \]
2. **crossing-denominator collapse**
   \[
   \langle b_n,b_n\rangle_{\Gamma_n}\to0;
   \]
3. **branch topology change** inside the selected amplitude interval;
4. **loss of a fixed-core branch**, so that the active geometry migrates outside every fixed compact set.

These are genuine compactness escape routes and must not be hidden by formal level differentiation.

---

## 12. DSD audit

### GREEN

Local analytic W1 compactness is strong enough to pass every finite-order M5-74--M5-76 defect through a persistent regular branch.

### GREEN

The exact regular endpoint set is closed in this topology.

### GREEN

A positive defect at one robust limit branch persists in a neighborhood and therefore yields a local strict endpoint gap.

### GREEN

The no-division joint residual remains continuous through isolated zeros of the crossing field.

### YELLOW

Uniform regularity of the selected amplitude branch is an additional geometric requirement, not a consequence of global `Lp` precompactness by itself.

### RED

Critical-level concentration or branch migration could still allow a saturating sequence to avoid the regular-branch continuity theorem.

---

## 13. Next calculation

The returned positive pump already has a uniform crossing lower bound through M5-71/M5-78.

The next step is therefore to combine

\[
X_w\ge c_1>0
\]

with

\[
T
=
\int w(\lambda)
\sum_k\tau(\lambda,k)\,d\lambda
\]

to determine whether every saturating sequence must contain at least one quantitatively nondegenerate regular crossing level.

If yes, M5-80 converts W1 compactness into an exact smooth endpoint limit.

If not, the only remaining escape is a measurable concentration of crossing mass toward critical/topology-changing levels or spatial escape, which becomes a sharply isolated geometric target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
