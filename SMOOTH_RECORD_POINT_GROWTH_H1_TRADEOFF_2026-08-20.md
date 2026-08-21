# Smooth Record-Point Growth / H1 Production Tradeoff — 2026-08-20

Status: **S-LEVEL POINTWISE LEMMA ON THE ORIGINAL SMOOTH SOLUTION, TRANSPOSE-AUDITED 2026-08-21. GLOBAL REGULARITY NOT PROVED.**

This note works only at finite smooth first-hitting times. It quantifies a direct incompatibility between efficient growth of the running vorticity maximum and strong local `P_V` H1 production at the same spatial point.

**Audit correction (2026-08-21):** with the convention `G_ij = partial_j Omega_i`, a maximum of `|Omega|` gives `G^T xi = 0`, not `G xi = 0`. The universal Böttcher–Wenzel tradeoff was unaffected, but the earlier exact-alignment spectral sharpening was too strong and has been corrected below.

## 1. Record-growth point

Use the running first-hitting envelope `M(t)` from `SMOOTH_FINITE_STAGE_TIGHTROPE_LEDGER_2026-08-20.md`.

At almost every time where

\[
M'(t)>0,
\]

the current vorticity supremum equals the running envelope. Choose a maximizing point `x_*` and set

\[
|\omega(x_*,t)|=M(t),
\qquad
\xi=\frac{\omega}{M},
\qquad |\xi|=1.
\]

Use the running normalization

\[
\Omega=M^{-1}\omega,
\qquad
\Sigma=M^{-1}S,
\qquad
y=M^{1/2}(x-X_0).
\]

Let

\[
G=\nabla_y\Omega,
\qquad
G_{ij}=\partial_j\Omega_i.
\]

At the maximum,

\[
\nabla_y|\Omega|^2=0.
\]

Since

\[
\partial_j|\Omega|^2
=2\Omega_i\partial_j\Omega_i,
\]

we have

\[
\boxed{G^T\xi=0.}
\]

This is the exact first-hitting constraint on the vorticity-gradient matrix in the stated convention.

## 2. Record growth has an exact viscous loss

The vorticity magnitude identity is

\[
\frac12(\partial_t+u\cdot\nabla)|\omega|^2
=
\omega\cdot S\omega
+\nu\left(
\frac12\Delta|\omega|^2-|\nabla\omega|^2
\right).
\]

At a spatial maximum of `|omega|`,

\[
\Delta|\omega|^2\le0.
\]

Therefore the upper Dini derivative of the running maximum satisfies

\[
M M'
\le
M^2\,\xi^TS\xi
-\nu|\nabla_x\omega|^2.
\]

Since

\[
|\nabla_x\omega|^2=M^3|G|^2,
\]

and

\[
b=\frac{M'}{M^2},
\]

we get

\[
\boxed{
b+\nu|G|^2\le\xi^T\Sigma\xi.}
\]

If `s3` is the largest eigenvalue of `Sigma`, define

\[
\boxed{
\delta_{align}=s_3-\xi^T\Sigma\xi\ge0.
}
\]

Then

\[
\boxed{
\nu|G|^2
\le
s_3-b-\delta_{align}.
}
\]

## 3. Universal local H1 production tradeoff

The vorticity-gradient representation of H1 production has density

\[
\boxed{
n_{H1}
=\frac12\Sigma:(G^TG-GG^T).
}
\]

Böttcher–Wenzel gives

\[
|G^TG-GG^T|
\le\sqrt2|G|^2.
\]

Therefore

\[
\boxed{
(n_{H1})^+
\le
\frac{|\Sigma|}{\sqrt2}|G|^2
\le
\frac{|\Sigma|}{\sqrt2\nu}
\left(s_3-b-\delta_{align}\right).
}
\]

This part never used `G xi = 0` and is unchanged by the transpose audit.

In particular, if

\[
b\to s_3,
\qquad
\delta_{align}\to0,
\]

then

\[
(n_{H1})^+\to0
\]

at the same record point.

## 4. Correct exact-alignment sharpening

Assume

\[
\xi=e_3
\]

is exactly the largest-strain eigenvector and write

\[
\Sigma=\operatorname{diag}(s_1,s_2,s_3),
\qquad
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

The correct maximum constraint is

\[
G^Te_3=0.
\]

Thus the third row of `G` vanishes. Since `tr G=div Omega=0`,

\[
\boxed{
G=
\begin{pmatrix}
a&c_{12}&c_{13}\\
c_{21}&-a&c_{23}\\
0&0&0
\end{pmatrix}.
}
\]

Direct calculation gives

\[
\boxed{
\begin{aligned}
2n_{H1}
={}&(s_2-s_1)c_{12}^2
+(s_3-s_1)c_{13}^2\\
&+(s_1-s_2)c_{21}^2
+(s_3-s_2)c_{23}^2.
\end{aligned}
}
\]

The positive coefficients are `s2-s1`, `s3-s1`, and `s3-s2`. Hence

\[
\boxed{
(n_{H1})^+
\le
\frac12(s_3-s_1)|G|^2.
}
\]

Using exact alignment in the record-growth inequality,

\[
\nu|G|^2\le s_3-b,
\]

we obtain

\[
\boxed{
(n_{H1})^+
\le
\frac{s_3-s_1}{2\nu}(s_3-b).
}
\]

## 5. Correct positive-middle spectral parameter

Write

\[
(s_1,s_2,s_3)
=(-2m,m-d,m+d),
\qquad
x=d/m\in[0,1].
\]

Then

\[
s_3-s_1=m(3+x),
\qquad
s_3=m(1+x).
\]

Therefore

\[
\boxed{
(n_{H1})^+
\le
\frac{3+x}{2(1+x)}
\frac{s_3(s_3-b)}{\nu}.
}
\]

At the middle-zero endpoint `x=1`,

\[
\boxed{
(n_{H1})^+
\le
\frac{s_3(s_3-b)}{\nu}.
}
\]

The earlier factor `1/2` at `x=1` and the associated special `x>3/5` record-point suppression are withdrawn.

The robust conclusion is instead spectral-independent in its main feature: efficient record growth `b -> s3` still forces same-point H1 production to vanish.

## 6. Smooth branch routing

### R1 — efficient record amplification

If

\[
s_3-b-\delta_{align}\ll1,
\]

then

\[
(n_{H1})^+\ll1.
\]

A globally significant `P_V` production packet must then sit away from the record point, creating a spatial-overlap/turnover obligation.

### R2 — strong local P_V production at the record point

If `(n_H1)^+` is order one, then

\[
s_3-b-\delta_{align}
\]

is order one as well, and the record core pays a definite vorticity-gradient diffusion cost. This feeds the derivative/H channel.

### R3 — extensional misalignment

If `delta_align` is not small, vorticity is not aligned with the strongest extensional strain axis. This feeds the projective/covariance/turnover deficit.

Thus the record maximum cannot simultaneously be

- maximally efficient for vorticity amplification;
- diffusion-light;
- and a strong local H1 nonnormality producer.

## 7. Dependency audit

The transpose correction affects only arguments that used the stronger aligned matrix form from the old Sections 4–5.

The following later ingredients remain valid because they use only the universal record-growth inequality or independent global identities:

- `b + nu |G|^2 <= xi^T Sigma xi`;
- the universal Böttcher–Wenzel record-point tradeoff;
- record-point scalar Taylor mass floors for `g=xi dot Omega`, since `grad g=G^T xi=0` is exactly the corrected condition;
- the smooth frequency corridor;
- the compatible projective-speed bound based on global `Q` and `Z`;
- the moving-ball variance closure;
- positive-middle transverse ribbon geometry;
- the anti-ribbon projective-speed time comparison.

Any note that invokes the old statement that only one positive H1 matrix coefficient survives at exact alignment must be treated as superseded by this file.

Status: **TRANSPOSE ERROR CORRECTED. THE UNIVERSAL SMOOTH RECORD-GROWTH/H1 TRADEOFF SURVIVES; THE FORMER MIDDLE-ZERO-SPECIFIC SHARPENING IS WITHDRAWN. THE CURRENT PURE-P_V MOVING-BALL / ANTI-RIBBON S-CLOSURE DOES NOT DEPEND ON THE WITHDRAWN SHARPENING.**