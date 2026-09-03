# DSD M17-006 — Great-circle winding is a real-potential complex Schrödinger nodal defect

Date: 2026-09-03
Canonical ID: **M17-006**

Status: **INTERNAL NODAL-SET REFORMULATION / ON THE GREAT-CIRCLE BRANCH, THE TWO NONZERO VORTICITY COMPONENTS COMBINE INTO A COMPLEX SCALAR `f = W_1 + i W_2` SATISFYING THE REAL-POTENTIAL ELLIPTIC EQUATION `Delta f = kappa f`. THE PHASE CURRENT IS `Im(conj(f) grad f) = rho^2 grad psi` AND IS DIVERGENCE-FREE. NONTRIVIAL DIRECTOR WINDING IS THEREFORE EXACTLY A NODAL-DEFECT / PHASE-INDEX PHENOMENON OF THIS REAL-POTENTIAL SCHRODINGER FIELD. THE WEIGHT `rho^2` MAKES SUCH DEFECTS NON-QUANTIZED IN DIRECTION ENERGY: ANALYTIC ZEROS CAN SUPPORT INTEGER WINDING WITH ARBITRARILY SMALL LOCAL WEIGHTED PHASE ENERGY. THUS A PURE ENERGY-QUANTIZATION SHORTCUT IS INVALID / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Complex scalar form

Choose the fixed great-circle plane from M17-003--005 as the `(e_1,e_2)` plane and write

\[
W=(W_1,W_2,0).
\]

Define

\[
\boxed{f:=W_1+iW_2.}
\]

Then

\[
|f|=\rho,
\qquad
f=\rho e^{i\psi}
\]

on the active set.

Because CE-H gives

\[
\Delta W=\kappa W
\]

with real scalar `kappa`, the two component equations combine into

\[
\boxed{\Delta f=\kappa f.}
\]

Thus the rank-one great-circle director is a complex solution of a real-potential scalar elliptic equation.

---

## 2. Phase current as a Wronskian current

Define

\[
\boxed{J_\psi:=\operatorname{Im}(\bar f\nabla f).}
\]

Using `f = rho e^{i psi}` gives

\[
\boxed{J_\psi=\rho^2\nabla\psi.}
\]

Its divergence is

\[
\nabla\cdot J_\psi
=\operatorname{Im}(\nabla\bar f\cdot\nabla f+\bar f\Delta f).
\]

The first term is real, and

\[
\bar f\Delta f=\kappa|f|^2
\]

is real because `kappa` is real. Hence

\[
\boxed{\nabla\cdot J_\psi=0.}
\]

This recovers the weighted harmonic phase law of M17-003/005 directly from the real-potential Schrödinger equation.

---

## 3. Nodal-set interpretation of winding

Let

\[
Z_f:=\{f=0\}=\{W=0\}
\]

within the great-circle branch.

For any closed loop `gamma` in the active complement,

\[
\boxed{
N_\gamma
:=\frac1{2\pi}\oint_\gamma d\psi
\in\mathbb Z
}
\]

is the phase winding number.

M17-005 shows that a nonzero rank-one survivor must have

\[
\boxed{N_\gamma\neq0}
\]

for at least one loop. Therefore the surviving topology is tied to components of the real-analytic nodal set `Z_f`.

---

## 4. Why ordinary phase-energy quantization fails

The direction energy is

\[
P_{dir}
=\int\rho^2|\nabla\psi|^2dy.
\]

Near a regular codimension-two nodal filament, use transverse polar distance `r` and suppose the analytic amplitude vanishes to order `m >= 1`:

\[
\rho\sim C r^m.
\]

A winding number `N != 0` gives the leading phase gradient

\[
|\nabla\psi|\sim\frac{|N|}{r}.
\]

Therefore the weighted phase-energy density behaves like

\[
\rho^2|\nabla\psi|^2
\sim
C^2N^2r^{2m-2}.
\]

Including the transverse area measure `r dr dtheta`, the energy inside a tube of radius `eps` behaves as

\[
\boxed{
E_{phase}(\varepsilon)
\sim
C_N\int_0^\varepsilon r^{2m-1}dr
=O(\varepsilon^{2m}).
}
\]

Hence

\[
\boxed{E_{phase}(\varepsilon)\to0}
\]

as `eps -> 0`, even with nonzero integer winding.

Thus there is no fixed positive local direction-energy quantum attached solely to the winding number.

---

## 5. Division-free current becomes small at the defect core

Although

\[
\nabla\psi\sim N/r
\]

is singular in phase coordinates, the physical current is

\[
J_\psi=\rho^2\nabla\psi
\sim
C^2N r^{2m-1}e_\theta,
\]

which vanishes at the nodal core for every `m >= 1`.

This is consistent with the polynomial identity

\[
(J_\psi)_i
=W_1\partial_iW_2-W_2\partial_iW_1.
\]

Therefore the topological defect is invisible to any argument that only lower-bounds the magnitude of the smooth current `J_psi` near `W=0`.

---

## 6. Elliptic nodal constraint

The topology is nevertheless not arbitrary. The complex field must simultaneously satisfy

\[
\boxed{\Delta f=\kappa f}
\]

with the self-consistent CE-H potential `kappa` and the divergence-free horizontal-vorticity constraint inherited from M17-004.

Thus the winding branch is not an arbitrary `S^1` map: it is the nodal topology of a real-analytic complex Schrödinger field coupled to the Navier--Stokes strain/eigenline system.

---

## 7. Audit consequence

The tempting implication

\[
\text{nonzero winding}
\Rightarrow
\text{fixed direction-energy cost}
\]

is false in the weighted CE-H setting.

The correct surviving problem is

\[
\boxed{
\text{persistent analytic nodal winding}
+
\Delta f=\kappa f
+
\text{materially frozen director}
+
\text{finite recurrent genealogy}.
}
\]

The next useful leverage must come from one of:

1. evolution/topology of the nodal set under the CE-H material law;
2. nodal-index constraints of the self-consistent real potential `kappa`;
3. interaction of winding defects with the finite-transverse-flux / zero-set machinery of M13--M14.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
