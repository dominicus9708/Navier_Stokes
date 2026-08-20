# Fully Explicit Cutoff Second-Order Gate — 2026-08-20

Status: **FULLY EXPLICIT LOCALIZATION CONSTANTS — GLOBAL REGULARITY NOT PROVED.**

This note gives a weaker but completely explicit alternative to the Bogovskii-corrected solenoidal gate. It sacrifices the solenoidal constant improvement but removes the unknown localization constant `C_loc^(2)`.

## 1. Explicit radial cutoff

Let

\[
s=(|x|-R)/R
\]

on the annulus `A_R=B_{2R}\setminus B_R` and use

\[
\phi(s)=1-10s^3+15s^4-6s^5,
\qquad0\le s\le1.
\]

Set `chi_R=1` on `B_R`, `chi_R=phi(s)` on `A_R`, and `chi_R=0` outside `B_{2R}`.

The exact derivative maxima are

\[
\max|\phi'|=15/8,
\qquad
\max|\phi''|=10/\sqrt3.
\]

Therefore

\[
\boxed{
|\nabla\chi_R|\le\frac{15}{8R},
}
\]

and, since `|x|>=R` on the annulus,

\[
\boxed{
|\Delta\chi_R|
\le
\left(\frac{10}{\sqrt3}+\frac{15}{4}\right)R^{-2}.
}
\]

## 2. Generic compact-support second-order uncertainty

For any scalar or vector field `f` in `H^2(R^3)` with finite second moment, the ordinary 3D Heisenberg inequality and Cauchy interpolation give

\[
\left(\int|x|^2|f|^2\right)
\|\Delta f\|_2
\ge
\frac94\|f\|_2^3.
\]

If `supp f subset B_{2R}`, then

\[
\int|x|^2|f|^2\le4R^2\|f\|_2^2,
\]

hence

\[
\boxed{
\|\Delta f\|_2
\ge
\frac9{16R^2}\|f\|_2.
}
\]

No divergence-free assumption is required.

## 3. Apply to the cutoff vorticity

Set

\[
f=\chi_R\Omega.
\]

Then `f=Omega` on `B_R` and is supported in `B_{2R}`, so

\[
\|f\|_2\ge\|\Omega\|_{L^2(B_R)}.
\]

Also

\[
\Delta(\chi_R\Omega)
=\chi_R\Delta\Omega
+2\nabla\chi_R\cdot\nabla\Omega
+(\Delta\chi_R)\Omega.
\]

Therefore

\[
\boxed{
\begin{aligned}
&R^2
\frac{\|\Delta\Omega\|_{L^2(B_{2R})}}
{\|\Omega\|_{L^2(B_R)}}\\
&\quad+\frac{15}{4}R
\frac{\|\nabla\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}}\\
&\quad+
\left(\frac{10}{\sqrt3}+\frac{15}{4}\right)
\frac{\|\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}}
\ge\frac9{16}.
\end{aligned}
}
\]

Every constant in this local gate is explicit.

## 4. Combine with first-hitting analyticity

Assume the normalized analytic strip data

\[
|\Omega(y_*)|=1,
\qquad
\sup_{|\operatorname{Im}y|<\rho_0}|\Omega|\le M_0.
\]

As derived in `ANALYTICITY_LOCAL_MASS_LEAKAGE_GATE_2026-08-20.md`, for

\[
R\le\frac{\rho_0}{12M_0}
\]

we have

\[
R^2
\frac{\|\Delta\Omega\|_{L^2(B_{2R})}}
{\|\Omega\|_{L^2(B_R)}}
\le
96\sqrt6M_0\frac{R^2}{\rho_0^2}.
\]

If additionally

\[
R
\le
0.03458381\frac{\rho_0}{\sqrt{M_0}},
\]

then the analytic local `Delta Omega` term is at most `9/32`.

Thus for

\[
\boxed{
R\le
R_{ex}^{explicit}
:=
\min\left\{
\frac{\rho_0}{12M_0},
0.03458381\frac{\rho_0}{\sqrt{M_0}}
\right\},
}
\]

the annular terms must satisfy

\[
\boxed{
\frac{15}{4}\varepsilon_1
+\left(\frac{10}{\sqrt3}+\frac{15}{4}\right)\varepsilon_0
\ge\frac9{32},
}
\]

where

\[
\varepsilon_1
=R\frac{\|\nabla\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}},
\qquad
\varepsilon_0
=\frac{\|\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}}.
\]

Consequently at least one explicit branch holds:

\[
\boxed{
\varepsilon_1\ge\frac3{80}=0.0375
}
\]

or

\[
\boxed{
\varepsilon_0
\ge
\frac{9/64}{10/\sqrt3+15/4}
\approx0.01476610.
}
\]

The first is a fixed annular derivative fraction and is an `H` candidate. The second is a fixed annular vorticity-mass fraction and is a bounded-radius leakage/turnover `T` candidate. Converting repeated occurrence into the formal global `H/T` alternatives still requires the corresponding packing/nonrepeatability lemma.

## 5. Clay-data specialization

On the smooth rapidly-decaying initial-data track, the analyticity theorem gives

\[
M_0=M,
\qquad
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M)}
\]

for arbitrary `M>1` and `0<sigma<1`.

Hence

\[
\boxed{
R_{ex}^{explicit}(M,\sigma)
=
\frac{\sqrt{\sigma\nu}}{c(M)}
\min\left\{
\frac1{12M},
\frac{0.03458381}{\sqrt M}
\right\}.
}
\]

For `M=2`, the second entry is smaller:

\[
\boxed{
R_{ex}^{explicit}(2,\sigma)
\approx
\frac{0.02445445\sqrt{\sigma\nu}}{c(2)}.
}
\]

With the conservative choice `sigma=1/2`,

\[
R_{ex}^{explicit}
\approx
\frac{0.01729191}{c(2)}\sqrt\nu.
\]

This lower scale is numerically weaker than the Bogovskii-solenoidal route but has no unspecified localization constant.

Status: **A FULLY EXPLICIT CUTOFF ARGUMENT SHOWS THAT A FIRST-HITTING CORE BELOW `R_ex^explicit` MUST CARRY EITHER AT LEAST `3/80` NORMALIZED ANNULAR GRADIENT LEAKAGE OR AT LEAST `0.0147661` ANNULAR VORTICITY-MASS LEAKAGE. THE ONLY REMAINING NONNUMERICAL INPUT ON THE CLAY-DATA TRACK IS THE STANDARD ANALYTICITY CONSTANT `c(M)`.**