# DSD M19-132 — Differentiated scattering equivariance plus uniform hard-mode observability excludes positive Lyapunov exponents

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT SCATTERING COVARIANCE IS DIFFERENTIATED ON THE FINITE HARD BUNDLE / IN A TRANSLATION-INVARIANT SCATTERING NORM, UNIFORM OBSERVABILITY FORCES THE HARD TANGENT COCYCLE TO HAVE NO POSITIVE LYAPUNOV EXPONENT / THE HYPERBOLIC-UNSTABLE ESCAPE INTRODUCED BY THE M19-120 CORRECTION IS REMOVED ON THIS APPLICATION LANE / EXTRA ZERO-CENTER DIRECTIONS MAY STILL REMAIN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact scattering covariance

On the controlled spectator branch, the nonlinear scattering map satisfies

\[
\boxed{
\mathscr S(\sigma_tU)
=
T_{-t/2}\mathscr S(U),
}
\]

where `sigma_t` is similarity-time evolution and

\[
(T_aA)(q,\omega)=A(q+a,\omega)
\]

is log-radius translation.

Let

\[
\Phi_t(U):=D\sigma_t(U)
\]

be the linearized interior cocycle.

Differentiating the exact covariance gives

\[
\boxed{
D\mathscr S_{\sigma_tU}\,\Phi_t(U)
=
T_{-t/2}\,D\mathscr S_U.
}
\]

This is an exact intertwining relation, not an asymptotic estimate.

---

## 2. Translation-invariant scattering norm

Let `X_sc` be a scattering-history norm on the retained hard tangent class for which

\[
\boxed{
\|T_aB\|_{X_{sc}}=\|B\|_{X_{sc}}
}
\]

for all real `a`.

A natural model is a uniformly local / bounded-history norm in `q`, strong enough to retain the spectator derivative regularity but not weighted in a way that breaks q-translation invariance.

This norm choice is an explicit application gate.

---

## 3. Uniform hard-mode observability

By M19-131, once the hard spectral spaces form a continuous finite-rank bundle over a compact corridor and the scattering derivative is fiberwise injective, compactness upgrades injectivity to uniform norm equivalence on the hard bundle.

Assume therefore

\[
\boxed{
 c_{sc}\|v\|_H
\le
\|D\mathscr S_Uv\|_{X_{sc}}
\le
C_{sc}\|v\|_H
}
\]

for every hard mode

\[
v\in E_h(U),\qquad U\in K,
\]

with constants independent of `U`.

The upper bound follows from continuity on the compact unit hard bundle.
The lower bound is the M19-131 observability conclusion, now taken in the translation-invariant scattering norm.

---

## 4. Uniform forward bound for the hard tangent cocycle

Let

\[
v_t:=\Phi_t(U)v.
\]

Apply the lower observability estimate at the evolved background:

\[
 c_{sc}\|v_t\|_H
\le
\|D\mathscr S_{\sigma_tU}v_t\|_{X_{sc}}.
\]

Use exact differentiated equivariance:

\[
\|D\mathscr S_{\sigma_tU}v_t\|_{X_{sc}}
=
\|T_{-t/2}D\mathscr S_Uv\|_{X_{sc}}.
\]

Translation invariance gives

\[
=
\|D\mathscr S_Uv\|_{X_{sc}}
\le
C_{sc}\|v\|_H.
\]

Hence

\[
\boxed{
\|\Phi_t(U)v\|_H
\le
\frac{C_{sc}}{c_{sc}}\|v\|_H
\qquad(t\ge0)
}
\]

for every hard tangent vector whose orbit stays in the certified hard bundle.

This is uniform in time.

---

## 5. Positive Lyapunov exponents are impossible

For a nonzero hard mode define

\[
\lambda(v)
=
\limsup_{t\to\infty}
\frac1t\log\frac{\|\Phi_t(U)v\|_H}{\|v\|_H}.
\]

The uniform bound immediately yields

\[
\boxed{
\lambda(v)\le0.
}
\]

Therefore

\[
\boxed{
E_h^{>0}=\{0\}.
}
\]

In particular, on the uniformly observable hard corridor,

\[
\boxed{
E_{\perp}^{>0}=0.
}
\]

This removes the hyperbolic-unstable mechanism that forced the authoritative M19-120 correction.

---

## 6. What remains after eliminating positive exponents

M19-120 correctly warned that

\[
E^c_{extra}=0
\]

alone does not rule out aperiodic hyperbolic recurrence if positive transverse exponents are allowed.

M19-132 removes precisely that loophole on the scattering-observable hard bundle.
The remaining nonnegative transverse spectrum is therefore purely zero-growth:

\[
\boxed{
E_{\perp}^{\ge0}=E_{\perp}^{0}.
}
\]

Hence the full transverse theorem now reduces again to the finite-dimensional zero-center statement

\[
\boxed{
E_{\perp}^{0}
=\text{symmetry-generated neutral directions only}.
}
\]

After rotation quotient this is

\[
\boxed{
E_q^0=\operatorname{span}\{\partial_sU\}.
}
\]

Thus the corrected strategy is:

1. differentiated scattering equivariance + uniform observability eliminates **positive** transverse exponents;
2. the quarter-gap / compact-core spectral theorem must eliminate **extra zero** transverse exponents;
3. only after both statements can recurrent dynamics be reduced to the symmetry/relative-periodic center manifold.

---

## 7. Reverse-time remark

If, on a complete finite-dimensional center bundle, the hard cocycle is invertible for all positive and negative times and the same uniform observability estimates hold along the complete orbit, the argument applied backward gives a matching lower bound and hence

\[
\lambda(v)=0.
\]

This stronger statement should **not** be applied to arbitrary stable parabolic directions without a certified backward-complete finite-dimensional bundle.

The forward conclusion

\[
\lambda\le0
\]

is the unconditional conclusion of the present calculation under the stated gates.

---

## 8. Failure routing

If a positive hard exponent appears despite the formal scattering factor, at least one gate must fail:

\[
\boxed{
G_{\lambda>0}
\Longrightarrow
G_{spectral-bundle}
\lor
G_{scattering-differentiability}
\lor
G_{translation-norm}
\lor
G_{observability}
\lor
G_{spectator-compactness}.
}
\]

By M19-131, most of these failures already route to spectral degeneration or application-gate loss.

---

## 9. Updated principal analytic target

On the certified compact hard corridor, the major spectral problem is reduced from

\[
E_{\perp}^{\ge0}=0
\]

to

\[
\boxed{
\mathcal T_{zero-center}:
E_{\perp}^{0}
=E_{sym}^{0}.
}
\]

That is a finite-dimensional compact-core zero-eigenchannel problem.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
