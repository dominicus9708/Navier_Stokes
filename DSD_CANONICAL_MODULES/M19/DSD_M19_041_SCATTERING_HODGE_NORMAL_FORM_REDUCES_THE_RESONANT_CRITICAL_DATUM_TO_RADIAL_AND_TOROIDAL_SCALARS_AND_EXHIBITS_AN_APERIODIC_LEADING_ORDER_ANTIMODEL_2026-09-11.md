# M19-041 — Scattering Hodge normal form reduces the resonant critical datum to radial and toroidal scalars and exhibits an aperiodic leading-order anti-model

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL NORMAL FORM / APERIODIC LEADING-ORDER FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

On the passive critical-tail branch,

\[
U(y,\theta)
=
\frac1r A(q,\omega)+O(r^{-3}),
\qquad
q=\log r-\frac\theta2,
\qquad
\omega=\frac y{|y|}.
\]

M5-567 gives the leading divergence-free constraint

\[
\boxed{
\partial_q A_r+A_r+\operatorname{div}_{S^2}A_T=0,
}
\]

where

\[
A=A_r\omega+A_T,
\qquad A_T\cdot\omega=0.
\]

For a bounded recurrent datum,

\[
\boxed{
\int_{S^2}A_r(q,\omega)d\omega=0.
}
\]

M19-035 shows that the \(r^{-1}\) sector is the unique similarity-transport resonance; the \(r^{-3}\) residual can generically be absorbed by a correction.

## 2. Hodge decomposition on the sphere

For each \(q\), every sufficiently regular tangential vector field on \(S^2\) has the Hodge decomposition

\[
\boxed{
A_T
=
\nabla_{S^2}\phi
+
\omega\times\nabla_{S^2}\psi,
}
\]

with scalar potentials \(\phi,\psi\), unique after fixing zero spherical means.

The second term is surface-divergence free:

\[
\operatorname{div}_{S^2}
(\omega\times\nabla_{S^2}\psi)=0.
\]

Therefore the divergence constraint becomes

\[
\boxed{
\Delta_{S^2}\phi
=
-(\partial_q+1)A_r.
}
\]

Because \(A_r\) has zero spherical mean, the right-hand side has zero spherical mean and this equation is solvable uniquely in the mean-zero class.

Thus

\[
\boxed{
\phi
=
-\Delta_{S^2}^{-1}(\partial_q+1)A_r.
}
\]

## 3. Exact leading-data parameterization

The complete divergence-free leading scattering datum is therefore parameterized by only two scalar fields:

\[
\boxed{
(A_r,\psi),
\qquad
\int_{S^2}A_r\,d\omega=0,
}
\]

through

\[
\boxed{
A
=
A_r\omega
-
\nabla_{S^2}\Delta_{S^2}^{-1}(\partial_q+1)A_r
+
\omega\times\nabla_{S^2}\psi.
}
\]

The poloidal/gradient part is determined by \(A_r\).
The genuinely independent tangential freedom is the toroidal scalar \(\psi\).

Thus the critical rigidity problem does not concern an arbitrary three-component vector profile.  It concerns

1. one mean-zero radial scalar channel;
2. one toroidal scalar channel.

## 4. Pure toroidal sector

Set

\[
A_r=0.
\]

Then \(\phi=0\) and

\[
\boxed{
A(q,\omega)
=
\omega\times\nabla_{S^2}\psi(q,\omega).
}
\]

This field is tangent to every sphere and automatically satisfies the leading divergence constraint for arbitrary sufficiently regular \(q\)-dependence of \(\psi\).

Hence divergence-free geometry alone imposes no \(q\)-rigidity on the toroidal channel.

## 5. Explicit aperiodic recurrent leading datum

Fix a nonconstant spherical harmonic \(Y_{\ell m}(\omega)\) with \(\ell\ge1\), and let

\[
\boxed{
 b(q)=\sin q+\frac12\sin(\sqrt2\,q).
}
\]

This is bounded, smooth, quasiperiodic and recurrent under translations, but has no nonzero period.

Define

\[
\psi(q,\omega)
=b(q)Y_{\ell m}(\omega),
\]

and

\[
\boxed{
A(q,\omega)
=b(q)\,\omega\times\nabla_{S^2}Y_{\ell m}(\omega).
}
\]

Then:

1. \(A_r=0\);
2. \(\operatorname{div}_{S^2}A_T=0\);
3. \(A\) is bounded and smooth in \((q,\omega)\);
4. its translation orbit in \(q\) is compact and recurrent but aperiodic;
5. unless \(A\equiv0\), it is not in global \(L^3(dq\,d\omega)\), because its amplitude does not decay as \(|q|\to\infty\);
6. its exponentially weighted derivative/enstrophy density is finite on every remote half-line:
   \[
   \int_{q_0}^{\infty}e^{-q}\mathcal D[A](q,\omega)dq\,d\omega<\infty.
   \]

Thus this datum satisfies the currently certified **leading-order** passive-tail constraints while remaining genuinely aperiodic and weak-critical.

## 6. This is not an exact Navier--Stokes solution

The field

\[
U_0=r^{-1}A(q,\omega)
\]

constructed above is only a leading critical scattering profile.

It is not claimed to solve the full Navier--Stokes similarity equation.

M19-035 shows only that the first \(r^{-3}\) residual is nonresonant under the linear similarity transport and can formally be assigned to a subleading correction.  That does not prove convergence of a full asymptotic expansion, global realization, pressure compatibility, or existence of a smooth ancient solution with this datum.

Therefore the anti-model proves a **firewall**, not existence.

## 7. Consequence for local rigidity attempts

Any proposed R-critical proof based only on

- divergence-free leading geometry;
- zero net radial flux;
- bounded recurrent scattering amplitude;
- finite exponentially weighted enstrophy;
- failure of strong \(L^3\);
- one or finitely many nonresonant asymptotic correction equations

cannot by itself eliminate the aperiodic toroidal class.

Those conditions are all compatible with the explicit leading-order quasiperiodic datum above.

Hence the missing theorem must use genuinely global dynamical information beyond the local leading constraints.

## 8. Sharpened R-critical theorem frontier

The old target

\[
\mathcal T_{critical}:
\text{aperiodic weak-critical }q\text{-cocycle rigidity}
\]

can now be split into two scalar sectors:

\[
\boxed{
\mathcal T_{critical}
=
\mathcal T_{radial/poloidal}
+
\mathcal T_{toroidal}.
}
\]

The toroidal sector is especially important because it survives the leading divergence constraint with no radial component at all.

A closure theorem must therefore show that a nonzero recurrent aperiodic toroidal scattering datum cannot be globally realized by a complete ancient Navier--Stokes trajectory in the certified hull class, or else force a previously typed critical/remote/turnover exit.

## 9. Boundary-history interpretation

M5-567 identifies \(q\) with historical crossing time at a fixed spectator boundary:

\[
\theta_{cross}=2(\rho_{spec}-q).
\]

Thus the quasiperiodic toroidal datum corresponds, at leading order, to an aperiodic recurrent toroidal boundary history.

This suggests that the correct future rigidity observable should be a finite-radius boundary-history functional or a global cocycle over the recurrent hull, not another local radial asymptotic coefficient.

## 10. Next target

The next calculation should test natural integrated boundary quantities on a fixed spectator sphere—energy flux, angular momentum/circulation flux, or vorticity-flux moments—for a scale-critical toroidal history.

The objective is to determine whether any of these gives a finite-total-variation or one-sign cocycle on the original finite-energy parent.

If every such quantity is physically integrable with the similarity Jacobian, that will certify that the remaining toroidal rigidity really requires a new global theorem rather than a missed elementary budget.

---

\[
\boxed{\text{M19-041 COMPLETE; THE LEADING APERIODIC CRITICAL FREEDOM REDUCES TO TWO SCALAR CHANNELS, WITH AN EXPLICIT TOROIDAL ANTI-MODEL.}}
\]