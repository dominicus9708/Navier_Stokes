# DSD M17-197 — Bulk strain, amplitude, and director payers collapse to one vorticity-palinstrophy occupancy

Date: 2026-09-06  
Canonical ID: **M17-197**

Status: **BULK PAYER COMPRESSION / ON A REGULAR SIMPLE-EIGENVALUE GREAT-CIRCLE BRANCH, `partial_j sigma = xi^T (partial_j Sigma) xi`, HENCE `|grad sigma| <= |grad Sigma|`. FOR DIVERGENCE-FREE VELOCITY, FOURIER ALGEBRA GIVES THE EXACT GLOBAL IDENTITY `||grad Sigma||_2^2 = (1/2)||grad W||_2^2`. TOGETHER WITH `|grad W|^2=|grad rho|^2+rho^2|grad xi|^2` AND BOUNDED HIGH-AMPLITUDE WEIGHTS, ALL BULK `D_sigma`, `D_rho`, `P_xi` PAYERS AND THE NON-KAPPA THRESHOLD GRADIENT CHARGES ARE DOMINATED BY ONE PALINSTROPHY OCCUPANCY. THE REGULAR M5-688 PAYER TREE THEREFORE COMPRESSES TO PALINSTROPHY, THRESHOLD `grad kappa`, THRESHOLD REPLENISHMENT/PHASE SEGREGATION, OR COMPONENT/INTERFACE ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Eigenvalue-gradient bound

On the regular Rank-1 branch,

\[
\Sigma\xi=\sigma\xi,
\qquad |\xi|=1.
\]

Differentiate in `x_j`:

\[
(\partial_j\Sigma)\xi+\Sigma\partial_j\xi
=(\partial_j\sigma)\xi+\sigma\partial_j\xi.
\]

Dot with `xi`. Since `xi dot partial_j xi=0` and `Sigma xi=sigma xi`,

\[
\boxed{
\partial_j\sigma
=\xi^T(\partial_j\Sigma)\xi.
}
\]

Therefore

\[
\boxed{
|\nabla\sigma|^2\le|\nabla\Sigma|_F^2.
}
\]

No derivative of the eigenvector is needed in this estimate.

---

## 2. Exact Fourier relation between strain gradient and vorticity palinstrophy

For divergence-free `U`, in Fourier variables

\[
\widehat\Sigma_{ij}
=\frac i2(\zeta_i\widehat U_j+\zeta_j\widehat U_i),
\qquad
\zeta\cdot\widehat U=0.
\]

Hence

\[
|\widehat\Sigma|_F^2
=\frac12|\zeta|^2|\widehat U|^2.
\]

Since

\[
|\widehat W|^2
=|\zeta\times\widehat U|^2
=|\zeta|^2|\widehat U|^2,
\]

multiplying by `|zeta|^2` and integrating gives

\[
\boxed{
\|\nabla\Sigma\|_2^2
=\frac12\|\nabla W\|_2^2.
}
\]

Consequently

\[
\boxed{
\|\nabla\sigma\|_2^2
\le\frac12\|\nabla W\|_2^2.
}
\]

---

## 3. Amplitude/director decomposition

For `W=rho xi`, `|xi|=1`,

\[
\boxed{
|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
}
\]

Thus the M17-195 bulk charges satisfy, with `|kappa|<=K_*`,

\[
D_\rho
\le e^{2K_*}\int|\nabla W|^2dy,
\]

\[
P_\xi
\le e^{2K_*}\int|\nabla W|^2dy.
\]

If `rho<=M_0` on the retained compact hull,

\[
D_\sigma
:=\int\chi e^{2\kappa}\rho^2|\nabla\sigma|^2dy
\le
\frac12e^{2K_*}M_0^2
\int|\nabla W|^2dy.
\]

---

## 4. Non-kappa threshold charges also lie at palinstrophy order

On the fixed transition collar, `rho`, `chi'`, and `e^{2kappa}` are uniformly bounded. Hence

\[
B_\rho
=\int\chi'e^{2\kappa}\rho|\nabla\rho|^2dy
\le C_{coll}\int|\nabla W|^2dy,
\]

and

\[
B_\sigma
=\int\chi'e^{2\kappa}\rho^3|\nabla\sigma|^2dy
\le C_{coll}\int|\nabla\Sigma|^2dy
\le\frac{C_{coll}}2\int|\nabla W|^2dy.
\]

The exception is

\[
B_\kappa
=\int\chi'e^{2\kappa}\rho^3|\nabla\kappa|^2dy,
\]

which is a genuine multiplier-gradient threshold charge and is not reduced to ordinary palinstrophy by this argument.

---

## 5. Compressed payer tree

M17-193 folds connected quarter-strain phase segregation into `D_sigma`.
M17-194--196 fold the geometric remainder into gradient/threshold charges.
The present module folds the bulk fixed-order gradient charges into palinstrophy.

Thus, modulo explicit lower-order residence terms and component bookkeeping, the regular M5-688 payer structure reduces to

\[
\boxed{
D_\kappa>0
\Longrightarrow
P_W
\lor
B_\kappa
\lor
T_{replenish}^{high\text{-}\kappa}
\lor
G_{component/interface},
}
\]

where

\[
\boxed{
P_W:=\int|\nabla W|^2dy
}
\]

(or its bounded exponentially weighted high-amplitude version) denotes the common bulk palinstrophy occupancy.

The quarter-strain `Q_sigma^(2)` branch is either supported by its positive unweighted palinstrophy/threshold baseline or, if generated mainly by phase segregation on a connected component, returns to the same palinstrophy class through M17-193.

---

## 6. DSD audit

- The global Fourier identity is unweighted. Weighted charges are dominated using boundedness of the high-amplitude weight; no weighted Riesz theorem is assumed.
- A positive palinstrophy occupancy is not yet a finite cumulative budget in three-dimensional Navier--Stokes.
- `B_kappa` remains genuinely higher in the multiplier variable.
- Disconnected component/interface segregation remains separate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
