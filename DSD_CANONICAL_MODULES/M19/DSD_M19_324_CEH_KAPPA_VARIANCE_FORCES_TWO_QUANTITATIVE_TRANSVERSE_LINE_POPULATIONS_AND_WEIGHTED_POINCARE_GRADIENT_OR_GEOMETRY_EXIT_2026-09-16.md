# M19-324 — CE-H kappa variance forces two quantitative transverse line populations and a weighted-Poincare gradient-or-geometry exit

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / EXACT CE-H SPATIAL-VARIANCE SHARPENING / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-322--323

On the exact CE-H compact branch,

\[
\Delta\Omega=\kappa\Omega,
\qquad
D_\xi\kappa=0.
\]

M19-322 gives a quantitative enstrophy-weighted coefficient variance on the spatial branch,

\[
\operatorname{Var}_{\pi}(\kappa)\ge c_\kappa>0.
\]

M19-323 identifies the snapshot spatial variance with the variance of the linewise coefficient under the flux-line probability measure \(\Pi\):

\[
\operatorname{Var}_{\Pi}(\kappa_\lambda)
=
\operatorname{Var}_{\pi}(\kappa).
\]

Compactness gives a uniform coefficient bound

\[
|\kappa_\lambda-\bar\kappa|\le M_\kappa<\infty.
\]

## 2. Variance cannot be carried by a vanishing exceptional population

Set

\[
X:=\kappa_\lambda-\bar\kappa,
\qquad
\mathbb E_\Pi X=0,
\qquad
\mathbb E_\Pi X^2\ge c_\kappa.
\]

Write

\[
a:=\mathbb E_\Pi X_+=\mathbb E_\Pi X_-.
\]

Since \(|X|\le M_\kappa\),

\[
\mathbb E X^2
\le
M_\kappa\mathbb E|X|
=2M_\kappa a.
\]

Hence

\[
\boxed{
a\ge \frac{c_\kappa}{2M_\kappa}.}
\]

Choose

\[
\delta_\kappa:=\frac{a}{2}
\ge
\frac{c_\kappa}{4M_\kappa}.
\]

Since

\[
a=\mathbb E X_+
\le
\delta_\kappa+M_\kappa\Pi(X\ge\delta_\kappa),
\]

we get

\[
\Pi(X\ge\delta_\kappa)
\ge
\frac{a}{2M_\kappa}
\ge
\frac{c_\kappa}{4M_\kappa^2}.
\]

The same estimate applies to the negative side. Therefore

\[
\boxed{
\Pi\!\left(\kappa_\lambda\ge\bar\kappa+\delta_\kappa\right)
\ge m_\kappa,
}
\]

\[
\boxed{
\Pi\!\left(\kappa_\lambda\le\bar\kappa-\delta_\kappa\right)
\ge m_\kappa,
}
\]

with

\[
\boxed{
\delta_\kappa\ge\frac{c_\kappa}{4M_\kappa},
\qquad
m_\kappa:=\frac{c_\kappa}{4M_\kappa^2}>0.
}
\]

Thus the CE-H spatial branch contains two coefficient-separated vortex-line populations of fixed positive line measure. The variance is not carried by a rare exceptional set.

## 3. The transition is purely transverse

Because

\[
D_\xi\kappa=0,
\]

we have

\[
\boxed{
\nabla\kappa
=P_\xi^\perp\nabla\kappa.
}
\]

Therefore every transition between the two coefficient populations is transverse to the instantaneous vortex-line direction.

There is no longitudinal recharge channel available on exact CE-H.

## 4. Weighted Poincare conversion

Let the active connected carrier component at one normalized snapshot carry the enstrophy weight

\[
d\pi=\frac{\rho^2}{E}\,dx,
\qquad
E=\int\rho^2dx.
\]

Suppose this weighted component has Poincare constant \(C_P\):

\[
\int \rho^2|f-\langle f\rangle_\pi|^2dx
\le
C_P
\int \rho^2|\nabla f|^2dx.
\]

Apply it to \(f=\kappa\). Then

\[
E\operatorname{Var}_{\pi}(\kappa)
\le
C_P
\int\rho^2|\nabla\kappa|^2dx.
\]

Hence

\[
\boxed{
\int\rho^2|\nabla_\perp\kappa|^2dx
\ge
\frac{E c_\kappa}{C_P}.
}
\]

On the retained own-scale record packet, normalized enstrophy is bounded below, so if

\[
E\ge E_*>0,
\qquad
C_P\le C_*<\infty,
\]

then

\[
\boxed{
\int\rho^2|\nabla_\perp\kappa|^2dx
\ge
c_{\nabla\kappa}>0.
}
\]

Thus bounded own-scale geometry turns the M19-322 spectral/coefficient variance into a fixed transverse coefficient-gradient payment.

## 5. Relation to the late-M17 geometry split

The late-M17 audit separates dimensional transverse size from scale-free Poincare/neck degeneration. Write schematically

\[
C_P=\mathfrak A\,\Pi_{shape},
\]

where \(\mathfrak A\) measures transverse size and \(\Pi_{shape}\) measures scale-free spectral-shape/neck degeneration.

Then

\[
\boxed{
\int\rho^2|\nabla_\perp\kappa|^2
\gtrsim
\frac{E c_\kappa}{\mathfrak A\Pi_{shape}}.
}
\]

Therefore persistent spatial coefficient variance forces the explicit dichotomy

\[
\boxed{
\mathcal G_{\nabla\kappa}
\lor
\mathcal G_{transverse-size}
\lor
\mathcal G_{neck/shape},
}
\]

where

- \(\mathcal G_{\nabla\kappa}\): fixed own-scale transverse coefficient-gradient payment;
- \(\mathcal G_{transverse-size}\): extra transverse-size dilution makes \(\mathfrak A\to\infty\);
- \(\mathcal G_{neck/shape}\): scale-free Poincare constant degenerates, \(\Pi_{shape}\to\infty\).

If the two positive-mass line populations are not contained in one connected regular active component, the alternative is instead component/interface/nodal segregation, already typed in the late-M17 exit architecture.

## 6. Why this is stronger than the previous qualitative statement

M19-323 only said that nonzero spatial variance is transverse line-label heterogeneity.

M19-324 adds two quantitative facts:

1. two coefficient-separated line populations each have fixed positive line measure;
2. on any uniformly connected own-scale geometry, their coexistence forces a fixed weighted transverse-gradient charge.

Thus spatial CE-H heterogeneity cannot be hidden in a vanishing line population or arbitrarily small coefficient gap.

## 7. Global-budget firewall

The new gradient payment is still an unsigned own-scale local charge.

M18-058--059 and M19-315--319 show that another fixed normalized unsigned payment does not automatically contradict the ancestral budget under geometric record scaling.

Therefore

\[
\boxed{
\text{fixed }\nabla_\perp\kappa\text{ payment}
\not\Rightarrow
\text{global contradiction}.
}
\]

The next useful question is whether exact linewise constancy plus the positive-mass two-population split forces one of the following stronger effects:

- duration growing with record scale;
- multiplicity growing like the record factor;
- unavoidable interface turnover/sign fragmentation;
- transverse-size or neck decompactification;
- critical/remote export.

## 8. Canonical conclusion

On the spatial M19-322 branch,

\[
\boxed{
\operatorname{Var}_\Pi(\kappa_\lambda)\ge c_\kappa
}
\]

forces two positive-mass vortex-line populations separated by a fixed coefficient gap. Since \(D_\xi\kappa=0\), their transition is purely transverse. Under uniformly bounded own-scale weighted Poincare geometry this forces a fixed transverse coefficient-gradient payment; otherwise one of the already typed transverse-size, neck/shape, component/interface, nodal, or export exits occurs.

\[
\boxed{
\text{M19-324 COMPLETE; THE OPEN ISSUE IS NOW PERSISTENCE/MULTIPLICITY OR GEOMETRY EXIT, NOT EXISTENCE OF A TRANSVERSE GRADIENT.}
}
\]
