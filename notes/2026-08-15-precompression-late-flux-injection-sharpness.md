# Precompression followed by late viscous flux injection is the sharp escape of the reset-cost ledger

Date: 2026-08-15

Status: **VARIATIONAL SHARPNESS AUDIT / RESET PRICE q^-1/2 CANNOT BE IMPROVED FROM PROBE SCALE HISTORY ALONE / NEW COUPLING TARGET IDENTIFIED.**

This note asks whether the scalar smooth material-flux reset estimate can be strengthened merely by using the fact that the material probe may have been much larger earlier in the reset interval.

The answer is no without an additional coupling between probe deformation and future vorticity flux.

The adversarial strategy is simple:

\[
\boxed{
\text{precompress a nearly flux-free material probe}
\quad\longrightarrow\quad
\text{inject the flux only after the smallest scale is reached}.
}
\]

This realizes the smallest scale weight in the reset inequality and shows why the existing `q^-1/2` price is structurally sharp within this ledger.

---

## 1. Time-dependent material scale

Let a smooth material flux probe have instantaneous physical scale

\[
\ell(t).
\]

Assume bounded normalized shape, so that

\[
\boxed{
\|\psi(t)\|_2^2
\le C_0\ell(t),
\qquad
\|\Delta\psi(t)\|_2^2
\le C_2\ell(t)^{-3}.
}
\]

Define

\[
F(t)=\Phi f(t),
\]

where `Phi` is the final characteristic circulation/flux and `f` is the dimensionless flux fraction.

---

## 2. Instantaneous occupancy and viscous-rate bounds

Cauchy--Schwarz gives

\[
|F|^2
\le E_\omega\|\psi\|_2^2,
\]

hence

\[
\boxed{
E_\omega(t)
\ge
\frac{\Phi^2}{C_0\ell(t)}|f(t)|^2.
}
\]

The exact material-adjoint rate identity gives

\[
|F'|
\le
\nu E_\omega^{1/2}\|\Delta\psi\|_2,
\]

so

\[
\boxed{
E_\omega(t)
\ge
\frac{\Phi^2\ell(t)^3}{\nu^2C_2}|f'(t)|^2.
}
\]

---

## 3. Weighted duration-free action

Taking the geometric mean of the two lower bounds,

\[
\boxed{
E_\omega(t)
\ge
\frac{\Phi^2\ell(t)}{\nu\sqrt{C_0C_2}}
|f(t)f'(t)|.
}
\]

Therefore

\[
\boxed{
\nu\int_I E_\omega(t)dt
\ge
c\Phi^2
\int_I\ell(t)|f(t)f'(t)|dt.
}
\]

Let

\[
\ell_{\min}=\inf_{t\in I}\ell(t).
\]

If `|f|` changes from at most `a` to at least `b`, then

\[
\int_I|ff'|dt
\ge\frac12(b^2-a^2),
\]

and hence

\[
\boxed{
\nu\int_I E_\omega dt
\ge
c_{a,b}\Phi^2\ell_{\min}.
}
\]

---

## 4. Coherent crossing specialization

At the final coherent crossing,

\[
\Phi\asymp R^2,
\qquad
\ell_{\min}\sim\ell_c=R/\sqrt W.
\]

Therefore

\[
\boxed{
\Phi^2\ell_c
\asymp
\frac{R^5}{\sqrt W}
=q^{-1/2},
\qquad q=W/R^{10}.
}
\]

Thus allowing the probe to have a much larger parent scale earlier does not automatically improve the universal lower bound.

The integral is weighted by `ell(t)`, and the flux variation can in principle be concentrated near the time when `ell(t)` is smallest.

---

## 5. Adversarial minimizer

The abstract minimizing strategy is

1. while `ell(t)` is large, keep
   \[
   f(t)\approx0;
   \]
2. use strain/deformation to shrink the material probe to `ell_c`;
3. only then change
   \[
   f:0\to1
   \]
   through viscous flux transfer.

Then

\[
\int\ell|ff'|dt
\approx
\ell_c\int|ff'|dt,
\]

and the lower bound is only

\[
\boxed{
\nu\int E_\omega dt
\gtrsim
\Phi^2\ell_c
=q^{-1/2}.
}
\]

Therefore a larger parent scale, by itself, does not force an order-one reset cost.

---

## 6. Why this matters for the power-law Zeno family

The adversarial family

\[
q=W^\alpha,
\qquad 0<\alpha<1,
\]

has reset price

\[
q^{-1/2}=W^{-\alpha/2},
\]

which is summable on geometric first-hitting levels.

The present sharpness audit shows that this decay cannot be removed merely by replacing the terminal scale by an earlier, larger material scale in the scalar reset inequality.

A proof needs an additional statement preventing the future flux from remaining negligible throughout the precompression phase.

---

## 7. New missing theorem: precompression--future-flux coupling

The exact new target is a statement of the schematic form

\[
\boxed{
\text{large future coherent flux}
+\text{large prior material compression}
\Longrightarrow
\text{nontrivial flux already present during compression}
\lor
\text{another critical source cost}.
}
\]

If one could prove that `f(t)` must remain bounded below by a positive function while `ell(t)` decreases through a large scale ratio, then the weighted action

\[
\int\ell(t)|ff'|dt
\]

would acquire a parent-scale gain.

Alternatively, if `f` can stay tiny, one must identify the mechanism that injects `O(Phi)` circulation at the end and charge that injection to a scale-invariant derivative/strain quantity that is not physically summable in a Zeno cascade.

---

## 8. PDE interpretation

The vorticity equation is homogeneous in vorticity for a prescribed velocity field,

\[
D_t\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

Thus a nearly vorticity-free material core cannot generate circulation from an algebraic source independent of surrounding vorticity. Late flux injection must arrive through

- viscous diffusion across the material boundary;
- strong gradients / opposite-polarity shielding;
- or prior non-negligible vorticity compressed by strain.

These are precisely the channels that a future coupling theorem must quantify jointly rather than separately.

---

## 9. Claim boundary

This note does not prove that the adversarial precompression strategy is realized by Navier--Stokes.

It proves only that the current scalar occupancy-plus-viscous-rate inequalities do not exclude it.

Therefore any claimed improvement that replaces `q^-1/2` by a larger reset cost must use genuinely new PDE information coupling material deformation to vorticity transport; scale history alone is insufficient.

Status: **CURRENT RESET COST IS SHARP UNDER DECOUPLED PRECOMPRESSION/INJECTION / FINAL ACTIVE TARGET = MATERIAL PRECOMPRESSION--FUTURE-FLUX COUPLING.**