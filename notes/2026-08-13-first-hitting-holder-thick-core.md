# Bounded first-hitting windows produce a uniform terminal thick core

Date: 2026-08-13

Status: **LOCAL PARABOLIC-SMOOTHING BRIDGE / THICK-CORE CONSEQUENCE ON THE BOUNDED NORMALIZED-ENSTROPHY BRANCH**.

The first-hitting normalization gives `||Omega||_infinity<=1` on the whole backward amplification interval.  If normalized global enstrophy is also bounded and the interval has nonzero normalized length, local parabolic smoothing gives a uniform spatial Hölder modulus at the terminal checkpoint.  The normalized maximum one then occupies a fixed positive-volume neighborhood rather than only a point.

Classical external context: Grujic and Kukavica, *Space Analyticity for the Navier--Stokes and Related Equations with Initial Data in L^p*, J. Functional Analysis 152 (1998), 447--466, DOI 10.1006/jfan.1997.3167, gives substantially stronger spatial analyticity estimates.  The present route only needs a weaker local Hölder consequence.

---

## 1. First-hitting bounded block

Normalize by the later first-hitting checkpoint so that on a fixed backward interval

\[
[-\delta_0,0]
\]

we have

\[
\boxed{
\|\Omega(s)\|_\infty\le1.
}
\]

Assume

\[
\boxed{
\sup_{-\delta_0\le s\le0}
\|\Omega(s)\|_2^2
\le M_E.
}
\]

Choose a fixed normalized ball `B_R`, `R>2`.

---

## 2. Bounded local drift after removing mean transport

For every finite `p>=2`, interpolation gives

\[
\|\Omega(s)\|_p\le M_E^{1/p}.
\]

The Biot--Savart/Riesz relation yields

\[
\|\nabla U(s)\|_p
\le C_pM_E^{1/p}.
\]

Choose `p>3`.  Poincare--Morrey on `B_R` gives

\[
\boxed{
\|U-(U)_{B_R}\|_{L^\infty(B_R)}
\le C_{p,R}M_E^{1/p}.
}
\]

A time-dependent spatially constant velocity is removed by the already-developed mean-flow/Galilean moving frame.  Vorticity is unchanged by this translation.

Thus the local drift in the normalized vorticity equation is uniformly bounded.

---

## 3. Conservative vorticity form

Because

\[
\nabla\cdot U=0,
\qquad
\nabla\cdot\Omega=0,
\]

we may write

\[
\boxed{
\partial_s\Omega-
u\Delta\Omega
=
\nabla\cdot
(\Omega\otimes U-U\otimes\Omega).
}
\]

After multiplying by a fixed cutoff supported in `B_R`, the localized equation has the form

\[
\partial_s(\chi\Omega)-\nu\Delta(\chi\Omega)
=
\nabla\cdot F_1+F_0,
\]

where, on a smaller fixed ball and after mean-frame subtraction,

\[
\|F_1\|_\infty
+\|F_0\|_p
\le C(M_E,R,p,\nu)
\]

using the amplitude, drift, and cutoff bounds.  The exact cutoff terms are lower order and live away from the core.

---

## 4. Heat-kernel Hölder smoothing

For the heat semigroup in three dimensions,

\[
\|\Lambda^\alpha e^{\nu\tau\Delta}f\|_\infty
\le
C_{\alpha,\nu}
\tau^{-\alpha/2}
\|f\|_\infty,
\]

and for one-divergence forcing,

\[
\|\Lambda^\alpha
\nabla e^{\nu\tau\Delta}F\|_\infty
\le
C_{\alpha,\nu}
\tau^{-(1+\alpha)/2}
\|F\|_\infty.
\]

The latter time singularity is integrable for every

\[
\boxed{0<\alpha<1.}
\]

Applying Duhamel on a positive time gap, e.g. from `-delta0/2` to `0`, yields on `B_1`

\[
\boxed{
[\Omega(\cdot,0)]_{C^\alpha(B_1)}
\le
C(M_E,R,\nu,\delta_0,\alpha).
}
\]

The exact value of the constant is irrelevant to the structural argument; only uniformity over the bounded normalized branch is needed.

---

## 5. Uniform thick terminal core

Choose the normalized center so

\[
|\Omega(0,0)|=1.
\]

Let

\[
H_\alpha
=[\Omega(\cdot,0)]_{C^\alpha(B_1)}.
\]

For

\[
|y|\le
r_*:=\min\left\{
\frac12,
(2H_\alpha)^{-1/\alpha}
\right\},
\]

we have

\[
|\Omega(y,0)-\Omega(0,0)|
\le H_\alpha|y|^\alpha
\le\frac12.
\]

Hence

\[
\boxed{
|\Omega(y,0)|\ge\frac12
\qquad(|y|\le r_*).
}
\]

Therefore

\[
\boxed{
\left|
\{y\in B_1:|\Omega(y,0)|\ge1/2\}
\right|
\ge
\frac{4\pi}{3}r_*^3
=:\theta_*>0.
}
\]

The lower volume fraction depends only on the bounded normalized state parameters, not on the amplification index.

---

## 6. Consequences

On the bounded first-hitting normalized-enstrophy branch:

1. terminal nontriviality is a fixed positive-volume `L2` statement, not only a point value;
2. the compactness limit cannot lose the dangerous endpoint solely by spatial concentration at one point;
3. a terminal sparseness escape below `r_*` is unavailable;
4. the projective/polarity/multicore descriptors have a genuinely non-negligible terminal core on which to act.

If such a uniform Hölder/thick-core conclusion fails, one of the bounded-block inputs -- normalized global enstrophy, noncollapsed time, or local mean-frame drift/control -- must fail and is already a typed concentration/deformation branch.

---

## 7. Important scope

This does **not** prove that the intense set remains thick for every earlier time in the amplification window.  It supplies a uniform thick core at the terminal first-hitting checkpoint, and the temporal-enstrophy gate supplies a positive persistence time under bounded source/shell channels.

Status: **TERMINAL THICK CORE DERIVED ON THE BOUNDED FIRST-HITTING BRANCH**.
