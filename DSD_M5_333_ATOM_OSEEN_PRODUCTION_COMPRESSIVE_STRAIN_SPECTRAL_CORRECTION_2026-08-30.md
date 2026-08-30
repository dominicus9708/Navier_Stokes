# DSD M5-333 — Atom Oseen Production / Compressive-Strain Spectral Correction

Date: 2026-08-30

Status: **CORRECTION / ATOM PRODUCTION SEES THE NEGATIVE SPECTRAL PART OF STRAIN, NOT THE FULL STRAIN NORM UNIFORMLY / ENERGY ATOM FORCES NONSUMMABLE CRITICAL `L_t^2 L_x^3` COMPRESSIVE-STRAIN ACTION / VORTICITY-AXIS SPLIT MUST BE APPLIED ONLY AFTER THIS SPECTRAL STEP / GLOBAL REGULARITY UNPROVED.**

## 1. Why the previous axis split was too coarse

The previous atom audit reached a parent strain action and then used

\[
|S|^2=\frac32\gamma^2+2|\tau|^2+|D_\perp|^2.
\]

That identity is exact, but the atom-selected Oseen production has more structure than a full-strain norm.

For the constrained Oseen descendant `H`, let

\[
G=\nabla H,
\qquad A=GG^T\ge0.
\]

The production is

\[
\boxed{
\mathcal P
=-\int_{\mathbb R^3} S:A\,dx.
}
\]

Hence antisymmetric rotation is absent, and positive Oseen production comes from compressive spectral directions of `S`.

## 2. Spectral positive/negative parts

Write the symmetric trace-free strain as

\[
S=S_+-S_-,
\qquad S_\pm\ge0,
\qquad S_+S_-=0.
\]

Since `A>=0`,

\[
-S:A=S_-:A-S_+:A\le S_-:A.
\]

Therefore

\[
\boxed{
(\mathcal P)_+
\le
\int S_-:A\,dx.
}
\]

This is the correct spectral payer for atom-selected positive production.

## 3. Critical estimate

Use Holder with exponents `(3,6,2)`:

\[
\int S_-:GG^T
\le
\|S_-\|_3\,\|G\|_6\,\|G\|_2.
\]

Sobolev gives

\[
\|G\|_6\lesssim\|\nabla G\|_2
\asymp\|\Delta H\|_2.
\]

Set

\[
\Gamma=\|\nabla H\|_2^2,
\qquad
K=\|\Delta H\|_2^2.
\]

Then

\[
\boxed{
(\mathcal P)_+
\le C\|S_-\|_3\,\Gamma^{1/2}K^{1/2}.
}
\]

Young yields, for any fixed viscosity `nu>0`,

\[
\boxed{
(\mathcal P)_+
\le
\frac\nu2K
+C\nu^{-1}\|S_-\|_3^2\Gamma.
}
\]

Thus if

\[
\int_{t_0}^{T_*}\|S_-(t)\|_3^2dt<\infty,
\]

the Oseen H1 energy inequality gives Gronwall control of `Gamma` and finite delayed second-order action `int K dt` on every late fixed-root descendant.

This contradicts the atom-selected full-tail Oseen saturation/second-order divergence obtained in the preceding atom transfer audits.

Therefore an endpoint kinetic-energy atom requires

\[
\boxed{
\int^{T_*}\|S_-(t)\|_{L_x^3}^2dt=\infty.
}
\]

This is scale critical.

## 4. Consequence for formation/axis decomposition

The correct order of decomposition is now

\[
\boxed{
\text{atom}
\Longrightarrow
\text{compressive spectral strain }S_-
\Longrightarrow
\text{axis-relative decomposition}.
}
\]

One must not infer directly from atom production that each of

\[
\gamma,\quad \tau,\quad D_\perp
\]

is a possible positive payer with equal status.

The negative spectral subspace must first be related to the vorticity axis.

## 5. Two spectral geometries

Let

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

There are two nondegenerate sign patterns:

1. `lambda_2>=0`: two-positive / one-negative strain. The compressive subspace is essentially one-dimensional.
2. `lambda_2<0`: one-positive / two-negative strain. The compressive subspace is two-dimensional.

The first geometry is naturally tied to the existing positive-middle/Betchov ledger.
The second is not; large compression may coexist with `lambda_2^+=0`.

Thus the next rigorous fork is

\[
\boxed{
S_-\text{-action}
\Longrightarrow
[\lambda_2^+\text{ productive sector}]
\ \lor\
[\lambda_2<0\text{ two-dimensional compression sector}].
}
\]

The second sector is the genuinely new axis-analysis target.

## 6. DSD/formation audit

- Formation role: separates the spectral sign-pattern before applying axis descriptors.
- Axis role: only after the sign-pattern is fixed do `gamma`, `tau`, and `D_perp` describe how the vorticity axis sits inside the compressive/expansive eigenspaces.
- Standard mathematics remains decisive: all closure claims must come from the Navier–Stokes/Oseen identities above.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
