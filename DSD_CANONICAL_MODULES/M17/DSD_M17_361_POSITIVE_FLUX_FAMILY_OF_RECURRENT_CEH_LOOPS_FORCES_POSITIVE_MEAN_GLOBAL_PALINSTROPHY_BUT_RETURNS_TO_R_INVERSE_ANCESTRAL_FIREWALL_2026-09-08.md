# DSD M17-361 — Positive-flux family of recurrent CE-H loops forces positive mean global palinstrophy but returns to the inverse-record-scale ancestral firewall

Date: 2026-09-08  
Canonical ID: **M17-361**

Status: **ACTIVE LOOP-PAYER PHYSICALIZATION / NO GLOBAL CONTRADICTION CLAIM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-188 and M17-360

On a compact recurrent same-material closed-loop CE-H state, M17-188 gives

\[
\left\langle
\|\partial_s\sigma\|_{L^2(ds)}
\|\partial_s\rho\|_{L^2(ds)}
\right\rangle
\ge c_*>0.
\]

Hence by Young,

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2^2
+
\|\partial_s\rho\|_2^2
\right\rangle
\ge2c_*.
}
\]

M17-360 shows that a compact nondegenerate closed-loop orbit contains such a recurrent minimal-hull state.

The present module assumes a retained recurrent loop **flux family** `Lambda` with total oriented positive flux

\[
\boxed{
\Phi_{loop}:=\int_\Lambda d\Phi\ge\Phi_*>0
}
\]

and uniform compact loop constants, so the same lower constant `c_*` applies throughout the family.

If no positive-flux recurrent family is available, retain the explicit exit

\[
G_{loop\ flux\ thinning/allocation}.
\]

## 2. Integrate the loop payer over flux labels

For each loop label `lambda`, write

\[
a_\lambda^2
:=
\oint_{\Gamma_\lambda}|\partial_s\sigma|^2ds,
\]

\[
b_\lambda^2
:=
\oint_{\Gamma_\lambda}|\partial_s\rho|^2ds.
\]

Integrating the recurrent lower bound over material flux labels gives

\[
\boxed{
\left\langle
\int_\Lambda
(a_\lambda^2+b_\lambda^2)d\Phi
\right\rangle
\ge
2c_*\Phi_*.
}
\]

## 3. Flux-coordinate conversion

On the regular vortex-tube family,

\[
dy=\frac{d\Phi\,ds}{\rho},
\]

so

\[
\boxed{d\Phi\,ds=\rho\,dy.}
\]

Therefore

\[
\int_\Lambda b_\lambda^2d\Phi
=
\int_{\mathcal T_{loop}}
\rho|\partial_s\rho|^2dy.
\]

Likewise

\[
\int_\Lambda a_\lambda^2d\Phi
=
\int_{\mathcal T_{loop}}
\rho|\partial_s\sigma|^2dy.
\]

On the compact branch

\[
\rho\le M_\rho.
\]

Hence

\[
\int_\Lambda b_\lambda^2d\Phi
\le
M_\rho
\int_{\mathcal T_{loop}}|\nabla\rho|^2dy.
\]

Since `rho=|W|`, Kato's pointwise inequality gives

\[
|\nabla\rho|\le|\nabla W|.
\]

Thus

\[
\boxed{
\int_\Lambda b_\lambda^2d\Phi
\le
M_\rho\|\nabla W\|_2^2.
}
\]

## 4. Exact CE-H eigenvalue-gradient identity

On CE-H,

\[
\Sigma\xi=\sigma\xi,
\qquad |\xi|=1.
\]

Differentiate

\[
\sigma=\xi\cdot\Sigma\xi.
\]

For each coordinate `j`,

\[
\partial_j\sigma
=
(\partial_j\xi)\cdot\Sigma\xi
+
\xi\cdot(\partial_j\Sigma)\xi
+
\xi\cdot\Sigma(\partial_j\xi).
\]

Using

\[
\Sigma\xi=\sigma\xi
\]

and

\[
\xi\cdot\partial_j\xi=0,
\]

the two eigenvector-derivative terms cancel exactly. Hence

\[
\boxed{
\partial_j\sigma
=
\xi\cdot(\partial_j\Sigma)\xi.
}
\]

Therefore

\[
\boxed{|
\nabla\sigma|
\le
|\nabla\Sigma|.}
\]

Consequently

\[
\int_\Lambda a_\lambda^2d\Phi
\le
M_\rho\|\nabla\Sigma\|_2^2.
\]

## 5. Global Fourier identity for divergence-free velocity

For divergence-free `U`, with

\[
W=\nabla\times U,
\qquad
\Sigma=\frac12(\nabla U+\nabla U^T),
\]

the Fourier identities give

\[
\boxed{
\|\nabla\Sigma\|_2^2
=
\frac12\|\nabla W\|_2^2.
}
\]

Indeed, at frequency `xi`, divergence-free means `xi·Uhat=0`, and

\[
|\widehat\Sigma|^2
=\frac12|\xi|^2|\widehat U|^2,
\]

while

\[
|\widehat W|^2
=|\xi|^2|\widehat U|^2.
\]

Multiplying both by `|xi|^2` and integrating proves the identity.

## 6. Positive recurrent palinstrophy mean

Combining Sections 2--5,

\[
2c_*\Phi_*
\le
M_\rho
\left(
\|\nabla\Sigma\|_2^2
+
\|\nabla W\|_2^2
\right).
\]

Hence

\[
2c_*\Phi_*
\le
\frac32M_\rho\|\nabla W\|_2^2.
\]

Taking the recurrent time mean gives

\[
\boxed{
\left\langle
\|\nabla W\|_2^2
\right\rangle
\ge
\frac{4c_*\Phi_*}{3M_\rho}
=:
 p_*>0.
}
\]

Thus a positive-flux family of compact recurrent CE-H loops necessarily carries a fixed positive normalized palinstrophy density.

## 7. Relation to M5-688 strain-gradient payer

The exact identity

\[
|\nabla\sigma|\le|\nabla\Sigma|
\]

also confirms that the M17-188 strain-gradient channel is not an independent high-order mystery: it lies at the same derivative order as vorticity palinstrophy.

On high-amplitude tube regions, weighted quantities such as

\[
\rho^2|\nabla\sigma|^2
\]

are correspondingly controlled above by compact-amplitude multiples of palinstrophy-scale fields.

This is a payer identification, not a sign contradiction.

## 8. Cross-generation audit

The recurrent lower bound

\[
\langle\|\nabla W\|_2^2\rangle\ge p_*
\]

is a normalized second-generation statement.

M17-306--307 show that under record blow-down, a unit descendant palinstrophy window pulls back with the inverse record-scale currency:

\[
\boxed{
R_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds
}
\]

is the ancestral finite quantity.

Thus fixed normalized loop palinstrophy payments at every record generation contribute only

\[
\sim R_m^{-1}
\]

to the first-generation ancestral ledger.

Because the record scales are geometric,

\[
\sum_mR_m^{-1}<\infty.
\]

Therefore

\[
\boxed{
\text{positive recurrent loop palinstrophy density}
\not\Rightarrow
\text{ancestral palinstrophy contradiction}.
}
\]

The R21/M17-307 firewall survives.

## 9. Updated loop branch

The compact positive-flux closed-loop branch now satisfies

\[
\boxed{
H_{compact\ recurrent\ loop\ family}
\Longrightarrow
H_{positive\ normalized\ palinstrophy\ density}
\Longrightarrow
G_{ancestral\ R^{-1}\ firewall}.
}
\]

If the positive-flux loop family itself disappears, retain

\[
G_{loop\ flux\ thinning/allocation}.
\]

Thus the loop geometry is quantitatively physicalized, but the remaining obstruction is again cross-generation criticality rather than local payer identification.

## 10. DSD-theory role

The heuristic role is to demand that a geometric payer be translated into an ordinary PDE norm before it is treated as evidence. The translation above is standard flux-coordinate calculus, the CE-H eigenvector identity, and Fourier analysis.

No DSD axiom is used as a PDE hypothesis.

## 11. Audit verdict

**PASS as a loop-payer physicalization.**

It closes the ambiguity about what the M17-188 gradient payer costs, while explicitly showing why that cost still does not close the cross-generation proof.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
