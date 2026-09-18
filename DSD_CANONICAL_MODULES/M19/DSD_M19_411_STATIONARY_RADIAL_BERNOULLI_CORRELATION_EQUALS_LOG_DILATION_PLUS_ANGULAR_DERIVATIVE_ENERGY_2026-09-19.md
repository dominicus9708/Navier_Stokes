# M19-411 — Stationary radial Bernoulli correlation equals log-dilation plus angular derivative energy

Date: 2026-09-19

Status: **NEW EXACT STATIONARY IDENTITY / COMBINING THE TERMINAL ENERGY-FLUX FORMULA WITH M19-408 CLOSES AN OLD OPEN SIGN ISSUE FROM M5-258. FOR EVERY BOUNDED RECURRENT STATIONARY CRITICAL TAIL (VISCOSITY-NORMALIZED), THE INVARIANT RADIAL BERNOULLI CORRELATION SATISFIES \`B_r = D_q + D_S >= 0\`, WHERE \`D_q=<int|partial_q A|^2>\` AND \`D_S=<int|grad_S A|^2>\`. THUS THE ARBITRARY-AMPLITUDE STATIONARY RADIAL BERNOULLI CORRELATION IS NEVER NEGATIVE. ON THE NONTRIVIAL SMOOTH ZERO-FORCE BRANCH M19-407 GIVES \`D_q>0\`, SO \`B_r>0\` STRICTLY. THIS SUPERSEDES THE M5-258/M5-259 OPEN QUESTION ABOUT WHETHER POSITIVE RADIAL BERNOULLI CORRELATION PERSISTS BEYOND THE LANDAU FAMILY. IT DOES, ON THE BOUNDED RECURRENT STATIONARY CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal head pressure and energy flux

Let

\[
u=r^{-1}A(q,\omega),
\qquad
p=r^{-2}P(q,\omega),
\qquad
q=\log r.
\]

Define

\[
E_A(q,\omega)
:=
\frac12|A|^2
\]

and the head-pressure coefficient

\[
\boxed{
h
:=
P+E_A.
}
\]

The physical stationary energy flux is

\[
J
=
\left(
\frac12|u|^2+p
\right)u
-
\nabla\left(
\frac12|u|^2
\right)
\]

in viscosity-normalized units.

Its scale-normalized radial sphere flux is

\[
\Phi_E(q)
=
r\int_{S_r}J\cdot n\,dS.
\]

---

## 2. Exact coefficient formula for Phi_E

Since

\[
\frac12|u|^2
=
r^{-2}E_A,
\]

one has

\[
\partial_r
\left(
r^{-2}E_A
\right)
=
r^{-3}
(\partial_q-2)E_A.
\]

Therefore

\[
\boxed{
\Phi_E(q)
=
\int_{S^2}
\left[
hA_r
-
(\partial_q-2)E_A
\right]d\omega.
}
\]

Define the radial Bernoulli correlation

\[
\boxed{
\mathcal B_r
:=
\left\langle
\int_{S^2}
hA_r\,d\omega
\right\rangle_q.
}
\]

Taking the invariant \(q\)-mean and using

\[
\left\langle
\partial_q
\int_{S^2}E_A\,d\omega
\right\rangle_q
=
0,
\]

gives

\[
\boxed{
\langle\Phi_E\rangle
=
\mathcal B_r
+
2
\left\langle
\int_{S^2}E_A\,d\omega
\right\rangle_q.
}
\]

Since

\[
2E_A=|A|^2,
\]

write

\[
E_0
:=
\left\langle
\int_{S^2}|A|^2d\omega
\right\rangle_q.
\]

Then

\[
\boxed{
\langle\Phi_E\rangle
=
\mathcal B_r+E_0.
}
\]

---

## 3. Stationary energy payer identity

M5-575 gives on the stationary branch \(C=0\),

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle.
}
\]

M19-408 gives the exact dissipation decomposition

\[
\boxed{
\langle\mathcal D_A\rangle
=
D_q+E_0+D_S,
}
\]

where

\[
D_q
:=
\left\langle
\int_{S^2}
|\partial_qA|^2d\omega
\right\rangle_q,
\]

and

\[
D_S
:=
\left\langle
\int_{S^2}
|\nabla_{S^2}A|^2d\omega
\right\rangle_q.
\]

---

## 4. Exact Bernoulli identity

Equating Sections 2 and 3,

\[
\mathcal B_r+E_0
=
D_q+E_0+D_S.
\]

The base \(L^2\) term cancels exactly.

Therefore

\[
\boxed{
\mathcal B_r
=
D_q+D_S.
}
\]

Hence

\[
\boxed{
\mathcal B_r\ge0.
}
\]

This is exact on the bounded recurrent stationary class.

---

## 5. Equality case

If

\[
\mathcal B_r=0,
\]

then

\[
D_q=0,
\qquad
D_S=0.
\]

Thus

\[
\partial_qA=0,
\qquad
\nabla_{S^2}A=0
\]

on the invariant support.

Hence \(A\) is constant in \(q\) and \(\omega\).

A nonzero constant vector coefficient

\[
u=r^{-1}A_0
\]

does not satisfy the global divergence-free stationary critical structure on the sphere in the retained class unless additional singular/angular defects are introduced.

On the smooth retained branch, the equality case collapses to the trivial state.

Therefore every nontrivial smooth bounded recurrent stationary tail has

\[
\boxed{
\mathcal B_r>0
}
\]

unless an angular/sphere singular branch is present.

---

## 6. Zero-force branch

M19-407 proves that on every nontrivial smooth zero-force recurrent stationary component,

\[
D_q>0.
\]

Therefore immediately

\[
\boxed{
\mathcal B_r
=
D_q+D_S
>0.
}
\]

Thus the surviving zero-force tail simultaneously has

\[
\boxed{
\mathcal F_A=0
}
\]

for the vector momentum/stress flux and

\[
\boxed{
\mathcal B_r>0
}
\]

for the scalar radial Bernoulli correlation.

This separation is exact.

---

## 7. Close the M5-258/M5-259 sign OPEN

M5-258 derived

\[
2\nu\overline H_0+\mathcal B_r
=
\nu\mathcal Z_T
\]

and left the sign of \(\mathcal B_r\) open at arbitrary critical amplitude.

M5-259 verified

\[
\mathcal B_r>0
\]

explicitly on the Landau family and perturbatively near it.

M19-411 closes the sign question on the full bounded recurrent stationary class:

\[
\boxed{
\mathcal B_r\ge0
}
\]

universally, with strict positivity on every nontrivial smooth zero-force recurrent component.

Thus the old question

\[
\text{“does Landau-compatible positive radial Bernoulli correlation survive at arbitrary recurrent critical amplitude?”}
\]

has answer

\[
\boxed{\text{YES}}
\]

under the present bounded recurrent stationary hypotheses.

---

## 8. Head-pressure mean consequence

Combining

\[
2\nu\overline H_0+\mathcal B_r
=
\nu\mathcal Z_T
\]

with the general-viscosity form

\[
\mathcal B_r
=
\nu(D_q+D_S),
\]

gives

\[
\boxed{
2\overline H_0
=
\mathcal Z_T
-
D_q
-
D_S.
}
\]

Hence the invariant mean head pressure is no longer independent of the terminal vorticity and log/angular derivative energies.

Its sign remains undetermined in general, but its exact value is constrained by these three nonnegative quantities.

---

## 9. Relation to positive energy flux

M19-409 gives

\[
\Phi_E(q)>0
\qquad
\forall q
\]

on every nontrivial bounded recurrent stationary hard tail.

M19-411 shows that after invariant averaging, the part of that energy flux beyond the unavoidable base \(L^2\) contribution is exactly

\[
\boxed{
D_q+D_S.
}
\]

Thus genuine log-radius or angular complexity is paid precisely by positive radial Bernoulli transport.

This is not merely a qualitative payer statement.

---

## 10. Updated stationary target

The radial Bernoulli sign is no longer an OPEN.

The remaining zero-force problem is sharper:

\[
\boxed{
\mathcal F_A=0,
\qquad
\mathcal B_r=D_q+D_S>0,
\qquad
\Phi_E(q)>0.
}
\]

The next theorem must determine whether a smooth recurrent stationary critical tail can have **zero vector momentum force but strictly positive scalar Bernoulli/energy transport** at every scale.

This is now a stress-energy compatibility problem rather than a Bernoulli-sign problem.

---

\[
\boxed{\text{M19-411 COMPLETE; STATIONARY RADIAL BERNOULLI CORRELATION IS EXACTLY }D_q+D_S\ge0.}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
