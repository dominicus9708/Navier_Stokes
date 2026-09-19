# M20-012 — A common homogeneity-corrected material generator closes the enstrophy-weighted projective-strain product ledger

Date: 2026-09-20  
Canonical ID: **M20-012**  
Status: **COMMON-GENERATOR RESOLUTION / THE M20-011 GENERATOR MISMATCH CAN BE PARTLY REMOVED BY USING THE EXACT TERMINAL HOMOGENEITY-CORRECTED MATERIAL OPERATOR M_m / ENSTROPHY E=|B|^2 AND PROJECTIVE STRAIN K=|[Sigma,Q]|^2 BOTH HAVE HOMOGENEITY FOUR, SO THEIR PRODUCT EK HAS HOMOGENEITY EIGHT / THE PRODUCT RULE YIELDS AN EXACT JOINT LEDGER IN WHICH AXIAL STRETCHING ENTERS WITH NET COEFFICIENT -2 / q-SPHERE AVERAGING CONVERTS THE MATERIAL DERIVATIVE INTO A WEDGE-DEPTH DERIVATIVE PLUS AN EXPLICIT RADIAL FLUX, ELIMINATING THE NEED TO ASSUME q-RECURRENCE IS MATERIAL-LINE RECURRENCE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Homogeneity-corrected terminal material generator

Let a physical scalar coefficient have the form

\[
f_{\rm phys}(x,s)
=
r^{-m}F(z,q,\omega).
\]

At the terminal boundary \(z=0\),

\[
u=r^{-1}A.
\]

A direct calculation gives

\[
D_t f_{\rm phys}
=
r^{-m-2}
\mathcal M_mF,
\]

where

\[
\boxed{
\mathcal M_mF
:=
-\partial_zF
+
A_r(\partial_q-m)F
+
A_T\cdot\nabla_SF.
}
\]

Thus \(\mathcal M_m\) is the exact terminal normalized material generator for a coefficient of physical homogeneity \(r^{-m}\).

## 2. Product rule

If F has homogeneity m and G has homogeneity n, then FG has homogeneity \(m+n\).

The generators satisfy the exact product rule

\[
\boxed{
\mathcal M_{m+n}(FG)
=
F\,\mathcal M_nG
+
G\,\mathcal M_mF.
}
\]

This is the key algebraic mechanism that allows amplitude and projective-strain dynamics to be combined without confusing their physical scaling.

## 3. q-sphere invariant-mean formula

Let

\[
\langle\cdot\rangle
\]

denote the invariant q-mean followed by sphere integration.

The terminal incompressibility condition is

\[
(\partial_q+1)A_r+\operatorname{div}_SA_T=0.
\]

Hence

\[
\partial_qA_r+\operatorname{div}_SA_T=-A_r.
\]

For any scalar F,

\[
\left\langle
A_r\partial_qF
+
A_T\cdot\nabla_SF
\right\rangle
=
\left\langle
A_rF
\right\rangle.
\]

Therefore

\[
\boxed{
\left\langle
\mathcal M_mF
\right\rangle
=
-\frac d{dz}
\langle F\rangle\Big|_{z=0}
+
(1-m)
\langle A_rF\rangle.
}
\]

In particular,

\[
\boxed{
\langle\mathcal M_4F\rangle
=
-\langle F\rangle_z'
-
3\langle A_rF\rangle,
}
\]

and

\[
\boxed{
\langle\mathcal M_8F\rangle
=
-\langle F\rangle_z'
-
7\langle A_rF\rangle.
}
\]

Thus q-recurrence does not make the material derivative vanish; it leaves an explicit radial flux term.

This is the corrected common-measure statement.

## 4. Enstrophy coefficient equation

Let

\[
E:=|B|^2.
\]

The physical enstrophy density is

\[
|\omega|^2=r^{-4}E.
\]

From the exact vorticity-magnitude equation,

\[
D_t|\omega|^2
=
2\gamma_{\rm phys}|\omega|^2
+
2|\omega|\Delta|\omega|
-
2|\omega|^2|\nabla\xi|^2.
\]

At the terminal coefficient level,

\[
\boxed{
\mathcal M_4E
=
2\gamma E
+
\mathcal R_E,
}
\]

where

\[
\boxed{
\mathcal R_E
:=
2\beta\,\mathcal L_2\beta
-
2E\mathcal D_\xi,
}
\]

with

\[
\beta=|B|,
\qquad
\mathcal D_\xi
=
|\partial_q\xi|^2
+
|\nabla_S\xi|^2.
\]

Thus \(\mathcal R_E\) is the scalar diffusion/direction-gradient remainder in material form.

## 5. Projective-strain coefficient equation

Let the terminal strain coefficient be \(\Sigma\), so that

\[
S_{\rm phys}=r^{-2}\Sigma.
\]

Define

\[
\boxed{
K
:=
\|[\Sigma,Q]\|_F^2
=
2|P_\xi^\perp\Sigma\xi|^2.
}
\]

Then the physical quantity

\[
\|[S_{\rm phys},Q]\|_F^2
=
r^{-4}K.
\]

M20-006 gives, after exact normalization,

\[
\boxed{
\frac14\mathcal M_4K
+
\gamma K
=
\mathcal R_K,
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal R_K
:={}&
-\frac12
\langle[\Sigma,Q],[H,Q]\rangle_F
\\
&+
\nu\,s_\perp\cdot(\mathcal L_S\Sigma)\xi
+
s_\perp\cdot(\Sigma-\gamma I)v_\perp.
\end{aligned}
}
\]

Here H is the normalized pressure-Hessian coefficient and \(\mathcal L_S\Sigma\) denotes the correctly normalized strain-diffusion coefficient.

The exact detailed notation of the viscous strain operator may be expanded in a later dedicated derivative module; only its homogeneity-six physical scaling is used here.

Equivalently,

\[
\boxed{
\mathcal M_4K
=
-4\gamma K
+
4\mathcal R_K.
}
\]

## 6. Exact product ledger

Since both E and K have homogeneity four, their product has homogeneity eight.

Using Section 2,

\[
\mathcal M_8(EK)
=
K\mathcal M_4E
+
E\mathcal M_4K.
\]

Substitute Sections 4 and 5:

\[
\begin{aligned}
\mathcal M_8(EK)
&=
K(2\gamma E+\mathcal R_E)
+
E(-4\gamma K+4\mathcal R_K)
\\
&=
-2\gamma EK
+
K\mathcal R_E
+
4E\mathcal R_K.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal M_8(EK)
+
2\gamma EK
=
K\mathcal R_E
+
4E\mathcal R_K.
}
\]

This is the main M20-012 joint material ledger.

## 7. Structural meaning of the net -2 gamma coefficient

Enstrophy alone gains

\[
+2\gamma E
\]

under forward material stretching.

Projective strain misalignment alone has homogeneous contribution

\[
-4\gamma K.
\]

Therefore their product has net stretching contribution

\[
\boxed{
-2\gamma EK.
}
\]

Thus positive axial stretching simultaneously:

- amplifies vorticity magnitude;
- aligns vorticity with strain strongly enough that the enstrophy-weighted projective-misalignment product is damped overall.

Negative axial stretching has the opposite effect.

This makes the competition identified in M20-010 exact at the product level.

## 8. q-averaged terminal wedge-depth ledger

Define

\[
\boxed{
\mathscr J_{EK}(z)
:=
\left\langle
E(z)K(z)
\right\rangle.
}
\]

At z=0, Section 3 with \(m=8\) gives

\[
\left\langle
\mathcal M_8(EK)
\right\rangle
=
-\mathscr J_{EK}'(0)
-
7
\left\langle
A_rEK
\right\rangle.
\]

Therefore the product law yields

\[
\boxed{
\begin{aligned}
-\mathscr J_{EK}'(0)
&-
7\langle A_rEK\rangle
+
2\langle\gamma EK\rangle
\\
&=
\langle K\mathcal R_E\rangle
+
4\langle E\mathcal R_K\rangle.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
2\langle\gamma EK\rangle
={}&
\mathscr J_{EK}'(0)
+
7\langle A_rEK\rangle
\\
&+
\langle K\mathcal R_E\rangle
+
4\langle E\mathcal R_K\rangle.
\end{aligned}
}
\]

This is a genuine terminal wedge-depth signed ledger.

No material-line invariant measure has been assumed.

## 9. Relation to the M20-011 signed moment

Recall the terminal enstrophy probability

\[
d\pi_B=\frac{E}{b_2}d\mu.
\]

Then

\[
M_{\gamma K}
=
\mathbb E_{\pi_B}[\gamma K]
=
\frac{\langle\gamma EK\rangle}{b_2}.
\]

Hence

\[
\boxed{
\begin{aligned}
2b_2M_{\gamma K}
={}&
\mathscr J_{EK}'(0)
+
7\langle A_rEK\rangle
\\
&+
\langle K\mathcal R_E\rangle
+
4\langle E\mathcal R_K\rangle.
\end{aligned}
}
\]

Thus the second row of M20-011 is no longer an abstract material-line quantity.

It is exactly represented by:

1. a finite-depth derivative of the enstrophy-weighted projective-misalignment moment;
2. an explicit radial transport term;
3. scalar vorticity diffusion/direction-gradient coupling;
4. transverse pressure/strain-diffusion/viscous-projective forcing.

## 10. Resolution of the M20-011 generator firewall

M20-011 correctly warned that q-recurrence alone does not imply

\[
\mathbb E[D_tK]=0.
\]

M20-012 does not contradict that warning.

Instead it removes the need for the false step.

The normalized material generator converts exactly into

\[
\boxed{
\text{wedge-depth derivative}
+
\text{radial flux}.
}
\]

Therefore the correct route is not

\[
q\text{-recurrence}
\Rightarrow
\langle D_tK\rangle=0.
\]

It is

\[
\boxed{
D_t
\Rightarrow
\partial_z
+
\text{explicit terminal flux}.
}
\]

This is a stronger and safer formulation.

## 11. Joint neutrality now has a concrete PDE meaning

If the M20-011 signed moment is small,

\[
M_{\gamma K}\approx0,
\]

then the product ledger requires

\[
\boxed{
\mathscr J_{EK}'(0)
+
7\langle A_rEK\rangle
+
\langle K\mathcal R_E\rangle
+
4\langle E\mathcal R_K\rangle
\approx0.
}
\]

Thus projective-strain neutrality must be paid by an exact combination of:

- finite-depth deformation of the weighted projective moment;
- radial transport;
- scalar magnitude diffusion/direction damping;
- off-axis pressure/strain diffusion/viscous projective forcing.

There is no untyped remainder.

## 12. Pressure contribution inside the product ledger

The pressure part of \(4E\mathcal R_K\) is

\[
\boxed{
-2E
\langle[\Sigma,Q],[H,Q]\rangle_F.
}
\]

M20-007 shows this remains a traceless Calderon--Zygmund critical channel.

Thus the common product ledger does not convert pressure into a noncritical resource.

It only places pressure in the correct enstrophy-weighted signed correlation.

## 13. Direction-gradient coupling appears twice but must not be double counted

The direction-gradient field enters:

- \(\mathcal R_E\) through vorticity-magnitude damping;
- \(\mathcal R_K\) through viscous projective direction motion.

These are distinct algebraic appearances of the same underlying derivative geometry.

Therefore future estimates must preserve their joint origin.

One must not count both as independent positive payers without an orthogonality or coercivity theorem.

## 14. New common-generator frontier

The M20 joint state can now be studied through

\[
\boxed{
(E,\;K,\;\gamma)
}
\]

with the exact product ledger

\[
\boxed{
\mathcal M_8(EK)+2\gamma EK
=
K\mathcal R_E+4E\mathcal R_K.
}
\]

This is the first M20 equation that simultaneously contains:

- amplitude;
- projective strain;
- stretching;
- pressure;
- diffusion;
- direction-gradient effects;

under one generator.

## 15. What remains missing

The new product ledger is exact, but it still has no one-way sign.

The terms

\[
\mathscr J_{EK}'(0),
\qquad
\langle A_rEK\rangle,
\qquad
\langle K\mathcal R_E\rangle,
\qquad
\langle E\mathcal R_K\rangle
\]

are signed.

Therefore no contradiction follows from the identity alone.

The key question becomes whether the hard recurrent component can make all four compensators recycle at the exact critical scale.

## 16. Next target

M20-013 should inspect the first two terms:

\[
\mathscr J_{EK}'(0)
+
7\langle A_rEK\rangle.
\]

These are the pure finite-depth/radial-transport parts of the common ledger.

The goal is to determine whether they form an exact conservative coboundary, as happened in the M19-440 energy audit, or whether a genuine signed finite-depth current remains.

Only after that audit should the pressure/diffusion right-hand side be treated as a possible independent compensation resource.

\[
\boxed{\text{M20-012 COMPLETE; A COMMON HOMOGENEITY-CORRECTED MATERIAL GENERATOR YIELDS AN EXACT ENSTROPHY-WEIGHTED PROJECTIVE-STRAIN PRODUCT LEDGER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
