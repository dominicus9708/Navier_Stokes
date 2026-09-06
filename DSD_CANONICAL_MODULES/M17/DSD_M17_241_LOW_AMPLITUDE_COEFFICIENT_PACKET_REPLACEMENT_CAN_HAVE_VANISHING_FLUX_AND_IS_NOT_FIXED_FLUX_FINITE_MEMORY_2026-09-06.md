# DSD M17-241 — Low-amplitude coefficient-packet replacement can have vanishing flux and is not fixed-flux finite memory

Date: 2026-09-06  
Canonical ID: **M17-241**

Status: **FINITE-MEMORY FIREWALL / M5-641 PROVES POSITIVE-RATE REPLACEMENT FOR COHERENT STRONGLY-NEGATIVE PACKETS ONLY AFTER EXTRACTING A UNIFORM NONZERO VORTICITY-FLUX FLOOR `phi_*>0`. THE CURRENT M17 ARG PACKET MAY HAVE RADIUS `ell->0` AND MEAN AMPLITUDE `a->0`. ITS DIRECTED VORTICITY FLUX ACROSS AN `O(ell^2)` CROSS-SECTION CAN BE ONLY `O(a ell^2)=O(M^(1/2) ell^(1/2))`, WHERE `M~a^2 ell^3` IS THE PACKET ENSTROPHY MASS. THUS THE COEFFICIENT GEOMETRY AND EVEN ORDER-ONE RELATIVE KAPPA DYNAMICS CAN BE CARRIED BY MATERIAL LABELS WHOSE PHYSICAL FLUX TENDS TO ZERO. POSITIVE-RATE REPLACEMENT OF SUCH LABELS IS NOT THE FIXED-FLUX REPLACEMENT COUNTED BY THE EXISTING FINITE-MEMORY THEOREMS. A NEW FLUX-QUANTIZATION OR AMPLITUDE-RETURN THEOREM WOULD BE REQUIRED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-flux hypothesis in the existing replacement theorem

The strongly-negative packet theorem M5-641 extracts a coherent packet with

\[
\boxed{
\phi_*\le|\Phi|\le\phi^*
}
\]

for constants independent of time/state on the compact recurrent hull.

The finite lifetime of one strongly-negative label then forces positive-rate replacement of **fixed-strength material flux packets**.

The lower bound \(\phi_*>0\) is essential.

---

## 2. Current intrinsic coefficient packet

Let a current ARG packet have radius

\[
\ell\to0
\]

and mean-dominated amplitude scale

\[
a:=|\bar W|.
\]

On the good bulk,

\[
|W|\asymp a.
\]

Its enstrophy mass satisfies schematically

\[
\boxed{
M\asymp a^2\ell^3.
}
\]

No current theorem gives a lower bound on \(a\) independent of \(\ell\) or shell radius.

---

## 3. Flux scale of a small packet

Take a transverse disk \(D_\ell\) of area \(O(\ell^2)\) contained in the packet.

The directed flux obeys

\[
|\Phi_\ell|
=\left|\int_{D_\ell}W\cdot n\,dA\right|
\le
\int_{D_\ell}|W|dA.
\]

On a coherent mean-dominated packet,

\[
\boxed{
|\Phi_\ell|\lesssim a\ell^2.
}
\]

Using

\[
a\asymp M^{1/2}\ell^{-3/2},
\]

we obtain

\[
\boxed{
|\Phi_\ell|
\lesssim
M^{1/2}\ell^{1/2}.
}
\]

Therefore

\[
M\to0
\quad\text{and/or}\quad
\ell\to0
\]

is compatible with

\[
\boxed{|\Phi_\ell|\to0.}
\]

---

## 4. Relative kappa dynamics does not repair the flux floor

M17-239 shows that

\[
|\kappa|\sim\ell^{-2}
\]

for an own-scale parabolic time \(O(\ell^2)\) can change amplitude or flux by an order-one **multiplicative factor**.

For example a negative coherent phase may satisfy schematically

\[
|\Phi(\tau_\ell)|
\le e^{-c}|\Phi(0)|.
\]

But if

\[
|\Phi(0)|\to0,
\]

then both the initial and descendant fluxes remain vanishingly small in absolute units.

Thus

\[
\boxed{
\text{order-one relative flux decay}
\not\Rightarrow
\text{order-one physical flux payment}.
}
\]

---

## 5. Positive-rate tiny-flux replacement is not excluded by fixed memory

Suppose each coefficient packet has flux \(\phi_j\to0\) and material lifetime bounded in its strongly-negative/high-coefficient role.

Even if replacement occurs at a positive rate in normalized time, the existing fixed-flux memory argument cannot count each event as consuming one label of size \(\phi_*\), because no uniform \(\phi_*>0\) exists.

A sequence such as

\[
\phi_j=2^{-j}
\]

has finite total absolute flux size

\[
\sum_j\phi_j<\infty
\]

while containing infinitely many distinct labels.

This model does not assert that Navier--Stokes realizes such a sequence; it demonstrates the logical gap in importing fixed-flux finite memory.

---

## 6. Scale-normalized flux does not solve the physical budget problem

One may define a normalized flux

\[
\widehat\Phi
:=
\frac{\Phi}{a\ell^2}.
\]

On a coherent packet \(\widehat\Phi\) may be order one.

However finite-memory and global energy/enstrophy ledgers are physical/amplitude-weighted. They do not currently provide a finite budget for the number of order-one normalized tiny-flux labels.

Hence

\[
\boxed{
\widehat\Phi\asymp1
}
\]

is not a replacement contradiction.

---

## 7. Correct replacement split

The ARG genealogy branch must distinguish

\[
\boxed{
T_{replacement}
\Longrightarrow
T_{fixed\text{-}flux}
\lor
T_{vanishing\text{-}flux}.
}
\]

For the first branch, existing finite-memory/replacement machinery is applicable.

For the second branch, the unresolved task is to prove either

\[
\boxed{
\text{flux quantization / amplitude return}
}
\]

or a different amplitude-independent budget for the replacement process.

---

## 8. Relation to M17-238--240

M17-238 prevents point-marker weakening from being called replacement.

M17-239 shows that same-lineage critical multiplier activity forces relative segregation or amplitude-independent coefficient/strain action.

M17-240 types rapid multiplier turnover into exact constitutive payer channels.

M17-241 adds the genealogy firewall:

\[
\boxed{
\text{even true material replacement}
\text{ need not have fixed physical flux at low amplitude}.
}
\]

Thus ARG cannot be closed by replacement counting alone.

---

## 9. DSD audit

- The M5-641 fixed flux floor is preserved as an explicit hypothesis.
- Small packet radius and small amplitude are not converted into a fictitious fixed flux.
- Relative decay and absolute flux are kept distinct.
- Scale-normalized flux is not silently identified with a globally budgeted quantity.
- Vanishing-flux replacement remains a genuine survivor.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
