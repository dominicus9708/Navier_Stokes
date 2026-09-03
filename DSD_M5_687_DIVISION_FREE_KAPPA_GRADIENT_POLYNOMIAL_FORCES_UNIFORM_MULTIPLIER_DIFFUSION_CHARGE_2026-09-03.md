# DSD M5-687 — A division-free kappa-gradient polynomial forces a uniform multiplier-diffusion charge on the compact CE-H hull

Date: 2026-09-03

Status: **INTERNAL COERCIVE-CHARGE REDUCTION / ON CE-H, `Delta W=kappa W`; DIFFERENTIATING THIS RELATION AND ELIMINATING THE QUOTIENT DEFINES THE GLOBAL POLYNOMIAL `P_i=|W|^2 W·partial_i Delta W-(W·Delta W)(W·partial_i W)=|W|^4 partial_i kappa` ON THE ACTIVE SET / IF THIS POLYNOMIAL VANISHED IDENTICALLY AT ONE NONZERO STATE, `kappa` WOULD BE CONSTANT ON AN OPEN ACTIVE COMPONENT, ANALYTIC CONTINUATION WOULD FORCE `Delta W=cW` GLOBALLY, AND THE L2 SPECTRUM OF THE LAPLACIAN ON R3 WOULD FORCE `W=0`; THEREFORE EVERY NONZERO COMPACT CE-H STATE HAS POSITIVE KAPPA-GRADIENT POLYNOMIAL CHARGE / GLOBAL SMOOTH COMPACTNESS UPGRADES THIS TO A UNIFORM POSITIVE GAP AND, ON A FIXED HIGH-AMPLITUDE CUTOFF, TO A UNIFORM LOWER BOUND FOR `int chi rho^2 |grad kappa|^2` / THIS SUPPLIES A GENUINE POSITIVE PDE CHARGE ABSENT FROM THE PURE HYSTERESIS LEDGER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H multiplier relation

On the CE-H branch,

\[
\boxed{
\Delta W=\kappa W.
}
\]

The scalar multiplier `kappa` is naturally defined on the active set

\[
\rho:=|W|>0.
\]

M5-682 and M5-683 use a high-amplitude cutoff because quotient formulas for `kappa` and its derivatives are not canonical at vorticity zeros.

To obtain a compact-hull functional that remains globally meaningful, remove the quotient algebraically.

---

## 2. Differentiate the eigen-relation

For each spatial index `i`,

\[
\partial_i\Delta W
=(\partial_i\kappa)W
+\kappa\partial_iW.
\]

Dot with `W`:

\[
W\cdot\partial_i\Delta W
=\rho^2\partial_i\kappa
+\kappa W\cdot\partial_iW.
\]

Since

\[
W\cdot\Delta W
=\kappa\rho^2,
\]

multiply the previous identity by `rho^2` and eliminate `kappa`:

\[
\rho^2 W\cdot\partial_i\Delta W
-(W\cdot\Delta W)(W\cdot\partial_iW)
=\rho^4\partial_i\kappa.
\]

Define the division-free vector polynomial

\[
\boxed{
\mathcal P_\kappa
:=
\left(
\rho^2 W\cdot\partial_i\Delta W
-(W\cdot\Delta W)(W\cdot\partial_iW)
\right)_{i=1}^3.
}
\]

Then on `rho>0`,

\[
\boxed{
\mathcal P_\kappa
=\rho^4\nabla\kappa.
}
\]

Unlike `nabla kappa` itself, `mathcal P_kappa` is a polynomial in `W` and its derivatives up to order three and therefore extends smoothly through `W=0`.

---

## 3. Vanishing polynomial would force a constant multiplier on an open set

Assume for contradiction that at one nonzero CE-H state

\[
\boxed{
\mathcal P_\kappa\equiv0.
}
\]

On every active component,

\[
\rho>0
\quad\Longrightarrow\quad
\nabla\kappa=0.
\]

Choose any point with `W!=0`.
By continuity there is an open ball `B` contained in the active set.
On the connected active portion of that ball,

\[
\boxed{
\kappa\equiv c
}
\]

for some real constant `c`.

Hence

\[
\boxed{
\Delta W-cW=0
\qquad\text{on }B.
}
\]

---

## 4. Analytic continuation makes the eigen-relation global

The compact smooth ancient similarity hull used in the current proof line has the same spatial analyticity input already used in M5-677.
Therefore

\[
\Delta W-cW
\]

is a real-analytic vector field.

It vanishes on the nonempty open ball `B`, so unique continuation for real-analytic functions gives

\[
\boxed{
\Delta W=cW
\qquad\text{on all of }\mathbb R^3.
}
\]

This step uses only analyticity of the already smooth CE-H state; it does not infer global constancy of `kappa` by dividing through nodal points.

---

## 5. No nonzero L2 Laplacian eigenfunction exists on R3

Because the similarity hull has finite enstrophy,

\[
W\in L^2(\mathbb R^3).
\]

Fourier transforming the global constant-eigenvalue equation gives

\[
\boxed{
(-|\xi|^2-c)\widehat W(\xi)=0.
}
\]

If `c>0`, the factor never vanishes and `W=0`.

If `c=0`, the Fourier transform is supported only at `xi=0`, a measure-zero set, hence an `L2` Fourier function must vanish.

If `c<0`, the Fourier transform is supported on the sphere

\[
|\xi|=\sqrt{-c},
\]

again a measure-zero subset of `R3`, so an `L2` Fourier function must vanish.

Therefore for every real `c`,

\[
\boxed{
\Delta W=cW,
\quad
W\in L^2(\mathbb R^3)
\Longrightarrow
W\equiv0.
}
\]

This contradicts the marked nonzero CE-H component.

Hence

\[
\boxed{
\mathcal P_\kappa\not\equiv0
}
\]

at every nonzero state of the compact CE-H hull.

---

## 6. Compactness upgrades nonvanishing to a uniform polynomial gap

Define

\[
\boxed{
\mathfrak D_{poly}(Y)
:=
\|\mathcal P_{\kappa,Y}\|_{L^2(\mathbb R^3)}^2.
}
\]

The polynomial uses at most third derivatives of `W`.
M5-507 gives uniform fixed-order Sobolev bounds and M5-508 gives global strong compactness in every finite Sobolev order on the tight branch.
Therefore

\[
Y\mapsto \mathfrak D_{poly}(Y)
\]

is continuous on the compact CE-H hull.

The preceding section proves that it is strictly positive at every marked state.
Compactness therefore gives

\[
\boxed{
\inf_{Y\in\mathcal H_{CEH}}
\mathfrak D_{poly}(Y)
=:d_{poly}>0.
}
\]

This is a statewise uniform gap, not merely a positive time average.

---

## 7. A uniform local kappa-gradient packet

The all-order compact hull also gives global tail tightness and uniform pointwise derivative bounds.
Consequently the positive `L2` gap cannot escape to spatial infinity or collapse into arbitrarily thin unresolved spikes.

By the usual compactness/thickening argument, there exist fixed constants

\[
R_*>0,
\quad
r_*>0,
\quad
p_*>0,
\quad
a_*>0
\]

such that every marked CE-H state contains a ball

\[
B_{r_*}(y_*),
\qquad |y_*|\le R_*,
\]

on which

\[
\boxed{
|\mathcal P_\kappa|\ge p_*,
\qquad
\rho\ge a_*.
}
\]

The amplitude floor follows because `mathcal P_kappa` contains positive powers of `W` and all derivatives of `W` entering it are uniformly bounded.
A nonzero uniform polynomial packet therefore cannot occur with `rho->0`.

---

## 8. Convert the polynomial gap into weighted kappa diffusion

On the active set,

\[
|\mathcal P_\kappa|^2
=\rho^8|\nabla\kappa|^2.
\]

Let

\[
\|W\|_{L^\infty}\le M_0
\]

uniformly on the compact hull.
Then

\[
\rho^8|\nabla\kappa|^2
\le
M_0^6\rho^2|\nabla\kappa|^2.
\]

Choose the M5-683 cutoff `chi(rho)` so that

\[
\chi=1
\qquad
(\rho\ge a_*/2)
\]

and its transition lies strictly below the local packet amplitude.
On the ball extracted above, `chi=1`.
Therefore

\[
\begin{aligned}
\int \chi\rho^2|\nabla\kappa|^2dy
&\ge
\frac1{M_0^6}
\int_{B_{r_*}(y_*)}
|\mathcal P_\kappa|^2dy\\
&\ge
\frac{p_*^2|B_{r_*}|}{M_0^6}.
\end{aligned}
\]

Define

\[
\boxed{
d_\kappa
:=
\frac{p_*^2|B_{r_*}|}{M_0^6}>0.
}
\]

Then every recurrent CE-H state satisfies

\[
\boxed{
\int_{\mathbb R^3}
\chi(\rho)\rho^2|\nabla\kappa|^2dy
\ge d_\kappa>0.
}
\]

Equivalently, integrating the M5-683 level density,

\[
\boxed{
\int_{\mathbb R}
A_{\kappa\kappa}(k,\theta)dk
\ge d_\kappa.
}
\]

---

## 9. Exponentially weighted version

On the retained high-amplitude support, compactness gives

\[
|\kappa|\le K_*.
\]

Hence for any fixed real `beta`,

\[
\int e^{\beta k}A_{\kappa\kappa}(k)dk
\ge
 e^{-|\beta|K_*}d_\kappa.
\]

In particular the weight that will arise naturally from the stationary continuity/constitutive equations is `beta=2`:

\[
\boxed{
D_\kappa^{(2)}
:=
\int e^{2k}A_{\kappa\kappa}(k)dk
\ge
 e^{-2K_*}d_\kappa
=:d_\kappa^{(2)}>0.
}
\]

Thus the pure `kappa`-diffusion channel carries a uniform positive charge on every state of the hard compact CE-H hull.

---

## 10. DSD audit

This result does **not** say that the positive diffusion charge already gives a contradiction.

M5-683 showed that the constitutive current also contains

\[
A_{\kappa\sigma}
\]

with no sign, together with geometric and cutoff-transition remainders.

The valid conclusion is narrower and stronger than the previous heuristic:

\[
\boxed{
\text{the survivor cannot turn off }\nabla\kappa\text{ diffusion completely.}
}
\]

Therefore every recurrent state must continuously pay a fixed positive multiplier-diffusion charge through another term of the exact constitutive/measure ledger.

The next calculation should derive that ledger in a weighting for which the kinematic source term identified in M5-686 cancels exactly.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
