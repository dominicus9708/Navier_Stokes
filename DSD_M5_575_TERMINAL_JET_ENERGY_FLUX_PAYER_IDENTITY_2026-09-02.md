# DSD M5-575 — Terminal-Jet Energy-Flux Payer Identity

Date: 2026-09-02

Status: **THE POSITIVE LOG-CELL DISSIPATION OF THE CRITICAL TERMINAL TRACE IS PAID EXACTLY BY SCALE-NORMALIZED ENERGY FLUX AND/OR CORRELATION WITH THE FIRST PARABOLIC RESIDUAL. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Leading critical field and residual

Let

\[
v(x)=r^{-1}A(q,\omega),
\qquad
p_0(x)=r^{-2}P(q,\omega),
\]

and let its stationary Navier-Stokes residual be

\[
\boxed{
R_A
:=-\Delta v+(v\cdot\nabla)v+\nabla p_0
=r^{-3}C(q,\omega).
}
\]

By M5-572, \(C\) is exactly the first parabolic terminal-jet coefficient.

---

## 2. Exact energy identity for a nonstationary residual

Dot the residual equation with \(v\). Using \(\nabla\cdot v=0\),

\[
\boxed{
v\cdot R_A
=|
abla v|^2+\nabla\cdot J_A,
}
\]

where one may take the stationary energy-flux vector

\[
\boxed{
J_A
:=
\left(\frac12|v|^2+p_0\right)v
-\nabla\left(\frac12|v|^2\right).
}
\]

All terms have the critical scaling

\[
v\cdot R_A\sim r^{-4},
\qquad
|
abla v|^2\sim r^{-4},
\qquad
J_A\sim r^{-3}.
\]

---

## 3. Log-cell dissipation density

For \(v=r^{-1}A\),

\[
|
abla v|^2
=r^{-4}
\left(
|(
partial_q-1)A|^2
+|
abla_{S^2}A|^2
\right).
\]

Define

\[
\boxed{
\mathcal D_A(q)
:=
\int_{S^2}
\left[
|(
partial_q-1)A|^2
+|
abla_{S^2}A|^2
\right]d\omega.
}
\]

This is nonnegative and is the natural critical dissipation per unit log radius.

The residual correlation is

\[
\boxed{
\mathcal C_{AC}(q)
:=
\int_{S^2}A(q,\omega)\cdot C(q,\omega)d\omega.
}
\]

---

## 4. Scale-normalized physical energy flux

Because \(J_A\sim r^{-3}\), the physical energy flux through \(S_r\) scales as \(r^{-1}\).

Define its scale-normalized version

\[
\boxed{
\Phi_E(q)
:=
r
\int_{|x|=r}J_A\cdot n\,dS.
}
\]

Then \(\Phi_E\) is an order-one observable on the compact log-profile hull.

Writing

\[
\int_{S_r}J_A\cdot n\,dS
=r^{-1}\Phi_E(q)
\]

and differentiating the shell energy identity gives

\[
\boxed{
\Phi_E'(q)-\Phi_E(q)
=
\mathcal C_{AC}(q)-\mathcal D_A(q).
}
\]

The extra \(-\Phi_E\) term is the exact homogeneity correction: the *physical* energy flux decays like \(1/r\), while \(\Phi_E\) is its scale-normalized amplitude.

---

## 5. Ergodic mean payer identity

On the compact recurrent log-radius factor, \(\Phi_E\) is bounded. Hence

\[
\langle\Phi_E'\rangle=0.
\]

Averaging the exact identity yields

\[
-\langle\Phi_E\rangle
=
\langle\mathcal C_{AC}\rangle
-\langle\mathcal D_A\rangle.
\]

Therefore

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle
-
\langle\mathcal C_{AC}\rangle.
}
\]

This is the first exact terminal-jet energy payer identity.

---

## 6. Interpretation

The positive critical dissipation density

\[
\langle\mathcal D_A\rangle\ge0
\]

must be paid by two channels:

1. scale-normalized radial energy flux
   \[
   \langle\Phi_E\rangle;
   \]
2. correlation with the first parabolic terminal residual
   \[
   \langle\mathcal C_{AC}\rangle
   =
   \left\langle\int A\cdot C\right\rangle.
   \]

Equivalently,

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\langle\mathcal C_{AC}\rangle.
}
\]

This does **not** imply a contradiction because neither payer has a fixed sign under the current assumptions.

---

## 7. Stationary branch

If

\[
C=0,
\]

then

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle.
}
\]

Thus any nontrivial stationary critical terminal profile must carry a positive mean scale-normalized energy flux sufficient to pay its dissipation.

For a homogeneous Landau-type branch this is naturally interpreted as energy supplied by the terminal point-defect/stress source.

Therefore the Landau defect is visible not only in momentum flux but also in the critical energy ledger.

---

## 8. Dynamic branch

If

\[
C\neq0,
\]

then parabolic terminal evolution can pay part or all of the critical dissipation through

\[
\mathcal C_{AC}.
\]

Hence a proof attempting to show that radial energy flux alone must be positive is invalid unless it first controls \(A\cdot C\).

The correct dynamic branch is

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\langle A\cdot C\rangle.
}
\]

---

## 9. Hardy-excess form

Expanding the radial derivative term,

\[
|(
partial_q-1)A|^2-|A|^2
=
|
partial_qA|^2
-
partial_q|A|^2.
\]

Therefore the weighted viscous-Hardy excess has ergodic mean

\[
\boxed{
\left\langle
\int_{S^2}
\left(
|(
partial_q-1)A|^2
+|
abla_{S^2}A|^2
-|A|^2
\right)d\omega
\right\rangle
=
\left\langle
\int_{S^2}
\left(
|
partial_qA|^2
+|
abla_{S^2}A|^2
\right)d\omega
\right\rangle
\ge0.
}
\]

This explains why the critical \(1/r\) tail saturates the radial Hardy scaling: only genuine log-radius/angular variation produces positive excess after averaging.

---

## 10. Updated frontier

The terminal hard core now carries simultaneous exact ledgers:

\[
\boxed{
\mathcal F_A'=-m_C
}
\]

from momentum, and

\[
\boxed{
\Phi_E'-\Phi_E
=
\mathcal C_{AC}-\mathcal D_A
}
\]

from energy.

Their invariant means give

\[
\boxed{
\langle m_C\rangle=0,
\qquad
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\langle A\cdot C\rangle.
}
\]

The next useful gate is to decide whether either payer on the right can be independently forced to vanish on the unforced recurrent ancient branch. If both vanished, the profile would have zero log/angular dissipation and collapse to the already classified homogeneous kernel.

Status: **THE TERMINAL ENERGY LEDGER HAS BEEN REDUCED TO TWO PAYERS: SCALE-NORMALIZED ENERGY FLUX AND PARABOLIC RESIDUAL CORRELATION. GLOBAL REGULARITY REMAINS UNPROVED.**