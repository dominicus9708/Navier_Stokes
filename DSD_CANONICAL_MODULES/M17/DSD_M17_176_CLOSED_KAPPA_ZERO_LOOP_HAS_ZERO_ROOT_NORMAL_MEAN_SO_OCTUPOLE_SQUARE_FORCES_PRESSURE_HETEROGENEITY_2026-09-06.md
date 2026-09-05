# DSD M17-176 — A closed regular `kappa=0` loop has zero root-normal mean, so the octupole-square balance forces quantitative axial-pressure heterogeneity

Date: 2026-09-06  
Canonical ID: **M17-176**

Status: **COERCIVE CLOSED-LOOP CONSEQUENCE / FOR ANY CLOSED REGULAR SEMILINEAR ZERO CURVE `Gamma`, THE UNIT NORMAL `n_kappa=(F_qq,F_q3)/|grad kappa|` HAS ZERO VECTOR INTEGRAL, SO `oint F_qq/|grad kappa| ds=0`. COMBINING THIS PURE GEOMETRIC FACT WITH M17-170 GIVES `oint F_qq(H_V-Hbar)/|grad kappa| ds =25 oint O_V^2/(|Q|^4|grad kappa|) ds`, WHERE `Hbar` MAY BE ANY CONSTANT, IN PARTICULAR THE ZERO-CURVE MEAN OF `H_V`. CAUCHY--SCHWARZ THEN FORCES A POSITIVE LOWER BOUND ON THE VARIANCE OF THE GLOBAL AXIAL PRESSURE COORDINATE ALONG THE ZERO LOOP WHENEVER THE OCTUPOLE IS NONTRIVIAL. ON THE CONDITIONAL M17-172 BOUNDED-DENSITY PUSHFORWARD BRANCH, THE STRICT M5 HYSTERESIS BIAS GIVES A POSITIVE TIME-AVERAGED LOWER BOUND ON THE OCTUPOLE-SQUARE CROSSING MASS, AND THEREFORE ON THIS PRESSURE HETEROGENEITY. THIS IS A GENUINE COERCIVE SPATIAL CONSEQUENCE, BUT NOT YET A NONRECYCLABLE TEMPORAL COST. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Zero-curve normal geometry

Let `Gamma` be a smooth closed regular component of

\[
\kappa(q,x_3)=0.
\]

Choose the outward unit normal

\[
\boxed{
\mathbf n_\kappa
=\frac{(F_{qq},F_{q3})}{|\nabla\kappa|}.
}
\]

For every closed plane curve bounding a region `D`, the divergence theorem applied to a constant vector `c` gives

\[
\oint_\Gamma c\cdot n\,ds
=\int_D\operatorname{div}c\,dA
=0.
\]

Since this holds for every constant vector,

\[
\boxed{
\oint_\Gamma\mathbf n_\kappa\,ds=0.
}
\]

Hence componentwise

\[
\boxed{
\oint_\Gamma
\frac{F_{qq}}{|\nabla\kappa|}ds=0,
}
\]

and

\[
\boxed{
\oint_\Gamma
\frac{F_{q3}}{|\nabla\kappa|}ds=0.
}
\]

---

## 2. Recall the octupole-square balance

M17-170 gives

\[
\boxed{
\oint_\Gamma
\frac{F_{qq}H_V}{|\nabla\kappa|}ds
=25\oint_\Gamma
\frac{O_V^2}{|Q|_F^4|\nabla\kappa|}ds.
}
\]

Define

\[
\boxed{
d\nu_\Gamma:=\frac{ds}{|\nabla\kappa|}.}
\]

Then

\[
\int_\Gamma F_{qq}H_Vd\nu_\Gamma
=25\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma.
\]

---

## 3. Constant pressure offsets drop out

Section 1 gives

\[
\int_\Gamma F_{qq}d\nu_\Gamma=0.
\]

Therefore for **any constant** `c`,

\[
\boxed{
\int_\Gamma F_{qq}(H_V-c)d\nu_\Gamma
=25\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma.
}
\]

Choose the zero-curve mean

\[
\boxed{
\bar H_\Gamma
:=\frac1{\nu_\Gamma(\Gamma)}
\int_\Gamma H_Vd\nu_\Gamma.
}
\]

Then

\[
\boxed{
\int_\Gamma F_{qq}(H_V-\bar H_\Gamma)d\nu_\Gamma
=25\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma.
}
\]

Thus the square term can only be paid by spatial variation of `H_V` correlated with the sign-changing root-normal component `F_qq`.

---

## 4. Cauchy--Schwarz pressure-variance lower bound

Define

\[
A_O
:=\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma,
\]

\[
A_F
:=\int_\Gamma F_{qq}^2d\nu_\Gamma,
\]

and

\[
V_H
:=\int_\Gamma(H_V-\bar H_\Gamma)^2d\nu_\Gamma.
\]

Then

\[
25A_O
\le A_F^{1/2}V_H^{1/2}.
\]

Therefore, if `A_F>0`,

\[
\boxed{
V_H
\ge
625\frac{A_O^2}{A_F}.
}
\]

This is a quantitative lower bound on axial-pressure heterogeneity along the closed zero loop.

If `A_F=0`, then `F_qq=0` identically on the loop and the M17-170 identity forces `A_O=0`; hence there is no nontrivial octupole branch in that case.

---

## 5. Compact hard-hull simplification

On a compact regular zero-loop class assume

\[
|F_{qq}|\le C_F,
\qquad
0<\nu_\Gamma(\Gamma)\le L_\Gamma.
\]

Then

\[
A_F\le C_F^2L_\Gamma.
\]

Hence

\[
\boxed{
V_H
\ge
\frac{625}{C_F^2L_\Gamma}A_O^2.
}
\]

Thus any uniform lower bound on octupole-square mass produces a uniform lower bound on pressure variance.

---

## 6. M5 bias forces octupole-square mass — conditional M17-172 branch

Under M17-172, define the current-flux zero-curve measure

\[
\boxed{
d\nu_\theta^w
:=w_\theta\frac{ds}{|\nabla\kappa|}.}
\]

M17-095 gives the strict time-averaged bias

\[
\boxed{
\beta
:=\overline{
\int_{\Gamma_0}
 r_V\frac{O_V}{|Q|_F^2}
d\nu_\theta^w
}>0.
}
\]

Assume the recurrent crossing intensity obeys

\[
\boxed{
R_2
:=\overline{
\int_{\Gamma_0}r_V^2d\nu_\theta^w
}<\infty.
}
\]

Cauchy--Schwarz in the long-time crossing measure gives

\[
\beta^2
\le
R_2\,
\overline{
\int_{\Gamma_0}
\frac{O_V^2}{|Q|_F^4}
d\nu_\theta^w
}.
\]

Therefore

\[
\boxed{
\overline{
\int_{\Gamma_0}
\frac{O_V^2}{|Q|_F^4}
d\nu_\theta^w
}
\ge\frac{\beta^2}{R_2}>0.
}
\]

The relative-speed sign has disappeared after squaring.

---

## 7. Remove the transported density up to comparability

If the M17-172 bounded-density branch holds,

\[
0<c_w\le w_\theta\le C_w,
\]

then

\[
\int X^2d\nu_\theta^w
\le C_w\int X^2d\nu_\Gamma.
\]

Thus

\[
\boxed{
\overline{
\int_{\Gamma_0}
\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma
}
\ge
\frac{\beta^2}{C_wR_2}>0.
}
\]

On closed components satisfying the compact bounds of Section 5, M17-176 then gives a positive time-averaged pressure-heterogeneity floor.

---

## 8. Conditional averaged pressure-heterogeneity floor

Suppose the retained M5 crossing population lies on closed regular zero components with uniform

\[
|F_{qq}|\le C_F,
\qquad
\nu_\Gamma(\Gamma)\le L_\Gamma.
\]

Let

\[
A_O(\theta)
=\int\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma.
\]

Section 7 gives a positive lower bound on `overline A_O`.
By Jensen,

\[
\overline{A_O^2}
\ge(\overline A_O)^2.
\]

Hence

\[
\boxed{
\overline{V_H}
\ge
\frac{625}{C_F^2L_\Gamma}
\left(
\frac{\beta^2}{C_wR_2}
\right)^2
>0.
}
\]

Thus, on this fully regular conditional branch, M5 hysteresis forces recurrent nonzero spatial variance of the global axial pressure coordinate along the semilinear zero loop.

---

## 9. What this does and does not close

This is stronger than a sign covariance:

\[
\boxed{
\text{M5 hysteresis}
\Longrightarrow
\text{positive octupole-square crossing mass}
\Longrightarrow
\text{positive pressure heterogeneity}
}
\]

under the stated pushforward/closed-loop compactness assumptions.

However a recurrent smooth flow can in principle maintain positive spatial variance indefinitely.
No temporal dissipation or nonrecyclable turnover cost follows solely from `V_H>0`.

Therefore the next missing bridge is to the **pressure transport law**

\[
D_BH_V=\Pi_V^{prod}+\Pi_V^{rel}.
\]

One must determine whether maintaining the forced zero-loop pressure variance requires a positive production/relative-transport action that can be bounded by an existing global budget.

---

## 10. DSD audit

### Audit A — claiming `F_qq` has fixed sign on a closed zero loop
Rejected. Its normal component has zero signed integral and generically changes sign.

### Audit B — converting strict M5 linear bias directly to pointwise `O_V^2>0`
Rejected. The correct statement is an integrated Cauchy--Schwarz lower bound.

### Audit C — dropping the pushforward density
Only allowed under the explicit bounded-density comparability branch of M17-172.

### Audit D — treating positive pressure variance as contradiction
Rejected. It is a recurrent spatial occupancy requirement.

### Audit E — proof status
A coercive pressure heterogeneity floor is derived conditionally; global regularity remains open.

---

## 11. Updated Rank-1 pressure frontier

On the conditional closed-loop bounded-density branch, the M5 hysteresis no longer ends at an abstract covariance firewall. It forces

\[
\boxed{
\overline{
\int_\Gamma(H_V-\bar H_\Gamma)^2
\frac{ds}{|\nabla\kappa|}
}>0.
}
\]

The next gate is a **pressure-variance maintenance cost**: combine the material transport of `H_V` with motion/deformation of the zero-loop measure to compute the evolution of this variance and identify the exact production, relative-transport, and loop-motion terms required to sustain it.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
