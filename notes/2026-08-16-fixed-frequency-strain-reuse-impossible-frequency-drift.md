# Fixed-frequency strain reuse is impossible: nested logarithmic amplification forces frequency drift

Date: 2026-08-16

Status: **DERIVED PHYSICAL-FREQUENCY EVACUATION FOR SHRINKING NESTED EPISODES / CRITICAL-SATURATION MESOSCOPIC FREQUENCY FLOOR DERIVED / FREQUENCY DRIFT ALONE DOES NOT YET CONTRADICT FINITE DISSIPATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Why nested time intervals are not enough

The current clean-to-crossing estimate forces a logarithmic productive/affine strain action, schematically

\[
A_j\gtrsim c\log R_j,
\qquad R_j\to\infty.
\]

For nearby first-hitting levels, the physical time intervals are nested, so the same strain event can in principle be counted in many episodewise integrals.

The question is whether a fixed physical scale can be reused indefinitely in this way.

## 2. Littlewood--Paley band estimate

Let

\[
S_k=\Delta_k S
\]

be a standard physical dyadic Littlewood--Paley band with frequency `|xi| ~ 2^k`.

Bernstein gives

\[
\boxed{
\|S_k(t)\|_\infty
\le C 2^{3k/2}\|S_k(t)\|_2.
}
\]

For a physical time interval `I`, Cauchy--Schwarz in time gives

\[
\boxed{
\int_I\|S_k(t)\|_\infty dt
\le
C2^{3k/2}|I|^{1/2}
\left(
\int_I\|S_k(t)\|_2^2dt
\right)^{1/2}.
}
\]

Because

\[
\|S\|_2^2=\frac12\|\omega\|_2^2,
\]

the band dissipation is bounded by the finite global enstrophy-time budget.

## 3. Every fixed physical frequency evacuates the singular tail

Let `I_j` be any nested/shrinking family with

\[
I_j\subset(t_j,T^*),
\qquad
t_j\uparrow T^*,
\qquad
|I_j|\to0.
\]

For each fixed `k`, absolute continuity of the finite dissipation measure gives

\[
\int_{I_j}\|S_k\|_2^2dt\to0.
\]

Therefore

\[
\boxed{
\int_{I_j}\|S_k\|_\infty dt\to0
\qquad\text{for every fixed }k.
}
\]

The same holds for any fixed finite collection of physical frequency bands.

Consequently a required action

\[
A_j\gtrsim c\log R_j\to\infty
\]

cannot be supplied by repeatedly reusing a fixed macroscopic or fixed mesoscopic strain field.

The active physical frequency must drift to infinity.

## 4. Quantitative low-frequency ceiling

Let

\[
S_{\le K}=P_{\le K}S
\]

where `K` is a physical frequency cutoff. Summing Bernstein by Cauchy--Schwarz over dyadic bands gives

\[
\boxed{
\int_I\|S_{\le K}(t)\|_\infty dt
\le
C K^{3/2}|I|^{1/2}
\left(
\int_I\|S(t)\|_2^2dt
\right)^{1/2}.
}
\]

Write

\[
D(I)=\int_I\|S(t)\|_2^2dt.
\]

If a strain action `A` is to be supplied entirely by frequencies at most `K`, then necessarily

\[
\boxed{
K
\gtrsim
\left(
\frac{A}{\sqrt{|I|D(I)}}
\right)^{2/3}.
}
\]

This is a quantitative frequency floor, not only a qualitative drift statement.

## 5. Critical-saturation evaluation

On the minimal recent-source branch, let the physical coherent-core radius be

\[
\ell=\frac{R}{\sqrt W}.
\]

The source horizon is one core-parabolic time up to fixed/slow factors:

\[
|I|\asymp\ell^2
=\frac{R^2}{W}.
\]

Critical terminal occupancy gives the enstrophy-time scale

\[
D(I)\asymp\frac{R^3}{\sqrt W}
\]

up to the critical-saturation factor `Xi=O(1)` and harmless viscosity constants.

For the logarithmic amplification branch

\[
A\gtrsim c\log R,
\]

the low-frequency ceiling yields

\[
\boxed{
K_{\min}
\gtrsim
W^{1/2}R^{-5/3}(\log R)^{2/3}.
}
\]

The coherent-core frequency is

\[
k_c=\ell^{-1}=\frac{\sqrt W}{R}.
\]

Hence

\[
\boxed{
\frac{K_{\min}}{k_c}
\gtrsim
\left(\frac{\log R}{R}\right)^{2/3}.
}
\]

Equivalently, a strain field that supplies the critical logarithmic action cannot remain on arbitrarily larger physical scales. Its wavelength must obey

\[
\boxed{
L_{\rm strain}
\lesssim
\ell
\left(\frac{R}{\log R}\right)^{2/3}.
}
\]

Thus the repeated amplifier is forced into a mesoscopic window whose physical frequency diverges with the singular sequence.

## 6. Upper end of the amplifier window

The Gaussian mean strain at core scale `ell` is itself a heat/Gaussian low-pass quantity. Frequencies much larger than `ell^-1` are exponentially suppressed in the affine mean. If they nevertheless dominate, the required amplitude is correspondingly large and routes to the existing high-frequency / derivative branch.

Therefore on the bounded-derivative branch the reusable affine amplifier is confined schematically to

\[
\boxed{
K_{\min}
\lesssim |\xi|
\lesssim
C\ell^{-1}.
}
\]

The logarithmic width of this mesoscopic frequency window is

\[
\asymp\frac23\log\frac{R}{\log R}.
\]

It grows, but every fixed physical band eventually leaves the active window behind.

## 7. What this closes and what it does not

This proves that nested time intervals do **not** permit literal reuse of one fixed physical strain field through infinitely many coherent crossings.

A surviving nested cascade must execute a frequency cascade in its productive strain:

\[
\boxed{
\text{nested logarithmic strain action}
\Longrightarrow
\text{physical frequency drift to infinity}.
}
\]

However, this is not yet a contradiction. At higher frequencies the dissipation cost per episode can decrease, and the adversarial super-separated power families can still make the scalar band-energy costs summable.

The next target is to combine this mandatory frequency drift with the exact Gaussian dyadic variance partition. The desired conclusion would be that every genuinely new productive scale occupies a new positive dyadic increment, while attempts to skip increments force high-frequency derivative concentration.

Status: **FIXED-FREQUENCY REUSE REMOVED / CRITICAL AMPLIFIER FORCED INTO A MOVING MESOSCOPIC FREQUENCY WINDOW / CROSS-SCALE BAND PACKING REMAINS THE FINAL ISSUE.**
