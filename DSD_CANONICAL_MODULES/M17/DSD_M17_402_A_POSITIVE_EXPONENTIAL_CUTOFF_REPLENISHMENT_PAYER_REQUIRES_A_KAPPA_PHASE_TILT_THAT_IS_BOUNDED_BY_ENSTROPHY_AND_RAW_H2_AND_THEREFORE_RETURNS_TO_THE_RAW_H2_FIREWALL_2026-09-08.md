# DSD M17-402 — A positive exponential cutoff-replenishment payer requires a `kappa`-phase tilt that is bounded by enstrophy and raw-`H2`, and therefore returns to the raw-`H2` firewall

Date: 2026-09-08  
Canonical ID: **M17-402**

Status: **ACTIVE CUTOFF-PAYER PHYSICALIZATION / THRESHOLD-PHASE REDUCTION / RAW-H2 RETURN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-191/192

The M5-688 cutoff source is

\[
C_\chi(k,\theta)
:=
\int
\delta(k-\kappa)
\chi'(\rho)\rho^3
(\sigma+\kappa-1)dy.
\]

Write the recurrent mean density as

\[
C(k):=\overline{C_\chi(k)}.
\]

M17-191 proves that its unweighted total is strictly nonpositive and, on a nontrivial transition layer,

\[
\boxed{
\mathcal C_0
:=
\int C(k)dk
=-A_0<0.
}
\]

The M5-688 exponentially tilted cutoff payer is

\[
\boxed{
\mathcal C_2
:=
\int e^{2k}C(k)dk.
}
\]

M17-192 shows that `C_2>=0` requires a fixed positive upward/replenishing threshold-turnover population biased toward larger `kappa`.

The present module identifies the PDE resource required by that bias.

## 2. Exact cutoff phase-tilt decomposition

Write

\[
e^{2k}=1+(e^{2k}-1).
\]

Then

\[
\boxed{
\mathcal C_2
=
\mathcal C_0
+
\mathcal P_{cut}^{tilt},
}
\]

where

\[
\boxed{
\mathcal P_{cut}^{tilt}
:=
\int(e^{2k}-1)C(k)dk.
}
\]

In spatial form,

\[
\boxed{
\mathcal P_{cut}^{tilt}
=
\left\langle
\int
\chi'(\rho)\rho^3
(e^{2\kappa}-1)
(\sigma+\kappa-1)dy
\right\rangle.
}
\]

Since

\[
\mathcal C_0=-A_0,
\]

any nonnegative cutoff contribution to the M5-688 payer ledger satisfies

\[
\boxed{
\mathcal C_2\ge0
\Longrightarrow
\mathcal P_{cut}^{tilt}\ge A_0>0.
}
\]

More generally, `C_2>=c_*>0` gives `P_cut^tilt>=A_0+c_*`.

Thus the positive cutoff payer is entirely a coefficient-phase tilt of amplitude-threshold turnover.

## 3. Linearize the coefficient tilt on the compact hull

On the compact recurrent CE-H hull,

\[
|\kappa|\le K_*.
\]

Therefore

\[
|e^{2\kappa}-1|
\le
C_{K_*}|\kappa|.
\]

Hence

\[
|\mathcal P_{cut}^{tilt}|
\le
C_{K_*}
\left\langle
\int
\chi'\rho^3
|\kappa|
|\sigma+\kappa-1|dy
\right\rangle.
\]

## 4. Cauchy--Schwarz factorization

For one time slice, define

\[
H_{thr}
:=
\int
\chi'(\rho)\rho^3\kappa^2dy,
\]

and

\[
T_{thr}
:=
\int
\chi'(\rho)\rho^3
(\sigma+\kappa-1)^2dy.
\]

Then

\[
\boxed{
|P_{cut}^{tilt}(\theta)|
\le
C_{K_*}
H_{thr}(\theta)^{1/2}
T_{thr}(\theta)^{1/2}.
}
\]

The cutoff transition collar satisfies

\[
a_-\le\rho\le a_+,
\]

so all powers of `rho` in these expressions are harmless fixed weights.

## 5. `H_thr` is controlled by raw-H2

On exact CE-H,

\[
|\Delta W|^2
=\kappa^2\rho^2.
\]

Since on the collar `rho<=a_+` and `chi'` is fixed and bounded,

\[
\chi'\rho^3\kappa^2
\le
C\kappa^2\rho^2.
\]

Therefore

\[
\boxed{
H_{thr}
\le
C H_{raw},
\qquad
H_{raw}:=\|\Delta W\|_2^2.
}
\]

## 6. Threshold-turnover speed is controlled by enstrophy plus raw-H2

Expand

\[
(\sigma+\kappa-1)^2
\le
3\sigma^2+3\kappa^2+3.
\]

On the fixed amplitude collar,

\[
\chi'\rho^3\le C.
\]

For the strain term,

\[
\int_{collar}\sigma^2dy
\le
\int|\Sigma|^2dy
=
\frac12\|W\|_2^2.
\]

For the coefficient term, Section 5 gives a raw-`H2` bound.

For the constant term, the positive amplitude floor gives

\[
|\{\chi'\ne0\}|
\le
 a_-^{-2}\int_{collar}\rho^2dy
\le
 a_-^{-2}E,
\]

where

\[
E:=\|W\|_2^2.
\]

Thus

\[
\boxed{
T_{thr}
\le
C(E+H_{raw}).
}
\]

## 7. Positive cutoff payer forces raw-H2 occupancy under bounded enstrophy

Combine Sections 4--6:

\[
\boxed{
|P_{cut}^{tilt}(\theta)|
\le
C
H_{raw}(\theta)^{1/2}
\left(E(\theta)+H_{raw}(\theta)\right)^{1/2}.
}
\]

After recurrent averaging and Cauchy--Schwarz/Hölder, the compact hull bound

\[
E\le E_*<\infty
\]

gives a schematic but quantitative estimate

\[
\boxed{
|\mathcal P_{cut}^{tilt}|
\le
C
\left\langle H_{raw}\right\rangle^{1/2}
\left(E_*+\left\langle H_{raw}\right\rangle\right)^{1/2}.
}
\]

Therefore

\[
\mathcal P_{cut}^{tilt}\ge A_0>0
\]

forces

\[
\boxed{
\left\langle H_{raw}\right\rangle
\ge
h_*(A_0,E_*,C)>0.
}
\]

One explicit choice is the positive root of

\[
C^2H(E_*+H)=A_0^2.
\]

Thus a positive exponential cutoff payer requires a fixed positive normalized raw-`H2` occupancy.

## 8. Consequence for M17-192 threshold replenishment

M17-192 interprets the positive cutoff payer as quantitative high-`kappa` upward amplitude-threshold turnover.

M17-402 now adds

\[
\boxed{
\text{positive high-`kappa` threshold replenishment}
\Longrightarrow
\text{positive normalized raw-`H2` occupancy}.
}
\]

Therefore threshold replenishment is not an independent energy source.

It requires the same higher-derivative raw-`H2` resource already present in M17-381/385/400.

## 9. Exact scale ownership is already available

M17-381 and M17-386 give exact coefficient-scale ownership for raw-`H2` snapshot and spacetime measures.

Hence the raw derivative charge forced by Section 7 is not subject to an unresolved scale double-counting ambiguity.

It is assigned to intrinsic coefficient scales by `|kappa|` itself.

The remaining problem is again budget, not ownership.

## 10. The raw-H2 budget firewall survives

No finite first-generation global spacetime budget is certified for

\[
\int H_{raw}(t)dt.
\]

Therefore

\[
\boxed{
\text{positive cutoff replenishment}
\to
\text{raw-`H2` occupancy}
\not\to
\text{global contradiction}.
}
\]

This is the same terminal resource firewall reached by M17-400 from the phase-tilted strain-residence branch.

## 11. Completed M5-688 payer classification at resource level

After M17-398--402, the non-topological M5-688 payer channels have the following resource classification:

\[
\boxed{
\begin{aligned}
D_\sigma,P_W,B_\rho,B_\sigma
&\to \text{palinstrophy firewall},\\
\mathcal P_{\kappa\sigma}^{tilt}
&\to \text{raw-`H2` firewall},\\
B_\kappa^{away}
&\to \text{log-`kappa` diffusion critical firewall},\\
B_\kappa^{near}
&\to \text{zero-corridor architecture},\\
\mathcal C_2^{positive}
&\to \text{raw-`H2` firewall}.
\end{aligned}
}
\]

Thus no broad analytic source term in M5-688 remains untyped.

The only residual categories are explicit zero-level, interface/rank/domain/genealogy losses and the lack of cross-generation finite budgets for the already identified critical/higher-derivative resources.

## 12. DSD audit role

The DSD role is a source-versus-resource audit.

A positive threshold turnover looks kinematically different from raw derivative energy, but the coefficient phase tilt required to reverse the recurrent cutoff sign cannot be large without raw-`H2` occupancy.

The canonical proof uses amplitude support, Cauchy--Schwarz, exact CE-H, and standard strain/vorticity `L2` identities.

## 13. Audit verdict

**PASS — positive cutoff/threshold replenishment is returned to the existing raw-`H2` firewall.**

At the resource-classification level, the M5-688 payer tree is now complete on the compact analytic CE-H branch.

The next proof problem is no longer local payer identification.

It is a cross-generation theorem that either supplies a finite ancestral budget/rigidity for the identified critical charges or forces escape through the explicit zero/interface/genealogy branches.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
