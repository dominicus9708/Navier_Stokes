# M19-302 — q-z wedge circulation is not source free: its exact divergence is dissipation plus signed radial energy current

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE GEOMETRY / TWO-DIMENSIONAL WEDGE BALANCE / SOURCE-FREE CYCLE NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Starting point

The state-level sphere energy law is

\[
\partial_z e
=
\mathcal L_qj-2z\partial_zj-j+d.
\]

Define

\[
\boxed{
K(z,Y):=e(z,Y)+2zj(z,Y).
}
\]

Then

\[
\partial_zK
=
\partial_ze+2j+2z\partial_zj.
\]

Substituting the wedge energy law gives

\[
\boxed{
\partial_zK-\mathcal L_qj=d+j.
}
\]

## 2. q-z current interpretation

On an orbit chart where `L_q` is represented by q-translation, define the two-dimensional current

\[
\boxed{
\mathbf F_{qz}:=(-j,K).
}
\]

Then

\[
\boxed{
\operatorname{div}_{q,z}\mathbf F_{qz}
=d+j.
}
\]

Thus a loop or circulation in the joint recurrent-phase/depth geometry is not divergence free in general.

Its exact source density is

\[
\boxed{d+j.}
\]

## 3. Meaning of the two source terms

The first term satisfies

\[
d\ge0
\]

and is normalized viscous dissipation.

The second term

\[
j
\]

is the signed global radial local-energy current through the transparent observation sphere.

Therefore a source-free q-z cycle would require an exact cancellation

\[
\boxed{
d+j=0
}
\]

in the relevant weak/integrated sense. Since `d` is nonnegative, such a cancellation requires an inward/negative radial-current contribution wherever dissipation is nonzero.

No general theorem currently forbids this signed radial transport.

## 4. Conditioned weak form

Multiply by the fixed-lag production marker `m_h` and take invariant means.

Define

\[
\mathscr K_m(z)
:=
\langle m_hK(z)\rangle
=
\mathscr E_m(z)+2z\mathscr J_m(z).
\]

Generator integration by parts gives

\[
-\langle m_h\mathcal L_qj\rangle
=
\langle(\mathcal L_qm_h)j\rangle
=-\mathscr B_m.
\]

Hence

\[
\boxed{
\mathscr K_m'(z)
=
\mathscr D_m(z)
+\mathscr J_m(z)
+\mathscr B_m(z).
}
\]

This is exactly the combined-potential identity already obtained algebraically in M19-300, now interpreted as the weak q-z divergence law.

## 5. Consequence for B_hyst and Z_replenishment

M19-301 leaves two circulation-like branches:

- q/event hysteresis `B_m`;
- z/depth replenishment through sign changes of `Z_m`.

M19-302 shows these are not independent source-free cycles. Both are embedded in one two-dimensional balance whose source is `d+j`.

Therefore

\[
\boxed{
\text{q-hysteresis + z-replenishment}
\not\Rightarrow
\text{free topological circulation}.
}
\]

Any closed/returning balance must account for dissipative source and signed radial-energy transport.

## 6. Integrated strip law

For any finite depth interval `[z_1,z_2]`,

\[
\boxed{
\mathscr K_m(z_2)-\mathscr K_m(z_1)
=
\int_{z_1}^{z_2}
\left(
\mathscr D_m+\mathscr J_m+\mathscr B_m
\right)dz.
}
\]

Thus if the conditioned combined potential returns to the same value across a depth strip, then necessarily

\[
\boxed{
\int_{z_1}^{z_2}
\left(
\mathscr D_m+\mathscr J_m+\mathscr B_m
\right)dz=0.
}
\]

A positive dissipation contribution must then be canceled by negative radial current and/or event-boundary circulation.

## 7. Relation to the unconditioned wedge system

Without the marker,

\[
\boxed{
\left(\mathscr E+2z\mathscr J\right)'
=
\mathscr D+\mathscr J,
}
\]

which is M5-583's total-derivative form.

M19-302 therefore does not invent a new conservation law. It identifies the conditioned q-hysteresis term as the extra weak-boundary contribution produced by selecting recurrent production phases.

## 8. New reduced gate

The dynamic circulation branch is reduced to

\[
\boxed{
\mathcal T_{cycle}^{qz}
\Longrightarrow
\mathcal T_{radial}^{signed}
\lor
\mathcal T_{event}^{hyst}
\lor
\mathcal D_{cond},
}
\]

with an exact balance among them.

Since `D_cond` is unsigned and physically scale-sensitive, while `B_event` is recurrent hysteresis, the new potentially informative signed quantity is the global radial energy current `j` itself.

The next audit should determine whether the required negative/inward radial-current compensation is compatible with the terminal scattering law and the Type-I large-z endpoint, or whether it forces a forbidden endpoint/export defect.

---

\[
\boxed{\text{M19-302 COMPLETE; THE SURVIVING q-z CIRCULATION HAS AN EXPLICIT SOURCE AND IS NOT A FREE TOPOLOGICAL CYCLE.}}
\]