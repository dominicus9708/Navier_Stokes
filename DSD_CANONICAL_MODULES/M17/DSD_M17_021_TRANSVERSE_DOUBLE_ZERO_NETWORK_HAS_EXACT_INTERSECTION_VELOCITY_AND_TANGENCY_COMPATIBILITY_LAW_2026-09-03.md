# DSD M17-021 — A transverse double-zero network has an exact intersection velocity; only tangency imposes a compatibility law

Date: 2026-09-03
Canonical ID: **M17-021**

Status: **INTERNAL DOUBLE-ZERO NETWORK COMPATIBILITY / AT AN INTERSECTION OF THE ANGULAR BOUNDARY `chi=0` AND THE KAPPA TRANSITION `kappa=0`, THE RELATIVE VELOCITY `w=V_C-B` OF A REGULAR INTERSECTION CURVE MUST SATISFY `grad chi dot w = T` AND `grad kappa dot w = -h`. IF THE TWO GRADIENTS ARE TRANSVERSE, THIS 2X2 GRAM SYSTEM HAS AN EXPLICIT UNIQUE NORMAL-PLANE SOLUTION FOR ARBITRARY FINITE `T` AND `h`; THERE IS THEREFORE NO GENERIC ALGEBRAIC CONFLICT BETWEEN THE ANGULAR-LOBE TURNOVER BIAS AND THE KAPPA HYSTERESIS BIAS. WHEN THE ZERO SURFACES BECOME TANGENT, THE GRAM DETERMINANT VANISHES AND PERSISTENCE REQUIRES THE EXACT COMPATIBILITY `h = -lambda T` WHEN `grad kappa = lambda grad chi`. OTHERWISE THE DOUBLE-ZERO INTERSECTION MUST BREAK, RECONNECT, OR PASS THROUGH A JOINT RANK-LOSS EVENT. THE NEXT HARD BRANCH IS THUS UNIFORMLY TRANSVERSE DOUBLE-ZERO RECURRENCE VERSUS FINITE-JET TANGENCY/RECONNECTION, NOT A DIRECT CURRENT-SIGN CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two moving level sets

Define

\[
T:=\nabla_h\psi\cdot\nabla_hq.
\]

On a regular `chi=0` surface, M17-020 gives

\[
D_B\chi=-T.
\]

On a regular `kappa=0` surface,

\[
D_B\kappa=h.
\]

Let

\[
C(\theta)
:=\{\chi=0\}\cap\{\kappa=0\}
\]

be a regular intersection curve.
Let `V_C` be a geometric velocity of the intersection curve and set

\[
\boxed{w:=V_C-B.}
\]

---

## 2. Level-set constraints on the intersection velocity

Along a moving intersection point,

\[
0
=\partial_\theta\chi+V_C\cdot\nabla\chi
=D_B\chi+w\cdot\nabla\chi.
\]

Therefore

\[
\boxed{
\nabla\chi\cdot w=T.
}
\]

Likewise,

\[
0
=D_B\kappa+w\cdot\nabla\kappa,
\]

so

\[
\boxed{
\nabla\kappa\cdot w=-h.
}
\]

Thus the two turnover currents become two linear constraints on the same intersection velocity.

---

## 3. Transverse double-zero intersection

Set

\[
a:=\nabla\chi,
\qquad
b:=\nabla\kappa.
\]

Assume

\[
\boxed{
a\times b\ne0.}
\]

The Gram determinant is

\[
\boxed{
\Delta_{\chi\kappa}
:=|a|^2|b|^2-(a\cdot b)^2
=|a\times b|^2
>0.
}
\]

The component of `w` normal to the intersection curve lies in

\[
\operatorname{span}\{a,b\}.
\]

Write

\[
w_\perp=\alpha a+\beta b.
\]

The constraints give

\[
\begin{pmatrix}
|a|^2&a\cdot b\\
a\cdot b&|b|^2
\end{pmatrix}
\begin{pmatrix}
\alpha\\\beta
\end{pmatrix}
=
\begin{pmatrix}
T\\-h
\end{pmatrix}.
\]

Since `Delta_chikappa > 0`, the system is invertible.

---

## 4. Exact normal-plane velocity

Solving the Gram system gives

\[
\boxed{
\alpha
=\frac{|b|^2T+(a\cdot b)h}{\Delta_{\chi\kappa}},
}
\]

and

\[
\boxed{
\beta
=\frac{-(a\cdot b)T-|a|^2h}{\Delta_{\chi\kappa}}.
}
\]

Hence

\[
\boxed{
\begin{aligned}
w_\perp
={}&
\frac{|b|^2T+(a\cdot b)h}{\Delta_{\chi\kappa}}\,a\\
&-
\frac{(a\cdot b)T+|a|^2h}{\Delta_{\chi\kappa}}\,b.
\end{aligned}
}
\]

An arbitrary tangential component along

\[
a\times b
\]

only reparametrizes the intersection curve and does not affect the level-set constraints.

---

## 5. Orthogonal special case

If

\[
a\cdot b=0,
\]

then

\[
\boxed{
w_\perp
=\frac{T}{|a|^2}a
-\frac{h}{|b|^2}b.
}
\]

The two currents simply drive the two independent normal directions.

This makes clear that a nonzero mean angular-boundary turnover and a nonzero kappa-crossing hysteresis current are not generically incompatible.

---

## 6. Tangency limit

Now suppose the zero surfaces become tangent:

\[
\boxed{
b=\lambda a}
\]

for some nonzero scalar `lambda` at a regular common zero.
Then the two velocity constraints become

\[
a\cdot w=T,
\]

and

\[
\lambda a\cdot w=-h.
\]

A common smooth intersection velocity exists only if

\[
\boxed{
h=-\lambda T.}
\]

This is the exact **double-zero tangency compatibility law**.

If

\[
h\ne-\lambda T,
\]

then the two zero sets cannot remain tangent and share the same smoothly moving intersection at that event.
The geometry must instead undergo separation, reconnection, creation/destruction of intersection branches, or another joint rank-loss event.

---

## 7. Near-tangency amplification

For transverse intersections,

\[
\Delta_{\chi\kappa}
=|a|^2|b|^2\sin^2\vartheta,
\]

where `vartheta` is the angle between the gradients.

Thus the explicit formula contains the factor

\[
\boxed{\sin^{-2}\vartheta.}
\]

As the two zero surfaces approach tangency, the normal-plane intersection velocity becomes geometrically ill-conditioned unless the numerator simultaneously approaches the tangency compatibility relation.

Therefore a recurrent compact branch approaching tangency has two options:

1. **compatible grazing** — `h + lambda T` vanishes at the matching rate;
2. **joint zero-network event** — the intersection topology changes.

This is a geometric conditioning statement, not by itself a field singularity theorem.

---

## 8. Relation to M5-685 and M17-020

M5-685 requires a directed flux-weighted bias in the `kappa=0` current `h`.
M17-020 requires a strict signed mean angular-lobe boundary current `T` for every bounded recurrent lobe.

M17-021 shows that, on a transverse double-zero network, both can coexist:

\[
\boxed{
T\ne0,
\quad
h\ne0,
\quad
\nabla\chi\times\nabla\kappa\ne0
}
\]

has a regular intersection velocity.

Therefore the shortcut

\[
\boxed{
\text{two directed currents}
\Longrightarrow
\text{contradiction}
}
\]

is false.

The genuine extra condition appears only at tangency or rank loss.

---

## 9. DSD interpretation

### 9.1 Two descriptors, one moving intersection
The angular descriptor `chi` and multiplier descriptor `kappa` have independent material derivatives, but their common zero geometry is controlled by one rank-two linear system.

### 9.2 Transversality as describability
When

\[
\Delta_{\chi\kappa}>0,
\]

the two zero surfaces remain separately describable and their intersection motion is finite/algebraically determined.

When

\[
\Delta_{\chi\kappa}=0,
\]

the two normal descriptions collapse to one direction and an additional compatibility condition is required.

### 9.3 Branch reduction
The problem is now naturally split by the rank of

\[
\nabla(\chi,\kappa).
\]

---

## 10. DSD audit

### Audit A — independent surface velocities at their intersection
Rejected.
The same intersection point must satisfy both level-set constraints.

### Audit B — claiming transversality causes a sign conflict
Rejected.
The Gram system is invertible for arbitrary finite `T,h`.

### Audit C — interpreting large intersection speed near tangency as Navier-Stokes blow-up
Rejected.
Geometric intersection velocity can become large while the underlying fields remain smooth; topology change is another possibility.

### Audit D — tangency without compatibility
Rejected for a smoothly persistent common intersection.
Tangency requires `h=-lambda T`.

### Audit E — proof status
No global contradiction is obtained.

---

## 11. Updated double-zero frontier

The bounded recurrent non-axisymmetric branch now splits into

\[
\boxed{
Z_{2}^{transverse}
\ \lor\ 
Z_{2}^{tangent-compatible}
\ \lor\ 
Z_{2}^{rank-loss/reconnect}.
}
\]

- `Z_2^transverse`: `grad chi x grad kappa != 0`; both turnover currents coexist with an exact intersection velocity.
- `Z_2^{tangent-compatible}`: gradients align and `h=-lambda T` allows compatible grazing.
- `Z_2^{rank-loss/reconnect}`: tangency compatibility fails or one gradient vanishes, forcing a joint zero-network event.

---

## 12. Next target — persistent transverse network versus finite-jet event

The remaining high-value question is whether a compact recurrent survivor can keep the double-zero network uniformly transverse forever while simultaneously satisfying

\[
\boxed{
D_{-,\Omega}>D_{+,\Omega},
}
\]

for each defect lobe,

\[
\boxed{
\left\langle
s\int_{\partial\Omega_s}\frac{T}{|\nabla\chi|}
\right\rangle
=\frac32\langle V_s\rangle,
}
\]

and the M5-685 directed `h` hysteresis.

If uniform transversality cannot be maintained, the remaining event is a finite-order joint tangency/rank-loss classification problem.

This is the **Persistent Transverse Network Gate (PTNG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
