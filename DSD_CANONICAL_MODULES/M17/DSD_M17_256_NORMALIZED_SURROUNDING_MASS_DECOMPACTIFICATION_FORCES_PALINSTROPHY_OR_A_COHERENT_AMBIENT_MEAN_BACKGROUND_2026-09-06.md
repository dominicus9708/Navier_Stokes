# DSD M17-256 — Normalized surrounding-mass decompactification forces palinstrophy or a coherent ambient mean background

Date: 2026-09-06  
Canonical ID: **M17-256**

Status: **MASS-DECOMPACTIFICATION CLASSIFICATION / M17-255 LEAVES ONE EXPLICIT FAILURE: ON A FIXED OWN-SCALE BALL `B_{K r_j}`, THE SURROUNDING `L2` MASS MAY BE ARBITRARILY LARGE RELATIVE TO THE SELECTED PACKET MASS `E_j`. SPLIT THE SURROUNDING VORTICITY INTO ITS SPATIAL MEAN PLUS A MEAN-ZERO FLUCTUATION. IF THE FLUCTUATION CARRIES A FIXED FRACTION OF THE LARGE SURROUNDING MASS, MEAN-ZERO POINCARE FORCES A NORMALIZED PALINSTROPHY COST PROPORTIONAL TO THE MASS RATIO, WHICH DIVERGES. THEREFORE DECOMPACTIFICATION ON A PALINSTROPHY-QUIET BRANCH MUST BE MEAN DOMINATED: THE PACKET SITS INSIDE AN ALMOST CONSTANT AMBIENT VORTICITY BACKGROUND WHOSE AMPLITUDE IS LARGE ONLY RELATIVE TO THE TINY PACKET NORMALIZATION. THIS COHERENT-MEAN BRANCH IS DISTINCT FROM PHYSICAL ENERGY BLOWUP AND REQUIRES ITS OWN DYNAMIC/RENORMALIZATION AUDIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Decompactifying surrounding mass

Let `E_j` be the selected intrinsic packet mass used for normalization.

Fix one finite

\[
K>1.
\]

Define

\[
\boxed{
M_{j,K}
:=
\int_{B_{Kr_j}(q_j)}|W_j|^2dy.
}
\]

The M17-255 normalized mass-decompactification branch is

\[
\boxed{
L_{j,K}
:=
\frac{M_{j,K}}{E_j}
\to\infty.
}
\]

The ball radius is only a fixed multiple of the packet scale.

Thus this is not escape to macroscopic similarity distance.

It is a local amplitude/mass mismatch around the selected packet.

---

## 2. Mean/fluctuation decomposition on the larger ball

Let

\[
\boxed{
 c_{j,K}
 :=
 \frac{1}{|B_{Kr_j}|}
 \int_{B_{Kr_j}(q_j)}W_jdy
}
\]

and

\[
\boxed{
 w_{j,K}:=W_j-c_{j,K}.
}
\]

Then

\[
\int_{B_{Kr_j}}w_{j,K}dy=0.
\]

Set the fluctuation mass

\[
\boxed{
F_{j,K}
:=
\int_{B_{Kr_j}}|w_{j,K}|^2dy.
}
\]

Orthogonality gives

\[
\boxed{
M_{j,K}
=F_{j,K}
+|B_{Kr_j}|\,|c_{j,K}|^2.
}
\]

---

## 3. Fixed-fraction fluctuation forces large normalized palinstrophy

Fix

\[
0<\vartheta<1.
\]

Suppose

\[
\boxed{
F_{j,K}\ge\vartheta M_{j,K}.
}
\]

Mean-zero Poincare on a ball of radius `Kr_j` gives

\[
F_{j,K}
\le
C_P(Kr_j)^2
\int_{B_{Kr_j}}|\nabla w_{j,K}|^2dy.
\]

Since

\[
\nabla w_{j,K}=\nabla W_j,
\]

we obtain

\[
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\ge
c_P\vartheta(Kr_j)^{-2}M_{j,K}.
\]

Multiply by `r_j^2/E_j`:

\[
\boxed{
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\ge
c_{P,K}\vartheta
\frac{M_{j,K}}{E_j}.
}
\]

Thus on the decompactifying branch

\[
L_{j,K}\to\infty,
\]

we have

\[
\boxed{
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\to\infty.
}
\]

So fluctuation-dominated normalized mass decompactification is a strong palinstrophy branch.

---

## 4. Quiet decompactification is mean dominated

On the complementary branch assume the normalized local palinstrophy does not diverge.

Then for every fixed `vartheta>0`, after subsequence,

\[
\boxed{
\frac{F_{j,K}}{M_{j,K}}\to0.
}
\]

Therefore

\[
\boxed{
M_{j,K}
\sim
|B_{Kr_j}|\,|c_{j,K}|^2.
}
\]

Since

\[
|B_{Kr_j}|=c_3K^3r_j^3,
\]

while the packet amplitude normalization satisfies

\[
a_j^2r_j^3\asymp E_j,
\]

we obtain

\[
\boxed{
\left|\frac{c_{j,K}}{a_j}\right|^2
\asymp
K^{-3}\frac{M_{j,K}}{E_j}
=K^{-3}L_{j,K}.
}
\]

Hence if `L_{j,K}->infinity`,

\[
\boxed{
|c_{j,K}|/a_j\to\infty.
}
\]

The selected derivative packet is therefore a small relative perturbation of a much larger coherent local mean.

---

## 5. The coherent mean is not automatically a physical blowup

The statement

\[
|c_{j,K}|/a_j\to\infty
\]

is relative to the packet normalization `a_j`.

It does **not** imply

\[
|c_{j,K}|\to\infty
\]

in the original similarity variables.

Both quantities may tend to zero while `a_j` tends to zero faster.

Thus the correct label is

\[
\boxed{
G_{coherent\ ambient\ mean\ dominance},
}
\]

not `amplitude blowup`.

This is another form of the amplitude-scaling firewall identified in M17-242.

---

## 6. Dynamic size of the ambient mean

A local almost-constant vorticity background affects the own-scale dynamics through the velocity-gradient/drift coefficient, not merely through its normalized amplitude.

Define the dimensionless ambient-mean size

\[
\boxed{
\beta_{j,K}
:=
r_j^2|c_{j,K}|.
}
\]

Using

\[
|c_{j,K}|
\asymp
 a_jK^{-3/2}L_{j,K}^{1/2},
\]

we obtain

\[
\boxed{
\beta_{j,K}
\asymp
(a_jr_j^2)
K^{-3/2}L_{j,K}^{1/2}.
}
\]

M17-245 shows

\[
a_jr_j^2\to0
\]

on the low-amplitude self-nonlinear branch.

But the decompactification factor `L_{j,K}^{1/2}` may compensate this decay.

Therefore split again:

\[
\boxed{
\beta_{j,K}\not\to0
\Longrightarrow
G_{scaled\ ambient\ coefficient},
}
\]

while

\[
\boxed{
\beta_{j,K}\to0
}
\]

is a dynamically weak but normalization-dominant coherent background.

The latter is the genuinely new residual.

---

## 7. Why subtracting the mean is not automatically legitimate

It is tempting to replace

\[
W_j
\]

by

\[
W_j-c_{j,K}.
\]

Spatial derivatives are unchanged, but the Navier--Stokes/CE-H equations are not invariant under this subtraction.

M17-232 already established the elliptic firewall

\[
\Delta(W-c)=\kappa(W-c)+\kappa c.
\]

Similarly, the time-dependent similarity equation acquires forcing and background-coupling terms.

Therefore coherent-mean removal requires a separate rescaled dynamic audit.

It cannot be silently quotiented out.

---

## 8. Canonical decompactification split

For every fixed `K`,

\[
\boxed{
G_{normalized\ mass\ decompactification}(K)
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{scaled\ ambient\ coefficient}
\lor
G_{dynamically\ weak\ coherent\ mean\ dominance}.
}
\]

Thus `mass decompactification` is removed as an untyped terminal branch.

The third alternative means

\[
\boxed{
M_{j,K}/E_j\to\infty,
\quad
F_{j,K}/M_{j,K}\to0,
\quad
r_j^2|c_{j,K}|\to0.
}
\]

It is a large **relative** background with vanishing own-scale dynamical coefficient.

---

## 9. Consequence for the heat tangent strategy

If the dynamically weak coherent mean can be subtracted or shown to decouple in the limit, one may recover a fluctuation heat tangent even though the full normalized field is not locally `L2` bounded.

If it cannot be removed, then the correct tangent object is not the raw vorticity `V_j` but a renormalized fluctuation field plus an explicit background parameter.

This is now the narrow normalized-mass frontier.

---

## 10. DSD audit

- Surrounding mass decompactification is tested by an exact mean/variance decomposition.
- A large fluctuation fraction is converted into a quantitative normalized palinstrophy cost.
- Relative mean dominance is not mislabeled as absolute amplitude blowup.
- The dimensionless dynamical size `r_j^2|c|` is separated from the normalized mean size `|c|/a_j`.
- Mean subtraction is not treated as an invariance of CE-H or similarity dynamics.
- The only new residual is a dynamically weak coherent mean background.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
