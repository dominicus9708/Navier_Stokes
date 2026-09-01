# DSD M5-462 — Uniform metric Kato bilinear estimate

Date: 2026-09-01

Status: **THE NONLINEAR METRIC COVECTOR SYSTEM CAN BE WRITTEN WITH A Duhamel OPERATOR OF EXACTLY ONE NET SPATIAL DERIVATIVE, THE SAME AS STANDARD NAVIER--STOKES / UNIFORM ELLIPTICITY AND THE EXPLICIT METRIC HEAT KERNEL THEREFORE GIVE THE STANDARD KATO CRITICAL BILINEAR ESTIMATES / SMALL CRITICAL DATA THEORY IS NOT A NEW OBSTRUCTION; THE REMAINING ISSUE IS LARGE WEAK-`L3` STABILITY/TERMINAL RIGIDITY / GLOBAL REGULARITY REMAINS UNPROVED.**

Let

\[
m=C(t)w,
\qquad
\eta=\nabla\times m.
\]

The vorticity equation is

\[
\partial_t\eta-\nabla\cdot(G\nabla\eta)
=\eta\cdot\nabla w-w\cdot\nabla\eta.
\]

Because `div w=0`, and because the covector Lie derivative differs from `w dot grad m` only by the gradient

\[
(\nabla w)^Tm=\nabla\left(\frac12w\cdot Cw\right),
\]

we have the distributional identity

\[
\boxed{
\eta\cdot\nabla w-w\cdot\nabla\eta
=-\nabla\times\nabla\cdot(w\otimes m).
}
\]

Thus

\[
\boxed{
\eta(t)
=P_G(t,s)\eta_s
-\int_s^t
P_G(t,\tau)
\nabla\times\nabla\cdot
\big(w\otimes C(\tau)w\big)(\tau)d\tau.
}
\]

Applying the metric Biot--Savart inverse at the final time gives

\[
\boxed{
w(t)
=\mathcal S_C(t,s)w_s
+\mathcal B_C(w,w)(t),}
\]

where

\[
\boxed{
\mathcal B_C(u,v)(t)
:=-\int_s^t
\mathcal B_{C(t)}P_G(t,\tau)
\nabla\times\nabla\cdot
\big(u\otimes C(\tau)v\big)d\tau.
}
\]

The spatial orders are

\[
-1\quad(\mathcal B_C),
\qquad +1\quad(\operatorname{curl}),
\qquad +1\quad(\operatorname{div}),
\]

so the net order is exactly `+1`.

Consequently the kernel obeys the standard gradient-heat estimate. For `1<p<=q<infinity`,

\[
\boxed{
\|\mathcal K_C(t,\tau)F\|_{L^q}
\le
C
(t-\tau)^{-\frac12-\frac32(1/p-1/q)}
\|F\|_{L^p},
}
\]

where `K_C` denotes the spatial operator inside the Duhamel integral and the constant depends only on the ellipticity class.

Choose `q>3` and

\[
\alpha_q:=\frac12\left(1-\frac3q\right).
\]

Define the Kato norm

\[
\|u\|_{X_q(s,T)}
:=
\sup_{s<t<T}
(t-s)^{\alpha_q}\|u(t)\|_{L^q}.
\]

Taking `p=q/2` gives

\[
\|\mathcal B_C(u,v)(t)\|_q
\le
C\int_s^t
(t-\tau)^{-\frac12-\frac{3}{2q}}
\|u(\tau)\|_q\|v(\tau)\|_q d\tau.
\]

Since

\[
2\alpha_q=1-\frac3q<1
\]

and

\[
\frac12+\frac{3}{2q}<1,
\]

the Beta integral is finite and scale invariant. Therefore

\[
\boxed{
\|\mathcal B_C(u,v)\|_{X_q}
\le
C_{q,\kappa}
\|u\|_{X_q}\|v\|_{X_q}.
}
\]

Lorentz-space variants follow by the same real-interpolation/weak Young estimates used for the standard Kato theory.

Combining with M5-461 gives a contraction for sufficiently small critical initial data in `L^{3,infinity}` or the corresponding critical Besov spaces, with thresholds depending only on the uniform metric class.

Firewall:

- this proves the uniform bilinear estimate and hence the small-data architecture;
- it does not construct the large weak-`L^{3,infinity}` solution/stability class required by Albritton--Barker's large-data Liouville theorem;
- coefficient convergence must also be included in that stability theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]