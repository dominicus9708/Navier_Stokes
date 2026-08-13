# Far-strain covariance gap and the local near/constant/variation source split

Date: 2026-08-13

Status: **DERIVED TRACE-FREE COVARIANCE GAP + LOCAL SOURCE DECOMPOSITION / OPEN QUANTITATIVE ABSORPTION**.

The magnitude-direction palinstrophy split gives a strict coefficient deficit for the near nonlinear strain.  The far strain has a complementary structure: on a small dangerous core, its leading part is approximately a constant symmetric trace-free matrix, and a projectively multi-axis vorticity covariance cannot exploit such a common strain as efficiently as a one-axis state.

---

## 1. Exact constant trace-free strain identity

Let `B` be a local region and define

\[
N_B=\int_B\omega\otimes\omega dx,
\qquad
E_B=\operatorname{tr}N_B,
\]

\[
C_B=N_B/E_B
\]

when `E_B>0`.  Then

\[
C_B\ge0,
\qquad
\operatorname{tr}C_B=1.
\]

Define

\[
J_B=1-\operatorname{tr}(C_B^2),
\qquad
0\le J_B\le\frac23.
\]

For any constant symmetric trace-free matrix `S0`,

\[
\int_B\omega\cdot S_0\omega dx
=E_B\operatorname{tr}(S_0C_B).
\]

Since `tr S0=0`,

\[
\operatorname{tr}(S_0C_B)
=\operatorname{tr}\left[S_0\left(C_B-\frac13I\right)\right].
\]

Cauchy--Schwarz in matrix space yields

\[
\left|\operatorname{tr}(S_0C_B)\right|
\le
|S_0|_F
\left|C_B-\frac13I\right|_F.
\]

But

\[
\left|C_B-\frac13I\right|_F^2
=\operatorname{tr}(C_B^2)-\frac13
=\frac23-J_B.
\]

Therefore

\[
\boxed{
\left|
\int_B\omega\cdot S_0\omega dx
\right|
\le
E_B|S_0|_F
\sqrt{\frac23-J_B}.
}
\]

Relative to the one-axis optimum `J=0`, the projective mixing factor is

\[
\boxed{
g(J)
=\sqrt{1-\frac32J}.
}
\]

At isotropic covariance `C=I/3`, `J=2/3` and a common trace-free strain has zero net enstrophy-production coupling.

---

## 2. Equality characterization

Matrix Cauchy--Schwarz is saturated exactly when

\[
S_0
\parallel
C_B-\frac13I.
\]

Thus even the far constant-strain term can be near-extremal only if its principal strain frame is tuned to the traceless part of the local vorticity covariance.

This adds another simultaneous-saturation alignment requirement to a residual singular window.

---

## 3. Near/far strain split

Let `x0` be the dangerous center and choose a smooth cutoff `chi` that equals one on a neighborhood of `B_{2r}(x0)`.  Using the zero-order strain/vorticity singular-integral operator `T`, write

\[
S_{\rm near}=\mathbb T(\chi\omega),
\qquad
S_{\rm far}=S-S_{\rm near}.
\]

Both pieces are symmetric trace-free matrix fields.

The local source is

\[
Q_{B_r}
=\int_{B_r}\omega\cdot S\omega dx
=Q_{\rm near}+Q_{\rm far}.
\]

---

## 4. Near term with magnitude-direction deficit

The Calderon--Zygmund `L^3` bound gives schematically

\[
|Q_{\rm near}|
\lesssim
\|\omega\|_{L^3(B_{cr})}^3
\]

for a fixed buffered radius `c r`.

Using a second smooth cutoff for scalar Sobolev on `rho=|omega|`, for every fixed `eps>0`,

\[
\|\omega\|_{L^6(B_{cr})}^2
\lesssim
(1+\varepsilon)P_{\rm mag,B_{Cr}}
+C_\varepsilon r^{-2}E_{B_{Cr}}.
\]

Since

\[
P_{\rm mag}=P-P_{\rm ang},
\]

define

\[
\mathcal B_r
=(1+\varepsilon)P_{B_{Cr}}
+C_\varepsilon r^{-2}E_{B_{Cr}},
\]

\[
\eta_r
=\frac{(1+\varepsilon)P_{\rm ang,B_{Cr}}}{\mathcal B_r}.
\]

Then

\[
\boxed{
|Q_{\rm near}|
\lesssim
E_{B_{Cr}}^{3/4}
\mathcal B_r^{3/4}
(1-\eta_r)^{3/4}.
}
\]

Thus the cutoff cost dilutes but does not erase the angular-palinstrophy subtraction.

---

## 5. Far term: constant plus variation

For `x in B_r`, write

\[
S_{\rm far}(x)
=S_{\rm far}(x_0)+R_{\rm far}(x).
\]

Then

\[
Q_{\rm far}
=
E_{B_r}\operatorname{tr}[S_{\rm far}(x_0)C_{B_r}]
+
\int_{B_r}\omega\cdot R_{\rm far}\omega dx.
\]

The exact covariance gap gives

\[
\boxed{
|Q_{\rm far}^{(0)}|
\le
E_{B_r}|S_{\rm far}(x_0)|_F
\sqrt{\frac23-J_{B_r}}.
}
\]

For the variation,

\[
\boxed{
|Q_{\rm far}^{(1)}|
\le
E_{B_r}
\sup_{B_r}|R_{\rm far}|
\le
E_{B_r}r
\|\nabla S_{\rm far}\|_{L^\infty(B_r)}.
}
\]

---

## 6. Remote variation has one extra decay power

The strain kernel has homogeneity `-3`; its spatial derivative has homogeneity `-4`.

For dyadic remote annuli `A_j` at distance

\[
R_j\sim2^jr,
\]

Cauchy--Schwarz gives schematically

\[
\boxed{
\|\nabla S_{\rm far}\|_\infty
\lesssim
\sum_{j\ge1}
R_j^{-5/2}
\|\omega\|_{L^2(A_j)}.
}
\]

Hence

\[
\boxed{
r\|\nabla S_{\rm far}\|_\infty
\lesssim
\sum_{j\ge1}
2^{-5j/2}
 r^{-3/2}
\|\omega\|_{L^2(A_j)}.
}
\]

Compared with the far constant strain itself, spatial variation gains one dyadic power.  This is the same locality principle already seen in affine-free pressure differences: remote fields may have a leading low-order component, but their variation across a small dangerous window decays faster.

---

## 7. Combined local source inequality

Combining the previous pieces gives the structural bound

\[
\boxed{
\begin{aligned}
|Q_{B_r}|
\lesssim{}&
E_{B_{Cr}}^{3/4}
\mathcal B_r^{3/4}
(1-\eta_r)^{3/4}\\
&+
E_{B_r}|S_{\rm far}(x_0)|_F
\sqrt{\frac23-J_{B_r}}\\
&+
E_{B_r}r
\|\nabla S_{\rm far}\|_{L^\infty(B_r)}.
\end{aligned}
}
\]

The three terms have distinct DSD types:

1. **near nonlinear source:** depleted by angular palinstrophy;
2. **far common strain:** depleted by local multi-axis covariance;
3. **far spatial variation:** charged to remote-scale gradient/dyadic channels.

No far term is discarded.

---

## 8. Residual bounded-window consequence

Suppose a naturally renormalized dangerous subsequence has, on a fixed buffered ball,

- bounded normalized local energy;
- bounded normalized palinstrophy;
- bounded remote strain/variation channels;
- projective roughness `J>=j0>0`.

Then both leading source mechanisms carry strict coefficient deficits:

\[
(1-\eta_r)^{3/4}
\le1-\delta_1,
\]

and

\[
\sqrt{1-\frac32J}
\le1-\delta_2
\]

for positive dimensionless deficits depending on the bounded state block.

Thus a residual compactness limit cannot simultaneously saturate the generic near Sobolev source and the optimal one-axis far constant-strain source.

What remains is to prove that the two deficits plus viscous dissipation dominate the far-variation and localization terms quantitatively on every residual normalized window.

---

## 9. Current strict-gain target

The new local target is no longer merely

\[
\text{source}\lesssim\text{critical size}.
\]

It is

\[
\boxed{
\text{source}
\le
(1-\delta)\times\text{critical extremal source}
+
\text{strictly localizable remainder}.
}
\]

A proof-producing closure would establish a uniform `delta>0` on the residual rough/non-sparse bounded-channel class and show that the remote variation cannot refill that gap.

Status: **OPEN UNIFORM SOURCE-GAP / REMOTE-VARIATION ABSORPTION**.
