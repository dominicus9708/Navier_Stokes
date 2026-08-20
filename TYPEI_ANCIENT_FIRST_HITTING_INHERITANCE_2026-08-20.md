# First-Hitting Structure Inherited by a Type-I Ancient Limit — 2026-08-20

Overall status: **ANCIENT-LIMIT STRUCTURE IDENTIFIED — GLOBAL REGULARITY NOT PROVED.**

This note records additional structure inherited by any ancient limit extracted from the non-`H/T`, Type-I-sized first-hitting tower. The key point is that first-hitting normalization provides more than generic Type-I scaling: it gives a global backward vorticity cap and a geometric sequence of backward times at which the vorticity supremum decays like the inverse backward time.

---

## 1. Fixed-center blow-up sequence

Let

\[
r_j=W_j^{-1/2},
\qquad W_j=q^jW_0,
\]

and let `X_*` be the limiting center supplied by the non-turnover nesting condition. Define the ordinary fixed-center Navier--Stokes rescaling

\[
U_j(y,\tau)
=r_j u(X_*+r_jy,t_j+r_j^2\tau),
\]

\[
\Omega_j(y,\tau)
=r_j^2\omega(X_*+r_jy,t_j+r_j^2\tau).
\]

At the first-hitting time `t_j`,

\[
\|\Omega_j(\cdot,0)\|_{\infty}=1.
\]

Moreover, because `t_j` is the first time at which `W=W_j`,

\[
\boxed{
\|\Omega_j(\cdot,\tau)\|_{\infty}\le1
\quad\text{for every }\tau\le0
}
\]

on the backward lifespan of the rescaled solution.

---

## 2. Backward stage times in the current scaling

Assume the non-`H/T`, `P_V`-recurrent branch has stage lengths

\[
0<L_-\le L_k\le L_+<\infty.
\]

The physical duration of stage `k` satisfies

\[
\frac{L_k}{qW_k}
\le
\Delta t_k
\le
\frac{L_k}{W_k}.
\]

For the stage `j-m`, define its time in the stage-`j` fixed scaling by

\[
\tau_{j,m}
=W_j(t_{j-m}-t_j)
=-W_j\sum_{k=j-m}^{j-1}\Delta t_k.
\]

Since

\[
\frac{W_j}{W_{j-l}}=q^l,
\]

there are constants `c_-,c_+>0`, depending only on `q,L_-,L_+`, such that

\[
\boxed{
c_-q^m\le|\tau_{j,m}|\le c_+q^m.
}
\]

Equivalently, with `R_m=q^{m/2}`,

\[
\boxed{|\tau_{j,m}|\asymp R_m^2.}
\]

---

## 3. Vorticity amplitude at backward first-hitting times

At time `t_{j-m}` the physical vorticity supremum is `W_{j-m}`. Therefore in the stage-`j` scaling,

\[
\|\Omega_j(\cdot,\tau_{j,m})\|_{\infty}
=
\frac{W_{j-m}}{W_j}
=q^{-m}=R_m^{-2}.
\]

Together with `|tau_{j,m}| asymp R_m^2`, this gives

\[
\boxed{
\|\Omega_j(\cdot,\tau_{j,m})\|_{\infty}
\asymp
\frac1{|\tau_{j,m}|}.
}
\]

Thus the geometric first-hitting tower automatically carries a backward Type-I vorticity sequence.

---

## 4. Passage to an ancient limit

Suppose the non-`H/T` branch supplies enough local compactness to extract

\[
U_j\to U_{\infty},
\qquad
\Omega_j\to\Omega_{\infty}
\]

locally on expanding backward cylinders. Then the global first-hitting cap passes to the limit:

\[
\boxed{
\|\Omega_{\infty}(\cdot,\tau)\|_{\infty}\le1
\quad(\tau\le0).
}
\]

The first-hitting maximum points satisfy

\[
y_j=\frac{X_j-X_*}{r_j}=O(1).
\]

Under local derivative compactness, after a subsequence `y_j -> y_infty`, and

\[
\boxed{
|\Omega_{\infty}(y_{\infty},0)|=1,
}
\]

so the limit is nontrivial.

By a diagonal extraction over the backward geometric stages, the limit also inherits a sequence `tau_m -> -infinity` with

\[
\boxed{
\|\Omega_{\infty}(\cdot,\tau_m)\|_{\infty}
\lesssim
|\tau_m|^{-1}.
}
\]

The maximizers at these backward times may lie at spatial distance `O(sqrt(|tau_m|))`, consistent with the Type-I tower geometry.

---

## 5. Why this is stronger than a generic ancient limit

A generic bounded ancient Navier--Stokes solution need not come equipped with a first-hitting normalization. The present limit has three extra properties:

1. a global backward vorticity cap `||Omega||_infty <= 1`;
2. nontriviality at the terminal normalized time, `|Omega(y_infty,0)|=1`;
3. a geometric backward sequence with `||Omega(tau_m)||_infty = O(|tau_m|^{-1})`.

These properties should be retained when formulating the restricted Liouville target. They may be substantially stronger than the generic Type-I ancient class even though no general Liouville theorem for this subclass has yet been established here.

---

## 6. Current restricted ancient target

The non-`H/T` endgame can therefore be formulated as the possible existence of a nontrivial ancient suitable/mild solution satisfying simultaneously:

\[
\|\Omega(\tau)\|_{\infty}\le1\quad(\tau\le0),
\]

\[
|\Omega(y_*,0)|=1,
\]

\[
\|\Omega(\tau_m)\|_{\infty}\lesssim|\tau_m|^{-1}
\quad\text{for }\tau_m\downarrow-\infty,
\]

plus the inherited Type-I local bounds and the `P_V/G_Q` projective restrictions developed in the main proof route.

Status: **ANY NON-H/T TYPE-I COMPACT LIMIT IS NOT A GENERIC ANCIENT SOLUTION; IT INHERITS A GLOBAL FIRST-HITTING VORTICITY CAP AND A BACKWARD 1/|t| VORTICITY SEQUENCE.**