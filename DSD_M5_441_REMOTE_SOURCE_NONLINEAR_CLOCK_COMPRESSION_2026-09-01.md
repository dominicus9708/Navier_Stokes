# DSD M5-441 — Remote-source nonlinear clock compression to the current first-hitting time

Date: 2026-09-01

Status: **DYNAMIC INTERPRETATION OF M5-440 / A GENUINELY REMOTE FIXED-FRACTION STRAIN PAYER HAS RELATIVE RMS VELOCITY `U_R >= c nu K^2/R`, SO ITS LOCAL NONLINEAR TURNOVER TIME `R/U_R` IS AT MOST `C r^2/nu`, THE SAME ORDER AS THE CURRENT FIRST-HITTING CORE TIME, EVEN THOUGH ITS VISCOUS TIME IS `R^2/nu = K^2 r^2/nu` / THEREFORE THE REMOTE PAYER IS NOT A PASSIVE SLOW OLD SHELL: IT IS A HIGH-REYNOLDS DYNAMIC OBJECT WHOSE NONLINEAR CLOCK IS COMPRESSED BY `K^2` / THE FORMER FROZEN-SHELL INTERPRETATION IS SUPERSEDED FOR ACTIVE FIXED-FRACTION STRAIN PAYERS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Remote-source oscillatory velocity scale

M5-437 gives for a remote source at physical radius

\[
R=Kr
\]

the Galilean-invariant local variance

\[
E_{osc}(R)
\gtrsim
\nu^2K^4R.
\]

The source domain has volume comparable to `R^3`. Define its RMS relative velocity by

\[
\boxed{
U_R
:=
R^{-3/2}E_{osc}(R)^{1/2}.
}
\]

Then

\[
\boxed{
U_R
\gtrsim
\frac{\nu K^2}{R}
=
\frac{\nu K}{r}.
}
\]

The corresponding first-hitting core natural velocity scale is `~nu/r`, so the remote source oscillation is at least a factor `K` larger in velocity amplitude.

---

## 2. Nonlinear turnover time

Define the shell-scale nonlinear turnover time

\[
\boxed{
\tau_{nl}(R)
:=
\frac{R}{U_R}.
}
\]

Using the lower velocity scale,

\[
\tau_{nl}(R)
\lesssim
\frac{R^2}{\nu K^2}.
\]

Since

\[
R=Kr,
\]

one obtains

\[
\boxed{
\tau_{nl}(R)
\lesssim
\frac{r^2}{\nu}.
}
\]

This is precisely the current target's natural parabolic/first-hitting time scale.

Thus the remote source does not evolve on its own large viscous time simply because its radius is large. Its required amplitude accelerates the nonlinear clock by exactly the compensating factor `K^2`.

---

## 3. Viscous time versus nonlinear time

The source viscous time is

\[
\boxed{
\tau_\nu(R)=\frac{R^2}{\nu}
=K^2\frac{r^2}{\nu}.
}
\]

Therefore

\[
\boxed{
\frac{\tau_\nu(R)}{\tau_{nl}(R)}
\gtrsim
K^2.
}
\]

Equivalently, the shell-scale Reynolds number based on the forced oscillatory velocity obeys

\[
\boxed{
Re_R
:=
\frac{U_RR}{\nu}
\gtrsim
K^2.
}
\]

A genuinely remote source is automatically a high-Reynolds source object.

---

## 4. Energy-turnover scale

The oscillatory energy is

\[
E_{osc}
\gtrsim
\nu^2K^4R.
\]

Dividing by the nonlinear time gives the characteristic nonlinear energy-processing rate

\[
\frac{E_{osc}}{\tau_{nl}}
\gtrsim
\nu^3\frac{K^6}{R}.
\]

Over one current target time `~r^2/nu`, this scale processes

\[
\left(
\nu^3\frac{K^6}{R}
\right)
\frac{r^2}{\nu}
=
\nu^2K^4R,
\]

which is the same order as `E_osc` itself.

Thus the amplitude required to source the target strain is exactly large enough for order-one shell energy turnover on a current first-hitting time.

This is a scaling statement, not a sign-definite energy-flux theorem, but it identifies the correct dynamic clock.

---

## 5. Correction to the old-shell picture

The earlier remaining-time argument noticed

\[
\frac{T_*-t_j}{R^2/\nu}
\lesssim
K^{-2}
\]

and therefore interpreted a remote shell as having only a tiny fraction of its **viscous** natural time left.

M5-440--441 show that an actual fixed-fraction strain payer cannot remain at ordinary shell amplitude. Its amplitude grows by `K^2`, so the relevant nonlinear time shrinks by the same factor:

\[
\boxed{
\frac{T_*-t_j}{\tau_{nl}(R)}
=O(1),
}
\]

rather than `O(K^-2)`.

Therefore the active remote source is dynamically current, not dynamically old.

A genuinely passive historical shell may still freeze after it ceases to pay the current strain, but that passive residue is not an independent source mechanism for the singular tower.

---

## 6. Relation to strong throughput

M5-440 already gives

\[
A_{rel}(R),\quad
R^{1/2}\|\nabla u\|_2,\quad
\|u\|_{\dot H^{1/2}}/\nu
\gtrsim
K^2.
\]

M5-441 adds the dynamic statement

\[
\boxed{
\tau_{nl}(R)
\lesssim
r^2/\nu.
}
\]

Hence the remote payer is a concrete realization of the strong critical-throughput branch:

- large relative amplitude;
- large derivative/enstrophy content;
- large critical Sobolev mass;
- current-stage nonlinear turnover.

It should no longer be represented by a separate quiet/frozen terminal in the master proof tree.

---

## 7. Firewall

The turnover-time calculation uses an RMS velocity scale and does not prove a signed outward or inward energy flux.

It therefore does not by itself contradict finite total energy.

Likewise `Re_R -> infinity` is entirely compatible with a hypothetical singularity.

The gain is classificatory and dynamical: a remote fixed-fraction payer cannot evade the proof tree by claiming to be a slow, passive, large-scale shell.

---

## 8. Audit verdict

### Derived

\[
\boxed{
U_R\gtrsim\nu K^2/R,
\qquad
Re_R\gtrsim K^2,
\qquad
\tau_{nl}(R)\lesssim r^2/\nu.
}
\]

### Removed interpretation

An active remote fixed-fraction strain source is not a quiet old-shell conveyor on the relevant nonlinear clock.

### Remaining hard problem

Exclude or rigidify the resulting strong scale-critical, high-Reynolds throughput itself.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
