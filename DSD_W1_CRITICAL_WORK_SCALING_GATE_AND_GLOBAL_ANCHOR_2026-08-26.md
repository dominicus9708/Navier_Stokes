# DSD W1 Critical-Work Scaling Gate and Global Anchor

Date: 2026-08-26

Status: **NAIVE SUBQUADRATIC CRITICAL-WORK ESTIMATE REJECTED BY SCALING / ANY USEFUL IMPROVEMENT MUST CONTAIN A GENUINE GLOBAL OR INTERFACE SCALE-BREAKING ANCHOR / THIS RECONNECTS THE LAMB-CASCADE ENDPOINT TO THE FINITE-ENERGY PARENT AND CORE-TRACE INTERFACE / GLOBAL REGULARITY UNPROVED.**

## 1. The standard endpoint estimate

For the physical solution define

\[
D(t):=\|\nabla u(t)\|_2^2.
\]

The critical `p=3` pressure/Lamb work has the estimate

\[
|\Pi_3|
\lesssim
\|P\|_3
\|u\cdot\nabla|u|\|_{3/2}.
\]

Calderon--Zygmund and Sobolev give

\[
\|P\|_3
\lesssim\|u\|_6^2
\lesssim D,
\]

and

\[
\|u\cdot\nabla|u|\|_{3/2}
\le
\|u\|_6\|\nabla u\|_2
\lesssim D.
\]

Hence

\[
\boxed{
|\Pi_3(t)|\lesssim D(t)^2.
}
\]

This estimate is exactly critical.

---

## 2. Why the square is the dangerous exponent

On a W1 Type-I corridor,

\[
D(t)
=(T_*-t)^{-1/2}Z(s)
\]

with normalized `Z(s)` uniformly bounded above and recurrently bounded below.

Therefore

\[
D(t)^2
\sim
(T_*-t)^{-1}
\]

at the scale level, and

\[
\int^t D(\tau)^2d\tau
\]

has exactly logarithmic divergence.

This matches the previously derived positive W1 critical work.

Thus the ordinary endpoint estimate is sharp at the level of self-similar scaling and cannot close the survivor.

---

## 3. Scaling audit of a naive power improvement

Under Navier--Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

we have

\[
D_\lambda=\lambda D
\]

and

\[
\Pi_{3,\lambda}=\lambda^2\Pi_3.
\]

Therefore a bare inequality

\[
|\Pi_3|
\lesssim D^{2-\varepsilon}
\]

cannot be scale invariant for any positive `epsilon`.

So the hoped-for subquadratic gain cannot arise from a purely local homogeneous estimate using `D` alone.

---

## 4. What a scale-consistent gain would require

The total kinetic energy

\[
E(t):=\|u(t)\|_2^2
\]

scales as

\[
E_\lambda=\lambda^{-1}E.
\]

Hence the formal expression

\[
E^{-\varepsilon}D^{2-\varepsilon}
\]

has the same scaling as `Pi_3`:

\[
\lambda^{\varepsilon}\lambda^{2-\varepsilon}
=\lambda^2.
\]

This does **not** establish such an inequality. It only shows what kind of scale-breaking input is dimensionally capable of producing a power gain in `D`.

The negative power of global energy also warns that this cannot be obtained by routine Gagliardo--Nirenberg interpolation.

---

## 5. Local core energy restores exact criticality

A self-similar core of physical radius

\[
r(t)\sim\sqrt{T_*-t}
\]

has the natural scalings

\[
E_{core}(t)\sim r(t),
\qquad
D_{core}(t)\sim r(t)^{-1}.
\]

Hence

\[
E_{core}^{-\varepsilon}
D_{core}^{2-\varepsilon}
\sim
r^{-\varepsilon}r^{-2+\varepsilon}
=r^{-2}
\sim
(T_*-t)^{-1}.
\]

So **using only the shrinking core energy does not gain anything**. The self-similar core exactly restores the critical exponent.

This is another form of the half-power barrier.

---

## 6. Genuine gain must come from the parent/interface

To beat the logarithmic endpoint, a scale-breaking quantity must remain anchored at a scale not shrinking with the singular core.

Candidates are therefore not purely local critical norms but quantities of the form

\[
\boxed{
\text{finite-energy parent information},
\quad
\text{core--tail mismatch},
\quad
\text{trace/interface defect},
\quad
\text{nonlocal conserved or monotone anchor}.
}
\]

This is exactly the structure already exposed independently by the periodic W1 quotient calculation:

- the far `1/r` trace can support its own nonresonant asymptotic corrections;
- the quotient is finite-energy/finite-`L3`;
- the unresolved issue is how that critical trace is attached to the finite-energy parent/core.

The Lamb-cascade route therefore converges to the same frontier.

---

## 7. DSD conclusion

The proof search should no longer target

\[
\boxed{\text{a better local estimate for }\Pi_3}
\]

without an additional scale.

Such a route is blocked by exact scaling.

The correct DSD target is

\[
\boxed{
\text{projection--cascade recurrence}
+
\text{a nonshrinking parent/interface anchor}.
}
\]

A successful inequality must measure the incompatibility between the recurrent critical core/tail mechanism and the fact that it descends from one finite-energy physical solution.

This is a stricter and more useful target than a generic `subquadratic D` estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
