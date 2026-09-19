# M20-009 — The terminal reweighting speed has an exact vorticity-magnitude PDE decomposition into transport, axial stretching, scalar diffusion, and direction-gradient damping

Date: 2026-09-20  
Canonical ID: **M20-009**  
Status: **REWEIGHTING-TO-PDE BRIDGE / THE RELATIVE AMPLITUDE SPEED lambda=partial_z log|G||_0 IS DETERMINED EXACTLY BY THE TERMINAL VORTICITY-MAGNITUDE EQUATION / ITS CENTERED REWEIGHTING CURRENT SPLITS INTO EULERIAN TRANSPORT-HOMOGENEITY, AXIAL STRETCHING, SCALAR VORTICITY DIFFUSION, AND DIRECTION-GRADIENT DAMPING / THE ALL-PROJECTIVE-MOMENT-BLIND FIBER BRANCH THEREFORE REQUIRES A CONDITIONAL COMPENSATION AMONG THESE PDE CHANNELS / NO ONE CHANNEL IS FORCED WITHOUT FURTHER COVARIANCE INFORMATION / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Wedge vorticity magnitude

Write the exact wedge vorticity as

\[
\omega(x,s)
=
r^{-2}G(z,q,\omega),
\]

with

\[
z=\frac{-s}{r^2},
\qquad
q=\log r.
\]

Define

\[
\varrho(z,q,\omega):=|G(z,q,\omega)|,
\]

and on the nonzero set

\[
\xi(z,q,\omega):=\frac{G}{|G|}.
\]

At the terminal boundary,

\[
\boxed{
\beta:=\varrho(0)=|B|,
}
\]

and

\[
\boxed{
\lambda
:=
\partial_z\log\varrho\big|_{z=0}
=
\frac{B\cdot D_\omega}{|B|^2}.
}
\]

## 2. Physical vorticity-magnitude equation

For viscosity normalized to one in the canonical wedge equations,

\[
\boxed{
(\partial_s+u\cdot\nabla)\rho
=
\gamma_{\rm phys}\rho
+
\Delta\rho
-
\rho|\nabla\xi|^2,
}
\]

where

\[
\rho=|\omega|,
\]

and

\[
\gamma_{\rm phys}
=
\xi^T\Sigma_u\xi.
\]

The last term is the standard direction-gradient diffusion penalty.

## 3. Exact wedge conversion

Because

\[
\rho=r^{-2}\varrho,
\]

we have

\[
\partial_s\rho
=
-r^{-4}\partial_z\varrho.
\]

For a scalar coefficient of homogeneity two,

\[
\nabla(r^{-2}\varrho)
=
r^{-3}
\left[
e_r(\mathfrak D-2)\varrho
+
\nabla_{S^2}\varrho
\right],
\]

where

\[
\mathfrak D
=
\partial_q-2z\partial_z.
\]

Since

\[
u=r^{-1}F,
\]

the advection term is

\[
u\cdot\nabla\rho
=
r^{-4}
\left[
F_r(\mathfrak D-2)\varrho
+
F_T\cdot\nabla_S\varrho
\right].
\]

Also,

\[
\Delta\rho
=
r^{-4}\mathfrak L_2\varrho,
\]

with

\[
\boxed{
\mathfrak L_2
=
(\mathfrak D-2)(\mathfrak D-1)
+
\Delta_{S^2}.
}
\]

Finally,

\[
|\nabla\xi|^2
=
r^{-2}
\left(
|\mathfrak D\xi|^2
+
|\nabla_S\xi|^2
\right).
\]

Let

\[
\Gamma_F:=\xi^T\Sigma_F\xi,
\]

so that

\[
\gamma_{\rm phys}=r^{-2}\Gamma_F.
\]

## 4. Exact wedge magnitude equation

Substitution gives

\[
\boxed{
\begin{aligned}
-\partial_z\varrho
&+
F_r(\mathfrak D-2)\varrho
+
F_T\cdot\nabla_S\varrho
\\
&=
\Gamma_F\varrho
+
\mathfrak L_2\varrho
-
\varrho
\left(
|\mathfrak D\xi|^2
+
|\nabla_S\xi|^2
\right).
\end{aligned}
}
\]

This is the scalar magnitude counterpart of the wedge vorticity equation from M5-585.

## 5. Terminal formula for lambda

At z=0,

\[
F=A,
\qquad
\varrho=\beta,
\qquad
\mathfrak D=\partial_q.
\]

Define

\[
\gamma
:=
\xi_B^T\Sigma_A\xi_B,
\]

and

\[
\boxed{
\mathcal D_\xi
:=
|\partial_q\xi_B|^2
+
|\nabla_S\xi_B|^2.
}
\]

Then

\[
-\lambda\beta
+
A_r(\partial_q-2)\beta
+
A_T\cdot\nabla_S\beta
=
\gamma\beta
+
\mathcal L_2\beta
-
\beta\mathcal D_\xi.
\]

Therefore, on \(\{\beta>0\}\),

\[
\boxed{
\lambda
=
A_r
\left(
\partial_q\log\beta-2
\right)
+
A_T\cdot\nabla_S\log\beta
-
\gamma
-
\frac{\mathcal L_2\beta}{\beta}
+
\mathcal D_\xi.
}
\]

This is the main M20-009 identity.

## 6. Four typed amplitude-growth channels

Define

\[
\boxed{
X_T
:=
A_r
\left(
\partial_q\log\beta-2
\right)
+
A_T\cdot\nabla_S\log\beta,
}
\]

\[
\boxed{
X_S:=-\gamma,
}
\]

\[
\boxed{
X_D
:=
-\frac{\mathcal L_2\beta}{\beta},
}
\]

and

\[
\boxed{
X_\xi:=\mathcal D_\xi.
}
\]

Then

\[
\boxed{
\lambda
=
X_T+X_S+X_D+X_\xi.
}
\]

Interpretation:

- \(X_T\): Eulerian transport plus radial homogeneity;
- \(X_S\): backward-wedge contribution of axial stretching;
- \(X_D\): scalar vorticity-magnitude diffusion;
- \(X_\xi\): direction-gradient damping in physical forward time, appearing positively in backward wedge depth.

## 7. Sign interpretation and wedge orientation

Increasing z moves backward in physical time at fixed x because

\[
s=-zr^2.
\]

Therefore forward physical stretching

\[
\gamma>0
\]

increases vorticity toward the terminal time but contributes

\[
-\gamma
\]

to the backward-depth growth speed \(\lambda\).

Likewise physical direction-gradient diffusion damps vorticity forward in time and therefore contributes

\[
+\mathcal D_\xi
\]

to backward-depth growth.

The signs in Section 5 are therefore consistent with the time orientation.

## 8. Log-amplitude expansion

Let

\[
h:=\log\beta.
\]

At z=0,

\[
\mathcal L_2
=
\partial_q^2
-
3\partial_q
+
2
+
\Delta_S.
\]

Hence

\[
\frac{\mathcal L_2\beta}{\beta}
=
h_{qq}
+
\Delta_Sh
+
|h_q|^2
+
|\nabla_Sh|^2
-
3h_q
+
2.
\]

Thus

\[
\boxed{
\begin{aligned}
\lambda
={}&
A_r(h_q-2)
+
A_T\cdot\nabla_Sh
-
\gamma
+
\mathcal D_\xi
\\
&-
h_{qq}
-
\Delta_Sh
-
|h_q|^2
-
|\nabla_Sh|^2
+
3h_q
-
2.
\end{aligned}
}
\]

This makes the scalar diffusion and amplitude-gradient penalties explicit.

## 9. Centered reweighting current

M20-003 defines

\[
\alpha
=
\mathbb E_{\pi_B}\lambda,
\]

and

\[
\phi
=
\lambda-\alpha.
\]

If the four channels are square-integrable under \(\pi_B\), define their centered versions

\[
\widetilde X_j
:=
X_j-\mathbb E_{\pi_B}X_j.
\]

Then

\[
\boxed{
\phi
=
\widetilde X_T
+
\widetilde X_S
+
\widetilde X_D
+
\widetilde X_\xi.
}
\]

Thus relative amplitude reweighting is not a fifth independent dynamics.

It is the centered sum of four standard vorticity-magnitude mechanisms.

## 10. Quantitative variance fork

Using

\[
|x_1+x_2+x_3+x_4|^2
\le
4\sum_{j=1}^4|x_j|^2,
\]

we obtain

\[
\boxed{
\operatorname{Var}_{\pi_B}(\lambda)
\le
4
\left[
\operatorname{Var}(X_T)
+
\operatorname{Var}(X_S)
+
\operatorname{Var}(X_D)
+
\operatorname{Var}(X_\xi)
\right].
}
\]

Therefore if

\[
\operatorname{Var}_{\pi_B}(\lambda)
\ge v_*>0,
\]

then at least one channel has

\[
\boxed{
\operatorname{Var}_{\pi_B}(X_j)
\ge
\frac{v_*}{16}.
}
\]

Hence

\[
\boxed{
V_{\rm reweight}
\Longrightarrow
R_T
\lor
R_S
\lor
R_D
\lor
R_\xi.
}
\]

This is the PDE-resolved reweighting fork.

## 11. Near-zero audit and robust amplitude localization

The ratio

\[
\frac{\mathcal L_2\beta}{\beta}
\]

and log derivatives are only typed on \(\{\beta>0\}\).

However M20-004 proves

\[
D_\omega=0
\quad\text{a.e. on }\{B=0\}.
\]

The reweighting L2 density is

\[
(\lambda-\alpha)^2|B|^2.
\]

If the reweighting branch has positive invariant mass, monotone convergence gives a fixed

\[
\boxed{
\beta_*>0
}
\]

such that a positive fraction of that mass lies on

\[
\{|B|\ge\beta_*\}.
\]

On this robust set all ratios in Section 5 are smooth and uniformly typed by compactness.

Thus the PDE split can be localized away from nodal singularities.

Any failure to globalize the individual \(X_j\) moments because of near-zero blow-up must be recorded as a nodal/interface localization issue, not silently absorbed.

## 12. Conditional fiber balance

M20-008 identifies the all-direction-observable blind kernel as

\[
\mathbb E[\phi\mid Q]=0.
\]

Using the PDE decomposition,

\[
\boxed{
\mathbb E[
\widetilde X_T
+
\widetilde X_S
+
\widetilde X_D
+
\widetilde X_\xi
\mid Q
]
=
0
}
\]

on the fiber-silent branch.

Thus a direction-fiber-hidden reweighting current is not arbitrary.

It requires a conditional compensation among:

- transport/homogeneity;
- axial stretching;
- scalar diffusion;
- direction-gradient damping.

## 13. Why Q alone cannot resolve the compensation

Each of the four channels depends on information not determined by projective direction Q alone.

For example:

- \(\gamma\) depends on strain eigenvalues and loading;
- \(X_D\) depends on magnitude curvature;
- \(X_T\) depends on velocity and amplitude gradients;
- \(X_\xi\) depends on spatial/log-radial direction derivatives.

Therefore the conditional cancellation in Section 12 can occur inside one fixed direction fiber.

This explains structurally why the pure projective hierarchy in M20-008 is incomplete.

## 14. Natural joint labels

The most promising enlargements of the projective state are:

\[
(Q,\gamma),
\]

\[
(Q,\mathcal D_\xi),
\]

\[
(Q,X_D),
\]

or the full typed block

\[
\boxed{
\mathcal Z_{\rm rw}
=
(Q,X_T,\gamma,X_D,\mathcal D_\xi).
}
\]

A useful next theorem would show that on the hard compact hull, one of these joint labels must carry a nonzero conditional selection current that maps to an already finite/nonrecyclable resource.

No such theorem is yet established.

## 15. Relation to existing direction-diffusion audits

Earlier vorticity-direction analyses show that large spatial direction gradients incur viscous magnitude damping and can be scale critical.

M20-009 places that same mechanism directly inside the terminal reweighting speed through

\[
+\mathcal D_\xi
\]

in backward wedge depth.

Thus the direction branch and the reweighting branch are not independent at the PDE level.

Spatial direction texture can drive both:

- local projective motion through M20-002;
- relative amplitude selection through M20-009.

This coupling should be retained rather than double counted.

## 16. Updated M20 reweighting frontier

The reweighting branch now has two complementary descriptions:

### observability split

\[
V_{\rm reweight}
\Longrightarrow
R_{\rm high}
\lor
R_{\rm fiber},
\]

### PDE mechanism split

\[
V_{\rm reweight}
\Longrightarrow
R_T
\lor
R_S
\lor
R_D
\lor
R_\xi.
\]

These are not eight independent roots.

They are two coordinate systems on the same reweighting dynamics:

- what the direction marginal can observe;
- what the vorticity-magnitude PDE generates.

## 17. Next target

The strongest overlap is the stretching label

\[
\gamma.
\]

It appears in both:

- M20-006 projective-strain compensation;
- M20-009 amplitude reweighting.

M20-010 should therefore form a **joint \((Q,\gamma)\) state** and test whether the same axial stretching field can simultaneously hide the reweighting current inside direction fibers and support recurrent projective strain noncommutation without producing a detectable signed covariance.

That is a more constrained target than treating the two branches separately.

\[
\boxed{\text{M20-009 COMPLETE; THE TERMINAL REWEIGHTING SPEED IS EXACTLY RESOLVED INTO TRANSPORT, STRETCHING, SCALAR DIFFUSION, AND DIRECTION-GRADIENT DAMPING.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
