# DSD Fixed-Lag Exposure Uniform Bound

Date: 2026-08-25

Status: **FIXED-LAG DEFORMATION EXPOSURE UNIFORMLY BOUNDED / FIXED-LAG DIFFUSION EXPOSURE UNIFORMLY BOUNDED / EXPLICIT MATERIAL-RETENTION CONSTANT TEST DERIVED / NUMERICAL CLOSURE NOT ESTABLISHED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`DSD_FIXED_LAG_PACKET_IDENTITY_REPLACEMENT_GATE_2026-08-25.md` reduced the positive-density recurrent remote-witness branch to

\[
E\lor R\lor T_{multi},
\]

where `E` meant failure of quiet material transport over one fixed finite generation lag `k_0`.

Because `k_0` is fixed, the stage-wide analyticity and bounded-Z corridor can be used to test whether the deformation part of `E` is actually an unbounded escape.

The answer is no: deformation and every fixed-order diffusion exposure have finite universal upper bounds over the fixed lag.

The remaining issue is whether the diffusion upper bound is small enough to guarantee material amplitude retention.

---

## 2. Stage-wide analytic constants

For every sufficiently late first-hitting stage `m`, use the parent normalization

\[
\Omega_m=\frac{\omega}{W_m},
\qquad
U_m=\frac{r_m}{\nu}u,
\qquad
r_m=\sqrt{\frac\nu{W_m}}.
\]

The stage-wide restart argument gives fixed constants

\[
\boxed{
\|\nabla\Omega_m\|_\infty\le C_{1,an},
\qquad
\|\Delta\Omega_m\|_\infty\le C_{2,an},
}
\]

uniformly throughout the stage.

The endpoint bounded-Z branch and the in-stage enstrophy amplification estimate give

\[
\boxed{
\widetilde Z_m(t)
\le
Z_{st}:=
Z_*\exp\left(\frac{2L_+}{\sqrt3}\right).
}
\]

---

## 3. Uniform normalized velocity-gradient ceiling

The endpoint-Riesz-safe strain interpolation gives

\[
\|\Sigma_m\|_\infty
\le
C_I
\|\nabla\Omega_m\|_\infty^{3/5}
\|\Omega_m\|_2^{2/5}.
\]

Hence

\[
\boxed{
\|\Sigma_m\|_\infty
\le
B_{st}:=
C_I C_{1,an}^{3/5}Z_{st}^{1/5}.
}
\]

The antisymmetric part of `grad U_m` is algebraically controlled by vorticity.

Inside stage `m`,

\[
\|\Omega_m\|_\infty
\le q,
\]

so for a fixed algebraic constant `C_A`,

\[
\boxed{
\|\nabla U_m\|_\infty
\le
A_{st}:=B_{st}+C_Aq<\infty.
}
\]

No endpoint Riesz transform on `L^infinity` is used; the strain term is controlled by the near/far interpolation already audited in the repository.

Status: **PROVED on the bounded-Z stage-wide analytic corridor.**

---

## 4. Physical gradient scaling

Because

\[
U_m(y,t)=\frac{r_m}{\nu}u(x,t),
\]

we have

\[
\nabla_yU_m
=
\frac{r_m^2}{\nu}\nabla_xu
=
\frac1{W_m}\nabla_xu.
\]

Therefore

\[
\boxed{
\|\nabla_xu(t)\|_\infty
\le
A_{st}W_m
}
\]

throughout stage `m`.

The physical strain obeys the same upper bound up to the smaller symmetric part:

\[
\|S(t)\|_\infty
\le A_{st}W_m.
\]

---

## 5. Fixed-lag deformation exposure is automatically finite

Let

\[
n=j-k_0
\]

and let `t` be any witness time in stage `j`.

The interval `[t_n,t]` crosses at most `k_0+1` complete/partial stages.

For each stage `m`,

\[
W_m(t_{m+1}-t_m)
\le L_+.
\]

Hence

\[
\begin{aligned}
\int_{t_n}^{t}\|\nabla u(s)\|_\infty ds
&\le
A_{st}
\sum_{m=n}^{j}
W_m|I_m\cap[t_n,t]|\\
&\le
A_{st}(k_0+1)L_+.
\end{aligned}
\]

Thus every local tube exposure is bounded by the same global quantity:

\[
\boxed{
\Lambda_n([t_n,t])
\le
L_{fix}:=
A_{st}(k_0+1)L_+.
}
\]

Likewise

\[
\boxed{
\Sigma_n([t_n,t])
\le L_{fix}.
}
\]

Therefore the fixed-lag E branch cannot survive as arbitrarily large strain or tube deformation on the bounded-Z analytic corridor.

Status: **PROVED.**

---

## 6. Fixed-lag vorticity-Laplacian exposure is also finite

From

\[
\Omega_m=\frac\omega{W_m},
\qquad
y=\frac{x-X_m}{r_m},
\]

we obtain

\[
\Delta_y\Omega_m
=
\frac{r_m^2}{W_m}\Delta_x\omega
=
\frac\nu{W_m^2}\Delta_x\omega.
\]

Therefore

\[
\boxed{
\|\Delta_x\omega\|_\infty
\le
C_{2,an}\frac{W_m^2}{\nu}.
}
\]

Recall the ancestor-normalized material diffusion exposure

\[
\mathcal D_n([t_n,t])
=
\frac\nu{W_n}
\int_{t_n}^{t}
\sup_{A_n(s)}|\Delta\omega|ds.
\]

Using the global pointwise upper bound,

\[
\begin{aligned}
\mathcal D_n
&\le
\frac{C_{2,an}}{W_n}
\sum_{m=n}^{j}
W_m^2|I_m\cap[t_n,t]|\\
&\le
C_{2,an}L_+
\sum_{h=0}^{k_0}q^h.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal D_n
\le
D_{fix}:=
C_{2,an}L_+
\frac{q^{k_0+1}-1}{q-1}.
}
\]

Thus the diffusion channel is a finite fixed-lag constant problem, not an unbounded derivative escalation.

Status: **PROVED.**

---

## 7. Explicit sufficient material-retention test

The amplitude-location genealogy bridge shows that the ancestor packet retains at least half of its analytic-core amplitude if

\[
\mathcal D_n
\le
\frac{b_0}{2}e^{-L}
\]

while the strain/tube exposure is at most `L`.

Use the universal fixed-lag choice

\[
L=L_{fix}.
\]

A sufficient condition for every fixed-lag ancestor packet to remain coherent is therefore

\[
\boxed{
D_{fix}
<
\frac{b_0}{2}e^{-L_{fix}}.
}
\]

Substituting the explicit bounds,

\[
\boxed{
C_{2,an}L_+
\frac{q^{k_0+1}-1}{q-1}
<
\frac{b_0}{2}
\exp\left[-A_{st}(k_0+1)L_+\right].
}
\]

Call this the **Fixed-Lag Material Retention Constant Test (FMRCT)**.

If FMRCT holds, the E branch is removed completely and FPIRG reduces to

\[
\boxed{R\lor T_{multi}.}
\]

Status: **PROVED SUFFICIENT CONDITION.**

---

## 8. If FMRCT does not close numerically

Failure to verify FMRCT does not prove that material retention fails.

It means only that the current universal analyticity constants are too coarse to guarantee

\[
\mathcal D_n<\frac{b_0}{2}e^{-L_{fix}}.
\]

The actual event-wise alternatives remain

\[
\boxed{
\mathcal D_n
\le
\frac{b_0}{2}e^{-L_{fix}}
\quad\Longrightarrow\quad
R\lor T_{multi},
}
\]

or

\[
\boxed{
\mathcal D_n
>
\frac{b_0}{2}e^{-L_{fix}}.
}
\]

Thus the unresolved E branch has been sharpened to a single finite fixed-order diffusion-erosion threshold.

There is no longer an independent fixed-lag unbounded-strain or unbounded-tube-deformation escape on this corridor.

---

## 9. Scope correction concerning the cubic return-density ledger

The fixed shell `k_0` extracted from recurrent remote-witness time averaging must not be confused with the unbounded tail label `k -> infinity` in

\[
\sum_kJ_k^{3/2}=\infty.
\]

A positive return density for one fixed recurrent shell does not by itself imply

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

on the entire cubic-divergent tail.

Therefore FMRCT and FPIRG advance the recurrent-core genealogy problem, but they do not by themselves close the non-L3 cubic genealogy deficit ledger.

This distinction is mandatory for the audit.

---

## 10. DSD audit

The following finite constants are formed separately:

- stage analytic derivative ceilings `C_1,an`, `C_2,an`;
- in-stage enstrophy ceiling `Z_st`;
- normalized velocity-gradient ceiling `A_st`;
- fixed-lag deformation ceiling `L_fix`;
- fixed-lag diffusion ceiling `D_fix`;
- analytic-core initial amplitude `b_0`.

FMRCT compares these formed values; it does not identify them as one channel.

---

## 11. Updated frontier

On the bounded-Z recurrent branch, the fixed-lag Eulerian-to-material gate is now

\[
\boxed{
\text{fixed-age coherent Eulerian packet}
\Longrightarrow
D_{erosion}\lor R\lor T_{multi},
}
\]

where `D_erosion` is a finite explicit second-vorticity-derivative exposure threshold.

If FMRCT closes, this becomes simply

\[
\boxed{R\lor T_{multi}.}
\]

The next quantitative task is to sharpen/extract the analyticity constants enough to test FMRCT, or else to charge repeated diffusion-erosion events by a spacetime derivative budget.

---

## 12. Audit verdict

### PROVED

- stage-wide fixed-order analytic bounds;
- uniform bounded-Z normalized strain/velocity-gradient ceiling;
- fixed-lag strain and tube deformation exposure upper bound;
- fixed-lag vorticity-Laplacian exposure upper bound;
- FMRCT as an explicit sufficient material-retention criterion;
- deformation is no longer an unbounded fixed-lag escape.

### NOT DERIVED

- numerical truth of FMRCT with the currently inherited non-explicit analyticity constants;
- a global spacetime budget excluding repeated diffusion-erosion events if FMRCT fails;
- scale-uniform return lower bounds for the full `k -> infinity` cubic tail;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
