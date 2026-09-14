# DSD M19-255 — GMS weighted payer splits into high-frequency transfer, low-frequency, and pressure gates

Date: 2026-09-14
Status: VALID FREQUENCY-SPLIT REDUCTION + NO-GO; TRANSFER/LOW/PRESSURE OPEN; NOT A CLOSURE THEOREM
Parent: M19-254

## 0. Goal

M19-254 reduced every hypothetical singular point to the necessary logarithmically divergent payer

\[
\mathcal P_{GMS}^{log}(V)
=
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
=\infty
\]

for every fixed constant Galilean velocity \(V\).

The purpose of M19-255 is to compare this payer with the certified whole-space derivative/ancestry ledgers and identify the actual remaining gates.

---

## 1. Dyadic Galilean shells and frequency split

Let \(r_m=2^{-m}r_0\) and consider the corresponding Galilean parabolic shells/windows. At scale \(r\), split

\[
u=u_{\le r^{-1}}+u_{>r^{-1}}.
\]

The high-frequency part is measured against the physical frequency threshold \(|\xi|\sim r^{-1}\).

---

## 2. High-frequency velocity estimate

Interpolation between \(L^2\) and \(L^6\) gives

\[
\|f\|_{10/3}^{10/3}
\lesssim
\|f\|_2^{4/3}\|f\|_6^2.
\]

For \(f=u_{>r^{-1}}\), Sobolev and high-frequency Bernstein give

\[
\|u_{>r^{-1}}\|_6
\lesssim
\|\nabla u_{>r^{-1}}\|_2
\lesssim
r\,\|D^2u\|_2
\simeq
r\,\|\nabla\omega\|_2.
\]

Using \(\|u_{>r^{-1}}\|_2\le\|u\|_2\),

\[
\boxed{
\|u_{>r^{-1}}\|_{10/3}^{10/3}
\lesssim
r^2\|u\|_2^{4/3}\|\nabla\omega\|_2^2.
}
\]

Hence on a parabolic time window \(I_r\) of length comparable to \(r^2\), the GMS logarithmic normalization obeys

\[
\boxed{
r^{-5/3}
\int_{I_r}\|u_{>r^{-1}}\|_{10/3}^{10/3}dt
\lesssim
B_{-1}^{2/3}
\,r^{1/3}
\int_{I_r}\|\nabla\omega\|_2^2dt,
}
\]

where \(B_{-1}=\|u\|_2^2=\|\omega\|_{\dot H^{-1}}^2\) is the low-frequency energy currency.

For \(0<r\le1\), \(r^{1/3}\le r^{-1}\). Therefore a correctly transferred finite ledger of the M17 form

\[
\sum_m r_m^{-1}
\int_{I_m}\|\nabla\omega\|_2^2dt<\infty
\]

is more than sufficient to make the high-frequency velocity contribution to the GMS weighted sum finite.

This conclusion is conditional on a physical scale/domain/genealogy transfer. M19-255 does not assume that transfer for free.

---

## 3. Low-frequency NO-GO

For the low-frequency component, Bernstein only gives

\[
\boxed{
\|u_{\le r^{-1}}\|_{10/3}
\lesssim
r^{-3/5}\|u\|_2.
}
\]

Therefore

\[
\|u_{\le r^{-1}}\|_{10/3}^{10/3}
\lesssim
r^{-2}\|u\|_2^{10/3}.
\]

After integrating over a time interval of length \(\asymp r^2\), the physical integral is only bounded by an order-one energy quantity. Multiplication by the GMS weight \(r^{-5/3}\) leaves a divergent scale factor.

Thus the finite energy currency \(B_{-1}\) alone does not close the low-frequency part.

A fixed Galilean subtraction \(u\mapsto u-V\) removes one constant mode only. It does not remove a general low-frequency tail.

Permanent firewall:

\[
\boxed{
\text{high-frequency derivative control}
\not\Rightarrow
\text{low-frequency GMS weighted tightness}.
}
\]

---

## 4. Pressure gate

For the canonical whole-space pressure,

\[
 p=R_iR_j(u_i u_j)
\]

up to the usual time-dependent gauge.

At a fixed time, the spatial power weight \(|x-a|^{-5/3}\) lies in the Muckenhoupt class \(A_{5/3}(\mathbb R^3)\), since

\[
-3<-\frac53<3\left(\frac53-1\right)=2.
\]

This makes weighted Calderón--Zygmund control a plausible mechanism for reducing the pressure payer to a weighted velocity payer. However the actual GMS weight is parabolic/truncated,

\[
\rho_V(x,t)^{-5/3}
=
\max\{|x-a_V(t)|,\sqrt{t_0-t}\}^{-5/3},
\]

and the target is localized to a moving cylinder. Uniform \(A_{5/3}\) control, the canonical pressure gauge, localization, and the nonlocal far-field pressure contribution must therefore be certified separately.

Define this remaining obligation as

\[
\boxed{\mathcal T_{GMS}^{press}}.
\]

---

## 5. Raw-H2 and higher ledgers do not transfer automatically

The certified M17 ancestry weights include

\[
\sum_m R_m^{-1}\int\|\nabla\Omega_m\|_2^2<\infty,
\qquad
\sum_m R_m^{-3}\int\|\Delta\Omega_m\|_2^2<\infty,
\]

with still higher derivative control available in the retained whole-space lane.

These are potentially stronger than the high-frequency estimate above, but they live on specific record/genealogy domains. They are not automatically estimates on the GMS moving shells.

Hence

\[
\boxed{
\text{finite M17 raw-H2/ancestry ledger}
\not\Rightarrow
\mathcal P_{GMS}^{log}<\infty
}
\]

without a physical shell/domain/genealogy transfer theorem.

Define that gate as

\[
\boxed{\mathcal T_{GMS}^{transfer}}.
\]

---

## 6. Reduced active structure

M19-255 therefore refines

\[
\mathcal T_{GMS}^{weight}
\]

into three typed obligations:

\[
\boxed{
\mathcal T_{GMS}^{weight}
\Leftarrow
\mathcal T_{GMS}^{transfer}
+\mathcal T_{GMS}^{low}
+\mathcal T_{GMS}^{press}.
}
\]

Here

- \(\mathcal T_{GMS}^{transfer}\): transfer the certified M17 derivative/ancestry ledgers to the same physical Galilean scale windows with bounded overlap and correct domain/genealogy correspondence;
- \(\mathcal T_{GMS}^{low}\): control the low-frequency weighted velocity tail beyond the single constant mode removed by \(V\);
- \(\mathcal T_{GMS}^{press}\): reduce the weighted nonlocal pressure payer to controlled velocity currencies.

Under \(\mathcal T_{GMS}^{transfer}\), the high-frequency velocity is not the leading obstruction.

---

## 7. New firewalls

\[
\boxed{
\text{M17 derivative strength}
\neq
\text{GMS physical-shell control without transfer coherence}.}
\]

\[
\boxed{
V\text{ removes one constant drift}
\neq
\text{control of the full low-frequency tail}.}
\]

\[
\boxed{
|x-a|^{-5/3}\in A_{5/3}
\neq
\text{localized moving-cylinder pressure closure without a uniform weighted-CZ audit}.}
\]

---

## 8. Next target

The next calculation is to audit the scaling and geometry of \(\mathcal T_{GMS}^{transfer}\): determine whether the M17 ancestry factors \(R^{1-2k}\) exactly match the physical parabolic rescaling of \(D^k\omega\), and isolate any remaining center/domain/genealogy mismatch.

Global regularity remains unproved.
