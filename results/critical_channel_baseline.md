# Critical-channel baseline

Checks passed: **10/10**

## Key exact findings

- `tr S = 0`.
- `omega^T S omega = 64*z*(x**2 + y**2)*(2*x**2 + 2*y**2 + 2*z**2 - 5)**2*exp(-3*x**2)*exp(-3*y**2)*exp(-3*z**2)`.
- normalized signed shell stretching = `0`.
- normalized positive-part shell stretching = `r**3*(32*r**4 - 160*r**2 + 200)*exp(-3*r**2)`.
- global positive stretching = `992*pi/81` and the negative part is its exact opposite.

The zero global sum therefore hides nonzero local stretching. This is an aggregation-cancellation witness, not a regularity theorem.

## Pressure closure

div R_adv = -Q, div R_pres = +Q when -Delta p=Q, and div R_visc=0.

## Claim boundary

This is a benchmark cancellation witness. It is not a general bound on vortex stretching.
