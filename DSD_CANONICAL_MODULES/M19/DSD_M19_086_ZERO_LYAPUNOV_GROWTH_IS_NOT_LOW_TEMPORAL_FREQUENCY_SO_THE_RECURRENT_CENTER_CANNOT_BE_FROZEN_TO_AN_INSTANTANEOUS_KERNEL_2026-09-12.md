# DSD M19-086 — Zero Lyapunov growth is not low temporal frequency, so the recurrent center cannot be frozen to an instantaneous kernel

Date: 2026-09-12

Status: **SPECTRAL-VARIABLE CORRECTION / A ZERO OR NEAR-ZERO LYAPUNOV-SACKER--SELL GROWTH RATE IS A STATEMENT ABOUT LONG-TIME NORM GROWTH, NOT ABOUT SMALL TEMPORAL OSCILLATION FREQUENCY OR SMALL TIME DERIVATIVE / A BOUNDED CENTER SOLUTION MAY ROTATE OR OSCILLATE AT ORDER-ONE SPEED WHILE ITS NORM HAS EXACTLY ZERO EXPONENT / THEREFORE THE PROPOSED LAMBDA->0 FREEZING OF THE RECURRENT BACKGROUND TO AN INSTANTANEOUS KERNEL IS INVALID WITHOUT AN ADDITIONAL REDUCIBILITY/ADIABATIC HYPOTHESIS / THE CORRECT ZERO-CENTER OBJECT IS AN AVERAGED SYMMETRIC-PART BALANCE, RETURNING TO THE STRAIN-SUPPORTED NEUTRALIZATION CONDITION OF M19-079 / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two different spectral notions must be separated

There are two quantities that can both be informally called a frequency or spectral parameter but have different meanings.

### Temporal oscillation frequency

For an autonomous or reducible system one may have a mode

\[
W(\theta)=e^{i\omega\theta}\Phi.
\]

Then \(\omega\) measures oscillation speed and

\[
\|\partial_\theta W\|=|\omega|\|W\|.
\]

### Lyapunov growth exponent

For a general nonautonomous recurrent cocycle,

\[
\boxed{
\lambda(W)
:=
\limsup_{T\to\infty}
\frac1T\log\|W(T)\|
}
\]

measures exponential norm growth.

The center condition is

\[
\boxed{\lambda(W)=0,}
\]

not \(\omega=0\).

---

## 2. Elementary counterexample

Let

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]

and consider

\[
\boxed{x'=Jx.}
\]

Then

\[
|x(t)|=|x(0)|
\]

for all \(t\), so every nonzero solution has

\[
\boxed{\lambda=0.}
\]

But

\[
|x'|=|x|
\]

and the solution rotates with order-one temporal frequency.

Thus

\[
\boxed{
\lambda=0
\not\Rightarrow
\partial_t x\approx0.
}
\]

---

## 3. Recurrent skew systems make the same point

More generally, if

\[
x'=A(t)x,
\qquad A(t)^T=-A(t),
\]

with recurrent bounded \(A(t)\), then the evolution is orthogonal:

\[
|x(t)|=|x(0)|.
\]

All Lyapunov exponents are zero even though \(A(t)\) and \(x'(t)\) may vary rapidly and aperiodically.

Therefore a recurrent zero-growth bundle can have nontrivial internal phase dynamics.

This is exactly the type of phenomenon that a center/factor theorem must control rather than freeze away.

---

## 4. Why the frozen-operator limit is invalid

Suppose a sequence of cocycle directions has

\[
\lambda_n\to0.
\]

It does **not** follow that

\[
\|\partial_\theta W_n\|\to0.
\]

Hence one cannot pass formally from

\[
\partial_\theta W_n=L(\theta)W_n
\]

to

\[
L(\theta_*)W_*=0
\]

by selecting a recurrent phase \(\theta_*\).

The time-dependent background continues to rotate and deform the center direction at order-one speed.

A frozen kernel becomes relevant only under an extra hypothesis such as:

1. an autonomous stationary background;
2. exact periodic/Floquet reducibility with a controlled Floquet exponent;
3. an adiabatic regime with \(\|W_\theta\|\to0\);
4. a proven conjugacy to a constant-coefficient center system.

None is currently certified for the aperiodic recurrent branch.

---

## 5. Correction to the interpretation of M19-085

M19-085 correctly proves a **boundary-local temporal-frequency** statement:

\[
\text{large actual time derivative / high temporal harmonic}
\Rightarrow
\text{large parabolic graph norm or derivative/pressure exit}.
\]

But the final sentence must not be read as identifying the Sacker--Sell/Lyapunov center variable with temporal frequency.

The genuine unresolved object is not simply

\[
\omega\to0.
\]

It is

\[
\boxed{
\text{zero real growth rate with potentially order-one internal oscillation}.
}
\]

This is the corrected spectral firewall.

---

## 6. Logarithmic norm identity

Let

\[
E_w(\theta)=\|W(\theta)\|_w^2.
\]

Whenever \(E_w>0\),

\[
\boxed{
\frac12\frac{d}{d\theta}\log E_w
=
\frac{\langle W,L_s(\theta)W\rangle_w}{\langle W,W\rangle_w},
}
\]

where

\[
L_s:=\frac12(L+L^\dagger)
\]

is the weighted symmetric part.

The skew part of the cocycle rotates phase/direction but contributes nothing directly to the norm growth.

Thus a zero Lyapunov exponent means that along the normalized projective direction

\[
e(\theta)=W/\|W\|_w,
\]

the long-time average satisfies

\[
\boxed{
\left\langle
\langle e,L_s(\theta)e\rangle_w
\right\rangle=0
}
\]

along the corresponding averaging subsequence.

This is the correct center condition.

---

## 7. Return to M19-079 neutralization

The symmetric-part identity is exactly what M19-079 computed in PDE variables:

\[
\text{OU/viscous damping}
=
\text{transport/pressure weight work}
+
\text{strain-supported work}
\]

on long-time average for a bounded complete center witness.

Therefore M19-086 does not open a frozen-kernel shortcut.

It confirms that the central obstacle is the averaged symmetric-part balance.

Symbolically,

\[
\boxed{
\lambda=0
\Longleftrightarrow
\text{persistent neutralization of the negative symmetric part by recurrent strain/work},
}
\]

not

\[
\lambda=0
\Longleftrightarrow
L(\theta_*)W=0.
\]

---

## 8. Projective center dynamics

Normalize

\[
e(\theta)=W(\theta)/\|W(\theta)\|_w.
\]

Then schematically

\[
\boxed{
e'
=
L(\theta)e
-\langle e,L_s(\theta)e\rangle_w e.
}
\]

The projective direction can therefore move nontrivially even when the scalar growth rate averages to zero.

Aperiodic center dynamics may live precisely in this projective equation.

Thus the center/factor problem is partly a projective-cocycle rigidity problem.

---

## 9. What theorem would now suffice

A sufficient statement would be a strict transverse logarithmic-norm gap:

\[
\boxed{
\limsup_{T\to\infty}
\frac1T
\int_0^T
\langle e(\theta),L_s(\theta)e(\theta)\rangle_wd\theta
<0
}
\]

for every normalized rotation-transverse projective trajectory not generated by the time tangent.

This directly excludes every extra zero Lyapunov direction regardless of its temporal oscillation frequency.

This is stronger and more appropriate than a frozen-kernel theorem.

---

## 10. Certified conclusion

\[
\boxed{
\text{zero Lyapunov exponent}
\neq
\text{zero temporal frequency}
\neq
\text{instantaneous kernel mode}.
}

The current analytic frontier is therefore an averaged/projective coercivity problem, not a small-frequency perturbation of a frozen operator.

---

## 11. Next calculation

M19-087 should study the projective equation directly and ask whether recurrence plus the radial-A2 symmetric-part structure can produce a strict gap **away from the finite-dimensional symmetry bundle**.

A useful object is the instantaneous Rayleigh quotient

\[
\mathfrak r(\theta,e)
:=
\langle e,L_s(\theta)e\rangle_w.
\]

The next audit should determine whether compactness of the recurrent hull and of the symmetry-transverse unit sphere in an appropriate local topology can turn pointwise negativity of \(\mathfrak r\) into a uniform negative gap, or whether radial escape destroys exactly that compactness.
