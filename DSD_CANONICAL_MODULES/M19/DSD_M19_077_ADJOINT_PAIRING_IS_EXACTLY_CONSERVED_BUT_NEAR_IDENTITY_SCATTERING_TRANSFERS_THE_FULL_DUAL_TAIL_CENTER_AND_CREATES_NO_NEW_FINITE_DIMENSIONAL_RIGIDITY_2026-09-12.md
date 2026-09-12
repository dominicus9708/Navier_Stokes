# DSD M19-077 — Adjoint pairing is exactly conserved but near-identity scattering transfers the full dual tail center and creates no new finite-dimensional rigidity

Date: 2026-09-12

Status: **ADJOINT AUDIT / THE ROTATION-TRANSVERSE LINEAR COCYCLE HAS THE STANDARD CONSERVED PRIMAL-ADJOINT PAIRING, BUT THIS IS A DUALITY IDENTITY RATHER THAN A NEW SIGNED INVARIANT / BECAUSE THE OUTWARD SCATTERING DERIVATIVE IS I+O(R_SPEC^-2), ITS ADJOINT IS ALSO NEAR IDENTITY AND THEREFORE TRANSPORTS THE INFINITE-DIMENSIONAL DUAL OF THE FORMAL TAIL CENTER BACK TO THE FINITE SPECTATOR BOUNDARY / A FINITE-DIMENSIONAL CENTER CONCLUSION WOULD REQUIRE AN INDEPENDENT FREDHOLM/OBSERVABILITY OR EXPONENTIAL-DICHOTOMY THEOREM, WHICH IS PRECISELY THE CURRENTLY MISSING INTERIOR INPUT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rotation-transverse cocycle

After M19-076, remove the exact rotational orbit directions using the radial-A2 orthogonality gauge.

Write the resulting linearized equation schematically as

\[
\boxed{
\partial_\theta W=L(\theta)W,
}
\]

on the moving rotation-transverse weighted space.

The exact time tangent

\[
Z_t=\partial_\theta U
\]

remains visible.

The live question is whether another bounded zero-exponent solution \(W\) exists.

---

## 2. Weighted adjoint cocycle

Let \(L(\theta)^\dagger\) denote the adjoint in the radial weighted inner product

\[
\langle F,G\rangle_w
:=
\int_{\mathbb R^3}F\cdot G\,w(y)\,dy.
\]

Define the adjoint trajectory by

\[
\boxed{
\partial_\theta\Psi
=-L(\theta)^\dagger\Psi.
}
\]

Then for every sufficiently regular primal-adjoint pair,

\[
\begin{aligned}
\frac{d}{d\theta}\langle W,\Psi\rangle_w
&=
\langle L(\theta)W,\Psi\rangle_w
-\langle W,L(\theta)^\dagger\Psi\rangle_w\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{
\langle W(\theta),\Psi(\theta)\rangle_w
=\text{constant}.
}
\]

This is exact but purely dual: it is available for every nonautonomous linear equation once an adjoint solution is chosen.

---

## 3. Why this is not yet a new invariant of the nonlinear flow

The adjoint field \(\Psi\) depends on the full background trajectory and on terminal/initial dual data.

Thus the scalar pairing is not an independently prescribed conserved functional of \(U\) alone.

It does not have a sign, and it does not by itself reduce the number of center directions.

To use it for dimension reduction one would need an independent theorem such as:

\[
\boxed{
\dim E^{c,*}_{rot\text{-}transverse}=1
}
\]

or a Fredholm index relation identifying the annihilator of the stable/unstable bundles.

That statement is equivalent in difficulty to controlling the primal center and cannot be assumed.

---

## 4. Linearized scattering map

M19-069 gives, at a sufficiently remote spectator boundary \(R_{spec}\),

\[
D\mathscr S_{R_{spec}}
=I+K_{R_{spec}},
\qquad
\|K_{R_{spec}}\|\lesssim R_{spec}^{-2}.
\]

For \(R_{spec}\) large enough,

\[
\|K_{R_{spec}}\|<1.
\]

Hence the derivative is locally invertible by Neumann series,

\[
\boxed{
(D\mathscr S_{R_{spec}})^{-1}
=I+O(R_{spec}^{-2}).
}
\]

Taking adjoints gives

\[
\boxed{
D\mathscr S_{R_{spec}}^*
=I+O(R_{spec}^{-2}),
}
\]

and this adjoint map is also locally invertible.

---

## 5. Formal tail center and its dual

M19-068 found the leading formal tail center

\[
\delta U_0=r^{-1}B(q,\omega),
\]

subject to the leading divergence constraint.

This is infinite-dimensional because, for example,

\[
B(q,\omega)=c(q)a\times\omega
\]

is allowed for arbitrary bounded smooth \(c(q)\) at the leading formal level.

Let \(\mathcal C_{tail}\) denote this formal center space.

Its continuous dual \(\mathcal C_{tail}^*\) is likewise infinite-dimensional in every natural local/scattering topology used here.

Because \(D\mathscr S^*\) is near identity and invertible,

\[
\boxed{
D\mathscr S^*:\mathcal C_{tail}^*
\longrightarrow
\text{spectator-boundary dual observables}
}
\]

cannot collapse the dual center to finite dimension.

Therefore outward scattering is no more rigid in the adjoint direction than in the primal direction.

---

## 6. Boundary observable interpretation

A tail dual functional \(\Lambda\in\mathcal C_{tail}^*\) induces, through the adjoint scattering map, a spectator-boundary functional

\[
\boxed{
\Lambda_{spec}
:=(D\mathscr S_{R_{spec}})^*\Lambda.
}
\]

Since the map is invertible near identity, distinct tail functionals remain distinct boundary functionals.

Thus the finite spectator boundary remembers the same infinite-dimensional family of leading tail observables unless the **interior recurrent dynamics** imposes additional restrictions.

This is the dual form of the M19-069 conclusion.

---

## 7. A finite-dimensional center conclusion needs an independent range theorem

Suppose one wants to prove that only the time tangent survives after rotation quotient.

A dual route would require a statement of the form

\[
\boxed{
\operatorname{Ran}D\mathscr R_{int}
\cap\mathcal C_{tail}
=\operatorname{span}\{\partial_qA\}
}
\]

where \(\mathscr R_{int}\) is the interior-to-spectator-boundary realization map.

Equivalently, one needs enough adjoint functionals annihilating every forbidden tail center direction while annihilating no genuine time tangent.

No such observability/range theorem has yet been certified.

The adjoint identity does not manufacture it automatically.

---

## 8. Exponential dichotomy circularity firewall

For a finite-dimensional nonautonomous system, a spectral/exponential dichotomy can often identify center dimension by the Fredholm index of the evolution operator.

Here that route would require proving in advance that the rotation-transverse cocycle has an exponential dichotomy away from a finite-dimensional center.

But the existence of an additional zero Lyapunov/Sacker--Sell direction is exactly what is open.

Therefore one must not write

\[
\text{compact recurrent cocycle}
\Rightarrow
\text{finite-dimensional center}
\]

without an independent compactness/smoothing property for the relevant full-space evolution operator.

The formal tail center and M19-069 near-identity scattering show why such a property is nontrivial.

---

## 9. Certified conclusion

The adjoint calculation gives a useful negative result:

\[
\boxed{
\text{primal-adjoint conservation}
+\text{near-identity scattering}
\not\Rightarrow
\text{center-dimension reduction}.
}
\]

More sharply,

\[
\boxed{
\text{any center reduction must occur in the interior realization map, not in outward scattering or formal duality.}
}
\]

---

## 10. Refined missing theorem

The live theorem can be written as an interior range/observability statement:

\[
\boxed{
\mathcal T_{real}:
\operatorname{Ran}(D\mathscr R_{int})
\cap\mathcal C_{tail}
\subset
\operatorname{span}\{\partial_qA\}
+T_A(SO(3)\cdot A).
}
\]

After the symmetry-safe rotation quotient, this becomes

\[
\boxed{
\operatorname{Ran}(D\mathscr R_{int})
\cap\mathcal C_{tail}^{rot\perp}
\subset
\operatorname{span}\{\partial_qA\}.
}
\]

M19-077 does not prove this theorem. It identifies it as the exact location where a genuinely new PDE input is required.

---

## 11. Next calculation

The next natural possibility is to ask whether the interior realization map is compact or smoothing from a fixed finite core to the spectator boundary over a positive similarity-time interval.

Parabolic smoothing is strong in ordinary local Sobolev scales, but the q-translation tail corresponds to boundary history over arbitrarily old similarity times.

M19-078 will distinguish:

1. finite-time local parabolic compactness;
2. global-in-history compactness of the recurrent boundary realization map;
3. whether backward/history translation destroys the compactness needed for a finite-dimensional center conclusion.
