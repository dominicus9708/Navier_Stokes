# DSD M5-568 — Log-scale scattering datum is the terminal critical trace of the ancient solution

Date: 2026-09-02

Status: **COORDINATE IDENTIFICATION / THE M5-567 SCATTERING INVARIANT `q=LOG |y|-THETA/2` IS EXACTLY `LOG |x|` IN THE PHYSICAL ANCIENT VARIABLES / THE SCALED TAIL PROFILE `|y| U(y,THETA)` IS EXACTLY `|x| u(x,s)` ALONG A FIXED PHYSICAL ANCIENT POSITION / THEREFORE THE PASSIVE TAIL SCATTERING DATUM IS NOT AN ABSTRACT REMOTE DEGREE OF FREEDOM: IT IS THE CRITICAL TERMINAL TRACE `A(LOG|x|,OMEGA)=LIM_{s->0-}|x|u(x,s)` WHEN THAT OFF-ORIGIN TRACE EXISTS / FOR DSS THIS IS A LOG-PERIODIC `1/|x|` TERMINAL PROFILE, THE CLASSICAL BORDERLINE WEAK-`L3` GEOMETRY LEFT OPEN BY GENERAL BACKWARD-DSS THEORY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity and physical ancient coordinates

Recall

\[
a=-s=e^{-\theta},
\qquad
 y=\frac{x}{\sqrt a},
\]

and

\[
U(y,\theta)
=\sqrt a\,u(x,s).
\]

The log-scale scattering coordinate from M5-567 is

\[
\boxed{
q
:=
\log|y|-\frac\theta2.
}
\]

---

## 2. The scattering coordinate is physical log radius

Because

\[
|y|
=\frac{|x|}{\sqrt a}
=e^{\theta/2}|x|,
\]

we have

\[
\log|y|
=\log|x|+\frac\theta2.
\]

Therefore

\[
\boxed{
q=\log|x|.
}
\]

The outward similarity dilation characteristic is simply a trajectory of **fixed physical ancient radius**.

This is the geometric meaning of the M5-563 conveyor.

---

## 3. Critical scaled velocity is also a physical quantity

Multiply the similarity velocity by `|y|`:

\[
|y|U(y,\theta)
=
\frac{|x|}{\sqrt a}
\sqrt a\,u(x,s).
\]

Hence

\[
\boxed{
|y|U(y,\theta)
=|x|u(x,s).
}
\]

Thus the M5-567 characteristic limit

\[
A(q,\omega)
=
\lim_{\tau\to\infty}
R(\tau)U(R(\tau)\omega,\theta+\tau)
\]

is exactly

\[
\boxed{
A(\log|x|,\omega)
=
\lim_{s\uparrow0}
|x|u(x,s)
}
\]

for the corresponding fixed ancient physical point

\[
x=|x|\omega.
\]

---

## 4. Terminal trace interpretation

Whenever the ancient solution has an off-origin terminal trace

\[
u_0(x)
:=
\lim_{s\uparrow0}u(x,s),
\qquad x\ne0,
\]

we therefore have

\[
\boxed{
A(\log|x|,x/|x|)
=|x|u_0(x).
}
\]

Equivalently,

\[
\boxed{
u_0(x)
=
\frac1{|x|}
A\left(\log|x|,\frac x{|x|}\right).
}
\]

Thus the entire passive critical tail scattering datum is simply the terminal critical spatial trace written in logarithmic radial coordinates.

---

## 5. Why the off-origin trace is natural

The selected ancient solution is smooth for every `s<0`.

On branches where the potential terminal singularity is localized at the blow-up center, standard local regularity away from that center gives smooth convergence on compact subsets of

\[
\mathbb R^3\setminus\{0\}
\]

as

\[
s\uparrow0.
\]

On such a branch, the terminal trace `u_0` is an ordinary smooth vector field away from the origin.

Firewall: if the current ancient package has not yet proved isolated terminal singularity, the identity with the **characteristic limit** remains valid, while the phrase `smooth terminal trace` must be restricted to the off-origin regular subbranch.

---

## 6. DSS terminal trace

If the ancient solution is backward `lambda`-DSS,

\[
u(x,t)
=\lambda u(\lambda x,\lambda^2t),
\]

then taking the off-origin terminal limit yields

\[
\boxed{
u_0(x)
=\lambda u_0(\lambda x).
}
\]

Equivalently,

\[
u_0(\lambda x)
=\lambda^{-1}u_0(x).
\]

Therefore

\[
|x|u_0(x)
\]

is periodic in log radius with period

\[
\log\lambda.
\]

This exactly matches M5-566:

\[
\boxed{
u_0(x)
=
\frac1{|x|}
 a\left(
\log|x|,
\frac x{|x|}
\right),
\qquad
a(s+\log\lambda,\omega)=a(s,\omega).
}
\]

---

## 7. Exact self-similar terminal trace

For continuous self-similarity, the same relation holds for every scaling factor.

Then

\[
u_0(\lambda x)=\lambda^{-1}u_0(x)
\qquad\forall\lambda>0,
\]

so `u_0` is exactly homogeneous of degree `-1`.

The corresponding similarity profile is stationary, which M5-565 already excludes in the inherited `L6` class by classical self-similar Liouville theory.

Thus the unresolved terminal trace must be genuinely log-periodic or aperiodic in scale.

---

## 8. Weak-L3 criticality

If the scattering datum is bounded,

\[
|A(q,\omega)|\le C,
\]

then

\[
|u_0(x)|
\le
\frac C{|x|}.
\]

The model `1/|x|` belongs to

\[
L^{3,\infty}(\mathbb R^3)
\]

but not to

\[
L^3(\mathbb R^3).
\]

Therefore the terminal trace lies naturally at the weak-`L3` Type-I endpoint.

This is exactly the critical class in which general backward DSS and Type-I singularity questions remain difficult.

---

## 9. Global L3 in terminal-trace variables

Using

\[
u_0(x)=|x|^{-1}A(\log|x|,\omega),
\]

we obtain

\[
\int|u_0|^3dx
=
\int_{\mathbb R}
\int_{S^2}|A(q,\omega)|^3d\omega\,dq
\]

up to the usual radial coordinate normalization.

Hence

\[
\boxed{
u_0\in L^3
\Longleftrightarrow
A\in L^3(\mathbb R\times S^2).
}
\]

The M5-562 nontrivial invariant component therefore corresponds to a terminal trace whose critical log-radius amplitude is nonintegrable.

---

## 10. Finite enstrophy versus terminal singularity

At every `s<0`, the ancient solution has finite vorticity enstrophy.

The terminal critical trace may nevertheless have

\[
|\nabla u_0(x)|\sim |x|^{-2}
\]

and thus fail to have a finite Dirichlet integral near the singular center.

There is no contradiction: the physical enstrophy can diverge as `s->0-` while remaining finite at each negative time.

Therefore one must not pass the finite-enstrophy bound directly to the terminal trace at the origin.

---

## 11. Conceptual correction to the word `remote`

A shell with very large similarity radius `|y|` at late similarity time does not necessarily represent large physical ancient radius.

Along the dilation characteristic,

\[
|x|
=e^{-\theta/2}|y|
\]

is fixed.

Thus the `remote similarity tail` is simultaneously a record of the terminal physical profile at fixed ancient spatial positions.

The escaping-shell conveyor is the coordinate manifestation of approaching the terminal time while holding physical `x` fixed.

This distinction is essential when interpreting historical replenishment and physical transport.

---

## 12. Revised hard endpoint

The passive-tail endpoint can now be stated without similarity-tail language:

\[
\boxed{
\text{nontrivial Type-I ancient solution}
+
\text{critical terminal trace}
}
\]

with

\[
\boxed{
u_0(x)
=
|x|^{-1}A(\log|x|,x/|x|),
}
\]

where:

- `A` is bounded in the critical branch;
- `A` is non-`L3` in log radius on the nontrivial recurrent component;
- exact self-similar `A=constant in q` is excluded;
- exact DSS gives nonzero log-periodic `A` and remains open for general scaling factor;
- aperiodic recurrence gives an aperiodic critical terminal scale pattern.

---

## 13. Highest-value next target

This identification suggests a different final attack:

> Work directly with the terminal trace `u_0`. Determine which `-1`-critical, log-recurrent terminal traces can actually arise as terminal traces of a smooth finite-enstrophy Type-I ancient Navier--Stokes solution carrying the persistent core/lineage structure.

Useful possible constraints include:

1. local energy inequality across `s=0` away from the center;
2. pressure/head-pressure structure of the critical trace;
3. backward uniqueness after subtracting or localizing the terminal trace;
4. compatibility of the terminal trace with the finite persistent material-flux genealogy.

This may be cleaner than continuing to track infinitely many similarity shells.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
