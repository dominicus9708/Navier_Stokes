# DSD RSS Speed-Floor -> Rotational Phase-Payment Gate

Date: 2026-08-25

Status: **PINEAU-VICOL ONE-SLICE SPEED FLOOR CONVERTED TO A GLOBAL VORTICITY-GENERATOR LOWER BOUND FOR RSS / GENERATOR IDENTITY CONVERTS THIS TO A RADIAL-ANGULAR OR NONLINEAR PHASE PAYMENT / NO UNIVERSAL CONTRADICTION YET / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

Assume an exact RSS orbit

\[
V(Y,s)=R(\alpha s)U(R(-\alpha s)Y),
\]

with vorticity

\[
W(Y,s)=R(\alpha s)\Omega(R(-\alpha s)Y).
\]

Assume also that the spatial Type-I and pressure-annulus hypotheses needed for the Pineau-Vicol one-slice regularity criterion hold.

For a hypothetical singular survivor, their criterion yields a uniform late-time lower bound on an admissible self-similar-time motion norm. We use the weaker Gaussian-weighted version because it interfaces cleanly with global Sobolev control.

---

## 2. Gaussian-weighted speed floor

Let

\[
w(Y):=(1+|Y|)e^{-|Y|^2/8}.
\]

For a singular survivor, the one-slice theorem implies, after fixing the theorem constants, a positive lower bound of the form

\[
\boxed{
\int_{\mathbb R^3}
|\partial_sV(Y,s)|w(Y)dY
\ge\delta_{PV}>0
}
\]

at every sufficiently late applicable time.

For RSS,

\[
\partial_sV=\alpha\mathcal GV.
\]

Therefore

\[
\boxed{
|\alpha|
\int|\mathcal GV|w
\ge\delta_{PV}.
}
\]

---

## 3. Weighted L1 controlled by the vorticity rotation generator

The weight satisfies

\[
w\in L^{6/5}(\mathbb R^3).
\]

Holder gives

\[
\int|\mathcal GV|w
\le
\|w\|_{6/5}
\|\mathcal GV\|_6.
\]

The rotation generator preserves divergence-free vector fields. Moreover curl commutes with the rotation action, hence

\[
\boxed{
\nabla\times(\mathcal GV)
=\mathcal G\Omega.
}
\]

For a divergence-free field in the homogeneous Sobolev class,

\[
\|\mathcal GV\|_6
\le
C_S\|\nabla\mathcal GV\|_2
=C_S\|\mathcal G\Omega\|_2.
\]

Thus

\[
\boxed{
\int|\mathcal GV|w
\le
C_w\|\mathcal G\Omega\|_2,
}
\]

where

\[
C_w:=C_S\|w\|_{6/5}.
\]

Combining with the speed floor gives

\[
\boxed{
|\alpha|\,\|\mathcal G\Omega\|_2
\ge
\delta_{rot}
:=\frac{\delta_{PV}}{C_w}>0.
}
\]

Equivalently, with

\[
A:=\|\mathcal G\Omega\|_2^2,
\]

\[
\boxed{
|\alpha|\sqrt A\ge\delta_{rot}.
}
\]

This is a global vorticity-generator consequence of the local one-slice regularity theorem.

---

## 4. Insert the exact rotation-generator identity

The exact RSS generator identity is

\[
\alpha A
+\frac12I+B=0,
\]

where

\[
I:=\langle D\Omega,\mathcal G\Omega\rangle,
\]

and

\[
B:=\langle\mathcal N_\Omega,\mathcal G\Omega\rangle.
\]

Divide its absolute value by `sqrt(A)`:

\[
|\alpha|\sqrt A
\le
\frac{|I|}{2\sqrt A}
+
\frac{|B|}{\sqrt A}.
\]

The speed floor therefore forces

\[
\boxed{
\frac{|I|}{2\sqrt A}
+
\frac{|B|}{\sqrt A}
\ge
\delta_{rot}.
}
\]

This is the **rotational phase-payment gate**.

A surviving RSS cannot rotate solely as a kinematic label. It must carry a definite amount of either

1. radial-angular phase covariance `I`; or
2. nonlinear angular vorticity transfer `B`.

---

## 5. Quantitative two-branch split

At least one of

\[
\boxed{
|I|
\ge
\delta_{rot}\sqrt A
}
\]

or

\[
\boxed{
|B|
\ge
\frac{\delta_{rot}}{2}\sqrt A
}
\]

must hold, after a harmless redistribution of the factor `1/2` in the first term.

More symmetrically, for any `0<eta<1`, either

\[
\boxed{
|I|
\ge
2\eta\delta_{rot}\sqrt A
}
\]

or

\[
\boxed{
|B|
\ge
(1-\eta)\delta_{rot}\sqrt A.
}
\]

This creates two explicit phase branches rather than one vague intermediate-rotation survivor.

---

## 6. Pure homogeneous passive tail does not pay the I channel at leading order

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

vanishes.

Thus the `I` payment cannot come from a perfectly homogeneous passive critical tail at leading order. It must be supplied by radial modulation of angular phase, the core/tail transition, or the active core itself.

Similarly, the nonlinear tail contribution decays faster than the leading `1/R` velocity tail. Hence the phase-payment gate is naturally concentrated toward finite/transition radii, even though a rigorous localization fraction is not yet proved.

---

## 7. Immediate crude bound and why it is insufficient

Cauchy-Schwarz gives

\[
\frac{|I|}{\sqrt A}
\le
\|D\Omega\|_2,
\]

and

\[
\frac{|B|}{\sqrt A}
\le
\|\mathcal N_\Omega\|_2.
\]

Hence every singular RSS in this class must satisfy

\[
\boxed{
\frac12\|D\Omega\|_2
+\|\mathcal N_\Omega\|_2
\ge
\delta_{rot}.
}
\]

This is valid but not a contradiction: both terms may be order one on a compact active core.

Therefore the next target must exploit **compatibility/sign/localization**, not merely norm size.

---

## 8. Combine with the rotation-dilation discriminant

The preceding discriminant gate gives

\[
B^2+2AC\ge0,
\]

where

\[
C=
-\frac32Z
+\frac12\|D\Omega\|_2^2
+C_N
-\frac\nu2Q.
\]

The present speed floor gives

\[
\left|\frac12I+B\right|
=|\alpha|A
\ge
\delta_{rot}\sqrt A.
\]

Thus a surviving intermediate RSS must satisfy **both**

\[
\boxed{
B^2+2AC\ge0
}
\]

and

\[
\boxed{
\left|\frac12I+B\right|
\ge
\delta_{rot}\sqrt A.
}
\]

with

\[
I^2+2BI-2AC=0.
\]

This is now a closed finite algebraic compatibility system for the four phase scalars

\[
A,I,B,C.
\]

The PDE difficulty has been isolated into estimating which region of this scalar compatibility set is actually realizable by incompressible finite-energy vorticity profiles.

---

## 9. DSD audit

The new formed channels are

- Pineau-Vicol speed threshold `delta_rot`;
- angular activity `A`;
- radial-angular covariance `I`;
- nonlinear angular transfer `B`;
- dilation residual `C`.

The external speed theorem is used only after its Type-I and pressure hypotheses are explicitly assumed.

No conclusion is drawn for general recurrent motion that is not exact RSS.

---

## 10. Updated RSS frontier

The intermediate RSS problem has been sharpened from

\[
\alpha\text{ intermediate}
\]

to the finite phase-geometry requirement

\[
\boxed{
\begin{cases}
I^2+2BI-2AC=0,\\
B^2+2AC\ge0,\\
|\frac12I+B|\ge\delta_{rot}\sqrt A,\\
A>0.
\end{cases}
}
\]

A new closure must show that incompressibility, strain compatibility, Betchov structure, and the critical-tail geometry cannot realize this system in the remaining parameter regime.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
