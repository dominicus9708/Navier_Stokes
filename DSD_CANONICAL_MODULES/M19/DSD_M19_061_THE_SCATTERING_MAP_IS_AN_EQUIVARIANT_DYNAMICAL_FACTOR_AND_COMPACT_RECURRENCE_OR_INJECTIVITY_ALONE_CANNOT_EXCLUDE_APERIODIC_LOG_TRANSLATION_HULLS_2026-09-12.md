# M19-061 — The scattering map is an equivariant dynamical factor, and compact recurrence or injectivity alone cannot exclude aperiodic log-translation hulls

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL R-CRITICAL REALIZABILITY FORMULATION / DYNAMICAL-FACTOR FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-055--060 successively ruled out several local or elliptic shortcuts for the recurrent weak-critical scattering datum

\[
A(q,\omega).
\]

The remaining issue is global: whether a complete recurrent ancient similarity trajectory can realize a nonzero aperiodic weak-critical boundary history.

This module formulates that problem as an equivariant dynamical-factor problem and determines what properties are **not** sufficient for closure.

The key result is negative but structurally decisive:

\[
\boxed{
\text{compact recurrence of the interior hull, even plus injective scattering data, does not force periodicity or triviality of }A.
}
\]

A genuinely PDE-specific rigidity theorem must exclude nontrivial translation factors of the recurrent Navier--Stokes hull.

## 2. Recurrent ancient similarity hull

Let \(Y\) denote a complete ancient similarity trajectory in the retained bounded/compact corridor.

Let

\[
\boxed{\mathcal H:=\overline{\{\sigma_tY:t\in\mathbb R\}}}
\]

be its recurrent hull in the topology certified by the upstream compactness construction.

Here

\[
\sigma_t:\mathcal H\to\mathcal H
\]

is similarity-time translation.

On the quiet recurrent branch, \(\mathcal H\) is compact and invariant under \(\sigma_t\).

## 3. Scattering map

For each state/trajectory \(Z\in\mathcal H\), let

\[
\boxed{
\mathscr S(Z)=A_Z(q,\omega)
}

be the weak-critical scattering datum supplied by the outward characteristic construction.

The M5-567 covariance rule is

\[
\boxed{
A_{\sigma_tZ}(q,\omega)
=
A_Z(q-t/2,\omega).
}
\]

Define the log-translation action

\[
(T_sA)(q,\omega):=A(q+s,\omega).
\]

Then the scattering map obeys the exact equivariance relation

\[
\boxed{
\mathscr S\circ\sigma_t
=
T_{-t/2}\circ\mathscr S.
}
\]

Thus the scattering hull is a dynamical factor of the interior recurrent hull.

## 4. The scattering image is itself a compact translation hull

Assuming the scattering map is continuous in the certified topology, compactness of \(\mathcal H\) implies compactness of

\[
\boxed{
\mathcal K_A:=\mathscr S(\mathcal H).
}
\]

Equivariance gives

\[
T_s\mathcal K_A=\mathcal K_A.
\]

Hence \(\mathcal K_A\) is a compact translation-invariant hull of functions of \(q\).

This is exactly the natural setting of periodic, quasiperiodic, almost-periodic, and more general recurrent translation dynamics.

Compactness therefore does not imply that the image consists of constant or periodic functions.

## 5. Explicit abstract compact-recurrent anti-model

Consider the torus

\[
\mathbb T^2=\mathbb R^2/(2\pi\mathbb Z)^2
\]

with irrational linear flow

\[
\boxed{
\sigma_t(\phi_1,\phi_2)
=(\phi_1+t,\phi_2+\sqrt2\,t)
\pmod{2\pi}.
}
\]

This flow is compact, recurrent, and aperiodic.

Define a continuous observable

\[
\boxed{
b(\phi_1,\phi_2)=\sin\phi_1+\frac12\sin\phi_2.}
\]

Along one orbit,

\[
b(\sigma_t\phi)
=
\sin(\phi_1+t)
+
\frac12\sin(\phi_2+\sqrt2\,t),
\]

which is quasiperiodic and nonperiodic.

Coupling this scalar observable to a fixed toroidal spherical mode produces exactly the qualitative form of the M19-041 leading anti-model.

Therefore

\[
\boxed{
\text{compact recurrent interior dynamics can have a nontrivial aperiodic translation factor.}
}
\]

This abstract example is not a Navier--Stokes solution.  It is a dynamical-systems firewall against an invalid inference from compact recurrence alone.

## 6. Injectivity of the scattering map is also insufficient

One might hope that if \(\mathscr S\) is injective, then distant \(q\)-phases correspond to distinct interior states and recurrence would force repetition.

This is false in general.

If \(\mathscr S\) is a homeomorphism from a compact aperiodic hull onto its image, then

\[
(\mathcal H,\sigma_t)
\cong
(\mathcal K_A,T_{-t/2})
\]

as dynamical systems.

The image is then just as aperiodic as the interior system.

Thus

\[
\boxed{
\text{injective scattering data do not imply periodic or constant scattering.}
}
\]

Injectivity solves state reconstruction, not rigidity.

## 7. What would actually be sufficient

A closure theorem must supply information that is incompatible with a nontrivial translation factor.

Examples of genuinely sufficient structures would include one of the following.

### A. Trivial-factor theorem

Prove directly that every continuous factor of the retained recurrent Navier--Stokes hull into the critical translation system is trivial:

\[
\boxed{
\mathscr S(\mathcal H)=\{0\}
\quad\text{or a rigid periodic class already excluded upstream}.}
\]

### B. Strict contraction

Find a metric \(d\) on the relevant interior quotient for which

\[
\boxed{
 d(\sigma_tY_1,\sigma_tY_2)
\le e^{-\gamma t}d(Y_1,Y_2),
\qquad t>0,
}
\]

while the scattering translation acts isometrically or noncontractively in the corresponding boundary metric.

A recurrent compact strictly contractive flow has only a singleton recurrent component, forcing a constant scattering state.

### C. Finite-variation cocycle

Find a boundary observable \(C(A)\) whose total variation along translation is finite on every complete recurrent orbit but is strictly positive for every nonconstant \(A\).  Recurrence would then force constancy.

M19-042--043 show that ordinary energy flux and Kelvin circulation do not have the required property.

### D. Spectral/dynamical exclusion

Prove that the retained Navier--Stokes recurrent hull has no irrational/quasiperiodic translation factor in the critical channel, for example through a spectral gap, unique continuation, or a PDE-specific mixing/rigidity theorem.

None of these structures is currently certified.

## 8. The ordinary L2 difference estimate does not give automatic contraction

Let \(U,V\) be two similarity solutions and set

\[
W:=U-V.
\]

Then

\[
\partial_\theta W
+\frac12W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
+(W\cdot\nabla)V
+\nabla Q
=\nu\Delta W.
\]

Taking the unweighted \(L^2\) inner product with \(W\), using incompressibility, gives

\[
\boxed{
\frac12\frac d{d\theta}\|W\|_2^2
+\nu\|\nabla W\|_2^2
=
\frac14\|W\|_2^2
-
\int W_iW_j\,\partial_jV_i\,dy.
}
\]

Thus the similarity drift contributes a \(+\frac14\|W\|_2^2\) term on the right after integration by parts, and the strain term has no fixed sign.

Therefore ordinary unweighted \(L^2\) does **not** provide an unconditional strict contraction metric.

Any contraction strategy needs additional structure, weighting, spectral information, or strain control.

## 9. Updated theorem frontier

After the local-observable and pressure firewalls, the remaining dominant theorem can be stated more precisely as

\[
\boxed{
\mathcal T_{critical}^{factor}:
\text{the retained recurrent Navier--Stokes ancient hull admits no nonzero aperiodic weak-critical log-translation factor.}
}
\]

This formulation is stronger and more accurate than merely asking for compactness or injectivity of the scattering map.

## 10. Certified / not certified

### Certified

1. Exact equivariance of the scattering map with similarity-time/log-radius translations.
2. Compact recurrent interior dynamics can abstractly support aperiodic translation factors.
3. Injectivity of the scattering map does not exclude such factors.
4. Ordinary unweighted \(L^2\) difference dynamics are not automatically contractive.
5. Therefore the missing closure theorem must use a PDE-specific rigidity mechanism beyond compactness, recurrence, or reconstruction.

### Not certified

1. Continuity/injectivity of the scattering map in every desired strong topology.
2. Existence of a strict contracting metric on the actual NS recurrent hull.
3. Exclusion of quasiperiodic/almost-periodic critical factors by Navier--Stokes dynamics.
4. Global 3D Navier--Stokes regularity.

## 11. Next calculation

The most concrete next internal calculation is to test whether a **Gaussian/Ornstein--Uhlenbeck weighted difference norm** can reverse the unfavorable \(+\frac14\|W\|_2^2\) contribution and produce a spectral-gap estimate on the recurrent compact corridor.

M19-062 should derive the weighted linearized energy identity exactly before any nonlinear estimate is attempted.  If the weighted linear operator has a usable gap but the nonlinear strain term is the only obstruction, the global factor theorem reduces to a quantitatively stated strain-vs-gap condition rather than an unspecified unique-continuation problem.

---

\[
\boxed{\text{M19-061 COMPLETE; COMPACT RECURRENCE AND SCATTERING INJECTIVITY DO NOT BY THEMSELVES EXCLUDE APERIODIC CRITICAL TRANSLATION FACTORS.}}
\]
