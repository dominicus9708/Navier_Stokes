# DSD M19-129 — On any bounded-period DSS corridor, the positive cubic-tail floor and shell-H1 ceiling force a nontrivial finite low-mode scattering core

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-098 CUBIC-MASS FLOOR COMBINED WITH THE CRITICAL SHELL H1 CEILING / HIGH LOG-FOURIER AND ANGULAR MODES CANNOT CARRY ALL OF THE NONZERO DSS TAIL / A FIXED POSITIVE FRACTION OF THE CUBIC MASS LIVES IN FINITELY MANY LOW MODES ON EVERY BOUNDED-PERIOD CORRIDOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. DSS tail cell

For ordinary DSS,

\[
A(q+L,\omega)=A(q,\omega),
\qquad
L=\log\lambda=S/2.
\]

Work on the compact three-dimensional cell

\[
\boxed{
\mathcal C_L
:=S^1_L\times S^2.
}
\]

M19-098 gives, on the Barker--Prange application lane, the positive cubic-density floor

\[
\boxed{
\frac1L\int_{\mathcal C_L}|A|^3\,dq\,d\omega
\ge a_3>0,
}
\]

where one may take

\[
a_3=2c_M
\]

at the theorem-dependent scale.

---

## 2. Shell H1 ceiling

The critical spectator/Type-I shell control gives a finite bound of the form

\[
\boxed{
\frac1L\|A\|_{H^1(\mathcal C_L)}^2
\le H_*^2
}
\]

on a retained bounded-period smooth corridor.

Here the exact `H1` norm is the norm equivalent to the leading weighted Dirichlet shell charge, including log-radius and angular derivatives.

For a period interval

\[
0<L_*\le L\le L^*<\infty,
\]

the Sobolev constants on `C_L` are uniformly comparable after rescaling the circle variable to a fixed unit circle.

Hence

\[
\boxed{
\|f\|_{L^6(\mathcal C_L)}
\le C_{Sob}(L_*,L^*)\|f\|_{H^1(\mathcal C_L)}.
}
\]

---

## 3. Spectral cutoff

Let

\[
P_{\le\Lambda}
\]

be the spectral projection onto joint log-Fourier/spherical-harmonic modes whose compact-cell Laplace eigenvalue is at most

\[
\Lambda^2.
\]

Write

\[
A=A_{lo}+A_{hi},
\qquad
A_{lo}=P_{\le\Lambda}A.
\]

By the spectral theorem,

\[
\boxed{
\|A_{hi}\|_2
\le
\Lambda^{-1}\|A\|_{H^1}.
}
\]

Also

\[
\|A_{hi}\|_6
\le
C_{Sob}\|A_{hi}\|_{H^1}
\le
C_{Sob}\|A\|_{H^1}.
\]

Interpolate between `L2` and `L6`:

\[
\|A_{hi}\|_3
\le
\|A_{hi}\|_2^{1/2}
\|A_{hi}\|_6^{1/2}.
\]

Therefore

\[
\boxed{
\|A_{hi}\|_3^3
\le
C
\Lambda^{-3/2}
\|A\|_{H^1}^3.
}
\]

On the normalized bounded-period corridor,

\[
\boxed{
\frac1L\|A_{hi}\|_3^3
\le
C_*\Lambda^{-3/2}H_*^3.
}
\]

---

## 4. Choose a finite cutoff from the cubic floor

Choose `Lambda_*` so large that

\[
C_*\Lambda_*^{-3/2}H_*^3
\le
\frac{a_3}{8}.
\]

Then

\[
\frac1L\|A_{hi}\|_3^3
\le
\frac{a_3}{8}.
\]

Using

\[
A=A_{lo}+A_{hi}
\]

and the elementary inequality

\[
|x+y|^3\le4(|x|^3+|y|^3),
\]

we get

\[
\frac1L\|A\|_3^3
\le
4\frac1L\|A_{lo}\|_3^3
+4\frac1L\|A_{hi}\|_3^3.
\]

Since the left side is at least `a_3`,

\[
\boxed{
\frac1L\|A_{lo}\|_3^3
\ge
\frac{a_3}{8}.
}
\]

Thus finitely many low modes carry a fixed positive amount of cubic mass.

---

## 5. Finite-dimensional tail core

For fixed

\[
L_*\le L\le L^*,
\]

there are only finitely many joint modes below the uniform cutoff

\[
\Lambda_*.
\]

Hence define

\[
\boxed{
E_{tail}^{low}
:=P_{\le\Lambda_*}L^2(\mathcal C_L).
}
\]

Its dimension is uniformly finite on the bounded-period corridor, and every nontrivial DSS survivor has

\[
\boxed{
\|P_{\le\Lambda_*}A\|_{L^3(\mathcal C_L)}
\ge c_{tail}>0.
}
\]

Therefore the nonzero DSS critical tail cannot hide entirely in arbitrarily fine log-radius/angular oscillations.

---

## 6. Relation to M19-101 and M19-114

M19-101 reduces the **interior** unit-circle Floquet problem to finitely many modes.

M19-129 now gives, on bounded-period DSS corridors, a corresponding finite-dimensional **far-field tail core** carrying positive cubic mass.

Thus both ends of the DSS problem have finite-dimensional hard cores:

\[
\boxed{
\text{interior finite Floquet core}
\quad\leftrightarrow\quad
\text{far-field finite low-mode scattering core}.
}
\]

The missing theorem is a quantitative matching map between them.

---

## 7. Long-period firewall

The uniform finite-dimensional conclusion uses

\[
L\le L^*<\infty.
\]

If

\[
L\to\infty,
\]

the number of low q-Fourier modes below a fixed physical spectral cutoff grows with `L`.

Therefore

\[
\boxed{
\text{bounded-period finite tail core}
\not\Rightarrow
\text{uniform finite tail core as }L\to\infty.
}
\]

The long-period regime remains tied to the invariant-measure/transverse-stability analysis of M19-119--123.

---

## 8. RDSS extension

M19-128 supplies the twisted Floquet--Bloch spectrum for RDSS.

If an analogous positive cubic tail-density floor is certified for the RDSS branch, the same spectral-tail argument applies with the twisted covariant derivative and gives a finite low-cost Bloch-angular tail core on bounded `(L,beta)` corridors.

Such an RDSS cubic lower bound is not asserted here merely by analogy.

---

## 9. Next target

For bounded-period DSS, the next useful calculation is to linearize the spectator scattering map between:

- the finite-dimensional interior unit-multiplier/Fredholm core;
- the finite-dimensional low-mode tail core above.

If the resulting finite matrix has full rank after symmetry gauges, one obtains a genuine tail-to-core observability map in the finite hard sector.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
