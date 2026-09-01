# DSD M5-442 — Stage-integrated remote-strain enstrophy tax

Date: 2026-09-01

Status: **GLOBAL NON-DOUBLE-COUNTING DISSIPATION LEDGER / IF A FIXED FRACTION OF ONE FIRST-HITTING STAGE'S REQUIRED LONGITUDINAL STRETCHING ACTION IS SUPPLIED BY VORTICITY AT DISTANCE AT LEAST `K_j r_j`, THE L2 BIOT--SAVART KERNEL BOUND AND CAUCHY IN TIME FORCE PHYSICAL ENERGY DISSIPATION `nu int_I ||omega||_2^2 dt >= c nu^2 K_j^3 r_j` / SUMMING DISJOINT FIRST-HITTING STAGES GIVES `SUM K_j^3 r_j < INFINITY` / THIS QUANTIFIES THE STRONG REMOTE-THROUGHPUT LANE WITHOUT A PERSISTENCE ASSUMPTION, BUT IS STILL SCALE-COMPATIBLE WITH THE FIFTH-ROOT CEILING `K <= C r^-1/5` / GLOBAL REGULARITY UNPROVED.**

---

## 1. First-hitting stretching action

Let stage `j` have parent natural scale

\[
r_j=\sqrt{\frac{\nu}{W_j}}.
\]

The existing first-hitting maximum argument gives

\[
\boxed{
\int_{I_j}\gamma^+(t)dt
\ge
\log q,
}
\]

where `gamma` is the longitudinal strain acting on a vorticity maximum.

Suppose a remote source component supplies a fixed fraction `theta>0` of this required action:

\[
\boxed{
\int_{I_j}\gamma_{rem}^+(t)dt
\ge
\theta\log q.
}
\]

Assume that the vorticity producing this component lies at physical distance at least

\[
\boxed{
R_j=K_jr_j,
\qquad K_j\ge K_0>1,
}
\]

from the target throughout the selected remote source action.

This formulation is integrated in time and does not require the source to persist at one fixed point or to remain coherent for the full stage.

---

## 2. L2 far-kernel bound for vorticity

The strain kernel has magnitude `~|y|^-3`. Its `L2` norm on the exterior of radius `R` satisfies

\[
\left(
\int_{|y|>R}|y|^{-6}dy
\right)^{1/2}
\asymp
R^{-3/2}.
\]

Therefore

\[
\boxed{
|\gamma_{rem}(t)|
\le
C R_j^{-3/2}
\|\omega(t)\|_{L^2(\text{remote region})}
\le
C R_j^{-3/2}\|\omega(t)\|_2.
}
\]

Hence

\[
\boxed{
\|\omega(t)\|_2^2
\ge
c R_j^3|\gamma_{rem}(t)|^2.
}
\]

---

## 3. Time Cauchy converts fixed stretching action into enstrophy action

Integrate over the stage:

\[
\int_{I_j}\|\omega(t)\|_2^2dt
\ge
cR_j^3
\int_{I_j}|\gamma_{rem}(t)|^2dt.
\]

By Cauchy--Schwarz in time,

\[
\int_{I_j}|\gamma_{rem}|^2dt
\ge
\frac{\left(\int_{I_j}\gamma_{rem}^+dt\right)^2}{|I_j|}.
\]

The fixed remote action fraction gives

\[
\int_{I_j}|\gamma_{rem}|^2dt
\ge
\frac{\theta^2(\log q)^2}{|I_j|}.
\]

The first-hitting stage ceiling gives

\[
\boxed{
|I_j|
\le
L_*\frac{r_j^2}{\nu}.
}
\]

Therefore

\[
\begin{aligned}
\int_{I_j}\|\omega\|_2^2dt
&\ge
cR_j^3\frac{\nu}{L_*r_j^2}\\
&=
c\nu K_j^3r_j.
\end{aligned}
\]

Multiplying by viscosity,

\[
\boxed{
\nu\int_{I_j}\|\omega(t)\|_2^2dt
\ge
c_*\nu^2K_j^3r_j.
}
\]

This is an actual physical energy-dissipation charge.

---

## 4. Global stage packing

For a finite-energy Leray/smooth pre-singular solution,

\[
\nu\int_0^{T_*}\|\omega(t)\|_2^2dt
\le
C E_0.
\]

The first-hitting stages are disjoint in time. Therefore every collection of remote-dominated stages satisfies

\[
\boxed{
\sum_jK_j^3r_j
\le
C\frac{E_0}{\nu^2}.
}
\]

This is a genuine global non-double-counting ledger.

It requires neither shell persistence nor common-time spatial packing.

---

## 5. Consequences for separation growth

If on an infinite subsequence

\[
K_j\gtrsim r_j^{-\beta},
\]

then the stage charge is

\[
K_j^3r_j
\gtrsim
r_j^{1-3\beta}.
\]

Thus the dissipation ledger immediately excludes sustained remote corridors with

\[
\beta\ge\frac13
\]

at positive stage density, modulo the exact sparse-subsequence summability interpretation at the endpoint.

However the finite-energy fifth-root visibility ceiling gives only

\[
K_j\lesssim Cr_j^{-1/5}.
\]

At this maximal allowed remote scale,

\[
K_j^3r_j
\lesssim
r_j^{2/5},
\]

which is geometrically summable over first-hitting stages.

Therefore M5-442 is a real global tax but does not close the fifth-root-compatible remote escalation.

---

## 6. Relation to M5-440 and M5-441

M5-440 gives the snapshot costs

\[
A_{rel}(R_j),
\quad
R_j^{1/2}\|\nabla u\|_2,
\quad
X^{1/2}/\nu
\gtrsim
K_j^2.
\]

M5-441 gives the compressed nonlinear time

\[
\tau_{nl}(R_j)\lesssim r_j^2/\nu.
\]

M5-442 adds a stage-integrated physical dissipation price:

\[
\boxed{
D_j^{remote}
\gtrsim
\nu^2K_j^3r_j.
}
\]

These are three complementary manifestations of the same strong remote throughput.

---

## 7. Distributed and time-dependent remote sources

The proof only uses a lower bound on the distance of the source portion assigned to `gamma_rem` and the integrated action fraction.

Therefore it remains valid when:

- the source moves within the remote exterior;
- different remote subregions pay at different times;
- the source is diffuse rather than a formed carrier;
- no single shell persists for a full stage.

If the angular source is spread across radii, one may apply the estimate to an action-selected radial band or define an action-weighted effective radius. The statement should not be read as requiring one rigid annulus.

---

## 8. Firewall

The global sum

\[
\sum K_j^3r_j<\infty
\]

is compatible with a geometric first-hitting tower when `K_j` grows no faster than the fifth-root ceiling.

It is therefore not a regularity proof.

Do not replace the time-integrated remote action assumption by a one-time source event without an additional persistence argument.

---

## 9. Audit verdict

### Proved

\[
\boxed{
\text{fixed-fraction remote stretching action at }R_j=K_jr_j
\Longrightarrow
\nu\int_{I_j}\|\omega\|_2^2dt
\gtrsim
\nu^2K_j^3r_j.
}
\]

and globally

\[
\boxed{
\sum_jK_j^3r_j<\infty.
}
\]

### Still open

- exclusion of the fifth-root-compatible range `1 << K_j <= C r_j^-1/5`;
- rigidity of strong critical/delocalized throughput;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
