# DSD M17-322 — line-weight memory splits exactly into flux-ratio and strain-residence channels

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope

This module starts from the exact M17-318/M5-684 line identities.  A separate DSD heuristic companion suggested the change of variables, but no DSD theoretical statement is used as a proof hypothesis here.

For one regular captured material vortex line, write

\[
l:=\log L_\rho.
\]

The established identities are

\[
\dot l
=\kappa-\frac12+2\bar\sigma_\rho,
\]

and

\[
\frac d{d\theta}\log\frac{L_\rho}{\Phi}
=2\bar\sigma_\rho-\frac12.
\]

## 2. Exact channel coordinates

Define

\[
u:=\log\Phi,
\qquad
z:=\log\frac{L_\rho}{\Phi}.
\]

Then

\[
l=u+z.
\]

Subtracting the two established line laws gives the exact flux law

\[
\boxed{\dot u=\kappa.}
\]

The residence variable satisfies

\[
\boxed{\dot z=2\bar\sigma_\rho-\frac12.}
\]

Thus

\[
\boxed{
\dot l
=\dot u+\dot z
=\kappa+2\bar\sigma_\rho-\frac12.
}
\]

No new hypothesis has entered.

## 3. Pairwise memory decomposition

For two captured line labels \(\lambda,\mu\), put

\[
q:=l_\lambda-l_\mu,
\qquad
p:=u_\lambda-u_\mu,
\qquad
r:=z_\lambda-z_\mu.
\]

Then exactly

\[
\boxed{q=p+r.}
\]

Moreover

\[
\boxed{
\dot p=\kappa_\lambda-\kappa_\mu,
}
\]

and

\[
\boxed{
\dot r=2(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}).
}
\]

Hence a line-weight contrast is not one indivisible memory variable.  It is the sum of a flux-ratio contrast and a strain-residence contrast.

## 4. Pointwise dichotomy

If at some time \(\theta\)

\[
|q(\theta)|\ge c_L,
\]

then the triangle inequality gives

\[
\boxed{
|p(\theta)|\ge\frac{c_L}{2}
\quad\lor\quad
|r(\theta)|\ge\frac{c_L}{2}.
}
\]

Equivalently,

\[
\boxed{
\left|\log\frac{\Phi_\lambda}{\Phi_\mu}\right|
\ge\frac{c_L}{2}
\quad\lor\quad
\left|
\log\frac{(L_\rho/\Phi)_\lambda}{(L_\rho/\Phi)_\mu}
\right|
\ge\frac{c_L}{2}.
}
\]

Thus the old untyped `ancestral line-weight memory` branch splits into two standard mathematical channels.

## 5. Time-density version

Suppose on an interval \(I\)

\[
|q(\theta)|\ge c_L
\qquad\text{for every }\theta\in I.
\]

Define

\[
I_\Phi
:=\left\{\theta\in I:|p(\theta)|\ge c_L/2\right\},
\]

\[
I_\sigma
:=\left\{\theta\in I:|r(\theta)|\ge c_L/2\right\}.
\]

Then

\[
I=I_\Phi\cup I_\sigma,
\]

so

\[
\boxed{
|I_\Phi|\ge\frac{|I|}{2}
\quad\lor\quad
|I_\sigma|\ge\frac{|I|}{2}.
}
\]

This prevents a persistent composite contrast from remaining completely untyped over a long interval, although the dominant channel may switch in time.

## 6. Finite-age creation costs

### 6.1 Flux-ratio creation

Let \(J=[\theta_0,\theta_1]\), \(|J|=T\), and assume

\[
|p(\theta_1)|\ge c_\Phi,
\qquad
|p(\theta_0)|\le \eta c_\Phi,
\qquad 0\le\eta<1.
\]

Then

\[
\left|
\int_J(\kappa_\lambda-\kappa_\mu)d\theta
\right|
\ge(1-\eta)c_\Phi.
\]

By Cauchy--Schwarz,

\[
\boxed{
\int_J|\kappa_\lambda-\kappa_\mu|^2d\theta
\ge
\frac{(1-\eta)^2c_\Phi^2}{T}.
}
\]

Thus a recently created flux-ratio memory requires a coefficient-separation payment.

### 6.2 Strain-residence creation

Assume instead

\[
|r(\theta_1)|\ge c_\sigma,
\qquad
|r(\theta_0)|\le\eta c_\sigma.
\]

Since

\[
\dot r=2\Delta\bar\sigma_\rho,
\]

we get

\[
2\left|
\int_J\Delta\bar\sigma_\rho\,d\theta
\right|
\ge(1-\eta)c_\sigma,
\]

and hence

\[
\boxed{
\int_J|\Delta\bar\sigma_\rho|^2d\theta
\ge
\frac{(1-\eta)^2c_\sigma^2}{4T}.
}
\]

Thus recently created strain-residence memory requires a transverse/line-averaged strain-separation payment.

## 7. What this does not prove

The two lower bounds still decay like \(T^{-1}\) when the memory age tends to infinity.  Therefore M17-320's ancient-memory firewall remains active:

\[
\boxed{
\text{arbitrarily ancient flux memory or strain-residence memory}
\not\Rightarrow
\text{fixed payment}.
}
\]

Likewise neither \(p\) nor \(r\) is automatically a bounded state function on the recurrent hull.  Path/genealogy dependence remains a valid exit.

## 8. Updated late-memory gate

The previous generic ancestral-memory branch should now be read as

\[
\boxed{
H_{ancestral\ line\text{-}weight\ memory}
\Rightarrow
H_{flux\text{-}ratio\ memory}
\lor
H_{strain\text{-}residence\ memory}.
}
\]

Each branch further splits into

\[
\boxed{
\text{finite-age creation payment}
\lor
\text{arbitrarily ancient carrier}
\lor
\text{genealogy/replacement exit}.
}
\]

## 9. Audit verdict

**PASS as an exact decomposition.**

The value of the DSD heuristic was limited to proposing the channel coordinates.  The canonical result itself follows entirely from the existing Navier--Stokes/CE-H material-line identities.

## 10. Next target

The flux channel has

\[
\dot u=\kappa,
\]

so the fixed negative zero-\(\kappa\) current from M17-314 naturally suggests a directed crossing activity that cannot cancel by sign.  The next step is to test whether this produces a genuine nonnegative turnover ledger or merely another normalized label-space quantity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
