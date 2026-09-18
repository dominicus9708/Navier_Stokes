# M19-409 — Stationary terminal energy flux is the positive future resolvent of critical dissipation

Date: 2026-09-19

Status: **NEW EXACT STATIONARY RESOLVENT / ON THE STATIONARY TERMINAL BRANCH \`C=0\`, M5-575 REDUCES POINTWISE IN LOG RADIUS TO \`Phi_E'-Phi_E=-D_A\`. FOR ANY BOUNDED RECURRENT PROFILE, THE UNIQUE BOUNDED SOLUTION IS THE FORWARD EXPONENTIAL RESOLVENT \`Phi_E(q)=int_0^infty e^{-s}D_A(q+s)ds\`. HENCE THE SCALE-NORMALIZED ENERGY FLUX IS NONNEGATIVE AT EVERY LOG RADIUS, AND IT IS STRICTLY POSITIVE AT EVERY Q ON ANY NONTRIVIAL BOUNDED RECURRENT STATIONARY PROFILE. IN PARTICULAR THE NONTRIVIAL ZERO-FORCE LOG-DILATION SURVIVOR OF M19-407--408 CARRIES STRICTLY POSITIVE OUTWARD CRITICAL ENERGY FLUX THROUGH EVERY SPHERE, EVEN THOUGH ITS MOMENTUM/STRESS FORCE FLUX VANISHES. THIS IDENTIFIES A SCALAR ENERGY-DEFECT/INNER-SUPPLY CHANNEL DISTINCT FROM VECTOR POINT FORCE; IT IS NOT YET EXCLUDED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pointwise stationary terminal energy law

M5-575 gives

\[
\Phi_E'(q)-\Phi_E(q)
=
\mathcal C_{AC}(q)-\mathcal D_A(q).
\]

On the stationary terminal branch,

\[
C=0,
\]

so

\[
\mathcal C_{AC}=0.
\]

Therefore

\[
\boxed{
\Phi_E'(q)-\Phi_E(q)
=
-\mathcal D_A(q),
}
\]

where

\[
\mathcal D_A(q)
=
\int_{S^2}
\left(
|(\partial_q-1)A|^2
+
|\nabla_{S^2}A|^2
\right)d\omega
\ge0.
\]

---

## 2. Solve the bounded recurrent ODE

Rewrite as

\[
\frac d{dq}
\left(
e^{-q}\Phi_E(q)
\right)
=
-e^{-q}\mathcal D_A(q).
\]

For \(Q>q\),

\[
e^{-Q}\Phi_E(Q)
-
e^{-q}\Phi_E(q)
=
-\int_q^Q
e^{-s}\mathcal D_A(s)\,ds.
\]

Since \(\Phi_E\) is bounded on the compact recurrent hull,

\[
e^{-Q}\Phi_E(Q)\to0
\qquad
(Q\to+\infty).
\]

Hence

\[
e^{-q}\Phi_E(q)
=
\int_q^\infty
e^{-s}\mathcal D_A(s)\,ds.
\]

Multiplying by \(e^q\),

\[
\boxed{
\Phi_E(q)
=
\int_q^\infty
e^{q-s}\mathcal D_A(s)\,ds
=
\int_0^\infty
e^{-\tau}\mathcal D_A(q+\tau)\,d\tau.
}
\]

This is the exact stationary resolvent formula.

---

## 3. Pointwise positivity

Because

\[
\mathcal D_A\ge0,
\]

the resolvent immediately gives

\[
\boxed{
\Phi_E(q)\ge0
\qquad
\forall q.
}
\]

Suppose for some \(q_0\),

\[
\Phi_E(q_0)=0.
\]

Then the nonnegative integral implies

\[
\mathcal D_A(q_0+\tau)=0
\]

for almost every \(\tau\ge0\), and by continuity,

\[
\mathcal D_A(q)=0
\qquad
\forall q\ge q_0.
\]

Thus

\[
(\partial_q-1)A=0,
\qquad
\nabla_{S^2}A=0
\]

on the forward half-line.

The angular equation says \(A\) is independent of \(\omega\), while

\[
\partial_qA=A
\]

gives

\[
A(q)=e^{q-q_0}A(q_0).
\]

Bounded recurrence forces

\[
A(q_0)=0.
\]

Hence \(A=0\) on the forward orbit, and by recurrence/continuation the supported stationary profile is trivial.

Therefore on a nontrivial bounded recurrent stationary profile,

\[
\boxed{
\Phi_E(q)>0
\qquad
\forall q.
}
\]

---

## 4. Mean identity is recovered automatically

Taking invariant \(q\)-means,

\[
\langle\Phi_E\rangle
=
\int_0^\infty
e^{-\tau}
\langle\mathcal D_A\rangle
\,d\tau.
\]

Thus

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle,
}
\]

recovering M5-575's stationary payer identity.

M19-409 strengthens it from an averaged equality to a pointwise-in-\(q\) positive resolvent.

---

## 5. Physical sphere energy flux

The physical energy flux through \(S_r\) is

\[
\int_{S_r}J_A\cdot n\,dS
=
r^{-1}\Phi_E(\log r).
\]

Therefore every sphere in the stationary recurrent hard tail carries

\[
\boxed{
\int_{S_r}J_A\cdot n\,dS
>0.
}
\]

With the standard outward normal convention, this is an outward energy flux.

The stationary local energy law gives

\[
\nabla\cdot J_A
=
-|\nabla v|^2.
\]

Thus the outward flux decreases with radius as dissipation is paid in the intervening shells.

---

## 6. Combine with M19-407--408

M19-407 gives on a nontrivial smooth zero-force recurrent tail

\[
D_q
=
\left\langle
\int_{S^2}|\partial_qA|^2d\omega
\right\rangle
>0.
\]

M19-408 gives

\[
\langle\mathcal D_A\rangle
=
D_q+E_A+D_S.
\]

Therefore

\[
\boxed{
\langle\Phi_E\rangle
=
D_q+E_A+D_S
>0.
}
\]

More strongly, the pointwise resolvent implies

\[
\boxed{
\Phi_E(q)>0
}
\]

at every log radius.

So the zero-force recurrent survivor has:

\[
\boxed{
\text{zero vector momentum-force flux}
\quad+\quad
\text{strictly positive scalar energy flux}.
}
\]

---

## 7. This does not yet contradict zero force

The momentum stress flux is vector-valued:

\[
\mathcal F_A
=
\int_{S^2}\mathbb T_Ae_r\,d\omega.
\]

Zero force means

\[
\boxed{
\mathcal F_A=0.
}
\]

The energy flux is a different scalar quantity,

\[
\Phi_E
=
r\int_{S_r}J_A\cdot n\,dS.
\]

There is no algebraic implication

\[
\mathcal F_A=0
\Rightarrow
\Phi_E=0.
\]

Thus M19-409 identifies a real surviving channel rather than an immediate contradiction.

---

## 8. Interpretation: scalar inner energy supply

The stationary \(1/r\) hard tail dissipates a positive critical amount on every active log-radius phase.

The resolvent shows that this dissipation is sustained by energy flowing outward from smaller radii.

For the zero-force branch, that inner energy supply is present despite zero net vector point force.

Hence the remaining hard endpoint may be viewed as a potential

\[
\boxed{
\text{zero-momentum-force but positive-energy-flux singular core}.
}
\]

Whether such a core is compatible with the inherited suitable/ancient Navier--Stokes structure is now a sharper rigidity question.

---

## 9. Updated stationary zero-force target

The previous gate

\[
\mathcal T_{dil-stress}^{zero-force}
\]

refines to

\[
\boxed{
\mathcal T_{energy-force}^{zero}:
\text{classify/exclude a smooth stationary recurrent }1/r\text{ tail with}
}
\]

\[
\boxed{
\mathcal F_A=0,
\qquad
\Phi_E(q)>0\ \forall q,
\qquad
D_q>0.
}
\]

Possible closures:

1. a suitable/local-energy condition inherited through the blow-down;
2. a distributional defect theorem showing positive critical energy supply forces nonzero momentum defect or another forbidden source;
3. a stationary log-cylinder stress-energy identity;
4. a spectral/virial rigidity theorem.

---

## 10. Double-counting firewall

The positive energy flux is not a new additive resource independent of \(\mathcal D_A\).

It is exactly the resolvent payer of the same dissipation:

\[
\boxed{
\Phi_E
=
(1-\partial_q)^{-1}\mathcal D_A
}
\]

on bounded recurrent stationary profiles.

Thus it should be used as a structural sign/transport statement, not summed as an additional cost.

---

\[
\boxed{\text{M19-409 COMPLETE; STATIONARY TERMINAL ENERGY FLUX IS STRICTLY POSITIVE POINTWISE ON EVERY NONTRIVIAL BOUNDED RECURRENT HARD TAIL.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
