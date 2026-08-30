# DSD M5-282 — Detached Satellite Inheritance, Affine Anti-Model, and Energy-Visibility Split

Date: 2026-08-30

Parent: `DSD_M5_281_REMOTE_SATELLITE_PARABOLIC_POINT_PICKING_AND_AMBIENT_STRAIN_FORK_2026-08-30.md`

Status: **INHERITANCE AUDIT / DETACHED SATELLITES INHERIT SMOOTH LOCAL ANCIENT NAVIER--STOKES STRUCTURE AND A GLOBAL VORTICITY CAP, BUT NOT AUTOMATIC GLOBAL WEAK-`L^3`, CRITICAL MORREY, OR TERMINAL BESOV CONTROL / AN EXACT AFFINE SOLID-ROTATION ANCIENT SOLUTION IS A COUNTERMODEL TO ANY LIOUVILLE CLAIM FROM THE LOCAL DATA ALONE / FINITE-ENERGY ANCESTRY PRODUCES A NEW FIFTH-POWER VISIBILITY SCALE `R_E ~ (q E_0)^{1/5}` / SATELLITES SPLIT INTO ENERGY-VISIBLE AND ENERGY-SHIELDED GEOMETRIES / GLOBAL REGULARITY UNPROVED.**

---

## 1. Detached satellite package from M5-281

After point-picking and satellite scaling, write

\[
\widetilde u_n(z,\sigma)
=q_n^{-1}
 u\left(x_n+\frac z{q_n},
 t_n+\frac\sigma{q_n^2}\right),
\]

with

\[
q_n:=|\omega(x_n,t_n)|^{1/2}.
\]

On cylinders

\[
B_{A_n}\times[-A_n^2,0],
\qquad A_n\to\infty,
\]

M5-281 gives

\[
|\widetilde\omega_n(0,0)|=1,
\qquad
|\widetilde\omega_n|\le4.
\]

The original tracked core lies at satellite-normalized distance

\[
L_n:=q_nd_n\to\infty,
\]

where `d_n` is the physical/ancestor-frame distance from the selected satellite to the tracked main core.

On the bounded-ambient-strain subbranch, after a constant Galilean normalization and diagonal extraction one obtains a smooth ancient local limit

\[
\widetilde u_\infty
\quad\text{on}\quad
\mathbb R^3\times(-\infty,0]
\]

with

\[
\boxed{
|\widetilde\omega_\infty(0,0)|=1,
\qquad
|\widetilde\omega_\infty|\le4.
}
\]

This is the class denoted `A_detached`.

---

## 2. What is inherited without any new hypothesis

The point-picking/compactness construction gives, on every fixed backward compact cylinder:

1. the Navier--Stokes equation;
2. incompressibility;
3. smoothness after the bounded-ambient-strain bootstrap;
4. suitable/local-energy structure inherited from the smooth approximants;
5. a global-in-space vorticity cap in the diagonal limit:
   \[
   |\widetilde\omega_\infty(z,\sigma)|\le4
   \quad\text{for every fixed }(z,\sigma);
   \]
6. nontriviality at the marked point:
   \[
   |\widetilde\omega_\infty(0,0)|=1.
   \]

These are strong **local** properties.

They do not yet supply a global critical velocity class.

---

## 3. What is not automatically inherited

The following implications are not justified:

\[
|\widetilde\omega|\le4
\not\Rightarrow
\widetilde u\in L^{3,\infty},
\]

\[
|\widetilde\omega|\le4
\not\Rightarrow
\sup_R R^{-1}\int_{B_R}|\widetilde u|^2<\infty,
\]

and

\[
|\widetilde\omega|\le4
\not\Rightarrow
\widetilde u(0)\in\dot B^{-1}_{\infty,\infty}.
\]

The obstruction is the curl-free/divergence-free harmonic velocity component exposed already in M5-281.

After recentering, the main core and the old canonical tail may both escape to spatial infinity, so a global weak-critical norm of the old frame is not automatically tight in the satellite frame.

Therefore Albritton--Barker cannot be re-applied to `A_detached` from the M5-281 data alone.

---

## 4. Exact affine ancient anti-model

This failure is not merely technical.

Let `A` be a fixed nonzero antisymmetric `3 x 3` matrix and define

\[
u(x,t)=Ax.
\]

Then

\[
\nabla\cdot u=\operatorname{tr}A=0,
\qquad
\Delta u=0,
\]

and

\[
(u\cdot\nabla)u=A^2x.
\]

Since `A^2` is symmetric, choose

\[
p(x)=-\frac12 x^TA^2x.
\]

Then

\[
(u\cdot\nabla)u+\nabla p=0.
\]

Hence

\[
\boxed{
u(x,t)=Ax
}
\]

is an exact stationary ancient Navier--Stokes solution.

Its vorticity is a nonzero constant vector, so after normalizing `A` one may have

\[
|\omega(0,0)|=1,
\qquad
|\omega|\equiv1.
\]

But

\[
|u(x)|\sim|x|,
\]

so

\[
u\notin L^{3,\infty}(\mathbb R^3)
\]

and the critical terminal Besov hypothesis used in M5-276 fails.

Therefore

\[
\boxed{
\text{smooth ancient}
+\text{ bounded nonzero vorticity}
\not\Rightarrow
\text{Liouville triviality in 3D}.
}
\]

Any closure of `A_detached` must use an ancestry/growth condition not present in the local point-picked limit alone.

---

## 5. Finite-energy ancestry under satellite scaling

For this section normalize viscosity to `nu=1`; restoring viscosity is a harmless nondimensional rescaling.

Let the original Leray--Hopf kinetic-energy bound be

\[
\|u(t)\|_2^2\le E_0.
\]

Under satellite scaling,

\[
\widetilde u_n(z,\sigma)
=q_n^{-1}u(x_n+z/q_n,t_n+\sigma/q_n^2).
\]

A change of variables gives the exact global energy scaling

\[
\boxed{
\|\widetilde u_n(\sigma)\|_2^2
=q_n\|u(t_n+\sigma/q_n^2)\|_2^2
\le q_nE_0.
}
\]

For any ball, subtracting its mean only lowers `L^2` energy, hence

\[
\boxed{
\int_{B_R}
|\widetilde u_n-(\widetilde u_n)_{B_R}|^2
\le q_nE_0.
}
\]

Similarly the global energy inequality gives

\[
\int_0^{T^*}\int|\omega|^2\lesssim E_0,
\]

and therefore, on any satellite cylinder contained in the smooth physical interval,

\[
\boxed{
\int_{-R^2}^0\int_{B_R}
|\widetilde\omega_n|^2
\lesssim q_nE_0.
}
\]

Thus finite-energy ancestry is not lost completely; it is weakened by the factor `q_n`.

---

## 6. Why the fifth power appears

For the affine anti-model

\[
u(z)=Az,
\]

one has

\[
\int_{B_R}|u-(u)_{B_R}|^2
\asymp |A|^2R^5.
\]

The same `R^5` scaling occurs for a nonzero constant vorticity on the parabolic cylinder:

\[
\int_{-R^2}^0\int_{B_R}|\omega|^2
\asymp |\omega|^2R^5.
\]

Consequently the finite-energy ancestry can detect an order-one affine/constant-vorticity limit only once

\[
R^5\gg q_nE_0.
\]

Define the ancestry visibility radius

\[
\boxed{
R_{E,n}:=(q_nE_0)^{1/5}.
}
\]

The point-picking construction is geometrically allowed only up to scales small compared with

\[
L_n=q_nd_n.
\]

This produces the new dimensionless visibility ratio

\[
\boxed{
\Xi_n
:=\frac{L_n}{R_{E,n}}
=E_0^{-1/5}q_n^{4/5}d_n.
}
\]

---

## 7. Energy-visible satellite branch

Assume

\[
\boxed{\Xi_n\to\infty.}
\]

Then one may choose radii

\[
R_n\to\infty
\]

such that simultaneously

\[
R_{E,n}\ll R_n\ll L_n.
\]

The point-picking cylinder remains detached from the main core on `B_{R_n}`, while the global ancestry estimate gives

\[
R_n^{-5}
\int_{B_{R_n}}
|\widetilde u_n-(\widetilde u_n)_{B_{R_n}}|^2
\le
\frac{q_nE_0}{R_n^5}	o0.
\]

Likewise

\[
R_n^{-5}
\int_{-R_n^2}^0\int_{B_{R_n}}
|\widetilde\omega_n|^2
\to0.
\]

Therefore a detached limit carrying a nonzero **uniform affine-gradient / constant-vorticity component out to the full visible radii** is impossible on this branch.

In particular the exact solid-rotation anti-model cannot be the full large-radius ancestry profile when `Xi_n -> infinity`.

Important scope firewall: this does **not** yet prove weak-`L^3` or Liouville triviality of the detached limit. It removes the simplest linear-growth obstruction but does not classify all sublinear or intermittent ancient growth.

---

## 8. Energy-shielded satellite branch

If the energy-visible condition fails along a subsequence, then

\[
\Xi_n\le C_E.
\]

Equivalently,

\[
\boxed{
q_n^{4/5}d_n
\lesssim E_0^{1/5}
}
\]

or, after taking the fifth power,

\[
\boxed{
q_n^4d_n^5
\lesssim E_0.
}
\]

Since

\[
q_nd_n\to\infty,
\]

this is a genuine two-scale geometry: the satellite is very remote in its own natural units, yet the spatial separation is not large enough relative to the fifth-root global-energy visibility scale to expose an affine limit before the main core enters the observation region.

Call this branch

\[
\boxed{S_{shield}.}
\]

In terms of the natural satellite length

\[
\ell_n=q_n^{-1},
\]

the shield condition reads

\[
\boxed{
\ell_n
\gtrsim
E_0^{-1/4}d_n^{5/4}
}
\]

up to fixed constants.

Thus an energy-shielded remote satellite cannot have an arbitrarily tiny natural scale relative to its physical separation; it is forced into a precise `5/4` scale relation.

---

## 9. Why finite energy alone still does not close the shielded branch

The relations

\[
q_nd_n\to\infty
\]

and

\[
q_n^4d_n^5\lesssim E_0
\]

are compatible.

For example, as `d_n -> 0`, one may have a scale satisfying schematically

\[
q_n\sim d_n^{-1-\varepsilon}
\]

for a suitable small `epsilon>0`, while remaining under the `d^{-5/4}` ceiling.

Hence finite physical energy does not contradict satellite detachment.

This is another critical-scale firewall, analogous to the previously audited summability of packet energy along a Zeno cascade.

---

## 10. Updated detached frontier

The detached class is now split as

\[
\boxed{
A_{detached}
\Longrightarrow
A_{visible}
\lor
S_{shield}.
}
\]

On `A_visible`, finite-energy ancestry excludes a persistent order-one affine/constant-vorticity background across the entire detached observation scale, but a full weak-critical Liouville bridge is still missing.

On `S_shield`, every satellite must satisfy

\[
\boxed{
q_n^4d_n^5\lesssim E_0,
\qquad
q_nd_n\to\infty.
}
\]

This is the sharp new quantitative target.

The most useful next questions are:

1. whether the `5/4` shield law is compatible with the first-hitting time/space nesting and vorticity Type-I ceiling;
2. whether repeated shielded satellites can be packed along one nested genealogy without forcing dynamic turnover;
3. whether the energy-visible branch inherits enough sublinear/critical growth to invoke an existing ancient-solution Liouville theorem.

---

## 11. DSD verdict

### PROVED

- detached point-picking preserves only local ancient structure plus the vorticity mark unless additional global tightness is supplied;
- bounded-vorticity local ancient data alone admit an exact nontrivial affine Navier--Stokes anti-model;
- finite-energy ancestry scales as `q_n E_0` in the satellite frame;
- affine relative energy and constant-vorticity spacetime dissipation grow as `R^5`;
- the natural energy-visibility radius is
  \[
  R_E=(qE_0)^{1/5};
  \]
- the failure of energy visibility forces
  \[
  q^4d^5\lesssim E_0.
  \]

### NOT PROVED

- weak-`L^3` inheritance for detached satellites;
- exclusion of every sublinear-growth detached ancient solution;
- impossibility of the energy-shielded `5/4` geometry;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]