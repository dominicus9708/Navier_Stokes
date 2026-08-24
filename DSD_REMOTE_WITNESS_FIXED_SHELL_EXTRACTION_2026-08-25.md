# DSD Remote-Witness Fixed-Shell Extraction Gate

Date: 2026-08-25

Status: **FIXED-SHELL EXTRACTION FROM POSITIVE-DENSITY REMOTE ENSTROPHY PROVED / FIXED-AGE LOCAL CONCENTRATION PROVED / MATERIAL IDENTITY STILL NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous direct-Betchov positive-density gate produces a recurrent-time set of positive density on which the parent first-hitting normalization carries a fixed amount of vorticity enstrophy outside a fixed normalized radius.

The remaining concern was that this remote mass might evade every finite genealogy comparison by moving through larger and larger shells, so that no fixed shell or fixed generation lag recurs.

This note shows that such complete radial drift is impossible at the level of recurrent time averages.

The argument is purely nonnegative shell algebra plus Tonelli and does not require a material genealogy assumption.

---

## 2. Imported positive-density remote witness

Work on the bounded-Z recurrent first-hitting/Leray corridor.

From `DSD_DIRECT_BETCHOV_HIGH_ENSTROPHY_POSITIVE_DENSITY_2026-08-25.md`, there exists a measurable recurrent-time set `A_rw` with

\[
\boxed{\mu(A_{rw})=d_{rw}>0}
\]

and fixed constants

\[
R_0>0,
\qquad
m_*>0
\]

such that for every `s in A_rw`, after transfer to the parent first-hitting normalization of the containing stage,

\[
\boxed{
\int_{|y|>R_0}|\Omega(y,s)|^2dy\ge m_*.
}
\]

Why `R_0` can be fixed: the canonical quantile radius in the previous note has a uniform positive lower bound `R_min`; the witness mass lies outside `alpha R_epsilon(s)`, hence also outside the smaller fixed radius `R_0=alpha R_min`.

No upper bound on the actual quantile radius is assumed.

---

## 3. Generation-adapted shells

Let

\[
\lambda:=\sqrt q>1.
\]

Use the geometric shells

\[
A_k
:=
\{R_k\le |y|<\lambda R_k\},
\qquad
R_k:=R_0\lambda^k,
\qquad k=0,1,2,\ldots.
\]

Define shell enstrophy masses

\[
\boxed{
m_k(s):=\int_{A_k}|\Omega(y,s)|^2dy.}
\]

Then on every remote-witness time,

\[
\sum_{k=0}^\infty m_k(s)
\ge m_*.
\]

The choice `lambda=sqrt(q)` is deliberate: at a first-hitting checkpoint,

\[
r_{j-k}=\lambda^k r_j.
\]

Thus a fixed shell index is also a fixed finite generation lag, up to the constant base factor `R_0`.

---

## 4. Critical shell mass inequality

Define

\[
\boxed{
a_k(s):=(R_km_k(s))^{3/2}.}
\]

Then

\[
m_k=a_k^{2/3}R_k^{-1}.
\]

Holder with exponents `3/2` and `3` gives

\[
\sum_km_k
\le
\left(\sum_ka_k\right)^{2/3}
\left(\sum_kR_k^{-3}\right)^{1/3}.
\]

Because

\[
\sum_{k=0}^\infty R_k^{-3}
=
\frac{R_0^{-3}}{1-\lambda^{-3}},
\]

we obtain, on every `s in A_rw`,

\[
\boxed{
\sum_{k=0}^\infty (R_km_k(s))^{3/2}
\ge
\sqrt{1-\lambda^{-3}}\,
R_0^{3/2}m_*^{3/2}.
}
\]

Set

\[
\boxed{
A_*:=
\sqrt{1-\lambda^{-3}}\,
R_0^{3/2}m_*^{3/2}>0.
}
\]

This step uses only exterior L2 mass. It does not use the non-H shell merger or a velocity-tail estimate.

---

## 5. Tonelli extracts one fixed shell

Integrate over the positive-density witness set.

Since all terms are nonnegative, Tonelli gives

\[
\begin{aligned}
\sum_{k=0}^\infty
\int_{A_{rw}}a_k(s)d\mu(s)
&=
\int_{A_{rw}}
\sum_{k=0}^\infty a_k(s)d\mu(s)\\
&\ge
A_*d_{rw}>0.
\end{aligned}
\]

Therefore not every fixed shell can have zero recurrent mean.

There exists at least one finite index

\[
\boxed{k_0<\infty}
\]

such that

\[
\boxed{
\int_{A_{rw}}
(R_{k_0}m_{k_0}(s))^{3/2}d\mu(s)>0.
}
\]

Thus complete radial dephasing through shell indices tending to infinity cannot carry all of the positive-density remote-witness charge.

Status: **PROVED.**

---

## 6. Positive-density threshold on the fixed shell

A nonnegative measurable function with positive integral must exceed some positive threshold on a set of positive measure.

Hence there exist

\[
\delta_*>0
\]

and a measurable set

\[
B_*\subset A_{rw}
\]

such that

\[
\boxed{\mu(B_*)>0}
\]

and for every `s in B_*`,

\[
\boxed{
(R_{k_0}m_{k_0}(s))^{3/2}\ge\delta_*.
}
\]

Equivalently,

\[
\boxed{
R_{k_0}m_{k_0}(s)
\ge
J_*:=\delta_*^{2/3}>0.
}
\]

So a fixed generation-adapted shell carries a fixed scale-critical enstrophy mass on a positive-density recurrent-time set.

Status: **PROVED.**

---

## 7. Finite covering converts shell mass to a local ball

The fixed annulus `A_{k_0}` has fixed aspect ratio `lambda`.

Choose a fixed `sigma in (0,1)` small enough that `A_{k_0}` can be covered by at most

\[
N_*=N_*(\lambda,\sigma)<\infty
\]

balls of normalized radius

\[
\rho_*:=\sigma R_{k_0}.
\]

For every `s in B_*`, at least one covering ball `B_{rho_*}(y_*(s))` satisfies

\[
\int_{B_{\rho_*}(y_*)}|\Omega|^2dy
\ge
\frac{m_{k_0}(s)}{N_*}.
\]

Therefore

\[
\boxed{
\rho_*
\int_{B_{\rho_*}(y_*)}|\Omega|^2dy
\ge
\frac{\sigma}{N_*}
R_{k_0}m_{k_0}(s)
\ge
\kappa_*,
}
\]

where

\[
\boxed{
\kappa_*:=\frac{\sigma}{N_*}J_*>0.
}
\]

Thus diffuse mass on the entire exterior cannot remain diffuse after fixed-shell recurrent extraction: a positive-density subfamily contains a fixed-scale local L2 packet.

Status: **PROVED.**

---

## 8. Physical critical local-enstrophy concentration

Let the witness time lie in first-hitting stage `j`, with parent radius

\[
r_j=\sqrt{\nu/W_j}.
\]

The physical ball radius is

\[
\boxed{
R_*^{phys}=\rho_*r_j.
}
\]

Since

\[
\Omega=\frac{r_j^2}{\nu}\omega,
\qquad
dx=r_j^3dy,
\]

we have

\[
\int_{B_{R_*^{phys}}}|\omega|^2dx
=
\frac{\nu^2}{r_j}
\int_{B_{\rho_*}}|\Omega|^2dy.
\]

Using the local critical mass inequality,

\[
\boxed{
\int_{B_{R_*^{phys}}}|\omega|^2dx
\ge
\kappa_*\frac{\nu^2}{R_*^{phys}}.
}
\]

This is exactly the critical local-enstrophy scale used by the Galilean moving-window genealogy gate.

Status: **PROVED.**

---

## 9. Fixed shell implies fixed finite generation lag

Because

\[
R_{k_0}=R_0\lambda^{k_0}
\]

and

\[
r_{j-k_0}=\lambda^{k_0}r_j,
\]

we have

\[
\boxed{
R_*^{phys}
=
\sigma R_0\,r_{j-k_0}.
}
\]

Thus the extracted local packet lives at a fixed constant multiple of the natural radius of the fixed-age ancestor `j-k_0`.

The previous arbitrary remote-radius problem has therefore been reduced to a **finite-lag matching-scale problem**.

No statement is made that the packet is already the material descendant of that ancestor.

Status: **PROVED SCALE IDENTITY / MATERIAL IDENTITY NOT DERIVED.**

---

## 10. Compatibility with the terminal analytic-window dissipation gate

`TERMINAL_ANALYTIC_WINDOW_DISSIPATION_GATE_2026-08-25.md` gives a uniform parent-scale analytic window

\[
I_j^{an}
=
[t_j-\alpha_0r_j^2/\nu,t_j]
\]

on the recurrent first-hitting corridor.

For the extracted ball,

\[
\frac{|I_j^{an}|}{(R_*^{phys})^2/\nu}
=
\frac{\alpha_0}{\rho_*^2}.
\]

Since `rho_*` is fixed after the fixed-shell extraction, this is a fixed positive fraction of the ball's parabolic time scale.

Therefore whenever an extracted packet occurs in the terminal analytic portion of a stage, the local persistence-or-crossing machinery applies with constants depending on the fixed data

\[
(\kappa_*,\rho_*,\alpha_0,A_{an}).
\]

It yields a fixed historical local-gradient/dissipation charge unless one of the already explicit transport/derivative alternatives is activated.

This paragraph imports the previous gate; it does not claim that every recurrent witness time is automatically terminal. The clock-location reduction of a positive-density witness set to terminal subwindows remains a separate bookkeeping step if needed.

---

## 11. DSD audit

The argument uses only finite formed channels at each stage:

- fixed exterior mass `m_*`;
- geometric shell masses `m_k`;
- critical shell quantities `(R_k m_k)^(3/2)`;
- one extracted finite index `k_0`;
- one finite covering family;
- one local ball packet.

The infinite shell family enters only through a nonnegative convergent weight `sum R_k^-3` and Tonelli. It is not treated as one indivisible Stage-VII object.

The material ancestor channel is kept separate from the Eulerian shell channel.

---

## 12. What is now pruned

The following escape is removed:

\[
\boxed{
\text{positive-density remote mass}
+\text{ but every fixed normalized shell has zero recurrent charge}.
}
\]

It is incompatible with the critical shell lower bound and Tonelli.

Likewise, once a fixed shell is selected, complete spatial diffuseness inside that shell cannot prevent local L2 concentration because the shell has finite normalized volume and a finite covering.

Thus the recurrent remote witness necessarily has a positive-density subbranch with a fixed finite-generation local packet.

---

## 13. New frontier: Fixed-Lag Packet Identity / Replacement Gate

The remaining question is no longer arbitrary remote localization.

Let

\[
n=j-k_0.
\]

The extracted packet has physical radius

\[
R_*^{phys}\asymp r_n.
\]

The amplitude-location genealogy bridge separately transports the actual ancestor maximum packet from stage `n` to the descendant time.

The next gate is therefore finite and concrete:

\[
\boxed{
\text{fixed-age Eulerian packet at scale }r_n
\stackrel{?}{\Longrightarrow}
\text{material ancestor contact}
\;\lor\;
\text{deformation/diffusion payment}
\;\lor\;
\text{packet replacement / multicore turnover}.
}
\]

Call this the

\[
\boxed{\text{Fixed-Lag Packet Identity / Replacement Gate (FPIRG)}.}
\]

This is strictly narrower than the former Eulerian-to-material genealogy problem because the shell radius, generation lag, and packet scale are all now fixed.

---

## 14. Audit verdict

### PROVED

- positive-density remote enstrophy implies a positive lower bound on the sum of critical shell masses;
- Tonelli extracts one fixed finite shell index with positive recurrent mean;
- a positive-density threshold subset exists on that fixed shell;
- finite covering converts the shell mass into a fixed-scale local L2 packet;
- the physical packet has the critical local-enstrophy size `nu^2/R`;
- the packet radius is a fixed multiple of the natural radius of a fixed finite-age ancestor;
- arbitrary shell-index drift and complete fixed-shell diffuseness are pruned.

### NOT DERIVED

- material identity of the extracted packet with the fixed-age ancestor;
- unconditional conversion of every witness time to a terminal analytic-window charge;
- closure of packet replacement/multicore turnover;
- FPIRG;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
