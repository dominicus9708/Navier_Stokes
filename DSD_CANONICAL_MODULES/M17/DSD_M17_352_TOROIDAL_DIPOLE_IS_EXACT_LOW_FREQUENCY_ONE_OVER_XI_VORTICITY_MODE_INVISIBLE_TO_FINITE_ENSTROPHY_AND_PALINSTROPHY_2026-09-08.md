# DSD M17-352 — The toroidal dipole is the exact low-frequency `1/|xi|` vorticity mode invisible to finite enstrophy and palinstrophy

Date: 2026-09-08  
Canonical ID: **M17-352**

Status: **ACTIVE LOW-FREQUENCY IDENTIFICATION / M17-351 TAIL PARAMETER**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Dipole tail

M17-350--351 reduce the harmonic weak-critical exterior branch to

\[
\boxed{
\Omega_{dip}(x)
=
\frac{a_*\times x}{|x|^3},
\qquad
a_*\ne0,
}
\]

up to lower multipoles.

The vector `a_*` is constant in time on the coherent harmonic-tail branch and invariant under Navier--Stokes parabolic scaling.

## 2. Fourier transform of the vorticity dipole

Use

\[
\frac{x}{|x|^3}
=-\nabla\frac1{|x|}.
\]

With the standard Fourier convention in which

\[
\widehat{|x|^{-1}}(\xi)
=4\pi|\xi|^{-2}
\]

up to the fixed transform normalization, we get

\[
\boxed{
\widehat\Omega_{dip}(\xi)
=
-4\pi i
\frac{a_*\times\xi}{|\xi|^2}
}
\]

up to the same convention constant.

Hence near zero frequency,

\[
\boxed{
|\widehat\Omega_{dip}(\xi)|
\asymp
\frac{|a_*\times\hat\xi|}{|\xi|}.
}
\]

Thus the toroidal harmonic tail is exactly a `1/|xi|` low-frequency vorticity singularity.

## 3. Corresponding velocity singularity

For divergence-free velocity,

\[
\widehat V(\xi)
=
\frac{i\xi\times\widehat\Omega(\xi)}{|\xi|^2}.
\]

Insert the dipole term:

\[
\begin{aligned}
\widehat V_{dip}(\xi)
&\propto
\frac{\xi\times(a_*\times\xi)}{|\xi|^4}\\
&=
\frac{|\xi|^2a_*-(a_*\cdot\xi)\xi}{|\xi|^4}.
\end{aligned}
\]

Therefore

\[
\boxed{
\widehat V_{dip}(\xi)
\propto
\frac{P_{\xi^\perp}a_*}{|\xi|^2}.
}
\]

This is the Fourier signature of a physical `1/r` velocity tail.

## 4. Why finite enstrophy allows the mode

Near `xi=0`,

\[
|\widehat\Omega_{dip}|^2\sim|\xi|^{-2}.
\]

The three-dimensional Fourier volume element is

\[
d\xi\sim r^2drd\omega.
\]

Hence the low-frequency enstrophy contribution behaves like

\[
\int_0^\varepsilon r^2r^{-2}dr
\sim\varepsilon<\infty.
\]

Thus

\[
\boxed{
\Omega_{dip}\in L^2
}
\]

at the low-frequency level is completely compatible with M5-477 finite enstrophy.

## 5. Why finite palinstrophy is even less sensitive to it

The palinstrophy Fourier density has the additional factor `|xi|^2`:

\[
|\xi|^2|\widehat\Omega_{dip}|^2
\sim1.
\]

Therefore

\[
\int_{|\xi|<\varepsilon}
|\xi|^2|\widehat\Omega_{dip}|^2d\xi
\sim
\int_0^\varepsilon r^2dr
=O(\varepsilon^3).
\]

Hence the dipole is extremely cheap in the palinstrophy ledger at low frequency.

This explains structurally why M5-477 finite total palinstrophy and M17-307's weighted ancestral budget do not remove the weak-critical tail.

## 6. Why it blocks strong L3 velocity

The velocity mode behaves as

\[
|\widehat V_{dip}|\sim|\xi|^{-2}
\]

near zero frequency, corresponding to physical decay

\[
|V_{dip}(x)|\sim|x|^{-1}.
\]

A `1/r` tail lies at the weak `L3` endpoint and fails strong global `L3` logarithmically.

Thus the one vector `a_*` is exactly the obstruction separating

\[
\boxed{
V\in L^{3,\infty}_{weak}
}
\]

from the strong-`L3` gate of M17-347 on the harmonic tail branch.

## 7. Strong-L3 branch in Fourier language

If

\[
a_*=0,
\]

then the `1/|xi|` vorticity singularity is absent.

The harmonic tail starts one multipole lower, M17-350 gives

\[
\Omega\in L^{3/2},
\]

and hence

\[
V\in L^3.
\]

Equivalently, the strong-tail problem is reduced to proving the cancellation of one explicit low-frequency coefficient.

## 8. New ancestry target

The next question can now be stated in either physical or Fourier form:

\[
\boxed{
 a_*=0?
}
\]

or equivalently

\[
\boxed{
\lim_{\xi\to0}
|\xi|\,\widehat\Omega(\xi)
\text{ has no toroidal }a_*\times\hat\xi\text{ component}.
}
\]

A closing ancestry theorem would need to show that the first-hitting/finite-energy prelimit cannot generate this singular low-frequency coefficient in the ancient blow-up limit, or that retaining it forces a named winding/genealogy escape.

## 9. DSD-theory role

The useful heuristic is to identify the exact external/low-frequency structural channel rather than repeatedly testing high-frequency finite resources against it.

The derivation is standard Fourier/Biot--Savart analysis.

No DSD axiom enters the PDE proof.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
