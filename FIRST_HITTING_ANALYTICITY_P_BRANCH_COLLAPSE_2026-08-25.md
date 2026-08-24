# First-Hitting Analyticity Collapse of the P Branch

Date: 2026-08-25

Status: **SNAPSHOT REDUCTION PROVED / INTERVAL GENEALOGY CONDITIONAL / GLOBAL REGULARITY NOT PROVED.**

This note combines the occupied palinstrophy packet gate with the repository's first-hitting analyticity corridor.

The purpose is to determine which of the three severe-P-deficit escapes

\[
\frac{d_j}{J_j^{1/2}}\to0,
\qquad
H_{d_j}\to\infty,
\qquad
K_{\omega,2;d_j}\to\infty
\]

can actually survive at a first-hitting maximum-centered snapshot.

The calculation is performed in the standard first-hitting normalization `nu=1`, natural vorticity radius `r_j=1`, and

\[
\|\Omega_j(\cdot,0)\|_\infty=1.
\]

---

## 1. Imported analytic corridor

From `ANALYTICITY_LOCAL_MASS_LEAKAGE_GATE_2026-08-20.md`, the normalized first-hitting snapshots have a fixed complex strip and a uniform amplitude bound.  Therefore, for every fixed derivative order `m`, Cauchy estimates give

\[
\boxed{
\|\nabla^m\Omega_j(\cdot,0)\|_\infty\le C_m
}
\]

with constants independent of `j`.

Choose a maximum point `y_j` so that

\[
|\Omega_j(y_j,0)|=1.
\]

The uniform first derivative bound yields a fixed radius `r_a>0` such that

\[
\boxed{
|\Omega_j(y,0)|\ge \frac12
\qquad
(y\in B_{r_a}(y_j)).
}
\]

Thus the vorticity direction

\[
\xi_j=\Omega_j/|\Omega_j|
\]

is smooth on this ball and, by quotient differentiation,

\[
\boxed{
\|\nabla\xi_j\|_{L^\infty(B_{r_a})}
+\|\nabla^2\xi_j\|_{L^\infty(B_{r_a})}
+\|\nabla^3\xi_j\|_{L^\infty(B_{r_a})}
\le C_\xi.
}
\]

**Status: PROVED from the imported analytic corridor.**

---

## 2. Curvature-active P packets cannot microcollapse

At the maximum point define the normalized transverse direction curvature

\[
b_j
:=
|P_{\xi_j^\perp}\nabla^2\xi_j(y_j,0)|.
\]

Suppose the P branch is genuinely curvature-active:

\[
b_j\ge b_0>0.
\]

The previous direction-curvature persistence lemma used

\[
m_{\xi,j}
=
\min\left\{1,\frac{b_j}{1+k_{3,j}}\right\},
\qquad
k_{3,j}=\|\nabla^3\xi_j\|_\infty
\]

in normalized coordinates.

Since analyticity gives `k_{3,j}<=C_xi`, one has

\[
\boxed{
m_{\xi,j}\ge m_0:=\min\left\{1,\frac{b_0}{1+C_\xi}\right\}>0.}
\]

Therefore the corresponding occupied P-packet radius satisfies

\[
\boxed{d_j\ge c_0>0}
\]

in the normalized variables, or in physical variables

\[
\boxed{d_j^{\rm phys}\ge c_0r_j.}
\]

Hence a maximum-centered, curvature-active P packet cannot escape through

\[
d_j^{\rm phys}/r_j\to0.
\]

If the persistence radius collapses, the event is not a pure P packet; it must already have left the fixed-order analytic corridor or moved away from the maximum-centered occupied core.

**Status: PROVED for maximum-centered first-hitting snapshots.**

---

## 3. Fixed-order vorticity-Laplacian needle is also excluded at the snapshot

The temporal escape quantity in the occupied packet gate is

\[
K_{\omega,2;d}
=
\frac{d^2}{W_*}\|\Delta\omega\|_\infty.
\]

Under the first-hitting normalization this becomes

\[
K_{\Omega,2;d_j}=d_j^2\|\Delta\Omega_j\|_\infty.
\]

For any packet with `d_j<=r_a`, the Cauchy estimate gives

\[
\boxed{
K_{\Omega,2;d_j}
\le
r_a^2C_2.
}
\]

Thus a second-vorticity-derivative temporal needle cannot diverge at the maximum-centered snapshot.

More generally, every fixed normalized derivative order is uniformly bounded at the snapshot.  Therefore an `N` escape can survive only through a failure of fixed-scale tightness, a derivative order tending to infinity, or a smaller physical scale not captured by the fixed normalized ball.

**Status: PROVED for each fixed derivative order at the first-hitting snapshot.**

---

## 4. Velocity-gradient decomposition

Write

\[
\nabla U_j=S_j+A_j,
\]

where `S_j` is the symmetric strain and `A_j` is the antisymmetric part.

Because `A_j` is algebraically determined by `Omega_j`,

\[
\boxed{
\|A_j\|_\infty\le C\|\Omega_j\|_\infty\le C.
}
\]

The only possible large normalized deformation is therefore the strain.

Represent the strain by its Biot-Savart Calderon-Zygmund kernel

\[
S_j(y)=\operatorname{p.v.}\int_{\mathbb R^3}K(z)\Omega_j(y-z)\,dz,
\]

where `K` is even, homogeneous of degree `-3`, and has zero spherical mean.

Fix a radius `0<R<r_a/4` and split

\[
S_j=S_{j,<R}+S_{j,>R}.
\]

---

## 5. Near strain is uniformly bounded by analyticity

For the principal-value near term, subtract the Taylor polynomial through first order:

\[
\Omega_j(y-z)
=
\Omega_j(y)-\nabla\Omega_j(y)z+\mathcal R_2(y,z).
\]

The constant term vanishes because the kernel has zero spherical mean, and the linear term vanishes because `K` is even while `z` is odd.

Hence

\[
|S_{j,<R}(y)|
\le
C\int_{|z|<R}|z|^{-3}|z|^2dz\,
\|\nabla^2\Omega_j\|_\infty.
\]

Since

\[
\int_{|z|<R}|z|^{-1}dz\sim R^2,
\]

we obtain

\[
\boxed{
\|S_{j,<R}\|_{L^\infty(B_{r_a/2}(y_j))}
\le
CR^2C_2.
}
\]

Thus the near-field deformation is uniformly bounded at every first-hitting snapshot.

**Status: PROVED.**

---

## 6. Snapshot deformation escape is purely far-field

Combining the antisymmetric and near-strain estimates gives, on the maximum-centered analytic core,

\[
\boxed{
\|\nabla U_j\|
\le
C_R+|S_{j,>R}|.
}
\]

For a P packet with normalized radius `d_j` bounded above and below by positive constants, its deformation quantity obeys

\[
H_{d_j}
=d_j^2\|\nabla U_j\|_\infty
\le
C_{R,d}+d_j^2\|S_{j,>R}\|_\infty.
\]

Therefore

\[
\boxed{
H_{d_j}\to\infty
\quad\Longrightarrow\quad
\|S_{j,>R}\|_\infty\to\infty.
}
\]

The severe-P-deficit strong-deformation escape is thus not an independent local mechanism.  At a maximum-centered analytic first-hitting snapshot it is a **far-strain / nonlocal-tail escape**.

**Status: PROVED at the snapshot.**

---

## 7. Collapse of the instantaneous P escape tree

For a maximum-centered, curvature-active P packet inside the first-hitting analytic corridor:

1. spatial microcollapse `d_j/r_j -> 0` is excluded;
2. fixed-order `Delta omega` needle blowup is excluded;
3. local/near velocity-gradient blowup is excluded;
4. any remaining large deformation must come from far strain.

Therefore the instantaneous severe-P-deficit tree reduces to

\[
\boxed{
P_{\rm snapshot}
\Longrightarrow
\text{occupied fixed-scale packet}
\quad\lor\quad
F_{\rm far\ strain}.
}
\]

Equivalently, `P` is not an independent terminal survivor at the snapshot once first-hitting analyticity is imposed.

**Status: PROVED in the stated maximum-centered snapshot scope.**

---

## 8. What is not yet proved in time

The analytic statement above is a snapshot statement.

To turn it into a positive return residence contribution one needs a time interval on which

- the occupied packet remains tracked,
- the fixed-order analytic/Cauchy bounds remain controlled in the moving packet,
- the far-strain alternative remains small if one wants the P packet to persist.

The repository contains first-hitting time corridors, but this note does **not** assume without verification that a previously used symbol `L_j` is exactly the forward lifespan needed here.

Thus the implication

\[
P_{\rm snapshot}+F_{\rm quiet}
\Longrightarrow
\mathfrak R_j\gtrsim r_j
\]

is still **PROVED CONDITIONAL** on an interval propagation/tracking lemma.

This distinction is essential: snapshot analyticity removes instantaneous microcollapse and fixed-order needles, but does not by itself create a macroscopic time interval.

---

## 9. Audit table

| Claim | Status |
|---|---|
| Uniform fixed-order Cauchy bounds at normalized first-hitting snapshots | **PROVED by imported analyticity corridor** |
| Fixed occupied ball around a max-vorticity point | **PROVED by imported analyticity corridor** |
| Curvature-active P packet has `d_j >= c r_j` | **PROVED** |
| Fixed-order `Delta omega` needle cannot diverge at the snapshot | **PROVED** |
| Near strain is bounded by second-derivative analyticity and kernel parity | **PROVED** |
| Large snapshot deformation on the P core must be far strain | **PROVED** |
| P is not an independent instantaneous terminal survivor | **PROVED in max-centered first-hitting scope** |
| P produces positive return residence without further time control | **NOT DERIVED unconditionally** |
| Global regularity | **UNPROVED** |

---

## 10. Updated frontier

The former four-way residual partition

\[
F\cup S\cup P\cup N
\]

has, at maximum-centered first-hitting snapshots with fixed-order analyticity, the sharper interpretation

\[
\boxed{
P\rightsquigarrow F
\quad\text{unless it pays an occupied fixed-scale packet cost.}
}
\]

Likewise, fixed-order `N` is not an independent snapshot survivor; only non-tight/finer-scale or order-to-infinity derivative escape remains.

The next calculation should therefore quantify the far-strain branch by converting it into a normalized enstrophy tax over a first-hitting epoch.