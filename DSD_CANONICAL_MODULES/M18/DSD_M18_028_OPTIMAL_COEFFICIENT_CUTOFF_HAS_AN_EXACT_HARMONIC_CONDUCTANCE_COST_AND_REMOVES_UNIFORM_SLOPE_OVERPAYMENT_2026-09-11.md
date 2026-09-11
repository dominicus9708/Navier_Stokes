# M18-028 — Optimal coefficient cutoff has an exact harmonic conductance cost and removes uniform-slope overpayment

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / VARIATIONAL CUTOFF / HARMONIC COLLAR CONDUCTANCE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-027 showed that the cutoff current does not care about an isolated essential-supremum gradient spike unless that spike carries first-jet weight.

The remaining Young residual for a coefficient cutoff \(\chi\) is controlled by

\[
\int (\chi'(\kappa))^2\rho^2|\nabla\kappa|^4dx.
\]

M18-023 used a fixed approximately uniform slope \(|\chi'|\sim\delta_0^{-1}\). This module asks whether that choice overpays.

The answer is yes. After coarea, choosing the cutoff is an exact one-dimensional weighted Dirichlet problem. The optimal cutoff places most of its transition where the gradient-weighted collar conductance is smallest.

## 2. One-sided collar

Fix one coefficient transition interval

\[
I_c=[s_-,s_+],
\qquad
L_c:=s_+-s_->0,
\]

with

\[
L_c\asymp\delta_0
\]

inside a retained regular coefficient tube.

Require

\[
\chi(s_-)=1,
\qquad
\chi(s_+)=0.
\]

The negative-side collar is treated identically; the two costs add.

Define

\[
g:=|\nabla\kappa|
\]

and the instantaneous coefficient-level quartic conductance density

\[
\boxed{
W(s,t)
:=
\int_{\{\kappa=s\}}ho^2g^3\,dS.
}
\]

By coarea,

\[
\boxed{
\int_{\{s_-<\kappa<s_+\}}
(\chi'(\kappa))^2\rho^2g^4dx
=
\int_{s_-}^{s_+}
(\chi'(s))^2W(s,t)ds.
}
\]

## 3. Exact instantaneous variational problem

For fixed time, define

\[
\mathcal E_t[\chi]
:=
\int_{s_-}^{s_+}
W(s,t)|\chi'(s)|^2ds.
\]

Assume first that

\[
0<W(s,t)<\infty
\]

for almost every level in the collar and

\[
\int_{s_-}^{s_+}\frac{ds}{W(s,t)}<\infty.
\]

Since

\[
1
=\left|\int_{s_-}^{s_+}\chi'(s)ds\right|,
\]

weighted Cauchy--Schwarz gives

\[
1
\le
\mathcal E_t[\chi]^{1/2}
\left(
\int_{s_-}^{s_+}\frac{ds}{W(s,t)}
\right)^{1/2}.
\]

Therefore

\[
\boxed{
\mathcal E_t[\chi]
\ge
\left(
\int_{s_-}^{s_+}\frac{ds}{W(s,t)}
\right)^{-1}.
}
\]

Equality is attained by

\[
\boxed{
\chi'_{\rm opt}(s)
=-
\frac{W(s,t)^{-1}}
{\int_{s_-}^{s_+}W(r,t)^{-1}dr}.
}
\]

Thus the exact minimum is

\[
\boxed{
\mathcal G_c(t)
:=
\left(
\int_{s_-}^{s_+}\frac{ds}{W(s,t)}
\right)^{-1}.
}
\]

We call \(\mathcal G_c\) the coefficient-collar conductance.

## 4. Degenerate levels help rather than hurt

If there is a subinterval or a sufficiently strong measurable bottleneck on which \(W\) tends to zero so that

\[
\int_{s_-}^{s_+}\frac{ds}{W(s,t)}=\infty,
\]

then

\[
\boxed{
\inf_\chi\mathcal E_t[\chi]=0.
}
\]

In that case the cutoff can transition through an arbitrarily low-current coefficient bottleneck.

Therefore a large cutoff cost requires not merely one high-gradient level but the **absence of low-conductance levels across the whole transition collar**.

## 5. Uniform-slope cutoff is never better

For the linear cutoff

\[
|\chi'|=L_c^{-1},
\]

the cost is

\[
\mathcal E_t^{\rm lin}
=
L_c^{-2}
\int_{s_-}^{s_+}W(s,t)ds.
\]

By the arithmetic-harmonic mean inequality,

\[
\boxed{
\mathcal G_c(t)
\le
L_c^{-2}
\int_{s_-}^{s_+}W(s,t)ds.
}
\]

Thus the M18-023 uniform-slope estimate is a valid upper bound but not the canonical minimal cost.

A highly concentrated gradient spike can make the arithmetic cost large while leaving the harmonic conductance small if another coefficient level supplies a cheap transition route.

## 6. Relation to level flux

Recall

\[
F(s,t)
:=
\int_{\{\kappa=s\}}\rho^2g\,dS.
\]

When \(F(s,t)>0\), define the flux-weighted surface gradient moment

\[
\boxed{
\gamma(s,t)
:=
\frac{W(s,t)}{\delta_0^3F(s,t)}
=
\frac{
\int_{\Sigma_s}\rho^2g^3dS
}{
\delta_0^3
\int_{\Sigma_s}\rho^2g\,dS
}.
}
\]

This is scale invariant.

Then

\[
W(s,t)=\delta_0^3\gamma(s,t)F(s,t),
\]

and

\[
\boxed{
\mathcal G_c(t)
=
\delta_0^3
\left(
\int_{s_-}^{s_+}
\frac{ds}{\gamma(s,t)F(s,t)}
\right)^{-1}.
}
\]

Hence a robust flux floor alone does not force a large cutoff cost. Large cost also requires the flux-bearing levels to have persistently large normalized gradient moment \(\gamma\).

## 7. Time-independent cutoff for a spacetime interval

The instantaneous optimizer depends on time and cannot be inserted directly into the M18-024 identity without creating a new \(\partial_t\chi\) term.

To avoid that problem, fix a record time interval \(I\) and define the time-integrated level weight

\[
\boxed{
\mathbb W_I(s)
:=
\int_IW(s,t)dt.
}
\]

For a single time-independent cutoff \(\chi(s)\),

\[
\int_I\mathcal E_t[\chi]dt
=
\int_{s_-}^{s_+}
|\chi'(s)|^2\mathbb W_I(s)ds.
\]

Therefore the exact spacetime minimizer is

\[
\boxed{
\chi'_{I,\rm opt}(s)
=-
\frac{\mathbb W_I(s)^{-1}}
{\int_{s_-}^{s_+}\mathbb W_I(r)^{-1}dr},
}
\]

with minimal spacetime cost

\[
\boxed{
\mathcal G_{c,I}
:=
\left(
\int_{s_-}^{s_+}
\frac{ds}{\mathbb W_I(s)}
\right)^{-1}.
}
\]

No time-dependent-cutoff term is introduced.

## 8. Scaling audit

Instantaneously,

\[
W_R=R^{11}W.
\]

After time integration,

\[
\mathbb W_{I,R}=R^9\mathbb W_I.
\]

Since the coefficient variable scales as

\[
ds_R=R^2ds,
\]

we obtain

\[
\boxed{
\mathcal G_{c,I,R}=R^7\mathcal G_{c,I}.
}
\]

This is exactly the spacetime scaling of the optimized quartic cutoff residual.

If

\[
Q_{B,I}
:=
\int_I
\int_{\mathcal K}ho^2g^2dxdt,
\]

then \(Q_{B,I}\) scales as \(R^5\), so

\[
\boxed{
\mathfrak C_{c,I}
:=
\frac{\mathcal G_{c,I}}
{\delta_0Q_{B,I}}
}
\]

is scale invariant whenever the reference width \(\delta_0\) is fixed on the normalized record interval.

## 9. Optimized cutoff-current estimate

The corrected general-viscosity M18-023 Young estimate with arbitrary \(\chi\) gives

\[
|\mathcal C_\phi(t)|
\le
\varepsilon\nu^{-1}H_\phi(t)
+C_{\varepsilon}\nu\,
\mathcal E_t[\chi].
\]

Integrating over \(I\) and choosing the spacetime-optimal time-independent cutoff yields

\[
\boxed{
\int_I|\mathcal C_\phi|dt
\le
\varepsilon\nu^{-1}
\int_IH_\phi dt
+C_{\varepsilon}\nu\,
\mathcal G_{c,I}.
}
\]

Thus the canonical cutoff obstruction is not an essential supremum and not even the arithmetic quartic moment. It is the harmonic collar conductance \(\mathcal G_{c,I}\).

## 10. Refined failure branch

The cutoff-current branch is now

\[
\boxed{
G_{\rm cutoff\ current}
\Longrightarrow
G_{\rm absorbed\ coefficient\ rate}
\lor
G_{\rm high\ spacetime\ collar\ conductance}
\lor
G_{\rm collar/tube/domain\ loss}.
}
\]

A high conductance means that there is no coefficient-level bottleneck through which a time-independent cutoff can cheaply transition over the whole record interval.

This is a stronger and more representation-safe statement than saying that some point has large \(|\nabla\kappa|\).

## 11. Relation to M18-027 weighted-gradient moment

For a collar of length \(L_c\asymp\delta_0\),

\[
\mathcal G_{c,I}
\le
L_c^{-2}
\int_{s_-}^{s_+}\mathbb W_I(s)ds.
\]

By coarea,

\[
\int_{s_-}^{s_+}\mathbb W_I(s)ds
=
\int_I\int_{\mathcal K}ho^2g^4dxdt.
\]

Therefore the weighted arithmetic moment of M18-027 controls the conductance from above, while the harmonic conductance can be much smaller.

Hence the hierarchy is

\[
\boxed{
\text{essential-sup gradient}
\;\Rightarrow\;
\text{arithmetic weighted moment upper control}
\;\Rightarrow\;
\text{harmonic conductance obstruction},
}
\]

but none of the reverse implications is automatic.

## 12. Audit verdict

### Certified

1. The coefficient-cutoff problem is an exact weighted one-dimensional Dirichlet minimization problem.
2. The minimum cutoff cost is the harmonic conductance \(\mathcal G_c\).
3. A low-conductance coefficient bottleneck allows the cutoff current to be made small even if other levels have very large gradients.
4. A time-independent spacetime optimizer avoids introducing a \(\partial_t\chi\) term.
5. The spacetime conductance has exact scaling \(R^7\).

### Not certified

1. A uniform bound on \(\mathcal G_{c,I}\).
2. A standard Navier--Stokes ancestry ledger directly controlling \(\mathcal G_{c,I}\).
3. Elimination of a collar whose every coefficient level has high time-integrated conductance.
4. Elimination of trace-free Hessian/tube-geometry decompactification.
5. Global 3D Navier--Stokes regularity.

## 13. Next target

M18-029 should audit the high-conductance branch itself.

The natural question is whether

\[
\mathcal G_{c,I}
\]

can be large while the existing first-jet spacetime charge remains controlled. Because conductance is harmonic in coefficient level, a large value requires the absence of low-current bottlenecks across the entire transition interval. The next audit should convert that statement into either a quantitative lower bound on first-jet/raw-H2 occupation or an explicit level-geometry concentration exit.