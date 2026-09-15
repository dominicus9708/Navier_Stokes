# M19-300 — The full-depth production-conditioned wedge ODE shows Z is not independent but the exact residual of dissipation, event hysteresis, and radial-current redistribution

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE CALCULATION / FULL CONDITIONED WEDGE ODE / CHANNEL-INDEPENDENCE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. State-level sphere energy law

The exact sphere-integrated wedge local-energy equality is

\[
\boxed{
\partial_z e
=
\mathcal L_q j
-2z\partial_z j
-j
+d,
}
\]

where

\[
e(z,Y)=\int_{S^2}E_Yd\omega,
\qquad
j(z,Y)=\int_{S^2}\mathcal J_{r,Y}d\omega,
\qquad
d(z,Y)=\int_{S^2}\mathcal D_{F,Y}d\omega\ge0.
\]

## 2. Production-conditioned observables

Let

\[
m_h(Y)=m_{pd}(\sigma_{-h}Y)
\]

be the smooth fixed-lag production marker and define

\[
\mathscr E_m(z):=\langle m_he(z)\rangle,
\]

\[
\mathscr J_m(z):=\langle m_hj(z)\rangle,
\]

\[
\mathscr D_m(z):=\langle m_hd(z)\rangle\ge0,
\]

and

\[
\boxed{
\mathscr B_m(z):=-\langle(\mathcal L_qm_h)j(z)\rangle.
}
\]

The marker is independent of wedge depth `z`.

## 3. Exact full-depth conditioned ODE

Multiply the state-level equation by `m_h` and take invariant means.

Invariance gives generator integration by parts,

\[
\langle m_h\mathcal L_qj\rangle
=-\langle(\mathcal L_qm_h)j\rangle
=\mathscr B_m.
\]

Therefore

\[
\boxed{
\mathscr E_m'(z)
+2z\mathscr J_m'(z)
+\mathscr J_m(z)
=
\mathscr D_m(z)+\mathscr B_m(z).
}
\]

This identity holds for every depth in the smooth wedge, not only at `z_E`.

## 4. Exact formula for the depth channel

M19-298 defines

\[
Z_m(z):=-\mathscr E_m'(z).
\]

Hence

\[
\boxed{
Z_m(z)
=
\mathscr D_m(z)
+\mathscr B_m(z)
-2z\mathscr J_m'(z)
-\mathscr J_m(z).
}
\]

Thus `Z_m` is not an independent source term. It is exactly the mismatch between

1. conditioned dissipation;
2. production-event boundary/hysteresis current;
3. radial wedge-current redistribution.

## 5. Equivalent signed-current derivative form

Define

\[
\mathscr G_m(z):=\sqrt z\,\mathscr J_m(z).
\]

Then

\[
2\sqrt z\,\mathscr G_m'
=
2z\mathscr J_m'+\mathscr J_m.
\]

Therefore

\[
\boxed{
2\sqrt z\,\mathscr G_m'(z)
=
\mathscr D_m(z)
+\mathscr B_m(z)
+Z_m(z).
}
\]

Since `m_h` is depth-independent,

\[
\mathscr G_m'(z)
=
\left\langle
m_h\,\partial_z(\sqrt z\,j)
\right\rangle.
\]

At `z=z_E` this exactly reproduces the M19-297 three-channel balance.

## 6. The three M19-297 channels are not three independent resources

M19-297 wrote

\[
2\sqrt{z_E}\langle m_h\Gamma_E\rangle
=D_{cond}+Z_{cond}+B_{event}.
\]

M19-300 clarifies the interpretation:

- `D_cond` is a genuine nonnegative density;
- `B_event` is the q-event hysteresis/circulation term of M19-288--289;
- `Z_cond` is the exact depth derivative required to balance those terms against the radial-current derivative.

Therefore the split is algebraically exact but resource-wise coupled.

Permanent firewall:

\[
\boxed{
D_{cond},Z_{cond},B_{event}
\text{ are balance channels, not automatically three independently accumulable payers.}
}
\]

## 7. Sign changes of Z_m

If

\[
Z_m(z)>0,
\]

then the production-conditioned energy decreases with wedge depth.

If

\[
Z_m(z)<0,
\]

then the conditioned energy is being replenished with depth.

But in either case the ODE forces the sign to be represented by

\[
\mathscr D_m+\mathscr B_m
-(2z\mathscr J_m'+\mathscr J_m).
\]

Thus any oscillatory depth profile is not an undefined escape. Its replenishment is carried by explicit radial-current/event-boundary terms.

## 8. Combined potential identity

Define

\[
\mathscr K_m(z)
:=
\mathscr E_m(z)+2z\mathscr J_m(z).
\]

Then

\[
\boxed{
\mathscr K_m'(z)
=
\mathscr D_m(z)
+\mathscr B_m(z)
+\mathscr J_m(z).
}
\]

This gives a second exact one-dimensional conditioned balance. A future endpoint argument can use it if the large-z behavior of `z\mathscr J_m(z)` is certified strongly enough.

## 9. Updated dynamic target

M19-298 removes `Z_m` as a new unbounded signed resource. M19-299 removes endpoint-only monotonicity. M19-300 removes channel independence.

The remaining high-value question is now narrower:

\[
\boxed{
\text{Can the explicit pair }(\mathscr B_m,\mathscr J_m)
\text{ sustain the required production-conditioned depth covariance without triggering an existing exit?}
}
\]

Equivalently, the live signed structure is a coupled q-hysteresis / z-radial-current circulation, not a scalar one-way drift.

---

\[
\boxed{\text{M19-300 COMPLETE; THE CONDITIONED DEPTH PROFILE IS FULLY EMBEDDED IN AN EXACT ONE-DIMENSIONAL WEDGE BALANCE.}}
\]