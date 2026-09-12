# DSD M19-152 — Authoritative correction: the tau-nonlinearity homotopy is exactly amplitude-rescaled Navier--Stokes, and nonzero RDSS escapes as 1/tau

Date: 2026-09-12

Status: **AUTHORITATIVE M19 CORRECTION / THE M19-151 HOMOTOPY PARAMETER DOES NOT PRODUCE A GENUINELY NEW DYNAMICAL FAMILY FOR TAU>0 / THE CHANGE OF VARIABLES V=TAU U AND PI=TAU P CONVERTS THE TAU-EQUATION EXACTLY TO THE ORIGINAL SIMILARITY NAVIER--STOKES EQUATION / EVERY NONZERO ORIGINAL RDSS GENERATES U_TAU=V/TAU AND THEREFORE ESCAPES TO INFINITE AMPLITUDE AS TAU->0 / THE HOMOTOPY CANNOT REDUCE NONEXISTENCE TO A KERNEL EVENT WITHOUT AN IMPOSSIBLE UNIFORM AMPLITUDE COMPACTNESS ASSUMPTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The M19-151 homotopy

M19-151 introduced

\[
\partial_sU
+\frac12U
+\frac12(y\cdot\nabla)U
+\tau(U\cdot\nabla)U
=-\nabla P+\nu\Delta U,
\qquad
\nabla\cdot U=0,
\]

with

\[
\tau\in[0,1].
\]

It is true that `tau` is an external parameter of this written equation.
However the family has an exact amplitude-rescaling equivalence for every

\[
\tau>0.
\]

---

## 2. Exact rescaling

Set

\[
\boxed{
V:=\tau U,
\qquad
\Pi:=\tau P.
}
\]

Multiply the tau-equation by `tau`.
Because

\[
\tau^2(U\cdot\nabla)U
=(V\cdot\nabla)V,
\]

we obtain

\[
\boxed{
\partial_sV
+\frac12V
+\frac12(y\cdot\nabla)V
+(V\cdot\nabla)V
=-\nabla\Pi+\nu\Delta V,
\qquad
\nabla\cdot V=0.
}
\]

This is exactly the original similarity Navier--Stokes equation.

Hence, for every `tau>0`, the tau-family is algebraically equivalent to the original equation by amplitude scaling.

---

## 3. Relative-periodicity is preserved

If

\[
U(s+S)=Q_*U(s),
\]

then

\[
V(s+S)
=\tau U(s+S)
=Q_*\tau U(s)
=Q_*V(s).
\]

Thus the intrinsic relative-periodic moduli

\[
S,
\qquad Q_*
\]

are unchanged by the amplitude transformation.

---

## 4. Every nonzero original orbit generates a singular homotopy branch

Let `V` be any nonzero original RDSS/RSS/DSS solution.
Then for every

\[
\tau>0
\]

define

\[
\boxed{
U_\tau:=\frac{V}{\tau},
\qquad
P_\tau:=\frac{\Pi}{\tau}.
}
\]

The pair `(U_tau,P_tau)` solves the tau-equation and has exactly the same period/holonomy.

As

\[
\tau\downarrow0,
\]

we have

\[
\boxed{
\|U_\tau\|=\tau^{-1}\|V\|\to\infty
}
\]

in every homogeneous amplitude norm in which `V` is nonzero.

Therefore the nonzero solution component does not need to meet the trivial `tau=0` state or encounter a multiplier-one fold.
It can escape every bounded compact corridor by simple amplitude blow-up.

---

## 5. Consequence for M19-151

The logical local statement in M19-151 remains true:

- a compact solution branch cannot turn or terminate at a regular fixed point without fixed-point degeneracy.

But the proposed global use fails because the homotopy compactness hypothesis is not merely unproved; the exact scaling shows that a nonzero original orbit naturally violates it as

\[
\tau\to0.
\]

Thus

\[
\boxed{
\mathcal R_{RDSS}^{nonzero}
\not\Rightarrow
\text{a mu=1 event along this tau-homotopy}.
}
\]

Instead the canonical branch is

\[
\boxed{
U_\tau=\tau^{-1}V,
}

which realizes the compactness-loss alternative explicitly.

---

## 6. Why renormalizing the amplitude does not rescue the argument

One might try to impose an amplitude normalization on `U_tau` to prevent the `1/tau` escape.
But after the change

\[
V=\tau U,
\]

such a normalization changes the equation or introduces an additional nonlinear constraint/Lagrange multiplier.
It is no longer the simple homotopy of M19-151.

Therefore an amplitude-normalized continuation would require a genuinely new equation and a separate Fredholm/compactness analysis.
It cannot be smuggled into the present argument.

---

## 7. Correct status of the periodic hard core

The moderate finite-amplitude RSS/RDSS existence problem remains independent.

M19-151 should now be read only as a local continuation bookkeeping note.
It does **not** reduce the original relative-periodic nonexistence problem to kernel rigidity.

The valid live structures remain:

\[
\boxed{
\mathcal T_{kernel}^{nsym},
\qquad
\mathcal T_{elliptic}^{irr},
\qquad
\mathcal T_{RSS/RDSS}^{nonlinear}.
}
\]

---

## 8. Broader audit lesson

The correction is another instance of a permanent DSD firewall:

\[
\boxed{
\text{formal external parameter}
\neq
\text{genuinely independent deformation direction}.
}
\]

An algebraically removable parameter cannot provide topological information about the original solution set unless the rescaling singularity is independently controlled.

---

## 9. Audit verdict

### Certified

1. For every `tau>0`, the M19-151 tau-equation is exactly equivalent to original similarity NS by `V=tau U`.
2. Nonzero original relative-periodic solutions generate `U_tau=V/tau` and escape as `tau->0`.
3. Uniform amplitude compactness along this homotopy is incompatible with that canonical nonzero branch.
4. M19-151 cannot be used as a global nonexistence reduction.

### Still valid from M19-151

- local implicit-function/fold bookkeeping at a fixed bounded point of a genuinely parameterized family.

### Not proved

- nonsymmetry kernel exclusion;
- irrational elliptic exclusion;
- RSS/RDSS nonexistence;
- global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
