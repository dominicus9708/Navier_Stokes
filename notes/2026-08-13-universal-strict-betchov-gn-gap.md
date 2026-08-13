# Universal strict gap below the formal Betchov--sharp-GN source constant

Date: 2026-08-13

Status: **DERIVED STRICT-GAP THEOREM USING STANDARD SHARP-GN CONCENTRATION--COMPACTNESS / GLOBAL REGULARITY NOT IMPLIED**.

This note promotes the previous exact extremizer incompatibility to a qualitative **universal strict constant gap**.  The argument is by contradiction: any incompressible-strain sequence approaching the formal product constant would force the scalar strain magnitude to become a sharp Gagliardo--Nirenberg optimizer, the matrix direction to freeze by Kato equality, and the strain shape to approach the Betchov determinant extremizer.  The resulting fixed-shape field is separated by an exact `L2` spectral angle from every incompressible strain field.

External standard inputs:

- Michael I. Weinstein, *Nonlinear Schrödinger equations and sharp interpolation estimates*, Communications in Mathematical Physics 87 (1983), 567--576: sharp interpolation constant and ground-state optimizer for the relevant NLS/Gagliardo--Nirenberg variational problem;
- P.-L. Lions, *The concentration-compactness principle in the calculus of variations. The locally compact case, part 1*, Annales de l'I.H.P. Analyse non linéaire 1 (1984), 109--145: compactness mechanism modulo translations for normalized maximizing/minimizing sequences.

The concentration--compactness step is sketched below for the exact `L2`--gradient-`L2`--`L3` functional so that no stronger quantitative stability theorem is assumed.

---

## 1. Formal global upper bound

Let

\[
S=\frac12(\nabla u+\nabla u^T),
\qquad
\omega=\nabla\times u,
\]

for a smooth decaying divergence-free velocity on `R3`.  Write

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\]

and

\[
Q=\int\omega\cdot S\omega dx.
\]

Betchov gives

\[
Q=-4\int\det Sdx.
\]

The sharp trace-free determinant bound is

\[
-\det S
\le
\frac1{3\sqrt6}|S|^3.
\]

The scalar sharp Gagliardo--Nirenberg inequality gives

\[
\||S|\|_3^3
\le
C_{\rm GN}^3
\|S\|_2^{3/2}
\|\nabla|S|\|_2^{3/2}.
\]

Kato gives

\[
\|\nabla|S|\|_2
\le
\|\nabla S\|_2.
\]

For incompressible strain,

\[
\|S\|_2^2=E/2,
\qquad
\|\nabla S\|_2^2=P/2.
\]

Therefore

\[
\boxed{
Q
\le
C_0 E^{3/4}P^{3/4},
\qquad
C_0=\frac{C_{\rm GN}^3}{3\sqrt3}.
}
\]

---

## 2. Strict-gap theorem

There exists a universal number

\[
\boxed{\delta_{\rm inc}>0}
\]

(depending only on the sharp scalar GN constant and the incompressible strain class, not on the particular solution) such that every nonzero smooth decaying divergence-free velocity satisfies

\[
\boxed{
Q
\le
(1-\delta_{\rm inc})
C_0 E^{3/4}P^{3/4}.
}
\]

Equivalently,

\[
\boxed{
\sup_{\substack{u\ne0\\ \nabla\cdot u=0}}
\frac{
\int\omega\cdot S\omega
}{
E^{3/4}P^{3/4}
}
<
\frac{C_{\rm GN}^3}{3\sqrt3}.
}
\]

The proof below establishes existence of a positive gap but does not compute its optimal numerical value.

---

## 3. Contradiction hypothesis and normalization

Assume no positive gap exists.  Then there is a sequence of incompressible strains `S_j` with positive source and

\[
\frac{Q_j}{E_j^{3/4}P_j^{3/4}}
\to C_0.
\]

Amplitude and spatial dilation preserve this dimensionless ratio and preserve membership in the incompressible strain class.  Normalize so

\[
\boxed{
\|S_j\|_2=1,
\qquad
\|\nabla S_j\|_2=1.
}
\]

Let

\[
\sigma_j=|S_j|.
\]

Then

\[
\|\sigma_j\|_2=1,
\qquad
\|\nabla\sigma_j\|_2\le1.
\]

---

## 4. Factor the formal extremal ratio

Define three ratios:

\[
\boxed{
D_j
=
\frac{Q_j}
{(4/(3\sqrt6))\int\sigma_j^3dx}
\le1,
}
\]

\[
\boxed{
G_j
=
\frac{\|\sigma_j\|_3^3}
{C_{\rm GN}^3
\|\sigma_j\|_2^{3/2}
\|\nabla\sigma_j\|_2^{3/2}}
\le1,
}
\]

and

\[
\boxed{
K_j
=
\left(
\frac{\|\nabla\sigma_j\|_2}
{\|\nabla S_j\|_2}
\right)^{3/2}
\le1.
}
\]

Because `||S_j||_2=||grad S_j||_2=1`, the normalized source ratio divided by its formal upper constant is exactly

\[
\boxed{
D_jG_jK_j.
}
\]

The contradiction hypothesis therefore implies

\[
\boxed{
D_j\to1,
\qquad
G_j\to1,
\qquad
K_j\to1.
}
\]

In particular,

\[
\boxed{
\|\nabla\sigma_j\|_2\to1
}
\]

and `sigma_j` is a normalized sharp-GN maximizing sequence.

---

## 5. Compactness of the scalar sharp-GN maximizing sequence

After a negligible dilation adjustment one may enforce both scalar constraints exactly.  The concentration--compactness alternatives are then:

1. vanishing;
2. dichotomy;
3. compactness modulo translations.

Vanishing is impossible because

\[
\|\sigma_j\|_3^3
\to C_{\rm GN}^3>0.
\]

For a hypothetical split with squared `L2` masses `a,1-a` and squared gradient masses `b,1-b`, the sharp GN inequality on both pieces gives the normalized upper factor

\[
(ab)^{3/4}
+[(1-a)(1-b)]^{3/4}.
\]

For `0<a,b<1`,

\[
\sqrt{ab}+
\sqrt{(1-a)(1-b)}
\le1,
\]

and strict convexity of `x^{3/2}` gives

\[
\boxed{
(ab)^{3/4}
+[(1-a)(1-b)]^{3/4}
<1.
}
\]

Thus a genuine dichotomy cannot maximize the sharp functional.

Hence, after translations `x_j`, a subsequence is tight.  The standard weak-limit/Brezis--Lieb argument then gives strong convergence in both constraints:

\[
\boxed{
\sigma_j(\cdot+x_j)
\to Q_{\rm GN}
\quad\text{strongly in }H^1(\mathbb R^3),
}
\]

where `Q_GN` is a normalized positive sharp-GN ground-state optimizer.

From now on absorb the translations into `S_j`.

---

## 6. The matrix strains themselves become strongly compact in `L2`

The sequence `S_j` is bounded in `H1`, so on every fixed ball Rellich gives a locally strongly `L2` convergent subsequence:

\[
S_j\to S_\infty
\quad\text{in }L^2_{\rm loc}.
\]

But

\[
|S_j|=\sigma_j
\to Q_{\rm GN}
\quad\text{strongly in }L^2(\mathbb R^3).
\]

Therefore the `L2` mass of `S_j` is uniformly tight.  Local strong convergence plus the scalar tail control yields

\[
\boxed{
S_j\to S_\infty
\quad\text{strongly in }L^2(\mathbb R^3).
}
\]

The uniform `H1` bound then gives, by interpolation,

\[
\boxed{
S_j\to S_\infty
\quad\text{strongly in }L^p
\quad(2\le p<6),
}
\]

in particular in `L3`.

Also

\[
\boxed{|S_\infty|=Q_{\rm GN}}
\]

almost everywhere.

---

## 7. Kato near-equality freezes the matrix direction in the limit

Weak `H1` compactness gives

\[
\|\nabla S_\infty\|_2
\le1.
\]

But

\[
|S_\infty|=Q_{\rm GN}
\]

and scalar strong `H1` convergence gives

\[
\|\nabla|S_\infty|\|_2
=\|\nabla Q_{\rm GN}\|_2
=1.
\]

Kato's inequality gives

\[
1
=\|\nabla|S_\infty|\|_2
\le
\|\nabla S_\infty\|_2
\le1.
\]

Hence equality holds throughout:

\[
\boxed{
\|\nabla S_\infty\|_2
=\|\nabla|S_\infty|\|_2.
}
\]

Since `Q_GN>0` on `R3`, write

\[
S_\infty=Q_{\rm GN}\,A(x),
\qquad |A(x)|_F=1.
\]

The exact matrix Kato decomposition gives

\[
|\nabla S_\infty|^2
=|\nabla Q_{\rm GN}|^2
+Q_{\rm GN}^2|\nabla A|^2.
\]

Equality of the two gradient norms therefore forces

\[
\boxed{
\nabla A=0
}
\]

almost everywhere.  Thus

\[
\boxed{
S_\infty(x)
=Q_{\rm GN}(x)A
}
\]

for one fixed symmetric trace-free Frobenius-unit matrix `A`.

---

## 8. Determinant near-equality fixes `A` to the Betchov source-optimal shape

Strong `L3` convergence makes the cubic determinant functional continuous:

\[
\det S_j\to\det S_\infty
\quad\text{in }L^1.
\]

Since

\[
D_j\to1,
\]

the limit saturates the integrated determinant bound:

\[
-\int\det S_\infty
=
\frac1{3\sqrt6}
\int|S_\infty|^3.
\]

Because

\[
S_\infty=Q_{\rm GN}A
\]

and `Q_GN>0`, this reduces to

\[
\boxed{
-\det A
=\frac1{3\sqrt6}.
}
\]

Thus `A` is a rotated source-optimal matrix with eigenvalue shape

\[
\boxed{
(-2,1,1)/\sqrt6.
}
\]

---

## 9. Exact `1/2` spectral gap gives the contradiction

The previously derived Fourier spectral-angle theorem states that for every scalar `f` and every fixed rotation `A` of the source-optimal matrix,

\[
\boxed{
\inf_{\substack{S=\operatorname{sym}\nabla u\\ \nabla\cdot u=0}}
\|S-fA\|_2
\ge
\frac12\|f\|_2.
}
\]

Every `S_j` belongs to the incompressible strain class.  Taking

\[
f=Q_{\rm GN}
\]

therefore gives

\[
\boxed{
\|S_j-Q_{\rm GN}A\|_2
\ge
\frac12\|Q_{\rm GN}\|_2.
}
\]

But Section 6--8 gave

\[
S_j\to Q_{\rm GN}A
\quad\text{strongly in }L^2.
\]

Contradiction.

Therefore no maximizing sequence can approach the formal product constant.

This proves the existence of a strict universal gap `delta_inc>0`.

---

## 10. What this theorem does **not** solve

The strict source estimate is

\[
\boxed{
Q
\le
(1-\delta_{\rm inc})
\frac{C_{\rm GN}^3}{3\sqrt3}
E^{3/4}P^{3/4}.
}

This is stronger than the formal Betchov--GN bound, but the powers are still Navier--Stokes critical.

By itself it does **not** imply

\[
Q<\nu P
\]

for arbitrary `E,P`; the coefficient can still be overcome in high-enstrophy/low-palinstrophy-ratio states.

The theorem therefore supplies the sought **uniform coefficient gain**, not global regularity.

The next task is to combine this universal source gap with

- first-hitting amplitude normalization;
- automatic terminal H1/V2 bootstrap on bounded normalized-enstrophy windows;
- angular-palinstrophy compactness gap;
- finite-shell/multicore localization;
- and the complementary normalized-enstrophy concentration branch.

Status: **UNIVERSAL GLOBAL SOURCE CONSTANT STRICTLY IMPROVED / GLOBAL SMOOTHNESS STILL OPEN**.
