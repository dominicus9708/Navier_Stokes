# M_nonsat middle-axis locking — 2026-08-20

Status: **ACTIVE CALCULATION NOTE — POINTWISE LOCKING PROVED; SPATIAL PACKING STILL OPEN.**

This note continues `M_NONSAT_DETERMINANT_2026-08-20.md` and combines the fixed-gap branch with the A/C/M first-hitting trichotomy.

---

## 1. Conventions

Order the strain eigenvalues increasingly:

\[
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

On the positive-middle sector write

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

with

\[
m>0,
\qquad
0\le d<m.
\]

Let `e_i` be the eigenvectors and

\[
b_i=(\xi\cdot e_i)^2,
\qquad
b_1+b_2+b_3=1,
\]

where `xi` is the unit vorticity direction.

Define

\[
\Gamma=\xi^TS\xi
\]

and the strain-induced axis-conversion amplitude

\[
\chi=|P_{\xi^\perp}S\xi|.
\]

Exactly,

\[
\boxed{
\chi^2
=\xi^TS^2\xi-\Gamma^2
=\sum_{i=1}^3b_i(s_i-\Gamma)^2.
}
\]

Thus `chi` is the weighted variance of the sampled strain eigenvalue around the stretching rate `Gamma`.

---

## 2. Translate the A/C/M branch conditions

In the earlier A/C/M split, the principal extensional axis is `e_3` in the present increasing-order notation.

On the residual `M` branch:

1. `A` fails, so the vorticity is not strongly locked to `e_3`:

\[
\boxed{b_3\le\frac34.}
\]

2. `C` fails, so axis conversion is small:

\[
\boxed{
\chi<\frac{\Gamma}{4\sqrt3}.
}
\]

3. the positive middle eigenvalue is large:

\[
\boxed{
s_2\ge\frac34\Gamma>0.}
\]

Equivalently,

\[
\Gamma\le\frac43s_2.
\]

---

## 3. Compressive component is automatically tiny

Because

\[
s_1=-2m<0<\Gamma,
\]

one has

\[
|s_1-\Gamma|\ge\Gamma.
\]

The variance identity therefore gives

\[
b_1\Gamma^2
\le\chi^2
<\frac{\Gamma^2}{48}.
\]

Hence

\[
\boxed{
b_1<\frac1{48}.}
\]

Thus a low-conversion positive-stretching `M` point cannot carry appreciable vorticity along the compressive eigenvector.

---

## 4. Fixed nonsaturation forces the extensional component small as well

Take the fixed nonsaturation threshold

\[
\boxed{\frac d m\ge\frac13.}
\]

Then

\[
s_2=m-d\le\frac23m,
\qquad
s_3=m+d\ge\frac43m.
\]

Since on `M`

\[
\Gamma\le\frac43s_2,
\]

we obtain

\[
\Gamma\le\frac89m.
\]

Therefore

\[
s_3-\Gamma
\ge
\frac43m-\frac89m
=
\frac49m.
\]

Also

\[
\chi
<
\frac{\Gamma}{4\sqrt3}
\le
\frac{2m}{9\sqrt3}.
\]

Using the `b_3` contribution in the variance identity,

\[
b_3(s_3-\Gamma)^2\le\chi^2,
\]

hence

\[
\boxed{
b_3<\frac1{12}.}
\]

---

## 5. Quantitative middle-eigenvector locking

Combining

\[
b_1<\frac1{48},
\qquad
b_3<\frac1{12},
\]

with `b_1+b_2+b_3=1` gives

\[
\boxed{
b_2>\frac{43}{48}.}
\]

Equivalently,

\[
\boxed{
|\xi\cdot e_2|^2>\frac{43}{48}.
}
\]

Thus every point satisfying

- the `M` branch conditions;
- `d/m >= 1/3`;

has vorticity projectively locked to the **middle strain eigenvector**.

The projective angular defect is at most

\[
1-b_2<\frac5{48}.
\]

---

## 6. Stretching rate is also close to the middle eigenvalue

The variance identity gives

\[
b_2(s_2-\Gamma)^2\le\chi^2.
\]

Therefore

\[
|s_2-\Gamma|
\le
\frac{\chi}{\sqrt{b_2}}
<
\frac{\Gamma}{4\sqrt3}
\sqrt{\frac{48}{43}}.
\]

Thus

\[
\boxed{
|s_2-\Gamma|<c_*\Gamma,
\qquad
c_*:=\frac1{4\sqrt3}\sqrt{\frac{48}{43}}<0.153.
}
\]

In particular

\[
\boxed{
s_2>0.847\,\Gamma.}
\]

So this branch is not merely directionally close to `e_2`; the actual stretching rate is quantitatively close to the middle eigenvalue itself.

---

## 7. The middle eigenvector has a robust spectral gap

On `d/m >= 1/3`,

\[
s_3-s_2=2d\ge\frac23m,
\]

while

\[
s_2-s_1=3m-d>2m.
\]

Hence

\[
\boxed{
\operatorname{gap}(s_2)
:=
\min\{s_2-s_1,s_3-s_2\}
\ge\frac23m.
}
\]

Where `S` is differentiable and the eigenvalues are simple, the standard symmetric-matrix eigenvector derivative formula gives schematically

\[
|\nabla e_2|
\lesssim
\frac{|\nabla S|}{\operatorname{gap}(s_2)}.
\]

Thus on this branch

\[
\boxed{
|\nabla e_2|
\lesssim
\frac{|\nabla S|}{m}.
}
\]

Therefore a spatially occupied fixed-gap `M` region has only two possibilities:

1. `|nabla S|/m` is large, producing a derivative/eigenframe-bending `H` cost;
2. the middle axis `e_2` is locally coherent over the occupied region.

---

## 8. Connection to the aligned incompressibility identity

For any **constant** unit axis `n`, incompressibility gives

\[
n^TSn=\partial_nU_n=-\nabla_\perp\cdot U_\perp.
\]

Hence for a cutoff `phi` and scalar weight `rho^2`,

\[
\boxed{
\int\phi\rho^2n^TSn
=
\int\rho^2U_\perp\cdot\nabla_\perp\phi
+2\int\phi\rho U_\perp\cdot\nabla_\perp\rho.
}
\]

If the robust-gap middle eigenvector is coherent, choose `n` as the approximately constant local middle axis. Since

\[
|\xi\cdot e_2|^2>43/48
\]

and

\[
s_2\simeq\Gamma>0,
\]

the strong local stretching is then carried by a nearly middle-axis-aligned tube. The identity shows that such coherent positive axial strain must be balanced by transverse shell flux and/or transverse magnitude-interface transport.

Thus the expected routing is

\[
\boxed{
M_{nonsat}(d/m\ge1/3)
\Longrightarrow
H
\ \text{or}\ 
T/interface.
}
\]

The **pointwise locking part is proved above**. The final spatial routing still requires an occupied-neighborhood estimate controlling the errors from replacing the varying `e_2(x)` by one constant local axis.

---

## 9. Consequence for the remaining M branch

The former split

\[
M^*\to
P_{defect}^*\lor H
\quad\text{for near max-mid},
\]

or

\[
M_{nonsat}^*
\quad\text{for fixed gap}
\]

is now sharpened by taking `eta=1/3`:

### Near max-mid

\[
0\le d/m<1/3:
\]

already routed by the invariant max-mid-defect estimate to

\[
P_{defect}^*\lor H\lor G_Q\text{-visibility}.
\]

### Fixed-gap nonsaturated M

\[
d/m\ge1/3:
\]

now satisfies the quantitative middle-axis locking

\[
|\xi\cdot e_2|^2>43/48
\]

with a robust eigenvalue gap, and is therefore reduced to a local axis-coherence/transport estimate.

---

## 10. Next target

Prove a weighted local constant-axis replacement lemma:

If on a bounded normalized ball

- `s_2 >= c > 0` on an occupied subregion;
- `d/m >= 1/3`;
- `|xi . e_2|^2 >= 43/48`;
- the derivative/eigenframe cost is below the `H` threshold;

then there exists a constant axis `n` on a smaller ball for which

\[
\int\phi\rho^2 n^TSn
\]

retains a fixed fraction of the middle-strain stretching action. The exact aligned identity would then force a fixed transverse flux/interface cost, routing the branch to bounded-radius `T` unless `H` is activated.

Status: **FIXED-GAP M BRANCH POINTWISE LOCKED TO THE MIDDLE STRAIN AXIS; REMAINING GAP = LOCAL CONSTANT-AXIS REPLACEMENT/PACKING.**