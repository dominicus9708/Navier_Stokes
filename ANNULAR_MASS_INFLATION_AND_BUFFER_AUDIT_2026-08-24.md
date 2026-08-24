# Annular Mass Inflation / Buffer Audit — 2026-08-24

Status: **ANTI-PROOF AUDIT OF THE LAST LOCAL-BUFFER ESCAPE / GLOBAL REGULARITY NOT PROVED.**

This note audits the complement `Z_tr > epsilon_b Z_phi` in `LOCALIZED_CORE_ENSTROPHY_TELESCOPING_GATE_2026-08-24.md`. The aim is to avoid relabeling comparable annular vorticity mass as `T` without proof.

## 1. Radial cumulative enstrophy and first-hitting cap

At one dynamically normalized first-hitting snapshot,

\[
\|\Omega\|_\infty\le1.
\]

Around a tracked center `a`, define

\[
M(r):=\int_{B_r(a)}|\Omega|^2dy.
\]

Hence

\[
\boxed{M(r)\le |B_r|=\frac{4\pi}{3}r^3.}
\]

Assume the tracked terminal core supplies a fixed local mass floor

\[
\boxed{M(R_0)\ge m_0>0.}
\]

## 2. Consecutive comparable annuli cannot continue arbitrarily when the radial factor is thin enough

Fix `epsilon>0` and `lambda>1`. Suppose for `n=0,...,N-1`,

\[
M(\lambda^{n+1}R_0)-M(\lambda^nR_0)
\ge \epsilon M(\lambda^nR_0).
\]

Then

\[
M(\lambda^nR_0)\ge (1+\epsilon)^n m_0.
\]

The pointwise first-hitting cap gives simultaneously

\[
M(\lambda^nR_0)
\le \frac{4\pi}{3}R_0^3\lambda^{3n}.
\]

Therefore, if

\[
\boxed{\lambda^3<1+\epsilon,}
\]

then

\[
\left(\frac{1+\epsilon}{\lambda^3}\right)^n
\le
\frac{4\pi R_0^3}{3m_0}.
\]

Consequently the number of consecutive `epsilon`-comparable annuli is uniformly bounded by

\[
\boxed{
N_*
:=1+
\left\lceil
\frac{
\log\left(\frac{4\pi R_0^3}{3m_0}\right)
}{
\log\left(\frac{1+\epsilon}{\lambda^3}\right)
}
\right\rceil.
}
\]

Thus at each first-hitting snapshot there is a shell among the first `N_*` thin radial enlargements for which

\[
\boxed{
M(\lambda r)-M(r)<\epsilon M(r).
}
\]

This conclusion is independent of the total normalized enstrophy and therefore remains valid on a globally non-tight branch.

## 3. Important audit: the thin quiet shell does not by itself imply the previous H1 Dirichlet frequency floor

For a cutoff equal to one on `B_r`, vanishing outside `B_{\lambda r}`, and satisfying

\[
|\nabla\psi|\lesssim[(\lambda-1)r]^{-1},
\]

the elementary triangle/Dirichlet estimate has the schematic sharp form

\[
\sqrt{Q_\phi/Z_\phi}
\ge
\frac1r
\left[
\frac\pi\lambda
-
\frac{\sqrt\epsilon}{\lambda-1}
\right]_+.
\]

A positive lower bound therefore requires

\[
\epsilon
<
\pi^2\frac{(\lambda-1)^2}{\lambda^2}.
\]

The volume-growth argument of Section 2 requires instead

\[
\epsilon>\lambda^3-1.
\]

These two inequalities cannot hold simultaneously for any `lambda>1`. Indeed they would imply

\[
\lambda^2+\lambda+1
<
\pi^2\frac{\lambda-1}{\lambda^2},
\]

but

\[
\pi^2\frac{\lambda-1}{\lambda^2}
\le\frac{\pi^2}{4}<3
\le\lambda^2+\lambda+1.
\]

Hence

\[
\boxed{
\text{amplitude cap + radial mass growth alone}
\not\Rightarrow
\text{positive localized H1 frequency floor}.
}
\]

This closes an anti-proof loophole: a nearly constant-vorticity plateau is a genuine static counterexample to that attempted implication.

## 4. The correct static dichotomy is derivative versus coherent plateau

Let `D` be a fixed-shape bounded connected region of diameter `O(R)`, such as a ball or a finite-thickness annulus. Let

\[
Z_D=\int_D|\Omega|^2,
\qquad
Q_D=\int_D|\nabla\Omega|^2,
\qquad
\bar\Omega_D=|D|^{-1}\int_D\Omega.
\]

Poincare gives

\[
\boxed{
\int_D|\Omega-\bar\Omega_D|^2
\le C_D R^2Q_D.
}
\]

Therefore either

\[
\boxed{R^2Q_D\ge\theta Z_D}
\]

for a chosen fixed `theta>0`, which is a local derivative/viscous-frequency cost, or

\[
R^2Q_D<\theta Z_D
\]

and

\[
\boxed{
|D|\,|\bar\Omega_D|^2
\ge
(1-C_D\theta)Z_D.
}
\]

For `C_D theta<1`, the second alternative has a nonzero mean vorticity vector and is a **coherent vorticity plateau**, not a multicore label by definition.

## 5. Why a plateau is a dynamical rather than a static obstruction

A spatially almost constant vorticity packet can carry large annular `L2` mass while paying little instantaneous derivative cost. Therefore it cannot be excluded from a single snapshot.

However a dynamically normalized first-hitting stage changes the reference vorticity scale by `q`. If the same coherent plateau reappears with comparable normalized mean amplitude at the next checkpoint, its physical mean vorticity has had to follow the first-hitting amplification. This requires stretching or boundary/rebuild action.

The exact mean-vorticity ledger is derived separately in

`MEAN_VORTICITY_PLATEAU_STAGE_LEDGER_2026-08-24.md`.

Thus the corrected annular branch is

\[
\boxed{
\text{comparable annular mass}
\Longrightarrow
\text{local derivative cost}
\lor
\text{coherent mean-vorticity plateau}.
}
\]

The plateau then enters a finite-stage stretching/deformation/turnover ledger rather than being declared `T` statically.

Status: **THE REPEATED ANNULAR-MASS AUDIT FINDS A UNIFORM THIN-SHELL MASS-GROWTH BOUND, BUT ALSO PROVES THAT THIS BOUND CANNOT BY ITSELF SUPPLY THE H1 DIRICHLET FREQUENCY FLOOR USED IN THE LOCAL TELESCOPE. THE TRUE LOW-DERIVATIVE SURVIVOR IS A COHERENT VORTICITY PLATEAU. THIS SURVIVOR MUST BE HANDLED DYNAMICALLY THROUGH ITS MEAN-VORTICITY AMPLIFICATION, NOT BY STATIC MULTICORE LABELING. GLOBAL REGULARITY REMAINS UNPROVED.**