# DSD M5-503 — Remote palinstrophy escape forces a remote shell scale-frequency defect

Date: 2026-09-01

Status: **REMOTE-P SHARPENING / M5-502 SHOWS THAT UNBOUNDED SIMILARITY PALINSTROPHY CANNOT OCCUR ON ANY FIXED BALL / BECAUSE TOTAL SIMILARITY ENSTROPHY REMAINS UNIFORMLY BOUNDED, A DYADIC SHELL DECOMPOSITION FORCES SOME REMOTE SHELL TO HAVE AN UNBOUNDED DIMENSIONLESS DERIVATIVE-TO-ENSTROPHY RATIO / EQUIVALENTLY THE INTRINSIC VORTICITY VARIATION LENGTH BECOMES NEGLIGIBLE RELATIVE TO THE SHELL RADIUS / THUS `H_tail^(remote-P)` IS NOT MERELY REMOTE OCCUPANCY: IT CONTAINS A GENUINE REMOTE SCALE-FREQUENCY DEFECT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-502

Along the unbounded-palinstrophy branch there is a sequence of similarity states/times `theta_j` such that

\[
P(\theta_j)
=
\int_{\mathbb R^3}|\nabla W(y,\theta_j)|^2dy
\to\infty.
\]

For every fixed `R`, local smooth compactness gives

\[
\int_{|y|\le R}|\nabla W(y,\theta_j)|^2dy
\le C_R,
\]

hence

\[
\int_{|y|>R}|\nabla W(y,\theta_j)|^2dy
\to\infty.
\]

The similarity enstrophy remains uniformly bounded:

\[
E(\theta)
=
\int_{\mathbb R^3}|W(y,\theta)|^2dy
\le Z_*<\infty.
\]

---

## 2. Diagonal choice of remote radii

Choose any sequence

\[
R_n\to\infty.
\]

By the M5-502 exterior divergence, after a diagonal subsequence of the palinstrophy-divergent states we may arrange

\[
\boxed{
P_{ext}(R_n,\theta_n)
:=
\int_{|y|>R_n}|\nabla W(y,\theta_n)|^2dy
\ge n.
}
\]

Thus the derivative escape occurs beyond radii tending to infinity, not merely beyond one fixed ball.

---

## 3. Dyadic shell ledger

For each `n`, decompose the exterior into shells

\[
A_{n,k}
:=
\{2^kR_n<|y|<2^{k+1}R_n\},
\qquad k\ge0.
\]

Define

\[
E_{n,k}
:=
\int_{A_{n,k}}|W|^2dy,
\]

and

\[
P_{n,k}
:=
\int_{A_{n,k}}|\nabla W|^2dy.
\]

Then

\[
\sum_{k\ge0}E_{n,k}
\le Z_*,
\]

while

\[
\sum_{k\ge0}P_{n,k}
=
P_{ext}(R_n,\theta_n)
\ge n.
\]

If `E_{n,k}=0`, then `W=0` almost everywhere on that open shell and consequently `P_{n,k}=0`; such shells may be omitted from the quotient below.

---

## 4. Dimensionless shell-frequency quotient

Let

\[
r_{n,k}:=2^kR_n.
\]

For every shell with `E_{n,k}>0`, define

\[
\boxed{
\Lambda_{n,k}
:=
r_{n,k}^2
\frac{P_{n,k}}{E_{n,k}}.
}
\]

This is the natural dimensionless derivative-to-amplitude ratio of the shell.

If

\[
\Lambda_n^{sup}
:=
\sup_{k:E_{n,k}>0}\Lambda_{n,k},
\]

then

\[
P_{n,k}
=
\frac{\Lambda_{n,k}}{r_{n,k}^2}E_{n,k}
\le
\frac{\Lambda_n^{sup}}{R_n^2}E_{n,k}.
\]

Summing over `k`,

\[
P_{ext}(R_n,\theta_n)
\le
\frac{\Lambda_n^{sup}}{R_n^2}
\sum_{k\ge0}E_{n,k}
\le
\frac{\Lambda_n^{sup}}{R_n^2}Z_*.
\]

Therefore

\[
\boxed{
\Lambda_n^{sup}
\ge
\frac{R_n^2}{Z_*}
P_{ext}(R_n,\theta_n).
}
\]

Using `P_ext >= n`,

\[
\boxed{
\Lambda_n^{sup}
\ge
\frac{nR_n^2}{Z_*}
\to\infty.
}
\]

Hence there are shell indices `k_n` such that

\[
\boxed{
\Lambda_{n,k_n}\to\infty.
}
\]

Their radii

\[
\rho_n:=2^{k_n}R_n
\]

also satisfy

\[
\rho_n\to\infty.
\]

---

## 5. Intrinsic variation scale

Define the shell intrinsic derivative length

\[
\ell_n
:=
\left(
\frac{E_{n,k_n}}{P_{n,k_n}}
\right)^{1/2}.
\]

Then

\[
\frac{\ell_n}{\rho_n}
=
\Lambda_{n,k_n}^{-1/2}.
\]

Thus

\[
\boxed{
\frac{\ell_n}{\rho_n}
\to0.
}
\]

The vorticity varies on a scale asymptotically much smaller than the radius of the remote shell carrying it.

This is stronger than radial mass escape.

It is a genuine scale separation:

\[
\boxed{
\text{remote radius}
\gg
\text{intrinsic derivative length}.
}
\]

---

## 6. Unit-annulus normalization

Set

\[
z=\frac{y}{\rho_n}
\]

and consider the shell profile

\[
F_n(z)
:=
W(\rho_n z,\theta_n),
\qquad 1<|z|<2.
\]

Then

\[
\|F_n\|_{L^2(A_{1,2})}^2
=
\rho_n^{-3}E_{n,k_n},
\]

and

\[
\|\nabla_zF_n\|_{L^2(A_{1,2})}^2
=
\rho_n^{-1}P_{n,k_n}.
\]

Therefore

\[
\boxed{
\frac{\|\nabla_zF_n\|_2^2}
{\|F_n\|_2^2}
=
\rho_n^2
\frac{P_{n,k_n}}{E_{n,k_n}}
=
\Lambda_{n,k_n}
\to\infty.
}
\]

If we normalize only for diagnostic purposes by

\[
G_n
:=
\frac{F_n}{\|F_n\|_2},
\]

then

\[
\|G_n\|_2=1,
\qquad
\|\nabla G_n\|_2^2\to\infty.
\]

Thus the remote-P branch contains an explicit fixed-annulus frequency defect after shell normalization.

---

## 7. DSD firewall: diagnostic normalization is not a new NS solution

The amplitude normalization used in `G_n` is only a compactness/frequency diagnostic.

It is **not** an admissible Navier--Stokes scaling and must not be treated as producing another NS solution.

Likewise, the shell quotient proves a scale-frequency defect but does not yet prove

- concentration at one point of the shell;
- a nonzero recentered ancient bubble;
- a Fourier-supported monochromatic packet;
- or direct convergence to the M5-481 terminal Dirichlet profile.

Those are stronger assertions requiring additional compactness or transport arguments.

---

## 8. Exact remote-frequency branch

Define

\[
\boxed{
H_{tail}^{remote-F}
:
\quad
\exists\rho_n\to\infty
\text{ and remote shells }A_{\rho_n,2\rho_n}
\]

such that

\[
\boxed{
\rho_n^2
\frac{
\int_{A_{\rho_n,2\rho_n}}|\nabla W|^2dy
}{
\int_{A_{\rho_n,2\rho_n}}|W|^2dy
}
\to\infty.
}
\]

Then M5-502 sharpens to

\[
\boxed{
H_{tail}^{remote-P}
\Longrightarrow
H_{tail}^{remote-F}.
}
\]

Equivalently, a uniformly bounded remote shell-frequency quotient would imply

\[
P_{ext}(R)
\lesssim
R^{-2}E_{ext}(R),
\]

and therefore would make an unbounded remote-P escape impossible under the enstrophy cap.

---

## 9. Relation to the terminal Dirichlet genealogy

M5-481--483 force a nontrivial scale-critical terminal Dirichlet/dilation structure on the bounded terminal corridor.

M5-503 now shows that the interior remote-P escape has a different but closely related scale statement:

\[
\boxed{
\text{terminal branch: critical shell derivative occupancy}
}
\]

versus

\[
\boxed{
\text{remote-P branch: supercritical shell derivative/enstrophy frequency ratio}.
}
\]

The two are not yet identified.

A future bridge must transport or compare the remote interior shell structure across similarity time to the terminal blow-down genealogy.

---

## 10. Updated projected-diffusion branch

M5-501--503 give

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-F}
\lor
\mathcal C_{bounded-P}^{proj},
}
\]

where the bounded-P survivor obeys the quantitative M5-501 thresholds

\[
Z_*P_*\ge K_{EP},
\]

and

\[
P_*\ge P_{min}^{proj}(Z_*,h_{proj}).
\]

Thus the unbounded branch is no longer an untyped global palinstrophy escalation.

It is a remote geometric-scale/frequency defect.

---

## 11. Highest-value next target

The shell quotient suggests an all-derivative audit.

Since

\[
E=\|W\|_2^2
\]

is uniformly bounded while

\[
P=\|\nabla W\|_2^2
\to\infty,
\]

Fourier moment interpolation should determine whether every higher Sobolev derivative necessarily escalates along the same sequence.

If so, M5-503's remote-frequency defect would become an explicit infinite Sobolev-cascade endpoint rather than only a first-derivative defect.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
