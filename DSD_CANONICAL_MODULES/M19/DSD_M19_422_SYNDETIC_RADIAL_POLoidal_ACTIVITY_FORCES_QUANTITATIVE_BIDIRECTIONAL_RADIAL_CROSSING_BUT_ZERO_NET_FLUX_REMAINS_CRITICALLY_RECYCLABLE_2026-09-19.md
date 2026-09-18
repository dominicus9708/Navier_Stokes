# M19-422 — Syndetic radial/poloidal activity forces quantitative bidirectional radial crossing, but zero net flux remains critically recyclable

Date: 2026-09-19  
Canonical ID: **M19-422**  
Status: **RADIAL/POLoidal CHANNEL REDUCTION / ANY SYNDETIC RP EVENT FORCES A NEARBY FIXED RADIAL-AMPLITUDE EVENT BY THE HODGE CONSTRAINT AND COMPACT q-REGULARITY / ZERO SPHERE MEAN THEN FORCES QUANTITATIVE INWARD AND OUTWARD CRITICAL CROSSING ON THE SAME SPHERE / ZERO NET FLUX DOES NOT CANCEL PRESSURE OR ENERGY WORK / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-421

On the RP branch, one fixed normalized log window \(I_*\) recurs syndetically and satisfies
\[
\boxed{
\|A_{RP}\|_{L^2(I_*\times S^2)}
\ge
\eta_{RP}>0.
}
\]

The exact Hodge form is
\[
A_{RP}
=
A_r\omega
-
\nabla_S\Delta_S^{-1}(\partial_q+1)A_r,
\]
with
\[
\boxed{
\int_{S^2}A_r(q,\omega)d\omega=0
}
\]
for every \(q\) on the bounded recurrent leading tail.

The radial and tangential pieces are pointwise orthogonal.

## 2. RP activity splits into radial amplitude or poloidal-divergence activity

Write
\[
g:=(\partial_q+1)A_r.
\]

Then
\[
\|A_{RP}\|_2^2
=
\|A_r\|_2^2
+
\|\nabla_S\Delta_S^{-1}g\|_2^2.
\]

Hence over the fixed window at least one of
\[
\boxed{
\int_{I_*}\|A_r\|_2^2dq
\ge
\frac{\eta_{RP}^2}{2}
}
\]
or
\[
\boxed{
\int_{I_*}
\|\nabla_S\Delta_S^{-1}g\|_2^2dq
\ge
\frac{\eta_{RP}^2}{2}
}
\]
holds.

Because \(g\) has zero spherical mean, the first nonzero scalar spherical eigenvalue is \(2\), so
\[
\|\nabla_S\Delta_S^{-1}g\|_2^2
\le
\frac12
\|g\|_2^2.
\]

Thus the second alternative implies
\[
\boxed{
\int_{I_*}\|g\|_2^2dq
\ge
\eta_{RP}^2.
}
\]

## 3. Large g forces either A_r itself or its q-derivative

Since
\[
g=\partial_qA_r+A_r,
\]
we have
\[
\|g\|_2^2
\le
2\|\partial_qA_r\|_2^2
+
2\|A_r\|_2^2.
\]

Therefore a fixed RP event forces at least one of

\[
\boxed{
\int_{I_*}\|A_r\|_2^2dq
\ge
c_1\eta_{RP}^2
}
\]

or

\[
\boxed{
\int_{I_*}\|\partial_qA_r\|_2^2dq
\ge
c_2\eta_{RP}^2
}
\]

for harmless universal constants \(c_1,c_2>0\).

## 4. Compact q-regularity converts derivative action into an amplitude excursion

The smooth compact terminal hull gives a uniform bound
\[
\boxed{
\|\partial_q^2A_r(q)\|_{L^2(S^2)}
\le
M_{rr}
}
\]
on the finite detector family.

Suppose the derivative branch occurs:
\[
int_{I_*}
\|\partial_qA_r\|_2^2dq
\ge
d_r>0.
\]

Then some \(q_0\in I_*\) satisfies
\[
\|\partial_qA_r(q_0)\|_2
\ge
\sqrt{d_r/|I_*|}.
\]

The second-derivative ceiling forces this derivative to remain of comparable Hilbert-space size over a fixed one-sided interval of length
\[
h_r>0
\]
depending only on \(d_r,|I_*|,M_{rr}\).

Integrating in \(q\) gives two nearby phases \(q_0,q_1\) with
\[
\boxed{
\|A_r(q_1)-A_r(q_0)\|_2
\ge
\delta_r>0.
}
\]

Therefore
\[
\max\{
\|A_r(q_0)\|_2,
\|A_r(q_1)\|_2
\}
\ge
\frac{\delta_r}{2}.
\]

Thus both subbranches produce, within a uniformly bounded log shift of the original RP event,
\[
\boxed{
\|A_r(q_*)\|_{L^2(S^2)}
\ge
a_r>0.
}
\]

Because the RP detector returns syndetically, these radial-amplitude events are also syndetic after enlarging the bounded return gap by the fixed local shift.

## 5. Zero net radial flux forces simultaneous inward and outward sectors

For every \(q\),
\[
\int_{S^2}A_r,d\omega=0.
\]

Write
\[
A_r=A_r^+-A_r^-,
\qquad
A_r^\pm\ge0.
\]

Then
\[
\boxed{
\int A_r^+d\omega
=
\int A_r^-d\omega
=:
S_r.
}
\]

Let the compact hull give
\[
\|A_r\|_{L^\infty(S^2)}
\le
M_r.
\]

At a radial-amplitude event,
\[
a_r^2
\le
\int|A_r|^2d\omega
\le
M_r
\int|A_r|d\omega
=
2M_rS_r.
\]

Hence
\[
\boxed{
S_r
\ge
\frac{a_r^2}{2M_r}
=:
s_*>0.
}
\]

Thus every selected RP event contains quantitatively nontrivial positive and negative radial crossing on the same sphere:
\[
\boxed{
\int A_r^+d\omega
=
\int A_r^-d\omega
\ge
s_*.
}
\]

## 6. Physical crossing size is critical

For the physical terminal tail
\[
u_r(r,omega)
=
r^{-1}A_r(\log r,omega),
\]
the signed sphere flux is
\[
\int_{S_r}u_r,dS
=
r
\int_{S^2}A_r,d\omega
=
0.
\]

But the positive and negative unsigned crossing magnitudes are
\[
\int_{S_r}(u_r)^+dS
=
r
\int_{S^2}A_r^+d\omega,
\]
and similarly for the negative part.

Hence on the selected spheres
\[
\boxed{
\int_{S_r}(u_r)^+dS
=
\int_{S_r}(u_r)^-dS
\ge
s_*r.
}
\]

The critical tail therefore supports order-\(r\) opposing volume-crossing currents whose signed sum is exactly zero.

This is recirculation, not a source/sink.

## 7. Zero signed flux does not kill energy or pressure transport

The scale-normalized radial energy current contains weighted correlations of the form
\[
\int_{S^2}
\left(
\frac12|A|^2+P
\right)A_r,d\omega
\]
together with the viscous energy-flux term.

The identity
\[
\int A_r=0
\]
does not cancel these correlations because the weights are not constant.

In particular inward and outward sectors can carry different pressure and kinetic-energy densities.

This is the same structural lesson as the earlier zero-flux reconnection audit:
signed mass/volume flux may cancel while pressure work remains positive or oscillatory.

Therefore
\[
\boxed{
\text{zero net radial flux}
\not\Rightarrow
\text{zero radial energy/pressure work}.
}
\]

## 8. Critical-budget firewall

The order-\(r\) absolute radial crossing may look large, but it is exactly what a \(1/r\) velocity tail over an area \(r^2\) produces.

Finite kinetic energy of the original parent does not pass to an absolute-flux bound on the noncompact blow-down corridor with sufficient uniformity to kill this critical recirculation.

Likewise the opposing positive/negative currents may reconnect through angular flow without any physical source.

Thus
\[
\boxed{
RP^{syndetic}
\not\Rightarrow
\text{mass-flux contradiction}.
}
\]

The gain from M19-422 is geometric/formed: RP is now a **quantitative bidirectional radial-crossing branch**, not an abstract Hodge norm.

## 9. Updated three-channel frontier

M19-421 gave
\[
R3
\lor
RP
\lor
T_{\ge2}.
\]

M19-422 refines the middle branch to
\[
\boxed{
R3^{syndetic,critical}
\lor
BRC^{syndetic}
\lor
T_{\ge2}^{syndetic},
}
\]
where
\[
BRC
:=
\text{quantitative bidirectional radial crossing with zero signed sphere flux}.
\]

The BRC branch requires a new signed correlation theorem, not another unsigned flux count.

The next useful target is to pair the two radial sign sectors with the exact terminal energy ledger
\[
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\langle A\cdot C\rangle
\]
and ask whether persistent bidirectional crossing forces a nonzero covariance between \(A_r\) and pressure/energy density that must be paid by one of the already typed residual channels.

Absent such a covariance theorem, the radial branch remains a critical recirculation firewall rather than a contradiction.

\[
\boxed{\text{M19-422 COMPLETE; RP ACTIVITY IS REDUCED TO SYNDETIC QUANTITATIVE BIDIRECTIONAL RADIAL CROSSING.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
