# DSD–Navier–Stokes first-pass computational summary

Status: **COMPUTATIONAL CHECK / FIRST-PASS BRIDGE**

Checks passed: **12/12**

## Exact / deterministic checks

- PASS — `symbolic_divergence_zero`
- PASS — `symbolic_omega_match`
- PASS — `pressure_source_match`
- PASS — `energy_angular_formula_match`
- PASS — `energy_isotropic_at_sqrt2`
- PASS — `axis_energy_sums`
- PASS — `radial_origin_undefined`
- PASS — `radial_equator_defined_zero`
- PASS — `scale_energy`
- PASS — `scale_enstrophy`
- PASS — `scale_pressure_l2`
- PASS — `aggregate_collision_constructed`

## Two structural shell findings

- At `r=sqrt(2)≈1.41421356237`, total shell energy density is angularly isotropic, while axis-resolved energies remain unequal.
- At `r=sqrt(5/2)≈1.58113883008`, `T_W≈1.417e-31` while `T_E≈0.0988232226533` remains nonzero.

These are information-separation examples, not regularity theorems.

## Typed zero / undefined check

- At the origin the radial direction is inapplicable/undefined.
- At `(1,0,0)` the radial channel is applicable and has defined value zero.

## Scale-aware diagnostic snapshot

For the exploratory `alpha=beta=1` centered quantity, finite sampling gives:

- sampled maximum value: `13.8952583208`
- radius: `0.96`

This sampled maximum is **not** a supremum proof and the descriptor is still `CONJECTURE / TARGET`.

## Claim boundary

These checks validate the displayed DSD-to-Navier-Stokes bridge constructions for one analytic Schwartz seed. They do not prove global existence, smoothness, coercivity, or an a-priori bound.
