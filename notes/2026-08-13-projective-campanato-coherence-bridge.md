# Projective Campanato bridge: from dense-core covariance decay to pointwise vorticity-direction coherence

Date: 2026-08-13

Status: **DERIVED CONDITIONAL CAMPANATO BRIDGE + EXTERNAL GEOMETRIC REGULARITY ANCHOR / GLOBAL REGULARITY NOT PROVED**.

This note upgrades uniform multiscale decay of the local projective covariance defect to pointwise projective Hölder coherence on a volumetrically thick intense-vorticity set.

The result closes a conceptual gap between the averaged covariance descriptor and the pointwise vorticity-direction geometry used in the Constantin--Fefferman / Beirao da Veiga--Berselli regularity line.

## 1. Projective direction matrix

On the nonzero-vorticity set define

\[
\xi=\omega/|\omega|,
\]

and the sign-invariant rank-one projector

\[
\boxed{
P_\xi=\xi\otimes\xi.
}
\]

Then

\[
\boxed{
\|P_\xi(x)-P_\xi(y)\|_F^2
=2[1-(\xi(x)\cdot\xi(y))^2]
=2|\xi(x)\times\xi(y)|^2.
}
\]

Thus Hölder regularity of `P_xi` is exactly projective vorticity-direction coherence and treats parallel/antiparallel directions identically.

## 2. Thick intense-vorticity set

Fix a time and let

\[
H\subset\{x:|\omega(x)|\ge aW\},
\qquad
W=\|\omega\|_\infty,
\qquad
0<a<1.
\]

Assume a quantitative thickness condition: there are

\[
\theta>0,
\qquad
r_0>0
\]

such that for every `x in H` and `0<r<=r_0`,

\[
\boxed{
|H\cap B_r(x)|
\ge\theta |B_r|.
}
\]

If this condition fails strongly at a dangerous point/scale, the active route returns to the occupancy/line-sparseness branch instead of using the present lemma.

## 3. Restricted pairwise projective oscillation

Let

\[
H_{x,r}=H\cap B_r(x).
\]

Define

\[
\boxed{
\mathcal O_{H}(x,r)
=\frac1{|H_{x,r}|^2}
\iint_{H_{x,r}\times H_{x,r}}
[1-(\xi(y)\cdot\xi(z))^2]dydz.
}
\]

The projector identity and the variance formula give

\[
\boxed{
\mathcal O_H(x,r)
=
\fint_{H_{x,r}}
\|P_\xi-(P_\xi)_{H_{x,r}}\|_F^2.
}
\]

## 4. Control the restricted oscillation by the smooth local covariance defect

Use the positive Student-type kernel `eta_r` from the local covariance lemma. On a fixed inner ratio `|y-x|<=c r`,

\[
\eta_r(x-y)\ge c_\eta r^{-3}.
\]

For simplicity absorb the fixed inner-ratio constant into `theta` and write the local set at the comparable scale as `H_{x,r}`.

The smooth projective numerator is

\[
E_r(x)^2J_r(x)
=
\iint
\eta_r(x-y)\eta_r(x-z)
|\omega(y)\times\omega(z)|^2dydz.
\]

On `H`,

\[
|\omega|\ge aW.
\]

Also, because the kernel is normalized and `|omega|<=W`,

\[
E_r(x)\le W^2.
\]

Therefore

\[
\begin{aligned}
J_r(x)
&\ge
c_\eta^2 a^4 r^{-6}
\iint_{H_{x,r}\times H_{x,r}}
[1-(\xi(y)\cdot\xi(z))^2]dydz.
\end{aligned}
\]

Using

\[
|H_{x,r}|\ge c\theta r^3,
\]

we obtain

\[
\boxed{
\mathcal O_H(x,r)
\le
C_{\eta,a,\theta}J_r(x).
}
\]

Thus smooth-kernel covariance control gives an ordinary projective Campanato oscillation bound on every thick intense-core ball.

## 5. Campanato decay implies projective Hölder coherence

Assume that for some

\[
0<\alpha\le1
\]

and every `x in H`, `0<r<=r_0`,

\[
\boxed{
J_r(x)
\le M^2r^{2\alpha}.
}
\]

Then

\[
\mathcal O_H(x,r)
\le
C M^2r^{2\alpha}.
\]

A direct Campanato telescoping argument on the uniformly thick set `H` gives a representative of `P_xi` satisfying

\[
\boxed{
\|P_\xi(x)-P_\xi(y)\|_F
\le
C_{\eta,a,\theta,\alpha}
M|x-y|^\alpha
}
\]

for `x,y in H` at sufficiently small separation.

### Sketch of the telescoping argument

The thickness assumption gives uniform doubling of the restricted Lebesgue measure on `H`:

\[
|H\cap B_{2r}(x)|
\le
\frac{8}{\theta}
|H\cap B_r(x)|.
\]

The `L^2` oscillation bound implies that averages of `P_xi` on nested radii `r, r/2, r/4,...` differ by `O(M r^alpha)`. Summing the geometric series gives convergence to `P_xi(x)` at density points with the same rate.

For two nearby points, compare both small-ball averages to the average on a common larger restricted ball. Uniform thickness controls the measure ratios and yields the Hölder estimate above.

## 6. Convert projector Hölder control to direction coherence

Since

\[
|\xi(x)\times\xi(y)|
=\frac1{\sqrt2}
\|P_\xi(x)-P_\xi(y)\|_F,
\]

we obtain

\[
\boxed{
|\xi(x)\times\xi(y)|
\le
C M|x-y|^\alpha.
}
\]

For the critical exponent

\[
\boxed{\alpha=\frac12,}
\]

this is the familiar projective `1/2`-Hölder vorticity-direction coherence scale appearing in the established geometric-depletion regularity theory.

Therefore, when all hypotheses needed by the relevant external theorem are satisfied on its high-vorticity region, the branch

\[
\boxed{
J_r(x)\lesssim r
\quad\text{uniformly on a thick intense core}
}

feeds the classical regularity gate rather than remaining an open covariance-only condition.

## 7. Dense/sparse/projective trichotomy sharpened

At a dangerous point and scale, the intense set now has three structurally different possibilities.

### A. Sparse branch

The thickness condition fails strongly.

This feeds the existing volume-to-line-sparseness / harmonic-measure regularity track.

### B. Thick and projectively coherent branch

The set remains thick and

\[
\sup_{x\in H,\,r\le r_0}
\frac{J_r(x)}{r^{2\alpha}}
<\infty
\]

with a coherence exponent sufficient for an external geometric regularity criterion.

Then the covariance field upgrades to pointwise projective Hölder coherence.

### C. Thick and projectively rough branch

The set remains thick but the scale-normalized covariance defect is unbounded or non-small:

\[
\boxed{
\sup
\frac{J_r(x)}{r^{2\alpha}}
=\infty
}

along dangerous small scales.

This is the genuinely residual geometric branch. It must sustain direction disorder at the same scales where occupancy remains large.

## 8. Relation to the small-scale limit

At smooth nonzero-vorticity points,

\[
J_r
\sim2m_\eta r^2|\nabla\xi|^2.
\]

Thus the `alpha=1` Campanato regime corresponds to bounded direction gradient.

The weaker critical `alpha=1/2` condition permits

\[
|\nabla\xi|
\sim r^{-1/2}
\]

at the scale level, consistent with the known half-Hölder depletion threshold.

This shows that the covariance route naturally interpolates between smooth axis-field control and the critical geometric coherence scale.

## 9. Remaining open branch

The residual singularity candidate must now keep the intense region sufficiently non-sparse **and** violate the projective Campanato decay needed for the coherence gate.

That failure means `J_r` remains too large relative to the physical scale. The active question becomes whether such persistent projective roughness necessarily forces enough

\[
P_\phi J_\phi^2
\]

in the adjoint-window inequality, or enough direction-gradient/palinstrophy cost, to contradict the remaining finite spacetime budgets.

Status: **OPEN THICK-ROUGH PROJECTIVE BRANCH**.
