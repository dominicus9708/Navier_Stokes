# Galilean Local-Enstrophy Genealogy Gate — 2026-08-25

## Status

**NEW CALCULATION — RIGOROUS PRE-SINGULAR LOCAL GATE; GLOBAL REGULARITY NOT PROVED.**

This note replaces one overly ambitious arrow in the previous local-energy genealogy route.

The earlier target was

\[
\text{current gradient concentration}
\stackrel{?}{\Longrightarrow}
\text{nontrivial local kinetic-energy crossing}.
\]

That implication is not available in general: Poincare controls velocity fluctuation from above by the gradient,

\[
\|u-u_B\|_2^2\le C R^2\|\nabla u\|_2^2,
\]

but does not reverse large gradient concentration into a kinetic-energy lower bound.

The natural replacement is a moving-window **local enstrophy** ledger.

---

## 1. Moving vorticity window

Let

\[
\omega=\nabla\times u,
\qquad
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

For a smooth cutoff `phi`, with

\[
0\le\phi\le1,
\qquad
\phi=1\text{ on }B_1,
\qquad
\operatorname{supp}\phi\subset B_2,
\]

set

\[
\psi_R(x,t)
=
\phi\!\left(\frac{x-X_R(t)}{R}\right).
\]

Then

\[
\partial_t\psi_R
=-\dot X_R\cdot\nabla\psi_R,
\]

and

\[
|\nabla\psi_R|\le C R^{-1},
\qquad
|\Delta\psi_R|\le C R^{-2}.
\]

Define

\[
W_R(t)=\int |\omega(x,t)|^2\psi_R(x,t)\,dx.
\]

---

## 2. Exact moving local-enstrophy identity

Multiplying the vorticity equation by `omega psi_R` and integrating gives

\[
\boxed{
\begin{aligned}
\frac12\frac d{dt}W_R(t)
+\nu\int |\nabla\omega|^2\psi_R\,dx
&=
\frac\nu2\int |\omega|^2\Delta\psi_R\,dx\\
&\quad+
\frac12\int |\omega|^2
(u-\dot X_R)\cdot\nabla\psi_R\,dx\\
&\quad+
\int (\omega\cdot\nabla u)\cdot\omega\,\psi_R\,dx.
\end{aligned}
}
\]

There is no pressure term.

Status: **PROVED for smooth pre-singular solutions.**

---

## 3. Galilean-covariant center choice

Choose the center by

\[
\boxed{
\dot X_R(t)
=
\fint_{B_{4R}(X_R(t))}u(y,t)\,dy.
}
\]

For a smooth pre-singular solution this defines the moving center locally in time.

Under a constant Galilean transformation

\[
u'=u-c,
\qquad
X_R'=X_R-ct,
\]

one has

\[
u'-\dot X_R'=u-\dot X_R.
\]

Therefore the boundary transport is genuinely relative.

Moreover, Poincare-Sobolev on `B_{4R}(X_R)` gives

\[
\boxed{
\|u-\dot X_R\|_{L^3(B_{4R})}
\le
C R^{1/2}
\|\nabla u\|_{L^2(B_{4R})}.
}
\]

Define the critical physical-scale gradient cost

\[
G_R(t)
:=
R\int_{B_{4R}(X_R(t))}|\nabla u|^2dx.
\]

Then

\[
\boxed{
\|u-\dot X_R\|_{L^3(B_{4R})}
\le C G_R(t)^{1/2}.
}
\]

Status: **PROVED.**

---

## 4. Positive local-enstrophy growth trichotomy

Write

\[
B_R(t)
=
\frac12\int |\omega|^2
(u-\dot X_R)\cdot\nabla\psi_R\,dx,
\]

\[
S_R(t)
=
\int(\omega\cdot\nabla u)\cdot\omega\,\psi_R\,dx.
\]

For `I=[t_1,t_2]`, suppose

\[
\boxed{
W_R(t_2)-W_R(t_1)
\ge
2\varepsilon\frac{\nu^2}{R}.
}
\]

Since palinstrophy dissipation is nonnegative, the integrated identity implies

\[
\boxed{
\frac\nu2
\int_I\int |\omega|^2|\Delta\psi_R|\,dxdt
+
\int_I\big(|B_R(t)|+|S_R(t)|\big)dt
\ge
\varepsilon\frac{\nu^2}{R}.
}
\]

Hence at least one of the following three mechanisms carries a fixed fraction of the critical amount:

1. cutoff-diffusion boundary enstrophy;
2. relative boundary transport;
3. vortex stretching.

Status: **PROVED.**

---

## 5. Cutoff-diffusion channel directly forces historical gradient cost

Let

\[
A_R^\partial(t)
=
\operatorname{supp}\nabla\psi_R(\cdot,t)
\subset
B_{2R}(X_R(t))\setminus B_R(X_R(t)),
\]

and

\[
e_R^\partial(t)
=
R\int_{A_R^\partial(t)}|\omega|^2dx.
\]

If

\[
|I|\le\theta\frac{R^2}{\nu},
\]

then

\[
\frac\nu2
\int_I\int |\omega|^2|\Delta\psi_R|
\le
C\frac{\theta}{R}
\sup_{t\in I}e_R^\partial(t).
\]

Therefore, if this channel contributes at least

\[
\delta\frac{\nu^2}{R},
\]

then

\[
\boxed{
\sup_{t\in I}
\frac{e_R^\partial(t)}{\nu^2}
\ge
c\frac{\delta}{\theta}.
}
\]

Since pointwise

\[
|\omega|^2\le2|\nabla u|^2,
\]

it follows that

\[
\boxed{
\sup_{t\in I}
\frac{R\int_{A_R^\partial(t)}|\nabla u|^2dx}{\nu^2}
\ge
c\frac{\delta}{\theta}.
}
\]

This branch already produces the desired historical physical-shell deformation cost.

Status: **PROVED CONDITIONAL ON CHANNEL OCCUPANCY.**

---

## 6. Relative boundary-transport channel

Define the critical boundary-vorticity amplitude

\[
q_R^\partial(t)
:=
R\|\omega(t)\|_{L^3(A_R^\partial(t))}.
\]

By Holder and the moving-frame Poincare estimate,

\[
\begin{aligned}
|B_R(t)|
&\le
C R^{-1}
\|u-\dot X_R\|_{L^3}
\|\omega\|_{L^3(A_R^\partial)}^2\\
&\le
C R^{-3}
G_R(t)^{1/2}
\big(q_R^\partial(t)\big)^2.
\end{aligned}
\]

Thus

\[
\boxed{
|B_R|
\le
C R^{-3}G_R^{1/2}(q_R^\partial)^2.
}
\]

Assume on `I`

\[
q_R^\partial(t)\le Q\nu,
\qquad
|I|\le\theta R^2/\nu.
\]

If

\[
\int_I|B_R(t)|dt
\ge
\delta\frac{\nu^2}{R},
\]

then

\[
\boxed{
\sup_{t\in I}\frac{G_R(t)^{1/2}}{\nu}
\ge
c\frac{\delta}{\theta Q^2},
}
\]

and therefore

\[
\boxed{
\sup_{t\in I}\frac{G_R(t)}{\nu^2}
\ge
c\frac{\delta^2}{\theta^2Q^4}.
}
\]

If the assumed bound on `q_R^partial` fails, that failure is itself a scale-critical historical `L^3` vorticity certificate rather than a loss of information.

Status: **PROVED CONDITIONAL DICHOTOMY.**

---

## 7. Stretching channel

Define

\[
g_R(t)
:=
R\|\nabla u(t)\|_{L^3(B_{2R}(X_R(t)))},
\]

\[
q_R^c(t)
:=
R\|\omega(t)\|_{L^3(B_{2R}(X_R(t)))}.
\]

Holder gives

\[
\boxed{
|S_R(t)|
\le
R^{-3}g_R(t)(q_R^c(t))^2.
}
\]

If

\[
q_R^c(t)\le Q\nu,
\qquad
|I|\le\theta R^2/\nu,
\]

and

\[
\int_I|S_R(t)|dt
\ge
\delta\frac{\nu^2}{R},
\]

then

\[
\boxed{
\sup_{t\in I}\frac{g_R(t)}{\nu}
\ge
c\frac{\delta}{\theta Q^2}.
}
\]

If `q_R^c` is not bounded, one instead obtains a large critical vorticity-amplitude certificate.

Important audit: large `L^3` gradient amplitude does **not** by itself force a lower bound on

\[
G_R=R\|\nabla u\|_2^2,
\]

because on a bounded ball Holder gives the opposite-direction estimate

\[
\|\nabla u\|_2
\le C R^{1/2}\|\nabla u\|_3.
\]

Therefore the stretching branch remains a distinct critical `W^{1,3}`-type certificate unless an additional occupancy or anti-concentration estimate is proved.

Status: **PROVED DICHOTOMY; CONVERSION TO `G_R` NOT DERIVED.**

---

## 8. Local curl-versus-gradient defect

The global identity

\[
\int|\nabla u|^2dx
=
\int|\omega|^2dx
\]

does not localize without a boundary defect.

For a smooth cutoff `chi`, divergence-free `u` gives

\[
|\nabla u|^2-|\omega|^2
=\partial_i u_j\,\partial_j u_i,
\]

and hence, for any constant vector `c`,

\[
\boxed{
\int\chi\big(|\nabla u|^2-|\omega|^2\big)dx
=
-\int
(u_i-c_i)(\partial_j\chi)(\partial_i u_j)dx.
}
\]

Choose `chi=1` on `B_R(X)`, supported in `B_{2R}(X)`, with `|grad chi|<=C/R`, and choose

\[
c=(u)_{B_{4R}(X)}.
\]

Poincare then yields

\[
\boxed{
\left|
\int\chi(|\nabla u|^2-|\omega|^2)dx
\right|
\le
C
D_4^{1/2}D_\chi^{1/2},
}
\]

where

\[
D_4=\int_{B_{4R}(X)}|\nabla u|^2dx,
\qquad
D_\chi=\int_{\operatorname{supp}\nabla\chi}|\nabla u|^2dx.
\]

Let

\[
D_{\rm core}=\int_{B_R(X)}|\nabla u|^2dx.
\]

Then

\[
\boxed{
\int\chi|\omega|^2dx
\ge
D_{\rm core}-C(D_4D_\chi)^{1/2}.
}
\]

Status: **PROVED.**

---

## 9. Quiet-annulus / active-annulus gate

Fix `0<eta<1`.

If

\[
D_{\rm core}<\eta D_4,
\]

then the broad shell already contains

\[
\boxed{
\int_{B_{4R}\setminus B_R}|\nabla u|^2dx
>(1-\eta)D_4.
}
\]

If instead

\[
D_{\rm core}\ge\eta D_4,
\]

there are two subcases.

If

\[
D_\chi
\ge
\frac{\eta^2}{4C^2}D_4,
\]

then the cutoff annulus itself already carries a fixed fraction of the gradient cost.

If

\[
D_\chi
<
\frac{\eta^2}{4C^2}D_4,
\]

then the defect estimate gives

\[
\boxed{
\int\chi|\omega|^2dx
\ge
\frac\eta2 D_4.
}
\]

Thus a distinguished-scale gradient concentration must satisfy one of

\[
\boxed{
\text{broad-shell gradient cost}
\;\lor\;
\text{cutoff-annulus gradient cost}
\;\lor\;
\text{localized vorticity concentration}.
}
\]

This is the missing rigorous bridge from gradient concentration to a quantity governed by the local-enstrophy equation.

Status: **PROVED.**

---

## 10. Persistence-or-crossing genealogy lemma

Suppose at a terminal pre-singular time `t_*` the moving local vorticity window satisfies

\[
W_R(t_*)
\ge
2\varepsilon\frac{\nu^2}{R}.
\]

Look backward over

\[
I_*
=
\left[t_*-\theta\frac{R^2}{\nu},\,t_*\right].
\]

There are two mutually exhaustive cases.

### A. Persistence

If

\[
W_R(t)
\ge
\varepsilon\frac{\nu^2}{R}
\quad
\text{for every }t\in I_*,
\]

then

\[
W_R(t)
\le
\int_{B_{2R}(X_R(t))}|\omega|^2dx
\le
2\int_{B_{2R}(X_R(t))}|\nabla u|^2dx,
\]

so throughout the interval

\[
\boxed{
R\int_{B_{2R}(X_R(t))}|\nabla u|^2dx
\ge
\frac\varepsilon2\nu^2.
}
\]

Thus the desired historical gradient-cost certificate already persists.

### B. Crossing

Otherwise there exists `t_1 in I_*` with

\[
W_R(t_1)<\varepsilon\frac{\nu^2}{R}.
\]

Since

\[
W_R(t_*)\ge2\varepsilon\frac{\nu^2}{R},
\]

continuity gives an interval on which local enstrophy grows by at least

\[
\varepsilon\frac{\nu^2}{R}.
\]

Applying the positive-growth identity with adjusted constants forces at least one of:

1. historical cutoff-annulus gradient cost;
2. historical relative-transport gradient cost, unless critical `L^3` vorticity is already large;
3. historical critical stretching / `W^{1,3}` deformation, unless critical `L^3` vorticity is already large.

Therefore terminal local vorticity concentration cannot appear without a parabolic-time historical certificate.

Status: **PROVED AS A CONDITIONAL ALTERNATIVE.**

---

## 11. Combined gradient-to-history statement

Assume at `t_*` a distinguished-scale gradient concentration

\[
R D_4(t_*)
\ge
K\nu^2.
\]

The quiet/active-annulus gate gives either an immediate terminal shell-gradient certificate or a local-vorticity lower bound of order

\[
W_R(t_*)
\gtrsim_{\eta}
K\frac{\nu^2}{R}.
\]

In the vorticity-concentration subcase, the persistence-or-crossing lemma produces a historical parabolic-scale certificate.

Thus the previous unsupported arrow

\[
\text{gradient concentration}
\stackrel{?}{\Longrightarrow}
\text{kinetic-energy crossing}
\]

is replaced by the rigorous proof tree

\[
\boxed{
\text{current gradient concentration}
\Longrightarrow
\begin{cases}
\text{terminal shell gradient cost},\\
\text{persistent historical gradient cost},\\
\text{cutoff-diffusion historical gradient cost},\\
\text{relative-transport historical gradient cost or large critical }L^3\text{ vorticity},\\
\text{stretching }W^{1,3}\text{ certificate or large critical }L^3\text{ vorticity}.
\end{cases}
}
\]

This derivation itself does **not** assume bounded `Z`; however, combining it with the earlier cubic nonsummability ledger must still respect the corrected bounded-`Z`, recurrent, non-`L^3` scope recorded in `AMPLITUDE_GENEALOGY_SCOPE_CORRECTION_2026-08-24.md`.

---

## 12. Audit table

| Claim | Status |
|---|---|
| Large gradient concentration generally forces a local kinetic-energy lower bound | **NOT VALID IN GENERAL** |
| Exact moving local-enstrophy identity | **PROVED** |
| Moving-center formulation is Galilean covariant | **PROVED** |
| Positive local-enstrophy growth forces cutoff/transport/stretching activity | **PROVED** |
| Cutoff-diffusion activity forces historical shell gradient cost | **PROVED CONDITIONAL** |
| Relative transport forces gradient cost unless critical `L^3` vorticity is large | **PROVED CONDITIONAL DICHOTOMY** |
| Stretching forces critical `W^{1,3}` deformation unless critical `L^3` vorticity is large | **PROVED CONDITIONAL DICHOTOMY** |
| Critical `W^{1,3}` deformation alone forces `G_R` lower bound | **NOT DERIVED** |
| Local gradient concentration converts either to shell cost or localized vorticity concentration | **PROVED** |
| Terminal vorticity concentration yields persistence-or-crossing historical alternatives | **PROVED** |
| These alternatives alone exclude every hypothetical singularity | **NOT DERIVED** |
| Global regularity | **UNPROVED** |

---

## 13. New active bottleneck

The genealogy front is now narrower.

The next genuinely unresolved branch is the stretching certificate

\[
\boxed{
R\|\nabla u\|_{L^3}
\text{ large}
}
\]

without already-large shell `L^2` gradient cost.

To close that branch one needs either

1. a quantitative occupancy/anti-concentration lemma converting critical `L^3` deformation into repeated `L^2` shell cost; or
2. an independent regularity/Liouville obstruction for a recurrent critical `W^{1,3}` stretching branch.

This is now the most precise local genealogy bottleneck produced by the current calculation.