# Translation and cross-coupling baseline

Checks passed: **5/5**

## Translation completeness

- translated seed center: `(1.5, 0.0, 0.0)`
- centered special-shell CV: `4.575e-16`
- same-radius shell about the old origin CV: `3.29628`

This confirms that a fixed-origin shell analysis is not translation complete.

## Nonlinear coupling

- `Q_cross = -16*z*(4*x**3 + 2*x**2 - 12*x + 6*y**2 + 6*z**2 - 3)*exp(-1)*exp(2*x)*exp(-2*x**2)*exp(-2*y**2)*exp(-2*z**2)`
- test-point value: `-14.1790480169`

Velocity composition is linear and remains divergence-free, but the pressure/advection closure source `Q` contains a nonzero cross term. Static composition therefore does not imply dynamical independence.

## Claim boundary

Finite translated/superposed benchmarks establish covariance and a cross-coupling witness only; they do not cover arbitrary initial data.
