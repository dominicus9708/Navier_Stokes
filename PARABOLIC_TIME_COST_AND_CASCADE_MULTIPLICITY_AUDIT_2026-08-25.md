# Parabolic Time Cost and Cascade Multiplicity–Dwell Audit

Date: 2026-08-25

## 1. Scope

This note audits the remaining high-derivative concentration escape branch by attaching the natural parabolic time scale to each spatial concentration scale.

The purpose is deliberately narrow:

1. determine whether an infinite spatial concentration chain is excluded by the ordinary Leray energy-dissipation ledger once parabolic dwell time is included;
2. determine whether palinstrophy or higher-derivative dissipation can be summed without an additional hypothesis;
3. extract a rigorous multiplicity/recurrence obstruction that does use one common finite ledger.

Throughout Sections 2–8 we nondimensionalize viscosity to

\[
\nu=1.
\]

The standard Navier–Stokes scaling is

\[
u_
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t).
\]

Global regularity is not claimed.

---

## 2. Critical single-core scaling at radius \(r\)

At a critical concentration radius \(r\), the scale-invariant amplitudes are

\[
|u|\sim r^{-1},
\qquad
|\omega|\sim |\nabla u|\sim r^{-2},
\]

and, more generally,

\[
|\nabla^m u|\sim r^{-(m+1)}.
\]

The natural parabolic dwell time is

\[
\tau_r\sim r^2.
\]

For one active ball of volume comparable to \(r^3\),

\[
\int_{B_r}|\nabla u|^2\,dx
\sim
r^{-4}r^3
=
r^{-1}.
\]

Therefore its contribution to the ordinary spacetime energy-dissipation ledger over one parabolic epoch is

\[
\int_{t_r-c r^2}^{t_r}\int_{B_r}|\nabla u|^2\,dx\,dt
\sim
r^{-1}r^2
=
r.
\]

Thus the common Leray ledger charges a critical single-core epoch only order \(r\).

**Status: scaling identity / dimensionally proved.**

---

## 3. Geometric scale cascade is not excluded by the energy ledger alone

Let

\[
r_k=\lambda^kR,
\qquad 0<\lambda<1.
\]

If there is only one critical active core at each scale and each scale persists for one parabolic epoch, the scale-model dissipation charge is

\[
D_k\asymp r_k.
\]

Hence

\[
\sum_{k=0}^{\infty}D_k
\asymp
\sum_{k=0}^{\infty}r_k
=
\frac{R}{1-\lambda}
<\infty.
\]

This does **not** prove that such a cascade exists. It proves only the audit statement:

\[
\boxed{
\text{finite Leray energy dissipation alone does not exclude a one-core geometric cascade by scale summation.}
}
\]

Consequently, the proposed route

\[
\text{infinitely many shrinking critical cores}
\Longrightarrow
\text{infinite ordinary energy dissipation}
\]

is invalid without an additional nonsummable multiplicity, dwell, recurrence, or amplitude mechanism.

**Status: PROVED as a budget audit; existence of such a cascade is NOT asserted.**

---

## 4. Palinstrophy becomes expensive, but it is not a common finite ledger

At the same critical scale,

\[
|\nabla\omega|\sim r^{-3}.
\]

Therefore

\[
\int_{B_r}|\nabla\omega|^2\,dx
\sim
r^{-6}r^3
=
r^{-3}.
\]

Over a parabolic epoch,

\[
\int_{I_r}\int_{B_r}|\nabla\omega|^2\,dx\,dt
\sim
r^{-3}r^2
=
r^{-1}.
\]

So palinstrophy charges smaller scales more strongly, and a geometric sequence would formally give

\[
\sum_k r_k^{-1}=\infty.
\]

However, this is **not** a contradiction under the finite-energy Leray assumptions, because those assumptions give a finite common budget for

\[
\int_0^T\|\nabla u(t)\|_2^2\,dt,
\]

but not, near a hypothetical first singular time, an a priori finite global budget for

\[
\int_0^T\|\nabla\omega(t)\|_2^2\,dt.
\]

Using the latter as if it were already finite would import additional regularity into the proof.

Hence

\[
\boxed{
\text{palinstrophy divergence is informative but is not yet a contradiction ledger.}
}
\]

**Status: PROVED scaling; contradiction from it is NOT DERIVED.**

---

## 5. General derivative-order audit

For \(m\ge 0\), critical scaling gives

\[
|\nabla^m u|\sim r^{-(m+1)}.
\]

Thus the spatial \(L^2\) size at order \(m\) is

\[
E_m(r)
:=
\int_{B_r}|\nabla^m u|^2\,dx
\sim
r^3r^{-2(m+1)}
=
r^{1-2m}.
\]

The next-derivative dissipation density is

\[
\int_{B_r}|\nabla^{m+1}u|^2\,dx
\sim
r^{-1-2m}.
\]

Multiplying by the parabolic time \(r^2\) gives

\[
D_m(r)
:=
\int_{I_r}\int_{B_r}|\nabla^{m+1}u|^2\,dx\,dt
\sim
r^{1-2m}.
\]

Thus parabolic time does not by itself create an extra derivative-order contradiction; it reproduces the natural critical scaling of the corresponding \(H^m\) energy.

Most importantly, one may **not** sum

\[
D_0+D_1+D_2+\cdots
\]

as if all terms were withdrawals from one finite conserved or dissipative quantity. They belong to different derivative-energy ledgers. Finite-energy Navier–Stokes controls the \(m=0\) dissipation ledger, not all \(m\) uniformly through a possible singular time.

Therefore the proposed proof pattern

\[
\text{high-derivative escape at every order}
\Longrightarrow
\sum_m D_m=\infty
\Longrightarrow
\text{contradiction}
\]

is **INVALID / CIRCULAR** without an independent common high-order bound.

---

## 6. Cascade multiplicity–dwell proposition

The ordinary energy ledger does become restrictive when many critical cores or repeated time-separated critical epochs must be paid from that same ledger.

### Proposition

Let \(u\) be a finite-energy Leray solution on \([0,T)\), normalized to \(\nu=1\), and let

\[
E_0:=\frac12\|u_0\|_{L^2(\mathbb R^3)}^2.
\]

For each \(k\), suppose there is a time interval \(I_k\), radius \(r_k>0\), and \(N_k\) spatially disjoint balls

\[
B_{r_k}(x_{k,1}),\ldots,B_{r_k}(x_{k,N_k})
\]

such that:

1. the intervals \(I_k\) have time-overlap multiplicity at most \(Q<\infty\);
2. each interval has parabolic dwell
   \[
   |I_k|\ge \theta r_k^2
   \]
   for some fixed \(\theta>0\);
3. for every \(t\in I_k\) and every active ball,
   \[
   \int_{B_{r_k}(x_{k,j})}|\nabla u(x,t)|^2\,dx
   \ge
   \frac{\alpha}{r_k}
   \]
   for some fixed \(\alpha>0\).

Then

\[
\boxed{
\sum_k N_k r_k
\le
\frac{Q E_0}{\alpha\theta}.
}
\]

In particular,

\[
\boxed{
\sum_k N_k r_k<\infty.
}
\]

### Proof

Spatial disjointness at fixed \(k,t\) gives

\[
\int_{\mathbb R^3}|\nabla u(x,t)|^2\,dx
\ge
\sum_{j=1}^{N_k}
\int_{B_{r_k}(x_{k,j})}|\nabla u(x,t)|^2\,dx
\ge
\frac{\alpha N_k}{r_k}.
\]

Integrating over \(I_k\),

\[
\int_{I_k}\int_{\mathbb R^3}|\nabla u|^2\,dx\,dt
\ge
\frac{\alpha N_k}{r_k}|I_k|
\ge
\alpha\theta N_k r_k.
\]

Summing over \(k\) and using time-overlap multiplicity at most \(Q\),

\[
\alpha\theta\sum_kN_kr_k
\le
\sum_k\int_{I_k}\|\nabla u(t)\|_2^2\,dt
\le
Q\int_0^T\|\nabla u(t)\|_2^2\,dt.
\]

The Leray energy inequality yields

\[
\int_0^T\|\nabla u(t)\|_2^2\,dt
\le
E_0,
\]

and the claim follows.

**Status: PROVED CONDITIONAL on the stated geometric/dwell hypotheses.**

---

## 7. Consequences of the multiplicity–dwell gate

### 7.1 One core per geometric scale

For \(N_k=1\) and \(r_k=\lambda^kR\),

\[
\sum_kN_kr_k<\infty.
\]

Therefore this gate does not exclude a single nested geometric core.

### 7.2 Multiplicity of order \(r_k^{-1}\)

If along infinitely many bounded-overlap epochs

\[
N_k\gtrsim r_k^{-1},
\]

then

\[
N_kr_k\gtrsim1,
\]

so

\[
\sum_kN_kr_k=\infty,
\]

contradicting the proposition.

Thus a cascade cannot repeatedly support order \(r^{-1}\) mutually disjoint critical cores for full parabolic dwell while keeping uniformly bounded time overlap.

### 7.3 Recurrence alone is insufficient

A recurrence statement does not automatically produce summable lower bounds, because heavily nested or repeatedly overlapping time windows can charge the same physical dissipation multiple times in bookkeeping.

Hence the needed upgrade is not merely

\[
\text{recurrence},
\]

but something like

\[
\boxed{
\text{recurrence + bounded time overlap + nonsummable }N_kr_k.
}
\]

The derivation of such a property from the current active-core recurrence framework remains open.

---

## 8. Relation to the high-derivative escape branch

Suppose a derivative-order concentration at \((x_r,t_r)\) satisfies

\[
|\nabla^m u(x_r,t_r)|\gtrsim r^{-(m+1)}.
\]

Under the critical rescaling

\[
v_r(y,s)
=
r\,u(x_r+ry,t_r+r^2s),
\]

one has

\[
|\nabla_y^m v_r(0,0)|\gtrsim1.
\]

Therefore high-derivative escape can always be converted into a nontrivial unit-scale derivative profile.

But this alone is not contradictory. To pass to an ancient or limiting profile, one still needs enough uniform critical control on the rescaled cylinders to obtain compactness. To eliminate the limit, one then needs a Liouville/backward-uniqueness/rigidity mechanism appropriate to that branch.

So the parabolic-time audit reconnects the high-derivative escape branch to the existing compactness/ancient-solution route rather than closing it independently.

---

## 9. Audit verdict

| Statement | Status |
|---|---|
| Critical single-core ordinary dissipation over one parabolic epoch scales like \(r\) | PROVED / scaling |
| A geometric one-core cascade gives a summable scale-model ordinary dissipation charge | PROVED / budget audit |
| Finite Leray dissipation alone therefore excludes every infinite shrinking cascade | FALSE |
| Critical palinstrophy spacetime cost scales like \(r^{-1}\) | PROVED / scaling |
| A finite global palinstrophy budget is available under the present finite-energy hypotheses | NOT DERIVED |
| High-order dissipation may be summed across derivative order as one finite ledger | INVALID / CIRCULAR |
| Bounded-overlap multiplicity–dwell gate \(\sum_kN_kr_k<\infty\) | PROVED CONDITIONAL |
| Recurrence automatically supplies bounded-overlap epochs and nonsummable multiplicity | NOT DERIVED |
| High-derivative concentration rescales to a nontrivial unit profile | PROVED / scaling |
| This note proves global regularity | FALSE |

---

## 10. New frontier

The high-derivative branch is now separated into two possibilities:

\[
\boxed{
\text{high-derivative concentration}
\Longrightarrow
\begin{cases}
\text{nonsummable multiplicity/dwell in the common }L^2\text{ dissipation ledger},\\
\text{or a nested/sparse one-core cascade requiring rescaled-profile rigidity.}
\end{cases}
}
\]

The first branch is excluded whenever the hypotheses of the multiplicity–dwell proposition force

\[
\sum_kN_kr_k=\infty.
\]

The second branch survives this audit and should be attacked by compactness plus a critical-norm/Liouville obstruction, not by summing derivative-order dissipation.