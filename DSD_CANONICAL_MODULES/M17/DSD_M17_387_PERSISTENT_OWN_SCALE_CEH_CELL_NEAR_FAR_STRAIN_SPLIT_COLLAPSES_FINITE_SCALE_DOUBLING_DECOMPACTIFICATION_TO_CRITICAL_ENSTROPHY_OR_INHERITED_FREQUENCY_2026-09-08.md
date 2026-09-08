# DSD M17-387 — Persistent own-scale CE-H cell near/far strain split collapses finite-scale doubling decompactification to critical enstrophy or inherited frequency

Date: 2026-09-08  
Canonical ID: **M17-387**

Status: **ACTIVE LOCAL ELLIPTIC/BIOT--SAVART REDUCTION / STRONGER DOUBLING-PAYER THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why M17-386 leaves one spatial issue

M17-386 proves exact spacetime raw-`H2` ownership by coefficient scale and a single-genealogy temporal Carleson packing.

Its remaining obstruction is that the M17-385 deformation payer

\[
\|\Sigma\|_\infty
\]

is nonlocal. A coherent large-scale strain can deform many spatial child cells simultaneously, so it cannot be charged independently to each child raw-`H2` cell without a localization theorem.

The present module asks a more direct question:

> on a persistent own-scale exact CE-H cell, can the strain itself be bounded at the natural scale without invoking a separate local raw-`H2` allocation?

The answer is yes, conditionally on persistent own-scale CE-H geometry.

## 2. Persistent own-scale CE-H cell

Let `x_t` be a material center and let `R>0` be the spatial cell scale.

Assume throughout a time interval `I_R` that the enlarged moving ball

\[
B_{8R}(x_t)
\]

remains inside one regular exact CE-H region and that

\[
\boxed{
\Delta\Omega=\kappa\Omega
}
\]

there, with coefficient ceiling

\[
\boxed{
|\kappa(x,t)|\le C_\kappa R^{-2}
\qquad
\text{on }B_{8R}(x_t)\times I_R.
}
\]

This is stronger than a one-snapshot M17-382 cell: the cell and its enlarged elliptic neighborhood must persist through the whole own-scale time window.

Failure of this persistence is retained explicitly as

\[
G_{CEH/interface/domain/genealogy\ loss}.
\]

## 3. Local Caccioppoli and elliptic H2 control

At one fixed time, standard interior estimates for

\[
\Delta\Omega=\kappa\Omega
\]

with

\[
|\kappa|\lesssim R^{-2}
\]

give

\[
\boxed{
\|\nabla\Omega\|_{L^2(B_{7R})}
\lesssim
R^{-1}
\|\Omega\|_{L^2(B_{8R})}.
}
\]

The interior `H2` estimate gives

\[
\|D^2\Omega\|_{L^2(B_{6R})}
\lesssim
\|\Delta\Omega\|_{L^2(B_{7R})}
+R^{-2}\|\Omega\|_{L^2(B_{7R})}.
\]

Using exact CE-H,

\[
\|\Delta\Omega\|_{L^2(B_{7R})}
\le
C_\kappa R^{-2}
\|\Omega\|_{L^2(B_{7R})},
\]

hence

\[
\boxed{
\|D^2\Omega\|_{L^2(B_{6R})}
\lesssim
R^{-2}
\|\Omega\|_{L^2(B_{8R})}.
}
\]

Thus on a persistent own-scale CE-H cell, second spatial derivatives are already elliptically tied to the cell-scale enstrophy.

## 4. Near-field strain bound

Let `chi_R` be a smooth cutoff satisfying

\[
\chi_R=1
\quad\text{on }B_{5R}(x_t),
\]

\[
\operatorname{supp}\chi_R
\subset B_{6R}(x_t),
\]

and

\[
|D^j\chi_R|\lesssim R^{-j},
\qquad j=1,2.
\]

For divergence-free velocity, the strain is an order-zero singular integral of vorticity:

\[
\Sigma=\mathcal T\Omega.
\]

Define

\[
\Sigma_{near}
:=
\mathcal T(\chi_R\Omega).
\]

The `L2` boundedness of the Calderon--Zygmund operator gives

\[
\|\Sigma_{near}\|_2
\lesssim
\|\chi_R\Omega\|_2.
\]

Because derivatives commute with the Fourier multiplier,

\[
\|D^2\Sigma_{near}\|_2
\lesssim
\|D^2(\chi_R\Omega)\|_2.
\]

The cutoff derivative terms together with Section 3 imply

\[
\boxed{
\|D^2(\chi_R\Omega)\|_2
\lesssim
R^{-2}
\|\Omega\|_{L^2(B_{8R})}.
}
\]

Apply the three-dimensional Gagliardo--Nirenberg inequality

\[
\|f\|_\infty
\lesssim
\|f\|_2^{1/4}
\|D^2f\|_2^{3/4}.
\]

Then

\[
\boxed{
\|\Sigma_{near}\|_\infty
\lesssim
R^{-3/2}
\|\Omega\|_{L^2(B_{8R})}.
}
\]

Thus the near-field singular integral is controlled at the exact own-scale rate by cell enstrophy.

No separate raw-`H2` spacetime payer is needed for this estimate.

## 5. Far-field strain bound

Define

\[
\Sigma_{far}
:=
\mathcal T((1-\chi_R)\Omega).
\]

The strain-vorticity kernel satisfies

\[
|K(z)|\lesssim |z|^{-3}.
\]

For

\[
x\in B_R(x_t),
\]

the support of `(1-chi_R) Omega` lies a distance comparable to `R` away.

Therefore

\[
|\Sigma_{far}(x)|
\lesssim
\int_{|y-x_t|\gtrsim R}
\frac{|\Omega(y)|}{|x-y|^3}dy.
\]

By Cauchy--Schwarz,

\[
\begin{aligned}
|\Sigma_{far}(x)|
&\lesssim
\|\Omega\|_2
\left(
\int_{|z|\gtrsim R}|z|^{-6}dz
\right)^{1/2}\\
&\lesssim
R^{-3/2}\|\Omega\|_2.
\end{aligned}
\]

Hence

\[
\boxed{
\|\Sigma_{far}\|_{L^\infty(B_R(x_t))}
\lesssim
R^{-3/2}\|\Omega\|_2.
}
\]

This estimate treats coherent parent-scale strain as one global enstrophy-controlled field rather than charging it once per child cell.

## 6. Full own-scale strain bound

Combining Sections 4 and 5,

\[
\boxed{
\|\Sigma(t)\|_{L^\infty(B_R(x_t))}
\lesssim
R^{-3/2}
\|\Omega(t)\|_2.
}
\]

Define

\[
E(t):=\|\Omega(t)\|_2^2,
\qquad
E_*:=\sup_{t\in I_R}E(t).
\]

Then

\[
\boxed{
\|\Sigma(t)\|_{L^\infty(B_R(x_t))}
\lesssim
R^{-3/2}E_*^{1/2}.
}
\]

## 7. Own-scale material deformation is controlled by critical enstrophy

Let

\[
|I_R|\le c_t\frac{R^2}{\nu}.
\]

The M17-384 material deformation variable satisfies

\[
K_{I_R}
:=
\int_{I_R}
\|\Sigma(t)\|_{L^\infty(B_R(x_t))}dt.
\]

Section 6 yields

\[
K_{I_R}
\lesssim
R^{-3/2}|I_R|E_*^{1/2}.
\]

Therefore

\[
\boxed{
K_{I_R}
\lesssim
C(c_t,\nu)
(RE_*)^{1/2}.
}
\]

The quantity

\[
\boxed{RE_*}
\]

is the scale-critical enstrophy density associated with the own-scale window.

Thus on a persistent exact CE-H cell, unbounded own-scale deformation requires

\[
\boxed{RE_*\to\infty.}
\]

## 8. Insert into the M17-384 finite-scale doubling inequality

M17-384/M17-385 give

\[
\mathfrak D_\theta(t)
\le
\mathfrak D_{\theta e^{-2K_{I_R}}}(t_0)
+4K_{I_R}
+C(G_*,c_t),
\]

on the bounded scale-normalized coefficient-gradient branch.

Suppose

\[
RE_*\le M_E<\infty.
\]

Then Section 7 gives

\[
K_{I_R}\le C(M_E,c_t,\nu).
\]

Hence

\[
\theta e^{-2K_{I_R}}
\ge
\eta_*(\theta,M_E,c_t,\nu)>0.
\]

Therefore, if the ancestor has bounded local doubling uniformly for radius ratios in the fixed compact interval

\[
\eta\in[\eta_*,\theta],
\]

then the descendant doubling is uniformly bounded as well.

Consequently

\[
\boxed{
\begin{aligned}
G_{finite\text{-}scale\ doubling\ decompactification}
\Longrightarrow{}&
G_{inherited/ancestral\ high\ doubling}\\
&\lor G_{critical\ enstrophy\ density\ decompactification}\\
&\lor G_{coefficient\ gradient\ decompactification}\\
&\lor G_{CEH/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

## 9. Relation to M17-385

M17-385 is a correct general inequality:

\[
K_I
\lesssim
E_*^{1/8}|I|^{5/8}
\left(\int_IHdt\right)^{3/8}.
\]

The present result is stronger only on the additional branch where an enlarged own-scale CE-H cell persists through the whole interval.

There the elliptic equation itself supplies the local derivative control needed to estimate the near field, while the far field is bounded directly from global enstrophy.

Thus on the **persistent own-scale CE-H cell branch**, the M17-385 terminal alternative

\[
G_{raw\text{-}H2\ spacetime\ concentration}
\]

is not needed as an independent payer for finite-scale doubling decompactification.

If persistent CE-H cell geometry is unavailable, M17-385 remains the valid fallback.

## 10. Concurrent spatial multiplicity is no longer charged per child

Suppose one coherent far-field strain deforms many disjoint child cells at the same time.

Section 5 bounds that field once by

\[
R^{-3/2}\|\Omega\|_2.
\]

It is therefore represented as one parent/global critical-enstrophy payer, not as `N` independent child raw-`H2` payments.

For the near field, each persistent CE-H child already obeys the same scale-local elliptic estimate.

Thus the specific artificial multiplicity identified in M17-386 is removed at the level of the deformation **upper bound**.

What remains is not a raw-`H2` ownership problem but whether critical enstrophy density can decompactify along the required genealogy while respecting the certified Navier--Stokes energy-dissipation ledger.

## 11. New narrow frontier

Combining M17-381--387, the late exact CE-H localization/frequency branch is now

\[
\boxed{
\begin{aligned}
H_{late\ persistent\ CEH}
\Longrightarrow{}&
H_{bounded\ doubling\Rightarrow scale\text{-}comparable\ packet}\\
&\lor G_{inherited\ high\ frequency}\\
&\lor G_{RE\to\infty}\\
&\lor G_{r^3|\nabla\kappa|\to\infty}\\
&\lor G_{CEH/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

The raw-`H2` snapshot/spacetime ownership debt and the separate finite-scale strain-payer ambiguity are both removed on this persistent branch.

## 12. DSD audit role

The DSD role is a payer and scale audit:

- do not localize a nonlocal strain payer by declaration;
- split it into standard near/far singular-integral pieces;
- use the exact CE-H elliptic equation only where the persistent cell hypothesis justifies it;
- count coherent far-field deformation once;
- retain cell-persistence failure explicitly rather than hiding it inside a norm estimate.

All canonical estimates are standard interior elliptic regularity, Calderon--Zygmund `L2` boundedness, Gagliardo--Nirenberg, Biot--Savart kernel decay, and Cauchy--Schwarz.

## 13. Audit verdict

**PASS — major strengthening on the persistent own-scale CE-H branch.**

The central estimate is

\[
\boxed{
K_{I_R}
\lesssim
C(c_t,\nu)(RE_*)^{1/2}.
}
\]

Therefore finite-scale doubling decompactification cannot be generated freely inside a scale-critical enstrophy-compact persistent CE-H cell.

The next highest-value task is to audit the remaining branch

\[
\boxed{RE_*\to\infty}
\]

against the standard energy-dissipation ledger and determine exactly what duration or multiplicity is required before critical enstrophy decompactification becomes globally non-summable.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
