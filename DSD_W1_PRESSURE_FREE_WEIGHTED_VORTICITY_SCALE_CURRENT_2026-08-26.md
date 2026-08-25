# DSD W1 Pressure-Free Weighted-Vorticity Scale Current

Date: 2026-08-26

Status: **EXACT PRESSURE-FREE SCALE--TIME VORTICITY LEDGER / INVARIANT VORTICITY SCALE SURPLUS IDENTIFIED AS A NONNEGATIVE LOG-SCALE DERIVATIVE / PRELIMIT HARDY--LERAY LOWER BOUND PROVIDES THE DIAGONAL GROWTH INPUT / POSITIVE INVARIANT ENDPOINT LIMIT NOT YET TRANSFERRED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The critical Gaussian `p=3` ledger compresses the W1 endpoint to the Bernoulli surplus

\[
\mathcal S_B(R)>0,
\qquad
\mathcal S_B(R)\to\mathscr R_3/6.
\]

That representation contains pressure through the Bernoulli scalar.

To audit whether the endpoint is genuinely hydrodynamic rather than an artifact of pressure bookkeeping, construct a second scale current using only vorticity.

The natural critical weight is the first radial vorticity moment, softened by a Gaussian cutoff.

---

## 2. Leray vorticity equation

For the standard backward Leray equation

\[
U_s-\nu\Delta U+(U\cdot\nabla)U
+\frac12U+\frac12Y\cdot\nabla U+\nabla P=0,
\qquad \nabla\cdot U=0,
\]

let

\[
\Omega=\nabla\times U.
\]

Then

\[
\boxed{
\Omega_s-\nu\Delta\Omega
+(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U
+\Omega
+\frac12Y\cdot\nabla\Omega
=0.
}
\]

Pressure has disappeared identically.

Set

\[
q:=\frac12|\Omega|^2.
\]

Dotting with `Omega` gives

\[
q_s
-\nu\Delta q
+U\cdot\nabla q
+\frac12Y\cdot\nabla q
+2q
-
\Omega\cdot S\Omega
+\nu|\nabla\Omega|^2
=0.
\]

---

## 3. Critical Gaussian-radial weight

For `R>0`, set

\[
r:=|Y|,
\qquad
\psi_R(r):=e^{-r^2/R^2},
\]

and

\[
\boxed{
w_R(r):=r\psi_R(r).}
\]

Define

\[
\boxed{
I_R(s)
:=
\int w_Rq\,dY
=
\frac12\int r e^{-r^2/R^2}|\Omega|^2dY.
}
\]

For a smooth prelimit solution or a fixed Gaussian scale on the W1 compact class, this quantity is finite.

The nonsmoothness of `r` at the origin may be handled by `r_epsilon=(r^2+epsilon^2)^{1/2}` and then `epsilon downarrow 0`; no endpoint conclusion below depends on the origin singularity.

---

## 4. The Leray dilation becomes a scale derivative

The weight satisfies

\[
Y\cdot\nabla w_R
=
r\partial_rw_R
=w_R\left(1-\frac{2r^2}{R^2}\right).
\]

Also

\[
\partial_{\log R}w_R
=
\frac{2r^2}{R^2}w_R.
\]

Therefore

\[
\boxed{
Y\cdot\nabla w_R-w_R
=-\partial_{\log R}w_R.
}
\]

This is the vorticity analogue of the Gaussian `p=3` scale identity.

---

## 5. Exact weighted-vorticity scale--time identity

Multiply the `q` equation by `w_R` and integrate.

Diffusion gives

\[
\nu\int w_R\Delta q
=
\nu\int q\Delta w_R,
\]

and the dissipative correction remains

\[
-\nu\int w_R|\nabla\Omega|^2.
\]

Material transport gives

\[
-\int w_RU\cdot\nabla q
=
\int q\,U\cdot\nabla w_R.
\]

The Leray dilation plus the `2q` term gives

\[
-\frac12I_R
+\frac12\int qY\cdot\nabla w_R
=
-\frac12\partial_{\log R}I_R.
\]

Hence

\[
\boxed{
\begin{aligned}
I_R'
+\frac12\partial_{\log R}I_R
+\nu A_R
={}&G_{str,R}+G_{mat,R}+G_{wt,R},
\end{aligned}
}
\]

where

\[
\boxed{
A_R:=\int w_R|\nabla\Omega|^2dY,
}
\]

\[
\boxed{
G_{str,R}:=\int w_R\,\Omega\cdot S\Omega\,dY,
}
\]

\[
\boxed{
G_{mat,R}:=\frac12\int (U\cdot\nabla w_R)|\Omega|^2dY,
}
\]

and

\[
\boxed{
G_{wt,R}:=\frac\nu2\int(\Delta w_R)|\Omega|^2dY.
}
\]

For reference,

\[
\Delta w_R
=
e^{-r^2/R^2}
\left[
\frac2r
-\frac{10r}{R^2}
+\frac{4r^3}{R^4}
\right]
\]

away from the origin.

The identity contains **no pressure term**.

Status: **EXACT.**

---

## 6. Invariant-measure scale current

Let `mu` be an invariant probability measure on the nontrivial compact minimal W1 set and define

\[
\bar I(R):=\langle I_R\rangle_\mu,
\qquad
\bar A(R):=\langle A_R\rangle_\mu,
\]

\[
\bar G(R):=
\langle G_{str,R}+G_{mat,R}+G_{wt,R}\rangle_\mu.
\]

Invariance removes the time derivative:

\[
\boxed{
\frac12\partial_{\log R}\bar I(R)
+\nu\bar A(R)
=
\bar G(R).
}
\]

Define the pressure-free vorticity surplus

\[
\boxed{
\mathcal S_\Omega(R)
:=
\bar G(R)-\nu\bar A(R).
}
\]

Then exactly

\[
\boxed{
\mathcal S_\Omega(R)
=
\frac12\partial_{\log R}\bar I(R).
}
\]

Since `w_R` increases pointwise with `R`,

\[
\partial_{\log R}\bar I(R)\ge0.
\]

Therefore

\[
\boxed{
\mathcal S_\Omega(R)\ge0.
}
\]

This is an exact scale current in vorticity language.

---

## 7. Relation to the prelimit Hardy--Leray lower bound

The companion Hardy--Leray note proves on the actual late prelimit orbit

\[
\boxed{
\int |Y||\Omega(Y,s)|^2dY
\ge c_{M1}s-C.
}
\]

Thus the untruncated critical vorticity moment grows at least linearly in Leray time whenever the W1 positive-density shell corridor persists.

The present scale current says that any analogous growth of the invariant Gaussian moment across `log R` must be paid by

\[
\mathcal S_\Omega(R).
\]

This creates a pressure-free version of the same DSD source-chain:

\[
\boxed{
\text{critical shell memory}
\longrightarrow
\text{first-weighted-enstrophy growth}
\longrightarrow
\text{vorticity scale current}.
}
\]

---

## 8. Why the endpoint limit is not yet claimed positive

It is tempting to combine

\[
M_{crit}>0
\]

with the Hardy--Leray bridge and immediately assert

\[
\liminf_{R\to\infty}\mathcal S_\Omega(R)>0.
\]

That step has **not** been proved.

The obstruction is the order of limits:

1. the Hardy--Leray lower bound is presently obtained on the actual prelimit using shell radii that grow with late time;
2. the invariant measure is obtained by first taking late-time limits at fixed Leray radius;
3. `I_R` uses a growing Gaussian radial moment, so transferring the prelimit linear moment to the invariant `R->infinity` derivative requires a uniform moving-scale compactness/localization lemma.

This is the same type of diagonal issue previously encountered when attempting to transfer the periodic `1/r` tail directly into fixed physical space.

Therefore the rigorous current status is

\[
\boxed{
\mathcal S_\Omega(R)\ge0
}
\]

at each fixed scale, together with a separate prelimit theorem

\[
\boxed{
\mathcal M_1^\Omega(s)\gtrsim s.
}
\]

The positive endpoint identification between the two remains a bridge target.

---

## 9. Comparison with the Bernoulli current

The Bernoulli scale surplus satisfies

\[
\mathcal S_B(R)
=
\frac16\left(1-\frac1{2R^2}\right)
\partial_{\log R}\bar E_3(R)
+
\frac1{4R^2}\bar E_3(R),
\]

and has the already proved endpoint

\[
\mathcal S_B(R)\to\mathscr R_3/6>0.
\]

The vorticity current satisfies

\[
\mathcal S_\Omega(R)
=
\frac12\partial_{\log R}\bar I(R)
\ge0.
\]

Thus the critical endpoint now has two independent exact ledgers:

- velocity/pressure language: Bernoulli cubic current;
- pressure-free language: weighted-vorticity current.

A successful moving-scale transfer theorem identifying positive asymptotic `S_Omega` from the prelimit lower bound would make the endpoint genuinely dual rather than merely one-sided.

---

## 10. Updated missing lemma

The narrow new bridge is:

\[
\boxed{
\text{prelimit-to-invariant weighted-vorticity scale transfer:}
}
\]

if

\[
\mathcal M_1^\Omega(s)\ge cs-C
\]

is generated by the W1 positive-density shells, prove an Abelian or diagonal statement strong enough to imply

\[
\limsup_{R\to\infty}
\frac{\bar I(R)}{\log R}>0
\]

and preferably

\[
\liminf_{R\to\infty}\mathcal S_\Omega(R)>0.
\]

The second conclusion is stronger than the first and is not assumed.

No contradiction is claimed without this bridge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
