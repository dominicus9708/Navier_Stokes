# Transverse Uncertainty Gap for Near-Saturated P_V Covariance — 2026-08-20

Overall status: **QUANTITATIVE H/T ROUTING FOR FIXED-AXIS NEAR SATURATION — GLOBAL REGULARITY NOT PROVED.**

This note combines the `7/9` H1 covariance cap with a two-dimensional uncertainty inequality. It shows that a strain field cannot be simultaneously transversely tight, derivative-controlled, and arbitrarily close to covariance saturation about a fixed axis.

---

## 1. A matrix-valued transverse uncertainty inequality

Fix a unit vector `n` and let

\[
x_\perp=P_{n^\perp}(x-X)
\]

relative to any center `X`. For a matrix field `F in H^1(R^3) cap L^2(R^3)` define

\[
E_F=\|F\|_2^2,
\]

\[
M_{\perp,F}=\int |x_\perp|^2|F|_F^2dx,
\]

\[
G_{\perp,F}=\int|\nabla_\perp F|_F^2dx.
\]

Integration by parts in the two transverse dimensions gives

\[
2E_F
=-2\int x_\perp\cdot(F:\nabla_\perp F)dx.
\]

Cauchy--Schwarz therefore yields

\[
\boxed{
E_F^2\le M_{\perp,F}G_{\perp,F}.
}
\]

Define the transverse rms radius

\[
R_{\perp,F}^2=M_{\perp,F}/E_F.
\]

Then

\[
\boxed{
G_{\perp,F}\ge\frac{E_F}{R_{\perp,F}^2}.
}
\]

This is the two-dimensional Heisenberg/Poincare lower bound in the transverse plane and is componentwise valid for matrix fields.

---

## 2. Integrated covariance saturation defect

For the strain field `S`, let

\[
P_S=\|\nabla S\|_2^2.
\]

For a fixed axis `n`, define the palinstrophy-weighted combined covariance defect

\[
\overline\varepsilon_n
=
\frac1{P_S}
\int |\nabla S|^2
\left(\frac79-n^T\overline C(x)n\right)dx.
\]

The pointwise defect splitting from the previous note implies

\[
|\nabla S|^2
\left(\frac79-n^T\overline Cn\right)
\ge
\frac13\left(|\nabla S|^2-|\partial_nS|^2\right).
\]

Hence

\[
\boxed{
\overline\varepsilon_n
\ge
\frac{\|\nabla_\perp S\|_2^2}{3P_S}.
}
\]

Applying the transverse uncertainty inequality with `F=S` gives

\[
\boxed{
\overline\varepsilon_n
\ge
\frac{\|S\|_2^2}
{3R_{\perp,S}^2\|\nabla S\|_2^2}.
}
\]

Equivalently,

\[
\boxed{
R_{\perp,S}^2\frac{\|\nabla S\|_2^2}{\|S\|_2^2}
\ge
\frac1{3\overline\varepsilon_n}.
}
\]

---

## 3. Immediate trichotomy

If the covariance approaches the `7/9` cap,

\[
\overline\varepsilon_n\to0,
\]

then at least one of the following must happen:

1. `R_perp,S -> infinity`: transverse spatial non-tightness / transport (`T`);
2. `||grad S||_2^2 / ||S||_2^2 -> infinity`: derivative concentration (`H`);
3. the fixed-axis description fails because the relevant compressive axis rotates by order one across the core, which is a projective/eigenframe reorganization channel already measured by derivative-gap terms.

Thus for a fixed coherent axis,

\[
\boxed{
\text{tightness} + \text{derivative control}
\Longrightarrow
\overline\varepsilon_n\ge\varepsilon_0>0.
}
\]

This turns the exact-saturation rigidity into a quantitative positive gap.

---

## 4. Localized core version

For a cutoff `chi` supported in a bounded parent ball, set

\[
F=\chi S.
\]

Then

\[
\nabla_\perp F
=\chi\nabla_\perp S
+(\nabla_\perp\chi)S,
\]

so

\[
\|\nabla_\perp F\|_2^2
\le
2\int\chi^2|\nabla_\perp S|^2
+2\int|\nabla_\perp\chi|^2|S|^2.
\]

The uncertainty lower bound applied to `F` therefore implies

\[
\frac{\|\chi S\|_2^2}{R_{\perp,\chi S}^2}
\lesssim
\int\chi^2|\nabla_\perp S|^2
+
\int|\nabla\chi|^2|S|^2.
\]

The second term is a shell/interface contribution. On a tight recurrent core it can be made subdominant by taking a sufficiently large fixed normalized parent radius; if it cannot, that is precisely a bounded-radius turnover/non-tightness event `T`.

Hence the global fixed-axis inequality has a local-core analogue modulo the already identified shell turnover channel.

---

## 5. Axis coherence

In the positive-middle-strain region the compressive eigenvalue is simple. The derivative eigenvector formula gives

\[
|\nabla n|^2
\lesssim
\frac{
\sum_k\operatorname{dist}(\partial_kS,\mathcal L_n)^2
}{\operatorname{gap}_-^2}.
\]

Near covariance saturation, the numerator is bounded by the previous rigidity estimate by `O(epsilon |grad S|^2)`. Thus, on a core with a uniform normalized compressive spectral gap, axis bending is also `O(sqrt(epsilon))` in the corresponding weighted norm.

Consequently, if the axis cannot be replaced by a nearly constant axis on the tight core, that failure itself is a derivative/projective cost rather than a free escape from the transverse uncertainty bound.

---

## 6. Consequence for the P_V H1 endgame

A recurrent `P_V` orbit must make

\[
-\langle R_{VI},-\Delta S\rangle
\]

large enough to pay scale damping and viscosity in the normalized H1 ledger. The most efficient way is to push the combined covariance toward the compressive `7/9` cap. The present inequality shows that this efficient regime cannot persist in a bounded-radius, derivative-controlled, coherent-axis core with arbitrarily small defect.

Therefore repeated near-maximal H1 projective replenishment routes quantitatively to

\[
\boxed{H\lor T\lor\text{axis/projective reorganization}.}
\]

What remains is the non-saturated covariance regime, where the defect is bounded below. There the next task is to turn the fixed defect into a strict loss in the maximum possible H1 replenishment rate and compare that loss against the fixed first-hitting scale-damping cost.

Status: **TIGHT + DERIVATIVE-CONTROLLED + COHERENT-AXIS CORES HAVE A POSITIVE GAP BELOW THE 7/9 H1 COVARIANCE CAP. APPROACHING THE CAP FORCES TRANSVERSE NON-TIGHTNESS, DERIVATIVE CONCENTRATION, OR AXIS REORGANIZATION.**