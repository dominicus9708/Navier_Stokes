# M19-225 — The primal–adjoint Green flux pairs r^-1 and r^-2 critical data and conditionally excludes zero-q kernels

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / CRITICAL DUAL-FLUX IDENTITY + CONDITIONAL ZERO-Q CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Let W,Q solve the primal linearized similarity equation about a retained smooth background U,

\[
\partial_s W
=
\nu\Delta W
-b\cdot\nabla W
-\frac12W
-(\nabla U)W
-\nabla Q,
\qquad
b=\frac y2+U,
\]

and let Psi,Pi solve the backward formal adjoint from M19-224,

\[
-\partial_s\Psi
=
\nu\Delta\Psi
+b\cdot\nabla\Psi
+\Psi
-(\nabla U)^T\Psi
+\nabla\Pi.
\]

Both W and Psi are divergence free.

Assume the q=0 critical asymptotics

\[
\boxed{
W=r^{-1}B(\omega)+O(r^{-3}),
\qquad
\Psi=r^{-2}C(\omega)+O(r^{-4})
}
\]

with the corresponding retained derivative bounds. The compatible pressure scales are

\[
Q=O(r^{-2}),
\qquad
\Pi=O(r^{-3}).
\]

## 2. Exact local Green identity

A direct integration-by-parts calculation gives

\[
\boxed{
\partial_s(W\cdot\Psi)
=\nabla\cdot\mathfrak J[W,\Psi]
}
\]

with bilinear current

\[
\boxed{
\mathfrak J
=
\nu\bigl((\nabla W)^T\Psi-(\nabla\Psi)^TW\bigr)
-b\,(W\cdot\Psi)
-Q\Psi
-\Pi W.
}
\]

The pressure sign depends on the adjoint pressure convention; either convention gives the same critical limit because the pressure contributions decay two powers faster than the similarity-drift flux.

Equivalently, on the ball B_R,

\[
\boxed{
\frac d{ds}
I_R(s)
=
\mathcal F_R(s),
\qquad
I_R(s):=\int_{B_R}W\cdot\Psi\,dy,
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal F_R
:=\int_{S_R}
\Bigl[
&\nu(\Psi\cdot\partial_nW-W\cdot\partial_n\Psi)
-(b\cdot n)W\cdot\Psi\\
&-Q\,\Psi\cdot n
-\Pi\,W\cdot n
\Bigr]dS.
\end{aligned}
}
\]

## 3. Critical flux limit

At q=0,

\[
W\cdot\Psi
=r^{-3}B\cdot C+O(r^{-5}).
\]

Also

\[
b\cdot n
=\frac r2+O(r^{-1}).
\]

Therefore the similarity-drift part is

\[
\begin{aligned}
-\int_{S_R}(b\cdot n)W\cdot\Psi\,dS
&=
-\frac12
\int_{S^2}B\cdot C\,d\omega
+O(R^{-2}).
\end{aligned}
\]

The remaining terms satisfy

\[
\int_{S_R}
\nu(\Psi\cdot\partial_nW-W\cdot\partial_n\Psi)dS
=O(R^{-2}),
\]

\[
\int_{S_R}Q\,\Psi\cdot n\,dS=O(R^{-2}),
\qquad
\int_{S_R}\Pi\,W\cdot n\,dS=O(R^{-2}),
\]

and the U contribution inside b is also O(R^-2).

Hence

\[
\boxed{
\lim_{R\to\infty}\mathcal F_R(s)
=
-\frac12
\langle B,C\rangle_{S^2}.
}
\]

This is the critical dual flux: r^-1 primal data and r^-2 adjoint data are exactly complementary under the similarity drift.

## 4. Relative-periodic integration

Let the background be bounded-period RSS/RDSS with period S and rotational holonomy Q_* in the natural vector-field representation.

Assume W is a symmetry-quotient zero-q unit kernel mode and Psi is a relative-periodic adjoint mode with the same geometric return law. Because B_R is rotation invariant and the Euclidean dot product is preserved,

\[
\boxed{I_R(s+S)=I_R(s).}
\]

Integrating the Green identity over one period gives, for every R,

\[
\boxed{
0
=
\int_0^S\mathcal F_R(s)ds.
}
\]

The zero-q labels B,C are s-independent in the scattering frame and holonomy-fixed. Passing R to infinity therefore yields

\[
0
=
-\frac S2
\langle B,C\rangle_{S^2}.
\]

Thus every physically realized relative-periodic adjoint witness must satisfy

\[
\boxed{
\langle B,C\rangle_{S^2}=0.
}
\]

## 5. Angular duality is nondegenerate

M19-041 gives the primal q=0 Hodge form

\[
B
=
B_r\omega
-\nabla_{S^2}\Delta_{S^2}^{-1}B_r
+\omega\times\nabla_{S^2}\psi,
\]

where B_r has zero spherical mean.

M19-224 gives the adjoint q=0 form

\[
C
=
C_r\omega
+\omega\times\nabla_{S^2}\chi.
\]

Radial/tangential orthogonality and the sphere Hodge orthogonality between gradients and toroidal fields give

\[
\boxed{
\langle B,C\rangle_{S^2}
=
\int_{S^2}B_rC_r\,d\omega
+
\int_{S^2}\nabla_{S^2}\psi\cdot\nabla_{S^2}\chi\,d\omega.
}
\]

For a nonzero B choose the canonical angular dual datum

\[
\boxed{
C_B
:=
B_r\omega
+\omega\times\nabla_{S^2}\psi.
}
\]

Then

\[
\boxed{
\langle B,C_B\rangle_{S^2}
=
\|B_r\|_{L^2(S^2)}^2
+
\|\nabla_{S^2}\psi\|_{L^2(S^2)}^2
>0
}
\]

unless B=0.

If B is holonomy-fixed, the radial/toroidal Hodge components may be chosen in the same holonomy-fixed class, so C_B is also holonomy-fixed.

Therefore there is no angular/Hodge obstruction to a nondegenerate dual witness.

## 6. Conditional zero-q closure theorem

The preceding calculation gives an exact conditional theorem:

\[
\boxed{
\begin{array}{c}
B\ne0\text{ is a zero-q holonomy-fixed primal hard kernel label},\\
C_B\text{ has a global smooth relative-periodic adjoint realization}\\
\Downarrow\\
0=\langle B,C_B\rangle_{S^2}>0,
\end{array}
}
\]

which is impossible.

Hence

\[
\boxed{
\mathcal T_{dual-real}:
\text{realize the canonical nondegenerate }r^{-2}C_B\text{ datum as a global relative-periodic adjoint solution}
}
\]

would close the entire zero-q nonsymmetry kernel branch.

## 7. Important scope distinction

M19-223 already supplies an abstract invariant hard covector through the scattering-pullback metric. That does not yet imply a physical adjoint field Psi with the r^-2 critical asymptotic required here.

The new result is therefore not a completed kernel exclusion. It identifies the precise bridge between the finite-dimensional hard Fredholm dual and a PDE Green-flux dual.

Permanent firewall:

\[
\boxed{
\text{abstract hard adjoint covector}
\neq
\text{global physical }r^{-2}\text{ adjoint realization}.
}
\]

## 8. Certified / not certified

### Certified

1. Exact primal-adjoint Green identity on finite balls.
2. The only O(1) far-field boundary contribution is the similarity-drift pairing -1/2 <B,C>.
3. Relative-periodicity forces any realized primal/adjoint zero-q critical pair to have zero sphere pairing.
4. The primal and adjoint Hodge spaces possess an explicit nondegenerate angular pairing.
5. Global realization of C_B would therefore exclude every nonzero zero-q primal kernel.

### Not certified

1. Global smooth adjoint realization of C_B.
2. Relative-periodic adjoint existence in the physical function class.
3. Equality between the M19-223 abstract hard dual and the M19-224 physical adjoint scattering state.
4. Nonzero-q finite-resonance exclusion.
5. Global regularity.

## 9. Next target

Audit whether any existing result already supplies T_dual-real. In particular, distinguish unique continuation/Carleman (uniqueness) from adjoint boundary/scattering solvability (existence). If no existing bridge is available, formulate the transpose-scattering map whose surjectivity onto the finite hard dual would be sufficient.
