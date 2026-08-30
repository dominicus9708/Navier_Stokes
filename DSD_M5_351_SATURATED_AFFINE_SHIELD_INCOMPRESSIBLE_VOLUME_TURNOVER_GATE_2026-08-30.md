# DSD M5-351 — Saturated Affine Shield / Incompressible Material-Volume Turnover Gate

Date: 2026-08-30

Status: **FORMATION-AXIOM MATERIAL-LINEAGE REDUCTION / SATURATED AFFINE SHIELD SHRINKS BY A FIXED VOLUME FACTOR PER FIRST-HITTING GENERATION / INCOMPRESSIBILITY FORCES FIXED-FRACTION MATERIAL TURNOVER UNLESS AFFINE OCCUPANCY/SHAPE DEGENERATES / GLOBAL REGULARITY UNPROVED.**

## 1. First-hitting scale ratio

Let the first-hitting vorticity amplitude increase geometrically:

\[
\boxed{W_{j+1}=qW_j,\qquad q>1.}
\]

Define the natural length

\[
r_j:=W_j^{-1/2}.
\]

Then

\[
\boxed{
r_{j+1}=q^{-1/2}r_j.
}
\]

## 2. Saturated affine-shield radius

The finite-energy/Morrey saturated affine benchmark derived in M5-317--320 has physical radius

\[
\boxed{d_j\asymp r_j^{4/5}.}
\]

Therefore

\[
\boxed{
\frac{d_{j+1}}{d_j}=q^{-2/5}
}
\]

up to the fixed comparability constants defining the saturated corridor.

The corresponding geometric volume scales as

\[
V_j\asymp d_j^3\asymp r_j^{12/5}.
\]

Hence

\[
\boxed{
\frac{V_{j+1}}{V_j}=q^{-6/5}.
}
\]

## 3. Material volume cannot shrink

Let `Phi_{j->j+1}` be the incompressible Lagrangian flow map from stage `j` to stage `j+1`.

For every measurable material set `A`,

\[
\boxed{
|\Phi_{j\to j+1}(A)|=|A|.
}
\]

Thus a coherent material population occupying a fixed positive fraction of the stage-`j` affine shield cannot itself contract by the factor `q^{-6/5}`.

## 4. Occupied affine material set

Assume the saturated affine core contains a material population `A_j` with fixed occupancy

\[
|A_j|\ge\theta_-V_j,
\qquad \theta_->0.
\]

Assume the next affine shield has total volume at most

\[
|B_{j+1}^{aff}|\le\theta_+V_{j+1}
\]

with fixed `theta_+`.

The amount of old material that can remain inside the next affine shield satisfies

\[
|\Phi(A_j)\cap B_{j+1}^{aff}|
\le |B_{j+1}^{aff}|
\le \theta_+q^{-6/5}V_j.
\]

Therefore the retained fraction of `A_j` is at most

\[
\boxed{
\operatorname{Ret}_j
\le
\frac{\theta_+}{\theta_-}q^{-6/5}.
}
\]

On the comparable-occupancy corridor `theta_+/theta_- ~ 1`, this is a strict fixed number below one.

## 5. Canonical fixed-fraction turnover

In the ideal equal-occupancy benchmark,

\[
\boxed{
\operatorname{Ret}_j\le q^{-6/5},
\qquad
\operatorname{Turn}_j\ge1-q^{-6/5}.
}
\]

For the repository's standard `q=2`,

\[
2^{-6/5}\approx0.4353,
\]

so

\[
\boxed{
\operatorname{Turn}_j\gtrsim0.5647.
}
\]

Thus more than half of the coherent affine material population must be replaced/exported at every generation in the ideal saturated benchmark.

## 6. Formation-axiom interpretation

The key distinction is between

- **state shrinkage**: the geometric affine-support radius decreases with the new natural scale;
- **material shrinkage**: impossible under incompressible transport.

Therefore the state can follow the saturated radius only through structural re-formation:

\[
\boxed{
\text{saturated affine state contraction}
\Longrightarrow
\text{material export/replacement}.
}
\]

This is exactly a `T_dynamic` event, not a new affine terminal leaf.

## 7. Exhaustive alternatives

The conclusion can fail only if at least one of the corridor hypotheses fails:

### A. Occupancy degenerates

\[
\theta_j\to0.
\]

Then the affine region carries vanishing material occupancy and joins the massless/derivative microstructure `H_micro` branch.

### B. Shape degenerates strongly

The affine set ceases to be comparable to a three-dimensional ball/ellipsoid with bounded condition number.

This creates a ribbon/sheet/tube geometry and is routed to the existing projective/anisotropic `H/T` shape ledgers.

### C. Shield does not contract at the saturated rate

If the old material population retains volume `~V_j` while the affine gradient grows to the next first-hitting scale, the affine kinetic-energy lower bound exceeds the finite-energy/Morrey capacity that produced `d_j~r_j^(4/5)`.

Thus this exits the saturated finite-energy corridor.

### D. Fixed-fraction turnover

The generic remaining case is

\[
\boxed{T_{mat/repl}.}
\]

## 8. Relation to exact affine anti-model

M5-350 showed that a time-dependent dual-hyperbolic affine NSE flow is locally exact.

That model evades the present argument because it occupies all of `R^3` and has infinite energy; there is no shrinking finite-energy shield to follow.

Once the affine model is embedded in a finite-energy shrinking region, incompressibility forces the fixed-fraction material replacement quantified above.

Thus finite-energy ancestry is exactly the ingredient that destroys persistent material self-similarity of the affine anti-model.

## 9. Consequence for the master tree

On the energy-bearing saturated corridor,

\[
\boxed{
C_{dual-hyp}^{energy}
\Longrightarrow
T_{dynamic}
\ \lor\
H_{micro/shape}.
}
\]

Hence the dual-hyperbolic affine core need not remain an independent terminal branch if the comparability/occupancy hypotheses are maintained.

This does **not** yet close `T_dynamic`; previous audits showed that fixed-fraction turnover can still have geometrically summable physical energy cost.

## 10. Firewall

Do not infer that a material ellipsoid must remain spherical. It may deform anisotropically while preserving volume.

The argument uses only the fact that a fixed-volume material population cannot fit inside a next-stage three-dimensional affine region whose available volume has dropped by a fixed factor, unless occupancy/shape assumptions fail.

Therefore severe anisotropic escape must be recorded separately rather than silently treated as turnover.

## 11. Audit verdict

### PROVED

- saturated shield volume ratio `q^{-6/5}`;
- incompressibility preserves coherent material volume;
- comparable occupied affine shields force fixed-fraction export/replacement;
- energy-bearing affine persistence is routed to dynamic turnover unless occupancy/shape degenerates.

### OPEN

- exclusion of repeated fixed-fraction turnover despite summable physical energy cost;
- anisotropic/massless microstructure branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]