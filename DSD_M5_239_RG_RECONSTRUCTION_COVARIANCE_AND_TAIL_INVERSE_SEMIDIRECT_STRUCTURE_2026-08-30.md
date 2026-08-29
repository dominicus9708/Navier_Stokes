# DSD M5-239 — RG Reconstruction Covariance and Tail-Inverse Semidirect Structure

Date: 2026-08-30

Parent: `DSD_M5_238_MINIMAL_HULL_GLOBAL_RESIDUAL_GAP_AND_STATIONARY_ALL_OR_NONE_2026-08-30.md`

Status: **STRUCTURAL CLOSURE OF THE MAP DIAGRAM / ON THE REALIZED W1 TAIL HULL THE INVERSE OF THE CANONICAL TAIL MAP IS EXACTLY THE `rho=1` VALUE OF THE BACKWARD RG RECONSTRUCTION / SCALE COVARIANCE OF STATIONARY NAVIER--STOKES GIVES AN EXACT TWO-PARAMETER SEMIDIRECT IDENTITY / THE LERAY FLOW IS RECOVERED FROM DILATION PLUS RG RECONSTRUCTION / THIS DOES NOT BY ITSELF EXCLUDE APERIODIC MINIMAL TAILS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Realized reconstruction map

For a realized canonical tail `T=T_V`, M5-237 gives a descendant family

\[
\mathcal D_h[V],
\qquad h\ge0,
\]

with

\[
\mathcal D_h[V]\to T
\quad(h\to\infty).
\]

Set

\[
\rho=e^{-h}\in(0,1].
\]

Define

\[
\boxed{
\mathscr R_\rho(T)
:=
\mathcal D_{-\log\rho}[V].
}
\]

At the tail boundary,

\[
\boxed{
\mathscr R_0(T)=T
}
\]

in the punctured limiting topology.

At `rho=1`,

\[
\boxed{
\mathscr R_1(T)=V.
}
\]

---

## 2. Tail injectivity identifies the inverse map

M5-217 proves

\[
T_V=T_W
\Longrightarrow
V=W.
\]

Thus the realized reconstruction is single valued at `rho=1`.

Since M5-218 makes

\[
\mathfrak T:M\to\mathcal T
\]

a homeomorphism,

\[
\boxed{
\mathscr R_1
=\mathfrak T^{-1}.
}
\]

Therefore the tail-to-core inverse is not an abstract decoder: it is the endpoint of the actual backward-RG reconstruction.

---

## 3. RG equation in `rho`

M5-237 gives

\[
\boxed{
\partial_\rho\mathscr R_\rho(T)
=-\mathcal F(\mathscr R_\rho(T)),
}
\]

where

\[
\mathcal F(U)
=\nu\Delta U-\mathbb P\nabla\cdot(U\otimes U).
\]

This equation is understood on the punctured local class with the inner singular boundary layer supplied by the realized W1 trajectory.

---

## 4. Velocity scaling

For `lambda>0`, define the Navier--Stokes velocity scaling

\[
\boxed{
(S_\lambda U)(x)
:=
\lambda U(\lambda x).
}
\]

The stationary operator has degree three:

\[
\boxed{
\mathcal F(S_\lambda U)
=
\lambda^2 S_\lambda\mathcal F(U).
}
\]

Indeed the right-hand side is

\[
\lambda^3\mathcal F(U)(\lambda x).
\]

The tail dilation `D_tau` corresponds to

\[
\lambda=e^{-\tau/2}.
\]

---

## 5. Exact two-parameter covariance

Let

\[
U(\rho)=\mathscr R_\rho(T).
\]

Define

\[
\widetilde U(\rho)
:=
S_\lambda U(\lambda^2\rho).
\]

Then

\[
\partial_\rho\widetilde U
=
\lambda^2S_\lambda\partial_\rho U(\lambda^2\rho)
=
-\lambda^2S_\lambda\mathcal F(U)
=
-\mathcal F(\widetilde U).
\]

At `rho=0`,

\[
\widetilde U(0)=S_\lambda T.
\]

By realized reconstruction uniqueness,

\[
\boxed{
\mathscr R_\rho(S_\lambda T)
=
S_\lambda\mathscr R_{\lambda^2\rho}(T).
}
\]

Using `lambda=e^{-tau/2}`:

\[
\boxed{
\mathscr R_\rho(D_\tau T)
=
D_\tau
\mathscr R_{e^{-\tau}\rho}(T).
}
\]

This is the exact semidirect covariance relation.

---

## 6. Recover the W1 Leray flow

Set `rho=1`:

\[
\mathscr R_1(D_\tau T)
=
D_\tau\mathscr R_{e^{-\tau}}(T).
\]

The left side is

\[
\mathfrak T^{-1}(D_\tau T).
\]

By tail conjugacy this is precisely

\[
S(\tau)V.
\]

Therefore

\[
\boxed{
S(\tau)V
=
D_\tau\mathscr R_{e^{-\tau}}(T_V).
}
\]

So Leray time evolution is reconstructed by:

1. move inward along the RG reconstruction from `rho=1` to `rho=e^{-tau}`;
2. apply the compensating spatial dilation `D_tau`.

---

## 7. Infinitesimal compatibility

Let

\[
\mathcal G(U)
:=-\frac12(U+x\cdot\nabla U)
\]

be the infinitesimal dilation generator.

Scale covariance of `F` gives

\[
\mathcal F(D_\tau U)
=
e^{-\tau}D_\tau\mathcal F(U).
\]

Differentiate at `tau=0`:

\[
\boxed{
D\mathcal F_U[\mathcal G(U)]
=
\mathcal G(\mathcal F(U))
-\mathcal F(U).
}
\]

Equivalently, in Lie-bracket notation,

\[
\boxed{
[\mathcal G,\mathcal F]
=\mathcal F.
}
\]

This is the infinitesimal form of the semidirect scaling law.

---

## 8. Why this does not contradict recurrence

The residual `F(T)` has physical degree `-3`, while `T` has degree `-1`.

Writing

\[
F_T(r\theta)=r^{-3}\mathcal R_T(y,\theta),
\]

the normalized residual coefficient obeys only translation under tail dilation:

\[
\mathcal R_{D_\tau T}(y,\theta)
=
\mathcal R_T(y-\tau/2,\theta).
\]

Thus the apparent exponential factor in the velocity-space covariance is exactly canceled by the change of physical degree after critical normalization.

Hence compact recurrent residual profiles are compatible with the semidirect law.

The bracket identity is structure, not a contradiction.

---

## 9. Realized-range formulation

Define the realized RG range

\[
\boxed{
\mathfrak R_{W1}
:=
\left\{
T:\
\mathscr R_\rho(T)
\text{ exists for }0<\rho\le1
\text{ with the W1 regularity/compactness package}
\right\}.
}
\]

Then

\[
\mathcal T\subset\mathfrak R_{W1}.
\]

The semidirect covariance gives

\[
\boxed{
D_\tau\mathfrak R_{W1}
\subset\mathfrak R_{W1}
}
\]

on the realized complete corridor.

The residual-active endgame is therefore:

\[
\boxed{
\text{classify compact minimal dilation subsets of }
\mathfrak R_{W1}
\text{ with }\mathbf F\ge\varepsilon_{glob}>0.
}
\]

---

## 10. DSD verdict

### PROVED

- `R_1` equals the inverse canonical-tail map;
- exact two-parameter RG/dilation covariance;
- exact reconstruction formula for the W1 Leray flow;
- infinitesimal commutator `[G,F]=F`.

### NOT PROVED

The semidirect structure alone does not exclude periodic, quasiperiodic, or more general aperiodic minimal normalized residual profiles.

### NEXT TARGET

Derive the triangular `rho`-jet recursion at `rho=0` and audit whether realized W1 reconstruction supplies convergence/quasi-analytic control of that jet.  The crucial distinction is again:

\[
\text{all finite RG jets determined}
\quad\not\Rightarrow\quad
\text{convergent RG Taylor series}.
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]