# DSD M5-447 — Euler-scale ambient-strain tail tightness or multiscale enstrophy escape

Date: 2026-09-01

Status: **AMBIENT/HARMONIC SOURCE REDUCTION / IN THE CANONICAL REMOTE EULER VARIABLES, THE STRAIN CONTRIBUTION OF A DYADIC VORTICITY SHELL AT RADIUS `2^m` IS BOUNDED BY `C 2^(-3m/2) e_m^(1/2)`, WHERE `e_m` IS ITS NORMALIZED L2 VORTICITY MASS / IF THE SOURCE-SCALE EXTERIOR ENSTROPHY IS UNIFORMLY BOUNDED, CAUCHY GIVES AN EXPONENTIALLY TIGHT STRAIN TAIL, SO ALL ORDER-ONE AMBIENT STRAIN IS GENERATED INSIDE ONE FIXED EULER-SCALE BALL / IF NO SUCH FIXED BALL EXISTS, THE EXTERIOR NORMALIZED ENSTROPHY MUST ESCALATE ON GROWING SHELLS AND THE BRANCH IS ALREADY STRONG MULTISCALE THROUGHPUT / THUS AMBIENT HARMONIC STRAIN IS NOT A THIRD QUIET SOURCE-SCALE TERMINAL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Source Euler variables

Use the canonical normalization of M5-443 around a remote source scale `R_j`:

\[
y=(x-x_j^s)/R_j,
\qquad
\Omega_j=\omega/W_j.
\]

The first-hitting cap gives

\[
\boxed{|\Omega_j|\le q.}
\]

The selected productive source lies in a fixed annulus of radius `O(1)`.

We now examine the vorticity outside that selected band and its contribution to the local harmonic/ambient strain.

---

## 2. Dyadic outer shell decomposition

For `m>=1`, define normalized dyadic shells

\[
A_m
=\{2^m\le|y|<2^{m+1}\}.
\]

Let

\[
\boxed{
e_{j,m}
:=
\int_{A_m}|\Omega_j(y)|^2dy.
}
\]

Let `s_{j,m}` denote the magnitude of the strain tensor contribution at a fixed marked point in the inner source region from vorticity in `A_m`.

The strain kernel has size `~|y|^-3`, so its `L2(A_m)` norm is

\[
\asymp 2^{-3m/2}.
\]

Therefore

\[
\boxed{
s_{j,m}
\le
C2^{-3m/2}e_{j,m}^{1/2}.
}
\]

This estimate is independent of the detailed angular structure and applies componentwise to the full ambient strain.

---

## 3. Uniform exterior enstrophy implies strain-tail tightness

Assume the Euler-scale exterior normalized enstrophy is uniformly bounded:

\[
\boxed{
\sum_{m\ge1}e_{j,m}
\le B
}
\]

with `B` independent of the late stage `j` on the selected corridor.

Then by Cauchy--Schwarz,

\[
\begin{aligned}
\sum_{m>M}s_{j,m}
&\le
C
\left(\sum_{m>M}e_{j,m}\right)^{1/2}
\left(\sum_{m>M}2^{-3m}\right)^{1/2}\\
&\le
C B^{1/2}2^{-3M/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\sup_j
\sum_{m>M}s_{j,m}
\longrightarrow0
\qquad(M\to\infty).
}
\]

The ambient strain is uniformly tight in Euler-scale radius.

For every `epsilon>0`, there is a fixed `M(epsilon,B)` such that all vorticity beyond radius `2^M` contributes less than `epsilon` to the local source-scale strain.

---

## 4. Consequence: bounded-enstrophy ambient field can be absorbed into a finite Euler cluster

On the bounded exterior-enstrophy branch, choose `M` so that the far tail contribution is negligible compared with the order-one source/strain action.

Then all dynamically relevant vorticity producing the source-scale strain lies inside one fixed normalized ball

\[
B_{2^M}.
\]

Inside that ball:

- `|Omega_j|<=q`;
- the selected source rotational component is spatially compact by M5-445;
- the additional finitely many outer shells are also bounded-vorticity regions;
- local Hodge estimates give spatial compactness modulo the remaining pressure/time issue.

Thus a bounded-enstrophy ambient field does not require an infinite source recursion. It enlarges the compact Euler source cluster by only a fixed factor.

---

## 5. Failure of tightness forces multiscale enstrophy escalation

Suppose instead that for some fixed `epsilon_0>0`, ambient strain of size at least `epsilon_0` persists outside every fixed Euler radius along a late subsequence.

Then the previous tail estimate cannot hold with a stage-independent `B`.

Therefore

\[
\boxed{
\sum_{m\ge1}e_{j,m}\to\infty
}
\]

or, more precisely, the exterior normalized enstrophy needed on expanding shells is unbounded along that subsequence.

This is exactly

\[
\boxed{
H_{Euler\text{-}scale\ multiscale\ enstrophy}^{strong}.
}
\]

Thus an ambient strain that continually escapes to larger source-scale radii is already a strong scale-distributed critical-throughput branch.

---

## 6. Quantitative radius from an enstrophy budget

If the exterior enstrophy budget is `B`, choosing

\[
M
\gtrsim
\frac13\log_2\left(\frac{CB}{\epsilon^2}\right)
\]

is sufficient to make the exterior strain tail less than `epsilon`.

Thus the radius needed to contain the active ambient source grows only polynomially in `B`:

\[
2^M
\lesssim
C B^{1/3}\epsilon^{-2/3}
\]

up to fixed constants.

This can be used later when comparing a growing Euler-scale enstrophy budget with the physical first-hitting/fifth-root scale ceiling.

---

## 7. Revised source-scale split

Combining M5-445 and M5-447,

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
H_{multiscale\ enstrophy}^{strong}
\lor
E_{bounded\text{-}cluster}^{Euler\ dynamics}.
}
\]

The second branch contains the selected nonzero rotational source plus every outer vorticity shell needed to generate order-one ambient strain, all inside one fixed Euler-scale ball.

The only remaining compactness issue there is time/pressure dynamics, not spatial source formation or an infinite harmonic tail.

---

## 8. Relation to the old remote recursion

Earlier remote-of-remote audits correctly prevented large harmonic strain from being silently treated as local vorticity derivative blowup.

M5-447 does not retract that warning. It sharpens it:

- if source-scale exterior enstrophy is unbounded, remote recursion is a real multiscale H branch;
- if it is bounded, the recursion terminates inside a fixed Euler-scale cluster because the strain kernel tail is summable in `L2`.

Thus infinite remote recursion is equivalent to an explicit growing enstrophy budget rather than an independent geometric mystery.

---

## 9. Firewall

Bounded source-scale enstrophy is not known globally on a hypothetical singular tower.

The compact Euler cluster is not itself impossible; nontrivial Euler flows with bounded vorticity exist.

Therefore M5-447 reduces the ambient tail but does not prove rigidity of the resulting Euler dynamics.

---

## 10. Audit verdict

### Proved

\[
\boxed{
s_{j,m}\le C2^{-3m/2}e_{j,m}^{1/2}
}
\]

and, under `sum e_{j,m}<=B`,

\[
\boxed{
\sum_{m>M}s_{j,m}
\le CB^{1/2}2^{-3M/2}.
}
\]

### Removed as independent quiet source-scale mechanism

An indefinitely remote ambient harmonic strain tail with bounded Euler-scale enstrophy.

### Current remote strong frontier

\[
\boxed{
H_{multiscale\ enstrophy}^{strong}
\lor
E_{bounded\text{-}cluster}^{Euler\ dynamics}.
}
\]

### Still open

- strong multiscale enstrophy exclusion;
- time/pressure compactness of the bounded Euler cluster;
- Euler rigidity;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
