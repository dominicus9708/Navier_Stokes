# DSD M5-205 — Degree-(-2) Vorticity Cylinder Operator and Matrix-Diffusion Identity

Date: 2026-08-29

Parent: `DSD_M5_204_FULL_GRADIENT_MATRIX_SYMMETRIZER_SCOPE_CORRECTION_AUDIT_2026-08-29.md`

Status: **EXACT OPERATOR DERIVATION / A DEGREE-`-2` CRITICAL VORTICITY PROFILE HAS ADDITIONAL HOMOGENEITY TERMS THAT ARE ABSENT FROM THE ABSTRACT FIRST-ORDER SYMMETRIZER MODEL / AFTER FACTORING `omega=r^-2 W`, THE LAPLACIAN BECOMES `W_yy+3W_y+2W+Delta_S W` AND THE ADVECTIVE TERM ACQUIRES `-2 Phi_r W` / EVEN IF A MATRIX METRIC EXACTLY SKEW-SYMMETRIZES THE FULL CRITICAL ADVECTIVE/STRETCHING PROFILE OPERATOR, THE WEIGHTED VISCOUS BALANCE CONTAINS AN INDEFINITE `Delta_cyl H` COMMUTATOR AND THE DEGREE-`-2` HOMOGENEITY POTENTIAL / THERE IS NO PURE POSITIVE-DIFFUSION CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Critical velocity and vorticity profiles

Let

\[
B_T(x)
=
\frac1r\Phi(y,\theta),
\qquad
r=|x|,
\qquad
y=-\log r,
\qquad
\theta=x/r.
\]

A critical vorticity profile has degree `-2`:

\[
\boxed{
\omega_T(x)
=
r^{-2}W(y,\theta).
}
\]

Let

\[
\mathcal G
:=r^2\nabla B_T
\]

be the full scaled velocity gradient.

Then

\[
(\omega_T\cdot\nabla)B_T
=
r^{-4}\mathcal GW.
\]

---

## 2. Exact degree-`-2` Laplacian

For a Cartesian component of

\[
f=r^\alpha\psi(\rho,\theta),
\qquad
\rho=\log r,
\]

the standard identity is

\[
\Delta f
=
r^{\alpha-2}
\left[
\partial_\rho^2
+(2\alpha+1)\partial_\rho
+\alpha(\alpha+1)
+\Delta_{S^2}
\right]\psi.
\]

For

\[
\alpha=-2,
\]

and

\[
\partial_\rho=-\partial_y,
\]

we obtain

\[
\boxed{
\Delta(r^{-2}W)
=
r^{-4}
\left[
W_{yy}
+3W_y
+2W
+\Delta_{S^2}W
\right].
}
\]

Define the flat product-cylinder Laplacian

\[
\boxed{
\Delta_c
:=
\partial_{yy}+\Delta_{S^2}.
}
\]

Then

\[
\boxed{
r^4\Delta\omega_T
=
\Delta_cW+3W_y+2W.}
\]

---

## 3. Exact critical advection on a degree-`-2` field

Write

\[
\Phi=\Phi_re_r+\Phi_\tau.
\]

Since

\[
\partial_r(r^{-2}W)
=
r^{-3}(-2W-W_y),
\]

and the angular derivative contributes `r^-3 grad_S W`,

\[
(B_T\cdot\nabla)\omega_T
=
r^{-4}
\left[
-\Phi_rW_y
+
\Phi_\tau\cdot\nabla_SW
-2\Phi_rW
\right].
\]

Using

\[
T_\Phi
=-\Phi_r\partial_y
+
\Phi_\tau\cdot\nabla_S,
\]

we get

\[
\boxed{
(B_T\cdot\nabla)\omega_T
=
r^{-4}
\left[T_\Phi W-2\Phi_rW\right].
}
\]

The term

\[
\boxed{-2\Phi_rW}
\]

is a pure homogeneity contribution and must not be omitted from the exact profile equation.

---

## 4. Exact stationary critical vorticity cylinder equation

For a stationary incompressible Navier--Stokes field,

\[
-\nu\Delta\omega
+(u\cdot\nabla)\omega
-(\omega\cdot\nabla)u
=0.
\]

Substituting the critical profiles and multiplying by `r^4` gives

\[
\boxed{
-\nu
(\Delta_cW+3W_y+2W)
+
T_\Phi W
-2\Phi_rW
-\mathcal GW
=0.
}
\]

Equivalently,

\[
\boxed{
-\nu\Delta_cW
+
(T_\Phi-3\nu\partial_y)W
-
(\mathcal G+2\Phi_rI)W
-
2\nu W
=0.
}
\]

This is the exact flat-cylinder form for the stationary degree-`-2` vorticity profile.

---

## 5. Effective first-order characteristic field

The radial first-order term from viscosity may be grouped with the critical advection:

\[
\boxed{
\widetilde a
:=
(-\Phi_r-3\nu,\Phi_\tau).
}
\]

Then

\[
\widetilde a\cdot D
=
T_\Phi-3\nu\partial_y.
\]

Because the added radial vector is constant,

\[
\boxed{
\operatorname{div}_{cyl}\widetilde a
=
-\Phi_r.
}
\]

Thus the cylinder-divergence defect itself is unchanged.

---

## 6. Full profile lower-order matrix

Define

\[
\boxed{
\mathcal C
:=
\mathcal G+2\Phi_rI.
}
\]

The exact first-order/profile operator is

\[
\widetilde a\cdot D-\mathcal C.
\]

For a positive matrix metric `H`, its symmetric residual is

\[
\boxed{
K_H^{prof}
=
-(\widetilde a\cdot D)H
+
\Phi_rH
-
(H\mathcal C+\mathcal C^TH).
}
\]

Since

\[
\mathcal C
=
\mathcal G+2\Phi_rI,
\]

this becomes

\[
\boxed{
K_H^{prof}
=
-(\widetilde a\cdot D)H
-3\Phi_rH
-
(H\mathcal G+\mathcal G^TH).
}
\]

---

## 7. Determinant equation for exact profile skewness

If one requires exact skewness of the entire first-order critical profile operator,

\[
K_H^{prof}=0,
\]

then

\[
\boxed{
(\widetilde a\cdot D)H
=
-3\Phi_rH
-
H\mathcal G
-
\mathcal G^TH.
}
\]

Take normalized trace. Since

\[
\operatorname{tr}\mathcal G=0,
\]

we obtain

\[
\boxed{
(\widetilde a\cdot D)\log\det H
=-9\Phi_r.
}
\]

Thus the exact degree-`-2` profile symmetrizer has an even stronger radial determinant cohomology condition than the abstract physical-unknown first-order problem of M5-202/204.

This does not contradict M5-202: the two equations symmetrize different transformed operators. The additional factor comes from the degree-`-2` homogeneity term `-2 Phi_r W`.

---

## 8. Exact matrix-weighted diffusion identity

Let `D_c` denote the product-cylinder gradient

\[
D_c=(\partial_y,\nabla_{S^2}).
\]

For smooth compactly supported/periodic-decaying `W` and symmetric `H`, integration by parts gives

\[
\begin{aligned}
\int W^TH(-\Delta_cW)
&=
\int (D_cW)^TH(D_cW)\\
&\quad+
\sum_\mu
\int W^T(\partial_\mu H)(\partial_\mu W).
\end{aligned}
\]

The cross term can be integrated once more:

\[
\sum_\mu
\int W^T(\partial_\mu H)(\partial_\mu W)
=
-\frac12
\int W^T(\Delta_cH)W.
\]

Therefore

\[
\boxed{
\int W^TH(-\Delta_cW)
=
\int(D_cW)^TH(D_cW)
-
\frac12
\int W^T(\Delta_cH)W.
}
\]

This is exact.

A variable symmetrizer produces an unavoidable second-derivative metric potential.

---

## 9. Energy identity after exact first-order profile skewing

Assume `H` solves

\[
K_H^{prof}=0.
\]

Pair the stationary profile equation with `HW`.

The grouped first-order/profile contribution vanishes by construction.

The remaining equation is

\[
-\nu\Delta_cW
-2\nu W
+
(\widetilde a\cdot D-\mathcal C)W
=0.
\]

Hence

\[
\boxed{
\nu
\int(D_cW)^TH(D_cW)
-
\frac\nu2
\int W^T(\Delta_cH)W
-
2\nu
\int W^THW
=0.
}
\]

Equivalently,

\[
\boxed{
\int(D_cW)^TH(D_cW)
=
\frac12
\int W^T(\Delta_cH)W
+
2
\int W^THW.
}
\]

This is the exact matrix-diffusion balance for the fully first-order-symmetrized stationary degree-`-2` profile.

---

## 10. No pure positive-diffusion contradiction

The left side is nonnegative.

However the right side contains

1. the metric-curvature term
   \[
   \frac12\int W^T(\Delta_cH)W,
   \]
   which has no universal sign;
2. the positive homogeneity potential
   \[
   2\int W^THW.
   \]

Thus exact first-order skewness does **not** imply

\[
D_cW=0.
\]

Even if `H` were constant, the identity reduces to

\[
\boxed{
\int|D_cW|_H^2
=2\int|W|_H^2,
}
\]

which is a legitimate spectral balance rather than a contradiction.

The number `2` is precisely the degree-`-2` homogeneity potential.

---

## 11. Spherical spectral interpretation for constant metric

If `W` is `y`-independent and `H` constant, then

\[
\int_{S^2}|\nabla_SW|_H^2
=2\int_{S^2}|W|_H^2
\]

selects the first nonzero spherical Laplacian eigenvalue

\[
\lambda_1(S^2)=2.
\]

Therefore the residual viscous balance is naturally compatible with `l=1` spherical modes.

This is another reason why viscosity plus exact first-order skewness alone cannot eliminate every critical homogeneous profile.

One must use the divergence/curl relation tying `W` to the velocity profile, the pressure/NSE residual, or additional tail/core constraints.

---

## 12. Metric-curvature commutator is critical

Suppose

\[
cI\le H\le CI.
\]

Then the positive diffusion controls

\[
\int|D_cW|^2.
\]

But the commutator term obeys only schematically

\[
\left|
\int W^T(\Delta_cH)W
\right|
\le
\|\Delta_cH\|_\infty
\int|W|^2.
\]

Thus absorption would require a quantitative relation between

\[
\|\Delta_cH\|_\infty
\]

and the cylinder spectral gap / available Carleman coercivity.

The first-order Lyapunov transport equation for `H` controls derivatives **along characteristics**, not its full transverse Hessian.

Therefore no bound on `Delta_c H` follows merely from bounded ellipticity and elliptic Floquet monodromy.

This is a new independent regularity obligation for any local matrix symmetrizer method.

---

## 13. Completing-square form for first metric derivatives

Before the second integration by parts, one may estimate

\[
\int(DW)^THDW
+
\int W^T(DH)DW.
\]

Pointwise Young gives, for any `0<eta<1`,

\[
|W^T(\partial_\mu H)(\partial_\mu W)|
\le
\eta(\partial_\mu W)^TH(\partial_\mu W)
+
\frac1{4\eta}
W^T
(\partial_\mu H)H^{-1}(\partial_\mu H)
W.
\]

Hence matrix-gradient absorption requires control of

\[
\boxed{
\sum_\mu
(\partial_\mu H)H^{-1}(\partial_\mu H),
}
\]

again a full spatial metric-regularity quantity not supplied by monodromy alone.

Thus both the Hessian and first-gradient forms expose the same missing transverse regularity.

---

## 14. Relation to M5-203 elliptic monodromy

Elliptic monodromy ensures that along a periodic characteristic there exists a bounded positive metric satisfying the first-order cocycle equation.

M5-205 shows this is only a **zeroth-order/characteristic** success.

To use that metric in a PDE energy or Carleman estimate one additionally needs spatial regularity across neighboring characteristics:

\[
\boxed{
H,
\quad D_cH,
\quad\Delta_cH
\text{ uniformly controlled}.
}
\]

A family of individually elliptic monodromies can still vary rapidly across the sphere/log-radius variable and create an arbitrarily large diffusion commutator.

Therefore

\[
\boxed{
\text{elliptic Floquet type}
\not\Longrightarrow
\text{usable PDE symmetrizer}.
}
\]

---

## 15. Dynamic tails

If the critical tail/metric depends on similarity time, pairing a dynamic equation introduces in addition

\[
\frac12
\int W^TH_sW
\]

in the weighted energy derivative.

Thus a dynamic symmetrizer requires control of

\[
H_s
\]

as well as its spatial derivatives.

The periodic stationary-characteristic classification of M5-203 is therefore a necessary structural guide, not a complete dynamic backward-uniqueness theorem.

---

## 16. Updated matrix-method frontier

The local matrix route now has three successive gates:

\[
\boxed{
\begin{aligned}
\text{Gate 1: radial determinant cohomology}
&\quad\langle\Phi_r\rangle=0,\\
\text{Gate 2: full-gradient Floquet type}
&\quad M\sim O,\\
\text{Gate 3: PDE metric regularity}
&\quad D H,\Delta H,H_s\text{ controlled}.
\end{aligned}
}
\]

Only after all three can a matrix Carleman/energy scheme be meaningfully attempted.

The generic critical tail currently satisfies none of these universally.

---

## 17. DSD verdict

### PROVED

- exact degree-`-2` cylinder Laplacian;
- exact `-2 Phi_r W` homogeneity advection term;
- exact stationary critical vorticity cylinder equation;
- exact profile-level matrix symmetrizer residual;
- exact determinant equation `tilde a·grad log det H=-9 Phi_r` when the full profile lower-order operator is skewed;
- exact matrix-weighted diffusion identity with `Delta_c H` potential;
- exact post-symmetrization energy balance;
- pure positive-diffusion contradiction fails even for constant metric because of the degree-`-2` spectral potential;
- elliptic monodromy does not control metric spatial derivatives and is insufficient for a PDE symmetrizer.

### OPEN

- NSE constraints on the `l=1`-compatible residual modes;
- spatial regularity of an elliptic matrix metric across characteristics;
- dynamic metric derivative control;
- finite-window matrix Carleman estimates;
- generic critical backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 18. Next target

The most concrete remaining subbranch is the apparent `l=1` spectral compatibility.

A free vector field on the sphere can satisfy

\[
-\Delta_SW=2W,
\]

but `W` is not free: it must be the vorticity of a divergence-free degree-`-1` velocity profile `Phi` and must satisfy the full stationary/recurrent NSE sphere equations.

The next audit should classify which degree-`-2`, `l=1` vorticity modes are actually curls of smooth divergence-free degree-`-1` fields on `R^3\setminus\{0\}`, and then test them against the stationary homogeneous Navier--Stokes/Landau classification. If the only compatible modes reconstruct the already known Landau/zero families, the residual spectral branch will collapse back to the known homogeneous rigidity gate.