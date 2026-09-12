# DSD M19-141 — Uniform transverse contraction restores the recurrent-to-relative-periodic reduction after the M19-120 correction

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-120 CORRECTLY BLOCKED THE SHORTCUT FROM ONE-DIMENSIONAL CENTER TO PERIODICITY WHEN UNSTABLE DIRECTIONS WERE ALLOWED / M19-132 REMOVES POSITIVE OBSERVABLE HARD EXPONENTS / IF THE REMAINING SYMMETRY-TRANSVERSE SPECTRUM IS UNIFORMLY SEPARATED FROM ZERO, THE QUOTIENT FLOW HAS EXPONENTIAL TRANSVERSE CONTRACTION AND EVERY RECURRENT POINT IS LOCKED TO A PERIODIC ORBIT / LIFTING GIVES RSS/RDSS / THE ZERO-CENTER SPECTRAL GAP REMAINS THE LIVE GATE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why M19-120 was necessary

The statement

\[
\dim E^c=1
\]

alone does not imply periodic recurrent dynamics.
A hyperbolic flow may have

\[
E^s\oplus E^c\oplus E^u,
\qquad
\dim E^c=1,
\]

and still support aperiodic recurrence through the unstable bundle.

M19-120 therefore replaced the old shortcut by the stronger transverse target.

---

## 2. Positive transverse growth is now removed on the observable hard lane

M19-132 proves, under differentiated scattering equivariance and uniform hard-mode observability,

\[
\boxed{E_{\perp}^{>0}=0.}
\]

M19-133 strengthens complete hard dynamics to a scattering-pullback isometry.

Thus the only possible obstruction to strict transverse stability is an additional zero-growth transverse direction.

---

## 3. Zero-center rigidity plus spectral separation

Assume the remaining zero-center theorem holds after rotation quotient:

\[
\boxed{
E_q^0
=
\operatorname{span}\{\partial_sU\}.
}
\]

Assume also that the symmetry-transverse Sacker--Sell spectrum is uniformly separated from zero over the compact recurrent corridor.

Since positive transverse spectrum is absent, compactness gives a number

\[
\gamma>0
\]

such that

\[
\boxed{
\Sigma_{SS}^{\perp}
\subset(-\infty,-\gamma].
}
\]

Equivalently, the transverse linear cocycle satisfies a uniform exponential estimate

\[
\boxed{
\|\Phi_t^{\perp}(U)\|
\le
C e^{-\gamma t}
\qquad(t\ge0)
}
\]

on the quotient recurrent corridor.

This is the precise strengthening missing in the pre-M19-120 argument.

---

## 4. Recurrent return map

Let `[U(s)]` denote the rotation-quotient orbit.
Take a recurrent point and a sequence

\[
T_n\to\infty,
\qquad
[U(T_n)]\to[U(0)].
\]

Choose a local codimension-one section `Sigma` transverse to the flow at `[U(0)]`.
For sufficiently close returns, the flow defines a Poincare return map

\[
\mathcal P_n:\Sigma_{loc}\to\Sigma.
\]

The derivative of this return map acts only on the symmetry-transverse directions.
The uniform exponential bound gives

\[
\boxed{
\|D\mathcal P_n\|
\le
C e^{-\gamma T_n}
}
\]

up to the uniformly bounded local flow-box coordinate factors.

For large `n`,

\[
\|D\mathcal P_n\|<1.
\]

Hence `P_n` is a contraction on a sufficiently small return neighborhood.

---

## 5. Contraction forces an actual periodic point

By the contraction mapping theorem, the close return has a unique fixed point in the local section.
That fixed point lies on a periodic orbit of the quotient flow.

Because the original recurrent point shadows the exponentially attracting transverse fiber and returns arbitrarily close, recurrence excludes a distinct forward-asymptotic but nonperiodic orbit in the same local stable leaf.

Thus the recurrent quotient orbit itself belongs to the periodic orbit.

Schematically,

\[
\boxed{
\text{quotient recurrence}
+
\text{uniform transverse contraction}
\Longrightarrow
\text{quotient periodicity}.
}
\]

---

## 6. Lift through rotation symmetry

A periodic orbit in the rotation quotient means that for some

\[
S>0,
\qquad
Q_*\in SO(3),
\]

we have

\[
\boxed{
U(s+S)=Q_*U(s).
}
\]

Thus the physical similarity solution is RDSS.

Special cases are:

- `Q_*=Id`: ordinary DSS;
- a continuous relative equilibrium: RSS;
- stationary quotient equilibrium with no group drift: ordinary self-similar profile.

Therefore, under the strengthened spectral hypotheses,

\[
\boxed{
\mathcal R_{critical}^{recurrent}
\Longrightarrow
\mathcal R_{RSS/RDSS}.
}
\]

This is the corrected form of the earlier M19-103 reduction.

---

## 7. Exact remaining gate

Because M19-132 has already removed positive exponents, the recurrent-to-relative-periodic reduction now fails only if

\[
\boxed{
\text{there exists an extra symmetry-transverse zero spectral channel}
}
\]

or if the uniform spectral-separation/application gates fail.

Hence the main aperiodic spectral theorem is reduced to

\[
\boxed{
\mathcal T_{zero-center}:
E_q^0=\operatorname{span}\{\partial_sU\}.
}
\]

This is strictly narrower than the M19-120 target `E_perp^{>=0}=0` because positive growth has been eliminated independently by scattering observability.

---

## 8. Firewalls

The present reduction requires **uniform** transverse contraction.
It must not be inferred merely from:

- nonpositive Lyapunov exponents almost everywhere;
- absence of a second eigenvector at one time;
- pointwise spectral gaps without a compact-corridor Sacker--Sell gap.

Thus

\[
\boxed{
\text{zero-center rigidity}
+
\text{uniform spectral separation}
\Longrightarrow
\text{periodic reduction},
}

not zero-center dimension alone.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
