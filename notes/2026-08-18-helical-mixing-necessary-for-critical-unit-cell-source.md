# Helical-sign mixing is necessary for same-scale critical-source growth

Date: 2026-08-18

Status: **EXACT HELICAL DECOMPOSITION OF THE CRITICAL H^(1/2) SOURCE + FIXED-SHELL MINORITY-HELICITY DEPLETION. PURE HOMOCHIRAL SAME-SCALE INTERACTIONS DO NOT GROW THE CRITICAL H^(1/2) CHARGE; A SURVIVING UNIT-CELL CASCADE MUST RETAIN HETEROCHIRAL MIXING OR LEAVE THE FIXED-SHELL REGIME. GLOBAL REGULARITY NOT PROVED.**

## 1. Helical decomposition

For nonzero Fourier frequency `k`, let `P^+` and `P^-` be the two helical projections satisfying

\[
\nabla\times u^\pm
=\pm\Lambda u^\pm,
\qquad
\Lambda=(-\Delta)^{1/2}.
\]

Write

\[
u=u^++u^-.
\]

Define the two positive helical critical charges

\[
\boxed{
H_+=\|\Lambda^{1/2}u^+\|_2^2,
\qquad
H_-=\|\Lambda^{1/2}u^-\|_2^2.
}
\]

Then

\[
\boxed{
H_+-H_-
=\int u\cdot\omega\,dx
}
\]

is helicity, while

\[
\boxed{
H_++H_-
=\|u\|_{\dot H^{1/2}}^2
}
\]

is the positive scale-critical Sobolev charge encountered in the moving-band frontier.

## 2. Sector equations

Let

\[
B(u,v)=\mathbb P(u\cdot\nabla v)
\]

with `P` the Leray projector.  The helical sector equations are

\[
\partial_tu^\sigma
+\nu\Lambda^2u^\sigma
+P^\sigma B(u,u)=0,
\qquad
\sigma\in\{+,-\}.
\]

Therefore

\[
\frac12\dot H_\sigma
+\nu\|\Lambda^{3/2}u^\sigma\|_2^2
=-\left\langle
\Lambda u^\sigma,
P^\sigma B(u,u)
\right\rangle.
\]

## 3. Pure homochiral critical-source cancellation

If `u=u^+` is purely positive helical, then

\[
\omega=\Lambda u^+.
\]

The inviscid Euler nonlinearity conserves helicity, hence

\[
\left\langle
\Lambda u^+,
B(u^+,u^+)
\right\rangle=0.
\]

Orthogonality of the helical projections gives

\[
\boxed{
\left\langle
\Lambda u^+,
P^+B(u^+,u^+)
\right\rangle=0.
}
\]

Similarly,

\[
\boxed{
\left\langle
\Lambda u^-,
P^-B(u^-,u^-)
\right\rangle=0.
}
\]

Thus the pure `+++` and `---` interactions make no nonlinear contribution to the positive critical charge `H_++H_-`.

This algebraic fact is consistent with the sign-definite-helicity regularity mechanism of the helical-decimated Navier--Stokes model, but no decimated-model theorem is imported into the full equation here.

## 4. Exact heterochiral source identity

Expand the nonlinearity by input and output helicity signs.  After removing the two vanishing pure homochiral terms, define

\[
\mathcal T_{\rm het}
=-\sum_{(\sigma,\sigma_1,\sigma_2)\,\mathrm{mixed}}
\left\langle
\Lambda u^\sigma,
P^\sigma B(u^{\sigma_1},u^{\sigma_2})
\right\rangle,
\]

where `mixed` means that the triple of signs contains both `+` and `-`.

Then exactly

\[
\boxed{
\frac12\frac d{dt}
\|u\|_{\dot H^{1/2}}^2
+\nu\|u\|_{\dot H^{3/2}}^2
=\mathcal T_{\rm het}.
}
\]

Hence nonlinear growth of the critical `H^(1/2)` charge is purely heterochiral.

## 5. Fixed-shell minority-helicity depletion

Now restrict to one normalized same-scale shell

\[
|\xi|\asymp1.
\]

All Sobolev weights on that shell are equivalent up to fixed constants.  Let

\[
A_+=\|u^+\|_{2,\mathrm{shell}},
\qquad
A_-=\|u^-\|_{2,\mathrm{shell}}.
\]

Bernstein and the fixed-shell trilinear estimate give, for every mixed helical term,

\[
|T_{\sigma;\sigma_1\sigma_2}|
\lesssim
A_\sigma A_{\sigma_1}A_{\sigma_2}.
\]

Every surviving mixed term contains at least one factor from each helicity sign.  Therefore

\[
\boxed{
|\mathcal T_{\rm het}|
\lesssim
A_+A_-(A_++A_-).
}
\]

Let

\[
A=(A_+^2+A_-^2)^{1/2},
\qquad
\eta_h=\frac{\min(A_+,A_-)}{A}.
\]

Then

\[
\boxed{
|\mathcal T_{\rm het}|
\lesssim
\eta_h A^3.
}
\]

Thus a fixed-shell source operating at the generic cubic size requires

\[
\boxed{
\eta_h\not\to0.
}
\]

If one helicity sign becomes negligible, the same-scale critical source acquires a strict coefficient depletion unless cross-scale transfer or derivative concentration invalidates the fixed-shell reduction.

## 6. Updated same-scale network requirement

The compact high--high interaction wall therefore has another necessary structural channel:

\[
\boxed{
\text{persistent heterochiral mixing}
}
\]

or else it must pay

\[
\boxed{
\text{cross-scale commutator / derivative escape}.
}
\]

Combined with the physical-space projective analysis, a minimal same-scale source-active network must simultaneously avoid

- projective isotropy, which depletes common affine strain;
- excessive angular roughness, which is directly viscously damped;
- signed-line cancellation, which is a polarity/gradient branch;
- homochiral polarization, which depletes fixed-shell critical `H^(1/2)` production.

Thus the irreducible unit-cell motif is not merely noncoherent. It must be a **heterochiral, signed/projectively organized, same-scale nonlocal strain network**.

## 7. Claim boundary

The helical-decimated model has a sign-definite helicity and corresponding global regularity theory, but the full Navier--Stokes equation can regenerate the opposite helicity sector.  The present note uses only the algebraic source cancellation and fixed-shell depletion above; it does not transfer global regularity of the decimated model to the full equation.

Status: **PURE HOMOCHIRAL SAME-SCALE SOURCE REMOVED / SURVIVING UNIT-CELL CASCADE REQUIRES HETEROCHIRAL MIXING OR CROSS-SCALE DERIVATIVE TRANSFER.**