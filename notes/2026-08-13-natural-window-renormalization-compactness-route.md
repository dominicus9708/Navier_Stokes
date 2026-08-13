# Natural-window renormalization: from adaptive DSD tracking to a compactness-rigidity target

Date: 2026-08-13

Status: **DERIVED NATURAL-SCALE RENORMALIZATION DICTIONARY / OPEN COMPACTNESS-RIGIDITY CLOSURE**.

The current DSD-assisted route no longer needs to inspect all physical space at a fixed resolution.  It follows dangerous cores through amplification checkpoints.  Because the remaining estimates repeatedly saturate at the natural Navier--Stokes scale, the next useful representation is to renormalize every dangerous checkpoint to one fixed unit-scale window.

This note records that dictionary and the exact claim boundary.

---

## 1. Dangerous checkpoint

Let

\[
W_j=\|\omega(t_j)\|_\infty
\]

and choose a dangerous center `x_j`.  Define the natural vorticity length

\[
\boxed{
r_j=W_j^{-1/2}.
}
\]

Introduce the normalized variables

\[
\boxed{
y=\frac{x-x_j}{r_j},
\qquad
s=\frac{t-t_j}{r_j^2},
}
\]

and fields

\[
\boxed{
U_j(y,s)=r_j u(x_j+r_jy,t_j+r_j^2s),
}
\]

\[
\boxed{
P_j(y,s)=r_j^2p(x_j+r_jy,t_j+r_j^2s).
}
\]

The normalized vorticity is

\[
\boxed{
\Omega_j(y,s)
=r_j^2\omega(x_j+r_jy,t_j+r_j^2s).
}
\]

If `x_j` is chosen at a vorticity maximum at `t_j`, then

\[
\boxed{|\Omega_j(0,0)|=1.}
\]

The viscosity remains `nu`; this is the standard Navier--Stokes scaling written with `r=1/lambda`.

---

## 2. Occupancy becomes unit-scale occupancy

A physical natural core has volume

\[
|C_j|\asymp r_j^3.
\]

Under the change of variables,

\[
\boxed{
\frac{|C_j|}{r_j^3}
=|\widetilde C_j|.
}
\]

Thus the thick/sparse occupancy channel becomes an ordinary volume fraction in a fixed unit ball.

This is exactly the desired adaptive behavior: the physical support may shrink to zero, while the renormalized structural occupancy remains directly comparable from checkpoint to checkpoint.

---

## 3. Projective channels are invariant

For any nonzero scalar multiplier, the direction projector

\[
P_\xi=\xi\otimes\xi
\]

is unchanged.  Hence the normalized and physical vorticity directions agree.

Therefore all dimensionless directional channels are invariant:

\[
\boxed{
J_r,
\quad
\Pi_r,
\quad
\text{polarity fractions},
\quad
\text{axis participation matrices}.
}
\]

The natural-scale projective Campanato ratio also becomes a unit-scale condition after the appropriate power of `r_j` is factored out.

---

## 4. Palinstrophy normalization

Since

\[
\nabla_y\Omega_j
=r_j^3\nabla_x\omega,
\qquad
dy=r_j^{-3}dx,
\]

we have

\[
\boxed{
\int|\nabla_y\Omega_j|^2dy
=r_j^3
\int|\nabla_x\omega|^2dx.
}
\]

Thus the natural physical palinstrophy scale

\[
\int_{B_{r_j}}|\nabla\omega|^2dx
\sim W_j^{3/2}=r_j^{-3}
\]

becomes an order-one normalized quantity.

---

## 5. `k=2` Cauchy-defect normalization

Because

\[
\Delta_y\Omega_j
=r_j^4\Delta_x\omega
\]

and

\[
dyds=r_j^{-5}dxdt,
\]

we obtain

\[
\boxed{
\int\!\!\int
|\Delta_y\Omega_j|^2dyds
=r_j^3
\int\!\!\int
|\Delta_x\omega|^2dxdt.
}
\]

Hence the amplification-step V2 cost

\[
\int_I|\Delta\omega|^2
\gtrsim W_j^{3/2}=r_j^{-3}
\]

is exactly an order-one cost in the normalized window.

This makes the critical saturation transparent rather than hiding it behind growing powers of `W_j`.

---

## 6. Strain exposure is invariant

The normalized strain satisfies

\[
S_{U_j}=r_j^2S_u.
\]

Since

\[
ds=r_j^{-2}dt,
\]

any pathwise strain exposure is invariant:

\[
\boxed{
\int e^TS_{U_j}e\,ds
=
\int e^TS_ue\,dt.
}
\]

Therefore the Cauchy I-lane requirement

\[
\int e_z^TSe_zdt
\ge\log(bq/2)
\]

is also an order-one unit-window condition for fixed amplification ratio `q`.

The flow-gradient deformation matrices `F`, `F^{-1}` are dimensionless and likewise pass directly to the normalized description.

---

## 7. Cauchy I/V split is invariant

The Cauchy formula

\[
\omega=I+V
\]

scales by the same factor `r_j^2` in both contributions.  Hence the ratio

\[
\frac{|I|}{|\omega|},
\qquad
\frac{|V|}{|\omega|}
\]

is invariant.

Thus each normalized final core still splits into the same two causal lanes:

1. inviscid directional material stretch;
2. viscous Cauchy rewrite.

No material genealogy information is lost by renormalization.

---

## 8. Standardized DSD dangerous-window state

At each checkpoint retain a normalized state block

\[
\boxed{
\mathfrak S_j
=
(
\mathcal O_j,
J_j,
\Pi_j,
\mathcal P_j,
\mathcal I_j,
\mathcal V_{2,j},
\mathcal K_j,
\mathcal G_j,
\ldots
),
}
\]

where schematically

- `O_j`: unit-scale intense-core occupancy;
- `J_j,Pi_j`: projective multi-axis defect;
- `P_j`: normalized palinstrophy/direction-gradient cost;
- `I_j`: inviscid strain-exposure lane;
- `V2_j`: normalized second-vorticity-derivative Cauchy defect;
- `K_j`: recent material deformation;
- `G_j`: remaining geometric/sparseness gate data.

This is the renormalized version of DSD's channel-resolved moving localization.

---

## 9. Why compactness is the next *target*, not yet a theorem here

If a hypothetical singularity produces infinitely many dangerous checkpoints, then after renormalization one obtains a sequence of unit-scale Navier--Stokes windows.

A compactness-rigidity strategy would seek:

1. uniform bounds in a suitable scale-critical local function class;
2. a convergent subsequence;
3. a nontrivial limiting suitable/ancient local solution;
4. inherited residual-channel properties from the DSD state blocks;
5. a rigidity theorem showing that no such limiting object can satisfy all of them simultaneously.

However **Step 1 is not automatic** from the current finite-energy estimates.  For example, scale-invariant local energy/Morrey quantities can themselves become unbounded under blowup rescaling.

Therefore the correct next dichotomy is

\[
\boxed{
\text{critical channel unbounded}
\quad\text{or}\quad
\text{bounded normalized sequence admits a compactness target}.
}
\]

No compactness theorem is claimed without verifying the required bounds.

---

## 10. Saturation-rigidity frontier

The current estimates repeatedly return the same scale-critical sizes.  Therefore a residual singularity with bounded normalized channels must approach simultaneous near-saturation of several mechanisms:

1. natural-scale occupancy remains non-sparse;
2. projective coherence criteria remain just out of reach;
3. projective Poincare cost remains critical rather than supercritical;
4. off-axis self-stretching remains large enough to match viscosity;
5. Cauchy I/V amplification pays only order-one normalized cost;
6. derivative/projective dissipation does not produce a strict gain.

This suggests the next proof-producing question:

\[
\boxed{
\text{Can one unit-scale limiting configuration saturate all required channels simultaneously?}
}
\]

A negative answer with a quantitative gap would provide the strict gain missing from the present power-counting arguments.

Status: **OPEN COMPACTNESS / SIMULTANEOUS-SATURATION RIGIDITY PROBLEM**.
