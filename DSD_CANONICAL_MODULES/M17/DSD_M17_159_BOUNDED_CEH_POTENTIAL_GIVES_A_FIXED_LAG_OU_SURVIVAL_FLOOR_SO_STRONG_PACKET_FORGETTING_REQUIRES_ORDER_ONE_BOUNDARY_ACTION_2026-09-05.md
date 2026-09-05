# DSD M17-159 — Bounded CE-H potential gives a fixed-lag OU survival floor, so strong packet forgetting requires order-one boundary action

Date: 2026-09-05  
Canonical ID: **M17-159**

Status: **FIXED-LAG MASS-GENEALOGY GATE / M17-158 SHOWS THAT THE ONLY MASS ESCAPE FROM THE ETERNAL `L2` OU CONTRADICTION IS UNBOUNDED NORMALIZED PACKET-MASS CHANGE OVER SOME FIXED FINITE LAG, UNLESS ANOTHER HARD EXIT OCCURS. BOUNDED CE-H POTENTIAL GIVES `||grad f||_2^2/||f||_2^2 <= K0` FOR THE AMPLITUDE-NORMALIZED PACKET. THE EXACT OU SEMIGROUP THEN HAS A POSITIVE `L2` SURVIVAL FACTOR OVER EVERY FIXED LAG: JENSEN APPLIED TO THE FOURIER FORMULA GIVES `||S_T f||_2 >= eta_OU(T,K0)||f||_2`. THEREFORE STRONG FORGETTING BELOW THAT FLOOR REQUIRES ORDER-ONE DUHAMEL ACTION. ON THE QUIET RELATIVE-THICK REMOTE BRANCH, THE RESIDUAL VELOCITY-DRIFT AND STRAIN-STRETCHING ACTIONS TEND TO ZERO, SO THE REQUIRED ORDER-ONE ACTION MUST COME FROM PACKET BOUNDARY/LOCALIZATION/DIFFUSIVE TRANSFER. THUS THE STRONG FIXED-LAG MASS EXIT IS ROUTED TO A TYPED BOUNDARY-TURNOVER CHANNEL RATHER THAN REMAINING A FREE GENEALOGY ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Linear OU semigroup

Let

\[
\mathcal L_{OU}
:=
\Delta-\frac12z\cdot\nabla-1.
\]

Write

\[
S_T:=e^{T\mathcal L_{OU}}.
\]

The exact Fourier formula is

\[
\widehat{S_Tf}(\xi)
=
 e^{T/2}
 e^{-(e^T-1)|\xi|^2}
 \widehat f(\xi e^{T/2}).
\]

Changing variables `eta=xi e^{T/2}` gives

\[
\boxed{
\|S_Tf\|_2^2
=
 e^{-T/2}
\int
 e^{-2(1-e^{-T})|\eta|^2}
|\widehat f(\eta)|^2d\eta.
}
\]

---

## 2. Bounded CE-H potential gives a frequency-second-moment ceiling

If

\[
\Delta f=\kappa f,
\qquad
|\kappa|\le K_0,
\qquad
f\in L^2,
\]

then cutoff integration by parts gives

\[
\|\nabla f\|_2^2
=-\int\kappa|f|^2
\le K_0\|f\|_2^2.
\]

Thus, for the probability measure

\[
d\mu_f
:=
\frac{|\widehat f(\eta)|^2}{\|f\|_2^2}d\eta,
\]

\[
\boxed{
\int|\eta|^2d\mu_f\le K_0.
}
\]

---

## 3. Jensen gives a strict OU survival floor

The function

\[
x\mapsto e^{-a x}
\]

is convex for every `a>0`.
Therefore Jensen gives

\[
\int
 e^{-2(1-e^{-T})|\eta|^2}
 d\mu_f
\ge
\exp\left[
-2(1-e^{-T})
\int|\eta|^2d\mu_f
\right].
\]

Using the spectral ratio bound,

\[
\boxed{
\|S_Tf\|_2^2
\ge
 e^{-T/2}
 e^{-2(1-e^{-T})K_0}
\|f\|_2^2.
}
\]

Define

\[
\boxed{
\eta_{OU}(T,K_0)
:=
 e^{-T/4}
 e^{-(1-e^{-T})K_0}
>0.
}
\]

Then

\[
\boxed{
\|S_Tf\|_2
\ge
\eta_{OU}(T,K_0)\|f\|_2.
}
\]

Thus bounded-potential OU diffusion cannot erase an arbitrary fraction of packet `L2` mass in one fixed finite lag.

---

## 4. Localized normalized packet equation

For an amplitude-normalized translated packet with a smooth localization, write schematically

\[
\boxed{
\partial_\tau f
=
\mathcal L_{OU}f
+\mathcal N_j
+\mathcal R_j.
}
\]

Here:

- `N_j` is the interior perturbation from the residual remote velocity drift and strain stretching;
- `R_j` contains cutoff motion, diffusive leakage, pressure/solenoidal corrections if the velocity packet representation is used, and all packet-boundary transfer.

The mild formula over `0<=tau<=T` is

\[
 f(T)
=S_Tf(0)
+\int_0^TS_{T-s}(\mathcal N_j+\mathcal R_j)(s)ds.
\]

The OU semigroup satisfies

\[
\|S_tg\|_2\le e^{-t/4}\|g\|_2\le\|g\|_2.
\]

---

## 5. Exact fixed-lag forgetting tax

Suppose

\[
\|f(T)\|_2
\le
\varepsilon\|f(0)\|_2
\]

with

\[
0\le\varepsilon<\eta_{OU}(T,K_0).
\]

Reverse triangle plus the OU survival floor gives

\[
\boxed{
\int_0^T
\left(
\|\mathcal N_j(s)\|_2
+
\|\mathcal R_j(s)\|_2
\right)ds
\ge
\left(
\eta_{OU}-\varepsilon
\right)
\|f(0)\|_2.
}
\]

Thus strong forgetting has a fixed dimensionless action cost.

This is the OU analogue of the earlier M5 localized natural-band forgetting gate, but it uses the CE-H bounded-potential spectral ratio rather than a separately chosen Fourier band.

---

## 6. Quiet relative-thick branch kills the internal action

On the M17-155 remote packet:

\[
U(p_j+z)-U(p_j)\to0
\]

uniformly on fixed cylinders.
The normalized packet has fixed local derivative control on the relative-thick bounded-potential branch.
Hence the residual transport action satisfies

\[
\int_0^T
\|[U(p_j+z)-U(p_j)]\cdot\nabla f_j\|_2d\tau
=o(1)\|f_j(0)\|_2.
\]

Likewise the quiet spacetime strain ledger gives

\[
\int_0^T\|\Sigma_jf_j\|_2d\tau
=o(1)\|f_j(0)\|_2.
\]

Therefore

\[
\boxed{
\int_0^T\|\mathcal N_j\|_2d\tau
=o(1)\|f_j(0)\|_2.
}
\]

---

## 7. Strong fixed-lag forgetting must be boundary turnover

For sufficiently remote packets, the fixed forgetting tax therefore forces

\[
\boxed{
\int_0^T
\|\mathcal R_j(s)\|_2ds
\ge
c(T,K_0,\varepsilon)
\|f_j(0)\|_2.
}
\]

So the M17-158 strong finite-lag mass exit becomes

\[
\boxed{
G_{mass}^{strong}
\Longrightarrow
G_{boundary/turnover}^{order\ one}
\lor
H_{1,crit}^{spacetime}
\lor
G_{\kappa,\infty}
\lor
G_{relative-thin}.
}
\]

No quiet interior diffusion/strain mechanism can silently erase the packet.

---

## 8. Connection to the existing M5 forgetting gate

The earlier M5 localized packet equation already classifies order-one remainder action into

- material/advective shell crossing;
- pressure transfer through the buffer;
- viscous shell leakage;
- Bogovskii/solenoidal correction;
- internal nonlinear turnover.

The present OU calculation removes the internal quiet contribution on the relative-thick CE-H ribbon branch.
Thus the surviving action is exactly of the already typed M5 boundary/turnover kind.

This does not yet prove that the total boundary action over infinitely many packets is impossible.
It removes `strong fixed-lag forgetting` as an **untyped** survivor.

---

## 9. DSD audit

1. The survival floor uses the bounded CE-H potential in an essential way.
2. The lower bound is for fixed finite `T`; no long-time spectral gap is asserted.
3. Localization remainders are not discarded; they are the surviving order-one mechanism.
4. Pressure is absent from the vorticity interior equation but can re-enter through a localized velocity/Bogovskii representation of packet boundary transfer.
5. The next problem is a packing/total-variation bound for repeated order-one boundary action across the remote ribbon population.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
