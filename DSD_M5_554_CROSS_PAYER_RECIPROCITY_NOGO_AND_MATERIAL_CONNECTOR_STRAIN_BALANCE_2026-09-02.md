# DSD M5-554 — Cross-payer reciprocity fails algebraically, but a recurrent material dual pair obeys an exact connector-compression balance

Date: 2026-09-02

Status: **PAIR-INTERACTION AUDIT AND CONNECTOR IDENTITY / M5-553 EXTRACTS A POSITIVE RECURRENT ORDERED BIOT--SAVART PAYER EDGE, BUT THE CLASSICAL VORTEX-STRETCHING KERNEL HAS NO PAIRWISE ACTION-REACTION SIGN LAW: A POSITIVE `b -> a` AXIAL-STRETCHING FACTOR CAN COEXIST WITH ZERO OR OPPOSITE-SIGN `a -> b` FACTOR / THEREFORE CROSS-PAYER RECIPROCITY CANNOT CLOSE THE GRAPH / HOWEVER THE TWO PERSISTENT MATERIAL MARKERS SATISFY AN EXACT SEPARATION ODE UNDER THE SIMILARITY MATERIAL VELOCITY `B=U+y/2`; IF THEIR COHERENT CARRIER SEPARATION REMAINS BETWEEN FIXED POSITIVE BOUNDS, RECURRENCE FORCES THE MEAN LINE-AVERAGED LONGITUDINAL STRAIN ALONG THEIR CONNECTOR TO EQUAL EXACTLY `-1/2` / THIS ADDS A UNIVERSAL COMPRESSIVE CHANNEL TO THE SAME FINITE ACTIVE CORE / IT AGAIN IMPOSES A FIXED STRAIN-SQUARE COST BUT IS NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-553

On a positive-density subsequence of productive events there is a fixed ordered source pair

\[
(a,b)
\]

such that

\[
\boxed{
q_{a\leftarrow b}
=
e_a^T\mathcal R_{strain}[W_b](x_a)e_a
\ge q_{pay}>0.
}
\]

The cross branch has

\[
a\ne b.
\]

The first question is whether the same kernel forces a controlled reverse contribution

\[
q_{b\leftarrow a}.
\]

---

## 2. Classical axial-stretching geometric factor

For a target vorticity direction `a`, a coherent source direction `b`, and source-target separation unit vector `n`, the leading directional factor in the classical singular-integral representation of the stretching factor has the form

\[
\boxed{
D(n,b,a)
=(n\cdot a)\det(n,b,a).
}
\]

The full contribution also contains the source vorticity magnitude and the `|y|^{-3}` kernel weight.

The key point for the present audit is the algebra of `D` under target/source reversal.

---

## 3. Reverse interaction factor

For the reverse target/source configuration the separation vector changes from `n` to `-n`, while source and target directions interchange.

Thus

\[
D(-n,a,b)
=(-n\cdot b)\det(-n,a,b).
\]

Using multilinearity and antisymmetry of the determinant,

\[
\det(-n,a,b)
=-\det(n,a,b)
=\det(n,b,a).
\]

Hence

\[
\boxed{
D(-n,a,b)
=-(n\cdot b)\det(n,b,a).
}
\]

while

\[
\boxed{
D(n,b,a)
=(n\cdot a)\det(n,b,a).
}
\]

Therefore, whenever the common triple product is nonzero,

\[
\boxed{
\frac{D(-n,a,b)}{D(n,b,a)}
=-\frac{n\cdot b}{n\cdot a}
}
\]

provided `n dot a` is nonzero.

There is no universal sign or size relation.

---

## 4. Explicit one-way kernel witness

Take

\[
a=e_1,
\qquad
b=e_2,
\]

and choose

\[
n=\frac{e_1-e_3}{\sqrt2}.
\]

Then

\[
n\cdot a=\frac1{\sqrt2},
\qquad
n\cdot b=0,
\]

and

\[
\det(n,b,a)\ne0.
\]

Consequently

\[
\boxed{
D(n,b,a)>0,
\qquad
D(-n,a,b)=0.
}
\]

Thus even at the exact directional-kernel level a positive one-way stretching geometry does not force a reverse stretching lower bound.

For sufficiently separated narrow coherent packets the integrated cross terms approximate this same directional algebra.

This witness is used only to rule out an algebraic reciprocity theorem based on the retained directions/separation; it is not asserted to be a complete Navier--Stokes solution.

---

## 5. Reciprocity verdict

Therefore no estimate of the form

\[
q_{a\leftarrow b}\ge q_0>0
\quad\Longrightarrow\quad
q_{b\leftarrow a}\ge c(q_0)>0
\]

or

\[
q_{b\leftarrow a}\le-c(q_0)
\]

can follow from pairwise kernel symmetry alone.

The cross-payer graph can contain genuinely directed edges.

Hence pairwise action--reaction is not the missing cycle obstruction.

---

## 6. Material-marker separation is a different shared-field observable

Now use the fact that the two persistent carrier markers are material trajectories in similarity variables.

They obey

\[
\boxed{
Y_i'
=B(Y_i,\theta)
=U(Y_i,\theta)+\frac12Y_i,
\qquad i=a,b.
}
\]

Define the connector

\[
r:=Y_a-Y_b,
\qquad
d:=|r|,
\qquad
n:=\frac r{|r|}.
\]

Then

\[
\boxed{
r'
=\frac12r+U(Y_a)-U(Y_b).
}
\]

---

## 7. Exact line-averaged velocity-gradient matrix

By the fundamental theorem of calculus along the straight connector,

\[
U(Y_a)-U(Y_b)
=
\int_0^1
\nabla U(Y_b+s r)\,r\,ds.
\]

Define

\[
\boxed{
G_{ab}(\theta)
:=
\int_0^1\nabla U(Y_b+s r,\theta)\,ds.
}
\]

Then the connector satisfies the exact finite-dimensional equation

\[
\boxed{
r'
=\left(\frac12I+G_{ab}\right)r.
}
\]

This identity uses the common Eulerian velocity field and therefore retains PDE coupling that the lineage graph omitted.

---

## 8. Exact connector-length equation

Take the scalar product with `n`.

The antisymmetric part of `G_ab` drops out.

Let

\[
\boxed{
S_{ab}
:=
\int_0^1\Sigma(Y_b+s r,\theta)\,ds.
}
\]

Then

\[
\boxed{
\frac d{d\theta}\log d
=
\frac12+n^TS_{ab}n.
}
\]

Equivalently,

\[
\boxed{
\frac d{d\theta}\log d
=
\frac12+
\int_0^1
n^T\Sigma(Y_b+s r,\theta)n\,ds.
}
\]

This is an exact connector-strain identity.

---

## 9. Why the persistent pair has two-sided separation bounds

The recurrent dual carriers have fixed-radius coherent neighborhoods and fixed angular separation.

After a harmless fixed shrinking of those neighborhoods, the two selected coherent carrier cells are disjoint on the retained pair event.

The compact core gives an upper bound

\[
d\le d_+<\infty,
\]

while disjoint fixed-radius carrier cells give

\[
\boxed{
0<d_-\le d.
}
\]

If the representation is instead allowed to merge the centers arbitrarily closely, the fixed-angle coherent-ball description breaks and must be routed to the already typed high-direction-gradient/merger branch.

Thus on the clean persistent-pair corridor

\[
\boxed{
d_-\le d(\theta)\le d_+.}
\]

---

## 10. Recurrence forces mean connector compression `-1/2`

Because `log d` is bounded on the complete recurrent pair component,

\[
\left\langle
\frac d{d\theta}\log d
\right\rangle
=0.
\]

Insert the exact connector equation.

Then

\[
\boxed{
\left\langle
n^TS_{ab}n
\right\rangle
=-\frac12.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int_0^1
n^T\Sigma(Y_b+s r)n\,ds
\right\rangle
=-\frac12.
}
\]

This number is universal: it exactly cancels the `+1/2` similarity dilation of material separation.

---

## 11. Connector direction equation

Project the connector ODE perpendicular to `n`.

The scalar dilation term drops out, giving

\[
\boxed{
n'
=(I-n\otimes n)G_{ab}n.
}
\]

Thus the pair geometry has its own projective action channel.

Either

\[
\langle|n'|\rangle>0,
\]

or the connector direction is invariant on an ergodic component.

Positive connector-direction motion is again an unsigned recurrent geometric action, not by itself a contradiction.

---

## 12. Fixed strain-square cost along the connector

At each time,

\[
|\Sigma|^2
\ge
\frac32(n^T\Sigma n)^2
\]

for a trace-free symmetric `3x3` strain tensor.

Apply Jensen first along the connector and then in invariant time:

\[
\begin{aligned}
\left\langle
\int_0^1|\Sigma(Y_b+s r)|^2ds
\right\rangle
&\ge
\frac32
\left\langle
\left(
\int_0^1 n^T\Sigma n\,ds
\right)^2
\right\rangle\\
&\ge
\frac32
\left(
\left\langle
\int_0^1 n^T\Sigma n\,ds
\right\rangle
\right)^2\\
&=
\boxed{\frac38}.
\end{aligned}
\]

Hence every recurrent bounded persistent pair carries a universal mean connector strain-square charge.

---

## 13. Thickening the connector charge

Global smooth compactness supplies uniform spatial derivative bounds for `Sigma`.

The positive line/time strain-square charge can therefore be thickened to a fixed-radius tubular neighborhood on a positive fraction of times, unless the connector passes through a vanishing-thickness geometry already typed as a frequency/gradient defect.

Thus the clean branch gives

\[
\boxed{
\left\langle
\int_{\mathcal T_{ab}}
|\Sigma|^2dy
\right\rangle
\ge c_{conn}>0.
}
\]

This is another finite-core enstrophy/strain threshold.

---

## 14. Why this still does not close

The connector compression is genuinely new and has fixed sign in invariant mean,

\[
\langle s_{conn}\rangle=-1/2.
\]

But it is not an accumulated positive scalar drift.

It is exactly the signed balance required to keep two material markers at recurrent similarity separation against the explicit similarity expansion.

A sufficiently large finite enstrophy core can pay this charge repeatedly.

Thus M5-554 produces another rigidity condition and threshold, not a contradiction.

---

## 15. Updated pair-level hard core

The recurrent cross-payer component must now satisfy simultaneously

\[
\boxed{
\begin{aligned}
&q_{a\leftarrow b}\ge q_{pay}>0
\quad\text{at positive frequency},\\
&\langle n^TS_{ab}n\rangle=-1/2,\\
&\langle Q_{core}\rangle>0,\\
&\text{dual noncollinearity and ratchet activity},\\
&\text{zero signed material-flux drift},\\
&\text{and the anchored/migration alternatives.}
\end{aligned}
}
\]

The common PDE source now carries both a positive stretching edge and a universal compressive connector channel.

---

## 16. Highest-value next target

The remaining shared-field question is not pairwise reciprocity.

It is whether the same finite-core strain field can recurrently support

1. positive parent-directed stretching;
2. universal `-1/2` connector compression;
3. noncollinear persistent vorticity directions;
4. and zero-excess anchored/migration balances;

without forcing an additional coherent source packet or a strict growth of a shape/deformation observable.

A natural next observable is the finite material **shape matrix** built from several persistent connector vectors.

For two points only, length and direction can cycle.

If the recurrent source-attribution network forces a third independent persistent marker, the similarity material volume/area evolution may provide a stronger determinant obstruction because `div B=3/2` is exact.

The alternative self-payer branch should be audited in parallel through its internal transverse reservoir.

---

## 17. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
