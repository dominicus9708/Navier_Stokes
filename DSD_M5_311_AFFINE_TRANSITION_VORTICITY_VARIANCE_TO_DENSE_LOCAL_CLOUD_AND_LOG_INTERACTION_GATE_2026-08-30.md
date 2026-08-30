# DSD M5-311 — Affine-Transition Vorticity Variance to Dense Local Cloud and Log-Interaction Gate

Date: 2026-08-30

Parents:
- `DSD_M5_310_AFFINE_TRANSITION_GRADIENT_VARIANCE_TO_STRAIN_OR_VORTICITY_SECONDARY_SATELLITE_FORK_2026-08-30.md`
- `DSD_M5_298_SATELLITE_LOCAL_DYADIC_INTERACTION_DENSITY_AND_AMBIENT_STRAIN_CLUSTER_GATE_2026-08-30.md`
- `DSD_M5_299_DENSE_CANCELLING_CLOUD_DYNAMIC_TENSOR_BALANCE_AND_SYMMETRY_FIREWALL_2026-08-30.md`

Status: **SECONDARY-SATELLITE STRENGTHENING / A VORTICITY-DOMINATED AFFINE BREAK WITH BOUNDED POINT-PICKED VORTICITY DOES NOT PRODUCE MERELY ONE SECONDARY POINT: IT PRODUCES ORDER `R_br^3` UNIT-SCALE STATE-SEPARATED CELLS / AFTER EXCLUDING CELL-SCALE HIGH-FREQUENCY H, A POSITIVE FRACTION BECOMES NATURALLY OCCUPIED SOLENOIDAL PACKETS / ANY SUCH POSITIVE-DENSITY 3D PACKING HAS CRITICAL DEGREE-`-3` INTERACTION DENSITY AT LEAST `c log R_br` FOR SOME/TYPICAL PACKETS, SO THE BRANCH ROUTES TO `H_sat-local` UNLESS THE ANGULAR TENSOR OUTPUT CANCels, IN WHICH CASE IT ENTERS THE M5-299 DENSE-CANCELLING CLOUD / GLOBAL REGULARITY UNPROVED.**

---

## 1. Vorticity-variance input

From M5-310, on the vorticity-dominated affine transition branch there is a radius

\[
R=R_{br}\to\infty
\]

(along a genuine detached affine sequence) such that

\[
\boxed{
R^{-3}
\int_{B_R}
|\omega-\omega_R|^2dy
\ge\delta_*>0.
}
\]

The point-picking construction gives a uniform vorticity cap on the retained satellite cylinder:

\[
\boxed{|\omega|\le C_\omega.}
\]

The affine reference vorticity `omega_R` is also order-one on the affine branch.

Hence

\[
|\omega-\omega_R|\le C_*.
\]

---

## 2. Positive-volume mismatch

Choose a fixed threshold `eta>0` sufficiently small compared with `delta_*`.

Let

\[
E_R
:=
\{y\in B_R:|\omega(y)-\omega_R|\ge\eta\}.
\]

If `|E_R|` were too small, then

\[
\int_{B_R}|\omega-\omega_R|^2
\le
\eta^2|B_R|+C_*^2|E_R|
\]

would contradict the variance floor.

Therefore

\[
\boxed{|E_R|\ge c_E R^3.}
\]

---

## 3. Unit-cell extraction

Partition `B_R` into unit cubes or fixed-shape unit balls with bounded overlap in the satellite natural units.

Since `E_R` occupies a fixed volume fraction, there are

\[
\boxed{N_R\ge c_NR^3}
\]

unit cells with a fixed local mismatch mass, after discarding a fixed fraction if necessary:

\[
\boxed{
\int_{Q_j}|\omega-\omega_R|^2dy
\ge e_\omega>0.
}
\]

The constants are independent of `R`.

---

## 4. Residual velocity packet in one cell

Subtract the affine reference velocity

\[
U_R^{aff}(y)=c_R+M_Ry.
\]

Set

\[
v=U-U_R^{aff}.
\]

Then

\[
\nabla\cdot v=0,
\qquad
\nabla\times v=\omega-\omega_R.
\]

Localize `v` on a fixed enlargement of one active unit cell and apply the same cutoff/Bogovskii construction used in the localized solenoidal phase-space trichotomy.

This produces a compact divergence-free packet `f_j` whose retained core contains the vorticity-mismatch cell.

Up to fixed cutoff losses, the local curl energy obeys

\[
\|\nabla\times f_j\|_2^2\ge c e_\omega
\]

unless the transition/correction region itself already carries a boundary/derivative H/T event.

---

## 5. Cell-scale H or natural occupancy

For a compact divergence-free unit-scale packet,

\[
\|\nabla f_j\|_2^2
=\|\nabla\times f_j\|_2^2.
\]

Define the unit-scale derivative ratio

\[
\Gamma_j
:=
\frac{\|\nabla f_j\|_2}{\|f_j\|_2}.
\]

If

\[
\Gamma_j>\Gamma_*
\]

for a positive fraction of active cells, the transition already contains a positive-density cell-scale derivative-frequency branch

\[
\boxed{H_{cell}.}
\]

On the complementary non-H cells,

\[
\Gamma_j\le\Gamma_*,
\]

and the curl lower bound gives

\[
\boxed{
\|f_j\|_2^2\ge e_*>0.
}
\]

Thus a positive fraction of the `cR^3` active cells become **genuinely occupied unit natural packets**.

Therefore, outside H/T corrections,

\[
\boxed{N_{occ}(R)\ge cR^3.}
\]

---

## 6. Critical interaction lower bound for a positive-density packing

Let the occupied cell centers be `z_1,...,z_N` inside `B_R`, with fixed minimum separation from the disjoint packet construction and

\[
N\ge cR^3.
\]

Define the scalar critical interaction potential at center `i`:

\[
\boxed{
I_i
:=
\sum_{j\ne i}
\frac1{(1+|z_i-z_j|)^3}.
}
\]

The kernel exponent equals the spatial dimension.

A positive-density separated point set in a ball of radius `R` has logarithmically divergent average critical interaction:

\[
\boxed{
\frac1N\sum_{i=1}^N I_i
\ge c\log R-C.
}
\]

One elementary proof partitions pair separations dyadically. At scale `2^k`, Cauchy counting over cubes of side `2^k` gives at least order `N2^{3k}` near-pair incidences (up to endpoint constants) for a positive-density set; multiplying by `2^{-3k}` gives order `N` per occupied logarithmic layer. Summing `k=O(1),...,O(\log R)` and dividing by `N` yields the logarithm.

Thus there exists at least one occupied packet, and in fact a positive average class, with

\[
\boxed{I_i\gtrsim\log R.}
\]

This is the discrete version of

\[
\int_1^R r^{2}r^{-3}dr\sim\log R.
\]

---

## 7. From scalar interaction mass to strain

M5-298 shows that a comparable unit packet at distance `r` contributes a leading ambient strain tensor of natural size `~r^{-3}` times its angular/moment tensor.

Hence `I_i` is the absolute interaction mass underlying the satellite-local strain descriptor

\[
\mathscr I_{loc}.
\]

If the corresponding signed tensor sum does not cancel,

\[
\left|
\sum_{j\ne i}r_{ij}^{-3}\mathcal K_{ij}
\right|
\to\infty,
\]

then

\[
\boxed{H_{sat-local}.}
\]

If the tensor output remains bounded despite

\[
I_i\gtrsim\log R\to\infty,
\]

then the branch is exactly the dense-cancelling cloud class of M5-299.

Thus

\[
\boxed{
S_{\omega-br}
\Longrightarrow
H_{cell}
\lor H_{sat-local}
\lor C_{dense,cancel}
\lor T_{localization}.
}
\]

---

## 8. Formation significance

The affine transition shell does not merely expose one new object.

On the vorticity-variance branch, the object count itself becomes volumetric:

\[
N\sim R^3.
\]

Because the Biot–Savart strain kernel is degree `-3`, this is the critical dimension in which every logarithmic distance decade contributes order one interaction mass.

Thus the affine shield naturally feeds the same dense-cancellation frontier already isolated by the cloud analysis.

---

## 9. Important firewall: tensor cancellation may still be exact

The logarithmic lower bound concerns the **absolute scalar interaction mass**.

It does not imply logarithmically growing actual strain if packet axes/moments cancel by symmetry.

Therefore

\[
I_i\to\infty
\not\Rightarrow
|S_i|\to\infty
\]

without angular information.

The correct residual branch is M5-299's dynamically cancelling tensor cloud, not an immediate contradiction.

---

## 10. Relation to parent Morrey energy

A positive-density `R^3` collection of **occupied residual packets** each carrying order-one mean-free kinetic energy would itself require order `R^3` satellite-frame energy.

The parent Morrey ceiling from M5-308 is `O(L)`.

At the first affine-break scale `R<=CL^{1/5}`, one has

\[
R^3\le C L^{3/5}\ll L,
\]

so this volumetric transition cloud is still compatible with the parent energy budget.

Thus the new cloud is not eliminated by Morrey energy alone.

---

## 11. Audit verdict

### PROVED UNDER THE VARIANCE/CAP AND LOCALIZATION ASSUMPTIONS

- positive volume fraction of vorticity mismatch;
- `~R^3` unit active cells;
- non-H active cells have fixed natural packet occupancy.

### GEOMETRIC/CRITICAL INTERACTION RESULT

Positive-density unit packing in 3D has average `r^{-3}` interaction `>=c log R`.

### ROUTING

\[
\boxed{
S_{\omega-br}
\to
H_{cell}\lor H_{sat-local}\lor C_{dense,cancel}\lor T.
}
\]

### OPEN

- dynamic exclusion/rigidity of the dense-cancelling symmetric cloud;
- strain-dominated affine breaks;
- critical detached `1/R` endpoint;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]