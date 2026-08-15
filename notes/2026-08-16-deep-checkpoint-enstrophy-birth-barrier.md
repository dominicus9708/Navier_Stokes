# Deep checkpoint to coherent crossing forces `R^3` global enstrophy birth

Date: 2026-08-16

Status: **DERIVED GLOBAL ENSTROPHY-GROWTH NECESSITY INDEPENDENT OF WHERE THE `log q` ACTION IS TEMPORALLY LOCATED / POSITIVE-MIDDLE-STRAIN OR DERIVATIVE PRODUCTION REQUIRED / GLOBAL REGULARITY NOT PROVED.**

## 1. Coherent crossing enstrophy floor

At the coherent Reynolds-one crossing,

\[
|\bar\Omega|\ge c_0,
\qquad
V_\omega\lesssim R^{-4}.
\]

On a fixed fractional Gaussian core `B_{cR}`, the unweighted variance estimate gives

\[
\int_{B_{cR}}|\Omega-\bar\Omega|^2dy
\lesssim R^{-1}.
\]

Therefore, for all sufficiently large `R`, an order-one fraction of the `R^3` core volume has vorticity magnitude bounded below by a fixed constant. Hence

\[
\boxed{
E_c:=\|\Omega(s_c)\|_2^2
\gtrsim R^3.
}
\]

---

## 2. Deep first-hitting checkpoint ceiling

Choose

\[
q_\beta=\frac{W}{R^\beta},
\]

with fixed `beta>0` such that the earlier physical vorticity level

\[
W_-=R^\beta
\]

is still on the late first-hitting cascade.

The first-hitting logistic relaxation estimate gives at that checkpoint

\[
\boxed{
E_-
\lesssim
\frac{W^{1/2}}{q_\beta}
=
\frac{R^\beta}{W^{1/2}}
}
\]

up to fixed viscosity/initial-energy constants.

The coherent Gaussian-tail energy barrier gives

\[
R^5(\log R)^{5/2}
\lesssim W^{1/2}.
\]

Therefore

\[
E_-
\lesssim
R^{\beta-5}(\log R)^{-5/2}.
\]

Relative to the crossing floor,

\[
\frac{E_-}{R^3}
\lesssim
R^{\beta-8}(\log R)^{-5/2}.
\]

Thus for every fixed

\[
\boxed{\beta<8,}
\]

we have

\[
\boxed{E_-=o(R^3).}
\]

---

## 3. Enstrophy birth

Combining the two endpoints,

\[
\boxed{
E_c-E_-
\gtrsim R^3.
}
\]

This conclusion does not depend on where the amplification action is distributed in time. In particular it survives the correction that the full deep-checkpoint `log q` need not occur in the final `O(R^2)` crossing block.

The coherent crossing must be preceded by the creation of a genuinely new global enstrophy reservoir of size `R^3` in terminal normalization.

---

## 4. Enstrophy-action lower bound

On the terminal first-hitting past,

\[
\|\Omega\|_\infty\le1.
\]

The exact enstrophy identity is

\[
\frac12E'
+\nu P
=Q,
\]

where

\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2,
\qquad
Q=\int\Omega\cdot S\Omega.
\]

Calderon--Zygmund plus interpolation gives

\[
|Q|
\lesssim
\|\Omega\|_\infty E
\lesssim E.
\]

Dropping the nonnegative viscous term gives

\[
E'\lesssim E.
\]

Integrating the enstrophy identity more directly,

\[
E_c-E_-
\le
C\int_{s_-}^{s_c}E(s)ds.
\]

Hence

\[
\boxed{
D_{\rm deep}
:=\int_{s_-}^{s_c}E(s)ds
\gtrsim R^3.
}
\]

This is stronger than the final-block annular price `R(log q)^2` whenever `R^2` dominates the relevant logarithmic factors.

---

## 5. Positive middle strain is unavoidable on the growth route

For trace-free strain eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0,
\]

Betchov gives

\[
Q=-4\int\det S.
\]

The positive part of `Q` can occur only through the two-positive-eigenvalue shape (`lambda_2>0`). A simple pointwise estimate gives

\[
Q_+
\lesssim
\int \lambda_2^+|S|^2dx.
\]

Since

\[
E_c-E_-+2\nu\int P
=2\int Q,
\]

we necessarily have

\[
\boxed{
\int_{s_-}^{s_c}\int
\lambda_2^+|S|^2dxds
\gtrsim R^3
}
\]

up to a universal constant on the net-growth branch.

If the production instead appears through highly localized derivative activity, that is the already typed palinstrophy/Hessian branch.

Thus deep stochastic ancestry must ultimately feed a large positive-middle-strain or derivative-production episode before the coherent crossing.

---

## 6. Physical dissipation scaling and remaining Zeno possibility

The normalized-to-physical relation is

\[
D_{\rm norm}
=W^{1/2}\int E_{\rm phys}(t)dt.
\]

Therefore one deep-to-crossing episode costs at least

\[
\boxed{
\int_{I}E_{\rm phys}dt
\gtrsim
\frac{R^3}{W^{1/2}}.
}
\]

This can still be summable along a super-separated sequence because `W` may grow much faster than `R`.

However, since `R_j -> infinity`, one may choose a subsequence of coherent crossings whose deep start levels `R_j^beta` lie above the preceding selected terminal vorticity level. The corresponding deep-to-crossing intervals are then disjoint. On every such disjoint subsequence,

\[
\boxed{
\sum_j\frac{R_j^3}{W_j^{1/2}}<\infty
}
\]

is a necessary condition imposed by the finite kinetic-energy dissipation budget.

This is a new Zeno summability requirement, not yet a contradiction.

---

## 7. Updated interpretation

A hypothetical singular cascade can no longer be described as merely transporting a pre-existing coherent vortex object from the deep checkpoint to the terminal crossing.

For every sufficiently deep checkpoint with `beta<8`, it must create

\[
\boxed{O(R^3)}
\]

new normalized global enstrophy before reaching the coherent crossing.

Therefore the surviving endgame is simultaneously

\[
\boxed{
\text{stochastic ancestor geometric degeneration}
+\text{large enstrophy birth}
+\text{critical middle-strain/derivative production}.
}
\]

Overall status: **DEEP ANCESTRY MUST BUILD A NEW `R^3` ENSTROPHY RESERVOIR; SUPER-SEPARATED CRITICAL SATURATION REMAINS POSSIBLE.**
