# Exact dynamics of the global vorticity covariance and projective dispersion

Date: 2026-08-13

Status: **DERIVED GLOBAL MATRIX IDENTITY / OPEN DYNAMIC CLOSURE**.

This note evolves the axis-choice-free projective vorticity-dispersion channel

\[
\mathcal J_\omega=1-\operatorname{tr}(\mathsf C_\omega^2)
\]

under the ordinary 3D incompressible Navier--Stokes vorticity equation.

No extra DSD force law is introduced.

## 1. Vorticity equation

For a smooth decaying whole-space solution,

\[
\partial_t\omega+(u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega,
\qquad
S=\frac12(\nabla u+\nabla u^T).
\]

Let

\[
E=\int|\omega|^2dx,
\qquad
N=\int\omega\otimes\omega\,dx,
\qquad
C=\frac NE.
\]

Also define the stretching moment

\[
A=\int(S\omega)\otimes\omega\,dx
\]

and the gradient covariance

\[
H
=\sum_{k=1}^3
\int(\partial_k\omega)\otimes(\partial_k\omega)\,dx.
\]

Then

\[
Q=\operatorname{tr}A
=\int\omega\cdot S\omega\,dx,
\qquad
P=\operatorname{tr}H
=\int|\nabla\omega|^2dx.
\]

## 2. Exact second-moment evolution

The transport contribution disappears after whole-space integration because `div u=0` and the field decays sufficiently fast.

The stretching term gives `A+A^T`, while integration by parts gives the viscous contribution `-2 nu H`.

Hence

\[
\boxed{
\dot N
=A+A^T-2\nu H.
}
\]

Taking the trace recovers the enstrophy equation

\[
\boxed{
\dot E
=2Q-2\nu P.
}
\]

## 3. Normalized covariance evolution

Introduce

\[
B=\frac AE,
\qquad
G=\frac HE,
\qquad
q=\frac QE=\operatorname{tr}B,
\qquad
p=\frac PE=\operatorname{tr}G.
\]

Differentiating `C=N/E` gives

\[
\boxed{
\dot C
=B+B^T-2\nu G
-2(q-\nu p)C.
}
\]

The last term removes the part of the raw second-moment growth that is only an overall enstrophy amplification/decay. Therefore `C` records directional redistribution rather than total magnitude.

## 4. Exact projective-dispersion budget

Let

\[
\mathcal J=1-\operatorname{tr}(C^2).
\]

Then

\[
\dot{\mathcal J}
=-2\operatorname{tr}(C\dot C),
\]

so

\[
\boxed{
\frac14\dot{\mathcal J}
=
\underbrace{
q(1-\mathcal J)-\operatorname{tr}(CB)
}_{\mathcal M_S}
+
\nu\underbrace{
\left[
\operatorname{tr}(CG)-p(1-\mathcal J)
\right]
}_{\mathcal M_\nu}.
}
\]

Define

\[
\boxed{
\mathcal M_S
=q\operatorname{tr}(C^2)-\operatorname{tr}(CB)
}
\]

and

\[
\boxed{
\mathcal M_\nu
=\operatorname{tr}(CG)-p\operatorname{tr}(C^2).
}
\]

Then

\[
\boxed{
\dot{\mathcal J}
=4\mathcal M_S+4\nu\mathcal M_\nu.
}
\]

This is an exact global two-channel budget:

- `M_S`: directional mixing/demixing caused by vortex stretching;
- `M_nu`: directional mixing/demixing caused by viscous gradient covariance.

Neither term has a universal sign for arbitrary data.

## 5. Unnormalized pairwise cross-axis content

Define

\[
K=E^2\mathcal J.
\]

By the projective-dispersion identity,

\[
\boxed{
K
=\iint|\omega(x)\times\omega(y)|^2dxdy.
}
\]

Differentiating either this expression or `K=E^2-tr(N^2)` gives

\[
\boxed{
\frac14\dot K
=
E Q-\operatorname{tr}(NA)
+\nu\left[
\operatorname{tr}(NH)-EP
\right].
}
\]

Thus the total pairwise cross-axis content is created or destroyed by deviations of the stretching/gradient moments from the directional covariance already present in `N`.

## 6. Exact one-axis invariant test

Suppose

\[
\omega(x)=f(x)n
\]

for a fixed unit vector `n`, and suppose the instantaneous stretching and gradient covariance preserve that same axis:

\[
S\omega=s(x)\omega,
\qquad
\partial_k\omega=(\partial_k f)n.
\]

Then

\[
C=n\otimes n,
\qquad
\mathcal J=0,
\]

and both mixing channels vanish:

\[
\mathcal M_S=0,
\qquad
\mathcal M_\nu=0,
\qquad
\dot{\mathcal J}=0.
\]

Therefore multi-axis content is not generated merely by scalar amplification along an already existing common axis.

## 7. Relation to the previous axis-conversion channel

The principal-axis calculation identified

\[
\chi_n=|P_{n^\perp}Sn|
\]

as a direct principal-to-off-axis conversion amplitude, with

\[
\chi_n^2
=
\sum_{i<j}b_i b_j(\lambda_i-\lambda_j)^2.
\]

The matrix channel `M_S` is the orientation-free aggregate version of the same phenomenon at the level of the normalized second moment. It also contains self-stretching of already existing off-axis vorticity.

Thus the two descriptions should be retained at different resolutions:

1. `chi_n`: local / principal-axis conversion amplitude;
2. `M_S`: global axis-choice-free directional-mixing budget.

## 8. What would close the route

The Miller-derived residual condition requires

\[
E\mathcal J\notin L^2(0,T^*)
\]

for any hypothetical blowup.

The new exact evolution shows that maintaining this projective dispersion requires persistent contribution from

\[
\mathcal M_S
\quad\text{and/or}\quad
\nu\mathcal M_\nu.
\]

A proof-producing estimate would need to connect these channels to quantities with known finite spacetime budgets, or show that the configurations making them large trigger one of the already established geometric/sparseness regularity gates.

The immediate next target is therefore a **mixing-channel closure dichotomy**:

\[
\boxed{
\text{large }\mathcal M_S
\Rightarrow
\text{strain/alignment gate},
\qquad
\text{large }\mathcal M_\nu
\Rightarrow
\text{palinstrophy/derivative gate}.
}
\]

Status: **OPEN MIXING-CHANNEL CLOSURE**.
