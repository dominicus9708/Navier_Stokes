# DSD M5-516 — Rigid dual pair splits into moving-frame action or exact strain-diffusion cancellation

Date: 2026-09-01

Status: **RIGID-FRAME REDUCTION / M5-515 LEAVES A RIGID NONCOLLINEAR PAIR WITH CONSTANT RELATIVE ANGLE / SUCH A PAIR DEFINES AN ORTHONORMAL `SO(3)` FRAME WHOSE ANGULAR VELOCITY IS QUANTITATIVELY EQUIVALENT TO THE TWO ACTUAL DIRECTIONAL MATERIAL VELOCITIES / IF THE FRAME HAS POSITIVE MEAN ANGULAR SPEED, THE SAME PAIR CARRIES POSITIVE PROJECTIVE ACTION AND REJOINS THE PAIR-RATCHET BRANCH / IF THE FRAME HAS ZERO MEAN ANGULAR SPEED, ERGODICITY AND NONNEGATIVITY FORCE THE FRAME TO BE STATIONARY, SO EACH OF THE TWO LINEAGE DIRECTION EQUATIONS REDUCES EXACTLY TO `tau_i + D_i = 0` / THUS THE ONLY RIGID-PAIR ESCAPE IS AN ANCHORED NONCOLLINEAR FRAME MAINTAINED BY EXACT TRANSVERSE-STRAIN/PROJECTED-DIFFUSION CANCELLATION ON BOTH LINEAGES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-515

On the common ergodic component `mu_*`, M5-515 reduces the persistent dual pair `(a,b)` to

\[
\boxed{
\langle|c_{ab}'|\rangle>0
\quad\lor\quad
c_{ab}\equiv c_*,
\quad |c_*|<1.
}
\]

The first branch already forces positive same-pair transverse/diffusive action.

M5-516 analyzes the second, rigid-relative-angle branch.

Set

\[
s_*:=\sqrt{1-c_*^2}>0.
\]

---

## 2. Build the pair frame

Define

\[
e_1:=\xi_a,
\]

\[
e_2
:=
\frac{\xi_b-c_*\xi_a}{s_*},
\]

and

\[
e_3:=e_1\times e_2.
\]

Then

\[
R_{ab}:=(e_1,e_2,e_3)\in SO(3).
\]

Because `c_*` is constant,

\[
e_1'=\xi_a',
\]

and

\[
\boxed{
e_2'
=
\frac{\xi_b'-c_*\xi_a'}{s_*}.
}
\]

The frame angular-velocity matrix is

\[
\mathcal A_{ab}
:=
R_{ab}'R_{ab}^T
\in\mathfrak{so}(3).
\]

There is a unique vector

\[
\varpi_{ab}\in\mathbb R^3
\]

such that

\[
\boxed{
\mathcal A_{ab}v
=
\varpi_{ab}\times v
}
\]

for every vector `v`.

Thus

\[
\boxed{
e_i'=\varpi_{ab}\times e_i,
\qquad i=1,2,3.
}
\]

---

## 3. Pair directional velocities

For each persistent lineage, the material direction equation is

\[
\boxed{
\xi_i'
=
\tau_i+\mathcal D_i,
\qquad i=a,b,
}
\]

with

\[
\tau_i
=(I-\xi_i\otimes\xi_i)\Sigma_i\xi_i
\]

and

\[
\mathcal D_i
=
\rho_i^{-1}(I-\xi_i\otimes\xi_i)\Delta W_i.
\]

Define

\[
v_a:=\xi_a',
\qquad
v_b:=\xi_b'.
\]

Then

\[
v_i=\tau_i+\mathcal D_i.
\]

---

## 4. Angular speed is quantitatively equivalent to pair direction speed

For any orthonormal frame transported by angular velocity `varpi`,

\[
\sum_{j=1}^3|e_j'|^2
=2|\varpi|^2.
\]

Since

\[
e_1'=v_a,
\]

and

\[
e_2'
=(v_b-c_*v_a)/s_*,
\]

we obtain constants

\[
0<c_{frame}(c_*)
\le C_{frame}(c_*)<\infty
\]

such that

\[
\boxed{
c_{frame}
\bigl(|v_a|+|v_b|\bigr)
\le
|\varpi_{ab}|
\le
C_{frame}
\bigl(|v_a|+|v_b|\bigr).
}
\]

The constants remain finite because

\[
s_*>0.
\]

Thus common rigid-frame motion is not an independent hidden channel; it is exactly the combined directional motion of the two lineages.

---

## 5. Moving-frame branch forces same-pair projective action

Suppose

\[
\boxed{
\langle|\varpi_{ab}|\rangle_{\mu_*}>0.
}
\]

By the upper comparison above,

\[
\left\langle
|v_a|+|v_b|
\right\rangle
>0.
\]

Since

\[
|v_i|
=|\tau_i+\mathcal D_i|
\le
|\tau_i|+|\mathcal D_i|,
\]

we obtain

\[
\boxed{
\left\langle
|\tau_a|+|\tau_b|+|\mathcal D_a|+|\mathcal D_b|
\right\rangle
>0.
}
\]

Hence a moving rigid dual frame is again a same-pair ratchet/action branch.

The relative angle may be fixed, but the whole pair rotates and therefore pays projective motion.

---

## 6. Zero mean angular speed forces an anchored frame

Now suppose

\[
\boxed{
\langle|\varpi_{ab}|\rangle_{\mu_*}=0.
}
\]

Because `|varpi_ab|` is nonnegative,

\[
\varpi_{ab}=0
\]

for `mu_*`-almost every state/time.

Thus

\[
e_1'=e_2'=e_3'=0
\]

almost everywhere along the ergodic trajectory.

By continuity on the smooth compact support, the frame is stationary on the entire retained support:

\[
\boxed{
R_{ab}(\theta)
\equiv R_*.
}
\]

Equivalently,

\[
\boxed{
\xi_a'\equiv0,
\qquad
\xi_b'\equiv0.
}
\]

This is the **anchored rigid-pair branch**.

---

## 7. Exact strain-diffusion cancellation on an anchored pair

Insert

\[
\xi_i'=0
\]

into the exact direction equation:

\[
0
=
\tau_i+\mathcal D_i.
\]

Therefore

\[
\boxed{
\tau_a
=-\mathcal D_a,
\qquad
\tau_b
=-\mathcal D_b.
}
\]

This is an exact vector cancellation, not merely an averaged identity.

Consequently

\[
\boxed{
|\tau_a|=|\mathcal D_a|,
\qquad
|\tau_b|=|\mathcal D_b|.
}
\]

Any nonzero transverse strain on either anchored lineage must be matched pointwise in similarity time by an equal projected-diffusion vector in the opposite direction.

---

## 8. Two subcases of the anchored branch

The anchored branch itself has two possibilities.

### A. Passive anchored axes

\[
\tau_a=\mathcal D_a=0,
\qquad
\tau_b=\mathcal D_b=0.
\]

Then both persistent directions are instantaneous eigen-directions of their local strain tensors and receive no projected directional diffusion.

Their amplitudes and surrounding fields may still evolve.

### B. Actively balanced anchored axes

At least one lineage has

\[
|\tau_i|=|\mathcal D_i|>0
\]

on a positive-measure set.

Then transverse strain and projected diffusion continuously cancel in direction while each channel has positive absolute/squared activity.

Thus the direction is fixed only because two nonzero mechanisms exactly balance.

---

## 9. Squared balance on the active anchored subbranch

If, for example,

\[
\langle|\tau_a|^2\rangle>0,
\]

then exact cancellation gives

\[
\boxed{
\langle|\mathcal D_a|^2\rangle
=
\langle|\tau_a|^2\rangle
>0.
}
\]

After the same carrier-thickening argument used in M5-500 and M5-515, the pair pays simultaneous local PDE charges

\[
\boxed{
\left\langle
\int\rho_a^2|\tau_a|^2
\right\rangle>0,
}
\]

and

\[
\boxed{
\left\langle
\int|(I-\xi_a\otimes\xi_a)\Delta W|^2
\right\rangle>0.
}
\]

Thus the active anchored branch is more constrained than the generic ratchet branch: the two channels have matched pointwise direction vectors.

---

## 10. Symmetric-strain firewall

One might try to argue that two fixed noncollinear directions cannot both be compatible with a symmetric strain tensor.

That argument is invalid here because the two persistent packets generally occupy different spatial locations and therefore sample different tensors

\[
\Sigma_a
\ne
\Sigma_b.
\]

Two eigenvectors of one symmetric matrix have orthogonality/degeneracy constraints, but M5-491 already audited that one cannot silently replace `Sigma_a` and `Sigma_b` by one common matrix.

Therefore the passive anchored branch is not eliminated by elementary symmetric-matrix algebra.

---

## 11. Global-rotation firewall

Likewise, a moving pair frame

\[
R_{ab}(\theta)
\]

does not imply that the entire velocity field satisfies a rigid rotated-self-similar ansatz.

The frame angular velocity

\[
\varpi_{ab}(\theta)
\]

is a two-lineage local/genealogical observable, not the global RSS/RDSS parameter of Pineau--Vicol.

Thus no rotated Liouville theorem is imported at this step.

---

## 12. Final rigid-pair reduction

M5-515--516 give

\[
\boxed{
\mathcal R_{pair}^{rigid}
\Longrightarrow
\mathcal A_{frame}^{move}
\lor
\mathcal B_{pair}^{anchor},
}
\]

with

\[
\mathcal A_{frame}^{move}:
\quad
\langle|\varpi_{ab}|\rangle>0
\]

forcing positive same-pair projective action, while

\[
\mathcal B_{pair}^{anchor}:
\quad
\xi_a,\xi_b\text{ fixed and noncollinear},
\]

satisfies

\[
\boxed{
\tau_i=-\mathcal D_i
\quad(i=a,b).
}
\]

Therefore the only branch not already returned to positive pair motion is the anchored exact-cancellation branch.

---

## 13. Updated hard core

Inside the one coupled ergodic component from M5-514, the dual-pair geometry now satisfies

\[
\boxed{
\text{relative-angle motion}
\lor
\text{common-frame motion}
\lor
\text{anchored exact cancellation}.
}
\]

The first two branches carry positive same-pair directional action.

The third has two fixed nonparallel directions whose transverse strain and projected diffusion cancel exactly lineage by lineage.

This is the narrowest compact pair-level survivor obtained so far.

---

## 14. Highest-value next target

Audit the anchored branch against the finite-lineage production/flux cycle.

For each anchored lineage decompose

\[
\Sigma_i\xi_i
=
\sigma_i\xi_i+\tau_i,
\]

with

\[
\tau_i=-\mathcal D_i.
\]

The next question is whether positive recurrent axial production can coexist with two fixed noncollinear lineage axes and exact transverse strain-diffusion cancellation without forcing

- positive scalar flux oscillation;
- repeated carrier replacement;
- or a low-frequency/remote velocity decay defect.

This is now a sharply specified balance problem rather than an unspecified recurrence problem.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
