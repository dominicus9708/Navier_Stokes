# DSD M5-627 — Kappa-level-surface normal transport and material-relabeling split

Date: 2026-09-03

Status: **INTERNAL QUOTIENT-SCALAR TRANSPORT LAW / WITH `N_kappa=nabla kappa` AND `h=D_B kappa`, CE-H GIVES `N_kappa perp xi`, `nabla h perp xi`, AND THE EXACT MATERIAL NORMAL EQUATION `D_B N_kappa = nabla h - L_perp^T N_kappa` / IF `P_perp nabla h` IS NONZERO, THE VISCOUS MULTIPLIER DEVELOPS A TRUE CROSS-VORTEX-LINE ACCELERATION; IF IT VANISHES, `h` IS LOCALLY A FUNCTION OF THE KAPPA LABEL AND THE KAPPA LEVEL SURFACES ARE MATERIAL UP TO SCALAR RELABELING / THIS PRODUCES A NEW FORCED-VERSUS-RELABELED QUOTIENT BRANCH BUT NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Kappa is a vortex-line first integral

On CE-H,

\[
\boxed{W\cdot\nabla\kappa=0.}
\]

Where `W=rho xi` is nonzero,

\[
\boxed{\xi\cdot\nabla\kappa=0.}
\]

Define

\[
\boxed{N_\kappa:=\nabla\kappa.}
\]

Then

\[
\boxed{N_\kappa\perp\xi.}
\]

At regular points, `N_kappa` is the normal to the instantaneous level surface of `kappa`.

---

## 2. Material derivative of kappa is also a vortex-line first integral

Let

\[
\boxed{h:=D_B\kappa.}
\]

M5-611 derived

\[
[D_B,W\cdot\nabla]
=\left(\kappa-\frac32\right)(W\cdot\nabla).
\]

Apply this to `kappa`.

Since

\[
(W\cdot\nabla)\kappa=0,
\]

we obtain

\[
\boxed{W\cdot\nabla h=0.}
\]

Thus

\[
\boxed{\xi\cdot\nabla h=0.}
\]

and `h` is another scalar on the vortex-line quotient.

---

## 3. Gradient transport equation

For any scalar `f`,

\[
D_B(\nabla f)
=\nabla(D_Bf)-(\nabla B)^T\nabla f.
\]

Apply this to `f=kappa`:

\[
D_BN_\kappa
=\nabla h-(\nabla B)^TN_\kappa.
\]

Because `N_kappa` is transverse to `xi`, and the CE-H velocity-gradient block preserves the splitting `span{xi} plus xi-perp`, define

\[
L_\perp:=P_\xi^\perp(\nabla B)P_\xi^\perp.
\]

Then

\[
\boxed{
D_BN_\kappa
=\nabla h-L_\perp^TN_\kappa.
}
\]

Since `nabla h` is also transverse,

\[
\boxed{
D_BN_\kappa
=P_\xi^\perp\nabla h-L_\perp^TN_\kappa.
}
\]

This has exactly the structure of a material covector with an additive cross-line source.

---

## 4. Norm equation

Taking the scalar product with `N_kappa`,

\[
\frac12D_B|N_\kappa|^2
=N_\kappa\cdot\nabla h
-N_\kappa\cdot\Sigma N_\kappa
-\frac12|N_\kappa|^2.
\]

Hence

\[
\boxed{
\frac12D_B|\nabla\kappa|^2
=\nabla\kappa\cdot\nabla(D_B\kappa)
-\nabla\kappa\cdot\Sigma\nabla\kappa
-\frac12|\nabla\kappa|^2.
}
\]

There is no universal one-sign drift because the quotient acceleration `nabla h` and transverse strain remain sign-indefinite.

---

## 5. Forced quotient branch

If

\[
\boxed{|\nabla h|\ge h_*>0}
\]

on a positive-density coherent event set, then the viscous multiplier has a genuine cross-vortex-line material acceleration.

This is a higher-order version of the M5-622/M5-626 `nabla kappa` forcing channel:

\[
\boxed{
F_{\kappa,1}:=\nabla\kappa,
\qquad
F_{\kappa,2}:=\nabla(D_B\kappa).
}
\]

The M5-611 induction implies all higher material jets remain quotient scalars, so repeated failure of relabeling can in principle generate a hierarchy

\[
\nabla(D_B^m\kappa).
\]

No infinite hierarchy is asserted yet; this note only identifies the next exact source.

---

## 6. Relabeling branch

Suppose on a connected regular quotient region

\[
\boxed{\nabla h\parallel\nabla\kappa.}
\]

Since both gradients are transverse to vortex lines, this means `h` is constant on each connected `kappa` level surface.

Locally there exists a scalar function `f` such that

\[
\boxed{h=f(\kappa,\theta).}
\]

Therefore

\[
\boxed{D_B\kappa=f(\kappa,\theta).}
\]

Along every material label, the `kappa` value evolves by the same scalar relabeling ODE according only to its current level value and time.

---

## 7. Level surfaces are material up to relabeling

Let a material point start on

\[
\kappa=c_0.
\]

In the relabeling branch its value evolves according to

\[
\dot c=f(c,\theta).
\]

All points on the same connected initial level surface obey the same scalar ODE.

Hence that surface is transported by `B` into another `kappa` level surface:

\[
\boxed{
\{\kappa=c_0\}
\xrightarrow{\text{material flow}}
\{\kappa=c(\theta)\}.
}
\]

Thus the foliation is material modulo relabeling of the scalar level value.

This is stronger than the general instantaneous tangency statement of M5-626.

---

## 8. Normal evolution in the relabeling branch

If

\[
h=f(\kappa,\theta),
\]

then

\[
\nabla h=f_\kappa\nabla\kappa.
\]

The normal equation becomes

\[
\boxed{
D_BN_\kappa
=f_\kappa N_\kappa-L_\perp^TN_\kappa.
}
\]

Thus the normal is a transverse material covector with an isotropic scalar growth term `f_kappa`.

For the unit normal

\[
n_\kappa=N_\kappa/|N_\kappa|,
\]

only the anisotropic part of the transverse deformation rotates the normal; the scalar relabeling derivative changes its magnitude but not its orientation.

---

## 9. Autonomous subcase firewall

If the relabeling law were autonomous,

\[
D_B\kappa=f(\kappa)
\]

with no explicit time dependence, then a one-dimensional scalar ODE cannot support a nonconstant periodic orbit.

A recurrent material line with bounded nonconstant `kappa` would then have to approach an equilibrium zero of `f`, not oscillate forever.

However the actual recurrent hull permits explicit similarity-time dependence through the global state, so

\[
f=f(\kappa,\theta)
\]

must be retained.

No autonomous assumption is made.

---

## 10. Relation to flux turnover

Material vortex-tube flux obeys

\[
D_B\log|\phi|=\kappa.
\]

Thus in the relabeling branch every vortex line label obeys the coupled scalar system

\[
\boxed{
\begin{cases}
D_B\kappa=f(\kappa,\theta),\\
D_B\log|\phi|=\kappa.
\end{cases}
}
\]

A persistent fixed-flux label must still satisfy zero long-time mean of `kappa`.

Therefore a relabeled quotient process that supports persistent flux recurrence must arrange sign-changing or zero-mean `kappa` histories under the common scalar level ODE.

This is a much narrower turnover mechanism than arbitrary pointwise viscous diffusion.

---

## 11. Updated kappa branch

The forced `P nabla kappa` branch from M5-622/M5-623 now splits as

\[
\boxed{
F_{\nabla\kappa}
\Longrightarrow
F_{\nabla D_B\kappa}
\lor
R_{\kappa\text{-level relabeling}}.
}
\]

The first carries genuine cross-line acceleration of the multiplier field.

The second transports an entire foliation of vortex-line-containing level surfaces by a common scalar relabeling dynamics.

---

## 12. Highest-value next target

The relabeling branch is now finite-dimensional in the scalar level variable but still coupled to spatial transverse deformation.

A useful next calculation is the Jacobian/area evolution of a material `kappa` level surface and the induced flux distribution over it.

The forced branch should instead be compared with the commutator equation for `D_B kappa` from M5-601 to see whether `nabla D_B kappa` can be estimated by already retained derivative charges.

---

## 13. Firewall

The implication

\[
\nabla h\parallel\nabla\kappa
\Longrightarrow h=f(\kappa,\theta)
\]

is local on connected regular level-set regions. Critical points of `kappa` and disconnected level components require separate patching.

No global single-valued `f` is assumed without that patching.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
