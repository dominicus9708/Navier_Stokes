# DSD M5-524 — Audit Pineau--Vicol local near-self-similar regularity criterion against the compact hard core

Date: 2026-09-01

Status: **EXTERNAL-THEOREM HYPOTHESIS AUDIT / PINEAU--VICOL (ARXIV:2607.09619v2, THEOREM 1.9) DOES NOT IDENTIFY RECURRENCE WITH APPROXIMATE SELF-SIMILARITY: THEIR LOCAL REGULARITY CRITERION REQUIRES SMALLNESS OF THE ACTUAL SIMILARITY-TIME DERIVATIVE `partial_s U` AT ONE LATE TIME ON AN EXPANDING SIMILARITY BALL, TOGETHER WITH A SPATIAL TYPE-I VELOCITY BOUND AND A PRESSURE BOUND ON A FIXED ANNULUS / M5-509'S COMPACT HARD CORE IS UNIFORMLY NONSTATIONARY, AND M5-523 ONLY GIVES UNIFORM `U->0`, NOT THE REQUIRED `1/(1+|y|)` TYPE-I RATE / THEREFORE THE THEOREM CANNOT BE SILENTLY IMPORTED TO CLOSE THE CURRENT RECURRENT HULL / INSTEAD IT SHARPENS THE TARGET: A HYPOTHETICAL SURVIVOR MUST REMAIN QUANTITATIVELY AWAY FROM LOCAL NEAR-SELF-SIMILARITY OR FAIL THE SPATIAL TYPE-I/PRESSURE HYPOTHESES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External theorem being audited

Reference:

Ben Pineau and Vlad Vicol,
`On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations`,
arXiv:2607.09619v2 (2026), Theorem 1.9.

The theorem considers a smooth Navier--Stokes solution on

\[
B_1\times[-1,0)
\]

with the local spatial Type-I bound

\[
\boxed{
|u(x,t)|
\le
\frac{C_u}{\sqrt{-t}+|x|}.
}
\]

It also assumes a pressure bound on the annulus

\[
\frac12<|x|<\frac34.
\]

For constants `delta_0(C_u)>0` and `s_0(C_u,C_p)`, regularity at `(0,0)` follows if at one sufficiently late time

\[
\bar t=-e^{-\bar s}
\]

one has

\[
\sqrt{-\bar t}
\left\|
(-\bar t)\partial_tu
-\frac12u
-\frac12(x\cdot\nabla)u
\right\|_{L^\infty(B_1)}
\le\delta_0.
\]

In similarity variables this is exactly

\[
\boxed{
\|\partial_sU(\cdot,\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}
\le\delta_0.
}
\]

Thus the hypothesis is small **instantaneous similarity velocity**, not merely return of the orbit near an earlier state.

---

## 2. Recurrence is not derivative smallness

The M5-483--508 similarity hull is recurrent/compact in similarity time.

Recurrence gives sequences

\[
s_n<t_n,
\qquad
U(\cdot,t_n)\approx U(\cdot,s_n)
\]

in strong compact topologies.

This does **not** imply the existence of an intermediate time `tau_n` with

\[
\|\partial_sU(\tau_n)\|
\ll1.
\]

A periodic orbit moving at nonzero constant phase speed is the elementary countermodel:

\[
U(s+T)=U(s)
\]

while

\[
\inf_s\|\partial_sU(s)\|>0
\]

is possible.

Therefore

\[
\boxed{
\text{recurrence}
\not\Rightarrow
\text{Pineau--Vicol approximate self-similarity}.
}
\]

---

## 3. M5-509 points in the opposite direction

M5-509 excluded stationary points from the marked compact hull and obtained a fixed local nonstationarity bound for vorticity,

\[
\boxed{
\inf_{\widehat{\mathfrak H}}
\|\partial_sW\|_{L^2(B_R)}
\ge\delta_W>0
}
\]

for a suitable fixed marked ball `B_R`.

Since

\[
\partial_sW
=\nabla\times(\partial_sU),
\]

the hard core is already separated from exact similarity equilibrium.

On the M5-508 all-order compact branch, all fixed derivatives of `partial_s U` are uniformly bounded through the similarity equation.

Therefore the `L2` curl lower bound can be thickened to a quantitative local `C0` velocity-derivative lower bound, as recorded below.

---

## 4. Upgrade vorticity-time nonstationarity to velocity-time nonstationarity

From

\[
\|\partial_sW\|_{L^2(B_R)}
\ge\delta_W,
\]

there exists a point `y_* in B_R` such that

\[
|\partial_sW(y_*)|
\ge
c_R\delta_W
=:
g_*>0.
\]

Because

\[
\partial_sW=\nabla\times\partial_sU,
\]

at least one first spatial derivative of `partial_sU` has magnitude at least `c g_*` at `y_*`.

Global smooth compactness gives a uniform bound

\[
\|\nabla^2\partial_sU\|_\infty
\le M_{s,2}<\infty.
\]

Hence on a fixed line segment of length

\[
r_*
\asymp
\frac{g_*}{M_{s,2}}
\]

through `y_*`, one component of `grad partial_s U` keeps a fixed sign and at least half its initial magnitude.

The fundamental theorem of calculus then forces

\[
\boxed{
\|\partial_sU\|_{L^\infty(B_{R+r_*})}
\ge
\delta_U>0,
}
\]

where `delta_U` depends only on the compact-hull constants.

Thus the marked compact hard core is uniformly separated from stationary similarity flow even at the velocity level.

---

## 5. Consequence for the Pineau--Vicol small-derivative condition

For every sufficiently late `s`, the Pineau--Vicol expanding ball

\[
B_{e^{s/2}}
\]

contains the fixed ball `B_(R+r_*)`.

Therefore

\[
\boxed{
\|\partial_sU(\cdot,s)\|_{L^\infty(B_{e^{s/2}})}
\ge\delta_U
}
\]

on the retained hard core.

If the Pineau--Vicol threshold satisfies

\[
\delta_0<\delta_U,
\]

their approximate-self-similarity hypothesis is automatically avoided.

If the numerical ordering of the two constants is unknown, the logically safe conclusion is still that M5-509 provides no mechanism making their derivative-smallness hypothesis true.

The theorem cannot be triggered from recurrence alone.

---

## 6. Independent missing spatial Type-I hypothesis

Theorem 1.9 assumes

\[
|u(x,t)|
\le
\frac{C_u}{\sqrt{-t}+|x|}
\]

on the physical unit cylinder.

In similarity coordinates this corresponds to

\[
|U(y,s)|
\le
\frac{C_u}{1+|y|}
\]

on the expanding region

\[
|y|<e^{s/2}.
\]

M5-523 proves only

\[
\sup_s|U(y,s)|\to0
\quad(|y|\to\infty)
\]

with the quantitative estimate

\[
|U(y,s)|
\le
C Z_*^{1/2}|y|^{-1/2}
+
C M_*^{1/3}\varepsilon_E(|y|/4)^{1/3}.
\]

This does not imply

\[
|U(y,s)|\lesssim|y|^{-1}.
\]

Hence the spatial Type-I hypothesis is an independent unresolved gate.

---

## 7. Pressure hypothesis

Theorem 1.9 also assumes bounded pressure on the fixed physical annulus

\[
\frac12<|x|<\frac34.
\]

The globally smooth similarity hull gives excellent local pressure regularity after pressure normalization, but the physical annulus corresponds to an expanding similarity annulus as `t->0-`.

Therefore a uniform pressure bound on that physical annulus is not automatic from fixed-ball similarity compactness alone.

M5-523's velocity vanishing suggests this may be accessible if stronger far-field velocity decay is proved, but no such implication is claimed here.

---

## 8. Exact audit verdict

The Pineau--Vicol local criterion requires three gates:

\[
\boxed{
\begin{aligned}
&PV_1:\quad |u(x,t)|\lesssim(\sqrt{-t}+|x|)^{-1},\\
&PV_2:\quad p\text{ bounded on a fixed physical annulus},\\
&PV_3:\quad \|\partial_sU(\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}\le\delta_0
\text{ at one late time}.
\end{aligned}
}
\]

The current compact hard core has not established `PV_1` or `PV_2`.

Moreover M5-509 shows persistent quantitative nonstationarity rather than a route toward `PV_3`.

Therefore

\[
\boxed{
\text{M5-508 compact recurrence}
\not\Rightarrow
\text{Theorem 1.9 regularity}.
}
\]

This prevents an invalid external-theorem shortcut.

---

## 9. What the theorem does teach the current program

The theorem identifies a strong local rigidity target.

A hypothetical singular Type-I-like survivor must avoid one-time local near-self-similarity.

The DSD program has independently reached a recurrent hard core with

\[
\boxed{
\text{positive phase-space motion}
+
\text{positive dual/ratchet activity}
+
\text{positive production}.
}
\]

Thus the two analyses are compatible:

\[
\boxed{
\text{survival requires persistent motion in similarity space, not convergence to one profile.}
}
\]

This makes the remaining problem closer to a genuine recurrent/breather obstruction than to an approximately stationary self-similar profile.

---

## 10. Updated external-theory frontier

The exact stationary branch is excluded by classical backward self-similar Liouville theorems.

Short exact DSS/RDSS branches under spatial Type-I assumptions are partially excluded by Chae--Wolf and Pineau--Vicol-type results.

One-time near-self-similar Type-I behavior is excluded by Pineau--Vicol Theorem 1.9.

The current survivor is therefore forced toward

\[
\boxed{
\text{nonstationary recurrent similarity dynamics}
}
\]

with either

\[
H_{low}^{velocity/pressure}
\]

preventing the spatial Type-I hypotheses, or persistent similarity-time motion preventing approximate self-similarity.

---

## 11. Highest-value next target

The highest-value internal target is now the low-frequency gate from M5-523.

Rather than searching for another positive-derivative estimate, audit whether the dilation/first-hitting genealogy constrains the nearly Galilean broad velocity modes responsible for failure of `L3` and `1/r` decay.

A useful decomposition is, on large annuli,

\[
U
=
(U)_{A_R}
+
\big(U-(U)_{A_R}\big).
\]

The fluctuation is controlled by vorticity/Dirichlet energy, while the annular mean is a low-frequency drift mode.

If the scale-dependent means can be shown to telescope, be Galilean-removable, or force a typed remote affine deformation, the missing spatial Type-I/L3 gate may shrink substantially.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
