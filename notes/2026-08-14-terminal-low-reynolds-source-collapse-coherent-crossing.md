# Terminal low-Reynolds source collapse forces a coherent fast-rotation crossing

Date: 2026-08-14

Status: **DERIVED ON THE BOUNDED-CONDITION, BOUNDED-ACCUMULATED-AFFINE GAUSSIAN BRANCH. THE FIRST BACKWARD `R_G=1` CROSSING CANNOT ACQUIRE ORDER-ONE MEAN VORTICITY FROM THE TERMINAL LOW-REYNOLDS SEGMENT; IT MUST ALREADY CARRY ORDER-ONE COHERENT MEAN VORTICITY. CONSEQUENTLY THE CROSSING IS AUTOMATICALLY A FAST-ROTATION STATE. GLOBAL REGULARITY NOT PROVED.**

## 1. First backward critical crossing

Use backward normalized age

\[
\tau=-s\ge0
\]

and, for notational clarity, the isotropic matched relation

\[
R(\tau)^2\asymp\tau.
\]

Define

\[
\mathcal R_G(\tau)
=R(\tau)^2\sqrt{B(\tau)}.
\]

Near the terminal point,

\[
\mathcal R_G(\tau)\to0,
\]

whereas on a surviving responsible pulse

\[
\mathcal R_G\to\infty.
\]

Let `tau_c` be the **first** backward age for which

\[
\boxed{\mathcal R_G(\tau_c)=1.}
\]

Then for every

\[
0<\tau\le\tau_c,
\]

we have

\[
\boxed{\mathcal R_G(\tau)\le1.}
\]

Hence

\[
\boxed{B(\tau)\lesssim\tau^{-2}.}
\]

At the crossing,

\[
\boxed{B_cR_c^4\asymp1.}
\]

## 2. Combine all three available ceilings on the terminal segment

The surviving bounded-affine branch has

\[
\boxed{B(\tau)\le m,\qquad m\to0.}
\]

Terminal Gaussian collapse gives

\[
\boxed{B(\tau)\lesssim\tau.}
\]

The first-crossing condition gives

\[
\boxed{B(\tau)\lesssim\tau^{-2}.}
\]

Therefore on the entire terminal low-Reynolds segment,

\[
\boxed{
B(\tau)
\lesssim
\min\{C\tau,m,C\tau^{-2}\}.
}
\]

## 3. The total residual action before the crossing is `O(sqrt(m))`

For sufficiently small `m`, the three envelopes exchange dominance near

\[
\tau\sim m
\]

and

\[
\tau\sim m^{-1/2}.
\]

Thus

\[
\begin{aligned}
\int_0^{\tau_c}B(\tau)d\tau
&\le
C\int_0^\infty
\min\{\tau,m,\tau^{-2}\}d\tau\\
&\lesssim
\int_0^m\tau d\tau
+
\int_m^{m^{-1/2}}m d\tau
+
\int_{m^{-1/2}}^\infty\tau^{-2}d\tau\\
&\lesssim
m^2+\sqrt m+\sqrt m.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_0^{\tau_c}B(\tau)d\tau
\lesssim\sqrt m
\to0.
}
\]

This is independent of the exact location of the first crossing.

## 4. Co-affine mean-vorticity action on the terminal segment

The Gaussian mean vorticity satisfies

\[
\bar\Omega'=L\bar\Omega+J,
\qquad
|J|\lesssim_K B.
\]

Let `F` be the bounded affine propagator and define the co-affine mean

\[
Z(\tau)=F(0,-\tau)\bar\Omega(-\tau)
\]

with the appropriate backward-time convention. On the bounded accumulated-affine branch,

\[
\|F\|+\|F^{-1}\|\le C_K.
\]

The co-affine equation gives

\[
|Z'(\tau)|\lesssim_K B(\tau).
\]

Hence

\[
\boxed{
|Z(0)-Z(\tau_c)|
\lesssim_K\sqrt m
=o(1).
}
\]

At terminal first hitting the Gaussian collapses to the tracked point, so

\[
\boxed{|Z(0)|=|\Omega(0,0)|=1.}
\]

Therefore

\[
\boxed{
|Z(\tau_c)|\ge1-o(1).
}
\]

Using the bounded inverse affine propagator,

\[
\boxed{
|\bar\Omega(\tau_c)|
\ge c_K>0
}
\]

for all sufficiently large first-hitting levels.

Thus the terminal low-Reynolds interval cannot create the terminal order-one coherent vorticity. It can change it only by `o(1)`.

## 5. The crossing radius must diverge

At the crossing,

\[
B_c\asymp R_c^{-4}.
\]

Since the surviving pulse obeys

\[
B_c\le m,
\]

we obtain

\[
\boxed{
R_c\gtrsim m^{-1/4}\to\infty.
}
\]

Therefore the critical crossing is genuinely mesoscopic in terminal-normalized coordinates.

## 6. Automatic fast-rotation parameter

The ratio of coherent mean vorticity to residual-gradient scale is

\[
\Gamma_c
:=
\frac{|\bar\Omega_c|}{\sqrt{B_c}}.
\]

Since

\[
|\bar\Omega_c|\ge c_K
\]

and

\[
\sqrt{B_c}\asymp R_c^{-2},
\]

we get

\[
\boxed{
\Gamma_c
\gtrsim_K
R_c^2
\gtrsim_K
m^{-1/2}
\to\infty.
}
\]

Thus

\[
\boxed{
\text{first critical Reynolds crossing}
\Longrightarrow
\text{coherent fast-rotation crossing}.
}
\]

The former `mean rotation not dominant at the critical crossing` subbranch is removed on the bounded-affine survivor.

## 7. Combine with critical residual normalization

At the crossing,

\[
R_c^2\sqrt{B_c}\asymp1.
\]

Hence the standard crossing-scale residual has order-one velocity amplitude and critical local `L3` size.

If the crossing is low curvature/tight, the existing Coriolis-kernel rigidity applies to the fast-rotation parameter

\[
\Gamma_c\to\infty.
\]

A nonzero compact residual limit is then impossible unless one of the explicitly typed non-Coriolis forcings becomes unbounded.

Therefore the surviving crossing must activate at least one of

\[
\boxed{
\text{high curvature / higher Hermite},
}
\]

\[
\boxed{
\text{spatial non-tightness / shell transport},
}
\]

or

\[
\boxed{
\text{large symmetric-affine / frame / nonlinear forcing}.
}
\]

## 8. Endgame consequence

The dynamic missing-power problem is now sharpened substantially:

1. every large-Reynolds pulse crosses `BR^4=1`;
2. the first such crossing has `R_c->infinity`;
3. its coherent mean rotation is automatically order one;
4. its rotation/residual ratio diverges like at least `m^-1/2`;
5. therefore a tight low-curvature crossing is excluded by the existing fast-rotation rigidity mechanism.

Thus the bounded-affine H-branch can no longer survive through a generic low-curvature critical crossing.

Status: **TERMINAL LOW-REYNOLDS SOURCE ACTION IS `O(sqrt(m))` / FIRST `R_G=1` CROSSING IS AUTOMATICALLY COHERENT FAST ROTATION / LOW-CURVATURE TIGHT CROSSING ROUTED TO CONTRADICTION OR ALREADY-TYPED FORCING ESCAPES / GLOBAL REGULARITY NOT PROVED.**
