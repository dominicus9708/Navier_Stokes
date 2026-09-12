# DSD M19-137 — Antipodally odd critical data automatically kill the first l=3 pressure solvability moment by parity

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE FIRST NONAUTOMATIC PRESSURE-RESONANCE CANDIDATE OF M19-136 IS AUDITED AGAINST ANTIPODAL PARITY / ODD LEADING CRITICAL DATA FORCE THE FIRST VELOCITY CORRECTION TO REMAIN ODD, THE ORDER-1 CROSS STRESS IS EVEN, AND ITS DOUBLE DIVERGENCE HAS NO l=3 COMPONENT / THE FIRST CUBIC PRESSURE MOMENT IS THEREFORE NOT A UNIVERSAL CLOSURE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Odd critical datum

Assume the leading critical coefficient satisfies

\[
\boxed{
A(q,-\omega)=-A(q,\omega).
}
\]

Equivalently, for each fixed q the physical leading field

\[
U_0(x)=r^{-1}A(q,\omega)
\]

is antipodally odd:

\[
\boxed{U_0(-x)=-U_0(x).}
\]

This class includes many odd spherical-harmonic/toroidal sectors and is preserved by rigid rotations.

---

## 2. Parity of the order-r^-3 residual

For an odd vector field `U_0`:

- `Delta U_0` is odd;
- `nabla U_0` is even;
- `(U_0 dot nabla)U_0` is odd.

The leading pressure source is quadratic in first derivatives,

\[
-\Delta P_0
=\partial_iU_{0j}\partial_jU_{0i},
\]

so it is even.
With the decaying/recurrent pressure normalization, `P_0` is even and therefore

\[
\nabla P_0
\]

is odd.

Hence the complete first forcing at order `r^-3` is odd.

Because the first similarity-correction operator is invertible and parity preserving,

\[
\boxed{B_1(q,-\omega)=-B_1(q,\omega).}
\]

---

## 3. Parity of the n=1 pressure stress

M19-136 identifies

\[
T^{(1)}
=
B_0\otimes B_1+B_1\otimes B_0.
\]

Both `B_0=A` and `B_1` are odd.
Therefore

\[
\boxed{T^{(1)}(-\omega)=T^{(1)}(\omega).}
\]

So the cross stress is even.

Two spatial derivatives preserve parity overall, hence

\[
\boxed{F_1(-\omega)=F_1(\omega)}
\]

for the order-1 pressure source

\[
F_1=\partial_i\partial_jT^{(1)}_{ij}.
\]

---

## 4. The l=3 resonant projection vanishes

Every degree-three spherical harmonic is antipodally odd:

\[
Y_3(-\omega)=-Y_3(\omega).
\]

Therefore

\[
\int_{S^2}
Y_3(\omega)
\,\mathbb M_qF_1(\omega)
\,d\omega
=0.
\]

Thus

\[
\boxed{
\Pi_3\mathbb M_qF_1=0
}
\]

automatically on the antipodally odd critical class.

Equivalently,

\[
\boxed{
\mathfrak M_3[A]=0
\qquad
\text{for antipodally odd }A.
}
\]

---

## 5. Consequence

The M19-136 `n=1,l=3` pressure resonance is a genuine **generic mixed-parity candidate**, but it is not a universal obstruction.

In particular it cannot by itself eliminate:

- antipodally odd toroidal critical tails;
- RSS spirals generated from an odd seed, since rigid rotation preserves antipodal parity;
- RDSS twisted histories whose critical coefficient remains in the odd parity sector.

Hence

\[
\boxed{
\text{first pressure solvability moment}
\neq
\text{universal critical-tail closure}.
}
\]

---

## 6. Next question

There are now two pressure-hierarchy directions:

1. evaluate `M_3[A]` on genuinely mixed-parity low-mode tails, where it may impose a nontrivial cubic algebraic condition;
2. move to the next resonance in the odd-parity class, where the relevant harmonic degree and parity may allow the first nonzero obstruction.

For the odd class, the resonance ladder alternates in a way that must be audited before claiming any higher-order closure.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
