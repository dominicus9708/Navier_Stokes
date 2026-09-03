# DSD M5-616 — Nodal audit and quantitative generalized kappa-force dipole extraction

Date: 2026-09-03

Status: **CORRECTION + DIPOLE EXTRACTION / THE SCALAR KAPPA IS NATURALLY DEFINED ONLY ON THE ACTIVE SET `W!=0`; THE ANALYTIC IDENTITY `W x Delta W=0` DOES NOT BY ITSELF ASSIGN A FINITE KAPPA AT A VORTICITY ZERO / HOWEVER THE STRESS TENSOR CAN BE WRITTEN GLOBALLY USING THE SMOOTH PRODUCT `W·Delta W`, SO `F_kappa:=-2 div T` IS A GLOBAL SMOOTH GENERALIZED FORCE AND AGREES WITH `|W|^2 nabla kappa` OFF THE NODAL SET / ITS ZERO TOTAL FORCE AND POSITIVE VIRIAL REMAIN EXACT / A UNIFORM L1 CAP PLUS FINITE-CORE LOCALIZATION FORCES A QUANTITATIVE SEPARATED POSITIVE/NEGATIVE DIPOLE IN AT LEAST ONE CARTESIAN PROJECTION / THIS DOES NOT YET IMPLY THAT EACH LOBE IS A FIXED-FLUX VORTICITY PACKET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Nodal-set firewall

M5-599 gives the analytic vector alignment

\[
W\times\Delta W=0
\]

globally.

On the active set

\[
\Omega_W:=\{W\neq0\},
\]

define

\[
\kappa
:=
\frac{W\cdot\Delta W}{|W|^2},
\]

so

\[
\Delta W=\kappa W
\]

on `Omega_W`.

At a point with `W=0`, the cross-product identity is automatic and does not force `Delta W=0` or a finite scalar `kappa`.

Therefore `kappa` should not be silently treated as an everywhere-smooth scalar quotient.

For a nontrivial real-analytic vector field, the common zero set has three-dimensional measure zero unless the field vanishes identically, so all `L2` identities involving the products `kappa |W|^2` or `kappa^2|W|^2` remain valid almost everywhere.

---

## 2. Global stress tensor without dividing by |W|

Rewrite the M5-615 tensor as

\[
\boxed{
\mathbb T_{ij}
=
\partial_iW\cdot\partial_jW
-
\frac12
\left(
|\nabla W|^2+W\cdot\Delta W
\right)\delta_{ij}.
}
\]

This expression uses only the smooth analytic field `W` and its derivatives.

Hence `T` is globally smooth, including across the nodal set.

Define the global generalized force

\[
\boxed{
\mathcal F_\kappa
:=-2\nabla\cdot\mathbb T.
}
\]

On `Omega_W`, the CE-H eigenvalue equation gives

\[
\boxed{
\mathcal F_\kappa
=|W|^2\nabla\kappa.
}
\]

Thus this is the canonical smooth extension of the active-set kappa force.

---

## 3. Exact global moments survive the audit

The terminal-tail decay gives zero traction at infinity, hence

\[
\boxed{
\int_{\mathbb R^3}\mathcal F_\kappa dy=0.
}
\]

The stress trace calculation is unchanged, so

\[
\boxed{
\int_{\mathbb R^3}y\cdot\mathcal F_\kappa dy
=2P>0.
}
\]

Likewise symmetry of `T` gives zero total torque.

Thus the force/virial conclusions of M5-615 are retained, but the globally correct object is `mathcal F_kappa`, not an assumed smooth quotient field at zeros.

---

## 4. Uniform L1 cap

Because

\[
\mathcal F_\kappa=-2\nabla\cdot\mathbb T
\]

and `T` is quadratic in `W,nabla W,Delta W`, all-order Sobolev bounds give a uniform `L1` estimate of schematic form

\[
\boxed{
\|\mathcal F_\kappa\|_1
\le M_F<\infty.
}
\]

For example, after expanding `div T`, every term is controlled by products such as

\[
\|\nabla W\|_2\|\nabla^2W\|_2,
\qquad
\|W\|_2\|\nabla\Delta W\|_2,
\qquad
\|\nabla W\|_2\|\Delta W\|_2,
\]

which are uniformly bounded on the compact hard component.

---

## 5. Finite-core localization of the force moments

The terminal tail has

\[
W=O(r^{-2}),
\qquad
\nabla W=O(r^{-3}),
\qquad
\nabla^2W=O(r^{-4}),
\]

so

\[
\mathcal F_\kappa
=O(r^{-7})
\]

at the level needed for its zeroth and first moments.

Choose a fixed `R_F` so large that the exterior contributions to

\[
\int\mathcal F_\kappa
\]

and

\[
\int y\cdot\mathcal F_\kappa
\]

are smaller than a prescribed fraction of the compact lower virial `2p0`.

Thus the zero-force/positive-virial dipole is effectively contained in one fixed finite core.

---

## 6. Choose a Cartesian projection with positive first moment

Let

\[
F_j:=(\mathcal F_\kappa)_j.
\]

Since

\[
\sum_{j=1}^3\int y_jF_jdy
=2P\ge2p_0,
\]

there exists at least one coordinate `j_*` with

\[
\boxed{
\int y_{j_*}F_{j_*}dy
\ge\frac{2p_0}{3}.
}
\]

Also

\[
\boxed{
\int F_{j_*}dy=0.
}
\]

---

## 7. Positive and negative force masses

Write

\[
F_{j_*}=F_+-F_-,
\qquad
F_\pm\ge0.
\]

The zero-mean law gives

\[
\int F_+=\int F_-=:m_F.
\]

The `L1` cap gives

\[
m_F\le M_F/2.
\]

After choosing `R_F` so the first-moment tail is small, the positive first moment inside the finite core gives a positive lower bound

\[
\boxed{m_F\ge m_0>0}
\]

because `|y_{j_*}|<=R_F` there.

---

## 8. Barycenter separation

Define the one-dimensional barycenters

\[
a_+
:=
\frac1{m_F}
\int y_{j_*}F_+dy,
\]

\[
a_-
:=
\frac1{m_F}
\int y_{j_*}F_-dy.
\]

Then

\[
\int y_{j_*}F_{j_*}dy
=m_F(a_+-a_-).
\]

Hence

\[
\boxed{
a_+-a_-
\ge
\frac{2p_0/3}{m_F}
\ge
\frac{4p_0}{3M_F}
=:d_F>0.
}
\]

Therefore the positive and negative projected force populations have a fixed nonzero barycentric separation.

In particular their supports cannot collapse onto one spatial point or one vanishingly small common region.

---

## 9. Coherent force lobes

Compact all-order regularity gives uniform local continuity of the smooth generalized force field.

Since each sign population has fixed `L1` mass in a fixed finite volume, one can extract points of fixed positive/negative amplitude and thicken them to fixed small neighborhoods, modulo a further finite partition if needed.

Thus the hard component contains a recurrent generalized force dipole with two sign-opposed lobes separated at a fixed normalized distance.

---

## 10. Genealogical firewall

A force lobe is not automatically a fixed-flux vorticity packet.

Near the analytic vorticity nodal set, `mathcal F_kappa` may be supported by derivative geometry even when `|W|` is small.

Therefore the implication

\[
\text{force lobe}
\Longrightarrow
\text{material flux lineage}
\]

is not yet valid.

The correct next split is

\[
\boxed{
\text{force lobe}
\Longrightarrow
\text{active-vorticity lobe}
\lor
\text{derivative/nodal stress lobe}.
}
\]

The first may enter the finite flux genealogy; the second must be tested against the all-order compact derivative hierarchy and unique-continuation/nodal geometry.

---

## 11. Updated frontier

The CE-H hard core now contains a mandatory finite-scale dipole architecture in the generalized kappa-force, in addition to the persistent dual-flux geometry extracted earlier.

The next high-value question is whether these two dual structures must overlap or whether the kappa-force dipole can be supported entirely by low-vorticity/nodal derivative regions.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
