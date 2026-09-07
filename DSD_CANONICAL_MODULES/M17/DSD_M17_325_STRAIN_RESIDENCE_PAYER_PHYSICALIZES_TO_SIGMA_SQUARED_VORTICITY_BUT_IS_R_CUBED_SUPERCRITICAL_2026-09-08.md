# DSD M17-325 — strain-residence payer physicalizes to sigma-squared vorticity but is R-cubed supercritical

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION / SCALING AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-324

One surviving branch of the inverse-line-weight renormalized current reduction gives a positive normalized time density of

\[
\int
\bar\sigma_\rho^2\,L_\rho^{-1}\,d\Phi,
\]

restricted to the retained negative-\(\kappa\) material population.

Here

\[
L_\rho
=\int_{\Gamma}\rho\,ds,
\qquad
\bar\sigma_\rho
=\frac{\int_{\Gamma}\sigma\rho\,ds}{L_\rho},
\]

and \(d\Phi\) is oriented material vorticity flux.

## 2. Flux-coordinate physicalization

On a regular vortex tube,

\[
d\Phi=\rho\,dA,
\]

and therefore

\[
dy=dA\,ds=\frac{d\Phi}{\rho}\,ds.
\]

Weighted Jensen/Cauchy--Schwarz on one retained line gives

\[
\left(\int_\Gamma\sigma\rho\,ds\right)^2
\le
\left(\int_\Gamma\rho\,ds\right)
\left(\int_\Gamma\sigma^2\rho\,ds\right).
\]

Hence

\[
\boxed{
\bar\sigma_\rho^2L_\rho
\le
\int_\Gamma\sigma^2\rho\,ds.
}
\]

Multiplying by \(d\Phi\) and using the tube Jacobian,

\[
\boxed{
\bar\sigma_\rho^2L_\rho\,d\Phi
\le
\int_\Gamma\sigma^2\rho\,ds\,d\Phi
=
\int_{tube}\sigma^2\rho^2\,dy.
}
\]

Thus the strain-residence square has a genuine spatial PDE realization.

## 3. Convert the inverse-line-weight payer

Suppose the retained captured family satisfies the lower line-weight bound

\[
L_\rho\ge L_*>0.
\]

Then

\[
\bar\sigma_\rho^2L_\rho
=L_\rho^2
\left(\bar\sigma_\rho^2L_\rho^{-1}\right)
\ge
L_*^2
\left(\bar\sigma_\rho^2L_\rho^{-1}\right).
\]

Therefore

\[
\boxed{
\int_{retained}\sigma^2\rho^2\,dy
\ge
L_*^2
\int_{labels}
\bar\sigma_\rho^2L_\rho^{-1}\,d\Phi.
}
\]

If the lower line-weight bound fails, record the already typed amplitude/line-weight degeneration exit rather than importing the inequality.

Hence M17-324's positive strain-residence payer does physicalize spatially to the nonnegative quantity

\[
\boxed{
Q_\sigma(\theta)
:=
\int_{retained}\sigma^2|W|^2dy.
}
\]

On exact CE-H, \(\Sigma W=\sigma W\), so equivalently

\[
Q_\sigma
=\int_{retained}|\Sigma W|^2dy.
\]

## 4. Record blow-down scaling

For the standard Navier--Stokes parabolic blow-down

\[
V_R(y,s)=R V(Ry,R^2s),
\]

vorticity and strain both scale as

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

\[
\Sigma_R(y,s)=R^2\Sigma(Ry,R^2s).
\]

Consequently

\[
\rho_R=R^2\rho,
\qquad
\sigma_R=R^2\sigma.
\]

Thus

\[
\sigma_R^2\rho_R^2
=R^8\sigma^2\rho^2.
\]

Since

\[
dy=R^{-3}dx,
\qquad
ds=R^{-2}dt,
\]

we obtain

\[
\boxed{
\int_I\int
\sigma_R^2\rho_R^2\,dy\,ds
=
R^3
\int_{R^2I}\int
\sigma^2\rho^2\,dx\,dt.
}
\]

Therefore this spacetime payer is supercritical by **three powers of the record scale**.

## 5. Comparison with the M17-307 ancestral palinstrophy ledger

Vorticity palinstrophy obeys

\[
\int|\nabla\Omega_R|^2dy\,ds
=R
\int|\nabla\Omega|^2dx\,dt.
\]

Hence its ancestral transfer requires one inverse power \(R^{-1}\).

By contrast the newly physicalized strain-stretching square requires

\[
\boxed{R^{-3}}
\]

for scale-neutral ancestral accounting.

Thus, as an ancestral finite-budget candidate,

\[
\boxed{
\int\sigma^2\rho^2
\quad\text{is two scale powers worse than palinstrophy.}
}
\]

## 6. No certified finite original-coordinate spacetime budget

The currently certified first-generation finite resource is the palinstrophy-type quantity used in M17-307.  There is no established implication in the present chain of the form

\[
\int_{-\infty}^0\int\sigma^2\rho^2dxdt<\infty.
\]

Smoothness on compact time slabs does not supply a uniform ancient-time integral, and the pointwise/spatial physicalization above does not create one.

Therefore the following shortcut is forbidden:

\[
\boxed{
\text{positive normalized }Q_\sigma\text{ density}
\not\Rightarrow
\text{finite-budget contradiction}.
}
\]

## 7. Consequence for the DSD-derived route

The DSD channel-separation heuristic successfully exposed a real PDE quantity, but the scaling audit rejects it as the desired cross-generation finite currency.

This is useful pruning:

\[
\boxed{
\text{strain-residence square is a local payer, not the missing critical ancestral ledger.}
}
\]

The remaining high-value possibilities are therefore:

1. extract a scale-critical quantity from directed zero-level turnover;
2. find a dimensionless ratio combining turnover with line/flux scales;
3. prove a rigidity theorem directly in the normalized recurrent hull, avoiding finite-budget accumulation;
4. return to a typed genealogy/replacement exit.

## 8. Audit verdict

**PASS for spatial physicalization; FAIL as a presently available ancestral finite-budget closure.**

The failure is quantitative and comes from exact Navier--Stokes scaling, not from the DSD heuristic.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
