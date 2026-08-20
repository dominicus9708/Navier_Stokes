# First-Hitting Ancient Vorticity Cap — 2026-08-20

Overall status: **STRONGER ANCIENT-LIMIT INHERITANCE — GLOBAL REGULARITY NOT PROVED.**

This note records an inheritance property that is stronger than the previously stated backward Type-I decay. It follows directly from the definition of the geometric first-hitting times.

---

## 1. First-hitting rescaling

Let `t_j` be the first time at which

\[
W(t_j)=W_j,
\qquad
W(t)=\|\omega(t)\|_\infty,
\]

with

\[
W_j=q^jW_0.
\]

Set

\[
r_j=W_j^{-1/2}.
\]

Using the fixed limiting singular center `X_*` on the non-turnover branch, define

\[
U_j(y,\tau)
=r_j u(X_*+r_jy,t_j+r_j^2\tau),
\]

\[
\Omega_j(y,\tau)
=r_j^2\omega(X_*+r_jy,t_j+r_j^2\tau).
\]

---

## 2. Exact backward cap before taking a limit

Because `t_j` is the **first** hitting time of `W_j`,

\[
W(t)\le W_j
\qquad\text{for every }t\le t_j.
\]

Therefore for every rescaled backward time for which the original solution is defined,

\[
\boxed{
\|\Omega_j(\tau)\|_\infty\le1,
\qquad \tau\le0.
}
\]

This does not require Type-I stage-length control. It is an exact first-hitting property.

---

## 3. Nontrivial terminal normalization

Let `x_j` be a point at which

\[
|\omega(x_j,t_j)|=W_j.
\]

Non-turnover center nesting gives

\[
|x_j-X_*|\lesssim r_j.
\]

Hence

\[
y_j=\frac{x_j-X_*}{r_j}
\]

remains bounded. Along a subsequence,

\[
y_j\to y_*.
\]

At the terminal time,

\[
|\Omega_j(y_j,0)|=1.
\]

Thus any sufficiently strong local ancient limit satisfies

\[
\boxed{
|\Omega_\infty(y_*,0)|=1,
}
\]

so it is nontrivial.

---

## 4. Passage to an ancient limit

Assume the non-H/T compactness bridge supplies enough local compactness to extract a smooth ancient limit on compact subsets. Then the uniform first-hitting cap passes to the limit:

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty\le1
\qquad\text{for every }\tau\le0.
}
\]

Thus the ancient candidate has globally bounded vorticity throughout its entire backward lifetime, not merely a bound along selected first-hitting times.

---

## 5. Combination with the Type-I backward decay

On the non-H/T P_V branch, previous stage-length estimates give

\[
0<L_-\le L_j\le L_+<\infty.
\]

This implies the continuous backward Type-I estimate

\[
\sup_{\tau\le-\tau_0}
|\tau|\,\|\Omega_\infty(\tau)\|_\infty<\infty.
\]

Combining it with the first-hitting cap gives

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty
\le
\min\left\{1,\frac{C}{|\tau|}\right\}
\qquad (\tau<0).
}
\]

In particular,

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty\to0
\qquad\text{as }\tau\to-\infty.
}
\]

This is stronger than the previously recorded statement that `|tau| ||Omega||_infty` is bounded.

---

## 6. Why this does not yet give a Liouville theorem

The general three-dimensional classification of bounded mild ancient Navier--Stokes solutions remains open. Moreover, bounded vorticity does not by itself provide a global `L^infty` bound for velocity because the strain is a singular integral of vorticity and the globally necessary critical tail may carry low-frequency velocity content.

Therefore

\[
\|\Omega(\tau)\|_\infty\to0
\quad(\tau\to-\infty)
\]

is a substantial restriction on the ancient survivor, but it is not presently a proved triviality criterion in the full three-dimensional setting used here.

---

## 7. Interaction with the L3-tail necessity

The Albritton--Barker Liouville theorem says that a nontrivial mild ancient solution cannot have a globally bounded `L^3` norm along a backward sequence. Hence the restricted ancient survivor must simultaneously satisfy

\[
\|\Omega(\tau)\|_\infty\to0
\quad\text{as }\tau\to-\infty,
\]

while

\[
\|U(\tau)\|_3
\to\infty
\quad\text{in the sense that no bounded backward subsequence exists.}
\]

Thus the backward-divergent critical tail must become increasingly **low-vorticity / low-gradient** while retaining large scale-invariant velocity mass.

This sharpens the core-tail picture:

\[
\boxed{
\text{tight active core}
+
\text{backward-growing low-vorticity critical velocity tail}.
}
\]

The tail cannot supply order-one core strain on the non-H branch by the aggregate halo palinstrophy barrier.

---

## 8. New core-tail target

A particularly concrete remaining question is now:

\[
\boxed{
\begin{gathered}
\text{Can an ancient Navier--Stokes solution have}\
\|\Omega(\tau)\|_\infty\lesssim |\tau|^{-1}\text{ backward},\n\text{a nontrivial tight terminal core, and}\
\text{a globally divergent }L^3\text{ velocity tail that remains dynamically passive?}
\end{gathered}
}
\]

Any contradiction must use the coexistence of the **vanishing backward vorticity amplitude** and the **unbounded backward critical velocity mass**, rather than either property alone.

Status: **FIRST-HITTING RESCALINGS CARRY AN EXACT GLOBAL BACKWARD VORTICITY CAP. THE NON-H/T ANCIENT LIMIT SATISFIES `||Omega(tau)||_infty <= min(1,C/|tau|)` AND IS NONTRIVIAL AT TERMINAL TIME. THE REMAINING GLOBAL TAIL MUST THEREFORE BE LARGE IN L3 WHILE BECOMING LOW-VORTICITY BACKWARD.**