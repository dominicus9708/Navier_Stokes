# DSD M17-304 — Parent similarity gradient and mass-interface ledgers are finite on every forward similarity tail

Date: 2026-09-07  
Canonical ID: **M17-304**

Status: **TRUE-RESOURCE ATTACHMENT GATE / M17-303 SHOWS THAT A FIXED OWN-SCALE GRADIENT-INTERFACE PAYMENT PULLS BACK WITH WEIGHT `m_j=a_j^2 r_j^3`, WHILE A FIXED MASS-INTERFACE PAYMENT PULLS BACK WITH WEIGHT `m_j r_j^2`, BUT IT LEAVES OPEN WHETHER THE PARENT-SIMILARITY QUANTITIES ARE THEMSELVES ATTACHED TO A GENUINELY FINITE ORIGINAL ANCIENT-SOLUTION RESOURCE. USING THE EXACT SIMILARITY MAP ALREADY RECORDED IN M5-526, THE SIMILARITY VORTICITY IS `W=(-s) Omega`, WHERE `theta=-log(-s)`. CONSEQUENTLY `||grad_y W||_2^2 dtheta = (-s)^(1/2)||grad_x Omega||_2^2 ds` AND `||W||_2^2 dtheta = (-s)^(-1/2)||Omega||_2^2 ds`. M5-477 GIVES FINITE TOTAL ANCIENT PALINSTROPHY, AND M5-474 GIVES FINITE/BOUNDED VORTICITY `L2` ON EVERY COMPACT ANCIENT TIME INTERVAL. THEREFORE BOTH PARENT LEDGERS ARE FINITE ON EVERY FORWARD SIMILARITY HALF-LINE `theta>=theta_0`. THUS, FOR ANY FAMILY OF PAYING WINDOWS WITH UNIFORMLY BOUNDED SPACETIME OVERLAP, `sum m_j` AND `sum m_j r_j^2` MUST BE FINITE. THIS DOES NOT CREATE A CONTRADICTION, BECAUSE M17-303 SHOWS THE CURRENT LOWER FLOORS DO NOT FORCE THOSE SUMS TO DIVERGE. THE LATE PROBLEM IS NOW SHARPER: PROVE NONSUMMABLE WEIGHTED PAYMENT OR FORCE STRICT DESCENT/GENEALOGY; THE FINITE-RESOURCE IDENTIFICATION ITSELF IS NO LONGER MISSING FOR THE TWO INTERFACE CHANNELS. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-303

For an own-scale packet,

\[
W(y,\theta)=a_jV_j(z,\tau),
\qquad
y=q_j+r_jz,
\qquad
\theta=\theta_j+r_j^2\tau,
\]

and

\[
\boxed{m_j:=a_j^2r_j^3.}
\]

M17-303 proves the exact pullbacks

\[
\boxed{
\int |\nabla_yW|^2dy\,d\theta
=m_j\int |\nabla_zV_j|^2dz\,d\tau,
}
\]

and

\[
\boxed{
\int |W|^2dy\,d\theta
=m_jr_j^2\int |V_j|^2dz\,d\tau.
}
\]

Thus a fixed normalized gradient-interface payment carries parent weight `m_j`, and a fixed normalized mass-interface payment carries parent weight `m_j r_j^2`.

M17-303 deliberately did not yet identify the entire parent similarity spacetime integrals with a finite ancient-solution resource.  The present module supplies that missing map.

---

## 2. Exact similarity map

M5-526 records the ancient physical/similarity velocity relation

\[
\boxed{
\mathcal V(x,s)
=(-s)^{-1/2}
U\left(\frac{x}{\sqrt{-s}},-\log(-s)\right),
\qquad s<0.
}
\]

Set

\[
\lambda:=\sqrt{-s},
\qquad
y=\frac{x}{\lambda},
\qquad
\theta=-\log(-s).
\]

Then

\[
U(y,\theta)=\lambda\mathcal V(x,s).
\]

Let

\[
W=\nabla_y\times U,
\qquad
\Omega=\nabla_x\times\mathcal V.
\]

Since

\[
\nabla_y=\lambda\nabla_x,
\]

we obtain

\[
\boxed{
W(y,\theta)=\lambda^2\Omega(x,s)=(-s)\Omega(x,s).
}
\]

Also

\[
dy=\lambda^{-3}dx,
\qquad
d\theta=\lambda^{-2}ds.
\]

These are exact Jacobian identities.

---

## 3. Gradient ledger transformation

Differentiate the vorticity relation:

\[
\nabla_yW
=\lambda^3\nabla_x\Omega.
\]

Therefore at one time,

\[
\begin{aligned}
\|\nabla_yW(\theta)\|_2^2
&=\lambda^6\lambda^{-3}
\|\nabla_x\Omega(s)\|_2^2\\
&=\boxed{\lambda^3\|\nabla_x\Omega(s)\|_2^2}.
\end{aligned}
\]

Multiplying by

\[
d\theta=\lambda^{-2}ds
\]

gives

\[
\boxed{
\|\nabla_yW(\theta)\|_2^2d\theta
=\lambda\|\nabla_x\Omega(s)\|_2^2ds
=(-s)^{1/2}\|\nabla_x\Omega(s)\|_2^2ds.
}
\]

Fix any finite similarity time `theta_0` and put

\[
s_0:=-e^{-\theta_0}<0.
\]

Then

\[
\boxed{
\int_{\theta_0}^{\infty}
\|\nabla_yW(\theta)\|_2^2d\theta
=
\int_{s_0}^{0}
(-s)^{1/2}\|\nabla_x\Omega(s)\|_2^2ds.
}
\]

On `[s_0,0]`,

\[
(-s)^{1/2}\le(-s_0)^{1/2}.
\]

M5-477 gives

\[
\int_{-\infty}^{0}\|\nabla_x\Omega(s)\|_2^2ds<\infty.
\]

Hence

\[
\boxed{
\mathcal P_{\nabla}(\theta_0)
:=
\int_{\theta_0}^{\infty}
\|\nabla_yW(\theta)\|_2^2d\theta
<\infty.
}
\]

This is a genuine positive finite resource on every forward similarity tail.

---

## 4. Mass ledger transformation

From

\[
W=\lambda^2\Omega
\]

and `dy=lambda^-3 dx`,

\[
\begin{aligned}
\|W(\theta)\|_2^2
&=\lambda^4\lambda^{-3}\|\Omega(s)\|_2^2\\
&=\boxed{\lambda\|\Omega(s)\|_2^2}.
\end{aligned}
\]

Multiplying by `dtheta=lambda^-2 ds` gives

\[
\boxed{
\|W(\theta)\|_2^2d\theta
=\lambda^{-1}\|\Omega(s)\|_2^2ds
=(-s)^{-1/2}\|\Omega(s)\|_2^2ds.
}
\]

Thus

\[
\boxed{
\int_{\theta_0}^{\infty}
\|W(\theta)\|_2^2d\theta
=
\int_{s_0}^{0}
(-s)^{-1/2}\|\Omega(s)\|_2^2ds.
}
\]

The marked ancient element is smooth on compact ancient-time intervals and has

\[
\Omega\in L^\infty_{loc,s}L_x^2
\]

by M5-474.  Therefore there is a finite constant `C_{s_0}` such that

\[
\sup_{s\in[s_0,0]}\|\Omega(s)\|_2^2\le C_{s_0}.
\]

Since

\[
\int_{s_0}^{0}(-s)^{-1/2}ds
=2\sqrt{-s_0}<\infty,
\]

we obtain

\[
\boxed{
\mathcal P_{0}(\theta_0)
:=
\int_{\theta_0}^{\infty}
\|W(\theta)\|_2^2d\theta
<\infty.
}
\]

Thus the parent spacetime mass ledger is also genuinely finite on every forward similarity tail.

---

## 5. Charging bounded-overlap gradient-interface windows

Let `Q_j` be parent-similarity spacetime regions corresponding to selected unit own-scale gradient-interface payment windows, all lying in `theta>=theta_0`.

Assume a uniform spacetime overlap bound

\[
\boxed{
\sum_j1_{Q_j}(y,\theta)\le N_{ov}<\infty.
}
\]

M17-303 gives

\[
\int_{Q_j}|\nabla_yW|^2dy\,d\theta
\ge c_{grad}m_j.
\]

Summing and using bounded overlap,

\[
\begin{aligned}
c_{grad}\sum_jm_j
&\le
\sum_j\int_{Q_j}|\nabla_yW|^2\\
&\le
N_{ov}\int_{\theta_0}^{\infty}\int_{\mathbb R^3}|\nabla_yW|^2.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_jm_j
\le
\frac{N_{ov}}{c_{grad}}\mathcal P_{\nabla}(\theta_0)
<\infty.
}
\]

Therefore any proof that the same bounded-overlap paying family satisfies

\[
\sum_jm_j=\infty
\]

would be a genuine contradiction.

The missing part is now solely the nonsummability/bounded-overlap theorem, not resource identification.

---

## 6. Charging bounded-overlap mass-interface windows

Let `Q_j^0` be selected mass-interface regions on `theta>=theta_0` with

\[
\sum_j1_{Q_j^0}\le N_{ov,0}.
\]

M17-303 gives

\[
\int_{Q_j^0}|W|^2dy\,d\theta
\ge c_{mass}m_jr_j^2.
\]

Therefore

\[
\boxed{
\sum_jm_jr_j^2
\le
\frac{N_{ov,0}}{c_{mass}}\mathcal P_0(\theta_0)
<\infty.
}
\]

Thus a bounded-overlap mass-migration genealogy with

\[
\sum_jm_jr_j^2=\infty
\]

would also give a genuine contradiction.

Again the finite resource is now available; the missing theorem is the divergent charge or a return to strict scale descent.

---

## 7. Why this does not contradict M17-303

M17-303 conditionally obtains only lower floors of the form

\[
m_j\gtrsim
R_j^{-4}\operatorname{polylog}(R_j)^{-1}
\]

and

\[
m_jr_j^2\gtrsim
R_j^{-4}\operatorname{polylog}(R_j)^{-1}.
\]

On dyadic remote shells those guaranteed floors are summable.

Therefore the new finite-resource bounds are fully compatible with infinitely many payment events.

The correct situation is

\[
\boxed{
\text{finite true resource}
+\text{summable presently guaranteed event floors}
=\text{no contradiction yet}.
}
\]

This is progress in bookkeeping: one of the two missing ingredients has been supplied exactly.

---

## 8. Mass-interface events remain migration, not dissipation

The positivity of

\[
\mathcal P_0(\theta_0)
\]

allows mass-interface windows to be charged to a finite occupancy resource if overlap is controlled.

It does **not** turn a mass-interface event into signed dissipation.

A given parcel/packet may cross different localization boundaries repeatedly, so a bounded-overlap or bounded-reuse genealogy theorem remains mandatory.

M17-238's scope firewall also remains active:

\[
\boxed{
\text{point-marker migration}
\not\Rightarrow
\text{material/flux lineage replacement}.
}
\]

Thus packet/flux identity, rather than marker identity, must be used when proving the required overlap/reuse bound.

---

## 9. Relation to the coefficient/recharge branch

The present resource attachment applies directly to

1. gradient-interface action;
2. mass-interface/migration action.

It does not produce a global finite resource for the M17-303 coefficient forcing norm

\[
\int\|G_j\|_{L_y^2}d\theta.
\]

That branch remains routed, as in M17-303, to

\[
G_{scaled\ coefficient}
\lor
G_{normalized\ decompactification},
\]

unless a separate finite/signed coefficient ledger is proved.

---

## 10. Corrected late endpoint

The two interface branches can now be written as true finite-resource gates:

\[
\boxed{
\begin{aligned}
H_{gradient\ interface}
&\Longrightarrow
\left[
\sum_jm_j<\infty
\text{ for bounded-overlap selected windows}
\right],\\
H_{mass\ interface}
&\Longrightarrow
\left[
\sum_jm_jr_j^2<\infty
\text{ for bounded-overlap selected windows}
\right].
\end{aligned}
}
\]

Consequently a terminal contradiction may be obtained by proving either

\[
\boxed{
\sum_jm_j=\infty
}
\]

or

\[
\boxed{
\sum_jm_jr_j^2=\infty
}
\]

for a family whose parent spacetime overlap is uniformly bounded.

The alternative is to show that failure of bounded overlap is itself a bounded-multiplicity genealogy violation, true packet replacement, or strict scale descent.

---

## 11. Next target

M17-303 proposed payment multiplicity/genealogy.  M17-304 sharpens that target by removing the resource-identification ambiguity.

The next calculation should compare the maximum multiplicity available from

\[
T_j=A\log R_j
\]

and shell packet packing against the critical M17-207 currency

\[
\sum_kb_k^{3/2}=\infty.
\]

The key question is whether multiplicity can compensate the factors `m_j` or `m_j r_j^2`, or whether it necessarily forces the shell spectral ratio/coefficient channel to become large.

---

## 12. DSD audit

- The parent-to-ancient similarity map is exact and already present in the repository.
- `W=(-s)Omega` is derived from the velocity similarity map; no new normalization is invented.
- M5-477 is used only for the gradient ledger, where its finite total palinstrophy applies directly after the exact weight transformation.
- The mass ledger uses only compact-time `L2` boundedness of the smooth ancient vorticity and the integrability of `(-s)^(-1/2)` near `s=0`.
- No claim of finiteness is made for the full backward similarity line `theta->-infinity`; only every forward half-line `theta>=theta_0` is used.
- Payment sums are charged only under an explicit bounded spacetime-overlap hypothesis.
- Marker migration is not identified with packet/flux replacement.
- The coefficient forcing branch remains separate.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
