# Advection H gate: strain-gradient compression and non-collinear Fourier triads

Date: 2026-08-19

Status: **DERIVED EXACT ADVECTION IDENTITY + TRIAD ANGULAR CERTIFICATE / GLOBAL REGULARITY NOT PROVED**.

This note sharpens the remaining advection-saturated `H/T` branch.

---

## 1. H1 strain energy and the vorticity orthogonality anchor

For the strain equation

\[
\partial_tS-\nu\Delta S
+(u\cdot\nabla)S
+S^2
+\frac14\omega\otimes\omega
-\frac14|\omega|^2I
+\operatorname{Hess}p=0,
\]

the 2024/2026 Miller identity gives

\[
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0.
}
\]

Thus direct vorticity feedback does not drive the `H1` strain norm.

After pairing with `-Delta S`, the dangerous `H1` production is carried by advection and strain self-interaction, modulo the strain projection/pressure representation.

---

## 2. Exact advection-gradient identity

For incompressible `u`, integration by parts gives

\[
\begin{aligned}
\langle (u\cdot\nabla)S,-\Delta S\rangle
&=
\sum_{k,a,b}
\int
\partial_k(u_j\partial_jS_{ab})
\partial_kS_{ab}\,dx\\
&=
\sum_{k,j,a,b}
\int
(\partial_ku_j)(\partial_jS_{ab})(\partial_kS_{ab})\,dx.
\end{aligned}
\]

The term with `u_j partial_j partial_k S_ab` vanishes by incompressibility.

For each tensor component define

\[
g^{ab}=\nabla S_{ab}.
\]

Since the skew part of `nabla u` vanishes in a quadratic form,

\[
\boxed{
\langle (u\cdot\nabla)S,-\Delta S\rangle
=
\sum_{a,b}\int (g^{ab})^TSg^{ab}\,dx.
}
\]

Because the strain equation contributes this term with the opposite sign to the time derivative of `||nabla S||_2^2`, **advection-driven H1 growth occurs through compression of strain gradients**.

In the strain eigenframe,

\[
(g^{ab})^TSg^{ab}
=
\sum_{i=1}^3\lambda_i|g_i^{ab}|^2.
\]

Hence positive advection contribution to H1 growth favors gradient energy in the negative/compressive eigenframe, especially `e_1`.

---

## 3. Cross-axis consequence on the near-saturated M geometry

The near-saturated determinant geometry has

\[
\lambda_1\simeq-\lambda_3,
\qquad
\lambda_2\simeq0^+.
\]

The surviving vortex-stretching alignment subbranch favors vorticity close to the principal extensional axis `e_3`.

The identity above shows that simultaneous advection-driven derivative growth favors strain-gradient energy close to the principal compressive axis `e_1`.

Thus a joint near-saturated `M` + advection-`H` survivor has the typed cross-axis structure

\[
\boxed{
\omega\ \text{primarily along }e_3,
\qquad
\nabla S\ \text{primarily along }e_1.
}
\]

This is not a contradiction; it is a filament/sheet-like anisotropic certificate that should be tested against geometric sparseness and local concentration criteria.

---

## 4. Fourier triad angular factor

For a Fourier mode `p`, incompressibility gives

\[
p\cdot\widehat u(p)=0.
\]

The Fourier coefficient of the advection interaction contains factors of the form

\[
\widehat u(p)\cdot q.
\]

Let `theta_{pq}` be the angle between nonzero wavevectors `p` and `q`. Since `u_hat(p)` is perpendicular to `p`,

\[
\boxed{
|\widehat u(p)\cdot q|
\le
|\widehat u(p)|\,|q|\,|\sin\theta_{pq}|.
}
\]

Therefore exactly collinear Fourier interactions do not generate the advective derivative transfer.

A nearly one-directional high-frequency state carries an angular depletion factor. Advection-saturated `H` consequently requires a non-negligible population of non-collinear triads or a compensating growth of amplitudes.

---

## 5. DSD angular channel

This suggests retaining an explicit derivative-triad angular channel, schematically

\[
\boxed{
\mathcal A_{\rm triad}
\sim
\frac{
\sum_{p+q=k}
|\widehat u(p)|\,|q|\,|\widehat S(q)|
|\sin\theta_{pq}|
}{
\text{corresponding unweighted convolution}
}.
}
\]

`A_triad -> 0` is an advection-depletion regime.

A dangerous high-derivative sequence must instead keep

\[
\boxed{
\mathcal A_{\rm triad}\not\to0
}
\]

or compensate the angular loss by stronger amplitude/derivative concentration.

This is a genuine off-diagonal directional interaction channel; it is not equivalent to merely increasing derivative order.

---

## 6. Revised hard survivor

After the August 19 reductions, the difficult compact branch is more specifically

\[
\boxed{
\begin{gathered}
\text{non-saturated critical middle-strain production},
\quad\text{or}\\
\text{near-planar }(\lambda_1\simeq-\lambda_3,\lambda_2\simeq0^+)\\
+\ \omega/e_3\text{ extension alignment}\\
+\ \nabla S/e_1\text{ compression alignment}\\
+\ \text{non-collinear derivative triad saturation}.
\end{gathered}
}
\]

The next useful theorem would bound the advective `H1` production by a quantitative angular/projective dispersion defect, with a strict gain when the high-derivative Fourier support or physical gradient covariance becomes nearly one-directional.

Status: **ADVECTION H RECLASSIFIED AS COMPRESSIVE STRAIN-GRADIENT AMPLIFICATION WITH A NON-COLLINEAR TRIAD REQUIREMENT; ANGULAR DISPERSION CLOSURE OPEN**.
