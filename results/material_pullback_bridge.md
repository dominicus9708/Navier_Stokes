# Material pullback / boundary-geometry bridge

Status: **DERIVED PULLBACK / BOUNDARY-GEOMETRY BRIDGE + COMPUTATIONAL CHECK**

Checks passed: **7/7**

## Exact split

- Bulk material measure: `J=det F=1`, so volume aggregation pulls back to the fixed initial ball without a changing Jacobian.
- Boundary oriented area: `n dS = F^{-T} n0 dS0`.
- Pressure work and viscous boundary transport therefore retain an explicit deformation-geometry coupling through `F^{-T}`.

## Frozen Gaussian anchor

For `F=diag(exp(2 c tau),exp(2 c tau),exp(-4 c tau))`, `c=e^(-1/4)`:

- `det F=1` exactly;
- `||F^{-T}||_op=exp(4 c tau)` for `tau>=0`;
- minimum oriented-area factor is `exp(-2 c tau)`;
- boundary anisotropy ratio is `exp(6 c tau)`.

Sample values:

- tau=0.00: max=1, min=1, ratio=1
- tau=0.05: max=1.16855, min=0.925075, ratio=1.26319
- tau=0.10: max=1.3655, min=0.855764, ratio=1.59565
- tau=0.20: max=1.86459, min=0.732333, ratio=2.5461
- tau=0.50: max=4.74742, min=0.458956, ratio=10.344

## Interpretation

Incompressibility freezes the material bulk Jacobian but not boundary geometry. The remaining pressure and viscous boundary interactions are weighted by `F^{-T}`. Compression of one material direction can therefore amplify the oriented-area factor even while total volume is exactly preserved. This is a structural coupling channel, not a blow-up theorem.

## Claim boundary

Nanson pullback and `J=1` are exact smooth-flow identities. The exponential formulas are only for the frozen local Gaussian anchor and do not represent a time-solved Navier-Stokes trajectory.
