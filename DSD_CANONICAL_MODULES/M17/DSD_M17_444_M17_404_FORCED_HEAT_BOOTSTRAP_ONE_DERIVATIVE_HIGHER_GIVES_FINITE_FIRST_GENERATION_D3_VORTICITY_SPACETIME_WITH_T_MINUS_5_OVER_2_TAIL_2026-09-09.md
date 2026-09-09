# DSD M17-444 — The M17-404 forced-heat argument bootstraps one derivative higher and gives finite first-generation `D3 Omega` spacetime with a `T^{-5/2}` backward tail

Date: 2026-09-09  
Canonical ID: **M17-444**

Status: **ACTIVE HIGHER-RESOURCE THEOREM / FIRST-GENERATION D3-VORTICITY FINITENESS**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

Let `(V,Omega)` be the viscosity-one first-generation ancient element used in M17-404.

M5-475 supplies, for large negative time `tau`,

\[
\|V(\tau)\|_\infty\lesssim(-\tau)^{-1/2},
\]

\[
\|\Omega(\tau)\|_\infty\lesssim(-\tau)^{-1},
\]

and

\[
E(\tau):=\|\Omega(\tau)\|_2^2
\lesssim(-\tau)^{-1/2}.
\]

M5-477 gives the quantitative palinstrophy tail

\[
\boxed{
\int_{-\infty}^{-T}
P(\tau)d\tau
\lesssim T^{-1/2},
\qquad
P:=\|\nabla\Omega\|_2^2.
}
\]

M17-404 gives the raw-`H2` tail

\[
\boxed{
\int_{-\infty}^{-T}
H(\tau)d\tau
\lesssim T^{-3/2},
\qquad
H:=\|\Delta\Omega\|_2^2.
}
\]

The goal is to prove

\[
\boxed{
\int_{-\infty}^{0}
J(\tau)d\tau<\infty,
\qquad
J:=\|\nabla\Delta\Omega\|_2^2
\asymp\|D^3\Omega\|_2^2.
}
\]

## 2. Forced heat equation and one derivative

M17-404 writes

\[
\partial_\tau\Omega-\Delta\Omega=F,
\qquad
F=-V\cdot\nabla\Omega+S\Omega.
\]

Differentiate spatially:

\[
\boxed{
\partial_\tau\nabla\Omega
-\Delta\nabla\Omega
=\nabla F.
}
\]

We require a dyadic `L2` estimate on `nabla F`.

## 3. Estimate the differentiated forcing without `nabla V` in `L-infinity`

Expand

\[
\nabla F
=-(\nabla V)\nabla\Omega
-V\,D^2\Omega
+(\nabla S)\Omega
+S\nabla\Omega.
\]

The easy terms satisfy

\[
\|V D^2\Omega\|_2
\le
\|V\|_\infty H^{1/2},
\]

and Calderon--Zygmund gives

\[
\|\nabla S\|_2
\lesssim
\|\nabla\Omega\|_2,
\]

so

\[
\|(\nabla S)\Omega\|_2
\lesssim
\|\Omega\|_\infty P^{1/2}.
\]

For the two mixed terms, use

\[
\|\nabla V\|_6+\|S\|_6
\lesssim
\|\Omega\|_6.
\]

Also

\[
\|\nabla\Omega\|_3
\le
\|\nabla\Omega\|_2^{1/2}
\|\nabla\Omega\|_6^{1/2}
\lesssim
P^{1/4}H^{1/4}.
\]

Hence

\[
\|(\nabla V)\nabla\Omega\|_2
+
\|S\nabla\Omega\|_2
\lesssim
\|\Omega\|_6P^{1/4}H^{1/4}.
\]

Interpolate `L2` and `L-infinity`:

\[
\|\Omega\|_6
\le
\|\Omega\|_2^{1/3}
\|\Omega\|_\infty^{2/3}.
\]

On a dyadic backward annulus `|tau| asymp T`,

\[
\|\Omega\|_2\lesssim T^{-1/4},
\qquad
\|\Omega\|_\infty\lesssim T^{-1},
\]

so

\[
\boxed{
\|\Omega\|_6\lesssim T^{-3/4}.
}
\]

Therefore

\[
\boxed{
\|\nabla F\|_2^2
\lesssim
T^{-1}H
+T^{-2}P
+T^{-3/2}P^{1/2}H^{1/2}.
}
\]

## 4. Dyadic forcing tail

Integrate over any interval contained in `[-4T,-T]`.

The first two terms give

\[
T^{-1}\int H
\lesssim T^{-5/2},
\]

\[
T^{-2}\int P
\lesssim T^{-5/2}.
\]

For the mixed term, Cauchy--Schwarz gives

\[
\int P^{1/2}H^{1/2}
\le
\left(\int P\right)^{1/2}
\left(\int H\right)^{1/2}
\lesssim
T^{-1/4}T^{-3/4}
=T^{-1}.
\]

Thus

\[
\boxed{
\int_{-4T}^{-T}
\|\nabla F\|_2^2d\tau
\lesssim T^{-5/2}.
}
\]

## 5. Find a small `H` starting time

Use the preceding annulus

\[
[-4T,-2T].
\]

M17-404 gives

\[
\int_{-4T}^{-2T}H(\tau)d\tau
\lesssim T^{-3/2}.
\]

The interval has length `2T`, so there exists

\[
\tau_T\in[-4T,-2T]
\]

with

\[
\boxed{
H(\tau_T)
\lesssim T^{-5/2}.
}
\]

## 6. `H2` energy estimate

Take the global `L2` inner product of

\[
\partial_\tau\nabla\Omega
-\Delta\nabla\Omega
=\nabla F
\]

with

\[
-\Delta\nabla\Omega.
\]

On `R3`, Fourier equivalence gives

\[
\|D^2\Omega\|_2^2
\asymp
\|\Delta\Omega\|_2^2=H
\]

and

\[
\|D^3\Omega\|_2^2
\asymp
\|\nabla\Delta\Omega\|_2^2=J.
\]

Therefore

\[
\frac12\frac d{d\tau}\|D^2\Omega\|_2^2
+J
=
-\int\nabla F\cdot\Delta\nabla\Omega.
\]

Young's inequality gives

\[
\boxed{
\frac d{d\tau}H+cJ
\lesssim
\|\nabla F\|_2^2.
}
\]

Integrate from `tau_T` to `-T`:

\[
\int_{\tau_T}^{-T}Jd\tau
\lesssim
H(\tau_T)
+
\int_{\tau_T}^{-T}\|\nabla F\|_2^2d\tau.
\]

Sections 4--5 yield

\[
\boxed{
\int_{-2T}^{-T}
\|D^3\Omega(\tau)\|_2^2d\tau
\lesssim T^{-5/2}.
}
\]

## 7. Sum the backward tail

For `T_n=2^nT_0`,

\[
\sum_nT_n^{-5/2}<\infty.
\]

Hence

\[
\boxed{
\int_{-\infty}^{-T_0}
\|D^3\Omega(\tau)\|_2^2d\tau
<\infty.
}
\]

Smoothness on the finite interval `[-T_0,0]` gives the remaining finite part. Therefore

\[
\boxed{
\mathscr J_{anc}
:=
\int_{-\infty}^{0}
\|D^3\Omega(\tau)\|_2^2d\tau
<\infty.
}
\]

More quantitatively,

\[
\boxed{
\int_{-\infty}^{-T}
\|D^3\Omega(\tau)\|_2^2d\tau
\lesssim T^{-5/2}.
}
\]

## 8. Scaling

For

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

one has

\[
D^3\Omega_R=R^5D^3\Omega.
\]

Therefore

\[
\boxed{
\int_I\|D^3\Omega_R\|_2^2ds
=
R^5
\int_{R^2I}\|D^3\Omega\|_2^2dt.
}
\]

Thus the exact ancestry weight for this resource is

\[
\boxed{R_m^{-5}.}
\]

The corresponding record ledger is obtained under the same finite-overlap genealogy bookkeeping as M17-405.

## 9. Why this matters for coefficient gradients

On exact CE-H,

\[
\Delta\Omega=\kappa\Omega.
\]

Differentiating gives

\[
\boxed{
\nabla\Delta\Omega
=(\nabla\kappa)\otimes\Omega
+\kappa\nabla\Omega.
}
\]

Therefore

\[
\boxed{
\rho^2|\nabla\kappa|^2
\lesssim
|D^3\Omega|^2
+\kappa^2|\nabla\Omega|^2.
}
\]

This opens a genuine finite-resource route for the coefficient-gradient architecture, although the second term and the exact record scaling must be audited separately. That is the next module; M17-444 itself does not yet claim a finite global coefficient-gradient budget.

## 10. DSD audit role

DSD only suggested testing whether the previous absence of a higher-order resource was a true obstruction or an unperformed energy estimate. The proof is standard forced-heat differentiation, Sobolev interpolation, Calderon--Zygmund, and dyadic summation.

## 11. Audit verdict

**PASS — the first-generation ancient element has finite total `D3 Omega` spacetime charge with a `T^{-5/2}` backward tail.**

The new resource has exact ancestry weight `R_m^{-5}`. It is stronger regularity but carries a more severe record discount than raw-`H2` or palinstrophy.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
