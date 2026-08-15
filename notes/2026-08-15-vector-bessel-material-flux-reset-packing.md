# Vector-valued Bessel packing for overlapping material-flux resets

Date: 2026-08-15

Status: **DERIVED MATERIAL-FLUX CARLESON PACKING UNDER UNIFORM BESSEL PROBE GEOMETRY / OVERLAP DOUBLE COUNTING REMOVED / NON-BESSEL CLUSTERING REMAINS.**

This note strengthens the scalar smooth material-flux reset cost.

The scalar estimate could be summed immediately only for disjoint or bounded-overlap reset intervals. The present lemma removes time-interval overlap entirely, provided the simultaneously active material probes form uniform `L2` Bessel families after their natural scale normalization.

The key point is to sum the occupancy and viscous-rate inequalities **before** integrating in time.

---

## 1. Physical material probes

Work in physical variables on a smooth interval before a hypothetical singular time `T*`.

For each candidate reset episode `j`, let

\[
I_j\subset[0,T^*)
\]

be its active time interval and let

\[
\ell_j>0
\]

be its physical coherent scale.

Let `psi_j(t)` solve the inviscid adjoint material equation on `I_j`:

\[
\boxed{
\partial_t\psi_j
+(u\cdot\nabla)\psi_j
+(\nabla u)^T\psi_j
=0.
}
\]

Define the smooth material-flux observable

\[
\boxed{
F_j(t)=\langle\omega(t),\psi_j(t)\rangle.
}
\]

The exact vorticity/adjoint cancellation gives

\[
\boxed{
F_j'(t)
=\nu\langle\omega(t),\Delta\psi_j(t)\rangle.
}
\]

Write

\[
F_j(t)=\Phi_j f_j(t),
\]

where `Phi_j>0` is the characteristic flux amplitude of the reset and `f_j` is dimensionless.

---

## 2. Natural probe normalization

A smooth flux probe at physical scale `ell` has the Euclidean scaling

\[
\|\psi\|_2^2\asymp\ell,
\qquad
\|\Delta\psi\|_2^2\asymp\ell^{-3}.
\]

Therefore define

\[
\boxed{
p_j(t)=\ell_j^{-1/2}\psi_j(t),
\qquad
k_j(t)=\ell_j^{3/2}\Delta\psi_j(t).
}
\]

Both are dimensionless `L2`-normalized probe shapes under bounded material distortion.

---

## 3. Uniform Bessel hypothesis

Assume that at every physical time `t`, the simultaneously active families satisfy

\[
\boxed{
\sum_{j:t\in I_j}
|\langle g,p_j(t)\rangle|^2
\le C_B\|g\|_2^2
}
\]

and

\[
\boxed{
\sum_{j:t\in I_j}
|\langle g,k_j(t)\rangle|^2
\le C_B\|g\|_2^2
}
\]

for every `g in L2(R3)`.

This is a phase-space packing assumption on the transported material probes, not a time-overlap assumption.

It is natural for

- dyadically separated dilates of one smooth probe;
- bounded-overlap translates at a fixed scale;
- bounded `C2` deformations of such families;

but it is not asserted here for an arbitrary infinitely clustered material family.

---

## 4. Simultaneous occupancy estimate

Since

\[
F_j
=\langle\omega,\psi_j\rangle
=\ell_j^{1/2}\langle\omega,p_j\rangle,
\]

we have

\[
\frac{|F_j|^2}{\ell_j}
=|\langle\omega,p_j\rangle|^2.
\]

Applying the Bessel inequality with `g=omega`,

\[
\boxed{
\sum_{j:t\in I_j}
\frac{\Phi_j^2}{\ell_j}|f_j(t)|^2
\le
C_B E_\omega(t),
}
\]

where

\[
E_\omega(t)=\|\omega(t)\|_2^2.
\]

Thus many overlapping nontrivial material fluxes cannot each charge the same enstrophy independently; the Bessel geometry performs the correct orthogonal packing.

---

## 5. Simultaneous viscous-rate estimate

Using

\[
F_j'
=\nu\langle\omega,\Delta\psi_j\rangle
=\nu\ell_j^{-3/2}\langle\omega,k_j\rangle,
\]

we obtain

\[
\frac{\ell_j^3|F_j'|^2}{\nu^2}
=|\langle\omega,k_j\rangle|^2.
\]

The second Bessel inequality therefore gives

\[
\boxed{
\sum_{j:t\in I_j}
\frac{\ell_j^3\Phi_j^2}{\nu^2}|f_j'(t)|^2
\le
C_B E_\omega(t).
}
\]

Again this is valid regardless of how many time intervals overlap, provided the active probes retain the Bessel phase-space geometry.

---

## 6. Integrate both ledgers

Define

\[
A_j=\int_{I_j}|f_j(t)|^2dt,
\qquad
B_j=\int_{I_j}|f_j'(t)|^2dt.
\]

Tonelli and the two simultaneous bounds yield

\[
\boxed{
\sum_j\frac{\Phi_j^2}{\ell_j}A_j
\le
C_B\int_0^{T^*}E_\omega(t)dt
}
\]

and

\[
\boxed{
\sum_j\frac{\ell_j^3\Phi_j^2}{\nu^2}B_j
\le
C_B\int_0^{T^*}E_\omega(t)dt.
}
\]

The global kinetic-energy identity makes the common right side finite.

---

## 7. Each genuine reset has a one-dimensional action gap

Suppose the reset changes `|f_j|` from at most `a` to at least `b`, with fixed

\[
0\le a<b.
\]

Absolute continuity gives

\[
\int_{I_j}|f_jf_j'|dt
\ge
\frac12(b^2-a^2).
\]

By Cauchy--Schwarz,

\[
\boxed{
\sqrt{A_jB_j}
\ge
\frac12(b^2-a^2)
=:c_{a,b}>0.
}
\]

This is the duration-free scalar reset gap.

---

## 8. Sum the reset gaps without interval-overlap loss

Apply Cauchy--Schwarz in the discrete index `j`:

\[
\begin{aligned}
&\sum_j
\frac{\Phi_j^2\ell_j}{\nu}
\sqrt{A_jB_j}\\
&\le
\left(
\sum_j\frac{\Phi_j^2}{\ell_j}A_j
\right)^{1/2}
\left(
\sum_j\frac{\ell_j^3\Phi_j^2}{\nu^2}B_j
\right)^{1/2}.
\end{aligned}
\]

Using the integrated Bessel ledgers,

\[
\sum_j
\frac{\Phi_j^2\ell_j}{\nu}
\sqrt{A_jB_j}
\le
C_B\int_0^{T^*}E_\omega(t)dt.
\]

Since every genuine reset has `sqrt(A_jB_j)>=c_ab`,

\[
\boxed{
\sum_j\Phi_j^2\ell_j
\le
\frac{C_B\nu}{c_{a,b}}
\int_0^{T^*}E_\omega(t)dt
<\infty.
}
\]

This is the desired **overlap-robust material-flux packing estimate**.

---

## 9. Apply to coherent Reynolds-one crossings

For a terminal crossing with normalized parameters `(W_j,R_j)`, the physical scale is

\[
\boxed{
\ell_j=\frac{R_j}{\sqrt{W_j}}.
}
\]

The signed flux is Navier--Stokes scale invariant and satisfies

\[
\boxed{
\Phi_j\asymp R_j^2.
}
\]

Hence

\[
\boxed{
\Phi_j^2\ell_j
\asymp
\frac{R_j^5}{\sqrt{W_j}}.
}
\]

With

\[
q_j=\frac{W_j}{R_j^{10}},
\]

this becomes

\[
\boxed{
\Phi_j^2\ell_j
\asymp q_j^{-1/2}.
}
\]

Therefore any infinite family of genuine fixed-fraction resets whose transported probes retain a uniform Bessel geometry must satisfy

\[
\boxed{
\sum_jq_j^{-1/2}<\infty,
}
\]

**without requiring the reset time intervals to be disjoint or of bounded multiplicity.**

---

## 10. What remains after this lemma

The earlier interval-overlap branch is removed under the Bessel probe condition.

The only way to reuse the same finite enstrophy action for infinitely many non-summable reset weights is now to violate the probe-frame geometry itself:

\[
\boxed{
\text{uniform Bessel failure}
}
\]

through one or more of

- arbitrarily dense same-scale material clustering;
- loss of spatial scale separation;
- severe material deformation of the probe shapes;
- higher-derivative folding that destroys the normalized frame bounds.

The last two are already routed to the material-probe `H2` derivative-collapse branch.

The first two require a stopping-time / phase-space pruning lemma distinguishing genuinely new reset events from repeated counting of one persistent flux structure.

---

## 11. Claim boundary

This is a Hilbert-space packing lemma under an explicit Bessel hypothesis. It does not assert that the full family of material probes arising from an arbitrary hypothetical singular solution automatically has a uniform Bessel constant.

Thus global regularity is not proved.

The new frontier is smaller:

\[
\boxed{
\text{super-separated summable Zeno}
\quad\lor\quad
\text{non-Bessel material clustering / probe distortion}.
}
\]

Status: **TIME-OVERLAP DOUBLE COUNTING CLOSED UNDER UNIFORM PROBE FRAME GEOMETRY / NON-BESSEL MATERIAL CLUSTERING IS THE ACTIVE PACKING TARGET.**