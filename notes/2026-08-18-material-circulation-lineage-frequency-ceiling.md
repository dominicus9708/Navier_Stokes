# Material circulation lineage has a K -> K^(3/2) frequency ceiling before reset/reach collapse

Date: 2026-08-18

Status: **DERIVED CONDITIONAL GEOMETRIC CEILING FOR A SIGNED-COHERENT MATERIAL I-LANE TUBE SEGMENT. A FLUX-PRESERVING EMBEDDED LINEAGE CANNOT CARRY NATURAL-SCALE VORTICITY FROM K0 TO ARBITRARILY HIGH K1 WITHOUT EITHER A VISCOUS FLUX RESET OR A TUBULAR-REACH COLLAPSE. GLOBAL REGULARITY NOT PROVED.**

## 1. Natural signed-coherent tube segment

At physical frequency `K0`, take a signed-coherent dangerous tube segment with

\[
r_0\asymp K_0^{-1},\qquad |\omega_0|\asymp K_0^2,
\]

and scale-invariant circulation / vorticity flux

\[
\Gamma\asymp |\omega_0|r_0^2\asymp 1.
\]

Take a natural initial segment length

\[
L_0\asymp K_0^{-1}.
\]

The material segment volume is therefore

\[
V_0\asymp r_0^2L_0\asymp K_0^{-3}.
\]

## 2. I-lane flux and volume preservation

For the inviscid Cauchy contribution

\[
I=F\omega_0,
\]

under the volume-preserving flow map, vorticity flux through material cross-sections is preserved.  Thus along an I-dominated signed-coherent lineage the child flux remains comparable to `Gamma`.

Suppose the same lineage reaches a later natural frequency `K1>K0`, so the dangerous vorticity magnitude is

\[
|\omega_1|\asymp K_1^2.
\]

Flux preservation forces the terminal cross-sectional area

\[
A_1\asymp \Gamma K_1^{-2}.
\]

Material volume preservation gives

\[
A_1L_1\asymp V_0.
\]

Hence

\[
\boxed{
L_1\gtrsim \frac{K_1^2}{K_0^3}.
}
\]

Equivalently, the length multiplies by the vorticity amplification factor `(K1/K0)^2`.

## 3. Circulation-energy lower bound for an embedded tube

Assume the terminal tube admits a non-self-overlapping tubular neighborhood of radius comparable to the core radius `r1~K1^-1` along a fixed fraction of its length.  On each transverse loop in one annulus `c r1 <= rho <= C r1`, circulation is comparable to `Gamma`.

Cauchy--Schwarz on each loop gives

\[
\int_{\partial D_\rho}|u|^2ds
\gtrsim \frac{\Gamma^2}{\rho}.
\]

Integrating over one fixed-ratio radial annulus and along the tube length yields

\[
\boxed{
\|u\|_2^2\gtrsim c\Gamma^2L_1.
}
\]

No logarithmic radial gain is needed for the present ceiling.

If such a tubular neighborhood does not exist, this is precisely the previously typed **reach-collapse / self-approach branch**.

## 4. Frequency ceiling

Since kinetic energy is globally bounded by the initial energy `E0`, and `Gamma>=gamma0>0` on a dangerous signed-coherent lineage,

\[
E_0\gtrsim L_1\gtrsim \frac{K_1^2}{K_0^3}.
\]

Therefore

\[
\boxed{
K_1\lesssim C(E_0,\gamma_0)K_0^{3/2}.
}
\]

Thus one embedded flux-preserving I-lineage cannot jump from `K0` beyond `K0^(3/2)` up to fixed constants.

## 5. Iterated consequence

Let

\[
K_0<K_1<\cdots<K_n
\]

be successive starts/ends of embedded I-runs, where between runs one allows either

1. a viscous Cauchy / flux-reset event, or
2. a reach-collapse / self-approach event.

Every pure I-run satisfies

\[
K_{j+1}\le CK_j^{3/2}.
\]

Writing `x_j=log K_j`,

\[
x_{j+1}\le \frac32x_j+O(1).
\]

Hence to reach `K_n=Kmax -> infinity` from a fixed lower scale requires

\[
\boxed{
n\gtrsim c\log\log K_{\max}-O(1).
}
\]

So every arbitrarily high signed-coherent material lineage must accumulate an unbounded number of **viscous-reset or reach-collapse events**.

## 6. Why this is not yet a contradiction

The number of required exceptional events diverges only logarithmically in `log K`.  Existing physical dissipation / V2 / reset prices may decay with the scale and can still be summable along a super-separated sequence.

Therefore the present result is a genealogy restriction, not a proof of global regularity.

The next target is to prove that each reset/reach event needed by an organized radial stack carries a **scale-critical non-summable charge** (projective, V2, positive-middle-strain, or radial-flux defect), rather than only a decaying physical energy cost.

Status: **FLUX-PRESERVING I-RUN FREQUENCY CEILING K1 <= C K0^(3/2) / ARBITRARILY HIGH LINEAGES REQUIRE >= c log log K RESET-OR-REACH EVENTS / GLOBAL REGULARITY NOT PROVED.**