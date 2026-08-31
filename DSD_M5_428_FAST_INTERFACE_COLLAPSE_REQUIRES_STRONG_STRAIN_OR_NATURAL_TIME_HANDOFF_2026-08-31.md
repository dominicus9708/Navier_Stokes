# DSD M5-428 — Fast interface collapse requires strong strain; otherwise handoff occurs on natural time

Date: 2026-08-31

Status: **INTERFACE-SPEED REDUCTION / ON A FIRST-HITTING ACTIVE CARRIER WITH `|Omega|>=lambda0`, STAGE-WIDE ANALYTICITY BOUNDS THE NORMALIZED LAPLACIAN AND THEREFORE BOUNDS AMPLITUDE, DIRECTION, AND MATERIAL-FLUX CHANGE RATES WHenever LOCAL STRAIN IS BOUNDED / AN ORDER-ONE REORIENTATION, FLUX LOSS, OR SOURCE-STATE REFORMATION CANNOT OCCUR IN VANISHING NORMALIZED TIME WITHOUT STRAIN ESCALATION / STRAIN ESCALATION ALREADY ROUTES BY M5-400--402 TO STRONG/DELOCALIZED CRITICAL MASS OR REMOTE ACTIVITY / NATURAL-TIME INTERFACE EVENTS FALL BACK INTO THE RECURRENT/FRESH-STATE ANALYSIS OF M5-426--427 / THUS `H_strong interface` IS NOT AN INDEPENDENT FAST TERMINAL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Work in a late first-hitting parent normalization.

On every formed active main/source carrier there is a fixed amplitude floor

\[
\boxed{|\Omega|\ge\lambda_0>0}
\]

on a fixed normalized subregion, by the Taylor/analyticity constructions used in M5-390 and M5-394.

M5-392 gives

\[
\boxed{
\|\Delta\Omega\|_{L^\infty}
\le C_2
}
\]

throughout the stage, with `C2` independent of the late stage index.

---

## 2. Vorticity-vector change rate

The normalized vorticity equation has the form

\[
D_\tau\Omega
=
\Sigma\Omega+\Delta\Omega
\]

(up to the fixed viscosity normalization convention).

On the first-hitting stage

\[
|\Omega|\le q
\]

and therefore, if the local strain satisfies

\[
\|\Sigma\|_{L^\infty(\mathcal C)}\le B,
\]

then on the active carrier

\[
\boxed{
|D_\tau\Omega|
\le qB+C_2
=:M_\Omega(B).
}
\]

Hence an order-one change

\[
|\Omega(\tau_1)-\Omega(\tau_0)|\ge\delta_\Omega
\]

along a retained material trajectory requires

\[
\boxed{
|\tau_1-\tau_0|
\ge
\frac{\delta_\Omega}{M_\Omega(B)}.
}
\]

Thus bounded strain prevents arbitrarily fast amplitude/source-state collapse.

---

## 3. Direction change rate

On the active set, define

\[
\xi=\frac{\Omega}{|\Omega|}.
\]

Projecting the vorticity equation orthogonally to `xi` gives

\[
D_\tau\xi
=
(I-\xi\otimes\xi)\Sigma\xi
+
\frac1{|\Omega|}
(I-\xi\otimes\xi)\Delta\Omega.
\]

Therefore

\[
\boxed{
|D_\tau\xi|
\le
B+\frac{C_2}{\lambda_0}
=:M_\xi(B).
}
\]

An order-one axis rotation

\[
|\xi(\tau_1)-\xi(\tau_0)|\ge\delta_\xi
\]

requires

\[
\boxed{
|\tau_1-\tau_0|
\ge
\frac{\delta_\xi}{M_\xi(B)}.
}
\]

Thus a projective/source-axis interface cannot rotate through a fixed angle in `o(1)` normalized time unless the local strain loses its bounded corridor.

---

## 4. Material-surface flux change rate

Let `S(\tau)` be a material cross-section retained inside a formed natural carrier.

The exact flux identity is

\[
\frac d{d\tau}
\int_{S(\tau)}\Omega\cdot n\,dA
=
\int_{S(\tau)}\Delta\Omega\cdot n\,dA
\]

in normalized variables.

As long as the cross-section stays in the formed natural geometry, its normalized area is bounded above by a fixed constant `A_*`.

Therefore

\[
\boxed{
\left|
\frac d{d\tau}\Phi_S(\tau)
\right|
\le
C_2A_*.
}
\]

A fixed flux change

\[
|\Delta\Phi_S|\ge\phi_*>0
\]

requires

\[
\boxed{
\Delta\tau
\ge
\frac{\phi_*}{C_2A_*}
}
\]

unless the surface itself leaves/deforms out of the retained natural geometry.

Rapid loss of the geometry is again a strain/deformation interface event.

---

## 5. Fast disappearance of the source packet

M5-394 forms a source packet with fixed normalized radius, amplitude, angular separation, and signed flux.

To destroy this packet in a normalized time `delta tau -> 0`, at least one of the following must occur:

1. its vorticity amplitude changes by a fixed amount;
2. its axis rotates by a fixed amount;
3. its fixed flux changes by a fixed amount;
4. the material geometry is deformed/exported out of the fixed natural window.

The first three are impossible in vanishing normalized time under bounded `Sigma` by Sections 2--4.

The fourth is itself controlled by the deformation gradient and requires large strain action when it occurs on a vanishing clock.

Hence

\[
\boxed{
\text{fast order-one interface collapse}
\Longrightarrow
H_{strain}^{strong}.
}

---

## 6. Route strong strain to the existing delocalized branch

M5-400 gives a parent-scale Calderon--Zygmund bound of the form

\[
\|\Sigma\|_\infty
\lesssim
C_1+Z^{1/2}
\]

with fixed local analytic contribution.

Therefore pointwise parent strain escalation forces normalized enstrophy/critical mass escalation.

M5-401 then routes that escalation to remote active shells/relative-frequency critical activity.

The satellite analogue is M5-402.

Thus

\[
\boxed{
H_{strain}^{strong}
\Longrightarrow
C_{strong/deloc\,mass}.
}

(up to the already typed remote/satellite realization of the same class).

---

## 7. Slow/natural-time interface events are not a separate branch

If strain remains bounded, every order-one amplitude/direction/flux/interface transition needs a fixed normalized time.

Such a transition is therefore a natural-time formed event, not an instantaneous escape.

It falls into the same two possibilities audited in M5-426--427:

- the normalized Eulerian state remains recurrent/precompact;
- or the state becomes noncompact through strong/delocalized critical throughput.

The recurrent case enters the complete ancient W1/W2 corridor.

Hence

\[
\boxed{
H_{interface}^{natural\ time}
\Longrightarrow
C_{Eulerian\,recurrent}
\lor
C_{strong/deloc\,mass}.
}

---

## 8. Updated status of the interface label

The former firewall label

\[
H_{strong\,interface}
\]

can now be sharpened:

\[
\boxed{
H_{strong\,interface}
\Longrightarrow
C_{strong/deloc\,mass}
\lor
C_{Eulerian\,recurrent}.
}

The recurrent branch is not a final terminal because it returns to W1/W2.

Thus a genuinely fast interface is absorbed into strong strain/delocalized critical throughput, while a bounded-rate interface is absorbed into the ordinary recurrent/handoff dynamics.

---

## 9. Firewall

This note does **not** say that an order-one flux change over one natural time is impossible.

It is perfectly compatible with M5-393/M5-395 and may recur.

The point is only that it is not a separate arbitrarily fast mechanism once M5-392 analyticity is enforced.

Do not convert the fixed lower time into a globally summable Leray cost; that would reintroduce the critical-norm error firewalled by M5-415.

---

## 10. Audit verdict

### REMOVED AS INDEPENDENT TERMINAL

A vanishing-normalized-time source/axis/flux interface collapse under bounded parent derivatives.

### ROUTING

\[
\boxed{
\text{fast interface}
\to
\text{strong strain}
\to
C_{strong/deloc\,mass},
}
\]

\[
\boxed{
\text{natural-time interface}
\to
C_{Eulerian\,recurrent}
\lor
C_{strong/deloc\,mass}.
}
\]

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
