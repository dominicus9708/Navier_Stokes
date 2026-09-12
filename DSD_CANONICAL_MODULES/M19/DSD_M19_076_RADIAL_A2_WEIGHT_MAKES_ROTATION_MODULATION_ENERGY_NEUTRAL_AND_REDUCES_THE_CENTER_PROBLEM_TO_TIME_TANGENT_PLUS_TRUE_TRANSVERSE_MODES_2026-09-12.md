# DSD M19-076 — Radial A2 weight makes rotation modulation energy-neutral and reduces the center problem to time tangent plus true transverse modes

Date: 2026-09-12

Status: **SYMMETRY-SAFE MODULATION / THE POLYNOMIAL A2 WEIGHT USED IN M19-063 IS RADIAL, SO THE EXACT SO(3) GENERATORS ARE SKEW-ADJOINT IN THE WEIGHTED HILBERT SPACE / AFTER CHOOSING A CO-ROTATING REPRESENTATIVE BY ORTHOGONALITY TO THE ROTATION ORBIT, THE ROTATION MODULATION TERM CONTRIBUTES EXACTLY ZERO TO THE DIFFERENCE ENERGY / THE ONLY COST IS SOLVABILITY OF THE FINITE-DIMENSIONAL MODULATION EQUATIONS, WHICH REQUIRES A UNIFORM ROTATION-GRAM GAP OR ELSE EXITS THROUGH ISOTROPY-ORBIT DEGENERATION / THE LIVE CENTER PROBLEM IS THEREFORE TIME TANGENT PLUS GENUINE TRANSVERSE CENTER, NOT ROTATIONAL REPRESENTATION DEGENERACY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted space and rotation generator

Use the radial A2 weight from M19-063,

\[
w(y)=(1+\kappa |y|^2)^{-a/2}.
\]

For any skew matrix \(A^T=-A\), define the infinitesimal rotation action on vector fields

\[
\boxed{
\mathcal J_A F
:=
AF-(Ay)\cdot\nabla F.
}
\]

Because

\[
\nabla\cdot(Ay)=\operatorname{tr}A=0
\]

and \(Ay\) is tangent to Euclidean spheres,

\[
(Ay)\cdot\nabla w=0.
\]

Therefore

\[
\nabla\cdot(wAy)=0.
\]

The matrix part \(A\) is skew on vector values, while the transport part is skew by weighted integration by parts. Hence

\[
\boxed{
\langle F,\mathcal J_A G\rangle_w
=-\langle \mathcal J_A F,G\rangle_w.
}
\]

In particular,

\[
\boxed{
\langle F,\mathcal J_A F\rangle_w=0.
}
\]

---

## 2. Co-rotating comparison

Let \(U_1(\theta)\) and \(U_2(\theta)\) be two complete trajectories in the compact recurrent corridor.

Choose a time-dependent rotation \(Q(\theta)\in SO(3)\), and set

\[
\widetilde U_2(y,\theta)
:=Q(\theta)U_2(Q(\theta)^Ty,\theta).
\]

Define the difference

\[
\boxed{W:=U_1-\widetilde U_2.}
\]

Let

\[
\Gamma:=Q'Q^T\in\mathfrak{so}(3).
\]

Differentiating the rotated trajectory gives

\[
\partial_\theta\widetilde U_2
=\mathcal N(\widetilde U_2)
+\mathcal J_\Gamma\widetilde U_2,
\]

where \(\mathcal N\) denotes the similarity Navier--Stokes vector field.

Therefore the exact difference equation is

\[
\boxed{
\partial_\theta W
=\mathcal N(U_1)-\mathcal N(\widetilde U_2)
-\mathcal J_\Gamma\widetilde U_2.
}
\]

---

## 3. Rotation-orbit orthogonality gauge

Choose a basis \(A_1,A_2,A_3\) of \(\mathfrak{so}(3)\), and define the orbit tangents

\[
Z_j:=\mathcal J_{A_j}\widetilde U_2.
\]

On the nondegenerate rotation-orbit stratum impose

\[
\boxed{
\langle W,Z_j\rangle_w=0,
\qquad j=1,2,3,
}
\]

for the independent orbit directions.

If the state has nontrivial isotropy, only the linearly independent tangents are retained.

Write

\[
\Gamma=\sum_j\gamma_jA_j.
\]

Then the modulation term in the weighted energy is

\[
-\left\langle W,\mathcal J_\Gamma\widetilde U_2\right\rangle_w
=-\sum_j\gamma_j\langle W,Z_j\rangle_w.
\]

Hence the orthogonality gauge gives the exact cancellation

\[
\boxed{
\left\langle W,\mathcal J_\Gamma\widetilde U_2\right\rangle_w=0.
}
\]

Thus time-dependent rotation modulation costs no direct weighted energy.

---

## 4. Modulation rates and the rotation Gram matrix

The orthogonality constraints must persist:

\[
\frac{d}{d\theta}\langle W,Z_i\rangle_w=0.
\]

Differentiating produces a finite-dimensional linear system for \(\gamma_j\):

\[
\boxed{
\sum_j G_{ij}(\theta)\gamma_j
=F_i(W,U_1,\widetilde U_2),
}
\]

where the leading orbit Gram matrix is

\[
\boxed{
G_{ij}
:=
\langle Z_i,Z_j\rangle_w.
}
\]

The forcing \(F_i\) contains the unmodulated difference dynamics and derivatives of the orbit frame.

If on the recurrent hull stratum

\[
\boxed{
\lambda_{\min}(G)\ge g_{rot}>0,
}
\]

then

\[
|\gamma|
\le g_{rot}^{-1}|F|.
\]

Because the modulation term already cancels in the energy identity, such a rate bound is needed for regularity of the moving frame and higher-order estimates, but not to pay a new zeroth-order energy defect.

---

## 5. Isotropy degeneration is the only rotation-modulation exit

If \(G\) loses rank, then some nonzero generator \(A\) satisfies

\[
\mathcal J_AU\to0.
\]

This means the trajectory approaches a state with enlarged rotational isotropy.

That is not a new turbulent payer; it is a symmetry-orbit degeneration.

Hence rotation modulation splits cleanly into

\[
\boxed{
\text{uniform orbit Gram gap}
\quad\lor\quad
\text{isotropy enhancement/stratum change}.
}
\]

On a compact fixed orbit-type stratum, continuity gives a uniform positive Gram floor after removing generators belonging to the isotropy algebra.

---

## 6. M19-064 weighted energy survives unchanged after rotation quotient

M19-064 gave schematically

\[
\frac12E_w'
+\frac\nu2G_w
+\delta_*E_w
\le0
\]

for an unmodulated difference, with

\[
\delta_*=c_{gap}-\text{transport/pressure/strain defects}.
\]

The co-rotating equation adds only

\[
-\langle W,\mathcal J_\Gamma\widetilde U_2\rangle_w,
\]

which vanishes exactly under the rotation-orbit gauge.

Therefore

\[
\boxed{
\text{the M19-064 coercivity constant is not degraded by symmetry-safe SO(3) modulation.}
}
\]

This is a genuine positive result: rotational center degeneracy can be removed without paying another nonlinear constant.

---

## 7. Why the same construction must not be used for time translation

One could formally impose another orthogonality condition against

\[
Z_t=\partial_\theta U
\]

and introduce a time-phase modulation \(\tau(\theta)\).

But the scattering law is

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

Thus time-phase modulation is exactly q-translation modulation.

Using it to define the quotient would identify the aperiodic scattering translations whose realizability is the object under investigation.

Hence M19-076 removes rotations but deliberately retains the time tangent as a visible center direction.

---

## 8. Correct projected cocycle

Let

\[
\mathcal H_{rot}(	heta)
:=
\left(T_{U(\theta)}(SO(3)\cdot U(\theta))\right)^{\perp_w}.
\]

After the rotation gauge, the cocycle acts on this moving weighted orthogonal complement.

The known exact center inside it is

\[
\boxed{
Z_t=\partial_\theta U
}
\]

provided \(Z_t\) is not itself a rotational tangent.

The live question is now precise:

\[
\boxed{
\text{does }\mathcal H_{rot}\text{ contain another bounded zero-exponent cocycle direction linearly independent of }Z_t?
}
\]

Such an extra direction is the interior candidate for an aperiodic scattering factor.

---

## 9. Relation to tail center

M19-068 found an infinite-dimensional formal critical-tail center,

\[
\delta U_0=r^{-1}B(q,\omega).
\]

M19-069 showed outward scattering is locally near-identity, so it does not collapse that center.

M19-076 removes only the finite-dimensional angular-frame degeneracy.

Therefore any remaining reduction from the formal infinite-dimensional tail center to a one-dimensional interior time center must still come from an interior observability/realizability mechanism.

---

## 10. New frontier

The theorem target becomes

\[
\boxed{
\mathcal T_{rot\text{-}transverse}:
\text{on the rotation-quotiented recurrent cocycle, every bounded zero-exponent direction is proportional to }\partial_\theta U.
}
\]

M19-076 proves that no additional coercivity loss is caused by removing rotations in the radial A2 norm.

It does **not** prove \(\mathcal T_{rot\text{-}transverse}\).

---

## 11. Next calculation

The next step is to test an adjoint/duality formulation.

If an additional bounded center solution \(W\) exists, pair it with a bounded adjoint solution \(\Psi\) of the rotation-transverse adjoint cocycle and examine whether the conserved pairing

\[
\langle W,\Psi\rangle_w
\]

can be represented at the spectator boundary as an observable of the scattering datum.

If every such transverse adjoint observable decays or is slaved to the time tangent, the center collapses. If not, the adjoint mode identifies the exact missing realizability invariant.

That is M19-077.
