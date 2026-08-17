# Log-extended coherent occupancy: enstrophy and critical `L^3`

Date: 2026-08-17

Status: **DERIVED ON THE BOUNDED-CONDITION COHERENT GAUSSIAN BRANCH. SMALL GAUSSIAN GRADIENT VARIANCE AND ORDER-ONE MEAN VORTICITY FORCE COHERENT ENSTROPHY OCCUPANCY OUT TO `R sqrt(log R)`; THE SAME AFFINE-CORE ARGUMENT FORCES A CRITICAL VELOCITY `L^3` LOWER BOUND. THE ENLARGED COHERENT OCCUPANCY ADMITS SCALE-SEPARATED BESSEL PACKING. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `U` be terminal-normalized velocity, `Omega=curl U`, and let `gamma_Sigma` be a bounded-condition Gaussian whose covariance scale is

\[
R=(\det\Sigma)^{1/6}.
\]

Write

\[
L=E_\gamma\nabla U,
\qquad
\bar\Omega=E_\gamma\Omega,
\]

and

\[
B
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega)
=E_\gamma|\nabla U-L|^2.
\]

Assume at a coherent late-ramp time

\[
|\bar\Omega|\ge c_0>0,
\qquad
B\le C_0R^{-2}.
\]

The second condition is much weaker than the exact crossing value `B=R^-4`; it is the threshold needed for logarithmic Gaussian-tail extension.

## 2. Vorticity remains coherent on an enlarged Euclidean ball

Because

\[
\operatorname{Var}_\gamma(\Omega)
\le 2B
\lesssim R^{-2},
\]

and a bounded-condition Gaussian obeys on `B_{rho R}`

\[
\gamma_\Sigma(x)
\gtrsim
R^{-3}e^{-C\rho^2},
\]

we obtain

\[
\int_{B_{\rho R}}
|\Omega-\bar\Omega|^2dx
\lesssim
R^3e^{C\rho^2}B
\lesssim
Re^{C\rho^2}.
\]

Meanwhile the constant coherent part has

\[
\int_{B_{\rho R}}|\bar\Omega|^2dx
\gtrsim
\rho^3R^3.
\]

Choose

\[
\rho^2=\alpha\log R
\]

with fixed sufficiently small `alpha>0` so that `C alpha<1` (any fixed choice with exponent strictly below the available `R^2` margin is enough). Then

\[
\frac{Re^{C\rho^2}}{\rho^3R^3}\to0.
\]

Hence for large `R`,

\[
\boxed{
\int_{B_{cR\sqrt{\log R}}}
|\Omega|^2dx
\gtrsim
R^3(\log R)^{3/2}.
}
\]

Thus the coherent crossing is not merely an `R^3` enstrophy core. On the low-variance branch it occupies a logarithmically enlarged Euclidean volume.

## 3. Critical velocity `L^3` lower bound

The antisymmetric part of `L` is one half of the mean vorticity matrix, so

\[
|\operatorname{skew}L|\gtrsim c_0.
\]

The existing Gaussian-tail affine-core argument gives on the same enlarged ball of radius

\[
L_R\asymp R\sqrt{\log R}
\]

a decomposition

\[
U=Lx+d+h
\]

with

\[
\|h\|_{L^2(B_{L_R})}
=o(\|Lx\|_{L^2(B_{L_R})}).
\]

Therefore

\[
\|U\|_{L^2(B_{L_R})}^2
\gtrsim
L_R^5.
\]

On a set of volume `~L_R^3`, Holder gives

\[
\|U\|_2
\le
|B_{L_R}|^{1/6}\|U\|_3.
\]

Hence

\[
\|U\|_3^3
\gtrsim
\frac{\|U\|_2^3}{|B_{L_R}|^{1/2}}
\gtrsim
L_R^6.
\]

Thus

\[
\boxed{
\|U\|_3^3
\gtrsim
R^6(\log R)^3.
}
\]

Since velocity `L^3` is invariant under Navier--Stokes scaling, this is also a physical critical-norm lower bound at the corresponding physical time.

This does not contradict a hypothetical singularity; it states that the minimal coherent fixed point necessarily drives critical `L^3` escape.

## 4. A good late-ramp set exists under critical residual action

On the critical fixed-point branch,

\[
\int_{I_R}B(t)dt\asymp R^{-2}.
\]

If a fixed-length late-ramp subinterval `J_R` carries order-one mean vorticity, then for any fixed large `K`, Markov gives

\[
|\{t\in J_R:B(t)>KR^{-2}\}|
\lesssim K^{-1}.
\]

Hence a fixed positive fraction of the late-ramp interval satisfies simultaneously

\[
|\bar\Omega|\gtrsim1,
\qquad
B\lesssim R^{-2},
\]

provided the coherent mean itself remains order one on that late block, as in the critical ramp benchmark.

Therefore the enlarged occupancy is not restricted to a single exceptional instant on the near-saturation branch.

## 5. Enlarged-scale Bessel packing

Return to physical variables. The enlarged coherent scale is

\[
\widetilde\ell_j
\asymp
\frac{R_j\sqrt{\log R_j}}{\sqrt{W_j}}.
\]

For a geometrically separated physical-scale subsequence, the logarithmic factor does not destroy separation. Normalized bump/ball probes at scales `tilde ell_j` therefore form a uniformly Bessel family, independently of moving centers:

\[
|\langle p_j,p_k\rangle|
\lesssim
(\widetilde\ell_{\min}/\widetilde\ell_{\max})^{3/2}.
\]

The enlarged coherence estimate implies on the good late-ramp set

\[
|\langle\omega,p_j\rangle|^2
\gtrsim
W_j^2\widetilde\ell_j^3.
\]

A fixed normalized time block has physical duration `~W_j^-1`. Integrating the Bessel inequality in physical time yields

\[
\boxed{
\sum_j
W_j\widetilde\ell_j^3
\lesssim
\int_0^{T^*}\|\omega(t)\|_2^2dt
<\infty.
}
\]

Since

\[
W_j\widetilde\ell_j^3
\asymp
\frac{R_j^3(\log R_j)^{3/2}}{\sqrt{W_j}},
\]

we obtain the strengthened overlap-free occupancy ledger

\[
\boxed{
\sum_j
\frac{R_j^3(\log R_j)^{3/2}}{\sqrt{W_j}}
<\infty.
}
\]

This improves the earlier `sum R_j^3/sqrt(W_j)<infinity` terminal occupancy bound.

## 6. Stress test

For the adversarial family

\[
q=W^\alpha,
\qquad
R=W^{(1-\alpha)/10},
\qquad 0<\alpha<1,
\]

the new term behaves as

\[
W^{-(2+3\alpha)/10}(\log W)^{3/2},
\]

which is still summable along geometric first-hitting levels.

Therefore the logarithmic improvement does not close the Zeno family by itself.

## 7. Interpretation

The critical affine-residual fixed point now necessarily carries three simultaneous critical signatures:

\[
\boxed{
\text{coherent enstrophy volume}
\gtrsim R^3(\log R)^{3/2},
}
\]

\[
\boxed{
\|u\|_3^3
\gtrsim R^6(\log R)^3,
}
\]

and the scale-separated dissipation packing

\[
\boxed{
\sum_jR_j^3(\log R_j)^{3/2}/\sqrt{W_j}<\infty.
}
\]

The remaining issue is not whether the fixed point has a critical-norm footprint; it does. The issue is whether the exterior compensation needed to terminate this enlarged affine/coherent region can be recursively relocated to smaller physical scales without violating a scale-frequency packing theorem.

Status: **LOG-EXTENDED COHERENT ENSTROPHY AND CRITICAL `L^3` OCCUPANCY DERIVED / BESSEL TERMINAL PACKING STRENGTHENED / POWER-LAW ZENO STILL SURVIVES / GLOBAL REGULARITY NOT PROVED.**