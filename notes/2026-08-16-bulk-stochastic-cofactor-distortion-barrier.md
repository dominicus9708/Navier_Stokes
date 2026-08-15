# Coherent crossing forces pointwise-in-core stochastic cofactor distortion of order `q`

Date: 2026-08-16

Status: **SHARPENED STOCHASTIC CAUCHY CONSEQUENCE / ALMOST EVERY GOOD CORE POINT REQUIRES EXPECTED AREA DISTORTION `>= c q` / RARE STOCHASTIC-HISTORY CRITICALITY REMAINS.**

## 1. Good coherent core

At the coherent Reynolds-one crossing,

\[
|\bar\Omega|\ge c_0,
\qquad
\int_{B_{cR}}|\Omega-\bar\Omega|^2dx
\lesssim R^{-1}.
\]

Let

\[
e=\bar\Omega/|\bar\Omega|.
\]

Since the core volume is `~R^3` while the fluctuation `L2` mass is `O(R^-1)`, Chebyshev gives a good set

\[
G_R\subset B_{cR}
\]

with

\[
|G_R|\ge (1-o(1))|B_{cR}|\asymp R^3
\]

such that

\[
\boxed{
\Omega_T(x)\cdot e\ge c_1>0
\qquad (x\in G_R).
}
\]

---

## 2. Backward stochastic flow

Let

\[
Y^\varpi(x)=A_T^{s_-,\varpi}(x),
\qquad
G^\varpi(x)=\nabla_xY^\varpi(x).
\]

Incompressibility gives pathwise

\[
\det G^\varpi=1.
\]

If `F^varpi` is the inverse forward deformation gradient, then

\[
(F^\varpi)^T
=(G^\varpi)^{-T}
=\operatorname{cof}G^\varpi.
\]

The stochastic Cauchy formula gives

\[
\Omega_T(x)\cdot e
=
\mathbb E\left[
\Omega_-(Y^\varpi(x))
\cdot
\operatorname{cof}G^\varpi(x)e
\right].
\]

---

## 3. Pointwise first-hitting cap gives the sharp lower bound

At a deeper first-hitting checkpoint with amplification ratio `q`,

\[
\boxed{
\|\Omega_-\|_\infty\le q^{-1}.
}
\]

Therefore, for every `x in G_R`,

\[
\begin{aligned}
c_1
&\le
\Omega_T(x)\cdot e\\
&\le
q^{-1}
\mathbb E
|\operatorname{cof}G^\varpi(x)e|.
\end{aligned}
\]

Hence

\[
\boxed{
\mathbb E
|\operatorname{cof}G^\varpi(x)e|
\ge c_1q
\qquad (x\in G_R).
}
\]

By Jensen,

\[
\boxed{
\mathbb E
|\operatorname{cof}G^\varpi(x)e|^2
\ge c_1^2q^2
\qquad (x\in G_R).
}
\]

This is substantially stronger than the earlier volume-integrated estimate obtained from the global enstrophy `E_-`.

---

## 4. Bulk consequence

Averaging over the good core,

\[
\boxed{
\mathbb E\fint_{G_R}
|\operatorname{cof}G^\varpi e|\,dx
\gtrsim q,
}
\]

and

\[
\boxed{
\mathbb E\fint_{G_R}
|\operatorname{cof}G^\varpi e|^2dx
\gtrsim q^2.
}
\]

For the deep checkpoint

\[
q_\beta=\frac{W}{R^\beta},
\]

we get

\[
\boxed{
\mathbb E\fint_{G_R}
|\operatorname{cof}G^\varpi e|^2dx
\gtrsim
\frac{W^2}{R^{2\beta}}.
}
\]

Using

\[
W^{1/2}\gtrsim R^5(\log R)^{5/2},
\]

this implies

\[
\boxed{
\mathbb E\fint_{G_R}
|\operatorname{cof}G^\varpi e|^2dx
\gtrsim
R^{20-2\beta}(\log R)^{10}.
}
\]

For the canonical `beta=2`, the expected mean-square cofactor stretch is at least

\[
\boxed{R^{16}(\log R)^{10},}
\]

and the expected/RMS area stretch scale is at least order `q`.

---

## 5. Relation to the previous enstrophy-based bulk bound

Integrating stochastic Cauchy first and applying Cauchy--Schwarz with the global earlier enstrophy gave

\[
\mathbb E\int_{G_R}
|\operatorname{cof}G^\varpi e|^2dx
\gtrsim
R^6/E_-.
\]

This remains correct, but the pointwise cap is stronger on the coherent good set:

\[
\boxed{
\text{pointwise cap }q^{-1}
\Longrightarrow
\text{expected cofactor stretch }q
\text{ at essentially every core point}.
}
\]

Thus the bulk distortion is not merely forced by one large global integral.

---

## 6. Geometric and probabilistic meaning

The vector

\[
\operatorname{cof}G\,e
\]

is the backward area vector associated with a terminal area element whose normal is `e`.

Therefore almost every good point of the terminal coherent core demands a stochastic ancestor area amplification of order `q` **in expectation**.

This removes the need to choose one special ancestor loop or one special spanning surface as the primary descriptor.

However expectation still leaves a genuine loophole:

- a typical stochastic history may have moderate deformation;
- a sufficiently rare set of histories may have deformation much larger than `q` and carry the expectation.

The stochastic Feynman--Kac/Kato estimate already shows that such rare-history amplification requires critical `L_t^{8/5}L_x^4` strain action. That exponent lies exactly on the known vorticity/gradient regularity scaling line, so no contradiction follows from the moment bound alone.

---

## 7. Updated active target

The final stochastic ancestry problem is now more sharply stated:

\[
\boxed{
\begin{gathered}
\text{At almost every point of an }R^3\text{ coherent core,}\
\mathbb E|\operatorname{cof}G\,e|\gtrsim q\to\infty.\\
\text{Can this expectation be supported by increasingly rare}\
\text{stochastic histories while finite-energy NS remains}\
\text{inside all critical strain/middle-strain/derivative budgets?}
\end{gathered}
}
\]

Loop length, diameter, reach, and curvature are now secondary geometric manifestations of this pointwise-in-core stochastic area-distortion demand.

Overall status: **POINTWISE-IN-CORE STOCHASTIC AREA DISTORTION SHARPENED TO ORDER `q`; ONLY RARE-HISTORY CRITICAL SATURATION / DERIVATIVE INTERMITTENCY REMAINS.**
