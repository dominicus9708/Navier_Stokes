# M19-213 — Cayley–Pfaffian coordinate desquares orthogonal unit-kernel crossings and recovers the skew crossing form

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / LOCAL SPECTRAL-ORIENTATION REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Even-dimensional oriented quotient and Cayley chart

Work on a certified oriented symmetry-quotient hard fiber of real dimension

\[
N=2m,
\]

with relative return

\[
P\in SO(2m).
\]

Assume first that

\[
-1\notin\sigma(P),
\]

so that \(I+P\) is invertible. Define the Cayley transform

\[
\boxed{
\mathcal C(P):=(I-P)(I+P)^{-1}.
}
\]

Because \(P^TP=I\),

\[
\mathcal C(P)^T=-\mathcal C(P).
\]

Thus the relative return is represented in this chart by a real skew-symmetric operator.

## 2. Unit kernels become zeros of the skew Cayley operator

Since \(I+P\) is invertible,

\[
\boxed{
\ker\mathcal C(P)=\ker(I-P).
}
\]

Therefore the nonsymmetry \(+1\) kernel problem is exactly the singularity problem for a finite skew matrix.

On the oriented \(2m\)-dimensional quotient define the Pfaffian scalar

\[
\boxed{
\mathfrak p(P):=\operatorname{Pf}\mathcal C(P).
}
\]

Then

\[
\det\mathcal C(P)=\mathfrak p(P)^2,
\]

and hence

\[
\boxed{
\mathfrak p(P)=0
\iff
\ker(I-P)\ne\{0\}
}
\]

inside the \(-1\)-free Cayley chart.

Thus the Pfaffian is the natural scalar square root of the determinant defect that was invisible in M19-211.

## 3. Exact block formula

For the standard real rotation block

\[
R(\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},
\]

let

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

A direct calculation gives

\[
\boxed{
\mathcal C(R(\theta))
=-\tan\frac\theta2\,J.
}
\]

With the oriented convention

\[
\operatorname{Pf}
\begin{pmatrix}
0&a\\
-a&0
\end{pmatrix}=a,
\]

one obtains

\[
\boxed{
\operatorname{Pf}\mathcal C(R(\theta))
=\tan\frac\theta2.
}
\]

Therefore, after oriented block decomposition and away from \(-1\),

\[
\boxed{
\mathfrak p(P)
=\prod_{j=1}^{m}\tan\frac{\theta_j}{2}
}
\]

up to the fixed orientation convention of the quotient fiber.

A \(+1\) resonance is \(\theta_j\in2\pi\mathbb Z\), so it is a first-order zero of the corresponding Pfaffian factor rather than a quadratic zero.

## 4. Determinant factorization explains the M19-211 no-go

Since

\[
I-P=\mathcal C(P)(I+P),
\]

we have

\[
\boxed{
\det(I-P)
=\det(I+P)\,\mathfrak p(P)^2.
}
\]

In a \(-1\)-free orthogonal chart,

\[
\det(I+P)>0.
\]

Hence the nonnegative determinant of M19-211 is precisely a positive factor times the **square** of the signed Pfaffian coordinate.

This identifies the structural reason determinant sign cannot see a paired \(+1\) crossing.

## 5. Relation to the M19-212 skew crossing form

Let

\[
P(\lambda)\in SO(2m)
\]

be \(C^1\), and suppose \(\lambda_0\) is a unit-kernel point with

\[
K=\ker(I-P_0),
\qquad
\dim K=2r.
\]

Assume \(-1\notin\sigma(P_0)\). M19-212 defines

\[
B_K=\Pi_KP_0^T\dot P_0|_K.
\]

Since \(P_0=I\) on \(K\), differentiating the Cayley transform and restricting to \(K\) gives

\[
\boxed{
\Pi_K\dot{\mathcal C}(P_0)|_K
=-\frac12 B_K.
}
\]

Therefore, if the crossing form is nondegenerate on \(K\), the Pfaffian has leading behavior

\[
\boxed{
\mathfrak p(P(\lambda))
=c_0\,
\operatorname{Pf}\!\left(-\frac12B_K\right)
(\lambda-\lambda_0)^r
+o(|\lambda-\lambda_0|^r),
}
\]

where \(c_0\ne0\) is the Pfaffian contribution of the nonresonant complement in the chosen local oriented trivialization.

For the minimal two-dimensional kernel \(r=1\), with

\[
B_K=
\begin{pmatrix}
0&-\beta\\
\beta&0
\end{pmatrix},
\]

we get

\[
\boxed{
\mathfrak p(P(\lambda))
\sim c_0\frac{\beta}{2}(\lambda-\lambda_0)
}
\]

up to the fixed block-orientation convention.

Thus the Pfaffian changes sign across a transversal two-dimensional kernel crossing, exactly recovering the nonzero skew crossing coefficient of M19-212.

## 6. What the Pfaffian repairs — and what it does not

The Cayley–Pfaffian coordinate repairs one specific defect:

\[
\boxed{
\det(I-P)\text{ sees }\beta^2,
\qquad
\operatorname{Pf}\mathcal C(P)\text{ sees }\beta.
}
\]

However this is still only a **local spectral-orientation coordinate**.

Three global obstructions remain:

1. the Cayley chart is singular when \(-1\in\sigma(P)\);
2. the Pfaffian sign can be compared globally only after an oriented trivialization of the relevant even-dimensional hard bundle;
3. a sign-changing Pfaffian detects a crossing but does not prove that no crossing occurs in the admissible moderate parameter set.

Hence

\[
\boxed{
\text{Pfaffian crossing detector}
\neq
\text{kernel exclusion theorem}.
}
\]

## 7. Revised next target

The determinant-sign no-go of M19-211 is not the end of the topological route. The correct local scalar is the Cayley Pfaffian.

To turn it into a global rigidity theorem one must additionally establish at least one of:

- a global \(-1\)-free spectral chart plus fixed quotient orientation and Pfaffian sign trapping;
- a global phase lift whose image avoids \(2\pi\mathbb Z\);
- a profile-specific PDE identity fixing the sign/nonvanishing of the skew crossing form.

The bounded-period branch remains OPEN.