# DSD W1 Punctured Final Trace and Terminal Taylor Expansion

Date: 2026-08-26

Status: **GENERAL W1 CANONICAL PASSIVE TAIL INTERPRETED AS A STATIC PUNCTURED PHYSICAL FINAL TRACE / LOCAL TYPE-I BOUNDEDNESS GIVES REGULAR EXTENSION TO THE TERMINAL TIME AWAY FROM THE CENTER / STATIC-TAIL NS RESIDUAL IDENTIFIED AS THE FIRST TERMINAL TIME DERIVATIVE AND CANCELED BY THE O(T*-t) QUOTIENT CORRECTION / STATIONARY-TAIL RESIDUAL ROUTE CLOSED AS A FALSE PROOF STRATEGY / GLOBAL REGULARITY UNPROVED.**

## 1. Physical W1 solution and canonical trace

Let `V(s)` be a complete W1 Leray orbit and

\[
\lambda(t)=\sqrt{T_*-t}=e^{-s/2}.
\]

Its formal physical realization is

\[
u(x,t)=\lambda^{-1}V(x/\lambda,s).
\]

Let `T(Y,s)` be the canonical passive tail.  The covariance law

\[
T(Y,s+	au)
=e^{-\tau/2}T(e^{-\tau/2}Y,s)
\]

implies that its inverse similarity transform is independent of time.

Define

\[
\boxed{
b(x)
:=
\lambda^{-1}T(x/\lambda,s).
}
\]

Then `b` is independent of `s` wherever the canonical tail is defined.

The Type-I estimate gives

\[
\boxed{|b(x)|\le A_0|x|^{-1}.}
\]

Thus `b` is a critical punctured final-trace candidate.

---

## 2. Remainder

Define

\[
\boxed{q(x,t):=u(x,t)-b(x).}
\]

On every fixed physical annulus

\[
K=\{r_1<|x|<r_2\},
\qquad r_1>0,
\]

the corresponding normalized radius tends to infinity like

\[
R\asymp r/\lambda.
\]

The canonical-tail shell estimate therefore gives

\[
\|q(t)\|_{L^3(K)}
\to0
\]

and

\[
\|q(t)\|_{L^2(K)}
\to0
\]

as `t up T_*`, with quantitative model rates inherited from

\[
R^{-1/2}
\quad\text{and}\quad
R^{-1}.
\]

Hence

\[
\boxed{u(\cdot,t)\to b
\quad\text{locally in }L^2\cap L^3
\text{ on }\mathbb R^3\setminus\{0\}.}
\]

---

## 3. Uniform local boundedness away from the center

For `x` in the fixed annulus `K`, the W1 Type-I tail bound gives for all sufficiently late times

\[
|u(x,t)|
=
\lambda^{-1}|V(x/\lambda,s)|
\le
\lambda^{-1}
\frac{A_0}{|x|/\lambda}
=
\frac{A_0}{|x|}
\le
\frac{A_0}{r_1}.
\]

Therefore

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\|_{L^\infty(K)}<\infty.
}
\]

After enlarging the annulus slightly, standard local Navier--Stokes regularity implies uniform derivative bounds on compact subannuli up to the terminal time.

Thus `u` extends smoothly to `t=T_*` on every compact subset of the punctured space, with terminal value `b`.

This is a local statement; nothing is asserted at the singular center.

---

## 4. Static trace need not solve stationary Navier--Stokes

The projected physical Navier--Stokes equation is

\[
u_t
=
\nu\Delta u
-
\mathbb P\nabla\cdot(u\otimes u)
=:\mathcal N_{phys}(u).
\]

Because the punctured solution extends regularly to `T_*`, passing to the terminal time on a compact punctured region gives

\[
\boxed{
u_t(T_*^-)
=
\mathcal N_{phys}(b)
}
\]

where

\[
\boxed{
f_b
:=
\mathcal N_{phys}(b)
=
\nu\Delta b
-
\mathbb P\nabla\cdot(b\otimes b).
}
\]

There is no reason for `f_b` to vanish.

Hence the static physical trace is not required to be a stationary Navier--Stokes solution.

---

## 5. Exact quotient equation

Substitute

\[
u=b+q
\]

into the projected physical equation. Since `b_t=0`,

\[
\boxed{
q_t
-\nu\Delta q
+
\mathbb P\nabla\cdot
(q\otimes q+q\otimes b+b\otimes q)
=
f_b.
}
\]

The forcing is precisely the stationary residual of the canonical trace.

Thus the tail residual is not an external error term.  It is the deterministic source that drives the terminal-zero correction.

---

## 6. First terminal correction

On a fixed punctured compact set, smooth terminal extension gives

\[
u(t)
=
b
+(t-T_*)u_t(T_*^-)
+o(|t-T_*|).
\]

Using `u_t(T_*^-)=f_b`,

\[
\boxed{
q(t)
=
-(T_*-t)f_b
+o(T_*-t).
}
\]

Thus the canonical-tail residual is canceled at first order by the time-dependent quotient.

This is the rigorous punctured-space version of the previously formal example

\[
q\sim -(T_*-t)f_b.
\]

---

## 7. Higher terminal orders

On every compact set away from the center, local parabolic bootstrapping provides as many finite terminal derivatives as the local smooth extension allows.

Differentiating the equation yields recursively

\[
u_{tt}(T_*^-)
=
D\mathcal N_{phys}(b)[f_b],
\]

and higher derivatives are obtained from repeated Fréchet differentiation of the local Navier--Stokes vector field.

Therefore for each finite order justified by the local regularity,

\[
u(t)
=
b
-(T_*-t)f_b
+\frac12(T_*-t)^2
D\mathcal N_{phys}(b)[f_b]
+\cdots.
\]

No Fredholm or resonance condition forcing `f_b=0` appears at any finite punctured-space order.

---

## 8. Relation to the earlier nonresonant correction calculation

In Leray/log-radius variables the formal expansion had coefficient equations of the type

\[
(\partial_s-n)G_n=H_n,
\qquad n\ge1,
\]

whose periodic operator was invertible.

The present physical calculation explains the same phenomenon without periodicity:

- the leading passive tail becomes a static physical trace `b`;
- its nonzero residual is simply the terminal derivative of the correction;
- higher residuals determine higher terminal Taylor coefficients.

Thus the lack of resonance is a general punctured-space property, not a special feature of DSS periodicity.

---

## 9. Branch pruning

The following proposed closure is therefore invalid:

\[
\text{static physical tail}
\Longrightarrow
\text{stationary Navier--Stokes tail}
\Longrightarrow
\text{Liouville contradiction}.
\]

The first implication fails.

The correct structure is

\[
\boxed{
\text{static critical final trace }b
+
\text{terminal correction }q
\text{ driven by }f_b.
}
\]

Hence a stationary-profile Liouville theorem cannot close the general W1 endpoint unless an independent argument first proves

\[
\boxed{f_b=0.}
\]

No such argument is currently available.

---

## 10. Remaining singular locus

All ordinary terminal-time dynamics away from the center are now regular and accounted for by the Taylor expansion.

Therefore any true obstruction must be concentrated in the simultaneous limit

\[
\boxed{x\to0,
\qquad t\to T_*}
\]

or equivalently at similarity infinity/core matching in the normalized description.

This further narrows the DSD proof target:

\[
\boxed{
\text{punctured trace is regular; only the critical center matching can remain singular.}
}
\]

The problem is not the remote residual by itself.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
