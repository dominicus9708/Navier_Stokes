# DSD M5-194B — Vorticity Cutoff Criticality and Radial-Component Bottleneck Audit

Date: 2026-08-29

Parent: `DSD_M5_194A_EXACT_SCALAR_ADAPTED_WEIGHT_FIREWALL_2026-08-29.md`

Status: **CRITICAL-SCALE FIREWALL / THE RADIAL TAIL COMPONENT `Phi_r` IS A COMMON BOTTLENECK FOR BOTH RADIAL-PHASE ADAPTATION AND RADIAL-CUTOFF TRANSPORT COMMUTATORS / PURELY TANGENTIAL TAILS REMOVE THOSE TWO RADIAL OBSTRUCTIONS BUT NOT THE DIFFUSIVE CUTOFF COMMUTATORS / ZERO SPHERICAL FLUX IS TOO WEAK FOR POINTWISE OR WEIGHTED CANCELLATION / BACKWARD UNIQUENESS ENDPOINT REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Audit target

M5-194 and M5-194A left the Type-I vorticity/backward-uniqueness endpoint as the main surviving route.

The present audit asks a narrower question:

> After localizing the vorticity equation with a radial cutoff, are the generated source terms genuinely lower order at the critical `1/r` tail scale, or do they remain of the same scale as the principal vorticity dynamics?

The answer is: **they remain critical in relative scaling.**

Their unweighted absolute norms may decrease when the cutoff shell is pushed outward, but that fact alone does not create a small relative coefficient against the principal terms.

---

## 2. Vorticity equation and localized unknown

For smooth incompressible 3D Navier--Stokes,

\[
\partial_t\omega-\Delta\omega
+(u\cdot\nabla)\omega
-(\omega\cdot\nabla)u=0.
\]

Equivalently, with matrix multiplication `(nabla u) omega = (omega·nabla)u`, define

\[
L:=\partial_t-\Delta+u\cdot\nabla-\nabla u,
\]

so that

\[
L\omega=0.
\]

Let

\[
\chi_R(x)=\chi(|x|/R)
\]

be a time-independent radial cutoff and set

\[
w_R:=\chi_R\omega.
\]

A direct product-rule calculation gives

\[
\boxed{
Lw_R
=-2\nabla\chi_R\cdot\nabla\omega
-(\Delta\chi_R)\omega
+(u\cdot\nabla\chi_R)\omega.
}
\]

Denote the right-hand side by `F_R`.

The stretching term introduces no additional cutoff commutator because it is zeroth order in `omega`.

---

## 3. Shell scaling

On the annulus where the cutoff changes,

\[
A_R:=\{x:c_1R\lesssim |x|\lesssim c_2R\},
\]

we have

\[
|\nabla\chi_R|\lesssim R^{-1},
\qquad
|\Delta\chi_R|\lesssim R^{-2}.
\]

Therefore

\[
\boxed{
|F_R|
\lesssim
R^{-1}|\nabla\omega|
+R^{-2}|\omega|
+R^{-1}|u||\omega|.
}
\]

For a critical spatial tail on `r~R`, take the scale ledger

\[
|u|\sim R^{-1},
\qquad
|\nabla u|\sim R^{-2},
\qquad
|\omega|\sim R^{-2},
\qquad
|\nabla\omega|\sim R^{-3}.
\]

Then every cutoff source term has size

\[
R^{-1}|\nabla\omega|\sim R^{-4},
\]

\[
R^{-2}|\omega|\sim R^{-4},
\]

\[
R^{-1}|u||\omega|\sim R^{-4}.
\]

But the principal vorticity terms have the same size:

\[
|\Delta\omega|\sim R^{-4},
\]

\[
|u\cdot\nabla\omega|\sim R^{-4},
\]

\[
|(\omega\cdot\nabla)u|\sim R^{-4}.
\]

Hence

\[
\boxed{
\text{cutoff commutators are critical in relative scaling.}
}
\]

They do not become lower order merely because the cutoff shell is moved to a different scale.

---

## 4. Absolute smallness versus relative smallness

The volume of a three-dimensional annulus `A_R` is of order `R^3`. Therefore the critical pointwise size `R^{-4}` gives

\[
\|F_R\|_{L^2(A_R)}
\sim R^{-4}R^{3/2}
=R^{-5/2}.
\]

Likewise,

\[
\|\Delta\omega\|_{L^2(A_R)}
\sim R^{-5/2}.
\]

Thus, for an outward-moving shell,

\[
\|F_R\|_{L^2(A_R)}\to0
\]

can hold while simultaneously

\[
\frac{\|F_R\|_{L^2(A_R)}}
{\|\Delta\omega\|_{L^2(A_R)}}
\sim O(1).
\]

This distinction is essential for an endpoint Carleman argument:

\[
\boxed{
\text{absolute decay of the shell error}
\not\Rightarrow
\text{absorbable relative error.}
}
\]

The scale-invariant statement is the order-one relative ratio. The same warning applies if the continuation geometry is organized toward a small spatial scale rather than infinity.

---

## 5. Common-tail decomposition and the radial bottleneck

Write the critical common tail as in M5-194A,

\[
B_T(r,\theta)
=\frac1r
\left(
\Phi_r\,e_r+\Phi_\tau
\right).
\]

For the radial cutoff

\[
\chi_R(r)=\chi(r/R),
\]

we have

\[
\nabla\chi_R
=\frac1R\chi'(r/R)e_r.
\]

Consequently,

\[
\boxed{
B_T\cdot\nabla\chi_R
=
\frac{\Phi_r}{rR}\chi'(r/R).
}
\]

On `r~R`,

\[
B_T\cdot\nabla\chi_R
\sim \Phi_r R^{-2}.
\]

The corresponding drift-cutoff source is therefore

\[
\boxed{
(B_T\cdot\nabla\chi_R)\omega
\sim
\Phi_r R^{-4}.
}
\]

Now compare M5-194A. For a radial logarithmic Carleman phase

\[
\Psi(y)=\beta y,
\qquad y=-\log r,
\]

that audit obtained

\[
\boxed{
B_T\cdot\nabla\Psi
=-\beta r^{-2}\Phi_r.
}
\]

The same coefficient `Phi_r` controls both obstructions:

\[
\boxed{
\Phi_r
\quad\Longrightarrow\quad
\begin{cases}
\text{radial-phase adaptation residual},\\
\text{radial-cutoff transport commutator}.
\end{cases}
}
\]

This is the radial-component bottleneck.

---

## 6. Three radial-component regimes

### A. Purely tangential common tail

If

\[
\Phi_r=0,
\]

then simultaneously

\[
B_T\cdot\nabla\Psi=0
\]

for a radial phase and

\[
B_T\cdot\nabla\chi_R=0
\]

for a radial cutoff.

Thus the same favorable geometry removes both the M5-194A phase obstruction and the transport part of the present cutoff obstruction.

However, the diffusive commutators remain:

\[
-2\nabla\chi_R\cdot\nabla\omega
-(\Delta\chi_R)\omega.
\]

They are still critical under the scale ledger above.

So

\[
\boxed{
\Phi_r=0
\text{ is favorable but not sufficient to close backward uniqueness.}
}
\]

### B. Quantitatively small radial component

If

\[
\|\Phi_r\|_{L^\infty}\le\varepsilon,
\]

then both radial obstructions acquire an `epsilon` factor.

This creates a genuine perturbative candidate, but only if the endpoint Carleman inequality has a coercive margin with a constant that dominates the resulting terms.

No such theorem-specific threshold is proved in this audit.

### C. Order-one radial component

If `Phi_r` is order one, both the phase residual and radial drift-cutoff source remain at the critical scale.

There is no small parameter coming from scaling alone.

---

## 7. Why zero spherical flux is insufficient

Suppose only

\[
\int_{S^2}\Phi_r\,dS=0.
\]

The localized vorticity source contains the product

\[
\Phi_r(\theta)\,\omega(\theta),
\]

and energy pairings produce angularly varying factors such as `|omega|^2`.

In general,

\[
\int_{S^2}\Phi_r f\,dS
\]

need not vanish for a nonconstant `f`, even when the mean of `Phi_r` vanishes.

For example, choosing `f=Phi_r` gives

\[
\int_{S^2}\Phi_r^2\,dS>0
\]

unless `Phi_r` is identically zero.

Therefore

\[
\boxed{
\int_{S^2}\Phi_r\,dS=0
\quad\not\Rightarrow\quad
\text{cancellation of the radial cutoff drift term.}
}
\]

Pointwise smallness, orthogonality tied to `omega`, or a stronger PDE-specific cancellation would be required.

---

## 8. DSD firewall verdict

### CLOSED at this layer

The following shortcuts are not valid from critical scaling alone:

1. **Move the cutoff shell far away, therefore the commutator is automatically lower order.**

   False at the relative scale: the source and principal vorticity terms scale together.

2. **Zero spherical radial flux cancels the radial cutoff transport error.**

   False without additional angular information because the radial coefficient is multiplied by nonconstant vorticity data.

3. **A purely tangential tail by itself closes the localized backward-uniqueness argument.**

   False: it eliminates the radial transport/phase obstructions but leaves the diffusion cutoff commutators.

### SURVIVING branches

The following remain logically open:

- PDE-specific rigidity forcing `Phi_r=0` or making `Phi_r` quantitatively small for the canonical common tail;
- additional decay or annular leakage estimates for `omega` and `nabla omega` beyond critical scaling;
- weighted support separation in a Carleman estimate that suppresses the annular source even though its raw scaling is critical;
- an endpoint estimate with a strict coercivity margin sufficient to absorb an `epsilon`-small radial residual;
- vector/matrix symmetrization exploiting the coupled vorticity system;
- a different localization architecture that avoids the present commutator geometry.

---

## 9. Scope firewall

This note does not prove or disprove Navier--Stokes global regularity.

It does not prove that the actual canonical Type-I tail has an order-one radial component.

It does not invalidate backward uniqueness theorems.

It audits only whether the proposed localization errors become harmless from critical scaling and zero-flux geometry alone. They do not.

---

## 10. Next calculation

The next endpoint should quantify the two surviving diffusion-shell terms in the **weighted** norm actually needed by the Carleman architecture:

\[
\boxed{
\left\|e^{\Psi}R^{-1}\nabla\omega\right\|_{A_R},
\qquad
\left\|e^{\Psi}R^{-2}\omega\right\|_{A_R}.
}
\]

The key audit question is no longer raw scaling, but whether support separation, additional annular decay, or a coercive Carleman margin yields a strict inequality placing these weighted shell terms below the bulk left-hand side.

If not, the scalar-cutoff route reaches another endpoint firewall and the matrix/PDE-rigidity branches become the principal survivors.
