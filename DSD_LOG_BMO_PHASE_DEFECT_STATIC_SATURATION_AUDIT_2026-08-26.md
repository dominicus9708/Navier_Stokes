# DSD Log-BMO Phase-Defect Static Saturation Audit

Date: 2026-08-26

Status: **ANTI-PROOF COUNTERMODEL PROVED AT THE KINEMATIC/SCALING LEVEL / LOG-BMO FAILURE CANNOT BE RELABELED AS H OR TEMPORAL PROJECTIVE ACTION / GLOBAL REGULARITY NOT PROVED.**

## 1. Purpose

`DSD_W1_CRITICAL_VORTICITY_LORENTZ_AND_PHASE_DEFECT_GATE_2026-08-26.md` shows that the W1 corridor automatically lies in the vorticity-critical Lorentz class
\[
\omega\in L_t^\infty L_x^{3/2,\infty}.
\]
A recent 2026 preprint gives a conditional regularity theorem if the vorticity direction additionally satisfies a uniform logarithmic-BMO condition.

It would be tempting to declare failure of that phase condition to be an existing `H` or projective-action event.  This note shows that such a declaration is not justified.

---

## 2. Fixed normalized phase template

Take a fixed smooth divergence-free normalized vorticity template `Omega_*` on a bounded ball, with
\[
|\Omega_*|\ge c_*>0
\]
on a smaller ball and with a nontrivial but smooth direction field
\[
\xi_*(y)=\frac{\Omega_*(y)}{|\Omega_*(y)|}.
\]
Assume there is a fixed ball `B_c` on which the mean oscillation has a positive lower bound
\[
\boxed{
\fint_{B_c}
|\xi_*- (\xi_*)_{B_c}|dy
\ge \delta_*>0.
}
\]

All fixed normalized derivatives may nevertheless be finite:
\[
\|\nabla^m\Omega_*\|_\infty<\infty
\qquad(m=0,1,2,\ldots).
\]
Thus the template is completely compatible with the first-hitting analytic corridor.

---

## 3. Shrinking physical realization

At a first-hitting scale `r_j->0`, realize the same normalized template by
\[
\omega_j(x)
=\frac{\nu}{r_j^2}
\Omega_*\!\left(\frac{x-X_j}{r_j}\right).
\]
On the nonzero-vorticity part,
\[
\boxed{
\xi_j(x)
=\xi_*\!\left(\frac{x-X_j}{r_j}\right).
}
\]
Consider the physical ball
\[
B_{c r_j}(X_j).
\]
By change of variables, its mean direction oscillation is scale invariant:
\[
\boxed{
\fint_{B_{cr_j}(X_j)}
|\xi_j-(\xi_j)_{B_{cr_j}}|dx
=
\fint_{B_c}
|\xi_*-(\xi_*)_{B_c}|dy
\ge\delta_*.
}
\]

---

## 4. Logarithmic-BMO norm diverges

For the weight
\[
\phi(r)=\frac1{|\log r|},
\]
the generalized BMO seminorm contains the factor
\[
\frac1{\phi(cr_j)}
\fint_{B_{cr_j}(X_j)}
|\xi_j-(\xi_j)_{B_{cr_j}}|dx.
\]
Hence
\[
\boxed{
\|\xi_j\|_{\mathrm{bmo}_{1/|\log r|}}
\gtrsim
\delta_*|\log r_j|
\to\infty.
}
\]
Thus a completely smooth fixed normalized phase pattern violates any uniform-in-time log-BMO direction bound solely because its physical scale shrinks.

---

## 5. Yet no normalized derivative-frequency explosion occurs

The normalized field is always the same template. Therefore
\[
\boxed{
\|\nabla_y^m\Omega_j\|_\infty
=\|\nabla^m\Omega_*\|_\infty
=O(1)
}
\]
for every fixed `m`.
Likewise, if the localized velocity template has finite scale-normalized derivative ratio,
\[
\Gamma_*
=\frac{R\|\nabla f_*\|_2}{\|f_*\|_2}<\infty,
\]
then the same value is inherited under first-hitting scaling.

Hence
\[
\boxed{
\text{uniform log-BMO phase failure}
\not\Rightarrow
H_{amp}
\text{ or }H_{freq}.
}
\]

---

## 6. Temporal projective action may also vanish

Suppose the normalized template is stationary or exactly recurrent at selected return times.  Its spatial direction defect remains fixed, but its temporal projective derivative at those states can vanish:
\[
\partial_s\xi_*=0
\]
in the stationary idealization, or can have zero net shape change over a recurrence cycle.

Thus
\[
\boxed{
\text{spatial log-BMO defect}
\not\Rightarrow
\text{positive temporal projective-speed floor}.
}
\]

A persistent spatial phase defect is a state property; the existing projective-action ledgers primarily price motion/reorganization of that state.  They are not identical notions.

---

## 7. Consequence for the current frontier

The external logarithmic-direction theorem, even if fully accepted after independent audit, yields the honest branch
\[
\boxed{
W1+\text{singularity}
\Longrightarrow
\text{logarithmically critical phase defect}.
}
\]
But that defect cannot be silently absorbed into `H` or `T/projective` using the repository's present estimates.

The remaining proof obligation would be genuinely dynamical:

> show that a fixed normalized phase defect cannot be maintained recurrently by the Navier-Stokes/Leray dynamics at the critical weak-Lorentz tail without paying an already finite budget.

The static/scaling countermodel proves that no argument based only on fixed normalized derivative amplitudes, shell-frequency ratios, or instantaneous spatial smoothness can establish this.

---

## 8. DSD audit status

Valid:
\[
W1\Longrightarrow
\omega\in L_t^\infty L_x^{3/2,\infty}.
\]

Conditional on the 2026 external theorem:
\[
W1+\text{singularity}
\Longrightarrow
\text{log-BMO direction failure}.
\]

Invalid without a new lemma:
\[
\text{log-BMO direction failure}
\Longrightarrow H
\quad\text{or}\quad T.
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
