# Global Critical-Budget Audit — 2026-08-20

Overall status: **ACTIVE PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

The global stage-packing barrier shows that the ordinary kinetic-energy budget is short by one half-power of the first-hitting vorticity scale. This note audits obvious scale-critical alternatives before introducing a new functional.

---

## 1. Navier--Stokes scaling

Under

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

\[
\omega_\lambda(x,t)=\lambda^2\omega(\lambda x,\lambda^2t).
\]

The first-hitting vorticity level is `W~lambda^2`.

A natural singular packet therefore has radius `lambda^{-1}=W^{-1/2}` and time width `lambda^{-2}=W^{-1}`.

---

## 2. Kinetic energy is subcritical for stage counting

\[
E=\int|u|^2dx
\]

scales as

\[
E[u_\lambda]=\lambda^{-1}E[u].
\]

Thus a natural packet has energy/dissipation-stage weight

\[
\lambda^{-1}=W^{-1/2}.
\]

This is precisely the geometric summability obstruction established in `GLOBAL_STAGE_PACKING_BARRIER_2026-08-20.md`.

---

## 3. Velocity L3 is critical but not a priori bounded

\[
\|u_\lambda\|_3=\|u\|_3.
\]

Hence `L3` is an ideal scaling match for one-cost-per-scale arguments. However finite-energy Leray theory does not give a uniform global bound on `||u||_3`; indeed finite-time singularity forces failure of the endpoint critical bound. Therefore `L3` is a regularity criterion/obstruction, not an available finite global budget.

The standard energy interpolation does give

\[
\|u\|_3^4
\lesssim
\|u\|_2^2\|\nabla u\|_2^2,
\]

and hence

\[
\int_0^{T}\|u\|_3^4dt<\infty,
\]

but a natural first-hitting packet contributes only an additional physical-time factor `W^{-1}`. Without a lower bound `||u||_3^4 \gtrsim W`, this does not give a fixed critical stage payment.

---

## 4. Critical Sobolev norms are likewise not globally bounded for large data

The homogeneous norm

\[
\|u\|_{\dot H^{1/2}}
\]

is scaling invariant. It is therefore another formally suitable critical quantity, but no large-data a priori bound is available that could serve as the finite side of a stage-packing contradiction.

---

## 5. Helicity is scale-critical but sign-indefinite

Define

\[
\mathscr H(t)=\int u\cdot\omega\,dx.
\]

Under Navier--Stokes scaling,

\[
\boxed{\mathscr H[u_\lambda]=\mathscr H[u].}
\]

For smooth decaying solutions,

\[
\boxed{
\frac{d}{dt}\mathscr H
=-2\nu\int\omega\cdot(\nabla\times\omega)\,dx.
}
\]

Thus helicity has exactly the desired critical scaling, but its viscous production/dissipation has no fixed sign. Moreover non-helical or mirror-symmetric configurations may have `H=0` while retaining substantial strain/vorticity dynamics.

Therefore helicity cannot serve as a universal positive stage budget for `H`, `T`, and `P_V`.

The absolute helicity `int |u dot omega|` is positive but has no corresponding globally controlled monotone law.

---

## 6. Circulation is critical but not a universal positive global budget

For a loop `Gamma`,

\[
\oint_\Gamma u\cdot dl
\]

is scaling invariant. In the inviscid equation it is tied to Kelvin transport, but viscosity introduces a loop-dependent diffusion term. It is not a positive global functional, depends on the chosen loop, and may vanish through cancellation even in dynamically active configurations.

Thus circulation is better viewed as a possible geometric subchannel (e.g. coherent vortex tubes), not as the common global budget currently required.

---

## 7. The P_V projective action is critical but lacks an a priori finite total bound

The physical strain-projective action

\[
\mathscr A_V
=
\int
\frac{\|P_{st}(\frac13S^2+\frac14\omega\otimes\omega)\|_2}
{\|S\|_2}
\,dt
\]

is scale invariant.

However the first-hitting estimate gives only

\[
\frac{\|P_{st}(\frac13S^2+\frac14\omega\otimes\omega)\|_2}
{\|S\|_2}
\lesssim
\|\omega\|_\infty.
\]

Consequently

\[
\mathscr A_V
\lesssim
\int\|\omega\|_\infty dt,
\]

which is precisely the Beale--Kato--Majda clock that must diverge at a finite-time singularity. Hence `A_V` is critical but is not currently known to have the finite global side needed for contradiction.

---

## 8. Conclusion of the audit

No standard obvious quantity simultaneously has all three properties required for route G2:

1. scale-criticality;
2. positivity/coercivity on every surviving local branch;
3. an a priori finite global total for arbitrary smooth finite-energy data.

Kinetic energy has (2)-(3) but misses criticality by `W^(1/2)`. `L3` and critical Sobolev norms have criticality and positivity but not an a priori large-data global bound. Helicity/circulation have criticality but not universal positivity/coercivity. `P_V` action is critical and branch-specific but currently has no finite a priori total.

Therefore the remaining global strategy must be one of:

- derive the missing `W^(1/2)` amplification into the ordinary energy budget;
- find a genuinely new positive critical functional tied to the DSD/projective structure;
- or prove a local rigidity theorem strong enough that no global stage summation is needed.

Status: **STANDARD GLOBAL BUDGETS AUDITED; NONE CURRENTLY CLOSE THE CRITICAL STAGE-PACKING GAP. THE GLOBAL OBSTRUCTION IS NOW EXPLICIT RATHER THAN HIDDEN.**