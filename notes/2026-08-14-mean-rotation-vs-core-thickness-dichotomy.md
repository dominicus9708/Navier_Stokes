# Mean rotation versus terminal-core thickness dichotomy

Date: 2026-08-14

Status: **DERIVED COMPACT-CORE DICHOTOMY / COHERENT ROTATION OR DIVERGING CRITICAL L3 DEMAND**.

## 1. Gaussian vorticity decomposition

At a terminal-centered Gaussian window of radius `R`, write

\[
\bar\Omega_R=P_R\Omega,
\qquad
V_{\omega,R}=P_R|\Omega-\bar\Omega_R|^2.
\]

Then exactly

\[
\boxed{
P_R|\Omega|^2
=|\bar\Omega_R|^2+V_{\omega,R}.
}
\]

For the four-channel residual gradient variance,

\[
B
=V_S+\frac12V_\omega,
\]

so

\[
\boxed{V_\omega\le2B.}
\]

## 2. Terminal core thickness on the compact branch

At terminal first hitting,

\[
|\Omega(0,0)|=1.
\]

On the compact branch used elsewhere in the repository, local regularity/compactness supplies a fixed natural-scale thickness: there are constants `rho_*>0` and `c_*>0`, independent of the blow-up index, such that

\[
\boxed{
|\Omega(y,0)|\ge c_*
\qquad (|y|\le\rho_*).
}
\]

For example, a uniform local Holder bound together with the terminal point value gives such a ball.

If this thickness fails along the sequence, that failure is itself a derivative-concentration / loss-of-compactness branch and is not silently included below.

For `R>=1`, the centered Gaussian density on `B_{rho_*}` is bounded below by `c R^{-3}`. Hence

\[
\boxed{
P_R|\Omega|^2
\ge cR^{-3}.
}
\]

## 3. Dichotomy by coherent mean rotation

Consider the ratio

\[
\boxed{
\Gamma_R^2
:=\frac{|\bar\Omega_R|^2}{B}.
}
\]

After subsequence extraction there are two qualitative possibilities.

### A. Coherent-rotation branch

\[
\Gamma_R\to\infty.
\]

This is exactly the rapid mean-rotation branch. In turnover time, the Coriolis coefficient is `Gamma_R`, and the preceding coherent-rotation rigidity note applies: a tight low-curvature compact survivor is forced toward the zero `L2(R3)` Coriolis kernel, so survival requires higher chaos, spatial non-tightness, affine/frame forcing, or loss of the compact assumptions.

### B. Mean-nondominant branch

Suppose instead

\[
|\bar\Omega_R|^2\le C_0B
\]

along a subsequence. Then

\[
P_R|\Omega|^2
\le(C_0+2)B.
\]

Combining with the terminal-core lower bound gives

\[
\boxed{
BR^3\ge c_{C_0}>0.
}
\]

Thus

\[
\boxed{
R\gtrsim B^{-1/3}.
}
\]

## 4. Critical Reynolds consequence

Recall

\[
\mathcal R_G=R^2\sqrt B.
\]

On the mean-nondominant compact branch,

\[
R^3\gtrsim B^{-1}
\]

implies

\[
\boxed{
\mathcal R_G
\gtrsim B^{-1/6}
}
\]

and therefore

\[
\boxed{
\mathcal R_G^3
\gtrsim B^{-1/2}.
}
\]

For the surviving intermediate pulse `B -> 0`, this diverges.

## 5. Near-second-Hermite transport consequence

The preceding near-second-Hermite L3 lemma gives

\[
\int_{B_{CR}}|r|^3dx
\gtrsim\mathcal R_G^3.
\]

Hence the mean-nondominant compact near-Hermite branch satisfies

\[
\boxed{
\int_{B_{CR}}|r|^3dx
\gtrsim B^{-1/2}.
}
\]

If local stretching does not create the higher-chaos certificate and affine/previous-checkpoint inheritance is negligible, the exact local critical-mass balance requires shell/pressure/interior generation of at least this diverging amount.

Thus lack of coherent mean rotation does not make the pulse cheap; it forces spatial concentration and a diverging critical-transport demand.

## 6. Combined compact low-curvature branch tree

For a terminal-centered intermediate pulse with `B -> 0` and fixed terminal core thickness,

\[
\boxed{
\text{either}
\quad
\frac{|\bar\Omega_R|^2}{B}\to\infty
\quad\text{or}\quad
BR^3\gtrsim1.
}
\]

Therefore

\[
\boxed{
\text{coherent rotation}
\Rightarrow
\text{Coriolis tightness rigidity / escape},
}

while

\[
\boxed{
\text{noncoherent mean}
\Rightarrow
\mathcal R_G^3\gtrsim B^{-1/2}
\Rightarrow
\text{diverging critical L3 demand}.
}
\]

If terminal core thickness itself fails, the route is sent to the already retained derivative-concentration/higher-order sparseness branch.

Status: **MEAN-ROTATION ALTERNATIVE SHARPENED; COMPACT NEAR-HERMITE SURVIVOR MUST PAY EITHER CORIOLIS ESCAPE OR DIVERGING TRANSPORT/HIGHER-DERIVATIVE COST**.
