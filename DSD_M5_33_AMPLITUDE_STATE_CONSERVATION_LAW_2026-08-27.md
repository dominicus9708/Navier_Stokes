# DSD M5-33 — Exact Amplitude-State Conservation Law

Date: 2026-08-27

Status: **DERIVED EXACT CONSERVATION LAW / L2 ENERGY, Lp MOMENTS, THRESHOLD PUMP AND THE CRITICAL ENDPOINT ARE MOMENTS OR BOUNDARIES OF ONE AMPLITUDE-SPACE TRANSPORT / GLOBAL REGULARITY UNPROVED.**

## 1. Superlevel distribution and threshold flux

For a smooth finite-energy Navier--Stokes state `V(z,t)` define

\[
a=|V|,
\]

\[
N(\lambda,t)
:=
|\{z:a(z,t)>\lambda\}|.
\]

Let

\[
E_\lambda(t)
:=
\frac12\int(a^2-\lambda^2)_+dz.
\]

From M5-31--32,

\[
\boxed{
\partial_tE_\lambda
=G(\lambda,t),
}
\]

where

\[
\boxed{
G(\lambda,t)
:=
J_P(\lambda,t)-\nu D_\lambda^{surf}(t).
}
\]

The exact threshold terms are

\[
J_P(\lambda,t)
=
\int_{a=\lambda}\Pi V\cdot n_\lambda\,dS,
\]

and

\[
D_\lambda^{surf}
=
\int_{a>\lambda}|\nabla V|^2dz
+
\lambda\int_{a=\lambda}|\nabla a|dS.
\]

## 2. Derivative in amplitude level

Direct differentiation gives

\[
\boxed{
\partial_\lambda E_\lambda
=-\lambda N(\lambda,t).
}
\]

Define the amplitude-state density

\[
\boxed{
\rho(\lambda,t)
:=
\lambda N(\lambda,t).
}
\]

Then

\[
\rho=-\partial_\lambda E_\lambda.
\]

## 3. Conservation law

Commuting the `t` and `lambda` derivatives,

\[
\partial_t\rho
=-\partial_t\partial_\lambda E_\lambda
=-\partial_\lambda\partial_tE_\lambda.
\]

Using `partial_t E_lambda=G`,

\[
\boxed{
\partial_t\rho(\lambda,t)
+
\partial_\lambda G(\lambda,t)
=0.
}
\]

Thus the pressure-minus-viscous threshold gain is exactly the flux of weighted superlevel mass in amplitude state space.

## 4. Recovery of the kinetic-energy law

Layer cake gives

\[
\int_0^\infty \rho(\lambda,t)d\lambda
=
\int_0^\infty \lambda N(\lambda,t)d\lambda
=
\frac12\|V(t)\|_2^2.
\]

Integrating the conservation law over `lambda` gives

\[
\frac12\frac{d}{dt}\|V\|_2^2
+G(\infty,t)-G(0,t)=0.
\]

At the upper boundary `G(infty)=0`. At the zero-amplitude boundary,

\[
J_P(0)=0,
\qquad
D_0^{surf}=\|\nabla V\|_2^2,
\]

so

\[
G(0,t)=-\nu\|\nabla V\|_2^2.
\]

Hence

\[
\boxed{
\frac12\frac{d}{dt}\|V\|_2^2
+
u\|\nabla V\|_2^2=0.
}
\]

The ordinary energy equality is therefore the zeroth moment of the amplitude-state conservation law.

## 5. Recovery of the Lp hierarchy

For `p>2`,

\[
\int_0^\infty
\lambda^{p-2}\rho(\lambda,t)d\lambda
=
\int_0^\infty
\lambda^{p-1}N(\lambda,t)d\lambda
=
\frac1p\|V(t)\|_p^p.
\]

Multiplying

\[
\rho_t+G_\lambda=0
\]

by `lambda^{p-2}` and integrating by parts yields the corresponding `Lp` balance, with the weighted threshold flux moments reconstructing the pressure and viscous `p`-terms.

In particular, the critical `p=3` balance is the first amplitude moment of the same conservation law.

## 6. DSD compression

The following are now typed as different views of one transport system rather than independent laws:

- kinetic `L2` energy;
- the full `Lp` hierarchy;
- threshold pressure work;
- threshold viscous dissipation;
- the critical `p=3` pressure/dissipation balance;
- the high-amplitude `K` boundary coordinate.

Schematically,

\[
\boxed{
\text{amplitude density }\rho
\xleftrightarrow{\;G\;}
\text{amplitude-state transport}
\Longrightarrow
\begin{cases}
L^2\text{ moment},\\
L^p\text{ moments},\\
K\text{ boundary behavior}.
\end{cases}
}
\]

## 7. Meaning for M5

A large-threshold defect is an amplitude cascade: weighted superlevel mass is transported toward arbitrarily high physical amplitudes through the flux `G`.

The finite-energy law controls only the total zeroth moment. It does not prohibit a progressively thinner amount of amplitude-state mass from moving to larger `lambda`.

Thus M5 can be rephrased as:

\[
\boxed{
\text{Can finite-energy 3D Navier--Stokes sustain a nonvanishing critical amplitude-state flux to arbitrarily large }\lambda?
}
\]

This formulation is exact but does not by itself answer the question.

## 8. Audit lock

Because all threshold levels are part of one conservation law, fixed costs at multiple levels must not be summed as independent sources without tracking the amplitude flux connecting them.

Likewise, a new proof must use information beyond the moment identities already contained in this conservation law--for example geometric restrictions on the flux `G`, compactness in amplitude state space, or a genuine entropy/flux inequality not equivalent to an existing `Lp` moment.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
