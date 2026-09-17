# DSD M19-366 — The critical (3/2,-1/2) lock is a pure transverse-area inflation conveyor

Date: 2026-09-17  
Canonical ID: **M19-366**

Status: **ACTIVE CRITICAL-LOCK GEOMETRY / TRANSVERSE AREA INFLATION / STATIONARY PACKING FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-365 shows that a fully compact long dormant-to-active CE-H seed at the critical amplification boundary satisfies

\[
(\bar\kappa,\bar\sigma)\to\left(\frac32,-\frac12\right).
\]

M5-631 gives the exact material tube laws

\[
D_B\log\rho=\sigma+\kappa-1,
\]

\[
D_B\log A_\perp=1-\sigma,
\]

\[
D_B\log\ell=\sigma+\frac12,
\]

\[
D_B\log|\phi|=\kappa,
\]

and

\[
D_B\log|\mathcal K|=-\sigma-\frac12.
\]

## 2. Exact locked rates

At the pointwise locked model

\[
\kappa=\frac32,
\qquad
\sigma=-\frac12,
\]

one obtains

\[
\boxed{D_B\log\rho=0,}
\]

\[
\boxed{D_B\log|\mathcal K|=0,}
\]

\[
\boxed{D_B\log\ell=0,}
\]

\[
\boxed{D_B\log A_\perp=\frac32,}
\]

and

\[
\boxed{D_B\log|\phi|=\frac32.}
\]

Thus the critical seed does not need longitudinal stretching or vorticity-amplitude growth. Its flux growth is supplied exactly by transverse area expansion.

## 3. Tube aspect ratio

M5-631 defines

\[
\mathcal R_{tube}:=\frac{d\mathcal E}{\phi^2}=\frac{\ell}{A_\perp}
\]

with

\[
D_B\log\mathcal R_{tube}=2\sigma-\frac12.
\]

At the lock,

\[
\boxed{D_B\log\mathcal R_{tube}=-\frac32.}
\]

Hence over a preactivation interval of length \(T\),

\[
\boxed{\mathcal R_{tube}(T)\asymp e^{-3T/2}\mathcal R_{tube}(0).}
\]

The critical conveyor is therefore a progressive loss of longitudinal-to-transverse aspect ratio.

## 4. Enstrophy consistency

The tube enstrophy element is

\[
d\mathcal E=\phi^2\mathcal R_{tube}.
\]

Since

\[
\phi^2\sim e^{3T},
\qquad
\mathcal R_{tube}\sim e^{-3T/2},
\]

we recover

\[
\boxed{d\mathcal E\sim e^{3T/2}.}
\]

This is exactly the M19-365 material-enstrophy growth law and the M19-362 seed scaling.

## 5. Remaining-time profile

Use M19-364 remaining time \(s\ge0\), where activation occurs at \(s=0\).

For a seed whose activation cross-section is \(A_*\), line length is \(\ell_*\), amplitude is \(\rho_*\), and curvature is \(K_*\), the exact locked scaling is

\[
\boxed{A_\perp(s)=A_*e^{-3s/2},}
\]

while

\[
\boxed{\ell(s)=\ell_*,\quad \rho(s)=\rho_*,\quad |\mathcal K(s)|=K_*}
\]

in the ideal locked model.

Consequently

\[
\phi(s)=\rho_*A_*e^{-3s/2},
\]

and

\[
d\mathcal E(s)=\rho_*^2A_*\ell_*e^{-3s/2}.
\]

Thus flux, material volume, and enstrophy all share the same dormant \(e^{-3s/2}\) scale because the only shrinking dormant geometric coordinate is cross-sectional area.

## 6. Stationary area reservoir

For constant renewal rate \(\lambda\), the total instantaneous dormant transverse-area content is

\[
\mathcal A_{dorm}
:=\lambda\int_0^\infty A_*e^{-3s/2}ds
=\boxed{\frac23\lambda A_*<\infty.}
\]

Likewise the total dormant line-length weighted only by label count would diverge if every future seed retained an independent \(O(1)\) line segment forever, but this quantity is not a physical volume or flux resource because the corresponding cross-sectional area tends exponentially to zero. A contradiction cannot be inferred from line-count length alone without a nonzero-thickness or packing theorem.

## 7. Geometric interpretation

The critical seed is best described as

\[
\boxed{
\text{exponentially thin dormant material tube}
\to
\text{transverse inflation at rate }3/2
\to
\text{order-one active carrier},
}
\]

with approximately neutral longitudinal length, vorticity magnitude, and curvature.

This is not the ordinary vortex-stretching picture. The similarity-frame volume expansion is used almost entirely as transverse area growth.

## 8. Immediate no-go consequence

Therefore none of the following alone can close the critical branch:

1. finite instantaneous dormant material volume;
2. finite instantaneous dormant cross-sectional area;
3. bounded vorticity amplitude;
4. bounded curvature;
5. bounded material line length.

All are compatible with the locked conveyor at the scaling level.

A successful closure must prohibit the required repeated transverse-area inflation, or couple it nonrecyclably to transverse strain anisotropy, pressure/viscous forcing, topology/genealogy, or a minimum dormant thickness.

## 9. Relation to transverse strain

Incompressibility gives

\[
\lambda_2+\lambda_3=-\sigma=\frac12
\]

for the two transverse physical strain eigenvalues of \(\Sigma\).

The material \(B\)-flow transverse area rate is

\[
(\lambda_2+\tfrac12)+(\lambda_3+\tfrac12)
=\frac32,
\]

exactly matching the area law.

Thus the endpoint is dynamically coherent with trace-free strain: longitudinal \(B\)-rate is zero while total transverse \(B\)-rate is \(3/2\).

## 10. New target

The next theorem gate is no longer an abstract amplification gap. It is

\[
\boxed{
\mathcal T_{area}^{crit}:
\text{can positive-density critical seed renewals sustain repeated }e^{3T/2}
\text{ transverse-area inflation without a nonrecyclable transverse-deformation/topology cost?}
}
\]

The relevant historical inputs are M5-622--630: transverse magnitude forcing, strain-eigenvalue gap/collision compensation, kappa-level relabeling, and covariance/turnover corrections.

## 11. Audit verdict

**PASS — the critical (3/2,-1/2) seed conveyor has a concrete geometric realization at the level of exact CE-H transport laws.**

It is a transverse-area inflation mechanism, not an amplitude-growth or line-stretching mechanism. This sharpens the survivor rather than closing it.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
