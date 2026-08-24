# Vorticity-Tightness Dirichlet Frequency Floor — 2026-08-24

Status: **STAGE-WIDE TIGHTNESS NOW GIVES AN EXPLICIT POINTWISE PALINSTROPHY/ENSTROPHY FLOOR / NEW TIMING-INDEPENDENT SMALL-RADIUS CLOSURE / GLOBAL REGULARITY NOT PROVED.**

This note supplies a simpler lower bound for the frequency ratio than the terminal thick-core/Poincare construction. It uses only the existing assumption that the non-turnover candidate is vorticity-tight throughout each dynamically normalized stage.

---

## 1. Tightness hypothesis

At a dynamically normalized smooth time let

\[
Z=\|\Omega\|_2^2,
\qquad
Q=\|\nabla\Omega\|_2^2.
\]

Assume

\[
\boxed{
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z,
\qquad
0\le\varepsilon_Z<1.
}
\]

Equivalently,

\[
\int_{\mathbb R^3\setminus B_{R_Z}}|\Omega|^2
\le\varepsilon_Z Z.
\]

The existing smooth thick-core/enstrophy gate explicitly uses this hypothesis **throughout the stage**, so the estimate below is stage-wide on that corridor rather than merely an endpoint estimate.

---

## 2. Compact cutoff and Dirichlet Poincare

Fix `L>1`. Choose a radial Lipschitz cutoff `chi` satisfying

\[
\chi=1\text{ on }B_{R_Z},
\qquad
\chi=0\text{ outside }B_{LR_Z},
\]

and

\[
|\nabla\chi|
\le
\frac1{(L-1)R_Z}.
\]

Smooth cutoffs may approximate this bound arbitrarily closely.

Set

\[
f=\chi\Omega.
\]

Then

\[
\|f\|_2^2
\ge
(1-\varepsilon_Z)Z.
\]

Since `f in H_0^1(B_{LR_Z})`, the first Dirichlet eigenvalue of the three-dimensional ball gives

\[
\boxed{
\|f\|_2^2
\le
\frac{L^2R_Z^2}{\pi^2}
\|\nabla f\|_2^2.
}
\]

---

## 3. Separate interior gradient and cutoff-tail cost

For any `eta>0`,

\[
|a+b|^2
\le
(1+\eta)|a|^2
+
(1+\eta^{-1})|b|^2.
\]

Thus

\[
\|\nabla(\chi\Omega)\|_2^2
\le
(1+\eta)Q
+
(1+\eta^{-1})
\frac{\varepsilon_Z Z}{(L-1)^2R_Z^2}.
\]

Combining with Dirichlet Poincare yields

\[
(1-\varepsilon_Z)Z
\le
\frac{L^2R_Z^2}{\pi^2}
\left[
(1+\eta)Q
+
(1+\eta^{-1})
\frac{\varepsilon_Z Z}{(L-1)^2R_Z^2}
\right].
\]

Hence

\[
\boxed{
\frac QZ
\ge
\frac1{R_Z^2}
\frac{
\pi^2(1-\varepsilon_Z)L^{-2}
-
(1+\eta^{-1})\varepsilon_Z(L-1)^{-2}
}{1+\eta}.
}
\]

Whenever the numerator is positive this is a genuine scale-invariant frequency floor.

---

## 4. Optimize `eta` for fixed `L`

Set

\[
A=\frac{\pi^2(1-\varepsilon_Z)}{L^2},
\qquad
B=\frac{\varepsilon_Z}{(L-1)^2}.
\]

For `A>B`, maximizing over `eta>0` gives

\[
\boxed{
\eta_*
=\frac{\sqrt B}{\sqrt A-\sqrt B}
}
\]

and the optimized coefficient

\[
\boxed{
(\sqrt A-\sqrt B)^2.
}
\]

Therefore

\[
\frac QZ
\ge
\frac1{R_Z^2}
\left[
\frac{\pi\sqrt{1-\varepsilon_Z}}{L}
-
\frac{\sqrt{\varepsilon_Z}}{L-1}
\right]^2.
\]

---

## 5. Optimize the outer cutoff radius

Let

\[
a=\pi\sqrt{1-\varepsilon_Z},
\qquad
b=\sqrt{\varepsilon_Z}.
\]

The positive difference

\[
g(L)=\frac aL-\frac b{L-1}
\]

is maximized at

\[
\boxed{
L_*
=
\frac{\sqrt{a/b}}{\sqrt{a/b}-1}
}
\]

whenever `a>b`, which holds throughout the useful tightness range.

At this optimizer,

\[
g(L_*)
=
(\sqrt a-\sqrt b)^2.
\]

Hence the fully optimized tightness frequency coefficient is

\[
\boxed{
\Lambda_{tight}(\varepsilon_Z)
:=
\left[
\sqrt\pi(1-\varepsilon_Z)^{1/4}
-
\varepsilon_Z^{1/4}
\right]^4.
}
\]

Thus

\[
\boxed{
\frac QZ
\ge
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}.
}
\]

This is the main result of the note.

---

## 6. Quarter-tail benchmark

For

\[
\varepsilon_Z=\frac14,
\]

one obtains

\[
\boxed{
\Lambda_{tight}(1/4)
\approx0.7885770233.
}
\]

Hence

\[
\boxed{
\frac QZ
\ge
\frac{0.7885770233}{R_Z^2}.
}
\]

A simpler nonoptimized choice `L=2, eta=1` already gives

\[
\frac QZ
\ge
\frac{3\pi^2-8}{32R_Z^2}
\approx
\frac{0.6752754126}{R_Z^2},
\]

so the optimized gain is not dependent on a fragile choice.

---

## 7. Convert back to physical/ancient variables

Let `M(t)=||omega(t)||_infinity` and let `Z_phys,Q_phys` be physical enstrophy and palinstrophy. Under the dynamic first-hitting normalization,

\[
Z=M^{-1/2}Z_{phys},
\qquad
Q=M^{-3/2}Q_{phys}.
\]

Therefore

\[
\frac{Q_{phys}}{Z_{phys}}
=M\frac QZ.
\]

The tightness floor becomes

\[
\boxed{
\frac{Q_{phys}}{Z_{phys}}
\ge
M(t)
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}.
}
\]

This pointwise relation is stronger than a mere logarithmic-time average frequency floor.

Define

\[
\boxed{
\lambda_{tight}
:=
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}.
}
\]

Then

\[
Q_{phys}/Z_{phys}\ge\lambda_{tight}M.
\]

---

## 8. Insert into the trace-free enstrophy gate

The universal trace-free production estimate is

\[
\mathcal P
\le
\frac1{\sqrt3}MZ_{phys}.
\]

Hence

\[
\frac d{dt}\log Z_{phys}
\le
2\left(
\frac1{\sqrt3}-\nu\lambda_{tight}
\right)M(t).
\]

If

\[
\boxed{
\nu\lambda_{tight}\ge\frac1{\sqrt3},
}
\]

then the normalized enstrophy cannot grow forward from its backward-zero ancient limit, so the nontrivial ancient branch is impossible independently of the Type-I timing constant `K_I`.

Equivalently,

\[
\boxed{
R_Z^2
\le
\sqrt3\,\nu\Lambda_{tight}(\varepsilon_Z)
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

For quarter tails and viscosity normalized to `nu=1`,

\[
\boxed{
R_Z
\lesssim1.16869819
\quad\Longrightarrow\quad
\text{bounded-enstrophy tight ancient branch impossible.}
}
\]

This is a timing-independent small-tightness-radius closure.

---

## 9. Timing-assisted version outside the unconditional radius

If

\[
\nu\lambda_{tight}<1/\sqrt3
\]

and the ancient Type-I bound is

\[
M(t)\le K_I|t|^{-1},
\]

then the known decay `Z=O(|t|^{-1/2})` is incompatible with a nonzero solution whenever

\[
\boxed{
2K_I
\left(
\frac1{\sqrt3}
-
u\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)
<\frac12.
}
\]

Thus vorticity tightness improves the previous `K_I<sqrt(3)/4` threshold continuously rather than only through an averaged `c_log` correction.

---

## 10. Significance for the master certificate

The previous master note treated `c_log` as a separate recurrent input. On a stage-wide vorticity-tight corridor, this note supplies the stronger pointwise statement

\[
\boxed{
Q/Z\ge\lambda_{tight}M.
}
\]

Therefore the bounded-enstrophy ancient endgame can be rewritten directly in terms of

\[
\boxed{
K_I,
\quad
R_Z,
\quad
\varepsilon_Z,
\quad
\nu,
}
\]

without the analytic terminal-window constants used in the earlier explicit `c_log` construction.

The analytic/recurrent `c_log` route remains useful when stage-wide tightness is unavailable, but it is no longer the strongest route inside the stage-wide tight corridor.

Status: **VORTICITY TIGHTNESS ITSELF FORCES A SCALE-INVARIANT FREQUENCY FLOOR BY DIRICHLET POINCARE. AFTER DYNAMIC RESCALING THIS BECOMES `Q_phys/Z_phys >= lambda_tight M`, SO VISCOSITY DIRECTLY COMPETES WITH VORTEX STRETCHING AT THE SAME `M Z` SCALE. FOR QUARTER TAILS, `R_Z <= 1.1687 sqrt(nu)` CLOSES THE TIGHT ANCIENT BRANCH WITHOUT ANY TYPE-I TIMING CONSTANT. GLOBAL REGULARITY REMAINS UNPROVED.**