# DSD M19-164 — The five-quarter anisotropy gap gives an explicit forced-contraction criterion, but scalar-density-to-strain conversion prevents unconditional decay

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / SOURCE PRICING FOR THE 5/4 TENSOR GAP / UNCONDITIONAL ANISOTROPY DECAY NOT PROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-163 derived

\[
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
+
\frac54\|Q\|_2^2
=
I_G+I_{\rho S}+I_{SQ}+I_F,
\]

with

\[
\begin{aligned}
I_G&=-2\nu\int Q:\mathcal G^\circ,\\
I_{\rho S}&=\frac23\int\rho\,Q:S,\\
I_{SQ}&=\int Q:(SQ+QS)^\circ,\\
I_F&=\int Q:\mathcal F^\circ.
\end{aligned}
\]

The present module estimates these terms against the `5/4` gap and identifies the exact obstruction to unconditional anisotropy decay.

## 2. Gradient-anisotropy source

By Cauchy--Schwarz,

\[
|I_G|
\le
2\nu\|Q\|_2\|\mathcal G^\circ\|_2.
\]

For every `epsilon>0`,

\[
\boxed{
|I_G|
\le
\varepsilon\|Q\|_2^2
+
\frac{\nu^2}{\varepsilon}
\|\mathcal G^\circ\|_2^2.
}
\]

This term therefore behaves as an external tensor forcing unless additional control relates `G^circ` to `grad Q`.

No such sign relation is presently certified.

## 3. Scalar-density to strain forcing

Similarly,

\[
|I_{\rho S}|
\le
\frac23
\|Q\|_2
\|\rho S\|_2.
\]

Hence

\[
\boxed{
|I_{\rho S}|
\le
\varepsilon\|Q\|_2^2
+
\frac{1}{9\varepsilon}
\|\rho S\|_2^2
}
\]

up to the harmless optimization of the numerical Young constant.

This term is structurally important because it is present even when

\[
Q=0
\]

at one instant: the equation contains the source

\[
\boxed{
\frac{2\rho}{3}S.
}
\]

Thus a scalar hard-mode density in a nonzero strain field immediately generates collective anisotropy.

Permanent firewall:

\[
\boxed{
Q=0\text{ instantaneously}
\not\Rightarrow
Q\equiv0.
}
\]

## 4. Strain acting on existing anisotropy

Since pairing with `Q` removes the trace correction,

\[
I_{SQ}
=
2\int\operatorname{tr}(SQ^2).
\]

Therefore

\[
\boxed{
|I_{SQ}|
\le
2\|S\|_\infty\|Q\|_2^2.
}
\]

This is the only source among the four that directly shifts the linear damping coefficient without an additive forcing norm.

## 5. Nonlocal forcing tensor

The final source satisfies

\[
|I_F|
\le
\|Q\|_2\|\mathcal F^\circ\|_2,
\]

hence

\[
\boxed{
|I_F|
\le
\varepsilon\|Q\|_2^2
+
\frac{1}{4\varepsilon}
\|\mathcal F^\circ\|_2^2.
}
\]

By M19-160 the tensor `F` depends on `grad Omega` through Biot--Savart-type expressions; its far-tail part is form-small but its compact-core part need not be small.

## 6. Forced anisotropy inequality

Combining the four estimates gives, for every `epsilon>0`,

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
+
\left(
\frac54
-2\|S\|_\infty
-3\varepsilon
\right)
\|Q\|_2^2
\le{}&
C_\varepsilon
\Bigl[
\nu^2\|\mathcal G^\circ\|_2^2\\
&+\|\rho S\|_2^2
+\|\mathcal F^\circ\|_2^2
\Bigr].
\end{aligned}
}
\]

The precise harmless constants can be optimized, but the structural decomposition is exact.

## 7. Conditional contraction criterion

If a subcorridor satisfies

\[
\boxed{
2\|S(s)\|_\infty
+3\varepsilon
\le
\frac54-\delta_A
}
\]

for some `delta_A>0`, and the additive anisotropy forcing obeys

\[
\boxed{
C_\varepsilon
\left[
\nu^2\|\mathcal G^\circ\|_2^2
+
\|\rho S\|_2^2
+
\|\mathcal F^\circ\|_2^2
\right]
\le
\theta_A\|Q\|_2^2
}
\]

with

\[
\theta_A<\delta_A,
\]

then

\[
\boxed{
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
+
(\delta_A-\theta_A)\|Q\|_2^2
\le0.
}
\]

A nonzero recurrent/relative-periodic collective anisotropy is impossible on that subcorridor.

Thus the `5/4` gap produces a real conditional anisotropy-rigidity theorem.

## 8. Why the present hard corridor does not automatically satisfy it

The current M19 compact corridor gives boundedness of

\[
\|S\|_\infty,
\quad
\|\mathcal G^\circ\|_2,
\quad
\|\rho S\|_2,
\quad
\|\mathcal F^\circ\|_2,
\]

but not the required smallness relative to `5/4`.

In particular, the source

\[
\rho S
\]

need not become small merely because `Q` is small.

Therefore the inequality is a conditional gate, not an unconditional closure.

## 9. Exact obstruction restated

The hard-mode collective anisotropy is not a free neutral quantity. It is a forced response of the tensor equation

\[
\boxed{
\mathcal L_QQ
=
\frac{2\rho}{3}S
-2\nu\mathcal G^\circ
+
\mathcal F^\circ
+
\text{strain-on-Q},
}
\]

where `L_Q` has the strong bare `5/4` gap.

Hence persistent many-channel compensation requires a **persistent forced anisotropy balance**.

This is more restrictive than the scalar quarter-gap balance, but current scalar corridor bounds do not forbid it.

## 10. Relation to M19-159 kernel count

If a nonsymmetry kernel exists, M19-159 forces an additional superthreshold channel.
M19-162 then forces collective `Q`, and M19-163--164 show that this `Q` must solve the forced `5/4` balance.

Therefore

\[
\boxed{
K_{nsym}\ne0
\Longrightarrow
\text{a compact-core forced-anisotropy cycle overcoming the }5/4\text{ gap}.
}
\]

This is now a sharper characterization of the kernel obstruction.

## 11. Audit verdict

### Proved

1. Explicit source-by-source estimates for the collective anisotropy equation.
2. A conditional contraction criterion based on the `5/4` gap.
3. Identification of `rho S` as the main structural forcing that prevents unconditional decay.

### Not proved

1. Required smallness of the forcing terms on the full moderate hard corridor.
2. Uniform kernel rigidity.
3. Global regularity.

## 12. Next target

A direct smallness proof is now unlikely on the full finite-amplitude hard core.

M19-165 should instead exploit the fact that `rho S` is the leading anisotropy source and ask whether the **periodic forced response is uniquely determined by the scalar density `rho` and exact symmetry block**.

If so, an additional nonsymmetry compensation channel would have to alter the forced response in a way detected by the scattering observables, potentially reducing kernel rigidity to injectivity of a tensor response operator rather than to a smallness estimate.
