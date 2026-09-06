# DSD M17-248 — Kappa turnover can be purely linear-diffusive and is not by itself a nonlinear physical budget

Date: 2026-09-06  
Canonical ID: **M17-248**

Status: **ANTI-SHORTCUT / M17-239--240 PRODUCE AN AMPLITUDE-INDEPENDENT MATERIAL TURNOVER ACTION FOR `KAPPA`, BUT THE EXACT CONSTITUTIVE LAW CONTAINS THE LINEAR WEIGHTED-DIFFUSION TERM `L_rho kappa`. AN AMPLITUDE-INDEPENDENT CHANGE OF THE QUOTIENT `kappa=Delta W/W` CAN OCCUR EVEN IN A PURELY LINEAR HEAT EVOLUTION: TWO DECAYING FOURIER MODES CHANGE THEIR RELATIVE WEIGHTS, SO `kappa` CHANGES BY ORDER ONE WHILE THE FIELD AMPLITUDE MAY BE MULTIPLIED BY AN ARBITRARILY SMALL CONSTANT. THEREFORE `T_kappa>=c` IS A REAL MATERIAL-STATE REFORMATION OBSERVABLE BUT NOT A FINITE NONLINEAR ENERGY/FLUX PAYMENT BY ITSELF. THE LINEAR-DIFFUSIVE BRANCH MUST BE CLOSED BY A RECURRENCE/ANCIENT-LINEAR OBSTRUCTION OR BY INTERFACE/AMBIENT REPLENISHMENT, NOT BY CALLING TURNOVER AN ENERGY COST. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why this audit is needed

M17-239 defines

\[
\mathcal T_\kappa
=
\ell^{-1}\iint|D_B\kappa|
\]

and proves an order-one lower bound when a fixed material fraction loses its critical multiplier sign/magnitude.

M17-240 then gives

\[
D_B\kappa
=L_\rho\kappa
+L_\rho\sigma
-\kappa
+\mathcal R_{geom}.
\]

It would be incorrect to interpret every positive \(\mathcal T_\kappa\) as a nonlinear Navier--Stokes production cost, because \(L_\rho\kappa\) contains ordinary diffusion-driven coefficient reformation.

---

## 2. Linear heat toy model

Consider the scalar heat equation on a periodic line,

\[
\partial_t f=\partial_{xx}f.
\]

For any \(\varepsilon>0\), let

\[
\boxed{
f_\varepsilon(x,t)
=\varepsilon
\left(e^{-t}\cos x+e^{-4t}\cos2x\right).
}
\]

This is an exact linear heat solution.

At \(x=0\),

\[
f_\varepsilon(0,t)
=\varepsilon(e^{-t}+e^{-4t}),
\]

and

\[
\partial_{xx}f_\varepsilon(0,t)
=-\varepsilon(e^{-t}+4e^{-4t}).
\]

Define the local quotient

\[
\kappa_\varepsilon(t)
:=
\frac{\partial_{xx}f_\varepsilon(0,t)}{f_\varepsilon(0,t)}.
\]

Then

\[
\boxed{
\kappa_\varepsilon(t)
=-\frac{e^{-t}+4e^{-4t}}{e^{-t}+e^{-4t}}.
}
\]

The factor \(\varepsilon\) cancels exactly.

---

## 3. Order-one coefficient turnover at arbitrarily small amplitude

At \(t=0\),

\[
\kappa_\varepsilon(0)=-\frac52.
\]

As \(t\to\infty\),

\[
\kappa_\varepsilon(t)\to-1.
\]

Thus the quotient changes by a fixed order-one amount under a purely linear diffusion process:

\[
\boxed{
|\Delta\kappa|=\frac32.
}
\]

This change is independent of \(\varepsilon\).

Meanwhile every quadratic physical norm of the field scales as

\[
\boxed{
\|f_\varepsilon\|^2
=\varepsilon^2\|f_1\|^2.
}
\]

Hence one may take \(\varepsilon\to0\) while retaining the same coefficient turnover.

---

## 4. Meaning for M17

The toy model is not used as a Navier--Stokes counterexample. It proves a narrower logical point:

\[
\boxed{
\text{amplitude-independent quotient turnover}
\not\Rightarrow
\text{amplitude-independent physical energy cost}.
}
\]

A quotient built from derivatives divided by the field can reform because diffusion changes relative modal weights.

This is precisely the role of the \(L_\rho\kappa\) payer in M17-240.

---

## 5. Correct interpretation of the turnover trichotomy

M17-240 should therefore be read as

\[
\boxed{
H_{\mathcal T_\kappa}
\Longrightarrow
H_{linear/weighted\ multiplier\ diffusion}
\lor
H_{strain\ diffusion}
\lor
H_{geometric\ reformation}.
}
\]

Only the latter branches may involve strong ambient/nonlinear geometry.

The first branch can survive even as local physical amplitude tends to zero.

---

## 6. Interaction with M17-245

M17-245 shows that the packet's own quadratic Navier--Stokes self-interaction is smaller than diffusion by

\[
\varepsilon_{nl}=a\ell^2\to0.
\]

Thus the low-amplitude limit makes the linear-diffusive interpretation **more**, not less, relevant.

On a branch where ambient/nonlocal forcing and interface input are also negligible, the local dynamics approach a linear similarity diffusion problem.

This identifies the correct next endpoint:

\[
\boxed{
\text{linear-diffusive low-amplitude recurrence problem}.
}
\]

---

## 7. What can still close the branch

A linear-diffusive coefficient packet could be eliminated only by an argument using more than one instantaneous state, for example:

1. nonexistence of a nonzero recurrent/ancient finite-energy solution of the limiting linear similarity equation;
2. a quantitative forward forgetting theorem plus a backward replenishment/interface cost;
3. a compactness theorem producing a nonzero linear tangent with enough time lifetime;
4. proof that ambient forcing cannot remain negligible on recurrent coefficient packets.

Calling \(\mathcal T_\kappa\) itself a finite physical budget is not valid.

---

## 8. DSD audit

- The heat example is used only to test a logical implication, not as a Navier--Stokes model solution.
- Coefficient turnover and physical quadratic cost are kept distinct.
- Linear diffusion is retained as a legitimate M17-240 payer.
- The amplitude-scaling firewall of M17-242 is respected.
- The next target is dynamic recurrence/linear obstruction, not another instantaneous quotient inequality.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
