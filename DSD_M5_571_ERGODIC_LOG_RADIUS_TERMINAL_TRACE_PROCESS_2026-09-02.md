# DSD M5-571 — Ergodic Log-Radius Terminal-Trace Process

Date: 2026-09-02

Status: **THE HARD TERMINAL TAIL IS A STATIONARY ERGODIC PROCESS IN LOG RADIUS. NONTRIVIALITY FORCES POSITIVE MEAN CUBIC AND TERMINAL-VORTICITY DENSITIES. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Equivariant tail map

Let \((\mathfrak H,\sigma_t,\mu)\) be an ergodic component of the compact two-sided similarity hull retained after the previous reductions.

M5-567 gives to each hull state \(Y\) a terminal scattering/trace profile

\[
A_Y(q,\omega),
\qquad q\in\mathbb R,
\quad \omega\in S^2,
\]

with the exact shift covariance

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega).
}
\]

Let \(\mathcal A:Y\mapsto A_Y\) be this factor map and let

\[
\nu:=\mathcal A_\#\mu.
\]

Then \(\nu\) is invariant under all log-radius translations

\[
(T_hA)(q,\omega):=A(q-h,\omega).
\]

Because \(\nu\) is a factor of an ergodic flow, the induced translation process is ergodic on the corresponding factor component.

Thus the terminal critical tail is a stationary ergodic process on the log cylinder

\[
\mathbb R_q\times S^2.
\]

---

## 2. Local cubic observable

Define the unit-cell cubic observable

\[
C_3(A)
:=
\int_0^1\int_{S^2}|A(q,\omega)|^3d\omega\,dq.
\]

On the retained compact regular profile class this is a finite nonnegative observable.

If

\[
\int C_3\,d\nu=0,
\]

then \(C_3=0\) for \(\nu\)-almost every profile. Translation invariance then gives

\[
A\equiv0
\]

on the whole log cylinder for \(\nu\)-a.e. profile.

But M5-562/M5-569 exclude the zero/global-L3 profile on a nontrivial ergodic hard component.

Therefore

\[
\boxed{
c_3:=\int C_3\,d\nu>0.
}
\]

By the Birkhoff ergodic theorem, for \(\nu\)-a.e. \(A\),

\[
\boxed{
\frac1L
\int_0^L\int_{S^2}|A(q,\omega)|^3d\omega\,dq
\longrightarrow c_3>0.
}
\]

Hence the global-L3 divergence is not merely nonsummable on an arbitrary sparse shell set. On an ergodic hard component it has **positive asymptotic log-radius density**.

---

## 3. Terminal-vorticity observable

Let

\[
B_A=\operatorname{Curl}_{log}A
\]

be the coefficient defined by

\[
\omega_0(x)=r^{-2}B_A(\log r,\omega).
\]

Define

\[
C_\omega(A)
:=
\int_0^1\int_{S^2}|B_A(q,\omega)|^2d\omega\,dq.
\]

M5-570 established that on the retained bounded/regular critical class

\[
A\neq0
\Longrightarrow
B_A\neq0.
\]

Therefore the same ergodic argument gives

\[
\boxed{
c_\omega:=\int C_\omega\,d\nu>0.
}
\]

and for \(\nu\)-a.e. hard profile,

\[
\boxed{
\frac1L
\int_0^L\int_{S^2}|B_A|^2
\longrightarrow c_\omega>0.
}
\]

Thus the terminal vorticity obstruction also has positive log-density.

---

## 4. Consequence for terminal enstrophy tails

The physical terminal vorticity tail satisfies

\[
\int_{|x|>R}|\omega_0|^2dx
=
\int_{\log R}^{\infty}
 e^{-q}
 b(q)dq,
\]

where

\[
b(q):=\int_{S^2}|B_A(q,\omega)|^2d\omega.
\]

For the invariant ensemble,

\[
\mathbb E_\nu[b(q)]=c_\omega
\]

for all \(q\). Hence

\[
\boxed{
\mathbb E_\nu
\int_{|x|>R}|\omega_0|^2dx
=
\frac{c_\omega}{R}.
}
\]

This recovers the exact critical \(R^{-1}\) enstrophy-tail scaling statistically.

---

## 5. Logarithmic divergence of the Hardy-weighted terminal enstrophy

Consider

\[
H_\omega(R)
:=
\int_{1<|x|<R}|x|\,|\omega_0(x)|^2dx.
\]

Because

\[
|x||\omega_0|^2dx
=
 r\cdot r^{-4}|B_A|^2\cdot r^2drd\omega
=
\frac{dr}{r}|B_A|^2d\omega,
\]

we have the exact log-coordinate identity

\[
\boxed{
H_\omega(R)
=
\int_0^{\log R}
\int_{S^2}|B_A(q,\omega)|^2d\omega\,dq.
}
\]

Therefore for \(\nu\)-a.e. hard profile,

\[
\boxed{
\frac{H_\omega(R)}{\log R}
\longrightarrow c_\omega>0.
}
\]

So the surviving branch carries a **linear-in-log-radius Hardy weighted enstrophy tower**.

This strengthens the old statement `weighted moment diverges`: the divergence has a definite positive ergodic density.

---

## 6. Relation to the historical-shell audit

The earlier amplitude-sensitive historical genealogy showed that the non-L3 tail cannot be silently forgotten, but left a persistent passive high-ratio genealogy because viscosity can pay the weighted-moment balance on the short remaining-time scale.

M5-571 sharpens the persistent branch:

\[
\boxed{
\text{persistent passive tail}
\Longrightarrow
\text{positive-density stationary log-radius terminal process}.
}
\]

Thus the remaining endpoint is not an arbitrarily sparse set of passive shells. It must support positive mean densities

\[
c_3>0,
\qquad
c_\omega>0.
\]

This is potentially useful for a renormalized shell-balance or flux argument, because the relevant shell charges now possess ergodic means.

---

## 7. Current endpoint

The aperiodic/DSS distinction is now secondary. Both are instances of the same stationary log-radius factor:

- DSS: \(A(q,\omega)\) is periodic in \(q\);
- aperiodic recurrent: \(A\) is nonperiodic but distributed according to a translation-invariant ergodic measure.

Both satisfy on a nontrivial hard component

\[
\boxed{
\begin{gathered}
c_3>0,\\
c_\omega>0,\\
H_\omega(R)\sim c_\omega\log R
\quad\text{in ergodic mean}.
\end{gathered}
}
\]

The next target is to derive the renormalized local energy/enstrophy balance on one log-radius cell and test whether a stationary positive-density \(B_A\) process can be maintained without a nonzero mean PDE source or flux that is forbidden by the ancient compact-hull budgets.

Status: **THE FINAL CRITICAL TAIL HAS BEEN UPGRADED FROM AN INFINITE SHELL STACK TO A POSITIVE-DENSITY STATIONARY ERGODIC LOG-RADIUS VELOCITY/VORTICITY PROCESS. GLOBAL REGULARITY REMAINS UNPROVED.**