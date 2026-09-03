# DSD M5-688 — An exponential kappa ledger forces strain or geometric payment of the uniform multiplier-diffusion charge

Date: 2026-09-03

Status: **INTERNAL STATIONARY CONSTITUTIVE LEDGER / FOR THE M5-683 HIGH-AMPLITUDE ENSTROPHY-WEIGHTED KAPPA DISTRIBUTION, THE WEIGHT `m=chi(rho)rho^2` OBEYS `partial_theta F + partial_k G = (2k-1/2)F + 2S_sigma + C_chi`; COMBINING THIS WITH `G=partial_k(A_kk+A_ks)-kF+R_chi` ELIMINATES THE KINEMATIC `kF` SOURCE AND GIVES `G'+2G=2A'+2S_sigma+C_chi+2R_chi-(1/2)F` ON THE RECURRENT MEAN / MULTIPLICATION BY THE UNIQUE INTEGRATING FACTOR `e^{2k}` AND INTEGRATION OVER THE COMPACT KAPPA SUPPORT YIELDS AN EXACT CYCLE-WORK IDENTITY / M5-687 SUPPLIES A UNIFORM POSITIVE LOWER BOUND FOR THE PURE KAPPA-DIFFUSION TERM, SO THE SURVIVOR MUST PAY IT THROUGH A STRAIN-GRADIENT TERM, A NONZERO STRAIN-RESIDENCE MOMENT, THE AMPLITUDE-CUTOFF TRANSITION, OR THE EXPLICIT CE-H GEOMETRIC REMAINDER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Reuse the M5-683 high-amplitude measure

Let

\[
\rho=|W|,
\]

and let `chi(rho)` be the fixed high-amplitude cutoff of M5-683.
Define the transported spatial weight

\[
\boxed{
m:=\chi(\rho)\rho^2.
}
\]

Define

\[
\boxed{
F(k,\theta)
:=\int\delta(k-\kappa)m\,dy,
}
\]

\[
\boxed{
G(k,\theta)
:=\int h\,\delta(k-\kappa)m\,dy,
\qquad h=D_B\kappa.
}
\]

These are the enstrophy-weighted quantities of M5-683, not the pure transverse-flux measure of M5-681.

---

## 2. Exact evolution of the cutoff enstrophy weight

On CE-H,

\[
\boxed{
D_B\rho=(\sigma+\kappa-1)\rho.
}
\]

The similarity material velocity is

\[
B=U+\frac12y,
\]

so

\[
\boxed{
\nabla\cdot B=\frac32.
}
\]

Differentiate

\[
m=\chi(\rho)\rho^2.
\]

We obtain

\[
D_Bm
=\chi'(\rho)\rho^3(\sigma+\kappa-1)
+2\chi\rho^2(\sigma+\kappa-1).
\]

Hence

\[
\boxed{
D_Bm+(\nabla\cdot B)m
=\chi\rho^2\left(2\sigma+2\kappa-\frac12\right)
+\chi'(\rho)\rho^3(\sigma+\kappa-1).
}
\]

Define the cutoff-transition source distribution

\[
\boxed{
C_\chi(k,\theta)
:=\int
\delta(k-\kappa)
\chi'(\rho)\rho^3(\sigma+\kappa-1)dy.
}
\]

Also define the aligned-strain distribution

\[
\boxed{
S_\sigma(k,\theta)
:=\int
\delta(k-\kappa)
\chi(\rho)\rho^2\sigma\,dy.
}
\]

---

## 3. Kappa-space continuity law for the spatial measure

For a smooth test function `psi`, the transport identity gives

\[
\frac d{d\theta}\int\psi(\kappa)m\,dy
=
\int\psi'(\kappa)h m\,dy
+
\int\psi(\kappa)
\left[D_Bm+(\nabla\cdot B)m\right]dy.
\]

Therefore, distributionally in `k`,

\[
\boxed{
\partial_\theta F+\partial_kG
=
\left(2k-\frac12\right)F
+2S_\sigma
+C_\chi.
}
\]

This is the enstrophy-weighted analogue of the pure-flux continuity law in M5-681.

The additional terms are mandatory because `rho^2dy` is not a conserved material measure.

---

## 4. Insert the M5-683 constitutive current

M5-683 gives

\[
\boxed{
G
=\partial_kA-kF+\mathcal R_\chi,
}
\]

where

\[
\boxed{
A:=A_{\kappa\kappa}+A_{\kappa\sigma},
}
\]

\[
A_{\kappa\kappa}
=\int\delta(k-\kappa)
\chi\rho^2|\nabla\kappa|^2dy
\ge0,
\]

and

\[
A_{\kappa\sigma}
=\int\delta(k-\kappa)
\chi\rho^2\nabla\kappa\cdot\nabla\sigma\,dy.
\]

`R_chi` contains the explicit CE-H geometric remainder and the spatial derivative of the amplitude cutoff, exactly as in M5-683.

---

## 5. Pass to the recurrent mean

Take an invariant/recurrent long-time average and denote averaged quantities by overbars.
The mean time derivative vanishes, giving

\[
\boxed{
\partial_k\overline G
=
\left(2k-\frac12\right)\overline F
+2\overline S_\sigma
+\overline C_\chi.
}
\]

The constitutive relation becomes

\[
\boxed{
\overline G
=\partial_k\overline A
-k\overline F
+\overline{\mathcal R}_\chi.
}
\]

Solve the continuity equation for `k F`:

\[
2k\overline F
=
\partial_k\overline G
+\frac12\overline F
-2\overline S_\sigma
-\overline C_\chi.
\]

Therefore

\[
-k\overline F
=-\frac12\partial_k\overline G
-\frac14\overline F
+\overline S_\sigma
+\frac12\overline C_\chi.
\]

Substitute this into the constitutive relation:

\[
\boxed{
\frac12\partial_k\overline G
+\overline G
=
\partial_k\overline A
+\overline S_\sigma
+\frac12\overline C_\chi
+\overline{\mathcal R}_\chi
-\frac14\overline F.
}
\]

Equivalently,

\[
\boxed{
\partial_k\overline G+2\overline G
=
2\partial_k\overline A
+2\overline S_\sigma
+\overline C_\chi
+2\overline{\mathcal R}_\chi
-\frac12\overline F.
}
\]

This is the source-renormalized stationary constitutive equation.

---

## 6. The natural integrating factor is e^(2k)

Because the left side is

\[
\partial_k\overline G+2\overline G,
\]

its unique elementary integrating factor is

\[
\boxed{e^{2k}.}
\]

Thus

\[
\partial_k\left(e^{2k}\overline G\right)
=
e^{2k}
\left[
2\partial_k\overline A
+2\overline S_\sigma
+\overline C_\chi
+2\overline{\mathcal R}_\chi
-\frac12\overline F
\right].
\]

On the retained high-amplitude population, `kappa` has compact support in `[-K_*,K_*]`.
Choose the endpoints just outside the support, so

\[
\overline G=0,
\qquad
\overline A=0
\]

at both endpoints.

Integrating over all `k` gives

\[
0
=-4\int e^{2k}\overline A\,dk
+2\int e^{2k}\overline S_\sigma\,dk
+\int e^{2k}\overline C_\chi\,dk
+2\int e^{2k}\overline{\mathcal R}_\chi\,dk
-\frac12\int e^{2k}\overline F\,dk.
\]

Hence the exact exponential cycle-work identity is

\[
\boxed{
\begin{aligned}
\int e^{2k}\overline A\,dk
={}&
\frac12\int e^{2k}\overline S_\sigma\,dk
+\frac14\int e^{2k}\overline C_\chi\,dk\\
&+\frac12\int e^{2k}\overline{\mathcal R}_\chi\,dk
-\frac18\int e^{2k}\overline F\,dk.
\end{aligned}
}
\]

The source term responsible for the purely kinematic hysteresis of M5-686 has now been absorbed into an exact stationary ledger.

---

## 7. Separate the positive diffusion charge

Define

\[
\boxed{
D_\kappa
:=
\int e^{2k}\overline A_{\kappa\kappa}(k)dk.
}
\]

M5-687 gives the uniform positive lower bound

\[
\boxed{
D_\kappa\ge d_\kappa^{(2)}>0.
}
\]

Define the mixed gradient work

\[
\boxed{
X_{\kappa\sigma}
:=
\int e^{2k}\overline A_{\kappa\sigma}(k)dk.
}
\]

Also define

\[
\boxed{
\mathcal S
:=\int e^{2k}\overline S_\sigma(k)dk,
}
\]

\[
\boxed{
\mathcal C
:=\int e^{2k}\overline C_\chi(k)dk,
}
\]

\[
\boxed{
\mathcal R
:=\int e^{2k}\overline{\mathcal R}_\chi(k)dk,
}
\]

and the positive weighted mass

\[
\boxed{
\mathcal M
:=\int e^{2k}\overline F(k)dk>0.
}
\]

Then

\[
\boxed{
D_\kappa+X_{\kappa\sigma}
=
\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R
-\frac18\mathcal M.
}
\]

Equivalently,

\[
\boxed{
D_\kappa+\frac18\mathcal M
=
-X_{\kappa\sigma}
+\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R.
}
\]

The positive mass term lies on the same side as the positive diffusion charge; it cannot pay that charge.

---

## 8. Quantitative payer inequality

Introduce the exponentially weighted strain-gradient charge

\[
\boxed{
D_\sigma
:=
\left\langle
\int
\chi\rho^2e^{2\kappa}|\nabla\sigma|^2dy
\right\rangle.
}
\]

Space-time Cauchy-Schwarz gives

\[
\boxed{
|X_{\kappa\sigma}|
\le
\sqrt{D_\kappa D_\sigma}.
}
\]

Therefore

\[
\boxed{
D_\kappa+\frac18\mathcal M
\le
\sqrt{D_\kappa D_\sigma}
+\frac12|\mathcal S|
+\frac14|\mathcal C|
+\frac12|\mathcal R|.
}
\]

This is the first quantitative PDE payer inequality after the M5-686 kinematic correction.

---

## 9. Explicit payer dichotomy

There are two cases.

### Case A — strain-gradient payer

If

\[
D_\sigma\ge\frac14D_\kappa,
\]

then using M5-687,

\[
\boxed{
D_\sigma
\ge
\frac14d_\kappa^{(2)}>0.
}
\]

Thus the survivor carries a fixed positive aligned-strain gradient charge.

### Case B — non-gradient payer

If

\[
D_\sigma<\frac14D_\kappa,
\]

then

\[
\sqrt{D_\kappa D_\sigma}
<\frac12D_\kappa.
\]

Discarding only the additional positive term `M/8`, the payer inequality yields

\[
\frac12D_\kappa
\le
\frac12|\mathcal S|
+\frac14|\mathcal C|
+\frac12|\mathcal R|.
\]

Hence

\[
\max\{|
\mathcal S|,|\mathcal C|,|\mathcal R|\}
\ge
\frac25D_\kappa.
\]

Using the uniform diffusion floor,

\[
\boxed{
\max\{|
\mathcal S|,|\mathcal C|,|\mathcal R|\}
\ge
\frac25d_\kappa^{(2)}>0.
}
\]

Therefore the compact CE-H survivor must satisfy the quantitative alternative

\[
\boxed{
D_\sigma\ge\frac14d_\kappa^{(2)}
\quad\lor\quad
\max\{|
\mathcal S|,|\mathcal C|,|\mathcal R|\}
\ge\frac25d_\kappa^{(2)}.
}
\]

---

## 10. Interpretation of the remaining payers

The four surviving payer channels now have precise meanings.

1. `D_sigma`: persistent spatial variation of the aligned strain eigenvalue.

2. `S`: nonzero exponentially kappa-weighted aligned-strain residence moment,

\[
\mathcal S
=\left\langle
\int\chi\rho^2e^{2\kappa}\sigma\,dy
\right\rangle.
\]

3. `C`: the amplitude-threshold transition channel generated because the scalar `kappa` description is restricted away from `W=0`.

4. `R`: the explicit CE-H geometric/cutoff spatial remainder from M5-682/M5-683, containing the strain-Hessian amplitude coupling, direction-metric term, curl-amplitude coupling, and cutoff-gradient correction.

The first two are direct strain channels.
The last two must be audited further to separate genuine geometry from localization artifacts.

---

## 11. DSD audit

This calculation does **not** prove that any one payer is impossible.

It does prove that the last recurrent CE-H survivor cannot simultaneously make all of the following small:

\[
\boxed{
\nabla\sigma,
\quad
\text{weighted strain residence},
\quad
\text{cutoff transition},
\quad
\text{CE-H geometric remainder}.
}
\]

The reason is no longer the directed zero-crossing current itself.
The reason is the uniform positive `kappa`-diffusion charge of M5-687 combined with the exact constitutive/continuity equations.

Thus the proof line has moved from a qualitative hysteresis picture to a quantitative PDE payer alternative.

---

## 12. Updated frontier

The highest-value next step is to attack the four payer channels in the following order:

\[
\boxed{
D_\sigma
\longrightarrow
\mathcal S
\longrightarrow
\mathcal R
\longrightarrow
\mathcal C.
}
\]

The first two connect directly to the earlier Betchov/middle-strain genealogy of M5-674--676.

If they can be absorbed into that already finite-lifetime genealogy, the only remaining escape will be an explicit geometric or zero-set/localization channel rather than an abstract multi-sheet hysteresis cycle.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
