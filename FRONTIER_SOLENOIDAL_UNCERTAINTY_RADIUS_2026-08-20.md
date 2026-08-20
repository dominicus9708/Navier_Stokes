# Solenoidal-Uncertainty P_V Frontier — 2026-08-20

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note continues `FRONTIER_VORTICITY_HESSIAN_RADIUS_2026-08-20.md` and replaces the generic-vector Heisenberg constant in the new vorticity-Hessian estimate by the sharp constant for three-dimensional solenoidal fields.

External anchor:

- Naoki Hamamoto, *Sharp Uncertainty Principle inequality for solenoidal fields*, Journal de Mathematiques Pures et Appliquees 172 (2023), 202--235, DOI `10.1016/j.matpur.2023.01.008`.
- arXiv: `2104.02351`.

Hamamoto proves that for divergence-free vector fields on `R^N`,

\[
\int|\nabla v|^2dx\int|x|^2|v|^2dx
\ge C_N\left(\int|v|^2dx\right)^2,
\]

with sharp

\[
C_N=\frac14\left(\sqrt{N^2-4(N-3)}+2\right)^2
\quad(N\ge3).
\]

For `N=3`,

\[
\boxed{C_3=\frac{25}{4}.}
\]

---

## 1. Applicability to vorticity

For a smooth whole-space Navier--Stokes profile,

\[
\nabla\cdot\omega=0.
\]

Therefore the sharp solenoidal uncertainty inequality applies directly to the whole-space vorticity profile, including translated coordinates centered at any chosen `X`.

Define

\[
Z=\|\omega\|_2^2,
\qquad
P_\omega=\|\nabla\omega\|_2^2,
\]

\[
M_\omega=\int|x-X|^2|\omega|^2dx,
\qquad
R_\omega^2=M_\omega/Z,
\]

and

\[
D=\|\Delta\omega\|_2^2.
\]

Hamamoto's sharp `N=3` inequality gives

\[
\boxed{
M_\omega P_\omega
\ge\frac{25}{4}Z^2.
}
\]

Also

\[
P_\omega^2
=\langle-\Delta\omega,\omega\rangle^2
\le ZD.
\]

Combining the two,

\[
D
\ge
\frac{P_\omega^2}{Z}
\ge
\frac{625}{16}\frac{Z^3}{M_\omega^2}.
\]

Thus

\[
\boxed{
\sqrt{\frac ZD}
\le
\frac4{25}R_\omega^2.
}
\]

This is much stronger than the generic-vector estimate `sqrt(Z/D) <= (4/9) R_omega^2`.

---

## 2. Insert the vorticity-Hessian H1 bound

From `FRONTIER_VORTICITY_HESSIAN_RADIUS_2026-08-20.md`,

\[
\boxed{
\eta_{VI}
\le
\sqrt{\frac32}\,\|\omega\|_\infty
\sqrt{\frac ZD}.
}
\]

Therefore

\[
\eta_{VI}
\le
\sqrt{\frac32}\,\|\omega\|_\infty
\frac4{25}R_\omega^2.
\]

Hence the sharpened whole-space solenoidal bound is

\[
\boxed{
\eta_{VI}
\le
C_{sol}\,\|\omega\|_\infty R_\omega^2,
\qquad
C_{sol}=\frac{2\sqrt6}{25}
\approx0.1959591794.
}
\]

The successive explicit constants are now

\[
0.79048528
\;\longrightarrow\;
0.54433105
\;\longrightarrow\;
0.19595918,
\]

where the last step uses the divergence-free structure of vorticity.

---

## 3. First-hitting whole-space radius barrier

At first-hitting normalization,

\[
\|\Omega\|_\infty=1.
\]

A whole-space threshold profile satisfying

\[
\eta_{VI}\ge\nu
\]

must therefore obey

\[
R_\Omega^2
\ge
\frac{\nu}{C_{sol}}
=
\frac{25}{2\sqrt6}\nu.
\]

Equivalently,

\[
\boxed{
R_\Omega
\ge
\sqrt{\frac{25}{2\sqrt6}}\sqrt\nu
\approx2.25900501\sqrt\nu.
}
\]

For `nu=1`, a whole-space first-hitting `P_V` threshold profile with

\[
R_\Omega<2.2590
\]

is excluded by the present H1 threshold estimate.

---

## 4. Ancient Type-I consequence

If the restricted ancient candidate obeys

\[
\|\Omega(\tau)\|_\infty\le\frac{C_I}{|\tau|},
\]

then any whole-space recurrent threshold time with

\[
\eta_{VI}(\tau)\ge\nu
\]

must satisfy

\[
\boxed{
R_\Omega(\tau)
\ge
\sqrt{\frac{25}{2\sqrt6 C_I}}
\sqrt{\nu|\tau|}.
}
\]

Thus the lower edge of the allowed similarity-scale annulus is substantially raised.

---

## 5. Scope restriction

The `25/4` constant is a sharp theorem for globally divergence-free vector fields on `R^3` with the relevant finite norms.

Therefore this strengthened barrier applies directly to:

- the full first-hitting rescaled vorticity field;
- a whole-space strain-compatible compactness limit;
- the restricted ancient whole-space vorticity candidate.

It must **not** be applied without correction to an arbitrary cutoff vorticity cell, because multiplication by a cutoff generally destroys the solenoidal constraint. A localized use requires a divergence-free localization/correction or an argument passing through the whole-space profile first.

---

## 6. New endgame interpretation

The non-H/T `P_V` survivor now has a much larger mandatory vorticity rms radius at every whole-space threshold recurrence.

This strengthens the tension between:

1. a tight Type-I active core;
2. the raised threshold radius `R_Omega >= 2.259*sqrt(nu)` at first hitting;
3. the remote-halo passivity barrier;
4. the globally necessary low-vorticity critical tail.

The next quantitative target is to compare the new lower radius `2.259*sqrt(nu)` with the independently obtained non-T upper radius `c_+` in the fixed-center Type-I tower. If the available tower estimates force

\[
c_+<2.259\sqrt\nu,
\]

the recurrent whole-space `P_V` threshold branch closes immediately. If not, the numerical gap `c_+-2.259*sqrt(nu)` becomes the next explicit quantity to reduce.

A parallel target is to derive a solenoidal **second-order** uncertainty inequality directly for the pair `(D,M_omega,Z)`, which could improve the constant further beyond the two-step combination of Hamamoto's first-order sharp inequality and `P_omega^2 <= ZD`.

---

Status: **GLOBAL REGULARITY IS NOT PROVED. USING THE SHARP 3D SOLENOIDAL HEISENBERG CONSTANT `25/4`, THE WHOLE-SPACE FIRST-HITTING `P_V` RADIUS BARRIER IMPROVES TO `R_Omega >= 2.259005*sqrt(nu)`. THE NEXT DECISIVE CHECK IS WHETHER THE NON-T TYPE-I TOWER ALREADY HAS AN UPPER RMS-RADIUS CONSTANT BELOW THIS VALUE.**