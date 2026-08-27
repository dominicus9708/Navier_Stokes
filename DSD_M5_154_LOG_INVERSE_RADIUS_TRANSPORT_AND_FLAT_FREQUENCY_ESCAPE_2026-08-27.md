# DSD M5-154 — Log-Inverse-Radius Transport and Necessary Flat-Fiber Frequency Escape

Date: 2026-08-27

Status: **P1_B^S DYNAMIC REFINEMENT / THE FIXED-TIME INVERSE-RADIUS VORTICITY EQUATION IS REWRITTEN IN `tau=log xi`, WHERE THE LEADING OPERATOR IS THE ISOMETRIC TRANSPORT `partial_s+partial_tau` AND EVERY VISCOUS/ANGULAR/COMMON-TAIL CORRECTION IS MULTIPLIED BY `e^-tau`; CONSEQUENTLY A NONZERO SUPERALGEBRAICALLY FLAT FIBER CANNOT LIVE IN ANY UNIFORMLY BOUNDED CROSS-SECTION FREQUENCY BAND AND MUST ESCAPE TO PARABOLICALLY GROWING FREQUENCIES / GLOBAL REGULARITY UNPROVED.**

---

## 1. Starting equation

Use M5-153.  For a same-tail relative vorticity field write

\[
\Omega_U-\Omega_V=r^{-2}K(\xi,s,\theta),
\qquad \xi=r^2.
\]

The exact scaled equation is

\[
K_s+\xi K_\xi-4\nu\xi K_{\xi\xi}+2\nu K_\xi
-\frac\nu\xi(2+\Delta_{S^2})K
+\frac1\xi\mathcal N_s=0.
\]

Here `mathcal N_s` is the relative transport/stretching channel.  On the W1 far corridor it is linear in the pair difference once the two bounded recurrent backgrounds are fixed.

---

## 2. Log inverse-radius coordinate

Set

\[
\boxed{\tau:=\log\xi.}
\]

Then

\[
\xi\partial_\xi=\partial_\tau,
\]

and

\[
\xi K_{\xi\xi}
=e^{-\tau}(K_{\tau\tau}-K_\tau),
\qquad
K_\xi=e^{-\tau}K_\tau.
\]

Therefore

\[
\boxed{
K_s+K_\tau
=e^{-\tau}
\left[
4\nu K_{\tau\tau}-6\nu K_\tau
+\nu(2+\Delta_{S^2})K
-\mathcal N_s
\right].
}
\]

This equation is exact.

---

## 3. Leading transport

As `tau -> +infinity`, the right-hand side carries the integrable coefficient

\[
e^{-\tau}.
\]

The limiting normal equation is therefore

\[
\boxed{K_s+K_\tau=0.}
\]

Its solutions are translations along the characteristics

\[
q=s-\tau,
\qquad
K(\tau,s)=F(q).
\]

On Branch `P1_B^S`, the pair flow is measured by an invariant probability measure.  Translation in `s` is therefore isometric in the associated `L^2` pair space.

Hence the leading equation has no decaying normal mode: it transports cross-section amplitude without changing its invariant norm.

This is the log-coordinate counterpart of the M5-146/M5-148 statement that the normal constant-coefficient operator has no stable eigenvalue.

---

## 4. Fixed cross-section frequency cannot generate flatness

Consider first any finite-dimensional spectral sector in the pair-time/angular variables, or more generally a sector on which

\[
\|K_{\tau\tau}\|+\|K_\tau\|+\|\Delta_{S^2}K\|+\|\mathcal N_s\|
\le C_\Lambda\|K\|
\]

with `C_Lambda` independent of `tau`.

Along a characteristic of `partial_s+partial_tau`, the exact equation then gives

\[
\left\|\frac d{d\tau}K(\tau,s(\tau))\right\|
\le C_\Lambda e^{-\tau}\|K\|.
\]

The coefficient is integrable:

\[
\int_{\tau_0}^\infty e^{-\tau}d\tau<\infty.
\]

Thus the characteristic evolution converges to an invertible finite limit operator.  A nonzero cross-section state cannot be driven to zero superalgebraically by such an integrable perturbation.

Consequently

\[
\boxed{
\text{a nonzero flat fiber cannot remain in any fixed bounded frequency sector.}
}
\]

---

## 5. Necessary high-frequency balance

Suppose a cross-section frequency scale is denoted by `Omega(tau)`.

The largest viscous normal term has relative size

\[
e^{-\tau}\Omega(\tau)^2|K|.
\]

If

\[
e^{-\tau}\Omega(\tau)^2
\in L^1(d\tau),
\]

then its cumulative effect remains finite and the preceding finite-distortion argument persists.

Therefore a necessary condition for an actually decaying flat fiber is

\[
\boxed{
\int^{\infty}e^{-\tau}\Omega(\tau)^2d\tau=\infty.
}
\]

In particular the fiber must reach, along arbitrarily large ages, at least the parabolic frequency scale

\[
\boxed{
\Omega(\tau)\gtrsim e^{\tau/2}=\sqrt\xi=r.
}
\]

up to slowly varying factors.

This is a **necessary escape scale**, not a sufficient construction.

---

## 6. Relation to the earlier physical frequency escape

M5-116 showed that a noninjective same-tail fiber must escape to physical frequency

\[
k_{phys}\sim (T_*-t)^{-1/2}.
\]

The present result is the normal/genealogical counterpart:

\[
\boxed{
\text{flatness at }r\to\infty
\Longrightarrow
\text{cross-section frequency must rise at least like }r.
}
\]

Both statements say that noninjectivity cannot survive at a fixed resolution.

The fiber, if nonzero, must continually transfer its distinguishability to the parabolic resolution scale.

---

## 7. Why analytic compactness does not yet close the escape

Uniform analyticity of the compact W1 class gives exponential smallness of high-frequency coefficients, schematically

\[
|\widehat K(\Omega)|\lesssim e^{-\delta\Omega}.
\]

At the required frequency

\[
\Omega\sim e^{\tau/2},
\]

this produces

\[
e^{-\delta e^{\tau/2}},
\]

which is itself superalgebraically flat in `xi=e^tau`.

Thus analytic compactness is **compatible** with the amplitude scale required by the escape.

This is the frequency-space version of the M5-152 firewall: small amplitude cannot be used to bound frequency-to-amplitude ratios.

---

## 8. DSD four-chain audit

### Formation — GREEN

The escape is derived from the exact M5-153 equation, not imposed as an additional ansatz.

### Axis — GREEN

`tau=log xi` is used only to expose the asymptotic transport structure.  Pair time `s`, radial age `tau`, and angular frequency remain distinct channels.

### Static aggregation — GREEN

The integrable `e^-tau` coefficient is not accumulated as an order-one cost at every log shell.

### Dynamics — GREEN

The result is a necessary condition: bounded-frequency fibers are excluded, while high-frequency escape remains open.

### Cross-audit — GREEN

The conclusion agrees with M5-116 and M5-152 rather than silently replacing them.

---

## 9. Updated Branch-S frontier

Branch `P1_B^S` is no longer merely

\[
\text{flat radial solution?}
\]

It is now

\[
\boxed{
\text{Can the homogeneous same-tail relative NSE sustain an invariant nonzero fiber whose entire distinguishability}
\text{ runs to }\Omega(\tau)\gtrsim e^{\tau/2}\text{ while its amplitude becomes superalgebraically small?}
}
\]

Any closure must control this parabolic cross-section frequency cascade.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
