# Parent-Pressure Escalation Finite Gate — 2026-08-21

Status: **SMOOTH/TYPE-I PARENT-PRESSURE PRUNING LEMMA / GLOBAL REGULARITY NOT PROVED.**

This note continues `TRANSVERSE_SWAP_PRESSURE_ROUTING_2026-08-21.md`. The goal is to test whether the harmonic pressure-Hessian action required by a short anti-ribbon transverse swap can evade local closure by being promoted to larger and larger parent scales indefinitely.

## 1. Scale-invariant parent energy control

In dynamically normalized variables define the local kinetic-energy Morrey quantity

\[
\mathcal M_R(X,s)
=
R^{-1}\int_{B_R(X)}|U(y,s)|^2dy.
\]

On the bounded-channel Type-I parent range, assume the existing local-energy controls give

\[
\boxed{
\mathcal M_R\le M_*
}
\]

for the parent radii under consideration.

This is the scale-invariant local energy quantity already used in the remote-pressure estimates.

## 2. Absolute remote pressure-Hessian decay

The normalized whole-space pressure is

\[
P=\mathcal R_i\mathcal R_j(U_iU_j),
\]

and its Hessian kernel is homogeneous of degree \(-5\). For sources outside radius \(R\),

\[
|\Pi_{rem}^{>R}(X)|
\lesssim
\int_{|z-X|>R}
\frac{|U(z)|^2}{|z-X|^5}dz.
\]

Split into dyadic annuli

\[
A_k=
\{2^kR\le|z-X|<2^{k+1}R\}.
\]

Morrey control gives

\[
\int_{A_k}|U|^2
\le
\int_{B_{2^{k+1}R}}|U|^2
\le
M_*2^{k+1}R.
\]

Hence

\[
\begin{aligned}
|\Pi_{rem}^{>R}(X)|
&\lesssim
\sum_{k\ge0}
(2^kR)^{-5}
M_*2^{k+1}R\\
&\lesssim
M_*R^{-4}
\sum_{k\ge0}2^{-4k}.
\end{aligned}
\]

Therefore

\[
\boxed{
|\Pi_{rem}^{>R}|
\le
C_P M_*R^{-4}
}
\]

with a fixed pressure-kernel constant \(C_P\).

This is the absolute-Hessian counterpart of the previously derived affine-free remote-pressure locality estimate.

## 3. Required harmonic pressure action from the swap gate

On one short positive-middle stage define

\[
a_{swap}
:=
\left[
\frac\pi2-\frac{L_I}{2}
-\mathscr A_{mis}
-\mathscr A_{P,near}
-\mathscr A_\nu
\right]_+.
\]

The exact eigenframe-rotation routing gives

\[
\mathscr A_{P,far}
\ge a_{swap}.
\]

If the transverse spectral gap remains bounded below,

\[
g_{12}\ge g_->0,
\]

then

\[
\int_I |(\Pi_{far})_{12}|ds
\ge
 g_-a_{swap}.
\]

Suppose the pressure source remains unresolved outside a parent radius \(R\) for the entire stage. Using \(L_I\le L_+\),

\[
g_-a_{swap}
\le
\int_I|\Pi_{rem}^{>R}|ds
\le
C_PM_*L_+R^{-4}.
\]

Thus remote pressure can pay the required swap action only if

\[
\boxed{
R
\le
R_{P,max}
:=
\left(
\frac{C_PM_*L_+}{g_-a_{swap}}
\right)^{1/4}.
}
\]

## 4. Finite dyadic escalation count

Starting at child radius \(r\), let the parent cascade use

\[
R_n=2^nr.
\]

If the swap obligation remains genuinely remote at every level, then

\[
2^{4n}r^4
\le
\frac{C_PM_*L_+}{g_-a_{swap}}.
\]

Hence

\[
\boxed{
n
\le
\frac14
\log_2
\left(
\frac{C_PM_*L_+}{g_-a_{swap}r^4}
\right).
}
\]

In particular, an infinite parent-pressure escalation is impossible while the Type-I Morrey bound, stage-length ceiling, positive transverse gap, and positive swap deficit remain in force.

## 5. What happens at the terminal parent

The pressure route must terminate in one of the following ways before or at \(R_{P,max}\):

1. the source becomes resolved inside the parent buffer, hence enters the local \(L\times B+B\times B\) residual state;
2. the local Morrey bound fails, activating the existing local-energy/turnover branch;
3. the spectral gap collapses, leaving the persistent positive-middle lane;
4. viscous or residual action becomes large, activating \(H/T\);
5. the required anti-ribbon swap action disappears because the stage is long enough, in which case the moving-variance duration comparison applies instead.

Thus parent harmonic pressure is not an independent infinite escape route.

## 6. Combined anti-ribbon routing

A short thick positive-middle stage now satisfies

\[
\boxed{
\text{anti-ribbon swap}
\Longrightarrow
\begin{cases}
\text{local residual / non-affine action},\\
\text{viscous derivative }H,\\
\text{spectral/alignment transition},\\
\text{or finite-depth parent pressure escalation}.
\end{cases}
}
\]

The last line itself terminates after finitely many parent steps under the Type-I Morrey corridor.

Status: **THE HARMONIC PARENT-PRESSURE MECHANISM REQUIRED FOR A SHORT TRANSVERSE SWAP CANNOT BE ESCALATED TO ARBITRARILY LARGE PARENT SCALES UNDER THE SCALE-INVARIANT LOCAL-ENERGY MORREY BOUND. IT MUST RESOLVE INTO THE EXISTING RESIDUAL/H/T TREE AFTER FINITELY MANY STEPS.**