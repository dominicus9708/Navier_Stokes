# M19-251 — The frozen half-space Oseen–Stokes boundary determinant excludes bare poloidal unit shell modes

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / LOCAL SPECTRAL NORMAL FORM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-241 excludes bare toroidal cavity unit multipliers. M19-247--250 identify the poloidal pressure-supported shell as the only regular leading shell geometry, but show that every scale-tight regular sublinear profile is non-L2 unless it vanishes.

This module resolves the corresponding **frozen local spectral problem** directly. Near a remote boundary point, flatten the sphere and freeze the similarity drift. The resulting half-space Oseen–Stokes problem has no nonzero no-slip mode with unit/Floquet real part zero, in the poloidal sector as well.

## 2. Frozen local half-space model

Let

\[
x:=R-r>0
\]

be inward normal distance from the remote boundary. Freeze the leading similarity coefficient at \(r=R\) and ignore the lower-order critical background, curvature, and \(O(R^{-1})\) coefficient variations for the moment.

The bare local system is

\[
\boxed{
\lambda W
=
\nu(\partial_x^2+\Delta_T)W
+\frac R2\partial_xW
-\frac12W
-\nabla P,
}
\]

\[
\nabla\cdot W=0,
\qquad
W|_{x=0}=0,
\qquad
W\to0\quad(x\to\infty).
\]

A relative unit multiplier over a bounded period corresponds locally to

\[
\boxed{\operatorname{Re}\lambda=0}
\]

(the rotational/Floquet phase changes the imaginary part only).

## 3. Tangential Fourier decomposition

Take one tangential Fourier mode with wave vector \(\xi\) and

\[
k:=|\xi|\ge0.
\]

The toroidal polarization is pressure-free and is already covered by the M19-241 negative-gap architecture. The remaining two-dimensional plane spanned by the inward normal and \(\xi\) is the poloidal sector.

Write

\[
W=(V,U),
\]

where \(V\) is the inward-normal component and \(U\) is the tangential component parallel to \(\xi\). Then

\[
\partial_xV+ikU=0.
\]

## 4. Pressure harmonic mode

Taking divergence of the bare frozen system gives

\[
(\partial_x^2-k^2)P=0.
\]

The decaying pressure is therefore

\[
\boxed{P(x)=P_0e^{-kx}}
\]

for \(k>0\). For \(k=0\), a decaying pressure gradient is absent and the argument reduces to the scalar no-slip mode.

## 5. Viscous Oseen root

For a homogeneous velocity mode

\[
W_h=W_0e^{-\alpha x},
\qquad
\operatorname{Re}\alpha>0,
\]

the scalar Oseen factor is

\[
\boxed{
F(\alpha)
:=
\lambda
-\nu(\alpha^2-k^2)
+\frac R2\alpha
+\frac12.
}
\]

A homogeneous decaying mode satisfies

\[
\boxed{F(\alpha)=0.}
\]

For \(\operatorname{Re}\lambda=0\) and large positive \(R\), exactly one root belongs to the strongly decaying boundary-layer side; the other root is not a decaying half-space mode. The determinant argument below only needs the decaying root that can participate in no-slip matching.

## 6. Pressure-forced poloidal mode

For the pressure exponent \(e^{-kx}\),

\[
F(k)
=
\lambda+rac{Rk}{2}+\frac12.
\]

The pressure force is

\[
-\nabla P
=(kP_0,-ikP_0)e^{-kx}.
\]

When \(F(k)\neq0\), the pressure-forced divergence-free velocity is

\[
\boxed{
V_p=\frac{kP_0}{F(k)}e^{-kx},
\qquad
U_p=-\frac{ikP_0}{F(k)}e^{-kx}.
}
\]

Indeed

\[
\partial_xV_p+ikU_p=0.
\]

## 7. No-slip boundary determinant

Let the homogeneous viscous mode have normal boundary amplitude \(V_h(0)=C\). Incompressibility gives

\[
U_h(0)=-\frac{i\alpha}{k}C.
\]

The normal no-slip condition

\[
V_h(0)+V_p(0)=0
\]

forces

\[
C=-\frac{kP_0}{F(k)}.
\]

Then the tangential no-slip condition becomes

\[
\begin{aligned}
0
&=U_h(0)+U_p(0)\\
&=
\frac{i\alpha P_0}{F(k)}
-\frac{ikP_0}{F(k)}\\
&=
\frac{i(\alpha-k)P_0}{F(k)}.
\end{aligned}
\]

For a nonzero poloidal mode,

\[
\boxed{\alpha=k}
\]

is therefore necessary.

But \(\alpha\) must also satisfy \(F(\alpha)=0\). Hence a nonzero mode would require

\[
\boxed{F(k)=0.}
\]

## 8. Unit/Floquet real part makes the determinant strictly nonzero

If

\[
\operatorname{Re}\lambda=0,
\]

then

\[
\boxed{
\operatorname{Re}F(k)
=
\frac{Rk}{2}+\frac12
>0
}
\]

for every

\[
k\ge0.
\]

Therefore

\[
F(k)\neq0,
\]

so the necessary no-slip condition \(\alpha=k\) cannot be met.

Thus

\[
\boxed{
\text{the frozen bare half-space Oseen--Stokes problem has no nonzero poloidal mode with }\operatorname{Re}\lambda=0.
}
\]

For \(k=0\), incompressibility and decay force the normal component to vanish, while the remaining tangential scalar mode has only one decaying Oseen root and cannot satisfy nonzero no-slip data. Hence the conclusion also holds at \(k=0\).

## 9. Combined bare-shell conclusion

M19-241 supplies toroidal bare rigidity; the present determinant supplies poloidal bare rigidity. Therefore the complete frozen bare shell has no unit/Floquet mode:

\[
\boxed{
\text{bare frozen remote shell}
\Longrightarrow
\text{no nonzero }\operatorname{Re}\lambda=0\text{ no-slip mode}.
}
\]

The key poloidal boundary factor has a quantitative real separation

\[
\boxed{
\operatorname{Re}F(k)
\ge\frac12.
}
\]

For \(k>0\), the separation strengthens by \(Rk/2\).

## 10. Relation to M19-247

The local polynomial profile

\[
v_T=2d\nabla_{S^2}p_0,
\qquad
v_r=d^2\Delta_{S^2}p_0
\]

from M19-247 is the quasi-static leading Taylor balance produced before imposing decay/tightness on the half-line. M19-251 shows why that polynomial pressure-supported balance cannot become a decaying unit Floquet eigenmode of the full frozen half-space problem.

Thus

\[
\boxed{
\text{local pressure-work saturation}
\neq
\text{spectral unit return}.
}

## 11. Remaining perturbation problem

The actual cavity shell is not exactly frozen or bare. It contains:

- curvature of the sphere;
- \(r-R\) variation of the similarity coefficient;
- time/rotation dependence;
- the critical background \(U=O(R^{-1})\), \(\nabla U=O(R^{-2})\);
- possible scaled tangential/radial/time-frequency decompactification.

For compact shell frequencies and bounded local scales, these are lower-order coefficient perturbations of the frozen model. However a local spectral determinant is not automatically a global pseudospectral stability theorem.

The next target is therefore

\[
\boxed{
\mathcal T_{shell}^{pert}:
\text{prove that the }\operatorname{Re}F(k)\ge1/2\text{ boundary determinant remains nonvanishing under the actual lower-order shell perturbations,}
}
\]

or else show that any failure requires precisely the scaled decompactification already isolated in M19-250.

## 12. Scope firewall

This module proves a frozen local normal-form rigidity, not the full cavity spectral theorem.

Therefore

\[
\boxed{
\text{frozen half-space determinant gap}
\neq
\text{uniform full-cavity resolvent gap}.
}

The gap becomes a valid closure mechanism only after perturbation and localization errors are controlled in the same norm as the shell mode.
