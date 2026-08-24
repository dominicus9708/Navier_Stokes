# Ancestor-Radius Identity and Weighted Return-Density Gate

Date: 2026-08-25

Status: **EXACT SCALE IDENTITY DERIVED / CONDITIONAL RETURN-DENSITY GATE DERIVED / TIME-SEPARATION LOWER BOUND NOT DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

This note remains restricted to the corrected branch

\[
\boxed{\text{bounded-}Z+\text{recurrent}+\text{non-}L^3},
\]

for which the annular cubic ledger

\[
\sum_k J_k^{3/2}=\infty
\]

has already been established in the repository.

No claim is made here for the broader unbounded-\(Z\)/Morrey branch.

---

## 2. First-hitting scales

Use

\[
W_j=q^jW_0,\qquad q>1,
\]

and define the distinguished physical scale

\[
r_j=W_j^{-1/2}.
\]

For an age-\(k\) shell in the rescaled profile, let

\[
K_k=q^{k/2}.
\]

The physical radius at current stage \(j\) is

\[
R_{j,k}^{\mathrm{phys}}=r_jK_k.
\]

But

\[
\begin{aligned}
r_{j-k}
&=(q^{j-k}W_0)^{-1/2}\\
&=q^{k/2}(q^jW_0)^{-1/2}\\
&=K_kr_j.
\end{aligned}
\]

Therefore

\[
\boxed{
R_{j,k}^{\mathrm{phys}}=r_{j-k}.
}
\]

### Interpretation

An age-\(k\) shell observed at current first-hitting stage \(j\) occupies exactly the physical radius that was the distinguished scale at the earlier first-hitting stage \(j-k\).

This identifies the spatial genealogy exactly; it does **not** yet identify a persistent material packet or a time interval connecting the two stages.

**Status: PROVED algebraically.**

---

## 3. Temporal audit: upper remaining-time bounds do not give epoch separation

Suppose the existing first-hitting construction gives upper remaining-time estimates of the form

\[
T^*-t_j\lesssim r_j^2,
\qquad
T^*-t_{j-k}\lesssim r_{j-k}^2.
\]

These are two upper bounds. They do not imply a lower bound for

\[
t_j-t_{j-k}.
\]

In particular, one may not subtract them to conclude

\[
t_j-t_{j-k}\gtrsim r_{j-k}^2.
\]

Define the normalized epoch gap

\[
\boxed{
\Gamma_{j,k}:=
\frac{t_j-t_{j-k}}{r_{j-k}^2}.
}
\]

At the present stage no uniform positive lower bound

\[
\Gamma_{j,k}\ge c>0
\]

has been derived from the remaining-time upper bounds alone.

**Status: PROVED AUDIT; positive lower epoch separation NOT DERIVED.**

---

## 4. Conditional consequence of one-step lower epoch separation

If one independently proves

\[
t_m-t_{m-1}\ge c\,r_{m-1}^2
\]

for all relevant first-hitting stages, then

\[
\begin{aligned}
t_j-t_{j-k}
&=\sum_{m=j-k+1}^{j}(t_m-t_{m-1})\\
&\ge c\sum_{m=j-k+1}^{j}r_{m-1}^2.
\end{aligned}
\]

Since

\[
r_{j-k+h}^2=r_{j-k}^2q^{-h},
\]

we obtain

\[
t_j-t_{j-k}
\ge
c r_{j-k}^2\sum_{h=0}^{k-1}q^{-h}
\ge
c r_{j-k}^2.
\]

Hence

\[
\Gamma_{j,k}\ge c.
\]

But the premise itself is not yet available, so this is only a conditional bridge.

**Status: PROVED CONDITIONAL; premise NOT DERIVED.**

---

## 5. Weighted physical return density

The previous multiplicity-dwell gate can be sharpened without requiring every return to last a full parabolic epoch.

For annular label \(k\), let the physical genealogy produce return intervals

\[
I_{k,1},\ldots,I_{k,M_k}
\]

at a comparable physical radius \(\rho_k\). Write

\[
\tau_{k,\ell}:=|I_{k,\ell}|.
\]

Define the weighted return density

\[
\boxed{
\mathfrak R_k
:=
\frac1{\rho_k}
\sum_{\ell=1}^{M_k}\tau_{k,\ell}.
}
\]

This has the dimension of length in viscosity-normalized variables, just like \(M_k\rho_k\) under parabolic dwell.

Assume that throughout every return interval a tracked comparable shell satisfies

\[
\rho_k
\int_{A_{k,\ell}(t)}|\nabla u(x,t)|^2dx
\ge
c_0J_k,
\]

with fixed \(c_0>0\), and that the full collection of intervals has time-overlap multiplicity at most \(Q<\infty\).

Each interval then costs

\[
\int_{I_{k,\ell}}
\int_{A_{k,\ell}(t)}|\nabla u|^2dxdt
\ge
c_0J_k\frac{\tau_{k,\ell}}{\rho_k}.
\]

Summing over all returns and using the common Leray dissipation ledger gives

\[
\boxed{
\sum_kJ_k\mathfrak R_k
\le
\frac{QE_0}{c_0}<\infty,
}
\]

where

\[
E_0=\frac12\|u_0\|_2^2
\]

in the normalization \(\nu=1\).

**Status: PROVED CONDITIONAL on amplitude retention, shell tracking/comparability, and bounded time overlap.**

---

## 6. Parabolic-dwell return count is a special case

If each return has

\[
\tau_{k,\ell}\ge\theta\rho_k^2,
\]

then

\[
\mathfrak R_k
\ge
\theta M_k\rho_k.
\]

Thus the previous return-count gate

\[
\sum_kM_kJ_k\rho_k<\infty
\]

is recovered immediately.

The weighted-density formulation is strictly more flexible because it allows many short returns or nonuniform dwell times.

**Status: PROVED.**

---

## 7. Exact cubic-tail contradiction target

On any subset \(S\) carrying divergent cubic mass,

\[
\sum_{k\in S}J_k^{3/2}=\infty,
\]

suppose one proves

\[
\boxed{
\mathfrak R_k\ge c_1J_k^{1/2}
\qquad(k\in S)
}
\]

with fixed \(c_1>0\).

Then

\[
J_k\mathfrak R_k
\ge
c_1J_k^{3/2},
\]

so

\[
\sum_{k\in S}J_k\mathfrak R_k=\infty,
\]

contradicting the finite Leray return-density ledger.

Therefore the current bounded-\(Z\) energy-closure target can be written exactly as

\[
\boxed{
\sum J_k^{3/2}=\infty
\quad+\quad
\mathfrak R_k\gtrsim J_k^{1/2}
\quad\Longrightarrow\quad
\text{contradiction}.
}
\]

**Status: PROVED CONDITIONAL.**

---

## 8. Remaining-time-only persistence is too weak for remote age

At stage \(j\), an age-\(k\) shell has

\[
\rho=R_{j,k}^{\mathrm{phys}}
=r_{j-k}
=r_jK_k.
\]

If it is known to persist only for a time comparable to the current remaining time,

\[
\tau\asymp r_j^2,
\]

then its weighted return contribution is only

\[
\begin{aligned}
\frac{\tau}{\rho}
&\asymp
\frac{r_j^2}{r_jK_k}\\
&=
\frac{r_j}{K_k}\\
&=
\frac{\rho}{K_k^2}.
\end{aligned}
\]

Thus remote age \(k\) carries the severe weight loss

\[
\boxed{K_k^{-2}=q^{-k}}.
\]

Consequently, persistence merely through the current first-hitting remaining window does not automatically provide

\[
\mathfrak R_k\gtrsim J_k^{1/2}.
\]

This agrees with the previous audit showing that the cubic annular divergence is not by itself an ordinary physical-dissipation divergence.

**Status: PROVED / exact scaling audit.**

---

## 9. What the exact ancestor-radius identity does and does not buy

The identity

\[
R_{j,k}^{\mathrm{phys}}=r_{j-k}
\]

shows that the remote annulus is not attached to an arbitrary physical radius: it lands exactly on a previous distinguished scale.

Therefore the missing genealogy theorem can now be formulated as a temporal/amplitude statement rather than a spatial-scale matching problem.

What remains to prove is some version of:

\[
\boxed{
\text{age-}k\text{ annular mass at stage }j
\Longrightarrow
\text{sufficiently long or sufficiently repeated physical activity near scale }r_{j-k}.
}
\]

Neither the radius identity nor the first-hitting remaining-time upper bound alone gives this.

---

## 10. Audit verdict

| Statement | Status |
|---|---|
| \(R_{j,k}^{phys}=r_{j-k}\) | PROVED exactly |
| Age-\(k\) shell therefore matches an earlier distinguished physical scale | PROVED |
| It is automatically the same persistent material packet | NOT DERIVED |
| Remaining-time upper bounds imply \(t_j-t_{j-k}\gtrsim r_{j-k}^2\) | FALSE as an inference |
| One-step lower epoch separation would imply \(\Gamma_{j,k}\gtrsim1\) | PROVED CONDITIONAL |
| Weighted return ledger \(\sum J_k\mathfrak R_k<\infty\) | PROVED CONDITIONAL |
| Full parabolic dwell recovers \(\mathfrak R_k\gtrsim M_k\rho_k\) | PROVED |
| \(\mathfrak R_k\gtrsim J_k^{1/2}\) on a cubic-divergent subset closes that branch | PROVED CONDITIONAL |
| Remaining-time-only persistence supplies this bound | NOT DERIVED; generally too weak by \(K_k^{-2}\) |
| Global regularity | UNPROVED |

---

## 11. New frontier

The bounded-\(Z\), recurrent, non-\(L^3\) branch is now reduced more sharply to

\[
\boxed{
\text{ancient cubic annular mass}
\stackrel{?}{\Longrightarrow}
\text{physical weighted return density }
\mathfrak R_k\gtrsim J_k^{1/2}
}
\]

on a subset still carrying divergent \(\sum J_k^{3/2}\).

The spatial scale correspondence is exact; the unresolved part is temporal persistence/return multiplicity and amplitude retention with bounded overlap.

If that implication fails, the surviving alternative is a sparse/nested cascade whose physical return weight is summable. That branch should be attacked through rescaled-profile compactness and a Liouville/backward-uniqueness/tail-decoupling rigidity theorem rather than through the ordinary energy ledger.