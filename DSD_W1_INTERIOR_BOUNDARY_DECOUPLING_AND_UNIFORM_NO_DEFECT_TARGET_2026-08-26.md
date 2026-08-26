# DSD W1 Interior--Boundary Decoupling and Exact No-Defect Target

Date: 2026-08-26

Status: **CORRECTED FINAL TARGET / POINTWISE WEAK-L3 COEFFICIENT REMOVED FROM THE GENERAL W1 LANE / EXACT BOUNDARY COORDINATE IS THE TRUNCATED-ENERGY DEFECT `K=lambda E_lambda` / UNIFORM VANISHING OF `K` WOULD CLOSE W1 / GLOBAL REGULARITY UNPROVED.**

## 1. Interior and boundary layers

The recurrent W1 state has two logically distinct layers.

### Interior layer

This contains finite-parent dynamics such as

- amplitude BMO oscillation;
- `D3` amplitude/direction cost;
- pressure-gradient work;
- vorticity stretching;
- pressure--stretch locking and relative-vorticity compensation.

### Boundary layer

For

\[
\mathcal E_\lambda(U)
:=
\frac12\int (|U|^2-\lambda^2)_+\,dY,
\]

define

\[
\boxed{
K(U;\lambda)
:=
\lambda\mathcal E_\lambda(U).
}
\]

The exact invariant threshold audit gives

\[
\boxed{
\lim_{\lambda\downarrow0}
\langle K(U;\lambda)\rangle_\mu
=
\frac{\mathscr R_3}{3}>0.
}
\]

This statement does not require the pointwise limit of `lambda^3 N(lambda)`.

## 2. Every fixed finite-energy prelimit state has zero `K` defect

At every finite Leray time, `U(s) in L2`. Therefore

\[
0\le K(U(s);\lambda)
\le
\frac\lambda2\|U(s)\|_2^2,
\]

and hence

\[
\boxed{
\lim_{\lambda\downarrow0}K(U(s);\lambda)=0
}
\]

for every fixed `s`.

The W1 invariant limit instead carries the positive averaged endpoint

\[
\boxed{
K^A(0+)=\frac{\mathscr R_3}{3}>0.
}
\]

Thus the obstruction is a loss of **uniform critical truncated-energy tightness** under the noncompact Leray limit.

## 3. Exact uniform no-defect condition

A sufficient closure theorem is

\[
\boxed{
\lim_{\lambda\downarrow0}
\sup_{s\ge s_0}
K(U(s);\lambda)
=0.
}
\]

If this holds on the late prelimit corridor, then every invariant omega-limit measure satisfies

\[
\lim_{\lambda\downarrow0}
\langle K(U;\lambda)\rangle_\mu=0,
\]

which contradicts

\[
\frac{\mathscr R_3}{3}>0.
\]

Hence this exact `K`-tightness statement would close W1 without any Tauberian upgrade.

## 4. Physical-variable form

Let

\[
\tau=T_*-t=e^{-s},
\qquad
\lambda=L\sqrt\tau.
\]

Since

\[
U(Y,s)=\sqrt\tau\,u(x,t),
\qquad
dY=\tau^{-3/2}dx,
\]

one obtains exactly

\[
\boxed{
K(U(s);L\sqrt\tau)
=
\frac L2
\int_{\mathbb R^3}
(|u(x,t)|^2-L^2)_+\,dx.
}
\]

Thus the Leray zero-amplitude boundary coordinate is the physical **scale-critical high-amplitude truncated kinetic-energy tail**.

For one fixed physical threshold `L`, this quantity is transported by the moving amplitude characteristic. The W1 obstruction concerns loss of uniform tightness as the physical threshold grows relative to the pre-blowup state.

## 5. Why finite kinetic energy alone does not give uniform `K` tightness

The energy inequality only gives

\[
K(U(s);L\sqrt\tau)
\le
\frac L2\|u(t)\|_2^2.
\]

This bound grows with `L` and therefore does not imply

\[
\sup_{t<T_*}
\frac L2\int(|u|^2-L^2)_+dx
\to0
\qquad(L\to\infty).
\]

A critical `1/r` corridor is compatible with finite `L2` energy and time-integrable ordinary dissipation, so the missing theorem must use more than the classical energy budget.

## 6. Relation to the amplitude pressure-pump identity

The exact threshold equation is

\[
\partial_s\mathcal E_\lambda
-\frac12\partial_\lambda(\lambda\mathcal E_\lambda)
+\nu D_\lambda
=J_P(\lambda).
\]

Equivalently,

\[
\boxed{
\partial_sK
-\frac\lambda2\partial_\lambda K
=\lambda\bigl(J_P-\nu D_\lambda\bigr).
}
\]

Therefore loss of `K` tightness is not an independent phenomenon: it is the boundary output of the amplitude-state pressure-minus-viscous processing.

At invariant-average level,

\[
\boxed{
\bar G(\lambda)
:=
\langle J_P(\lambda)-\nu D_\lambda\rangle_\mu
=-\frac12\partial_\lambda\bar K(\lambda).
}
\]

The positive endpoint residue is exactly the integrated net gain in the renormalized threshold ledger.

## 7. Defect-aware topology

For the general W1 lane, the correct augmented topology should control `K` rather than an unproved pointwise weak-`L3` coefficient. Schematically,

\[
 d_*(U,V)
=
\|U-V\|_{L^p}
+
\sup_{0<\lambda<\lambda_0}
|K(U;\lambda)-K(V;\lambda)|,
\qquad p>3.
\]

Precompactness of the late orbit in such a defect-aware critical topology would preserve the zero finite-time boundary coordinate and exclude a positive-`R3` W1 limit.

## 8. Correct final closure target

The shortest exact W1 closure route is now

\[
\boxed{
\text{finite-energy prelimit}
\Longrightarrow
\text{uniform critical `K`-tightness}
\Longrightarrow
\mathscr R_3=0
\Longrightarrow
\text{W1 contradiction}.
}
\]

Equivalently, one may prove a pressure-pump absorption theorem strong enough to force the same boundary coordinate to vanish.

No unconditional proof of either equivalent endpoint statement is presently available in the repository.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
