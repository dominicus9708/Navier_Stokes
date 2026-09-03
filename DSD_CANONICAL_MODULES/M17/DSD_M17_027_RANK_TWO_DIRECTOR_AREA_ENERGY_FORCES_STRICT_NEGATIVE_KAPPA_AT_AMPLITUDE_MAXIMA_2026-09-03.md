# DSD M17-027 — Rank-two director area-energy forces strict negative kappa at vorticity-amplitude maxima

Date: 2026-09-03
Canonical ID: **M17-027**

Status: **INTERNAL RANK-TWO AREA-ENERGY COERCIVITY / DECOMPOSING `W=rho xi` IN `Delta W=kappa W` GIVES THE EXACT AMPLITUDE EQUATION `Delta rho=(kappa+|grad xi|^2)rho`. AT A RANK-TWO DIRECTOR POINT THE TWO NONZERO SINGULAR VALUES OF `d xi` GIVE `2|J_xi| <= |grad xi|^2`. HENCE ANY POSITIVE LOCAL MAXIMUM OF VORTICITY AMPLITUDE LYING IN THE RANK-TWO REGION SATISFIES `kappa <= -|grad xi|^2 <= -2|J_xi| < 0`. GLOBALLY, `int kappa rho^2 = -int |grad rho|^2 - int rho^2|grad xi|^2 <= -int |grad rho|^2 - 2 int rho^2|J_xi|`. THEREFORE RANK-TWO DIRECTOR AREA IS A COERCIVE NEGATIVE-KAPPA COST, NOT A NEUTRAL GEOMETRIC DECORATION. ON A COMPACT HIGH-AMPLITUDE BRANCH UNIFORMLY SEPARATED FROM RANK LOSS, THIS PRODUCES A FIXED NEGATIVE PAYER FLOOR. IT DOES NOT YET CONTRADICT RECURRENCE BECAUSE THE REQUIRED NEGATIVE COST CAN BE BALANCED BY THE EXISTING KAPPA CONVEYOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scalar amplitude equation

Write

\[
W=\rho\xi,
\qquad
\rho=|W|>0,
\qquad
|\xi|=1.
\]

The CE-H Laplacian eigenline is

\[
\Delta W=\kappa W.
\]

Expand:

\[
\Delta(\rho\xi)
=(\Delta\rho)\xi
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi.
\]

Dot with `xi`.
Because

\[
\xi\cdot\partial_i\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

we obtain

\[
\boxed{
\Delta\rho
-\rho|\nabla\xi|^2
=\kappa\rho.
}
\]

Equivalently,

\[
\boxed{
\Delta\rho
=(\kappa+|\nabla\xi|^2)\rho.
}
\]

---

## 2. Rank-two area-energy inequality

At a rank-two point, the differential

\[
d\xi:T_x\mathbb R^3\to T_\xi S^2
\]

has two nonzero singular values

\[
s_1,s_2>0.
\]

The Dirichlet density is

\[
\boxed{
|\nabla\xi|^2=s_1^2+s_2^2.
}
\]

The director-area current magnitude is the two-dimensional Jacobian

\[
\boxed{
|J_\xi|=s_1s_2.
}
\]

By the arithmetic-geometric mean inequality,

\[
s_1^2+s_2^2\ge2s_1s_2.
\]

Therefore

\[
\boxed{
|\nabla\xi|^2
\ge2|J_\xi|.
}
\]

Equality holds exactly when

\[
s_1=s_2,
\]

i.e. the rank-two director differential is conformal on its two-dimensional active subspace.

---

## 3. Vorticity-amplitude maximum principle

Let `x_*` be a positive local maximum of `rho`:

\[
\rho(x_*)>0,
\qquad
\nabla\rho(x_*)=0,
\qquad
\Delta\rho(x_*)\le0.
\]

The amplitude equation gives

\[
(\kappa+|\nabla\xi|^2)\rho
=\Delta\rho\le0.
\]

Since `rho>0`,

\[
\boxed{
\kappa(x_*)
\le
-|\nabla\xi(x_*)|^2.
}
\]

If the maximum lies in the rank-two region,

\[
|J_\xi(x_*)|>0,
\]

and hence

\[
\boxed{
\kappa(x_*)
\le
-|\nabla\xi|^2
\le
-2|J_\xi|
<0.
}
\]

Thus a rank-two vorticity-amplitude ridge is necessarily on the strictly negative side of the multiplier field.

---

## 4. Global amplitude-director energy identity

Multiply

\[
\Delta\rho
=(\kappa+|\nabla\xi|^2)\rho
\]

by `rho` and integrate under the retained decay assumptions:

\[
\int\rho\Delta\rho
=-\int|\nabla\rho|^2.
\]

Therefore

\[
\boxed{
\int\kappa\rho^2
=-\int|\nabla\rho|^2
-\int\rho^2|\nabla\xi|^2.
}
\]

This is the amplitude-direction decomposition of the usual CE-H identity

\[
\int\kappa|W|^2=-\int|\nabla W|^2.
\]

Indeed

\[
|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

---

## 5. Rank-two area lower bound on the negative budget

Use

\[
|\nabla\xi|^2\ge2|J_\xi|.
\]

Then

\[
\boxed{
\int\kappa\rho^2
\le
-\int|\nabla\rho|^2
-2\int\rho^2|J_\xi|.
}
\]

Thus the director-area current contributes a coercive amount to the globally negative kappa budget.

In particular,

\[
\boxed{
-\int\kappa\rho^2
\ge
2\int\rho^2|J_\xi|.
}
\]

The right-hand side vanishes only if rank-two area disappears almost everywhere in the vorticity-weighted region.

---

## 6. Transverse area density version

M17-026 gives

\[
j_\xi=J_\xi\cdot\xi.
\]

Hence

\[
|j_\xi|\le|J_\xi|.
\]

Therefore

\[
\boxed{
|\nabla\xi|^2
\ge2|J_\xi|
\ge2|j_\xi|.
}
\]

The global budget also obeys

\[
\boxed{
-\int\kappa\rho^2
\ge
2\int\rho^2|j_\xi|.
}
\]

This directly connects the M16-025 transverse director-area density to the negative-kappa cost.

---

## 7. Pointwise rank-two ridge classification

At an amplitude maximum there are now three director-rank possibilities:

### Rank zero

\[
\nabla\xi=0.
\]

Then only

\[
\kappa\le0
\]

is forced by the amplitude equation.

### Rank one

\[
\operatorname{rank}d\xi=1.
\]

Then

\[
\kappa\le-|\nabla\xi|^2<0
\]

if the director is nonconstant there.

### Rank two

\[
\operatorname{rank}d\xi=2.
\]

Then the stronger area estimate holds:

\[
\boxed{
\kappa\le-2|J_\xi|<0.
}
\]

Thus any genuinely varying director at a vorticity-amplitude maximum is automatically a negative-kappa payer.

---

## 8. Compact rank-two branch gives a finite local payer

Suppose the retained hard branch contains a marked high-amplitude point with uniform bounds

\[
\rho\ge\rho_*>0,
\qquad
|J_\xi|\ge J_*>0
\]

and remains uniformly separated from rank loss.

Compact `C^1/C^2` control then gives a fixed neighborhood of positive volume `V_*` where, after shrinking constants,

\[
\rho\ge\frac{\rho_*}{2},
\qquad
|J_\xi|\ge\frac{J_*}{2}.
\]

Therefore

\[
\boxed{
\int_{neighborhood}
\rho^2|J_\xi|
\ge
\frac{\rho_*^2J_*}{8}V_*>0.
}
\]

The global negative-kappa budget consequently has a fixed lower contribution from the rank-two patch.

This quantitative step is conditional on uniform separation from rank loss and high-amplitude marking; it is not claimed for an arbitrary rank-two point approaching zero density.

---

## 9. DSD interpretation

### 9.1 Rank is dynamically costly
Rank-two direction geometry cannot be inserted without cost into the scalar multiplier budget.
Its two-dimensional area density appears directly in the negative side of the amplitude equation.

### 9.2 Maximum descriptor
The sign of `kappa` at amplitude ridges distinguishes geometry:
strong direction variation forces strict negativity.

### 9.3 Degeneration exit
To make the area cost vanish while remaining high amplitude, the branch must drive

\[
|J_\xi|\to0,
\]

which is precisely approach to rank-one/rank-loss geometry.

---

## 10. DSD audit

### Audit A — claiming kappa is negative at every rank-two point
Rejected.
The pointwise strict sign was derived at local maxima of `rho`; away from maxima `Delta rho/rho` can compensate.

### Audit B — replacing |J_xi| by j_xi without absolute-value inequality
Avoided.
Only `|j_xi| <= |J_xi|` is used.

### Audit C — treating the global negative budget as a contradiction
Rejected.
The CE-H field already requires a negative weighted mean kappa.
Rank-two geometry strengthens the amount but does not reverse the global sign requirement.

### Audit D — universal fixed local payer
Rejected without the stated high-amplitude and rank-separation bounds.

### Audit E — proof status
Rank two remains open.

---

## 11. Updated rank-two frontier

A recurrent rank-two survivor must choose between

\[
\boxed{
R_2^{separated}
\ \lor\ 
R_2^{rank-loss\ approach}.
}
\]

On `R_2^{separated}`, director area gives a coercive negative-kappa cost.
On `R_2^{rank-loss approach}`, the branch approaches the rank-one geometry already developed in M17-003--025.

Inside the separated branch the co-frozen split from M17-026 remains

\[
R_2^{parallel}
\ \lor\ 
R_2^{oblique}.
\]

---

## 12. Next target — co-frozen flux geometry

The next calculation is to exploit the fact that

\[
J_\xi
\quad\text{and}\quad
\widetilde W=W/a
\]

obey the same Cauchy transport law.

The high-value questions are:

1. what additional invariant is carried by the parallel branch `J_xi || W`;
2. whether the oblique branch forces a persistent two-direction material frame incompatible with bounded recurrent cross-sections, or merely another regular frozen-in geometry.

This is the **Rank-Two Co-Frozen Geometry Gate (R2CFG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
