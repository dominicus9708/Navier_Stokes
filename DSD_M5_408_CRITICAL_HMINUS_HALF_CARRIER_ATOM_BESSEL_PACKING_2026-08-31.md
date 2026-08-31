# DSD M5-408 — Critical H^{-1/2} carrier atoms and phase-space Bessel packing

Date: 2026-08-31

Status: **A NATURAL FIRST-HITTING FLUX CARRIER HAS A SCALE-INVARIANT NONZERO COEFFICIENT IN THE CRITICAL VORTICITY SPACE `\dot H^{-1/2}`, EQUIVALENT TO THE VELOCITY SPACE `\dot H^{1/2}` / PHASE-SPACE SEPARATED CARRIERS FORM AN ALMOST-ORTHOGONAL BESSEL FAMILY, SO EACH DISTINCT COHERENT CARRIER COSTS AN ORDER-ONE AMOUNT OF CRITICAL SOBOLEV PACKET MASS WITHOUT THE SHRINKING `r_j` WEIGHT OF THE EARLIER L2/ENERGY LEDGERS / THIS PROVIDES A RECENTER- AND SCALE-INVARIANT COMMON PACKET COUNTER FOR LOCAL AND REMOTE FORMATION, BUT THE CRITICAL SOBOLEV NORM IS NOT A PRIORI BOUNDED ON A HYPOTHETICAL SINGULAR CORRIDOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-407 reduced the current frontier to

\[
H_{local}^{crit}
\lor
S_{remote}^{iterated}
\lor
T_{interface}^{projective/export/realization}.
\]

The next target was a common scale-space quantity satisfying

1. Navier--Stokes scale invariance;
2. translation/recentering invariance;
3. no double counting of genuinely separated scale-space packets.

Earlier Gaussian/Bessel packing in `L2` already removed cross-scale double counting for mean strain, but its physical packet weight was proportional to the shrinking length scale. Consequently a geometric cascade could still have finite total cost.

A natural vorticity carrier suggests the critical Sobolev pair instead:

\[
\boxed{
\omega\in\dot H^{-1/2}
\quad\Longleftrightarrow\quad
u_{vel}:=u\in\dot H^{1/2}.
}
\]

For divergence-free velocity the two norms are equivalent, and under Navier--Stokes scaling both are invariant.

The purpose of this note is to show that every coherent natural flux carrier gives an order-one coefficient in this space, and that phase-space separated carriers can be counted by Bessel packing.

---

## 2. Natural coherent carrier data

Take a smooth first-hitting or point-picked carrier centered at `x0` with natural radius `r`.

Retain a fixed geometric sub-ball

\[
B_{\rho r}(x_0),
\qquad 0<\rho<1,
\]

and a unit direction `e` such that

\[
\boxed{
\omega(x)\cdot e
\ge
c_\omega\frac{\nu}{r^2}
\quad\text{for }x\in B_{\rho r}(x_0).
}
\]

This is exactly the type of thick directed packet provided by the first-hitting Taylor carrier and by the M5-394 natural companion construction after rescaling back to physical variables.

The corresponding directed flux through a transverse natural disk is of order

\[
\Phi\asymp \nu.
\]

The new calculation uses the thick ball rather than a codimension-one surface, avoiding trace/capacity ambiguities.

---

## 3. A normalized critical test atom

Choose once and for all

\[
\varphi\in C_c^\infty(B_\rho),
\qquad
\varphi\ge0,
\qquad
\int\varphi>0.
\]

Define the vector test atom

\[
\boxed{
\psi_{r,x_0,e}(x)
:=
\frac1r
\varphi\!\left(\frac{x-x_0}{r}\right)e.
}
\]

The homogeneous Sobolev scaling law in three dimensions gives

\[
\|a\,\varphi((\cdot-x_0)/r)\|_{\dot H^{1/2}}
=
|a|r^{3/2-1/2}
\|\varphi\|_{\dot H^{1/2}}.
\]

With `a=r^{-1}`,

\[
\boxed{
\|\psi_{r,x_0,e}\|_{\dot H^{1/2}}
=
\|\varphi e\|_{\dot H^{1/2}}
=:C_\varphi,
}
\]

independent of `r` and `x0`.

Thus `psi` is a scale- and translation-normalized critical probe.

---

## 4. Every natural flux carrier has an order-one critical coefficient

Using the coherent sign in the carrier ball,

\[
\begin{aligned}
\langle\omega,\psi_{r,x_0,e}\rangle
&=
\frac1r
\int
\omega(x)\cdot e
\varphi\!\left(\frac{x-x_0}{r}\right)dx\\
&\ge
\frac1r
c_\omega\frac{\nu}{r^2}
\int
\varphi\!\left(\frac{x-x_0}{r}\right)dx\\
&=
 c_\omega\nu
\int\varphi(y)dy.
\end{aligned}
\]

Hence

\[
\boxed{
|\langle\omega,\psi_{r,x_0,e}\rangle|
\ge c_*\nu>0,
}
\]

where `c_*` depends only on the retained normalized carrier constants.

By duality,

\[
\boxed{
\|\omega\|_{\dot H^{-1/2}}
\ge
\frac{c_*}{C_\varphi}\nu.
}
\]

This lower bound contains no factor of `r`.

That is the central improvement over ordinary local enstrophy or physical kinetic-energy charges.

---

## 5. Equivalence with the velocity critical norm

For divergence-free `u`,

\[
\widehat\omega(\xi)
=i\xi\times\widehat u(\xi),
\qquad
\xi\cdot\widehat u=0.
\]

Therefore

\[
|\widehat\omega(\xi)|
=|\xi|\,|\widehat u(\xi)|
\]

and consequently

\[
\begin{aligned}
\|\omega\|_{\dot H^{-1/2}}^2
&=
\int |\xi|^{-1}|\widehat\omega(\xi)|^2d\xi\\
&=
\int |\xi|\,|\widehat u(\xi)|^2d\xi\\
&=
\boxed{\|u\|_{\dot H^{1/2}}^2.}
\end{aligned}
\]

Thus each formed carrier is an order-one atom in the standard critical velocity Sobolev norm.

---

## 6. Cross-scale overlap of the critical test atoms

Ignore center separation first and take two atoms at the same direction and center with scales

\[
0<r\le R.
\]

Their Fourier transforms have the form

\[
\widehat\psi_r(\xi)
=r^2e^{-ix_0\cdot\xi}\widehat\varphi(r\xi)e,
\]

\[
\widehat\psi_R(\xi)
=R^2e^{-ix_0\cdot\xi}\widehat\varphi(R\xi)e.
\]

The `dot H^{1/2}` inner product is

\[
\langle\psi_r,\psi_R\rangle_{\dot H^{1/2}}
=
\int |\xi|\,
\widehat\psi_r(\xi)
\overline{\widehat\psi_R(\xi)}d\xi.
\]

Putting `eta=R xi` gives the scale factor

\[
\boxed{
|\langle\psi_r,\psi_R\rangle_{\dot H^{1/2}}|
\le
C_\varphi\left(\frac rR\right)^2.
}
\]

The exponent two is not important; strict positive-power decay is enough.

Therefore geometrically separated scales

\[
r_{j+1}\le\theta r_j,
\qquad0<\theta<1,
\]

have exponentially summable Gram overlap.

This is the critical-space analogue of the earlier Gaussian L2 Bessel packing, but now the carrier coefficient itself is scale neutral.

---

## 7. Comparable-scale spatial separation

For comparable radii

\[
r_i\asymp r_j\asymp r
\]

with centers separated by

\[
|x_i-x_j|\ge K r,
\]

the smooth compactly supported atoms have rapidly decaying critical Sobolev interaction.

Using either the Fourier oscillation or the singular-integral representation of the `dot H^{1/2}` inner product gives, for any fixed sufficiently large decay power after choosing a smooth atom,

\[
\boxed{
|\langle\psi_i,\psi_j\rangle_{\dot H^{1/2}}|
\le C_N(1+K)^{-N}
}
\]

up to a harmless weaker polynomial exponent if one uses only the elementary fractional-kernel estimate.

For a uniformly separated family in `R3`, the number of centers in the `m`-th spatial shell grows only quadratically in `m`, so any decay exponent greater than three gives a summable Gram row.

Thus scale separation and ordinary spatial separation can be combined into one phase-space almost-orthogonality condition.

---

## 8. Phase-space Bessel theorem

Let

\[
\{(x_i,r_i,e_i)\}_{i\in I}
\]

be a family of coherent carrier atoms such that its critical probes have uniformly summable Gram rows. A sufficient condition is a standard phase-space separation rule: whenever two scales are comparable, their centers are separated by a fixed multiple of that scale; otherwise their scale ratio is geometrically separated.

Then the Schur test gives

\[
\boxed{
\sum_{i\in I}
|\langle f,\psi_i\rangle|^2
\le
C_{pack}
\|f\|_{\dot H^{-1/2}}^2.
}
\]

Apply this to `f=omega`.

Since every retained carrier satisfies

\[
|\langle\omega,\psi_i\rangle|
\ge c_*\nu,
\]

we obtain

\[
\boxed{
N_{carrier}\,c_*^2\nu^2
\le
C_{pack}
\|\omega\|_{\dot H^{-1/2}}^2
=
C_{pack}
\|u\|_{\dot H^{1/2}}^2.
}
\]

Equivalently,

\[
\boxed{
N_{carrier}
\lesssim
\nu^{-2}
\|u\|_{\dot H^{1/2}}^2.
}
\]

This is a true scale-invariant packet-count inequality.

---

## 9. Why this is the common local/remote carrier unit

The construction does not know whether the packet was created as

- the main first-hitting Taylor carrier;
- the M5-394 misaligned natural companion;
- a generic M5-395 replacement carrier;
- a point-picked remote satellite;
- a remote-of-remote satellite;
- a coherent local direction/capacity packet.

It only uses the final formed descriptor

\[
\boxed{
\text{natural radius }r
+
\text{thick directed vorticity of size }\nu/r^2.
}
\]

Thus the same critical coefficient counts both `H_local^crit` packets and `S_remote` packets.

This is precisely the common scale-space unit requested after M5-407.

---

## 10. Relation to energy and enstrophy packet costs

The same coherent packet has the familiar scaling

\[
\text{kinetic-energy scale}\sim \nu^2r,
\]

and

\[
\text{enstrophy scale}\sim \frac{\nu^2}{r}.
\]

Their geometric mean is scale invariant:

\[
\sqrt{
u^2r\cdot\nu^2/r}=\nu^2.
\]

This is exactly what the critical Sobolev norm detects.

Indeed the standard interpolation inequality

\[
\|u\|_{\dot H^{1/2}}^2
\le
\|u\|_2\,\|\nabla u\|_2
\]

has the same energy--enstrophy product structure.

The present atom theorem is stronger as a formation descriptor because it assigns a fixed critical coefficient to each phase-space separated coherent carrier rather than only estimating the total norm.

---

## 11. DSD no-double-counting rule

A material label is not itself a new Sobolev atom.

Two old/new material populations occupying the same Eulerian phase-space cell with the same total vorticity cannot be counted twice in the present ledger merely because their particle identities differ.

Likewise a carrier seen at two nearby centers/scales is one packet unless the corresponding critical probes are phase-space separated enough to enter the Bessel family.

Therefore

\[
\boxed{
\text{material multiplicity}
\not\Rightarrow
\text{critical Sobolev multiplicity}
}
\]

without Eulerian phase-space separation.

The existing material multiflux theorem remains the appropriate tool for label multiplicity inside one common cell.

This prevents a new form of double counting.

---

## 12. What the theorem does not close

The critical Sobolev norm is not controlled by the Leray kinetic-energy inequality.

Indeed a hypothetical finite-time singularity is fully compatible with

\[
\|u(t)\|_{\dot H^{1/2}}\to\infty.
\]

Therefore the packet-count estimate does not by itself contradict an unbounded number of critical atoms.

The gain is structural:

\[
\boxed{
\text{unbounded phase-space novelty}
\Longrightarrow
\|u\|_{\dot H^{1/2}}\text{ escalation}.
}
\]

Conversely, a corridor with uniformly bounded critical Sobolev norm can contain only uniformly finitely many mutually phase-space-separated natural carrier atoms at one time.

---

## 13. Updated target

The remaining problem can now be split by **critical phase-space novelty**.

### A. Novelty grows

Then

\[
N_{carrier}\to\infty
\Longrightarrow
\|u\|_{\dot H^{1/2}}\to\infty.
\]

This is a concrete critical H route.

### B. Novelty stays bounded

Then repeated local/remote formation must reuse a finite collection of Eulerian phase-space cells up to bounded overlap.

That is a recurrence/reuse problem rather than a packing problem and should be compared with the M5-398/M5-405 complete-ancient/Liouville machinery and with material-flux reuse.

The next high-value calculation is therefore to prove a **novelty-or-recurrence dichotomy for the iterated remote chain** in one common physical snapshot/time-slab, without assuming monotonicity of the successive satellite scales.

---

## 14. Audit verdict

### DERIVED

- a natural coherent flux carrier gives an order-one `dot H^{-1/2}` vorticity coefficient;
- this equals an order-one `dot H^{1/2}` velocity critical atom;
- scale- and space-separated carrier probes have summable Gram overlap;
- phase-space separated carriers obey the Bessel packet-count bound
  \[
  N\nu^2\lesssim\|u\|_{\dot H^{1/2}}^2;
  \]
- the construction is scale and translation invariant and does not carry the shrinking physical `r` weight.

### FIREWALL

- material labels are not counted twice inside one Eulerian phase-space cell;
- packet count is instantaneous/phase-space, not a free sum across different times;
- the critical Sobolev norm may diverge on a hypothetical singular corridor.

### STILL OPEN

- convert iterated remote recursion into either unbounded phase-space novelty or a compact recurrent class;
- obtain a coercive time-throughput law stronger than mere critical-norm escalation;
- generic projective/export interface routing;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]