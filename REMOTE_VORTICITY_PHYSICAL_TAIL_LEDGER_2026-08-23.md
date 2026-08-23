# Remote Vorticity Physical-Tail Ledger — 2026-08-23

Status: **EXACT S-LEVEL TAIL IDENTITY + CONDITIONAL DEPLETION TIME GATE — GLOBAL REGULARITY NOT PROVED.**

This note attacks one half of the remaining remote source-replacement problem: replacement caused by actual depletion/transport of the outer vorticity reservoir. The complementary case, in which the outer vorticity mass remains but its orientation/cancellation changes, stays in the remote projective/source-functional lane.

The key device is to use a cutoff at a **fixed physical radius**. This removes the artificial first-hitting dilation sweep from the boundary term and yields a physical tail-enstrophy ledger.

## 1. Normalized enstrophy density

The fixed-center normalized vorticity equation is

\[
\Omega_s
+U\cdot\nabla\Omega
+\frac b2y\cdot\nabla\Omega
+b\Omega
=\Sigma\Omega+\nu\Delta\Omega.
\]

Set

\[
e=\frac12|\Omega|^2,
\qquad
V=U+\frac b2y.
\]

Taking the scalar product with `Omega` gives

\[
e_s+V\cdot\nabla e+2be
=\Omega^T\Sigma\Omega+\nu\Delta e-\nu|\nabla\Omega|^2.
\]

Since

\[
\nabla\cdot V=\frac32b,
\]

this becomes

\[
\boxed{
 e_s
+\nabla\cdot(Ve)
+\frac b2e
=
\Omega^T\Sigma\Omega
+\nu\Delta e
-\nu|\nabla\Omega|^2.
}
\]

## 2. Fixed physical cutoff

Fix a physical radius

\[
\ell>0
\]

around the non-turnover limiting center `X_*`. In normalized variables the same physical sphere has radius

\[
\boxed{
R(s)=\ell M(s)^{1/2}.
}
\]

Therefore

\[
\boxed{
\frac{R_s}{R}=\frac b2.
}
\]

Choose a radial cutoff

\[
\psi_R(y,s)=\psi(|y|/R(s)),
\]

with `psi=0` inside unit radius and `psi=1` outside radius two. Then

\[
\psi_s
=-\frac{R_s}{R}y\cdot\nabla\psi_R
=-\frac b2y\cdot\nabla\psi_R.
\]

Thus the cutoff moves exactly with the normalization dilation of a fixed physical sphere.

## 3. Exact normalized tail ledger

Define

\[
E_\ell(s)
:=\int\psi_Re\,dy
=\frac12\int\psi_R|\Omega|^2dy,
\]

and

\[
D_\ell(s)
:=\int\psi_R|\nabla\Omega|^2dy.
\]

Differentiate and use the density equation. The dilation contribution in `V` cancels exactly against `psi_s`, leaving only the actual normalized material velocity `U` at the cutoff. One obtains

\[
\boxed{
(E_\ell)_s
+\frac b2E_\ell
+\nu D_\ell
=X_\ell+F_\ell+\nu C_\ell,
}
\]

where

\[
\boxed{
X_\ell
:=\int\psi_R\Omega^T\Sigma\Omega\,dy,
}
\]

\[
\boxed{
F_\ell
:=\int (U\cdot\nabla\psi_R)e\,dy,
}
\]

and

\[
\boxed{
C_\ell
:=\int e\,\Delta\psi_R\,dy.
}
\]

`F_ell` is actual material crossing of the fixed physical shell. `C_ell` is the viscous cutoff commutator.

## 4. Physical tail enstrophy removes normalization damping

Under the first-hitting scaling, physical enstrophy outside the corresponding smooth physical cutoff is

\[
\boxed{
\mathscr E_\ell(s)
:=M(s)^{1/2}E_\ell(s).
}
\]

Indeed `omega=M Omega` and `dx=M^(-3/2)dy`, so the factor is exactly `M^(1/2)`.

Since

\[
(M^{1/2})_s=\frac b2M^{1/2},
\]

the `b/2` term cancels:

\[
\boxed{
(\mathscr E_\ell)_s
+\nu M^{1/2}D_\ell
=M^{1/2}(X_\ell+F_\ell+\nu C_\ell).
}
\]

Thus a fixed physical tail reservoir changes only through

1. vorticity stretching/reorientation;
2. actual material flux through the physical shell;
3. viscous dissipation and the smooth cutoff commutator.

There is no artificial geometric first-hitting dilution left.

## 5. Stretching bound

On the analytic/tight corridor suppose

\[
\|\Sigma\|_\infty\le B_+.
\]

Then

\[
|\Omega^T\Sigma\Omega|
\le B_+|\Omega|^2,
\]

so

\[
\boxed{
|X_\ell|
\le2B_+E_\ell.
}
\]

Thus stretching alone changes the physical tail enstrophy at relative normalized-time rate at most `2B_+`.

## 6. Material boundary-flux bound under the Morrey corridor

Let the transition annulus be

\[
A_R=\{R<|y|<2R\}.
\]

Since

\[
|\nabla\psi_R|\lesssim R^{-1},
\]

Cauchy--Schwarz gives

\[
|F_\ell|
\lesssim
R^{-1}\|U\|_{L^2(A_R)}\|e\|_{L^2(A_R)}.
\]

At first hitting `|Omega|<=1`, hence

\[
e^2=\frac14|\Omega|^4
\le\frac14|\Omega|^2.
\]

Writing

\[
E_A=\frac12\int_{A_R}|\Omega|^2dy,
\]

we have

\[
\|e\|_{L^2(A_R)}\lesssim E_A^{1/2}.
\]

Under the existing scale-invariant local kinetic-energy Morrey bound

\[
\rho^{-1}\int_{B_\rho}|U|^2dy\le M_*,
\]

\[
\|U\|_{L^2(A_R)}\lesssim M_*^{1/2}R^{1/2}.
\]

Therefore

\[
\boxed{
|F_\ell|
\lesssim
M_*^{1/2}R^{-1/2}E_A^{1/2}.
}
\]

## 7. Active-reservoir relative flux is O(R^-2)

Suppose the exterior reservoir is dynamically active at the core with a pointwise remote-strain threshold

\[
|\mathcal S_R|\ge s_0>0.
\]

The direct `L2` Biot--Savart estimate gives

\[
\int_{|y|\ge R}|\Omega|^2dy
\gtrsim R^3s_0^2.
\]

Thus, up to fixed cutoff constants,

\[
\boxed{
E_\ell\ge\kappa_0R^3,
\qquad
\kappa_0\asymp s_0^2>0.
}
\]

Since `E_A<=E_ell`, the material boundary flux satisfies

\[
\frac{|F_\ell|}{E_\ell}
\lesssim
M_*^{1/2}R^{-1/2}E_\ell^{-1/2}
\lesssim
M_*^{1/2}\kappa_0^{-1/2}R^{-2}.
\]

Hence

\[
\boxed{
\frac{|F_\ell|}{E_\ell}
\lesssim
C_FM_*^{1/2}s_0^{-1}R^{-2}.
}
\]

A large active remote reservoir therefore cannot lose a fixed fraction of its mass rapidly merely by ordinary material crossing of a fixed physical sphere when `R>>1`, unless the Morrey corridor fails.

## 8. Viscous cutoff relative rate

Because

\[
|\Delta\psi_R|\lesssim R^{-2},
\]

\[
|C_\ell|
\lesssim R^{-2}E_A
\le R^{-2}E_\ell.
\]

Therefore

\[
\boxed{
\nu\frac{|C_\ell|}{E_\ell}
\lesssim\nu R^{-2}.
}
\]

The true exterior dissipation term

\[
\nu D_\ell
\]

has favorable sign in the tail-energy equation. If its relative action is large, that is precisely a derivative/dissipative `H` payment rather than a quiet turnover.

## 9. Fixed-fraction physical-tail depletion gate

Suppose on an interval `I=[s0,s1]` the active reservoir remains large enough that the preceding active lower bound is valid, and define the relative derivative-dissipation action

\[
\boxed{
\mathscr H_\ell(I)
:=
\nu\int_I\frac{D_\ell}{E_\ell}ds.
}
\]

From the physical-tail ledger,

\[
-\frac{d}{ds}\log\mathscr E_\ell
\le
2B_+
+C_FM_*^{1/2}s_0^{-1}R^{-2}
+C_\nu\nu R^{-2}
+\nu\frac{D_\ell}{E_\ell},
\]

where for a varying normalized radius corresponding to fixed physical `ell`, use the minimum `R_-` over the interval.

If the physical tail enstrophy is depleted by a fixed factor

\[
\mathscr E_\ell(s_1)
\le\theta\mathscr E_\ell(s_0),
\qquad
0<\theta<1,
\]

then

\[
\boxed{
\log\frac1\theta
\le
2B_+|I|
+C_R
\left(M_*^{1/2}s_0^{-1}+\nu\right)
R_-^{-2}|I|
+\mathscr H_\ell(I).
}
\]

Consequently, on a low-derivative-action branch with

\[
\mathscr H_\ell(I)\le h_0<\log(1/\theta),
\]

and for `R_-` sufficiently large,

\[
\boxed{
|I|
\gtrsim
\frac{\log(1/\theta)-h_0-o_{R\to\infty}(1)}{2B_+}.
}
\]

This is a finite normalized-time floor for actual depletion of a large remote physical vorticity reservoir.

## 10. What this closes and what remains

A remote payer can be replaced in two fundamentally different ways.

### A. Mass/depletion replacement

The old physical tail reservoir loses a fixed fraction of its enstrophy, or substantial vorticity crosses inward through a physical shell. The exact ledger above shows that on large remote scales this requires

- order-one stretching time `B_+L`;
- large derivative dissipation `H`;
- Morrey/material-flux failure `T`;
- or a non-negligible stage duration.

This is now quantitatively controlled.

### B. Orientation/cancellation replacement

The tail vorticity mass remains, but its weighted orientation changes so that its contribution to core strain is cancelled/reoriented while another source becomes dominant. Tail enstrophy need not decrease in this case, so the present scalar ledger alone cannot close it.

That mechanism is represented by the exact matrix-valued remote-strain source identity and its stretching term. It is the remaining genuinely projective remote-source replacement problem.

## 11. Current turnover refinement

The source-replacement bottleneck is therefore no longer a single vague branch. It splits as

\[
\boxed{
T_{source}
=
T_{mass}
\ \lor\ 
T_{proj},
}
\]

where

- `T_mass`: physical vorticity-reservoir depletion/cross-shell replacement, governed by the present tail ledger;
- `T_proj`: orientation/cancellation replacement with roughly persistent tail mass, governed by the remote strain/source-evolution identity.

The next target is `T_proj`.

Status: **FIXED-PHYSICAL-RADIUS VORTICITY-TAIL DEPLETION HAS AN EXACT LEDGER. FOR A LARGE ACTIVE REMOTE RESERVOIR, ORDINARY MATERIAL/CUTOFF FLUX HAS ONLY `O(R^-2)` RELATIVE RATE; FIXED-FRACTION DEPLETION THEREFORE REQUIRES STRETCHING TIME, DERIVATIVE DISSIPATION, OR AN ALREADY TYPED TURNOVER FAILURE. THE REMAINING SOURCE-REPLACEMENT PROBLEM IS PROJECTIVE ORIENTATION/CANCELLATION TURNOVER. GLOBAL REGULARITY IS NOT PROVED.**
