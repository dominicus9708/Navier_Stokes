# Explicit Projective-Speed / Swap Closure — 2026-08-21

Status: **EXPLICIT SMOOTH PURE-P_V CLOSURE CERTIFICATE / GLOBAL REGULARITY NOT PROVED.**

This note removes the abstract projective-speed constant from the transverse anti-ribbon swap gate.

## 1. Algebraic projective residual

Use the normalized full-NS algebraic projective residual

\[
\mathcal V
=P_{st}\left(
\frac13\Sigma^2
+\frac14\Omega\otimes\Omega
\right).
\]

Orthogonal projection does not increase the L2 norm, hence

\[
\|\mathcal V\|_2
\le
\frac13\|\Sigma\|_4^2
+\frac14\|\Omega\|_4^2.
\]

Let

\[
E=\|\Sigma\|_2^2,
\qquad
P=\|\nabla\Sigma\|_2^2,
\qquad
\lambda=P/E.
\]

Also

\[
\|\Omega\|_2^2=2E,
\qquad
\|\Omega\|_\infty\le1.
\]

## 2. Explicit L4 bound for strain

The sharp three-dimensional Sobolev inequality is

\[
\|f\|_6^2
\le
S_3^{-1}\|\nabla f\|_2^2,
\qquad
S_3=3\left(\frac\pi2\right)^{4/3}.
\]

Apply it to \(|\Sigma|\), using Kato's inequality, and interpolate L4 between L2 and L6:

\[
\|\Sigma\|_4
\le
\|\Sigma\|_2^{1/4}
\|\Sigma\|_6^{3/4}.
\]

Therefore

\[
\boxed{
\|\Sigma\|_4^2
\le
S_3^{-3/4}
E^{1/4}P^{3/4}.
}
\]

Dividing by \(\|\Sigma\|_2=E^{1/2}\),

\[
\boxed{
\frac{\|\Sigma\|_4^2}{\|\Sigma\|_2}
\le
S_3^{-3/4}\lambda^{3/4}E^{1/2}.
}
\]

## 3. Explicit vorticity term

The first-hitting cap gives

\[
\|\Omega\|_4^4
\le
\|\Omega\|_\infty^2\|\Omega\|_2^2
\le
2E.
\]

Hence

\[
\|\Omega\|_4^2
\le
\sqrt{2E}
\]

and

\[
\boxed{
\frac14
\frac{\|\Omega\|_4^2}{\|\Sigma\|_2}
\le
\frac{\sqrt2}{4}.
}
\]

## 4. Explicit projective-speed ceiling

Combining the two terms,

\[
\boxed{
\frac{\|\mathcal V\|_2}{\|\Sigma\|_2}
\le
C_V(E,\lambda)
:=
\frac13S_3^{-3/4}\lambda^{3/4}E^{1/2}
+\frac{\sqrt2}{4}.
}
\]

Thus on a smooth tightness corridor

\[
E\le E_+,
\qquad
\lambda\le\lambda_+,
\]

one may take

\[
\boxed{
C_{V,+}
=
\frac13S_3^{-3/4}\lambda_+^{3/4}E_+^{1/2}
+\frac{\sqrt2}{4}.
}
\]

No unspecified L4 Riesz-transform norm is needed.

## 5. Insert the smooth endpoint bounds

The vorticity-tightness cap gives

\[
E_+
=
\frac12Z_+
\le
\frac{2\pi R_Z^3}{3(1-\varepsilon_Z)}.
\]

The sharpened endpoint frequency corridor gives

\[
\lambda_+
\le
\frac{35}{16\sqrt2}
\frac{K_1^2K_2^{3/2}R_Q^3}{1-\varepsilon_Q}.
\]

Hence \(C_{V,+}\) is an explicit function of the smooth first-hitting analytic/tightness data.

## 6. M0=2 dimensionless specialization

Use the analytic endpoint bounds

\[
K_1\le\frac{2}{\rho_0},
\qquad
K_2\le\frac{4}{\rho_0^2}.
\]

Let

\[
R_Z=r_Z\rho_0,
\qquad
R_Q=r_Q\rho_0,
\]

and set \(\varepsilon_Z=\varepsilon_Q=0\) for the clean benchmark.

Then

\[
\lambda_+\rho_0^2
\le
32\frac{35}{16\sqrt2}r_Q^3
\]

and

\[
E_+^{1/2}\rho_0^{-3/2}
\le
\sqrt{\frac{2\pi}{3}}r_Z^{3/2}.
\]

For a common radius

\[
r_Z=r_Q=r,
\]

this simplifies numerically to

\[
\boxed{
C_{V,+}(r)
\le
0.3535533906
+2.5141113904\,r^{15/4}.
}
\]

## 7. Explicit anti-ribbon swap time

The transverse-axis swap gate gives

\[
L_j
\ge
\frac{\pi}{1+2C_{V,+}}.
\]

At the current zero-tail common-core floor

\[
r_*=0.53193814,
\]

we obtain

\[
\boxed{
C_{V,+}(r_*)
\le
0.58925565
}
\]

and therefore

\[
\boxed{
L_{swap}(r_*)
\ge
1.44208232.
}
\]

## 8. Compare with the moving-variance upper time

For \(M_0=2\), \(\sigma=1/2\),

\[
\rho_0^2
=\frac{\sigma\nu}{c(2)^2}.
\]

At common radius \(R_V=r_*\rho_0\), the moving-variance ceiling is

\[
L_{var}
=\Pi_V\frac{R_V^2}{\nu}
=\Pi_Vr_*^2\frac{\sigma}{c(2)^2}.
\]

Numerically,

\[
\boxed{
L_{var}
=0.14147909\,
\frac{\Pi_V}{c(2)^2}.
}
\]

Therefore the pure projective anti-ribbon branch is S-closed at the minimal common-core radius whenever

\[
0.14147909\frac{\Pi_V}{c(2)^2}
<1.44208232.
\]

Equivalently,

\[
\boxed{
\frac{\Pi_V}{c(2)^2}<10.1929
\quad\Longrightarrow\quad
\text{minimal-radius pure P_V anti-ribbon stage is S-closed}.
}
\]

## 9. Significance

The previous swap gate depended on an abstract projective-speed constant. The present estimate replaces it by endpoint quantities already controlled on the smooth first-hitting corridor.

The main unresolved numerical input in the minimal-radius benchmark is now the ratio

\[
\boxed{\Pi_V/c(2)^2.}
\]

If it can be bounded below the explicit threshold 10.1929, the pure coherent positive-middle anti-ribbon branch closes directly before any limiting argument.

If it exceeds the threshold, the amount by which it exceeds it quantifies exactly how much room remains for the stage.

Status: **THE PURE P_V PROJECTIVE SPEED IS NOW EXPLICITLY BOUNDED BY SHARP SOBOLEV INTERPOLATION. AT THE CURRENT MINIMAL COMMON-CORE RADIUS, S-CLOSURE REDUCES TO THE SINGLE NUMERICAL TEST `Pi_V/c(2)^2 < 10.1929`.**