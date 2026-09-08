# DSD M17-404 — Type-I ancient decay and finite palinstrophy force finite total raw-`H2` on the first-generation ancient element

Date: 2026-09-08  
Canonical ID: **M17-404**

Status: **ACTIVE TRUE-RESOURCE THEOREM / FIRST-GENERATION ANCIENT RAW-H2 FINITENESS / FORCED-HEAT ESTIMATE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs already certified upstream

Let `(V,Omega)` be the viscosity-one first-generation ancient element constructed in M5-474--477.

M5-475 gives, for `tau << -1`,

\[
\boxed{
\|V(\tau)\|_\infty
\le C(-\tau)^{-1/2},
}
\]

\[
\boxed{
\|\Omega(\tau)\|_\infty
\le C(-\tau)^{-1},
}
\]

and

\[
\boxed{
E(\tau):=\|\Omega(\tau)\|_2^2
\le C(-\tau)^{-1/2}.
}
\]

M5-477 gives finite total palinstrophy

\[
\boxed{
\int_{-\infty}^{0}
P(\tau)d\tau
<\infty,
\qquad
P(\tau):=\|\nabla\Omega(\tau)\|_2^2.
}
\]

The present module upgrades these facts to

\[
\boxed{
\int_{-\infty}^{0}
H(\tau)d\tau
<\infty,
\qquad
H(\tau):=\|\Delta\Omega(\tau)\|_2^2.
}
\]

## 2. Quantitative palinstrophy tail from M5-477

The ancient enstrophy identity is

\[
\frac12E'(\tau)+P(\tau)
=
\int S\Omega\cdot\Omega\,dx.
\]

M5-477 proves

\[
\left|
\int S\Omega\cdot\Omega dx
\right|
\le C(-\tau)^{-3/2}
\]

for sufficiently negative `tau`.

Because

\[
E(\tau)\to0
\qquad(\tau\to-\infty),
\]

integrating from `-infinity` to `-T` gives

\[
\frac12E(-T)
+
\int_{-\infty}^{-T}P(\tau)d\tau
=
\int_{-\infty}^{-T}
\int S\Omega\cdot\Omega.
\]

Therefore

\[
\boxed{
\int_{-\infty}^{-T}P(\tau)d\tau
\le C T^{-1/2},
\qquad T\gg1.
}
\]

This quantitative tail rate, rather than mere finiteness, is the key input below.

## 3. Rewrite vorticity as a forced heat equation

The ancient vorticity equation is

\[
\partial_\tau\Omega
+V\cdot\nabla\Omega
=S\Omega+\Delta\Omega.
\]

Write

\[
\boxed{
\partial_\tau\Omega-\Delta\Omega=F,
\qquad
F:=-V\cdot\nabla\Omega+S\Omega.
}
\]

Standard `L2` Calderon--Zygmund gives

\[
\|S\|_2\le C\|\Omega\|_2.
\]

Hence

\[
\begin{aligned}
\|F\|_2
&\le
\|V\|_\infty\|\nabla\Omega\|_2
+
\|\Omega\|_\infty\|S\|_2\\
&\le
\|V\|_\infty P^{1/2}
+C\|\Omega\|_\infty E^{1/2}.
\end{aligned}
\]

Thus

\[
\boxed{
\|F\|_2^2
\le
C\|V\|_\infty^2P
+C\|\Omega\|_\infty^2E.
}
\]

## 4. Dyadic backward annulus estimate

Fix large `T` and consider the target annulus

\[
J_T=[-2T,-T].
\]

Use the preceding interval

\[
J_T^-=[-4T,-2T].
\]

By the palinstrophy tail estimate,

\[
\int_{J_T^-}P(\tau)d\tau
\le C T^{-1/2}.
\]

Since `|J_T^-|=2T`, there exists

\[
\tau_T\in[-4T,-2T]
\]

such that

\[
\boxed{
P(\tau_T)
\le C T^{-3/2}.
}
\]

On the entire interval `[tau_T,-T]`, one has `|tau| asymp T`. Therefore M5-475 gives

\[
\|V\|_\infty^2\le CT^{-1},
\]

\[
\|\Omega\|_\infty^2\le CT^{-2},
\]

and

\[
E\le CT^{-1/2}.
\]

Consequently

\[
\begin{aligned}
\int_{\tau_T}^{-T}\|F\|_2^2d\tau
&\le
CT^{-1}
\int_{\tau_T}^{-T}P(\tau)d\tau\\
&\quad+
CT^{-2}
\int_{\tau_T}^{-T}E(\tau)d\tau.
\end{aligned}
\]

The first term is bounded by

\[
CT^{-1}\cdot CT^{-1/2}
=CT^{-3/2}.
\]

For the second term, the interval has length `O(T)` and `E<=CT^{-1/2}`, hence

\[
CT^{-2}\int E
\le
CT^{-2}\cdot T\cdot T^{-1/2}
=CT^{-3/2}.
\]

Therefore

\[
\boxed{
\int_{\tau_T}^{-T}\|F\|_2^2d\tau
\le CT^{-3/2}.
}
\]

## 5. `H1` energy estimate for the forced heat equation

Take the global `L2` inner product of

\[
\partial_\tau\Omega-\Delta\Omega=F
\]

with `-Delta Omega`.

Then

\[
\frac12\frac d{d\tau}P
+H
=
-\int F\cdot\Delta\Omega.
\]

By Young's inequality,

\[
\left|
\int F\cdot\Delta\Omega
\right|
\le
\frac12H+rac12\|F\|_2^2.
\]

Thus

\[
\boxed{
\frac d{d\tau}P+H
\le
\|F\|_2^2.
}
\]

Integrating from `tau_T` to `-T` gives

\[
\int_{\tau_T}^{-T}H(\tau)d\tau
\le
P(\tau_T)
+
\int_{\tau_T}^{-T}\|F\|_2^2d\tau.
\]

Using Sections 4 and 5,

\[
\boxed{
\int_{\tau_T}^{-T}H(\tau)d\tau
\le CT^{-3/2}.
}
\]

Since the target dyadic annulus `[-2T,-T]` lies inside `[tau_T,-T]`,

\[
\boxed{
\int_{-2T}^{-T}
\|\Delta\Omega(\tau)\|_2^2d\tau
\le CT^{-3/2}.
}
\]

## 6. Sum the dyadic tail

Set

\[
T_n=2^nT_0.
\]

Then

\[
\int_{-2T_n}^{-T_n}H
\le
C T_n^{-3/2}.
\]

The dyadic annuli cover the backward tail, and

\[
\sum_{n=0}^\infty T_n^{-3/2}<\infty.
\]

Therefore

\[
\boxed{
\int_{-\infty}^{-T_0}
\|\Delta\Omega(\tau)\|_2^2d\tau
<\infty.
}
\]

More quantitatively,

\[
\boxed{
\int_{-\infty}^{-T}
\|\Delta\Omega(\tau)\|_2^2d\tau
\lesssim T^{-3/2}
}
\]

up to adjustment of the fixed dyadic constants.

On the finite interval `[-T_0,0]`, the ancient element is smooth, so

\[
\int_{-T_0}^{0}\|\Delta\Omega\|_2^2d\tau<\infty.
\]

Hence

\[
\boxed{
\mathscr H_{anc}
:=
\int_{-\infty}^{0}
\|\Delta\Omega(\tau)\|_2^2d\tau
<\infty.
}
\]

## 7. Why no CE-H assumption is needed here

The proof used only

1. the ordinary ancient vorticity equation;
2. the M5-475 Type-I bounds;
3. the M5-477 enstrophy/palinstrophy estimate;
4. `L2` Calderon--Zygmund for the strain;
5. the elementary forced-heat `H1` estimate.

Thus the finite first-generation raw-`H2` resource is available upstream of the late CE-H specialization.

## 8. Cross-generation consequence

M17-403 gives the exact pullback

\[
R_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds
=
\int_{R_m^2I}\|\Delta\Omega\|_2^2dt.
\]

Together with the finite-overlap record windows and the new finite total `H_anc`, this immediately yields a genuine finite ancestral raw-`H2` ledger.

That summation is stated separately in M17-405.

## 9. DSD audit

The useful heuristic was to ask whether the raw-`H2` firewall was a true absence of a resource or merely an unperformed higher-energy estimate. The proof itself is standard PDE energy analysis and uses no DSD axiom.

## 10. Audit verdict

**PASS — the first-generation marked ancient element has finite total raw-`H2` spacetime charge.**

This removes the previous statement that no finite first-generation raw-`H2` budget is known for this specific ancient element.

It does **not** imply an unweighted finite budget in second-generation normalized record cells; M17-403 shows the required ancestry factor is `R_m^{-3}`.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
