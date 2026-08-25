# DSD Cauchy-Geometric Replacement Critical Saturation

Date: 2026-08-25

Status: **CAUCHY VARIABLE REMOVES STRAIN FROM MATERIAL IDENTITY / HIGH-AMPLITUDE RECRUITMENT SPLIT INTO VISCOUS DEFECT OR q^k DEFORMATION / INCOMPRESSIBILITY FORCES q^{-k/2} TRANSVERSE COMPRESSION / THIS MATCHES THE CURRENT FIRST-HITTING ANALYTIC SCALE EXACTLY / NO EXPONENT SLACK / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose and correction

`DSD_MATERIAL_MEAN_DIFFUSION_EROSION_QUADRATIC_CHARGE_2026-08-25.md` introduced a vorticity-weighted compressive exposure `C` when tracking the physical amplitude `|omega|` on a material packet.

That is a valid physical-amplitude decomposition, but it must not be interpreted as direct loss of material vorticity identity.

The repository already contains the exact Cauchy-vorticity variable

\[
\boxed{
\zeta(a,t)=F(a,t)^{-1}\omega(X(a,t),t),
}
\]

where

\[
F=D_aX,
\qquad
\det F=1.
\]

It satisfies

\[
\boxed{
\partial_t\zeta
=\nu F^{-1}\Delta\omega(X,t).
}
\]

Thus inviscid stretching, rotation, and compression are absorbed exactly into `F`; only viscosity changes the Cauchy material state.

This note retypes the replacement branch accordingly.

---

## 2. Exact Cauchy representation from ancestor stage n

Restart the flow at the ancestor first-hitting time `t_n` so that

\[
F(a,t_n)=I.
\]

Then

\[
\boxed{
\zeta(a,t)
=
\omega(a,t_n)
+\delta\zeta(a,t),
}
\]

with

\[
\boxed{
\delta\zeta(a,t)
:=
\nu\int_{t_n}^{t}
F(a,s)^{-1}\Delta\omega(X(a,s),s)ds.
}
\]

The physical vorticity is

\[
\boxed{
\omega(X(a,t),t)
=F(a,t)
\left[
\omega(a,t_n)+\delta\zeta(a,t)
\right].
}
\]

Because `W_n` is a first-hitting running maximum,

\[
\boxed{|
\omega(a,t_n)|\le W_n
\quad\text{for every material label }a.}
\]

---

## 3. High-amplitude recruited label dichotomy

Let the descendant witness lie in stage

\[
j=n+k
\]

so

\[
W_j=q^kW_n.
\]

Consider a material label outside the designated ancestor packet that belongs at the witness time to a thresholded current high-vorticity population satisfying

\[
\boxed{
|\omega(X(a,t),t)|
\ge
\theta W_j
=
\theta q^kW_n,
}
\]

for some fixed `theta>0`.

Choose

\[
\eta:=\theta/2.
\]

Suppose first that the endpoint deformation satisfies

\[
\|F(a,t)\|_{op}
<\eta q^k.
\]

Then

\[
\begin{aligned}
\theta q^kW_n
&\le
|\omega(X(a,t),t)|\\
&\le
\eta q^k
\left(W_n+|\delta\zeta(a,t)|\right).
\end{aligned}
\]

Dividing by `eta q^k` and using `theta/eta=2` gives

\[
2W_n
<
W_n+|\delta\zeta|.
\]

Hence

\[
\boxed{|
\delta\zeta(a,t)|>W_n.}
\]

Therefore every thresholded recruited label satisfies the exact finite alternative

\[
\boxed{
\|F(a,t)\|_{op}
\ge
\frac\theta2q^k
\quad\lor\quad
|\delta\zeta(a,t)|>W_n.
}
\]

Call these respectively

- `G_k`: critical geometric recruitment;
- `V_k`: order-one ancestor-scale viscous Cauchy defect.

Status: **PROVED.**

---

## 4. Interpretation of V_k

The `V_k` branch is genuine material-state alteration.

The exact Duhamel identity gives

\[
\delta\zeta
=
\nu\int F^{-1}\Delta\omega\,dt.
\]

Hence a positive-volume `V_k` population is precisely the Cauchy-vorticity turnover object already treated in

`notes/2026-08-13-cauchy-vorticity-material-turnover.md`.

Under a bounded-deformation window, its `L2` size forces a second-vorticity-derivative spacetime cost.

The new material-mean diffusion note supplies a complementary estimate that avoids pointwise recruitment and charges loss of an entire ancestor population directly by global hyperpalinstrophy.

Thus `V_k` is not a new independent mechanism.

---

## 5. Geometry forced by G_k

On the geometric branch let the singular values of `F(a,t)` be

\[
s_1\ge s_2\ge s_3>0.
\]

Incompressibility gives

\[
\boxed{s_1s_2s_3=1.}
\]

Since

\[
s_1=\|F\|_{op}
\ge
\frac\theta2q^k,
\]

we necessarily have

\[
s_3^2s_1
\le
s_1s_2s_3=1
\]

because `s_2>=s_3`.

Therefore

\[
\boxed{
s_3
\le
s_1^{-1/2}
\le
\left(\frac2\theta\right)^{1/2}
q^{-k/2}.
}
\]

Thus order-`q^k` material amplification forces at least one transverse compression direction of order

\[
\boxed{q^{-k/2}.}
\]

Status: **PROVED.**

---

## 6. The transverse compression scale matches the current natural radius

The ancestor radius is

\[
r_n=\sqrt{\frac\nu{W_n}}.
\]

The current descendant radius is

\[
r_j=\sqrt{\frac\nu{W_j}}
=q^{-k/2}r_n.
\]

Therefore the compressed image of one ancestor-scale transverse length obeys

\[
\boxed{
s_3r_n
\lesssim
r_j}
\]

up to the fixed factor `(2/theta)^(1/2)`.

This is the crucial saturation identity:

\[
\boxed{
q^k\text{ vorticity amplification}
\quad+\quad
\det F=1
\quad\Longrightarrow\quad
\text{transverse scale }q^{-k/2}r_n
=r_j.
}
\]

The geometric recruitment branch therefore compresses exactly to the natural first-hitting/analytic scale of the descendant stage, not automatically below it.

Status: **PROVED.**

---

## 7. No immediate analyticity contradiction

Stage-`j` analyticity naturally resolves spatial scales comparable to

\[
r_j.
\]

The preceding deformation estimate only forces a transverse scale comparable to `r_j`.

Hence one may not claim

\[
\text{large material deformation}
\Longrightarrow
\text{sub-analytic filament}
\Longrightarrow
\text{contradiction}.
\]

There is no spare exponent.

The extremal model

\[
(s_1,s_2,s_3)
\sim
(q^k,q^{-k/2},q^{-k/2})
\]

has determinant one and lands exactly on the descendant parabolic scale.

This is the material version of the same scale-critical tightrope seen in the `1/R` velocity / `1/R^2` vorticity tail.

---

## 8. Deformation-time requirement

For every material vector,

\[
\frac{d}{dt}|Fv|
\le
\|\nabla u\|_{op}|Fv|.
\]

Therefore

\[
\log\|F(a,t)\|_{op}
\le
\int_{t_n}^{t}\|\nabla u(X(a,s),s)\|_{op}ds
\]

up to the standard operator-norm propagation estimate.

On `G_k`,

\[
\boxed{
\int_{t_n}^{t}\|\nabla u(X(a,s),s)\|_{op}ds
\ge
k\log q+\log(\theta/2).
}
\]

Thus geometric recruitment requires an amount of integrated deformation linear in shell age.

The existing stage-wide ceiling gives only

\[
\int_{t_n}^{t}\|\nabla u\|_\infty ds
\le
A_{st}(k+1)L_+,
\]

so an explicit sufficient exclusion condition would be

\[
\boxed{
A_{st}(k+1)L_+
<
k\log q+\log(\theta/2).
}
\]

Asymptotically a constant-slope sufficient gate is

\[
\boxed{A_{st}L_+<\log q.}
\]

This inequality is not presently verified and should not be assumed.

Status: **PROVED SUFFICIENT CONSTANT GATE / NOT CLOSED.**

---

## 9. Relation to first-hitting maximum stretching

The repository already proves that nonzero recurrent first-hitting/Leray dynamics must have positive-density source-active stretching, and routes it into

\[
\text{positive-middle geometry}
\quad\lor\quad
T/H/\text{Betchov residual}.
\]

Therefore the deformation required by `G_k` is not an untyped scalar amplification mechanism.

When it recurrently feeds the active core it must be reconciled with the existing positive-middle / Betchov / projective-turnover ledgers.

What remains missing is a theorem transferring the labelwise lower bound

\[
\log\|F\|\gtrsim k\log q
\]

for a replacement population into one of those **spatially integrated recurrent action** thresholds without losing the critical scaling.

---

## 10. Critical scaling audit of material transport

The time from ancestor stage `n` to the singular time satisfies

\[
T^*-t_n\asymp W_n^{-1}
\asymp r_n^2/\nu.
\]

A material displacement of order `r_n` over this interval requires velocity scale

\[
\frac{r_n}{r_n^2/\nu}
=\frac\nu{r_n},
\]

which is exactly the natural Navier--Stokes velocity scale associated with vorticity `W_n`.

Thus all three material scales saturate simultaneously:

\[
\boxed{
\begin{aligned}
\text{length}&\sim r_n,\\
\text{time}&\sim r_n^2/\nu,\\
\text{velocity}&\sim\nu/r_n.
\end{aligned}
}
\]

There is no supercritical transport speed forced merely by replacement.

---

## 11. Updated turnover typing

The physically observed compression branch from the material-mean amplitude calculation should therefore be typed as **geometric deformation**, not as Cauchy material-identity destruction.

The rigorous replacement tree is

\[
\boxed{
T_{replacement}
\Longrightarrow
V_{Cauchy}
\lor
G_{critical\ deformation}.
}
\]

The first is viscous/derivative and already has second-vorticity-derivative costs.

The second is an exactly scale-critical deformation branch whose natural transverse scale equals `r_j`.

This explains why previous attempts to remove T solely through analyticity or ordinary energy repeatedly saturated rather than contradicted the equations.

---

## 12. DSD audit

The following objects remain distinct:

- physical vorticity amplitude `omega`;
- material Cauchy state `zeta`;
- deformation gradient `F`;
- viscous Cauchy defect `delta zeta`;
- high-amplitude recruitment;
- transverse geometric compression.

Compression of `omega` is not identified with destruction of `zeta`.

The calculation preserves that distinction explicitly.

---

## 13. Updated frontier

After the material-mean diffusion improvement and the Cauchy correction, the turnover frontier is

\[
\boxed{
\text{viscous material alteration}
\quad\lor\quad
\text{critical geometric deformation/recruitment}.
}
\]

The viscous side is increasingly well quantified.

The difficult survivor is now the critical geometric branch

\[
\boxed{
\|F\|\sim q^k,
\qquad
s_{min}(F)\sim q^{-k/2},
}
\]

which sits exactly at the descendant analytic radius.

The next efficient calculation is therefore not another derivative estimate. It is to combine this critical deformation geometry with the existing recurrent positive-middle/Betchov action ledger and ask whether **positive-density replacement of a nontrivial label population** forces a nonzero integrated projective/strain action per logarithmic generation.

---

## 14. Audit verdict

### PROVED

- Cauchy material identity changes only by viscosity;
- high-amplitude recruitment is either large Cauchy viscous defect or `q^k` geometric deformation;
- `q^k` deformation plus incompressibility forces `q^{-k/2}` transverse compression;
- that transverse scale equals the descendant first-hitting scale `r_j`;
- ordinary analyticity therefore gives no immediate contradiction;
- geometric recruitment requires integrated deformation at least `k log q + O(1)`;
- the entire replacement kinematics is parabolically scale critical.

### NOT DERIVED

- a spatially integrated action lower bound from the labelwise critical deformation;
- a contradiction from the constant gate `A_st L_+ < log q`;
- closure of recurrent critical geometric replacement;
- closure of escaping critical tail topology;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
