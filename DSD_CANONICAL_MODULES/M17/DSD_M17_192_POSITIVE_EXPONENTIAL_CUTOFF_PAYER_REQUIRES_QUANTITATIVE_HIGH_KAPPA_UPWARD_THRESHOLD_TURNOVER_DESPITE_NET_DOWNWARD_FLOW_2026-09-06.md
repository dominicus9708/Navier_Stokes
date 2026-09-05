# DSD M17-192 — A positive exponential cutoff payer requires quantitative high-`kappa` upward threshold turnover despite net downward flow

Date: 2026-09-06  
Canonical ID: **M17-192**

Status: **CUTOFF PHASE-SEGREGATION GATE / M17-191 PROVES THAT THE RECURRENT UNWEIGHTED CUTOFF SOURCE `C_0=int bar C_chi(k) dk` IS STRICTLY NEGATIVE ON A NONTRIVIAL TRANSITION LAYER, WITH `A_0:=-C_0=(3/2)int chi'(a)a^2 bar V_a da>0`. M5-688, HOWEVER, USES THE EXPONENTIALLY TILTED PAYER `C_2=int e^(2k) bar C_chi(k) dk`, WHICH CAN BE POSITIVE ONLY IF THE POSITIVE PART OF THE CUTOFF-SOURCE DISTRIBUTION IS SUFFICIENTLY CONCENTRATED AT HIGHER KAPPA. FOR SUPPORT `|k|<=K_*`, `C_2<= (e^(2K_*)-e^(-2K_*))C_+ - e^(-2K_*)A_0`, SO `C_2>=0` FORCES `C_+ >= A_0/(e^(4K_*)-1)`. VIA AMPLITUDE COAREA, THIS IS A FIXED POSITIVE UPWARD/REPLENISHING THRESHOLD-TURNOVER POPULATION EVEN THOUGH THE NET THRESHOLD FLOW IS DOWNWARD. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Signed cutoff-source density

Let

\[
\boxed{
C(k):=\overline{C_\chi(k)}
}
\]

be the recurrent mean cutoff-source density from M5-688.

Assume compact multiplier support

\[
\boxed{|k|\le K_*}.
\]

M17-191 gives

\[
\boxed{
\int C(k)dk
=-A_0<0,
}
\]

where

\[
\boxed{
A_0
:=\frac32
\int_0^\infty
\chi'(a)a^2\overline{V_a}\,da
>0
}
\]

on a nontrivial cutoff transition layer.

The M5-688 exponential cutoff payer is

\[
\boxed{
\mathcal C_2
:=\int e^{2k}C(k)dk.
}
\]

---

## 2. Positive and negative turnover masses

Write

\[
C=C_+-C_-,
\qquad
C_+,C_-\ge0.
\]

Define

\[
c_+:=\int C_+dk,
\qquad
c_-:=\int C_-dk.
\]

Since the total is `-A_0`,

\[
\boxed{c_- - c_+=A_0.}
\]

The negative part is the dominant unweighted threshold flow.

---

## 3. Upper bound for the exponential payer

Because

\[
e^{-2K_*}\le e^{2k}\le e^{2K_*},
\]

we have

\[
\begin{aligned}
\mathcal C_2
&=\int e^{2k}C_+dk-\int e^{2k}C_-dk\\
&\le e^{2K_*}c_+-e^{-2K_*}c_-.
\end{aligned}
\]

Use `c_-=A_0+c_+`:

\[
\boxed{
\mathcal C_2
\le
\left(e^{2K_*}-e^{-2K_*}\right)c_+
-e^{-2K_*}A_0.
}
\]

---

## 4. Quantitative positive-turnover requirement

If the cutoff channel is to be nonnegative in the M5-688 cycle-work,

\[
\boxed{\mathcal C_2\ge0,}
\]

then Section 3 forces

\[
\boxed{
c_+
\ge
\frac{A_0}{e^{4K_*}-1}.
}
\]

More generally, if

\[
\mathcal C_2\ge c_*>0,
\]

then

\[
\boxed{
c_+
\ge
\frac{e^{-2K_*}A_0+c_*}
{e^{2K_*}-e^{-2K_*}}.
}
\]

Thus a positive exponential cutoff payer requires a fixed positive amount of the otherwise subdominant positive cutoff source.

---

## 5. Threshold-turnover interpretation

M17-191 gives the amplitude-coarea representation

\[
C_\chi^{tot}
=\int\chi'(a)a^2\mathcal T_a da,
\]

where

\[
\mathcal T_a
=a\int_{\rho=a}
\frac{\sigma+\kappa-1}{|\nabla\rho|}dS.
\]

The pointwise positive part of the underlying cutoff source is therefore supported where

\[
\boxed{
\sigma+\kappa-1>0
}
\]

on amplitude-threshold surfaces.

This is precisely the material **upward/replenishing amplitude crossing** direction.

Because taking the positive part after averaging can only reduce the amount of positive microscopic source, the lower bound on `c_+` implies at least the same qualitative positive lower bound on the underlying space-time upward threshold-turnover occupancy.

---

## 6. Why the positive part must be `kappa`-phase segregated

Unweighted threshold turnover has

\[
\int C=-A_0<0.
\]

For the increasing weight `e^(2k)` to make the result nonnegative, positive turnover must receive a larger average exponential multiplier weight than negative turnover.

Thus the branch requires

\[
\boxed{
\text{upward threshold turnover biased toward larger }\kappa,
}
\]

relative to the net downward turnover population.

This is the cutoff analogue of the quarter-strain phase segregation in M17-187.

---

## 7. Updated M5-688 payer tree

After M17-191--192, the cutoff channel cannot be described simply as an arbitrary signed remainder.

Its two possibilities are

\[
\boxed{
\mathcal C_2<0
\quad\Rightarrow\quad
\text{it worsens the positive multiplier-diffusion payment},
}
\]

or

\[
\boxed{
\mathcal C_2\ge0
\quad\Rightarrow\quad
G_{threshold}^{up,+}
\text{ with quantitative }\kappa\text{-phase segregation}.
}
\]

Thus a positive cutoff payer itself carries a definite recurrent turnover obligation.

---

## 8. DSD audit

### Audit A — inferring the sign of `mathcal C_2` from the unweighted sign
Rejected; exponential tilting can reverse a signed distribution.

### Audit B — treating sign reversal as free
Rejected by the quantitative positive-part lower bound.

### Audit C — calling positive cutoff source a new independent mechanism
It is exactly amplitude-threshold replenishment written in the M5-688 weighted ledger; no double counting is allowed.

### Audit D — proof status
A new positive turnover population is forced if the cutoff channel pays, but recurrent replenishment is not yet contradictory.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
