# M18-024 — Viscosity consistency corrects the bulk rate identity and the combined source square descends to palinstrophy and D3

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE VISCOSITY CORRECTION / COMBINED-SOURCE DESCENT / SOURCE-SQUARE REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Audit trigger

The repository problem setting keeps

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nu>0.
\]

On exact CE-H,

\[
\Delta\Omega=\kappa\Omega,
\qquad
\Sigma\Omega=\sigma\Omega,
\]

where

\[
\Sigma:=\frac12(\nabla u+\nabla u^T).
\]

Hence the vorticity equation is

\[
\boxed{
D_t\Omega=(\sigma+\nu\kappa)\Omega.
}
\]

M17-339 and M18-022 wrote the physical coefficient law in the \(\nu=1\) form

\[
D_t\kappa=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom}.
\]

That formula is correct only after an explicit \(\nu=1\) normalization. The repository-level problem statement does not globally make that normalization, and M18-021--023 simultaneously retained \(\nu\) in the amplitude equation. Therefore the general-\(\nu\) coefficient law must be restored before continuing the audit.

This module is authoritative for M18-022--023 whenever \(\nu\neq1\).

## 2. Exact material-Laplacian commutator

For a smooth vector field \(X\),

\[
\boxed{
D_t\Delta X
=
\Delta D_tX
-2(\partial_i u_j)\partial_{ij}X
-(\Delta u_j)\partial_jX.
}
\]

Apply this to \(X=\Omega\).

Set

\[
\lambda:=\sigma+\nu\kappa,
\qquad
h:=D_t\kappa.
\]

Since

\[
D_t\Omega=\lambda\Omega
\]

and

\[
\Delta\Omega=\kappa\Omega,
\]

we have

\[
D_t(\Delta\Omega)
=h\Omega+\kappa\lambda\Omega.
\]

On the other hand,

\[
\Delta(\lambda\Omega)
=(\Delta\lambda)\Omega
+2\nabla\lambda\cdot\nabla\Omega
+\lambda\kappa\Omega.
\]

The \(\lambda\kappa\Omega\) terms cancel. Therefore

\[
\boxed{
 h\Omega
=(\Delta\lambda)\Omega
+2\nabla\lambda\cdot\nabla\Omega
-\mathcal K,
}
\]

where

\[
\boxed{
\mathcal K
:=
2(\partial_i u_j)\partial_{ij}\Omega
+(\Delta u_j)\partial_j\Omega.
}
\]

Because \(\partial_{ij}\Omega\) is symmetric in \(i,j\), the antisymmetric part of \(\partial_i u_j\) drops from the first contraction, so that term may equivalently use \(\Sigma_{ij}\).

## 3. Correct general-viscosity coefficient law

Write

\[
\Omega=\rho\xi,
\qquad
\rho=|\Omega|.
\]

On \(\rho>0\),

\[
\xi\cdot\partial_i\Omega=\partial_i\rho.
\]

Project Section 2 onto \(\xi\) and divide by \(\rho\):

\[
 h
=
\Delta\lambda
+2\nabla\log\rho\cdot\nabla\lambda
-\frac1\rho\xi\cdot\mathcal K.
\]

Thus

\[
\boxed{
D_t\kappa
=\nu L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{\rm geom},
}
\]

where

\[
L_\rho f
:=
\Delta f+2\nabla\log\rho\cdot\nabla f
=
\rho^{-2}\nabla\cdot(\rho^2\nabla f),
\]

and

\[
\boxed{
\mathcal R_{\rm geom}
=-\frac1\rho\xi\cdot\mathcal K.
}
\]

This recovers the previous M17-339 formula exactly when \(\nu=1\).

## 4. Corrected M18-022 bulk identity

M18-022 derived, before substituting the coefficient law,

\[
\boxed{
\dot B_\phi
=
2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx
-\int\phi'h\rho^2|\nabla\kappa|^2dx
-2\int\phi\rho^2hL_\rho\kappa\,dx.
}
\]

This pre-substitution identity remains correct.

Set

\[
A:=L_\rho\kappa,
\qquad
C:=L_\rho\sigma+\mathcal R_{\rm geom},
\]

so that the corrected coefficient law is

\[
\boxed{h=\nu A+C.}
\]

The exact algebraic identity is

\[
\boxed{
2hA
=\nu A^2+\nu^{-1}h^2-\nu^{-1}C^2.
}
\]

Therefore the general-viscosity bulk rate identity is

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+\nu\int\phi\rho^2|L_\rho\kappa|^2dx
+\nu^{-1}\int\phi\rho^2|D_t\kappa|^2dx\\
={}&
2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-\int\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx\\
&+\nu^{-1}\int\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
\end{aligned}
}
\]

M18-022 is the \(\nu=1\) specialization of this identity.

## 5. Corrected M18-023 cutoff absorption

For the squared cutoff \(\phi=\chi^2\), M18-023 used Young absorption into the favorable \(|h|^2\) term.

With the corrected coefficient in front of that term, for every \(\varepsilon>0\),

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon\nu^{-1}
\int\phi\rho^2|h|^2dx
+
\frac{\nu C_\chi^2}{\varepsilon\delta_0^2}
\int_{\mathcal K}\rho^2|\nabla\kappa|^4dx.
}
\]

Hence under the M18-023 normalized collar-gradient ceiling,

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon\nu^{-1}H_\phi
+C_{\chi,\varepsilon}\nu\,
\Gamma_{\mathcal K}\delta_0B_{\widetilde\phi}.
}
\]

Since \(\nu>0\) is fixed under Navier--Stokes scaling, this correction changes constants but not the representation class or the collar-gradient dichotomy.

## 6. Combined source before termwise decomposition

The source square left by M18-022 is

\[
R_\phi
:=
\int\phi\rho^2|C|^2dx,
\qquad
C=L_\rho\sigma+\mathcal R_{\rm geom}.
\]

M17-463 forbids estimating an invented termwise decomposition without exact provenance. Here the combined source has an exact commutator representation, so it can be audited as one object.

From Section 3,

\[
\boxed{
\rho C
=\rho L_\rho\sigma-\xi\cdot\mathcal K.
}
\]

No derivative of the coefficient \(\kappa\) appears in this formula.

## 7. Exact weighted formula for \(\rho L_\rho\sigma\)

On exact CE-H,

\[
\Sigma\xi=\sigma\xi,
\qquad
|\xi|=1.
\]

Since \(\Sigma\) is symmetric,

\[
\partial_i\sigma
=\xi\cdot(\partial_i\Sigma)\xi.
\]

Differentiating once more,

\[
\Delta\sigma
=
\xi\cdot(\Delta\Sigma)\xi
+2\sum_i
(\partial_i\xi)\cdot(\partial_i\Sigma)\xi.
\]

Using

\[
\partial_i\Omega
=(\partial_i\rho)\xi+\rho\partial_i\xi,
\]

we obtain the exact weighted cancellation

\[
\boxed{
\rho L_\rho\sigma
=
\rho\,\xi\cdot(\Delta\Sigma)\xi
+2\sum_i
\partial_i\Omega\cdot(\partial_i\Sigma)\xi.
}
\]

The separate \(\nabla\log\rho\) and \(\nabla\xi\) factors have combined into ordinary vorticity derivatives.

## 8. Combined source commutator formula

Combining Sections 6--7,

\[
\boxed{
\begin{aligned}
\rho C
={}&
\rho\,\xi\cdot(\Delta\Sigma)\xi
+2\sum_i
\partial_i\Omega\cdot(\partial_i\Sigma)\xi\\
&-
\xi\cdot
\left[
2\Sigma_{ij}\partial_{ij}\Omega
+(\Delta u_j)\partial_j\Omega
\right].
\end{aligned}
}
\]

For incompressible velocity,

\[
\Delta u=-\nabla\times\Omega.
\]

Thus the combined source uses only:

- \(\Omega\) and its first/second spatial derivatives;
- \(u\) through \(\Sigma\), \(\nabla\Sigma\), and \(\Delta\Sigma\), which are Calderon--Zygmund transforms of the corresponding vorticity derivatives.

No coefficient second or third jet is required.

## 9. Nodal-safe magnitude bound

The exact identity is derived on \(\rho>0\), but its magnitude yields a bound with no negative power of \(\rho\):

\[
\boxed{
\begin{aligned}
\rho^2|C|^2
\lesssim{}&
\rho^2|\Delta\Sigma|^2
+|\nabla\Omega|^2|\nabla\Sigma|^2\\
&+|\Sigma|^2|D^2\Omega|^2
+|\Delta u|^2|\nabla\Omega|^2.
\end{aligned}
}
\]

The right-hand side is meaningful across vorticity nodes. Therefore the weighted source square can be estimated without dividing by \(\rho\).

## 10. Whole-space Sobolev / Calderon--Zygmund descent

Define the snapshot resources

\[
P:=\|\nabla\Omega\|_2^2,
\qquad
H:=\|D^2\Omega\|_2^2,
\qquad
J_3:=\|D^3\Omega\|_2^2.
\]

On \(\mathbb R^3\), Calderon--Zygmund estimates give, for \(1<p<\infty\),

\[
\|D^k\Sigma\|_p
\lesssim
\|D^k\Omega\|_p,
\]

and incompressibility gives

\[
\Delta u=-\nabla\times\Omega.
\]

Sobolev and interpolation imply

\[
\|\Omega\|_6^2\lesssim P,
\]

\[
\|D^2\Omega\|_3^2
\lesssim
H^{1/2}J_3^{1/2},
\]

and

\[
\|\nabla\Omega\|_4^4
\lesssim
P^{1/2}H^{3/2}.
\]

Applying these estimates to Section 9 yields

\[
\boxed{
R_\phi
\lesssim
P\,H^{1/2}J_3^{1/2}
+P^{1/2}H^{3/2}.
}
\]

This estimate is independent of the detailed termwise representation of \(\mathcal R_{\rm geom}\).

## 11. Eliminate H in favor of P and D3

Fourier Cauchy--Schwarz gives

\[
\boxed{
H
\le
P^{1/2}J_3^{1/2}.
}
\]

Therefore both terms in Section 10 obey the same upper bound:

\[
P\,H^{1/2}J_3^{1/2}
\lesssim
P^{5/4}J_3^{3/4},
\]

and

\[
P^{1/2}H^{3/2}
\lesssim
P^{5/4}J_3^{3/4}.
\]

Hence

\[
\boxed{
R_\phi
\lesssim
P^{5/4}J_3^{3/4}.
}
\]

This is the main source-square descent theorem.

## 12. Spacetime consequence on a normalized record interval

Let \(I\) be a finite normalized record interval and set

\[
P_I^*:=\sup_{t\in I}P(t).
\]

Then

\[
\begin{aligned}
\int_I R_\phi(t)dt
&\lesssim
(P_I^*)^{5/4}
\int_I J_3(t)^{3/4}dt\\
&\le
(P_I^*)^{5/4}
|I|^{1/4}
\left(\int_IJ_3(t)dt\right)^{3/4}.
\end{aligned}
\]

Thus

\[
\boxed{
\int_I R_\phi dt
\lesssim
(P_I^*)^{5/4}|I|^{1/4}
\left(\int_I\|D^3\Omega\|_2^2dt\right)^{3/4}.
}
\]

M17-444 supplies the D3 spacetime resource. Therefore the full strain/geometry source square is controlled on normalized record families with a uniform snapshot palinstrophy ceiling.

No amplitude \(L^\infty\) ceiling and no full velocity-gradient \(L^\infty\) ceiling are required for this bound.

## 13. Exact remaining source exit

The source-square branch is therefore reduced to

\[
\boxed{
G_{\rm strain/geometry\ source\ square}
\Longrightarrow
G_{\rm D3\ spacetime\ resource}
\lor
G_{\rm palinstrophy\ snapshot\ decompactification}
\lor
G_{\rm interval/genealogy\ loss}.
}
\]

More precisely, if the normalized interval length and inherited D3 spacetime charge remain controlled while \(R_\phi\) cannot be controlled, then

\[
\boxed{
P_I^*=\sup_I\|\nabla\Omega\|_2^2\to\infty.
}
\]

Thus the previous opaque source-square branch is replaced by a standard analytic quantity: snapshot palinstrophy decompactification.

## 14. Scaling audit

The estimate in Section 12 is scale consistent.

Under

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

snapshot palinstrophy scales as

\[
P_R=R^3P,
\]

D3 snapshot energy scales as

\[
J_{3,R}=R^7J_3,
\]

and record time scales as \(R^{-2}\).

Therefore

\[
(P_R^*)^{5/4}|I_R|^{1/4}
\left(\int_{I_R}J_{3,R}ds\right)^{3/4}
\]

scales as

\[
R^{15/4}R^{-1/2}R^{15/4}=R^7,
\]

which is exactly the spacetime scaling of

\[
\int R_\phi dt.
\]

No hidden scale mismatch is present.

## 15. Corrected local bulk inequality

Combining the general-\(\nu\) identity with M18-023 gives, under the adapted-cutoff hypotheses,

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+\nu A_\phi
+(1-\varepsilon)\nu^{-1}H_\phi\\
&\le
C M_*\delta_0B_\phi
+C_{\chi,\varepsilon}\nu\Gamma_{\mathcal K}\delta_0B_{\widetilde\phi}
+\nu^{-1}R_\phi,
\end{aligned}
}
\]

where

\[
A_\phi:=\int\phi\rho^2|L_\rho\kappa|^2dx,
\qquad
H_\phi:=\int\phi\rho^2|D_t\kappa|^2dx.
\]

Using Section 11,

\[
R_\phi\lesssim P^{5/4}J_3^{3/4}.
\]

Therefore, inside the normalized compact collar family, the only newly exposed standard analytic exit is a large snapshot palinstrophy.

## 16. Updated local branch tree

The M18-023 branch tree is corrected and sharpened to

\[
\boxed{
\begin{aligned}
G_{\rm robust\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm normalized\ collar\ gradient\ concentration}\\
&\lor G_{\rm snapshot\ palinstrophy\ decompactification}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

The opaque independent strain/geometry source-square branch has been removed under the exact combined-source estimate.

## 17. Audit verdict

### Certified

1. For the repository's general \(\nu>0\) setting, the CE-H coefficient law contains \(\nu L_\rho\kappa\).
2. M18-022--023 are valid as written only in the \(\nu=1\) normalization; the formulas in this module supersede them for general \(\nu\).
3. The combined source has an exact material-Laplacian commutator provenance.
4. Weighted combination removes explicit negative powers of the amplitude from the source-square estimate.
5. The full source square satisfies
   \[
   R_\phi\lesssim P^{5/4}J_3^{3/4}.
   \]
6. With a uniform snapshot palinstrophy ceiling, the source square is spacetime controlled by the existing D3 resource on finite normalized intervals.

### Not certified

1. A record-uniform snapshot palinstrophy ceiling.
2. An ancestry contradiction from the source-square estimate alone.
3. Thickness or integrated payment from collar-gradient essential-sup concentration.
4. Closure of the remaining critical/tube/domain/genealogy exits.
5. Global 3D Navier--Stokes regularity.

## 18. Next target

M18-025 should audit the new standard exit

\[
\boxed{
P_I^*=\sup_{t\in I}\|\nabla\Omega(t)\|_2^2\to\infty.
}
\]

The goal is to determine whether a high snapshot palinstrophy can be thickened in time into the already finite raw-H2 or D3 spacetime ledgers, analogous to the earlier enstrophy/raw-H2 thickening steps, or whether rapid palinstrophy spikes define a new scale-invariant temporal concentration branch.
