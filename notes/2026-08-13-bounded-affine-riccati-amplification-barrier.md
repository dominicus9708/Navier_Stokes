# Bounded-affine Riccati amplification barrier for adaptive first-hitting steps

Date: 2026-08-13

Status: **DERIVED BOUNDED-AFFINE AMPLIFICATION-TIME BARRIER / AFFINE-DEGENERATION COMPLEMENT REMAINS**.

The adaptive checkpoint route left an intermediate temporal branch

\[
1\ll\sigma\ll q,
\]

where `q` is the first-hitting vorticity amplification ratio and `sigma` is the duration in terminal natural time.

The sharpened Gaussian mean-vorticity cancellation closes this branch on every uniformly bounded self-consistent affine/Gaussian geometry.  The mechanism is a Riccati-type endpoint inequality for the maximum vorticity.

---

## 1. First-hitting interval and maximum vorticity

Work in terminal normalized variables on a first-hitting interval `[s0,T]`.  Define

\[
M(s)=\|\Omega(s)\|_{L^\infty(\mathbb R^3)}.
\]

At the previous and terminal checkpoints,

\[
\boxed{
M(s_0)=\frac1q,
\qquad
M(T)=1.
}
\]

Throughout the interval,

\[
M(s)\le1.
\]

---

## 2. Bounded self-consistent affine geometry

For every terminal evaluation point/time needed to estimate `M(t)`, use the self-consistent Gaussian affine window and assume the corresponding affine transition/covariance obey

\[
\boxed{
\sup_{s_0\le s\le t}
\|F(t,s)\|_{op}\le K_F,
\qquad
\sup_{s_0\le s<t}
\kappa(\Sigma_t(s))\le K_\Sigma.
}
\]

Set `K` to denote constants depending only on these two bounds, the dimension, and viscosity normalization.

If these bounds fail, the evolution is placed in the affine-deformation / affine-heat-anisotropy branch rather than the present bounded-affine branch.

---

## 3. Four-channel variance is quadratic in the instantaneous vorticity cap

The self-consistent residual variance is

\[
\mathcal B_\gamma
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega).
\]

The vorticity part obeys immediately

\[
\operatorname{Var}_\gamma(\Omega)
\le\int\gamma|\Omega|^2
\le M(s)^2.
\]

For strain, the Calderon--Zygmund relation gives

\[
\|S\|_{BMO}
\le C M(s).
\]

A well-conditioned Gaussian weighted John--Nirenberg estimate yields

\[
\operatorname{Var}_\gamma(S)
\le C_{K_\Sigma}\|S\|_{BMO}^2
\le C_K M(s)^2.
\]

Consequently

\[
\boxed{
\mathcal B_\gamma(s)
\le C_K M(s)^2.
}
\]

The Gaussian weighted BMO variance statement can be proved by decomposing space into covariance-adapted dyadic annuli, applying the local John--Nirenberg estimate on each enlarged ellipsoid, controlling successive mean differences by BMO, and summing the exponentially decaying Gaussian tails.

---

## 4. Mean-vorticity cancellation makes the residual source quadratic

The sharpened Gaussian residual identity gives

\[
\left|
\int\gamma_s f_r\right|
\le
C[1+\sqrt{\kappa(\Sigma(s))}]
\mathcal B_\gamma(s).
\]

Therefore on the bounded-affine branch

\[
\boxed{
\left|
\int\gamma_s f_r\right|
\le C_KM(s)^2.
}
\]

This quadratic law is the essential improvement.  Without the mean-vorticity cancellation the older square-root residual estimate would only give an `O(M)` source and no `q`-scale time barrier.

---

## 5. Exact Duhamel inequality for the maximum

Fix `t in [s0,T]` and a point at which `|Omega(t)|` approaches `M(t)`.  The exact self-consistent affine Duhamel formula gives

\[
\Omega(t)
=F(t,s_0)P_{\Sigma_t(s_0)}\Omega(s_0)
+
\int_{s_0}^tF(t,s)
\left[\int\gamma_{t,s}f_r(s)\right]ds.
\]

Heat averaging is an `L^infinity` contraction, so

\[
\left|
F(t,s_0)P_{\Sigma_t(s_0)}\Omega(s_0)
\right|
\le K_FM(s_0).
\]

Using the quadratic residual estimate,

\[
\boxed{
M(t)
\le
K_FM(s_0)
+C_K\int_{s_0}^tM(s)^2ds.
}
\]

---

## 6. Riccati comparison

Define

\[
Y(t)=K_FM(s_0)+C_K\int_{s_0}^tM(s)^2ds.
\]

Then

\[
M(t)\le Y(t),
\]

and

\[
Y'(t)=C_KM(t)^2\le C_KY(t)^2.
\]

Therefore, while the denominator is positive,

\[
\boxed{
Y(t)
\le
\frac{K_FM(s_0)}
{1-C_KK_FM(s_0)(t-s_0)}.
}
\]

Insert

\[
M(s_0)=q^{-1}.
\]

If `M(T)=1`, then necessarily

\[
1
\le
\frac{K_F/q}
{1-C_KK_F(T-s_0)/q}.
\]

Rearranging,

\[
\boxed{
T-s_0
\ge
\frac{q-K_F}{C_KK_F}.
}
\]

Thus for `q >= 2 K_F`,

\[
\boxed{
T-s_0
\ge c_Kq.
}
\]

---

## 7. Elimination of the intermediate temporal lane

Let

\[
\sigma=q_{\rm terminal\ time}
=W(T-t_-)
\]

be the normalized first-hitting duration.  On every bounded-affine self-consistent Gaussian branch,

\[
\boxed{
\sigma\gtrsim_K q.
}
\]

Hence the previously open regime

\[
1\ll\sigma\ll q
\]

is impossible without leaving the bounded-affine/Gaussian branch.

The adaptive first-hitting step therefore has only the following alternatives:

1. `sigma >= c_K q`: amplification uses at least a previous-natural-time interval;
2. affine transition/covariance conditioning loses the fixed bound `K`: affine deformation/anisotropy branch;
3. one of the analytic assumptions needed for the quadratic residual estimate loses compact control, which is typed into high derivative / pressure / residual concentration.

---

## 8. Alignment with the one-step memory principle

The adaptive checkpoint choice was made so that the previous natural normalized time is exactly

\[
q.
\]

The residual-memory cutoff is also of order `q`.

The Riccati barrier now shows that, on the bounded-affine branch, a `q`-fold amplification cannot occur in substantially less time than the amount of history that the Gaussian endpoint kernel retains.

Thus the spatial and temporal adaptive scales are aligned:

\[
\boxed{
R_-^2=q
\sim
\text{minimum bounded-affine amplification time}.
}
\]

---

## 9. DSD interpretation

The resolved affine representative and four-channel residual provide a closed local causal estimate:

\[
\boxed{
\text{small current amplitude}
\Longrightarrow
\text{residual production rate}=O(M^2).
}
\]

Therefore a dangerous state cannot jump rapidly through many amplitude levels while the resolved affine geometry remains controlled.  Fast passage itself certifies the activation of another typed channel.

This converts the adaptive state graph from a qualitative list into a time-of-flight constraint.

---

## 10. Claim boundary

The theorem is conditional on a uniform bound for the self-consistent affine transition and Gaussian covariance condition number over the endpoint constructions used in the interval, plus the Gaussian weighted BMO variance lemma stated above.

The complementary unbounded-affine branch remains part of the active proof challenge.  The result does not by itself exclude a singular route with `sigma ~ q` at every step.

Status: **INTERMEDIATE `1 << sigma << q` LANE CLOSED ON BOUNDED-AFFINE BRANCH / LONG-STEP AND AFFINE-DEGENERATION LANES REMAIN**.
