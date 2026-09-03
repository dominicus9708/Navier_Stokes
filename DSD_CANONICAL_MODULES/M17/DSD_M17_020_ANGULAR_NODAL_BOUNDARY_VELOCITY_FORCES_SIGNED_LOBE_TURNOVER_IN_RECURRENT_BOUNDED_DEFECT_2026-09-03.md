# DSD M17-020 — Angular nodal-boundary velocity forces signed lobe turnover in every recurrent bounded defect

Date: 2026-09-03
Canonical ID: **M17-020**

Status: **INTERNAL LOBE HYSTERESIS COMPATIBILITY / ON A REGULAR CHI-ZERO SURFACE THE M17-017 MATERIAL EQUATION REDUCES TO `D_B chi = -T`, WHERE `T = grad_h psi dot grad_h q`. THE ZERO SURFACE THEREFORE MOVES RELATIVE TO THE MATERIAL VELOCITY WITH NORMAL SPEED `T/|grad chi|` IN THE INCREASING-CHI NORMAL. FOR A BOUNDED POSITIVE OR NEGATIVE CHI NODAL DOMAIN, REYNOLDS TRANSPORT GIVES THE EXACT VOLUME LAW `V_s' = 3/2 V_s - s int_boundary T/|grad chi|`, WHERE `s = sign chi` IN THE DOMAIN. HENCE A BOUNDED RECURRENT LOBE OF NONZERO MEAN VOLUME MUST HAVE A STRICT NONZERO SIGNED MEAN TURNOVER FLUX EQUAL TO `3/2` TIMES ITS MEAN VOLUME. IF THE COUPLING VANISHES ON THE REGULAR BOUNDARY, THE LOBE IS MATERIAL AND ITS SIMILARITY VOLUME GROWS LIKE `exp(3 theta/2)`, SO IT CANNOT REMAIN A BOUNDED RECURRENT LOBE. THE HARD BRANCH THEREFORE REQUIRES ANGULAR-BOUNDARY TURNOVER, AN UNBOUNDED DEFECT NETWORK, OR SINGULAR/FINITE-JET ZERO-SET EVENTS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material equation on the angular nodal boundary

M17-017 gives

\[
D_B\chi
=\left(\kappa-\partial_3U_3-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq.
\]

Define

\[
\boxed{
T
:=\nabla_h\psi\cdot\nabla_hq.
}
\]

On a regular angular nodal surface

\[
\chi=0,
\qquad
|\nabla\chi|>0,
\]

the multiplier term vanishes and

\[
\boxed{
D_B\chi=-T.
}
\]

Thus the motion of the zero set is controlled entirely by the shape-transfer coupling.

---

## 2. Relative normal velocity of chi = 0

Let `V_chi` denote the geometric velocity of a regular `chi=0` surface.
Along the moving surface,

\[
0
=\partial_\theta\chi+V_\chi\cdot\nabla\chi.
\]

Since

\[
D_B\chi
=\partial_\theta\chi+B\cdot\nabla\chi,
\]

we have

\[
0
=D_B\chi+(V_\chi-B)\cdot\nabla\chi.
\]

Using `D_B chi = -T`,

\[
(V_\chi-B)\cdot\nabla\chi=T.
\]

With the increasing-`chi` unit normal

\[
n_\chi:=\frac{\nabla\chi}{|\nabla\chi|},
\]

we obtain

\[
\boxed{
(V_\chi-B)\cdot n_\chi
=\frac{T}{|\nabla\chi|}.
}
\]

Therefore the angular nodal set is material exactly where

\[
\boxed{T=0.}
\]

---

## 3. Signed nodal-domain convention

Let `Omega_s(theta)` be a bounded regular nodal domain with

\[
\boxed{
s\chi>0
\quad\text{in }\Omega_s,
\qquad
s\in\{+1,-1\}.
}
\]

Its outward normal on the regular `chi=0` boundary is

\[
\boxed{
n_{out}
=-s\,n_\chi.
}
\]

Hence the zero-surface velocity relative to `B`, measured outward from the lobe, is

\[
\boxed{
(V_\chi-B)\cdot n_{out}
=-s\frac{T}{|\nabla\chi|}.
}
\]

---

## 4. Exact lobe-volume law

Let

\[
V_s(\theta):=|\Omega_s(\theta)|.
\]

Reynolds transport gives

\[
V_s'
=\int_{\partial\Omega_s}V_\chi\cdot n_{out}\,dA.
\]

Split `V_chi = B + (V_chi-B)`:

\[
V_s'
=\int_{\partial\Omega_s}B\cdot n_{out}\,dA
-s\int_{\partial\Omega_s}\frac{T}{|\nabla\chi|}\,dA.
\]

By the divergence theorem and

\[
\nabla\cdot B=\frac32,
\]

we obtain the exact law

\[
\boxed{
V_s'
=\frac32V_s
-s\int_{\partial\Omega_s}
\frac{T}{|\nabla\chi|}\,dA.
}
\]

This is the angular-lobe analogue of the material-volume expansion identities appearing earlier in M5.

---

## 5. Recurrent bounded lobe forces strict signed turnover

Assume `Omega_s(theta)` is a bounded recurrent lobe whose volume stays uniformly finite and has nonzero recurrent mean.
Then its long-time mean logarithmic/absolute drift vanishes in the recurrence average; in particular

\[
\langle V_s'\rangle=0.
\]

Therefore

\[
\boxed{
\left\langle
s\int_{\partial\Omega_s}
\frac{T}{|\nabla\chi|}\,dA
\right\rangle
=
\frac32\langle V_s\rangle
>0.
}
\]

Thus the boundary coupling has a **strict signed mean**:

- a positive-`chi` lobe requires positive mean `T/|grad chi|` in the increasing-`chi` orientation;
- a negative-`chi` lobe requires the opposite sign.

The transfer term cannot average to zero on every recurrent bounded defect boundary.

---

## 6. Material-boundary firewall

Suppose

\[
T=0
\]

on the entire regular boundary of a lobe over a time interval.
Then the boundary moves materially:

\[
V_\chi=B
\quad\text{normally on }\partial\Omega_s.
\]

The volume law reduces to

\[
\boxed{
V_s'=\frac32V_s.
}
\]

Hence

\[
\boxed{
V_s(\theta)
=V_s(\theta_0)
\exp\left[\frac32(\theta-\theta_0)\right].
}
\]

A nonzero bounded lobe with material boundary therefore cannot remain a bounded recurrent object in similarity coordinates.

Thus

\[
\boxed{
\text{bounded recurrence}
\Longrightarrow
\text{nonzero angular-boundary turnover}
}
\]

unless regularity of the `chi=0` boundary fails.

---

## 7. Branch split for the lobe geometry

A core-emergent non-axisymmetric lobe from M17-019 must therefore enter one of the following classes:

\[
\boxed{
L_{bounded}^{turnover}
\ \lor\ 
L_{unbounded}^{tail}
\ \lor\ 
L_{sing}^{chi=0}.
}
\]

### 7.1 Bounded recurrent lobe
It must realize the strict signed boundary flux

\[
\left\langle
s\int_{\partial\Omega_s}
\frac{T}{|\nabla\chi|}
\right\rangle
=\frac32\langle V_s\rangle.
\]

### 7.2 Unbounded lobe
The nodal domain reaches the far field and must be handled by a tail/localization audit.
The bounded-volume formula cannot be applied without truncation boundary terms.

### 7.3 Singular chi-zero event
If

\[
|\nabla\chi|=0
\]

on the zero set, the regular level-set velocity formula fails.
This is a finite-jet angular-zero degeneration branch and must be classified separately.

---

## 8. Relation to the kappa sign-reversal network

M17-019 gives inside every core-emergent global defect domain

\[
\kappa>0
\to
\kappa=0
\to
\kappa<0.
\]

M17-020 now shows that, if such a lobe remains bounded and recurrent, its **chi boundary itself must exchange material** through the `T` coupling.

Therefore two distinct moving zero networks coexist:

1. the internal `kappa=0` sign-reversal set;
2. the external/internal `chi=0` lobe boundary.

Their material velocities are governed by different scalar currents:

\[
\boxed{
(v_{\kappa}-B)\cdot n_\kappa
=-\frac{h}{|\nabla\kappa|},
}
\]

and

\[
\boxed{
(v_\chi-B)\cdot n_\chi
=\frac{T}{|\nabla\chi|}.
}
\]

The recurrent survivor must make these two turnover networks mutually compatible.

---

## 9. DSD interpretation

### 9.1 Boundary vs interior descriptors
M17-018/019 constrained the interior sign budget of each defect lobe.
M17-020 constrains the motion of the lobe boundary.

### 9.2 Turnover is not optional for bounded recurrence
Because the similarity material velocity has positive divergence `3/2`, a localized nonzero lobe cannot recur as the same material volume.
The `psi-q` coupling must continually replace its material content.

### 9.3 Two-current description
The hard branch now has two independent level-set currents:

\[
h=D_B\kappa
\]

for the `kappa` transition and

\[
T=\nabla_h\psi\cdot\nabla_hq
\]

for the angular-defect boundary.
Their compatibility, rather than either current alone, is the next structural target.

---

## 10. DSD audit

### Audit A — assuming chi nodal domains are material
Rejected.
They are material only where `T=0` on their regular boundary.

### Audit B — applying the bounded-volume identity to unbounded lobes
Rejected.
A localization/tail boundary term is required there.

### Audit C — dividing by |grad chi| at singular zero points
Rejected.
Those points form a separate finite-jet degeneration branch.

### Audit D — claiming turnover itself is a contradiction
Rejected.
A recurrent Eulerian structure may be maintained by continual material replacement.
The result only makes that replacement quantitatively mandatory.

### Audit E — proof status
Global regularity remains unproved.

---

## 11. Updated non-axisymmetric frontier

For every core-emergent defect lobe,

\[
\boxed{
\text{positive core}
\to
\kappa\text{-sign reversal}
\to
\begin{cases}
\text{strict angular-boundary turnover},\\
\text{unbounded tail},\\
\text{singular chi-zero event}.
\end{cases}
}
\]

The bounded recurrent subbranch must satisfy simultaneously

\[
\boxed{
\left\langle
s\int_{\partial\Omega_s}\frac{T}{|\nabla\chi|}
\right\rangle
=\frac32\langle V_s\rangle
}
\]

and the M5-685 `kappa=0` flux-weighted hysteresis condition.

---

## 12. Next target — two-zero-network compatibility

The next calculation is to analyze intersections and relative transport of

\[
\boxed{\chi=0}
\]

and

\[
\boxed{\kappa=0}
\]

using the two relative normal velocities

\[
\frac{T}{|\nabla\chi|}
\qquad\text{and}\qquad
-\frac{h}{|\nabla\kappa|}.
\]

The goal is to determine whether a compact recurrent lobe can sustain both required turnover biases without forcing

\[
\boxed{
\text{zero-set tangency/degeneration}
\ \lor\ 
\text{finite-jet reconnection}
\ \lor\ 
\text{axisymmetric firewall approach}.
}
\]

This is the **Double-Zero Network Compatibility Gate (DZNCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
