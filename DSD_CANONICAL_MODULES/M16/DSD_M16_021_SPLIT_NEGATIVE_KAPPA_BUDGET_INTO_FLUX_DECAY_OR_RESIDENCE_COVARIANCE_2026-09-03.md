# DSD M16-021 — Split a negative kappa budget into flux decay or residence covariance

Date: 2026-09-03
Canonical ID: **M16-021**

Status: **INTERNAL QUANTITATIVE MEASURE-SPLIT / AFTER THE M16-020 CORRECTION, A NEGATIVE ENSTROPHY-WEIGHTED `kappa` BUDGET ON A COHERENT MATERIAL TUBE ENSEMBLE HAS EXACTLY TWO WAYS TO SURVIVE: THE CURRENT TRANSVERSE-FLUX MEASURE ITSELF HAS A STRICT NEGATIVE `kappa` BIAS, OR THAT BIAS IS HIDDEN IN A STRICT NEGATIVE COVARIANCE BETWEEN `kappa` AND THE VORTICITY-WEIGHTED LINE-RESIDENCE FACTOR `L_rho`. THE FIRST BRANCH FORCES FLUX DECAY/REPLACEMENT; THE SECOND FORCES A UNIFORM LINE-RESIDENCE HETEROGENEITY FLOOR ON ANY HIGH-AMPLITUDE COMPACT ENSEMBLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material tube ensemble

Let `Lambda` be a finite coherent family of oriented material vortex-tube labels at a fixed similarity time. Since material vorticity flux satisfies

\[
\Phi_\lambda'=\kappa_\lambda\Phi_\lambda,
\]

its sign is preserved as long as the tube label remains nondegenerate. Hence we may use the positive current absolute-flux measure

\[
d\nu_\theta(\lambda):=|d\Phi_\lambda(\theta)|.
\]

For each tube label define

\[
L_\lambda
:=\int_{\Gamma_\lambda}\rho\,ds.
\]

M16-020 gives the tube-coordinate disintegration

\[
E_\Lambda
:=\int_\Lambda L_\lambda\,d\nu,
\]

and

\[
K_\Lambda
:=\int_\Lambda \kappa_\lambda L_\lambda\,d\nu.
\]

Assume that on the retained compensating/recurrent subensemble there is a fixed negative enstrophy-weighted budget

\[
\boxed{
K_\Lambda\le-p_\Lambda<0.
}
\]

The point of this note is to determine what this does and does not imply for the flux measure itself.

---

## 2. Flux probability measure

Let

\[
M_\Phi:=\nu(\Lambda)>0
\]

and normalize

\[
d\mu_\Phi:=\frac{d\nu}{M_\Phi}.
\]

Write

\[
\bar\kappa_\Phi
:=\mathbb E_{\mu_\Phi}[\kappa],
\qquad
\bar L_\Phi
:=\mathbb E_{\mu_\Phi}[L]
=\frac{E_\Lambda}{M_\Phi}.
\]

Then the exact covariance decomposition is

\[
\boxed{
\frac{K_\Lambda}{M_\Phi}
=
\bar\kappa_\Phi\,\bar L_\Phi
+
\operatorname{Cov}_{\mu_\Phi}(\kappa,L).
}
\]

Since `K_Lambda <= -p_Lambda`, at least one of the two terms on the right must carry a fixed negative amount.

---

## 3. Quantitative dichotomy

If

\[
\bar\kappa_\Phi\,\bar L_\Phi
\le
-\frac{p_\Lambda}{2M_\Phi},
\]

then because

\[
\bar L_\Phi=\frac{E_\Lambda}{M_\Phi},
\]

we obtain

\[
\boxed{
\bar\kappa_\Phi
\le
-\frac{p_\Lambda}{2E_\Lambda}.
}
\]

Call this branch

\[
\boxed{B_{\rm flux}^{-}}.
\]

Otherwise the covariance term must satisfy

\[
\boxed{
\operatorname{Cov}_{\mu_\Phi}(\kappa,L)
\le
-\frac{p_\Lambda}{2M_\Phi}.
}
\]

Call this branch

\[
\boxed{B_{\rm res}^{cov}}.
\]

Therefore

\[
\boxed{
K_\Lambda\le-p_\Lambda
\Longrightarrow
B_{\rm flux}^{-}
\ \lor\ 
B_{\rm res}^{cov}.
}
\]

---

## 4. The negative-flux-bias branch forces decay of the current flux resource

For a fixed material label ensemble `Lambda`, the total current absolute flux is

\[
M_\Phi(\theta)=\int_\Lambda d\nu_\theta.
\]

Because every label satisfies

\[
d\nu_\theta'=\kappa_\lambda\,d\nu_\theta,
\]

we have the exact law

\[
\boxed{
M_\Phi'
=\int_\Lambda\kappa\,d\nu
=M_\Phi\bar\kappa_\Phi.
}
\]

Hence on `B_flux^-`,

\[
\boxed{
\frac{d}{d\theta}\log M_\Phi
\le
-\frac{p_\Lambda}{2E_\Lambda}.
}
\]

If the coherent ensemble has a uniform enstrophy cap

\[
E_\Lambda\le E_*,
\]

then

\[
\boxed{
\frac{d}{d\theta}\log M_\Phi
\le
-\frac{p_\Lambda}{2E_*}
=:-c_\Phi<0.
}
\]

Thus a positive-density interval family in this branch exponentially consumes the current material-flux resource unless new labels enter/replacement occurs.

This is a genuine signed resource mechanism, unlike an unsigned palinstrophy charge.

---

## 5. The covariance branch forces residence heterogeneity

On the fixed high-amplitude compact CE-H core, `rho` is bounded below on the coherent packet support and all derivatives of `W` are uniformly bounded. Hence

\[
|\kappa|\le\kappa_*
\]

on the retained active tube ensemble.

Cauchy--Schwarz gives

\[
|\operatorname{Cov}(\kappa,L)|
\le
\operatorname{Std}(\kappa)\operatorname{Std}(L)
\le
\kappa_*\operatorname{Std}(L).
\]

Therefore `B_res^cov` implies

\[
\boxed{
\operatorname{Std}_{\mu_\Phi}(L)
\ge
\frac{p_\Lambda}{2M_\Phi\kappa_*}.
}
\]

Equivalently,

\[
\boxed{
\operatorname{Var}_{\mu_\Phi}(L)
\ge
v_L
:=
\left(\frac{p_\Lambda}{2M_\Phi\kappa_*}\right)^2>0.
}
\]

Thus if the flux-weighted `kappa` mean refuses to be negative, the ensemble must maintain a definite spread in the vorticity-weighted line-residence factor.

The negative Rayleigh budget is then hidden in the phase relation

\[
\boxed{
\kappa<0
\quad\text{preferentially where}\quad
L_\rho\text{ is large}.
}
\]

---

## 6. What has and has not been proved

This note does **not** prove that a positive residence variance is impossible.

A compact recurrent system can in principle maintain a nonzero variance forever.

The gain is structural:

\[
\boxed{
\text{negative enstrophy-weighted `kappa`}
\Rightarrow
\text{signed flux decay}
\lor
\text{quantitative residence heterogeneity}.
}
\]

The first branch reconnects directly to finite material-flux replacement.

The second branch must now be combined with the exact line-residence evolution

\[
D_B\log L_\rho
=\kappa+2\bar\sigma_\rho-\frac12
\]

from M16-020. This will determine whether the required negative covariance can be maintained without a new axial-strain-gradient / line-residence turnover mechanism.

---

## 7. Updated frontier

The incorrect population split of M16-019 has been replaced by the exact canonical dichotomy

\[
\boxed{
B_{\rm flux}^{-}
\ \lor\ 
B_{\rm res}^{cov}.
}
\]

The next target is `B_res^cov`.

Specifically, one must decide whether a finite recurrent CE-H tube network can maintain

\[
\operatorname{Cov}_{\Phi}(\kappa,L_\rho)<0
\]

while simultaneously satisfying

\[
D_B\log L_\rho
=\kappa+2\bar\sigma_\rho-\frac12
\]

and the strain/genealogy constraints inherited from M15--M16.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
