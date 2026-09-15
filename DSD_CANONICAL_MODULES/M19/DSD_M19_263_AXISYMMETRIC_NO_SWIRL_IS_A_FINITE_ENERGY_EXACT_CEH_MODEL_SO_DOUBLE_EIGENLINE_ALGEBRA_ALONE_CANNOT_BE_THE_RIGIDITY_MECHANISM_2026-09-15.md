# DSD M19-263 — Axisymmetric no-swirl is a finite-energy exact CE-H model, so double-eigenline algebra alone cannot be the rigidity mechanism

Date: 2026-09-15  
Canonical ID: **M19-263**  
Status: **ACTIVE STRUCTURAL FIREWALL / FINITE-ENERGY EXACT-CEH REGULAR MODEL / M5-599 RIGIDITY SCOPE CORRECTION / LOW-FREQUENCY-ANCIENT STRUCTURE PROMOTED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M5-599 promoted the CE-H carrier conditions to the global ancient double-eigenline system

\[
\omega\times S\omega=0,
\qquad
\omega\times\Delta\omega=0,
\]

or, on \(\{\omega\neq0\}\),

\[
S\omega=\sigma\omega,
\qquad
\Delta\omega=\kappa\omega.
\]

Its original firewall correctly warned that this algebra is not itself a contradiction and cited Burgers-type stretched vortices as local/exact aligned examples, while noting that the classical Burgers background strain is not in the present finite-energy class.

The present audit strengthens that firewall substantially:

\[
\boxed{
\text{nonzero finite-energy globally regular solutions can satisfy the exact CE-H algebra.}
}
\]

The model class is axisymmetric Navier--Stokes flow without swirl.

---

## 2. Axisymmetric no-swirl kinematics

Use cylindrical coordinates \((r,\theta,z)\) with orthonormal frame

\[
e_r,\qquad e_\theta,\qquad e_z.
\]

Let

\[
u
=u_r(r,z,t)e_r+u_z(r,z,t)e_z,
\qquad
u_\theta=0,
\qquad
\partial_\theta=0.
\]

The vorticity is purely azimuthal:

\[
\boxed{
\omega=\omega_\theta(r,z,t)e_\theta,
}
\]

with

\[
\omega_\theta=\partial_z u_r-\partial_r u_z
\]

up to the fixed curl sign convention.

---

## 3. Exact strain eigenline

For an axisymmetric no-swirl velocity field, the cylindrical strain components coupling the azimuthal direction to the meridional plane vanish:

\[
S_{r\theta}=0,
\qquad
S_{z\theta}=0.
\]

The azimuthal diagonal component is

\[
S_{\theta\theta}=\frac{u_r}{r}.
\]

Therefore

\[
\boxed{
S e_\theta=\frac{u_r}{r}e_\theta,
}
\]

and hence

\[
\boxed{
S\omega=\frac{u_r}{r}\,\omega.
}
\]

Thus the CE-H strain-alignment identity holds exactly:

\[
\boxed{
\omega\times S\omega=0.
}
\]

No singularity or near-singularity assumption is involved.

---

## 4. Exact Laplacian eigenline

For an axisymmetric azimuthal vector field

\[
\omega=\omega_\theta(r,z,t)e_\theta,
\]

the vector Laplacian is again purely azimuthal:

\[
\boxed{
\Delta\omega
=
\left(
\partial_{rr}
+\frac1r\partial_r
+\partial_{zz}
-\frac1{r^2}
\right)
\omega_\theta\,e_\theta.
}
\]

Therefore

\[
\boxed{
\omega\times\Delta\omega=0
}
\]

everywhere.

On the nonzero-vorticity set one may define

\[
\boxed{
\kappa
=
\frac{
(\partial_{rr}+r^{-1}\partial_r+\partial_{zz}-r^{-2})\omega_\theta
}{\omega_\theta}
}
\]

and obtain

\[
\boxed{
\Delta\omega=\kappa\omega.
}
\]

At vorticity zeros the quotient need not be defined, but the cross-product CE-H identity remains smooth and exact.

---

## 5. Exact longitudinal constancy of kappa

On \(\{\omega\neq0\}\), the vorticity direction is

\[
\xi=\operatorname{sgn}(\omega_\theta)e_\theta.
\]

The coefficient \(\kappa\) is axisymmetric, so

\[
\partial_\theta\kappa=0.
\]

Hence

\[
\boxed{
D_\xi\kappa
=
\xi\cdot\nabla\kappa
=0.
}
\]

Thus the M17-313 divergence-free CE-H correction is also exactly realized in this regular model.

---

## 6. This model can be finite-energy and nonzero

Choose smooth nonzero divergence-free axisymmetric no-swirl initial data with finite kinetic energy, for example a smooth rapidly decaying or compactly supported meridional stream-function construction.

Then

\[
u_0\in L^2(\mathbb R^3)
\]

and the corresponding vorticity is nonzero while retaining the exact identities above.

Classical work of Ladyzhenskaya and independently Ukhovskii--Yudovich established global regularity for three-dimensional axisymmetric Navier--Stokes flows without swirl.

Representative literature record:

- O. A. Ladyzhenskaya, *Unique global solvability of the three-dimensional Cauchy problem for the Navier--Stokes equations in the presence of axial symmetry* (1968).
- M. R. Ukhovskii and V. I. Yudovich, *Axially symmetric flows of ideal and viscous fluids filling the whole space* (1968).

Modern surveys and regularity papers continue to cite these as the classical no-swirl global-regularity results.

Therefore there exist nonzero, finite-energy, globally regular Navier--Stokes evolutions satisfying the exact CE-H double-eigenline geometry.

---

## 7. Strong correction to the M5-599 firewall

The earlier safe statement was

\[
\text{CE-H alignment itself is not a contradiction.}
\]

The stronger canonical statement is now

\[
\boxed{
\text{exact global CE-H double-eigenline algebra}
\not\Rightarrow
\text{zero solution, infinite energy, or singular behavior}.
}
\]

In particular, it is no longer sufficient to distinguish the present branch from Burgers vortices merely by invoking finite energy.

Finite-energy exact CE-H examples already exist inside the classical regular axisymmetric no-swirl class.

M5-599 remains valid as a **structural reduction** when its analyticity dependencies hold; it must not be interpreted as a near-Liouville theorem by itself.

---

## 8. What remains special about the DSD ancient branch

The extracted M5-474--477 ancient element has additional properties not shared by an arbitrary forward regular axisymmetric no-swirl solution:

1. nontrivial first-hitting normalization;
2. complete ancient-time existence on \(( -\infty,0]\);
3. backward Type-I decay
   \[
   \|V(\tau)\|_\infty\lesssim(-\tau)^{-1/2},
   \]
   \[
   \|\Omega(\tau)\|_\infty\lesssim(-\tau)^{-1},
   \qquad
   \|\Omega(\tau)\|_2^2\lesssim(-\tau)^{-1/2};
   \]
4. finite total palinstrophy and raw-H2 resources;
5. recurrent/first-hitting ancestry inherited from the hypothetical singularity corridor;
6. possible critical-tail/low-frequency structure at similarity infinity.

Therefore any CE-H rigidity theorem relevant to the singularity problem must use some of these additional ancient/critical structures.

---

## 9. Low-frequency firewall becomes central

For a whole-space divergence-free field,

\[
\boxed{
\|V\|_2^2
=
\|\Omega\|_{\dot H^{-1}}^2.
}
\]

M5-475 proves decay of

\[
\|\Omega(\tau)\|_2,
\]

but this does not imply decay of

\[
\|\Omega(\tau)\|_{\dot H^{-1}}
\]

because energy may migrate toward arbitrarily low frequencies.

This is the same low-frequency firewall already identified in M17/M18.

Thus CE-H cannot be closed merely by combining its high-frequency elliptic identities with finite enstrophy.

---

## 10. Finite kinetic energy plus backward energy extinction would close immediately

Suppose, in addition to the current ancient hypotheses, one could prove

\[
V(\tau)\in L^2(\mathbb R^3)
\]

and

\[
\boxed{
\|V(\tau)\|_2\to0
\qquad(\tau\to-\infty).
}
\]

For a smooth finite-energy ancient solution, the energy equality gives for \(s<t\le0\)

\[
\|V(t)\|_2^2
+2\int_s^t\|\nabla V(\tau)\|_2^2d\tau
=
\|V(s)\|_2^2.
\]

Letting \(s\to-\infty\) would imply

\[
\boxed{V(t)\equiv0,}
\]

contradicting the nontrivial first-hitting mark.

Hence a genuine low-frequency extinction theorem would close the ancient branch without requiring physical H3 transfer.

---

## 11. But finite enstrophy decay does not supply kinetic-energy extinction

The current facts

\[
\|\Omega(\tau)\|_2\to0,
\qquad
\|\Omega(\tau)\|_\infty\to0
\]

control high and medium frequencies but do not control

\[
\int_{|\xi|\ll1}
\frac{|\widehat\Omega(\xi,\tau)|^2}{|\xi|^2}\,d\xi.
\]

Therefore

\[
\boxed{
\Omega\to0\text{ in }L^2
\not\Rightarrow
V\to0\text{ in }L^2.
}
\]

This is not a technicality; it is the exact place where an ancient solution can retain kinetic energy while its vorticity moves to larger and larger spatial scales backward in time.

---

## 12. Revised CE-H rigidity target

The next CE-H target should not be

\[
\text{double-eigenline algebra}\Rightarrow0.
\]

It should instead ask whether the **double-eigenline algebra plus the special ancient first-hitting class** prevents low-frequency decompactification.

Define

\[
\boxed{
\mathcal T_{CEH}^{LF}:
\text{CE-H + ancient Type-I/first-hitting structure controls }
\|\Omega\|_{\dot H^{-1}}
\text{ strongly enough to force backward kinetic-energy extinction.}
}
\]

Possible routes include:

1. a moment/cancellation identity forced by CE-H;
2. a quantitative lower bound on the characteristic coefficient scale preventing migration to \(|\xi|\to0\);
3. a critical-tail contradiction if the spatial scale expands indefinitely backward;
4. an axisymmetric-like classification plus ancient finite-energy rigidity;
5. a direct low-frequency estimate from the material/genealogy equations.

---

## 13. Permanent firewalls after M19-263

\[
\boxed{
\omega\times S\omega=0,
\quad
\omega\times\Delta\omega=0
\not\Rightarrow
\omega=0.
}
\]

\[
\boxed{
\text{exact CE-H}
\not\Rightarrow
\text{infinite energy}.
}
\]

\[
\boxed{
\text{exact CE-H}
\not\Rightarrow
\text{singular or near-singular dynamics}.
}
\]

\[
\boxed{
\text{finite enstrophy/high-derivative control}
\not\Rightarrow
\text{low-frequency kinetic-energy control}.
}
\]

\[
\boxed{
\text{CE-H rigidity, if true for the DSD branch, must use ancient/critical/recurrence information beyond the double-eigenline algebra.}
}
\]

---

## 14. Immediate next target

Audit \(\mathcal T_{CEH}^{LF}\).

The first question is whether

\[
\Delta\Omega=\kappa\Omega,
\qquad
D_\xi\kappa=0,
\]

together with the M5-475 backward decay can force a lower bound on an intrinsic inverse length scale, or instead whether a regular CE-H field can let its entire coefficient/geometry scale drift to zero frequency while preserving the first-hitting normalization after rescaling.

If low-frequency migration remains possible, it should be typed explicitly as the R-critical escape rather than hidden inside CE-H.

Global 3D Navier--Stokes regularity remains unproved.
