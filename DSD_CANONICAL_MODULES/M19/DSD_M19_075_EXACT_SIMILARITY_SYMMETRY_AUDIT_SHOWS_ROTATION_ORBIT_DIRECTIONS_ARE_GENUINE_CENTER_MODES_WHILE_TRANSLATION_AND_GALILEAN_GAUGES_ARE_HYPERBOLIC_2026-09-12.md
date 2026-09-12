# DSD M19-075 — Exact similarity-symmetry audit shows rotation-orbit directions are genuine center modes while translation and Galilean gauges are hyperbolic

Date: 2026-09-12

Status: **CENTER-SYMMETRY CLASSIFICATION / THE TIME TANGENT IS NOT THE ONLY GENERIC EXACT CENTER DIRECTION: BROKEN ROTATIONAL SYMMETRY PRODUCES UP TO THREE ADDITIONAL NEUTRAL MODES / PHYSICAL SPACE TRANSLATION HAS SIMILARITY EXPONENT +1/2, GALILEAN BOOST HAS EXPONENT -1/2, AND PHYSICAL NS SCALING IS EXACTLY SIMILARITY-TIME TRANSLATION / ANY SIMPLE-CENTER THEOREM MUST THEREFORE QUOTIENT THE COMPACT ROTATION ORBIT BUT MUST NOT QUOTIENT THE LOG-TRANSLATION FACTOR IT IS TRYING TO EXCLUDE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity equation

Work with backward similarity variables around a fixed candidate singular point and time,

\[
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
=-\nabla P+\nu\Delta U,
\qquad \nabla\cdot U=0.
\]

Let \(\mathcal L_{U(\theta)}\) denote the exact linearization along a complete recurrent trajectory \(U(\theta)\).

Because the equation is autonomous in \(\theta\),

\[
Z_t:=\partial_\theta U
\]

solves

\[
\partial_\theta Z_t=\mathcal L_{U(\theta)}Z_t.
\]

This is the familiar orbit tangent.

---

## 2. Rotations generate additional exact neutral cocycle solutions

For \(Q\in SO(3)\), define

\[
U^Q(y,\theta):=Q\,U(Q^Ty,\theta),
\qquad
P^Q(y,\theta):=P(Q^Ty,\theta).
\]

This is again an exact similarity Navier--Stokes solution.

Take

\[
Q_\varepsilon=e^{\varepsilon A},
\qquad A^T=-A.
\]

Differentiating at \(\varepsilon=0\) gives

\[
\boxed{
Z_A
=A U-(Ay)\cdot\nabla U.
}
\]

Since \(U^{Q_\varepsilon}\) is an exact one-parameter solution family,

\[
\boxed{
\partial_\theta Z_A
=\mathcal L_{U(\theta)}Z_A.
}
\]

No exponential prefactor appears.

Hence each broken rotational generator gives a genuine zero/center cocycle direction.

If the isotropy subgroup of the trajectory is \(G_U\subset SO(3)\), then the rotational center dimension is

\[
\boxed{
\dim SO(3)-\dim G_U.
}
\]

Thus it ranges from \(0\) for fully rotationally invariant states to \(3\) for a generic state with discrete isotropy.

Therefore

\[
\boxed{
\text{generic exact symmetry center}
\supset
\operatorname{span}\{\partial_\theta U\}
\oplus T_U(SO(3)\cdot U).
}
\]

---

## 3. Physical NS scaling is not a new center mode

The physical Navier--Stokes scaling is

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).
\]

In similarity variables centered at the same singular spacetime point,

\[
\boxed{
U_\lambda(y,\theta)
=U(y,\theta-2\log\lambda).
}
\]

Therefore differentiation at \(\lambda=1\) gives only a multiple of

\[
\partial_\theta U.
\]

So physical scaling does not add another independent center direction: it is precisely similarity-time translation.

---

## 4. Physical spatial translations are unstable gauge modes, not center

Translate the physical solution by a constant vector \(a\):

\[
u_a(x,t)=u(x-a,t).
\]

With \(-t=e^{-\theta}\), the similarity representation is

\[
\boxed{
U_a(y,\theta)
=U(y-ae^{\theta/2},\theta).
}
\]

Hence the infinitesimal translation mode is

\[
\boxed{
Z_a^{\rm trans}
=-e^{\theta/2}(a\cdot\nabla)U.
}
\]

The explicit factor \(e^{\theta/2}\) shows similarity exponent

\[
\boxed{+\frac12}.
\]

Thus motion of the blow-up center is an unstable modulation direction, not a zero center direction.

This is why fixing the candidate singular center is not the same operation as quotienting a neutral factor.

---

## 5. Galilean boosts are stable gauge modes

For constant velocity \(c\), physical Galilean invariance gives

\[
u_c(x,t)=u(x-ct,t)+c.
\]

Since \(t=-e^{-\theta}\), one finds

\[
\boxed{
U_c(y,\theta)
=U(y+ce^{-\theta/2},\theta)+ce^{-\theta/2}.
}
\]

Therefore

\[
\boxed{
Z_c^{\rm Gal}
=e^{-\theta/2}\left[(c\cdot\nabla)U+c\right].
}
\]

Its explicit exponent is

\[
\boxed{-\frac12}.
\]

Hence the Galilean gauge is stable, not central.

---

## 6. Discrete symmetries do not add infinitesimal center dimensions

Reflections and other disconnected Euclidean symmetries may map one trajectory to another but have no infinitesimal generator inside the identity component.

They can create finite multiplicity of equivalent representatives, but they do not enlarge the linear center bundle.

---

## 7. Corrected center target

The previous naive target

\[
E^c=\operatorname{span}\{\partial_\theta U\}
\]

is false for a generic nonsymmetric recurrent trajectory because rotational orbit tangents are also exact neutral solutions.

The symmetry-safe target must instead be

\[
\boxed{
E^c_{\rm sym}(U)
:=
\operatorname{span}\{\partial_\theta U\}
\oplus T_U(SO(3)\cdot U).
}
\]

The live analytic theorem becomes

\[
\boxed{
E^c(U)=E^c_{\rm sym}(U)
}
\]

for the recurrent interior cocycle, after the unstable center-position gauge has been fixed.

Depending on isotropy, the allowed exact symmetry center dimension is therefore between \(1\) and \(4\).

---

## 8. Why quotienting rotations is legitimate but quotienting time is dangerous

The scattering datum transforms under rotations by

\[
A^Q(q,\omega)
=Q A(q,Q^T\omega),
\]

which changes only the angular frame.

Thus taking a quotient by the compact group \(SO(3)\) removes representational angular degeneracy without erasing the q-translation dynamics.

By contrast similarity-time translation obeys

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

Quotienting the full time orbit would identify precisely the q-translations whose nontrivial aperiodic realization is the current target.

Hence

\[
\boxed{
\text{rotation quotient: symmetry-safe},
\qquad
\text{time-orbit quotient: factor-destructive}.
}
\]

---

## 9. Consequence for exterior-square tests

M19-071 attempted to use two-volume contraction to show that there is at most one center exponent.

M19-075 shows that such a theorem cannot be correct before rotational degeneracy is removed.

For a generic state, up to four exact symmetry-generated zero directions may exist.

Therefore future volume-contraction tests must begin only after projection away from

\[
E^c_{\rm sym}.
\]

The relevant quantity is not the second Lyapunov exponent of the full cocycle, but the top Lyapunov exponent on the symmetry-transverse bundle.

---

## 10. New theorem frontier

The center/factor problem now has the sharper form

\[
\boxed{
\mathcal T_{transverse\ center}:
\text{after fixing center position and quotienting rotations, prove that no bounded zero-exponent cocycle direction exists beyond the time tangent.}
}
\]

Equivalently, before quotient notation,

\[
\boxed{
E^c(U)
=
\operatorname{span}\{\partial_\theta U\}
\oplus T_U(SO(3)\cdot U).
}
\]

If this fails, the extra center direction is the precise candidate through which an aperiodic scattering factor can be interior-realized.

---

## 11. Firewalls

\[
\boxed{\text{rotation tangent}\neq\text{aperiodic q-translation factor}},
\]

\[
\boxed{\text{physical translation gauge}\neq\text{center mode}},
\]

\[
\boxed{\text{Galilean gauge}\neq\text{center mode}},
\]

\[
\boxed{\text{physical NS scaling}\equiv\text{similarity-time translation}},
\]

\[
\boxed{\text{formal tail center}\neq\text{interior-realizable center}}.
\]

Global 3D Navier--Stokes regularity remains unproved.

---

## 12. Next calculation

The next step is to construct a symmetry-transverse modulation condition and audit whether the existing polynomial-A2 weighted coercivity can control the projected cocycle without reintroducing uncontrollable modulation terms.

That is M19-076.
