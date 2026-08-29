# DSD M5-276 — Weak-`L^3` no-H/no-T to Albritton–Barker Master Reduction

Date: 2026-08-30

Parent: `DSD_M5_275_ALBRITTON_BARKER_GLOBAL_RG_ANCIENT_LIOUVILLE_GATE_2026-08-30.md`

Status: **MAJOR MASTER REDUCTION / THE PREVIOUS SPATIAL POINTWISE TYPE-I REQUIREMENT IS NOT NEEDED FOR THE ALBRITTON–BARKER ENDGAME / ON THE AUDITED COMPLETE FIRST-HITTING ANCIENT CORRIDOR, UNIFORM NON-H DERIVATIVE RATIO PLUS UNIFORM NON-T CAMPANATO CONTROL GIVE A UNIFORM `L^{3,\infty}` BOUND / THE FIRST-HITTING VORTICITY CAP AND THIS WEAK-CRITICAL BOUND GIVE GLOBAL BOUNDEDNESS ON EVERY FIXED NEGATIVE-TIME SLAB AND HENCE THE REQUIRED MILD ANCIENT CLASS / THE TERMINAL TRACE BELONGS TO `L^{3,\infty}` AND THEREFORE TO THE ALBRITTON–BARKER SUBSPACE `\mathbb B` WITH DISTANCE ZERO / THE COMPLETE NONTRIVIAL NO-H/NO-T ANCIENT BRANCH IS EXCLUDED / GLOBAL REGULARITY UNPROVED BECAUSE H/T/COMPACTNESS ESCAPES REMAIN.**

---

## 1. Purpose

M5-275 closed the complete realized W1 branch after imposing a pointwise spatial Type-I tail bound.

The imported Albritton–Barker Liouville theorem is stronger than that formulation needs.  Theorem 4.1 of

- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier–Stokes equations and Liouville theorems*, J. Math. Fluid Mech. 21 (2019), 43, arXiv:1811.00502,

assumes a **mild ancient solution** and a sequence `t_k -> -infinity` with

\[
\|v(t_k)\|_{L^{3,\infty}}\le M,
\]

plus

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
(v(0),\mathbb B)\le\varepsilon(M),
\]

where the paper defines

\[
\boxed{
\mathbb B
=
\{f\in\dot B^{-1}_{\infty,\infty}:
 f(\lambda\,\cdot)\to0\text{ in }\mathcal D'
 \text{ as }\lambda\to\infty\}.
}
\]

The conclusion is `v=0`.

Thus the correct new question is whether the repository's **no-H/no-T complete ancient corridor already implies the theorem's weak-critical and mildness hypotheses**.

---

## 2. Audited no-H/no-T shell controls

On every normalized W1 time slice and every fixed-shape annulus `A_R`, use

\[
E_1(R)
:=R\int_{A_R^*}|\nabla V|^2,
\]

\[
\mathfrak C_A(R)
:=R^{-1}\int_{A_R^*}|V-(V)_{A_R^*}|^2,
\]

and the solenoidal localized derivative ratio

\[
\Gamma_R
:=
\frac{R\|\nabla f_R\|_2}{\|f_R\|_2}.
\]

The existing weak-`L^3` escalation audit proved

\[
\boxed{
\sup_R E_1(R)<\infty,
\qquad
\sup_R\mathfrak C_A(R)<\infty
\quad\Longrightarrow\quad
V\in L^{3,\infty}(\mathbb R^3).
}
\]

It also proved, in the genuinely escalating regime,

\[
\boxed{
\Gamma_R^2
\gtrsim
\frac{E_1(R)}{\mathfrak C_A(R)}.
}
\]

The non-escalating regime already has `E_1` bounded by a fixed multiple of the Campanato error.

Therefore if the retained pure corridor has uniform constants

\[
\boxed{
\Gamma_R\le\Gamma_*,
\qquad
\mathfrak C_A(R)\le C_T
\quad\text{for all }R,
}
\]

then there is a finite constant `E_*` depending only on the corridor constants such that

\[
\boxed{
E_1(R)\le E_*
\quad\text{for all }R.
}
\]

The already-audited dyadic-mean contribution is part of the same Campanato/no-turnover package.

Hence

\[
\boxed{
\|V(s)\|_{L^{3,\infty}}
\le M_*
\quad\text{uniformly on the complete W1 orbit.}
}
\]

This is the exact contrapositive of the earlier routing

\[
\|V\|_{L^{3,\infty}}\uparrow
\Longrightarrow
H_{freq}\lor T_{Campanato}.
\]

Status: **PROVED by the existing annular weak-`L^3` gate plus the non-H/non-T thresholds.**

---

## 3. Transfer the weak-critical bound to the global RG ancient solution

M5-274 gives the full RG reconstruction for all `rho>0`.

Write

\[
U(x,\tau)
:=\mathscr R_{-\tau}(T)(x),
\qquad
-\infty<\tau<0.
\]

For `rho=-tau`, the exact reconstruction is a Navier–Stokes scaling of one W1 state:

\[
\mathscr R_\rho(T)(x)
=
R\,(S(h)V)(Rx),
\qquad
R=\rho^{-1/2},
\qquad
h=-\log\rho.
\]

The `L^{3,\infty}` norm is critical under this scaling. Therefore

\[
\boxed{
\|U(\tau)\|_{L^{3,\infty}}
=
\|S(h)V\|_{L^{3,\infty}}
\le M_*
\quad\forall\tau<0.
}
\]

In particular, the Albritton–Barker backward-sequence hypothesis holds for every sequence

\[
\tau_k\downarrow-\infty.
\]

---

## 4. Mildness bridge from weak-`L^3` plus the first-hitting vorticity cap

The imported theorem requires a mild ancient solution belonging locally in time to `L^infinity_x`.

The complete first-hitting ancient corridor supplies a global vorticity cap in similarity variables.  Under the RG scaling, on every fixed negative-time slab

\[
-I=[-B,-A],
\qquad
0<A<B<\infty,
\]

there is a finite bound

\[
\boxed{
\sup_{\tau\in I}\|\Xi(\tau)\|_{L^\infty}
\le K_I(A,B)<\infty,
\qquad
\Xi=\nabla\times U.
}
\]

The weak-`L^3` bound gives a uniform local `L^2` bound on every unit ball.  Indeed Lorentz Hölder implies

\[
\boxed{
\sup_{x_0\in\mathbb R^3}
\|U(\tau)\|_{L^2(B_1(x_0))}
\le C M_*.
}
\]

Now use local div-curl/elliptic estimates on concentric balls.

First, from

\[
\nabla\cdot U=0,
\qquad
\nabla\times U=\Xi,
\]

one has an interior estimate

\[
\|U\|_{W^{1,2}(B_{3/4}(x_0))}
\le
C
\left(
\|\Xi\|_{L^2(B_1(x_0))}
+
\|U\|_{L^2(B_1(x_0))}
\right).
\]

Hence uniformly on the slab

\[
U\in L^6_{loc}
\]

with a constant independent of the ball center.

Apply the same div-curl estimate at exponent `p=6` on a smaller ball. Since

\[
\Xi\in L^\infty
\subset L^6(B_{3/4}(x_0))
\]

and `U` has the just obtained local `L^6` bound,

\[
\|U\|_{W^{1,6}(B_{1/2}(x_0))}
\le C(A,B,M_*,K_I).
\]

Sobolev embedding gives

\[
\boxed{
\sup_{\tau\in[-B,-A]}
\|U(\tau)\|_{L^\infty(\mathbb R^3)}
\le C(A,B,M_*,K_I)<\infty.
}
\]

Because `U` is the smooth complete RG realization and is globally bounded on every compact negative-time slab, the standard whole-space Duhamel/Stokes representation applies on every finite interval

\[
[t_0,t_1]\Subset(-\infty,0).
\]

Thus `U` belongs to the mild ancient class used in Albritton–Barker Theorem 4.1.

Status: **PROVED modulo standard interior div-curl estimates and the standard equivalence of bounded classical whole-space solutions with the mild/Duhamel representation on finite time intervals.**

---

## 5. The terminal trace is automatically in weak `L^3`

M5-269 supplies the actual terminal distributional trace

\[
U(\tau)\to T
\quad\text{in }\mathcal D'
\qquad(\tau\uparrow0).
\]

The family is uniformly bounded in `L^{3,\infty}`.

Using the Lorentz duality

\[
L^{3,\infty}=(L^{3/2,1})^*
\]

in the weak-star sense, the distributional limit belongs to the same space:

\[
\boxed{
T\in L^{3,\infty}(\mathbb R^3),
\qquad
\|T\|_{L^{3,\infty}}\le M_*.
}
\]

This step does **not** require the stronger pointwise bound `|T(x)|<=C/|x|` used in M5-275.

---

## 6. Every weak-`L^3` trace lies in the Albritton–Barker subspace `mathbb B`

First use the standard critical embedding

\[
\boxed{
L^{3,\infty}(\mathbb R^3)
\hookrightarrow
\dot B^{-1}_{\infty,\infty}(\mathbb R^3).
}
\]

For example, the heat-semigroup characterization gives

\[
\sup_{t>0}
\sqrt t\,\|e^{t\Delta}T\|_\infty
\le C\|T\|_{L^{3,\infty}}.
\]

It remains to check the defining distributional condition of `mathbb B`.

For `phi in C_c^infinity`, Lorentz Hölder gives

\[
\begin{aligned}
|\langle T(\lambda\cdot),\phi\rangle|
&=
\lambda^{-3}
|\langle T,\phi(\cdot/\lambda)\rangle|\\
&\le
\lambda^{-3}
\|T\|_{L^{3,\infty}}
\|\phi(\cdot/\lambda)\|_{L^{3/2,1}}.
\end{aligned}
\]

The Lorentz norm scales as

\[
\|\phi(\cdot/\lambda)\|_{L^{3/2,1}}
=
\lambda^2\|\phi\|_{L^{3/2,1}}.
\]

Therefore

\[
\boxed{
|\langle T(\lambda\cdot),\phi\rangle|
\le
\lambda^{-1}
M_*\|\phi\|_{L^{3/2,1}}
\to0.
}
\]

Hence

\[
\boxed{T\in\mathbb B.}
\]

Consequently

\[
\boxed{
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}
(T,\mathbb B)=0.
}
\]

Status: **PROVED.**

---

## 7. Apply Albritton–Barker Theorem 4.1

The global RG ancient solution `U` now satisfies all imported hypotheses:

1. `U` is a mild ancient solution on `R^3 x (-infinity,0)`;
2. for every backward sequence `tau_k -> -infinity`,
   \[
   \|U(\tau_k)\|_{L^{3,\infty}}\le M_*;
   \]
3. its terminal trace satisfies
   \[
   U(0)=T\in\mathbb B,
   \]
   hence the required Besov distance is zero.

Therefore the theorem gives

\[
\boxed{U\equiv0.}
\]

But at `rho=1`,

\[
U(-1)=\mathscr R_1(T)=V,
\]

and the first-hitting/checkpoint compactness package supplies a nonzero vorticity witness.

Contradiction.

Thus

\[
\boxed{
\text{complete nontrivial no-}H_{freq}\text{/no-}T_{Campanato}
\text{ ancient branch}=\varnothing.
}
\]

---

## 8. Updated post-Liouville master reduction

Suppose a hypothetical singular first-hitting tower survives.

If the compactness/complete-ancient extraction succeeds and both quiet structural conditions hold,

\[
\sup\Gamma_R<\infty,
\qquad
\sup\mathfrak C_A(R)<\infty,
\]

then Sections 2--7 give a contradiction.

Therefore every singular tower must enter at least one of

\[
\boxed{
H_{freq}
\quad\lor\quad
T_{Campanato}
\quad\lor\quad
C_{fail},
}
\]

where `C_fail` denotes failure of the compactness/completeness/local-energy passage required to construct the complete nontrivial ancient RG solution.

This is a substantially shorter master frontier than the previous stationary/DSS/aperiodic-tail tree.

---

## 9. What is and is not closed

### CLOSED on the complete no-H/no-T corridor

- strong `L^3` versus weak `L^3` tail distinction;
- persistent passive non-`L^3` shell genealogy as an independent final endpoint;
- stationary versus DSS versus aperiodic canonical-tail classification;
- spatial pointwise Type-I tail as an extra hypothesis for the Liouville step.

All of these collapse once uniform weak `L^3` and the complete RG ancient realization are available.

### STILL OPEN

- prove that every `H_freq` occurrence either prevents singularity or can be renormalized/reselected into a new first-hitting tower that re-enters the no-H corridor;
- close the genuine Campanato/material/pressure turnover branch `T`;
- audit and close every compactness/completeness failure mode in `C_fail`;
- verify that no hidden centering/gauge branch was omitted when passing the shell bounds uniformly along the complete orbit.

---

## 10. DSD verdict

### Formation — GREEN

The ancient solution and terminal trace are both realized objects from the first-hitting/RG construction.

### Axis — GREEN

Shell radius, W1 similarity time, RG depth `rho`, and physical ancient time `tau=-rho` remain distinct.

### Static aggregation — GREEN

Weak-`L^3` control is obtained from the already typed shell quantities; no pointwise tail regularity is inserted.

### Dynamics — GREEN

Mildness is derived from the realized vorticity cap and weak-critical local mass bound rather than assumed.

### Cross-audit — GREEN WITH EXPLICIT FRONTIER

The tail endgame is replaced by the shorter implication

\[
\boxed{
\text{singular survivor}
\Longrightarrow
H_{freq}\lor T_{Campanato}\lor C_{fail}.
}
\]

The global regularity problem is **not** solved because those three pre-Liouville exits have not all been closed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
