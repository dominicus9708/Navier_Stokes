# DSD M17-083 — A conformal vertical high angular jet has an exact material multiplier and signed transfer recurrence

Date: 2026-09-04
Canonical ID: **M17-083**

Status: **INTERNAL VERTICAL CONFORMAL HIGH-JET GATE / FOR A VERTICAL CONFORMAL POSITIVE CORE `Q=alpha I`, `alpha!=0`, LET `m>=3` BE THE FIRST NONZERO TRANSVERSE ORDER OF THE ANGULAR DEFECT `chi=Lq`. THE LEADING `chi` AND `psi=Lphi` JETS ARE HORIZONTAL HARMONIC MULTIPOLES. MATERIAL DIFFERENTIATION OF THE FIRST NONZERO `chi` JET, INCLUDING THE `m` COMMUTATOR COPIES OF `grad_h B=(lambda+1/2)I`, GIVES THE EXACT LAW `D_B X_m=[kappa+(2-m)lambda-(m+1)/2]X_m-m alpha Psi_m`. ALL LOWER `psi` JETS MUST VANISH BY ORDER CONSISTENCY OF THE `chi` MATERIAL EQUATION. ON A UNIFORMLY RECURRENT NONZERO HIGH-JET BRANCH, `D_B log|X_m|` HAS ZERO MEAN, AND THE REGULAR NODAL JACOBIAN STILL GIVES `<kappa>=3/2`. THEREFORE THE ANGULAR-POTENTIAL TRANSFER MUST SATISFY `<alpha (X_m:Psi_m)/|X_m|^2>=-((m-2)/m)(1/2+<lambda>)`. IF THE SAME MATERIAL AXIAL LINE ELEMENT IS ALSO RECURRENT, `D_B log ell_3=-2lambda+1/2` FORCES `<lambda>=1/4`, SO THE TRANSFER HAS THE STRICT NEGATIVE MEAN `-3(m-2)/(4m)`. THIS IS A NEW SIGNED RECHARGE OBLIGATION, NOT A CONTRADICTION; SHAPE RECURRENCE WITHOUT SAME-MARKER AXIAL RECURRENCE REMAINS AN EXPLICIT EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Conformal vertical high-jet branch

Center the vertical regular filament on the `x_3` axis and use

\[
\mathcal L=x_1\partial_2-x_2\partial_1,
\qquad
\chi=\mathcal Lq,
\qquad
\psi=\mathcal L\phi.
\]

Assume the first-order nodal shape is conformal positive:

\[
\boxed{
Q=\nabla_h^2q|_\Gamma=\alpha I_2,
\qquad
\alpha\neq0.
}
\]

Then

\[
q^{(2)}(z)=\frac\alpha2|z|^2.
\]

M17-016 and M17-019 imply that a branch uniformly separated from the axisymmetric no-swirl firewall has a finite first nonzero angular-defect order

\[
\boxed{m\ge3.}
\]

Write the first nonzero transverse homogeneous defect jet as

\[
\boxed{
\chi(z)=X_m(z)+O(|z|^{m+1}),
}
\]

where `X_m` is a nonzero homogeneous harmonic polynomial of degree `m`.

---

## 2. Leading psi jet and lower-order consistency

Write

\[
\psi(z)=\sum_{\ell\ge1}\Psi_\ell(z)
\]

in homogeneous horizontal degree.

The exact material equation from M17-017 is

\[
D_B\chi
=\left(\kappa-\partial_3U_3-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq.
\]

At the conformal core

\[
\nabla_hq=\alpha z+O(|z|^2).
\]

Suppose `1<=ell<m` and `Psi_ell` is the first nonzero lower `psi` jet.
Then the transfer term contains

\[
-\nabla_h\Psi_\ell\cdot(\alpha z)
=-\alpha\,\ell\,\Psi_\ell
\]

by Euler homogeneity.

But `chi` has no term of degree `ell`, so neither the left side nor the multiplier term has such a contribution.
Therefore

\[
\boxed{\Psi_\ell=0\qquad(1\le\ell<m).}
\]

Also `psi=0` on the axis, so its degree-zero term vanishes.

Thus the first `psi` jet capable of entering the first nonzero `chi` equation has degree `m`:

\[
\boxed{
\psi(z)=\Psi_m(z)+O(|z|^{m+1}).
}

---

## 3. Both leading jets are horizontal harmonic multipoles

M17-019 gives

\[
\boxed{\Delta_hX_m=0.}
\]

The companion equation

\[
\Delta_h\psi=-\partial_3(G_q\chi)
\]

has right-hand side beginning at transverse order `m`.
The degree `m-2` contribution on the left can therefore only come from `Delta_h Psi_m`, so

\[
\boxed{\Delta_h\Psi_m=0.}
\]

Thus both `X_m` and `Psi_m` lie in the same two-dimensional real harmonic-multipole space of order `m`.

The axial companion law is

\[
\boxed{
\partial_3\Psi_m=(G_q-1)X_m.
}
\]

This does not fix their instantaneous relative phase.

---

## 4. Material commutator on the first nonzero jet

At the regular nodal core,

\[
\Sigma=\operatorname{diag}(\lambda,\lambda,-2\lambda),
\qquad
\Omega=0.
\]

Hence the horizontal derivative of the similarity material velocity is

\[
\boxed{
\nabla_hB_h=(\lambda+\tfrac12)I_2.
}
\]

Also

\[
\nabla_hB_3=G_q\nabla_hq=0
\]

at the axis.

When `m` horizontal derivatives are commuted through `D_B`, every first-derivative commutator contributes one copy of

\[
-(\lambda+\tfrac12).
\]

All terms involving higher derivatives of `B` multiply lower `chi` jets and vanish because `m` is the first nonzero order.
Therefore the total commutator contribution is

\[
\boxed{-m(\lambda+\tfrac12)X_m.}
\]

---

## 5. Multiplier and transfer at order m

At the core,

\[
\partial_3U_3=-2\lambda.
\]

Therefore the pointwise multiplier in the `chi` equation is

\[
\kappa+2\lambda-\frac12.
\]

The leading transfer term is

\[
-\nabla_h\Psi_m\cdot\nabla_hq^{(2)}
=-\alpha z\cdot\nabla_h\Psi_m
=-m\alpha\Psi_m.
\]

Combining the field multiplier, the `m` commutator copies, and this transfer yields

\[
\boxed{
D_BX_m
=\left[
\kappa+(2-m)\lambda-\frac{m+1}{2}
\right]X_m
-m\alpha\Psi_m.
}
\]

This is the canonical first-nonzero angular-jet material law.

---

## 6. Internal normalization check at m=2

For a nonconformal quadratic core, M17-017 has

\[
m=2
\]

and the vertical nonconformal compatibility removes the leading `psi` transfer.
Then Section 5 reduces to

\[
D_BX_2
=\left(\kappa-\frac32\right)X_2,
\]

which is exactly M17-017's leading quadratic angular-defect law.

Thus the similarity coefficients and commutator count agree with the established M17 normalization.

---

## 7. Exact amplitude law

Use the natural Euclidean inner product on the finite-dimensional order-`m` harmonic coefficient space.
Define

\[
\boxed{
R_m
:=\frac{X_m:\Psi_m}{|X_m|^2}.
}
\]

As long as `X_m!=0`, Section 5 gives

\[
\boxed{
D_B\log|X_m|
=
\kappa+(2-m)\lambda-\frac{m+1}{2}
-m\alpha R_m.
}
\]

The orthogonal component of `Psi_m` rotates the angular multipole phase; only the projection `R_m` changes its norm.

---

## 8. Recurrent high-jet transfer gate

Assume a uniformly recurrent compact branch separated from the firewall with

\[
0<c_m\le|X_m|\le C_m<\infty.
\]

Then the long-time mean of `D_B log|X_m|` vanishes.
The regular nodal Jacobian law M17-010 gives

\[
\boxed{\langle\kappa\rangle=\frac32.}
\]

Therefore

\[
0
=\frac32+(2-m)\langle\lambda\rangle
-\frac{m+1}{2}
-m\langle\alpha R_m\rangle.
\]

Hence

\[
\boxed{
\left\langle
\alpha\frac{X_m:\Psi_m}{|X_m|^2}
\right\rangle
=
-\frac{m-2}{m}
\left(
\frac12+\langle\lambda\rangle
\right).
}
\]

This is an exact signed angular-potential transfer recurrence condition.

---

## 9. Material axial line-element law

Because the nodal filament is material, an infinitesimal material tangent vector along the vertical filament evolves by

\[
D_B\ell=(\nabla B)\ell.
\]

For a vertical tangent `ell=ell_3 e_3`, the core matrix gives

\[
\nabla B\,e_3
=\left(-2\lambda+\frac12\right)e_3.
\]

Therefore

\[
\boxed{
D_B\log\ell_3
=-2\lambda+\frac12.
}
\]

If the **same material axial spacing** remains uniformly bounded above and below and is recurrent, then

\[
\boxed{
\langle\lambda\rangle=\frac14.
}
\]

This is stronger than shape recurrence alone and must not be imposed when the selected recurrent core is allowed to move through material markers or when axial material spacing drifts.

---

## 10. Strict signed transfer under same-marker axial recurrence

Insert

\[
\langle\lambda\rangle=\frac14
\]

into Section 8.
Then

\[
\boxed{
\left\langle
\alpha\frac{X_m:\Psi_m}{|X_m|^2}
\right\rangle
=-\frac{3(m-2)}{4m}.
}
\]

For every conformal high-jet order

\[
m\ge3,
\]

this is strictly negative:

\[
\boxed{
\left\langle
\alpha\frac{X_m:\Psi_m}{|X_m|^2}
\right\rangle<0.
}
\]

Thus a same-marker recurrent conformal high-jet survivor must continuously recharge a definite negative angular-potential transfer bias.

---

## 11. Relation to the lobe payer network

M17-019 gives `2m` local angular sectors, each entering a global `chi` nodal domain that must connect a positive-`kappa` core portion to a negative-`kappa` payer.

M17-083 adds a dynamical requirement on the same first resolved multipole:

\[
\boxed{
\text{finite harmonic }m\text{-jet}
\to
\text{lobe-resolved }\kappa\text{ sign reversal}
\to
\text{signed }(X_m,\Psi_m)\text{ transfer recharge}.
}
\]

No identity yet fixes the sign of `alpha R_m` from the elliptic lobe payer alone, so the two obligations are compatible in principle.

---

## 12. DSD analysis

The conformal branch no longer has an unspecified "higher jet" escape.
Its first non-axisymmetric descriptor is a finite state in the two-dimensional harmonic order-`m` space:

\[
\boxed{(X_m,\Psi_m).}
\]

The state has three distinct channels:

1. scalar amplification through `kappa`;
2. vertical strain through `lambda`;
3. angular-potential transfer through `alpha R_m`.

Recurrence fixes their exact mean balance.

---

## 13. DSD audit

### Audit A — treating the raw field equation as the jet equation
Rejected. The `m` material/spatial commutator factors are essential and produce the term `-m(lambda+1/2)`.

### Audit B — allowing arbitrary lower psi jets
Closed on the retained branch. Any lower nonzero `psi` jet would force a lower `chi` term through `-grad_h psi dot grad_h q`, contradicting the definition of `m`.

### Audit C — assuming Psi_m is aligned with X_m
Rejected. Only its projection `R_m` enters the amplitude law; an orthogonal component may rotate the multipole phase.

### Audit D — using the m=2 formula for m>=3
Rejected. The extra `lambda` multiplier and `psi` transfer survive for high jets.

### Audit E — imposing <lambda>=1/4 from shape recurrence alone
Rejected. The value `1/4` requires recurrence/boundedness of the same material axial line element.

### Audit F — interpreting the strict negative mean as contradiction
Rejected. No sign theorem presently forbids the required angular-potential transfer.

### Audit G — firewall approach
If `|X_m|` loses its uniform lower bound or the first nonzero order changes, the branch exits toward higher-order degeneration or the axisymmetric no-swirl firewall and must be reclassified rather than contradicted.

### Audit H — proof status
No global contradiction is obtained.

---

## 14. Updated vertical conformal frontier

The conformal positive vertical branch now splits as

\[
\boxed{
G_{conf+}^{vertical}
\Longrightarrow
G_{axis/no\text{-}swirl}
\lor
A_m^{nonaxis},
\qquad
3\le m\le m_A.
}
\]

A uniformly separated recurrent `A_m^{nonaxis}` survivor must satisfy

\[
\boxed{
\begin{aligned}
\Delta_hX_m&=0,\\
\Delta_h\Psi_m&=0,\\
\partial_3\Psi_m&=(G_q-1)X_m,\\
D_BX_m
&=\left[\kappa+(2-m)\lambda-\frac{m+1}{2}\right]X_m-m\alpha\Psi_m,\\
\left\langle\alpha\frac{X_m:\Psi_m}{|X_m|^2}\right\rangle
&=-\frac{m-2}{m}\left(\frac12+\langle\lambda\rangle\right).
\end{aligned}
}
\]

Under same-marker axial recurrence, the final line sharpens to

\[
\boxed{
\left\langle\alpha\frac{X_m:\Psi_m}{|X_m|^2}\right\rangle
=-\frac{3(m-2)}{4m}<0.
}
\]

---

## 15. Next target — angular-transfer / payer sign bridge

The highest-value next question is whether the strict negative mean transfer required above can be connected to the lobe-resolved negative-`kappa` payer of M17-019 through the elliptic system

\[
\Delta_h\psi=-\partial_3(G_q\chi),
\qquad
\Delta\chi=\kappa\chi.
\]

A successful bridge would either

1. show the required negative transfer is automatically supplied by the payer geometry, leaving a regular survivor; or
2. show its sign/magnitude is incompatible with the recurrent payer/hysteresis ledger, closing the conformal high-jet branch.

Until that bridge is obtained, the branch remains open.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
