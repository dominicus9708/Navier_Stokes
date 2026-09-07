# DSD M17-308 — Record blow-down scaling atlas identifies the only lossless cross-generation currencies

Date: 2026-09-07  
Canonical ID: **M17-308**

Status: **CROSS-GENERATION SCALING CLASSIFICATION / M17-307 SHOWS THAT SECOND-GENERATION VORTICITY PALINSTROPHY MUST BE CHARGED TO THE FIRST ANCIENT ELEMENT WITH AN EXPLICIT `R_m^-1` WEIGHT. THE PRESENT MODULE PROVES THAT THIS LOSS IS NOT AN ARTIFACT OF THE CHARGING ARGUMENT: IT IS THE EXACT NAVIER--STOKES SCALING EXPONENT OF THE `L_t^2 \dot W_x^{1,2}` VORTICITY QUANTITY. FOR GENERAL VORTICITY DERIVATIVE NORMS THE BLOW-DOWN EXPONENT IS `q(2+k-3/p)-2`. ONLY EXPONENT-ZERO CURRENCIES CAN CROSS THE M5-478 RECORD BLOW-DOWN WITHOUT A POWER OF `R_m`. THIS SELECTS, AMONG OTHERS, `L_t^2L_x^3` VORTICITY/STRAIN, `L_t^1L_x^infinity` VORTICITY, STATIC `L_x^(3/2)` VORTICITY OR INVERSE-LENGTH-SQUARED COEFFICIENTS, AND THE VELOCITY SERRIN/ENDPOINT CLASS INCLUDING STATIC `L_x^3`. THE SCALE-INVARIANT WEIGHTED PALINSTROPHY `int sqrt(-t)||grad Omega||_2^2 dt` IS ALSO IDENTIFIED, BUT M5-477 DOES NOT MAKE IT GLOBALLY FINITE. THEREFORE FURTHER PROGRESS CANNOT REMOVE THE M17-307 DEFICIT BY REBOOKKEEPING PALINSTROPHY; IT MUST USE A CRITICAL RIGIDITY/TRANSFER THEOREM, STRICT SCALE DESCENT, OR ANOTHER STRUCTURE SPECIAL TO CE-H. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Record blow-down

Use the M5-478 second-generation scaling

\[
\boxed{
V_R(y,s)=R V(Ry,R^2s),
\qquad
\Omega_R(y,s)=R^2\Omega(Ry,R^2s).
}
\]

For an integer spatial derivative order `k>=0`,

\[
D_y^k\Omega_R(y,s)
=R^{2+k}(D_x^k\Omega)(Ry,R^2s).
\]

Hence

\[
\boxed{
\|D^k\Omega_R(s)\|_{L^p_y}
=R^{2+k-3/p}
\|D^k\Omega(R^2s)\|_{L^p_x}.
}
\]

Let `I subset (-infinity,0)` be a fixed cell-time interval and put `J_R=R^2I`. Since `ds=R^-2 dt`, for any finite `q>0`,

\[
\boxed{
\int_I
\|D^k\Omega_R(s)\|_{L^p}^q ds
=
R^{\alpha_\Omega(k,p,q)}
\int_{J_R}
\|D^k\Omega(t)\|_{L^p}^qdt,
}
\]

where

\[
\boxed{
\alpha_\Omega(k,p,q)
:=q\left(2+k-\frac3p\right)-2.
}
\]

This is the exact record-generation scaling exponent.

---

## 2. Criticality trichotomy

The sign of `alpha_Omega` gives three qualitatively different ancestry maps.

### Subcritical descendant quantity

If

\[
\alpha_\Omega<0,
\]

then the descendant normalized quantity is smaller by a power of `R` than the corresponding ancestor quantity.

### Critical quantity

If

\[
\boxed{\alpha_\Omega=0,}
\]

then the quantity crosses the record blow-down with **no record-scale power**.

### Supercritical descendant quantity

If

\[
\alpha_\Omega>0,
\]

then an order-one descendant charge maps back to an ancestor charge smaller by

\[
R^{-\alpha_\Omega}.
\]

This is exactly the mechanism exposed by M17-307.

---

## 3. Palinstrophy necessarily has exponent +1

For vorticity palinstrophy,

\[
k=1,
\qquad p=2,
\qquad q=2.
\]

Therefore

\[
\alpha_\Omega(1,2,2)
=2\left(3-\frac32\right)-2
=1.
\]

Thus

\[
\boxed{
\int_I\|\nabla\Omega_R\|_2^2ds
=R
\int_{J_R}\|\nabla\Omega\|_2^2dt.
}
\]

Consequently

\[
\boxed{
R^{-1}
\int_I\|\nabla\Omega_R\|_2^2ds
=
\int_{J_R}\|\nabla\Omega\|_2^2dt.
}
\]

The `R^-1` factor of M17-307 is therefore **dimensionally forced**.

No rearrangement of the same unweighted palinstrophy ledger can remove it.

---

## 4. Other useful vorticity exponents

### Spacetime enstrophy

For

\[
k=0,\quad p=2,\quad q=2,
\]

\[
\alpha_\Omega=-1.
\]

Hence

\[
\int_I\|\Omega_R\|_2^2ds
=R^{-1}
\int_{J_R}\|\Omega\|_2^2dt.
\]

### Critical vorticity `L_t^2L_x^3`

For

\[
k=0,\quad p=3,\quad q=2,
\]

\[
\boxed{\alpha_\Omega=0.}
\]

Thus

\[
\boxed{
\int_I\|\Omega_R\|_3^2ds
=
\int_{J_R}\|\Omega\|_3^2dt.
}
\]

The same statement applies to the strain `S`, since strain has the same Navier--Stokes scaling as vorticity.

### Critical `L_t^1L_x^infinity`

For

\[
k=0,\quad p=\infty,\quad q=1,
\]

again

\[
\boxed{\alpha_\Omega=0.}
\]

This is the vorticity Beale--Kato--Majda scaling class, although no BKM conclusion is imported here.

---

## 5. Static critical vorticity and coefficient norms

At one time slice,

\[
\|\Omega_R\|_{L^p}
=R^{2-3/p}\|\Omega\|_{L^p}.
\]

Hence the static critical exponent is

\[
\boxed{p=\frac32.}
\]

Thus

\[
\boxed{
\|\Omega_R(s)\|_{L^{3/2}}
=
\|\Omega(R^2s)\|_{L^{3/2}}.
}
\]

Any scalar coefficient with inverse-length-squared scaling,

\[
\kappa_R(y,s)=R^2\kappa(Ry,R^2s),
\]

has exactly the same critical static space:

\[
\boxed{
\|\kappa_R(s)\|_{L^{3/2}}
=
\|\kappa(R^2s)\|_{L^{3/2}}.
}
\]

This is directly relevant to the CE-H relation

\[
\Delta W=\kappa W.
\]

---

## 6. Velocity scaling atlas

For velocity,

\[
D_y^kV_R=R^{1+k}(D_x^kV)(Ry,R^2s),
\]

so

\[
\boxed{
\alpha_V(k,p,q)
=q\left(1+k-\frac3p\right)-2.
}
\]

At derivative order `k=0`, the lossless spacetime condition is

\[
\boxed{
\frac2q+\frac3p=1,
}
\]

which is the usual Navier--Stokes Serrin scaling line.

At a single time slice, velocity `L3` is invariant:

\[
\boxed{
\|V_R(s)\|_3
=\|V(R^2s)\|_3.
}
\]

This is the same critical currency used in the M5-526 `L3` packing route.

---

## 7. Scale-invariant weighted palinstrophy

Although unweighted palinstrophy is supercritical, insert the similarity weight `sqrt(-t)`.

For a fixed normalized cell interval `I`,

\[
\begin{aligned}
\int_I
\sqrt{-s}\,
\|\nabla\Omega_R(s)\|_2^2ds
&=
\int_{J_R}
\sqrt{-t}\,
\|\nabla\Omega(t)\|_2^2dt.
\end{aligned}
\]

Indeed the factor `sqrt(-s)=R^-1 sqrt(-t)` cancels the palinstrophy exponent `+1`.

Therefore

\[
\boxed{
\mathscr P_{crit}(J)
:=
\int_J\sqrt{-t}\,\|\nabla\Omega(t)\|_2^2dt
}
\]

is record-scale invariant.

However M5-477 proves only

\[
\int_{-\infty}^0\|\nabla\Omega\|_2^2dt<\infty.
\]

Because `sqrt(-t)` grows at backward infinity, this does **not** imply

\[
\int_{-\infty}^0
\sqrt{-t}\,\|\nabla\Omega\|_2^2dt<\infty.
\]

Thus the critical weighting removes the scale loss but also removes the known finite-budget property.

---

## 8. The exact tradeoff

The present ancestry offers a structural tradeoff:

\[
\boxed{
\text{finite global ancestral budget}
\Longrightarrow
\text{super/subcritical scale weights},
}
\]

while

\[
\boxed{
\text{lossless record transfer}
\Longrightarrow
\text{critical quantities not presently globally summable}.
}
\]

This is not a proof impossibility theorem; it identifies what a new theorem must add.

A successful continuation must use at least one of:

1. a rigidity theorem for a critical quantity;
2. a signed/monotone critical quantity rather than a positive finite budget;
3. CE-H coefficient structure such as the critical `kappa` channel;
4. strict physical scale descent preventing indefinite reuse;
5. critical endpoint transfer to the original singularity ancestry.

---

## 9. Relation to M17-207/M5-526

M5-526 identifies the velocity critical shell currency

\[
b_k=R_kE_k,
\qquad
\sum b_k^{3/2},
\]

whose summability controls velocity `L3`.

M17-207 preserves a nonsummable subfamily of this critical currency under tempered dyadic selection.

The present module explains why this line is qualitatively better suited to cross-generation transfer than palinstrophy counting:

\[
\boxed{
L^3\text{ velocity is exactly record-scale invariant.}
}
\]

What remains missing is not the scaling factor but the **ancestry theorem transporting the relevant `L3`/critical-shell structure through the M5-478 record blow-down and later M17 packet maps**.

---

## 10. DSD audit

- Every scaling exponent is derived from the exact M5-478 parabolic scaling.
- `R_m` record factors are not identified with late-M17 remote shell radii.
- Palinstrophy's `R^-1` ancestry loss is proved unavoidable for that specific unweighted currency.
- Critical quantities are not declared finite merely because they are scale invariant.
- The weighted critical palinstrophy is not declared globally finite.
- No external endpoint theorem is imported.
- The output is a scaling classification, not a regularity proof.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
