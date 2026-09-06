# DSD M17-264 — Bounded ancient multiplier on compact closed Rank-2 fibers is constant and contradicts critical sign balance

Date: 2026-09-06  
Canonical ID: **M17-264**

Status: **CONDITIONAL COMPACT-FIBER CLOSURE / M17-263 REDUCES THE RAW RANK-2 CE-H HEAT-TANGENT MULTIPLIER TO `K_tau=K_ss+b_f K_s` ALONG ONE-DIMENSIONAL DIRECTOR FIBERS. ON A CLOSED FIBER WITH UNIFORMLY BOUNDED LENGTH AND BOUNDED DRIFT, STANDARD UNIFORMLY PARABOLIC HEAT-KERNEL POSITIVITY GIVES A FIXED OSCILLATION-CONTRACTION FACTOR OVER A FIXED TIME. BECAUSE THE NON-SPIKE TANGENT HAS `|K|<=K_*` FOR ALL ANCIENT TIMES, ITERATING THE CONTRACTION FROM ARBITRARILY REMOTE PAST TIMES FORCES ZERO OSCILLATION AT THE PRESENT TIME. HENCE `K` IS CONSTANT ALONG EACH FIBER. M17-262 ALREADY MAKES ALL TRANSVERSE DERIVATIVES ZERO, SO `K` IS SPATIALLY CONSTANT ON THE CONNECTED RANK-2 PATCH. THE M17-233/234 SPECTRAL SURVIVOR, HOWEVER, REQUIRES NONTRIVIAL CRITICAL `K` OCCUPANCY TOGETHER WITH A SMALL SIGNED MEAN / NONZERO GRADIENT ALTERNATIVE, EXCLUDING A SINGLE SPATIAL CONSTANT. THEREFORE THE COMPACT CLOSED-FIBER, NONDEGENERATE, BOUNDED-DRIFT RAW CALORIC LANE CLOSES. REMAINING EXITS ARE FIBER BOUNDARY/INTERFACE, FIBER DECOMPACTIFICATION, NODAL/AMPLITUDE DEGENERATION, DRIFT/GEOMETRY BLOWUP, RANK LOSS, OR COEFFICIENT SPIKE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-263

On an active Rank-2 raw CE-H heat tangent,

\[
\boxed{
\partial_\tau K
=D_{t_f}^2K+b_fD_{t_f}K,
}
\]

where `t_f` is the unit tangent spanning

\[
\ker D\xi
\]

and

\[
\boxed{
b_f:=\nabla\cdot t_f+2D_{t_f}\log|a|.}
\]

Also M17-262 gives

\[
\boxed{
\nabla K\parallel t_f.
}
\]

Thus all spatial variation of `K` is already confined to one fiber direction.

---

## 2. Compact closed-fiber corridor

Fix one connected tangent patch and assume the following corridor.

### Closed fibers

Every relevant fiber is a closed one-dimensional curve with arclength coordinate

\[
s\in\mathbb R/L\mathbb Z.
\]

### Uniform fiber length

\[
\boxed{
0<L_-\le L\le L_+<\infty.
}
\]

### Nondegenerate active amplitude

On the retained fiber corridor,

\[
\boxed{
0<a_-\le |a(s,\tau)|\le a_+<\infty.
}
\]

### Bounded fiber drift

\[
\boxed{
|b_f(s,\tau)|\le B_*<\infty
\qquad(\tau\le0).
}
\]

### Non-spiking multiplier

\[
\boxed{
|K(s,\tau)|\le K_*<\infty
\qquad(\tau\le0).
}
\]

Any failure of these assumptions is retained as an explicit exit rather than silently repaired.

---

## 3. Uniform parabolic oscillation contraction

On each fiber,

\[
\partial_\tau K
=\partial_s^2K+b_f(s,\tau)\partial_sK.
\]

This is a scalar uniformly parabolic equation on a compact circle with unit diffusion coefficient and uniformly bounded drift.

Standard one-dimensional parabolic kernel estimates imply that there exist constants

\[
\tau_0>0,
\qquad
0<\eta<1
\]

depending only on

\[
L_-,L_+,B_*
\]

such that the evolution operator over any interval of length `tau_0` has a strictly positive mixing kernel.

Equivalently, the oscillation contracts by a uniform factor

\[
\boxed{
\operatorname{osc}_sK(\tau+\tau_0)
\le q\,\operatorname{osc}_sK(\tau),
\qquad
q:=1-\eta\in(0,1).
}
\]

This is the compact-fiber analogue of strict heat smoothing.

---

## 4. Ancient boundedness forces zero oscillation

Fix the observation time `tau=0`.

Iterate Section 3 backward from time

\[
-N\tau_0.
\]

Then

\[
\operatorname{osc}_sK(0)
\le
q^N
\operatorname{osc}_sK(-N\tau_0).
\]

The non-spike ceiling gives

\[
\operatorname{osc}_sK(-N\tau_0)
\le2K_*.
\]

Hence

\[
\operatorname{osc}_sK(0)
\le2K_*q^N.
\]

Letting `N->infinity`,

\[
\boxed{
\operatorname{osc}_sK(0)=0.
}
\]

The same argument after time translation gives

\[
\boxed{
D_{t_f}K=0
\quad\text{for all ancient times.}
}
\]

Thus `K` is constant along every retained closed fiber.

---

## 5. Rank-2 transverse rigidity makes K spatially constant

M17-262 already gives

\[
D_vK=0
\]

for every direction `v` transverse to the fiber kernel.

Section 4 gives the remaining fiber derivative

\[
D_{t_f}K=0.
\]

Therefore

\[
\boxed{
\nabla K=0
}
\]

on the connected active Rank-2 patch.

Hence

\[
\boxed{
K(z,\tau)=k(\tau)
}
\]

spatially.

The heat/CE-H relation then gives a spatial constant effective Laplacian multiplier at each time.

---

## 6. Conflict with the critical coefficient survivor

M17-233 converts the mean-dominated intrinsic spectral survivor, on the non-spike branch, into a scale-critical amplitude-independent coefficient occupancy

\[
\boxed{
\int_{B_A}|K|^{3/2}dz\ge c_K>0.
}
\]

M17-234 further shows that the signed mean of the same coefficient packet is small while its absolute critical mass remains nontrivial, forcing a nonzero scale-critical gradient / sign-balanced structure unless another coefficient-spike or interface exit occurs.

A single spatial constant `K=k(tau)` cannot simultaneously have

1. a nontrivial sign-balanced spatial population;
2. small signed mean relative to nonzero absolute occupancy;
3. nonzero spatial gradient.

If the constant tends to zero to satisfy the signed-mean condition, it violates the fixed critical occupancy lower bound.

If the constant remains nonzero to satisfy the occupancy bound, its signed mean is of the same order as its absolute mean and violates the sign-balance output.

Therefore

\[
\boxed{
H_{compact\ closed\ fiber}^{Rank2,nondeg,bounded\ drift}
\Longrightarrow\bot
}
\]

on the retained critical coefficient branch.

---

## 7. Explicit residual exits

The compact-fiber closure does not apply if any of the following occurs:

\[
\boxed{
G_{fiber\ boundary/interface}
\lor
G_{fiber\ decompactification}
\lor
G_{nodal/amplitude\ degeneration}
\lor
G_{fiber\ drift/geometry\ blowup}
\lor
G_{rank\ loss}
\lor
G_{K\text{-}spike}.
}
\]

These are not bookkeeping artifacts. Each is exactly a hypothesis failure used in the oscillation-contraction argument.

---

## 8. Relation to earlier director modules

M17-214 already treats large director-area carriers under bounded flux/fiber geometry and records fiber decompactification as an exit.

M17-215/216 track anisotropy and material distortion.

M17-264 now shows that **if the fiber refuses those decompactification/interface exits and stays compact/nondegenerate, the raw caloric coefficient cannot maintain its critical sign-balanced structure indefinitely.**

Thus the fiber-compact side of the old director/coefficient survivor is closed at the tangent level.

---

## 9. DSD audit

1. Closed-fiber topology is an explicit hypothesis; open fibers are not treated as periodic.
2. Uniform oscillation contraction is used only under fixed length and bounded drift.
3. Amplitude nondegeneracy is required because the drift contains `D_tf log|a|`.
4. Nodal/amplitude degeneration remains an exit.
5. The contradiction uses M17-233/234 coefficient sign-balance output, not merely nonzero `K`.
6. No claim is made that all Rank-2 fibers are closed.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
