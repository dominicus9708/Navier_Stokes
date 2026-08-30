# DSD M5-302 — Morrey–Dissipation–Amplification Exponent Feasibility and No-Go Region

Date: 2026-08-30

Parent: `DSD_M5_301_OCCUPIED_PACKET_PERSISTENCE_DISSIPATION_AND_SEREGIN_WEIGHTED_EF_CAPACITY_2026-08-30.md`

Status: **EXACT EXPONENT OPTIMIZATION / MORREY CAPACITY `N<=CL` PLUS BOUNDED SEREGIN-WEIGHTED DISSIPATION `N Theta^2<=CL^3` GIVES AN EXPLICIT MAXIMUM POSSIBLE PACKET-DOMINATED MIXED NORM / IN A LARGE ADMISSIBLE EXPONENT REGION, INCLUDING ALL `1<l<2` WITH `s<=3l/(l-1/2)`, THE MAXIMUM HAS NONPOSITIVE POWER OF `L`, SO `g(ell)->0` FORCES `g M_kappa ->0` AND EXCLUDES THE AMPLIFIED PACKET CLOUD / GLOBAL REGULARITY UNPROVED.**

---

## 1. Three inequalities

On the occupied packet-dominated branch assume:

### Morrey capacity

\[
\boxed{N\le C_ML.}
\]

### Weighted dissipation capacity

\[
\boxed{N\Theta^2\le C_EL^3.}
\]

### Mixed-norm packet model

\[
\boxed{
M_\kappa^{s,l}
\lesssim
\Theta L^{-\kappa}N^{l/s}.
}
\]

Here

\[
\boxed{
\kappa
=l\left(\frac3s+\frac2l-1\right)
=2+\frac{3l}{s}-l.
}
\]

Seregin's Type-II amplification condition is

\[
\boxed{
g(\ell)M_\kappa^{s,l}\ge\varepsilon_0,}
\]

with

\[
g(\ell)\to0.
\]

---

## 2. Optimize persistence at fixed packet number

The weighted-dissipation ceiling gives

\[
\Theta
\le
C_E^{1/2}L^{3/2}N^{-1/2}.
\]

Therefore

\[
M_\kappa
\lesssim
L^{3/2-\kappa}
N^{\frac ls-\frac12}.
\]

The remaining optimization is over

\[
1\le N\le C_ML.
\]

---

## 3. Case I: `l/s >= 1/2`

If

\[
\frac ls\ge\frac12,
\]

the right-hand side increases with `N`, so maximize at `N~L`:

\[
M_\kappa
\lesssim
L^{3/2-\kappa}
L^{l/s-1/2}
=
L^{\beta_1},
\]

where

\[
\boxed{
\beta_1
=1+\frac ls-\kappa
=l-1-\frac{2l}{s}.
}
\]

Thus amplification requires

\[
\boxed{
g(\ell)L^{\beta_1}\gtrsim1.}
\]

If `beta_1<=0`, this is impossible because `L->infinity` and `g(ell)->0`.

---

## 4. Case II: `l/s <= 1/2`

If

\[
\frac ls\le\frac12,
\]

the maximum occurs at the smallest packet count, `N~1`:

\[
M_\kappa
\lesssim
L^{\beta_2},
\]

with

\[
\boxed{
\beta_2
=\frac32-\kappa
=l-\frac12-\frac{3l}{s}.
}
\]

Again, if

\[
\beta_2\le0,
\]

then

\[
\boxed{g(\ell)M_\kappa\to0}
\]

and the amplified packet branch is impossible.

---

## 5. Combined no-go region for `1<l<2`

For `1<l<2`, consider the two cases.

### Region `s<=2l`

Here `l/s>=1/2`, so use `beta_1`.

Since

\[
s\le2l
\]

and `l<2`, one has

\[
\beta_1
=l-1-\frac{2l}{s}
\le
l-2
<0.
\]

Hence the whole region

\[
\boxed{1<s\le2l}
\]

is excluded.

### Region `s>=2l`

Use

\[
\beta_2
=l-\frac12-\frac{3l}{s}.
\]

The condition `beta_2<=0` is

\[
\boxed{
s\le\frac{3l}{l-1/2}.}
\]

For `1<l<2`,

\[
\frac{3l}{l-1/2}>2l.
\]

Therefore the two intervals join continuously and give

\[
\boxed{
1<l<2,
\qquad
1<s\le\frac{3l}{l-1/2}
\Longrightarrow
\text{packet-dominated amplification impossible}.
}
\]

This conclusion is subject, of course, to Seregin's own admissibility conditions on `(s,l)` and the packet/Morrey/weighted-dissipation hypotheses.

---

## 6. Examples

### `l=3/2`

\[
\frac{3l}{l-1/2}
=\frac{9/2}{1}
=\frac92.
\]

Thus

\[
\boxed{
1<s\le4.5
}
\]

is in the no-go range.

### `l->2^-`

The threshold tends to

\[
\frac{6}{3/2}=4.
\]

### `l->1^+`

The threshold tends to

\[
\frac3{1/2}=6.
\]

So for `1<l<2` the no-go threshold in `s` ranges from approximately `6` down to `4`.

---

## 7. Residual exponent-positive region

The only packet-dominated exponent region not removed by this algebra is

\[
\boxed{
\beta(s,l)>0.
}
\]

For `1<l<2` this means

\[
\boxed{
s>\frac{3l}{l-1/2}.}
\]

There amplification is possible only if the separation grows fast enough to overcome the vanishing factor `g(ell)`:

\[
\boxed{
g(\ell)L^{\beta(s,l)}\gtrsim1.}
\]

This is an **extreme separation-rate branch**, not a generic amplified cloud.

It should be compared next with:

- the energy-shield relation from M5-282/M5-286;
- Seregin's additional restrictions `s<p(eta), l<q(eta)`;
- the weighted pressure bound `D_f`;
- the relation between `L` and the physical distance to the singular core.

---

## 8. Formation interpretation

The amplified packet cloud is no longer a single undifferentiated branch.

It splits into

\[
\boxed{
S_{amp}^{packet}
\Longrightarrow
S_{exp-no-go}
\lor
S_{extreme-separation}.
}
\]

The first is empty under the stated capacities.

The second requires a precise asymptotic relation between `L` and `ell`.

This is a much narrower target than merely proving `Theta->infinity`.

---

## 9. Firewall: background/diffuse amplification

Nothing in this exponent optimization controls a mixed norm dominated by a diffuse/background velocity field rather than the counted occupied packets.

Thus

\[
\boxed{
S_{amp}^{background/diffuse}
}

remains routed to the separate weak-`L3`/Campanato/H machinery.

---

## 10. External theorem compatibility

Seregin's 2026 setup assumes

\[
l>\kappa>0,
\]

with `s>1,l>1`, plus additional theorem-specific restrictions such as

\[
s<p(eta),
\qquad
l<q(eta).
\]

The no-go region derived here is an **internal algebraic consequence of the packet capacity assumptions** and must be intersected with those admissible ranges before any external theorem is invoked.

---

## 11. Audit verdict

### PROVED UNDER THE THREE INPUT INEQUALITIES

\[
M_\kappa
\lesssim
\begin{cases}
L^{l-1-2l/s},&l/s\ge1/2,\\
L^{l-1/2-3l/s},&l/s\le1/2.
\end{cases}
\]

### EXCLUDED REGION

For `1<l<2`,

\[
\boxed{
1<s\le\frac{3l}{l-1/2}
}
\]

cannot support packet-dominated amplification with `g(ell)->0`.

### OPEN

- exponent-positive extreme-separation branch;
- weighted pressure;
- diffuse/background amplification;
- sparse/affine ancestry;
- dynamic turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]