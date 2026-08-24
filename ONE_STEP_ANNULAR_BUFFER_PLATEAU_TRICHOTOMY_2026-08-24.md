# One-Step Annular Buffer / Plateau Trichotomy — 2026-08-24

Status: **ONE-STEP LOCAL REDUCTION OF THE ANNULAR-MASS COMPLEMENT / GLOBAL REGULARITY NOT PROVED.**

This note combines the localized enstrophy gate with the annular-mass audit and mean-vorticity plateau ledger. The purpose is to avoid a long radial recursion: a single comparison between `B_R` and `B_{2R}` already gives a useful three-way split.

## 1. Core and first transition annulus

At a normalized first-hitting time define

\[
Z_C:=\int_{B_R(a)}|\Omega|^2dy,
\qquad
Z_A:=\int_{B_{2R}(a)\setminus B_R(a)}|\Omega|^2dy.
\]

Assume the retained terminal core supplies

\[
\boxed{Z_C\ge z_*>0.}
\]

The first-hitting cap is

\[
\|\Omega\|_\infty\le1.
\]

## 2. Case A: first annulus no larger than the core

Choose a cutoff `psi` equal to one on `B_R`, zero outside `B_{2R}`, with

\[
|\nabla\psi|\le R^{-1},
\qquad
\phi=\psi^2.
\]

Then

\[
Z_\phi=\|\psi\Omega\|_2^2\ge Z_C.
\]

If

\[
\boxed{Z_A\le Z_C,}
\]

then

\[
Z_A/Z_\phi\le1.
\]

The Dirichlet eigenvalue of `B_{2R}` and the triangle inequality give

\[
\frac\pi{2R}\sqrt{Z_\phi}
\le
\|\nabla(\psi\Omega)\|_2
\le
\sqrt{Q_\phi}+R^{-1}\sqrt{Z_A}.
\]

Hence

\[
\boxed{
\frac{Q_\phi}{Z_\phi}
\ge
\frac{\Lambda_{2,1}}{R^2},
\qquad
\Lambda_{2,1}:=\left(\frac\pi2-1\right)^2.
}
\]

Numerically,

\[
\boxed{\Lambda_{2,1}\approx0.3258084467.}
\]

Thus even a transition annulus carrying as much enstrophy as the core still leaves a positive local frequency floor when the cutoff factor is two.

Inserted into `LOCALIZED_CORE_ENSTROPHY_TELESCOPING_GATE_2026-08-24.md`, this gives the explicit quiet-buffer certificate

\[
\boxed{
\left[
C_{prod}(\beta_S)+f_b
-(1-\eta_b)\nu\frac{\Lambda_{2,1}}{R^2}
\right]_+
L_{stage,+}
<\frac14\log q.
}
\]

In the ideal zero-buffer-error benchmark, the timing-independent radius is

\[
\boxed{
R
\le
\sqrt{\sqrt3\,\Lambda_{2,1}\,\nu}
\approx0.7512102124\sqrt\nu.
}
\]

## 3. Case B: first annulus exceeds the core

Suppose instead

\[
\boxed{Z_A>Z_C.}
\]

Then on the doubled ball `D=B_{2R}(a)`,

\[
Z_D:=\int_D|\Omega|^2>Z_C+Z_A>2z_*.
\]

Let

\[
Q_D:=\int_D|\nabla\Omega|^2.
\]

By Payne--Weinberger on the ball of diameter `4R`,

\[
\boxed{
\int_D|\Omega-\bar\Omega_D|^2
\le
\frac{16R^2}{\pi^2}Q_D,
}
\]

where

\[
\bar\Omega_D=|D|^{-1}\int_D\Omega.
\]

Fix a coherence fraction `0<delta<1`. Then either

\[
\boxed{
\frac{R^2Q_D}{Z_D}
\ge
\frac{\delta\pi^2}{16},
}
\]

which is a fixed local derivative/frequency tax, or

\[
\frac{R^2Q_D}{Z_D}<\frac{\delta\pi^2}{16}
\]

and therefore

\[
\boxed{
|D|\,|\bar\Omega_D|^2
\ge
(1-\delta)Z_D
>
2(1-\delta)z_*.
}
\]

The second branch is a quantitatively nonzero mean-vorticity plateau.

For example, if the initial thick core has

\[
Z_C\ge\frac14|B_R|
\]

and choose `delta=1/2`, then `Z_D>|B_R|/2=|B_{2R}|/16`, so

\[
\boxed{
|\bar\Omega_D|^2>\frac1{32},
\qquad
|\bar\Omega_D|>\frac1{4\sqrt2}\approx0.1767766953.
}
\]

Thus the low-derivative complement cannot have a vanishing mean direction.

## 4. Dynamic interpretation of Case B

A fixed local derivative tax is not automatically labeled `H`; it contributes to the existing local palinstrophy/frequency ledger and, if repeated with positive time density, to the viscous logarithmic floor.

The low-derivative complement is the coherent plateau treated by

`MEAN_VORTICITY_PLATEAU_STAGE_LEDGER_2026-08-24.md`.

If the plateau mean is retained through a first-hitting stage and its transport/diffusive/covariance errors are small, it must satisfy

\[
\boxed{
\int_{I_j}
n^T\bar\Sigma n\,ds
\gtrsim\log q.
}
\]

Hence it enters the existing coherent deformation/projective corridor and has the stage-length floor

\[
\boxed{
L_j\gtrsim\frac{\log q}{B_{\Sigma,+}}
}
\]

up to the explicit mean-vorticity error action.

If the plateau mean is not retained, the loss/rebuild is paid by relative material transport, diffusion, derivative action, or strain-vorticity covariance, all explicitly present in the mean ledger.

## 5. Corrected local frontier

The first annular complement therefore has the standard-mathematical trichotomy

\[
\boxed{
\begin{aligned}
Z_A\le Z_C
&\Longrightarrow
\text{positive local H1 frequency floor},\\
Z_A>Z_C\ \&\text{and local derivative ratio large}
\Longrightarrow
\text{local frequency/palinstrophy tax},\\
Z_A>Z_C\ \&\text{and local derivative ratio small}
\Longrightarrow
\text{coherent mean-vorticity plateau}\to\text{deformation/rebuild ledger}.
\end{aligned}
}
\]

Thus `large transition-annulus mass` is no longer an independent static branch and is not automatically called multicore turnover.

What remains quantitative is to compare the derivative-tax persistence and the plateau deformation floor with the existing finite-stage upper-time/variance constants.

Status: **A SINGLE DOUBLING-SCALE TEST REDUCES THE LOCAL ANNULAR-MASS COMPLEMENT TO (I) AN EXPLICIT FREQUENCY FLOOR WITH CONSTANT `(pi/2-1)^2`, (II) A LOCAL DERIVATIVE/FREQUENCY TAX, OR (III) A COHERENT MEAN-VORTICITY PLATEAU THAT MUST PAY APPROXIMATELY `log q` OF LONGITUDINAL STRAIN ACTION PER RETAINED STAGE. THE ANNULAR-MASS ESCAPE IS NO LONGER AN UNTYPED PROOF-TREE LEAF, BUT THE FINAL CONSTANT COMPARISONS REMAIN OPEN. GLOBAL REGULARITY REMAINS UNPROVED.**