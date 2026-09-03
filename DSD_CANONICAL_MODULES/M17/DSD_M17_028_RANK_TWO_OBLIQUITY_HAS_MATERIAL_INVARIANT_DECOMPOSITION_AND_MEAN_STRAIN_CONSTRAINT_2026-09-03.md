# DSD M17-028 — Rank-two obliquity has a material-invariant decomposition and a mean strain constraint

Date: 2026-09-03
Canonical ID: **M17-028**

Status: **INTERNAL RANK-TWO CO-FROZEN GEOMETRY / WITH `W_tilde=W/a`, BOTH `J_xi` AND `W_tilde` OBEY THE SAME FROZEN-IN VECTOR-DENSITY LAW. THE SCALAR COEFFICIENT `c=(a j_xi)/rho`, WHICH IS THE COMPONENT OF `J_xi` ALONG `W_tilde`, IS EXACTLY MATERIAL INVARIANT. THEREFORE `K_xi:=J_xi-c W_tilde` IS A CO-FROZEN VECTOR PERPENDICULAR TO `xi`. `K_xi=0` IS THE PARALLEL BRANCH; `K_xi!=0` IS THE OBLIQUE BRANCH, AND THIS SPLIT IS MATERIAL. THE OBLIQUITY RATIO OBEYS `D_B log(|K_xi|/|W_tilde|)=sigma_K-sigma`, WHERE `sigma_K=Khat dot Sigma Khat`. A UNIFORMLY RECURRENT OBLIQUE RATIO FORCES `mean sigma_K = mean sigma`; IF THE DIRECTOR-AREA DENSITY/RESCALED VORTICITY MAGNITUDE IS ALSO RECURRENT, THEN `mean sigma=1` AND THE MATERIAL TRANSVERSE FRAME HAS MEAN QUADRATIC STRAINS `(1,1,-2)`. THIS IS A STRONG HYPERBOLIC RECURRENCE CONSTRAINT BUT NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Co-frozen fields

M17-026 gives

\[
\widetilde W:=\frac Wa,
\qquad
D_Ba=\kappa a,
\]

with

\[
\boxed{
D_B\widetilde W
=(\nabla B)\widetilde W-\frac32\widetilde W.
}
\]

The director-area current satisfies

\[
\boxed{
D_BJ_\xi
=(\nabla B)J_\xi-\frac32J_\xi.
}
\]

Also

\[
\widetilde W
=\frac\rho a\xi.
\]

---

## 2. Material invariant parallel coefficient

The component of `J_xi` along `xi` is

\[
j_\xi=J_\xi\cdot\xi.
\]

The magnitude of the rescaled vorticity is

\[
|\widetilde W|=\frac\rho a.
\]

Define

\[
\boxed{
c
:=\frac{j_\xi}{\rho/a}
=\frac{a j_\xi}{\rho}.
}
\]

Use

\[
D_B\log a=\kappa,
\]

\[
D_B\log|j_\xi|=\sigma-1,
\]

and

\[
D_B\log\rho=\sigma+\kappa-1.
\]

Then

\[
D_B\log|c|
=\kappa+(\sigma-1)-(\sigma+\kappa-1)=0.
\]

Hence

\[
\boxed{D_Bc=0.}
\]

This is the signed material ratio of director-area flux density to rescaled vorticity flux density.

---

## 3. Canonical obliquity vector

Define

\[
\boxed{
K_\xi
:=J_\xi-c\widetilde W.
}
\]

Because

\[
c\widetilde W\cdot\xi
=c\frac\rho a
=j_\xi,
\]

we have

\[
\boxed{K_\xi\cdot\xi=0.}
\]

Since `c` is materially constant and both parent fields satisfy the same linear transport law,

\[
\boxed{
D_BK_\xi
=(\nabla B)K_\xi-\frac32K_\xi.
}
\]

Thus `K_xi` is itself a co-frozen transverse vector-density field.

---

## 4. Parallel and oblique branches

The rank-two split is now exact:

### Parallel branch

\[
\boxed{K_\xi=0.}
\]

Then

\[
J_\xi=c\widetilde W
\parallel W.
\]

Since `J_xi` spans the kernel of `d xi`,

\[
\boxed{(\xi\cdot\nabla)\xi=0.}
\]

### Oblique branch

\[
\boxed{K_\xi\ne0.}
\]

Then `J_xi` has a nonzero component transverse to vorticity.

Because `K_xi` satisfies a homogeneous linear frozen-in equation, a nonzero material value cannot become exactly zero under an invertible smooth deformation.
Therefore parallel versus oblique is a material-invariant split on the regular rank-two branch.

---

## 5. Magnitude law for rescaled vorticity

Since

\[
\widetilde W=\widetilde\rho\,\xi,
\qquad
\widetilde\rho:=\rho/a,
\]

and `xi` is an eigenvector of the strain with eigenvalue `sigma`,

\[
D_B\log\widetilde\rho
=\sigma-1.
\]

Thus

\[
\boxed{
D_B\log|\widetilde W|=\sigma-1.
}
\]

This is identical to the scalar `j_xi` rate, consistent with constant `c`.

---

## 6. Magnitude law for the obliquity vector

Let

\[
\widehat K:=\frac{K_\xi}{|K_\xi|}
\]

and define the transverse quadratic strain

\[
\boxed{
\sigma_K
:=\widehat K\cdot\Sigma\widehat K.
}
\]

The antisymmetric part of `grad U` does not contribute to norm growth.
Since

\[
\nabla B=\nabla U+\frac12I,
\]

we obtain

\[
\begin{aligned}
D_B\log|K_\xi|
&=\widehat K\cdot(\nabla B)\widehat K-\frac32\\
&=\sigma_K+\frac12-\frac32.
\end{aligned}
\]

Therefore

\[
\boxed{
D_B\log|K_\xi|
=\sigma_K-1.
}
\]

---

## 7. Obliquity ratio

Define

\[
\boxed{
r_K
:=\frac{|K_\xi|}{|\widetilde W|}.}
\]

Then

\[
\boxed{
D_B\log r_K
=\sigma_K-\sigma.
}
\]

Equivalently, since the parallel component of `J_xi` is `c W_tilde`, the Euclidean obliquity angle `beta` satisfies

\[
\tan\beta
=\frac{r_K}{|c|}
\]

where `c != 0` on the transverse rank-two branch.
Hence

\[
\boxed{
D_B\log\tan\beta
=\sigma_K-\sigma.
}
\]

The angle itself need not be invariant; its logarithmic drift is exactly the transverse-minus-vortex strain difference.

---

## 8. Recurrent oblique geometry

Suppose the obliquity remains uniformly nondegenerate and bounded:

\[
0<c_r\le r_K(\theta)\le C_r<\infty
\]

on a recurrent marked rank-two trajectory.
Then

\[
\boxed{
\langle\sigma_K-\sigma\rangle=0.
}
\]

Thus

\[
\boxed{
\langle\sigma_K\rangle
=\langle\sigma\rangle.
}
\]

This is the rank-two obliquity recurrence condition.

---

## 9. Add recurrence of director-area density

If in addition the marked transverse director-area density remains bounded above and below,

\[
0<c_j\le|j_\xi|\le C_j<\infty,
\]

then

\[
D_B\log|j_\xi|=\sigma-1
\]

forces

\[
\boxed{
\langle\sigma\rangle=1.
}
\]

Hence recurrent obliquity gives

\[
\boxed{
\langle\sigma_K\rangle=1.
}
\]

---

## 10. Mean third transverse strain

At each point, `xi` is a strain eigenvector.
Because `Sigma` is symmetric, the plane `xi^perp` is invariant under `Sigma`.

Let

\[
\widehat N:=\xi\times\widehat K.
\]

Then `xi,Khat,Nhat` is an orthonormal frame.
Define

\[
\sigma_N:=\widehat N\cdot\Sigma\widehat N.
\]

Trace-free strain gives pointwise

\[
\boxed{
\sigma+\sigma_K+\sigma_N=0.
}
\]

Therefore under the recurrent conditions above,

\[
\boxed{
\langle\sigma_N\rangle=-2.
}
\]

Thus the mean quadratic strain pattern in the material rank-two frame is

\[
\boxed{
(\langle\sigma\rangle,
\langle\sigma_K\rangle,
\langle\sigma_N\rangle)
=(1,1,-2).
}
\]

This is a mean statement; `Khat` need not be a pointwise eigenvector of `Sigma`.

---

## 11. Add raw-vorticity recurrence

If the raw vorticity amplitude is also recurrent and bounded away from zero on the marked trajectory,

\[
D_B\log\rho
=\sigma+\kappa-1
\]

and

\[
\langle\sigma\rangle=1
\]

give

\[
\boxed{
\langle\kappa\rangle=0.
}
\]

Thus a fully recurrent rank-two material marker with stable director area, obliquity and amplitude must satisfy

\[
\boxed{
\langle\sigma\rangle=1,
\qquad
\langle\kappa\rangle=0.
}
\]

This is compatible with the earlier fixed-flux zero-mean kappa channels and is not yet contradictory.

---

## 12. DSD interpretation

### 12.1 Obliquity separated from flux amplification
Removing `a` from vorticity exposes the purely geometric co-frozen field.
The remaining difference between `J_xi` and vorticity is a material transverse vector `K_xi`.

### 12.2 Recurrent angle requires strain balance
A stable nonzero oblique angle cannot be maintained unless the material mean strain seen by the obliquity direction matches that seen by the vortex direction.

### 12.3 Hyperbolic frame
If director area itself also recurs, the mean frame necessarily has two directions at strain `+1` and a compensating transverse direction at `-2`.

---

## 13. DSD audit

### Audit A — claiming Khat is a strain eigenvector
Rejected.
Only its quadratic strain `sigma_K` is used.

### Audit B — claiming obliquity angle is invariant
Rejected.
Its drift is `sigma_K-sigma`.
Parallel/nonparallel status, not Euclidean angle, is the exact material invariant.

### Audit C — deriving mean sigma=1 without j recurrence
Rejected.
That step explicitly assumes bounded nonzero recurrent `j_xi`.

### Audit D — treating mean strain pattern as a contradiction
Rejected.
A recurrent Eulerian structure can be maintained by material turnover and anisotropic deformation.

### Audit E — proof status
Rank two remains open.

---

## 14. Updated rank-two subbranches

The separated rank-two branch is now

\[
\boxed{
R_2^{parallel}
\ \lor\ 
R_2^{oblique-recurrent}
\ \lor\ 
R_2^{obliquity-drift}.
}
\]

- `R_2^parallel`: `K_xi=0`, straight director along vortex lines.
- `R_2^{oblique-recurrent}`: nonzero bounded obliquity ratio with `mean sigma_K = mean sigma`.
- `R_2^{obliquity-drift}`: the angle drifts toward parallelity or transverse dominance, or leaves the recurrent bounded geometry.

---

## 15. Next target

The parallel branch has the additional exact geometric condition

\[
(\xi\cdot\nabla)\xi=0.
\]

The next useful audit is to combine this straight-vortex-direction condition with

\[
\nabla\cdot W=0,
\]

the weighted harmonic-director equation, and finite-energy/decay assumptions.

For the oblique branch, the next target is whether the mean `(1,1,-2)` material strain frame can remain compactly recurrent without rank loss or flux turnover.

These form the **Rank-Two Parallel/Oblique Closure Gate (R2POCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
