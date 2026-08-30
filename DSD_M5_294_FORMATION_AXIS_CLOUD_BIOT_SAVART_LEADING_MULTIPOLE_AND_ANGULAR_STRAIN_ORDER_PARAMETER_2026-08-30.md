# DSD M5-294 — Formation/Axis Cloud Biot–Savart Leading Multipole and Angular-Strain Order Parameter

Date: 2026-08-30

Parent: `DSD_M5_293_AMPLIFIED_PACKING_COHERENT_MEMORY_VS_PERSISTENT_SPATIAL_CLOUD_AUDIT_2026-08-30.md`

Status: **FORMATION-AXIOM OBJECT SPLIT + AXIS-ATTRIBUTE ANGULAR TENSOR / LEADING REMOTE STRAIN OF A LOCALIZED VORTICITY SATELLITE IS COMPUTED EXPLICITLY / NONCANCELLING CLOUDS ROUTE TO AMBIENT-STRAIN H / CANCELLING CLOUDS ARE REDUCED TO RADIAL-AXIS ALIGNMENT OR A FIVE-COMPONENT TRACE-FREE ANGULAR MOMENT CANCELLATION, WITH MONOPOLE-NEUTRAL PACKETS ROUTED TO THE NEXT MULTIPOLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose and scope

This note uses the Formation Axiom System and the Axis-Attribute Axiom System only as a **problem-decomposition layer**.

No new proof rule is imported from either system.

Every closure statement below is an ordinary Biot–Savart/Taylor estimate.

The target is the persistent spatial satellite cloud left by M5-293.

The main question is:

> if many natural-scale vorticity satellites coexist at large radius, what angular/moment cancellation is necessary for their aggregate far strain to remain quiet?

---

## 2. Minimal satellite descriptor

For a localized satellite packet indexed by `i`, write

\[
\mathscr S_i=(y_i,\ell_i,\chi_i\omega,\ldots),
\]

with center

\[
y_i=d_i n_i,\qquad |n_i|=1,
\]

and support diameter

\[
\operatorname{diam}(\operatorname{supp}\chi_i)\lesssim \ell_i,
\qquad \ell_i\ll d_i.
\]

The first moment needed by the remote strain is not a scalar circulation but the localized vorticity vector

\[
\boxed{
M_i:=\int \chi_i(y)\,\omega(y)\,dy.
}
\]

The Formation split is therefore

\[
\boxed{
M_i\neq0
\quad\lor\quad
M_i=0.
}
\]

The second case is not discarded; it is a genuine next-multipole branch.

---

## 3. Exact strain kernel

Use the Biot–Savart convention

\[
u(x)=\frac1{4\pi}\int \omega(y)\times\frac{x-y}{|x-y|^3}\,dy.
\]

Let

\[
r=x-y.
\]

Differentiating and symmetrizing gives

\[
\boxed{
S_{ab}(x)
=-\frac{3}{8\pi}
\int
\frac{
(\omega\times r)_a r_b
+(\omega\times r)_b r_a
}{|r|^5}\,dy.
}
\]

The Kronecker-delta terms cancel under the symmetric projection.

This kernel is homogeneous of degree `-3`, symmetric, and trace free.

---

## 4. Leading remote strain of one packet

Evaluate at the tracked core `x=0`.

Write

\[
y=d n+z,
\qquad |z|\lesssim\ell,
\qquad d\gg\ell.
\]

Taylor expansion of the degree-`-3` strain kernel gives

\[
\boxed{
S_{packet}(0)
=
\frac{3}{8\pi d^3}
\Big[
 n\otimes(n\times M)
+(n\times M)\otimes n
\Big]
+\mathcal E_1,
}
\]

with

\[
\boxed{
|\mathcal E_1|
\le
C d^{-4}
\int |z|\,|\chi\omega|\,dz.
}
\]

Thus define the leading angular-strain tensor

\[
\boxed{
\mathcal K(n,M)
:=
 n\otimes(n\times M)
+(n\times M)\otimes n.
}
\]

It is symmetric and trace free.

---

## 5. Axis-attribute interpretation

Decompose

\[
M=M_{\parallel}+M_{\perp},
\qquad
M_{\parallel}=(M\cdot n)n.
\]

Then

\[
n\times M=n\times M_{\perp}.
\]

Therefore

\[
\boxed{
\mathcal K(n,M)=0
\iff
M\parallel n
\quad\text{or}\quad M=0.
}
\]

This gives an exact axis-attribute split:

1. **radial-axis aligned packet** — its leading `d^{-3}` strain at the core vanishes individually;
2. **transverse-moment packet** — it generates a nonzero leading remote shear;
3. **monopole-neutral packet** `M=0` — the first nonzero contribution begins at the next multipole.

The first case is not a cancellation among different satellites. It is an individual geometric invisibility of the leading strain channel.

---

## 6. Natural-scale size

For a natural satellite,

\[
|\omega|\sim\ell^{-2},
\qquad
\operatorname{Vol}\sim\ell^3.
\]

Hence generically

\[
|M|\lesssim \ell.
\]

The leading remote strain therefore has size

\[
\boxed{
|S_{packet}(0)|
\lesssim
\frac{\ell}{d^3}.
}
\]

Compared with the satellite's own natural vorticity/strain scale `\ell^{-2}`, this is

\[
\boxed{
\frac{|S_{packet}(0)|}{\ell^{-2}}
\lesssim
\left(\frac\ell d\right)^3
=L^{-3},
\qquad L=d/\ell.
}
\]

This `L^{-3}` factor is the correct single-packet far-strain suppression.

---

## 7. Many comparable satellites on one radial band

Consider `N` comparable satellites with

\[
d_i\simeq d,
\qquad
\ell_i\simeq\ell,
\qquad
L=d/\ell\gg1.
\]

Write

\[
M_i=\ell\,m_i
\]

with dimensionless `m_i=O(1)` on the nondegenerate packet class.

Then

\[
S_{cloud}(0)
=
\frac{3\ell}{8\pi d^3}
\sum_{i=1}^N
\mathcal K(n_i,m_i)
+\text{higher multipoles/errors}.
\]

Define the normalized angular-strain order parameter

\[
\boxed{
\mathfrak A_0
:=
\frac1N
\sum_{i=1}^N
\mathcal K(n_i,m_i)
\in \operatorname{Sym}_0(3).
}
\]

Since `Sym_0(3)` has dimension five, leading-order cancellation imposes five scalar tensor conditions.

The leading cloud strain relative to the natural satellite scale is

\[
\boxed{
\frac{|S_{cloud}(0)|}{\ell^{-2}}
\simeq
\frac{N}{L^3}|\mathfrak A_0|
}
\]

up to fixed packet-shape constants and the higher-multipole error.

---

## 8. Immediate routing

If

\[
\boxed{
\frac{N}{L^3}|\mathfrak A_0|
\ge c_{amb}>0,
}
\]

then the cloud produces order-one ambient strain at the satellite natural scale.

This routes directly to

\[
\boxed{H_{ambient}.}
\]

Therefore a persistent amplified cloud which remains outside the ambient-strain branch must satisfy

\[
\boxed{
\frac{N}{L^3}|\mathfrak A_0|\to0.
}
\]

If `N\simeq cL^3`, this becomes the genuine angular cancellation condition

\[
\boxed{
\mathfrak A_0\to0.
}
\]

---

## 9. Formation split of leading-order cancellation

The equation `\mathfrak A_0\approx0` can occur by distinct mechanisms which must not be conflated.

### A. Individual radial-axis invisibility

For many packets,

\[
M_i\parallel n_i.
\]

Then their individual leading tensors vanish.

This is an **axis-alignment branch**, not collective cancellation.

### B. Collective tensor cancellation

The individual tensors are nonzero, but

\[
\sum_i\mathcal K(n_i,m_i)\approx0.
\]

This is a genuine five-component angular balance among different satellite axes/moments.

### C. Monopole-neutral packets

For many packets,

\[
M_i\approx0.
\]

Then the `d^{-3}` term is absent and one must retain the first moment tensor

\[
\boxed{
N_{ak}^{(i)}
:=
\int (y-y_i)_a\,\chi_i(y)\omega_k(y)\,dy.
}
\]

The next remote-strain contribution is of order

\[
\boxed{
O\!\left(
 d^{-4}|N^{(i)}|
\right).
}
\]

For a natural packet, generically `|N^{(i)}|\lesssim\ell^2`, so the normalized next-order far strain is `O(L^{-4})` per packet.

---

## 10. Important firewall: compact vortex packets may naturally be monopole-neutral

For a globally compact divergence-free vorticity field produced as the curl of a sufficiently decaying velocity,

\[
\int \omega\,dx=0.
\]

A localized cutoff packet, however, need not retain this exact cancellation because cutoff/Bogovskii localization separates the packet from its compensating exterior structure.

Therefore one must not assume either

\[
M_i\neq0
\]

or

\[
M_i=0
\]

universally.

Both are legitimate Formation branches.

This is why a scalar circulation descriptor alone is insufficient for the cloud audit.

---

## 11. Relation to the existing transverse covariance gate

The repository already has the exact transverse covariance identity

\[
E_\perp'=2q_\perp D+\mathcal R_\perp,
\]

which says that a coherent active remote transverse strain cannot remain simultaneously shape-invisible and residual-quiet.

M5-294 supplies the missing **source geometry** for that `D`:

\[
D_{far}
\quad\text{is generated at leading order by}\quad
\sum_i d_i^{-3}\mathcal K(n_i,M_i),
\]

plus higher multipoles.

Thus the two notes combine as

\[
\boxed{
\text{noncancelling angular cloud}
\Longrightarrow
H_{ambient}
\Longrightarrow
T_{shape}\lor T_{D-dir}\lor H/T/residual
}
\]

on the coherent covariance corridor.

---

## 12. Updated persistent-cloud frontier

The cloud branch is now

\[
\boxed{
\begin{aligned}
C_{cloud}
\Longrightarrow{}&
H_{ambient}
\\
&\lor C_{radial-align}
\\
&\lor C_{tensor-cancel}
\\
&\lor C_{M_0=0,next-multipole}.
\end{aligned}
}
\]

The next efficient audit is to determine whether the first two quiet branches can persist dynamically:

1. radial-axis alignment must be maintained while the satellites and main core move;
2. collective tensor cancellation must preserve five scalar constraints under vorticity transport/stretching;
3. monopole-neutral packets must satisfy the corresponding next-multipole cancellation.

The expected gain is not a purely algebraic contradiction but a **dynamic codimension/covariance cost**: maintaining the cancellation manifold may force projective/turnover action unless there is an exact symmetric invariant subclass.

---

## 13. Audit verdict

### PROVED / EXACT

- explicit degree-`-3` remote strain kernel;
- leading packet tensor `\mathcal K(n,M)`;
- exact radial-axis invisibility condition `M\parallel n`;
- natural single-packet suppression `L^{-3}`;
- cloud strain scaling `(N/L^3)|\mathfrak A_0|`;
- five-component leading collective cancellation condition;
- next-multipole order `d^{-4}` when `M=0`.

### NOT PROVED

- that `M_i` is uniformly nonzero;
- that angular cancellation cannot persist;
- that a persistent cloud must generate ambient strain;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]