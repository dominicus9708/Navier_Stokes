# DSD M5-179 — Spectral-Infinity Local Order Comparison (Corrected)

Date: 2026-08-28

Status: **AUDIT CORRECTION / THE LOCAL FORWARD ORDER COMPARISON `angular principal damping >> z-weighted first-order transfer` IS CORRECT, AS IS THE GENEALOGICAL COMPETITION SCALE `|omega|~z^-3`; HOWEVER THIS DOES NOT GLOBALLY EXCLUDE ANGULAR SPECTRAL ENTRANCE BECAUSE BACKWARD NORMAL RECONSTRUCTION CAN ACCUMULATE LARGE IN-BAND PRINCIPAL AMPLIFICATION OVER A LONG NORMAL INTERVAL / THE PREVIOUS CLAIM THAT EVERY SURVIVOR MUST BE ULTRAGENEALOGICAL IS WITHDRAWN / GLOBAL REGULARITY UNPROVED.**

---

## 1. What remains correct

Use the exact frozen stable damping

\[
\Gamma_z(\omega,\ell)=\frac{u-1}{8\nu z}.
\]

The variable transport/stretching channel enters the forward `tau` equation with coefficient `z` and has cross-section differential order one.

Thus the raw transfer scale is

\[
\mathfrak T_z(\omega,\ell)
\lesssim
z(1+|\omega|+\ell).
\]

For angular-dominant high frequency,

\[
\Gamma_z^{ang}\sim c\ell,
\qquad
\mathfrak T_z^{ang}\lesssim z\ell,
\]

so locally in forward `tau`,

\[
\boxed{
\mathfrak T_z^{ang}/\Gamma_z^{ang}=O(z).
}
\]

For genealogical-dominant high frequency,

\[
\Gamma_z^{gen}\sim c_\nu z^{-1/2}|\omega|^{1/2},
\qquad
\mathfrak T_z^{gen}\lesssim z|\omega|,
\]

so local order-one competition begins near

\[
\boxed{|\omega|\sim z^{-3}.}
\]

These are valid **local forward rate comparisons**.

---

## 2. What was wrong in the previous version

The previous version promoted the local rate comparison into the global statement

\[
\text{angular spectral infinity cannot furnish a flat entrance}.
\]

That promotion is invalid.

A spectral entrance is a boundary-to-core reconstruction problem.  Even if the local forward transfer is smaller than local damping, a high-frequency mode can accumulate substantial principal amplification when reconstructed backward across a long interval of normal depth.

Therefore

\[
\boxed{
\text{local damping dominance}
\not\Rightarrow
\text{global exclusion of the channel}.
}
\]

This is the same class of error caught earlier in the correction to the first M5-161 factorial non-explosion argument: in-band amplification cannot be omitted from a global path audit.

---

## 3. Angular backward action

For a fixed large angular degree `ell`, define the principal backward normal action from the tail boundary to a fixed finite depth `z_0` by

\[
\mathcal A_\ell(z_0)
:=
\int_0^{z_0}\Gamma_z(0,\ell)\frac{dz}{z}.
\]

Let

\[
x:=\nu z\ell.
\]

For large `ell` at fixed `x`, the leading angular root geometry gives

\[
\Gamma_z(0,\ell)
\sim
\ell\,
\frac{\sqrt{1+16x^2}-1}{8x}.
\]

Therefore

\[
\mathcal A_\ell(z_0)
\sim
\ell
\int_0^{\nu z_0\ell}
\frac{\sqrt{1+16x^2}-1}{8x^2}\,dx.
\]

The integrand behaves as

\[
\frac1{2x}
\]

for large `x`.  Hence

\[
\boxed{
\mathcal A_\ell(z_0)
=
\frac\ell2\log\ell+O(\ell).
}
\]

Thus angular in-band backward amplification can be super-exponential in `ell`:

\[
\boxed{
\exp(\mathcal A_\ell)
\approx
\exp\left[\frac\ell2\log\ell+O(\ell)\right].
}
\]

Ordinary analytic spectral smallness `e^{-delta ell}` does not by itself dominate this action.

---

## 4. Genealogical backward action

For a fixed large genealogical frequency `omega`, define

\[
\mathcal A_\omega(z_0)
:=
\int_0^{z_0}\Gamma_z(\omega,0)\frac{dz}{z}.
\]

Set

\[
x:=\nu z|\omega|.
\]

At large `|omega|` with fixed `x`, the leading root geometry gives

\[
 u(x)
=
\sqrt{\frac{\sqrt{1+256x^2}+1}{2}}
\]

and

\[
\Gamma_z(\omega,0)
\sim
|\omega|\frac{u(x)-1}{8x}.
\]

Therefore

\[
\mathcal A_\omega(z_0)
\sim
|\omega|
\int_0^{\infty}
\frac{u(x)-1}{8x^2}\,dx.
\]

The integral is finite and equals

\[
\boxed{
\int_0^{\infty}
\frac{u(x)-1}{8x^2}\,dx
=\frac\pi2.
}
\]

One direct derivation is integration by parts:

\[
I
=\int_0^\infty\frac{u'(x)}{8x}\,dx
=\int_0^\infty\frac{8}{u(x)\sqrt{1+256x^2}}\,dx.
\]

With `16x=sinh t`, this becomes

\[
I
=\int_0^\infty\frac{dt}{2\cosh(t/2)}
=\int_0^\infty\operatorname{sech}y\,dy
=\frac\pi2.
\]

Hence

\[
\boxed{
\mathcal A_\omega(z_0)
=\frac\pi2|\omega|+o(|\omega|).
}
\]

Thus ordinary time-analytic decay `e^{-delta|omega|}` beats the pure principal backward action only if its analytic exponent is larger than the corresponding action constant; no such universal inequality has been established for the W1 class.

---

## 5. Correct interpretation

The spectral-infinity problem therefore has two distinct features:

1. local forward first-order transfer is weak relative to high-frequency principal damping;
2. global backward reconstruction can compensate very small transfer fractions by large in-band principal amplification.

Both must be included.

Consequently neither angular nor genealogical spectral infinity is removed by local order comparison alone.

The previous necessary statement

\[
|\omega|\gtrsim z^{-3}
\quad\text{for every survivor}
\]

is withdrawn.

The scale `|omega|~z^-3` remains meaningful only as the point where the **local forward** genealogical transfer rate becomes comparable to the local frozen damping rate.

---

## 6. DSD audit correction

### Formation — GREEN

The damping and action integrals come from the actual frozen stable root.

### Axis — GREEN

Local forward rates and global backward action are now separate channels.

### Static aggregation — CORRECTED

The previous version omitted accumulated in-band amplification when converting local rate dominance into a global channel exclusion.

### Dynamics — GREEN for the action asymptotics / YELLOW for full entrance

The action calculations are valid principal-mode asymptotics.  Full spectral entrance still requires coupling between modes and exact fast-memory bookkeeping.

### Cross-audit — GREEN AFTER CORRECTION

The correction is consistent with the earlier M5-161 repair: transfer and amplification must never be audited separately when making a global cascade claim.

---

## 7. Updated frontier

M5-176 and M5-177 remain valid:

\[
zN\to\infty,
\qquad
E\lesssim e^{-c/z}.
\]

M5-178 remains valid for every frozen finite-frequency canonical-tail generator.

The exact remaining issue is now

\[
\boxed{
\text{can analytic spectral seeds plus inter-band transfer and accumulated principal backward action}
\text{create a nonzero flat entrance from spectral infinity?}
}
\]

A correct next calculation must compare **total backward action**, not only local damping/transfer ratios.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
