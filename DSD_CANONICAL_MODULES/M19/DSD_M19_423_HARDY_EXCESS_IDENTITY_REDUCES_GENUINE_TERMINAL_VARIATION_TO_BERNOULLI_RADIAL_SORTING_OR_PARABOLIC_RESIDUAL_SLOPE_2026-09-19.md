# M19-423 — Hardy-excess identity reduces genuine terminal variation to Bernoulli radial sorting or parabolic residual slope

Date: 2026-09-19  
Canonical ID: **M19-423**  
Status: **EXACT TERMINAL ENERGY REFINEMENT / THE STATIC 1/r HARDY BASELINE IS REMOVED / ALL GENUINE LOG-ANGULAR VARIATION IS PAID EXACTLY BY RADIAL BERNOULLI COVARIANCE AND/OR THE FIRST PARABOLIC RESIDUAL CORRELATION / HARD NONTRIVIALITY MAKES THIS EXCESS STRICTLY POSITIVE ON EVERY NONTRIVIAL ERGODIC TERMINAL COMPONENT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Terminal critical field

Let

\[
v=r^{-1}A(q,\omega),
\qquad
p=r^{-2}P(q,\omega),
\qquad
q=\log r.
\]

Define the angular kinetic-energy density

\[
E(q,\omega)
:=
\frac12|A(q,\omega)|^2,
\]

and the critical Bernoulli weight

\[
\boxed{
B(q,\omega)
:=
E(q,\omega)+P(q,\omega).
}
\]

Let

\[
K(q)
:=
\int_{S^2}E(q,\omega)d\omega
=
\frac12\int_{S^2}|A|^2d\omega.
\]

The leading divergence-free constraint implies

\[
\boxed{
\int_{S^2}A_r(q,\omega)d\omega=0
}
\]

on the bounded recurrent hard tail.

## 2. Exact radial energy-flux decomposition

M5-575 defines

\[
J_A
=
\left(\frac12|v|^2+p\right)v
-
\nabla\left(\frac12|v|^2\right)
\]

and the scale-normalized sphere flux

\[
\Phi_E(q)
=
r\int_{S_r}J_A\cdot n,dS.
\]

Since

\[
\frac12|v|^2
=
r^{-2}E
\]

and

\[
\partial_r(r^{-2}E)
=
r^{-3}(\partial_q-2)E,
\]

the radial flux is exactly

\[
\boxed{
\Phi_E(q)
=
\int_{S^2}
\left[
B A_r
-
(\partial_q-2)E
\right]d\omega.
}
\]

Therefore

\[
\boxed{
\Phi_E(q)
=
\Gamma_B(q)
-
K'(q)
+
2K(q),
}
\]

where

\[
\boxed{
\Gamma_B(q)
:=
\int_{S^2}B(q,\omega)A_r(q,\omega)d\omega.
}
\]

## 3. The radial term is exactly a Bernoulli covariance

Define the spherical mean

\[
\overline B(q)
:=
\frac1{4\pi}
\int_{S^2}B(q,\omega)d\omega.
\]

Because

\[
\int_{S^2}A_r,d\omega=0,
\]

we have

\[
\boxed{
\Gamma_B(q)
=
\int_{S^2}
\bigl(B-\overline B\bigr)A_r,d\omega.
}
\]

Thus the advective-plus-pressure part of the normalized radial energy current is not controlled by net mass flux.

It is exactly a **signed Bernoulli/radial-velocity covariance**.

In particular,

\[
\boxed{
\int A_r=0
\not\Rightarrow
\Gamma_B=0.
}
\]

## 4. Ergodic mean of the flux

On the compact recurrent log-radius factor,

\[
\langle K'\rangle_q=0.
\]

Hence

\[
\boxed{
\langle\Phi_E\rangle
=
\langle\Gamma_B\rangle
+
2\langle K\rangle.
}
\]

Since

\[
2K
=
\int_{S^2}|A|^2d\omega,
\]

the second term is precisely the static critical \(1/r\) Hardy baseline.

## 5. Remove the Hardy baseline from the terminal payer identity

M5-575 gives

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\left\langle
\int_{S^2}A\cdot C,d\omega
\right\rangle,
}
\]

with

\[
\mathcal D_A
=
\int_{S^2}
\left[
|(\partial_q-1)A|^2
+
|\nabla_{S^2}A|^2
\right]d\omega.
\]

Expanding the radial derivative and averaging,

\[
\boxed{
\langle\mathcal D_A\rangle
=
\left\langle
\|\partial_qA\|_2^2
+
\|\nabla_{S^2}A\|_2^2
+
\|A\|_2^2
\right\rangle.
}
\]

Insert Section 4 and cancel the common amplitude term

\[
\langle\|A\|_2^2\rangle
=
2\langle K\rangle.
\]

This gives the exact Hardy-excess identity

\[
\boxed{
\mathcal H_A
:=
\left\langle
\|\partial_qA\|_2^2
+
\|\nabla_{S^2}A\|_2^2
\right\rangle
=
\langle\Gamma_B\rangle
+
\left\langle
\int_{S^2}A\cdot C,d\omega
\right\rangle.
}
\]

Equivalently, using M5-583,

\[
\boxed{
\mathcal H_A
=
\langle\Gamma_B\rangle
+
\mathscr E'(0).
}
\]

This is stronger structurally than the total payer identity because the passive \(1/r\) amplitude baseline has been removed.

## 6. The Hardy excess is strictly positive on every nontrivial recurrent hard component

Suppose

\[
\mathcal H_A=0.
\]

The integrand is nonnegative, so smoothness and recurrence imply

\[
\partial_qA=0,
\qquad
\nabla_{S^2}A=0
\]

throughout the component.

Thus \(A\) is one constant Cartesian vector \(a\).

But

\[
v(x)=\frac a{|x|}
\]

has

\[
\nabla\cdot v
=
-\frac{a\cdot\omega}{r^2}.
\]

Incompressibility therefore forces

\[
a=0.
\]

This contradicts the retained nontrivial hard density

\[
c_3
=
\left\langle
\int_{S^2}|A|^3d\omega
\right\rangle
>0.
\]

Hence

\[
\boxed{
\mathcal H_A>0
}
\]

on every nontrivial ergodic hard terminal component.

## 7. Quantitative two-payer fork for genuine variation

Fix one such component and write

\[
h_A:=\mathcal H_A>0.
\]

Then

\[
\langle\Gamma_B\rangle
+
\mathscr E'(0)
=
h_A.
\]

Therefore at least one of

\[
\boxed{
\langle\Gamma_B\rangle
\ge
\frac{h_A}{2}
}
\]

or

\[
\boxed{
\mathscr E'(0)
=
\left\langle
\int A\cdot C
\right\rangle
\ge
\frac{h_A}{2}
}
\]

must hold.

Thus all genuine log/angular variation in the terminal hard tail is paid by one of only two signed mechanisms:

1. **Bernoulli radial sorting**
   \[
   \Gamma_B
   =
   \int(B-\bar B)A_r;
   \]

2. **parabolic residual slope**
   \[
   \mathscr E'(0)
   =
   \langle A\cdot C\rangle.
   \]

## 8. Relation to the M19-422 BRC branch

M19-422 reduces the radial/poloidal branch to quantitative bidirectional radial crossing:

\[
\int A_r^+
=
\int A_r^-
>0
\]

on syndetic selected events.

The present identity identifies the only terminal energy quantity that can distinguish those two sign sectors:

\[
\boxed{
\Gamma_B
=
\int B A_r.
}
\]

Thus BRC by itself is only a formed crossing geometry.

Its signed energetic content is exactly the difference in Bernoulli weight carried by the outward and inward sectors.

No third radial energy payer exists at the terminal level.

## 9. Residual-slope branch is not new

If

\[
\mathscr E'(0)
\ge
h_A/2>0,
\]

the branch is precisely the residual-payer geometry audited in M19-268--269.

It forces

- an interior wedge-energy maximum;
- a positive finite-depth dissipation floor;
- a positive derivative of the weighted radial current at that depth;

but no global monotone contradiction because the full wedge supplies compensating transport.

Therefore

\[
\boxed{
\mathscr E'(0)>0
\text{ is a typed finite-depth transport branch, not a new closure.}
}
\]

## 10. Updated role of BRC

The BRC branch can no longer be treated as an independent mass-flux root.

After the exact energy reduction, it can contribute new information only through

\[
\boxed{
\mathcal B_{sort}:
\langle\Gamma_B\rangle>0.
}
\]

If the Bernoulli covariance is not positive enough, the missing Hardy excess is automatically transferred into the already-known residual-slope branch.

Thus

\[
\boxed{
BRC
\Longrightarrow
\mathcal B_{sort}
\quad\lor\quad
\mathcal B_{residual-slope},
}
\]

at the invariant energy-ledger level, with the second branch already classified by M19-269.

## 11. Next target

The only potentially new part of the BRC route is therefore Bernoulli sorting.

The next calculation should resolve

\[
\Gamma_B
=
\int(B-\bar B)A_r
\]

into the positive and negative radial-crossing sectors and determine whether a fixed positive mean covariance implies a recurrent lower bound on the Bernoulli contrast between outward and inward flow.

If it does, the resulting object is a signed **radial Bernoulli-separation channel**.

That channel must then be compared with

- the pressure Poisson equation;
- the exact inward wedge-current theorem M19-304;
- and the higher-toroidal / \(l=3\) alternatives of M19-421--422.

\[
\boxed{\text{M19-423 COMPLETE; GENUINE TERMINAL VARIATION HAS ONLY BERNOULLI-SORTING OR RESIDUAL-SLOPE PAYMENT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
