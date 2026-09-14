# DSD M19-258 — Whole-space Biot–Savart identifies raw-H2 vorticity with H3 velocity and removes separate field/pressure gates

Date: 2026-09-15  
Status: **VALID WHOLE-SPACE ANALYTIC BRIDGE / CONDITIONAL ON UNTRUNCATED SAME-FIELD RECORD REPRESENTATION / NOT GLOBAL CLOSURE**  
Parent: M19-257

## 0. Goal

M19-257 separated the record-to-physical transfer problem into coverage/reuse, field matching, pressure matching, and root eligibility. This module audits whether the field and pressure gates are genuinely independent when the M17 record variable is the untruncated whole-space vorticity of the same rescaled Navier--Stokes solution.

They are not.

The remaining hard issue is then geometric/representational coherence: whether the certified record ledger actually covers the physical shrinking neighborhood with controlled multiplicity and the correct genealogy.

Global regularity remains unproved.

---

## 1. Exact whole-space velocity-vorticity derivative identity

Let \(u(\cdot,t)\) be divergence free on \(\mathbb R^3\) and

\[
\omega=\nabla\times u.
\]

In Fourier variables,

\[
\widehat\omega(\xi)=i\xi\times\widehat u(\xi),
\qquad
\xi\cdot\widehat u(\xi)=0.
\]

Hence

\[
|\widehat\omega(\xi)|^2
=|\xi|^2|\widehat u(\xi)|^2.
\]

Therefore

\[
\begin{aligned}
\|\omega\|_{\dot H^2}^2
&=\int_{\mathbb R^3}|\xi|^4|\widehat\omega(\xi)|^2\,d\xi\\
&=\int_{\mathbb R^3}|\xi|^6|\widehat u(\xi)|^2\,d\xi\\
&=\|u\|_{\dot H^3}^2.
\end{aligned}
\]

Since

\[
\|\Delta\omega\|_2^2=\|\omega\|_{\dot H^2}^2,
\]

we obtain the exact homogeneous identity

\[
\boxed{
\|\Delta\omega\|_2^2
=\|(-\Delta)^{3/2}u\|_2^2.
}
\]

The usual tensor derivative norm \(\|D^3u\|_2\) is equivalent to the right-hand side by a universal dimension-dependent constant.

Thus, for an **untruncated whole-space record field**, no local Biot--Savart commutator or boundary correction is required to convert raw-\(H^2\) vorticity control into third-derivative velocity control.

---

## 2. Exact compatibility with Navier--Stokes scaling

For a physical scale \(r\), use

\[
u^{(r)}(y,s)=r\,u(x_0+ry,t_0+r^2s),
\qquad
\omega^{(r)}(y,s)=r^2\omega(x_0+ry,t_0+r^2s).
\]

Then

\[
\omega^{(r)}=\nabla_y\times u^{(r)},
\qquad
\nabla_y\cdot u^{(r)}=0,
\]

and the same Fourier identity gives, for every normalized time \(s\),

\[
\boxed{
\|\Delta_y\omega^{(r)}(s)\|_2^2
=\|(-\Delta_y)^{3/2}u^{(r)}(s)\|_2^2.
}
\]

Consequently, once a record \(m\) is certified to be the same whole-space rescaled field as the physical shell/cylinder it is assigned to, the raw-H2 record currency is already the correct H3 velocity currency. No derivative-order loss occurs.

---

## 3. Time-integrated bridge

Integrating over a record time window \(I_m\),

\[
\boxed{
\int_{I_m}\|\Delta\Omega_m(s)\|_2^2\,ds
\simeq
\int_{I_m}\|D^3U_m(s)\|_2^2\,ds.
}
\]

Therefore the certified M17 ancestry ledger

\[
\sum_m R_m^{-3}
\int_{I_m}\|\Delta\Omega_m\|_2^2ds<\infty
\]

is simultaneously an H3-velocity ledger on the **same whole-space record fields**.

The word "same" is essential. The identity does not certify that a localized/cutoff record, a different ancient generation, or a record from a nonmatching genealogy represents the physical GMS cylinder.

---

## 4. Pressure follows once the physical H3 transfer is achieved

Suppose the coherence/coverage map transfers the record ledger into

\[
D^3u\in L^2(Q)
\]

on the required physical time-space neighborhood, together with the inherited finite-energy bound

\[
u\in L_t^\infty L_x^2.
\]

The three-dimensional Gagliardo--Nirenberg inequality gives at each time

\[
\|u(t)\|_6
\le C
\|D^3u(t)\|_2^{1/3}
\|u(t)\|_2^{2/3}.
\]

Hence

\[
\int\|u(t)\|_6^6dt
\le
C\|u\|_{L_t^\infty L_x^2}^4
\int\|D^3u(t)\|_2^2dt
<\infty.
\]

Thus

\[
\boxed{u\in L^6_{x,t}.}
\]

For the canonical whole-space pressure,

\[
p=R_iR_j(u_i u_j)
\]

up to the irrelevant time-dependent pressure gauge. Spatial Calderón--Zygmund boundedness gives

\[
\|p(t)\|_3\le C\|u(t)\|_6^2,
\]

and therefore

\[
\boxed{p\in L^3_{x,t}.}
\]

This reproduces the M19-255 analytic bridge without a separate pressure hypothesis.

---

## 5. Weighted GMS payer then becomes finite

From \(u\in L^6\),

\[
|u-V|^{10/3}\in L^{9/5}_{loc},
\]

and from \(p\in L^3\),

\[
|p|^{5/3}\in L^{9/5}_{loc}.
\]

In parabolic dimension five,

\[
\rho_V^{-5/3}\in L^{9/4}_{loc}.
\]

Hölder therefore yields

\[
\boxed{
\mathcal P_{GMS}^{log}(V)<\infty.
}
\]

This contradicts the M19-254 singularity necessity \(\mathcal P_{GMS}^{log}(V)=\infty\), **provided** the physical neighborhood is genuinely covered by the same whole-space raw-H2 record ledger.

---

## 6. Reduction of the M19-257 gate list

Under the untruncated same-field whole-space representation,

\[
\boxed{
\mathcal T_{GMS}^{field}
\text{ is discharged by the Fourier/Biot--Savart identity},
}
\]

and

\[
\boxed{
\mathcal T_{GMS}^{press}
\text{ is discharged by M19-255 + Calderón--Zygmund}.
}
\]

The active transfer complex therefore reduces to

\[
\boxed{
\mathcal T_{GMS}^{cover}
+\mathcal T_{GMS}^{repr}
+\mathcal T_{GMS}^{root}.
}
\]

Here

- \(\mathcal T_{GMS}^{cover}\): physical domain/time coverage, scale comparability, center coherence, and bounded shell-to-record reuse;
- \(\mathcal T_{GMS}^{repr}\): each assigned M17 record is the same untruncated whole-space rescaled solution/generation, not merely a local proxy;
- \(\mathcal T_{GMS}^{root}\): the hypothetical singular point enters the M17-eligible retained genealogy with the required hypotheses.

If the M17 objects are localized/cutoff fields rather than the whole-space fields assumed here, the field/interface gate reopens and M19-257's conservative formulation must be used.

---

## 7. Permanent firewalls

\[
\boxed{
\text{global Fourier velocity-vorticity identity}
\not\Rightarrow
\text{record-to-physical representation coherence}.
}
\]

\[
\boxed{
\text{raw-H2 record field}
\not\Rightarrow
\text{the same physical field/generation without a dictionary theorem}.
}
\]

\[
\boxed{
\text{pressure follows from transferred whole-space H3}
\not\Rightarrow
\text{pressure follows from an arbitrary localized vorticity cutoff}.
}
\]

\[
\boxed{
\text{analytic bridge closed}
\not\Rightarrow
\text{coverage, genealogy, or ROOT-CERT closed}.
}
\]

---

## 8. Immediate next target

The next audit should no longer spend effort on derivative exponents, local Biot--Savart reconstruction, or pressure as independent obstacles unless the M17 record is found to be truncated.

The decisive question is now:

\[
\boxed{
\text{For every sufficiently small physical GMS shell around the candidate point,
can one assign comparable-scale M17 whole-space records of the same genealogy
with uniformly bounded reuse?}
}
\]

This is the record-cover / representation-coherence theorem.

If yes, the entered GMS branch closes through M19-254--258. If no, the first failed condition becomes a typed survivor: tracking, domain, coverage, overlap, genealogy, representation, or upstream root entry.

Global regularity remains unproved.
