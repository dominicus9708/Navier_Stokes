# DSD Exact Nonzero Mild Ancient Core Gate

Date: 2026-08-25

Status: **EXACT NONZERO ANCIENT SUITABLE LIMIT ALREADY AVAILABLE / BOUNDED-VELOCITY AND MILDNESS UPGRADE DERIVED / ANCIENT-CORE EXTRACTION STEP CLOSED ON THE STATED CORRIDOR / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

Work on the already isolated corridor

\[
\boxed{\text{bounded normalized enstrophy}+\text{center nesting}+\text{no local }H/T.}
\]

The repository note `ANCIENT_LOCAL_COMPACTNESS_FROM_ENSTROPHY_TIGHTNESS_2026-08-24.md` already proves fixed-radius suitable compactness and, using local derivative compactness, nontriviality of the ancient limit.

The purpose of the present note is to make explicit that the remaining limit is not merely a distributional/local-energy object: on this corridor it is a bounded smooth ancient solution and therefore belongs to the standard mild ancient class used by the Albritton--Barker backward-`L^3` Liouville gate.

---

## 2. Imported exact ancient suitable limit

Use the fixed-center first-hitting rescaling

\[
U_j(y,\tau)=r_j u(X_*+r_jy,t_j+r_j^2\tau),
\qquad r_j=W_j^{-1/2}.
\]

The bounded dynamic enstrophy corridor gives

\[
\sup_j\sup_{\tau\le0}\|\Omega_j(\tau)\|_2^2\le Z_+.
\]

Hence

\[
\|\nabla U_j\|_2=\|\Omega_j\|_2\le Z_+^{1/2},
\qquad
\|U_j\|_6\le C_SZ_+^{1/2}.
\]

For each fixed parabolic cylinder, the local suitable quantities are uniformly bounded. A diagonal subsequence therefore gives an ancient suitable solution

\[
U_j\to U_\infty
\quad\text{on }\mathbb R^3\times(-\infty,0].
\]

The no-`H` analytic corridor supplies strong local vorticity convergence and bounded normalized center displacement. Thus for a subsequence of maximum points

\[
y_j\to y_*,
\]

and

\[
\boxed{|\Omega_\infty(y_*,0)|=1.}
\]

Therefore

\[
\boxed{U_\infty\not\equiv0.}
\]

Status: **IMPORTED / PROVED in the repository.**

---

## 3. Global `L2` and `L-infinity` vorticity bounds on finite ancient windows

At every fixed ancient time, the limit inherits

\[
\boxed{\|\Omega_\infty(\tau)\|_2^2\le Z_+.}
\]

The first-hitting/analytic corridor also supplies the pointwise vorticity Type-I bound. On every finite ancient interval

\[
[-T,0],
\]

there is a finite constant `M_T` such that

\[
\boxed{
\sup_{-T\le\tau\le0}
\|\Omega_\infty(\tau)\|_\infty
\le M_T<\infty.
}
\]

For sufficiently negative times the stronger backward decay estimate already derived in the repository is available,

\[
\|\Omega_\infty(\tau)\|_\infty\lesssim |\tau|^{-1}.
\]

---

## 4. Biot--Savart gives bounded ancient velocity

For a divergence-free whole-space velocity,

\[
U=\mathcal K*\Omega,
\qquad
|\mathcal K(z)|\le C|z|^{-2}.
\]

Split at radius `R>0`:

\[
|U(x)|
\le
C\int_{|z|<R}|z|^{-2}|\Omega(x-z)|dz
+
C\int_{|z|>R}|z|^{-2}|\Omega(x-z)|dz.
\]

The near part satisfies

\[
\int_{|z|<R}|z|^{-2}|\Omega|dz
\le C R\|\Omega\|_\infty.
\]

For the far part, Cauchy--Schwarz gives

\[
\int_{|z|>R}|z|^{-2}|\Omega|dz
\le
C R^{-1/2}\|\Omega\|_2.
\]

Therefore

\[
\boxed{
\|U\|_\infty
\le
C\left(R\|\Omega\|_\infty
+R^{-1/2}\|\Omega\|_2\right).
}
\]

Optimizing in `R` yields

\[
\boxed{
\|U\|_\infty
\le
C
\|\Omega\|_\infty^{1/3}
\|\Omega\|_2^{2/3}.
}
\]

Consequently, on every finite ancient interval,

\[
\boxed{
U_\infty\in L_t^\infty L_x^\infty.
}
\]

Together with the global homogeneous `H1` bound,

\[
U_\infty\in L_t^\infty L_x^6
\]

on every finite ancient interval.

Status: **PROVED.**

---

## 5. Smoothness on finite ancient windows

The no-`H` analytic corridor already supplies local derivative compactness. Alternatively, the bounded vorticity/velocity control on every compact ancient time window lets standard interior parabolic regularity bootstrap the ancient suitable solution.

Thus

\[
\boxed{
U_\infty\in C^\infty(\mathbb R^3\times(-\infty,0])
}
\]

on the corridor under discussion, with finite local derivative bounds on every finite backward window.

Status: **PROVED from the imported analytic corridor / standard bootstrap.**

---

## 6. Mild formulation

Fix arbitrary finite ancient times

\[
-T<t\le0.
\]

Because `U_infty` is a bounded classical solution on `[-T,t]`, the Stokes/Duhamel representation is valid:

\[
\boxed{
U_\infty(t)
=
e^{\nu(t+T)\Delta}U_\infty(-T)
-
\int_{-T}^{t}
 e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot(U_\infty\otimes U_\infty)(s)ds.
}
\]

Indeed the bounded-velocity estimate makes the heat-kernel convolution of `U\otimes U` locally time-integrable, since

\[
\|\nabla e^{\nu(t-s)\Delta}f\|_\infty
\le C(t-s)^{-1/2}\|f\|_\infty.
\]

Since `T` is arbitrary, the solution is a **mild ancient solution** in the standard finite-window sense.

Status: **PROVED.**

---

## 7. External Liouville gate cross-check

Albritton--Barker, *On Local Type I Singularities of the Navier--Stokes Equations and Liouville Theorems*, J. Math. Fluid Mech. 21 (2019), 43, arXiv:1811.00502, prove a Liouville theorem for mild ancient solutions whose global `L3` norm is uniformly bounded along a sequence of times tending to `-infinity`.

Therefore, for the nonzero ancient solution derived above,

\[
\boxed{
\exists\tau_n\to-\infty:
\sup_n\|U_\infty(\tau_n)\|_3<\infty
\Longrightarrow
U_\infty\equiv0,
}
\]

contradicting

\[
|\Omega_\infty(y_*,0)|=1.
\]

Hence a survivor must evade the theorem through the already isolated global critical tail.

Status: **EXTERNAL THEOREM VERIFIED / APPLICATION CONDITIONAL ONLY ON THE BACKWARD `L3` BOUND.**

---

## 8. DSD audit

The extraction chain is now

\[
\boxed{
\begin{aligned}
&\text{bounded-}Z + \text{center nesting}+\text{no-}H/T\\
&\Longrightarrow\text{exact ancient suitable limit}\\
&\Longrightarrow\text{nonzero strong local vorticity mark}\\
&\Longrightarrow\Omega\in L^2\cap L^\infty\text{ on finite windows}\\
&\Longrightarrow U\in L^\infty\cap L^6\\
&\Longrightarrow\text{smooth mild ancient solution}.
\end{aligned}
}
\]

There is no longer a separate `exact-core-extraction` terminal branch on this corridor.

The remaining obstruction is global critical-tail topology/integrability.

---

## 9. Updated status

### PROVED / CLOSED ON THIS CORRIDOR

- exact ancient suitable extraction;
- nontriviality;
- finite-window bounded velocity;
- smoothness;
- mild ancient formulation.

### STILL OPEN

- a bounded global `L3` backward sequence;
- elimination of the endpoint critical `1/r` / weak-`L3` tail;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
