# DSD M17-270 — Log-amplitude coupling returns to normalized palinstrophy, first-jet metric escalation, or strict subscale

Date: 2026-09-06  
Canonical ID: **M17-270**

Status: **POLAR-ENERGY RETURN GATE / M17-269 REDUCES BULK DIRECTOR SECOND-JET ESCALATION TO FIRST-JET METRIC GROWTH, LOG-AMPLITUDE COUPLING, OR ACTIVE-SET FAILURE. FOR `V=a xi`, THE EXACT ORTHOGONAL POLAR IDENTITY `|grad V|^2=|grad a|^2+a^2|grad xi|^2=a^2(|grad log a|^2+|grad xi|^2)` SHOWS THAT ON A NONDEGENERATE ACTIVE CORRIDOR `a>=a_*>0`, BULK `grad log a` GROWTH IS ALREADY NORMALIZED PALINSTROPHY. IF THE DIRECTOR FIRST JET IS BOUNDED, DIVERGENCE OF `||grad log a grad xi||_2` THEREFORE FORCES PALINSTROPHY; IF THE FIRST JET IS NOT BOUNDED, THE EVENT RETURNS TO DIRECTOR-METRIC ESCALATION. IF `grad log a` BLOWS UP ONLY IN `L-infinity` WHILE ITS `L2` MASS STAYS BOUNDED, THE EVENT IS A STRICT SMALLER-SCALE AMPLITUDE-GRADIENT MICROCARRIER. FAILURE OF THE AMPLITUDE FLOOR IS THE NODAL/AMPLITUDE-DEGENERATION EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Polar gradient identity

On the raw tangent active set write

\[
V=a\xi,
\qquad a=|V|>0,
\qquad |\xi|=1.
\]

For each spatial direction,

\[
\partial_iV
=(\partial_i a)\xi+a\partial_i\xi.
\]

Since

\[
\xi\cdot\partial_i\xi=0,
\]

the two terms are orthogonal.
Therefore

\[
\boxed{
|\nabla V|^2
=|\nabla a|^2+a^2|\nabla\xi|^2.
}
\]

With

\[
\psi:=\log a,
\qquad
\nabla a=a\nabla\psi,
\]

this becomes

\[
\boxed{
|\nabla V|^2
=a^2\left(|\nabla\psi|^2+|\nabla\xi|^2\right).
}
\]

There is no cross term and no inequality loss.

---

## 2. Active amplitude corridor

Fix a compact rescaled subpatch on which

\[
\boxed{0<a_*\le a\le a^*<\infty.}
\]

The upper bound follows on the compact tangent branch from the local Sobolev/elliptic control already used in M17-251.
The lower bound is an explicit active-set assumption.
Its failure is retained as

\[
G_{nodal/amplitude\ degeneration}.
\]

On this corridor,

\[
\boxed{
\int|\nabla\psi|^2
\le a_*^{-2}\int|\nabla V|^2
}
\]

and

\[
\boxed{
\int|\nabla\xi|^2
\le a_*^{-2}\int|\nabla V|^2.
}
\]

Thus both log-amplitude and director first-jet `L2` masses are paid by normalized palinstrophy when the amplitude is nondegenerate.

---

## 3. M17-269 coupling term

The bulk second-jet gate of M17-269 contains

\[
\boxed{
\|\nabla\psi\,\nabla\xi\|_{L^2}.
}
\]

Split according to the director first-jet size.

### Bounded director first jet

If

\[
\|\nabla\xi\|_{L^\infty}\le G_*,
\]

then

\[
\|\nabla\psi\,\nabla\xi\|_2
\le G_*\|\nabla\psi\|_2.
\]

Hence divergence of the coupling term forces

\[
\|\nabla\psi\|_2\to\infty,
\]

and therefore

\[
\boxed{
\int|\nabla V|^2\to\infty.
}
\]

This is the normalized-palinstrophy branch.

### Unbounded director first jet

If the `L-infinity` ceiling fails, retain

\[
\boxed{G_{director\ first\text{-}jet/metric\ escalation}.}
\]

Thus the product term cannot remain an independent payer.

---

## 4. Pointwise log-gradient spike with bounded L2 mass

Suppose

\[
\|\nabla\psi_j\|_{L^\infty}\to\infty
\]

while

\[
\|\nabla\psi_j\|_{L^2}\le C.
\]

Define the effective concentration volume

\[
\nu_j
:=
\frac{\|\nabla\psi_j\|_2^2}
{\|\nabla\psi_j\|_\infty^2}.
\]

Then

\[
\boxed{\nu_j\to0.}
\]

and the effective length

\[
\boxed{\varepsilon_j:=\nu_j^{1/3}\to0.}
\]

Thus a pure pointwise log-amplitude-gradient blowup with bounded bulk energy is a strict smaller-scale amplitude-gradient microcarrier.

It is not a bulk palinstrophy charge.

---

## 5. Correct log-amplitude split

Therefore

\[
\boxed{
G_{log\text{-}amplitude\ coupling}
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{director\ first\text{-}jet/metric\ escalation}
\lor
G_{strict\ amplitude\text{-}gradient\ subscale}
\lor
G_{nodal/amplitude\ degeneration}.
}
\]

Combined with M17-269,

\[
\boxed{
G_{director\ second\text{-}jet\ spike}
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{director\ first\text{-}jet/metric\ escalation}
\lor
G_{strict\ higher\text{-}derivative\ subscale}
\lor
G_{nodal/interface}.
}
\]

up to the explicit distinction between bulk and pointwise-only concentrations.

---

## 6. Relation to low-amplitude physical variables

This theorem is stated in the own-amplitude normalized tangent variables.

It does not claim that the corresponding physical palinstrophy is amplitude independent before normalization.
The amplitude-scaling firewall of M17-242 remains valid.

The conclusion is instead that within the selected nonzero normalized tangent, the log-amplitude coupling cannot act as a free geometric source.

---

## 7. DSD audit

- The polar identity is exact.
- An amplitude lower bound is never inferred from nonzero pointwise value; it is an explicit corridor condition.
- Failure of the lower bound is routed to nodal/amplitude degeneration.
- `L-infinity` spikes are separated from bulk `L2` growth.
- Normalized palinstrophy is not silently identified with an amplitude-independent physical tail budget.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
