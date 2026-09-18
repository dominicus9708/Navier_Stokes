# M19-419 — Pure l=1 first-jet residual is toroidal, but a nonzero pure toroidal l=1 leading trace necessarily leaks to l=3

Date: 2026-09-19  
Canonical ID: **M19-419**  
Status: **SPHERICAL-HARMONIC RESIDUAL CLASSIFICATION / BOUNDED RECURRENT DIVERGENCE-FREE PURE-l1 FIRST JET IS EXACTLY TOROIDAL / TORQUE BALANCE DOES NOT EXCLUDE IT / HOWEVER A NONZERO BOUNDED RECURRENT PURE-TOROIDAL-l1 LEADING TRACE GENERATES AN UNAVOIDABLE l=3 COMPONENT IN ITS FIRST STATIONARY RESIDUAL / PURE-l1 SELF-CLOSED SURVIVOR REMOVED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-418

The retained hard minimal hull has mandatory syndetic mean-free angular first-jet activity.

Write
\[
C(q,\omega)
=
C_{l=1}(q,\omega)
+
C_{l\ge2}(q,\omega),
\]
after the spherical mean has been removed.

The immediate question is whether all mandatory angular activity can live forever in the lowest nonconstant componentwise spherical sector
\[
l=1.
\]

## 2. General componentwise l=1 vector field

Every \(\mathbb R^3\)-valued componentwise \(l=1\) field has the form
\[
\boxed{
C_1(q,\omega)
=
\mathsf M(q)\omega
}
\]
for a real \(3\times3\) matrix \(\mathsf M(q)\).

The corresponding physical first-jet field is
\[
r^{-3}C_1
=
r^{-4}\mathsf M(q)x.
\]

## 3. Divergence-free condition

Direct differentiation gives
\[
\nabla\cdot(r^{-3}C_1)
=
r^{-4}
\left[
\operatorname{tr}\mathsf M
+
\omega^T(\mathsf M'-4\mathsf M)\omega
\right].
\]

Hence incompressibility for every \(\omega\) requires
\[
\boxed{
\operatorname{sym}(\mathsf M'-4\mathsf M)
=
-(\operatorname{tr}\mathsf M)I.
}
\]

Write
\[
\operatorname{sym}\mathsf M
=
\alpha I+Q,
\qquad
\operatorname{tr}Q=0.
\]

Then
\[
\boxed{
\alpha'=\alpha,
\qquad
Q'=4Q.
}
\]

On a two-sided bounded recurrent log-radius hull, neither \(e^q\) nor \(e^{4q}\) is admissible unless its coefficient is zero.

Therefore
\[
\boxed{
\operatorname{sym}\mathsf M=0.
}
\]

Thus \(\mathsf M\) is antisymmetric.

Every antisymmetric matrix is cross product with one vector \(a(q)\), so
\[
\boxed{
C_1(q,\omega)
=
a(q)\times\omega.
}
\]

Therefore a bounded recurrent divergence-free pure-\(l=1\) first jet is exactly toroidal.

## 4. It saturates the generic angular Poincare gap

For
\[
C_1=a\times\omega,
\]
one has
\[
\boxed{
\int_{S^2}|C_1|^2d\omega
=
\frac{8\pi}{3}|a|^2.
}
\]

Since every Cartesian component is an \(l=1\) harmonic,
\[
\boxed{
\int_{S^2}|\nabla_{S^2}C_1|^2d\omega
=
2
\int_{S^2}|C_1|^2d\omega
=
\frac{16\pi}{3}|a|^2.
}
\]

Thus the generic Poincare inequality used in M19-418 is sharp on this branch.

No stronger angular spectral constant is available unless this toroidal \(l=1\) sector is independently removed or coupled to higher modes.

## 5. Exact normalized torque relation

Let the critical momentum stress satisfy
\[
\nabla\cdot\mathbb S_T
=
r^{-3}C
\]
in the chosen residual sign convention.

Define the physical torque flux
\[
\mathcal Q(r)
:=
\int_{S_r}
x\times(\mathbb S_Tn)dS.
\]

Because \(\mathbb S_T\) is symmetric,
\[
\nabla\cdot(x\times\mathbb S_T)
=
x\times(\nabla\cdot\mathbb S_T).
\]

Define the scale-normalized torque
\[
\Theta(q)
:=
e^{-q}\mathcal Q(e^q).
\]

The shell divergence theorem gives
\[
\boxed{
\Theta'(q)+\Theta(q)
=
J_C(q),
}
\]
where
\[
J_C(q)
:=
\int_{S^2}
\omega\times C(q,\omega)d\omega.
\]

For the pure toroidal \(l=1\) field,
\[
\boxed{
J_C
=
\frac{8\pi}{3}a(q).
}
\]

Hence bounded recurrence gives the unique bounded resolvent
\[
\boxed{
\Theta(q)
=
\int_0^\infty
e^{-\tau}
J_C(q-\tau)d\tau.
}
\]

Taking the invariant mean,
\[
\boxed{
\langle\Theta\cdot J_C\rangle
=
\langle|\Theta|^2\rangle,
}
\]
and
\[
\boxed{
\langle|J_C|^2\rangle
=
\langle|\Theta'|^2\rangle
+
\langle|\Theta|^2\rangle.
}
\]

Therefore torque supplies an exact decomposition but no one-sign contradiction.

This agrees with the older M19-056 angular-momentum firewall.

## 6. Test the self-closed pure-toroidal l=1 leading trace

Now assume the leading terminal trace itself lies entirely in one fixed toroidal \(l=1\) axis.

By rotation take the axis to be \(e_z\), and write
\[
\boxed{
A(q,\omega)
=
b(q)e_z\times\omega.
}
\]

The physical leading velocity is
\[
v(x)
=
r^{-1}A
=
\frac{b(q)}{r^2}e_z\times x.
\]

Let
\[
h(q):=b(q)^2.
\]

The stationary first residual is
\[
C
=
-\mathcal L_1A
+
\mathcal N(A)
+
\mathcal G_2P.
\]

The viscous/log-radial linear term preserves the toroidal componentwise \(l=1\) sector.

Therefore every \(l=3\) component of \(C\) comes from the nonlinear-plus-pressure part.

## 7. Exact nonlinear acceleration

Because \(A\) is tangent to spheres, the radial amplitude is constant along its own streamlines.

The physical convective acceleration is
\[
(v\cdot\nabla)v
=
r^{-3}h(q)
\left[
\mu e_z-\omega
\right],
\qquad
\mu:=e_z\cdot\omega.
\]

Equivalently in spherical components,
\[
(v\cdot\nabla)v
=
-r^{-3}h
\left[
(1-\mu^2)e_r
+
\mu\sqrt{1-\mu^2}\,e_\theta
\right].
\]

Its divergence is
\[
\boxed{
\nabla\cdot[(v\cdot\nabla)v]
=
r^{-4}
\left[
\frac23(h-h')
+
\frac23(h'-4h)P_2(\mu)
\right].
}
\]

## 8. Exact l=2 pressure equation

Write the canonical pressure as
\[
P
=
r^{-2}
\left[
p_0(q)
+
p_2(q)P_2(\mu)
\right].
\]

The pressure equation
\[
-\Delta P
=
\nabla\cdot[(v\cdot\nabla)v]
\]
gives, in the \(l=2\) sector,
\[
\boxed{
p_2''-3p_2'-4p_2
=
\frac23(4h-h').
}
\]

The bounded recurrent pressure selection rules out exponentially growing homogeneous pressure modes.

## 9. l=3 coefficient of the first residual

Convert
\[
(v\cdot\nabla)v+\nabla P
\]
back to Cartesian-valued angular form.

The only cubic-in-\(\omega\) term, and therefore the only componentwise \(l=3\) contribution, has coefficient proportional to
\[
\boxed{
\frac32
\left(
p_2'-4p_2
\right).
}
\]

More explicitly the angular vector contains
\[
\frac32(p_2'-4p_2)
\,\mu^2\omega,
\]
whose traceless cubic part is a nonzero \(l=3\) vector harmonic unless the scalar coefficient vanishes.

Since the linear viscous part is pure \(l=1\), the full first residual can have no \(l=3\) part only if
\[
\boxed{
p_2'-4p_2=0.
}
\]

## 10. Bounded recurrence forces triviality if l=3 leakage is forbidden

The ODE
\[
p_2'=4p_2
\]
has
\[
p_2(q)=ce^{4q}.
\]

A bounded two-sided recurrent pressure coefficient therefore requires
\[
\boxed{p_2\equiv0.}
\]

Insert this into the exact pressure equation:
\[
0
=
\frac23(4h-h').
\]

Thus
\[
\boxed{
h'=4h.
}
\]

But
\[
h=b^2\ge0
\]
is bounded recurrent.

Hence
\[
\boxed{
h\equiv0
}
\]
and therefore
\[
\boxed{
b\equiv0.
}
\]

We have proved
\[
\boxed{
A=b(q)e_z\times\omega\neq0
\quad\Longrightarrow\quad
\Pi_{l=3}C\neq0
}
\]
for every bounded recurrent pure-toroidal \(l=1\) leading trace.

## 11. Main consequence

The simplest possible self-closed residual survivor is impossible.

One cannot have simultaneously

\[
\boxed{
A\text{ nonzero bounded recurrent pure toroidal }l=1
}
\]

and

\[
\boxed{
C^\perp\text{ supported only in }l=1.
}
\]

Nonlinear Navier--Stokes coupling plus the canonical pressure solve necessarily leaks the first residual into \(l=3\).

Therefore the mandatory angular activity of M19-418 cannot remain in a self-contained \(l=1\) toroidal system when the leading trace is itself confined to that same sector.

## 12. What remains open

This does **not** prove that every hard first residual has \(l\ge2\) activity.

A general leading trace may contain higher/mixed spherical modes whose cross interactions cancel the \(l=3\) leakage generated by its toroidal \(l=1\) component.

Thus the surviving pure-first-jet-l1 possibility has been converted into a **spectral compensation problem**:

\[
\boxed{
C_{l\ge2}=0
\Longrightarrow
\text{higher/mixed modes of }A
\text{ must cancel the intrinsic }l=3\text{ toroidal self-interaction.}
}
\]

This is a stronger and more concrete gate than the previous generic angular Poincare inequality.

## 13. Updated frontier

After M19-418--419, the residual hard branch satisfies

\[
\boxed{
A_{res}^{syndetic}
}
\]

and then either

\[
\boxed{
C_{l\ge2}^{syndetic/nontrivial}
}
\]

or

\[
\boxed{
\mathcal C_{spec}:
\text{persistent nonlinear spectral compensation by higher/mixed leading modes.}
}
\]

The next calculation should quantify this compensation.

On compact normalized states with a fixed nonzero toroidal \(l=1\) amplitude, continuity of the \(l=3\) residual map suggests a finite gap:

either the leading trace carries a definite higher/mixed harmonic mass, or the first residual carries a definite \(l=3\) mass.

Establishing that finite-gap fork is the next target.

\[
\boxed{\text{M19-419 COMPLETE; THE PURE-l1 SELF-CLOSED TERMINAL-JET SURVIVOR IS REMOVED.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
