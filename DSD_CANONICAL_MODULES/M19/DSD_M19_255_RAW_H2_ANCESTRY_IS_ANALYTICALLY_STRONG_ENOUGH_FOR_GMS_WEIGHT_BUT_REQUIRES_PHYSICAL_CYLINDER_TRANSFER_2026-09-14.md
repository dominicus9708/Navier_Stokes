# DSD M19-255 — Raw-H2 ancestry is analytically strong enough for the GMS weighted payer, but physical-cylinder transfer is the actual gate

Date: 2026-09-14
Status: VALID CONDITIONAL CLOSURE LEMMA + TRANSFER FIREWALL; GLOBAL REGULARITY UNPROVED
Parent: M19-254

## 0. Goal

M19-254 reduced every genuine singular point to the necessary logarithmically divergent Galilean payer

\[
\mathcal P_{GMS}^{log}(V)
=
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
=\infty
\]

for every fixed constant velocity \(V\).

The present calculation asks whether the certified M17 derivative ledgers are analytically strong enough to make this integral finite.

The answer splits sharply by derivative order:

\[
\boxed{\nabla\Omega\text{ / }R^{-1}\text{ ledger: not enough by direct Hölder;}}
\]

\[
\boxed{\Delta\Omega\text{ / }R^{-3}\text{ ledger: enough if transferred to the actual physical cylinder.}}
\]

Thus the present frontier is not another local integrability estimate. It is the parent/record-to-physical-cylinder transfer theorem.

---

## 1. General interpolation threshold

Assume on a physical time interval \(I\)

\[
u\in L_t^\infty L_x^2,
\qquad
D^m u\in L_t^2L_x^2.
\]

Gagliardo--Nirenberg gives

\[
\|u(t)\|_{L_x^s}
\lesssim
\|D^m u(t)\|_2^{a}\|u(t)\|_2^{1-a},
\qquad
\frac1s=\frac12-\frac{am}{3}.
\]

Choosing \(as=2\) so that the derivative term is time-integrable yields

\[
a=\frac2s,
\qquad
\boxed{s=2+\frac{4m}{3}}.
\]

Hence

\[
m=1\Rightarrow s=\frac{10}{3},
\qquad
m=2\Rightarrow s=\frac{14}{3},
\qquad
m=3\Rightarrow s=6.
\]

For the weighted GMS velocity integrand, write

\[
f_u=|u-V|^{10/3}.
\]

The parabolic weight \(w=\rho_V^{-5/3}\) belongs locally to \(L^q\) for every \(q<3\), because the backward parabolic homogeneous dimension is five:

\[
\int_0^{r_0} r^{4-(5/3)q}\,dr<\infty
\iff q<3.
\]

To control \(\int f_uw\) by Hölder we need

\[
f_u\in L^a,
\qquad
a'>1,
\qquad a'<3.
\]

Equivalently

\[
a>\frac32.
\]

Since \(u\in L^s\) gives \(f_u\in L^{3s/10}\), the direct weighted estimate requires

\[
\frac{3s}{10}>\frac32
\iff
\boxed{s>5}.
\]

Therefore the first integer derivative level obtainable from the energy interpolation family that crosses the weighted threshold is

\[
\boxed{m=3}.
\]

This is the exact analytic reason the \(R^{-1}\) palinstrophy ancestry and the \(R^{-3}\) raw-H2 ancestry behave differently for \(\mathcal P_{GMS}^{log}\).

---

## 2. The R^{-1} / palinstrophy ledger is below the threshold

The M17 \(R^{-1}\) ancestry ledger controls \(\nabla\Omega\), which corresponds, modulo standard div-curl/Riesz equivalence, to two derivatives of velocity:

\[
\nabla\Omega\sim D^2u.
\]

Thus the energy interpolation gives only

\[
\boxed{u\in L_{x,t}^{14/3}}.
\]

Then

\[
|u|^{10/3}\in L^{7/5},
\]

whose Hölder conjugate is

\[
\left(\frac75\right)'=\frac72>3.
\]

But \(\rho_V^{-5/3}\notin L^{7/2}_{loc}\). Hence the direct weighted estimate fails.

Permanent firewall:

\[
\boxed{
R^{-1}\text{ palinstrophy ancestry}
\not\Rightarrow
\mathcal P_{GMS}^{log}<\infty
\text{ by direct interpolation/Hölder}.
}
\]

This does not prove impossibility of a more structured estimate; it rules out the naive direct route.

---

## 3. The R^{-3} / raw-H2 ledger crosses the threshold

The M17 raw-H2 quantity \(\Delta\Omega\) corresponds to three derivatives of velocity:

\[
\|D^3u\|_2
\lesssim
\|D^2\Omega\|_2
\simeq
\|\Delta\Omega\|_2,
\]

using \(-\Delta u=\nabla\times\Omega\) for divergence-free velocity and the \(L^2\) Fourier/Riesz equivalence.

Assume for the moment that on an actual physical neighborhood of a candidate singular point one has

\[
E_0:=\operatorname*{ess\,sup}_{t\in I}\|u(t)\|_2^2<\infty,
\]

\[
J_3:=\int_I\|D^3u(t)\|_2^2dt<\infty.
\]

Then the \(m=3\) Gagliardo--Nirenberg estimate is

\[
\|u(t)\|_6
\lesssim
\|D^3u(t)\|_2^{1/3}\|u(t)\|_2^{2/3}.
\]

Raising to the sixth power and integrating gives

\[
\boxed{
\int_I\|u(t)\|_6^6dt
\lesssim
E_0^2J_3<\infty.
}
\]

Therefore

\[
\boxed{u\in L_{x,t}^6.}
\]

For canonical whole-space pressure

\[
-\Delta p=\partial_i\partial_j(u_i u_j),
\]

Calderon--Zygmund gives for a.e. time

\[
\|p(t)\|_3\lesssim\|u(t)\|_6^2,
\]

hence

\[
\boxed{p\in L_{x,t}^3.}
\]

---

## 4. Weighted GMS payer becomes finite

Set

\[
w_V=\rho_V^{-5/3}.
\]

Choose the conjugate pair

\[
\frac95,
\qquad
\frac94.
\]

Because \(9/4<3\),

\[
\boxed{w_V\in L^{9/4}(Q_{r_0}^V)}.
\]

Also

\[
|u|^{10/3}\in L^{9/5}
\quad\text{since}\quad
\frac{10}{3}\frac95=6,
\]

and

\[
|p|^{5/3}\in L^{9/5}
\quad\text{since}\quad
\frac53\frac95=3.
\]

Therefore Hölder yields

\[
\int_{Q_{r_0}^V}|u|^{10/3}w_V<\infty,
\qquad
\int_{Q_{r_0}^V}|p|^{5/3}w_V<\infty.
\]

The constant Galilean shift is harmless on a bounded cylinder because

\[
|u-V|^{10/3}\lesssim |u|^{10/3}+|V|^{10/3}
\]

and \(w_V\in L^1_{loc}\). Thus

\[
\boxed{
E_0<\infty,\ J_3<\infty
\Longrightarrow
\mathcal P_{GMS}^{log}(V)<\infty
\quad\text{for every fixed }V.
}
\]

Combined with M19-254, this excludes a genuine singular point.

---

## 5. Conditional closure theorem

Define the physical-transfer statement

\[
\boxed{
\mathcal T_{R^{-3}}^{phys}:
\text{the certified M17 }R^{-3}\text{ raw-H2 ancestry ledger transfers, with bounded overlap and correct scaling, to a physical neighborhood of the candidate singular point.}
}
\]

Then

\[
\boxed{
\mathcal T_{R^{-3}}^{phys}
\Longrightarrow
\mathcal T_{GMS}^{weight}
\Longrightarrow
\text{no singular point on that branch}.
}
\]

Thus the analytic part of \(\mathcal T_{GMS}^{weight}\) is conditionally closed.

What remains is the transfer theorem, not the weighted Hölder estimate.

---

## 6. Exact transfer obstruction

The existing M17 statement

\[
\sum_m R_m^{-3}
\int_{I_m}\|\Delta\Omega_m\|_2^2ds<\infty
\]

is an ancestry/record statement. Under the vorticity rescaling

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

one has

\[
\int\|\Delta_y\Omega_R\|_2^2ds
=
R^3\int\|\Delta_x\Omega\|_2^2dt,
\]

so

\[
\boxed{
R^{-3}
\int\|\Delta\Omega_R\|_2^2ds
=
\int\|\Delta\Omega\|_2^2dt.
}
\]

Hence the ancestry weight is exactly the physical raw-H2 scaling needed by the conditional lemma.

However, summability over record windows does not by itself say that those windows cover the moving physical cylinder around \(z_0\), nor that the same parent solution/domain/genealogy survives through the required lookback.

The remaining gate is therefore:

\[
\boxed{
\text{record-window raw-H2 ownership}
\not\Rightarrow
\text{physical-cylinder raw-H2 finiteness}
}
\]

without:

- parent-to-record scale-map certification;
- bounded-overlap coverage of the relevant physical cylinder/rings;
- domain/interface/rank persistence;
- no genealogy loss during the logarithmic lookback;
- correct identification of the M17 vorticity field with the physical field feeding the M19 Galilean cylinder.

---

## 7. Low-frequency audit correction

M17-407 correctly records that high-frequency derivative control alone does not remove the global velocity low-frequency tail.

For the present weighted payer, however, if the full physical \(D^3u\in L_t^2L_x^2\) bound is actually transferred on the same neighborhood, the ordinary finite-energy bound \(u\in L_t^\infty L_x^2\) supplies the low-frequency endpoint in the Gagliardo--Nirenberg interpolation.

Therefore the current hierarchy is:

\[
\boxed{
\text{before physical }R^{-3}\text{ transfer: low-frequency closure unavailable};
}
\]

\[
\boxed{
\text{after physical }R^{-3}\text{ transfer: no separate }B_{-1}\text{ obstruction is needed for }\mathcal P_{GMS}^{log}.
}
\]

This does not erase the global M17 low-frequency firewall; it narrows its relevance for this specific GMS-weighted target.

---

## 8. New canonical target

The next theorem target is

\[
\boxed{
\mathcal T_{GMS}^{transfer}:
\text{construct a representation-safe, bounded-overlap map from the M17 }R^{-3}\text{ record ledger to the physical Galilean cylinder/rings around }z_0.
}
\]

A successful proof closes the weighted whole-space branch immediately through M19-254--255.

If the transfer fails, the failure must be classified into a concrete survivor:

\[
\boxed{
\text{scale-map/genealogy loss}
\lor
\text{domain/interface/rank loss}
\lor
\text{coverage/decompactification failure}.
}
\]

Those survivors can then be pushed back into ROOT-CERT/non-CE-H bookkeeping rather than spawning new wall/cavity calculations.

---

## 9. Status

M19-255 substantially narrows the active problem:

\[
\boxed{
\text{weighted analytic closure is available conditionally at raw-H2 level; the live gate is physical transfer.}
}
\]

Global 3D Navier--Stokes regularity remains unproved.
