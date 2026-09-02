# DSD M5-574 — First-Jet Momentum / Stress-Flux Cancellation

Date: 2026-09-02

Status: **THE SPHERICAL MEAN OF THE FIRST PARABOLIC RESIDUAL C IS THE LOG-RADIUS DERIVATIVE OF A BOUNDED CRITICAL MOMENTUM-STRESS FLUX. RECURRENCE FORCES ZERO SIGNED MEAN NET-FORCE RESIDUAL. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Momentum form

For an incompressible Navier-Stokes solution with viscosity normalized to one,

\[
\partial_su+(u\cdot\nabla)u
=-\nabla p+\Delta u,
\qquad
\nabla\cdot u=0,
\]

define

\[
\boxed{
\mathbb T
:=
\nabla u+(\nabla u)^T
-u\otimes u-pI.
}
\]

Then

\[
\boxed{
\partial_su
=
\nabla\cdot\mathbb T.
}
\]

---

## 2. Leading critical stress

From M5-572,

\[
u(x,s)
=
r^{-1}A(q,\omega)
+(-s)r^{-3}C(q,\omega)+\cdots,
\]

\[
p(x,s)
=
r^{-2}P(q,\omega)+\cdots.
\]

The leading stress therefore has the form

\[
\boxed{
\mathbb T_0(x)
=
r^{-2}\mathbb S_A(q,\omega),
}
\]

where \(\mathbb S_A\) is built from first log-spherical derivatives of \(A\), the quadratic term \(A\otimes A\), and \(P\).

The first time derivative is

\[
\boxed{
\partial_su
=
-r^{-3}C(q,\omega)+O((-s)r^{-5}).
}
\]

Hence at leading \(r^{-3}\) order,

\[
\boxed{
\nabla\cdot(r^{-2}\mathbb S_A)
=
-r^{-3}C.
}
\]

---

## 3. Scale-normalized sphere stress flux

Define

\[
\boxed{
\mathcal F_A(q)
:=
\int_{S^2}
\mathbb S_A(q,\omega)e_r\,d\omega.
}
\]

This is exactly the physical stress flux through \(S_r\) for the leading critical field, because

\[
dS=r^2d\omega
\]

cancels the \(r^{-2}\) stress scaling.

Thus \(\mathcal F_A\) is a scale-critical vector observable depending only on \(q=\log r\).

---

## 4. Exact radial flux derivative

Integrate the leading momentum equation over the shell

\[
\{e^{q_1}<r<e^{q_2}\}.
\]

The divergence theorem gives

\[
\mathcal F_A(q_2)-\mathcal F_A(q_1)
=
-\int_{q_1}^{q_2}
\int_{S^2}C(q,\omega)d\omega\,dq.
\]

Therefore, in distributional/classical log-radius form,

\[
\boxed{
\frac{d}{dq}\mathcal F_A(q)
=
-m_C(q),
}
\]

where

\[
\boxed{
m_C(q):=\int_{S^2}C(q,\omega)d\omega.}
\]

This is the exact first-terminal-jet net-momentum relation.

---

## 5. Recovery of the stationary defect invariant

If

\[
C=0,
\]

then

\[
\boxed{
\mathcal F_A'(q)=0,
}
\]

so

\[
\mathcal F_A(q)\equiv\kappa,
\]

recovering M5-573's radius-independent stationary stress defect.

Thus the Landau point-force vector is the stationary special case of the more general first-jet stress-flux observable.

---

## 6. Recurrent dynamic branch

On the compact regular log-profile factor, \(\mathcal F_A(q)\) is a bounded observable along log-radius translation.

Hence

\[
\frac{\mathcal F_A(L)-\mathcal F_A(0)}{L}
\to0
\qquad(L\to\infty).
\]

Using the exact derivative identity,

\[
\boxed{
\frac1L
\int_0^Lm_C(q)dq
\to0.
}
\]

Equivalently, in invariant-measure notation,

\[
\boxed{
\langle m_C\rangle=0.
}
\]

Thus the spherical-mean component of the first parabolic residual cannot have a nonzero secular sign/mean on a recurrent hard component.

---

## 7. What this does and does not remove

This is a genuine cancellation law but not a contradiction.

It excludes

\[
\boxed{
\text{persistent one-sign net-force residual in }C.
}
\]

However, it allows:

1. oscillatory net-force residual with zero mean;
2. large spherical-mean-zero components of \(C\);
3. stationary \(C=0\) profiles with constant nonzero stress defect \(\kappa\).

Therefore the full residual norm

\[
\int_{S^2}|C|^2d\omega
\]

is not controlled by the signed vector mean \(m_C\).

---

## 8. DSD channel separation

The first terminal residual decomposes naturally into

\[
\boxed{
C
=
\overline C(q)
+C^\perp(q,\omega),
}
\]

where

\[
\overline C(q)
=
\frac1{4\pi}m_C(q),
\qquad
\int_{S^2}C^\perp d\omega=0.
\]

The net-force channel obeys the exact coboundary law

\[
\boxed{
4\pi\overline C
=-\mathcal F_A'.
}
\]

while \(C^\perp\) is invisible to total momentum flux and requires a different moment/projective observable.

This mirrors the earlier distinction between scalar material flux and projective directional diffusion: different projections must not be conflated.

---

## 9. Updated dynamic endpoint

The genuinely parabolic terminal branch now has

\[
\boxed{
\begin{gathered}
C=\mathcal R_{stat}[A,P]\neq0,\\
\mathcal F_A'=-m_C,\\
\langle m_C\rangle=0.
\end{gathered}
}
\]

The next efficient target is the mean-zero residual channel \(C^\perp\): construct the lowest tensor/spherical-harmonic stress moments that see it, determine which parts are again bounded coboundaries, and isolate any component that has a genuine positive production sign.

Status: **THE FIRST-JET NET-FORCE RESIDUAL HAS BEEN REDUCED TO A ZERO-MEAN COBoundary. THE REMAINING DYNAMIC TERMINAL OBSTRUCTION LIVES IN OSCILLATORY NET FORCE AND SPHERICAL-MEAN-ZERO RESIDUAL MODES. GLOBAL REGULARITY REMAINS UNPROVED.**