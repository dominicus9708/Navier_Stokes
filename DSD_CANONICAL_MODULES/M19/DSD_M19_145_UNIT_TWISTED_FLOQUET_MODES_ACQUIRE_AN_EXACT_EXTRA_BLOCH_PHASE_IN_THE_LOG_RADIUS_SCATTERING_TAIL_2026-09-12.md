# DSD M19-145 — Unit twisted Floquet modes acquire an exact extra Bloch phase in the log-radius scattering tail

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE FINITE-DIMENSIONAL ZERO-CENTER PROBLEM IS TRANSFERRED EXACTLY TO THE RDSS TAIL / A TWISTED FLOQUET EIGENMODE WITH UNIT MULTIPLIER mu=exp(i theta) HAS SCATTERING PERTURBATION B(q+L)=mu^-1 Q_*^-1 B(q) / THE LOG-RADIUS BLOCH MISMATCH IS SHIFTED BY THE FLOQUET PHASE / EXTRA ZERO MODES SPLIT INTO UNIT-KERNEL AND NONTRIVIAL-ELLIPTIC PHASE CHANNELS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RDSS background and twisted monodromy

Let the background satisfy

\[
\boxed{
U(s+S)=Q_*U(s),
\qquad
L=S/2.
}
\]

Let

\[
\Phi_S(U)=D\sigma_S(U)
\]

be the linearized time-S map and define the twisted monodromy

\[
\boxed{
\mathcal M_S^{tw}
:=Q_*^{-1}\Phi_S(U).
}
\]

Take a complexified hard eigenmode `v` with

\[
\boxed{
\mathcal M_S^{tw}v
=\mu v,
\qquad
|\mu|=1.
}
\]

Write

\[
\mu=e^{i\vartheta}.
\]

---

## 2. Scattering perturbation

Define

\[
\boxed{
B:=D\mathscr S_Uv.
}
\]

M19-132 gives differentiated time covariance

\[
D\mathscr S_{\sigma_SU}\Phi_Sv
=
T_{-L}B.
\]

Since

\[
\sigma_SU=Q_*U
\]

and scattering is rotation equivariant,

\[
D\mathscr S_{Q_*U}(Q_*w)
=
Q_*D\mathscr S_Uw.
\]

But the twisted eigenvalue equation gives

\[
\Phi_Sv
=Q_*\mu v.
\]

Therefore

\[
T_{-L}B
=
\mu Q_*B.
\]

Equivalently,

\[
\boxed{
B(q+L)
=
\mu^{-1}Q_*^{-1}B(q).
}
\]

This is the exact tail boundary condition for a hard Floquet eigenmode.

---

## 3. Untwist the rotation

Let the principal holonomy angle be

\[
\beta=\operatorname{Angle}(Q_*)\in[-\pi,\pi].
\]

On an azimuthal mode `m`, choose the convention in which

\[
Q_*^{-1}
\quad\text{acts by}\quad
e^{-im\beta}.
\]

Then the scalar coefficient `b(q)` of the perturbation satisfies

\[
\boxed{
 b(q+L)
=
e^{-i(\vartheta+m\beta)}b(q).
}
\]

Hence its allowed log-radius frequencies are

\[
\boxed{
\kappa_{n,m,\vartheta}
=
\frac{2\pi n-m\beta-\vartheta}{L},
\qquad n\in\mathbb Z,
}
\]

up to the fixed sign convention for the azimuthal representation.

For

\[
\vartheta=0,
\]

this reduces to the background RDSS Bloch mismatch of M19-128:

\[
\frac{2\pi n-m\beta}{L}.
\]

---

## 4. Shell derivative cost of a unit Floquet mode

The critical perturbation tail has

\[
W_{tail}
\sim
r^{-1}B(q,\omega).
\]

Its radial derivative contains

\[
\partial_qB-B.
\]

For a Bloch component,

\[
\partial_qB=i\kappa_{n,m,\vartheta}B.
\]

Thus the radial contribution to the shell Dirichlet charge contains

\[
\boxed{
1+
\frac{(2\pi n-m\beta-\vartheta)^2}{L^2}.
}
\]

Including angular derivatives gives the schematic positive mode cost

\[
\boxed{
\mathcal Q_{n,\ell,m,\vartheta}
\gtrsim
1+
\frac{(2\pi n-m\beta-\vartheta)^2}{L^2}
+c_{ang}\ell(\ell+1).
}
\]

---

## 5. Split the zero-center theorem into two spectral channels

The unit-circle hard spectrum now separates naturally.

### A. Kernel channel

\[
\boxed{\mu=1\quad(\vartheta=0).}
\]

This contains the exact time/scale tangent and rotation tangents before quotient.
Any additional unit eigenvector here is an **extra twisted-monodromy kernel mode**.

### B. Elliptic channel

\[
\boxed{\mu=e^{i\vartheta},\qquad \vartheta\not\equiv0\pmod{2\pi}.}
\]

This is a genuinely oscillatory neutral Floquet mode.
Its scattering tail necessarily carries the additional phase mismatch `vartheta/L`.

Thus the live zero-center theorem becomes

\[
\boxed{
\mathcal T_{zero-center}
=
\mathcal T_{kernel}
+
\mathcal T_{elliptic}.
}
\]

---

## 6. Ordinary DSS specialization

For ordinary DSS,

\[
Q_*=I,
\qquad
\beta=0.
\]

Then

\[
\boxed{
\kappa_{n,\vartheta}
=
\frac{2\pi n-\vartheta}{L}.
}
\]

Therefore every nontrivial unit Floquet phase

\[
\vartheta\ne0
\]

forces a nonzero q-Bloch frequency in the scattering perturbation.

The symmetry time tangent corresponds to

\[
\vartheta=0.
\]

---

## 7. What this gains

M19-145 does not eliminate either unit-circle channel.
It gives an exact observable signature:

\[
\boxed{
\text{interior unit Floquet phase}
\Longleftrightarrow
\text{log-radius scattering Bloch phase}.
}
\]

Because M19-131 gives uniform hard-mode observability, no extra unit multiplier can hide entirely in the compact core.

Therefore any future exclusion of unit Floquet phases may be carried out equivalently in the finite-dimensional scattering low-mode representation.

---

## 8. Next useful split

The kernel channel should be tested against:

- augmented orbit nondegeneracy and exact NS symmetries;
- possible stationary/self-similar tail perturbations.

The elliptic channel should be tested against:

- the finite low-mode shell-frequency ceiling;
- pressure/correction resonances;
- whether a nonzero `theta` can survive the one-slice/relative-periodic rigidity constraints.

This is narrower than treating all zero-growth hard directions uniformly.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
