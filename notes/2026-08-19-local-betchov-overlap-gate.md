# Local Betchov overlap gate: fresh production -> M / H / T

Date: 2026-08-19

Status: **DERIVED LOCAL KINEMATIC IDENTITY + CONDITIONAL OVERLAP GATE / GLOBAL REGULARITY NOT PROVED**.

This note addresses the mass/production segregation loophole left by the middle-strain saturation analysis.

---

## 1. Velocity-gradient notation

Let

\[
A=\nabla u,
\qquad
A_{ij}=\partial_j u_i,
\qquad
\operatorname{tr}A=0.
\]

Split

\[
A=S+W,
\qquad
S=\frac12(A+A^T),
\qquad
W=\frac12(A-A^T).
\]

The vorticity is

\[
\omega=\nabla\times u.
\]

For a trace-free `3 x 3` matrix,

\[
\operatorname{tr}(A^3)=3\det A.
\]

Algebraically,

\[
\boxed{
\operatorname{tr}(A^3)
=
\operatorname{tr}(S^3)
+\frac34\omega\cdot S\omega.
}
\]

Since `tr S=0`,

\[
\operatorname{tr}(S^3)=3\det S.
\]

---

## 2. Exact local divergence form

For an incompressible velocity gradient, the third Betchov invariant is an exact divergence:

\[
\boxed{
\operatorname{tr}(A^3)
=
\nabla\cdot F_B,
}
\]

with

\[
\boxed{
F_B
=
\left(A^2-\frac12\operatorname{tr}(A^2)I\right)u.
}
\]

Equivalently, in indices,

\[
(F_B)_i
=
u_j\partial_k u_i\partial_j u_k
-
\frac12u_i\partial_k u_j\partial_j u_k.
\]

Combining with the strain/vorticity decomposition gives the pointwise local Betchov identity

\[
\boxed{
\omega\cdot S\omega
+4\det S
=
\frac43\nabla\cdot F_B.
}
\]

The usual whole-space Betchov identity is obtained when the boundary/divergence contribution vanishes.

---

## 3. Cutoff form

Let `phi` be a smooth compactly supported spatial cutoff. Then

\[
\boxed{
\int\phi\,\omega\cdot S\omega
=
-4\int\phi\det S
-
\frac43\int\nabla\phi\cdot F_B.
}
\]

The second term is therefore not an untyped error. It is an exact shell/boundary flux.

For any spatially constant vector `c`, replacing `u` by `u-c` leaves the spatial gradient unchanged and gives the same divergence identity. Hence the shell flux may be written in a translation-relative form

\[
F_{B,c}
=
\left(A^2-\frac12\operatorname{tr}(A^2)I\right)(u-c).
\]

This is compatible with the moving-mean / moving-center route.

A crude pointwise bound is

\[
\boxed{
|F_{B,c}|
\le
\frac32|u-c|\,|\nabla u|^2.
}
\]

Therefore

\[
\boxed{
\left|\frac43\int\nabla\phi\cdot F_{B,c}\right|
\le
2\|\nabla\phi\|_\infty
\int_{\operatorname{supp}\nabla\phi}
|u-c|\,|\nabla u|^2.
}
\]

This is a typed cubic shell-transport channel.

---

## 4. Insert the middle-strain saturation defect

Let

\[
f=\lambda_2^+.
\]

The pointwise determinant estimate refined on 2026-08-19 is

\[
-\det S
\le
\frac12f|S|^2-f^3.
\]

Hence the localized vortex-stretching production satisfies

\[
\boxed{
\int\phi\,\omega\cdot S\omega
\le
2\int\phi f|S|^2
-4\int\phi f^3
+
\mathcal F_{B,\phi,c},
}
\]

where

\[
|\mathcal F_{B,\phi,c}|
\le
2\|\nabla\phi\|_\infty
\int_{\operatorname{supp}\nabla\phi}
|u-c|\,|\nabla u|^2.
\]

Thus local fresh stretching production cannot be separated arbitrarily from local middle-strain production unless a shell flux is activated.

---

## 5. Quantitative overlap implication

Define

\[
\mathcal P_\phi
=
\int\phi\,\omega\cdot S\omega,
\]

\[
A_\phi
=
\int\phi f|S|^2,
\qquad
Q_\phi
=
\int\phi f^3.
\]

Then

\[
\boxed{
\mathcal P_\phi
+4Q_\phi
\le
2A_\phi
+\mathcal F_{B,\phi,c}.
}
\]

Therefore if

\[
\mathcal P_\phi\ge P_0>0
\]

and

\[
|\mathcal F_{B,\phi,c}|\le\eta P_0,
\qquad 0\le\eta<1,
\]

then

\[
\boxed{
A_\phi
\ge
\frac{1-\eta}{2}P_0
+2Q_\phi.
}
\]

So a fixed local stretching pulse with small shell transport forces a fixed amount of local positive-middle-strain weighted production.

---

## 6. Convert weighted production into M or H

Take

\[
\phi=\psi^2,
\]

where `psi` is a standard cutoff supported in a parent ball. Then

\[
A_\phi
=
\int f|\psi S|^2
\le
\|f\|_{L^{3/2}(\operatorname{supp}\psi)}
\|\psi S\|_6^2.
\]

Sobolev gives

\[
\|\psi S\|_6^2
\le
C_S\|\nabla(\psi S)\|_2^2
\]

and hence

\[
\boxed{
A_\phi
\le
2C_S\|f\|_{3/2}
\left[
\int\psi^2|\nabla S|^2
+
\int|\nabla\psi|^2|S|^2
\right].
}
\]

Consequently, once the shell Betchov flux is small, a large local stretching pulse implies at least one of:

1. **M:** local critical middle-strain mass `||lambda_2^+||_(3/2)` is non-small;
2. **H:** local strain-gradient / derivative cost is large;
3. **H/T boundary:** the cutoff-gradient strain-energy term is large.

If the Betchov shell flux itself is large, the event is routed to **T**.

Thus the local kinematic implication is

\[
\boxed{
\text{fresh local vortex-stretching production}
\Longrightarrow
M\ \text{or}\ H\ \text{or}\ T.
}
\]

This is the desired local overlap gate at the level of an exact identity plus standard Holder/Sobolev estimates.

---

## 7. Moving vorticity-window form

For a moving cutoff

\[
\phi(x-X(t)),
\]

the localized vorticity enstrophy equation is

\[
\boxed{
\begin{aligned}
\frac12\frac d{dt}\int\phi|\omega|^2
+\nu\int\phi|\nabla\omega|^2
&=
\int\phi\,\omega\cdot S\omega\\
&\quad+
\frac12\int|\omega|^2(u-\dot X)\cdot\nabla\phi\\
&\quad+
\frac\nu2\int|\omega|^2\Delta\phi.
\end{aligned}
}
\]

Substitution of the local Betchov identity therefore yields a moving-window ledger whose source channels are explicitly:

- local positive-middle-strain production;
- cubic middle-strain saturation defect;
- Betchov cubic shell flux;
- relative vorticity transport through the moving shell;
- viscous shell correction;
- interior palinstrophy.

No independent untyped local stretching source remains.

---

## 8. What remains open

The local overlap problem is reduced, but a global proof still needs to show that an infinite first-hitting sequence cannot repeatedly distribute its cost among the `M/H/T` channels while all globally available budgets remain compatible.

The most important next step is therefore no longer proving qualitative overlap. It is a **packing/nonrepeatability estimate for the three explicit local costs**.

A useful target is a normalized first-hitting inequality of the schematic form

\[
\boxed{
\text{child pulse size}
\lesssim
\text{critical M excess}
+
\text{derivative H action}
+
\text{shell T flux},
}
\]

with a strict power or logarithmic gain under repeated scale descent.

---

## External anchor

M. Carbone and M. Wilczek, *Are there higher-order Betchov homogeneity constraints for incompressible isotropic turbulence?*, arXiv:2112.12820. Their equations for `Tr(A^3)` as a divergence provide the kinematic local-divergence anchor used here.

Status: **MASS/PRODUCTION SEGREGATION RECLASSIFIED AS EXACT SHELL FLUX; FRESH LOCAL STRETCHING -> M/H/T; GLOBAL PACKING STEP OPEN**.
