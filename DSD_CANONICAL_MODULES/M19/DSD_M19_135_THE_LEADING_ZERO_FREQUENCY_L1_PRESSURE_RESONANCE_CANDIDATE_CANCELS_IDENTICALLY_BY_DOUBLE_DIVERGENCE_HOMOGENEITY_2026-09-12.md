# DSD M19-135 — The leading zero-frequency l=1 pressure resonance candidate cancels identically by double-divergence homogeneity

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE ONLY ZERO-q RESONANCE OF THE LEADING r^-2 PRESSURE OPERATOR IS THE l=1 HARMONIC MODE / ITS QUADRATIC NAVIER--STOKES SOURCE MOMENT VANISHES IDENTICALLY AFTER q-AVERAGING BECAUSE THE SOURCE IS A DOUBLE DIVERGENCE OF A HOMOGENEOUS r^-2 STRESS AND LINEAR HARMONICS HAVE ZERO HESSIAN / THERE IS NO NEW LEADING PRESSURE SOLVABILITY CONDITION / HIGHER PRESSURE ORDERS REMAIN OPEN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Leading pressure operator

For the critical leading velocity

\[
U_0(y,s)=r^{-1}A(q,\omega),
\qquad
q=\log r-s/2,
\]

the leading pressure is

\[
P_0=r^{-2}\Pi(q,\omega).
\]

M19-059 gives

\[
-\left(\partial_q^2-3\partial_q+2+\Delta_{S^2}\right)\Pi=F[A].
\]

On spherical harmonic degree `l`, the q-operator factors as

\[
\mathcal L_l
=-(\partial_q-(l+2))(\partial_q-(1-l)).
\]

For real q-frequency `xi`, the only zero-frequency resonance is

\[
\boxed{l=1,\qquad xi=0.}
\]

Indeed the second factor has a zero root only when `l=1`.

---

## 2. Why a naive resonance argument looks dangerous

If the q-average of the `l=1` source were nonzero, then solving

\[
\mathcal L_1\Pi_{1,0}=F_{1,0}
\]

would produce a secular term linear in q,

\[
\Pi_{1,0}(q)\sim c q.
\]

In physical variables this corresponds to an

\[
r^{-2}\log r
\]

pressure contribution, incompatible with the bounded recurrent critical-pressure ansatz.

So one might expect a nonlinear solvability condition

\[
\Pi_{l=1}\mathbb M_qF[A]=0.
\]

The present module shows that this condition is automatic.

---

## 3. q-average of the quadratic stress

Take the Bohr/q-average of the quadratic tensor

\[
T_{ij}:=U_{0i}U_{0j}.
\]

For a periodic or finite-rank quasiperiodic critical datum, the zero q-frequency part has exact homogeneity

\[
\boxed{
\overline T_{ij}(x)
=r^{-2}\tau_{ij}(\omega).
}
\]

The corresponding averaged pressure source is

\[
\boxed{
\overline f
=\partial_i\partial_j\overline T_{ij},
}
\]

which is homogeneous of degree `-4`.

---

## 4. Annular moment identity

Let

\[
H_1(x)=a\cdot x
\]

be an arbitrary degree-one harmonic polynomial.

On an annulus

\[
A_{R_1,R_2}=\{R_1<|x|<R_2\},
\]

integrate twice by parts:

\[
\begin{aligned}
\int_A H_1\,\partial_i\partial_j\overline T_{ij}\,dx
={}&\text{boundary terms}
+
\int_A \overline T_{ij}\,\partial_i\partial_jH_1\,dx.
\end{aligned}
\]

But

\[
\boxed{D^2H_1=0.}
\]

Because `Tbar` is exactly homogeneous of degree `-2`, the two boundary contributions at `R_1` and `R_2` are scale-independent copies with opposite annular orientation and cancel.

Hence

\[
\boxed{
\int_{A_{R_1,R_2}}H_1\,\overline f\,dx=0.
}
\]

Since

\[
\overline f=r^{-4}f_0(\omega),
\qquad
H_1=r(a\cdot\omega),
\]

the radial integral is logarithmic:

\[
\int_{R_1}^{R_2}\frac{dr}{r}
\int_{S^2}(a\cdot\omega)f_0(\omega)d\omega=0.
\]

For arbitrary `R_1<R_2`, therefore

\[
\boxed{
\int_{S^2}(a\cdot\omega)f_0(\omega)d\omega=0
}
\]

for every vector `a`.

Thus the entire `l=1` source projection vanishes.

---

## 5. Leading pressure resonance is automatically removed

We obtain

\[
\boxed{
\Pi_{l=1}\mathbb M_qF[A]=0
}
\]

identically for every sufficiently regular critical datum for which the q-average and homogeneous stress are defined.

This cancellation does **not** require the special toroidal parity anti-model of M19-059.
It is structural and follows from

1. quadratic stress form;
2. double divergence;
3. zero-q homogeneity;
4. `D^2 H_1=0`.

Therefore

\[
\boxed{
\text{leading pressure resonance}
\not\Rightarrow
\text{new rigidity of }A.
}
\]

---

## 6. Why higher orders are different

The cancellation uses the fact that the resonant harmonic polynomial has degree one.
At higher pressure-correction orders the resonant spherical harmonic degree increases, and its Hessian is no longer zero.

Hence the same double-divergence argument does **not** automatically remove all higher resonances.

The next target is to derive the general pressure-resonance ladder and identify the first order at which a genuine moment solvability condition survives.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
