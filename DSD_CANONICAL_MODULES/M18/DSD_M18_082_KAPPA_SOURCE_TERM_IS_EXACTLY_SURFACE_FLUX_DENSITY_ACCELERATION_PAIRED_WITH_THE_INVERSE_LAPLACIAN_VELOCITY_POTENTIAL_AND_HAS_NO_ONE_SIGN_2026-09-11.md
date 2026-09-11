# M18-082 — The kappa-source term is exactly surface flux-density acceleration paired with the inverse-Laplacian velocity potential, and it has no one-sign structure

**Date:** 2026-09-11  
**Status:** CE-H SOURCE-TERM REINTERPRETATION / MATERIAL FLUX-DENSITY ACCELERATION / NEGATIVE LYAPUNOV AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-080--081 reduce recurrent surface-current energy evolution to

\[
\boxed{
\mathcal E_\psi'
=
G_{\kappa\text{-}src}
+
G_{\perp\text{-}strain},
}
\]

with

\[
G_{\kappa\text{-}src}
:=
\int_\Sigma
\psi\rho(D_B\kappa+\kappa^2)dA,
\]

and

\[
G_{\perp\text{-}strain}
:=
\int_\Sigma
\mathring\Sigma_\perp(J_G,J_G)dA.
\]

The present module rewrites the coefficient-source term in the natural material flux-density coordinate.

The result is exact:

\[
\boxed{
G_{\kappa\text{-}src}
=
\langle\psi,q_\Sigma''\rangle_{\Sigma_0},
}
\]

where

\[
q_\Sigma:=\rho A_\Sigma.
\]

Moreover the Poisson equation says that \(\psi\) is the inverse-surface-Laplacian potential of the **first** material derivative \(q_\Sigma'\).

Thus \(\mathcal E_\psi\) is an \(H^{-1}\)-type kinetic energy of redistribution speed, not a monotone potential energy.

This explains the sign-indefiniteness structurally.

---

## 2. Material flux-density coordinate

On the fixed reference material patch \(\Sigma_0\), define

\[
\boxed{
q_\Sigma(\theta,a)
:=
\rho(\theta,a)A_\Sigma(\theta,a).
}
\]

M18-078 gives

\[
D_B\log(\rho A_\Sigma)=\kappa.
\]

Therefore in fixed material coordinates

\[
\boxed{
q_\Sigma'
=
\kappa q_\Sigma.
}
\]

Differentiate once more:

\[
\boxed{
q_\Sigma''
=
(D_B\kappa+\kappa^2)q_\Sigma.
}
\]

This is an exact identity.

---

## 3. Pulled-back Poisson source is q-prime

The instantaneous surface Poisson problem is

\[
-\Delta_\Sigma\psi
=
\kappa\rho.
\]

After pullback to the reference patch, the weak source functional is

\[
\ell_\theta(v)
=
\int_{\Sigma(\theta)}
\kappa\rho\,v\,dA.
\]

Since

\[
q_\Sigma'\,da
=
\kappa\rho\,dA,
\]

where `da` denotes the fixed reference area coordinate, one has

\[
\boxed{
\ell_\theta(v)
=
\int_{\Sigma_0}v q_\Sigma'\,da.
}
\]

Thus the elliptic equation can be written abstractly as

\[
\boxed{
L_\theta\psi=q_\Sigma',
}
\]

where \(L_\theta\) is the positive Dirichlet surface Laplacian operator in pulled-back coordinates.

---

## 4. Current energy is an H-minus-one speed norm

Because

\[
\psi=L_\theta^{-1}q_\Sigma',
\]

one obtains

\[
\begin{aligned}
2\mathcal E_\psi
&=
\int_\Sigma|\nabla_\Sigma\psi|^2dA\\
&=
\langle\psi,q_\Sigma'\rangle\\
&=
\langle q_\Sigma',L_\theta^{-1}q_\Sigma'\rangle.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_\psi
=
\frac12
\|q_\Sigma'\|_{H^{-1}_{L_\theta}}^2.
}
\]

The surface-current Dirichlet energy is therefore naturally interpreted as a squared negative-order **redistribution speed**.

It is not a static free energy of the flux-density state \(q_\Sigma\).

---

## 5. The kappa-source term is acceleration work

Using Section 2,

\[
\rho(D_B\kappa+\kappa^2)dA
=
q_\Sigma''da.
\]

Therefore

\[
\boxed{
G_{\kappa\text{-}src}
=
\int_{\Sigma_0}
\psi q_\Sigma''\,da
=
\langle L_\theta^{-1}q_\Sigma',q_\Sigma''\rangle.
}
\]

For a fixed metric/operator this is exactly the time derivative of the quadratic speed energy:

\[
\boxed{
G_{\kappa\text{-}src}
=
\frac12\frac d{d\theta}
\langle q_\Sigma',L^{-1}q_\Sigma'\rangle
}
\]

when \(L\) is time independent.

For the evolving material surface, M18-080 shows that the failure of this fixed-metric formula is precisely the tracefree surface-strain correction.

---

## 6. Mechanical interpretation

The structure is analogous to a time-dependent kinetic metric:

\[
q_\Sigma
=\text{configuration},
\]

\[
q_\Sigma'
=\text{redistribution velocity},
\]

\[
\psi=L^{-1}q_\Sigma'
=\text{velocity potential},
\]

\[
\mathcal E_\psi
=\frac12\langle q_\Sigma',L^{-1}q_\Sigma'\rangle
=\text{kinetic action density}.
\]

Then

\[
G_{\kappa\text{-}src}
=
\langle L^{-1}q_\Sigma',q_\Sigma''\rangle
\]

is acceleration work.

Acceleration work necessarily changes sign during a recurrent oscillation.

This makes the absence of a Lyapunov sign natural rather than accidental.

---

## 7. Explicit reversible one-mode model

Take a fixed surface metric and one normalized eigenfunction \(e\) of \(L\):

\[
Le=\lambda e,
\qquad \lambda>0.
\]

Consider a small recurrent redistribution mode

\[
q_\Sigma(\theta)
=q_0+\varepsilon\cos(\omega\theta)e
\]

with positive background \(q_0\) and sufficiently small \(\varepsilon\).

Then

\[
q_\Sigma'
=-\varepsilon\omega\sin(\omega\theta)e,
\]

\[
\psi
=-\frac{\varepsilon\omega}{\lambda}
\sin(\omega\theta)e,
\]

and

\[
\mathcal E_\psi
\propto
\sin^2(\omega\theta).
\]

The acceleration work is proportional to

\[
\sin(\omega\theta)\cos(\omega\theta),
\]

which changes sign and has zero period mean.

Thus even in the simplest positive-density recurrent mode, the source term is not one-signed.

This is a structural counterexample to any hoped-for sign based solely on the `q`, `q'`, `q''` geometry.

---

## 8. Periodic/recurrent loop consequence

For a fixed metric periodic loop,

\[
q_\Sigma(\theta+T)=q_\Sigma(\theta),
\qquad
q_\Sigma'(\theta+T)=q_\Sigma'(\theta),
\]

one has

\[
\boxed{
\int_0^T G_{\kappa\text{-}src}\,d\theta=0.
}
\]

Yet

\[
\boxed{
\int_0^T\mathcal E_\psi\,d\theta>0
}
\]

for a nontrivial loop.

Thus recurrent redistribution can carry positive current action with zero signed source-work drift.

This is exactly the reversible-cycle behavior isolated in M18-077.

---

## 9. Evolving metric: source work trades with transverse strain anisotropy

When \(L_\theta\) evolves, M18-080--081 give

\[
\boxed{
\mathcal E_\psi'
=
G_{\kappa\text{-}src}
+
G_{\perp\text{-}strain}.
}
\]

Therefore over a recurrent loop,

\[
\boxed{
\oint G_{\kappa\text{-}src}\,d\theta
=
-\oint G_{\perp\text{-}strain}\,d\theta.
}
\]

The coefficient-source acceleration work can acquire a nonzero cycle integral only by exchanging work with transverse strain anisotropy / metric deformation.

Thus the two terms form a coupled work pair.

---

## 10. No independent sign from kappa squared

The expression

\[
D_B\kappa+\kappa^2
\]

contains a visibly nonnegative scalar \(\kappa^2\), but it is multiplied by \(\psi\rho\), whose sign is not fixed.

The acceleration representation proves that extracting \(\kappa^2\) as a positive payer would be wrong: it is inseparable from the time derivative of \(\kappa\) at the level of the natural flux-density acceleration.

Therefore

\[
\boxed{
\kappa^2\text{ inside }G_{\kappa\text{-}src}
\not\Rightarrow
\text{positive cycle work}.
}
\]

This prevents a new unsigned-payer shortcut.

---

## 11. Relation to M18-059 unsigned-payer firewall

The present result reinforces M18-059.

The current energy

\[
\mathcal E_\psi
\]

is a positive local action, but recurrent oscillation can repeatedly reuse the same bounded state-space kinetic energy.

Its positivity does not create a new finite additive original-parent budget.

Hence another attempt to sum

\[
\mathcal E_\psi>0
\]

over recurrence cycles would reproduce the same unsigned-resource mismatch.

---

## 12. What remains genuinely new

The surface-current problem is now reduced to **metric-coupled recurrent dynamics**.

The essential nontrivial object is not the sign of source work but the coupled loop

\[
\boxed{
(q_\Sigma,L_\theta)
}
\]

in the space of flux-density configurations and surface metrics.

A nonzero geometric phase may exist because the kinetic metric itself changes through \(\mathring\Sigma_\perp\).

This is the only place in the current surface-current route where a signed cycle effect can survive after one full recurrence.

---

## 13. Updated cycle frontier

The controlled CE-H current route becomes

\[
\boxed{
\text{recurrent redistribution}
\Longrightarrow
\begin{cases}
G_{fixed\text{-}metric\ reversible},\\
G_{metric\text{-}coupled\ geometric\ cycle},\\
G_{surface/label\ geometry\ loss},\\
G_{self\text{-}helicity/twist}.
\end{cases}
}
\]

The fixed-metric reversible branch is not excluded by the source-work identity.

The metric-coupled branch is encoded by transverse strain anisotropy.

---

## 14. Highest-value next target

The next audit should determine whether the metric-coupled loop has a genuine geometric phase or whether its cycle work is an exact differential on the enlarged state space.

A practical first calculation is to write the variation of the inverse elliptic operator:

\[
\boxed{
D_BL^{-1}
=-L^{-1}(D_BL)L^{-1},
}

and express the metric-cycle contribution as a bilinear form in

\[
q_\Sigma'
\]

and

\[
D_BL.
\]

This will determine whether the transverse-strain compensation is simply the standard kinetic-metric connection term or contains an additional non-exact curvature capable of producing a signed holonomy around a recurrent loop.

---

## 15. Audit verdict

### Certified

1. \(q_\Sigma'=\kappa q_\Sigma\).
2. \(q_\Sigma''=(D_B\kappa+\kappa^2)q_\Sigma\).
3. The surface Poisson source is the material redistribution velocity \(q_\Sigma'\).
4. \(\mathcal E_\psi\) is one half of the squared \(H^{-1}\)-type redistribution speed.
5. The kappa-source term is acceleration work \(\langle L^{-1}q',q''\rangle\).
6. It has no one-sign structure and vanishes in mean over fixed-metric periodic loops.
7. A nonzero cycle integral of source work can only be balanced by evolution of the surface metric, identified with transverse strain anisotropy.
8. The visible \(\kappa^2\) factor cannot be extracted as an independent positive payer.
9. Fixed-metric reversible redistribution remains a genuine recurrent possibility.

### Still open

- geometric phase/holonomy of the time-dependent surface Dirichlet metric;
- fixed-metric reversible-cycle rigidity;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 16. Next target

M18-083 should compute the connection form induced by the evolving inverse surface Laplacian in

\[
\mathcal E_\psi
=\frac12\langle q_\Sigma',L_\theta^{-1}q_\Sigma'\rangle
\]

and audit whether a closed loop in \((q_\Sigma,L_\theta)\) can carry a nonzero signed geometric phase that is not already the integral of the tracefree-strain work term.
