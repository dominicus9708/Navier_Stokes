# DSD M5-433 — Fifth-root remote saturation forces a terminal kinetic-energy atom

Date: 2026-08-31

Status: **REMOTE-SOURCE RIGIDITY SPLIT / A FIXED-FRACTION STRAIN PAYER LOCATED AT A FIXED FRACTION OF THE MAXIMAL FIFTH-ROOT ENERGY-VISIBILITY RADIUS MUST CARRY A FIXED POSITIVE AMOUNT OF KINETIC ENERGY / AS THE FIRST-HITTING RADII SHRINK AND CENTERS NEST, SUCH SOURCE ANNULI COLLAPSE TO THE SINGULAR POINT WHILE RETAINING POSITIVE ENERGY, FORCING A POINT ATOM IN THE TERMINAL KINETIC-ENERGY MEASURE / CONSEQUENTLY THE NON-ATOMIC REMOTE BRANCH MUST BE STRICTLY SUB-SATURATED: `R_j=o(r_j^{4/5})` / THIS EXTENDS THE ENERGY-ATOM ROUTE BEYOND THE AFFINE-SHIELD MODEL, BUT THE ATOM BRANCH STILL RETURNS TO THE EXISTING ATOMIC-RIGIDITY/CRITICAL-THROUGHPUT FRONTIER RATHER THAN CLOSING GLOBAL REGULARITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let

\[
r_j=\sqrt{\nu/W_j}
\]

be the first-hitting natural scale.

Assume the center-nesting corridor so that

\[
X_j\to X_*,
\qquad
|X_j-X_*|\lesssim r_j.
\]

Suppose a fixed fraction of the target natural strain

\[
S_j^{nat}\asymp\frac{\nu}{r_j^2}
\]

is supplied by a source region at physical distance/radius

\[
R_j\gg r_j
\]

from the current core.

For concreteness let the source be contained in a dyadic-thickness annulus

\[
A_j
:=
\{c_1R_j<|x-X_j|<c_2R_j\}
\]

with fixed `0<c1<c2<infinity`.

The argument applies to any comparable source region for which the far-kernel bound below holds with fixed constants.

---

## 2. Local far-energy strain estimate

The far strain contribution can be integrated by parts from vorticity to velocity.

On a region at distance comparable to `R_j`, the resulting velocity kernel has size `R_j^{-4}` and `L2` norm comparable to

\[
R_j^{-5/2}.
\]

Therefore the source contribution obeys

\[
\boxed{
|S_{A_j}(X_j)|
\lesssim
R_j^{-5/2}
\|u(t_j)\|_{L^2(A_j^+)}
}
\]

for a fixed enlarged annulus `A_j^+`.

Assume this source carries a fixed fraction `theta_s>0` of the natural target strain:

\[
|S_{A_j}(X_j)|
\ge
\theta_s\frac{\nu}{r_j^2}.
\]

Then

\[
\boxed{
\|u(t_j)\|_{L^2(A_j^+)}
\gtrsim
\nu R_j^{5/2}r_j^{-2}.
}
\]

Squaring,

\[
\boxed{
\int_{A_j^+}|u(x,t_j)|^2dx
\gtrsim
\nu^2\frac{R_j^5}{r_j^4}.
}
\]

This lower bound uses only the actual source contribution and finite-energy far-kernel geometry; no affine ansatz is imposed.

---

## 3. Fifth-root normalization

Write

\[
\boxed{
R_j
=a_j r_j^{4/5}.
}
\]

Then

\[
\frac{R_j^5}{r_j^4}
=a_j^5.
\]

Hence the source-energy lower bound becomes

\[
\boxed{
\int_{A_j^+}|u(x,t_j)|^2dx
\gtrsim
\nu^2a_j^5.
}
\]

Thus the dimensionless saturation parameter `a_j` directly measures the fifth root of the energy forced into the remote source region.

---

## 4. Saturated branch gives fixed positive energy

Suppose there is an infinite subsequence such that

\[
\boxed{a_j\ge a_0>0.}
\]

Then

\[
\boxed{
\int_{A_j^+}|u(x,t_j)|^2dx
\ge e_*>0,
\qquad
e_*\asymp\nu^2a_0^5.
}
\]

Because

\[
r_j\to0,
\]

we also have

\[
R_j\asymp r_j^{4/5}\to0.
\]

Moreover

\[
|X_j-X_*|\lesssim r_j=o(R_j)
\]

on the remote fifth-root branch.

Therefore for some fixed `C`,

\[
A_j^+
\subset
B_{CR_j}(X_*)
\]

for all sufficiently late `j`.

Hence

\[
\boxed{
\int_{B_{CR_j}(X_*)}|u(x,t_j)|^2dx
\ge e_*>0,
\qquad
CR_j\to0.
}
\]

---

## 5. Terminal energy measure acquires an atom

The kinetic-energy measures

\[
\mu_t(dx)=|u(x,t)|^2dx
\]

have uniformly bounded total mass by the energy inequality.

Along a sequence `t_j -> T_*`, extract a weak-* limit in the space of finite Radon measures:

\[
\mu_{t_j}\stackrel{*}{\rightharpoonup}\mu_*.
\]

Since balls centered at `X_*` with radii tending to zero carry at least `e_*`, the Portmanteau/outer-regularity argument gives

\[
\boxed{
\mu_*(\{X_*\})
\ge e_*>0.
}
\]

Thus the terminal kinetic-energy measure contains a point atom.

Symbolically,

\[
\boxed{
\text{fifth-root saturated remote source}
\Longrightarrow
A_{energy\ atom}.
}
\]

---

## 6. Relation to the existing atom machinery

The repository already contains a separate atom/rigidity program, including the Huang-based atomic full-tail route and the later reconsolidation of atom/satellite/affine branches into critical strain/throughput or dynamic escape.

The present result does not reproduce those theorems.

Its contribution is upstream:

\[
\boxed{
\text{general fixed-fraction remote strain source at fifth-root saturation}
\Longrightarrow
\text{terminal energy atom},
}
\]

without assuming the source is affine or ellipsoidal.

The atom branch should therefore be routed into the existing atomic-rigidity ledger rather than carried as a new remote-source terminal.

---

## 7. Non-atomic branch must be sub-saturated

Suppose instead the terminal kinetic-energy measure has no atom at the singular point along the retained branch.

Then for every sequence of shrinking balls

\[
R\to0,
\]

the concentrated energy tends to zero.

The lower bound

\[
\int_{A_j^+}|u|^2
\gtrsim
\nu^2a_j^5
\]

therefore forces

\[
\boxed{a_j\to0.}
\]

Equivalently,

\[
\boxed{
R_j=o(r_j^{4/5}).
}
\]

Thus the non-atomic remote source must lie strictly inside the maximal fifth-root shield scale.

---

## 8. Energy-modulus refinement

Define the local terminal/preterminal energy modulus around the singular point

\[
\mathcal E(\rho)
:=
\sup_{t\text{ sufficiently close to }T_*}
\int_{B_\rho(X_*)}|u(x,t)|^2dx
\]

on the selected corridor.

The source lower bound gives schematically

\[
\nu^2\frac{R_j^5}{r_j^4}
\lesssim
\mathcal E(CR_j).
\]

Hence

\[
\boxed{
R_j
\lesssim
r_j^{4/5}
\left(
\frac{\mathcal E(CR_j)}{\nu^2}
\right)^{1/5}.
}
\]

If the branch is non-atomic, the modulus factor tends to zero.

No quantitative power improvement follows without a quantitative decay rate for `mathcal E`, but the little-o gain is rigorous.

---

## 9. Relation to M5-351

M5-351 studied a saturated **affine shield** of radius

\[
d_j\asymp r_j^{4/5}
\]

and found fixed-fraction material turnover because the available shield volume contracts.

The present note shows why the same fifth-root radius is special without the affine model:

- it is exactly the radius at which a fixed-fraction far strain payer requires order-one physical kinetic energy;
- therefore saturation at this radius automatically creates an energy atom as the radius collapses.

Thus the fifth-root scale has both a material-volume interpretation in the affine benchmark and a general energy-concentration interpretation in the far-kernel estimate.

---

## 10. Firewall

This result does not say that every energy atom is impossible.

It only routes the saturated remote-source branch into the existing atom machinery.

It also does not give a power-law improvement over `r^(4/5)` in the non-atomic case; only

\[
R_j=o(r_j^{4/5})
\]

follows without an independent energy-modulus rate.

Do not assume the annular source contains all of the solution energy; the proof uses only the fixed positive amount forced by the strain contribution.

---

## 11. Updated remote frontier

For a fixed-fraction remote strain payer,

\[
\boxed{
\text{remote source}
\Longrightarrow
\begin{cases}
A_{energy\ atom},
& R_j\gtrsim c r_j^{4/5},\\[1mm]
R_j=o(r_j^{4/5}),
& \text{non-atomic branch}.
\end{cases}
}
\]

The first enters the existing atom/critical-throughput route.

The second is the genuinely surviving non-atomic remote geometry.

---

## 12. Audit verdict

### NEW GENERAL BRIDGE

\[
\boxed{
R_j\sim r_j^{4/5}
\text{ fixed-fraction remote strain}
\Longrightarrow
\text{terminal kinetic-energy atom}.
}
\]

### NON-ATOMIC CONSEQUENCE

\[
\boxed{R_j=o(r_j^{4/5}).}
\]

### STILL OPEN

Sub-fifth-root non-atomic remote source concentration and the atomic branch's final critical-throughput closure.

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
