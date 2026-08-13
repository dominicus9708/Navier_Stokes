# First-hitting `L^infinity` vorticity reduces local stretching to affine mean plus a bounded BMO remainder

Date: 2026-08-13

Status: **STANDARD CZ/BMO BRIDGE + DERIVED LOCAL SOURCE DECOMPOSITION / AFFINE-COVARIANCE DYNAMICS REMAIN OPEN**.

On a first-hitting normalized window,

\[
\|\Omega(s)\|_{L^\infty(\mathbb R^3)}\le1.
\]

The strain is a zero-order Calderon--Zygmund singular-integral transform of vorticity.  Therefore the endpoint harmonic-analysis mapping

\[
L^\infty\to BMO
\]

shows that the **mean-free local strain oscillation is uniformly bounded**, even though the local mean strain itself may be large.

This gives a sharp DSD compression of the local stretching source into a finite-dimensional affine mean plus a uniformly bounded residual-complexity term.

---

## 1. Strain as a zero-order singular integral of vorticity

For divergence-free velocity in `R3`, the Biot--Savart law and differentiation give

\[
\boxed{S=\mathcal T\Omega,}
\]

where `T` is a matrix-valued homogeneous Calderon--Zygmund operator of order zero.

Classical endpoint theory gives

\[
\boxed{
\|S\|_{BMO}
\le C\|\Omega\|_\infty.
}
\]

Hence on the first-hitting window,

\[
\boxed{
\|S\|_{BMO}\le C.
}
\]

The constant depends only on dimension/operator normalization.

---

## 2. John--Nirenberg upgrades mean oscillation to every finite `Lp`

For a fixed ball `B` and

\[
S_B=\fint_BS\,dz,
\]

John--Nirenberg implies, for every finite `p>=1`,

\[
\boxed{
\left(
\fint_B|S-S_B|^p dz
\right)^{1/p}
\le C_p\|S\|_{BMO}
\le C_p.
}
\]

In particular,

\[
\boxed{
\int_B|S-S_B|dz
\le C|B|
}
\]

and

\[
\boxed{
\int_B|S-S_B|^2dz
\le C|B|.
}
\]

Thus the mean-free residual strain cannot develop an arbitrarily large local finite-`Lp` norm while the first-hitting vorticity amplitude remains normalized by one.

---

## 3. Exact local source decomposition

Define the local enstrophy

\[
E_B=\int_B|\Omega|^2dz.
\]

When `E_B>0`, define the local vorticity covariance

\[
\boxed{
C_B
=\frac1{E_B}
\int_B\Omega\otimes\Omega\,dz.
}
\]

Then

\[
\operatorname{tr}C_B=1,
\qquad C_B\succeq0.
\]

The local stretching source is

\[
Q_B=\int_B\Omega\cdot S\Omega\,dz.
\]

Split

\[
S=S_B+(S-S_B).
\]

The affine-mean part is exactly

\[
\boxed{
\int_B\Omega\cdot S_B\Omega\,dz
=E_B\operatorname{tr}(S_BC_B).
}
\]

The residual part satisfies, using `|Omega|<=1`,

\[
\begin{aligned}
\left|
\int_B\Omega\cdot(S-S_B)\Omega\,dz
\right|
&\le
\|\Omega\|_\infty^2
\int_B|S-S_B|dz\\
&\le C|B|.
\end{aligned}
\]

Therefore

\[
\boxed{
Q_B
=E_B\operatorname{tr}(S_BC_B)
+R_B,
\qquad
|R_B|\le C|B|.
}
\]

This is the main local source reduction.

---

## 4. Projective covariance depletion of the affine term

Let

\[
J_B=1-\operatorname{tr}(C_B^2).
\]

Since `tr S_B=0`, the trace-free covariance comparison gives

\[
\boxed{
|\operatorname{tr}(S_BC_B)|
\le
|S_B|_F
\sqrt{\frac23-J_B}.
}
\]

Hence

\[
\boxed{
|Q_B|
\le
E_B|S_B|_F
\sqrt{\frac23-J_B}
+C|B|.
}
\]

Thus the only potentially unbounded local source channel is a **finite-dimensional affine mean strain coupled to a sufficiently favorable vorticity covariance**.

The non-affine strain complexity is uniformly bounded in the first-hitting normalization.

---

## 5. Relation to the optimal affine representative

The ball mean `S_B` is the simplest constant-strain representative.  With a smooth observation weight `phi`, the preferred DSD representative is

\[
S_\phi
=\operatorname{sym}
\frac{\int\phi\nabla U}{\int\phi}.
\]

The same structure holds with weighted averages, up to using the corresponding weighted BMO/finite-`Lp` estimates or a fixed nested ball/cutoff comparison.

The key ordering is

\[
\boxed{
\text{total local gradient}
\longrightarrow
\text{affine mean}
+\text{mean-free residual}.
}
\]

The residual has controlled oscillation; only the affine mean needs separate deformation/covariance tracking.

---

## 6. Consequence for local compactness

On bounded-affine windows, the residual strain lies uniformly in every finite local `Lp`.  This supplies exactly the finite-`Lp` coefficient control used by the local derivative-energy and parabolic compactness estimates.

Thus one no longer needs to treat arbitrary residual strain growth as an independent branch under first-hitting normalization.

The principal local alternatives become

\[
\boxed{
|S_B|\text{ bounded}
\Longrightarrow
\text{all local finite-}Lp\text{ strain channels bounded},
}
\]

or

\[
\boxed{
|S_B|\to\infty
\Longrightarrow
\text{coherent affine-strain concentration}.
}
\]

---

## 7. What this does not prove

The estimate

\[
|R_B|\le C|B|
\]

does not make the residual source small on a unit normalized ball; it only prevents it from becoming unbounded.

Order-one residual stretching is still enough to matter over an order-one normalized time interval.

Likewise, the estimate does not bound the affine mean `S_B`; BMO is invariant under addition of constants.

Therefore the remaining dynamic question is whether repeated first-hitting amplification can be sustained by

\[
E_B\operatorname{tr}(S_BC_B)
\]

plus an order-one residual source while respecting the Cauchy I/V, deformation, projective, and viscous budgets.

---

## 8. External harmonic-analysis anchors

The two standard ingredients are:

1. Calderon--Zygmund/Riesz transforms map `L-infinity` boundedly into `BMO`;
2. the John--Nirenberg theorem upgrades bounded mean oscillation to exponential integrability and hence to finite local `Lp` mean-oscillation bounds for every finite `p`.

These are classical harmonic-analysis results.  The present note uses them only as external endpoint estimates; the local Navier--Stokes source decomposition above is derived here.

---

## 9. DSD interpretation

At first-hitting resolution, the local strain channel becomes

\[
\boxed{
S
\rightsquigarrow
(S_B,\ S-S_B).
}
\]

The second component has uniformly bounded describable oscillation.  Therefore increasing resolution is not justified merely because the residual field looks complicated; its aggregate source capacity is already bounded.

Further resolution is required only if the finite-dimensional mean affine strain or its covariance coupling becomes dangerous.

Status: **LOCAL RESIDUAL STRAIN COMPLEXITY BOUNDED / AFFINE-MEAN COVARIANCE DYNAMICS IS THE REMAINING SOURCE CHANNEL**.
