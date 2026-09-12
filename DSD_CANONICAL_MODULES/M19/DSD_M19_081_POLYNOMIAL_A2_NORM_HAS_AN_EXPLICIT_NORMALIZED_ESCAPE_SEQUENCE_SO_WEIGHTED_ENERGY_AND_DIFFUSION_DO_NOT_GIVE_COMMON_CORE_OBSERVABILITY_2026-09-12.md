# DSD M19-081 — The polynomial A2 norm has an explicit normalized escape sequence, so weighted energy and diffusion do not give common-core observability

Date: 2026-09-12

Status: **NO-ESCAPE AUDIT / FOR EVERY 1<a<3 IN THE PRESSURE-COMPATIBLE POLYNOMIAL A2 FAMILY THERE IS AN EXPLICIT DIVERGENCE-FREE ANNULAR SEQUENCE WITH UNIT WEIGHTED L2 MASS, VANISHING WEIGHTED GRADIENT COST, VANISHING POINTWISE AMPLITUDE, AND SUPPORT ESCAPING TO INFINITE SIMILARITY RADIUS / THEREFORE THE RADIAL A2 NORM IS COERCIVE FOR THE LOCAL EVOLUTION IDENTITY BUT IS NOT SPATIALLY TIGHT / BOUNDED WEIGHTED ENERGY PLUS DIFFUSION CANNOT FORCE A COMMON COMPACT CORE FOR CENTER WITNESSES / ANY OBSERVABILITY THEOREM MUST USE THE PDE RECURRENT REALIZATION, NOT THE FUNCTION SPACE NORM ALONE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Question

M19-080 reduced the center-dimension problem to a common-core observability issue.

Can the polynomial A2 norm from M19-063 itself force every normalized center witness to keep a fixed fraction of its mass in one compact similarity ball?

The answer is no.

---

## 2. Weight asymptotics

Use

\[
w(y)=(1+\kappa|y|^2)^{-a/2},
\qquad 1<a<3.
\]

For \(|y|\sim R\gg1\),

\[
\boxed{
w(y)\asymp R^{-a}.}
\]

The range \(a<3\) is exactly the upper A2 restriction in three dimensions.

---

## 3. Divergence-free annular profile

Choose a nonzero smooth divergence-free vector field

\[
F\in C_c^\infty(\{1<|z|<2\};\mathbb R^3),
\qquad \nabla_z\cdot F=0.
\]

For \(R\gg1\), define

\[
\boxed{
W_R(y)
:=c_RR^{-1}F(y/R),
\qquad
c_R:=R^{(a-1)/2}.
}
\]

Then

\[
\nabla_y\cdot W_R=0
\]

and

\[
\operatorname{supp}W_R
\subset\{R<|y|<2R\}.
\]

Thus the support escapes every fixed compact set as \(R\to\infty\).

---

## 4. Weighted L2 mass stays order one

On the annulus \(|y|\sim R\),

\[
|W_R|^2
\sim c_R^2R^{-2}|F(y/R)|^2.
\]

Using \(dy=R^3dz\) and \(w(Rz)\asymp R^{-a}\),

\[
\begin{aligned}
\|W_R\|_{L^2(w)}^2
&\asymp
c_R^2R^{-2}R^3R^{-a}
\int|F(z)|^2dz\\
&=c_R^2R^{1-a}\|F\|_2^2.
\end{aligned}
\]

Since

\[
c_R^2=R^{a-1},
\]

we get

\[
\boxed{
\|W_R\|_{L^2(w)}^2
\asymp
\|F\|_2^2
\asymp1.
}
\]

After one fixed normalization of \(F\), the weighted mass may be taken asymptotically equal to one.

---

## 5. Weighted gradient cost vanishes

Differentiate:

\[
\nabla W_R
=c_RR^{-2}(\nabla F)(y/R).
\]

Therefore

\[
\begin{aligned}
\|\nabla W_R\|_{L^2(w)}^2
&\asymp
c_R^2R^{-4}R^3R^{-a}
\|\nabla F\|_2^2\\
&=c_R^2R^{-1-a}
\|\nabla F\|_2^2\\
&=R^{a-1}R^{-1-a}
\|\nabla F\|_2^2.
\end{aligned}
\]

Hence

\[
\boxed{
\|\nabla W_R\|_{L^2(w)}^2
\asymp R^{-2}
\to0.
}
\]

Thus even a uniform weighted H1 bound does not prevent complete radial escape.

---

## 6. Pointwise amplitude also vanishes

The amplitude satisfies

\[
\|W_R\|_\infty
\lesssim
c_RR^{-1}\|F\|_\infty
=R^{(a-3)/2}\|F\|_\infty.
\]

Because

\[
a<3,
\]

we obtain

\[
\boxed{
\|W_R\|_\infty\to0.
}
\]

Therefore the escape sequence does not rely on pointwise blow-up.

It hides unit weighted mass in an increasingly large annulus by exploiting volume against the polynomially decaying weight.

---

## 7. No common-core lower bound can follow from these norms

For every fixed \(K<\infty\),

\[
\boxed{
\int_{|y|<K}|W_R|^2w\,dy=0
}
\]

for all sufficiently large \(R\).

At the same time,

\[
\|W_R\|_{L^2(w)}\asymp1,
\qquad
\|\nabla W_R\|_{L^2(w)}\to0.
\]

Hence there is no estimate of the form

\[
\boxed{
\int_{|y|<K}|W|^2w\,dy
\ge c_K\|W\|_{L^2(w)}^2
}
\]

valid for all divergence-free fields controlled only by weighted L2 and weighted H1.

---

## 8. Compatibility with the weighted OU gap

At first sight the vanishing gradient cost might seem to contradict the positive OU gap from M19-063.

It does not.

The positive gap comes from the full similarity drift-plus-weight identity, not from a Poincare inequality based only on \(\nabla W\).

For an outward-translated annular packet, the radial drift crosses the nontranslation-invariant weight and generates the missing coercive contribution.

Thus

\[
\boxed{
\text{weighted OU coercivity}
\neq
\text{spatial tightness}.
}
\]

This distinction is essential.

---

## 9. Relation to q-translation escape

The annulus \(|y|\sim R\) corresponds to

\[
q\sim\log R-\theta/2.
\]

Therefore the explicit sequence \(W_R\) is the static functional-space analogue of shifting a perturbation packet to larger q/log-radius.

The normalization factor

\[
R^{(a-1)/2}
\]

exactly compensates the decay of the polynomial weight.

Hence the same log-radius translation noncompactness seen in M19-072 and M19-078 is present inside the M19-063 weighted space itself.

---

## 10. Rotation-transverse compatibility

The profile \(F\) can be chosen from an infinite-dimensional divergence-free annular subspace.

Finite-dimensional orthogonality conditions against rotation tangents and the time tangent can therefore be imposed by taking suitable linear combinations without destroying the scaling estimates.

Thus finite-codimensional symmetry projection does not remove the escape mechanism.

---

## 11. What this does and does not prove

M19-081 proves a functional-space firewall:

\[
\boxed{
\text{bounded }E_w+G_w
\not\Rightarrow
\text{common-core observability}.
}
\]

It does **not** construct an exact complete linearized Navier--Stokes center solution with this escape behavior.

The actual PDE may still forbid such sequences through recurrence, pressure, or interior-tail coupling.

Therefore the remaining theorem must be PDE-specific.

---

## 12. Revised observability target

A useful estimate must involve the equation, for example

\[
\boxed{
\text{complete zero-exponent cocycle solution}
\Longrightarrow
\text{positive recurrent mass in a fixed spectator/core annulus},
}
\]

rather than a bare weighted Sobolev embedding.

Equivalently, failure of such observability should be shown to produce an exact passive critical scattering mode that can then be attacked by the factor theorem.

---

## 13. Next calculation

M19-082 should derive an equation-level concentration-compactness dichotomy for a normalized complete center witness:

1. recurrent tightness in a fixed similarity annulus; or
2. radial escape of its weighted mass.

The radial-escape branch should then be rescaled around its moving radius and compared with the formal critical tail center of M19-068.

If that blow-down limit is forced to solve the pure dilation transport equation, the center problem may split cleanly into an interior tight branch and the already identified scattering-factor branch.
