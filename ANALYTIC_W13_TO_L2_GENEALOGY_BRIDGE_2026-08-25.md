# Analytic W^{1,3}-to-L2 Genealogy Bridge

Date: 2026-08-25

Status: **BOUNDED-Z FIRST-HITTING SNAPSHOT W^{1,3} / CRITICAL-L3 ESCAPE COLLAPSED TO L2 GRADIENT COST / HISTORICAL-TIME PROPAGATION STILL CONDITIONAL / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`GALILEAN_LOCAL_ENSTROPHY_GENEALOGY_GATE_2026-08-25.md` reduced the local genealogy problem to several historical alternatives. All but one already produce a critical L2 gradient cost or a directly critical certificate. The remaining local bottleneck was the stretching alternative

\[
R\|\nabla u\|_{L^3}\ \text{large},
\]

because large L3 gradient does not in general imply a lower bound for

\[
R\|\nabla u\|_2^2.
\]

This note shows that the implication does become valid on bounded-Z first-hitting analytic snapshots, because the same branch supplies a uniform pointwise velocity-gradient ceiling.

The result is deliberately snapshot-level. It does not silently extend first-hitting Cauchy bounds to an arbitrary historical interval.

---

## 2. Normalized first-hitting hypotheses

Work first in the repository's normalized snapshot variables with

\[
\nu=1,
\qquad
r_j=1,
\qquad
\|\Omega_j\|_\infty=1.
\]

On the first-hitting analytic corridor there are uniform Cauchy constants

\[
\|\nabla\Omega_j\|_\infty\le C_1.
\]

Restrict to the bounded-enstrophy recurrent branch

\[
Z_j:=\|\Omega_j\|_2^2\le Z_*<\infty.
\]

The strain-vorticity-gradient interpolation already established in the repository gives

\[
\|\Sigma_j\|_\infty
\le
C_I\|\nabla\Omega_j\|_\infty^{3/5}
\|\Omega_j\|_2^{2/5}.
\]

Hence

\[
\boxed{
\|\Sigma_j\|_\infty
\le
C_I C_1^{3/5} Z_*^{1/5}.
}
\]

The antisymmetric part of \(\nabla U_j\) is algebraically determined by vorticity, so

\[
\|A_j\|_\infty\le C_A\|\Omega_j\|_\infty\le C_A.
\]

Therefore

\[
\boxed{
\|\nabla U_j\|_\infty
\le
A_*:=C_A+C_I C_1^{3/5}Z_*^{1/5}<\infty.
}
\]

This is a branch-restricted pointwise deformation ceiling at the first-hitting snapshot.

Status: **PROVED from existing bounded-Z + analyticity inputs.**

---

## 3. Critical L3 deformation forces L2 gradient cost

For any measurable region \(E\),

\[
\|f\|_{L^3(E)}^3
\le
\|f\|_{L^\infty(E)}\|f\|_{L^2(E)}^2.
\]

Take

\[
f=\nabla U_j
\]

on a ball or shell of normalized radius \(R\). Define

\[
g_R:=R\|\nabla U_j\|_{L^3(E)},
\]

and

\[
G_R:=R\int_E|\nabla U_j|^2dy.
\]

Then

\[
\frac{g_R^3}{R^3}
\le
A_*\frac{G_R}{R},
\]

so

\[
\boxed{
G_R
\ge
\frac{g_R^3}{A_*R^2}.
}
\]

In the genealogy applications the region radius is a fixed multiple of the distinguished normalized scale, hence

\[
0<R_-\le R\le R_+<\infty.
\]

Therefore

\[
\boxed{
g_R\ge\gamma>0
\Longrightarrow
G_R\ge
\frac{\gamma^3}{A_*R_+^2}>0.}
\]

Thus the critical W^{1,3} stretching certificate is not an independent snapshot escape on bounded-Z analytic first-hitting cores.

Status: **PROVED.**

---

## 4. Scale-invariant physical form

Let the physical matching radius be \(R_{phys}\), and suppose the first-hitting/natural-scale pointwise ceiling has the form

\[
\boxed{
\|\nabla u\|_\infty
\le
A_*\frac{\nu}{R_{phys}^2}.
}
\]

Define

\[
g_{phys}:=R_{phys}\|\nabla u\|_3,
\qquad
G_{phys}:=R_{phys}\|\nabla u\|_2^2.
\]

Then

\[
\|\nabla u\|_3^3
\le
\|\nabla u\|_\infty\|\nabla u\|_2^2
\]

gives exactly

\[
\boxed{
g_{phys}^3\le A_*\nu G_{phys}.}
\]

Hence

\[
\boxed{
g_{phys}\ge\gamma\nu
\Longrightarrow
G_{phys}\ge\frac{\gamma^3}{A_*}\nu^2.}
\]

This is the desired critical-to-critical conversion with no residual physical length scale.

---

## 5. Large critical L3 vorticity also collapses

The local-enstrophy gate sometimes leaves the alternative

\[
q_R:=R\|\omega\|_{L^3(E)}\ \text{large}.
\]

Pointwise,

\[
|\omega|\le C_\omega|\nabla u|,
\]

so

\[
q_R\le C_\omega g_R.
\]

Therefore

\[
q_R\ge q_0
\Longrightarrow
g_R\ge q_0/C_\omega.
\]

Combining with Section 3 gives

\[
\boxed{
q_R\ge q_0
\Longrightarrow
G_R
\ge
\frac{q_0^3}
{C_\omega^3A_*R_+^2}.
}
\]

Thus at an analytic bounded-Z first-hitting snapshot, neither

1. large critical L3 vorticity, nor
2. large critical W^{1,3} deformation

is an independent alternative to L2 gradient cost.

Status: **PROVED at the snapshot.**

---

## 6. Updated snapshot genealogy collapse

The local-enstrophy genealogy gate previously produced

\[
\text{gradient concentration}
\Longrightarrow
\begin{cases}
\text{shell L2 cost},\\
\text{persistent L2 cost},\\
\text{cutoff-diffusion L2 cost},\\
\text{relative-transport L2 cost or critical L3 vorticity},\\
\text{W^{1,3} stretching or critical L3 vorticity}.
\end{cases}
\]

At a bounded-Z analytic first-hitting snapshot, Sections 3--5 collapse the last two critical-amplitude alternatives:

\[
\boxed{
\text{critical L3 vorticity}
\lor
\text{critical W^{1,3} stretching}
\Longrightarrow
\text{critical L2 gradient cost}.
}
\]

Hence the instantaneous/local branch map becomes

\[
\boxed{
\text{bounded-Z analytic snapshot genealogy activity}
\Longrightarrow
\text{L2 gradient/shell cost}
\lor
H_{remote}
\lor
T.
}
\]

The \(H_{remote}\) qualification remains because the pointwise ceiling uses bounded-Z plus local derivative amplitude control; remote derivative non-tightness is a different channel and is not removed by this calculation.

---

## 7. Last-crossing temporal reduction

Let a moving local-enstrophy window at terminal time \(t_*\) satisfy

\[
W_R(t_*)\ge2\varepsilon\frac{\nu^2}{R}.
\]

Define the last low-threshold time

\[
t_c:=\sup\left\{t<t_*:
W_R(t)\le\varepsilon\frac{\nu^2}{R}
\right\},
\]

whenever this set is nonempty.

By continuity,

\[
W_R(t)\ge\varepsilon\frac{\nu^2}{R}
\qquad(t_c<t\le t_*).
\]

Fix \(0<\alpha<1\) and compare \(t_*-t_c\) with a parabolic time \(\alpha R^2/\nu\).

### Long post-crossing residence

If

\[
t_*-t_c\ge\alpha\frac{R^2}{\nu},
\]

then on the final interval of that length the persistence argument gives

\[
\boxed{
R\int_{B_{2R}}|\nabla u|^2dx
\ge c\varepsilon\nu^2
}
\]

throughout the interval.

Thus a positive physical residence time is already obtained.

### Short post-crossing residence

If

\[
t_*-t_c<\alpha\frac{R^2}{\nu},
\]

then the entire last threshold increase from \(\varepsilon\nu^2/R\) to the terminal \(2\varepsilon\nu^2/R\) occurs inside the terminal parabolic window

\[
[t_* - \alpha R^2/\nu,t_*].
\]

Therefore the only missing temporal input for complete conversion of the crossing branch is:

\[
\boxed{
\text{a uniform analytic/pointwise-gradient ceiling on a fixed terminal parabolic subwindow.}
}
\]

If such a window estimate is supplied, the positive-growth trichotomy plus Sections 3--5 converts every short-crossing channel into an L2 gradient cost as well.

Status: **LAST-CROSSING REDUCTION PROVED; TERMINAL-WINDOW ANALYTIC PROPAGATION NOT IMPORTED HERE.**

---

## 8. EMGG consequence

The Eulerian-to-Material Genealogy Gate therefore no longer needs a general anti-concentration theorem for W^{1,3} deformation.

On bounded-Z first-hitting analytic snapshots,

\[
\boxed{
W^{1,3}\text{ stretching}
\rightsquigarrow
L^2\text{ gradient cost}.
}
\]

The remaining genealogy obstruction is temporal/material rather than spatial-amplitude based:

\[
\boxed{
\text{Can the required historical activity systematically avoid every fixed terminal analytic window while also avoiding long persistence?}
}
\]

The last-crossing lemma shows that it cannot do both if a fixed terminal analytic window is available.

Thus the next precise target is no longer generic EMGG, but the narrower

\[
\boxed{\text{Terminal Analytic Window Propagation Gate (TAWPG)}.}
\]

TAWPG asks for a fixed \(\alpha_0>0\) such that the first-hitting analyticity/deformation ceiling used at \(t_j\) remains uniformly valid on

\[
[t_j-\alpha_0r_j^2/\nu,t_j]
\]

in the matching moving core, or else pays an already formed \(H_{remote}\) / \(T\) escape.

---

## 9. DSD audit

Keep distinct channels:

- critical L3 vorticity amplitude;
- critical W^{1,3} deformation;
- L2 gradient/shell cost;
- pointwise analytic deformation ceiling;
- remote derivative non-tightness;
- material residence time.

The interpolation in Sections 3--5 is a legitimate channel implication only after the pointwise ceiling is formed. It must not be used on arbitrary historical times without TAWPG.

---

## 10. Audit verdict

### PROVED

- bounded-Z + first-hitting Cauchy derivative control yields a finite normalized velocity-gradient ceiling;
- under that ceiling, critical W^{1,3} deformation forces critical L2 gradient cost;
- large critical L3 vorticity also forces critical L2 gradient cost;
- the previous instantaneous W^{1,3} genealogy bottleneck is removed on analytic bounded-Z snapshots;
- last-crossing timing reduces the temporal problem to long persistence or a short terminal-window crossing.

### NOT DERIVED

- uniform pointwise-gradient/Cauchy control on an entire fixed terminal parabolic window;
- material tracking of every positive-density Eulerian witness;
- closure of H_remote;
- closure of T;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
