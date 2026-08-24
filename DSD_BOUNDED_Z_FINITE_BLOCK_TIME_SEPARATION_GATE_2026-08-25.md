# DSD bounded-Z finite-block time separation gate

Date: 2026-08-25

Status: **FIXED-GAP PARABOLIC TIME LOWER BOUND PROVED / INFINITELY MANY POSITIVE ADJACENT NORMALIZED GAPS PROVED / FULL ADJACENT LOWER CORRIDOR NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

This note continues the DSD first-hitting audit using only finite endpoint witnesses. It does not identify any previously used symbol `L_j` with the adjacent first-hitting gap. The goal is to decide whether all adjacent normalized time gaps can collapse to zero on the bounded-Z branch.

## 1. Global enstrophy differential inequality

Let

\[
Y(t):=\|\omega(t)\|_2^2,
\qquad
P(t):=\|\nabla\omega(t)\|_2^2.
\]

For a smooth whole-space pre-singular solution,

\[
\frac12Y'(t)+\nu P(t)
=
\int_{\mathbb R^3}\omega^TS\omega\,dx.
\]

By Calderon-Zygmund boundedness on `L^3`, Holder, and Gagliardo-Nirenberg,

\[
\begin{aligned}
\left|\int\omega^TS\omega\right|
&\le \|S\|_3\|\omega\|_3^2\\
&\le C\|\omega\|_3^3\\
&\le C\|\omega\|_2^{3/2}\|\nabla\omega\|_2^{3/2}\\
&=C Y^{3/4}P^{3/4}.
\end{aligned}
\]

Young's inequality gives

\[
C Y^{3/4}P^{3/4}
\le \frac\nu2P+C_0\nu^{-3}Y^3.
\]

Therefore, after enlarging the universal constant if necessary,

\[
\boxed{Y'(t)\le C_1\nu^{-3}Y(t)^3.}
\]

Equivalently wherever `Y>0`,

\[
\boxed{
\frac d{dt}Y(t)^{-2}
\ge -2C_1\nu^{-3}.
}
\]

Status: **PROVED.**

## 2. Bounded-Z early endpoint and analytic future endpoint

At first-hitting stage `j`, bounded-Z gives

\[
\boxed{
Y(t_j)
\le Z_*\frac{\nu^2}{r_j}.
}
\]

The analytic occupied core gives, at every late first-hitting stage `n`,

\[
\boxed{
Y(t_n)
\ge z_a\frac{\nu^2}{r_n},
\qquad
z_a:=\frac\pi3r_a^3>0.
}
\]

For a finite generation gap `k`, let

\[
n=j+k.
\]

Since

\[
r_j=q^{k/2}r_n,
\]

we have

\[
Y(t_j)
\le Z_*q^{-k/2}\frac{\nu^2}{r_n}.
\]

Choose once and for all

\[
\boxed{
k_T:=\min\left\{k\in\mathbb N:
Z_*q^{-k/2}\le\frac{z_a}{4}
\right\}.}
\]

For `n=j+k_T`, define the finite target level

\[
\boxed{
H_n:=\frac{z_a}{2}\frac{\nu^2}{r_n}.
}
\]

Then

\[
Y(t_j)\le\frac12H_n,
\qquad
Y(t_n)\ge2H_n.
\]

Hence, by continuity, there exists a first time `\bar t in (t_j,t_n)` with

\[
Y(\bar t)=H_n,
\]

and

\[
Y(t)\le H_n
\qquad(t_j\le t\le\bar t).
\]

Status: **PROVED.**

## 3. A finite first-hitting block needs parabolic time

Integrate the inverse-enstrophy inequality from `t_j` to `\bar t`:

\[
H_n^{-2}
\ge
Y(t_j)^{-2}
-2C_1\nu^{-3}(\bar t-t_j).
\]

Because `Y(t_j)<=H_n/2`,

\[
Y(t_j)^{-2}\ge4H_n^{-2}.
\]

Therefore

\[
2C_1\nu^{-3}(\bar t-t_j)
\ge3H_n^{-2}.
\]

Using

\[
H_n^2
=\frac{z_a^2}{4}\frac{\nu^4}{r_n^2},
\]

we obtain

\[
\boxed{
\bar t-t_j
\ge
c_T\frac{r_n^2}{\nu},
\qquad
c_T:=\frac{6}{C_1z_a^2}>0.
}
\]

Since `\bar t<t_n`,

\[
\boxed{
 t_{j+k_T}-t_j
\ge
c_T\frac{r_{j+k_T}^2}{\nu}.
}
\]

Equivalently, because `r_{j+k_T}^2=q^{-k_T}r_j^2`,

\[
\boxed{
\frac{\nu(t_{j+k_T}-t_j)}{r_j^2}
\ge
c_Tq^{-k_T}
=:\Theta_T>0.
}
\]

Thus the bounded-Z first-hitting tower cannot cross every fixed `k_T`-generation block in vanishing normalized parabolic time.

Status: **PROVED.**

## 4. Consequence for adjacent normalized first-hitting gaps

Define explicitly

\[
\boxed{
\tau_m
:=\frac{\nu(t_{m+1}-t_m)}{r_m^2}.
}
\]

For the fixed block length `k_T`,

\[
\begin{aligned}
\frac{\nu(t_{j+k_T}-t_j)}{r_j^2}
&=
\sum_{\ell=0}^{k_T-1}
\frac{\nu(t_{j+\ell+1}-t_{j+\ell})}{r_j^2}\\
&=
\sum_{\ell=0}^{k_T-1}
q^{-\ell}\tau_{j+\ell}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{\ell=0}^{k_T-1}q^{-\ell}\tau_{j+\ell}
\ge\Theta_T.
}
\]

Let

\[
Q_T:=\sum_{\ell=0}^{k_T-1}q^{-\ell}
<\frac q{q-1}.
\]

At least one index `m in {j,...,j+k_T-1}` must satisfy

\[
\boxed{
\tau_m\ge\tau_0:=\frac{\Theta_T}{Q_T}>0.
}
\]

Hence every sufficiently late fixed-length block contains at least one positive normalized adjacent dwell.

In particular,

\[
\boxed{
\tau_j\not\to0
\quad\text{along all late generations.}
}
\]

There are infinitely many adjacent first-hitting transitions with

\[
\tau_j\ge\tau_0.
\]

Status: **PROVED.**

## 5. Optional upper tightness from the previously established remaining-time bound

If one imports the already-established first-hitting remaining-time estimate

\[
T^*-t_j\le C_*\frac{r_j^2}{\nu},
\]

then

\[
t_{j+1}-t_j\le T^*-t_j
\]

immediately yields

\[
\boxed{
\tau_j\le C_*.
}
\]

Combined with Section 4, there exists an infinite subsequence of adjacent stages satisfying

\[
\boxed{
\tau_0\le\tau_{j_m}\le C_*.
}
\]

Thus a positive finite normalized-time subsequential limit can be extracted:

\[
\tau_{j_m}\to\tau_*\in[\tau_0,C_*].
\]

Status: **PROVED CONDITIONAL ON THE IMPORTED REMAINING-TIME UPPER BOUND.**

No use is made of differences of two remaining-time upper bounds; the earlier audit warning is respected.

## 6. DSD meaning

The singular approach is described by finite first-hitting witnesses. The present gate proves that a fixed finite amount of new normalized enstrophy cannot be formed arbitrarily fast in every generation block.

Therefore the transition tuple

\[
(a_j,\tau_j,\Omega_j,\Omega_{j+1})
\]

cannot escape exclusively through the `tau_j->0` channel.

The surviving transition alternatives are sharpened to:

\[
\boxed{
\text{positive normalized dwell on infinitely many transitions}
\lor
\text{center/base non-tightness}
\lor
\text{renormalization-state drift}.
}
\]

The previously excluded `tight same-profile zero-gap` branch is now seen to be non-generic even before invoking its L2 contradiction: bounded-Z forces positive dwell somewhere in every fixed finite block.

## 7. What this does not prove

The result does not show

\[
\tau_j\ge\tau_0
\quad\text{for every late }j.
\]

Nor does it identify the historical repository symbol `L_j` with `tau_j`.

It also does not yet show that a positive-dwell transition must have a large describability difference, or that state drift during such a transition carries a nonsummable kinetic-energy cost.

Those are separate gates.

## 8. Next DSD gate

On an infinite positive-dwell subsequence with bounded `tau_j`, the exact transition identity gives a genuine finite spacetime window on which neighboring normalized solution states may be compared.

The next question is therefore:

\[
\boxed{
\text{Can a compact bounded-Z renormalization state traverse an order-one first-hitting formation over positive normalized time indefinitely without either recurring or producing a finite-budget variation?}
}
\]

This is the **Renormalization-State Variation Gate (RSVG)**.

Current status:

\[
\boxed{\text{RSVG: NOT DERIVED.}}
\]

## 9. Audit verdict

### PROVED

- `Y'<=C nu^{-3}Y^3`;
- a fixed sufficiently large but finite first-hitting generation block needs time `>= c r_n^2/nu`;
- every such block contains an adjacent normalized gap `tau_j>=tau_0>0`;
- therefore all late adjacent gaps cannot collapse to zero.

### PROVED CONDITIONAL

- infinitely many adjacent gaps lie in a compact positive interval `[tau_0,C_*]`, if the established remaining-time upper bound is imported.

### NOT DERIVED

- a positive lower bound for every adjacent `tau_j`;
- identification of `L_j` with `tau_j`;
- RSVG;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
