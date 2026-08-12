# Moving control-volume energy budget

Status: **DERIVED MOVING-CONTROL IDENTITY + COMPUTATIONAL CHECK**

Checks passed: **7/7**

## Exact consequence

For a material cell, the boundary velocity equals the local fluid velocity.
Therefore the relative advective kinetic-energy flux is exactly zero.
Pressure work, viscous boundary transport, and interior viscous dissipation remain.

## Asymmetric two-seed rigid-sphere check

Center velocity: `[1.4715177646857693, 0.0, 4.0]`.

At `r=1`:
- N=64 fixed advective flux `-9.74417772189`, rigid co-moving `-8.6109552437`;
- N=80 fixed advective flux `-9.97261351879`, rigid co-moving `-8.90054650461`.

At `r=2`, the rigid co-moving relative flux changes sign while the fixed-sphere flux remains negative:
- N=64 fixed `-1.32912272026`, rigid co-moving `0.541586795202`;
- N=80 fixed `-1.39146242865`, rigid co-moving `0.543880051331`.

Thus a moving rigid sphere removes pure translation but still permits relative crossing. Only the deforming material cell removes advective crossing exactly.

## Claim boundary

The cancellation of relative material advection is exact Reynolds transport. The asymmetric sign comparisons are numerical audits on a large decay window, not a global regularity theorem.
