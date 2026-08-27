# DSD M5-85 — Uniform Higher Tangential Factor on the Returned W1 Pump Cell

Date: 2026-08-27

Status: **LOCALIZATION + ANALYTICITY CLOSURE / THE HIGHER FACTOR `M_tan,2` FROM M5-84 IS UNIFORMLY BOUNDED ON THE FIXED POSITIVE-AMPLITUDE RETURNED PUMP CELL / THEREFORE EVERY MINIMAL-PAYER SATURATING W1 RETURN HAS VANISHING COMPONENT-FREE TANGENTIAL DEFECT / REMOTE TAIL AND COMPONENT FRAGMENTATION NO LONGER BLOCK THIS PASSAGE / EXACT ENDPOINT NONEXISTENCE STILL OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the returned pump construction

M5-57 fixes one smooth amplitude weight

\[
w=w_{\delta_*}
\]

with compact support in a positive normalized band

\[
\boxed{
\operatorname{supp}w
\subset
I=[\lambda_-,\lambda_+]
\Subset(0,\infty).
}
\]

The W1 critical tail decays like `1/r` in the normalized cell. Consequently, after choosing a sufficiently large normalized radius `R_w`,

\[
\boxed{
|Y|>R_w
\Longrightarrow
|U(Y,s)|<\lambda_-/2
}
\]

uniformly on every returned pump segment in the retained compact W1 phase neighborhood.

Hence

\[
\boxed{
w(|U(Y,s)|)=0
\quad\text{for }|Y|>R_w.}
\]

Thus every M5-83/M5-84 weighted integral is supported in the fixed compact cylinder

\[
K_w
:=
B_{R_w}\times I_{time},
\]

where `I_time` is one fixed normalized pump interval.

This is exactly the fixed active phase-cell localization already used in M5-57.

---

## 2. No small-amplitude singularity

On the support of the weight,

\[
a:=|U|\ge\lambda_->0.
\]

Therefore

\[
b
:=
U\cdot\nabla\log a
=
\frac{U\cdot\nabla a}{a}
\]

and all finite spatial derivatives of `b` are smooth expressions in finite derivatives of `U`, with denominators bounded by powers of `lambda_-`.

The logarithmic amplitude therefore creates no singular coefficient on the returned pump cell.

---

## 3. W1 local analytic bounds

The W1 compact recurrent class has uniform local analytic bounds on every fixed bounded space-time cylinder.

Hence, after fixing `K_w`, for every finite integer `m` required below there exists

\[
C_m(K_w)<\infty
\]

such that every returned pump segment satisfies

\[
\boxed{
\sup_{K_w}
|\nabla_Y^\alpha\partial_s^jU|
\le
C_m
\qquad
(|\alpha|+2j\le m).
}
\]

The exact indexing of time versus space derivatives is immaterial here; only finitely many derivatives are used.

By the Leray Navier--Stokes equation the same local smooth control applies to the pressure gradient modulo its irrelevant time-dependent gauge.

---

## 4. Velocity-only expression for the first q derivative

Recall

\[
q:=P-2\nu b.
\]

M5-82 gives

\[
\boxed{
\nabla q=Z_L,
}
\]

where

\[
Z_L
=
\nu\Delta U
-\partial_sU
-U\cdot\nabla U
-\frac12Y\cdot\nabla U
-\frac12U
-2\nu\nabla b.
\]

Therefore `Z_L` and `grad Z_L` are controlled on `K_w` solely by finitely many local derivatives of `U` and the positive lower amplitude bound.

Thus there are finite constants

\[
\boxed{
\|Z_L\|_{L^\infty(K_w)}\le C_Z,
\qquad
\|\nabla Z_L\|_{L^\infty(K_w)}\le C_{\nabla Z}.
}
\]

No global pressure norm is needed.

---

## 5. Expand the second tangential derivative

For `i<j`, write

\[
L_{ij}=V_{ij}\cdot\nabla,
\]

with

\[
V_{ij}
=(\partial_i a)e_j-(\partial_j a)e_i.
\]

Since

\[
L_{ij}q=V_{ij}\cdot Z_L,
\]

we obtain

\[
\begin{aligned}
L_{ij}^2q
&=
V_{ij}\cdot\nabla(V_{ij}\cdot Z_L)\\
&=
(V_{ij}\cdot\nabla V_{ij})\cdot Z_L
+
(V_{ij}\otimes V_{ij}):\nabla Z_L.
\end{aligned}
\]

Therefore pointwise

\[
\boxed{
|L_{ij}^2q|
\le
C\Bigl(
|\nabla a|\,|\nabla^2a|\,|Z_L|
+
|\nabla a|^2|\nabla Z_L|
\Bigr).
}
\]

All factors on the right are uniformly bounded on `K_w` by W1 local analyticity.

Hence

\[
\boxed{
\sup_{K_w}|L_{ij}^2q|
\le C_{tan,2}<\infty
}
\]

uniformly over every returned W1 pump segment.

---

## 6. Weighted L2 bound

The M5 weight is

\[
d\mu=a\,w(a)dY.
\]

On `K_w`,

\[
0\le a\,w(a)
\le
\lambda_+\|w\|_\infty.
\]

Since `B_{R_w}` has finite volume,

\[
\begin{aligned}
\|L_{ij}^2q\|_{L^2(d\mu)}^2
&\le
\lambda_+\|w\|_\infty
|B_{R_w}|
C_{tan,2}^2.
\end{aligned}
\]

Therefore the M5-84 higher factor

\[
M_{tan,2}
:=
\left(
\sum_{i<j}
\|L_{ij}^2q\|_{L^2(d\mu)}^2
\right)^{1/2}
\]

obeys the uniform returned-pump estimate

\[
\boxed{
M_{tan,2}
\le
M_*<\infty.
}
\]

The constant depends only on the fixed W1 pump cell, the fixed amplitude weight, viscosity, and the compact-class analytic bounds; it does not depend on the return number.

---

## 7. Near-minimal payer now forces the local tangential defect to zero

M5-84 proved

\[
\int
|\nabla a\times Z_L|^2d\mu
\le
\sqrt3\,
M_{tan,2}
\mathcal E_w^{1/2},
\]

where M5-83 gives

\[
\mathcal E_w
=
S_{comp,w}
-4\nu^2(A_w+G_w)
-4\nu X_w
\ge0.
\]

Using the uniform bound from the preceding section,

\[
\boxed{
\int
|\nabla a\times Z_L|^2d\mu
\le
\sqrt3\,M_*\mathcal E_w^{1/2}.
}
\]

Thus for every minimal-payer saturating returned sequence

\[
\mathcal E_{w,n}\to0,
\]

we obtain

\[
\boxed{
\int
|\nabla a_n\times Z_{L,n}|^2d\mu_n
\to0.
}
\]

This is unconditional within the already retained fixed W1 pump cell.

---

## 8. Fragmentation and remote migration are removed from this step

The estimate does not contain:

- the number of connected superlevel components;
- a lower crossing bound on any individual component;
- any componentwise derivative of `m_k`;
- any contribution from spatial infinity.

The positive amplitude weight has compact spatial support in the normalized return cell, and the endpoint defect is formulated pointwise before integration.

Therefore component fragmentation and far-tail branch migration do not prevent passage from

\[
\mathcal E_w\to0
\]

to

\[
\nabla a\times Z_L\to0
\quad\text{in weighted }L^2.
\]

This closes the principal YELLOW item left in M5-84.

---

## 9. Compactness passage to an exact local endpoint

Take a saturating returned sequence and translate each pump interval to the fixed reference time window.

W1 local analytic precompactness yields, after a subsequence,

\[
U_n\to U_*
\]

smoothly on `K_w`.

Consequently

\[
a_n\to a_*,
\qquad
Z_{L,n}\to Z_{L,*},
\qquad
w(a_n)\to w(a_*)
\]

uniformly with the finite derivatives used above.

The vanishing weighted defect therefore passes to the limit:

\[
\boxed{
\int
 a_*w(a_*)
|\nabla a_*\times Z_{L,*}|^2dY
=0.
}
\]

Hence

\[
\boxed{
\nabla a_*\times Z_{L,*}=0
}
\]

at every point of the open active set where

\[
w(a_*)>0
\]

by continuity.

Thus a minimal-payer saturating recurrent sequence produces an exact smooth local M5-82 endpoint in the W1 omega limit.

---

## 10. The limit is not allowed to become crossing-trivial

The robust returned upstroke has

\[
X_w\ge c_1>0.
\]

At exact M5-70 saturation M5-71/M5-81 give

\[
T\ge c_1/\nu>0.
\]

For a near-saturating sequence the same positive crossing lower bound persists after taking the balance residual sufficiently small.

Because `T` is supported in the same fixed pump cell and all relevant fields converge smoothly, the limit retains

\[
\boxed{
T_*>0.
}
\]

Equivalently,

\[
\boxed{
\int a_*w(a_*)
|U_*\cdot\nabla\log a_*|^2dY>0.
}
\]

Therefore the exact local endpoint obtained above is nontrivial and genuinely crossing on a positive weighted set.

---

## 11. Updated compactness dichotomy

The returned positive pump now has a sharper alternative.

### Strict-gap branch

There is a uniform `epsilon_*>0` such that every returned pump satisfies

\[
\mathcal E_w\ge\epsilon_*.
\]

Then one has a fixed strict surplus above the sharp minimal pressure payer.

### Exact-endpoint branch

There exists a returned sequence with

\[
\mathcal E_{w,n}\to0.
\]

Then W1 compactness produces a nonzero smooth recurrent omega-limit pump satisfying

\[
\boxed{
\nabla a_*\times Z_{L,*}=0
}
\]

throughout its active amplitude region and carrying

\[
\boxed{T_*>0.}
\]

The previous intermediate fragmentation/critical-level bookkeeping is no longer needed to obtain this local endpoint.

---

## 12. DSD audit

### GREEN

The positive amplitude band from M5-57 localizes all M5 weighted quantities to one fixed normalized return cell.

### GREEN

W1 local analytic bounds uniformly control the finite derivatives entering `L_ij^2q`.

### GREEN

`M_tan,2` is therefore uniformly bounded along all returned pump segments.

### GREEN

Minimal payer saturation forces the component-free tangential defect to zero in weighted `L2`.

### GREEN

Local analytic compactness upgrades the vanishing integral defect to an exact smooth endpoint identity on the active limit region.

### GREEN

The robust positive crossing survives the same compactness passage, so the limit is not the trivial `b=0` endpoint.

### YELLOW

The exact local endpoint

\[
\nabla a\times Z_L=0,
\qquad
T>0,
\]

has not yet been proved impossible.

### RED

No global regularity conclusion follows until either the exact endpoint is excluded or the strict-gap branch is shown to contradict the recurrent budget.

---

## 13. Next calculation

On the exact endpoint write

\[
Z_L=\beta(a,s)\nabla a
\]

on each regular active patch.

Since

\[
Z_L=\nabla(P-2\nu b),
\]

its curl vanishes and forces

\[
\nabla\beta\times\nabla a=0.
\]

The next direct rigidity calculation should insert

\[
\nabla(P-2\nu b)=\beta(a,s)\nabla a
\]

back into the scalar amplitude equation and the incompressibility/streamline identities, seeking a closed transport equation for `a` and `b` whose positive-crossing recurrent solutions can be classified or excluded.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
