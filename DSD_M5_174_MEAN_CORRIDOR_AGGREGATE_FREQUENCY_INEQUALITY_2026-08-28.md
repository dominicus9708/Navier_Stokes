# DSD M5-174 — Mean-Corridor Aggregate Frequency Inequality

Date: 2026-08-28

Status: **P1_B^S AGGREGATE FREQUENCY LEMMA / THE FROZEN EXACT DAMPING SYMBOL, GLOBAL STABLE-ROOT TRACKING ERROR, AND FIRST-ORDER RELATIVE COMMUTATOR CAN BE AGGREGATED WITHOUT PROMOTING A MEAN FREQUENCY BOUND TO A SUPPORT BOUND / ON EVERY FIXED PARABOLIC MEAN CORRIDOR `z N <= kappa`, THE FULL STABLE SAME-TAIL RELATIVE VORTICITY FREQUENCY SATISFIES `N_tau <= C_kappa z (1+N)` / THIS IS THE M5-171 ENTRY INEQUALITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Work on the statistical same-tail branch `P1_B^S` after the stable fast mode has been selected.

Let

\[
A:=1-4G^2-\Delta_{S^2}\ge1
\]

be the cross-section frequency operator on the invariant pair Hilbert space.  For a nonzero stable relative-vorticity state `F`, define

\[
E:=\|F\|^2,
\qquad
N:=\frac{\langle AF,F\rangle}{E}.
\]

Let `mu_F` be the normalized spectral measure of `A`, so

\[
N=\int A\,d\mu_F.
\]

Fix a finite corridor parameter `kappa>0` and assume only the **mean** condition

\[
\boxed{zN\le\kappa.}
\]

No support bound `zA<=kappa` is assumed.

---

## 2. Exact frozen damping symbol

Use the M5-173 exact frozen stable damping

\[
\Gamma_z(\omega,\ell)
=\frac{u-1}{8\nu z}\ge0,
\]

where `sqrt(D)=u+iv` and

\[
\operatorname{Re}\lambda_s=\frac34-\Gamma_z.
\]

Write

\[
S:=4\omega^2+\ell(\ell+1),
\]

so `A=1+S` up to the fixed convention.

Let

\[
m:=\ell(\ell+1),
\qquad
b:=\nu z.
\]

Then

\[
d=d_0+16b^2m,
\qquad
d_0:=1+12b+4b^2,
\]

and

\[
y^2=64b^2(S-m).
\]

Because

\[
u^2=\frac{\sqrt{d^2+y^2}+d}{2},
\]

a direct derivative at fixed `S` gives

\[
\boxed{
\partial_m u^2
=8b^2\left[1+\frac{d-2}{\sqrt{d^2+y^2}}\right]\ge0.
}
\]

Hence for fixed total frequency `S`, angular allocation can only increase the damping.

Define the minimum-damping scalar function

\[
\boxed{
\phi_z(S):=\Gamma_z\left(\omega=\frac{\sqrt S}{2},\ell=0\right).
}
\]

Then

\[
\boxed{
\Gamma_z=\phi_z(S)+r_z,
\qquad r_z\ge0.
}
\]

Moreover `phi_z` is increasing in `S`, because at `m=0` the real part `d_0` is fixed and the square-root quantity increases with `y^2=64b^2S`.

---

## 3. Low-side anisotropy remainder

The exact identity

\[
1+\frac{d-2}{\sqrt{d^2+y^2}}
=
\frac{64b^2(S-m)+48b+16b^2+64b^2m}
{\sqrt{d^2+y^2}\,[\sqrt{d^2+y^2}+2-d]}
\]

shows that on a fixed parabolic support corridor `S<=kappa/z`,

\[
\partial_m\Gamma_z
\le C_{\kappa,\nu}z^2.
\]

Therefore

\[
\boxed{
0\le r_z\le C_{\kappa,\nu}z
\qquad(S\le\kappa/z).
}
\]

The key use below is only on the **low side** `S<N`, where the mean corridor automatically gives

\[
S<N\le\kappa/z.
\]

Thus no mean-to-support promotion occurs.

---

## 4. Frozen aggregate covariance

Let

\[
Q:=\operatorname{Cov}_{\mu_F}(A,\Gamma_z).
\]

Since adding the constant `1` to `S` does not change covariance,

\[
Q
=\operatorname{Cov}(S,\phi_z(S))
+\int(S-N_S)r_z\,d\mu_F,
\]

where `N_S=N-1` under the chosen convention.

Because `phi_z` is increasing,

\[
\operatorname{Cov}(S,\phi_z(S))\ge0.
\]

On `S>=N_S`, the remainder contribution is nonnegative because `r_z>=0`.  On `S<N_S`, Section 3 gives `r_z<=C_kappa z`.  Therefore

\[
\boxed{
Q\ge-C_\kappa zN.
}
\]

This is the exact frozen mean-support resolution.

---

## 5. Nonautonomous stable-root tracking error

M5-173 gives, modewise on the full spectrum,

\[
\operatorname{Re}\frac{f_\tau}{f}
=\frac34-\Gamma_z+e_z,
\qquad
|e_z|\le Cz(1+\Gamma_z).
\]

The scalar `3/4` cancels from the Dirichlet quotient.

Split the spectral measure into

\[
H:=\{A\ge N\},
\qquad
L:=\{A<N\}.
\]

Let

\[
D:=\int_H(A-N)d\mu_F
=\int_L(N-A)d\mu_F
\le N.
\]

On the low side, the mean corridor implies `A<N<=kappa/z`, so the exact root formula gives

\[
\Gamma_z\le C_\kappa,
\]

and hence

\[
|e_z|\le C_\kappa z.
\]

On the high side,

\[
|e_z|\le Cz(1+\Gamma_z).
\]

Therefore

\[
\operatorname{Cov}(A,e_z)
\le
CzD
+Cz\int_H(A-N)\Gamma_zd\mu_F
+C_\kappa zD.
\]

Write

\[
H_\Gamma:=\int_H(A-N)\Gamma_zd\mu_F,
\qquad
L_\Gamma:=\int_L(N-A)\Gamma_zd\mu_F.
\]

Then

\[
Q=H_\Gamma-L_\Gamma,
\qquad
L_\Gamma\le C_\kappa N.
\]

Hence

\[
\boxed{
\operatorname{Cov}(A,e_z)
\le CzQ+C_\kappa zN.
}
\]

Combining with `Q>=-C_kappa zN`, for sufficiently small `z`,

\[
\boxed{
-2Q+2\operatorname{Cov}(A,e_z)
\le C_\kappa z(1+N).
}
\]

Thus the nonautonomous tracking error does not reopen a high-frequency dust channel.

---

## 6. Variable first-order relative coupling

After the stable fast-normal reduction, the remaining variable relative transport/stretching/Biot--Savart coupling enters the forward `tau` evolution with the normal factor `z` and has cross-section differential order at most one:

\[
B_z=b^a\nabla_a+C+\mathcal S.
\]

The principal first derivative in the transport part is skew after the divergence-free integration by parts.  In the quotient derivative the highest derivative cancels, leaving the commutator/symmetric-coefficient form

\[
\frac{2z}{E}\operatorname{Re}\langle(A-N)F,B_zF\rangle.
\]

Using the uniform W1 coefficient bounds and the M5-163 analytic/commutator package,

\[
\boxed{
\left|
\frac{2z}{E}\operatorname{Re}\langle(A-N)F,B_zF\rangle
\right|
\le Cz(1+N).
}
\]

No second spectral moment is required: the apparent top-order term cancels by the first-order transport structure, and coefficient derivatives are uniformly bounded on the compact W1 class.

---

## 7. Full corridor inequality

Adding Sections 4--6 gives, whenever `F!=0` and

\[
zN\le\kappa,
\]

for all sufficiently small `z`,

\[
\boxed{
N_\tau
\le
C_\kappa z(1+N).
}
\]

Equivalently,

\[
\boxed{
\frac d{d\tau}\log(1+N)
\le C_\kappa e^{-\tau}.
}
\]

This is exactly the M5-171 first-parabolic-barrier entry inequality.

---

## 8. DSD four-chain audit

### Formation — GREEN

The spectral measure, exact damping symbol, tracking error, and variable coupling are all formed from the actual stable same-tail relative-vorticity system.

### Axis — GREEN

Total frequency `S`, angular allocation `m`, normal depth `z`, and pair-flow frequency remain distinct until the exact damping minimization is performed.

### Static aggregation — GREEN

A mean corridor is never promoted to a support corridor.  The anisotropy remainder is estimated only on the low side `A<N`, where the mean itself supplies the needed pointwise bound.

### Dynamics — GREEN within the W1 statistical flat branch

The fast explosive branch has already been removed by the flat selection.  The stable-root tracking and first-order relative commutator are the previously audited dynamic channels.

### Cross-audit — GREEN

The high-frequency dust that invalidated the first version of M5-172 is explicitly retained and shown not to worsen the covariance lower bound.

---

## 9. Consequence and remaining audit

M5-174 supplies the inequality needed by M5-171.  The next step is **not** another spectral estimate.  It is to combine the first-barrier argument with the earlier M5-154 flat-fiber necessity statement and re-audit that implication in its exact form:

\[
\boxed{
\text{bounded cross frequency on a deep tail}
\Rightarrow
\text{no nonzero superalgebraically flat statistical fiber}.
}
\]

Only after that cross-audit may `P1_B^S` be marked CLOSED.

`P1_B^P` remains separate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
