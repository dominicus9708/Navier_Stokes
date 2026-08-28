# DSD M5-180 — Exact Principal Backward Action and Spectral-Regularity Thresholds

Date: 2026-08-28

Status: **P1_B^S SPECTRAL-INFINITY ACTION AUDIT / THE CORRECTED M5-179 PRINCIPAL ACTION GIVES A FINITE LINEAR GENEALOGICAL ACTION CONSTANT `pi/2` AND A SUPERLINEAR ANGULAR ACTION `(ell/2) log ell` / ORDINARY ANALYTICITY IS THEREFORE STRUCTURALLY INSUFFICIENT TO EXCLUDE ANGULAR SPECTRAL ENTRANCE BY AMPLITUDE ALONE / THE ACTION CALCULATION IDENTIFIES EXPLICIT SUFFICIENT SPECTRAL DECAY THRESHOLDS WITHOUT CLAIMING THEY ARE PRESENT IN W1 / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-179 was corrected because local forward damping dominance does not exclude global backward spectral entrance.

The correct object is the accumulated principal backward action

\[
\mathcal A_\lambda(z_0)
=
\int_0^{z_0}\Gamma_z(\lambda)\frac{dz}{z}.
\]

A spectral seed of size `exp(-Psi(lambda))` cannot be excluded by amplitude comparison unless `Psi(lambda)` dominates this action, together with any transfer-path cost.

The present note records the pure principal thresholds exactly.

---

## 2. Genealogical action

For `ell=0` and large `|omega|`, set

\[
x=\nu z|\omega|.
\]

Then

\[
\Gamma_z(\omega,0)
\sim
|\omega|
\frac{u(x)-1}{8x},
\]

where

\[
u(x)=\sqrt{\frac{\sqrt{1+256x^2}+1}{2}}.
\]

Thus

\[
\mathcal A_\omega(z_0)
=|\omega|
\int_0^{\nu z_0|\omega|}
\frac{u(x)-1}{8x^2}dx
+o(|\omega|).
\]

The integral converges as the upper limit tends to infinity.

Integration by parts gives

\[
I
=\int_0^\infty\frac{u'(x)}{8x}dx
=\int_0^\infty\frac{8}{u(x)\sqrt{1+256x^2}}dx.
\]

With

\[
16x=\sinh t,
\]

we have

\[
u(x)=\cosh(t/2),
\]

and hence

\[
I
=\int_0^\infty\frac{dt}{2\cosh(t/2)}
=\int_0^\infty\operatorname{sech}y\,dy
=\frac\pi2.
\]

Therefore

\[
\boxed{
\mathcal A_\omega(z_0)
=\frac\pi2|\omega|+o(|\omega|).
}
\]

---

## 3. Genealogical analytic threshold

Suppose an absolute genealogical spectral envelope has the form

\[
|\widehat F(\omega)|\lesssim e^{-\delta_t|\omega|}.
\]

Pure principal backward amplification has size

\[
\exp\left[\frac\pi2|\omega|+o(|\omega|)\right].
\]

Therefore a sufficient amplitude-only inequality against the **pure principal genealogical action** is

\[
\boxed{
\delta_t>\frac\pi2.
}
\]

No such numerical lower bound on the W1 time-analytic radius has been proved.

If `delta_t<=pi/2`, this action comparison alone cannot exclude genealogical entrance.

---

## 4. Angular action

For `omega=0` and large `ell`, set

\[
x=\nu z\ell.
\]

The leading damping is

\[
\Gamma_z(0,\ell)
\sim
\ell
\frac{\sqrt{1+16x^2}-1}{8x}.
\]

Thus

\[
\mathcal A_\ell(z_0)
\sim
\ell
\int_0^{\nu z_0\ell}
\frac{\sqrt{1+16x^2}-1}{8x^2}dx.
\]

For large `x`,

\[
\frac{\sqrt{1+16x^2}-1}{8x^2}
=\frac1{2x}+O(x^{-2}).
\]

Hence

\[
\boxed{
\mathcal A_\ell(z_0)
=\frac\ell2\log\ell+O(\ell).
}
\]

---

## 5. Angular spectral threshold

Ordinary angular analyticity gives only

\[
|\widehat F_\ell|\lesssim e^{-\delta_\theta\ell}.
\]

But

\[
e^{-\delta_\theta\ell}
\exp\left[\frac\ell2\log\ell+O(\ell)\right]
\]

does not tend to zero.

Thus **no fixed ordinary angular analytic radius can defeat the pure principal angular action by amplitude alone.**

A sufficient pure-action envelope is instead

\[
\boxed{
|\widehat F_\ell|
\lesssim
\exp[-\sigma\ell\log\ell],
\qquad
\sigma>\frac12,
}
\]

up to the lower-order `O(ell)` action constant.

A Gaussian spectral envelope

\[
e^{-a\ell^2}
\]

is more than sufficient but is not the sharp pure-action threshold.

---

## 6. Relation to current W1 regularity

The retained W1 inputs provide ordinary space/time analyticity after radius loss, i.e. exponential spectral tails.

They do **not** currently provide

\[
e^{-\sigma\ell\log\ell}
\]

angular tails, nor a verified numerical genealogical radius

\[
\delta_t>\pi/2.
\]

Therefore the existing analyticity inputs do not close spectral infinity by a direct seed-versus-principal-action comparison.

---

## 7. Transfer remains an additional channel

The thresholds above compare only a fixed high-frequency seed with in-band principal backward amplification.

A full entrance path also contains inter-band transfer.  Such transfer may cost additional small factors, but M5-161/M5-179 audits show that those costs cannot be counted independently of subsequent in-band amplification.

Hence the present thresholds are **sufficient pure-action barriers**, not a complete characterization of the coupled optimal path.

---

## 8. DSD audit

### Formation — GREEN

The actions are integrals of the actual exact frozen stable damping symbol.

### Axis — GREEN

Genealogical and angular spectral directions have distinct action laws and are not collapsed.

### Static aggregation — GREEN

Analytic seed suppression and principal amplification are compared in the same exponent ledger.  No transfer cost is double-counted.

### Dynamics — GREEN for pure-mode action / YELLOW for coupled entrance

The pure action asymptotics are closed.  Coupled inter-band spectral entrance remains open.

### Cross-audit — GREEN

This note corrects the overreach in the first M5-179 version and refines, rather than contradicts, the earlier M5-164 regularity-threshold observation.

---

## 9. Updated frontier

The existing W1 analytic class is not strong enough to eliminate spectral infinity by amplitude alone.

The next legitimate closure routes are therefore:

1. prove an NSE-specific transfer/action inequality stronger than ordinary analyticity;
2. prove a backward-uniqueness theorem for the exact stable Fuchsian system that bypasses spectral seed estimates;
3. derive stronger spectral regularity from the W1 dynamics itself.

No route is yet GREEN.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
