# DSD M19-140 — Pressure resonance generates compatible polyhomogeneous log corrections unless a log-free asymptotic class is independently certified

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / AUTHORITATIVE FIREWALL ON M19-136--139 / A NONZERO ODD PRESSURE RESONANCE DOES NOT BY ITSELF CONTRADICT THE CURRENTLY CERTIFIED CRITICAL SCATTERING CLASS / IT PRODUCES A FASTER-DECAYING POLYHOMOGENEOUS LOG PRESSURE TERM AND A STILL-FURTHER-DECAYING LOG VELOCITY CORRECTION / THE LEADING r^-1 SCATTERING DATUM IS UNAFFECTED / PRESSURE-RESONANCE CONDITIONS BECOME MANDATORY ONLY AFTER AN INDEPENDENT LOG-FREE ASYMPTOTIC THEOREM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Resonant Poisson equation

At pressure level `n`, M19-136 identifies the zero-q resonance

\[
l=2n+1
\]

for a source of size

\[
r^{-(2n+4)}Y_{2n+1}(\omega).
\]

If the resonant source coefficient is nonzero, the ordinary pure-power inversion fails.
The standard resonant particular solution is instead polyhomogeneous:

\[
\boxed{
P_n^{log}
=
c_n\,r^{-(2n+2)}\log r\,Y_{2n+1}(\omega).
}
\]

This is the elliptic analogue of the linear-q secular solution seen in the log-radius coefficient equation.

---

## 2. The logarithmic pressure still decays faster than the leading critical pressure

The leading critical pressure is

\[
P_0^{crit}=O(r^{-2}).
\]

For every `n>=1`,

\[
P_n^{log}
=O(r^{-(2n+2)}\log r),
\]

hence

\[
\boxed{
P_n^{log}=o(r^{-2}).
}
\]

In particular the first nonautomatic resonance gives

\[
\boxed{
P_1^{log}
=O(r^{-4}\log r).
}
\]

Therefore it does not alter the leading critical pressure coefficient used in the M19 scattering factor.

---

## 3. Its pressure gradient is still farther down the velocity hierarchy

Differentiate:

\[
\nabla P_n^{log}
=O(r^{-(2n+3)}\log r).
\]

The next velocity level has exactly the same power:

\[
U_{n+1}\sim r^{-(2n+3)}.
\]

Thus the resonance forces a logarithmic version of the next velocity correction rather than the leading field.

---

## 4. Similarity transport remains invertible on the logarithmic velocity correction

For a pure radial power

\[
r^{-(2n+3)}C,
\]

the similarity dilation operator contributes the nonzero factor

\[
\frac12\left(1-(2n+3)\right)=-(n+1).
\]

For `n>=0`,

\[
\boxed{-(n+1)\ne0.}
\]

Applying the same operator to

\[
r^{-(2n+3)}\log r\,C
\]

produces

1. a nonzero multiple of the logarithmic term;
2. a lower log-degree pure-power term from differentiating `log r`.

The resulting triangular system is invertible because the diagonal coefficient `-(n+1)` is nonzero.

Hence

\[
\boxed{
P_n^{log}
\Longrightarrow
U_{n+1}^{log}
=O(r^{-(2n+3)}\log r)
}
\]

with no return to the leading `r^-1` resonance.

---

## 5. Iteration gives a polyhomogeneous expansion

Further nonlinear interactions of power-log terms may generate higher powers of `log r`, but always at successively faster radial decay.

The natural asymptotic class is therefore potentially

\[
\boxed{
U
\sim
r^{-1}A
+
\sum_{n\ge1}
\sum_{k=0}^{K_n}
 r^{-(2n+1)}(\log r)^kB_{n,k},
}
\]

and similarly for pressure.

This is a standard polyhomogeneous triangular structure: resonance increases log degree but does not move the correction back to the critical leading exponent.

---

## 6. Compatibility with periodic/recurrent similarity profiles

A term such as

\[
r^{-4}\log r\,Y_3
\]

is independent of similarity time when written at fixed spatial point `y`.
It is therefore compatible with time-periodicity of the full similarity profile.

Writing

\[
\log r=q+s/2
\]

may split this same term into a q-linear piece and a time-dependent homogeneous piece, but that decomposition is not itself the physical periodicity criterion.
Only the full pressure field matters.

Thus the linear-q secular coefficient equation does **not** by itself prove failure of DSS/RDSS/recurrent similarity.

---

## 7. Consequence for M19-136--139

The correct status is:

\[
\boxed{
\mathfrak M_{2n+1}[A]\ne0
\Longrightarrow
\text{polyhomogeneous log correction}
}
\]

under the currently certified asymptotic information.

It becomes a contradiction only if an independent theorem proves that the relevant spectator branch admits a genuinely log-free pure-power expansion.

Therefore

\[
\boxed{
\text{pressure-resonance ladder}
\neq
\text{current universal closure mechanism}.
}
\]

M19-139 remains useful because it proves the resonant functional is genuinely nontrivial on mixed-parity low modes, but its nonzero value currently predicts logarithmic correction rather than exclusion.

---

## 8. Updated value of the pressure hierarchy

The pressure-resonance analysis now has three uses:

1. **structure diagnosis:** determine where logs must enter the asymptotic expansion;
2. **parity classification:** odd critical data remain log-free with respect to this resonance ladder;
3. **future rigidity input:** if a stronger analytic theorem later establishes log-free asymptotics, the already-computed resonant moments become immediate algebraic constraints.

For the present M19 closure effort, the primary frontier returns to the finite-dimensional observable neutral dynamics and the nonlinear RSS/RDSS hard core.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
