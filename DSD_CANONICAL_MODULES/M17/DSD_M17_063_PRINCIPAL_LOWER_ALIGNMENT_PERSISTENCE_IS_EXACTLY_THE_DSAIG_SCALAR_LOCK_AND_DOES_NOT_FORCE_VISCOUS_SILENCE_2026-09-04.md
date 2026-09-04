# DSD M17-063 — Principal lower-alignment persistence is exactly the DSAIG scalar lock and does not force viscous silence

Date: 2026-09-04
Canonical ID: **M17-063**

Status: **INTERNAL PVSJG AUDIT / ON THE RECURRENT PRINCIPAL-SLANT CORE, HORIZONTAL STRAIN ISOTROPY GIVES `Sigma_12=0` AT EVERY MATERIAL NODAL TIME AND M17-060 GIVES THE LOWER ALIGNMENT `f:=partial_1 Sigma_12=0`. THE STRAIN PDE `D_B Sigma=Delta Sigma-Sigma-Sigma^2-Omega^2-nabla^2P`, TOGETHER WITH `Omega=0` AND DIAGONAL CORE STRAIN, FIRST GIVES `Delta Sigma_12=P_12`. MATERIAL-DIFFERENTIATING `f=0` AND USING THE DIAGONAL CORE `nabla B` MAKES THE COMMUTATOR TERM PROPORTIONAL TO f AND THEREFORE ZERO. DIFFERENTIATING THE STRAIN PDE THEN GIVES EXACTLY `partial_1 Delta Sigma_12=partial_112 P`; ALL DERIVATIVES OF `Sigma^2` AND `Omega^2` VANISH IN THIS COMPONENT AT THE CORE. IN THE PRINCIPAL GEOMETRY M17-062 HAS ALREADY SHOWN THAT THE POISSON TRACE PART OF `partial_112P` VANISHES, SO THIS IDENTITY IS PRECISELY `v_*=m_3`. THUS THE FIRST MATERIAL PERSISTENCE OF THE LOWER ALIGNMENT DOES NOT PROVIDE A SECOND CONDITION AND DOES NOT FORCE `v_*=0`. FURTHER MATERIAL DIFFERENTIATION INTRODUCES TRANSVERSE SECOND DERIVATIVES OF THE ALIGNMENT DEFECT AND HIGHER PRESSURE/VISCOUS JETS; WITHOUT A NEIGHBORHOOD VANISHING OR FINITE-VANISHING-ORDER INPUT IT ONLY BUILDS A NEW HIERARCHY. THE CORRECT HARD PRINCIPAL BRANCH IS THEREFORE THE SINGLE LOCAL/GLOBAL SCALAR LOCK FROM M17-062, NOT AN ARTIFICIALLY OVERDETERMINED JET SYSTEM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Lower principal alignment data

On every regular winding node, M17-010 gives

\[
\Sigma_h=\lambda I_2.
\]

Hence in the fixed material principal frame

\[
\boxed{\Sigma_{12}=0.}
\]

This holds at every retained regular nodal time, not merely at one instant.

M17-060 further gives on principal slant

\[
\boxed{f:=\partial_1\Sigma_{12}=\phi_{112}=0.}
\]

The PVSJG question is whether material persistence of these two lower zeros forces

\[
\partial_1\Delta\Sigma_{12}=0.
\]

It does not.

---

## 2. Off-diagonal strain equation at the node

M17-044 gives

\[
D_B\Sigma
=\Delta\Sigma-\Sigma-\Sigma^2-\Omega^2-\nabla^2P.
\]

At a regular nodal core,

\[
\Omega=0,
\qquad
\Sigma=\operatorname{diag}(\lambda,\lambda,-2\lambda).
\]

Therefore

\[
\Sigma_{12}=0,
\qquad
(\Sigma^2)_{12}=0,
\qquad
(\Omega^2)_{12}=0.
\]

Since the nodal core is material and horizontal isotropy persists,

\[
D_B\Sigma_{12}=0.
\]

Thus the `12` component of the strain equation becomes

\[
\boxed{
\Delta\Sigma_{12}=P_{12}.
}
\]

This is the zeroth-order viscous/pressure balance in the forbidden horizontal shear direction.

---

## 3. Material derivative of the first alignment zero

For any scalar component `S`,

\[
D_B(\partial_1S)
=\partial_1(D_BS)
-(\partial_1B_j)\partial_jS.
\]

At the regular nodal core

\[
\nabla B
=\operatorname{diag}
\left(\lambda+\frac12,
\lambda+\frac12,
-2\lambda+\frac12\right).
\]

Apply this to

\[
S=\Sigma_{12}.
\]

The only surviving coefficient in the commutator is

\[
(\partial_1B_1)\partial_1\Sigma_{12}
=\left(\lambda+\frac12\right)f.
\]

But principal alignment gives

\[
f=0.
\]

Hence

\[
\boxed{
D_Bf=\partial_1(D_B\Sigma_{12}).
}
\]

Because `f=0` at every material nodal time,

\[
D_Bf=0,
\]

so

\[
\boxed{
\partial_1(D_B\Sigma_{12})=0.
}
\]

---

## 4. Differentiate the strain PDE

Differentiate the `12` strain equation in the `x_1` direction:

\[
\begin{aligned}
\partial_1(D_B\Sigma_{12})
={}&\partial_1\Delta\Sigma_{12}
-\partial_1\Sigma_{12}
-\partial_1(\Sigma^2)_{12}\\
&-\partial_1(\Omega^2)_{12}
-\partial_{112}P.
\end{aligned}
\]

The first lower term is

\[
\partial_1\Sigma_{12}=f=0.
\]

For the quadratic strain term, at the diagonal core

\[
\partial_1(\Sigma^2)_{12}
=(\lambda+\lambda)\partial_1\Sigma_{12}
=2\lambda f
=0.
\]

Since

\[
\Omega=0
\]

at the node, every first derivative of the quadratic tensor `Omega^2` contains one undifferentiated factor `Omega`, so

\[
\boxed{\partial_1(\Omega^2)_{12}=0.}
\]

Therefore material persistence gives

\[
\boxed{
\partial_1\Delta\Sigma_{12}
=\partial_{112}P.
}
\]

---

## 5. This is exactly the M17-062 scalar lock

M17-062 defines

\[
\boxed{
v_*
=\varepsilon_E\sqrt2\,\partial_1\Delta\Sigma_{12}.
}
\]

The global harmonic pressure scalar is

\[
\boxed{m_3=M_3/P.}
\]

At principal slant M17-062 also proves that the local Poisson trace/particular pressure has zero forbidden projection.
Equivalently, in the `112` pressure component the STF trace correction is zero because

\[
\partial_2S_P=0.
\]

Hence the forbidden pressure third derivative is exactly the harmonic cubic share, and

\[
\varepsilon_E\sqrt2\,\partial_{112}P
=m_3.
\]

Thus Section 4 becomes

\[
\boxed{v_*=m_3,}
\]

which is precisely the DSAIG scalar lock already obtained in M17-062.

No new equation has appeared.

---

## 6. Why f = 0 does not force Delta f = 0

Because derivatives commute in the fixed Euclidean frame,

\[
\partial_1\Delta\Sigma_{12}
=\Delta(\partial_1\Sigma_{12})
=\Delta f.
\]

At the material nodal point

\[
f=0,
\]

but a smooth or analytic scalar may vanish at a point while

\[
\Delta f\ne0.
\]

Therefore

\[
\boxed{f=0\not\Rightarrow v_*=0.}
\]

To infer `v_*=0`, one would need additional transverse vanishing information about the local alignment-defect field, not merely its value on the one-dimensional material nodal filament.

---

## 7. Why one more material derivative does not automatically help

Let

\[
g:=\Delta f.
\]

Commuting `D_B` with the Laplacian gives schematically

\[
D_Bg
=\Delta(D_Bf)
-2(\partial_iB_j)\partial_{ij}f
-(\Delta B_j)\partial_jf.
\]

Although

\[
D_Bf=0
\]

at the marked point, neither

\[
\Delta(D_Bf)
\]

nor the transverse Hessian of `f` is forced to vanish there.

Using the PDE simply replaces them by higher viscous and pressure/source jets.
Thus blind repetition of material differentiation generates a higher-jet compatibility tower rather than a contradiction.

A closure would require an independent finite-vanishing-order, neighborhood symmetry, sign, or compactness argument adapted to the alignment-defect field.

---

## 8. DSD analysis

M17-062 gave two descriptions of one hard scalar:

\[
\boxed{
\text{local viscous fifth jet }v_*
\equiv
\text{global harmonic pressure scalar }m_3.
}
\]

PVSJG tests whether lower alignment supplies another independent constraint.
It does not.

The material persistence equation is merely the dynamical derivation of the same equality.
Counting it twice would be a DSD descriptor-duplication error.

---

## 9. DSD audit

### Audit A — treating material persistence as a new equation
Rejected. It reproduces the existing DSAIG scalar lock exactly.

### Audit B — inferring Laplacian silence from pointwise alignment silence
Rejected.

### Audit C — ignoring quadratic strain/vorticity derivatives
Checked explicitly; they vanish in this first differentiated `12` component at the diagonal zero-vorticity core.

### Audit D — launching an infinite derivative hierarchy without a new compactness principle
Rejected as non-progressive bookkeeping.

### Audit E — proof status
The principal branch remains open through one genuine local/global scalar cocycle.

---

## 10. Updated principal frontier

The uniformly recurrent principal-slant survivor is exactly

\[
\boxed{
\begin{aligned}
X_-&=X_+=0,\\
\mathfrak o_{loc}&=0,\\
E_Q:N_{part}&=0,\\
v_*&=m_3,\\
D_Bv_*&=\Pi_3^{prod}+\Pi_3^{rel}.
\end{aligned}
}
\]

No additional independent constraint follows from first material persistence of `partial_1 Sigma_12=0`.

---

## 11. Next target

Because the principal local hierarchy has reached an audited fixed scalar lock, the highest-value continuation is to return to the genuinely oblique slant class of M17-058.
There the kappa-gradient payer-octupole does **not** vanish and can be connected directly to the material derivative

\[
h=D_B\kappa.
\]

The next target is the **Oblique Kappa-Gradient Recharge Gate (OKGRG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
