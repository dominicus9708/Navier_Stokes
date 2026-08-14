# First-hitting logistic enstrophy ceiling

Date: 2026-08-14

Status: **EXACT ENSTROPHY/ENERGY LOGISTIC INEQUALITY + PREVIOUS-CHECKPOINT GLOBAL ENSTROPHY IMPROVEMENT**.

## 1. Global normalized quantities

Let `U` be a smooth whole-space incompressible Navier--Stokes solution on a first-hitting interval, with vorticity `Omega=curl U`. Define

\[
K(s)=\|U(s)\|_2^2,
\qquad
E(s)=\|\Omega(s)\|_2^2,
\qquad
P(s)=\|\nabla\Omega(s)\|_2^2.
\]

Kinetic energy is nonincreasing, so

\[
K(s)\le K_0.
\]

## 2. Fourier interpolation

For divergence-free `U`,

\[
E=\|\nabla U\|_2^2.
\]

Fourier Cauchy--Schwarz gives

\[
\begin{aligned}
E^2
&=
\left(
\int |\xi|^2|\widehat U(\xi)|^2d\xi
\right)^2\\
&\le
\left(
\int|\widehat U|^2
\right)
\left(
\int|\xi|^4|\widehat U|^2
\right).
\end{aligned}
\]

For divergence-free fields the last factor is equivalent to `P`, hence

\[
\boxed{
E^2\le K_0P.
}
\]

## 3. Stretching bound under an L-infinity vorticity cap

The enstrophy identity is

\[
\frac12E'+\nu P
=\int S\Omega\cdot\Omega\,dx.
\]

Using the L2 Calderon--Zygmund bound `||S||_2 <= C ||Omega||_2` and

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2,
\]

we obtain

\[
\left|
\int S\Omega\cdot\Omega
\right|
\le
C\|\Omega\|_\infty E.
\]

Therefore, on any interval where

\[
\|\Omega\|_\infty\le m,
\]

we have

\[
\boxed{
E'
+\frac{2\nu}{K_0}E^2
\le
C m E.
}
\]

This is a logistic upper differential inequality.

## 4. Relaxation ceiling

Compare with

\[
y'=amy-by^2,
\qquad
b=2\nu/K_0.
\]

After an interval of length comparable to `1/m`, independently of a larger earlier value,

\[
\boxed{
E(s)\le C_\nu mK_0
}
\]

up to an exponentially decaying memory of the initial enstrophy.

Thus a first-hitting vorticity cap which has persisted for at least one natural vorticity time forces a global enstrophy ceiling proportional to `m` times kinetic energy.

## 5. Apply at the adaptive previous checkpoint

In terminal first-hitting coordinates,

\[
\|\Omega\|_\infty\le1,
\]

and at the previous adaptive first-hitting threshold

\[
m=q^{-1},
\qquad
q=W^{1/3+2\varepsilon}.
\]

Because this is a first hitting, all sufficiently earlier normalized times satisfy `||Omega||_infty <= q^{-1}`. The physical history before that checkpoint has terminal-normalized duration much larger than `q`, so the logistic relaxation time is available on the blow-up sequence.

The terminal-normalized kinetic energy is

\[
K_0
=W^{1/2}\|u_0\|_2^2.
\]

Hence at the previous checkpoint

\[
\boxed{
E_-
:=\|\Omega(s_-)\|_2^2
\lesssim_\nu
\frac{W^{1/2}}{q}\|u_0\|_2^2.
}
\]

With the chosen `q`,

\[
\boxed{
E_-
\lesssim
W^{1/6-2\varepsilon}
}
\]

up to fixed initial-energy/viscosity constants.

## 6. Shell-density consequence

The previous checkpoint natural radius in terminal coordinates is

\[
R_-=\sqrt q
=W^{1/6+\varepsilon}.
\]

Partition `1 <= |y| <= R_-` into unit-width annuli. There are `N asymp R_-` such annuli. Their total vorticity-square mass is at most `E_-`, so the average annular enstrophy is

\[
\frac{E_-}{R_-}
\lesssim
W^{1/2}q^{-3/2}.
\]

For `q=W^{1/3+2varepsilon}`,

\[
\boxed{
\frac{E_-}{R_-}
\lesssim
W^{-3\varepsilon}.
}
\]

Consequently a positive fraction of the unit-width shells up to the previous natural radius have enstrophy mass `O(W^{-3varepsilon})`.

This gives a much stronger initial buffer statement than the earlier finite-shell selector, which assumed only a generic bounded normalized enstrophy.

## 7. Interpretation of the q exponent

For a general power `q=W^alpha`, the average previous-checkpoint shell mass scales as

\[
W^{1/2-3\alpha/2}.
\]

It decays precisely when

\[
\boxed{\alpha>1/3.}
\]

Thus the adaptive choice slightly above the `W^{1/3}` threshold has a second interpretation: besides matching the residual-memory scale, it creates a sparse family of low-enstrophy unit shells at the previous checkpoint.

## 8. Limitation

These low-enstrophy shells are guaranteed at the previous checkpoint, not throughout the entire later adaptive interval. A later transport cascade may fill them. Turning the initial shell density into a spacetime barrier requires a buffer-filling estimate: either the shell remains low and suppresses transport, or raising its enstrophy must be charged to stretching, incoming flux, or palinstrophy.

Status: **PREVIOUS-CHECKPOINT GLOBAL ENSTROPHY AND SHELL DENSITY SHARPENED / DYNAMIC BUFFER-FILLING COST OPEN**.
