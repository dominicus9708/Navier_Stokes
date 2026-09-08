# DSD M17-396 — The M17-395 `Phi^2/R` log-diffusion cost is exactly parabolically critical, not supercritical, and requires a finite ancestral budget or nonsummable normalized multiplicity

Date: 2026-09-08  
Canonical ID: **M17-396**

Status: **ACTIVE SCALING AUDIT / M17-395 INTERPRETATION CORRECTION / CRITICAL-CHARGE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why this audit is necessary

M17-395 proves on the retained positive-flux intrinsic coefficient-gradient branch that

\[
\nu
\int_{I_R}
\int_B
\rho^2|\nabla\log|\kappa||^2dxdt
\gtrsim
\Phi_*^2R^{-1}.
\]

The physical quantity grows as `R -> 0`.

However, physical growth alone does not determine whether a quantity is supercritical.

The correct test is its exact Navier--Stokes parabolic scaling.

## 2. Parabolic scaling dictionary

Normalize a physical scale-`R` episode by

\[
y=\frac{x-x_0}{R},
\qquad
s=\frac{t-t_0}{R^2}.
\]

The normalized vorticity and CE-H coefficient are

\[
\Omega_R(y,s)
=R^2\Omega(x,t),
\]

\[
\kappa_R(y,s)
=R^2\kappa(x,t).
\]

Hence

\[
\rho_R=R^2\rho.
\]

For the logarithmic coefficient,

\[
\log|\kappa_R|
=
\log|\kappa|+2\log R.
\]

Therefore the constant shift disappears under differentiation:

\[
\boxed{
\nabla_y\log|\kappa_R|
=R\nabla_x\log|\kappa|.
}
\]

Also

\[
dy=R^{-3}dx,
\qquad
 ds=R^{-2}dt.
\]

## 3. Exact scaling of the spacetime log-diffusion charge

Define the physical spacetime charge

\[
\mathscr D_{\log\kappa}^{ph}(I_R)
:=
\int_{I_R}\int
\rho^2
|\nabla_x\log|\kappa||^2dxdt.
\]

For the normalized solution,

\[
\begin{aligned}
\mathscr D_{\log\kappa}^{norm}
&=
\int\int
\rho_R^2
|\nabla_y\log|\kappa_R||^2dyds\\
&=
\int\int
R^4\rho^2
\cdot
R^2|\nabla_x\log|\kappa||^2
\cdot
R^{-3}dx
\cdot
R^{-2}dt.
\end{aligned}
\]

Thus

\[
\boxed{
\mathscr D_{\log\kappa}^{norm}
=
R\,
\mathscr D_{\log\kappa}^{ph}.
}
\]

Equivalently,

\[
\boxed{
\mathscr D_{\log\kappa}^{ph}
=R^{-1}
\mathscr D_{\log\kappa}^{norm}.
}
\]

The physical `R^{-1}` factor is therefore exactly the canonical scaling factor of this charge.

## 4. Reinterpretation of M17-395

M17-395 gives

\[
\nu\mathscr D_{\log\kappa}^{ph}
\gtrsim
\Phi_*^2R^{-1}.
\]

Multiply by `R`:

\[
\boxed{
\nu\mathscr D_{\log\kappa}^{norm}
\gtrsim
\Phi_*^2.
}
\]

Therefore the M17-395 positive-flux lower bound is a fixed positive **scale-critical normalized charge**.

It is not a supercritical blow-up merely because its physical representative grows as `R^{-1}`.

The correct interpretation is

\[
\boxed{
\text{positive flux}
+\text{intrinsic coefficient diffusion}
\Longrightarrow
\text{order-one normalized log-diffusion payment per retained episode}.
}
\]

## 5. Centered entropy has the same critical normalization

M17-395 defines

\[
\zeta_R=\log(R^2|\kappa|)
\]

and

\[
\mathcal H_R^{ph}
=
\int\chi\rho^2\zeta_Rdx.
\]

Under the same parabolic scaling,

\[
\rho_R^2d y
=R\rho^2dx.
\]

Since `zeta_R` becomes the unit-scale centered logarithm,

\[
\boxed{
\mathcal H^{norm}
=R\mathcal H_R^{ph}.
}
\]

Thus the physical endpoint entropy size

\[
\mathcal H_R^{ph}\sim\Phi_*^2/R
\]

is also exactly scale-critical when the positive-flux packet has fixed normalized mass.

The same applies to every term in the time-integrated centered log-entropy identity after the correct `R` normalization.

Therefore the M17-395 source/entropy payers are naturally compared in one dimensionless normalized ledger.

## 6. Why one order-one payment per generation is not a contradiction

Suppose geometrically shrinking episodes produce

\[
\mathscr D_{\log\kappa,j}^{norm}
\ge d_*>0
\]

for infinitely many `j`.

This gives infinitely many normalized critical payments.

But no theorem currently states that

\[
\sum_j
\mathscr D_{\log\kappa,j}^{norm}
<\infty.
\]

The standard kinetic-energy inequality controls a different quantity.

Therefore

\[
\boxed{
\text{infinitely many order-one normalized log-diffusion payments}
\not\Rightarrow
\text{contradiction}
}
\]

without an independent finite ancestral budget, bounded-multiplicity theorem in a single controlled measure, or rigidity result.

This is the same structural warning that appeared earlier for normalized palinstrophy payments.

## 7. Cross-generation requirement

A successful closure through M17-395 must establish at least one of the following:

1. **finite ancestral budget**
   \[
   \sum_j\mathscr D_{\log\kappa,j}^{norm}<\infty;
   \]
2. **physical weighted budget** whose exact record scaling makes repeated normalized payments nonsummable;
3. **recurrence rigidity** preventing the same normalized entropy/source architecture from servicing infinitely many episodes;
4. **nonsummable multiplicity/growth** causing the normalized charge itself to diverge with `j`;
5. a forced exit to flux thinning, gradient spike, zero crossing, interface, or genealogy loss.

No item in this list is currently certified globally.

## 8. Multiplicity version

Suppose at one normalized generation there are `M_j` genuinely disjoint positive-flux M17-235 cells, each carrying

\[
\nu\mathscr D_{\log\kappa}^{norm}
\ge d_*.
\]

Then additivity gives

\[
\nu\mathscr D_{\log\kappa,j}^{norm,total}
\ge d_*M_j.
\]

Thus large disjoint multiplicity amplifies the normalized critical charge linearly.

But again, to turn this into a contradiction one needs a finite or otherwise controlled total normalized log-diffusion budget.

The mere statement

\[
M_j\to\infty
\]

is a genuine decompactification signal, not yet a finite-energy contradiction.

## 9. Relation to M17-307 firewall

M17-307 established that fixed normalized descendant palinstrophy payments can pull back with a summable inverse-record-scale weight.

M17-396 does not assert that log-diffusion has the same scaling exponent as palinstrophy.

Instead it performs the scaling calculation directly and finds its own critical normalization

\[
R\mathscr D_{\log\kappa}^{ph}.
\]

Any future cross-generation summation must use this exact scaling and must not borrow the M17-307 weight without derivation.

## 10. Corrected interpretation of the M17-395 escalation

The statement

\[
\mathscr D_{\log\kappa}^{ph}
\gtrsim
\Phi_*^2R^{-1}
\]

remains mathematically correct.

The phrase `grows on small scales` is also literally correct in physical units.

But the canonical proof interpretation is now sharpened to

\[
\boxed{
\text{physical }R^{-1}\text{ growth}
=
\text{fixed positive parabolically normalized charge}.
}
\]

Thus M17-395 removes the low-amplitude firewall on its positive-flux subbranch, but M17-396 shows that it reaches a **critical-charge firewall**, not a supercritical contradiction.

## 11. Revised late coefficient-gradient branch

The branch now reads

\[
\boxed{
\begin{aligned}
H_{positive\ flux+intrinsic\ coefficient\ diffusion}
\Longrightarrow{}&
H_{fixed\ positive\ normalized\ log\text{-}diffusion}\\
&\to H_{normalized\ entropy/source\ payer}\\
&\lor G_{flux\ thinning}\\
&\lor G_{gradient\ spike}\\
&\lor H_{zero\ crossing}\\
&\lor G_{interface/domain/genealogy}.
\end{aligned}
}
\]

The remaining proof obligation is a finite-budget or rigidity theorem for the normalized log-diffusion/entropy/source architecture.

## 12. DSD audit role

The DSD role is a scale-currency audit.

A quantity that diverges in physical units may still represent the same order-one normalized object at every scale.

The exact parabolic scaling must be computed before declaring supercritical growth.

The canonical calculation above uses only the Navier--Stokes scaling dictionary.

## 13. Audit verdict

**PASS-CORRECTION — M17-395 is scale-critical, not supercritical.**

The exact invariant payment is

\[
\boxed{
R
\int_{I_R}\int
\rho^2|\nabla\log|\kappa||^2dxdt
\gtrsim
\Phi_*^2.
}
\]

The next highest-value target is therefore not another local lower bound of the same scale.

It is a genuine **ancestral-budget / recurrence-rigidity / source-return theorem** for this normalized critical charge.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
