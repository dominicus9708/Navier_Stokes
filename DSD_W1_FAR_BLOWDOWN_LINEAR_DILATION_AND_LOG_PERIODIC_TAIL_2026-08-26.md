# DSD W1 Far Blow-Down: Linear Dilation and Log-Periodic Tail

Date: 2026-08-26

Status: **FAR BLOW-DOWN COMPACTNESS AND LINEARIZATION PROVED UNDER W1 SHELL BOUNDS / PERIODIC LIMIT IS DISCRETELY HOMOGENEOUS OF DEGREE -1 / NONZERO LIMIT REQUIRES AN OCCUPIED-SHELL SUBSEQUENCE / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Work on the pure W1 corridor.  On fixed-shape geometric annuli `A_R={R<|Y|<2R}`, the previously proved shell estimates give uniformly in recurrent Leray time `s`

\[
\boxed{
\|U(s)\|_{L^2(A_R)}^2\le C_0 R,
\qquad
\|\nabla U(s)\|_{L^2(A_R)}^2\le C_1R^{-1}.
}
\]

The first estimate follows from bounded relative Campanato plus the shell-mean telescoping bound.  The second follows from bounded shell derivative ratio together with the same Campanato bound.  Enlarged fixed-overlap annuli may be used throughout without changing the powers.

The Leray equation is
\[
\boxed{
U_s+\frac12U+\frac12Y\cdot\nabla U
+\mathbb P\nabla\cdot(U\otimes U)
=\nu\Delta U,
}
\]
where `P` is the whole-space Leray projector.

---

## 2. Spatial far blow-down

For `R>1`, define
\[
\boxed{
V_R(z,s):=R\,U(Rz,s).
}
\]
On the fixed annulus
\[
A:=\{1<|z|<2\},
\]
change of variables gives
\[
\|V_R(s)\|_{L^2(A)}^2
=R^{-1}\|U(s)\|_{L^2(A_R)}^2
\le C_0,
\]
and
\[
\|\nabla_zV_R(s)\|_{L^2(A)}^2
=R\|\nabla_YU(s)\|_{L^2(A_R)}^2
\le C_1.
\]
Hence
\[
\boxed{
\sup_{R\ge R_0}\sup_s
\|V_R(s)\|_{H^1(A)}\le C.
}
\]
The same estimate holds on every fixed compact annulus `a<|z|<b` after covering it by finitely many geometric shells.

**Status: PROVED.**

---

## 3. Exact rescaled equation and the R^{-2} small parameter

Since
\[
U(Rz,s)=R^{-1}V_R(z,s),
\]
we have
\[
U_s=R^{-1}(V_R)_s,
\qquad
Y\cdot\nabla_YU
=R^{-1}z\cdot\nabla_zV_R,
\]
while
\[
\Delta_YU=R^{-3}\Delta_zV_R
\]
and
\[
\mathbb P_Y\nabla_Y\cdot(U\otimes U)
=R^{-3}\mathbb P_z\nabla_z\cdot(V_R\otimes V_R).
\]
Multiplying the Leray equation by `R` yields
\[
\boxed{
(V_R)_s
+\frac12V_R
+\frac12z\cdot\nabla V_R
=R^{-2}
\left[
\nu\Delta V_R
-\mathbb P\nabla\cdot(V_R\otimes V_R)
\right].
}
\]
Thus the exact strength of the nonlinear and viscous terms in the far blow-down is `R^{-2}`.

**Status: PROVED.**

---

## 4. Uniform time-derivative bound

On every fixed compact annulus `K\Subset R^3\setminus{0}`, the H1 bound implies by Sobolev interpolation
\[
\|V_R\|_{L^4(K)}\le C_K.
\]
For test fields in `H^1_0(K)`,
\[
\|\mathbb P\nabla\cdot(V_R\otimes V_R)\|_{H^{-1}(K)}
\le C\|V_R\|_4^2
\le C_K,
\]
and
\[
\|\Delta V_R\|_{H^{-1}(K)}
\le\|\nabla V_R\|_2
\le C_K.
\]
The linear dilation operator maps `H^1(K')` to `L^2(K)` for a slightly larger fixed annulus `K'`. Therefore
\[
\boxed{
\sup_R
\|(V_R)_s\|_{L^\infty_sH^{-1}(K)}
\le C_K.
}
\]
More precisely, the nonlinear-viscous part has the sharper estimate
\[
\boxed{
\left\|
(V_R)_s+\frac12V_R+\frac12z\cdot\nabla V_R
\right\|_{H^{-1}(K)}
\le C_KR^{-2}.
}
\]

**Status: PROVED.**

---

## 5. Compactness and exact linear far limit

Fix a finite time interval `I`.  The bounds
\[
V_R\ \text{bounded in }L^\infty(I;H^1(K)),
\]
\[
\partial_sV_R\ \text{bounded in }L^\infty(I;H^{-1}(K))
\]
allow Aubin-Lions/Rellich compactness after passing to a sequence `R_n->infinity`.

For every compact `K\Subset R^3\setminus{0}` and finite `I`, after diagonal extraction,
\[
V_{R_n}\to V_\infty
\]
strongly in `L^2(I;L^2(K))`, weak-star in `L^∞(I;H^1(K))`, and strongly in `L^2(I;L^q(K))` for every `q<6`.

The `R_n^{-2}` residual tends to zero in `L^∞(I;H^{-1}(K))`. Hence the limit satisfies
\[
\boxed{
(V_\infty)_s
+\frac12V_\infty
+\frac12z\cdot\nabla V_\infty
=0
}
\]
in distributions on
\[
(R^3\setminus\{0\})\times R.
\]
Also
\[
\nabla\cdot V_\infty=0.
\]

Thus the far W1 tail has no surviving Navier-Stokes nonlinearity or viscosity in this blow-down.  Its exact limiting dynamics is the dilation transport.

**Status: PROVED.**

---

## 6. Explicit solution form

The linear dilation equation is solved by characteristics:
\[
\boxed{
V_\infty(z,s)
=e^{-(s-s_0)/2}
F\!\left(e^{-(s-s_0)/2}z\right),
}
\]
where
\[
F(z)=V_\infty(z,s_0).
\]
Equivalently, in logarithmic radius `rho=log|z|`, the profile is transported at speed `1/2`.

---

## 7. Periodic W1 gives a discretely homogeneous tail

Assume now that the W1 minimal orbit is exactly periodic with period `S>0`:
\[
U(Y,s+S)=U(Y,s).
\]
Then every `V_R` is also `S`-periodic.  The compactness limit inherits
\[
V_\infty(z,s+S)=V_\infty(z,s).
\]
Using the characteristic formula,
\[
e^{-S/2}F(e^{-S/2}z)=F(z).
\]
Set
\[
\lambda=e^{S/2}>1.
\]
Then
\[
\boxed{
F(\lambda z)=\lambda^{-1}F(z).
}
\]
Thus every periodic far blow-down is a discretely homogeneous divergence-free field of degree `-1` with scaling factor `lambda`.

In log radius, its amplitude is periodic with period
\[
\boxed{\log\lambda=S/2.}
\]

**Status: PROVED.**

---

## 8. Vorticity blow-down

Define
\[
G_R(z,s):=R^2\Omega(Rz,s)=\nabla_z\times V_R(z,s).
\]
The W1 shell-enstrophy bound
\[
\int_{A_R}|\Omega|^2\le C/R
\]
gives
\[
\boxed{
\|G_R\|_{L^2(A)}^2
=R\int_{A_R}|\Omega|^2
\le C.
}
\]
Hence along the same subsequence
\[
G_R\rightharpoonup G_\infty=\nabla\times V_\infty.
\]
In the periodic case,
\[
\boxed{
G_\infty(\lambda z)=\lambda^{-2}G_\infty(z).
}
\]
This is the exact critical `R^{-2}` vorticity scaling.

---

## 9. Nontriviality from an occupied-shell subsequence

Suppose the selected radii additionally satisfy a fixed cubic shell occupancy
\[
\int_{A_{R_n}}|U(s_0)|^3dY\ge m_0>0.
\]
This is available on a positive-density shell subsequence in the singular W1 branch via the corrected Barker-Prange shell-density recovery.

The cubic integral is invariant under the spatial blow-down:
\[
\int_A|V_{R_n}(z,s_0)|^3dz
=
\int_{A_{R_n}}|U(Y,s_0)|^3dY
\ge m_0.
\]
At fixed time `s_0`, the uniform H1 bound and Rellich compactness give, after a further subsequence,
\[
V_{R_n}(s_0)\to F
\quad\text{strongly in }L^3(A).
\]
Therefore
\[
\boxed{
\int_A|F|^3dz\ge m_0>0,
}
\]
so the far blow-down is nonzero.

**Status: PROVED conditional on selecting an occupied-shell subsequence at a common recurrent time.**

---

## 10. Consequence for the quotient strategy

The hoped-for quotient now becomes more precise.

The W1 tail is not an unknown nonlinear ancient subsystem at infinity.  After critical spatial blow-down, it converges to an exact **linear dilation memory**.  For a periodic W1 survivor this memory is a nonzero discretely homogeneous `-1` velocity / `-2` vorticity profile.

Therefore a future rigidity theorem should not attempt to prove that the remote tail has strong-L3 decay.  That is false at the critical scaling.  Instead it must show that the active recurrent core cannot repeatedly **inject / couple to** this asymptotically linear log-periodic memory while all H/T/projective budgets remain quiet.

Schematically,
\[
\boxed{
\text{periodic W1}
\Longrightarrow
\text{nonzero recurrent core}
+\text{nonzero linear log-periodic far memory}
+\text{vanishing far self-interaction }O(R^{-2}).
}
\]

The residual obstruction is therefore an **interface/injection rigidity problem**, not a tail-self-dynamics problem.

---

## 11. Claim boundary

This note does **not** show that a nonzero discretely homogeneous `F` is impossible.  The limiting linear dilation equation permits such fields.  It also does not construct an exact nonlinear quotient core by subtracting `F`; static subtraction would create cutoff/interface forcing.

What is proved is that the far nonlinear and viscous effects vanish under W1 spatial blow-down at the exact rate `R^{-2}`, and that a periodic occupied far tail has a nonzero discretely homogeneous linear limit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
