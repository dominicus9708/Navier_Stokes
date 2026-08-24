# Local-Energy Flux Amplitude Genealogy Gate — 2026-08-24

## Status

**NEW CALCULATION — RIGOROUS CONDITIONAL GATE, NOT GLOBAL CLOSURE.**

Purpose: connect physical-scale local-energy change to a forced historical annular velocity amplitude, while explicitly auditing pressure tails and Galilean drift.

Throughout, let a smooth finite-energy solution satisfy

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0
\]

on a pre-singular time interval.

---

## 1. Local-energy identity at scale `R`

Fix `x_0` and a cutoff

\[
\phi_R(x)=\phi\!\left(\frac{x-x_0}{R}\right),
\]

with

\[
0\le \phi\le1,
\qquad
\phi=1\text{ on }B_1,
\qquad
\operatorname{supp}\phi\subset B_2,
\]

and

\[
|\nabla\phi_R|\le C R^{-1},
\qquad
|\Delta\phi_R|\le C R^{-2}.
\]

Define

\[
E_R(t)=\frac12\int |u(x,t)|^2\phi_R(x)\,dx.
\]

The exact smooth local-energy identity is

\[
\frac{d}{dt}E_R(t)
+\nu\int |\nabla u|^2\phi_R\,dx
=
\frac{\nu}{2}\int |u|^2\Delta\phi_R\,dx
+F_R(t),
\]

where

\[
F_R(t)=
\int
\left(\frac{|u|^2}{2}+p\right)
 u\cdot\nabla\phi_R\,dx.
\]

This is the exact scale-`R` energy-transfer ledger.

---

## 2. Velocity part of the flux

Let

\[
A_R=\{x:R<|x-x_0|<2R\},
\qquad
a_R(t)=\|u(t)\|_{L^3(A_R)}.
\]

Because `\nabla\phi_R` is supported in `A_R`,

\[
|F_R^{\rm vel}(t)|
\le
C R^{-1}\int_{A_R}|u|^3dx
=
C R^{-1}a_R(t)^3.
\]

Hence

\[
\boxed{
|F_R^{\rm vel}|
\le C R^{-1}a_R^3.
}
\]

Status: **PROVED.**

---

## 3. Pressure split

Choose a smooth spatial cutoff equal to one on `B_{4R}(x_0)` and split, modulo an irrelevant pressure constant,

\[
p=p_{\rm near}+p_{\rm far},
\]

with

\[
p_{\rm near}
=\mathcal R_i\mathcal R_j
\big(\chi_{4R}u_i u_j\big),
\]

and the complementary source assigned to `p_far`.

Define

\[
b_R(t)=\|u(t)\|_{L^3(B_{4R}(x_0))}.
\]

Calderon-Zygmund boundedness gives

\[
\|p_{\rm near}\|_{L^{3/2}}
\le C b_R^2.
\]

Therefore

\[
\left|
\int p_{\rm near}u\cdot\nabla\phi_Rdx
\right|
\le
C R^{-1}b_R^2a_R.
\]

Thus

\[
\boxed{
|F_R^{p,{\rm near}}|
\le C R^{-1}b_R^2a_R.
}
\]

Status: **PROVED.**

---

## 4. Far-pressure oscillation

For the pressure kernel `K`,

\[
|\nabla K(z)|\le C|z|^{-4}.
\]

For `x\in B_{2R}(x_0)` and far sources `|y-x_0|>4R`, subtract the constant

\[
c_R(t)=p_{\rm far}(x_0,t).
\]

The mean-value estimate gives

\[
|p_{\rm far}(x,t)-c_R(t)|
\le
C R
\int_{|y-x_0|>4R}
\frac{|u(y,t)|^2}{|y-x_0|^4}\,dy.
\]

Define the weighted pressure tail

\[
T_R(t)=
\int_{|y-x_0|>4R}
\frac{|u(y,t)|^2}{|y-x_0|^4}\,dy.
\]

Then

\[
|p_{\rm far}-c_R|
\le C R T_R.
\]

The constant contributes nothing because

\[
\int c_R u\cdot\nabla\phi_Rdx
=-c_R\int \phi_R\nabla\cdot u\,dx
=0.
\]

Also

\[
\|u\|_{L^1(A_R)}
\le C R^2 a_R.
\]

Hence

\[
\boxed{
|F_R^{p,{\rm far}}|
\le C R^2 T_R a_R
= C R^{-1}a_R\,(R^3T_R).
}
\]

Status: **PROVED.**

---

## 5. Factorized scale-`R` flux bound

Set

\[
\mathcal K_R(t)
:=a_R(t)^2+b_R(t)^2+R^3T_R(t).
\]

Combining the three pieces,

\[
\boxed{
|F_R(t)|
\le
C R^{-1}a_R(t)\,\mathcal K_R(t).
}
\]

This factorization is the main new estimate in this note.

Under Navier-Stokes scaling,

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

`a_R`, `b_R`, and `R^3T_R` have the required critical scaling, and the right-hand side has the same scaling as an instantaneous local-energy flux.

Status: **PROVED; scaling checked.**

---

## 6. Integrated crossing lemma

For `I=[t_1,t_2]`, define

\[
D_R(I)=
\nu\int_I\int |\nabla u|^2\phi_R\,dxdt,
\]

and

\[
H_R(I)=
\frac{\nu}{2}
\int_I\int |u|^2\Delta\phi_R\,dxdt.
\]

Integration gives

\[
E_R(t_2)-E_R(t_1)+D_R(I)-H_R(I)
=
\int_I F_R(t)dt.
\]

Assume a genuine scale-`R` transfer crossing:

\[
\boxed{
\left|
E_R(t_2)-E_R(t_1)+D_R(I)-H_R(I)
\right|
\ge \varepsilon\nu^2R.
}
\]

Assume also

\[
\sup_{t\in I}\mathcal K_R(t)
\le M\nu^2
\]

and a parabolic-length interval

\[
|I|\le \theta\frac{R^2}{\nu}.
\]

Then

\[
\varepsilon\nu^2R
\le
C R^{-1}M\nu^2
\int_I a_R(t)dt,
\]

so

\[
\int_I a_R(t)dt
\ge
c\frac{\varepsilon}{M}R^2.
\]

Consequently

\[
\boxed{
\sup_{t\in I}\frac{a_R(t)}{\nu}
\ge
c\frac{\varepsilon}{\theta M}.
}
\]

Thus a nontrivial local-energy crossing on a parabolic interval, together with a bounded critical flux bracket, forces a historical annular `L^3` velocity ancestor of scale-invariant size.

Status: **PROVED CONDITIONAL ON THE CROSSING AND BRACKET HYPOTHESES.**

---

## 7. Important Galilean audit: this does not yet force gradient amplitude

The current amplitude-genealogy front uses gradient-shell cost of the form

\[
J_R^{\rm phys}
=R\int_{B_{4R}}|\nabla u|^2dx.
\]

The crossing lemma above forces an **absolute** annular `L^3` amplitude `a_R`. Absolute amplitude can contain almost-rigid drift and therefore does not by itself imply a lower bound for `J_R^{phys}`.

For a relative fluctuation, however, Poincare-Sobolev gives

\[
\left\|u-u_{B_{4R}}
\right\|_{L^3(B_{4R})}
\le
C R^{1/2}
\|\nabla u\|_{L^2(B_{4R})},
\]

that is,

\[
\boxed{
\left\|u-u_{B_{4R}}
\right\|_{L^3(B_{4R})}^2
\le
C J_R^{\rm phys}.
}
\]

Therefore a **relative/Galilean-invariant** forced `L^3` amplitude would feed directly into the gradient-shell genealogy, while the absolute amplitude obtained above does not yet do so.

This is a real remaining gate, not a cosmetic issue.

---

## 8. Audit table

| Statement | Status |
|---|---|
| Exact local-energy identity before the hypothetical singular time | **PROVED** |
| Velocity cubic flux bound | **PROVED** |
| Near-pressure Calderon-Zygmund bound | **PROVED** |
| Far-pressure weighted oscillation bound | **PROVED** |
| Factorized flux estimate `|F_R| <= C R^{-1} a_R K_R` | **PROVED** |
| Nontrivial crossing + bounded bracket => historical absolute annular `L^3` amplitude | **PROVED CONDITIONAL** |
| Absolute annular `L^3` amplitude => gradient-shell lower bound | **FALSE IN GENERAL / DRIFT OBSTRUCTION** |
| Relative annular `L^3` amplitude => gradient-shell lower bound | **PROVED BY POINCARE-SOBOLEV** |
| Present core concentration automatically supplies the required crossing lower bound | **NOT DERIVED** |
| The estimate alone proves global regularity | **FALSE** |

---

## 9. New frontier produced by this calculation

The genealogy problem has been sharpened from

\[
\text{current concentration}
\stackrel{?}{\Longrightarrow}
\text{historical shell amplitude}
\]

to two explicit missing gates:

\[
\boxed{
\text{current distinguished-scale concentration}
\stackrel{?}{\Longrightarrow}
\text{nontrivial local-energy crossing}
}
\]

and

\[
\boxed{
\text{absolute crossing amplitude}
\stackrel{?}{\Longrightarrow}
\text{relative/Galilean amplitude}
\Longrightarrow
J_R^{\rm phys}>0.
}
\]

The second arrow on the last line is already controlled by Poincare-Sobolev; the first two arrows remain the active analytical bottlenecks.

This separates a genuine PDE transport problem from a drift artifact and gives the next calculation a precise target.