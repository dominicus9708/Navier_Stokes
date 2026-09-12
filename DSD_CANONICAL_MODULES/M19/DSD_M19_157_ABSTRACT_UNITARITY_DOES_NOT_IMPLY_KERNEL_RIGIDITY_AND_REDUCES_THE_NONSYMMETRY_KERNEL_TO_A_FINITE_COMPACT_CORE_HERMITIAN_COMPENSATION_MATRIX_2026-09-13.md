# DSD M19-157 — Abstract unitarity does not imply kernel rigidity and reduces the nonsymmetry kernel to a finite compact-core Hermitian compensation matrix

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / ABSTRACT-NO-GO + EXACT FINITE-DIMENSIONAL PDE CRITERION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-131--156 reduce the late critical survivor to a finite-dimensional, uniformly observable hard bundle with exact scattering isometry, and reduce the moderate relative-periodic nonlinear hard core substantially to the fixed-moduli unit-spectrum problem.

The first live target is the nonsymmetry kernel

\[
K_{\rm nsym}
=
\ker(I-\mathcal M_S^{tw})/E_{sym}^{\mu=1}.
\]

The present module asks whether the abstract structure already proved is sufficient to force

\[
K_{\rm nsym}=\{0\}.
\]

It is not. The gain is to isolate the exact additional Navier--Stokes sign condition that would be sufficient.

## 2. Abstract isometry alone is insufficient

On the observable hard fiber the scattering pullback metric satisfies

\[
\|\Phi_t(U)v\|_{sc,\sigma_tU}
=
\|v\|_{sc,U}.
\]

For a relative-periodic background this makes the twisted monodromy unitary in the corresponding finite-dimensional fiber metric.

But a finite-dimensional unitary matrix may have any multiplicity of the eigenvalue one. For example,

\[
M_{toy}
=
\operatorname{diag}
\left(
1_{time},
1_{extra},
e^{i\vartheta_3},
\ldots,
e^{i\vartheta_N}
\right)
\]

is semisimple, has no positive Lyapunov exponent, is uniformly bounded in both time directions, and satisfies every purely abstract unitary/quasi-compact conclusion retained so far, while still possessing an extra nonsymmetry kernel vector.

Therefore

\[
\boxed{
\text{quasi-compactness + observability + isometry}
\not\Rightarrow
K_{\rm nsym}=0.
}
\]

A genuinely PDE-specific sign, index, or orientation input is required.

## 3. Polarized linearized-vorticity identity

Let `W` be a linearized velocity perturbation and

\[
\eta=\nabla\times W.
\]

M19-087 gives

\[
\frac12\frac d{ds}\|\eta\|_2^2
+
\nu\|\nabla\eta\|_2^2
+
\frac14\|\eta\|_2^2
=
\mathcal C_U[W].
\]

Polarize the right-hand side. For two perturbations `W_a,W_b`, write

\[
\mathfrak C_U(W_a,W_b)
\]

for the Hermitian polarization of the real quadratic compensation form, so that

\[
\mathfrak C_U(W,W)=\mathcal C_U[W].
\]

Likewise define

\[
G_{ab}(s)
:=
\langle\eta_a,\eta_b\rangle_{L^2},
\]

\[
D_{ab}(s)
:=
\langle\nabla\eta_a,\nabla\eta_b\rangle_{L^2},
\]

and

\[
C_{ab}(s)
:=
\mathfrak C_U(W_a,W_b).
\]

The instantaneous Hermitian damping-minus-compensation matrix is

\[
\boxed{
H_U(s)
:=
\nu D(s)
+
\frac14G(s)
-
C(s).
}
\]

## 4. Exact one-period criterion for a kernel vector

Take a fixed-moduli twisted-periodic kernel perturbation

\[
\mathcal M_S^{tw}v=v,
\]

and transport it along the orbit:

\[
W(s)=\Phi_s v.
\]

Twisted return preserves the vorticity `L2` norm because the terminal rotation is orthogonal. Hence

\[
\|\eta(S)\|_2
=
\|\eta(0)\|_2.
\]

Integrating the exact vorticity identity over one period gives

\[
\boxed{
\int_0^S
\left[
\nu\|\nabla\eta\|_2^2
+
\frac14\|\eta\|_2^2
-
\mathcal C_U[W]
\right]ds
=0.
}
\]

Thus every nonzero kernel vector is a null direction of the period-averaged Hermitian form

\[
\boxed{
\mathscr H_U[v]
:=
\int_0^S
\left[
\nu\|\nabla\eta_v(s)\|_2^2
+
\frac14\|\eta_v(s)\|_2^2
-
\mathcal C_U[W_v(s)]
\right]ds.
}
\]

## 5. Symmetry quotient

Let

\[
E_{sym}^{\mu=1}
\]

be the exact fixed-moduli symmetry kernel remaining after the correct time/rotation representation from M19-147--148 is accounted for.

Choose the scattering-pullback orthogonal complement

\[
E_{q}
:=
(E_{sym}^{\mu=1})^{\perp_{sc}}
\cap E_{hard}.
\]

The desired kernel theorem is equivalent to showing that no nonzero `v in E_q` can satisfy the homogeneous twisted return.

A sufficient coercive criterion is therefore

\[
\boxed{
\exists\delta_{ker}>0:
\qquad
\mathscr H_U[v]
\ge
\delta_{ker}\|v\|_{sc,U}^2
\quad
\forall v\in E_q.
}
\]

If this holds uniformly over the compact moderate corridor, then

\[
\boxed{K_{\rm nsym}=0}
\]

uniformly.

## 6. Finite matrix form

Because `E_q` is finite-dimensional, choose a scattering-orthonormal basis

\[
e_1,\ldots,e_N.
\]

Transport each basis vector through one period. Define the period matrices

\[
\overline G_{ab}
:=
\int_0^S G_{ab}(s)ds,
\]

\[
\overline D_{ab}
:=
\int_0^S D_{ab}(s)ds,
\]

\[
\overline C_{ab}
:=
\int_0^S C_{ab}(s)ds.
\]

Then

\[
\boxed{
\overline H
=
\nu\overline D
+
\frac14\overline G
-
\overline C.
}
\]

Kernel rigidity follows from the finite-dimensional condition

\[
\boxed{
\lambda_{min}
\left(
\overline H|_{E_q}
\right)
>0.
}
\]

This is now an ordinary Hermitian eigenvalue problem on the compact hard fiber.

## 7. Relation to the quarter-gap/Ky-Fan budgets

M19-121--122 gave only necessary trace/Ky-Fan conditions for nonnegative transverse growth. Those estimates do not determine the smallest eigenvalue of `overline H`.

The present criterion is strictly sharper:

- Ky-Fan/trace information can say that several directions cannot all be neutral;
- kernel rigidity requires that **no individual nonsymmetry direction** be neutral;
- this is exactly a smallest-eigenvalue question for the finite compact-core compensation matrix.

Thus the remaining theorem is not a missing compactness argument. It is a missing **spectral sign theorem**.

## 8. Compact-corridor consequence

The moderate RSS and bounded-period RDSS hard sets from M19-153--155 are compact after all retained gauges and low-mode truncations.

If the hard spectral bundle and the matrices above vary continuously, then

\[
U\mapsto
\lambda_{min}(\overline H_U|_{E_q(U)})
\]

is continuous on each fixed-rank stratum.

Hence it is enough to prove pointwise strict positivity on a compact stratum; uniform positivity then follows automatically:

\[
\boxed{
\lambda_{min}>0\ \text{pointwise on compact stratum}
\Longrightarrow
\inf\lambda_{min}>0.
}
\]

Rank/isotropy changes remain typed boundary strata rather than being hidden.

## 9. What current estimates do and do not prove

Current estimates control the compensation form by quantities of the type

\[
\nu^{-1}\|\Omega\|_3^2
+
\|\nabla\Omega\|_3
\]

and descend them to palinstrophy/raw-H2 activity.

But M19-094 showed that unsigned derivative budgets do not force those quantities below the quarter-gap threshold, and M19-066 showed that the background itself needs positive stretching on average.

Therefore the presently available scalar norm bounds do **not** prove

\[
\overline H>0
\]

on the symmetry quotient.

A sign/orientation/index theorem about how compact-core strain and the nonlocal vorticity coupling act on the finite hard fiber is still required.

## 10. Audit verdict

### Proved

1. Purely abstract quasi-compact/unitary structure does not imply nonsymmetry kernel rigidity.
2. Every fixed-moduli kernel mode is an exact null direction of the period-averaged vorticity damping-minus-compensation form.
3. On the finite hard bundle, uniform kernel rigidity is equivalent to a finite-dimensional Hermitian smallest-eigenvalue problem after symmetry quotient.
4. Pointwise strict positivity automatically upgrades to a uniform positive gap on a compact fixed-rank hard stratum.

### Not proved

1. Positivity of the symmetry-quotient Hermitian compensation matrix.
2. Universal nonsymmetry kernel exclusion.
3. Irrational elliptic neutral-mode exclusion.
4. Global regularity.

## 11. Next target

M19-158 should sharpen the positive side of `overline H` by combining the compact-core activity floor from M19-150 with a localized vorticity Poincare estimate and the critical-tail boundary decay.

The goal is to replace the bare quarter-gap

\[
\frac14
\]

by

\[
\frac14+\delta_{core}
\]

on normalized nonsymmetry unit modes, leaving a correspondingly stronger explicit threshold for the compact-core compensation operator.
