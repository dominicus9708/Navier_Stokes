# DSD RSS Rotation–Dilation Discriminant Gate

Date: 2026-08-25

Status: **EXACT TWO-CHANNEL RSS COMPATIBILITY SYSTEM DERIVED / ROTATION PARAMETER AND RADIAL-ANGULAR PHASE CROSS TERM ELIMINATED / NEW DISCRIMINANT NECESSITY OBTAINED / NO UNIVERSAL SIGN CLOSURE YET / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

Continue the exact RSS vorticity profile equation

\[
\boxed{
\alpha\mathcal G\Omega
+\Omega
+\frac12D\Omega
+\mathcal N_\Omega
-\nu\Delta\Omega
=0,
}
\]

where

\[
D:=Y\cdot\nabla,
\]

\[
\mathcal G\Omega
:=J\Omega-(JY\cdot\nabla)\Omega,
\]

and

\[
\mathcal N_\Omega
:=(U\cdot\nabla)\Omega-(\Omega\cdot\nabla)U.
\]

Assume the pairings below are finite. In particular require

\[
D\Omega\in L^2,
\qquad
\mathcal G\Omega\in L^2,
\qquad
\mathcal N_\Omega\in L^2
\]

or an approximation/truncation regime justifying the identities.

For a regular genuine `1/R` Type-I profile with vorticity `Omega~R^-2`, these quantities have the correct far-field integrability, but this weighted/dilation regularity is retained as an explicit hypothesis rather than inferred from plain `H2` compactness.

---

## 2. Generator channel

Define

\[
\boxed{
A:=\|\mathcal G\Omega\|_2^2,
}
\]

\[
\boxed{
I:=\langle D\Omega,\mathcal G\Omega\rangle,
}
\]

and

\[
\boxed{
B:=\langle\mathcal N_\Omega,\mathcal G\Omega\rangle.
}
\]

As derived in the preceding rotation-generator audit,

\[
\langle\Omega,\mathcal G\Omega\rangle=0
\]

and

\[
\langle-\Delta\Omega,\mathcal G\Omega\rangle=0.
\]

Pairing the RSS equation with `G Omega` gives

\[
\boxed{
\alpha A+\frac12I+B=0.
}
\tag{G}
\]

For a genuinely rotation-active profile

\[
A>0.
\]

---

## 3. Dilation channel

Pair the same RSS equation with

\[
D\Omega=Y\cdot\nabla\Omega.
\]

The zeroth-order dilation identity in three dimensions is

\[
\boxed{
\langle\Omega,D\Omega\rangle
=-\frac32\|\Omega\|_2^2.
}
\]

Write

\[
Z:=\|\Omega\|_2^2,
\qquad
Q:=\|\nabla\Omega\|_2^2.
\]

For the viscous term,

\[
\begin{aligned}
\langle-\Delta\Omega,D\Omega\rangle
&=\int\nabla\Omega:\nabla(D\Omega)\\
&=Q+\int\nabla\Omega:D(\nabla\Omega)\\
&=Q-\frac32Q\\
&=-\frac12Q.
\end{aligned}
\]

Therefore

\[
\boxed{
\langle-\nu\Delta\Omega,D\Omega\rangle
=-\frac\nu2Q.
}
\]

Define the dilation nonlinear transfer

\[
\boxed{
C_N:=\langle\mathcal N_\Omega,D\Omega\rangle.
}
\]

The dilation pairing gives

\[
\boxed{
\alpha I
-\frac32Z
+\frac12\|D\Omega\|_2^2
+C_N
-\frac\nu2Q
=0.
}
\]

Define the total dilation residual

\[
\boxed{
C
:=
-\frac32Z
+\frac12\|D\Omega\|_2^2
+C_N
-\frac\nu2Q.
}
\]

Then the second channel is simply

\[
\boxed{
\alpha I+C=0.
}
\tag{D}
\]

---

## 4. Eliminate alpha

Assume `A>0`.

From (G),

\[
\alpha
=-\frac{\frac12I+B}{A}.
\]

Insert this into (D):

\[
-\frac{I(\frac12I+B)}{A}+C=0.
\]

Hence

\[
\boxed{
\frac12I^2+BI-AC=0.
}
\]

Equivalently,

\[
\boxed{
I^2+2BI-2AC=0.
}
\tag{RD}
\]

This is an exact RSS rotation–dilation compatibility condition with `alpha` removed.

---

## 5. Discriminant necessity

The quadratic equation (RD) has a real solution `I` only if

\[
\boxed{
B^2+2AC\ge0.
}
\]

Thus every genuinely rotation-active RSS profile in the stated class must satisfy the new phase-geometry inequality

\[
\boxed{
\left\langle\mathcal N_\Omega,\mathcal G\Omega\right\rangle^2
+
2\|\mathcal G\Omega\|_2^2
\left(
-\frac32Z
+\frac12\|D\Omega\|_2^2
+C_N
-\frac\nu2Q
\right)
\ge0.
}
\]

This condition is invisible to the ordinary H0/H1/Betchov scalar balances.

---

## 6. Direct exclusion criterion

If for an admissible profile one can prove

\[
\boxed{
C< -\frac{B^2}{2A},
}
\]

then

\[
B^2+2AC<0,
\]

which is impossible.

Therefore

\[
\boxed{
C< -\frac{B^2}{2A}
\Longrightarrow
\text{no genuinely rotation-active RSS profile in the class}.
}
\]

This is a new concrete intermediate-rotation exclusion target.

It does not refer to `alpha` at all; it tests whether the profile's radial/angular and nonlinear geometry can support **any** constant-rate rotation.

---

## 7. Recover alpha when the discriminant is nonnegative

Let

\[
\Delta_{RD}:=B^2+2AC\ge0.
\]

The two possible cross terms are

\[
\boxed{
I=-B\pm\sqrt{\Delta_{RD}}.
}
\]

Using (G), the corresponding angular speeds are

\[
\boxed{
\alpha
=-\frac{B\pm\sqrt{\Delta_{RD}}}{2A},
}
\]

with the signs paired consistently.

Thus the rotation speed is not a free parameter once the profile geometry is fixed: it is determined by the three scalar generator/dilation channels `A,B,C`.

This exact formula is useful even without a contradiction because it converts the external parameter `alpha` into internal profile quantities.

---

## 8. Critical homogeneous tail contributes no leading rotation–dilation cross term

For an exactly `-2` homogeneous vorticity tail,

\[
D\Omega=-2\Omega.
\]

Since

\[
\langle\Omega,\mathcal G\Omega\rangle=0,
\]

its contribution to

\[
I=\langle D\Omega,\mathcal G\Omega\rangle
\]

vanishes at the exact homogeneous level.

Therefore nonzero `I` measures deviation from a pure critical homogeneous tail, such as radial variation of angular phase or core/tail transition geometry.

This is consistent with the quiet-ancestor picture: a perfectly passive critical tail is rotation-dilation neutral to leading order, while the nontrivial phase burden is concentrated in the active transition/core structure.

---

## 9. Why the discriminant is not yet closed by existing estimates

The residual

\[
C
=
-\frac32Z
+\frac12\|D\Omega\|_2^2
+C_N
-\frac\nu2Q
\]

contains competing terms with no established universal sign.

Likewise

\[
B=\langle\mathcal N_\Omega,\mathcal G\Omega\rangle
\]

is a phase-sensitive nonlinear transfer rather than one of the previously bounded scalar production rates.

The existing H0/H1 recurrence taxes control different contractions of the same PDE and do not imply

\[
B^2+2AC<0.
\]

Therefore no intermediate-alpha RSS closure is claimed here.

---

## 10. Next quantitative target

A useful next calculation is to decompose

\[
\mathcal N_\Omega
=(U\cdot\nabla)\Omega-(\Omega\cdot\nabla)U
\]

into radial and tangential components relative to spheres.

The desired estimate is not merely an absolute bound on `B` or `C_N`, but a compatibility inequality of the form

\[
\boxed{
|B|^2
\le
2A(-C)-\delta_{rot}
}
\]

on a candidate class with `C<0`, which would force a negative discriminant.

Alternatively, if the discriminant remains nonnegative, the exact formula for `alpha` should be compared to the Pineau-Vicol small/large rotation thresholds.

This identifies a genuinely new angular/radial phase calculation rather than another scalar norm sharpening.

---

## 11. DSD audit

The finite formed channels are

- angular activity `A`;
- rotation–dilation covariance `I`;
- nonlinear angular transfer `B`;
- dilation residual `C`;
- angular speed `alpha`.

The two exact equations (G) and (D) are composed only after each quantity is separately defined.

No sign is assigned to the nonlinear phase channels without proof.

---

## 12. Updated frontier

The structured RSS test has produced a nontrivial new gate:

\[
\boxed{
B^2+2AC\ge0.
}
\]

Any profile violating it cannot support constant-rate rotated self-similarity.

The next step is to determine whether the incompressibility/Betchov/strain-compatibility structure controls `B` and `C` strongly enough to force a gap on the intermediate-rotation class.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
