# DSD M17-221 — Carrier-local H2/L2 spectral escape is a remote vorticity-derivative subscale or localization fragmentation

Date: 2026-09-06  
Canonical ID: **M17-221**

Status: **SPECTRAL-RECYCLE REMOVAL / THE M17-210/211 CARRIER-LOCAL SPECTRAL RATIO HAS AN INTRINSIC LENGTH `ell_S = Lambda_S^-1/2 = (||W||_2^2/||Delta W||_2^2)^(1/4)`. THUS `Lambda_S -> infinity` IS ALREADY AN ABSOLUTE SMALL-SCALE STATEMENT: `ell_S -> 0`, AND ON REMOTE SHELLS `ell_S/R -> 0`. IF THE SPECTRAL CARRIER CAN BE CAPTURED BY A BOUNDED-COMPLEXITY COMPACT LOCALIZATION WHOSE L2 MASS IS COMPARABLE TO THE CARRIER MASS, THE LOCALIZED FIELD HAS DIVERGENT `H2/L2`; FOURIER INTERPOLATION THEN FORCES ITS FIRST/SECOND-DERIVATIVE CORRELATION LENGTH TO ZERO AS WELL. THIS IS A REMOTE HIGHER-DERIVATIVE SUBSCALE HARD CORE, ADJACENT TO THE EXISTING M5 REMOTE-DERIVATIVE-SUBSCALE PROGRAM, NOT A NEW DIRECTOR-ANISOTROPY LOOP. IF NO SUCH COMPARABLE LOCALIZATION EXISTS, THE FAILURE ITSELF IS A FRAGMENTED/DIFFUSE MICROCARRIER PACKING EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Carrier-local spectral ratio

Let `S_R` be a measurable carrier in a remote shell of radius `R`, with

\[
E_S:=\int_{S_R}|W|^2dy>0
\]

and

\[
H_S^{(2)}:=\int_{S_R}|\Delta W|^2dy.
\]

Define the M17-210/211 RMS spectral quantity

\[
\boxed{
\Lambda_S^2
:=\frac{H_S^{(2)}}{E_S}.
}
\]

Here `Lambda_S` has the scaling of an inverse length squared.

Define the associated Laplacian correlation length

\[
\boxed{
\ell_S
:=\Lambda_S^{-1/2}
=\left(\frac{E_S}{H_S^{(2)}}\right)^{1/4}.
}
\]

This definition is exact whenever `H_S^(2)>0`.

---

## 2. Spectral concentration is already a small-scale statement

If

\[
\boxed{\Lambda_{S_R}\to\infty,}
\]

then

\[
\boxed{\ell_{S_R}\to0.}
\]

Since the carriers lie on shells with

\[
R\to\infty,
\]

we also have

\[
\boxed{
\frac{\ell_{S_R}}{R}\to0.
}
\]

Thus the spectral exit is not scale-coherent with the remote shell.
It is a two-scale object:

\[
\boxed{
\text{remote shell scale }R
\quad+\quad
\text{internal Laplacian scale }\ell_S=o(1)\ll R.
}
\]

This conclusion does not use director geometry.

---

## 3. Comparable compact localization gate

Suppose there exists a bounded-complexity packet neighborhood `T_R` and a smooth cutoff `chi_R` such that

\[
\chi_R\equiv1
\quad\text{on }S_R,
\]

`chi_R` is supported in `T_R`, its fixed-order cutoff derivatives are uniformly bounded in the translated packet scale, and

\[
\boxed{
\int_{T_R}|W|^2dy
\le C_EE_S
}
\]

with `C_E` independent of `R`.

Set

\[
\boxed{f_R:=\chi_RW.}
\]

Because `chi_R=1` on `S_R`,

\[
\Delta f_R=\Delta W
\qquad\text{on }S_R.
\]

Therefore

\[
\boxed{
\|\Delta f_R\|_2^2
\ge H_S^{(2)}.
}
\]

Also

\[
\|f_R\|_2^2
\le\int_{T_R}|W|^2dy
\le C_EE_S.
\]

Hence

\[
\boxed{
\frac{\|\Delta f_R\|_2^2}{\|f_R\|_2^2}
\ge\frac1{C_E}\Lambda_S^2.
}
\]

Thus carrier-local spectral divergence survives in a genuine compactly localized field whenever comparable localization is available.

---

## 4. Localized Laplacian length

For the compact field `f_R`, define

\[
\boxed{
\ell_f^4
:=\frac{\|f_R\|_2^2}{\|\Delta f_R\|_2^2}.
}
\]

Section 3 gives

\[
\boxed{
\ell_f
\le C_E^{1/4}\ell_S
\to0.
}
\]

Thus one extracts a finite local packet whose internal Laplacian length tends to zero.

---

## 5. First/second derivative correlation length also collapses

For compact `f_R in H^2`, Fourier Cauchy-Schwarz gives

\[
\|\nabla f_R\|_2^2
\le
\|f_R\|_2\|\Delta f_R\|_2.
\]

Define

\[
Z_f:=\|\nabla f_R\|_2^2,
\qquad
Q_f:=\|\Delta f_R\|_2^2
\]

and the first/second derivative correlation length

\[
\boxed{
\delta_f^2:=\frac{Z_f}{Q_f}.
}
\]

Then

\[
\delta_f^2
\le
\frac{\|f_R\|_2}{\|\Delta f_R\|_2}
=\ell_f^2.
\]

Therefore

\[
\boxed{
\delta_f\le\ell_f\to0.
}
\]

In particular

\[
\boxed{
\frac{\delta_f}{R}\to0.
}
\]

So the localized spectral branch is a genuine derivative-subscale object in the same concentration-compactness sense as the earlier remote-subscale program.

---

## 6. Relation to the earlier M5 remote derivative subscale

The earlier M5 residual used velocity derivative masses and a correlation length of the schematic form

\[
\delta_U^2
\sim
\frac{\|\nabla U\|_2^2}{\|\nabla^2U\|_2^2}.
\]

M17-221 uses the one-order-higher vorticity quantity

\[
\delta_W^2
\sim
\frac{\|\nabla W\|_2^2}{\|\Delta W\|_2^2}.
\]

Since `W=curl U`, these are structurally adjacent derivative-scale escapes but are not silently identified as the same theorem.

The valid conclusion is

\[
\boxed{
G_{carrier\text{-}local\ H2/L2\ spectral}
\Longrightarrow
H_{remote\ vorticity\ derivative\ subscale}
}
\]

provided comparable compact localization exists.

Existing finite-witness derivative ledgers may become applicable only after a separate packet/occupancy extraction at this derivative order.

---

## 7. What if comparable localization fails?

The condition

\[
\int_{T_R}|W|^2\le C_EE_S
\]

can fail when the spectral carrier is too fragmented or too small relative to every bounded-complexity neighborhood.

In that case any cutoff that captures `S_R` also captures much larger background enstrophy, so the carrier's large normalized spectral ratio is diluted in the localized field.

This is not a failure of the spectral estimate; it is a geometric packing statement.

Define the residual

\[
\boxed{G_{spectral\ microcarrier\ fragmentation}}
\]

by the absence of a uniformly bounded-complexity comparable-mass localization.

It includes possibilities such as:

- an increasing number of separated microcarriers;
- carriers whose enclosing neighborhoods contain much larger low-frequency mass;
- arbitrarily fine spatial fragmentation;
- interface/domain proliferation needed to isolate the high-frequency set.

No one of these is assumed without proof; the label records the exact localization failure.

---

## 8. Corrected nonrecycling gate

The carrier-local spectral return in M17-218 should therefore be routed as

\[
\boxed{
G_{carrier\text{-}local\ H2/L2\ spectral}
\Longrightarrow
H_{remote\ vorticity\ derivative\ subscale}
\lor
G_{spectral\ microcarrier\ fragmentation}.
}
\]

It need not be sent back through

\[
H2/L2
\to director\ metric
\to anisotropy
\to H2/L2
\]

unless director information is independently useful.

The apparent spectral/director cycle is therefore removed as a **classification cycle**: its spectral endpoint has a direct derivative-scale interpretation.

This does not yet close the derivative-subscale or fragmentation branches.

---

## 9. Combination with M17-219 and M17-220

M17-219 gives

\[
G_{director\ metric^2}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ anisotropy}
\lor
G_{director\text{-}metric\ microcarrier}
\lor
G_{other\ explicit\ exits}.
\]

M17-220 shows that on the quiet compact bounded-RMS fixed-fraction anisotropy lane, strain-gap payment is impossible, leaving ancestor anisotropy or spectral escape.

M17-221 now sends that spectral escape directly to

\[
H_{remote\ derivative\ subscale}
\lor
G_{microcarrier\ fragmentation}.
\]

Hence no independent `spectral/director recycling` label is needed in the compressed frontier.

---

## 10. DSD analysis

### 10.1 Scale separation

`Lambda_S` is a quotient of two norms on the same carrier.
Its divergence defines an intrinsic scale before any geometric interpretation is added.

### 10.2 Localization boundary

A norm quotient on an arbitrary measurable set is not automatically the quotient of a compact packet.
The comparable-localization hypothesis is therefore explicit.

### 10.3 Derivative-order boundary

The old M5 subscale theorem and the present vorticity subscale are adjacent but not identical derivative orders.
A bridging packet theorem remains required.

---

## 11. DSD audit

- No Fourier transform is applied directly to an arbitrary material subset; Fourier interpolation is used only after compact localization.
- `ell_S->0` follows directly from the definition of `Lambda_S` and requires no packet extraction.
- Failure of comparable localization is retained as a fragmentation/multiplicity exit.
- The spectral/director loop is removed only as a classification loop, not mathematically contradicted.
- The remote derivative subscale remains a hard branch.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
