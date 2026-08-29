# DSD M5-232 — Strain-Negative Mode / Compressive Spectral Gate

Date: 2026-08-30

Parent: `DSD_M5_231_NEGATIVE_CRITICAL_BALANCE_PRESSURE_TRANSPORT_CANCELLATION_FIREWALL_2026-08-30.md`

Status: **POSITIVE SHARPENING / THE THREE-CHANNEL PARTITION CAN BE MADE AGAINST THE ACTUAL VISCOUS CELL ENERGY, NOT ONLY ITS FIXED FLOOR / IF STRAIN PAYS ONE THIRD OF THE NEGATIVE BALANCE THEN THE COMMON STATIONARY TAIL MUST HAVE A QUANTITATIVELY LARGE COMPRESSIVE EIGENDIRECTION SEEN BY THE FINITE-DILATE RELATIVE VELOCITY MODE / THIS IS A LINEARIZED-SPECTRAL INSTABILITY CHANNEL, NOT THE BETCHOV VORTICITY-STRETCHING CHANNEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact negative balance

For one nontrivial finite dilation difference

\[
W=D_hT-T=r^{-1}\Psi,
\]

M5-230/231 give the exact invariant-mean identity

\[
\boxed{
\nu \mathcal D
+
\mathcal N_S
+
\mathcal N_{tr}
+
\mathcal N_p
=0,
}
\]

where

\[
\mathcal D
:=
\left\langle
\int_{S^2}
\bigl(|\partial_y\Psi|^2+|\nabla_{S^2}\Psi|^2\bigr)
\,d\theta
\right\rangle
>0.
\]

The strict positivity follows from the M5-230 solenoidal cell coercivity and the M5-219 finite-dilate separation.

M5-231 stated the safe fixed-floor fork using

\[
\mathcal D\ge d_D^*>0.
\]

But the exact identity gives a sharper partition:

\[
\boxed{
\mathcal N_S\le-\frac{\nu\mathcal D}{3}
\quad\lor\quad
\mathcal N_{tr}\le-\frac{\nu\mathcal D}{3}
\quad\lor\quad
\mathcal N_p\le-\frac{\nu\mathcal D}{3}.
}
\]

This relative-to-actual-dissipation form is used below.

---

## 2. Strain payer

Assume the first branch:

\[
\boxed{
\mathcal N_S
=
\left\langle
\int_{S^2}
\Psi^T\mathcal S_\Phi\Psi
\,d\theta
\right\rangle
\le
-\frac{\nu\mathcal D}{3}.
}
\]

Let

\[
\mathcal S_\Phi
=
\mathcal S_\Phi^+-\mathcal S_\Phi^-,
\qquad
\mathcal S_\Phi^\pm\ge0,
\]

be the spectral positive/negative parts.

Then

\[
\Psi^T\mathcal S_\Phi\Psi
\ge
-\Psi^T\mathcal S_\Phi^-\Psi,
\]

so

\[
\boxed{
\left\langle
\int_{S^2}
\Psi^T\mathcal S_\Phi^-\Psi
\,d\theta
\right\rangle
\ge
\frac{\nu\mathcal D}{3}.
}
\]

Thus a strain-paying survivor must place a fixed fraction of its relative mode inside compressive eigendirections of the background tail.

---

## 3. Use the solenoidal cell Poincare constant

Let `C_sol` denote the M5-230 solenoidal cell coercivity constant:

\[
\boxed{
\left\langle
\int_{S^2}|\Psi|^2d\theta
\right\rangle
\le
C_{\rm sol}\mathcal D.
}
\]

This is legitimate because the zero mode of

\[
|\Psi_y|^2+|\nabla_{S^2}\Psi|^2
\]

is excluded by the degree `-1` divergence-free constraint; equality at zero derivative would force `Psi=0`.

Let

\[
\Lambda_-^*
:=
\operatorname*{ess\,sup}_{(y,\theta)}
\lambda_{\max}(\mathcal S_\Phi^-(y,\theta)).
\]

Then

\[
\Psi^T\mathcal S_\Phi^-\Psi
\le
\Lambda_-^*|\Psi|^2,
\]

and therefore

\[
\frac{\nu\mathcal D}{3}
\le
\Lambda_-^* C_{\rm sol}\mathcal D.
\]

Since `D>0`, cancel it:

\[
\boxed{
\Lambda_-^*
\ge
\frac{\nu}{3C_{\rm sol}}.
}
\]

This is an amplitude threshold independent of the size of the selected finite-dilate difference.

---

## 4. Trace-free conversion to a strain-norm threshold

For any real symmetric trace-free `3x3` matrix `S`,

\[
|\lambda_{\min}(S)|
\le
\sqrt{\frac23}|S|.
\]

Equality occurs at the axisymmetric eigenvalue pattern

\[
(-2a,a,a).
\]

Hence the strain-payer condition implies

\[
\boxed{
\|\mathcal S_\Phi\|_{L^\infty(cyl)}
\ge
\frac{\nu}{\sqrt6\,C_{\rm sol}}.
}
\]

Thus the strain branch is automatically a **large critical strain-amplitude branch**.

It cannot occur in a perturbative tail regime below this threshold.

---

## 5. Compressive alignment occupancy

Define, where `Psi != 0` and `S^- != 0`,

\[
\mathfrak a_-(y,\theta)
:=
\frac{\Psi^T\mathcal S_\Phi^-\Psi}
{\lambda_{\max}(\mathcal S_\Phi^-)|\Psi|^2}
\in[0,1].
\]

Then

\[
\left\langle
\int
\lambda_{\max}(\mathcal S_\Phi^-)
\mathfrak a_-|\Psi|^2
\right\rangle
\ge
\frac{\nu\mathcal D}{3}.
\]

Therefore the negative payment cannot be generated solely by the existence of a remote compressive eigenvalue that is invisible to `Psi`.

There must be nonzero weighted occupancy of

\[
\boxed{
\text{large compression}
\cap
\text{relative-mode alignment}.
}
\]

A standard threshold split makes this quantitative: for any `0<eta<1`, either a positive portion of the `|Psi|^2` mass lies where

\[
\lambda_{\max}(S^-)
\ge
\eta\frac{\nu}{3C_{\rm sol}},
\]

or the complementary region cannot supply the required mean payment.

---

## 6. Why this is not the Betchov channel

The classical Betchov identity controls

\[
\int \omega^TS\omega
\]

through

\[
-4\int\det S.
\]

The present quantity is instead

\[
\int \Psi^TS\Psi,
\]

where `Psi` is a relative **velocity** mode between two dilates of the same stationary tail.

There is no identity

\[
\Psi^TS\Psi
\equiv
\omega^TS\omega
\]

or any universal sign conversion between them.

Hence the implication

\[
\boxed{
\mathcal N_S<0
\Rightarrow
\text{Betchov positive-middle production}
}
\]

is RED.

In fact the signs point in different geometric directions: the present mode pays by occupying compression, whereas positive vortex stretching pays by occupying extension.

---

## 7. Correct interpretation

The strain branch says that the stationary relative operator

\[
-\nu\Delta
+(T\cdot\nabla)
+(\,\cdot\,\nabla)T
\]

possesses a scale-critical mode whose symmetric-gradient quadratic form defeats a fixed fraction of viscosity.

Thus it is best typed as

\[
\boxed{
\text{large-amplitude compressive linearized-spectral channel}.
}
\]

Equivalently, after the transport/pressure pieces are separated, the strain payer is a negative direction of the symmetric part of the fixed-force stationary linearization in the scale-invariant cell metric.

This is a genuine stability/Morse-index issue, not a recurrence bookkeeping issue.

---

## 8. DSD verdict

### PROVED

- sharpened one-third trichotomy against the actual `D`, not only `d_D^*`;
- strain payer forces
  \[
  \Lambda_-^*\ge\nu/(3C_{sol});
  \]
- trace-free structure gives
  \[
  \|S_\Phi\|_\infty\ge\nu/(\sqrt6 C_{sol});
  \]
- the relative mode must actually occupy compressive directions.

### FIREWALL

Betchov/vorticity-stretching identities do not close this velocity-mode compression channel.

### REMAINING

The strain branch can now be excluded only by a nondegeneracy/stability theorem for the large fixed-point-force stationary solution, or by routing its compressive relative mode into another already finite DSD cost.

---

## 9. Next target

Audit the second M5-231 branch

\[
\mathcal N_{tr}\le-\frac{\nu\mathcal D}{3}
\]

using the exact finite-dilate identity

\[
\Psi_h(y,\theta)
=
\Phi(y-h/2,\theta)-\Phi(y,\theta).
\]

The question is whether persistent negative radial-transport payment forces a one-sided outward-sector locking incompatible with zero spherical flux and minimal log-translation recurrence, or merely creates another large-amplitude correlation channel.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]