# DSD M17-284 — A nonzero unbounded stationary nodal survivor requires global L2 spatial decompactification

Date: 2026-09-06  
Canonical ID: **M17-284**

Status: **UNBOUNDED-NODAL MASS GATE / AFTER M17-283, THE PAYER-FREE BOUNDED-K RAW CE-H TANGENT HAS TIME-STATIONARY ACTIVE/NODAL MEMBERSHIP. ON ONE UNBOUNDED STATIONARY ACTIVE COMPONENT `D`, THE POSITIVE AMPLITUDE SATISFIES THE AUTONOMOUS DIRICHLET SCHRODINGER-HEAT EQUATION `a_tau=(Delta-q)a`, `q=|grad xi|^2>=0`. IF THE COMPONENT AMPLITUDE WERE UNIFORMLY L2-BOUNDED FOR ALL ANCIENT TIMES, THE NONPOSITIVE SELF-ADJOINT GENERATOR `L=Delta-q` COULD HAVE SPECTRAL MASS ONLY AT THE ZERO EIGENVALUE; OTHERWISE BACKWARD EVOLUTION AMPLIFIES EVERY NEGATIVE SPECTRAL COMPONENT EXPONENTIALLY. BUT A ZERO-MODE IN L2 SATISFIES `int |grad a|^2+int q a^2=0`, SO IT IS CONSTANT WITH `q a=0`; DIRICHLET NODAL BOUNDARY FORCES ZERO, AND ON A WHOLE-SPACE COMPONENT A NONZERO CONSTANT IS NOT L2. THEREFORE EVERY NONZERO UNBOUNDED NODAL SURVIVOR MUST HAVE UNBOUNDED GLOBAL NORMALIZED L2 MASS / SPATIAL DECOMPACTIFICATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Stationary unbounded nodal component

By M17-283, on the bounded-K payer-free CE-H corridor, nodal membership cannot move in finite time.

Let `D` therefore be one time-stationary connected active component of the raw tangent.

On `D`, write

\[
V=a\xi,
\qquad a>0,
\]

with time-independent director `xi`.

The amplitude equation is

\[
\boxed{
\partial_\tau a
=(\Delta-q)a,
\qquad
q(x):=|\nabla\xi(x)|^2\ge0.
}
\]

On a genuine nodal component,

\[
a=0
\]

on the regular nodal boundary in the Dirichlet trace sense.

---

## 2. Self-adjoint generator

Define

\[
\boxed{L:=\Delta-q}
\]

on `L2(D)` with Dirichlet boundary condition when `partial D` is present.

Its quadratic form is

\[
\boxed{
\langle f,Lf\rangle
=-\int_D|\nabla f|^2dx
-\int_Dq|f|^2dx
\le0.
}
\]

Hence the spectrum of `L` lies in

\[
(-\infty,0].
\]

No compactness of the resolvent is assumed; `D` may be unbounded.

---

## 3. Ancient L2-bounded evolution cannot contain negative spectrum

Suppose, for contradiction, that the nonzero amplitude is uniformly ancient `L2` bounded:

\[
\boxed{
\sup_{\tau\le0}\|a(\tau)\|_{L^2(D)}<\infty.
}
\]

For `T>0`, spectral evolution gives

\[
a(0)=e^{TL}a(-T).
\]

Equivalently, on spectral value `lambda<=0`, backward evolution from time `0` to `-T` carries factor

\[
e^{-T\lambda}.
\]

For every `lambda<0` this factor diverges exponentially as `T->infinity`.

Uniform ancient `L2` boundedness therefore forces the spectral measure of `a` to be supported at

\[
\boxed{\lambda=0.}
\]

Thus

\[
\boxed{La=0}
\]

for every time, and the ancient solution is stationary in `L2`.

---

## 4. The L2 zero mode is trivial

If

\[
La=0,
\]

take the `L2` inner product with `a`:

\[
0
=\langle a,La\rangle
=-\int_D|\nabla a|^2dx
-\int_Dq a^2dx.
\]

Both terms are nonnegative after moving the sign, so

\[
\boxed{
\nabla a=0,
\qquad
q a=0
\quad\text{a.e. on }D.
}
\]

Hence `a` is constant on each connected component.

### If `D` has nodal boundary

The Dirichlet trace is zero, so the constant is zero.

### If `D=R3` or has no Dirichlet boundary

A nonzero constant is not in `L2(D)` when the component has infinite volume.

Therefore

\[
\boxed{a\equiv0,}
\]

contradicting the nonzero tangent normalization.

---

## 5. Correct unbounded-nodal conclusion

Hence a nonzero unbounded stationary nodal component cannot remain globally `L2` bounded through the ancient interval.

Therefore

\[
\boxed{
G_{unbounded\ stationary\ nodal\ domain}
\Longrightarrow
G_{global\ normalized\ L2\ spatial\ decompactification}
\lor
G_{coefficient/domain\ failure}.
}
\]

This is stronger than merely labeling the nodal domain unbounded.
The survivor must carry increasingly large normalized mass at increasing spatial radius.

---

## 6. Relation to fixed-K compactness

M17-261 excludes normalized mass decompactification on every **fixed** rescaled ball without paying normalized palinstrophy.

M17-284 is compatible with that theorem.
The only remaining possibility is a genuinely nonuniform limit in the order of radii:

\[
\forall K<\infty:
\quad
\int_{B_K}|V|^2<\infty,
\]

but

\[
\boxed{
\int_D|V|^2=\infty
}
\]

or the corresponding pre-limit global normalized mass diverges as the observation radius tends to infinity.

Thus the escape is to **spatial infinity**, not to a fixed local coherent mean.

---

## 7. DSD audit

- The argument does not use compact resolvent or a principal eigenfunction on the unbounded domain.
- Uniform global ancient `L2` boundedness is explicit and is the hypothesis being ruled out.
- Fixed-ball local `L2` compactness is not silently promoted to global `L2` compactness.
- Whole-space nonzero constants are excluded only because they are not global `L2`.
- The result is a spatial-decompactification gate, not yet a contradiction for infinite-mass ancient tangents.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
