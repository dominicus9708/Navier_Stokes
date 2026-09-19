# M20-011 — The joint stretching compensation system is a two-covariance matrix, but q-reweighting and material projective damping do not share an invariant generator

Date: 2026-09-20  
Canonical ID: **M20-011**  
Status: **JOINT SIGNED COMPENSATION MATRIX / THE COMMON AXIAL-STRETCHING SCALAR gamma COUPLES TERMINAL ENSTROPHY REWEIGHTING TO PROJECTIVE STRAIN NONCOMMUTATION THROUGH TWO EXACT SNAPSHOT IDENTITIES / SIMULTANEOUS NEUTRALITY FORCES POSITIVE Y-gamma COVARIANCE AND OPPOSITE-SIGN gamma-K SEGREGATION / HOWEVER THE SECOND ROW COMES FROM A MATERIAL DERIVATIVE WHILE THE FIRST COMES FROM WEDGE-DEPTH PROBABILITY REWEIGHTING, SO q-RECURRENCE DOES NOT CLOSE THE MATRIX DYNAMICALLY / A COMMON TERMINAL MATERIAL GENERATOR IS THE NEXT REQUIRED OBJECT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Common terminal probability space

Use the terminal normalized enstrophy probability from M20-003:

\[
d\pi_B
=
\frac{|B|^2}{b_2}\,d\mu.
\]

All expectations and covariances in this module are with respect to \(\pi_B\).

Define

\[
\bar\gamma:=\mathbb E\gamma,
\qquad
g:=\gamma-\bar\gamma.
\]

Let

\[
Y:=X_T+X_D+X_\xi
\]

from M20-009, so that

\[
\lambda=Y-\gamma.
\]

Let

\[
\boxed{
K:=\|[S,Q]\|_F^2
=
2|P_\xi^\perp S\xi|^2
\ge0.
}
\]

Write

\[
\bar K:=\mathbb EK,
\qquad
k:=K-\bar K.
\]

## 2. First row: amplitude-selection covariance

M20-010 gives

\[
\boxed{
C_{\lambda\gamma}
:=
\operatorname{Cov}(\lambda,\gamma)
=
\operatorname{Cov}(Y,\gamma)
-
\operatorname{Var}(\gamma).
}
\]

Define

\[
V_\gamma:=\operatorname{Var}(\gamma),
\qquad
C_{Y\gamma}:=\operatorname{Cov}(Y,\gamma).
\]

Then

\[
\boxed{
C_{Y\gamma}
=
V_\gamma+C_{\lambda\gamma}.
}
\]

If the amplitude-selection covariance is nearly neutral,

\[
|C_{\lambda\gamma}|
\le
\varepsilon V_\gamma,
\]

then

\[
\boxed{
C_{Y\gamma}
\ge
(1-\varepsilon)V_\gamma.
}
\]

Thus stretching heterogeneity cannot disappear from the reweighting ledger. It must be matched by the nonstretching channels.

## 3. Second row: projective-strain stretching moment

Define the signed projective-strain moment

\[
\boxed{
M_{\gamma K}
:=
\mathbb E[\gamma K].
}
\]

Center \(\gamma\) and K:

\[
\begin{aligned}
M_{\gamma K}
&=
\mathbb E[(\bar\gamma+g)(\bar K+k)]
\\
&=
\bar\gamma\,\bar K
+
\mathbb E[gk].
\end{aligned}
\]

Hence

\[
\boxed{
M_{\gamma K}
=
\bar\gamma\,\bar K
+
C_{\gamma K},
}
\]

where

\[
C_{\gamma K}:=\operatorname{Cov}(\gamma,K).
\]

Equivalently,

\[
\boxed{
C_{\gamma K}
=
M_{\gamma K}
-
\bar\gamma\,\bar K.
}
\]

## 4. Joint signed compensation vector

The two identities can be written as

\[
\boxed{
\begin{pmatrix}
C_{Y\gamma}\\
C_{\gamma K}
\end{pmatrix}
=
\begin{pmatrix}
V_\gamma\\
-\bar\gamma\,\bar K
\end{pmatrix}
+
\begin{pmatrix}
C_{\lambda\gamma}\\
M_{\gamma K}
\end{pmatrix}.
}
\]

This is the basic M20-011 joint compensation system.

The same scalar \(\gamma\) generates:

- a negative self-covariance in the amplitude-selection ledger;
- a signed loading of projective strain noncommutation.

## 5. Simultaneous near-neutrality

Assume

\[
|C_{\lambda\gamma}|
\le
\varepsilon_1V_\gamma
\]

and

\[
|M_{\gamma K}|
\le
\varepsilon_2 |\bar\gamma|\,\bar K
\]

when

\[
|\bar\gamma|\,\bar K>0.
\]

Then

\[
\boxed{
C_{Y\gamma}
\ge
(1-\varepsilon_1)V_\gamma,
}
\]

and

\[
\boxed{
C_{\gamma K}
=
-\bar\gamma\,\bar K
+
O(\varepsilon_2|\bar\gamma|\bar K).
}
\]

Therefore:

- if \(\bar\gamma>0\), projective misalignment K must be biased toward below-average \(\gamma\);
- if \(\bar\gamma<0\), K must be biased toward above-average \(\gamma\).

Thus neutral projective damping requires a systematic phase segregation between axial stretching and transverse strain misalignment.

## 6. Covariance-matrix lower bounds

The covariance matrix of the centered variables

\[
(g,\;Y-\bar Y,\;k)
\]

is positive semidefinite.

Hence Cauchy--Schwarz gives

\[
C_{Y\gamma}^2
\le
V_\gamma\,\operatorname{Var}(Y),
\]

and

\[
C_{\gamma K}^2
\le
V_\gamma\,\operatorname{Var}(K).
\]

If

\[
V_\gamma>0,
\]

then

\[
\boxed{
\operatorname{Var}(Y)
\ge
\frac{(V_\gamma+C_{\lambda\gamma})^2}{V_\gamma},
}
\]

and

\[
\boxed{
\operatorname{Var}(K)
\ge
\frac{(M_{\gamma K}-\bar\gamma\bar K)^2}{V_\gamma}.
}
\]

Under simultaneous near-neutrality,

\[
\boxed{
\operatorname{Var}(Y)
\gtrsim
V_\gamma,
}
\]

and, when \(|\bar\gamma|\bar K\) is nontrivial,

\[
\boxed{
\operatorname{Var}(K)
\gtrsim
\frac{\bar\gamma^2\bar K^2}{V_\gamma}.
}
\]

Thus neutralization does not erase structure; it transfers it into variance and phase segregation.

## 7. Constant-gamma edge case

If

\[
V_\gamma=0,
\]

then \(\gamma=\bar\gamma\) almost surely.

The first covariance row vanishes automatically:

\[
C_{\lambda\gamma}=0.
\]

But

\[
M_{\gamma K}
=
\bar\gamma\,\bar K.
\]

Therefore if

\[
\bar K>0
\]

and the projective-strain moment is neutral,

\[
M_{\gamma K}=0,
\]

then necessarily

\[
\boxed{
\bar\gamma=0.
}
\]

Hence a nonzero constant axial stretching rate cannot coexist with positive mean projective noncommutation and zero signed damping moment.

## 8. Sign-phase form of the second row

Write

\[
\gamma=\gamma_+-\gamma_-,
\]

with

\[
\gamma_\pm\ge0,
\qquad
\gamma_+\gamma_-=0.
\]

Then

\[
\boxed{
M_{\gamma K}
=
\mathbb E[\gamma_+K]
-
\mathbb E[\gamma_-K].
}
\]

Thus exact neutrality

\[
M_{\gamma K}=0
\]

means

\[
\boxed{
\mathbb E[\gamma_+K]
=
\mathbb E[\gamma_-K].
}
\]

So projective misalignment weighted by extensional stretching must be exactly balanced by projective misalignment weighted by compressive stretching.

This statement does not require a sign assumption on \(\bar\gamma\).

## 9. Terminal mean stretching is not known to be positive

The terminal enstrophy-weighted mean stretching is

\[
\bar\gamma
=
\frac{
\left\langle\int\gamma|B|^2
\right\rangle
}{
\left\langle\int|B|^2\right\rangle
}.
\]

Its numerator is the terminal stretching-production coefficient.

M5-585--586 show that terminal stretching is coupled to terminal enstrophy flux and diffusion:

\[
\mathscr K_\omega'(0)
+
3\mathscr J_\omega(0)
=
\mathscr P_\omega(0)
-
\mathscr Q_\omega(0).
\]

No sign theorem forces

\[
\bar\gamma>0.
\]

Therefore M20-011 must retain all three regimes:

\[
\boxed{
\bar\gamma>0,
\qquad
\bar\gamma<0,
\qquad
\bar\gamma\approx0.
}
\]

## 10. Why the two rows do not yet form a closed dynamical matrix

The first row

\[
C_{\lambda\gamma}
\]

belongs to the terminal wedge-depth probability evolution:

\[
\partial_zd\pi_z|_0
=
2(\lambda-\alpha)d\pi_B.
\]

The second row is motivated by M20-006, whose fundamental equation is a physical material derivative:

\[
D_tK+\text{stretching damping}
=
\text{pressure/viscous forcing}.
\]

These are different generators.

The q-minimal/recurrent hull controls log-radial translation.

It does not by itself imply that

\[
\mathbb E_{\pi_B}[D_tK]=0,
\]

nor that one material lineage samples the q-invariant measure.

Therefore

\[
\boxed{
q\text{-recurrence}
\not\Rightarrow
M_{\gamma K}\text{ is dynamically neutral}.
}
\]

This is the main M20-011 firewall.

## 11. What is exact and what is conditional

Exact snapshot identities:

\[
C_{\lambda\gamma}
=
C_{Y\gamma}-V_\gamma,
\]

\[
M_{\gamma K}
=
\bar\gamma\bar K+C_{\gamma K}.
\]

Exact covariance consequences:

\[
\operatorname{Var}(Y)
\ge
\frac{C_{Y\gamma}^2}{V_\gamma},
\]

\[
\operatorname{Var}(K)
\ge
\frac{C_{\gamma K}^2}{V_\gamma}.
\]

Conditional statement:

If both signed observables are dynamically near-neutral on a common invariant sampling scheme, then strong positive Y--gamma covariance and gamma--K phase segregation are forced.

What is not yet proved:

that the terminal q-probability and material-line sampling define such a common invariant scheme.

## 12. Common-generator target

The correct next object is the terminal normalized material generator.

For a dimensionless scalar or tensor observable F,

\[
\boxed{
\mathcal M_A F
:=
-\partial_zF
+
A_r\partial_qF
+
A_T\cdot\nabla_SF.
}
\]

This is the terminal normalized version of

\[
r^2D_t.
\]

M20-012 should rewrite both:

- the vorticity-amplitude probability law;
- the projective-strain law;

using the same generator \(\mathcal M_A\).

Only after that rewrite can one ask whether an invariant/current measure exists that legitimately averages the two rows together.

## 13. Updated joint frontier

The new structural fork is

\[
\boxed{
\text{joint neutrality}
\Longrightarrow
\text{Y--gamma covariance}
+
\text{gamma--K phase segregation}
+
\text{common-generator/lineage problem}.
}
\]

The last term is not bookkeeping noise.

It is the exact obstruction to converting snapshot recurrence into a material contradiction.

## 14. Next target

M20-012 should derive the terminal homogeneity-corrected material equations for:

\[
\log|\omega|
\]

and

\[
K=\|[S,Q]\|_F^2.
\]

The goal is one common \(\mathcal M_A\)-ledger with all radial homogeneity terms exposed.

This will decide whether the joint signed system can be made genuinely dynamical or whether a material-lineage invariant measure is an additional theorem-level requirement.

\[
\boxed{\text{M20-011 COMPLETE; THE JOINT STRETCHING SYSTEM IS AN EXACT TWO-COVARIANCE SNAPSHOT MATRIX, BUT DYNAMICAL CLOSURE REQUIRES A COMMON MATERIAL GENERATOR.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
