# DSD M17-448 — Transverse Poincare-gap collapse is a bi-Lipschitz geometry decompactification and costs only logarithmic material deformation, so standard energy alone does not close it

Date: 2026-09-09  
Canonical ID: **M17-448**

Status: **ACTIVE SPECTRAL-GAP GEOMETRY REDUCTION / MATERIAL-DEFORMATION FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-447

M17-447 shows that a robust low-amplitude separating bottleneck is a palinstrophy payer whenever the normalized transverse cross-section has a uniform Poincare constant.

Therefore one explicit escape is

\[
\boxed{C_{P,m}\to\infty,}
\]

where

\[
\int_{A_m}|f-\bar f|^2
\le
C_{P,m}
\int_{A_m}|\nabla f|^2.
\]

The present module identifies the geometric meaning and energy cost of this spectral-gap collapse.

## 2. Reference cross-section and bi-Lipschitz map

Let `A_0` be a fixed connected normalized reference cross-section with Poincare constant

\[
C_{P,0}<\infty.
\]

Suppose a retained cross-section is represented by a `C1` bi-Lipschitz map

\[
F:A_0\to A.
\]

Assume all singular values of `DF` satisfy

\[
\boxed{
m\le s_i(DF)\le M}
\]

with

\[
0<m\le M<\infty.
\]

Then the area Jacobian satisfies

\[
m^2\le J_F\le M^2.
\]

## 3. Poincare constant under bi-Lipschitz transport

Let `f` be a scalar on `A` and set

\[
g=f\circ F.
\]

Using an arbitrary constant `c`,

\[
\int_A|f-c|^2dA
=
\int_{A_0}|g-c|^2J_Fda
\le
M^2\int_{A_0}|g-c|^2da.
\]

Choose the optimal/reference mean constant and apply the Poincare inequality on `A_0`:

\[
\int_A|f-c|^2dA
\le
M^2C_{P,0}
\int_{A_0}|\nabla g|^2da.
\]

Since

\[
|\nabla g|
\le M|\nabla f|\circ F,
\]

and

\[
da\le m^{-2}dA,
\]

we obtain the sufficient estimate

\[
\boxed{
C_P(A)
\le
C_{P,0}\frac{M^4}{m^2}.
}
\]

The exponent is not claimed optimal; what matters is uniformity under bounded bi-Lipschitz distortion.

Therefore

\[
\boxed{
C_P(A_m)\to\infty
\Longrightarrow
M_m\to\infty
\quad\text{or}\quad
m_m^{-1}\to\infty
}
\]

unless the reference topology/chart itself changes.

Thus transverse spectral-gap collapse is a genuine geometry decompactification.

## 4. Material-flow deformation control

Suppose the transverse chart is transported from a material reference chart by the regular incompressible flow map.

Let

\[
K_I
:=
\int_I\|\Sigma(t)\|_\infty dt.
\]

Standard material-line distortion gives, up to rotation,

\[
e^{-K_I}|v|
\le
|DF\,v|
\le
e^{K_I}|v|.
\]

Hence one may take

\[
M\le e^{K_I},
\qquad
m\ge e^{-K_I}.
\]

Section 3 yields

\[
\boxed{
C_P(A)
\le
C_{P,0}e^{6K_I}.
}
\]

Therefore

\[
\boxed{
K_I
\ge
\frac16
\log\frac{C_P(A)}{C_{P,0}}
}
\]

whenever the same material cross-section chart remains valid.

If the chart is not the material image of a retained reference section, keep chart/genealogy/topology loss as an explicit exit instead.

## 5. Thin-neck interpretation

A classical geometric realization of

\[
C_P\to\infty
\]

is a dumbbell-like cross-section: two positive-area lobes are joined by an increasingly thin neck.

M17-448 does not require this particular picture. The spectral gap is the canonical descriptor.

But the interpretation is useful:

\[
\boxed{
\text{low-amplitude bottleneck escapes M17-447 by}
\quad
\text{neck/spectral-gap decompactification}.}
\]

This includes thin-neck, large-diameter, severe eccentricity, or topology/chart degeneration routes.

## 6. Standard-energy cost is only logarithmic

Suppose on record `m`

\[
C_{P,m}\sim m^p
\]

for some `p>0`.

Then Section 4 forces only

\[
K_m
\gtrsim
c\log C_{P,m}
\sim cp\log m.
\]

For geometric inverse record factor

\[
R_m\asymp q^m,
\]

the shrinking physical own-scale is

\[
r_m\asymp R_m^{-1}.
\]

The M17-388 deformation ledger weighs

\[
r_mK_m^2
\lesssim
R_m^{-1}(\log m)^2,
\]

which is summable.

Therefore

\[
\boxed{
C_P\to\infty
\not\Rightarrow
\text{standard-energy contradiction by material deformation alone}.}
\]

This is another logarithmic geometry firewall.

## 7. How fast must the spectral gap collapse to defeat M17-447?

M17-447 gives a palinstrophy lower bound schematically

\[
P_{bot}^{norm}
\gtrsim
\frac{v_*}{C_{P,m}}
\]

per robust own-time bottleneck packet.

If the bottleneck occupies parent-time fraction `beta_m`, then there are order

\[
\beta_mR_m^2
\]

own-time packets. After the M17-307 ancestry weight,

\[
\boxed{
\mathcal P_{anc,m}
\gtrsim
\beta_m
\frac{R_m}{C_{P,m}}.
}
\]

Thus finite ancestral palinstrophy requires

\[
\boxed{
\sum_m
\beta_m
\frac{R_m}{C_{P,m}}
<\infty.
}
\]

For a uniform positive time fraction `beta_m >= beta_*`, a power model in the growing record factor

\[
C_{P,m}\sim R_m^\gamma
\]

has ancestry contribution

\[
R_m^{1-\gamma}.
\]

On geometric records, avoiding divergence requires at least the threshold

\[
\boxed{\gamma\ge1}
\]

(up to borderline slowly varying corrections).

Thus a persistent bottleneck cannot escape merely through logarithmic or polynomial-in-record-index Poincare growth; it needs approximately **record-linear spectral-gap degeneration** if its time occupancy stays positive.

## 8. Deformation needed at the record-linear Poincare threshold

If

\[
C_{P,m}\gtrsim cR_m,
\]

then Section 4 gives

\[
K_m
\gtrsim
c\log R_m.
\]

This is precisely logarithmic deformation in inverse scale, which M17-390/423 already showed is compatible with the standard-energy geometric weight.

Therefore the two ledgers meet at a clear firewall:

- palinstrophy forces record-linear Poincare degeneration for persistent bottlenecks;
- material deformation can create record-linear Poincare degeneration at only logarithmic strain cost;
- standard energy still does not prohibit that cost.

## 9. Updated bottleneck split

\[
\boxed{
\begin{aligned}
G_{low\text{-}amplitude\ separator}
\Longrightarrow{}&
G_{palinstrophy\ payer}\\
&\lor G_{record\text{-}linear\ transverse\ spectral\ gap\ collapse}\\
&\lor G_{bottleneck\ time\ occupancy\ thinning}\\
&\lor G_{high\text{-}amplitude\ flux\ participation\ loss}\\
&\lor G_{chart/topology/genealogy\ loss}.
\end{aligned}
}
\]

The second branch is geometrically explicit but not closed by the standard-energy deformation ledger.

## 10. DSD audit role

DSD is used only to replace a vague `neck geometry loss` by the canonical transverse spectral-gap/Poincare descriptor and compare its cost across ledgers. The proof is elementary bi-Lipschitz transport of Poincare inequalities plus standard material deformation estimates.

## 11. Audit verdict

**PASS — failure of the M17-447 Poincare bridge is a true transverse geometry decompactification.**

For persistent bottlenecks, surviving the palinstrophy ledger requires roughly record-linear Poincare degeneration. That much spectral degeneration costs only logarithmic material strain, so it remains compatible with standard energy and becomes the next explicit geometry frontier rather than a contradiction.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
