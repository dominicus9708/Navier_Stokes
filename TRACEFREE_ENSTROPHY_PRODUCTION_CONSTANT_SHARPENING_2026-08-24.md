# Trace-Free Enstrophy Production Constant Sharpening — 2026-08-24

Status: **UNCONDITIONAL CONSTANT IMPROVEMENT INSIDE THE SMOOTH ANCIENT CLASS / GLOBAL REGULARITY NOT PROVED.**

This note sharpens the universal vortex-stretching estimate used in the ancient Gronwall rigidity gate.

The previous estimate

\[
|\mathcal P|
\le
\frac1{\sqrt2}
\|\Omega\|_\infty
\|\Omega\|_2^2
\]

used only the global `L2` strain-vorticity identity and Hölder. It did not use the fact that the strain tensor is pointwise symmetric and trace free.

That structure gives a strictly smaller universal coefficient.

---

## 1. Sharp pointwise largest-eigenvalue bound for trace-free strain

Let

\[
S=S^T,
\qquad
\operatorname{tr}S=0,
\]

with ordered eigenvalues

\[
s_1\le s_2\le s_3.
\]

Since

\[
s_1+s_2=-s_3,
\]

Cauchy gives

\[
s_1^2+s_2^2
\ge
\frac12(s_1+s_2)^2
=
\frac12s_3^2.
\]

Therefore

\[
|S|_F^2
=s_1^2+s_2^2+s_3^2
\ge
\frac32s_3^2.
\]

Hence

\[
\boxed{
 s_3
\le
\sqrt{\frac23}|S|_F.
}
\]

Equality occurs only when

\[
\boxed{s_1=s_2=-\frac12s_3,}
\]

i.e. the two compressive eigenvalues coincide.

---

## 2. Pointwise vortex-stretching bound

For vorticity `Omega`,

\[
\Omega^TS\Omega
\le
s_3|\Omega|^2.
\]

Thus

\[
\boxed{
\Omega^TS\Omega
\le
\sqrt{\frac23}|S||\Omega|^2.
}
\]

This is an upper bound, so negative vortex-stretching regions only improve it.

---

## 3. Whole-space enstrophy production

Let

\[
M:=\|\Omega\|_\infty,
\qquad
Z:=\|\Omega\|_2^2.
\]

For smooth decaying divergence-free velocity,

\[
\boxed{
\|S\|_2^2
=\frac12Z.
}
\]

Also

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2
=MZ^{1/2}.
\]

Therefore

\[
\begin{aligned}
\mathcal P
&:=
\int\Omega^TS\Omega\,dx
\\
&\le
\sqrt{\frac23}
\int |S||\Omega|^2dx
\\
&\le
\sqrt{\frac23}
\|S\|_2\|\Omega\|_4^2
\\
&\le
\sqrt{\frac23}
\frac{Z^{1/2}}{\sqrt2}
MZ^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal P
\le
\frac1{\sqrt3}MZ.
}
\]

Numerically,

\[
\boxed{
\frac1{\sqrt3}
\approx0.5773502692,
}
\]

instead of

\[
\frac1{\sqrt2}
\approx0.7071067812.
\]

This is an unconditional `18.35%` reduction in the production coefficient.

---

## 4. Improved physical ancient logarithmic inequality

The physical ancient enstrophy identity is

\[
\frac12Z'+\nu Q=\mathcal P.
\]

Using the sharpened bound,

\[
\boxed{
Z'
+2\nu Q
\le
\frac2{\sqrt3}MZ.
}
\]

Therefore, wherever `Z>0`,

\[
\boxed{
\frac d{dt}\log Z
\le
\frac2{\sqrt3}M
-2\nu\frac QZ.
}
\]

This replaces the earlier coefficient `sqrt(2)` by

\[
\boxed{
\frac2{\sqrt3}
\approx1.154700538.
}
\]

---

## 5. Improved tail-independent Gronwall criterion

Suppose

\[
Z(t)\le C|t|^{-\alpha},
\qquad
M(t)\le K|t|^{-1}
\]

for sufficiently negative ancient time.

Discarding viscosity first gives

\[
Z(t)
\le
Z(t_0)
\left(
\frac{|t_0|}{|t|}
\right)^{2K/\sqrt3}.
\]

Thus

\[
\boxed{
\frac{2K}{\sqrt3}<\alpha
\Longrightarrow
Z\equiv0.
}
\]

For the restricted first-hitting ancient decay

\[
\alpha=\frac12,
\]

we obtain the improved threshold

\[
\boxed{
K
<
\frac{\sqrt3}{4}
\approx0.4330127019.
}
\]

The former unsharpened threshold was

\[
1/(2\sqrt2)
\approx0.3535533906.
\]

---

## 6. Improved stage-length certificate

With

\[
K=K_I(q)
=
\frac{q^2}{q-1}L_{stage,+}(q),
\]

a sufficient rigidity condition is now

\[
\boxed{
L_{stage,+}(q)
<
\frac{\sqrt3}{4}
\frac{q-1}{q^2}.
}
\]

If `L_stage,+` is frozen only for the benchmark optimization, `q=2` minimizes the geometric factor `q^2/(q-1)` and gives

\[
\boxed{
L_{stage,+}
<
\frac{\sqrt3}{16}
\approx0.1082531755.
}
\]

Using the existing q=2 pure moving-ball benchmark

\[
L_j\le0.7483880874r^2,
\]

this would correspond to

\[
\boxed{
r<0.380326765.}
\]

This numerical substitution is only a benchmark and does not enlarge the already closed pure subcorridor by itself.

---

## 7. Viscously improved version

If the recurrent frequency-ratio tax satisfies

\[
\int_{t_0}^{t}\frac QZds
\ge
c_{log}
\log\frac{|t_0|}{|t|}
-O(1),
\]

then the effective backward exponent is

\[
\frac{2K}{\sqrt3}-2\nu c_{log}.
\]

Hence the improved viscous rigidity certificate is

\[
\boxed{
\frac{2K_I}{\sqrt3}
-2\nu c_{log}
<
\frac12.
}
\]

Equivalently, every nonzero recurrent survivor must satisfy

\[
\boxed{
\frac{2K_I}{\sqrt3}
\ge
\frac12+2\nu c_{log}.
}
\]

This should replace the `sqrt(2) K_I` version in future frontier summaries.

---

## 8. Further positive-middle improvement and its scope

If one knows pointwise that the relevant positive production occurs in the positive-middle sector

\[
s_2\ge0,
\]

then a stronger eigenvalue ratio holds:

\[
\boxed{
 s_3\le\frac1{\sqrt2}|S|.
}
\]

Indeed, for fixed `s3` and `s2>=0`, the smallest possible `|S|` occurs at `s2=0`, `s1=-s3`, giving `|S|=sqrt(2)s3`.

On a domain where this condition holds,

\[
\Omega^TS\Omega
\le
\frac1{\sqrt2}|S||\Omega|^2.
\]

If the **entire positive enstrophy production** could be localized to such a sector without paying an uncontrolled boundary/Betchov-transfer term, one would obtain the stronger whole-space coefficient

\[
\boxed{
\mathcal P\le\frac12MZ.
}
\]

and therefore the threshold

\[
K<\frac12
\]

before viscosity.

However, the repository currently proves positive-middle routing only for repeated source-active cells modulo Betchov/buffer/Hessian/residual exits. It does **not** yet justify replacing the global `1/sqrt(3)` coefficient by `1/2` unconditionally.

Therefore

\[
\boxed{
1/\sqrt3
}
\]

is the rigorous universal coefficient to use now.

---

## 9. Saturation geometry and connection to the audit

The universal `1/sqrt(3)` coefficient is saturated algebraically only when the largest-eigenvalue bound is saturated:

\[
(s_1,s_2,s_3)
\propto
(-1,-1,2),
\]

which lies in the **negative-middle** sector.

By contrast, the Betchov determinant representation of positive global vortex stretching receives its positive determinant contribution from the positive-middle sector.

Thus the exact saturation geometry of the new universal ceiling is already in tension with the recurrent Betchov/positive-middle route.

This suggests a possible future strict improvement below `1/sqrt(3)`, but obtaining it requires a quantitative global localization/segregation argument. It must not be assumed merely from the pointwise spectral observation.

Status: **TRACE-FREE STRAIN GEOMETRY SHARPENS THE UNIVERSAL ENSTROPHY PRODUCTION CEILING TO `P <= M Z / sqrt(3)`. THE VORTICITY-TIGHT ANCIENT GRONWALL THRESHOLD IMPROVES TO `K_I < sqrt(3)/4`, OR WITH RECURRENT VISCOSITY `2 K_I/sqrt(3) - 2 nu c_log < 1/2`. A FURTHER `1/2` PRODUCTION COEFFICIENT IS AVAILABLE ONLY AFTER A GLOBAL POSITIVE-MIDDLE ROUTING LEMMA. GLOBAL REGULARITY REMAINS UNPROVED.**