# DSD M19-101 — DSS monodromy has essential spectral radius below one and all unit Floquet multipliers are finite-multiplicity discrete modes

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / APPLICATION OF M19-095 QUASI-COMPACTNESS TO EXACT DSS PERIODIC COEFFICIENTS / UNIT-CIRCLE FLOQUET SPECTRUM IS DISCRETE AND FINITE-MULTIPLICITY / EXACT SYMMETRY MULTIPLIERS ARE SEPARATED BY M19-099 / DOES NOT EXCLUDE THE PERIODIC ORBIT ITSELF / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Periodic linearized vorticity cocycle

Let `U(y,s)` be an exact DSS similarity profile with period

\[
S=2\log\lambda>0.
\]

Let

\[
\mathcal M_S
:=
\mathcal U(s+S,s)
\]

be the one-period linearized vorticity monodromy operator on

\[
L^2_\sigma(\mathbb R^3).
\]

Periodicity makes its spectrum independent of the base phase up to conjugacy.

---

## 2. Essential spectral radius

M19-095 proves, on the controlled critical-tail coefficient class,

\[
\mathcal U(s+T,s)-e^{T\mathcal L_0}
\quad\text{compact},
\]

where

\[
\mathcal L_0
=\nu\Delta-1-\frac12y\cdot\nabla
\]

and

\[
\|e^{T\mathcal L_0}\|
\le e^{-T/4}.
\]

Taking `T=S`,

\[
\boxed{
\mathcal M_S-e^{S\mathcal L_0}
\quad\text{is compact}.
}
\]

Therefore

\[
\boxed{
r_{ess}(\mathcal M_S)
\le e^{-S/4}<1.}
\]

---

## 3. Unit-circle spectrum is discrete

Because the essential spectrum lies strictly inside the unit disk, every Floquet multiplier

\[
|\mu|\ge1
\]

belongs to the discrete spectrum of `M_S` and has finite algebraic multiplicity.

In particular,

\[
\boxed{
\ker(I-\mathcal M_S)
\text{ is finite-dimensional}.}
\]

Thus exact neutral DSS perturbations cannot arise from an infinite-dimensional far-tail continuous spectrum.

---

## 4. Exact symmetry multipliers

M19-099 identifies the symmetry spectrum:

\[
\boxed{
\begin{array}{c|c}
\text{symmetry} & \mu\\
\hline
\text{spatial translation} & \lambda\\
\text{blowup-time translation} & \lambda^2\\
\text{scaling/time phase} & 1\\
\text{rotation} & 1\\
\text{Galilean boost} & \lambda^{-1}.
\end{array}}
\]

Hence the known unit eigenspace is

\[
E_{sym,1}
=
\operatorname{span}\{\partial_sU\}
\oplus T_U(SO(3)\cdot U)
\]

modulo isotropy.

---

## 5. The genuine extra-neutral space

Define

\[
\boxed{
E_{DSS}^{extra}
:=
\ker(I-\mathcal M_S)
\ominus E_{sym,1}
}
\]

in a chosen symmetry-transverse slice.

M19-101 shows

\[
\boxed{
\dim E_{DSS}^{extra}<\infty.}
\]

Therefore the question of extra periodic phases is a finite-dimensional Fredholm kernel problem.

---

## 6. Fredholm formulation

Since `1` lies outside the essential spectrum,

\[
I-\mathcal M_S
\]

is Fredholm of index zero on the retained phase space.

After imposing the phase and rotational modulation conditions, DSS nondegeneracy is equivalent to

\[
\boxed{
\ker(I-\mathcal M_S)_{transverse}=\{0\}.}
\]

This is the periodic analogue of the M19-090 extra-center problem.

---

## 7. What nondegeneracy would and would not prove

If

\[
E_{DSS}^{extra}=0,
\]

then the DSS orbit is spectrally isolated modulo exact symmetries at multiplier one.

This would remove additional neutral phases and simplify local dynamics around the periodic orbit.

It would **not** imply that the periodic orbit itself is zero.

Thus

\[
\boxed{
\text{DSS nondegeneracy}
\neq
\text{DSS Liouville theorem}.}
\]

The existence of the nonzero periodic orbit remains the separate M19-092/096--100 hard problem.

---

## 8. Strategic value

The full weak-critical problem is now separated into three finite objects:

1. the extra-center eigenbundle for aperiodic recurrence;
2. the extra unit-multiplier Fredholm kernel for exact DSS;
3. the nonlinear existence/nonexistence of the DSS periodic orbit itself.

No infinite-dimensional center spectrum remains on the controlled smooth critical-tail corridor.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
