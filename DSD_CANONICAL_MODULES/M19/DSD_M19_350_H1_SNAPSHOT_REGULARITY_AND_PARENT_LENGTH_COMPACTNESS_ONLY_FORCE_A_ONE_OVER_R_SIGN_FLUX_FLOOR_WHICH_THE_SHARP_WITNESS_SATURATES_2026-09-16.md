# DSD M19-350 — H1 snapshot regularity plus parent-length compactness only forces a 1/R sign-flux floor, and the sharp sparse-residence witness saturates it

Date: 2026-09-16  
Canonical ID: **M19-350**

Status: **ACTIVE CRITICAL FLUX-FLOOR THEOREM / SNAPSHOT SOBOLEV LIMITATION / SHARPNESS AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Goal

M19-349 shows that any record-uniform superlinear moment of the line residence

\[
L_1(\lambda)=\int_{\Gamma_\lambda}\rho\,ds
\]

would eliminate sign-flux thinning.

The present module tests whether the currently certified snapshot regularity already yields such a gain.

The answer is negative: after the parent-length factor is included, the strongest direct Sobolev estimate gives only the critical lower bound

\[
\eta_S\gtrsim R^{-1},
\]

which is exactly saturated by M19-348.

## 2. Assumptions

Work on a retained normalized record slice with positive material-flux measure \(d\nu\), total flux

\[
0<\Phi_-\le\Phi\le\Phi_+<\infty,
\]

and flux probability

\[
dp_\Phi=d\nu/\Phi.
\]

Let \(S\) be one coefficient-sign sector with sign enstrophy floor

\[
\boxed{E_S:=\int_SL_1d\nu\ge e_*>0.}
\]

Assume the compact parent-length alternative

\[
\boxed{\ell(\lambda):=\mathcal H^1(\Gamma_\lambda)\le C_\ell R}
\]

for the represented lines relevant to \(S\).

If this upper bound fails, retain a super-parent arclength / line-folding decompactification branch instead of using the present theorem.

Finally assume the M19-319 snapshot palinstrophy/enstrophy bound, so by the whole-space Sobolev estimate

\[
\boxed{\|\rho\|_{L^6(\mathbb R^3)}\le C_S\|\nabla\Omega\|_2\le C_6.}
\]

## 3. Linewise Holder estimate

For any represented line,

\[
L_1(\lambda)=\int_{\Gamma_\lambda}\rho\,ds.
\]

Holder with exponent \(5\) gives

\[
\left(\int_{\Gamma_\lambda}\rho\,ds\right)^5
\le
\ell(\lambda)^4
\int_{\Gamma_\lambda}\rho^5ds.
\]

Using \(\ell(\lambda)\le C_\ell R\),

\[
\boxed{
L_1(\lambda)^5
\le
C R^4
\int_{\Gamma_\lambda}\rho^5ds.
}
\]

## 4. Integrate over flux labels

Integrating against \(dp_\Phi=d\nu/\Phi\),

\[
\mathbb E_{p_\Phi}[L_1^5]
\le
\frac{CR^4}{\Phi}
\int d\nu
\int_{\Gamma_\lambda}\rho^5ds.
\]

In flux coordinates

\[
d\nu\,ds=\rho\,dx.
\]

Therefore

\[
\int d\nu\int\rho^5ds
=
\int\rho^6dx.
\]

Hence

\[
\boxed{
\mathbb E_{p_\Phi}[L_1^5]
\le
CR^4\|\rho\|_6^6
\le
C_*R^4.
}
\]

This is a superlinear residence moment, but its norm grows exactly with the parent-length scale.

## 5. Sign-sector lower bound

Let

\[
\eta:=p_\Phi(S)=\Phi_S/\Phi.
\]

Its conditional mean residence is

\[
\bar L_S
=
\frac{E_S}{\Phi\eta}
\ge
\frac{e_*}{\Phi_+}\eta^{-1}
=:c_*\eta^{-1}.
\]

Jensen on the sign sector gives

\[
\mathbb E_{p_\Phi}[L_1^5]
\ge
\eta\bar L_S^5
\ge
c_*^5\eta^{-4}.
\]

Combining with Section 4,

\[
c_*^5\eta^{-4}
\le
C_*R^4.
\]

Thus

\[
\boxed{
\eta
\ge
\frac{c}{R}.
}
\]

This is the main M19-350 bound.

## 6. General exponent

More generally, if for some \(q>1\)

\[
\int\rho^{q+1}dx\le C_q
\]

and \(\ell(\lambda)\le C_\ell R\), then

\[
L_1^q
\le
(C_\ell R)^{q-1}
\int_{\Gamma_\lambda}\rho^qds,
\]

so

\[
\boxed{
\mathbb E_{p_\Phi}[L_1^q]
\le
C_q'R^{q-1}.
}
\]

The sign-sector lower bound is

\[
\mathbb E[L_1^q]
\ge
c_q\eta^{1-q}.
\]

Therefore for every such exponent

\[
\boxed{\eta\gtrsim R^{-1}.}
\]

The power of \(R\) cancels independently of \(q\). Stronger snapshot \(L^p\) integrability alone does not improve the flux-fraction exponent as long as line length remains of order \(R\).

## 7. L-infinity endpoint

If the normalized amplitude ceiling

\[
\rho\le M_\rho
\]

is used instead, then

\[
L_1\le M_\rho C_\ell R.
\]

Since \(E_S=\Phi\eta\bar L_S\ge e_*\), this again yields

\[
\boxed{\eta\ge cR^{-1}.}
\]

Thus even an amplitude \(L^\infty\) bound does not improve the critical exponent.

## 8. Sharpness via M19-348

The endpoint sparse-residence witness in M19-348 takes

\[
\eta\sim R^{-1},
\qquad
\bar L_S\sim R,
\qquad
\rho_S\sim1
\]

on a parent-length branch.

Then

\[
\eta\bar L_S\sim1
\]

and

\[
\eta\bar L_S^5\sim R^4,
\]

exactly saturating the Section 4 upper bound.

Therefore the \(R^{-1}\) flux floor cannot be improved by the present Holder/Sobolev argument.

## 9. Meaning for the residence-UI gate

M19-349 required a record-uniform bound on a superlinear function of \(L_1\).

M19-350 shows that current snapshot regularity gives instead a scale-dependent bound of the form

\[
\int L_1^qdp_\Phi
\lesssim R^{q-1}.
\]

This is precisely too weak to yield uniform integrability across the record sequence.

Hence

\[
\boxed{
\mathcal T_{res}^{UI}
\text{ is not supplied by snapshot }H^1/H^2\text{ regularity plus parent-length compactness alone.}
}
\]

A successful theorem must exploit additional structure, such as

1. temporal material-line deformation and return;
2. sign-interface capacity/coercivity;
3. a line-length bound sublinear in \(R\) on the thinning sign sector;
4. a nonreuse/genealogy theorem;
5. terminal dilation-hull rigidity.

## 10. Audit verdict

**PASS — current snapshot Sobolev control reduces sign thinning only to the critical \(1/R\) scale.**

Under a parent-length upper bound and the certified snapshot palinstrophy bound, a nontrivial sign-enstrophy sector must carry at least \(c/R\) of material flux. The M19-348 endpoint witness attains this rate, so no stronger conclusion follows from these ingredients alone.

The next target is the endpoint \(\eta\asymp R^{-1}\) geometry: determine whether an order-one-amplitude sign bundle of flux \(R^{-1}\) and parent length \(R\) can coexist with the global palinstrophy bound without paying a logarithmic transverse-capacity cost.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
