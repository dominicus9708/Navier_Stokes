# DSD M19-267 — Positive cubic tail density forces a quantitative terminal dissipation floor and a flux-or-residual payer dichotomy

Date: 2026-09-15  
Canonical ID: **M19-267**  
Status: **ACTIVE CALCULATION / M5-571 + M5-575 REIMPORT / QUANTITATIVE TERMINAL PAYER DICHOTOMY / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-266 / M5-571

On a nontrivial ergodic hard terminal component, the log-radius scattering datum satisfies

\[
\boxed{
c_3
:=
\left\langle
\int_{S^2}|A(q,\omega)|^3\,d\omega
\right\rangle_q
>0.
}
\]

The retained compact regular tail class also supplies a uniform amplitude ceiling

\[
\boxed{|A(q,\omega)|\le M_A<\infty.}
\]

Define

\[
c_2
:=
\left\langle
\int_{S^2}|A|^2\,d\omega
\right\rangle_q.
\]

Since

\[
|A|^3\le M_A|A|^2,
\]

we have the quantitative lower bound

\[
\boxed{
c_2\ge \frac{c_3}{M_A}>0.
}
\]

Thus the hard tail carries a strictly positive square-amplitude density, not merely a cubic one.

---

## 2. Terminal critical dissipation

M5-575 defines

\[
\mathcal D_A(q)
:=
\int_{S^2}
\left[
|(\partial_q-1)A|^2
+|\nabla_{S^2}A|^2
\right]d\omega.
\]

Expand the radial term:

\[
|(\partial_q-1)A|^2
=
|\partial_qA|^2+|A|^2-\partial_q|A|^2.
\]

The invariant log-radius mean kills the total derivative:

\[
\left\langle
\int_{S^2}\partial_q|A|^2d\omega
\right\rangle_q=0.
\]

Therefore

\[
\boxed{
\left\langle\mathcal D_A\right\rangle
=
\left\langle
\int_{S^2}
\left(
|\partial_qA|^2
+|\nabla_{S^2}A|^2
+|A|^2
\right)d\omega
\right\rangle_q.
}
\]

In particular,

\[
\boxed{
\left\langle\mathcal D_A\right\rangle
\ge c_2
\ge \frac{c_3}{M_A}
=:d_*>0.
}
\]

This is stronger than the earlier qualitative statement \(\langle\mathcal D_A\rangle\ge0\).

---

## 3. Exact terminal payer identity

M5-572 identifies the first parabolic terminal coefficient

\[
C=\mathcal R_{stat}[A,P],
\]

and M5-575 gives

\[
\boxed{
\left\langle\mathcal D_A\right\rangle
=
\left\langle\Phi_E\right\rangle
+
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle.
}
\]

Write

\[
\phi
:=
\langle\Phi_E\rangle,
\qquad
\chi
:=
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle.
\]

Then

\[
\phi+\chi
\ge d_*>0.
\]

Hence at least one payer satisfies

\[
\boxed{
\phi\ge\frac{d_*}{2}
}
\]

or

\[
\boxed{
\chi\ge\frac{d_*}{2}.
}
\]

Using the explicit lower bound for \(d_*\),

\[
\boxed{
\left\langle\Phi_E\right\rangle
\ge
\frac{c_3}{2M_A}
}
\]

or

\[
\boxed{
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle
\ge
\frac{c_3}{2M_A}.
}
\]

Thus every nontrivial ergodic hard tail pays a fixed quantitative amount through at least one of the two exact channels.

---

## 4. Flux-payer branch

Define

\[
\boxed{
\mathcal B_{flux}:
\quad
\langle\Phi_E\rangle
\ge
\frac{c_3}{2M_A}.
}
\]

This is a genuine scale-invariant radial energy-current lower bound.

On the stationary branch \(C=0\), M5-578 gives the stronger pointwise statement

\[
\Phi_E(q)>0
\quad\forall q,
\]

and

\[
\langle\Phi_E\rangle
=
\langle\mathcal D_A\rangle
\ge d_*.
\]

Thus the stationary hard tail is automatically in the flux-payer branch.

---

## 5. Residual-correlation payer branch

Define

\[
\boxed{
\mathcal B_{res}:
\quad
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle
\ge
\frac{c_3}{2M_A}.
}
\]

M5-583 identifies this correlation with the terminal wedge-energy derivative:

\[
\boxed{
\mathscr E'(0)
=
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle.
}
\]

Hence on \(\mathcal B_{res}\),

\[
\boxed{
\mathscr E'(0)
\ge
\frac{c_3}{2M_A}>0.
}
\]

The mean scale-normalized wedge energy therefore initially rises as one moves from the singular terminal boundary \(z=0\) into the positive-depth ancient wedge.

This is not itself a contradiction, but it is a signed boundary condition absent from the earlier qualitative formulation.

---

## 6. Quantitative residual-density consequence

Let

\[
c_C
:=
\left\langle
\int_{S^2}|C|^2d\omega
\right\rangle.
\]

By Cauchy--Schwarz,

\[
\chi^2
\le
c_2c_C.
\]

Also

\[
c_2
\le
4\pi M_A^2.
\]

Therefore on \(\mathcal B_{res}\),

\[
\boxed{
c_C
\ge
\frac{\chi^2}{c_2}
\ge
\frac{d_*^2}{16\pi M_A^2}.
}
\]

Since \(d_*\ge c_3/M_A\),

\[
\boxed{
c_C
\ge
\frac{c_3^2}{16\pi M_A^4}>0.
}
\]

Thus a residual-paying hard component carries a quantitative positive mean-square first-terminal-jet density, strengthening the qualitative M5-580 statement \(c_C>0\).

---

## 7. What is closed and what is not

The following escape is now removed:

\[
\boxed{
\text{nontrivial hard tail with arbitrarily small mean terminal payment}
}
\]

under a fixed compact-component amplitude ceiling \(M_A\).

Instead the terminal branch is quantitatively split as

\[
\boxed{
\text{hard tail}
\Longrightarrow
\mathcal B_{flux}
\lor
\mathcal B_{res}.
}
\]

However neither branch is yet impossible:

- M5-579 shows that the flux branch is compatible with Type-I core energy scaling;
- the residual branch is a positive terminal wedge-energy derivative and a positive residual-density branch, but the full wedge can absorb this through finite-depth transport.

Therefore this is a quantitative reduction, not a global regularity proof.

---

## 8. Immediate next target

Reimport the full M5-582--598 wedge/finite-depth chain and determine whether either quantitative payer can be promoted from an unsigned recurrent payment into one of:

1. a bounded signed observable with one-way drift;
2. a terminal local-energy defect excluded by original-variable inheritance;
3. a finite-depth compactness/Liouville obstruction;
4. a nonreuse/counting contradiction with a genuinely nonsummable physical weight.

If none occurs, the tail-balance route must be merged back into the explicit signed/rigidity frontier rather than treated as an independent closure mechanism.

Global 3D Navier--Stokes regularity remains unproved.
