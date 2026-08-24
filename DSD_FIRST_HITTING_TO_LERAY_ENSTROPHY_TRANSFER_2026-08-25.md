# DSD First-Hitting -> Leray Enstrophy Transfer

Date: 2026-08-25

Status: **EXACT NORMALIZATION TRANSFER DERIVED / UNIFORM IN-STAGE LERAY ENSTROPHY CEILING DERIVED / DIRECT BETCHOV BARRIER CONVERTED TO FIRST-HITTING VARIABLES / GLOBAL REGULARITY NOT PROVED.**

## 1. Purpose and scope

The direct recurrent Betchov frequency barrier was derived in standard backward-Leray variables. It states that a nonzero recurrent bounded-enstrophy Leray survivor must satisfy

\[
Z_{L,+}\ge 54\pi^2\nu^{3/2},
\]

where

\[
Z_L(s)=\|W_L(s)\|_{L_Y^2}^2,
\qquad
W_L(Y,s)=(T^*-t)\omega(x,t).
\]

The first-hitting branch, however, uses

\[
Z_j
:=
\frac{r_j}{\nu^2}\|\omega(t_j)\|_2^2,
\qquad
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
\]

These are not the same normalized enstrophy. This note derives the exact conversion and controls the whole stage, not only the endpoints.

The argument is restricted to the existing non-H/T recurrent stage corridor with

\[
0<L_-\le L_j\le L_+<\infty.
\]

---

## 2. Parent first-hitting normalization

Fix stage `j`. Use the parent scale

\[
r_j=\left(\frac\nu{W_j}\right)^{1/2}
\]

and coordinates

\[
y=\frac{x-X_j}{r_j}.
\]

Define the parent-normalized vorticity at an arbitrary time in the stage by

\[
\Omega_j(y,t)
:=
\frac{r_j^2}{\nu}\omega(x,t)
=
\frac{\omega(x,t)}{W_j}.
\]

Define its parent-normalized enstrophy

\[
\boxed{
\widetilde Z_j(t)
:=
\int|\Omega_j(y,t)|^2dy
=
\frac{r_j}{\nu^2}\|\omega(t)\|_2^2.
}
\]

At the endpoint,

\[
\widetilde Z_j(t_j)=Z_j.
\]

Assume the bounded endpoint branch

\[
\boxed{Z_j\le Z_*}
\]

for all sufficiently late retained stages.

---

## 3. Exact conversion to standard backward-Leray variables

Let

\[
\delta(t):=T^*-t
\]

and define the parent remaining-time amplitude

\[
\boxed{
\Theta_j(t)
:=W_j\delta(t)
=\frac{\nu(T^*-t)}{r_j^2}.
}
\]

Standard backward-Leray coordinates are

\[
Y=\frac{x-X^*}{\sqrt{T^*-t}},
\qquad
s=-\log(T^*-t),
\]

and standard Leray vorticity is

\[
W_L(Y,s)
=(T^*-t)\omega(x,t).
\]

A translation between `X_j` and `X^*` does not affect the `L2` norm, so only the scale ratio matters.

Since

\[
T^*-t
=
\frac{\Theta_j(t)r_j^2}{\nu},
\]

we have

\[
dY
=
\left(\frac{\nu}{\Theta_j(t)}\right)^{3/2}dy
\]

up to translation, and pointwise

\[
W_L
=
\Theta_j(t)\Omega_j.
\]

Therefore

\[
\begin{aligned}
Z_L(s)
&=\int|W_L|^2dY\\
&=\Theta_j(t)^2
\left(\frac\nu{\Theta_j(t)}\right)^{3/2}
\int|\Omega_j|^2dy.
\end{aligned}
\]

Hence the exact normalization identity is

\[
\boxed{
Z_L(s)
=
\nu^{3/2}\Theta_j(t)^{1/2}\widetilde Z_j(t).
}
\]

At the checkpoint `t=t_j`,

\[
\boxed{
Z_L(s_j)
=
\nu^{3/2}\Theta_j^{1/2}Z_j.
}
\]

This is the correct bridge between the two enstrophy conventions.

---

## 4. Uniform remaining-time amplitude bound

From the first-hitting/Leray clock coboundary note,

\[
\Theta_j
=
\sum_{n=0}^{\infty}q^{-n}\tau_{j+n},
\]

where

\[
\tau_j=W_j(t_{j+1}-t_j).
\]

On the recurrent stage corridor,

\[
\tau_j\le L_j\le L_+.
\]

Thus

\[
\boxed{
\Theta_j
\le
\Theta_+
:=
\frac{L_+}{1-q^{-1}}
=
\frac{q}{q-1}L_+.
}
\]

Within the stage, `Theta_j(t)` decreases monotonically from `Theta_j`, so

\[
\boxed{
0<\Theta_j(t)\le\Theta_+.
}
\]

---

## 5. Uniform in-stage enstrophy amplification

Let

\[
E_\omega(t)=\|\omega(t)\|_2^2,
\qquad
M(t)=\|\omega(t)\|_\infty.
\]

The sharp trace-free enstrophy inequality gives

\[
\frac12E_\omega'
+\nu Q_\omega
\le
\frac1{\sqrt3}M(t)E_\omega.
\]

Discarding the nonnegative viscous term,

\[
\frac d{dt}\log E_\omega
\le
\frac2{\sqrt3}M(t).
\]

The stage length is defined using the record/running vorticity maximum, and the actual `M(t)` is no larger than that record maximum. Therefore for every

\[
t\in[t_j,t_{j+1}],
\]

\[
\int_{t_j}^{t}M(\tau)d\tau
\le L_j\le L_+.
\]

Consequently

\[
E_\omega(t)
\le
E_\omega(t_j)
\exp\left(\frac{2L_+}{\sqrt3}\right).
\]

Since the parent normalization uses fixed `r_j`,

\[
\boxed{
\widetilde Z_j(t)
\le
Z_j
\exp\left(\frac{2L_+}{\sqrt3}\right)
\le
Z_*
\exp\left(\frac{2L_+}{\sqrt3}\right).
}
\]

This controls the whole first-hitting stage from the endpoint ceiling alone.

---

## 6. Uniform standard-Leray enstrophy ceiling

Combine the exact normalization identity with the two uniform bounds:

\[
Z_L(s)
=
\nu^{3/2}\Theta_j(t)^{1/2}\widetilde Z_j(t).
\]

Hence throughout every sufficiently late retained stage,

\[
\boxed{
Z_L(s)
\le
\nu^{3/2}
Z_*
\left(\frac{q}{q-1}L_+\right)^{1/2}
\exp\left(\frac{2L_+}{\sqrt3}\right).
}
\]

Thus the recurrent Leray trajectory has the uniform ceiling

\[
\boxed{
Z_{L,+}
\le
\nu^{3/2}
Z_*
\sqrt{\frac{qL_+}{q-1}}
\exp\left(\frac{2L_+}{\sqrt3}\right).
}
\]

No center-coherence assumption is needed for this `L2` estimate because translations preserve the norm.

---

## 7. Insert the direct Betchov recurrent barrier

The direct Betchov recurrent barrier requires every nonzero recurrent bounded-enstrophy survivor to satisfy

\[
Z_{L,+}
\ge
54\pi^2\nu^{3/2}.
\]

Using the first-hitting upper ceiling, a necessary condition is therefore

\[
\boxed{
Z_*
\sqrt{\frac{qL_+}{q-1}}
\exp\left(\frac{2L_+}{\sqrt3}\right)
\ge
54\pi^2.
}
\]

The factor `nu^(3/2)` cancels **exactly**.

Thus the recurrent bounded-`Z` obstruction has become a fully dimensionless first-hitting inequality.

Equivalently, the branch is S-closed whenever

\[
\boxed{
Z_*
\sqrt{\frac{qL_+}{q-1}}
\exp\left(\frac{2L_+}{\sqrt3}\right)
<
54\pi^2.
}
\]

---

## 8. Tightness-radius form

The stage-wide vorticity-tight corridor gives the endpoint ceiling

\[
\boxed{
Z_*
\le
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Therefore a nonzero recurrent survivor on that tight corridor must satisfy

\[
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
\sqrt{\frac{qL_+}{q-1}}
\exp\left(\frac{2L_+}{\sqrt3}\right)
\ge
54\pi^2.
\]

Solving for the tightness radius gives

\[
\boxed{
R_Z^3
\ge
\frac{81\pi}{2}
(1-\varepsilon_Z)
\sqrt{\frac{q-1}{qL_+}}
\exp\left(-\frac{2L_+}{\sqrt3}\right).
}
\]

This is the **Betchov recurrent enstrophy-radius/time tradeoff**.

At `q=2`,

\[
\boxed{
R_Z^3
\ge
\frac{81\pi}{2}
(1-\varepsilon_Z)
(2L_+)^{-1/2}
\exp\left(-\frac{2L_+}{\sqrt3}\right).
}
\]

Equivalently,

\[
\boxed{
R_Z
\ge
\left[
\frac{81\pi}{2}
(1-\varepsilon_Z)
(2L_+)^{-1/2}
 e^{-2L_+/\sqrt3}
\right]^{1/3}.
}
\]

---

## 9. Representative scale audit for q=2

For illustration only, not as inserted proof constants, take

\[
\varepsilon_Z=\frac14.
\]

Then the necessary radius floors are approximately

\[
\begin{array}{c|c}
L_+ & R_Z\text{ floor}\\
\hline
0.10 & 5.7500\\
0.20 & 4.9292\\
0.30 & 4.4332\\
0.50 & 3.7697\\
0.75 & 3.2001\\
1.00 & 2.7705\\
1.50 & 2.1361\\
2.00 & 1.6797
\end{array}
\]

Thus short recurrent stages require a very broad normalized enstrophy reservoir. Small tight recurrent cores cannot pay the direct Betchov similarity tax.

These numbers do **not** identify `R_Z` with any previously defined moving-variance radius `R_V`; that comparison requires a separate geometric bridge.

---

## 10. Interpretation

The direct Betchov barrier and first-hitting clock together force a clean tradeoff:

\[
\boxed{
\text{short first-hitting stage}
\Longrightarrow
\text{large normalized enstrophy radius},
}
\]

while

\[
\boxed{
\text{small tight enstrophy radius}
\Longrightarrow
\text{long normalized stage}.
}
\]

A survivor can avoid the contradiction only by paying one of two macroscopic costs:

1. a sufficiently large `R_Z` spatial/tail spread;
2. a sufficiently large `L_+` temporal persistence cost.

Both are already typed elsewhere in the proof tree as candidates for `T`/remote-tail activity.

---

## 11. DSD audit

The transfer uses only finite formed channels:

- endpoint first-hitting enstrophy `Z_j`;
- parent-stage enstrophy `Ztilde_j(t)`;
- remaining-time amplitude `Theta_j(t)`;
- standard Leray enstrophy `Z_L(s)`;
- finite stage ceiling `L_+`;
- tightness radius `R_Z` and leakage fraction `epsilon_Z`.

The different normalization systems are explicitly separated and then related by an exact formula. No variable is silently identified across gauges.

---

## 12. Updated frontier

The bounded-`Z` recurrent/tight corridor now obeys the necessary condition

\[
\boxed{
Z_*
\sqrt{\frac{qL_+}{q-1}}
 e^{2L_+/\sqrt3}
\ge54\pi^2,
}
\]

or, under stage-wide vorticity tightness,

\[
\boxed{
R_Z^3
\ge
\frac{81\pi}{2}
(1-\varepsilon_Z)
\sqrt{\frac{q-1}{qL_+}}
 e^{-2L_+/\sqrt3}.
}
\]

The next high-leverage gate is to compare this **lower** bound on `R_Z` with the existing no-turnover / moving-core / analyticity **upper** radii, without identifying unlike radii by fiat.

If a rigorous bridge gives an upper radius smaller than this Betchov floor, the recurrent bounded-`Z` tight corridor closes.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
