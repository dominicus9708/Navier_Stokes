# DSD W1 H2-Coherent Pressure-Free Vorticity Current Limit

Date: 2026-08-26

Status: **ON THE CRITICAL-H2-BOUNDED CORRIDOR, ALL-AGE H^-1 SHELL TRANSPORT UPGRADED TO H1 / WEIGHTED-VORTICITY SHELL CHARGE SHOWN DYADIC CAUCHY / LOGARITHMIC LOWER GROWTH FORCES A STRICTLY POSITIVE ASYMPTOTIC SHELL CHARGE / GAUSSIAN VORTICITY SCALE CURRENT CONVERGES TO A POSITIVE LIMIT / H2-ESCALATING CORRIDOR REMAINS A DERIVATIVE IRREGULARITY DIAGNOSTIC / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The localized Hardy--curl note proves on every W1 minimal state

\[
\bar I(R)\asymp\log R
\]

and consequently

\[
\mathcal S_\Omega(R)
=\frac12\partial_{\log R}\bar I(R)
\]

is uniformly positive on a positive density of logarithmic scales.

The missing strengthening is a positive **limit** analogous to the Bernoulli endpoint

\[
\mathcal S_B(R)\to\mathscr R_3/6>0.
\]

This note obtains that strengthening on the already identified critical-H2-coherent corridor.

The H2 condition is used only as a regularity tool for the vorticity current.  It is not restored as a separate terminal proof branch.

---

## 2. Fixed-cell rescaling

For a remote shell radius `R`, define the critical fixed-cell velocity

\[
F_R(z,s):=R\,U(Rz,s)
\]

on a fixed enlarged annulus `A_1^*`.

Critical scaling gives

\[
\|F_R\|_{H^1(A_1^*)}
\le C_1
\]

on W1.

The critical H2 shell quantity is equivalent to

\[
\boxed{
\|F_R\|_{H^2(A_1^*)}^2
\asymp
R^3\int_{A_R^*}|\nabla^2U|^2dY.
}
\]

Assume the H2-coherent corridor

\[
\boxed{
\sup_{R\gg1,s}
R^3\int_{A_R^*}|\nabla^2U|^2dY
\le H_{2,*}<\infty.
}
\]

Then

\[
\boxed{
\|F_R\|_{H^2(A_1^*)}
\le C_2.
}
\]

---

## 3. All-age co-moving defect

The existing W1 all-age transport theorem gives, for the co-moving critically rescaled shell field,

\[
\boxed{
\|F_R^{co}(h)-F_R^{co}(0)\|_{H^{-1}(A_1^*)}
\le
CR^{-2}
\qquad\forall h\ge0.
}
\]

Both endpoint fields have a uniform H2 bound, so their difference satisfies

\[
\|\delta F_R(h)\|_{H^2}
\le C.
\]

Interpolate `H^-1` and `H2` to `H1`.

Since

\[
1=(1-\theta)(-1)+\theta(2)
\]

gives

\[
\theta=\frac23,
\]

we obtain

\[
\begin{aligned}
\|\delta F_R(h)\|_{H^1}
&\le
C
\|\delta F_R(h)\|_{H^{-1}}^{1/3}
\|\delta F_R(h)\|_{H^2}^{2/3}\\
&\le
\boxed{CR^{-2/3}}.
\end{aligned}
\]

The constant is independent of shell age `h`.

Thus the all-age passive transport is now strong enough to compare vorticity on the shell.

---

## 4. Critical weighted-vorticity shell charge

Define

\[
\boxed{
J_\Omega(R,U)
:=
\int_{R<|Y|<2R}|Y||\Omega_U(Y)|^2dY.
}
\]

Under the critical rescaling `F_R(z)=R U(Rz)`,

\[
\nabla_z\times F_R(z)
=R^2\Omega_U(Rz).
\]

Therefore

\[
\boxed{
J_\Omega(R,U)
=
\int_{1<|z|<2}|z|
|\nabla_z\times F_R(z)|^2dz.
}
\]

So `J_Omega` is exactly scale invariant.

The uniform H1 bound gives

\[
J_\Omega(R,U)\le C_J.
\]

---

## 5. H1 shell closeness controls the charge difference

Let two co-moving fixed-cell fields be `F` and `G` with uniformly bounded H1 norm.

Then

\[
\begin{aligned}
&\left|
\int |z||\curl F|^2
-
\int |z||\curl G|^2
\right|\\
&\qquad\le
C
\|\curl(F-G)\|_2
\left(\|\curl F\|_2+\|\curl G\|_2\right)\\
&\qquad\le
C\|F-G\|_{H^1}.
\end{aligned}
\]

Thus the all-age H1 estimate gives

\[
\boxed{
\left|
J_\Omega(e^{h/2}R,\Phi_hU)
-J_\Omega(R,U)
\right|
\le
CR^{-2/3}
}
\]

for every `h>=0` on the H2-coherent corridor.

---

## 6. Use the dyadic Leray time

Choose

\[
h_0=2\log2.
\]

Then

\[
e^{h_0/2}R=2R.
\]

For the invariant W1 measure `mu`, invariance under `Phi_h0` gives

\[
\begin{aligned}
\bar J_\Omega(2R)
&:=
\int J_\Omega(2R,U)d\mu(U)\\
&=
\int J_\Omega(2R,\Phi_{h_0}U)d\mu(U)
\end{aligned}
\]

up to the harmless direction of applying invariance; equivalently change variables by the measure-preserving flow map.

Hence the all-age comparison yields

\[
\boxed{
|\bar J_\Omega(2R)-\bar J_\Omega(R)|
\le
CR^{-2/3}.
}
\]

Along dyadic radii

\[
R_k=2^kR_0,
\]

the errors are summable:

\[
\sum_kR_k^{-2/3}<\infty.
\]

Therefore

\[
\boxed{
\bar J_\Omega(R_k)
\longrightarrow
J_{\Omega,\infty}
}
\]

for a finite nonnegative limit.

---

## 7. The asymptotic shell charge cannot be zero

The localized Hardy--curl theorem already gives

\[
\boxed{
\bar I(R)
\ge
c_I\log R-C_I,
}
\]

where

\[
I(R)
=\frac12\int r e^{-r^2/R^2}|\Omega|^2.
\]

Equivalently, the cumulative first weighted enstrophy up to radius `R` has a positive logarithmic lower slope.

If

\[
J_{\Omega,\infty}=0,
\]

then the dyadic shell charges tend to zero.  Their Cesaro average would also tend to zero, so the cumulative weighted enstrophy divided by the number of dyadic shells would tend to zero.

This contradicts the positive logarithmic lower bound.

Hence

\[
\boxed{
J_{\Omega,\infty}>0.
}
\]

Thus every sufficiently remote dyadic shell carries asymptotically the same nonzero invariant weighted-vorticity charge on the H2-coherent corridor.

---

## 8. Log-radius density

Let

\[
q_\Omega(\rho)
\]

denote the invariant-mean density of the first weighted enstrophy in logarithmic radius, so that

\[
\bar J_\Omega(R)
=
\int_{\log R}^{\log R+\log2}
q_\Omega(\rho)d\rho.
\]

The preceding dyadic convergence gives an asymptotic mean density

\[
\boxed{
\mathscr R_\Omega
:=
\frac{J_{\Omega,\infty}}{\log2}>0.
}
\]

This is the vorticity analogue of the cubic log-density

\[
\mathscr R_3
=
\frac{M_{crit}}{\log2}>0.
\]

---

## 9. Abelian limit of the Gaussian vorticity scale derivative

Recall

\[
I_R
=
\frac12\int r e^{-r^2/R^2}|\Omega|^2dY.
\]

In logarithmic radius,

\[
\partial_{\log R}I_R
=
\int
K(\rho-\log R)
q_\Omega(\rho)d\rho,
\]

with

\[
\boxed{
K(x)=e^{2x}e^{-e^{2x}}.
}
\]

The kernel is positive and

\[
\boxed{
\int_{-\infty}^{\infty}K(x)dx
=\frac12.
}
\]

Because fixed-length log-window averages of `q_Omega` converge to `R_Omega` on the H2-coherent corridor and the shell charges are uniformly bounded, the standard Abelian convolution argument gives

\[
\boxed{
\partial_{\log R}\bar I(R)
\longrightarrow
\frac12\mathscr R_\Omega.
}
\]

The pressure-free scale surplus is

\[
\mathcal S_\Omega(R)
=
\frac12\partial_{\log R}\bar I(R).
\]

Therefore

\[
\boxed{
\mathcal S_\Omega(R)
\longrightarrow
\frac14\mathscr R_\Omega
=
\frac{J_{\Omega,\infty}}{4\log2}
>0.
}
\]

This is the full pressure-free endpoint limit on the H2-coherent corridor.

---

## 10. Comparison with the Bernoulli endpoint

The W1 survivor now has, on the H2-coherent corridor, two genuine positive endpoint limits:

\[
\boxed{
\mathcal S_B(R)
\longrightarrow
\frac{\mathscr R_3}{6}>0,
}
\]

and

\[
\boxed{
\mathcal S_\Omega(R)
\longrightarrow
\frac{\mathscr R_\Omega}{4}>0.
}
\]

They arise from distinct exact equations:

- `S_B`: critical velocity/Bernoulli `p=3` transport;
- `S_Omega`: pressure-free first-weighted-enstrophy transport.

Thus a coherent critical W1 tail must be simultaneously nontrivial in both currents.

---

## 11. What happens if H2 coherence fails

If

\[
\sup_R
R^3\int_{A_R^*}|\nabla^2U|^2
=\infty,
\]

then the H2 interpolation used above is unavailable.

This is exactly the already classified critical-H2 derivative/subscale escalation.

The current proof management is therefore

\[
\boxed{
W1
\Longrightarrow
H_{2,crit}^{tail}
\quad\lor\quad
\left[
\mathcal S_B(\infty)>0
\ \&\
\mathcal S_\Omega(\infty)>0
\right].
}
\]

This is not a restoration of the old multi-branch endgame.  The Bernoulli endpoint remains valid on both sides.  The H2 label only records why the **second, pressure-free endpoint limit** may fail to converge.

---

## 12. New narrow target

There are now two possible routes to further progress:

1. **H2-coherent route:** exploit the simultaneous positive Bernoulli and vorticity endpoint currents to derive an incompatibility or a stronger tail equation;
2. **H2-escalating route:** use the unbounded critical H2 charge to extract a finite derivative packet or show that the same Bernoulli current must pay an unbounded derivative cost.

Either route attacks the same W1 critical memory rather than separate geometric survivors.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
