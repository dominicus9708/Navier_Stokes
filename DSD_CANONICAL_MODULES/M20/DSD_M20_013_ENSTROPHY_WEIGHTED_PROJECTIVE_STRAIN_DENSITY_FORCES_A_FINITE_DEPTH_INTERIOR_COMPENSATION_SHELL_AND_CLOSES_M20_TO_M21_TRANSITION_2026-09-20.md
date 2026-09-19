# M20-013 — The enstrophy-weighted projective-strain density forces a finite-depth interior compensation shell and closes the M20-to-M21 transition

Date: 2026-09-20  
Canonical ID: **M20-013**  
Status: **FINITE-DEPTH TRANSITION THEOREM / THE COMMON M20-012 PRODUCT LEDGER EXTENDS TO ALL WEDGE DEPTHS AS A q-AVERAGED TRANSPORT ODE / ON ANY TERMINAL PROJECTIVE-STRAIN BRANCH WITH POSITIVE ENSTROPHY-WEIGHTED COMMUTATOR DENSITY, A NATURAL WEIGHTED CURRENT FUNCTIONAL STARTS POSITIVELY AT z=0 AND DECAYS TO ZERO IN THE SMOOTH TYPE-I CORE / THEREFORE IT HAS A POSITIVE INTERIOR MAXIMUM WHERE THE COMBINED PRESSURE-DIFFUSION-PROJECTIVE REMAINDER EXCEEDS TWICE THE STRETCHING-WEIGHTED JOINT DENSITY BY AN EXACT POSITIVE AMOUNT / THIS IS THE SEMANTIC AND MATHEMATICAL HANDOFF FROM TERMINAL M20 TO FINITE-DEPTH M21 / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Finite-depth joint fields

At general wedge depth z, write

\[
\omega=r^{-2}G,
\]

and let

\[
\Sigma_u=r^{-2}\Sigma_F.
\]

On \(\{G\neq0\}\), define

\[
\xi=\frac{G}{|G|},
\qquad
Q=\xi\otimes\xi.
\]

Set

\[
\boxed{
E:=|G|^2,
}
\]

and

\[
\boxed{
K:=\|[\Sigma_F,Q]\|_F^2
=
2|P_\xi^\perp\Sigma_F\xi|^2.
}
\]

The joint density is

\[
\boxed{
J:=EK\ge0.
}
\]

At \(z=0\), this reduces to the terminal M20 projective-strain density.

## 2. Physical homogeneity

The physical enstrophy density has degree four:

\[
|\omega|^2=r^{-4}E.
\]

The physical projective-strain square also has degree four:

\[
\|[\Sigma_u,Q]\|_F^2=r^{-4}K.
\]

Therefore the product has degree eight:

\[
\boxed{
|\omega|^2\|[\Sigma_u,Q]\|_F^2
=
r^{-8}J.
}
\]

Its advective flux

\[
u\,r^{-8}J
\]

has degree nine.

## 3. Finite-depth local joint balance

M20-012 gives the material product law in homogeneity-corrected form.

At finite depth, the same physical identity can be written in conservation form because

\[
\nabla\cdot u=0.
\]

Define the combined source remainder

\[
\boxed{
\mathcal R_J
:=
K\mathcal R_E
+
4E\mathcal R_K.
}
\]

Then the physical joint density obeys

\[
\boxed{
\partial_s(r^{-8}J)
+
\nabla\cdot
\left(
u\,r^{-8}J
\right)
+
2r^{-10}\Gamma_FJ
=
r^{-10}\mathcal R_J,
}
\]

where

\[
\Gamma_F:=\xi^T\Sigma_F\xi.
\]

## 4. Exact wedge transport equation

A vector flux of degree nine has divergence

\[
\nabla\cdot
\left(
r^{-9}JF
\right)
=
r^{-10}
\left[
(\mathfrak D-7)(JF_r)
+
\operatorname{div}_S(JF_T)
\right].
\]

Also

\[
\partial_s(r^{-8}J)
=
-r^{-10}\partial_zJ.
\]

Therefore

\[
\boxed{
-\partial_zJ
+
(\mathfrak D-7)(JF_r)
+
\operatorname{div}_S(JF_T)
+
2\Gamma_FJ
=
\mathcal R_J.
}
\]

This is the exact finite-depth enstrophy-projective-strain transport equation.

## 5. q-averaged finite-depth ODE

Define

\[
\boxed{
\mathscr Z(z)
:=
\left\langle
\int_{S^2}
J\,d\omega
\right\rangle_q
\ge0,
}
\]

\[
\boxed{
\mathscr F(z)
:=
\left\langle
\int_{S^2}
JF_r\,d\omega
\right\rangle_q,
}
\]

\[
\boxed{
\mathscr G(z)
:=
\left\langle
\int_{S^2}
\Gamma_FJ\,d\omega
\right\rangle_q,
}
\]

and

\[
\boxed{
\mathscr R(z)
:=
\left\langle
\int_{S^2}
\mathcal R_J\,d\omega
\right\rangle_q.
}
\]

Since

\[
\mathfrak D=\partial_q-2z\partial_z,
\]

the q-derivative and angular divergence average away, yielding

\[
\boxed{
\mathscr Z'
+
2z\mathscr F'
+
7\mathscr F
=
2\mathscr G
-
\mathscr R.
}
\]

At \(z=0\), this is exactly the M20-012 terminal product ledger.

## 6. Natural weighted current functional

Define

\[
\boxed{
\mathscr Y_{EK}(z)
:=
z^{5/2}\mathscr Z(z)
+
2z^{7/2}\mathscr F(z).
}
\]

Differentiate:

\[
\begin{aligned}
\mathscr Y_{EK}'
={}&
z^{5/2}
\left(
\mathscr Z'
+
2z\mathscr F'
+
7\mathscr F
\right)
\\
&+
\frac52z^{3/2}\mathscr Z.
\end{aligned}
\]

Use Section 5:

\[
\boxed{
\mathscr Y_{EK}'
=
z^{5/2}
\left(
2\mathscr G-\mathscr R
\right)
+
\frac52z^{3/2}\mathscr Z.
}
\]

This is the joint analogue of the weighted finite-depth witness functionals used earlier in the energy/enstrophy analysis.

## 7. Positive terminal joint density on the projective-strain branch

Suppose the terminal M20 strain branch has a quantitative floor on a robust high-vorticity subset:

\[
|B|\ge\beta_*>0,
\]

and

\[
\left\langle
1_{\{|B|\ge\beta_*\}}
|P_{\xi_B}^\perp\Sigma_A\xi_B|^2
\right\rangle
\ge s_*>0.
\]

Then

\[
E(0)=|B|^2
\]

and

\[
K(0)=2|P_{\xi_B}^\perp\Sigma_A\xi_B|^2.
\]

Therefore

\[
\boxed{
\mathscr Z(0)
\ge
2\beta_*^2s_*
>0.
}
\]

Call this lower bound

\[
Z_*>0.
\]

## 8. Near-terminal growth

The compact terminal jet gives bounded

\[
\mathscr G(z),
\qquad
\mathscr R(z),
\qquad
\mathscr Z(z)
\]

for small z.

Since

\[
\mathscr Z(0)=Z_*>0,
\]

Section 6 gives

\[
\boxed{
\mathscr Y_{EK}'(z)
=
\frac52Z_*z^{3/2}
+
O(z^{5/2})
>0
}
\]

for all sufficiently small \(z>0\).

Also

\[
\boxed{
\mathscr Y_{EK}(z)
=
Z_*z^{5/2}
+
O(z^{7/2})
>0
}
\]

near the terminal boundary.

Thus the terminal projective-strain branch launches a positive finite-depth joint current.

## 9. Smooth Type-I core decay

Let

\[
U(y,\theta)
\]

be the smooth similarity velocity near the center \(y=0\).

Since

\[
|y|=z^{-1/2},
\]

smooth bounded core fields give schematically

\[
F=O(z^{-1/2}),
\]

\[
G=O(z^{-1}),
\]

and

\[
\Sigma_F=O(z^{-1}).
\]

Therefore

\[
E=O(z^{-2}),
\]

\[
K=O(z^{-2}),
\]

and

\[
J=EK=O(z^{-4}).
\]

Hence

\[
\boxed{
\mathscr Z(z)=O(z^{-4}).
}
\]

Also

\[
JF_r=O(z^{-9/2}),
\]

so

\[
\boxed{
\mathscr F(z)=O(z^{-9/2}).
}
\]

Consequently,

\[
z^{5/2}\mathscr Z(z)=O(z^{-3/2})\to0,
\]

and

\[
z^{7/2}\mathscr F(z)=O(z^{-1})\to0.
\]

Thus

\[
\boxed{
\mathscr Y_{EK}(z)\to0
\qquad
(z\to\infty).
}
\]

## 10. Forced positive interior maximum

Sections 8 and 9 imply:

- \(\mathscr Y_{EK}(z)>0\) for small positive z;
- \(\mathscr Y_{EK}(z)\to0\) as \(z\to\infty\).

Therefore there exists at least one

\[
\boxed{
z_{EK}\in(0,\infty)
}
\]

at which \(\mathscr Y_{EK}\) attains a positive interior maximum.

At such a point,

\[
\mathscr Y_{EK}'(z_{EK})=0.
\]

Section 6 gives

\[
0
=
z_{EK}^{5/2}
(2\mathscr G-\mathscr R)
+
\frac52z_{EK}^{3/2}\mathscr Z.
\]

Hence

\[
\boxed{
\mathscr R(z_{EK})
-
2\mathscr G(z_{EK})
=
\frac{5}{2z_{EK}}
\mathscr Z(z_{EK})
>0.
}
\]

This is the main M20-013 finite-depth compensation-shell identity.

## 11. Meaning of the shell

At the forced depth \(z_{EK}\), the combined nonstretching remainder exceeds twice the stretching-weighted joint density by a strictly positive amount.

Recall

\[
\mathscr R
=
\langle K\mathcal R_E+4E\mathcal R_K\rangle.
\]

Thus the positive gap must be carried by a signed combination of:

- scalar vorticity diffusion;
- direction-gradient damping;
- transverse pressure-Hessian commutator;
- strain diffusion;
- viscous projective coupling.

The terminal projective-strain branch therefore cannot remain a purely terminal kinematic feature.

It forces a finite-depth PDE compensation event.

## 12. This is not yet a contradiction

The identity

\[
\mathscr R-2\mathscr G
=
\frac{5}{2z}\mathscr Z
>0
\]

does not imply that any one component of \(\mathscr R\) is positive.

Different signed channels may compensate each other.

Nor does it produce a noncritical original-variable power by itself.

It is a formed finite-depth witness, not a global regularity proof.

## 13. Comparison with earlier finite-depth witnesses

M5-587 forces an interior enstrophy-production shell through a weighted enstrophy functional.

M19-269 and later audits identify finite-depth energy transport structure on selected branches.

M20-013 now produces a different coupled witness:

\[
\boxed{
\text{enstrophy}
\times
\text{projective strain noncommutation}.
}
\]

It measures where strong vorticity and strain-axis misalignment are jointly present and must be compensated dynamically.

This quantity was not present in the earlier scalar energy/enstrophy witnesses.

## 14. M20 stop condition is reached

The organizational rule for M20 was:

> end M20 when terminal/projective information must be propagated through a genuinely finite-depth wedge corridor.

M20-013 reaches that condition exactly.

The proof object has changed from terminal projective geometry to finite-depth coupled wedge dynamics.

Therefore

\[
\boxed{
\text{M20 should be frozen at M20-013.}
}
\]

## 15. Handoff to M21

The natural M21 input is

\[
\boxed{
\mathscr Y_{EK}(z)
=
z^{5/2}\mathscr Z
+
2z^{7/2}\mathscr F
}
\]

with a forced interior maximum \(z_{EK}\) satisfying

\[
\boxed{
\mathscr R(z_{EK})
-
2\mathscr G(z_{EK})
=
\frac{5}{2z_{EK}}
\mathscr Z(z_{EK})
>0.
}
\]

M21 should study whether this shell can be placed in a uniform compact wedge corridor and coupled to the pre-existing energy/enstrophy finite-depth witnesses.

The first M21 module should establish the depth localization and determine whether same-corridor overlap is forced or merely possible.

\[
\boxed{\text{M20-013 COMPLETE; THE TERMINAL PROJECTIVE-STRAIN BRANCH FORCES A POSITIVE FINITE-DEPTH JOINT COMPENSATION SHELL.}}
\]

\[
\boxed{\text{M20 FREEZE CONDITION REACHED; NEXT ACTIVE FAMILY SHOULD BE M21.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
