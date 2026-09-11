# M19-035 — The critical r^-1 scattering datum has no first r^-3 solvability obstruction

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL SCATTERING / ASYMPTOTIC SOLVABILITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Critical scattering leading field

Use the passive critical-tail representation

\[
\boxed{
U_0(y,\theta)
=
\frac1rA(q,\omega),
\qquad
r=|y|,
\qquad
\omega=\frac y{|y|},
\qquad
q=\log r-\frac\theta2.
}
\]

The relevant linear similarity transport operator is

\[
\boxed{
\mathcal L_{sim}
:=
\partial_\theta
+
\frac12\left(1+y\cdot\nabla\right).
}
\]

The sign convention is the one consistent with the M5-567 outward characteristic.

## 2. Exact cancellation for arbitrary A

Since

\[
\partial_\theta q=-\frac12,
\qquad
r\partial_rq=1,
\]

we have

\[
\partial_\theta U_0
=-\frac12r^{-1}A_q,
\]

and

\[
y\cdot\nabla U_0
=r\partial_r(r^{-1}A)
=r^{-1}(-A+A_q).
\]

Hence

\[
\begin{aligned}
\mathcal L_{sim}U_0
&=
-\frac12r^{-1}A_q
+
\frac12r^{-1}(A-A+A_q)\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal L_{sim}
\left[r^{-1}A\left(\log r-\frac\theta2,\omega\right)\right]
=0
}
\]

for every sufficiently regular scattering datum \(A\), subject only to incompressibility.

This is the analytic origin of the free log-translation datum.

## 3. First Navier--Stokes residual is order r^-3

Spatial differentiation gives schematically

\[
\nabla U_0
=r^{-2}\mathcal D_1A,
\]

and

\[
\Delta U_0
=r^{-3}\mathcal D_2A,
\]

where \(\mathcal D_1,\mathcal D_2\) contain angular and \(q\)-derivatives.

Likewise

\[
(U_0\cdot\nabla)U_0
=r^{-3}\mathcal N(A).
\]

A critical pressure has the form

\[
P_0=r^{-2}\Pi(q,\omega),
\]

so

\[
\nabla P_0=r^{-3}\mathcal D_P\Pi.
\]

Thus after exact cancellation of the similarity transport,

\[
\boxed{
\mathcal R[U_0,P_0]
=r^{-3}
\mathcal F(A,\Pi).
}
\]

There is no residual of order \(r^{-1}\) or \(r^{-2}\).

## 4. The first correction has an invertible similarity coefficient

Take a correction

\[
\boxed{
U_1=r^{-3}B(q,\omega).
}
\]

Then

\[
\partial_\theta U_1
=-\frac12r^{-3}B_q,
\]

while

\[
y\cdot\nabla U_1
=r^{-3}(-3B+B_q).
\]

Therefore

\[
\begin{aligned}
\mathcal L_{sim}U_1
&=
-\frac12r^{-3}B_q
+
\frac12r^{-3}(B-3B+B_q)\\
&=-r^{-3}B.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal L_{sim}
\left[r^{-3}B(q,\omega)\right]
=-r^{-3}B(q,\omega).
}
\]

The coefficient at this order is nonzero.

## 5. Consequence: no first Fredholm-type constraint on A

At the first correction order, the schematic equation is

\[
-r^{-3}B
+
r^{-3}\mathcal F(A,\Pi)
+
\text{divergence/pressure correction}
=0.
\]

Thus, after the usual solenoidal/pressure projection, the order-\(r^{-3}\) forcing can generically be absorbed into the correction \(B\).

There is no zero coefficient of the similarity operator at this order that would force

\[
\mathcal F(A,\Pi)=0
\]

as a solvability condition on the leading datum.

Therefore

\[
\boxed{
\text{Navier--Stokes at first subleading order does not generically impose a closed local equation on }A(q,\omega).
}
\]

This is consistent with the M5-567 Duhamel scattering construction, where the residual is outward-integrable and only changes the \(O(r^{-3})\) correction.

## 6. Why stationary critical-tail rigidity is stronger

If the similarity state is stationary or discretely self-similar, then the scattering datum is constant or periodic in \(q\).

This adds a global dynamical constraint external to the local asymptotic expansion.

Stress/point-force/Pohozaev identities can then compare the same tail state across radii or periods.

For a general aperiodic recurrent scattering datum, the freedom

\[
q\mapsto A(q,\omega)
\]

is precisely the leading homogeneous solution of the transport operator. The subleading residual does not remove it.

Hence one cannot legitimately extend the stationary rigidity argument merely by keeping one more asymptotic order.

## 7. Higher-order resonance check

More generally, for

\[
U_n=r^{-(2n+1)}B_n(q,\omega),
\qquad n\ge0,
\]

the same calculation gives

\[
\boxed{
\mathcal L_{sim}U_n
=-n\,r^{-(2n+1)}B_n.
}
\]

Indeed the only zero eigenvalue in this odd inverse-power family occurs at

\[
n=0,
\qquad
r^{-1}A(q,\omega).
\]

All higher odd powers have nonzero algebraic similarity coefficient.

Thus the unique resonant asymptotic sector is exactly the critical \(r^{-1}\) scattering datum itself.

## 8. Updated R-critical theorem frontier

M19-035 eliminates a tempting local route:

\[
\boxed{
\text{compute one more asymptotic order}
\not\Rightarrow
\text{rigidity of }A.
}
\]

The unresolved theorem must act directly on the resonant translation datum.

Thus

\[
\boxed{
\mathcal T_{critical}
=
\text{a global }q\text{-translation/cocycle rigidity theorem for the resonant }r^{-1}\text{ sector}.
}
\]

## 9. Possible successful structures

A closure theorem would need information not contained in the local first correction, for example:

- a signed quantity whose \(q\)-derivative has a coercive sign;
- a finite parent budget controlling total variation of the scattering datum;
- a recurrence plus compactness theorem forcing periodicity;
- material/genealogical identification between distant \(q\)-phases;
- an external Liouville theorem covering aperiodic recurrent weak-critical scattering states.

None is derived here.

## 10. Next calculation

The next useful internal calculation is to inspect whether any classical conserved flux -- momentum, angular momentum, or stress flux -- produces a **bounded q-cocycle** for the resonant datum after subtracting the integrable \(r^{-3}\) correction.

If every such flux contains an unconstrained transport/storage term, R-critical should be explicitly marked as requiring a genuinely new rigidity theorem rather than more local asymptotic expansion.

---

\[
\boxed{\text{M19-035 COMPLETE; THE R-CRITICAL OBSTRUCTION LIVES IN THE RESONANT }r^{-1}\text{ TRANSLATION DATUM ITSELF.}}
\]
