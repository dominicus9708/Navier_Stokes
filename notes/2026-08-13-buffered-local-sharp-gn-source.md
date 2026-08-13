# Buffered local sharp-Gagliardo--Nirenberg source inequality

Date: 2026-08-13

Status: **DERIVED LOCAL NEAR-SOURCE INEQUALITY / CUT-OFF RESERVE EXPLICIT / CROSS-CORE GEOMETRY STILL OPEN**.

This note implements the sharp-GN audit correction in a fixed normalized moving-window frame.  It keeps the cutoff reserve explicit and separates the local nonlinear strain from remote/background strain.

---

## 1. Normalized window and nested cutoffs

Work at one naturally rescaled checkpoint.  Let

\[
B_1\subset B_{R_0}\subset B_{R_1}
\]

with `R1-R0` bounded below.  Choose

\[
\psi\in C_c^\infty(B_{R_1}),
\qquad
0\le\psi\le1,
\qquad
\psi=1\text{ on }B_{R_0}.
\]

Write

\[
\rho=|\Omega|.
\]

Define the buffered scalar magnitude

\[
\boxed{f=\psi\rho.}
\]

Let

\[
E_\psi=\int\psi^2\rho^2dy.
\]

---

## 2. Near/far strain split

Let `T` denote the strain/vorticity zero-order singular-integral operator and define

\[
S_{\rm near}=\mathbb T(\psi\Omega),
\]

\[
S_{\rm far}=S-S_{\rm near}.
\]

For a local source inside `B_R0`,

\[
Q_{R_0}
=\int_{B_{R_0}}\Omega\cdot S\Omega dy
=Q_{\rm near}+Q_{\rm far}.
\]

Because `psi=1` on the source region,

\[
|Q_{\rm near}|
\le
\|S_{\rm near}\|_3
\|\psi\Omega\|_3^2.
\]

The Calderon--Zygmund bound gives

\[
\|S_{\rm near}\|_3
\le C_R\|\psi\Omega\|_3.
\]

Hence

\[
\boxed{
|Q_{\rm near}|
\le
C_R\|f\|_3^3.
}
\]

---

## 3. Apply the canonical sharp GN inequality

The whole-space zero extension of `f` belongs to `H1(R3)`.  Therefore

\[
\|f\|_3^3
\le
C_{\rm GN}^3
\|f\|_2^{3/2}
\|\nabla f\|_2^{3/2}.
\]

Thus

\[
\boxed{
|Q_{\rm near}|
\le
C_\sharp
E_\psi^{3/4}
\|\nabla(\psi\rho)\|_2^{3/2},
\qquad
C_\sharp=C_RC_{\rm GN}^3.
}
\]

---

## 4. Keep the cutoff reserve explicit

Since

\[
\nabla(\psi\rho)
=\psi\nabla\rho+\rho\nabla\psi,
\]

for every `epsilon>0`,

\[
\boxed{
\|\nabla(\psi\rho)\|_2^2
\le
(1+\varepsilon)
P_{{\rm mag},\psi}
+
C_\varepsilon
\int_{A_\psi}\rho^2dy,
}
\]

where

\[
P_{{\rm mag},\psi}
=\int\psi^2|\nabla\rho|^2dy
\]

and `A_psi=supp grad psi` is the transition shell.

Using the exact magnitude/direction decomposition,

\[
P_{{\rm mag},\psi}
=P_\psi-P_{{\rm ang},\psi},
\]

with

\[
P_\psi=\int\psi^2|\nabla\Omega|^2dy
\]

and, on the nonzero set,

\[
P_{{\rm ang},\psi}
=\int\psi^2\rho^2|\nabla\xi|^2dy.
\]

Therefore

\[
\boxed{
|Q_{\rm near}|
\le
C_\sharp
E_\psi^{3/4}
\left[
(1+\varepsilon)(P_\psi-P_{{\rm ang},\psi})
+C_\varepsilon E_{A_\psi}
\right]^{3/4}.
}
\]

This is the canonical buffered local source inequality.

---

## 5. Compactness-rigidity coefficient gap

On the bounded buffered V2 branch, strong local `L2_t H1_x` vorticity compactness is available on a smaller cylinder.  If persistent source-active time slices give a nontrivial strongly `H1`-compact family

\[
f_j=\psi|\Omega_j|,
\]

then the canonical sharp-GN compactness-rigidity lemma yields a family-dependent

\[
\delta_{\rm GN}>0
\]

such that

\[
\|f_j\|_3^3
\le
(1-\delta_{\rm GN})^3
C_{\rm GN}^3
\|f_j\|_2^{3/2}
\|\nabla f_j\|_2^{3/2}.
\]

Hence on that compact nontrivial branch,

\[
\boxed{
|Q_{\rm near}|
\le
(1-\delta_{\rm GN})^3
C_\sharp
E_\psi^{3/4}
\left[
(1+\varepsilon)(P_\psi-P_{{\rm ang},\psi})
+C_\varepsilon E_{A_\psi}
\right]^{3/4}.
}
\]

If the sharp-GN gap fails, the sequence must leave this strong compactness class through a typed concentration/modulation branch.

---

## 6. Use the finite shell selector

On the bounded normalized-global-enstrophy branch, the finite-shell selector lets the proof move outward through parent shells until one obtains

\[
\boxed{
E_{A_\psi}\le\varepsilon_{\rm shell}
}
\]

for a chosen small shell mass, unless a previously typed global-enstrophy or local-H1 concentration channel becomes unbounded.

Thus the artificial cutoff reserve can be made small without inspecting every radius.

The price is that the interior `B_R0` may contain more than one active core.  Their interactions are handled by the multicore aggregation and far/common-strain decomposition rather than assumed absent.

---

## 7. Far/background strain

For the remaining source

\[
Q_{\rm far}
=\int_{B_{R_0}}\Omega\cdot S_{\rm far}\Omega dy,
\]

split around a chosen core/cluster center `y0`:

\[
S_{\rm far}(y)
=S_{\rm far}(y_0)
+[S_{\rm far}(y)-S_{\rm far}(y_0)].
\]

The constant trace-free part obeys the projective covariance gap

\[
\boxed{
|Q_{\rm far}^{(0)}|
\le
E_C|S_{\rm far}(y_0)|_F
\sqrt{\frac23-J_C}.
}
\]

The variation is bounded by

\[
\boxed{
|Q_{\rm far}^{(1)}|
\le
E_C\,\operatorname{diam}(C)
\|\nabla S_{\rm far}\|_\infty.
}
\]

At very large normalized distance the remote tail is uniformly small if the normalized global enstrophy is bounded:

\[
|S_{>R}|
=O(R^{-3/2}),
\qquad
|S_{>R}(y)-S_{>R}(y_0)|
=O(R^{-5/2}).
\]

---

## 8. What is now closed and what is not

Closed on the fully bounded normalized state block:

1. canonical sharp-GN form of the near source;
2. exact angular-palinstrophy subtraction;
3. compactness-rigidity sharp-GN deficit on persistent V2-bounded sequences;
4. finite search for a low-mass localization shell;
5. arbitrarily distant strain tail.

Still open:

1. quantitative bookkeeping of several active cores inside the selected parent buffer;
2. proving a **uniform** source/dissipation gap after adding finite-distance cross-core strain;
3. routing every failure into one of the already typed concentration/coherence/flux branches.

The multicore static-aggregation identity says that distinct core axes/magnitude levels add positive mismatch channels, suggesting that cross-core interaction should increase rather than decrease rigidity, but a full nonlinear source estimate is still required.

Status: **LOCAL NEAR-SOURCE SHARP-GN BRIDGE CLOSED / MULTICORE CROSS-SOURCE CLOSURE OPEN**.
