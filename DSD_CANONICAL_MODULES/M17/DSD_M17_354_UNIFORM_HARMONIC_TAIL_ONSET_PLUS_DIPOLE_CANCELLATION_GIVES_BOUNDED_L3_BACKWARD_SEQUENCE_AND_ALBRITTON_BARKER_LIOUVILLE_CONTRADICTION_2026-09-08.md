# DSD M17-354 — Uniform harmonic-tail onset plus dipole cancellation gives a bounded `L3` backward sequence and the Albritton--Barker Liouville contradiction

Date: 2026-09-08  
Canonical ID: **M17-354**

Status: **ACTIVE CONDITIONAL EXTERNAL-LIOUVILLE CLOSURE OF THE HARMONIC-EXTERIOR SUBBRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Ancient input

M5-474 extracts a nontrivial smooth whole-space ancient Navier--Stokes element `(V,Omega)` with

\[
|\Omega(0,0)|=1,
\]

and the canonical Galilean/Biot--Savart gauge.

M5-475/477 give at backward Type-I record times

\[
t_m=-T_m\to-\infty,
\qquad
R_m:=\sqrt{T_m},
\]

\[
\boxed{
\|\Omega(t_m)\|_\infty\le C R_m^{-2},
}
\]

and

\[
\boxed{
\|\Omega(t_m)\|_2^2\le C R_m^{-1}.
}
\]

Thus

\[
\|\Omega(t_m)\|_2\le C R_m^{-1/2}.
\]

## 2. Uniform normalized harmonic-tail onset

Work on the M17-349 coefficient-compact / unbounded-vortex-line branch and assume its harmonic exterior starts at a uniformly bounded normalized radius along the record sequence:

\[
\boxed{
\Delta\Omega(\cdot,t_m)=0
\qquad
\text{for }|x|>C_hR_m,
}
\]

with fixed `C_h<infinity`.

This is the natural same-scale realization of the record-cell compact tail.  Failure is recorded explicitly as

\[
G_{harmonic\text{-}onset/tail\text{-}topology\ decompactification}.
\]

M17-353 eliminates the only `r^-2` harmonic vorticity mode, so the exterior expansion begins at multipole order `ell>=2`.

## 3. Interior L^{3/2} vorticity bound

Let

\[
B_m:=B(0,2C_hR_m).
\]

On a finite-volume set, Hölder gives

\[
\|\Omega\|_{L^{3/2}(B_m)}
\le
|B_m|^{1/6}\|\Omega\|_{L^2(B_m)}.
\]

Since

\[
|B_m|^{1/6}\asymp R_m^{1/2},
\]

and

\[
\|\Omega(t_m)\|_2\le CR_m^{-1/2},
\]

we get

\[
\boxed{
\|\Omega(t_m)\|_{L^{3/2}(B_m)}\le C.
}
\]

The bound is uniform in `m`.

## 4. Uniform exterior harmonic decay after dipole cancellation

Rescale the exterior by `R_m`:

\[
\widetilde\Omega_m(y)
:=
R_m^2\Omega(R_my,t_m).
\]

The Type-I maximum bound gives

\[
\|\widetilde\Omega_m\|_\infty\le C.
\]

The field is harmonic for

\[
|y|>C_h,
\]

and M17-353 removes its `ell=1` / `|y|^-2` harmonic coefficient.  The `ell=0` / `|y|^-1` coefficient is excluded by `L2`.

Therefore the exterior spherical-harmonic expansion begins at `ell>=2`, and standard exterior harmonic estimates give, for `|y|>=2C_h`,

\[
\boxed{
|\widetilde\Omega_m(y)|
\le
C_h'|y|^{-3},
}
\]

with a constant uniform on the compact normalized tail family.

Returning to physical variables,

\[
\boxed{
|\Omega(x,t_m)|
\le
C\frac{R_m}{|x|^3}
\qquad
(|x|\ge2C_hR_m).
}
\]

## 5. Exterior L^{3/2} bound

Using the preceding decay,

\[
\begin{aligned}
\int_{|x|>2C_hR_m}|\Omega|^{3/2}dx
&\le
C R_m^{3/2}
\int_{2C_hR_m}^{\infty}
r^{-9/2}r^2dr\\
&\le C.
\end{aligned}
\]

Hence

\[
\boxed{
\|\Omega(t_m)\|_{L^{3/2}(|x|>2C_hR_m)}\le C.
}
\]

The transition annulus is already included in the interior estimate.

Therefore

\[
\boxed{
\sup_m\|\Omega(t_m)\|_{L^{3/2}(\mathbb R^3)}<\infty.
}
\]

## 6. Uniform strong L3 velocity sequence

In the canonical Biot--Savart gauge,

\[
V=\nabla\times(-\Delta)^{-1}\Omega.
\]

The Hardy--Littlewood--Sobolev estimate gives

\[
\|V\|_{L^3}
\le C\|\Omega\|_{L^{3/2}}.
\]

Thus

\[
\boxed{
\sup_m\|V(t_m)\|_{L^3(\mathbb R^3)}<\infty.
}
\]

This is scale critical and is exactly a backward sequence bound, not a uniform-in-all-time claim.

## 7. External Liouville theorem

Albritton--Barker, Theorem 1.2 in *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, proves:

> if `v` is a mild ancient solution on `R3` and there exists `t_k -> -infinity` with `sup_k ||v(t_k)||_3 < infinity`, then `v identically 0`.

The M5-474 ancient element is the smooth bounded ancient element obtained by whole-space Navier--Stokes blow-up compactness in the Biot--Savart/Galilean gauge; on the present branch it is read in the corresponding mild ancient class.

Therefore the record-sequence estimate gives

\[
\boxed{V\equiv0.}
\]

But M5-474 has

\[
|\Omega(0,0)|=1.
\]

Contradiction.

## 8. Closed harmonic-exterior branch

Hence the branch

\[
\boxed{
\text{coefficient-compact exterior}
+\text{unbounded vortex-line coverage}
+\text{uniform normalized harmonic onset}
}
\]

is impossible.

The active tail exits are reduced to

\[
\boxed{
G_{tail\ coefficient/nodal\ decompactification}
\lor
G_{bounded/winding\ tail\ topology}
\lor
G_{harmonic\text{-}onset\ decompactification}.
}
\]

The toroidal dipole is already removed by M17-353 and is not an additional survivor.

## 9. Audit firewall

- `V(t_m) in L3` at each time is not enough; a **uniform** backward-sequence bound is proved using the Type-I rates and normalized harmonic onset.
- Strong `L3` is not inferred from local annular compactness alone.
- The external theorem is applied only after the sequence bound is established.
- If the M5-474 ancient element were not justified in the mild class, that would be a separate restart/mildness audit gate; it is not hidden.
- No periodicity or DSS assumption is used in the Albritton--Barker Theorem 1.2 step.

## 10. DSD-theory role

The DSD heuristic contributes only the insistence that tail location and tail amplitude be normalized before importing an external Liouville theorem.  The actual argument is Hölder, harmonic multipole decay, HLS, and the published Liouville theorem.

## 11. Updated main target

The weak-critical tail no longer survives through a coefficient-compact unbounded-line harmonic exterior with bounded normalized onset.

The next internal target is therefore the geometric alternative

\[
\boxed{
G_{bounded/winding\ tail\ topology}
}
\]

and whether finite enstrophy plus CE-H line constancy can support arbitrarily far families of bounded/toroidal vortex lines without triggering rank/interface/genealogy or critical-crossing charges.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
