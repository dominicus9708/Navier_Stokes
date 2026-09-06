# DSD Deep Audit — Eigen-Gap Directional Packets: Endpoint and Small-Gap Gates

Date: 2026-09-06
Target family: *3D Navier-Stokes Global Regularity via Eigen-Gap Carleson Packing and Directional Packet Analysis* (Zenodo 17547746 / 17547747) and its directional-microlocal predecessors.
Status: **EARLIER L1 ENDPOINT FAIL_ROOT; LATEST VERSION OPEN_DEEP AT TWO EXPLICIT GATES**

## 1. Version separation

An earlier directional microlocal-Carleson description advertised a bound of the form

\[
\int_0^\infty \|\omega(t)\|_{L^1_x}\,dt\le C(\nu,E_0)
\]

and then a regularity conclusion.

Spatial `L^1` vorticity is not the Beale-Kato-Majda endpoint. Concentration can preserve `L^1` while `L^infinity` diverges. Thus

\[
\boxed{L^1_x\not\Rightarrow L^\infty_x.}
\]

The later Nov. 2025 eigen-gap packet version describes a separate “classical endpoint inequality” converting the ledger to maximum vorticity. The later version must therefore be audited on its own formula, not rejected solely because of the predecessor.

## 2. Endpoint gate

For continuation, one needs an actual regularity norm such as the BKM quantity

\[
\int_0^T\|\omega(t)\|_\infty\,dt.
\]

Suppose the directional ledger controls a packet quantity `L(t)` built from weighted energies, areas, counts, or Carleson masses. A valid endpoint theorem must display an estimate such as

\[
\|\omega(t)\|_\infty
\le F(L(t),\text{known lower-order norms})
\]

with the correct scaling and without consuming an unproved higher norm.

Checks required:

- amplitude homogeneity under `u -> A u`;
- packet reconstruction at a point, including overlaps;
- high-frequency summation in `ell^1` or another endpoint-sufficient sequence space;
- no conversion of an averaged/Carleson quantity into a supremum merely by naming it an endpoint functional.

## 3. Small eigen-gap gate

The packets are aligned to the dominant stretching eigenvector of a smoothed strain tensor. Near eigenvalue collision, that direction is unstable.

If `P_1` is the top eigenprojector and `gap=lambda_1-lambda_2`, then

\[
|\nabla P_1|\lesssim \frac{|\nabla S|}{gap}.
\]

Hence the analytic sublevel/Carleson theorem must prove that the region where `gap` is small has enough sparsity or low physical charge to absorb the inverse-gap commutator.

Mere analyticity of the smoothed strain is insufficient to produce solution-independent sublevel exponents: analytic eigen-gaps can vanish to arbitrarily high finite order.

## 4. Packet completeness gate

Directional packets must reconstruct the relevant vorticity without an omitted residual:

\[
\omega
=
\sum_{j,\theta} \omega_{j,\theta}
+
\omega_{degenerate}
+
\omega_{interface}
\]

schematically.

The last two terms cannot be discarded. The degenerate-axis set and moving-frame interface are exactly where the decomposition is least stable.

A Carleson packing theorem must therefore control the complete reconstruction, not only selected “active” packets.

## 5. Relation to M17-300/301

The useful lesson for the internal Fourier-band genealogy is:

\[
\boxed{
\text{Carleson sparsity controls counting/measure, but continuation still requires an amplitude-correct endpoint bridge.}
}
\]

Also, moving directional frames must retain the analog of M17's leakage term rather than assuming frame-local packet identity is preserved.

New regression test:

\[
\boxed{
R27:\ \text{directional packet ledger must export to a genuine continuation norm and price small-gap/frame leakage explicitly.}
}
\]

## 6. Verdict

Current status:

\[
\boxed{
\begin{aligned}
&\text{earlier }L^1\text{-endpoint formulation: FAIL_ROOT},\\
&\text{latest eigen-gap packet version: OPEN_DEEP}.
\end{aligned}}
}
\]

The two decisive remaining theorems are:

1. the advertised maximum-vorticity endpoint inequality;
2. the uniform small-eigen-gap Carleson/commutator estimate.

If both are proved with scale- and solution-uniform constants and the packet reconstruction is exhaustive, this family contains material of direct relevance to M17.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
