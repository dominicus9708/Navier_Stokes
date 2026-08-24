# Parabolic Time Cost and Cascade Multiplicity–Dwell Audit

Date: 2026-08-25

## 1. Scope

This note audits the remaining high-derivative concentration escape branch by attaching a time cost to each spatial concentration scale.

We normalize viscosity to

\[
\nu=1.
\]

The Navier–Stokes scaling used below is \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\).

Global regularity is not claimed.

---

## 2. Critical single-core scaling

At radius \(r\), critical scaling gives

\[
|u|\sim r^{-1},\qquad
|\omega|\sim |\nabla u|\sim r^{-2},\qquad
|\nabla^m u|\sim r^{-(m+1)}.
\]

The natural parabolic dwell time is

\[
\tau_r\sim r^2.
\]

For one active ball,

\[
\int_{B_r}|\nabla u|^2dx
\sim r^{-4}r^3
=r^{-1}.
\]

Hence one parabolic epoch contributes only

\[
\int_{I_r}\int_{B_r}|\nabla u|^2dxdt
\sim r^{-1}r^2
=r
\]

to the common Leray dissipation ledger.

**Status: PROVED / scaling.**

---

## 3. A one-core geometric cascade is not excluded by the energy ledger

Let

\[
r_k=\lambda^kR,\qquad 0<\lambda<1.
\]

The scale-model ordinary dissipation charge for one critical core and one parabolic epoch at each scale is

\[
D_k\asymp r_k.
\]

Therefore

\[
\sum_kD_k\asymp\sum_kr_k=\frac{R}{1-\lambda}<\infty.
\]

This does not construct such a cascade. It proves only that the finite Leray ledger cannot exclude it by the naive argument “infinitely many scales imply infinite dissipation.”

\[
\boxed{
\text{single nested geometric cascade is not ruled out by this ledger alone.}
}
\]

**Status: PROVED as a budget audit; existence NOT asserted.**

---

## 4. Palinstrophy is expensive but is not an available finite common ledger

Critical scaling also gives

\[
|\nabla\omega|\sim r^{-3},
\]

so

\[
\int_{B_r}|\nabla\omega|^2dx\sim r^{-3},
\]

and over a parabolic epoch

\[
\int_{I_r}\int_{B_r}|\nabla\omega|^2dxdt\sim r^{-1}.
\]

For geometric \(r_k\), \(\sum_kr_k^{-1}\) diverges. However finite-energy Leray theory supplies a common finite budget for

\[
\int_0^T\|\nabla u\|_2^2dt,
\]

not an a priori finite budget for

\[
\int_0^T\|\nabla\omega\|_2^2dt
\]

through a hypothetical first singular time. Treating the latter as already finite would import extra regularity.

\[
\boxed{
\text{palinstrophy divergence is informative, but not yet a contradiction.}
}
\]

---

## 5. Higher derivative ledgers cannot be summed across derivative order

For \(m\ge0\),

\[
E_m(r):=\int_{B_r}|\nabla^m u|^2dx\sim r^{1-2m}.
\]

The next-derivative dissipation over one parabolic epoch obeys the same scaling:

\[
D_m(r)
:=\int_{I_r}\int_{B_r}|\nabla^{m+1}u|^2dxdt
\sim r^{1-2m}.
\]

Thus parabolic time does not introduce an additional derivative-order contradiction.

In particular,

\[
D_0+D_1+D_2+\cdots
\]

cannot be treated as withdrawals from one finite conserved/dissipative quantity. These are different derivative-energy ledgers. Only the ordinary \(D_0\) ledger is available from finite energy without importing stronger regularity.

Therefore

\[
\text{high derivative escape at all orders}
\Rightarrow
\sum_mD_m=\infty
\Rightarrow
\text{contradiction}
\]

is **INVALID / CIRCULAR** under the present hypotheses.

---

## 6. General multiplicity–dwell gate

Let

\[
E_0:=\frac12\|u_0\|_2^2.
\]

For each \(k\), suppose there are \(N_k\) spatially disjoint active balls of radius \(r_k\) throughout a time interval \(I_k\), and assume

\[
\int_{B_{r_k}(x_{k,j})}|\nabla u(x,t)|^2dx
\ge \frac{\alpha}{r_k}
\]

for every active ball and every \(t\in I_k\), with fixed \(\alpha>0\).

Let

\[
\tau_k:=|I_k|.
\]

Assume the collection of intervals \(I_k\) has time-overlap multiplicity at most \(Q<\infty\).

Spatial disjointness gives

\[
\|\nabla u(t)\|_2^2\ge\frac{\alpha N_k}{r_k}
\]

on \(I_k\). Therefore

\[
\int_{I_k}\|\nabla u(t)\|_2^2dt
\ge
\alpha N_k\frac{\tau_k}{r_k}.
\]

Summing and using time-overlap multiplicity \(Q\),

\[
\alpha\sum_kN_k\frac{\tau_k}{r_k}
\le
Q\int_0^T\|\nabla u(t)\|_2^2dt
\le QE_0.
\]

Hence

\[
\boxed{
\sum_kN_k\frac{\tau_k}{r_k}
\le
\frac{QE_0}{\alpha}<\infty.
}
\]

This is the general multiplicity–dwell gate.

**Status: PROVED CONDITIONAL on the stated spatial disjointness, lower amplitude, and bounded time-overlap hypotheses.**

---

## 7. Parabolic-dwell corollary

If additionally

\[
\tau_k\ge\theta r_k^2
\]

with fixed \(\theta>0\), then

\[
\boxed{
\sum_kN_kr_k
\le
\frac{QE_0}{\alpha\theta}<\infty.
}
\]

Consequences:

- \(N_k=1\), \(r_k=\lambda^kR\): not excluded, because \(\sum r_k<\infty\).
- If \(N_k\gtrsim r_k^{-1}\) on infinitely many bounded-overlap parabolic epochs, then \(N_kr_k\gtrsim1\), so the gate is violated.
- More generally, any mechanism forcing \(\sum_kN_kr_k=\infty\) excludes that cascade geometry.

Recurrence alone does not imply this: nested intervals can count the same physical dissipation repeatedly. A quantitative recurrence theorem must control time overlap or produce a disjoint/bounded-overlap subfamily.

---

## 8. Continuous Type-I-scale form

Put

\[
r(t)=\sqrt{T-t}.
\]

If at time \(t\) there are \(N(t)\) disjoint critical balls with

\[
\int_{B_{r(t)}}|\nabla u|^2dx\gtrsim r(t)^{-1},
\]

then

\[
\|\nabla u(t)\|_2^2\gtrsim\frac{N(t)}{r(t)}.
\]

Thus finite Leray dissipation requires

\[
\int^{T}\frac{N(t)}{\sqrt{T-t}}dt<\infty.
\]

With \(r=\sqrt{T-t}\) and \(dt=-2r\,dr\), this becomes

\[
\boxed{
\int_0^{r_0}N(r)\,dr<\infty.
}
\]

Hence a power-law multiplicity

\[
N(r)\sim r^{-\beta}
\]

is excluded by this ledger when \(\beta\ge1\), while \(\beta<1\) is not excluded by this calculation alone.

**Status: PROVED CONDITIONAL / continuum version of the same gate.**

---

## 9. Enstrophy blow-up rate audit

For a smooth solution let

\[
Y(t):=\|\omega(t)\|_2^2.
\]

The global enstrophy identity and Calderón–Zygmund plus Gagliardo–Nirenberg estimates give

\[
\frac12Y'(t)+\|\nabla\omega\|_2^2
\le
C\|\omega\|_3^3
\le
C Y^{3/4}\|\nabla\omega\|_2^{3/2}.
\]

Young's inequality yields

\[
Y'(t)\le C Y(t)^3.
\]

If \(Y(t)\to\infty\) at a finite time \(T\), integration gives the necessary lower blow-up rate

\[
\boxed{
Y(t)\gtrsim (T-t)^{-1/2}.
}
\]

But

\[
\int^{T}(T-t)^{-1/2}dt<\infty.
\]

Therefore the minimum rate forced by this differential inequality is itself compatible with the finite ordinary energy-dissipation ledger.

Moreover a single critical parabolic core has

\[
Y(t)\sim r(t)^{-1}
\sim (T-t)^{-1/2},
\]

so the critical one-core model exactly matches this integrable threshold.

This is a second independent audit showing why ordinary energy dissipation alone cannot close the nested one-core branch.

**Status: PROVED CONDITIONAL on enstrophy blow-up; no global-regularity conclusion.**

---

## 10. Rescaled high-derivative branch

If

\[
|\nabla^m u(x_r,t_r)|\gtrsim r^{-(m+1)},
\]

then under

\[
v_r(y,s)=r\,u(x_r+ry,t_r+r^2s)
\]

we have

\[
|\nabla_y^mv_r(0,0)|\gtrsim1.
\]

Thus high-derivative escape produces a nontrivial unit-scale derivative profile after critical rescaling. This is not a contradiction. Compactness requires suitable uniform critical control on the rescaled cylinders, and elimination of a limiting ancient profile requires a Liouville/backward-uniqueness/rigidity input appropriate to the surviving branch.

Therefore the high-derivative branch reconnects to the existing ancient-solution route rather than closing independently through derivative-energy summation.

---

## 11. Audit verdict

| Statement | Status |
|---|---|
| One critical core over one parabolic epoch costs order \(r\) in the ordinary dissipation ledger | PROVED / scaling |
| Geometric one-core scale charges are summable | PROVED / budget audit |
| Finite Leray dissipation excludes every infinite shrinking cascade | FALSE |
| Critical palinstrophy epoch cost scales like \(r^{-1}\) | PROVED / scaling |
| A finite global palinstrophy budget is available under the present hypotheses | NOT DERIVED |
| Higher derivative dissipations can be summed across derivative order as one finite ledger | INVALID / CIRCULAR |
| General gate \(\sum N_k\tau_k/r_k<\infty\) under bounded overlap | PROVED CONDITIONAL |
| Parabolic gate \(\sum N_kr_k<\infty\) | PROVED CONDITIONAL |
| Critical multiplicity exponent \(\beta\ge1\) is incompatible with the common energy ledger | PROVED CONDITIONAL |
| Minimum enstrophy blow-up rate \(Y\gtrsim(T-t)^{-1/2}\) is integrable in time | PROVED CONDITIONAL |
| Recurrence automatically supplies nonsummable multiplicity or bounded-overlap epochs | NOT DERIVED |
| High-derivative concentration rescales to a nontrivial unit profile | PROVED / scaling |
| This note proves global regularity | FALSE |

---

## 12. New frontier

The high-derivative concentration branch is now reduced to

\[
\boxed{
\text{high-derivative concentration}
\Longrightarrow
\begin{cases}
\text{nonsummable multiplicity/dwell paid from the common }L^2\text{ ledger},\\
\text{or a sparse/nested one-core cascade requiring rescaled-profile rigidity.}
\end{cases}
}
\]

The first branch is excluded whenever its weighted recurrence satisfies

\[
\sum_kN_k\frac{\tau_k}{r_k}=\infty.
\]

The second branch survives the energy audit. The next useful calculation is therefore to connect the existing bounded-\(Z\), recurrent, non-\(L^3\) annular ledger to a quantitative return count, or else return directly to the ancient-profile compactness/Liouville obstruction.