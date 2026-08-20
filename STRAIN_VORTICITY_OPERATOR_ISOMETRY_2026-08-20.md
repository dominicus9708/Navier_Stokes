# Exact Strain--Vorticity Operator Isometry and KKT Multiplier Projection — 2026-08-20

Overall status: **OPERATOR-LEVEL KKT REDUCTION — GLOBAL REGULARITY NOT PROVED.**

This note identifies the exact Hilbert-space relation between the strain constraint space and divergence-free vorticity. It simplifies the first-hitting KKT source.

---

## 1. Strain--vorticity reconstruction operator

For `S in L^2_st`, define

\[
\mathcal B S
=\nabla\times[-2\operatorname{div}(-\Delta)^{-1}S].
\]

This is the vorticity corresponding to the unique divergence-free velocity reconstructed from the strain (modulo the standard whole-space gauge).

For divergence-free velocity fields,

\[
\boxed{
\|\omega\|_2^2
=2\|S\|_2^2.
}
\]

By polarization, for all `S_1,S_2 in L^2_st`,

\[
\boxed{
\langle\mathcal B S_1,\mathcal B S_2\rangle
=2\langle S_1,S_2\rangle.
}
\]

Hence

\[
\boxed{
\mathcal B^*\mathcal B
=2I
\quad\text{on }L^2_{st}.
}
\]

---

## 2. Surjectivity onto divergence-free vorticity

Every sufficiently regular divergence-free vorticity field with the whole-space integrability required for Biot--Savart determines a divergence-free velocity and hence a strain field in the constraint space. Thus on the divergence-free vorticity subspace,

\[
\boxed{
\mathcal B\mathcal B^*
=2I.
}
\]

On the full vector `L^2` space this becomes

\[
\boxed{
\mathcal B\mathcal B^*
=2P_{df},
}
\]

where `P_df` is the Leray projection onto divergence-free vector fields.

---

## 3. Explicit adjoint

The adjoint can also be written directly as

\[
\boxed{
\mathcal B^*f
=2(-\Delta)^{-1}\operatorname{sym}\nabla(\nabla\times f).
}
\]

This formula immediately annihilates curl-free vector fields.

---

## 4. Consequence for the KKT contact multiplier

The first-hitting threshold equation has source

\[
\mathcal B^*\boldsymbol\mu,
\]

where `boldsymbol mu` is supported on the maximum-vorticity contact set in the formal `p -> infinity` KKT limit.

Decompose

\[
\boldsymbol\mu
=P_{df}\boldsymbol\mu+\nabla\phi.
\]

Then

\[
\boxed{
\mathcal B^*\boldsymbol\mu
=\mathcal B^*P_{df}\boldsymbol\mu.
}
\]

Thus the gradient part of the contact multiplier is completely invisible to the strain variational equation.

Moreover, because the vorticity is divergence free,

\[
\boxed{
\langle\nabla\phi,\omega\rangle=0.
}
\]

Therefore the KKT reaction

\[
\Gamma_K=\langle\boldsymbol\mu,\omega\rangle
\]

depends only on the divergence-free part:

\[
\boxed{
\Gamma_K
=\langle P_{df}\boldsymbol\mu,\omega\rangle.
}
\]

---

## 5. Inversion of the visible KKT source

Let the strain-space KKT source be

\[
F=\mathcal B^*\boldsymbol\mu.
\]

Applying `mathcal B` gives

\[
\mathcal B F
=\mathcal B\mathcal B^*\boldsymbol\mu
=2P_{df}\boldsymbol\mu.
\]

Hence

\[
\boxed{
P_{df}\boldsymbol\mu
=\frac12\mathcal B F.
}
\]

Thus the dynamically relevant component of the contact multiplier is uniquely determined by the strain-space KKT forcing.

The KKT reaction can equivalently be written

\[
\Gamma_K
=\frac12\langle\mathcal B F,\mathcal B S\rangle
=\langle F,S\rangle,
\]

consistent with the amplitude homogeneity identity.

---

## 6. Interpretation

The maximum-vorticity constraint does not introduce an arbitrary vector-measure degree of freedom into the strain problem. Only the divergence-free component of the multiplier is visible, and that component is isometrically tied to the strain KKT source.

This reduces the contact-set problem to the question:

\[
\boxed{
\text{Can a contact-supported multiplier have a nontrivial divergence-free component that solves the threshold strain eigenproblem without producing H/T?}
}
\]

The next useful step is to pair the KKT equation with `-Delta S`. Because `mathcal B` commutes with `Delta`, the right-hand side becomes a contact-weighted vorticity curvature term, directly connecting the variational contact reaction to the dynamic first-hitting curvature identity.

Status: **THE STRAIN--VORTICITY MAP IS A sqrt(2)-ISOMETRY BETWEEN THE STRAIN CONSTRAINT SPACE AND DIVERGENCE-FREE VORTICITY. ONLY THE DIVERGENCE-FREE COMPONENT OF THE KKT CONTACT MULTIPLIER AFFECTS THE THRESHOLD EQUATION OR THE CONTACT REACTION. GLOBAL REGULARITY REMAINS UNPROVED.**