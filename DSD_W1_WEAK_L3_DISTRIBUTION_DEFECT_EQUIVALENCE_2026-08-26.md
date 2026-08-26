# DSD W1 Weak-L3 Distribution Defect Audit

Date: 2026-08-26

Status: **CORRECTED / GENERAL W1 ENDPOINT GIVES A POSITIVE ABEL--CESARO LOW-AMPLITUDE DEFECT; POINTWISE LIMIT `lambda^3 N(lambda)` REQUIRES AN ADDITIONAL TAUBERIAN OR REGULAR-VARIATION HYPOTHESIS / EXACT `1/r` AND PERIODIC-COHERENT REGIMES MAY RECOVER THE POINTWISE COEFFICIENT / GLOBAL REGULARITY UNPROVED.**

## 1. Distribution variables

For a W1 state `U`, write

\[
a=|U|,
\qquad
N(\lambda)=|\{Y:a(Y)>\lambda\}|,
\]

and

\[
\mathcal E_\lambda
=\frac12\int (a^2-\lambda^2)_+\,dY
=\int_\lambda^\infty \mu N(\mu)\,d\mu.
\]

Define

\[
K(\lambda)=\lambda\mathcal E_\lambda.
\]

For a pure critical model

\[
N(\lambda)\sim C_3\lambda^{-3},
\]

one has

\[
K(\lambda)\to C_3.
\]

Thus, **if** the pointwise weak-`L3` coefficient exists, then

\[
\lim_{\lambda\downarrow0}\lambda^3N(\lambda)
=
\lim_{\lambda\downarrow0}K(\lambda).
\]

## 2. What the `p downarrow 3` residue actually proves

The robust W1 endpoint quantity is

\[
\mathscr R_3
:=
\lim_{\varepsilon\downarrow0}
\varepsilon\int |U|^{3+\varepsilon}\,dY,
\]

or its invariant-measure version.

Using layer cake,

\[
\int |U|^{3+\varepsilon}
=(3+\varepsilon)
\int_0^\infty
\lambda^{2+\varepsilon}N(\lambda)\,d\lambda.
\]

Hence `mathscr R_3` is a Mellin/Abel residue of the low-amplitude distribution. It measures a **logarithmic average density** of

\[
C(\lambda):=\lambda^3N(\lambda),
\]

not, by itself, the pointwise limit of `C(lambda)`.

Therefore the implication

\[
\mathscr R_3>0
\quad\Longrightarrow\quad
\lim_{\lambda\downarrow0}\lambda^3N(\lambda)
=\frac{\mathscr R_3}{3}
\]

is **not valid without an additional Tauberian hypothesis** such as suitable regular variation, asymptotic monotonicity, or an exact/coherent tail representation.

## 3. Correct general endpoint object

For the general recurrent W1 endpoint define the defect at the Abel--Cesaro level:

\[
\boxed{
\mathscr C^{A}_{WL3}
:=
\frac{\mathscr R_3}{3}>0.
}
\]

This notation means: the low-amplitude distribution has a nonzero logarithmic/Abelian critical density. It does **not** assert that

\[
\lambda^3N(\lambda)
\]

has a pointwise limit.

One still obtains a genuine large weak-`L3` conclusion at the level needed for the existing endpoint audit: positive Abel density forces nontrivial critical distribution on arbitrarily small amplitude scales and therefore a nonzero `L^{3,\infty}` lower envelope along a sequence of levels.

## 4. Exact-tail regimes

If an additional tail theorem yields

\[
U(Y)=|Y|^{-1}\Phi(\widehat Y,\log|Y|)+o(|Y|^{-1})
\]

with sufficient regularity/periodicity or regular variation, then a Tauberian upgrade is available and one may define

\[
\mathscr C_{WL3}
:=
\lim_{\lambda\downarrow0}\lambda^3N(\lambda).
\]

For the isotropic model `U=A/|Y|`,

\[
\lambda^3N(\lambda)
=\frac{4\pi}{3}A^3,
\qquad
\mathscr R_3=4\pi A^3,
\]

so

\[
\boxed{
\mathscr C_{WL3}=\frac{\mathscr R_3}{3}.
}
\]

This exact coefficient relation therefore remains valid in the exact-tail/regular-variation lane, but it is **not** a theorem of the general W1 lane solely from the Mellin residue.

## 5. Fixed prelimit states

At every finite Leray time the physical finite-energy solution gives `U(s) in L2`, so

\[
N_s(\lambda)
\le \lambda^{-2}\|U(s)\|_2^2,
\]

and therefore

\[
\lambda^3N_s(\lambda)
\to0
\qquad(\lambda\downarrow0).
\]

Likewise

\[
K_s(\lambda)=\lambda\mathcal E_{\lambda,s}\to0.
\]

The W1 obstruction is therefore still a genuine **loss of critical low-amplitude tightness** under the noncompact Leray limit, but in the general lane that loss must be stated in Abel--Cesaro form rather than as an automatically existing pointwise coefficient.

## 6. DSD audit consequence

The correct hierarchy is

\[
\boxed{
\text{positive log-shell cubic density}
\Longleftrightarrow
\mathscr R_3>0
\Longleftrightarrow
\text{positive Abel--Cesaro low-amplitude defect}.
}
\]

Only with an additional Tauberian bridge may one append

\[
\Longleftrightarrow
\lim_{\lambda\downarrow0}\lambda^3N(\lambda)>0.
\]

This correction prevents the proof tree from using a pointwise weak-`L3` boundary coefficient where only an averaged endpoint residue has actually been established.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
