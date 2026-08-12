# Vorticity-window dissipation certificate for a hypothetical singularity

Date: 2026-08-12

Status: **DERIVED SUFFICIENT GATE / CONDITIONAL NECESSARY SINGULARITY CERTIFICATE**.

This note combines the occupancy-to-line-sparseness lemma with the timing/scaling in Grujic's vorticity geometric regularity theorem.

It does not prove global regularity.  It derives an additional scale-invariant quantity that a hypothetical singularity must repeatedly keep non-small.

## 1. The theorem-scale quantities

Write

\[
W(t)=\|\omega(t)\|_\infty.
\]

In the vorticity sparseness theorem, the comparison time `s` lies in a window of the form

\[
I_t
=
\left[
 t+\frac{1}{4d_0^2W(t)},
 t+\frac{1}{d_0^2W(t)}
\right],
\]

and an admissible geometric scale is

\[
r_t
=
\frac{1}{2d_0^2W(t)^{1/2}}.
\]

The intense-vorticity threshold has the form

\[
M_t
=d_0^{-\alpha}W(t),
\]

where `alpha` is chosen from the theorem according to the sparseness parameter `delta`.

The window length is

\[
|I_t|
=
\frac{3}{4d_0^2W(t)}.
\]

## 2. Global enstrophy packing condition at a comparison time

From the occupancy note, the active set

\[
S_s=\{x:|\omega(x,s)|>M_t\}
\]

is linearly `delta`-sparse around every point at the scale `r_t` if

\[
\frac{\|\omega(s)\|_2^2}{W(t)^{1/2}}
<
K_{\delta,d_0},
\]

where, using the explicit theorem-scale choices above,

\[
\boxed{
K_{\delta,d_0}
=
\frac{\pi}{6}
\delta^3
d_0^{-(2\alpha+6)}.
}
\]

Indeed this is exactly the condition ensuring that the total active-set volume is smaller than `delta^3` times the volume of a ball of radius `r_t`.

## 3. Use the enstrophy integral over the analyticity window

Define

\[
\mathcal I_\omega(t)
=
\int_{I_t}\|\omega(s)\|_2^2ds.
\]

There exists at least one `s in I_t` with

\[
\|\omega(s)\|_2^2
\le
\frac{\mathcal I_\omega(t)}{|I_t|}
=
\frac{4d_0^2}{3}
W(t)\mathcal I_\omega(t).
\]

Therefore

\[
\frac{\|\omega(s)\|_2^2}{W(t)^{1/2}}
\le
\frac{4d_0^2}{3}
W(t)^{1/2}\mathcal I_\omega(t).
\]

Introduce the dimensionless vorticity-window dissipation channel

\[
\boxed{
\mathcal Z_\omega(t)
=
W(t)^{1/2}
\int_{I_t}\|\omega(s)\|_2^2ds.
}
\]

Under Navier--Stokes scaling,

- `W^{1/2}` scales like `lambda`;
- `||omega||_2^2` scales like `lambda`;
- `dt` scales like `lambda^{-2}`;

so `mathcal Z_omega` is scale invariant.

## 4. Sufficient regularity gate

If

\[
\mathcal Z_\omega(t)
<
\frac{3}{4d_0^2}K_{\delta,d_0},
\]

then the averaging argument selects an `s in I_t` satisfying the global packing condition, hence the intense-vorticity set is linearly `delta`-sparse around every point at the admissible scale `r_t`.

Substituting `K_{delta,d0}` gives

\[
\boxed{
\mathcal Z_\omega(t)
<
\frac{\pi}{8}
\delta^3
d_0^{-(2\alpha+8)}
}
\]

as a sufficient gate for the geometric theorem at that starting time `t`.

This constant is not optimized; it is simply the result of the volume/Chebyshev bridge and the theorem's stated scale window.

## 5. Conditional necessary certificate for a singularity

Grujic's theorem requires the sparseness event for each sufficiently late starting time (unless the local analyticity interval already crosses the putative singular time, which itself gives regularity).

Therefore, if a singular time `T*` existed, then arbitrarily close to `T*` there must be starting times `t` for which the sufficient gate above fails:

\[
\boxed{
\mathcal Z_\omega(t)
\gtrsim
c_{\delta,d_0}>0.
}
\]

Equivalently, the flow must expend at least critical-order enstrophy over some vorticity-analyticity windows:

\[
\boxed{
\int_{I_t}\|\omega(s)\|_2^2ds
\gtrsim
W(t)^{-1/2}.
}
\]

This is a **necessary certificate within this external geometric-gate route**, not an unconditional standalone blow-up theorem.

## 6. Why finite total dissipation does not yet contradict it

For a smooth whole-space incompressible flow,

\[
\int_0^{T}\|\omega(s)\|_2^2ds
\]

is controlled by the kinetic-energy dissipation up to the maximal smooth time.

However the lower cost `W(t)^{-1/2}` shrinks as the vorticity maximum grows.  A sequence with rapidly increasing `W(t_n)` can have

\[
\sum_n W(t_n)^{-1/2}<\infty.
\]

Thus finite total dissipation alone does not rule out infinitely many critical windows.

The new information is structural: **a singular cascade cannot be both arbitrarily intense and arbitrarily cheap in enstrophy on every natural analyticity window.**

## 7. DSD interpretation

Add to the multiscale state the time-window channel

\[
\mathcal Z_{\omega,k}
=
\|\omega(t_k)\|_\infty^{1/2}
\int_{I_{t_k}}\|\omega(s)\|_2^2ds.
\]

The singular residual set now requires simultaneous survival of

1. moving velocity oscillation/dissipation concentration;
2. local pressure-cascade transfer;
3. non-sparse intense-vorticity occupancy;
4. non-small `mathcal Z_omega` on arbitrarily late natural windows;
5. no rescue by vorticity-direction or strain regularity gates.

This is suitable for the Formation-Axiom-style complement-elimination strategy: each independent regularity gate removes a class of candidate singular structures, leaving a progressively narrower residual class.

## 8. External anchor and claim boundary

External theorem used:

- Z. Grujic, *A geometric measure-type regularity criterion for solutions to the 3D Navier-Stokes equations*, arXiv:1111.0217, especially the vorticity version of the main theorem.

The volume-to-line lemma, Chebyshev estimate, scale substitution, and time-window averaging above are derived in this repository.

Status: **OPEN RESIDUAL-CLASS EXCLUSION**.
