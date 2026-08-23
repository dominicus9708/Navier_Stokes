# Ancient Local Compactness from Enstrophy Tightness — 2026-08-24

Status: **LOCAL ANCIENT COMPACTNESS BRIDGE STRENGTHENED / SCALE-UNIFORM TYPE-I CLASSIFICATION STILL SEPARATE / GLOBAL REGULARITY NOT PROVED.**

This note corrects an overly strong requirement in `TYPEI_COMPACTNESS_BRIDGE_2026-08-20.md`.

A scale-uniform bound

\[
\sup_R(A+C+D+E)<\infty
\]

is useful for classifying the limit as a Type-I ancient solution, but it is **not necessary merely to extract a local ancient suitable limit**.  On the vorticity-tight smooth corridor, the global normalized enstrophy bound already yields uniform local compactness on every fixed cylinder.

---

## 1. Fixed-center first-hitting scaling

Let

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\]

and let `X_*` be the limiting physical center supplied by the no-turnover nesting route.

Use the ordinary inertial rescaling

\[
U_j(y,\tau)
=r_j u(X_*+r_jy,t_j+r_j^2\tau),
\]

\[
P_j(y,\tau)
=r_j^2 p(X_*+r_jy,t_j+r_j^2\tau),
\]

\[
\Omega_j=\nabla\times U_j.
\]

Because the center is fixed in physical space, this is an ordinary translation and parabolic scaling.  No accelerated-frame affine pressure correction is introduced.

---

## 2. Dynamic enstrophy tightness implies a uniform fixed-scale global H1 bound

Let the running vorticity maximum at physical time `t` be

\[
M(t)=\|\omega(t)\|_\infty
\le W_j
\qquad(t\le t_j).
\]

In the dynamically normalized variables, define

\[
Z_{dyn}(t)
=M(t)^{-1/2}\|\omega(t)\|_2^2.
\]

Assume the recurrent vorticity-tight corridor gives

\[
\boxed{
Z_{dyn}(t)\le Z_+
}
\]

through the late backward tower.

In the fixed stage-`j` scaling,

\[
\|\Omega_j(\tau)\|_2^2
=W_j^{-1/2}\|\omega(t)\|_2^2
=\left(\frac{M(t)}{W_j}\right)^{1/2}Z_{dyn}(t).
\]

Since `M(t)<=W_j`,

\[
\boxed{
\|\Omega_j(\tau)\|_2^2
\le Z_+
\qquad(\tau\le0).
}
\]

For smooth decaying divergence-free velocity,

\[
\boxed{
\|\nabla U_j(\tau)\|_2^2
=\|\Omega_j(\tau)\|_2^2
\le Z_+.
}
\]

Thus the entire fixed first-hitting tower has a uniform global homogeneous-H1 velocity bound at every backward time.

---

## 3. Uniform global L6 velocity bound

The whole-space Sobolev inequality gives

\[
\|U_j(\tau)\|_6
\le C_S\|\nabla U_j(\tau)\|_2.
\]

Therefore

\[
\boxed{
\sup_j\sup_{\tau\le0}
\|U_j(\tau)\|_6
\le C_SZ_+^{1/2}.
}
\]

This estimate uses the actual decaying finite-energy rescaled velocity, so no arbitrary additive constant is present.

---

## 4. Fixed-R bounds for A and E

For any fixed `R>0`, Holder gives

\[
\int_{B_R}|U_j|^2
\le
|B_R|^{2/3}\|U_j\|_6^2
\le C R^2Z_+.
\]

Hence

\[
\boxed{
A_j(R)
\le C R Z_+.
}
\]

Similarly,

\[
\int_{-R^2}^0\int_{B_R}|\nabla U_j|^2
\le R^2 Z_+,
\]

so

\[
\boxed{
E_j(R)
\le R Z_+.
}
\]

The right sides grow with `R`, but for every fixed cylinder they are uniform in `j`.

---

## 5. Fixed-R cubic velocity bound

At each time,

\[
\|U_j\|_{L^3(B_R)}
\le
\|U_j\|_{L^2(B_R)}^{1/2}
\|U_j\|_{L^6(B_R)}^{1/2}.
\]

Therefore

\[
\int_{B_R}|U_j|^3
\le
C R^{3/2}Z_+^{3/2}.
\]

Integrating over a time interval of length `R^2`,

\[
\boxed{
C_j(R)
\le
C R^{3/2}Z_+^{3/2}.
}
\]

Again, this is uniform in `j` for each fixed `R`.

---

## 6. Fixed-R pressure bound without an accelerated gauge

In the inertial fixed-center scaling, take the standard whole-space pressure gauge

\[
P_j
=\mathcal R_i\mathcal R_k(U_{j,i}U_{j,k})
\]

up to a spatial constant.

Since `U_j in L6`,

\[
U_j\otimes U_j\in L^3
\]

and Riesz boundedness gives

\[
\boxed{
\|P_j(\tau)\|_3
\le C_P\|U_j(\tau)\|_6^2
\le C_PZ_+.
}
\]

On `B_R`,

\[
\int_{B_R}|P_j-[P_j]_{B_R}|^{3/2}
\le
C R^{3/2}Z_+^{3/2}.
\]

Thus

\[
\boxed{
D_j(R)
\le
C R^{3/2}Z_+^{3/2}.
}
\]

No time-dependent affine pressure gauge is needed because `X_*` is fixed.

---

## 7. Consequence: local suitable compactness

For every fixed `R`, the sequence has uniform bounds of the standard local suitable-solution type on

\[
B_R\times(-R^2,0).
\]

Therefore the usual local compactness argument gives, after a diagonal subsequence,

\[
U_j\to U_\infty
\]

strongly in the local velocity spaces required to pass the nonlinear term, with weak convergence of gradients and pressure in the corresponding local spaces.

The result is an ancient suitable solution on every finite cylinder, hence on

\[
\mathbb R^3\times(-\infty,0].
\]

This extraction uses **fixed-R bounds**, not a scale-uniform Type-I constant.

---

## 8. Nontriviality still needs the no-H higher-regularity input

Local suitable compactness alone does not automatically pass

\[
|\Omega_j(y_j,0)|=1
\]

pointwise.

The no-`H`/analytic corridor supplies the needed local derivative compactness.  Together with natural-scale center nesting,

\[
y_j=\frac{X_j-X_*}{r_j}=O(1),
\]

one may take a subsequence

\[
y_j\to y_*
\]

and obtain strong local vorticity convergence, hence

\[
\boxed{
|\Omega_\infty(y_*,0)|=1.
}
\]

Thus the ancient limit is nontrivial.

---

## 9. What this removes from the old compactness gap

The previous compactness draft listed four technical requirements:

1. natural-scale center nesting;
2. no-H derivative compactness;
3. uniform local Type-I `A,C,D,E` bounds on expanding scales;
4. a coherent accelerated pressure gauge.

For **local ancient extraction**, items 3 and 4 can be weakened/removed on the enstrophy-tight fixed-center route:

- fixed-R `A,C,D,E` bounds follow from `Z<=Z_+` and Sobolev/Riesz estimates;
- fixed-center inertial scaling removes the accelerated pressure-gauge problem.

The remaining extraction inputs are essentially

\[
\boxed{
\text{center nesting}
+\text{uniform normalized enstrophy}
+\text{no-H local derivative compactness}.
}
\]

---

## 10. Important distinction: extraction versus Type-I classification

The estimates above grow with `R`:

\[
A,E=O(R),
\qquad
C,D=O(R^{3/2}).
\]

Therefore this note does **not** prove

\[
\sup_R(A+C+D+E)<\infty.
\]

Such a scale-uniform bound remains a stronger property relevant to the Albritton-Barker Type-I classification and to global critical-tail control.

The important correction is logical:

\[
\boxed{
\text{scale-uniform Morrey/Type-I control is not required to extract the ancient limit itself.}
}
\]

It belongs to the subsequent rigidity/classification problem.

Status: **ON THE VORTICITY-TIGHT NO-H/T CORRIDOR, UNIFORM NORMALIZED GLOBAL ENSTROPHY ALONE YIELDS THE FIXED-R VELOCITY, DISSIPATION, CUBIC, AND PRESSURE BOUNDS NEEDED FOR LOCAL ANCIENT SUITABLE COMPACTNESS. FIXED-CENTER SCALING ALSO REMOVES THE ACCELERATED PRESSURE-GAUGE GAP. THE REMAINING COMPACTNESS INPUTS ARE CENTER NESTING AND STRONG LOCAL VORTICITY PASSAGE; SCALE-UNIFORM TYPE-I/MORREY CONTROL IS DEFERRED TO THE RIGIDITY STAGE. GLOBAL REGULARITY REMAINS UNPROVED.**