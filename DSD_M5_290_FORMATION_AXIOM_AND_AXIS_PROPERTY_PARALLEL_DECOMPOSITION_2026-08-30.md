# DSD M5-290 — Formation-Axiom and Axis-Property Parallel Decomposition of the Remaining Frontier

Date: 2026-08-30

Status: **PARALLEL ANALYSIS LAYER / FORMATION-AXIOM AND AXIS-PROPERTY SYSTEMS ARE USED ONLY TO DECOMPOSE THE PROBLEM, NOT AS PROOF RULES / STANDARD NAVIER–STOKES MATHEMATICS REMAINS THE ONLY CLOSURE MECHANISM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose and firewall

The current post-Liouville frontier has been reduced to dynamic turnover and remote satellite behavior.  Until now these branches were organized mainly by the DSD audit tree.

This note introduces two independent descriptive layers:

1. **Formation-Axiom decomposition**: identify what the mathematical object is, which data are inherited, which data are lost under rescaling/recentering, and which apparent branches are merely different descriptions of the same underlying object.
2. **Axis-Property decomposition**: split the directional action of strain, vorticity, radial separation, transport, and pressure into longitudinal, rotational, and transverse sectors.

Neither layer is accepted as a new theorem system for Navier–Stokes.  Every closure statement must still be proved by ordinary PDE analysis.

The logical pipeline is therefore

\[
\boxed{
\text{Formation / Axis decomposition}
\to
\text{standard PDE calculation}
\to
\text{DSD audit}.
}
\]

---

## 2. Formation descriptor for one satellite

A remote satellite is not adequately described only by the vorticity amplitude.  Introduce the minimal local descriptor

\[
\boxed{
\mathscr S
=
(x,t,\ell,d,a,L,\Theta,\chi;
\omega,S,p;\mathcal I)
}
\]

where

\[
\ell=|\omega(x,t)|^{-1/2},
\qquad
 d=|x-X_{core}(t)|,
\]

\[
L=\frac d\ell,
\qquad
\Theta=\frac{a}{\ell^2}=a|\omega(x,t)|,
\qquad
\chi=\frac a{d^2}=\frac{\Theta}{L^2},
\]

and `a=T^*-t` when a common terminal time is available.  The symbol `I` denotes inherited information from the original finite-energy first-hitting solution.

The previously derived remote-satellite condition is

\[
\boxed{L\to\infty.}
\]

The local Type-I/Type-II clock is

\[
\boxed{\Theta=(T^*-t)|\omega(x,t)|.}
\]

---

## 3. Inherited, lost, and newly free data

Under satellite point-picking and recentering the following information is robustly inherited on fixed compact cylinders:

- Navier–Stokes equation;
- divergence-free condition;
- local suitable/smooth structure after compactness;
- normalized nontrivial vorticity witness;
- local vorticity cap from the point-picking lemma;
- any ambient-strain bound explicitly assumed in the compactness lane.

Information that is **not** automatically inherited globally includes

- a uniform global weak-`L3` velocity norm;
- the original main-core center;
- the original canonical far tail;
- global kinetic energy after the satellite normalization;
- expanding-window control;
- coherent restart with one fixed critical datum norm.

This loss is precisely why the detached satellite cannot yet be passed directly to the Albritton–Barker Liouville theorem.

A new apparent freedom also enters after recentering: a curl-free/divergence-free harmonic or affine component.  The exact solid-rotation anti-model shows that bounded nonzero vorticity alone does not eliminate this freedom.

---

## 4. Formation correction: `S_iso` and `S_amp` are not different local objects

The earlier frontier distinguished

\[
S_{iso}
\quad\text{and}\quad
S_{amp}.
\]

Formation analysis shows that this is not an ontological split of local Navier–Stokes profiles.

Both branches are built from the same local satellite descriptor `S`.

The distinction appears only after introducing an **ensemble / packing descriptor** over a family of satellites:

\[
\boxed{
\mathscr P
=
\{\mathscr S_i\}_{i\in I}
+
(\text{multiplicity},\text{persistence},\text{space-time overlap}).
}
\]

For the Seregin Type-II scenario the relevant collective observable is schematically

\[
\boxed{
\Pi_{pack}:=g(\ell)M_\kappa^{s,l}.
}
\]

Thus

\[
\boxed{
S_{amp}
=
\{\text{the same satellite family with }\Pi_{pack}\ge\varepsilon_0\},
}
\]

whereas

\[
\boxed{
S_{iso/sparse}
=
\{\Pi_{pack}<\varepsilon_0\text{ along the relevant scales}\}.
}
\]

This removes one unnecessary conceptual branch.

The current frontier is better written as

\[
\boxed{
\text{singular tower}
\Longrightarrow
T_{dynamic}
\lor
\mathscr P_{satellite}.
}
\]

The satellite family is then tested by `Pi_pack` rather than split into two different solution classes from the outset.

---

## 5. Formation decomposition of dynamic turnover

The label `T_dynamic` also contains several mechanisms that should not be conflated.

Formation analysis separates changes of the **physical structure** from changes only in its **description**.

### 5.1 Physical replacement

The material/vorticity packet itself changes identity, support, or ancestry.

Examples:

- genuine material crossing of the shell boundary;
- packet destruction and rebuilding;
- transfer to a disjoint coherent packet;
- irreversible loss of the tracked vorticity lineage.

### 5.2 Center/label replacement

The mathematical center used by the first-hitting description changes, but the material packet may still be substantially the same.

This is a descriptive/gauge change unless a quantitative material mismatch is also proved.

### 5.3 Scale replacement

A high-frequency subpacket becomes the new natural scale.  This may represent genuine cascade, but it may also merely expose a pre-existing substructure.

### 5.4 Boundary/pressure redistribution

The localized packet changes because energy, momentum, or vorticity crosses the chosen observation boundary.

This is physical transfer but is not automatically material destruction.

Therefore the correct audit is

\[
\boxed{
T_{dynamic}
=
T_{material}
\cup T_{scale}
\cup T_{boundary/pressure}
\cup T_{descriptor},
}
\]

with the firewall

\[
\boxed{
T_{descriptor}\not\Rightarrow\text{physical turnover}
}
\]

unless a standard PDE/material estimate proves it.

This avoids charging a physical cost to a mere re-description.

---

## 6. Axis-Property decomposition at a nonzero-vorticity point

Let

\[
\xi:=\frac\omega{|\omega|}
\]

be the vorticity axis and let

\[
S:=\frac12(\nabla u+\nabla u^T)
\]

be the strain tensor.

Decompose the action of strain on the vorticity axis as

\[
\boxed{
S\xi
=\gamma\xi+\tau,
}
\]

where

\[
\boxed{
\gamma:=\xi^TS\xi,
\qquad
\tau:=(I-\xi\otimes\xi)S\xi.
}
\]

`gamma` is the longitudinal stretching/compression seen by the vorticity direction.

`tau` is the transverse strain that rotates/reorients the vorticity direction.

Let

\[
P_\perp:=I-\xi\otimes\xi
\]

and define the strain acting inside the plane normal to the vorticity axis:

\[
S_\perp:=P_\perp S P_\perp.
\]

Since `tr S=0`,

\[
\operatorname{tr}S_\perp=-\gamma.
\]

Write

\[
\boxed{
S_\perp
=-\frac\gamma2P_\perp+D_\perp,
\qquad
\operatorname{tr}_{\perp}D_\perp=0.
}
\]

Here `D_perp` is the trace-free transverse-plane shear.

---

## 7. Exact three-channel strain identity

In the orthogonal splitting

\[
\mathbb R^3
=\operatorname{span}\{\xi\}\oplus\xi^\perp,
\]

the symmetric strain tensor has block form

\[
S
=
\begin{pmatrix}
\gamma & \tau^T\\
\tau & -\frac\gamma2I_2+D_\perp
\end{pmatrix}.
\]

Therefore the Frobenius norm satisfies the exact identity

\[
\boxed{
|S|_F^2
=\frac32\gamma^2
+2|\tau|^2
+|D_\perp|_F^2.
}
\]

This is the axis-property replacement for the undifferentiated statement “strain is large.”

Every large-strain event must pay through at least one of the three genuinely different geometric channels:

\[
\boxed{
\text{longitudinal stretch }\gamma
\quad\lor\quad
\text{axis reorientation }\tau
\quad\lor\quad
\text{transverse-plane shear }D_\perp.
}
\]

Quantitatively, if `|S|_F=M`, then at least one of

\[
\boxed{
|\gamma|\ge\frac{\sqrt2}{3}M,
}
\]

\[
\boxed{
|\tau|\ge\frac1{\sqrt6}M,
}
\]

or

\[
\boxed{
|D_\perp|_F\ge\frac1{\sqrt3}M
}
\]

must hold.

---

## 8. Standard vorticity equations in the same decomposition

For `omega != 0`, the Navier–Stokes vorticity equation gives

\[
(\partial_t+u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega.
\]

Taking the component along `xi` gives the amplitude equation

\[
\boxed{
(\partial_t+u\cdot\nabla)|\omega|
=\gamma|\omega|
+\nu\,\xi\cdot\Delta\omega.
}
\]

Projecting orthogonally gives the direction equation

\[
\boxed{
(\partial_t+u\cdot\nabla)\xi
=\tau
+\frac\nu{|\omega|}
(I-\xi\otimes\xi)\Delta\omega.
}
\]

Thus the axis decomposition is not merely descriptive language:

- `gamma` is exactly the inviscid vorticity-amplitude production rate;
- `tau` is exactly the inviscid vorticity-axis turning rate;
- `D_perp` is invisible to the immediate action `S xi` but represents transverse-plane deformation and must enter through surrounding geometry, pressure, velocity gradients, or later reorientation.

---

## 9. Consequence for the remaining H/T frontier

A large ambient-strain H event can now be split without ambiguity:

\[
\boxed{
H_{ambient}
\Longrightarrow
H_{stretch}
\lor
T_{axis/projective}
\lor
H_{transverse}.
}
\]

Here

- `H_stretch` means large `|gamma|` and hence direct amplitude production/compression;
- `T_axis/projective` means large `|tau|`, hence fast vorticity-direction rotation and direct connection with the existing projective/rotation ledgers;
- `H_transverse` means large `|D_perp|`, a strain reservoir hidden from the instantaneous vorticity-axis action.

This is sharper than treating all ambient strain as one H event.

The next standard-PDE target should be `H_transverse`, because the first two channels already connect to existing amplitude and projective/turnover ledgers.

---

## 10. Radial satellite axis

For a satellite at `x` relative to a tracked center `X`, define

\[
\boxed{
n:=\frac{x-X}{|x-X|}.
}
\]

The following alignment observables are useful and scale invariant:

\[
\boxed{
a_{\omega r}:=|\xi\cdot n|^2,
}
\]

\[
\boxed{
a_{u r}:=\frac{|(u-\dot X)\cdot n|^2}{|u-\dot X|^2}
}
\]

when the denominator is nonzero, and

\[
\boxed{
a_{\omega i}:=|\xi\cdot e_i|^2
}
\]

for the strain eigenframe `e_i`.

These do not provide a proof by themselves.  They specify whether a dynamic event is

- radial transport;
- tangential circulation/reorientation;
- eigenframe stretching;
- or transverse-plane deformation.

The purpose is to prevent different directional mechanisms from being charged to the same scalar turnover budget.

---

## 11. Updated problem tree after the parallel decomposition

The most economical current tree is

\[
\boxed{
\text{hypothetical singularity}
\Longrightarrow
T_{physical}
\lor
T_{descriptor}
\lor
\mathscr P_{satellite}.
}
\]

`T_descriptor` must either be shown to be harmless/gauge or converted by a standard estimate into physical turnover.

For the satellite family:

\[
\boxed{
\mathscr P_{satellite}
\Longrightarrow
\begin{cases}
\Pi_{pack}\ge\varepsilon_0,
&\text{amplified Type-II scenario candidate},\\
\Pi_{pack}<\varepsilon_0,
&\text{sparse/isolated ancestry problem}.
\end{cases}
}
\]

For any large ambient strain inside either satellite lane:

\[
\boxed{
H_{ambient}
\Longrightarrow
H_{stretch}
\lor
T_{axis/projective}
\lor
H_{transverse}.
}
\]

This identifies `H_transverse` and `sparse/isolated ancestry` as the two least-reduced mathematical objects after the new descriptive decomposition.

---

## 12. Audit verdict

### PROVED AS STANDARD LINEAR ALGEBRA / PDE IDENTITIES

- the exact strain decomposition
  \[
  |S|^2=\frac32\gamma^2+2|\tau|^2+|D_\perp|^2;
  \]
- the amplitude and axis-direction vorticity equations;
- `S_iso` and `S_amp` should be represented as one local satellite class plus a collective packing observable rather than as distinct local solution types.

### DESCRIPTIVE / ORGANIZATIONAL, NOT A PDE THEOREM

- Formation-Axiom labels for inherited/lost/newly-free data;
- separation of physical turnover from descriptor/gauge turnover;
- alignment observables used to classify radial/tangential/eigenframe behavior.

### NEXT TARGETS

1. Use the exact transverse-plane strain `D_perp` to determine whether a large `H_transverse` event necessarily creates positive-middle strain, projective rotation, or a derivative/pressure payer already present in the finite-stage ledgers.
2. Define the satellite packing/persistence count needed to cross the Seregin mixed-norm threshold `Pi_pack >= epsilon_0`.
3. Treat the remaining sparse satellite family through ancestry/restart, not through repeated point-picking alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
