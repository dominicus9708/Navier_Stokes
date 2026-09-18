# M19-424 — BRC does not force Bernoulli sorting; an exact parity witness transfers the full Hardy excess into residual slope

Date: 2026-09-19  
Canonical ID: **M19-424**  
Status: **BRC COVARIANCE AUDIT / QUANTITATIVE BIDIRECTIONAL RADIAL CROSSING ALONE DOES NOT FORCE NONZERO BERNOULLI COVARIANCE / AN EXPLICIT DIVERGENCE-FREE RADIAL-POLoidal l1 LEADING TRACE HAS BRC BUT EXACTLY ZERO BERNOULLI SORTING BY PARITY / ITS ENTIRE HARDY EXCESS IS PAID BY A·C / WHEN BERNOULLI SORTING IS POSITIVE IT PRODUCES A SYNDETIC OUTWARD-INWARD BERNOULLI CONTRAST AND FORCES FINITE-DEPTH ENERGY-CURRENT REVERSAL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-423

The exact Hardy-excess identity is

\[
\boxed{
\mathcal H_A
=
\langle\Gamma_B\rangle
+
\mathscr E'(0),
}
\]

where

\[
\mathcal H_A
=
\left\langle
\|A_q\|_2^2
+
\|\nabla_{S^2}A\|_2^2
\right\rangle
>0,
\]

and

\[
\boxed{
\Gamma_B(q)
=
\int_{S^2}
(B-\bar B)A_r,d\omega,
\qquad
B=\frac12|A|^2+P.
}
\]

M19-422 gives a BRC event whenever the RP branch is selected:

\[
\int A_r^+
=
\int A_r^-
>0.
\]

The question is whether this sign-separated radial crossing already forces

\[
\Gamma_B\neq0.
\]

It does not.

## 2. Explicit radial/poloidal l1 leading trace

Fix a nonzero vector \(a\in\mathbb R^3\) and define

\[
\boxed{
A_a(\omega)
:=
\frac12
\left[
a+(a\cdot\omega)\omega
\right].
}
\]

This is independent of \(q\).

Its radial component is

\[
\boxed{
(A_a)_r
=
A_a\cdot\omega
=
a\cdot\omega.
}
\]

Its tangential component is

\[
(A_a)_T
=
\frac12
\left[
a-(a\cdot\omega)\omega
\right]
=
\frac12\nabla_{S^2}(a\cdot\omega).
\]

Since

\[
\Delta_{S^2}(a\cdot\omega)
=
-2(a\cdot\omega),
\]

we obtain

\[
(A_a)_r
+
\operatorname{div}_{S^2}(A_a)_T
=
(a\cdot\omega)
-
(a\cdot\omega)
=
0.
\]

Thus

\[
\boxed{
v_a(x)=r^{-1}A_a(\omega)
}
\]

is a smooth divergence-free critical degree-minus-one field on the punctured space.

This is the same radial/poloidal l1 velocity appearing in the historical M5-206 reconstruction.

## 3. It has exact bidirectional radial crossing

Because

\[
(A_a)_r=a\cdot\omega,
\]

we have

\[
\int_{S^2}(A_a)_r,d\omega=0.
\]

But for \(a\neq0\),

\[
(A_a)_r
\]

has nontrivial positive and negative hemispherical sectors.

Hence

\[
\boxed{
\int(A_a)_r^+
=
\int(A_a)_r^-
>0.
}
\]

So this profile is an exact BRC witness at the leading critical level.

## 4. Antipodal parity kills the Bernoulli covariance

Under \(\omega\mapsto-\omega\),

\[
A_a(-\omega)
=
A_a(\omega).
\]

Thus the leading velocity coefficient is antipodally even.

Its kinetic-energy density

\[
E_a
=
\frac12|A_a|^2
\]

is therefore even.

The canonical pressure is determined by the quadratic pressure Poisson equation.

For an even velocity field, the first spatial derivatives are odd, so the quadratic pressure source is even. With the canonical recurrent/decaying pressure normalization,

\[
\boxed{
P_a(-\omega)=P_a(\omega).
}
\]

Therefore

\[
B_a
=
E_a+P_a
\]

is even.

But

\[
(A_a)_r(-\omega)
=
-(A_a)_r(\omega).
\]

Hence

\[
\boxed{
\Gamma_B[A_a]
=
\int_{S^2}B_a(A_a)_r,d\omega
=
0.
}
\]

Thus

\[
\boxed{
BRC
\not\Rightarrow
\Gamma_B\neq0.
}
\]

This is an exact parity firewall, not merely a dimensional argument.

## 5. Its Hardy excess is strictly positive

The field is q-independent, so

\[
\partial_qA_a=0.
\]

Decompose componentwise into its constant and \(l=2\) pieces:

\[
A_a
=
\frac23a
+
\frac12
\left[
(a\cdot\omega)\omega
-
\frac13a
\right].
\]

Only the second term contributes to the spherical derivative.

A direct spherical calculation gives

\[
\boxed{
\int_{S^2}|A_a|^2d\omega
=
2\pi|a|^2,
}
\]

and

\[
\boxed{
\int_{S^2}
|\nabla_{S^2}A_a|^2d\omega
=
\frac{4\pi}{3}|a|^2.
}
\]

Therefore

\[
\boxed{
\mathcal H_{A_a}
=
\frac{4\pi}{3}|a|^2
>0.
}
\]

## 6. The full Hardy excess is transferred to the residual slope

Apply M19-423:

\[
\mathcal H_{A_a}
=
\Gamma_B[A_a]
+
\int_{S^2}A_a\cdot C_a,d\omega.
\]

Since

\[
\Gamma_B[A_a]=0,
\]

we obtain

\[
\boxed{
\int_{S^2}A_a\cdot C_a,d\omega
=
\frac{4\pi}{3}|a|^2
>0.
}
\]

Equivalently,

\[
\boxed{
\mathscr E'(0)
=
\frac{4\pi}{3}|a|^2
>0.
}
\]

Thus this BRC witness routes **all** genuine angular variation into the parabolic residual-slope branch.

It is not claimed to be an exact full ancient Navier--Stokes solution.

Its purpose is to prove that BRC geometry plus incompressibility and canonical pressure parity do not force Bernoulli sorting.

## 7. Bernoulli-sorting branch when it is active

Now suppose instead that on one nontrivial hard component

\[
\boxed{
\langle\Gamma_B\rangle
\ge
\gamma_B>0.
}
\]

Because \(\Gamma_B\) is a continuous bounded observable on the compact minimal hull, there exists

\[
0<\delta_B<\gamma_B
\]

such that the open set

\[
U_B
=
\{T:\Gamma_B(T)>\delta_B\}
\]

is nonempty.

Minimality gives syndetic returns to \(U_B\) on every hull orbit.

Thus positive Bernoulli sorting produces a fixed recurrent event, not merely a positive abstract mean.

## 8. Exact outward/inward Bernoulli contrast

At a state with \(\Gamma_B>0\), define

\[
S(q)
:=
\int A_r^+d\omega
=
\int A_r^-d\omega
>0.
\]

Define the flux-weighted Bernoulli means

\[
\beta_+
:=
\frac1S
\int B A_r^+d\omega,
\]

\[
\beta_-
:=
\frac1S
\int B A_r^-d\omega.
\]

Then exactly

\[
\boxed{
\Gamma_B
=
S(\beta_+-\beta_-).
}
\]

Compactness gives a uniform upper bound

\[
S\le S_{max}<\infty.
\]

Hence on every selected sorting event,

\[
\boxed{
\beta_+-\beta_-
\ge
\frac{\delta_B}{S_{max}}
=:
\Delta_B>0.
}
\]

Therefore the Bernoulli-sorting branch has a direct formed interpretation:

\[
\boxed{
\text{outward radial crossing carries a uniformly larger flux-weighted Bernoulli level than inward crossing.}
}
\]

## 9. Positive Bernoulli sorting forces positive terminal energy current

M19-423 gives

\[
\langle\Phi_E\rangle
=
\langle\Gamma_B\rangle
+
\left\langle
\int|A|^2d\omega
\right\rangle.
\]

Therefore

\[
\boxed{
\langle\Gamma_B\rangle>0
\Longrightarrow
\mathscr J(0)=\langle\Phi_E\rangle>0.
}
\]

M19-304 proves for every nontrivial retained wedge

\[
\boxed{
\int_0^\infty\mathscr J(z)dz
=
-\mathscr E(0)
-
\int_0^\infty\mathscr D(z)dz
<0.
}
\]

Consequently a Bernoulli-sorting branch must reverse the sign of the whole-sphere radial energy current at finite depth:

\[
\boxed{
\exists z_->0:
\mathscr J(z_-)<0.
}
\]

By continuity there is at least one finite-depth zero crossing of \(\mathscr J\).

M19-308 further shows that order-one compensation cannot be hidden arbitrarily deep because

\[
\mathscr J(z)=O(z^{-2}).
\]

Thus the reversal is a bounded/intermediate-depth phenomenon on the component.

## 10. This is still not a contradiction

The sign pattern

\[
\mathscr J(0)>0,
\qquad
\exists z_->0:mathscr J(z_-)<0
\]

is exactly compatible with the full wedge transport audited in M19-269 and M19-304--308.

It is a genuine current-reversal structure, but not a monotone recurrent obstruction.

Therefore

\[
\boxed{
\text{Bernoulli sorting}
\Longrightarrow
\text{terminal outward sorting + finite-depth inward reversal}
\not\Longrightarrow
\text{global contradiction}.
}
\]

## 11. Correct status of the BRC route

The BRC branch is now fully reclassified.

It does not create an independent fourth terminal resource.

Instead,

\[
\boxed{
BRC
\longrightarrow
\begin{cases}
\mathcal B_{sort}:&
\text{syndetic outward/inward Bernoulli separation + finite-depth current reversal},
\\
\mathcal B_{res}:&
\text{positive terminal residual slope, already routed through M19-269}.
\end{cases}
}
\]

The explicit \(A_a\) parity witness proves that the second option is genuinely necessary.

## 12. Updated frontier

The M19-422 three-way formed frontier

\[
R3
\lor
BRC
\lor
T_{\ge2}
\]

now becomes

\[
\boxed{
R3^{syndetic,critical}
\lor
\mathcal B_{sort}^{syndetic/reversal}
\lor
\mathcal B_{res}^{finite-depth}
\lor
T_{\ge2}^{syndetic}.
}
\]

But \(\mathcal B_{res}\) is already the M19-269 finite-depth transport branch.

Hence the genuinely new radial object is only

\[
\boxed{
\mathcal B_{sort}^{syndetic/reversal}.
}
\]

The next calculation should split

\[
\Gamma_B
=
\frac12\int|A|^2A_r
+
\int P A_r
\]

into kinetic-energy sorting and pressure sorting.

That will determine whether the surviving radial Bernoulli separation is carried locally by amplitude geometry or nonlocally by pressure.

\[
\boxed{\text{M19-424 COMPLETE; BRC ALONE DOES NOT FORCE BERNOULLI SORTING, AND THE RADIAL ROUTE IS REDUCED TO BERNOULLI SEPARATION OR THE ALREADY-KNOWN RESIDUAL-SLOPE BRANCH.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
