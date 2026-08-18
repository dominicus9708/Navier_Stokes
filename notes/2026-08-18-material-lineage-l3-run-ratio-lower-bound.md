# Clean material-lineage run ratio forces endpoint L3 growth

Date: 2026-08-18

Status: **DERIVED SCALE-INVARIANT L3 LOWER BOUND FOR AN EMBEDDED SIGNED-COHERENT MATERIAL I-RUN WITH A CLEAN CIRCULATION BUFFER. A LONG FLUX-PRESERVING RUN FROM K0 TO K1 FORCES ||u||_3 >= c K1/K0. THE COMPLEMENT IS BUFFER CANCELLATION OR REACH COLLAPSE. GLOBAL REGULARITY NOT PROVED.**

## 1. Geometry from the material-lineage ceiling

Let a signed-coherent material I-lineage start at natural frequency `K0` with

\[
r_0\asymp K_0^{-1},
\qquad
L_0\asymp K_0^{-1},
\qquad
\Gamma\ge\gamma_0>0.
\]

Suppose it reaches natural frequency `K1>K0` without a viscous flux reset.  Flux and material-volume preservation give

\[
r_1\asymp K_1^{-1}
\]

and

\[
L_1\gtrsim\frac{K_1^2}{K_0^3}.
\]

Let

\[
q=\frac{K_1}{K_0}.
\]

Then

\[
\boxed{
\frac{L_1}{r_1}\gtrsim q^3.
}
\]

Thus one octave of vorticity-frequency amplification multiplies the material tube aspect ratio by approximately `8`.

## 2. L3 lower bound from circulation

Assume a clean tubular annulus on a fixed fraction of the tube length: for `r1 <= rho <= 2r1`, the circulation around the transverse loop remains at least `gamma0/2` in magnitude.

For each loop,

\[
\gamma_0/2
\le
\int_{\partial D_\rho}|u|\,ds.
\]

Hölder on the one-dimensional loop gives

\[
\left(\int_{\partial D_\rho}|u|ds\right)^3
\le
(2\pi\rho)^2
\int_{\partial D_\rho}|u|^3ds.
\]

Hence

\[
\boxed{
\int_{\partial D_\rho}|u|^3ds
\gtrsim
\frac{\Gamma^3}{\rho^2}.
}
\]

Integrating over one fixed-ratio radial annulus and along the tube length yields

\[
\|u\|_3^3
\gtrsim
\Gamma^3L_1\int_{r_1}^{2r_1}\rho^{-2}d\rho
\gtrsim
\Gamma^3\frac{L_1}{r_1}.
\]

Therefore

\[
\boxed{
\|u\|_3^3
\gtrsim
c\Gamma^3q^3
}
\]

and, for `Gamma>=gamma0`, 

\[
\boxed{
\|u\|_3\gtrsim c q.
}
\]

## 3. Complementary branches

The bound can fail only if the clean circulation/tubular geometry fails.

- If circulation is cancelled in the `r1` to `2r1` annulus, the circulation-buffer dichotomy produces a same-scale opposite-signed/projective partner packet.
- If a tubular annulus cannot be embedded on a fixed fraction of the length, this is the reach-collapse / self-approach branch.

Thus the clean material route has the exhaustive local form

\[
\boxed{
\text{long embedded I-run}
\Rightarrow
\|u\|_3\gtrsim K_1/K_0
}
\]

or

\[
\boxed{
\text{same-scale partner / reach concentration}.
}
\]

## 4. Run-count tradeoff

Consider successive material I-runs with frequency ratios

\[
q_j=K_{j+1}/K_j.
\]

The total frequency gain satisfies

\[
\log(K_n/K_0)=\sum_{j=0}^{n-1}\log q_j.
\]

If every clean run occurs at a time when the global endpoint norm is at most `M`, then the L3 lower bound gives

\[
q_j\lesssim M.
\]

Hence

\[
\boxed{
n\gtrsim
\frac{\log(K_n/K_0)}{\log M+O(1)}.
}
\]

Thus bounded or slowly growing `L3` forces many reset/reach events; few exceptional events force at least one large-`q` run and therefore large `L3`.

This is compatible with endpoint regularity: a hypothetical singularity is allowed to drive `L3` to infinity.  The value of the result is the explicit genealogy tradeoff.

## 5. Limitation

No a priori finite bound controls the number of reset/reach events or the endpoint `L3` norm near a hypothetical singular time.  The tradeoff is therefore not yet a contradiction.

Status: **CLEAN I-RUN RATIO q FORCES ||u||_3 >= c q / SMALL L3 FORCES MANY RESET-REACH EVENTS / GLOBAL REGULARITY NOT PROVED.**