# Pairwise projective defect exactly measures angular partner supply

Date: 2026-08-18

Status: **EXACT DISCRETE/WEIGHTED PROJECTIVE IDENTITY PLUS A BOUNDED-GEOMETRY SOURCE CONSEQUENCE. IN A SAME-SCALE PACKET NETWORK WITH NO KERNEL-WEIGHT CONCENTRATION, ORDER-ONE CROSS-DIRECTION VORTEX-STRETCHING SUPPLY REQUIRES A POSITIVE PROJECTIVE DEFECT, HENCE A POSITIVE ANGULAR-VISCOUS COST. THE ESCAPE IS REACH/KERNEL-WEIGHT CONCENTRATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Packet direction covariance

Let `xi_i in S^2` be packet vorticity directions and `w_i>=0`, `sum_i w_i=1`, their normalized vorticity-energy weights.  Define

\[
C=\sum_iw_i\,\xi_i\otimes\xi_i.
\]

Then `C>=0` and `tr C=1`.  Define the projective dispersion

\[
J=1-\operatorname{tr}(C^2).
\]

## 2. Exact pairwise-angle identity

Because

\[
\operatorname{tr}(C^2)
=\sum_{i,j}w_iw_j(\xi_i\cdot\xi_j)^2,
\]

we obtain exactly

\[
\boxed{
J
=\sum_{i,j}w_iw_j
\left[1-(\xi_i\cdot\xi_j)^2\right]
=\sum_{i,j}w_iw_j\sin^2\theta_{ij}.
}
\]

Thus the projective defect is precisely the energy-weighted mean square pair angle, insensitive to sign reversal as required for a projective quantity.

## 3. Vortex-stretching partner angle

The geometric depletion form of the Biot--Savart vortex-stretching kernel contains a factor bounded by

\[
|\sin\theta_{ij}|.
\]

Consider a same-scale packet network in which

1. interacting packet separations remain comparable to the natural radius;
2. the remaining kernel/amplitude weights are uniformly comparable to the energy weights;
3. no vanishing subset of pairs carries an unbounded fraction of the Biot--Savart weight.

Then the dimensionless cross-direction source efficiency has the schematic bound

\[
\mathcal A_{\rm pair}
\lesssim
\sum_{i,j}w_iw_j|\sin\theta_{ij}|.
\]

Cauchy--Schwarz and the exact identity give

\[
\boxed{
\mathcal A_{\rm pair}
\lesssim
J^{1/2}.
}
\]

Therefore any bounded-geometry network supplying a fixed fraction `a0>0` of order-one same-scale stretching must satisfy

\[
\boxed{
J\ge c a_0^2>0.
}
\]

## 4. Angular damping consequence

On a thick natural unit cell, the existing projective Poincare estimate gives

\[
P_{\rm ang}\gtrsim EJ.
\]

The exact vorticity-magnitude identity contains

\[
-\nu P_{\rm ang}.
\]

Hence a bounded-geometry source-active partner network necessarily pays a fixed positive angular-viscous cost in normalized variables.

## 5. Escape = kernel-weight concentration / reach collapse

The bound above can fail only if the Biot--Savart source is concentrated on a set of pairs whose kernel weights are much larger than their energy weights.  At fixed packet scale this requires anomalously close approach, loss of bounded geometry, or a highly concentrated spatial partner configuration.

This is the already typed

\[
\boxed{
\text{reach collapse / spatial concentration branch}.
}
\]

Thus same-scale partner supply has the structural split

\[
\boxed{
\text{uniform projective roughness + angular damping}
\quad\lor\quad
\text{reach/kernel-weight concentration}.
}
\]

## 6. Limitation

A positive normalized angular-damping cost does not by itself contradict a hypothetical finite-time singularity: nonlinear stretching can replenish the loss.  The result removes a geometric free-source loophole but does not create a globally finite positive budget.

Status: **PAIRWISE PROJECTIVE DEFECT = MEAN-SQUARE PARTNER ANGLE / BOUNDED-GEOMETRY ORDER-ONE SOURCE FORCES J>=j0 AND ANGULAR DAMPING / ESCAPE = REACH CONCENTRATION / GLOBAL REGULARITY NOT PROVED.**