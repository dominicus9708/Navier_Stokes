# DSD M19-255 — Derivative threshold closes the analytic GMS payer conditional on physical raw-H2 transfer

Date: 2026-09-14
Status: CORRECTED CANONICAL VERSION / CONDITIONAL ANALYTIC CLOSURE; PHYSICAL TRANSFER OPEN; NOT GLOBAL CLOSURE
Parent: M19-254

> Audit note: the file name records the initial frequency-split draft. That weaker draft remains historically visible in Git history, but this corrected content is canonical. The direct derivative-threshold argument below is stronger and supersedes the need to leave low-frequency and pressure as independent analytic gates once the raw-H2 ledger is physically transferred.

## 0. Goal

M19-254 proved that a genuine singular point must satisfy, for every fixed constant Galilean velocity \(V\),

\[
\mathcal P_{GMS}^{log}(V)
=
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
=\infty.
\]

We ask which derivative level is sufficient to force the same weighted integral to be finite.

---

## 1. Isotropic spacetime integrability from a derivative ledger

Assume on a finite physical spacetime region

\[
u\in L_t^\infty L_x^2,
\qquad
D^m u\in L_t^2L_x^2.
\]

The Gagliardo--Nirenberg interpolation

\[
\|u(t)\|_{L^s}
\lesssim
\|u(t)\|_2^{1-a}
\|D^m u(t)\|_2^a,
\qquad
\frac1s=\frac12-\frac{am}{3},
\]

becomes directly time-integrable when \(as=2\). Solving gives

\[
\boxed{s=2+\frac{4m}{3}.}
\]

Therefore:

\[
m=2\quad\Longrightarrow\quad u\in L_{x,t}^{14/3},
\]

while

\[
\boxed{m=3\quad\Longrightarrow\quad u\in L_{x,t}^{6}.}
\]

At \(m=3\), more explicitly,

\[
\boxed{
\int\|u(t)\|_6^6dt
\lesssim
\left(\sup_t\|u(t)\|_2^4\right)
\int\|D^3u(t)\|_2^2dt.
}
\]

For divergence-free whole-space velocity,

\[
\|D^3u\|_2\simeq\|D^2\omega\|_2,
\]

and the M17 raw-H2 currency \(\|\Delta\omega\|_2^2\) is Fourier-equivalent to this derivative level.

---

## 2. Pressure rises to L3

For the canonical whole-space pressure,

\[
p=R_iR_j(u_i u_j)
\]

up to a time-dependent gauge. Since Riesz transforms are bounded on \(L^3\),

\[
\|p(t)\|_3
\lesssim
\|u(t)\otimes u(t)\|_3
\lesssim
\|u(t)\|_6^2.
\]

Hence

\[
\boxed{u\in L^6_{x,t}\Longrightarrow p\in L^3_{x,t}.}
\]

Thus the pressure gate is not analytically independent once the physical \(D^3u\in L^2\) transfer is available.

---

## 3. The parabolic GMS kernel is subcritical against L6/L3

The parabolic homogeneous dimension is five. For

\[
\rho_V(x,t)=\max\{|x-x_0-V(t-t_0)|,\sqrt{t_0-t}\},
\]

the kernel \(\rho_V^{-5/3}\) belongs locally to \(L^q\) for every \(q<3\). Choose

\[
q=\frac94,
\qquad
q'=\frac95.
\]

If \(u\in L^6\), then

\[
|u-V|^{10/3}\in L^{9/5}
\]

on every bounded Galilean cylinder. If \(p\in L^3\), then

\[
|p|^{5/3}\in L^{9/5}.
\]

Hölder therefore yields

\[
\boxed{
\int_{Q_{r_0}^V}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
<\infty.
}
\]

This directly contradicts the M19-254 necessary singularity payer.

---

## 4. Exact analytic conclusion

The analytic part of the moving-sphere/GMS branch is therefore conditionally closed:

\[
\boxed{
D^3u\in L^2_{x,t}\text{ on the required physical neighborhood}
\Longrightarrow
\mathcal P_{GMS}^{log}(V)<\infty.
}
\]

In particular, a representation-safe physical transfer of the certified M17 raw-H2 ancestry ledger would produce the contradiction.

The previous weaker frequency-split audit remains valid as a diagnostic, but it is not the active bottleneck.

---

## 5. The only active gate created here

The active theorem target becomes

\[
\boxed{
\mathcal T_{GMS}^{transfer}:
\text{transfer the M17 }R^{-3}\text{ raw-H2 ancestry ledger to the required physical Galilean neighborhood/shell family.}
}
\]

This requires correct scale conversion, physical domain coverage, bounded overlap/nonreuse, and genealogy/representation coherence.

Until that bridge is proved, one may not infer physical \(D^3u\in L^2\) on the GMS neighborhood merely from a normalized/ancestral raw-H2 ledger.

---

## 6. Permanent firewalls

\[
\boxed{
\text{normalized raw-H2 finiteness}
\not\Rightarrow
\text{physical GMS-neighborhood }D^3u\in L^2
\text{ without a transfer theorem}.}
\]

\[
\boxed{
\text{analytic }L^6/L^3\text{ closure}
\not\Rightarrow
\text{global regularity until physical transfer and upstream proof-tree entry are certified}.}
\]

---

## 7. Next target

Audit the exact Navier--Stokes scaling of \(D^k\omega\) against the M17 ancestry factors \(R^{1-2k}\), then isolate the remaining center/domain/coverage/genealogy conditions. This is M19-256.

Global regularity remains unproved.
