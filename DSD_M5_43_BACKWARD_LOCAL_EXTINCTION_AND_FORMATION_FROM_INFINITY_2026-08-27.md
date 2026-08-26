# DSD M5-43 — Backward Local Extinction and Formation from Infinity

Date: 2026-08-27

Status: **DERIVED FROM COMPLETE W1 COMPACTNESS + ANCIENT INVERSE-LERAY REPRESENTATION / THE FIRST-HIT ANCIENT CELL VANISHES LOCALLY BACKWARD IN TIME WHILE RETAINING A NONZERO STATIC `1/r` RESERVOIR AT SPATIAL INFINITY / THIS IS A NECESSARY FORMATION-FROM-INFINITY STRUCTURE, NOT A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

## 1. Ancient representation

M5-41 gives

\[
V_*(z,\sigma)
=(-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{-\sigma}},
-\log(-\sigma)
\right),
\qquad \sigma<0,
\]

where `U^#` is a complete trajectory in the compact recurrent W1 set.

Because the W1 set has a uniform finite-core ceiling and a uniform `1/|Y|` tail envelope, there exists `M_*<infinity` such that

\[
\boxed{
\sup_{\eta\in\mathbb R}
\|U^\#(\eta)\|_{L^\infty(\mathbb R^3)}
\le M_*.
}
\]

---

## 2. Global Type-I ancient bound

The inverse-Leray formula immediately yields

\[
\boxed{
\|V_*(\sigma)\|_\infty
\le
\frac{M_*}{\sqrt{-\sigma}}
\qquad(\sigma<0).
}
\]

Thus the ancient cell has the standard Type-I backward decay rate.

In particular, for every fixed compact set `K subset R^3`,

\[
\boxed{
V_*(\cdot,\sigma)\to0
\quad\text{uniformly on }K
\quad(\sigma\to-\infty).
}
\]

Using the corresponding local derivative bounds on the compact W1 orbit gives the stronger local smooth convergence

\[
V_*(\cdot,\sigma)\to0
\quad\text{in }C^m_{loc}
\]

for each fixed derivative order for which the retained W1 compactness provides uniform bounds.

---

## 3. Exact backward extinction of the threshold excess

For the threshold-one excess

\[
\mathcal G(V)
:=\frac12\int (|V|-1)_+^2dz,
\]

if

\[
-\sigma>M_*^2,
\]

then

\[
\|V_*(\sigma)\|_\infty<1.
\]

Hence

\[
\boxed{
\mathcal G(V_*(\sigma))=0
\qquad
\text{for all sufficiently negative }\sigma.
}
\]

Therefore the nonzero terminal first hit is formed during a finite ancient-time interval; it is not present throughout the whole ancient history.

---

## 4. Simultaneous nonzero spatial-infinity reservoir

M5-42 shows that every selected W1 tail-hull profile becomes a static ancient far field

\[
\boxed{
V_{tail}(z)
=\frac1{|z|}
\Phi\!\left(
\frac z{|z|},\log|z|
\right),
}
\]

independent of `sigma` at leading order.

If the W1 critical residue is nonzero, this tail is nontrivial in the corresponding hull/averaged sense.

Thus the ancient cell has the simultaneous asymptotics

\[
\boxed{
V_*(\cdot,\sigma)\to0
\text{ locally as }\sigma\to-\infty,
}
\]

while

\[
\boxed{
\text{a nonzero static critical `1/r` reservoir persists at spatial infinity.}
}
\]

---

## 5. DSD formation typing

The ancient-cell history therefore has the exact qualitative type

\[
\boxed{
\begin{array}{c}
\text{local backward vacuum / vanishing state}\\
+\\
\text{static critical reservoir at spatial infinity}\\
\Downarrow\\
\text{inward/intermediate-scale transport and pressure--Hodge formation}\\
\Downarrow\\
\text{finite-time first positive high-amplitude excess}.
\end{array}
}
\]

The terminal defect is therefore neither:

- an unexplained boundary creation; nor
- a quantity that was already locally present at arbitrarily early ancient times.

It has a same-trajectory formation ancestry from spatial infinity.

---

## 6. Fixed-ball local-energy consequence

For every fixed `R<infinity`, define

\[
E_R(\sigma)
:=\frac12\int_{B_R}|V_*(z,\sigma)|^2dz.
\]

The global Type-I bound gives

\[
E_R(\sigma)
\le
C_R(-\sigma)^{-1}
\]

for sufficiently negative `sigma`, hence

\[
\boxed{
E_R(\sigma)\to0
\qquad(\sigma\to-\infty).
}
\]

Integrating the local-energy identity from `-infinity` to a later time therefore represents every positive local energy amount as accumulated boundary flux minus local viscous dissipation.

Thus any nontrivial first-hit cell requires a genuinely nonzero inward energy ancestry across finite spheres.

This is a necessary flux statement, not yet a finite-budget contradiction, because the ancient limit possesses an infinite critical reservoir at spatial infinity.

---

## 7. Relation to standard Type-I ancient theory

The backward decay

\[
\|V_*(\sigma)\|_\infty\lesssim(-\sigma)^{-1/2}
\]

is consistent with the standard Type-I ancient-solution framework. It therefore does not by itself improve the known Liouville frontier.

The extra W1-specific content is the coexistence of:

- complete recurrent inverse-Leray ancestry;
- static nonzero `1/r` far-field memory;
- first-hit threshold history;
- and the terminal threshold--Hodge / direction-compression formation constraints.

---

## 8. Updated target

A genuinely new M5 closure must use the interaction between the backward-local-zero state and the static critical reservoir, rather than either property in isolation.

Natural next candidates are:

1. a moving-radius local-energy flux law measuring how the static reservoir feeds the interior;
2. a same-trajectory rigidity theorem excluding a first-hit cell with zero local backward state and nonzero static critical tail;
3. a tail-subtracted formulation with a controllable forcing/residual;
4. or a direct ancient Liouville theorem for this specific static-tail formation class.

No such closure is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
