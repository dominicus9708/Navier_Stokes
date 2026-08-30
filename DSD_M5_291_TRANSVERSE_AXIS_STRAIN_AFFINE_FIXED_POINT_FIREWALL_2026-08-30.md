# DSD M5-291 — Transverse-Axis Strain and the Affine Fixed-Point Firewall

Date: 2026-08-30

Parent: `DSD_M5_290_FORMATION_AXIOM_AND_AXIS_PROPERTY_PARALLEL_DECOMPOSITION_2026-08-30.md`

Status: **AXIS-DECOMPOSITION FOLLOW-UP / LARGE TRANSVERSE STRAIN DOES NOT FORCE VORTICITY STRETCHING, PROJECTIVE TURNING, OR POSITIVE-MIDDLE BETCHOV PAYMENT / AN EXPLICIT STATIONARY AFFINE NAVIER–STOKES FAMILY REALIZES NONZERO VORTICITY PLUS ARBITRARILY LARGE TRANSVERSE SHEAR WITH ZERO LONGITUDINAL AND AXIS-TURNING CHANNELS / H_TRANSVERSE THEREFORE MERGES WITH THE DETACHED-AFFINE ANCESTRY PROBLEM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Recall the exact axis decomposition

At a point with `omega != 0`, put

\[
\xi=\frac\omega{|\omega|}.
\]

From M5-290,

\[
S\xi=\gamma\xi+\tau,
\]

and

\[
S_\perp=-\frac\gamma2P_\perp+D_\perp,
\qquad
\operatorname{tr}_\perp D_\perp=0.
\]

The exact norm identity is

\[
\boxed{
|S|^2
=\frac32\gamma^2+2|\tau|^2+|D_\perp|^2.
}
\]

The unresolved axis branch is

\[
\boxed{
|D_\perp|\gg1,
\qquad
|\gamma|,|\tau|\text{ comparatively small}.
}
\]

---

## 2. Large transverse shear need not create positive middle strain

Choose an orthonormal frame with

\[
\xi=e_1
\]

and take

\[
\boxed{
S
=\begin{pmatrix}
0&0&0\\
0&a&0\\
0&0&-a
\end{pmatrix}.
}
\]

Then

\[
\gamma=0,
\qquad
\tau=0,
\qquad
D_\perp=\operatorname{diag}(a,-a).
\]

The eigenvalues are

\[
a,\ 0,\ -a.
\]

Hence

\[
\boxed{\lambda_2=0}
\]

regardless of how large `|a|` is.

Therefore

\[
\boxed{
|D_\perp|\gg1
\not\Rightarrow
\lambda_2^+>c>0.
}
\]

The existing positive-middle threshold cannot automatically close `H_transverse`.

---

## 3. Betchov cubic can also miss pure transverse shear

For the same matrix,

\[
\det S=0,
\qquad
\operatorname{tr}(S^3)=0.
\]

Thus a large transverse shear can have zero cubic strain invariant.

More generally, when `tau=0`, the transverse eigenvalues are

\[
-\frac\gamma2\pm\delta,
\qquad
|D_\perp|^2=2\delta^2,
\]

and

\[
\det S
=\gamma\left(\frac{\gamma^2}{4}-\delta^2\right).
\]

If `gamma` is small while `delta` is large, the determinant/Betchov signal may still be small compared with the quadratic transverse strain.

Hence

\[
\boxed{
H_{transverse}
\not\Rightarrow
\text{large Betchov cubic payment}.
}
\]

---

## 4. Add solid rotation about the vorticity axis

Let

\[
A
=\begin{pmatrix}
0&0&0\\
0&0&-b\\
0&b&0
\end{pmatrix},
\]

so that the corresponding vorticity is parallel to `e1` and has magnitude proportional to `|b|`.

Take

\[
M:=S+A.
\]

On the transverse plane,

\[
D=\begin{pmatrix}a&0\\0&-a\end{pmatrix},
\qquad
J_b=\begin{pmatrix}0&-b\\b&0\end{pmatrix}.
\]

A direct calculation gives

\[
\boxed{DJ_b+J_bD=0.}
\]

Therefore

\[
M^2=S^2+A^2+SA+AS
\]

is symmetric.

---

## 5. Exact stationary affine Navier–Stokes family

Define

\[
\boxed{u(x)=Mx.}
\]

Since

\[
\operatorname{tr}M=\operatorname{tr}S=0,
\]

we have

\[
\nabla\cdot u=0.
\]

Also

\[
\Delta u=0
\]

and

\[
(u\cdot\nabla)u=M^2x.
\]

Because `M^2` is symmetric, define

\[
\boxed{
p(x)=-\frac12x^TM^2x.
}
\]

Then

\[
\nabla p=-M^2x
\]

and hence

\[
\boxed{
-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0.
}
\]

Thus this is an exact stationary Navier–Stokes solution on all of `R3`.

Its properties are

\[
\boxed{
\omega\parallel e_1,
\qquad
|\omega|\sim|b|,
}
\]

\[
\boxed{
\gamma=0,
\qquad
\tau=0,
\qquad
|D_\perp|=\sqrt2|a|.
}
\]

Both `|a|` and `|b|` may be chosen independently large.

Therefore there exist exact NSE solutions with

- nonzero bounded vorticity;
- arbitrarily large transverse strain;
- zero instantaneous vorticity stretching;
- zero inviscid vorticity-axis turning;
- zero positive-middle strain;
- zero cubic strain invariant for the pure `gamma=0` choice.

---

## 6. Why viscosity does not remove this anti-model

The velocity is affine, so

\[
\Delta u=0.
\]

The vorticity is constant, so

\[
\Delta\omega=0.
\]

Hence the viscous terms do not act on this exact affine profile.

The required nonlinear acceleration is paid entirely by the quadratic pressure.

Thus one cannot claim

\[
\boxed{
\text{large transverse shear}
\Rightarrow
\text{viscous H2 payment}.
}
\]

without using non-affine/spatial-variation information.

---

## 7. Relation to the detached satellite obstruction

The affine family is not finite energy and is not in weak-`L3`.

But M5-281--M5-285 already showed that a satellite-centered local limit can lose precisely the global ancestry information that would exclude affine growth.

The former solid-rotation anti-model is the special case `a=0`.

The present family shows that the unresolved harmonic/affine sector is larger:

\[
\boxed{
\text{solid rotation}
+\text{transverse trace-free strain}.
}
\]

Consequently

\[
\boxed{
H_{transverse}
\text{ and }
A_{detached}^{affine}
}
\]

are not separate final problems.  They are two appearances of the same missing ancestry/growth restriction.

---

## 8. Formation-Axiom interpretation

In the original finite-energy solution, global growth at infinity is part of the admissible state description.

After local satellite recentering, that domain information is lost.

The affine family enters only because the new local descriptor no longer remembers the original global state class.

Thus the missing descriptor is not another local scalar invariant.  It is a **domain/ancestry condition** connecting the satellite window to the original finite-energy solution on expanding spatial scales.

This is exactly the type of information loss the Formation-Axiom decomposition was meant to expose.

---

## 9. Revised frontier

The axis decomposition now reduces the ambient-strain branch as follows:

\[
\boxed{
H_{ambient}
\Longrightarrow
H_{stretch}
\lor
T_{axis/projective}
\lor
A_{affine/transverse}.
}
\]

The first two have existing standard-PDE ledgers.

The third is not closable by local vorticity, Betchov, positive-middle, or viscosity alone.

Therefore the hard satellite branch becomes

\[
\boxed{
A_{ancestry}:
\text{rule out affine/weakly non-affine detached growth using inherited finite-energy or critical restart structure.}
}
\]

This merges two previously separate-looking gaps:

1. sparse/isolated satellite ancestry;
2. hidden transverse ambient strain.

---

## 10. Audit verdict

### PROVED

- large `D_perp` does not imply positive middle strain;
- large `D_perp` does not imply a large Betchov cubic invariant;
- the explicit family `u=(S+A)x` above is an exact stationary Navier–Stokes solution with nonzero vorticity and arbitrarily large transverse strain while `gamma=tau=0`;
- viscosity is exactly inactive on this affine family.

### FIREWALL

The following shortcuts are invalid:

\[
H_{transverse}\Rightarrow H_{stretch},
\]

\[
H_{transverse}\Rightarrow T_{projective},
\]

\[
H_{transverse}\Rightarrow \lambda_2^+>c,
\]

\[
H_{transverse}\Rightarrow\text{viscous derivative contradiction}.
\]

### NEW REDUCTION

\[
\boxed{
H_{transverse}
\text{ merges with the detached affine ancestry problem.}
}
\]

The next independent calculation should therefore focus on the other Formation branch: the collective satellite packing threshold.  Once amplified satellite families are quantified, the remaining sparse family and affine-transverse family can be treated together as a single ancestry/restart problem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
