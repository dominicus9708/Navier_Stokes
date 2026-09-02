# DSD M5-580 — Ergodic First Terminal-Residual Process

Date: 2026-09-02

Status: **ON THE GENUINELY PARABOLIC TERMINAL BRANCH, THE FIRST RESIDUAL C IS ITSELF A STATIONARY ERGODIC LOG-RADIUS PROCESS WITH POSITIVE MEAN SQUARE DENSITY. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. First terminal jet

The retained terminal expansion is

\[
u(x,s)
=
r^{-1}A(q,\omega)
+(-s)r^{-3}C(q,\omega)
+O(s^2r^{-5}),
\]

with

\[
C=\mathcal R_{stat}[A,P].
\]

M5-571 already showed that \(A\) is a stationary ergodic log-radius process on a hard component.

This note checks the transformation law of \(C\).

---

## 2. Navier-Stokes scaling of the terminal jet

For \(\lambda>0\), define the Navier-Stokes scaling

\[
u_\lambda(x,s)
:=
\lambda u(\lambda x,\lambda^2s).
\]

Insert the terminal expansion at \((\lambda x,\lambda^2s)\):

\[
\begin{aligned}
u_\lambda(x,s)
&=
\lambda\left[
(\lambda r)^{-1}A(q+\log\lambda,\omega)
+(-\lambda^2s)(\lambda r)^{-3}C(q+\log\lambda,\omega)
+\cdots
\right]
\\
&=
r^{-1}A(q+\log\lambda,\omega)
+(-s)r^{-3}C(q+\log\lambda,\omega)
+\cdots.
\end{aligned}
\]

Thus **both** terminal coefficients transform only by log-radius translation; there is no extra amplitude factor for \(C\):

\[
\boxed{
A_\lambda(q)=A(q+\log\lambda),
\qquad
C_\lambda(q)=C(q+\log\lambda).
}
\]

With the similarity-hull time convention used in M5-571,

\[
\boxed{
C_{\sigma_tY}(q,\omega)
=
C_Y(q-t/2,\omega),
}
\]

exactly in parallel with \(A\).

---

## 3. Pushforward invariant process

Let the terminal-jet factor map be

\[
\mathcal J:Y\mapsto(A_Y,C_Y).
\]

Push the ergodic similarity-hull measure \(\mu\) forward:

\[
\nu_J:=\mathcal J_\#\mu.
\]

Then \(\nu_J\) is invariant under simultaneous log translations

\[
T_h(A,C)(q)
=(A,C)(q-h).
\]

The factor is ergodic on the corresponding component.

Hence \((A,C)\) is a jointly stationary ergodic terminal-jet process on

\[
\mathbb R_q\times S^2.
\]

---

## 4. Dynamic vs stationary branch is an ergodic dichotomy

The property

\[
C\equiv0
\]

is invariant under every log translation.

Therefore on an ergodic terminal-jet component exactly one of the following occurs:

\[
\boxed{
C\equiv0\quad\nu_J\text{-a.e.}
}
\]

or

\[
\boxed{
C\not\equiv0\quad\nu_J\text{-a.e.}
}
\]

in the invariant-factor sense.

Thus the S/J split of M5-577 is not merely pointwise bookkeeping; it can be taken componentwise in the ergodic decomposition.

---

## 5. Positive residual density on J

Define the unit-cell residual charge

\[
\mathcal C_2(C)
:=
\int_0^1\int_{S^2}|C(q,\omega)|^2d\omega\,dq.
\]

On the compact regular terminal-jet class this is finite and nonnegative.

On a genuinely dynamic ergodic component, if

\[
\int\mathcal C_2\,d\nu_J=0,
\]

then \(C=0\) almost everywhere and, by the retained regularity, identically, contradicting the definition of the J branch.

Therefore

\[
\boxed{
c_C:=\int\mathcal C_2\,d\nu_J>0.
}
\]

By Birkhoff,

\[
\boxed{
\frac1L
\int_0^L\int_{S^2}|C(q,\omega)|^2d\omega\,dq
\longrightarrow c_C>0
}
\]

for \(\nu_J\)-almost every dynamic terminal jet.

Thus the first parabolic residual is not sparse in log radius.

---

## 6. Terminal time-derivative interpretation

Away from the singular core,

\[
\boxed{
\partial_su(x,0^-)
=
-r^{-3}C(\log r,\omega).
}
\]

Consequently the critical weighted terminal time-derivative moment

\[
K_C(R)
:=
\int_{1<|x|<R}|x|^3|\partial_su(x,0^-)|^2dx
\]

satisfies

\[
\begin{aligned}
K_C(R)
&=
\int_1^R
r^3r^{-6}r^2dr
\int_{S^2}|C(\log r,\omega)|^2d\omega
\\
&=
\boxed{
\int_0^{\log R}\int_{S^2}|C(q,\omega)|^2d\omega\,dq.
}
\end{aligned}
\]

Hence on the dynamic ergodic branch,

\[
\boxed{
\frac{K_C(R)}{\log R}
\longrightarrow c_C>0.
}
\]

So J carries a positive-density critical terminal acceleration/residual tower.

---

## 7. Combine with the momentum cancellation

M5-574 gives

\[
\mathcal F_A'=-m_C,
\qquad
m_C(q)=\int_{S^2}C(q,\omega)d\omega,
\]

and therefore

\[
\boxed{\langle m_C\rangle=0.}
\]

Together with

\[
\boxed{\langle|C|^2\rangle=c_C>0,}
\]

this proves that the dynamic residual is necessarily **fluctuating/projective** rather than a nonzero constant net force.

Its positive quadratic density survives even though its net vector mean vanishes.

---

## 8. Residual channel split

Write

\[
C=\overline C+C^\perp,
\]

where

\[
\overline C(q)
=\frac1{4\pi}\int_{S^2}C(q,\omega)d\omega,
\qquad
\int_{S^2}C^\perp d\omega=0.
\]

Then

\[
\boxed{
\langle\overline C\rangle=0,
}
\]

while

\[
\boxed{
\langle|\overline C|^2\rangle
+\langle|C^\perp|^2\rangle
=c_C>0.
}
\]

Thus at least one of two positive-density dynamic channels remains:

1. oscillatory net-force mode \(\overline C\);
2. spherical-mean-zero/projective mode \(C^\perp\).

---

## 9. Updated J endpoint

The dynamic terminal branch now obeys

\[
\boxed{
\begin{gathered}
C\neq0,\\
\langle|C|^2\rangle=c_C>0,\\
\langle m_C\rangle=0,\\
\langle\mathcal D_A\rangle
=\langle\Phi_E\rangle+\langle A\cdot C\rangle.
\end{gathered}
}
\]

The next efficient target is to derive the second terminal jet. Since \(C\) has positive log-density, its own stationary residual should be balanced by the next \((-s)^2r^{-5}\) coefficient. This tests whether an infinite parabolic terminal-jet hierarchy can remain bounded/recurrent or whether some weighted analytic norm must grow factorially/secularly.

Status: **THE DYNAMIC TERMINAL RESIDUAL HAS BEEN UPGRADED TO A POSITIVE-DENSITY ERGODIC CRITICAL PROCESS. GLOBAL REGULARITY REMAINS UNPROVED.**