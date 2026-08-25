# DSD W1 Localized Hardy--Curl and Invariant Vorticity Scale Current

Date: 2026-08-26

Status: **GLOBAL HARDY--LERAY BRIDGE LOCALIZED BY CUTOFF+BOGOVSKII / BARKER--PRANGE LOWER BOUND TRANSFERRED TO FIXED LERAY BALLS / EVERY W1 OMEGA-LIMIT STATE FORCED TO HAVE LOGARITHMIC LOCAL FIRST-WEIGHTED-ENSTROPHY GROWTH / PRESSURE-FREE INVARIANT SCALE CURRENT POSITIVE ON A POSITIVE DENSITY OF LOG SCALES / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous pressure-free vorticity-current note left one precise bridge open.

We knew:

1. on the actual prelimit,
   \[
   \int |Y||\Omega|^2\gtrsim s;
   \]
2. on the invariant W1 measure,
   \[
   \mathcal S_\Omega(R)
   =\frac12\partial_{\log R}\bar I(R)\ge0.
   \]

But the first statement used radii growing with late time, so it did not immediately imply a positive invariant scale derivative.

The key improvement is to localize the Hardy--curl bridge.  Barker--Prange Theorem A applies to **every** physical radius in an interval.  Hence every sufficiently large but fixed normalized Leray radius is admissible at sufficiently late time.

This lets the lower bound pass to the omega-limit at fixed `R` before sending `R` to infinity.

---

## 2. Barker--Prange fixed-normalized-radius lower bound

Under the Type-I bound, Barker--Prange Theorem A states that for every late `t` and every physical radius in the admissible interval

\[
R_{phys}
>
2\sqrt{\frac{T^*-t}{S_{BP}(M)}},
\]

one has

\[
\int_{|x|<R_{phys}}|u(x,t)|^3dx
\ge
c_{BP}(M)
\log\left(
\frac{R_{phys}^2}{C_{BP}(M)(T^*-t)}
\right).
\]

Reference:

T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), Theorem A.

Set

\[
R_{phys}=\sqrt{T^*-t}\,R
\]

in standard Leray scaling.  For every fixed

\[
R>R_{BP,*}:=2S_{BP}(M)^{-1/2},
\]

this physical radius is admissible at all sufficiently late times, while the upper radius restriction is automatic because the physical radius tends to zero.

Scale invariance of the cubic integral gives

\[
\boxed{
\int_{|Y|<R}|U(Y,s)|^3dY
\ge
c_3\log R-C_3
}
\]

for every fixed sufficiently large `R` and all sufficiently late `s`.

This is stronger for the present purpose than selecting only one radius `R=K(s)` growing with time.

---

## 3. Localized solenoidal cutoff

Fix a smooth radial cutoff `chi_R` satisfying

\[
\chi_R=1\quad(r\le R),
\qquad
\chi_R=0\quad(r\ge2R),
\]

and

\[
|\nabla\chi_R|\le C/R.
\]

The field `chi_R U` is not divergence free:

\[
\nabla\cdot(\chi_RU)
=\nabla\chi_R\cdot U
=:g_R,
\]

with support in

\[
A_R=\{R<r<2R\}.
\]

Because

\[
\int g_R
=\int\nabla\cdot(\chi_RU)=0,
\]

Bogovskii's operator on the fixed-shape annulus yields a vector field `b_R` supported in `A_R` with

\[
\nabla\cdot b_R=g_R
\]

and

\[
\boxed{
\|\nabla b_R\|_{L^2(A_R)}
\le
C_B\|g_R\|_2
\le
\frac{C_B}{R}\|U\|_{L^2(A_R)}.
}
\]

Define

\[
\boxed{
V_R:=\chi_RU-b_R.
}
\]

Then

\[
\nabla\cdot V_R=0,
\]

`V_R` is compactly supported in `B_{2R}`, and

\[
V_R=U
\qquad(r<R).
\]

---

## 4. Apply the global Hardy--curl inequality to the localized field

The companion Hardy--Leray note proved for compactly supported solenoidal fields

\[
\int r|\operatorname{curl}V|^2
\ge
c_{HL,\omega}
\int\frac{|V|^2}{r},
\]

where

\[
c_{HL,\omega}
=
\frac53-\sqrt{\frac53}>0.
\]

Apply this to `V_R`.

Since `V_R=U` on `B_R`,

\[
\boxed{
\int_{B_R}\frac{|U|^2}{r}
\le
c_{HL,\omega}^{-1}
\int r|\operatorname{curl}V_R|^2.
}
\]

Now

\[
\operatorname{curl}V_R
=
\chi_R\Omega
+\nabla\chi_R\times U
-\operatorname{curl}b_R.
\]

Therefore, using `r<=2R` on the transition annulus,

\[
\begin{aligned}
\int r|\operatorname{curl}V_R|^2
\le{}&
C\int_{B_{2R}}r|\Omega|^2\\
&+CR\int_{A_R}|\nabla\chi_R|^2|U|^2\\
&+CR\int_{A_R}|\nabla b_R|^2.
\end{aligned}
\]

The cutoff and Bogovskii estimates give

\[
CR\int_{A_R}|\nabla\chi_R|^2|U|^2
\le
\frac{C}{R}\int_{A_R}|U|^2,
\]

and

\[
CR\int_{A_R}|\nabla b_R|^2
\le
\frac{C}{R}\int_{A_R}|U|^2.
\]

Thus

\[
\boxed{
\int_{B_R}\frac{|U|^2}{r}
\le
C_H
\int_{B_{2R}}r|\Omega|^2
+
\frac{C_H}{R}
\int_{A_R}|U|^2.
}
\]

This is the localized solenoidal Hardy--curl inequality required by the DSD endpoint.

---

## 5. The localization error is only order one on W1

The W1 Type-I envelope gives on `A_R`

\[
|U|\le A_0/R.
\]

Hence

\[
\int_{A_R}|U|^2
\le
C A_0^2R.
\]

Therefore

\[
\boxed{
\frac1R\int_{A_R}|U|^2
\le C A_0^2.
}
\]

The localization correction does not grow with `R`.

Consequently

\[
\boxed{
\int_{B_{2R}}r|\Omega|^2
\ge
c_H
\int_{B_R}\frac{|U|^2}{r}
-C_HA_0^2.
}
\]

---

## 6. Convert fixed-radius cubic mass to local weighted vorticity

Outside one fixed core radius `R0`, the Type-I envelope also gives

\[
|U|^3
\le
\frac{A_0}{r}|U|^2.
\]

Hence

\[
\int_{R_0<r<R}rac{|U|^2}{r}
\ge
\frac1{A_0}
\int_{R_0<r<R}|U|^3.
\]

The fixed core contributes only `O(1)` cubic mass.  Insert the Barker--Prange fixed-radius lower bound:

\[
\boxed{
\int_{B_R}\frac{|U|^2}{r}
\ge
c_J\log R-C_J.
}
\]

Then the localized Hardy--curl inequality yields

\[
\boxed{
\int_{B_{2R}}r|\Omega|^2dY
\ge
c_\Omega\log R-C_\Omega
}
\]

for every fixed sufficiently large `R` and all sufficiently late prelimit times.

This is the key new local lower bound.

---

## 7. Pass to every omega-limit state

Fix one finite `R`.

The W1 omega-limit construction gives smooth/local strong convergence on `B_{2R}` along every defining late-time sequence.

The weighted vorticity integral

\[
U\mapsto
\int_{B_{2R}}r|\Omega_U|^2
\]

is continuous under that local convergence.

Since the lower bound in Section 6 holds for **all sufficiently late times**, every omega-limit state `U_*` satisfies

\[
\boxed{
\int_{B_{2R}}r|\Omega_{U_*}|^2dY
\ge
c_\Omega\log R-C_\Omega.
}
\]

Since `R` was arbitrary, this holds simultaneously for all sufficiently large finite radii.

Thus the local weighted-vorticity growth is not lost in the omega-limit operation.

This closes the moving-scale transfer gap left in the previous pressure-free current note at the level of logarithmic cumulative growth.

---

## 8. Gaussian first-weighted-enstrophy growth on the minimal set

Recall

\[
I_R(U)
=\frac12
\int r e^{-r^2/R^2}|\Omega_U|^2dY.
\]

On `B_R`, the Gaussian is bounded below by `e^{-1}`. Therefore

\[
I_{2R}(U)
\ge
\frac{e^{-1/4}}2
\int_{B_{2R}}r|\Omega_U|^2dY.
\]

After harmless radius renaming,

\[
\boxed{
I_R(U)
\ge
c_I\log R-C_I
}
\]

for every state in the W1 minimal set and all sufficiently large `R`.

Averaging over any invariant measure gives

\[
\boxed{
\bar I(R)
:=\langle I_R\rangle_\mu
\ge
c_I\log R-C_I.
}
\]

---

## 9. Matching upper logarithmic bound

W1 also has a uniform fixed-annulus `H1` bound.  In physical shell notation this gives

\[
R\int_{A_R}|\nabla U|^2dY
\le C_{H1}
\]

on every sufficiently remote dyadic annulus.

Since

\[
|\Omega|^2\le 2|\nabla U|^2,
\]

one obtains

\[
\int_{A_R}r|\Omega|^2dY
\le C
\]

per geometric shell.

Summing the shells under the Gaussian and using exponential suppression outside `r\gg R` gives

\[
\boxed{
\bar I(R)
\le C_I^+\log R+C_I^+.
}
\]

Thus the invariant weighted-vorticity moment has exact logarithmic order:

\[
\boxed{
\bar I(R)\asymp\log R
}
\]

up to fixed multiplicative/additive constants.

---

## 10. Uniform bound on the logarithmic scale derivative

The exact derivative is

\[
\partial_{\log R}I_R
=
\int
\frac{r^3}{R^2}
e^{-r^2/R^2}|\Omega|^2dY.
\]

Decompose into dyadic shells.

For `r\lesssim R`, the shell bound

\[
\int_{A_r}|\Omega|^2\lesssim r^{-1}
\]

gives shell contribution

\[
\lesssim
\frac{r^3}{R^2}\frac1r
=
\frac{r^2}{R^2}.
\]

The dyadic sum over inner shells is geometric and bounded.

For `r\gg R`, the Gaussian gives exponential decay.

Therefore

\[
\boxed{
0\le
\partial_{\log R}\bar I(R)
\le K_I<\infty
}
\]

uniformly for all sufficiently large `R`.

Equivalently,

\[
\boxed{
0\le\mathcal S_\Omega(R)
\le K_I/2.
}
\]

---

## 11. Positive-density scales with positive pressure-free current

Write

\[
\rho=\log R,
\qquad
f(\rho)=\bar I(e^\rho).
\]

Sections 8--10 give

\[
f(\rho)\ge c_I\rho-C,
\]

and

\[
0\le f'(\rho)\le K_I.
\]

Fix a large interval `[rho0,L]`. Then

\[
\int_{\rho_0}^{L}f'(\rho)d\rho
=f(L)-f(\rho_0)
\ge
c_I L-O(1).
\]

Let

\[
E_L
:=
\{\rho\in[\rho_0,L]:f'(\rho)\ge c_I/2\}.
\]

Using the upper bound `K_I`,

\[
\int f'
\le
\frac{c_I}{2}(L-|E_L|)
+K_I|E_L|+O(1).
\]

Comparison with the lower bound gives

\[
\boxed{
\liminf_{L\to\infty}
\frac{|E_L|}{L}
\ge
\frac{c_I}{2K_I-c_I}
=:\rho_\Omega>0.
}
\]

Since

\[
\mathcal S_\Omega(R)
=\frac12f'(\log R),
\]

we obtain

\[
\boxed{
\mathcal S_\Omega(R)
\ge
\frac{c_I}{4}
}
\]

on a fixed positive lower density of logarithmic scales.

In particular,

\[
\boxed{
\limsup_{R\to\infty}\mathcal S_\Omega(R)
\ge
\frac{c_I}{4}>0.
}
\]

This is the first theorem-level positive invariant endpoint statement in the pressure-free vorticity language.

---

## 12. What remains different from the Bernoulli endpoint

The Bernoulli current has the stronger limit

\[
\boxed{
\mathcal S_B(R)
\to\mathscr R_3/6>0.
}
\]

For the vorticity current we have now proved

\[
\boxed{
\bar I(R)\asymp\log R
}
\]

and positive lower-density scales on which

\[
\boxed{
\mathcal S_\Omega(R)\ge c>0.
}
\]

We have **not** proved that `S_Omega(R)` has a limit or a positive liminf at every sufficiently large scale.

That stronger statement would require additional scale-equicontinuity or asymptotic translation rigidity of the weighted-vorticity shell profile.

This distinction is retained explicitly.

---

## 13. DSD consequence

The final W1 memory now has two genuinely positive invariant currents:

\[
\boxed{
\mathcal S_B(R)\to\mathscr R_3/6>0
}
\]

and

\[
\boxed{
\mathcal S_\Omega(R)>c>0
\quad\text{on a positive density of log scales}.
}
\]

The first is velocity/Bernoulli based.

The second is pressure free and vorticity based.

Therefore the endpoint cannot be dismissed as an artifact of pressure gauge, periodic tail representation, or a particular Gaussian `p=3` test.

A hypothetical W1 singularity must sustain the same critical memory simultaneously in velocity and vorticity descriptions.

The next useful target is no longer prelimit-to-invariant transfer; that cumulative bridge is now closed.  It is a **scale-rigidity theorem** upgrading the positive-density vorticity current to either a positive liminf or a contradiction with the recurrent Bernoulli/core structure.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
