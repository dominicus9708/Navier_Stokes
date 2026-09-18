# M19-440 — Authoritative correction: the terminal Hardy-excess payer fork collapses by exact convection and pressure coboundary cancellation to the viscous Dirichlet identity

Date: 2026-09-19  
Canonical ID: **M19-440**  
Status: **MAJOR AUDIT CORRECTION / THE M19-423 HARDY-EXCESS IDENTITY IS EXACT BUT ITS BERNOULLI-VERSUS-RESIDUAL INTERPRETATION OVERCOUNTS CONSERVATIVE TRANSPORT / THE ENTIRE KINETIC CONVECTION TERM AND THE ENTIRE PRESSURE TERM EACH FORM AN EXACT q-COBOUNDARY WITH THEIR MATCHING RADIAL ENERGY-FLUX TERMS / AFTER INVARIANT AVERAGING THE HARDY EXCESS REDUCES IDENTICALLY TO THE VISCOUS DIRICHLET FORM / M19-424--429 STRUCTURAL SUBCALCULATIONS REMAIN CONDITIONALLY VALID BUT MUST NOT BE COUNTED AS AN INDEPENDENT TERMINAL PAYER TREE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Identity being audited

M19-423 writes

\[
\boxed{
\mathcal H_A
=
\langle\Gamma_B\rangle
+
\left\langle
\int A\cdot C
\right\rangle,
}
\]

where

\[
\mathcal H_A
=
\left\langle
\|A_q\|_2^2
+
\|\nabla_{S^2}A\|_2^2
\right\rangle,
\]

and

\[
\Gamma_B
=
\Gamma_K+\Gamma_P,
\]

with

\[
\Gamma_K
=
\int_{S^2}
\frac12|A|^2A_r,d\omega,
\]

\[
\Gamma_P
=
\int_{S^2}
P A_r,d\omega.
\]

The identity itself is correct.

The issue is whether the two terms on the right are independent payers.

They are not.

## 2. Decompose the stationary residual

Write

\[
\boxed{
C
=
C_{vis}
+
C_{conv}
+
C_{pres},
}
\]

where

\[
C_{vis}
=
-\mathcal L_1A,
\]

\[
C_{conv}
=
\mathfrak N(A,A),
\]

and

\[
C_{pres}
=
\mathfrak G_2P.
\]

Then

\[
\int A\cdot C
=
I_{vis}+I_{conv}+I_{pres}.
\]

## 3. Exact convection coboundary

Let

\[
E
=
\frac12|A|^2.
\]

In physical variables,

\[
v=r^{-1}A
\]

and

\[
v\cdot(v\cdot\nabla)v
=
v\cdot\nabla
\left(
\frac12|v|^2
\right).
\]

Because \(\nabla\cdot v=0\),

\[
v\cdot(v\cdot\nabla)v
=
\nabla\cdot
\left[
\frac12|v|^2v
\right].
\]

Now

\[
\frac12|v|^2v
=
r^{-3}EA.
\]

For a degree-minus-three vector flux,

\[
\nabla\cdot(r^{-3}EA)
=
r^{-4}
\left[
(\partial_q-1)(EA_r)
+
\operatorname{div}_{S^2}(EA_T)
\right].
\]

Integrating over the sphere kills the angular divergence.

Therefore the normalized nonlinear work is

\[
\boxed{
I_{conv}(q)
:=
\int_{S^2}
A\cdot C_{conv},d\omega
=
\Gamma_K'(q)
-
\Gamma_K(q).
}
\]

Hence

\[
\boxed{
\Gamma_K+I_{conv}
=
\Gamma_K'.
}
\]

The kinetic Bernoulli flux and nonlinear residual work are one conservative transport pair.

## 4. Exact pressure coboundary

Similarly,

\[
v\cdot\nabla p
=
\nabla\cdot(pv)
\]

because \(\nabla\cdot v=0\).

Since

\[
pv
=
r^{-3}PA,
\]

the same homogeneous divergence formula gives

\[
\boxed{
I_{pres}(q)
:=
\int_{S^2}
A\cdot C_{pres},d\omega
=
\Gamma_P'(q)
-
\Gamma_P(q).
}
\]

Thus

\[
\boxed{
\Gamma_P+I_{pres}
=
\Gamma_P'.
}
\]

M19-436's harmonic-dipole cancellation is the \(l=1\) special case of this general pressure identity.

## 5. Both conservative pairs vanish in invariant mean

On the compact recurrent terminal hull,

\[
\Gamma_K,
\Gamma_P
\]

are bounded observables.

Therefore

\[
\boxed{
\langle\Gamma_K'\rangle
=
0,
\qquad
\langle\Gamma_P'\rangle
=
0.
}
\]

Hence

\[
\boxed{
\langle\Gamma_K\rangle
+
\langle I_{conv}\rangle
=
0,
}
\]

and

\[
\boxed{
\langle\Gamma_P\rangle
+
\langle I_{pres}\rangle
=
0.
}
\]

Neither kinetic Bernoulli sorting nor pressure sorting is an independent invariant-mean energy payer.

## 6. The viscous term is exactly the Hardy excess

The viscous normalized residual is

\[
C_{vis}
=
-
\left[
(\partial_q-1)\partial_q
+
\Delta_{S^2}
\right]A.
\]

Pair with A and take the invariant mean.

Integration by parts in q and on the sphere gives

\[
\boxed{
\left\langle
\int A\cdot C_{vis}
\right\rangle
=
\left\langle
\|A_q\|_2^2
+
\|\nabla_{S^2}A\|_2^2
\right\rangle
=
\mathcal H_A.
}
\]

Therefore after the conservative terms cancel,

\[
\boxed{
\mathcal H_A
=
\left\langle
\int A\cdot C_{vis}
\right\rangle.
}
\]

This is simply the viscous Dirichlet identity.

## 7. Full reconstruction of the M5-575 energy identity

M5-575 gives

\[
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\left\langle
\int A\cdot C
\right\rangle.
\]

Write

\[
K
=
\int_{S^2}
\frac12|A|^2d\omega.
\]

Then

\[
\Phi_E
=
\Gamma_K
+
\Gamma_P
-
K'
+
2K.
\]

Also

\[
\langle\mathcal D_A\rangle
=
\mathcal H_A
+
2\langle K\rangle.
\]

Substitute the residual decomposition.

The q-derivative of K averages to zero, and Sections 3--5 cancel the kinetic and pressure pairs.

The identity reduces to

\[
\mathcal H_A
+
2\langle K\rangle
=
2\langle K\rangle
+
\mathcal H_A.
\]

Thus the invariant terminal energy ledger closes identically.

## 8. Consequence for M19-423

M19-423's equation

\[
\mathcal H_A
=
\langle\Gamma_B\rangle
+
\langle A\cdot C\rangle
\]

is mathematically correct.

But the interpretation

\[
\mathcal H_A
\Longrightarrow
\text{Bernoulli sorting}
\lor
\text{residual slope}
\]

is not a new structural dichotomy.

The two quantities contain equal-and-opposite pieces of the same conservative convection/pressure transport.

Therefore

\[
\boxed{
\text{M19-423 payer fork}
\text{ is demoted from proof-tree root to an exact transport decomposition.}
}
\]

## 9. Consequence for M19-424--425

M19-424's explicit BRC/parity witness remains a valid geometric example.

M19-425's statements

- kinetic sorting implies radial-amplitude/strain structure;
- pressure sorting implies pressure-gradient structure;

remain valid **conditional implications**.

But neither sorting branch is forced as an independent invariant terminal payment after the conservative cancellation is respected.

In particular,

\[
\boxed{
P_{tan}^{critical}
}
\]

must not remain in the master proof tree merely because \(\Gamma_P\) is large.

A large pressure flux may be exactly canceled by pressure residual work.

## 10. Consequence for M19-429

M19-429 proposed the master terminal fork

\[
R_{slope}^{finite-depth}
\lor
S_{rr}^{critical}
\lor
P_{tan}^{critical}.
\]

That fork relied on the independent-payer interpretation of M19-423.

After M19-440, it is not authoritative.

The geometric calculations inside those branches remain available if their hypotheses arise from an independent argument.

But the terminal energy identity alone does not force that trichotomy.

## 11. What remains genuinely nontrivial

The mandatory information established before M19-423 remains intact:

- M19-412 closes the realized stationary terminal branch;
- M19-413 gives the uniform global stationary-residual gap;
- M19-417 gives syndetic recurrence of a fixed residual channel;
- M19-418 reduces force activity to mandatory mean-free angular first-jet activity;
- M19-414 shows direct unsigned raw-H2 accumulation of that angular residual remains critically summable.

Thus the live nontrivial object is still

\[
\boxed{
C^\perp
\text{ with syndetic angular activity},
}
\]

not the Hardy-excess flux split.

## 12. Corrected next direction

The next calculation must return to the **structure of the first residual itself** and avoid decompositions that are merely conservative energy transport.

Useful candidates are:

1. curl of C, where pressure disappears;
2. divergence/Hodge constraints on C;
3. coupling of C to the wedge vorticity equation;
4. a signed moment not expressible as a divergence/coboundary;
5. a noncritical observability gain.

The M19-433--439 pressure-harmonic firewalls remain relevant specifically when trying to infer C from curl at finite depth.

\[
\boxed{\text{M19-440 COMPLETE; THE TERMINAL HARDY-EXCESS PAYER TREE COLLAPSES TO A VISCOUS TAUTOLOGY AFTER EXACT CONSERVATIVE CANCELLATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
