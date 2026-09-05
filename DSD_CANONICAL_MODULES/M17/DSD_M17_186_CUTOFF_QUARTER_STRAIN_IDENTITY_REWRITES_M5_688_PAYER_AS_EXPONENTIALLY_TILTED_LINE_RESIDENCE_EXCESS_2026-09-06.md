# DSD M17-186 — The cutoff quarter-strain identity rewrites the M5-688 payer as exponentially tilted line-residence excess

Date: 2026-09-06  
Canonical ID: **M17-186**

Status: **M5-688 / GREAT-CIRCLE SYNTHESIS / M17-185 IDENTIFIED THE FULL-SPACE QUARTER-STRAIN EXCESS `int (sigma_bar_rho-1/4)L_rho dPhi` WITH PALINSTROPHY. M5-688 USES A HIGH-AMPLITUDE CUTOFF, SO THE FULL-SPACE IDENTITY CANNOT BE INSERTED SILENTLY. WITH `m=chi(rho)rho^2`, DIRECT INTEGRATION OF `Delta W=kappa W` GIVES `int chi kappa rho^2=-D_chi-B_chi`, WHERE `D_chi=int chi|grad W|^2` AND `B_chi=int chi' rho |grad rho|^2 >=0` FOR MONOTONE `chi`. COMBINING WITH THE CUTOFF ENSTROPHY CONTINUITY LAW GIVES `int(S_sigma-F/4)dk=D_chi+B_chi+E_chi'/2-C_chi^tot/2`. ON RECURRENT MEAN THIS DEFINES THE EXACT CUTOFF QUARTER-STRAIN PAYMENT. M5-688'S EXPONENTIAL CYCLE-WORK THEN SIMPLIFIES TO `D_kappa+X_kappasigma=(1/2)Q_sigma^(2)+(1/4)C+(1/2)R`, WHERE `Q_sigma^(2)=int e^(2k)(S_sigma-F/4)dk`. THUS THE NON-GRADIENT STRAIN PAYER IN M5-688 IS EXACTLY THE EXPONENTIALLY TILTED VERSION OF THE GREAT-CIRCLE LINE-RESIDENCE EXCESS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. High-amplitude cutoff quantities

Use the M5-683/M5-688 cutoff

\[
0\le\chi(\rho)\le1,
\qquad
\chi'\ge0,
\]

and define

\[
\boxed{E_\chi:=\int\chi(\rho)\rho^2dy.}
\]

The `kappa` distribution and aligned-strain distribution are

\[
F(k)=\int\delta(k-\kappa)\chi\rho^2dy,
\]

\[
S_\sigma(k)=\int\delta(k-\kappa)\chi\rho^2\sigma dy.
\]

Define the cutoff transition source

\[
\boxed{
C_\chi(k)
:=\int\delta(k-\kappa)
\chi'(\rho)\rho^3(\sigma+\kappa-1)dy
}
\]

and its total

\[
\boxed{C_\chi^{tot}:=\int C_\chi(k)dk.}
\]

---

## 2. Cutoff elliptic `kappa` moment

From

\[
\Delta W=\kappa W
\]

we have

\[
\int\chi\kappa\rho^2dy
=\int\chi W\cdot\Delta Wdy.
\]

Integrate by parts:

\[
\int\chi W\cdot\Delta W
=-\int\chi|\nabla W|^2
-\int\nabla\chi\cdot(W\cdot\nabla W).
\]

Since

\[
\nabla\chi=\chi'(\rho)\nabla\rho,
\qquad
W\cdot\partial_iW=\rho\partial_i\rho,
\]

the second term is

\[
-\int\chi'(\rho)\rho|\nabla\rho|^2dy.
\]

Define

\[
\boxed{D_\chi:=\int\chi|\nabla W|^2dy\ge0,}
\]

\[
\boxed{B_\chi:=\int\chi'(\rho)\rho|\nabla\rho|^2dy\ge0.}
\]

Then

\[
\boxed{
\int kF(k)dk
=\int\chi\kappa\rho^2dy
=-D_\chi-B_\chi.
}
\]

This is the cutoff analogue of M17-185's full-space negative `kappa` residence moment.

---

## 3. Integrated cutoff continuity equation

M5-688 gives

\[
\partial_\theta F+\partial_kG
=\left(2k-\frac12\right)F+2S_\sigma+C_\chi.
\]

Integrate over compact `k` support:

\[
E_\chi'
=2\int kFdk
-\frac12E_\chi
+2\int S_\sigma dk
+C_\chi^{tot}.
\]

Substitute Section 2 and rearrange:

\[
\boxed{
\int\left(S_\sigma-\frac14F\right)dk
=D_\chi+B_\chi
+\frac12E_\chi'
-\frac12C_\chi^{tot}.
}
\]

---

## 4. Recurrent cutoff quarter-strain excess

Take the recurrent long-time mean.
Since `E_chi` is bounded on the retained compact ensemble,

\[
\overline{E_\chi'}=0.
\]

Define

\[
\boxed{
Q_\sigma^{(0)}
:=\overline{
\int\left(S_\sigma-\frac14F\right)dk
}.
}
\]

Then

\[
\boxed{
Q_\sigma^{(0)}
=\overline{
D_\chi+B_\chi-\frac12C_\chi^{tot}
}.
}
\]

When the cutoff transition vanishes, this reduces to a strictly nonnegative quarter-strain excess, and on the full-space `chi=1` branch it reduces exactly to M17-185:

\[
Q_\sigma^{(0)}=\overline D.
\]

With a genuine cutoff, loss of positivity can occur only through the explicit transition source `C_chi^tot`.

---

## 5. Exponentially tilted quarter-strain payer

Define

\[
\boxed{
Q_\sigma^{(2)}
:=\int e^{2k}
\left(\overline S_\sigma(k)-\frac14\overline F(k)\right)dk.
}
\]

M5-688 writes

\[
D_\kappa+X_{\kappa\sigma}
=\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R
-\frac18\mathcal M,
\]

with

\[
\mathcal S=\int e^{2k}\overline S_\sigma dk,
\qquad
\mathcal M=\int e^{2k}\overline F dk.
\]

But

\[
\frac12\mathcal S-\frac18\mathcal M
=\frac12Q_\sigma^{(2)}.
\]

Therefore the exact M5-688 ledger becomes

\[
\boxed{
D_\kappa+X_{\kappa\sigma}
=\frac12Q_\sigma^{(2)}
+\frac14\mathcal C
+\frac12\mathcal R.
}
\]

Here

\[
D_\kappa
=\int e^{2k}\overline A_{\kappa\kappa}dk
\ge d_\kappa^{(2)}>0
\]

by M5-687.

---

## 6. Geometric interpretation of the quarter offset

On a regular great-circle vortex line, M5-684 gives

\[
\frac d{d\theta}\log L_\rho
=\kappa-\frac12+2\bar\sigma_\rho.
\]

Define

\[
\boxed{r_\rho:=\bar\sigma_\rho-\frac14.}
\]

Then

\[
\boxed{
\frac d{d\theta}\log L_\rho
=\kappa+2r_\rho,
}
\]

and relative to material flux `Phi'=kappa Phi`,

\[
\boxed{
\frac d{d\theta}\log\frac{L_\rho}{\Phi}
=2r_\rho.
}
\]

Thus the quantity

\[
S_\sigma-\frac14F
\]

is the `kappa`-resolved enstrophy measure of **extra line-residence growth relative to pure vorticity-flux amplification**.

The integrating-factor weight `e^{2k}` in M5-688 therefore tilts precisely this residence-growth channel by multiplier phase.

---

## 7. Correct payer architecture

The exact cycle-work now has only three conceptual payer blocks:

\[
\boxed{
\text{positive multiplier diffusion}
+\text{mixed kappa/strain-gradient work}
}
\]

balanced by

\[
\boxed{
\text{exponentially tilted quarter-strain residence}
+\text{cutoff transition}
+\text{explicit CE-H geometry}.
}
\]

The ordinary positive mass term of M5-688 is not an independent payer; it is part of the quarter-strain normalization.

---

## 8. DSD audit

### Audit A — inserting M17-185 directly into a cutoff ledger
Rejected; Sections 2--4 provide the required transition correction.

### Audit B — treating `Q_sigma^(0)>0` as automatic with cutoff
Rejected. A sufficiently strong positive cutoff-transition source can reverse it.

### Audit C — treating `Q_sigma^(2)` as having the same sign as `Q_sigma^(0)`
Rejected. The signed quarter-strain density can be phase-segregated across `kappa`.

### Audit D — proof status
The payer ledger is simplified and geometrically interpreted, but no contradiction is obtained.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
