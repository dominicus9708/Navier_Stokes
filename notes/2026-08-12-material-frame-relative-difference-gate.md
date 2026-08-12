# Material-frame relative-difference gate

Date: 2026-08-12

Status: **DERIVED MATERIAL-FRAME IDENTITY + DSD BRIDGE + OPEN PROOF OBLIGATION**.

## 1. Correct the role of `F^{-T}`

For a material cell

\[
\Omega_t=\Phi_t(B_\ell(a)),
\qquad
F=D_a\Phi_t,
\qquad
J=\det F=1,
\]

the pulled-back oriented boundary element is

\[
n_t\,dS_t=F^{-T}n_0\,dS_0.
\]

Therefore a surface representation of pressure work contains an explicit geometry factor:

\[
-\int_{\partial\Omega_t}p\,u\cdot n\,dS.
\]

However, because `div u=0`, the same term is exactly

\[
-\int_{\Omega_t}u\cdot\nabla p\,dx.
\]

Similarly,

\[
\nu\int_{\partial\Omega_t}u\cdot\partial_nu\,dS
-\nu\int_{\Omega_t}|\nabla u|^2dx
=
\nu\int_{\Omega_t}u\cdot\Delta u\,dx.
\]

Using `J=1`, the material-cell kinetic-energy balance can therefore be pulled back to the fixed initial ball as

\[
\frac{d}{dt}\frac12\int_{B_\ell(a)}|u(\Phi_t(b),t)|^2db
=
\int_{B_\ell(a)}
\left[-u\cdot\nabla p+\nu u\cdot\Delta u\right](\Phi_t(b),t)\,db.
\]

**Consequence:** `F^{-T}` is a valid boundary-geometry diagnostic, but it is not by itself an independent pressure-energy amplification mechanism. A proof route should not treat the surface geometry factor as a new source term when an equivalent volume representation removes it explicitly.

## 2. Exact growth channel for material boundary geometry

Let

\[
G=F^{-T}.
\]

Since

\[
\dot F=(\nabla u)F,
\]

we have

\[
\dot G=-(\nabla u)^T G.
\]

For an oriented-area vector

\[
g(t)=G(t)n_0,
\qquad
\eta=\frac{g}{|g|},
\]

write

\[
S=\frac12(\nabla u+\nabla u^T).
\]

Then

\[
\frac{d}{dt}\log|g|
=-\eta^TS\eta.
\]

If

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0,
\]

then

\[
\frac{d}{dt}\log|g|
\le -\lambda_1.
\]

Thus along a material trajectory,

\[
\boxed{
\|F^{-T}(t)\|
\lesssim
\exp\left(\int_0^t[-\lambda_1(\Phi_s(a),s)]\,ds\right)
}
\]

with the usual operator-norm interpretation (and a supremum over labels when controlling a whole cell).

This identifies the local compression channel

\[
\chi=-\lambda_1\ge0
\]

as the direct instantaneous growth rate for the worst oriented-area direction.

## 3. `lambda_2^+` does not control boundary geometry by itself

Consider the trace-free local strain model

\[
S=\operatorname{diag}(-M,0,M),
\qquad M>0.
\]

Then

\[
\lambda_2^+=0,
\]

but

\[
F(t)=\operatorname{diag}(e^{-Mt},1,e^{Mt}),
\qquad
\|F^{-T}(t)\|=e^{Mt}.
\]

Hence no pointwise material-geometry bound of the form

\[
\|F^{-T}\|\le \mathcal F\left(\int\lambda_2^+dt\right)
\]

can hold without additional information.

This does **not** invalidate middle-eigenvalue regularity criteria. It only shows that the DSD material-geometry channel and the known `lambda_2^+` danger channel are not interchangeable and must remain separately typed.

## 4. Remove the center motion: material-frame difference variable

Let the center material particle be

\[
X(t)=\Phi_t(a),
\qquad
U(t)=u(X(t),t).
\]

For each initial label `b` in `B_ell(a)`, define

\[
V(b,t)
=
u(\Phi_t(b),t)-U(t).
\]

This is the velocity difference inside the same tracked material cell.

Since each point follows a material trajectory,

\[
D_tu=-\nabla p+\nu\Delta u,
\]

so

\[
\boxed{
\dot V
=-\delta(\nabla p)+\nu\,\delta(\Delta u)
}
\]

where

\[
\delta(\nabla p)
=\nabla p(\Phi_t(b),t)-\nabla p(X(t),t)
\]

and similarly for `delta(Delta u)`.

This removes two irrelevant common motions automatically:

1. uniform translation of the whole local fluid cell;
2. uniform pressure-gradient acceleration applied equally to the center and neighboring material particles.

Only **differences across the tracked cell** remain.

## 5. Scale-critical material relative-energy channel

Define

\[
\boxed{
C_{\rm rel}(a,\ell,t)
=
\ell^{-1}
\int_{B_\ell(a)}|V(b,t)|^2db
}
\]

and the signed rate channels

\[
P_{\rm rel}
=
\ell\int_{B_\ell(a)}
V\cdot\delta(\nabla p)\,db,
\]

\[
V_{\rm rel}
=
\nu\ell\int_{B_\ell(a)}
V\cdot\delta(\Delta u)\,db.
\]

Then exactly

\[
\boxed{
\ell^2\partial_t C_{\rm rel}
=-2P_{\rm rel}+2V_{\rm rel}
}
\]

for fixed material label radius `ell`.

Under the Navier--Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),
\]

with material labels and radius scaled as

\[
a_\lambda=\lambda^{-1}a,
\qquad
\ell_\lambda=\lambda^{-1}\ell,
\]

the three quantities

\[
C_{\rm rel},\qquad P_{\rm rel},\qquad V_{\rm rel}
\]

are scale invariant.

This makes them legitimate critical-scale bridge candidates. It does not make them regularity criteria automatically.

## 6. Small-scale smooth expansion

At a smooth point, for `b=a+y`,

\[
\Phi_t(a+y)-\Phi_t(a)=F(a,t)y+o(|y|),
\]

and hence

\[
V(a+y,t)
=(\nabla u)(X(t),t)F(a,t)y+o(|y|).
\]

Using

\[
\int_{B_\ell}y_i y_jdy
=\delta_{ij}\frac{4\pi}{15}\ell^5,
\]

we obtain

\[
\boxed{
C_{\rm rel}(a,\ell,t)
=
\frac{4\pi}{15}\ell^4
\| (\nabla u)(X(t),t)F(a,t)\|_F^2
+o(\ell^4)
}
\]

as `ell -> 0` while the solution remains smooth.

Thus `C_rel` tends to zero at a smooth point. Under a critical concentration in which `grad u` grows like the inverse parabolic length squared, the `ell^4` normalization can keep this channel order one. This is a scaling observation only, not a blow-up characterization.

## 7. Revised DSD material block

The local material block should now separate

\[
\mathcal M(a,\ell,t)=
\left(
C_{\rm rel},
P_{\rm rel},
V_{\rm rel},
\chi=-\lambda_1,
\lambda_2^+,
\Delta_{\rm shape},
\omega,\text{alignment},\ldots
\right).
\]

Important separations:

- `chi=-lambda_1`: direct material-compression / boundary-geometry growth channel;
- `lambda_2^+`: established strain-growth danger channel, not a substitute for `chi`;
- `C_rel`: internal velocity difference after removing cell translation;
- `P_rel`: differential pressure coupling across the cell;
- `V_rel`: differential viscous coupling across the cell;
- `Delta_shape`: accumulated shape deformation.

## 8. New proof target

The next route is not to bound `||F^{-T}||` and multiply it blindly by pressure. Instead seek a non-circular all-label/all-scale estimate for the scale-critical internal-difference block, for example

\[
\sup_{a\in\mathbb R^3}\sup_{\ell>0}C_{\rm rel}(a,\ell,t)
\]

or a stronger time-space quantity built from `C_rel`, `P_rel`, `V_rel`, and the strain/alignment channels, and prove that its boundedness forces an established local or global regularity gate.

Status: **OPEN PROOF OBLIGATION**.
