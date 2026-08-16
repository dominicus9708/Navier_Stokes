# Clean precursor: cubic enstrophy growth forces a long lifespan and a physical dissipation cost

Date: 2026-08-16

Status: **EXACT CLASSICAL H1/ENSTROPHY DIFFERENTIAL INEQUALITY APPLIED TO THE CLEAN MINIMUM-ENSTROPHY CHECKPOINT. IT STRENGTHENS THE SUB-PARABOLIC SMOOTHING BARRIER TO AN `E_m^{-2}` NORMALIZED-TIME BARRIER. GLOBAL REGULARITY NOT PROVED.**

## 1. Global enstrophy source in the H1 form

Let

\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2.
\]

The enstrophy equation is

\[
\frac12E'+\nu P=Q,
\qquad
Q=\int S\Omega\cdot\Omega.
\]

Use Calderon--Zygmund in `L3` and Sobolev interpolation:

\[
\|S\|_3\lesssim\|\Omega\|_3,
\]

\[
\|\Omega\|_3
\le
\|\Omega\|_2^{1/2}\|\Omega\|_6^{1/2}
\lesssim
E^{1/4}P^{1/4}.
\]

Therefore

\[
\boxed{
|Q|
\lesssim
E^{3/4}P^{3/4}.
}
\]

Young's inequality gives

\[
|Q|
\le
\frac\nu2P
+C\nu^{-3}E^3.
\]

Hence

\[
\boxed{
E'
\le
C\nu^{-3}E^3.
}
\]

This is the classical cubic enstrophy-growth inequality behind the `H1` local existence time.

---

## 2. Integrate from the clean minimum to the coherent crossing

Let `s_m` be the minimum-enstrophy checkpoint and `s_c` the coherent crossing. Since `E` is smooth and positive on the relevant nonzero branch,

\[
\frac d{ds}E^{-2}
=-2E^{-3}E'
\ge
-C\nu^{-3}.
\]

Integrating,

\[
E_c^{-2}
\ge
E_m^{-2}
-C\nu^{-3}(s_c-s_m).
\]

Therefore

\[
\boxed{
s_c-s_m
\gtrsim
\nu^3
\left(E_m^{-2}-E_c^{-2}\right).
}
\]

At the coherent crossing `E_c >= c R^3`, whereas `E_m -> 0`, so the terminal term is negligible and

\[
\boxed{
s_c-s_m
\gtrsim
\nu^3E_m^{-2}.}
\]

This is stronger than the previous `c log R` and `c R^2` barriers whenever `E_m` is sufficiently small.

---

## 3. Insert the deep-checkpoint ceiling

The clean minimum obeys

\[
E_m
\le E_-
\lesssim
\frac{R^\beta}{W^{1/2}},
\qquad 0<\beta<4.
\]

Hence

\[
\boxed{
s_c-s_m
\gtrsim
\nu^3\frac{W}{R^{2\beta}}.}
\]

In physical variables, `ds=W dt`, so

\[
\boxed{
t_c-t_m
\gtrsim
\frac{\nu^3}{R^{2\beta}}.}
\]

The right side still tends to zero for fixed `beta>0`, so this alone does not exclude finite-time accumulation.

---

## 4. Integrated enstrophy action

Because `s_m` is the minimum of `E` on `[s_-,s_c]`,

\[
E(s)\ge E_m
\qquad(s_m\le s\le s_c).
\]

Therefore

\[
\int_{s_m}^{s_c}E(s)ds
\ge
E_m(s_c-s_m)
\gtrsim
\nu^3E_m^{-1}.
\]

Using the deep ceiling,

\[
\boxed{
\int_{s_m}^{s_c}E(s)ds
\gtrsim
\nu^3\frac{W^{1/2}}{R^\beta}.}
\]

---

## 5. Convert to physical kinetic-energy dissipation

Under terminal first-hitting normalization,

\[
E_{\rm norm}(s)
=W^{-1/2}E_{\rm phys}(t),
\qquad
 ds=Wdt.
\]

Thus

\[
\int E_{\rm norm}ds
=W^{1/2}
\int E_{\rm phys}dt.
\]

Consequently

\[
\boxed{
\nu\int_{t_m}^{t_c}
\|\omega(t)\|_2^2dt
\gtrsim
\frac{c\nu^4}{R^\beta}.}
\]

Up to the fixed viscosity convention, each such clean-precursor-to-coherent-crossing episode consumes at least an `R^-beta` amount of the physical kinetic-energy dissipation budget.

---

## 6. Comparison with earlier reset costs

Earlier material-flux / Bessel packing led to costs of the form

\[
q^{-1/2}
\]

or, for the canonical reset scale, approximately

\[
R^5/W^{1/2}.
\]

The present clean-enstrophy cost is

\[
\boxed{R^{-\beta},}
\]

which is much larger on late coherent branches for fixed small `beta` because `W^(1/2) >= R^5(log R)^(5/2)`.

However, a super-separated sequence `R_j` may still satisfy

\[
\sum_jR_j^{-\beta}<\infty.
\]

So the estimate is a stronger budget but not yet a nonrepeatability theorem.

---

## 7. Tail-dissipation interpretation

The estimate can be read without summing crossing episodes:

> once a clean precursor has normalized enstrophy `E_m`, reaching a coherent crossing requires at least order `1/E_m` normalized enstrophy action and order `E_m^-2` normalized time.

This is a scale-resolved form of the classical Leray `H1` lifespan barrier.

It shows that an arbitrarily fast late reconstruction cannot be supported merely by stochastic path intermittency or shell relocation; the global enstrophy itself imposes a minimum lifespan and dissipation tail.

---

## 8. Active remaining issue

To obtain a contradiction from infinitely many crossings one still needs one of:

1. a packing theorem that prevents the `R^-beta` physical dissipation costs from being hidden in heavily overlapping nested intervals;
2. a lower bound whose cost does not decay with `R`;
3. or a coupling of the clean-enstrophy lifespan with the stochastic deformation / Malliavin derivative ledger that forces an additional non-summable cost.

Overall status: **CLEAN PRECURSOR LIFESPAN UPGRADED TO `E_m^-2`; PHYSICAL DISSIPATION COST UPGRADED TO `R^-beta`; SUPER-SEPARATED SUMMABILITY REMAINS POSSIBLE.**
