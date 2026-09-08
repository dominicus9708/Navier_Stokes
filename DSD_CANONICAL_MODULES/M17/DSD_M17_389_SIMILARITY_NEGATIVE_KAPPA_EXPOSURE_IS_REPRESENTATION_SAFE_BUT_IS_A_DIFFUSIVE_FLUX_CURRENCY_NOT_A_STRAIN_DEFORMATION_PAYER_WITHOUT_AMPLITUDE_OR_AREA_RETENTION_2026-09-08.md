# DSD M17-389 — Similarity negative-`kappa` exposure is representation safe but is a diffusive flux currency, not a strain-deformation payer without amplitude or area retention

Date: 2026-09-08  
Canonical ID: **M17-389**

Status: **ACTIVE REPRESENTATION BRIDGE / FLUX-TO-DEFORMATION NO-GO / CONDITIONAL AMPLITUDE-RETENTION BRIDGE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-372

M17-372 works inside one fixed similarity representation and one retained material flux-family genealogy.

Its basic family law is

\[
\boxed{
\frac d{d\theta}\log\Phi_F
=
\bar\kappa_{\Phi,F}^{sim}.
}
\]

If the family evacuates from fixed positive flux to

\[
\Phi_F(\theta_r)\lesssim r^{5/2},
\]

then

\[
\boxed{
\int
\overline{(\kappa^{sim})_-}_{\Phi,F}
\,d\theta
\gtrsim
\frac52\log\frac1r-O(1).
}
\]

M17-372 explicitly forbids direct cross-generation use without the M17-338 physical/similarity dictionary.

## 2. Exact M17-338 dictionary

Write

\[
s:=-t>0,
\qquad
\theta=-\log s.
\]

M17-338 gives

\[
\boxed{
\kappa^{sim}=s\kappa^{ph},
}
\]

and

\[
\boxed{
d\theta=\frac{dt}{s}.
}
\]

The corresponding material vorticity flux is representation invariant: similarity vorticity contributes a factor `s`, while similarity cross-sectional area contributes `s^{-1}`.

Therefore

\[
d\Phi^{sim}=d\Phi^{ph}
\]

for corresponding material surface labels.

Since `s>0`,

\[
(\kappa^{sim})_-
=s(\kappa^{ph})_-.
\]

Hence

\[
\boxed{
(\kappa^{sim})_-d\theta
=
(\kappa^{ph})_-dt.
}
\]

After flux averaging over the same material family,

\[
\boxed{
\int
\overline{(\kappa^{sim})_-}_{\Phi,F}d\theta
=
\int
\overline{(\kappa^{ph})_-}_{\Phi,F}dt.
}
\]

Thus the signed exposure integral itself is representation safe.

The scale label attached to a similarity event still requires the parent-to-M17 scale-map dictionary before being identified with a physical own-scale radius.

## 3. Physical material-flux law

In the repository normalization `nu=1`, the similarity family law therefore becomes

\[
\boxed{
\frac d{dt}\log\Phi_F
=
\bar\kappa_{\Phi,F}^{ph}.
}
\]

If physical viscosity is restored explicitly, the law is

\[
\boxed{
\frac d{dt}\log\Phi_F
=
\nu\bar\kappa_{\Phi,F}^{ph}.
}
\]

This may also be obtained directly from the vorticity equation and the evolution of a material surface element.

## 4. Why strain cancels from material flux

On exact physical CE-H,

\[
D_t\Omega
=
\Sigma\Omega+
u\Delta\Omega
=
(\sigma+\nu\kappa)\Omega.
\]

Writing

\[
\rho=|\Omega|,
\]

we get

\[
\boxed{
D_t\log\rho
=
\sigma+\nu\kappa.
}
\]

Let `dA` be a material area element normal to the vorticity eigen-direction `xi`.

For incompressible flow, the material area vector obeys

\[
D_t(dS)
=-(\nabla u)^T dS.
\]

Since

\[
\Sigma\xi=\sigma\xi,
\]

the magnitude of the transverse area satisfies

\[
\boxed{
D_t\log dA
=-\sigma.
}
\]

The infinitesimal vorticity flux is

\[
d\Phi=\rho\,dA.
\]

Therefore

\[
\begin{aligned}
D_t\log d\Phi
&=D_t\log\rho+D_t\log dA\\
&=(\sigma+\nu\kappa)-\sigma.
\end{aligned}
\]

Hence

\[
\boxed{
D_t\log d\Phi
=
\nu\kappa.
}
\]

The strain contribution cancels exactly.

## 5. Main no-go: flux evacuation alone does not force M17-388 deformation

M17-388's standard-energy payer is built from

\[
K_I
=
\int_I\|\Sigma\|_\infty dt.
\]

But Section 4 shows that material flux decay is controlled by

\[
\nu\int\kappa\,dt
\]

after the strain cancellation.

Therefore no implication of the form

\[
\boxed{
\int\kappa_-dt\gg1
\Longrightarrow
K_I\gg1
}
\]

follows from the material-flux law alone.

Thus M17-372/379 cannot be inserted directly into the M17-388 weighted energy ledger merely because both concern a long same-family history.

An additional amplitude, area, shape, or strain-coupling datum is required.

## 6. Conditional bridge under amplitude retention

Suppose, in addition to the negative coefficient exposure, the same retained material label/family has pointwise or uniformly representative amplitude retention

\[
0<c_\rho
\le
\frac{\rho(t_1)}{\rho(t_0)}
\le C_\rho<\infty.
\]

Integrating

\[
D_t\log\rho
=
\sigma+\nu\kappa
\]

gives

\[
\int_{t_0}^{t_1}\sigma dt
=
\log\frac{\rho(t_1)}{\rho(t_0)}
-
\nu\int_{t_0}^{t_1}\kappa dt.
\]

If

\[
\int\kappa dt
\le
-c_\kappa\log\frac1r+C,
\]

then amplitude retention implies

\[
\boxed{
\int_{t_0}^{t_1}\sigma dt
\ge
\nu c_\kappa\log\frac1r-O(1).
}
\]

Since

\[
|\sigma|\le\|\Sigma\|,
\]

we obtain

\[
\boxed{
K_I
\ge
\left|\int_I\sigma dt\right|
\gtrsim
\nu c_\kappa\log\frac1r-O(1).
}
\]

Thus a logarithmic deformation lower bound becomes available **only after amplitude retention is added**.

## 7. Equivalent area-retention/thinning interpretation

Because

\[
\Phi=\rho A,
\]

flux evacuation together with retained amplitude forces material cross-sectional area to shrink.

The exact area law

\[
D_t\log A=-\sigma
\]

then gives the same logarithmic strain integral.

Hence the extra datum may be stated either as amplitude retention or as a quantitative flux-to-area conversion on the same material tube.

## 8. The logarithmic bridge still does not beat the M17-388 energy firewall

Suppose the parent-to-M17 scale dictionary identifies a physical own-scale radius `R_j` for each retained event, and the conditional bridge yields

\[
K_j
\gtrsim
c\log\frac1{R_j}
\]

up to fixed representation constants.

M17-388 charges deformation by

\[
R_jK_j^2.
\]

Therefore the conditional logarithmic lower bound gives only

\[
\boxed{
R_jK_j^2
\gtrsim
R_j\log^2\frac1{R_j}.
}
\]

For geometric scales

\[
R_j=2^{-j}R_0,
\]

\[
\boxed{
\sum_j
R_j\log^2\frac1{R_j}
<\infty.
}
\]

Thus even the amplitude-retained logarithmic flux-exposure bridge remains compatible with the standard finite-energy budget.

It does not by itself close the proof.

## 9. Consequence for the current search

The M17-388 firewall requires a deformation growth/duration/multiplicity law strong enough that

\[
\sum_jR_jK_j^2
=\infty.
\]

M17-372 supplies only logarithmic coefficient exposure.

After the strongest direct amplitude-retention conversion available from Section 6, that yields logarithmic `K`, still geometrically summable.

Therefore the strict-subscale flux-exposure route needs an additional enhancement, such as:

1. super-logarithmic deformation growth;
2. sufficiently many independent same-scale episodes;
3. a long enough physical residence factor;
4. a non-geometric scale genealogy;
5. another certified payer not carrying the `R` geometric discount.

## 10. Representation audit

The exact safe chain is

\[
\boxed{
\begin{aligned}
&\text{M17-372 fixed-similarity negative exposure}\\
&\xrightarrow{\text{M17-338 dictionary}}
\text{physical negative-`kappa` exposure}\\
&\xrightarrow{\text{amplitude/area retention only}}
\text{logarithmic strain deformation}\\
&\xrightarrow{\text{M17-388}}
R\log^2(1/R)\text{ energy cost}.
\end{aligned}
}
\]

The first arrow is exact.

The second arrow is conditional.

The final cost is summable on geometric scales.

No stronger conclusion is certified.

## 11. DSD audit role

The DSD role is to prevent a channel substitution:

- coefficient exposure is a diffusion/flux channel;
- strain deformation is a geometric/material-flow channel;
- the two interact in the amplitude equation but cancel in the flux equation;
- therefore one cannot replace one by the other without an explicit amplitude/area condition.

All canonical identities are standard similarity/physical change of variables, material area evolution, and the exact CE-H vorticity equation.

## 12. Audit verdict

**PASS — representation bridge completed, false direct flux-to-deformation bridge rejected, and the strongest elementary conditional bridge quantified.**

The decisive no-go is

\[
\boxed{
\text{logarithmic `kappa` exposure alone}
\not\Rightarrow
\text{large strain deformation}.
}
\]

With amplitude retention one gets at most the direct logarithmic bridge

\[
\boxed{
K\gtrsim\log(1/r),
}
\]

whose M17-388 energy cost remains geometrically summable.

The next highest-value task is therefore to test the **recurrence/closed-loop and strict-subscale multiplicity** branches for a stronger-than-logarithmic or same-scale multiplicity enhancement, rather than reusing M17-372 exposure alone.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
