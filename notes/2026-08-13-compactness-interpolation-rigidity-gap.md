# Compactness-rigidity gap for the critical magnitude interpolation

Date: 2026-08-13

Status: **CONDITIONAL COMPACTNESS-RIGIDITY LEMMA / FIRST CLOSED SATURATION OBSTRUCTION / TIME-SELECTION STILL OPEN**.

The magnitude-heterogeneity channel shows that the critical `L2-L3-L6` interpolation can saturate only when the enstrophy-weighted vorticity magnitude becomes almost single-level.  On a compact, nontrivial, cutoff-normalized family this limiting profile is impossible.  This gives a genuine strict-gap mechanism once strong enough vorticity compactness is available.

---

## 1. Cutoff-normalized scalar magnitude

Work in one naturally rescaled dangerous window and choose

\[
\chi\in C_c^\infty(B_R),
\qquad
0\le\chi\le1,
\]

with `chi=1` on the core ball.

Define

\[
\boxed{
f_j=\chi|\Omega_j|.}
\]

Then

\[
f_j\in H_0^1(B_R),
\qquad
f_j\ge0.
\]

Assume a persistent nontriviality lower bound

\[
\boxed{
\|f_j\|_2\ge c_0>0.
}
\]

This is stronger and more compactness-stable than relying only on the point value `|Omega_j(0,0)|=1`.

---

## 2. Magnitude heterogeneity functional

For any nonzero `f>=0`, define

\[
E_f=\int f^2,
\qquad
d\mu_f=\frac{f^2}{E_f}dx.
\]

Let

\[
m_f=\mathbb E_{\mu_f}[f],
\]

\[
v_f=\operatorname{Var}_{\mu_f}(f).
\]

Define

\[
\boxed{
\chi_{\rm mag}[f]
=\frac{v_f}{m_f^2}.
}
\]

The interpolation deficit is

\[
\boxed{
\mathcal R_{\rm int}[f]
\le
(1+\chi_{\rm mag}[f])^{-1/2}.
}
\]

---

## 3. Zero heterogeneity is rigid

If

\[
\chi_{\rm mag}[f]=0,
\]

then

\[
\operatorname{Var}_{\mu_f}(f)=0.
\]

Therefore there exists a constant `c>0` such that

\[
\boxed{
f=c
\quad\mu_f\text{-almost everywhere}.}
\]

Since `mu_f` has density `f^2`, this means

\[
f(x)\in\{0,c\}
\]

for almost every `x`.

A Sobolev function in `H^1` that takes values in a discrete set has weak gradient zero almost everywhere; on the connected ball it is therefore almost everywhere constant.  Since `f in H_0^1(B_R)`, the constant must be zero.

Hence

\[
\boxed{
\chi_{\rm mag}[f]=0,
\quad
f\in H_0^1(B_R)
\Longrightarrow
f\equiv0.
}
\]

---

## 4. Compact nontrivial family has a uniform gap

Let `f_j` be a sequence such that

\[
f_j\to f_\infty
\quad\text{strongly in }H^1(B_R)
\]

and

\[
\|f_j\|_2\ge c_0>0.
\]

Strong `H1` convergence gives strong `L^p` convergence for `2<=p<=6`, so the moments entering `chi_mag` converge.

Suppose for contradiction

\[
\chi_{\rm mag}[f_j]\to0.
\]

Then

\[
\chi_{\rm mag}[f_\infty]=0.
\]

The `L2` lower bound gives

\[
f_\infty\not\equiv0,
\]

contradicting the rigidity statement above.

Therefore

\[
\boxed{
\liminf_{j\to\infty}
\chi_{\rm mag}[f_j]
>0.
}
\]

Equivalently, every strongly `H1`-compact nontrivial family of such cutoff magnitudes has a uniform interpolation deficit

\[
\boxed{
\mathcal R_{\rm int}
\le1-\delta_{\rm int}
}
\]

for some family-dependent `delta_int>0`.

---

## 5. How the required strong `H1` compactness can arise

The basic velocity compactness block only gives strong local `L2` velocity convergence and is not enough here.

A stronger bounded branch includes a normalized V2 reserve

\[
\int_{Q_R}|\Delta\Omega_j|^2dyds\le M_2
\]

together with local vorticity/enstrophy bounds and the vorticity equation.

On a strictly smaller cylinder, elliptic interior estimates and time compactness can then be used to seek

\[
\boxed{
\Omega_j\to\Omega_\infty
\quad\text{strongly in }L_s^2H_y^1.
}
\]

This spacetime convergence gives strong `H1` convergence along a subsequence for almost every time.

This note does **not** claim that the required bounds hold automatically for every amplification sequence.  Failure of the V2/compactness block is a typed high-derivative branch.

---

## 6. Time-selection issue

The nonlinear source need not be near saturation at every normalized time.  Therefore a proof must still distinguish:

1. **persistent source-active times:** a positive normalized time measure on which the source approaches its critical bound; then strong spacetime compactness can select times carrying the rigidity gap;
2. **temporally intermittent source:** the near-saturation set collapses to vanishing time measure; this becomes a temporal-concentration branch and must be charged to the amplification-time / I-V / derivative channels.

Thus the remaining time problem is explicit rather than hidden.

---

## 7. Combine with angular palinstrophy

On the compact nontrivial branch, the source estimate becomes

\[
\boxed{
|Q|
\le
C_*E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4}
(1-\delta_{\rm int}).
}
\]

Therefore even if the angular fraction tends to zero, compactness/nontriviality prevents the **magnitude interpolation** factor from reaching one.

If the angular fraction is also bounded below, the two strict factors multiply.

This is stronger than the previous critical exponent comparison.

---

## 8. Source/dissipation threshold improves

In the angular-palinstrophy optimization, replacing the generic source constant by the interpolation-defpleted constant multiplies the fourth-power threshold by

\[
(1-\delta_{\rm int})^4.
\]

Equivalently, using

\[
(1+\chi_{\rm mag})^{-1/2}
\]

directly, the angular palinstrophy threshold for guaranteed viscous dominance is reduced by

\[
\boxed{
(1+\chi_{\rm mag})^{-2}.
}
\]

Thus compactness-rigidity feeds quantitatively back into the enstrophy balance.

---

## 9. Current significance

This is the first branch where the compactness-rigidity program produces a genuine logical obstruction rather than merely a reformulation:

\[
\boxed{
\text{strong compactness}
+\text{nontrivial normalized core}
+\text{interpolation saturation}
\Longrightarrow
\text{impossible cutoff limit}.
}
\]

The unresolved work is to guarantee that any bounded residual amplification sequence enters this compact persistent regime, or else to show that failure necessarily activates one of the already typed unbounded/temporal concentration channels.

Status: **ACTIVE RIGIDITY GAP / OPEN COMPACTNESS-OR-CONCENTRATION EXHAUSTION**.
