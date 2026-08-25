# DSD Pineau--Vicol Local Core-Speed Gate

Date: 2026-08-25

Status: **PRESSURE-ANNULUS BRIDGE DERIVED ON SPATIAL TYPE-I LANE / 2026 PINEAU--VICOL ONE-SLICE CRITERION IMPORTED / HYPOTHETICAL SINGULAR SURVIVOR FORCED TO HAVE A UNIFORM POSITIVE GAUSSIAN-WEIGHTED CORE SPEED / PASSIVE FROZEN TAIL CANNOT PAY THIS SPEED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The remaining pure bounded-`Z` survivor has been reduced to

\[
\boxed{
\text{similarity-scale recurrent active core}
+
\text{frozen passive critical endpoint tail}.
}
\]

The tail is too weak locally to force the core, but it prevents direct use of the strong global `L3` ancient Liouville theorem.

A recent local regularity theorem of Pineau--Vicol provides a different gate: under a local Type-I upper bound and a bounded pressure annulus, one sufficiently late time slice with small **self-similar time derivative** implies regularity.

Because the theorem has a Gaussian-weighted version, the passive remote tail can be removed from the speed test.

---

## 2. External theorem cross-check

Reference:

Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v2, revised 2026-08-06.

Their Theorem 1.9 considers a smooth solution on

\[
B_1\times[-1,0)
\]

satisfying

\[
\boxed{
|u(x,t)|
\le
\frac{C_u}{\sqrt{-t}+|x|}
}
\]

and a uniform pressure bound on the annulus

\[
A=\{1/2<|x|<3/4\}.
\]

There exist positive constants depending on the Type-I/pressure bounds such that, if at one sufficiently late time `tbar<0`,

\[
\sqrt{-\bar t}
\left\|
(-\bar t)\partial_tu
-\frac12u
-\frac12(x\cdot\nabla)u
\right\|_{L^\infty(B_1)}
\le\delta_0,
\]

then `(0,0)` is regular.

In self-similar variables

\[
U(y,s)=\sqrt{-t}\,u(x,t),
\qquad
x=\sqrt{-t}\,y,
\qquad
s=-\log(-t),
\]

this is exactly a smallness condition on

\[
\partial_sU.
\]

Their Remark 1.11 states that the proof also works with a weaker Gaussian-weighted condition of the form

\[
\boxed{
\int_{B_{e^{s/2}}}
|\partial_sU(y,s)|
(1+|y|)e^{-|y|^2/8}dy
\le\delta_w
}
\]

for a sufficiently small positive threshold `delta_w` depending only on the theorem constants.

Status: **EXTERNAL PREPRINT THEOREM / VERIFIED AGAINST arXiv v2.**

---

## 3. Spatial Type-I branch in the repository

The annular `H2` bridge already shows that if

\[
\sup_{R\ge R_0}
R\int_{A_R^*}|\nabla U|^2dy
\le E_*,
\]

and

\[
\sup_{R\ge R_0}
R^3\int_{A_R^*}|\nabla^2U|^2dy
\le H_*,
\]

then

\[
\boxed{
|U(Y,s)|
\le
\frac{C_*}{1+|Y|}.
}
\]

Failure of either bound is an explicit critical remote `H1/H2` tail and is excluded from the present pure lane.

Scaling back to physical variables gives exactly

\[
\boxed{
|u(x,t)|
\le
\frac{C_*}{|x|+\sqrt{T^*-t}}
}
\]

near the candidate singular point, after translating `T^*` to zero.

Thus the velocity hypothesis of the Pineau--Vicol local theorem matches the pure spatial-Type-I branch.

---

## 4. Pressure-annulus bridge

The earlier annular note left the pressure hypothesis as a separate lemma. It can be closed on the present smooth spatial-Type-I lane.

Fix an annulus

\[
A=\{1/2<|x|<3/4\}
\]

and a slightly larger annulus `A+` still separated from the origin.

On `A+`, the Type-I bound is uniformly bounded in time:

\[
|u(x,t)|\le C_A.
\]

Standard interior Navier--Stokes regularity away from the candidate singular center therefore gives uniform local derivative/Hölder bounds on a smaller fixed annulus.

Choose a smooth cutoff `chi` equal to one near `A` and write the pressure, after a time-dependent scalar gauge, as

\[
p=p_{loc}+p_{far},
\]

where

\[
p_{loc}
=R_iR_j(\chi u_iu_j).
\]

Because `chi u_i u_j` is compactly supported and uniformly smooth/Hölder on the annular neighborhood, local Calderon--Zygmund/Schauder estimates give

\[
\boxed{
\|p_{loc}\|_{L^\infty(A)}\le C_{loc}.
}
\]

For the far contribution choose `x_0 in A` and subtract its value:

\[
p_{far}(x,t)-p_{far}(x_0,t)
=
\int
[K_{ij}(x-y)-K_{ij}(x_0-y)]
(1-\chi(y))u_i(y,t)u_j(y,t)dy.
\]

The source is a fixed positive distance from `A`. Near the origin and on bounded intermediate regions the kernel difference is uniformly bounded, while at infinity

\[
|K(x-y)-K(x_0-y)|\le C_A|y|^{-4}.
\]

The physical kinetic energy satisfies

\[
\sup_{t<T^*}\|u(t)\|_2^2\le2E_0.
\]

Therefore

\[
\boxed{
\sup_{t<T^*}
\sup_{x\in A}
|p_{far}(x,t)-p_{far}(x_0,t)|
\le C(E_0,A).
}
\]

Fixing the pressure gauge by `p(x_0,t)=0` gives

\[
\boxed{
\sup_{A\times[-1,0)}|p|\le C_p<\infty.
}
\]

Status: **PROVED modulo standard interior/Schauder pressure estimates on the fixed annulus.**

---

## 5. Contrapositive speed floor

Assume the candidate point remains singular while all spatial-Type-I and pressure-annulus hypotheses above hold.

Then the Pineau--Vicol criterion cannot be satisfied at any sufficiently late self-similar time.

Consequently there exist

\[
s_0<\infty,
\qquad
\delta_w>0
\]

such that for every

\[
s\ge s_0,
\]

\[
\boxed{
\mathscr S_w(s)
:=
\int_{B_{e^{s/2}}}
|\partial_sU(y,s)|
(1+|y|)e^{-|y|^2/8}dy
\ge
\delta_w.
}
\]

This is a **uniform positive self-similar trajectory-speed floor** for every sufficiently late time, not merely a positive time average.

Status: **PROVED CONDITIONALLY by contrapositive of the imported theorem.**

---

## 6. Frozen tail cannot pay the Gaussian speed floor

On the pure spatial-Type-I/derivative corridor, the Leray equation and derivative bounds give the rough tail estimate

\[
|\partial_sU(y,s)|
\le
\frac{C_s}{1+|y|}
\]

for large `|y|`.

This is consistent with the frozen critical conveyor, for which the leading homogeneous `1/r` profile is stationary in self-similar coordinates.

Hence for every `R>=1`,

\[
\begin{aligned}
\int_{|y|>R}
|\partial_sU|(1+|y|)e^{-|y|^2/8}dy
&\le
C_s\int_{|y|>R}e^{-|y|^2/8}dy.
\end{aligned}
\]

The right side tends to zero exponentially as `R -> infinity`, uniformly on the pure corridor.

Choose one fixed `R_PV` sufficiently large that

\[
C_s\int_{|y|>R_{PV}}e^{-|y|^2/8}dy
\le
\frac{\delta_w}{2}.
\]

Then the singular speed floor forces

\[
\boxed{
\int_{B_{R_{PV}}}
|\partial_sU(y,s)|
(1+|y|)e^{-|y|^2/8}dy
\ge
\frac{\delta_w}{2}
}
\]

for every sufficiently late `s`.

Thus the passive critical tail cannot supply the Pineau--Vicol obstruction. The required motion is localized to one fixed similarity-scale core ball.

Status: **PROVED.**

---

## 7. Convert to a local `L2` speed floor

On the fixed ball `B_{R_PV}`, the Gaussian weight is bounded above by a finite constant. By Cauchy--Schwarz,

\[
\int_{B_{R_{PV}}}
|\partial_sU|(1+|y|)e^{-|y|^2/8}dy
\le
C_{PV,R}
\|\partial_sU\|_{L^2(B_{R_{PV}})}.
\]

Therefore

\[
\boxed{
\|\partial_sU(\cdot,s)\|_{L^2(B_{R_{PV}})}
\ge
\sigma_{PV}>0
}
\]

for every sufficiently late `s`, where

\[
\sigma_{PV}
:=
\frac{\delta_w}{2C_{PV,R}}.
\]

Status: **PROVED.**

---

## 8. Updated recurrent-core dichotomy

The final pure Type-I lane now has the exact alternative

\[
\boxed{
\begin{aligned}
&\exists\text{ one late slice with sufficiently small local self-similar speed}
&&\Longrightarrow\text{regularity},\\
&\text{or}\\
&\|\partial_sU\|_{L^2(B_{R_{PV}})}\ge\sigma_{PV}
\text{ for every late }s
&&\Longrightarrow\text{persistent moving recurrent core}.
\end{aligned}
}
\]

The frozen weak-`L3` tail is absent from the second inequality except through fixed constants.

---

## 9. DSD interpretation

The global critical-tail obstruction and the local dynamical obstruction are now separated:

\[
\boxed{
\text{global tail channel}
\neq
\text{core-speed channel}.
}
\]

The tail may remain frozen at the weak-`L3` endpoint, but a singularity still requires the compact active core to move forever with a fixed positive self-similar speed.

Thus the final rigidity problem is no longer

\[
\text{remove the entire }1/r\text{ tail first}.
\]

It may instead be attacked as

\[
\boxed{
\text{exclude a bounded/precompact recurrent Leray core orbit with }
\|U_s\|_{L^2(B_R)}\ge\sigma_0>0,
}
\]

while all remote derivative/turnover/projective exits are excluded.

---

## 10. Remaining obligation

A compact recurrent orbit can in abstract dynamics move forever at positive speed (for example, a periodic orbit), so the speed floor alone is not yet a contradiction.

The next calculation must use Navier--Stokes-specific structure to show that such perpetual local motion pays one of the already quantified costs:

- projective/eigenframe action;
- material replacement/flux turnover;
- local derivative/hyperpalinstrophy action;
- or a recurrent-orbit rigidity theorem.

No claim is made that general recurrence plus a positive speed floor is impossible by topology alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
