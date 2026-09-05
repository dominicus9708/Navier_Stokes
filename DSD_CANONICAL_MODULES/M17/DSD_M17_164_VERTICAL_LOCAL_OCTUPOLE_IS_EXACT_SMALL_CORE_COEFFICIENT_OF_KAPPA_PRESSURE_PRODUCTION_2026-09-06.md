# DSD M17-164 — The vertical local payer octupole is the exact small-core coefficient of the global `-kappa rho^2` axial pressure-production channel

Date: 2026-09-06  
Canonical ID: **M17-164**

Status: **LOCAL-TO-GLOBAL SOURCE BRIDGE / THE GLOBAL AXIAL STF PRESSURE-PRODUCTION CHANNEL ALREADY ISOLATED IN M17-089, `Pi_{V,kappa}^{prod}=-<kappa rho^2,K_333>`, USES THE SAME PAYER SOURCE DENSITY WHOSE FIRST LOCAL ODD TERM DEFINES THE M17-057 OCTUPOLE. FOR A RADIAL CORE CUTOFF `chi_R(z)=chi(|z|/R)`, THE EVEN QUADRATIC SHEATH IS EXACTLY l=3-ORTHOGONAL AND THE CUBIC TERM PAIRS WITH THE NEWTONIAN STF KERNEL BY A UNIVERSAL REPRODUCING CONSTANT: `-int chi_R F_3 K_333 = (6/7)m_chi R^2 O_V`, WHERE `m_chi=int_0^infty chi(s)s ds>0` AND `O_V=(O_loc^(3))_333`. FOR THE SHARP BALL THIS IS `(3/7)R^2 O_V`. HENCE THE SIGN OF THE VERTICAL LOCAL OCTUPOLE IS EXACTLY THE SIGN OF THE SUFFICIENTLY SMALL LOCALIZED KAPPA-PRODUCTION CORE, UP TO `O(R^3)` TAYLOR ERROR. THIS REMOVES THE LOCAL-SOURCE-DENSITY PART OF THE M17-096 COVARIANCE FIREWALL; THE REMAINING GAP IS LABEL WEIGHT / RELATIVE SPEED VERSUS MESOSCOPIC AND GLOBAL SPATIAL CANCELLATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Global kappa-production channel

M17-089 isolates the `-kappa rho^2` contribution to the vertical `l=3` pressure production:

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=-\int_{\mathbb R^3}
\kappa(y)\rho(y)^2
\,\mathcal K_{333}(Y-y)\,dy.
}
\]

The Newtonian STF kernel is

\[
\boxed{
\mathcal K_{333}(z)
=\frac{3}{4\pi}
\frac{z_3(3|z|^2-5z_3^2)}{|z|^7}.
}
\]

Tensorially,

\[
\boxed{
\mathcal K_{ijk}(z)
=-\frac{15}{4\pi}
\frac{STF_3(z^{\otimes3})_{ijk}}{|z|^7}
}
\]

away from the origin.

---

## 2. Local payer expansion

Center the marked vertical regular nodal core at `Y=0`.
M17-056--057 gives

\[
\kappa\rho^2
=F_2+F_3+O(|z|^4),
\]

where `F_2` is inversion even and has only `l=0,2` angular content, while

\[
\boxed{
F_3(z)=T_{ijk}z_iz_jz_k.
}
\]

The local payer octupole tensor is

\[
\boxed{
\mathcal O_{loc}^{(3)}=STF_3T.
}
\]

Define its vertical component

\[
\boxed{
O_V:=(\mathcal O_{loc}^{(3)})_{333}.
}
\]

On the vertical regular filament M17-090 further gives

\[
O_V
=-\frac15\partial_3(\kappa|Q|_F^2),
\]

and at a regular `kappa=0` crossing,

\[
O_V=-\frac15|Q|_F^2\kappa_3.
\]

---

## 3. Radial localized production core

Let `chi:[0,infty)->[0,1]` be smooth, radial, compactly supported, and not identically zero.
Set

\[
\chi_R(z):=\chi(|z|/R).
\]

Define the localized kappa-production core

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
:=-\int
\chi_R(z)
\,\kappa(z)\rho(z)^2
\,\mathcal K_{333}(z)\,dz.
}
\]

Because `F_2` contains no `l=3` component and the cutoff is radial,

\[
\boxed{
\int \chi_R F_2\mathcal K_{333}=0.
}
\]

Thus the first nonzero local term is cubic.

---

## 4. Universal STF reproducing constant

Only the STF part of `T` contributes to the angular pairing.
For any STF rank-three tensor `O`, rotational invariance gives

\[
\int_{S^2}
(O:n^{\otimes3})
\,STF_3(n^{\otimes3})_{333}
\,d\omega
=c_3 O_{333}.
\]

Evaluate on

\[
O=STF_3(e_3^{\otimes3}).
\]

Then

\[
O_{333}=\frac25,
\]

and

\[
O:n^{\otimes3}
=n_3^3-\frac35n_3
=\frac25P_3(n_3).
\]

Using

\[
\int_{S^2}P_3(n_3)^2d\omega=\frac{4\pi}{7},
\]

one obtains

\[
\boxed{
\int_{S^2}
(F_3/r^3)
\,\mathcal K_{333}(rn)r^4
\,d\omega
=-\frac67O_V.
}
\]

Equivalently, the angular factor in the production `-F_3 K_333` is

\[
\boxed{+\frac67O_V.}
\]

---

## 5. Exact radial coefficient

Since

\[
F_3(rn)\sim r^3,
\qquad
\mathcal K_{333}(rn)\sim r^{-4},
\qquad
dz=r^2drd\omega,
\]

the radial factor is `r dr`.
Define

\[
\boxed{
m_\chi:=\int_0^\infty\chi(s)s\,ds>0.}
\]

Then

\[
\int_0^\infty\chi(r/R)r\,dr
=R^2m_\chi.
\]

Therefore

\[
\boxed{
-\int\chi_R(z)F_3(z)\mathcal K_{333}(z)dz
=\frac67m_\chi R^2O_V.
}
\]

For the sharp unit-ball cutoff,

\[
m_\chi=\int_0^1sds=\frac12,
\]

so

\[
\boxed{
-\int_{|z|<R}F_3(z)\mathcal K_{333}(z)dz
=\frac37R^2O_V.
}
\]

---

## 6. Taylor remainder

Assume on a fixed local core

\[
|\kappa\rho^2-F_2-F_3|
\le M_4|z|^4.
\]

Since `|K_333(z)|<=C|z|^-4`,

\[
\left|
\int\chi_R
(\kappa\rho^2-F_2-F_3)
\mathcal K_{333}
\right|
\le C_\chi M_4R^3.
\]

Hence

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac67m_\chi R^2O_V
+O(M_4R^3).
}
\]

Thus for `O_V != 0`, sufficiently small `R` gives

\[
\boxed{
\operatorname{sgn}\Pi_{V,\kappa}^{core}(R)
=\operatorname{sgn}O_V.
}
\]

---

## 7. What this removes from the old firewall

M17-096 correctly stated that the local crossing ledger and the full global pressure state use different measures and different global architectures.

However, for the **kappa-production channel itself**, the local octupole and the global source now share exactly the same density:

\[
\boxed{
\kappa\rho^2.
}
\]

The local octupole is not merely analogous to the global production source. It is the first small-core `l=3` coefficient of that source under the same Newtonian STF kernel.

Therefore the old gap

\[
\text{local payer source}
\quad\text{vs}\quad
\text{global kappa-production source}
\]

is closed at the asymptotic core level.

---

## 8. What remains open

The full global production is

\[
\Pi_{V,\kappa}^{prod}
=\Pi_{V,\kappa}^{core}(R)
+\Pi_{V,\kappa}^{outer}(R).
\]

The outer term is signed and may cancel the local core.
Moreover M17-095 weights the local crossing with

\[
a\,r_V|Q|_F^{-2}\delta(\kappa)d\mu_0,
\]

not current spatial volume.

Thus the remaining firewall has two precise pieces:

1. **label/relative-speed pushforward**;
2. **mesoscopic/global outer cancellation**.

---

## 9. DSD audit

### Audit A — ignoring the singular distribution at the origin
The cubic source vanishes to third order. Its pairing with the homogeneous `r^-4` kernel is locally integrable, so no hidden delta contribution enters this cubic coefficient.

### Audit B — using a nonradial cutoff
The exact `l=3` orthogonality of `F_2` and the scalar reproducing coefficient rely on a radial cutoff. Nonradial cutoffs introduce lower-order angular mixing.

### Audit C — identifying the local core with the full global production
Rejected. The signed outer term remains.

### Audit D — identifying the M5 label current with spatial volume
Rejected. M17-095 remains in force.

### Audit E — proof status
The local-source part of the covariance firewall is reduced, not the full branch.

---

## 10. Updated Rank-1 vertical gate

At a regular vertical zero crossing,

\[
\boxed{
\Pi_{V,\kappa}^{core}(R)
=\frac67m_\chi R^2O_V+O(R^3),
}
\]

and

\[
\boxed{
h=-\frac{5r_V}{|Q|_F^2}O_V.}
\]

Hence M5 hysteresis and global pressure production now meet on the same explicit local octupole variable.

The next gate is to place this localized production coefficient inside the original M5 label measure and isolate the exact remaining outer-cancellation term.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
