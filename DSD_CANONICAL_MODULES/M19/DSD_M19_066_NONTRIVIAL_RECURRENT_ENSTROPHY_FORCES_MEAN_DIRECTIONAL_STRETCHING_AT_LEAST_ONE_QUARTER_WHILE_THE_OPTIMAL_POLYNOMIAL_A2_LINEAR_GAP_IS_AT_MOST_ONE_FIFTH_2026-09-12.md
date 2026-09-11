# M19-066 — Nontrivial recurrent enstrophy forces mean directional stretching at least 1/4, while the optimal polynomial A2 linear gap is at most 1/5

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / RECURRENT-STRETCHING FIREWALL / A2 GAP OPTIMIZATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-063--065 produced a genuine pressure-compatible linear contraction geometry and reduced factor rigidity to a quantitative gap-versus-nonlinearity condition.

A natural hope was that recurrence and the existing enstrophy/palinstrophy budgets might make the nonlinear strain contribution small on average.

This module shows that nontrivial recurrence points in the opposite direction.  On any invariant recurrent measure with nonzero mean enstrophy, the enstrophy-weighted directional stretching rate is exactly

\[
\frac14+\nu\frac{\langle P\rangle}{\langle Z\rangle}
\]

and is therefore at least \(1/4\).

At the same time, the polynomial \(A_2\) weight family of M19-063 has an exactly optimizable uniform linear gap whose supremum over the full \(A_2\) range is only \(1/5\).

These two constants live in different norms and therefore do **not** by themselves form a contradiction.  They do show that a naive argument in which recurrence makes strain generically sub-gap is structurally implausible: a nonzero recurrent state must sustain positive stretching at the same similarity scale.

## 2. Invariant-measure enstrophy identity

Let \(\mu\) be an invariant probability measure on a compact complete recurrent similarity hull.  Write

\[
Z(Y):=\|\Omega_Y\|_2^2,
\qquad
P(Y):=\|\nabla\Omega_Y\|_2^2,
\]

and

\[
\mathcal S(Y)
:=
\int_{\mathbb R^3}\Omega_Y\cdot S_Y\Omega_Y\,dy.
\]

M19-065 gives the exact similarity enstrophy equation along each smooth trajectory:

\[
\boxed{
\frac12Z'
+\frac14Z
+\nu P
=\mathcal S.
}
\]

For an invariant measure, the average derivative of a sufficiently regular bounded observable vanishes:

\[
\boxed{\langle Z'\rangle_\mu=0.}
\]

Hence

\[
\boxed{
\nu\langle P\rangle_\mu
+\frac14\langle Z\rangle_\mu
=
\langle\mathcal S\rangle_\mu.
}
\]

## 3. Recurrent stretching has a positive exact lower scale

Assume the recurrent component is nontrivial in enstrophy:

\[
\boxed{\langle Z\rangle_\mu>0.}
\]

Define the enstrophy-weighted mean directional stretching rate

\[
\boxed{
\bar\sigma_\Omega
:=
\frac{\langle\mathcal S\rangle_\mu}
{\langle Z\rangle_\mu}.
}
\]

The exact invariant-measure identity gives

\[
\boxed{
\bar\sigma_\Omega
=
\frac14
+\nu
\frac{\langle P\rangle_\mu}
{\langle Z\rangle_\mu}
\ge
\frac14.
}
\]

Equality can occur only if the mean palinstrophy vanishes.  On a genuinely nonconstant vorticity state one expects strict inequality, but no uniform strict excess is asserted here.

Thus a nontrivial recurrent similarity state cannot have vanishing mean stretching in the vorticity direction.  Stretching is not merely an error term; it is required to balance the similarity damping and viscous diffusion.

## 4. A lower bound on mean L3 strain under compact-corridor amplitude bounds

Suppose, as in M19-064, that on the retained compact corridor

\[
\|\Omega\|_\infty\le M_\Omega,
\qquad
Z\le Z_*.
\]

By Holder,

\[
\mathcal S
\le
\|S\|_3\|\Omega\|_3^2.
\]

Also

\[
\|\Omega\|_3^3
\le
M_\Omega Z,
\]

so

\[
\|\Omega\|_3^2
\le
M_\Omega^{2/3}Z^{2/3}
\le
M_\Omega^{2/3}Z_*^{2/3}.
\]

Therefore

\[
\boxed{
\langle\|S\|_3\rangle_\mu
\ge
\frac{\langle\mathcal S\rangle_\mu}
{M_\Omega^{2/3}Z_*^{2/3}}
\ge
\frac{\langle Z\rangle_\mu}
{4M_\Omega^{2/3}Z_*^{2/3}}.
}
\]

This lower bound is not universal because \(\langle Z\rangle_\mu\) may be small relative to the corridor ceilings.  It nevertheless confirms that the strain norm is not forced to zero by recurrence.

## 5. Exact optimization of the polynomial A2 linear gap

Return to the M19-063 weight

\[
w(y)=(1+\kappa r^2)^{-a/2},
\qquad
\beta=\nu\kappa.
\]

Use the compact variable

\[
\boxed{t:=\frac{\kappa r^2}{1+\kappa r^2}\in[0,1).}
\]

The exact linear coefficient can be written as

\[
\boxed{
4C_{a,\beta}(t)
=
1-at
+2a\beta
\left[(a-1)t(1-t)-3(1-t)^2\right].
}
\]

For \(\beta>0\), this is a concave quadratic polynomial in \(t\).

A uniform linear gap \(c_{gap}>0\) means

\[
C_{a,\beta}(t)\le-c_{gap}
\qquad(0\le t<1).
\]

## 6. Universal upper bound inside the full A2 family

For any \(a>1\), evaluate the coefficient at

\[
\boxed{t_*:=\frac3{a+2}.}
\]

At this point the entire diffusion-dependent bracket vanishes:

\[
(a-1)t_*(1-t_*)-3(1-t_*)^2=0.
\]

Therefore, independently of \(\beta\),

\[
4C_{a,\beta}(t_*)
=1-a\frac3{a+2}
=
\frac{2(1-a)}{a+2}.
\]

Hence every member of this weight family satisfies

\[
\boxed{
 c_{gap}
\le
\frac{a-1}{2(a+2)}.
}
\]

Because the \(A_2(\mathbb R^3)\) condition requires

\[
0<a<3,
\]

we obtain the sharp family-wide ceiling

\[
\boxed{
 c_{gap}<\frac15.
}
\]

## 7. The bound is asymptotically sharp

Choose

\[
\boxed{
\beta_{opt}(a)
=\frac1{2(a-1)},
\qquad 1<a<3.
}
\]

Then the concave quadratic \(C_{a,\beta}(t)\) has its maximum exactly at

\[
t=t_*=rac3{a+2}.
\]

Consequently

\[
\boxed{
 c_{gap}^{opt}(a)
=
\frac{a-1}{2(a+2)}.
}
\]

As \(a\to3^-\),

\[
\beta_{opt}\to\frac14,
\qquad
c_{gap}^{opt}(a)\to\frac15.
\]

The endpoint \(a=3\) itself lies outside \(A_2\), so the value \(1/5\) is a supremum rather than an attained \(A_2\) gap.

This improves the merely sufficient parameter window recorded in M19-063 and gives the exact best linear gap for the whole regularized polynomial family.

## 8. Comparison with the recurrent stretching scale

The two exact constants are

\[
\boxed{
\bar\sigma_\Omega\ge\frac14,
\qquad
c_{gap}^{poly}<\frac15.
}
\]

Numerically,

\[
\frac14>\frac15.
\]

However they cannot be directly subtracted in the M19-064 difference inequality:

- \(\bar\sigma_\Omega\) is an enstrophy-weighted directional stretching average of one trajectory;
- \(c_{gap}\) is a weighted \(L^2\) velocity-difference spectral gap;
- the contraction estimate prices strain through \(L^3\) norms and universal interpolation constants.

Therefore

\[
\boxed{
\frac14>\frac15
\quad\text{is a structural firewall, not a proof of non-contraction.}
}
\]

It does show that the nonlinear stretching sustaining a nontrivial recurrent state lives at an order-one scale larger than the best available linear gap in this weight family.  Any successful contraction proof must exploit cancellation, geometry, or a quotient structure rather than simply bounding the full strain magnitude by a small number.

## 9. Consequence for the mean-gap shortcut

M19-065 asked whether existing budgets might force

\[
\overline\Lambda_{NL}<c_{gap}.
\]

The invariant-measure identity now shows why no such conclusion follows from generic recurrence:

\[
\boxed{
\text{nontrivial recurrence itself requires positive mean vortex stretching.}
}
\]

Hence the correct next target is not another unsigned upper bound on \(\|S\|\).  One must separate

\[
\boxed{
\text{stretching needed to sustain each trajectory}
}
\]

from

\[
\boxed{
\text{strain acting transversely on the difference }W.
}
\]

A relative/quotient energy or alignment cancellation may still contract differences even while each individual trajectory has large positive vortex stretching.

## 10. Certified / not certified

### Certified

1. Exact invariant-measure enstrophy balance.
2. Every nontrivial recurrent enstrophy measure satisfies
   \[
   \bar\sigma_\Omega\ge1/4.
   \]
3. Compact-corridor bounds give a positive lower estimate for mean \(L^3\) strain in terms of \(\langle Z\rangle\).
4. The exact optimal uniform linear gap of the polynomial \(A_2\) weight family is
   \[
   c_{gap}^{opt}(a)=\frac{a-1}{2(a+2)}.
   \]
5. Its \(A_2\)-admissible supremum is \(1/5\).
6. Generic small-strain averaging is therefore not a natural consequence of nontrivial recurrence.

### Not certified

1. Impossibility of every weighted contraction metric.
2. A direct contradiction from \(1/4>1/5\).
3. Cancellation of the relative strain term in the difference equation.
4. Global factor rigidity.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

M19-067 should exploit the distinction exposed here.  Instead of estimating

\[
-\int W^TS_VW\,w
\]

by the full unsigned norm \(\|S_V\|_3\), decompose the strain into the part required by the background recurrent trajectory and the part that genuinely separates two trajectories.

A natural first calculation is to quotient out the common similarity phase / scattering translation direction and derive the linearized difference equation transverse to the orbit.  If the order-one recurrent stretching lies primarily in the neutral phase direction while transverse modes see the \(<1/5\) OU gap, orbital contraction may still be possible even though absolute contraction is not.

---

\[
\boxed{\text{M19-066 COMPLETE; RECURRENT STRETCHING IS ORDER ONE AND THE POLYNOMIAL A2 GAP MAXES OUT AT 1/5.}}
\]
