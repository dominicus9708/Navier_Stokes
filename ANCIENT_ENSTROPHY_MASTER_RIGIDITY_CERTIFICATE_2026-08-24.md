# Ancient Enstrophy Master Rigidity Certificate — 2026-08-24

Status: **BOUNDED-ENSTROPHY ANCIENT ENDGAME REDUCED TO THREE NORMALIZED CONSTANTS / VELOCITY TAIL DOES NOT ENTER THE CERTIFICATE / GLOBAL REGULARITY NOT PROVED.**

This note combines the two tail-independent vorticity-only rigidity routes:

1. the universal trace-free stretching coefficient;
2. the positive-middle/Betchov-residual absorption inequality.

The purpose is to remove redundant constants and identify the smallest remaining quantitative target.

---

## 1. Restricted ancient inputs

On the vorticity-tight ancient branch, the existing first-hitting inheritance gives

\[
\boxed{
M(t):=\|\Omega(t)\|_\infty
\le \frac{K_I}{|t|}
}
\]

and

\[
\boxed{
Z(t):=\|\Omega(t)\|_2^2
\le
Z_+K_I^{1/2}|t|^{-1/2}.
}
\]

Thus the backward decay exponent is

\[
\alpha=\frac12
\]

and the amplitude constant in the notation of the Betchov-absorption note is not independent:

\[
\boxed{
A=Z_+K_I^{1/2},
\qquad
A^2=Z_+^2K_I.
}
\]

The recurrent active-core windows additionally give a logarithmic frequency floor

\[
\boxed{
\liminf_{T\to\infty}
\frac1{\log T}
\int_{-T}^{-1}\frac{Q}{Z}\,dt
\ge c_{\log}>0.
}
\]

---

## 2. Route A: universal trace-free stretching

The sharp trace-free eigenvalue estimate gives

\[
\mathcal P\le\frac1{\sqrt3}MZ.
\]

Hence

\[
\frac d{dt}\log Z
\le
\frac{2K_I}{\sqrt3|t|}
-2\nu\frac QZ.
\]

After logarithmic averaging, define

\[
\boxed{
\Gamma_{TF}
:=
\frac{2K_I}{\sqrt3}
-2\nu c_{\log}.
}
\]

Then

\[
\boxed{
\Gamma_{TF}<\frac12
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

Without the frequency floor this reduces to

\[
K_I<\frac{\sqrt3}{4}.
\]

---

## 3. Route B: positive-middle coefficient plus global Betchov absorption

The sharp global absorption note gives, for `0<delta<=1`,

\[
\frac d{dt}\log Z
\le
M
+\frac{32}{729\pi^4}
\delta^{-3}\nu^{-3}Z^2
-2(1-\delta)\nu\frac QZ.
\]

Use

\[
M\le K_I|t|^{-1}
\]

and

\[
Z^2
\le Z_+^2K_I|t|^{-1}.
\]

Then the effective logarithmic exponent is

\[
\boxed{
\Gamma_B(\delta)
=
K_I\left[
1+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3\delta^3}
\right]
-2(1-\delta)\nu c_{\log}.
}
\]

Therefore

\[
\boxed{
\inf_{0<\delta\le1}\Gamma_B(\delta)<\frac12
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

The formal optimizer is

\[
\boxed{
\delta_*
=
\left(
\frac{16Z_+^2K_I}
{243\pi^4\nu^4c_{\log}}
\right)^{1/4},
\qquad
\delta_{opt}=\min\{1,\delta_*\}.
}
\]

---

## 4. Master certificate

Define

\[
\boxed{
\Gamma_{best}
:=
\min\left\{
\Gamma_{TF},
\Gamma_B(\delta_{opt})
\right\}.
}
\]

Then the bounded-enstrophy ancient branch is impossible whenever

\[
\boxed{
\Gamma_{best}<\frac12.
}
\]

Indeed backward integration would force `Z(t0)=0` for every finite `t0<0`, contradicting terminal first-hitting nontriviality.

---

## 5. Remaining normalized parameters

The certificate depends only on

\[
\boxed{
K_I,
\qquad
Z_+,
\qquad
c_{\log},
\qquad
\nu.
}
\]

For fixed viscosity, there are only three dynamical normalized constants.

Their meanings are:

- `K_I`: continuous backward Type-I vorticity constant inherited from first-hitting stage timing;
- `Z_+`: normalized dynamic enstrophy ceiling from the vorticity-tight corridor;
- `c_log`: logarithmic frequency/palinstrophy floor forced by recurrent active-core windows.

No global velocity `L3` norm, weak-`L3` tail, remote velocity radius, or spatial Betchov-localization constant appears.

---

## 6. Substitute the known enstrophy-tightness ceiling

If

\[
\int_{B_{R_Z}}|\Omega|^2
\ge(1-\varepsilon_Z)Z
\]

and `||Omega||_infinity<=1`, then

\[
\boxed{
Z_+
=\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Thus `Z_+` can itself be replaced by the geometric pair

\[
R_Z,\qquad\varepsilon_Z.
\]

The Betchov cubic correction becomes

\[
\frac{32}{729\pi^4}Z_+^2
=
\boxed{
\frac{512}{6561\pi^2}
\frac{R_Z^6}{(1-\varepsilon_Z)^2}
}
\]

before the factors `K_I/(nu^3 delta^3)` are inserted.

Hence a tighter enstrophy radius directly improves the new rigidity gate with sixth-power sensitivity.

---

## 7. Interpretation

The ancient low-frequency velocity tail remains a genuine object geometrically, but it is no longer present in this particular closure test.

The proof program now has two logically different options:

1. continue classifying/removing the persistent passive velocity tail;
2. prove `Gamma_best<1/2` from first-hitting timing, enstrophy tightness, and recurrent frequency production alone.

The second route is shorter if its constants can be closed.

---

## 8. Next quantitative target

The highest-leverage next calculation is not another tail decomposition. It is to reduce or lower-bound the three master inputs:

\[
\boxed{
K_I\downarrow,
\qquad
Z_+\downarrow,
\qquad
c_{\log}\uparrow.
}
\]

The existing files already contain separate estimates for all three:

- moving-variance / stage-duration ceilings for `K_I`;
- thick-core/tightness geometry for `Z_+`;
- active-core Poincare/palinstrophy windows for `c_log`.

They should now be optimized against the single scalar inequality `Gamma_best<1/2` instead of being developed as separate proof branches.

Status: **THE BOUNDED-ENSTROPHY ANCIENT ENDGAME HAS A SINGLE EXPLICIT TAIL-INDEPENDENT MASTER CERTIFICATE. FOR FIXED VISCOSITY IT DEPENDS ONLY ON `K_I`, `Z_+`, AND `c_log`. GLOBAL REGULARITY REMAINS UNPROVED.**