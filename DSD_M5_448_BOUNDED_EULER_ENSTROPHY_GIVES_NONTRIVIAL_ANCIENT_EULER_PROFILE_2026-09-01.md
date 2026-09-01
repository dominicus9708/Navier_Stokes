# DSD M5-448 — Bounded source-scale enstrophy yields a nontrivial ancient Euler vorticity profile

Date: 2026-09-01

Status: **EULER-PROFILE EXTRACTION WITHOUT A SEPARATE PRESSURE-COMPACTNESS ASSUMPTION / IN THE CANONICAL REMOTE EULER SCALING THE FIRST-HITTING RECORD GIVES UNIFORM `L-infinity` VORTICITY FOR ALL BACKWARD TIMES, AND IF THE GLOBAL SOURCE-SCALE `L2` VORTICITY IS ALSO UNIFORMLY BOUNDED ON EACH COMPACT BACKWARD TIME INTERVAL, BIOT--SAVART GIVES UNIFORM LOCAL VELOCITY `L-infinity` AND `W^{1,p}` BOUNDS / THE VORTICITY EQUATION THEN GIVES TIME EQUICONTINUITY IN DISTRIBUTIONS, THE VANISHING VISCOSITY TERM DISAPPEARS, AND A SUBSEQUENCE CONVERGES TO A NONTRIVIAL ANCIENT EULER SOLUTION DETECTED BY THE FIXED REMOTE-STRAIN PAIRING / IF THE SOURCE-SCALE `L2` VORTICITY BOUND FAILS, THE BRANCH IS STRONG MULTISCALE ENSTROPHY ESCALATION / GLOBAL REGULARITY UNPROVED BECAUSE SUCH ANCIENT EULER PROFILES ARE NOT GENERICALLY FORBIDDEN.**

---

## 1. Canonical source Euler sequence

Take remote source stages with

\[
R_j=K_jr_j,
\qquad
K_j\to\infty.
\]

Use the canonical velocity scale

\[
U_j^E=\frac{\nu K_j^2}{R_j}
\]

and time scale

\[
T_j^E=\frac{R_j}{U_j^E}=\frac{r_j^2}{\nu}.
\]

After a fixed Galilean translation for each `j`, define

\[
V_j(y,\tau)
=
\frac{u(x,t)-c_j}{U_j^E},
\qquad
\Omega_j=\nabla\times V_j.
\]

Then

\[
\boxed{
\partial_\tau V_j+V_j\cdot\nabla V_j
=-\nabla P_j+K_j^{-2}\Delta V_j.
}
\]

---

## 2. Backward vorticity cap from first-hitting record structure

At the first-hitting time `t_j`,

\[
W_j=\|\omega(t_j)\|_\infty.
\]

By the record/first-hitting definition, for all earlier physical times in the retained smooth interval,

\[
\|\omega(t)\|_\infty\le W_j.
\]

Since the Euler vorticity unit is exactly `W_j`,

\[
\boxed{
\|\Omega_j(\tau)\|_\infty\le1
}
\]

for every backward scaled time represented before `t_j`.

The physical scale `T_j^E=r_j^2/nu` tends to zero, while `t_j` approaches a positive finite singular time. Thus the available backward scaled interval length tends to infinity.

Hence every fixed interval

\[
[-A,0]
\]

is contained in the rescaled domain for all sufficiently large `j`.

---

## 3. Bounded-enstrophy branch

Assume that for every fixed `A<infinity`,

\[
\boxed{
\sup_j\sup_{\tau\in[-A,0]}
\|\Omega_j(\tau)\|_2
\le B_A<\infty.
}
\]

If this fails for some `A`, the branch is by definition source-scale/multiscale enstrophy escalation and belongs to

\[
\boxed{H_{Euler\text{-}enstrophy}^{strong}.}
\]

Thus we only analyze the bounded branch below.

---

## 4. Biot--Savart gives uniform velocity control

For whole-space divergence-free velocity, modulo the fixed Galilean constant, velocity is recovered from vorticity by Biot--Savart.

The kernel has degree `-2`. Split the integral into `|y-z|<1` and `>1`.

The near part is bounded by `||Omega_j||_infinity`, while the far part is bounded by Cauchy--Schwarz using `||Omega_j||_2` because the velocity kernel is square integrable at infinity.

Therefore on `[-A,0]`,

\[
\boxed{
\|V_j(\tau)\|_\infty
\le C(1+B_A).
}
\]

Similarly Riesz/div-curl estimates give, for every finite `2<=p<infinity`,

\[
\boxed{
\|\nabla V_j(\tau)\|_p
\le C_p
\|\Omega_j(\tau)\|_p
\le C_{p,A},
}
\]

using interpolation between `L2` and `L-infinity` for `Omega_j`.

Hence `V_j` is locally spatially precompact in `C^{0,alpha}` for every `alpha<1` after choosing sufficiently large finite `p`.

---

## 5. Vorticity equation avoids pressure compactness

Curl the rescaled Navier--Stokes equation:

\[
\boxed{
\partial_\tau\Omega_j
+\nabla\cdot
(V_j\otimes\Omega_j-\Omega_j\otimes V_j)
=K_j^{-2}\Delta\Omega_j.
}
\]

Let `phi` be a fixed compactly supported smooth vector test function. Then

\[
\frac d{d\tau}\int\Omega_j\cdot\phi
=
\int
(V_j\otimes\Omega_j-\Omega_j\otimes V_j):\nabla\phi
+K_j^{-2}\int\Omega_j\cdot\Delta\phi.
\]

The right-hand side is uniformly bounded on `[-A,0]` because

\[
\|V_j\|_\infty+\|\Omega_j\|_\infty\le C_A.
\]

Therefore the scalar functions

\[
\tau\mapsto\int\Omega_j(\tau)\cdot\phi
\]

are equi-Lipschitz on compact backward intervals.

This gives time compactness in the weak/distributional topology without any direct pressure estimate.

---

## 6. Extract an ancient vorticity limit

By weak-* compactness in `L-infinity` and weak compactness in `L2`, together with the test-function time equicontinuity, pass to a diagonal subsequence so that on every compact space-time cylinder

\[
\Omega_j\stackrel{*}{\rightharpoonup}\Omega
\]

and

\[
V_j\to V
\]

strongly locally after the Biot--Savart spatial smoothing and the fixed Galilean gauge.

Because `V_j` converges strongly and `Omega_j` weakly, the products

\[
V_j\otimes\Omega_j
\]

pass to the limit distributionally.

Moreover

\[
K_j^{-2}\to0,
\]

so the viscous term vanishes against test functions.

Thus

\[
\boxed{
\partial_\tau\Omega
+\nabla\cdot
(V\otimes\Omega-\Omega\otimes V)
=0
}
\]

on

\[
\mathbb R^3\times(-\infty,0].
\]

Together with `div V=0` and `curl V=Omega`, this is the incompressible Euler equation in vorticity form.

---

## 7. Nontriviality is preserved by the source functional

M5-445 identifies a fixed smooth source kernel `mathcal K` supported in a unit annulus such that at `tau=0`

\[
\left|
\int\mathcal K(y)\Omega_j(y,0)dy
\right|
\ge\theta_0>0.
\]

Weak convergence preserves this linear pairing:

\[
\boxed{
\left|
\int\mathcal K(y)\Omega(y,0)dy
\right|
\ge\theta_0.
}
\]

Therefore

\[
\boxed{
\Omega(\cdot,0)\not\equiv0,
\qquad
V\not\equiv0.
}
\]

The Euler profile cannot disappear through weak microscopic cancellation.

---

## 8. Limit class

For every finite backward interval `[-A,0]`, the limit satisfies

\[
\boxed{
\Omega\in L^\infty([-A,0];L^2\cap L^\infty),
}
\]

with corresponding bounded/local `W^{1,p}` velocity control.

Thus the strong remote Type-II branch has the exact split

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
H_{Euler\text{-}enstrophy}^{strong}
\lor
E_{ancient}^{\Omega\in L^\infty_t(L^2\cap L^\infty)}.
}
\]

---

## 9. Relation to Seregin's Type-II program

Recent work of Seregin also uses Euler scaling to turn selected Navier--Stokes Type-II scenarios into nontrivial ancient Euler solutions under scale-weighted compactness assumptions.

M5-448 reaches an ancient Euler profile from a different internally generated condition: the first-hitting vorticity cap plus a uniform source-scale `L2` vorticity bound.

The resulting limit class is not asserted to coincide with the precise class in Seregin's theorem, and no Liouville conclusion is imported automatically.

---

## 10. Why this is not yet a contradiction

Nontrivial steady and ancient Euler structures with bounded vorticity exist in broad function classes. Bounded vorticity plus `L2` vorticity is not by itself a known zero-Liouville condition sufficient for the present purpose.

The remaining task is to use **additional first-hitting ancestry/source properties**, not merely generic Euler regularity, to rigidify the limit.

Possible extra descriptors to carry into the limit include:

- marked positive longitudinal source pairing;
- source/target angular geometry;
- recurrent first-hitting production balance;
- material-flux ancestry or replacement information;
- tail/energy conditions inherited from finite physical energy.

---

## 11. Audit verdict

### Proved conditional profile extraction

If source-scale vorticity enstrophy is uniformly bounded on every compact backward interval, then a subsequence converges to a nonzero ancient Euler solution with

\[
\boxed{
\Omega\in L^\infty_{loc,t}(L^2\cap L^\infty).
}
\]

### Alternative

Failure of that bound is strong Euler-scale enstrophy escalation.

### Current hard split

\[
\boxed{
H_{Euler\text{-}enstrophy}^{strong}
\lor
E_{ancient}^{nontrivial}.
}
\]

### Still open

- carry first-hitting/genealogy invariants into the Euler limit;
- establish an applicable Euler rigidity theorem;
- exclude strong source-scale enstrophy escalation;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
