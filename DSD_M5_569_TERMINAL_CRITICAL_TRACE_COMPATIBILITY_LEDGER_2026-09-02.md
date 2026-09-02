# DSD M5-569 — Terminal Critical Trace Compatibility Ledger

Date: 2026-09-02

Status: **CRITICAL TERMINAL TRACE IS COMPATIBLE WITH THE INHERITED FINITE-ENSTROPHY/L6 PACKAGE; GLOBAL L3 FAILURE IS EXACTLY A LOG-RADIUS PROFILE NONINTEGRABILITY. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-568

On the retained remote spectator lane, the ancient solution has terminal critical trace

\[
u_0(x)
=
\frac1r A(q,\omega),
\qquad
r=|x|,
\quad q=\log r,
\quad \omega=x/r,
\]

up to a subcritical remainder. Equivalently, for fixed ancient time \(s<0\),

\[
u(x,s)
=
\frac1r A(\log r,\omega)
+O\!\left(\frac{|s|}{r^3}\right)
\qquad(r\to\infty).
\]

The leading \(1/r\) coefficient is independent of physical ancient time; the time dependence first enters two spatial orders lower.

This note audits whether the leading trace is already incompatible with the quantities inherited by the compact Type-I ancient hull.

---

## 2. Divergence-free constraint on the log-radius profile

Write

\[
A=A_r\,e_r+A_T,
\qquad A_T\cdot e_r=0.
\]

For

\[
u_0=r^{-1}A(q,\omega),
\]

the incompressibility condition is

\[
\boxed{
(\partial_q+1)A_r
+\operatorname{div}_{S^2}A_T
=0.
}
\]

Thus the terminal profile is not an arbitrary vector field on the log cylinder \(\mathbb R_q\times S^2\).

---

## 3. Vorticity scaling

One spatial derivative of \(r^{-1}A(q,\omega)\) costs one additional factor \(r^{-1}\). Hence

\[
\boxed{
\omega_0:=\nabla\times u_0
=
\frac1{r^2}B_A(q,\omega),
}
\]

where \(B_A\) is a first-order log-spherical differential operator applied to \(A\).

Consequently,

\[
\int_{|x|>R}|\omega_0|^2dx
=
\int_{\log R}^{\infty}
 e^{-q}
 \int_{S^2}|B_A(q,\omega)|^2d\omega\,dq.
\]

If the retained compact/non-H lane gives a uniform local log-cylinder bound on \(B_A\), then

\[
\boxed{
\int_{|x|>R}|\omega_0|^2dx
\lesssim R^{-1}.
}
\]

Therefore a nonzero \(1/r\) terminal trace is fully compatible with finite enstrophy at spatial infinity.

This is an important anti-proof correction: finite enstrophy alone does **not** remove the terminal critical trace.

---

## 4. L6 compatibility

Similarly,

\[
\int_{|x|>R}|u_0|^6dx
=
\int_{\log R}^{\infty}
 e^{-3q}
 \int_{S^2}|A(q,\omega)|^6d\omega\,dq.
\]

Uniform boundedness of the log-cylinder profile gives

\[
\boxed{
\|u_0\|_{L^6(|x|>R)}^6
\lesssim R^{-3}.
}
\]

Hence the \(L^6\) quantity inherited from finite enstrophy is also compatible with the critical terminal trace.

---

## 5. Exact global-L3 obstruction

The cubic norm is different because \(1/r\) is exactly critical in three dimensions:

\[
\begin{aligned}
\int_{|x|>R}|u_0|^3dx
&=
\int_R^\infty
r^2\frac{dr}{r^3}
\int_{S^2}|A(\log r,\omega)|^3d\omega
\\
&=
\boxed{
\int_{\log R}^{\infty}
\int_{S^2}|A(q,\omega)|^3d\omega\,dq.
}
\end{aligned}
\]

Therefore

\[
\boxed{
 u_0\in L^3(|x|>R)
\iff
 A\in L^3((\log R,\infty)\times S^2).
}
\]

The previously derived weighted Dirichlet shell obstruction is thus equivalent, at terminal-trace level, to a failure of log-radius cubic summability.

For a nonzero periodic or recurrent profile with positive mean cubic density,

\[
\int_{\log R}^{\infty}\int_{S^2}|A|^3=\infty,
\]

and the global \(L^3\) Liouville gate is avoided exactly at the critical exponent.

---

## 6. Local energy scaling

The terminal trace has

\[
|u_0|^2\sim r^{-2}.
\]

Hence on a large ball,

\[
\int_{B_R}|u_0|^2dx
\sim R
\]

for a statistically nontrivial recurrent log profile.

Thus

\[
\boxed{
R^{-1}\int_{B_R}|u_0|^2dx
\sim O(1),
}
\]

which is exactly the scale-invariant local-energy growth allowed by a Type-I local-energy ancient solution.

Again there is no contradiction.

---

## 7. Pressure class

Formally the whole-space pressure obeys

\[
-\Delta p_0
=\partial_i\partial_j(u_{0,i}u_{0,j}).
\]

Because

\[
u_0\otimes u_0\sim r^{-2},
\]

the critical pressure has the compatible form

\[
\boxed{
 p_0(x)
=
\frac1{r^2}P_A(q,\omega)
}
\]

modulo subcritical/harmonic pieces.

In log-spherical coordinates,

\[
\Delta(r^{-2}P)
=
r^{-4}
\left[
\partial_q^2-3\partial_q+2+\Delta_{S^2}
\right]P.
\]

Hence the pressure coefficient is determined by an elliptic equation on the log cylinder with a quadratic source built from \(A\).

There is no exponent mismatch: the pressure stays in the expected critical \(r^{-2}\) class.

---

## 8. Far-field energy flux audit

For \(u\sim r^{-1}\), \(p\sim r^{-2}\),

- advective/pressure energy flux through \(S_R\) is of order \(R^{-1}\),
- viscous energy flux is also of order \(R^{-1}\).

Thus

\[
\boxed{
\text{net energy flux through }S_R\to0
\quad(R\to\infty)
}
\]

at the level of the critical asymptotic class.

Therefore the surviving tail does not require a finite nonzero energy source at spatial infinity.

---

## 9. Updated exact hard-core statement

The remote terminal trace has now passed the basic compatibility audit:

\[
\boxed{
\begin{gathered}
u_0=r^{-1}A(\log r,\omega),\\
\omega_0=r^{-2}B_A(\log r,\omega),\\
\int_{|x|>R}|\omega_0|^2\lesssim R^{-1},\\
\int_{|x|>R}|u_0|^6\lesssim R^{-3},\\
 u_0\notin L^3
\iff
 A\notin L^3(dq\,d\omega).
\end{gathered}
}
\]

Thus finite enstrophy, \(L^6\), local energy growth, and critical pressure scaling do not by themselves remove the \(1/r\) survivor.

The next useful gate must involve the **terminal vorticity coefficient** \(B_A\) and the hypotheses needed by backward uniqueness / unique continuation.

Status: **THE TERMINAL CRITICAL TRACE SATURATES, RATHER THAN VIOLATES, THE INHERITED TYPE-I/FIXED-ENSTROPHY SCALINGS. THE GLOBAL-L3 OBSTRUCTION IS EXACTLY LOG-RADIUS NONSUMMABILITY OF A. GLOBAL REGULARITY REMAINS UNPROVED.**