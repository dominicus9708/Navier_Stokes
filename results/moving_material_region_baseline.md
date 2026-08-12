# Moving observer sphere / material-cell baseline

Status: **DERIVED KINEMATIC BRIDGE + COMPUTATIONAL CHECK**

Checks passed: **10/10**

## Exact kinematic split

- Co-moving observer sphere: center follows `dX/dt=u(X,t)` but radius/shape are held spherical.
- Material cell: `Omega_ell^mat(t)=Phi_t(B_ell(a))` follows the same fluid particles and may deform.
- For incompressible smooth flow, `det D_a Phi_t = 1`; volume is preserved even when shape changes.

## Gaussian anchor

At `a=(0,0,1/2)`, with `c=e^(-1/4)`:

- center velocity: `(0,0,4c)`;
- strain eigenvalues: `(-4c, 2c, 2c)`;
- local rotation tensor: `0`;
- trace of strain: `0`.

The frozen local model therefore has principal stretches

`(exp(2 c tau), exp(2 c tau), exp(-4 c tau))`,

whose product is exactly `1`. Two directions expand while one contracts.

## Local DSD shape gap

For `U=sqrt(F^T F)`, use the bridge quantity

`Delta_shape = ||log U||_F`.

In the frozen anchor model,

`Delta_shape = 2 sqrt(6) e^(-1/4) |tau|`.

This is zero for pure co-translation but positive for strain-driven deformation.

## Sample values

- tau=0.00: sigma=(1,1,1), detF=1, aspect=1, Delta_shape=0
- tau=0.05: sigma=(1.08099,1.08099,0.855764), detF=1, aspect=1.26319, Delta_shape=0.190766
- tau=0.10: sigma=(1.16855,1.16855,0.732333), detF=1, aspect=1.59565, Delta_shape=0.381533
- tau=0.20: sigma=(1.3655,1.3655,0.536311), detF=1, aspect=2.5461, Delta_shape=0.763066
- tau=0.50: sigma=(2.17886,2.17886,0.210641), detF=1, aspect=10.344, Delta_shape=1.90766

## Claim boundary

The flow-map/Jacobian identities are exact for a smooth incompressible flow up to the lifespan on which the flow map is a diffeomorphism. The Gaussian frozen-gradient ellipsoid is only a local t=0 deformation model and is not a time-integrated Navier-Stokes solution.

The next proof-relevant step is not to keep one sphere centered at one origin, but to label local cells by every initial material point `a` and scale `ell`, then track deformation/pressure/vorticity channels along their trajectories.
