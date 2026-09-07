# DSD M17-351 — The toroidal harmonic dipole coefficient is time-constant, scale invariant, and exactly matches Type-I enstrophy saturation

Date: 2026-09-08  
Canonical ID: **M17-351**

Status: **ACTIVE CONDITIONAL DIPOLE-DYNAMICS REDUCTION / M17-350 NON-STRONG-L3 BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-350

On the harmonic-exterior weak-critical branch,

\[
\Omega(x,t)
=
\frac{a(t)\times x}{|x|^3}
+O(|x|^{-3})
\qquad(|x|\to\infty),
\]

where the displayed leading term has magnitude `r^-2` and the remainder begins one harmonic order lower in magnitude.

The associated velocity, after a harmless Galilean constant is fixed, has critical size

\[
V(x,t)=O(r^{-1}),
\qquad
\nabla V(x,t)=O(r^{-2}).
\]

The exterior vorticity is harmonic:

\[
\Delta\Omega=0.
\]

## 2. Leading-order vorticity dynamics

The physical vorticity equation is

\[
\partial_t\Omega
+V\cdot\nabla\Omega
=S\Omega+\Delta\Omega.
\]

On the harmonic exterior,

\[
\Delta\Omega=0.
\]

For the dipole tail,

\[
\nabla\Omega=O(r^{-3}).
\]

Therefore

\[
V\cdot\nabla\Omega=O(r^{-4}),
\]

and

\[
S\Omega=O(r^{-2})O(r^{-2})=O(r^{-4}).
\]

A possible spatially constant Galilean velocity contributes only `O(r^-3)` to advection and hence also does not create an `r^-2` term.

Thus the right-hand side of the vorticity equation has no `r^-2` contribution.

## 3. The dipole coefficient is time independent

Differentiate the leading tail:

\[
\partial_t\Omega
=
\frac{a'(t)\times x}{r^3}
+O(r^{-3}).
\]

The first term has magnitude `r^-2`.

Since no other term in the vorticity equation has an `r^-2` contribution, its coefficient must vanish:

\[
\boxed{a'(t)=0.}
\]

Hence on every time interval on which the harmonic-exterior expansion persists coherently,

\[
\boxed{a(t)\equiv a_*\in\mathbb R^3.}
\]

The weak-critical harmonic obstruction is therefore a conserved finite-dimensional tail parameter, not an arbitrary time-dependent function.

## 4. Exact parabolic scale invariance

Under physical Navier--Stokes scaling

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

the dipole term becomes

\[
\begin{aligned}
R^2
\frac{a_*\times(Ry)}{|Ry|^3}
&=
R^3\frac{a_*\times y}{R^3|y|^3}\\
&=
\frac{a_*\times y}{|y|^3}.
\end{aligned}
\]

Therefore

\[
\boxed{a_R=a_*.}
\]

The dipole coefficient is exactly record-scale invariant.

This is stronger than the palinstrophy currency, which loses one inverse record-scale power when returned to the first ancient ancestor.

## 5. Exterior enstrophy carried by the dipole

For the leading field

\[
\Omega_{dip}=rac{a_*\times x}{r^3},
\]

\[
|\Omega_{dip}|^2
=
\frac{|a_*|^2\sin^2\vartheta}{r^4}.
\]

Hence

\[
\begin{aligned}
\int_{|x|>R}|\Omega_{dip}|^2dx
&=
|a_*|^2
\left(\int_{S^2}\sin^2\vartheta\,d\omega\right)
\int_R^\infty r^{-2}dr\\
&=
\frac{8\pi}{3}\frac{|a_*|^2}{R}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\Omega_{dip}\|_{L^2(|x|>R)}^2
=
\frac{8\pi}{3}\frac{|a_*|^2}{R}.
}
\]

## 6. Exact match with the M5-477 Type-I enstrophy rate

At ancient time `t=-T`, the natural similarity radius is

\[
R\sim\sqrt{T}.
\]

A conserved toroidal dipole beginning at that similarity radius carries

\[
\boxed{
\int_{|x|\gtrsim\sqrt T}|\Omega_{dip}|^2dx
\asymp
|a_*|^2T^{-1/2}.
}
\]

M5-477 proves precisely the critical Type-I enstrophy order

\[
\|\Omega(-T)\|_2^2\asymp T^{-1/2}
\]

along the backward record sequence.

Therefore a nonzero conserved dipole is **perfectly compatible** with the previously observed enstrophy saturation.

It cannot be rejected merely because the ancient enstrophy tends to zero.

## 7. Why finite total palinstrophy also does not immediately remove a_*

The dipole is scale invariant while its enstrophy contribution on an old physical record window moves outward to radius `sqrt(T)` and has size `T^-1/2`.

Thus the tail can persist while every fixed spatial compact set sees vanishing influence at backward infinity.

This is exactly the low-frequency/escape mechanism already isolated in M5-476 and explains why local strong convergence does not determine the coefficient `a_*`.

## 8. Updated weak-critical tail

The entire harmonic weak-critical branch is now reduced to

\[
\boxed{
\text{one constant scale-invariant vector }a_*\ne0.
}
\]

If

\[
a_*=0,
\]

M17-350 gives strong global `L3`.

If

\[
a_*\ne0,
\]

then the survivor is an asymptotically toroidal critical tail carrying exactly the Type-I enstrophy rate.

## 9. New highest-value target

The next closing question is no longer generic tail decay.  It is:

\[
\boxed{
\text{Can finite-energy first-hitting ancestry / material genealogy generate or retain a nonzero }a_*?
}
\]

Possible mechanisms to audit are:

1. whether `a_*` is representable as an asymptotic circulation/impulse invariant inherited from the prelimit;
2. whether the fixed-axis toroidal tail is compatible with the M17-313 material-line genealogy and positive recurrent `Q_0`;
3. whether nonzero `a_*` forces unbounded winding/reuse that enters an already typed geometric exit.

## 10. DSD-theory role

The useful heuristic is to replace a broad weak-critical class by the invariant structural datum that actually survives the PDE and scaling audits.

The derivation of `a'=0`, scale invariance, and the `T^-1/2` enstrophy law is standard asymptotic Navier--Stokes analysis.

No DSD axiom is used as a proof hypothesis.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
