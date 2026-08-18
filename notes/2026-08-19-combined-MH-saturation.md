# Combined M/H saturation: quadratic survival forces enstrophy power growth

Date: 2026-08-19

Status: **DERIVED CONDITIONAL CROSS-BRANCH POWER LAW / GLOBAL REGULARITY NOT PROVED**.

This note combines:

1. the local middle-strain saturation power gain;
2. the high-derivative saturation ratio anchored to Miller 2024.

The purpose is to distinguish quadratic high-derivative survival from advection/material-turnover survival.

---

## 1. Input from near-saturated M

For an order-one local fresh stretching pulse with subdominant Betchov shell flux, define

\[
\delta_\phi
=\frac{Q_\phi}{A_\phi}
=
\frac{\int\phi(\lambda_2^+)^3}
{\int\phi\lambda_2^+|S|^2}.
\]

The previous power-gain lemma gives

\[
\boxed{
E_\omega P_\omega
\gtrsim
P_0^{4/3}\delta_\phi^{-2/3},
}
\]

up to fixed cutoff/shell constants.

Write

\[
A=\|S\|_2,
\qquad
B=\|\Delta S\|_2.
\]

Then

\[
E_\omega=2A^2,
\]

and interpolation gives

\[
P_\omega
\lesssim
A B.
\]

Hence

\[
\boxed{
E_\omega P_\omega
\lesssim
A^3B.
}
\]

---

## 2. Split the dangerous H saturation

The Miller-type dangerous numerator is

\[
N_H
=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right).
\]

If the ratio `||N_H||_2/B` stays order one, then by the triangle inequality at least one of the following is order one relative to `B`:

### Q-H branch: quadratic saturation

\[
\|S^2\|_2+\|\omega\otimes\omega\|_2
\gtrsim B.
\]

### A-H branch: advection saturation

\[
\|(u\cdot\nabla)S\|_2
\gtrsim B.
\]

These two mechanisms have different consequences.

---

## 3. Quadratic H saturation

From

\[
\|S^2\|_2+\|\omega\otimes\omega\|_2
\lesssim
A^{5/4}B^{3/4},
\]

quadratic saturation forces

\[
\boxed{
B\lesssim A^5.
}
\]

Therefore

\[
E_\omega P_\omega
\lesssim
A^3B
\lesssim
A^8.
\]

Combining with the near-saturated M lower bound gives

\[
A^8
\gtrsim
P_0^{4/3}\delta_\phi^{-2/3}.
\]

Thus

\[
\boxed{
A
\gtrsim
P_0^{1/6}\delta_\phi^{-1/12},
}
\]

and hence

\[
\boxed{
E_\omega
\gtrsim
P_0^{1/3}\delta_\phi^{-1/6}.
}
\]

This is scale-consistent: `P0` has the same Navier--Stokes homogeneity as an integrated cubic strain/vortex-stretching production.

Therefore, as `delta_phi -> 0`, a near-saturated M pulse cannot survive through a purely quadratic H saturation while keeping enstrophy bounded.

Under the first-hitting normalized cap `||Omega||_infty<=1`, divergent normalized enstrophy is a spatial non-tightness certificate.

Hence

\[
\boxed{
\text{near-saturated M}
+\text{quadratic H saturation}
\Longrightarrow
T\text{ through enstrophy non-tightness}.
}
\]

---

## 4. Advection H saturation

The advection estimate is

\[
\|(u\cdot\nabla)S\|_2
\lesssim
K^{1/4}A^{7/8}B^{7/8},
\qquad
K=\|u\|_2.
\]

Advection saturation therefore gives

\[
\boxed{
B\lesssim K^2A^7.
}
\]

Consequently

\[
E_\omega P_\omega
\lesssim
K^2A^{10}.
\]

Combining with the M power gain,

\[
\boxed{
A
\gtrsim
K^{-1/5}P_0^{2/15}\delta_\phi^{-1/15},
}
\]

and

\[
\boxed{
E_\omega
\gtrsim
K^{-2/5}P_0^{4/15}\delta_\phi^{-2/15}.
}
\]

This is weaker because the kinetic-energy scale enters explicitly. In first-hitting normalized variables the normalized kinetic energy is not uniformly bounded even though the physical kinetic energy is.

Thus the advection-saturated branch cannot yet be converted unconditionally to non-tightness by this estimate alone.

This identifies advection/material turnover as the harder survivor.

---

## 5. Revised endgame

The compact near-saturated branch is now reduced as follows:

\[
\boxed{
\text{near-saturated M fresh pulse}
\Longrightarrow
\begin{cases}
\text{large shell flux }T,\\
\text{quadratic H saturation }\Rightarrow\text{ enstrophy power growth }\Rightarrow T,\\
\text{advection H saturation }(A\!H/T),\\
\text{or non-saturated critical M.}
\end{cases}
}
\]

Therefore the strongest remaining mechanism on the near-saturated route is no longer generic high derivative growth. It is specifically

\[
\boxed{
\text{advection-sustained derivative saturation / bounded-radius material turnover}.
}
\]

This is consistent with the 2024 strain--vorticity interaction analysis, which identifies the alignment of advection with the quadratic strain nonlinearity as decisive for depletion or maintenance of nonlinear growth.

Status: **QUADRATIC H SURVIVAL OF NEAR-SATURATED M REDUCED TO ENSTROPHY NON-TIGHTNESS; HARD SURVIVOR = ADVECTION-SATURATED H/T OR NON-SATURATED CRITICAL M**.
