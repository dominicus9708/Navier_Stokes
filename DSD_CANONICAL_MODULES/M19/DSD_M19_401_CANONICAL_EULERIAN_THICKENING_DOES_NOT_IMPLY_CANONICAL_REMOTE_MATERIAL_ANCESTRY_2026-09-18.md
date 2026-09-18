# M19-401 — Canonical Eulerian thickening does not imply canonical remote material ancestry; zero-flux seeds reduce to latent sublabels plus renewal

Date: 2026-09-18

Status: **CANONICAL RECOMPRESSION / M19-400'S MATERIAL-SUBPARTITION FIREWALL IS COMBINED WITH M17-120, M18-045, AND M19-358--364. UNIFORM ANALYTIC/FIXED-JET COMPACTNESS CAN THICKEN AN ORDER-ONE CURVATURE OR VORTICITY MARK INTO A ROBUST EULERIAN PACKET OF NATURAL FIRST-HITTING SIZE, BUT IT DOES NOT FORCE THE REMOTE MATERIAL PREIMAGE OF THE FUTURE CARRIER TO BE THE SAME THICK PACKET. IN FACT M17-120 SHOWS THAT ONE MATERIAL RIBBON CARRIER CAN REMAIN IN THE SAME COMPACT FIRST-HITTING CLASS FOR ONLY FINITELY MANY STAGES. THEREFORE A REMOTE-PAST ZERO-FLUX CRITICAL SEED MUST BE READ AS A LATENT MATERIAL SUBLABEL EMBEDDED IN LARGER EULERIAN STRUCTURE UNTIL A FINITE-STAGE CANONICALIZATION/RENEWAL EVENT. THE NEW SEED-CANONICALITY GATE IS THUS NOT AN INDEPENDENT ROOT; IT RECONNECTS TO THE EXISTING RENEWAL/REPLACEMENT/TURNOVER FRONTIER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two notions of “canonical seed”

The previous modules expose two distinct objects that must not be identified.

### Eulerian canonical packet

At a first-hitting/record state, analyticity and fixed jet margins can thicken a nontrivial pointwise carrier into a packet with fixed normalized:

- radius,
- amplitude,
- derivative margins,
- local enstrophy,
- and, on the coherent flux/tube branch, a natural scale-invariant flux fraction.

This is a canonical **Eulerian** object selected by the first-hitting construction.

### Material ancestral sublabel

The future packet also contains infinitely many possible material subsets.

Tracing one such subset backward gives a material ancestor that may have arbitrarily small flux/volume:

\[
\Phi(\theta_0)\ll1,
\qquad
V(\theta_0)\ll1.
\]

M19-400 proves that smoothness of the ambient packet does not prevent this.

Hence

\[
\boxed{
\text{canonical Eulerian packet}
\neq
\text{canonical remote material sublabel}.
}
\]

---

## 2. Robust Eulerian thickening still holds

Suppose a retained seed point satisfies a fixed curvature-amplitude mark

\[
Z_{\rm curv}
=
\rho|\mathcal K|
\ge z_*>0
\]

and the compact all-order hull gives

\[
|\nabla Z_{\rm curv}|
\le C_Z.
\]

Then on a ball of radius

\[
r_*:=\frac{z_*}{2C_Z}
\]

one has

\[
Z_{\rm curv}\ge \frac{z_*}{2}.
\]

Thus an order-one pointwise mark cannot be supported on a spatial set of arbitrarily small Eulerian diameter inside the normalized compact branch.

The same principle applies to any fixed-margin amplitude/jet observable used in the first-hitting construction.

Therefore

\[
\boxed{
\text{order-one retained mark}
\Longrightarrow
\text{robust Eulerian neighborhood}.
}
\]

This is a legitimate compactness thickening statement.

---

## 3. But the future material ancestor may occupy only a tiny part of that neighborhood

Let \(C(\theta)\) be the robust Eulerian neighborhood from Section 2.

At one reference time choose a material subset

\[
A_\varepsilon(\theta)\subset C(\theta)
\]

with arbitrarily small positive transverse flux.

Following exactly that material subset forward does not alter the surrounding Eulerian field.

At the critical seed rate,

\[
D_B\log\Phi
\approx \frac32,
\]

so a base flux

\[
\Phi_0\asymp e^{-3T/2}
\]

may become order one after time \(T\).

Therefore the existence of the robust ambient packet at the base time does **not** imply

\[
\Phi_0\gtrsim1
\]

for the distinguished future material ancestor.

The ancestor can be a latent material sublabel inside a much larger robust Eulerian packet.

---

## 4. M17-120 rules out remote persistence of one canonical material ribbon

On the compact ribbon branch, M17-120 proves that the physical per-flux volume is material-invariant, while its similarity value changes by the fixed factor

\[
q^{3/2}
\]

per first-hitting stage.

Hence one fixed material loop can remain in the same compact ribbon class for at most

\[
\boxed{
M_{\rm stage}
\le
1+
\left\lfloor
\frac{2}{3\log q}
\log\frac{v_+}{v_-}
\right\rfloor
}
\]

stages.

Therefore a remote-age recurrent Eulerian ribbon packet cannot be represented by one material loop that stays canonical through arbitrarily many generations.

Thus the desired statement

\[
\text{future canonical core}
\Rightarrow
\text{remote ancestor was already the same canonical core}
\]

is generally false on the ribbon branch.

---

## 5. Canonicalization occurs only within a finite stage window

If a material seed is a fixed-flux canonical carrier at activation stage \(j\), then tracing it backward by more than \(M_{\rm stage}\) stages necessarily leaves the same compact ribbon class, unless a typed representation/geometry exit occurs.

Therefore a long critical seed history naturally decomposes as

\[
\boxed{
\text{remote latent material sublabel}
\longrightarrow
\text{finite-stage canonicalization/renewal window}
\longrightarrow
\text{active first-hitting carrier}.
}
\]

The long \(3/2\) amplification prehistory can therefore occur mostly while the selected material subset is **not yet** the canonical first-hitting carrier.

This explains why a minimum canonical packet size at activation does not defeat the M19-362--364 discounted seed witness.

---

## 6. M18-045 classifies the canonicalization window

For a fixed finite generation lag, M18-045 gives the exhaustive comparison

\[
\boxed{
G_{\rm fixed\text{-}lag\ genealogy}
\Longrightarrow
G_{\rm contact}
\lor
G_{\rm paid\ exposure}
\lor
G_{\rm replacement}.
}
\]

Thus when the latent sublabel becomes part of the next robust canonical carrier, there is no fourth quiet mechanism.

The transition is represented by:

1. genuine material contact with the earlier canonical packet;
2. paid strain/deformation/diffusion exposure;
3. or replacement by new high-vorticity material.

Hence

\[
\boxed{
\text{latent seed}
\to
\text{canonical carrier}
}
\]

is already a typed finite-stage genealogy event.

---

## 7. Relation to the natural first-hitting flux scale

On the natural first-hitting core,

\[
W_j r_j^2
\]

is scale invariant (equal to the viscosity-normalized constant in the repository convention).

Therefore a fixed-fraction replacement of a thick natural first-hitting core is a fixed-fraction replacement of **scale-invariant current flux**, not merely a shrinking-volume event.

This does not imply a non-discounted remote base-flux charge.

It means only that **once canonicalization occurs**, the carrier has entered the existing fixed-flux finite-memory genealogy.

That is exactly the regime treated by M19-358--359.

---

## 8. The zero-flux ancient seed is therefore not a new root

Combine:

- M19-399: remote-past zero-flux histories escape complete zero-to-zero excursion closure;
- M19-400: arbitrary material subdivision defeats a smoothness-only minimum flux;
- M17-120: one material canonical ribbon persists only finitely many stages;
- M18-045: finite-stage canonicalization is contact/exposure/replacement;
- M19-358--359: positive curvature activity forces positive renewal and discharge density.

Then

\[
\boxed{
G_{\rm remote-past/zero-flux}^{reset}
}
\]

does not require a new independent “minimum seed flux” root.

It refines to

\[
\boxed{
G_{\rm latent\ sublabel}^{3/2}
\longrightarrow
G_{\rm finite\text{-}stage\ renewal/replacement}
\longrightarrow
G_{\rm discounted\ turnover}
\lor
G_{\rm typed\ exit}.
}
\]

The genuine unresolved step remains the **non-discounted cost of renewal**, not the existence of a canonical remote ancestor.

---

## 9. Corrected theorem target

M19-400 proposed

\[
\mathcal T_{\rm canonical}^{seed}.
\]

The corrected target is narrower:

\[
\boxed{
\mathcal T_{\rm activation}^{nonreuse}:
\text{show that repeated latent-sublabel}\to\text{canonical-carrier activations incur a non-discounted cost,}
}
\]

or else force one of the already typed:

\[
G_{\rm paid\ exposure},
\quad
G_{\rm projective/representation},
\quad
G_{\rm export},
\quad
G_{\rm H/high\text{-}jet},
\quad
G_{\rm remote/tail}.
\]

This is the same global turnover frontier isolated independently by M19-359--360.

---

## 10. Audit verdict

**PASS AS A RECOMPRESSION / NO-GO FOR REMOTE CANONICAL-ANCESTRY REQUIREMENT.**

Eulerian compactness can make the **field packet** robust.

It cannot make an arbitrary remote material ancestor thick.

Moreover, the repository already proves that remote same-material canonical ancestry is generally impossible on the ribbon branch.

The correct object is therefore a latent material sublabel that is promoted into a canonical carrier through finite-stage renewal.

The proof frontier returns to:

\[
\boxed{
\text{activation/renewal nonreuse under critical }e^{-3T/2}\text{ discount}.
}
\]

---

\[
\boxed{\text{M19-401 COMPLETE; REMOTE ZERO-FLUX SEEDS ARE LATENT SUBLABELS PLUS FINITE-STAGE CANONICALIZATION, NOT PERSISTENT CANONICAL MATERIAL CORES.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
