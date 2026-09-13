# M19-226 — Adjoint critical-data realization has the same Fredholm compatibility as zero-q kernel exclusion and cannot be assumed as an independent bridge

**Date:** 2026-09-14  
**Status:** ACTIVE AUDIT / FREDHOLM-CIRCULARITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why M19-225 must be audited

M19-225 proves that if a nonzero zero-q primal kernel label B admits a relative-periodic physical adjoint realization with the canonical nondegenerate r^-2 datum C_B, then the Green flux yields

\[
0
=-\frac S2\langle B,C_B\rangle_{S^2},
\]

while

\[
\langle B,C_B\rangle_{S^2}>0.
\]

This is a valid conditional contradiction.

However, one must not simply promote

\[
\text{every prescribed }C_B\text{ has a relative-periodic adjoint realization}
\]

to an independent theorem without checking Fredholm compatibility.

## 2. Abstract periodic operator formulation

Let

\[
\mathcal P_U:=\partial_s-L_U
\]

act on the relative-periodic primal class, with the symmetry quotient understood.

A zero-q unit kernel mode is

\[
\boxed{
W\in\ker\mathcal P_U,
\qquad W\ne0.
}
\]

The formal adjoint periodic operator is

\[
\mathcal P_U^*
=-\partial_s-L_U^*.
\]

Prescribing a nonzero r^-2 adjoint scattering datum C at infinity is not a homogeneous domain condition. It is a boundary/asymptotic forcing condition for the adjoint problem.

## 3. Green identity is exactly the compatibility condition

For any primal kernel W with leading datum B and any adjoint candidate Psi with leading datum C, M19-225 gives

\[
I_R(S)-I_R(0)
=
\int_0^S\mathcal F_R(s)ds.
\]

Relative-periodicity makes the left side zero. Passing R to infinity gives the necessary condition

\[
\boxed{
\langle B,C\rangle_{S^2}=0.
}
\]

Therefore the boundary/asymptotic adjoint problem with prescribed C can only be solvable when C annihilates every primal zero-q kernel datum B.

This is the standard Fredholm-alternative geometry in critical scattering form.

## 4. Canonical dual datum is deliberately incompatible with a nonzero kernel

For a nonzero B, M19-225 chooses C_B so that

\[
\boxed{
\langle B,C_B\rangle_{S^2}>0.
}
\]

Consequently, if the primal kernel actually exists, the relative-periodic adjoint problem with prescribed datum C_B must fail somewhere: at global existence, periodic return, regularity, or the asymptotic class.

Thus

\[
\boxed{
\text{unconditional surjectivity onto }C_B
}
\]

would already contain the desired kernel-exclusion theorem.

It cannot be treated as a free consequence of local adjoint solvability.

## 5. Why M5-217 Carleman does not supply the missing existence

M5-217 uses a linearized Navier--Stokes Carleman estimate to prove unique continuation/injectivity for an already existing Oseen/linearized solution under a terminal-flatness package.

That result has the logical direction

\[
\boxed{
\text{solution + vanishing data on a suitable region}
\Longrightarrow
\text{solution vanishes}.
}
\]

It does not establish

\[
\boxed{
\text{arbitrary prescribed critical adjoint datum at infinity}
\Longrightarrow
\text{global relative-periodic adjoint solution}.
}
\]

Carleman uniqueness is therefore not an adjoint-surjectivity theorem.

## 6. Why M19-131 observability is also insufficient by itself

M19-131 gives a finite-dimensional primal observation operator

\[
\mathcal O_U:E_h(U)\to Y_{spec}
\]

with a uniform lower bound

\[
\|v\|\lesssim\|\mathcal O_Uv\|.
\]

Algebraically, because E_h is finite dimensional, the transpose

\[
\mathcal O_U^*:Y_{spec}^*\to E_h(U)^*
\]

is surjective onto the hard dual.

This certifies that every hard covector can be represented by some spectator/scattering functional.

But it does not imply that the representing functional is the trace at infinity of a **homogeneous global physical adjoint PDE solution** satisfying the required relative-periodic return.

Hence

\[
\boxed{
\text{dual observability/surjectivity in finite-dimensional functional space}
\neq
\text{physical adjoint critical-state realization}.
}
\]

## 7. Correct use of the M19-225 flux

The Green flux remains valuable because it identifies the exact cokernel pairing:

\[
\boxed{
\mathfrak B(B,C)
:=
\langle B,C\rangle_{S^2}.
}
\]

It shows that the zero-q kernel problem is a genuine boundary-Fredholm problem whose primal and adjoint critical exponents are r^-1 and r^-2.

But the next theorem must not merely restate surjectivity against this same pairing.

A noncircular closure would need independent PDE structure that forces one of the following:

1. the relative-periodic adjoint problem is solvable for a specific nonannihilating C for reasons independent of primal kernel-freeness;
2. every primal kernel has zero critical label B, contradicting hard scattering injectivity;
3. the interior PDE imposes a direct sign/current identity on B without first constructing a forbidden adjoint boundary state;
4. the Fredholm index/cokernel is determined independently and excludes the critical boundary obstruction.

## 8. Refined theorem frontier

The previous label T_dual-real is too close to the desired conclusion if stated as arbitrary critical-datum surjectivity.

Replace it by the narrower noncircular target

\[
\boxed{
\mathcal T_{q0}^{noncirc}:
\text{find an independently generated PDE adjoint/current constraint that annihilates no nonzero hard }B.
}
\]

Equivalently, one needs a PDE-selected dual object whose existence is certified without assuming the absence of the very kernel it is meant to exclude.

## 9. Permanent firewall

\[
\boxed{
\text{prescribed nonorthogonal adjoint critical datum is solvable}
\not\text{ an independent consequence of Fredholm theory when a primal kernel may exist}.}
\]

M19-225 is therefore retained as an exact Green-pairing reduction, while M19-226 prevents circular use of its conditional closure statement.

## 10. Next target

The remote spectator scattering map is near identity (M19-069), so its transpose is also near identity and should allow critical dual data to propagate between infinity and a sufficiently remote finite spectator boundary without using the core kernel question.

The next calculation should prove that remote adjoint transport is independently invertible, thereby localizing all remaining obstruction to the finite spectator boundary/interior relative-periodic problem.
