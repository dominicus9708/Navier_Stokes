# DSD M17-187 — Suppressing the exponential quarter-strain payer forces quantitative `kappa`-phase-segregated strain deficit

Date: 2026-09-06  
Canonical ID: **M17-187**

Status: **PHASE-SEGREGATION GATE / LET `Q(k)=bar S_sigma(k)-(1/4)bar F(k)` BE THE RECURRENT CUTOFF QUARTER-STRAIN DENSITY OF M17-186, SUPPORTED IN `[-K_*,K_*]`. IF ITS UNWEIGHTED TOTAL `P_0=int Q` IS POSITIVE BUT THE M5-688 EXPONENTIALLY TILTED PAYER `Q^(2)=int e^(2k)Q` IS SMALL, THE NEGATIVE PART OF `Q` CANNOT BE ARBITRARILY SMALL. EXACTLY, `Q^(2) >= e^(-2K_*) P_0 -(e^(2K_*)-e^(-2K_*)) P_-`, SO `P_- >= [e^(-2K_*)P_0-Q^(2)]_+/(e^(2K_*)-e^(-2K_*))`. IN PARTICULAR, IF `Q^(2)<=(1/2)e^(-2K_*)P_0`, THEN `P_- >= P_0/[2(e^(4K_*)-1)]`. THUS A SURVIVOR THAT REFUSES TO PAY THE MULTIPLIER-DIFFUSION CHARGE THROUGH A POSITIVE EXPONENTIAL QUARTER-STRAIN TERM MUST MAINTAIN A FIXED POSITIVE POPULATION OF `sigma-1/4` DEFICIT, ARRANGED AT SUFFICIENTLY LARGE KAPPA TO BENEFIT FROM THE EXPONENTIAL TILT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Signed quarter-strain density

Use the recurrent high-amplitude cutoff distributions of M17-186:

\[
\boxed{
Q(k)
:=\overline S_\sigma(k)-\frac14\overline F(k).
}
\]

Assume the retained `kappa` support satisfies

\[
\boxed{|k|\le K_*<\infty.}
\]

Define the unweighted total

\[
\boxed{P_0:=\int_{-K_*}^{K_*}Q(k)dk}
\]

and the M5-688 exponential payer

\[
\boxed{
P_2:=\int_{-K_*}^{K_*}e^{2k}Q(k)dk.
}
\]

M17-186 identifies `P_2=Q_sigma^(2)`.

The present module assumes first

\[
\boxed{P_0>0.}
\]

The complementary `P_0<=0` branch is treated in Section 6.

---

## 2. Positive/negative decomposition

Write

\[
Q=Q_+-Q_-,
\qquad
Q_+,Q_-\ge0,
\]

with disjoint supports in the scalar sign sense.

Define

\[
P_+:=\int Q_+dk,
\qquad
P_-:=\int Q_-dk.
\]

Then

\[
\boxed{P_+-P_-=P_0.}
\]

Because

\[
e^{-2K_*}\le e^{2k}\le e^{2K_*},
\]

we have

\[
\begin{aligned}
P_2
&=\int e^{2k}Q_+dk-\int e^{2k}Q_-dk\\
&\ge e^{-2K_*}P_+-e^{2K_*}P_-.
\end{aligned}
\]

Using `P_+=P_0+P_-`,

\[
\boxed{
P_2
\ge
 e^{-2K_*}P_0
-\left(e^{2K_*}-e^{-2K_*}\right)P_-.
}
\]

---

## 3. Quantitative deficit lower bound

Rearranging Section 2 gives

\[
\boxed{
P_-
\ge
\frac{
\left[e^{-2K_*}P_0-P_2\right]_+
}{e^{2K_*}-e^{-2K_*}}.
}
\]

This is an exact algebraic consequence of compact `kappa` support.

In particular, if the exponential payer is suppressed below half of the minimal positive-weight scale,

\[
\boxed{
P_2
\le
\frac12e^{-2K_*}P_0,
}
\]

then

\[
\boxed{
P_-
\ge
\frac{P_0}{2(e^{4K_*}-1)}.
}
\]

Thus an order-one positive unweighted quarter-strain excess cannot have an arbitrarily small negative part if exponential tilting makes its net payer small.

---

## 4. Physical meaning of the negative part

On the interior region where the high-amplitude cutoff is one, great-circle flux coordinates give

\[
S_\sigma(k)-\frac14F(k)
=\int
\left(\bar\sigma_\rho-\frac14\right)
L_\rho
\delta(k-\kappa)d\Phi.
\]

Even when several labels contribute at one `k`, the scalar negative part satisfies

\[
\boxed{
P_-
\le
\overline{
\int
\left(\frac14-\bar\sigma_\rho\right)_+
L_\rho\,d\Phi
}
}
\]

up to the explicit cutoff-transition segment bookkeeping already isolated in M17-186.

Therefore the bound in Section 3 forces a genuine positive enstrophy-residence population with

\[
\boxed{
\bar\sigma_\rho<\frac14.
}
\]

This is the **quarter-strain deficit population**.

---

## 5. Why this is `kappa`-phase segregation

The exponential weight `e^(2k)` is strictly increasing in `k`.

For a positive unweighted total `P_0` to become small or negative after this tilt, negative quarter-strain contributions must be placed sufficiently far toward larger `kappa` relative to the positive contributions.

Thus the escape is not arbitrary cancellation; it requires a covariance pattern

\[
\boxed{
\text{quarter-strain excess biased toward lower }\kappa,
\qquad
\text{quarter-strain deficit biased toward higher }\kappa.
}
\]

The coarse lower bound of Section 3 quantifies the amount of deficit required even without assuming a detailed ordering of the supports.

---

## 6. The `P_0<=0` branch is a cutoff-transition payer

M17-186 gives on recurrent mean

\[
P_0
=\overline{
D_\chi+B_\chi-\frac12C_\chi^{tot}
}.
\]

Here

\[
D_\chi\ge0,
\qquad
B_\chi\ge0.
\]

Therefore if

\[
\boxed{P_0\le0,}
\]

then necessarily

\[
\boxed{
\overline{C_\chi^{tot}}
\ge
2\overline{D_\chi+B_\chi}.
}
\]

Thus failure of the positive unweighted quarter-strain excess is not free: the amplitude-cutoff transition layer must supply a positive source at least as large as twice the cutoff palinstrophy-plus-amplitude-gradient payment.

Hence the branch split is

\[
\boxed{
P_0\le0
\Longrightarrow
G_{cutoff\ transition}^{+},
}
\]

or

\[
\boxed{
P_0>0
\Longrightarrow
G_{quarter}^{exp,+}
\lor
G_{quarter}^{deficit/phase\ segregation}.
}
\]

---

## 7. Combine with the M5-688 positive diffusion charge

M17-186 rewrites M5-688 as

\[
D_\kappa+X_{\kappa\sigma}
=\frac12P_2
+\frac14\mathcal C
+\frac12\mathcal R,
\]

with

\[
D_\kappa\ge d_\kappa^{(2)}>0.
\]

Therefore the regular conveyor can pay the uniform multiplier-diffusion charge only through a combination of

1. strain-gradient work `X_kappasigma`;
2. positive exponential quarter-strain residence `P_2`;
3. the quantitative quarter-strain deficit / `kappa`-phase segregation of Sections 3--5, if `P_2` is suppressed;
4. cutoff transition `C`;
5. explicit CE-H geometric remainder `R`.

The formerly vague strain-residence escape is now split into two quantitatively distinct subbranches.

---

## 8. DSD audit

### Audit A — claiming `P_0>0` forces `P_2>0`
Rejected; the signed density can phase-segregate in `kappa`.

### Audit B — calling phase segregation free
Rejected by the positive deficit lower bound.

### Audit C — identifying the scalar negative part with a unique set of vortex labels
The scalar inequality is one-way; cancellations at fixed `k` can only increase the underlying physical deficit occupancy needed.

### Audit D — proof status
A quantitative payer population is forced, but recurrent maintenance of that population is not yet contradictory.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
