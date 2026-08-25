# DSD Pineau--Vicol Core-Speed Orthogonal Channel Gate

Date: 2026-08-25

Status: **PERSISTENT LOCAL SELF-SIMILAR SPEED DECOMPOSED EXACTLY INTO MEAN / STRAIN-AMPLITUDE / STRAIN-SHAPE / VORTICITY-AMPLITUDE / VORTICITY-SHAPE CHANNELS / MEAN AND VORTICITY-AMPLITUDE BALANCES TYPED / FINAL RECURRENT PHASE-SPACE CIRCULATION NOT YET EXCLUDED / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the local one-slice gate

On the pure spatial-Type-I lane, `DSD_PINEAU_VICOL_LOCAL_CORE_SPEED_GATE_2026-08-25.md` gives one fixed similarity ball

\[
B_R\subset\mathbb R^3
\]

and one constant

\[
\sigma_0>0
\]

such that every sufficiently late Leray time satisfies

\[
\boxed{
\|U_s(\cdot,s)\|_{L^2(B_R)}\ge\sigma_0.
}
\]

The frozen remote critical tail is Gaussian/local-decoupled and cannot supply this lower bound. The present note decomposes the required motion of the active core itself.

---

## 2. Exact mean / mean-free split

Let

\[
B=B_R,
\qquad
|B|=V_R,
\]

and define the fixed-ball mean speed

\[
\boxed{
c(s):=(U_s)_B
=\frac1{V_R}\int_BU_s(y,s)dy.}
\]

Because `c` is constant in space,

\[
\int_B(U_s-c)dy=0,
\]

and therefore

\[
\boxed{
\|U_s\|_{L^2(B)}^2
=V_R|c|^2
+\|U_s-c\|_{L^2(B)}^2.
}
\]

Consequently, at every sufficiently late time at least one of the following holds:

### M. Mean/core-translation speed

\[
\boxed{
|c(s)|
\ge
\sigma_M
:=
\frac{\sigma_0}{\sqrt{2V_R}}.
}
\]

### G. Mean-free geometric speed

\[
\boxed{
\|U_s-c\|_{L^2(B)}
\ge
\frac{\sigma_0}{\sqrt2}.
}
\]

Status: **PROVED EXACTLY.**

---

## 3. Mean-free speed forces a gradient-speed floor

Poincare on the fixed ball gives

\[
\|U_s-c\|_{L^2(B)}
\le
C_P R\|\nabla U_s\|_{L^2(B)}.
\]

Hence branch `G` implies

\[
\boxed{
\|\nabla U_s\|_{L^2(B)}
\ge
\sigma_G
:=
\frac{\sigma_0}{\sqrt2 C_PR}.
}
\]

This already shows that a pure local Galilean-like oscillation is the only way to maintain the Pineau--Vicol speed floor without changing the local velocity gradient.

Status: **PROVED.**

---

## 4. Exact strain/vorticity-time orthogonality

Write

\[
\nabla U=S+K,
\qquad
S=\frac12(\nabla U+\nabla U^T),
\qquad
K=\frac12(\nabla U-\nabla U^T).
\]

Then

\[
\nabla U_s=S_s+K_s
\]

and symmetric/antisymmetric matrices are Frobenius-orthogonal pointwise. In three dimensions,

\[
|K_s|^2=\frac12|\Omega_s|^2.
\]

Therefore

\[
\boxed{
\|\nabla U_s\|_{L^2(B)}^2
=
\|S_s\|_{L^2(B)}^2
+
\frac12\|\Omega_s\|_{L^2(B)}^2.
}
\]

Thus branch `G` implies at least one of

### S. Strain-time speed

\[
\boxed{
\|S_s\|_{L^2(B)}
\ge
\frac{\sigma_G}{\sqrt2}.
}
\]

### V. Vorticity-time speed

\[
\boxed{
\|\Omega_s\|_{L^2(B)}
\ge
\sigma_G.
}
\]

Status: **PROVED EXACTLY.**

---

## 5. Hilbert polar decomposition of strain motion

Define the local strain amplitude

\[
a(s):=\|S(\cdot,s)\|_{L^2(B)}.
\]

Whenever `a>0`, define the normalized local strain state

\[
\widehat S:=S/a,
\qquad
\|\widehat S\|_{L^2(B)}=1.
\]

Differentiate the unit-norm condition:

\[
\langle\widehat S,\widehat S_s\rangle_{L^2(B)}=0.
\]

Since

\[
S_s=a_s\widehat S+a\widehat S_s,
\]

the radial and projective components are exactly orthogonal:

\[
\boxed{
\|S_s\|_{L^2(B)}^2
=|a_s|^2
+a^2\|\widehat S_s\|_{L^2(B)}^2.
}
\]

At a time where `a=0`, any nonzero `S_s` is assigned to the amplitude channel by continuity.

Hence branch `S` implies one of

### SA. Strain-amplitude turnover

\[
\boxed{
|a_s|
\ge
\sigma_{SA}
:=
\frac{\sigma_G}{2}.
}
\]

### SP. Local projective strain-shape motion

\[
\boxed{
a\|\widehat S_s\|_{L^2(B)}
\ge
\sigma_{SP}
:=
\frac{\sigma_G}{2}.
}
\]

Status: **PROVED EXACTLY.**

---

## 6. Hilbert polar decomposition of vorticity motion

Likewise define

\[
b(s):=\|\Omega(\cdot,s)\|_{L^2(B)}.
\]

For `b>0`, set

\[
\widehat\Omega:=\Omega/b.
\]

Then

\[
\boxed{
\|\Omega_s\|_{L^2(B)}^2
=|b_s|^2
+b^2\|\widehat\Omega_s\|_{L^2(B)}^2.
}
\]

Thus branch `V` implies one of

### VA. Local enstrophy-amplitude turnover

\[
\boxed{
|b_s|
\ge
\sigma_{VA}
:=
\frac{\sigma_G}{\sqrt2}.
}
\]

### VP. Vorticity-shape/direction motion

\[
\boxed{
b\|\widehat\Omega_s\|_{L^2(B)}
\ge
\sigma_{VP}
:=
\frac{\sigma_G}{\sqrt2}.
}
\]

Again `b=0` routes a nonzero time derivative to the amplitude channel.

Status: **PROVED EXACTLY.**

---

## 7. Five-channel Pineau--Vicol speed gate

Combining the previous sections, every sufficiently late singular-survivor time satisfies at least one fixed-threshold channel:

\[
\boxed{
M
\ \lor\ 
SA
\ \lor\ 
SP
\ \lor\ 
VA
\ \lor\ 
VP.
}
\]

Explicitly,

\[
\boxed{
\begin{aligned}
M:&\quad |(U_s)_B|\ge\sigma_M,\\
SA:&\quad |\partial_s\|S\|_{L^2(B)}|\ge\sigma_{SA},\\
SP:&\quad \|S\|_{L^2(B)}\|\partial_s(S/\|S\|_2)\|_{L^2(B)}\ge\sigma_{SP},\\
VA:&\quad |\partial_s\|\Omega\|_{L^2(B)}|\ge\sigma_{VA},\\
VP:&\quad \|\Omega\|_{L^2(B)}\|\partial_s(\Omega/\|\Omega\|_2)\|_{L^2(B)}\ge\sigma_{VP}.
\end{aligned}
}
\]

No sixth purely kinematic local speed channel exists after fixing the observation ball.

Status: **PROVED.**

---

## 8. Exact mean-speed balance

Let

\[
m(s):=(U)_B.
\]

Then

\[
m_s=c(s).
\]

The Leray equation is

\[
U_s+\frac12U+\frac12y\cdot\nabla U+(U\cdot\nabla)U+\nabla P
=\nu\Delta U.
\]

Integrating over `B_R` and using `div U=0` gives

\[
\int_B y\cdot\nabla U
=R\int_{\partial B}U\,dS-3\int_BU\,dy,
\]

\[
\int_B(U\cdot\nabla)U
=\int_{\partial B}(U\cdot n)U\,dS,
\]

and the divergence theorem for pressure and viscosity. Therefore

\[
\boxed{
\begin{aligned}
m_s
={}&m
-\frac1{V_R}
\int_{\partial B}
\left[
\frac R2U
+(U\cdot n)U
+Pn
-\nu\partial_nU
\right]dS.
\end{aligned}
}
\]

Thus the mean-speed channel is not an untyped bulk mechanism. It is exactly a mismatch between the local mean mode and fixed-ball boundary momentum/pressure/viscous flux.

On the previously defined moving-core ledger, order-one persistence of this mismatch is a center/mean-turnover channel `T_mean` unless it settles into a finite-dimensional recurrent mean mode.

Status: **PROVED EXACTLY / LONG-TIME RECURRENT MEAN-MODE RIGIDITY OPEN.**

---

## 9. Exact fixed-ball enstrophy-amplitude balance

Let

\[
E_B(s):=\frac12\int_B|\Omega|^2dy=\frac12b(s)^2.
\]

The Leray vorticity equation is

\[
\Omega_s+\Omega+rac12y\cdot\nabla\Omega+U\cdot\nabla\Omega
=S\Omega+\nu\Delta\Omega.
\]

Multiplying by `Omega` and integrating over `B_R` gives

\[
\boxed{
\begin{aligned}
(E_B)_s
+\frac12E_B
+\nu\int_B|\nabla\Omega|^2dy
={}&
\int_B\Omega^TS\Omega\,dy\\
&-\frac R4\int_{\partial B}|\Omega|^2dS\\
&-\frac12\int_{\partial B}(U\cdot n)|\Omega|^2dS\\
&+\nu\int_{\partial B}\Omega\cdot\partial_n\Omega\,dS.
\end{aligned}
}
\]

Since

\[
(E_B)_s=b b_s,
\]

a large `VA` event is therefore forced by at least one of the already typed quantities:

- local stretching production;
- local palinstrophy;
- radial similarity-boundary transport;
- material enstrophy flux;
- viscous derivative flux.

Thus `VA` is not a new primitive survivor.

Status: **PROVED EXACTLY.**

---

## 10. Relation of SP and VP to existing projective/material ledgers

The channels `SP` and `VP` are genuine shape-space velocities.

- `SP` measures fixed-ball strain-tensor motion after quotienting out its scalar `L2` amplitude.
- `VP` measures fixed-ball vorticity-field motion after quotienting out its scalar `L2` amplitude.

On a coherent positive-middle tube/core lane, `SP` is the local time-dependent counterpart of the already derived projective strain/eigenframe action. A large coherent projective excursion is charged by the existing projective-frequency/H1 tax.

If that coherent transfer fails because the strain frame varies strongly in space, the failure is itself an eigenaxis-bending/derivative `H/T` exit.

Similarly, a large `VP` motion which is not induced merely by observation-frame crossing must be supplied by

\[
\text{material transport/deformation}
\lor
\text{viscous Cauchy defect},
\]

using the exact material Cauchy identity

\[
\partial_t(F^{-1}\omega)=\nu F^{-1}\Delta\omega.
\]

The viscous part is an existing hyperpalinstrophy/flux cost; the material part is a turnover/deformation channel.

What is **not yet proved** is a universal quantitative inequality transferring every local Eulerian `SP/VP` threshold directly into one of the existing global action constants without a coherence or localization alternative.

---

## 11. DSD audit verdict

### PROVED

The persistent Pineau--Vicol local speed floor has only five orthogonal formed channels:

\[
\boxed{M,SA,SP,VA,VP.}
\]

The raw `U_s` obstruction is therefore no longer untyped.

The mean and vorticity-amplitude channels have exact local balance identities. The strain/vorticity shape channels are explicitly separated from scalar amplitude change.

### STILL OPEN

A compact recurrent orbit can circulate indefinitely among these channels. In particular, bounded scalar amplitudes do not rule out periodic amplitude oscillation, and positive projective/directional speed does not by itself rule out a periodic or quasiperiodic shape orbit.

Thus the remaining hard object is a **phase-space circulation problem**:

\[
\boxed{
\text{persistent finite-channel recurrent motion}
\stackrel{?}{\Longrightarrow}
\text{one existing viscous/turnover action with non-summable positive rate}.
}
\]

This is narrower than the previous generic weak-`L3` tail problem: the frozen tail has been removed from the local motion budget, and the active obstruction is now finite-channel core circulation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
