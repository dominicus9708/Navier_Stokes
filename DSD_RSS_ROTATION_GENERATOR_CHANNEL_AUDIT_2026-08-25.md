# DSD RSS Rotation-Generator Channel Audit

Date: 2026-08-25

Status: **H0/H1/BETCHOV RECURRENCE TAXES ARE ROTATION-BLIND ON AN EXACT RSS ORBIT / THE ROTATION PARAMETER ENTERS ONLY THROUGH A NON-INVARIANT GENERATOR CHANNEL / AN EXACT VORTICITY ROTATION IDENTITY IS DERIVED / NO INTERMEDIATE-ALPHA CONTRADICTION YET / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The LRMG/open-RSS audit shows that the remaining compact critical-tail class contains the structural features of the still-open intermediate-rotation RSS problem.

The next question is whether the repository's existing H0/H1/Betchov recurrence taxes already impose a hidden restriction on the RSS angular speed `alpha`.

The answer is **no**: every balance built only from rotation-invariant Sobolev norms loses `alpha` exactly.

This note proves that cancellation and derives the first channel in which `alpha` is visible.

---

## 2. RSS as a Leray orbit

Let

\[
V(Y,s)
=
R(\alpha s)
U(R(-\alpha s)Y),
\]

and let

\[
W(Y,s)=\nabla\times V(Y,s)
=
R(\alpha s)
\Omega(R(-\alpha s)Y).
\]

Define the infinitesimal rotation generator on vector fields by

\[
\boxed{
\mathcal Gf
:=
Jf-(JY\cdot\nabla)f,
}
\]

where `J` is the antisymmetric generator of the fixed rotation axis.

Then

\[
\boxed{
\partial_sV=\alpha\mathcal GV,
\qquad
\partial_sW=\alpha\mathcal GW.
}
\]

The group

\[
T_\theta f(Y)=R(\theta)f(R(-\theta)Y)
\]

is unitary on every rotation-invariant `H^m` space. Therefore its generator `G` is skew-adjoint:

\[
\boxed{
\langle f,\mathcal Gf\rangle=0.
}
\]

It also commutes with constant-coefficient rotation-invariant differential operators such as `Delta`, curl, and integer powers of `-Delta`.

---

## 3. H0 enstrophy is exactly rotation-blind

The Leray vorticity enstrophy identity is

\[
\frac12Z_s
+\frac14Z
+\nu Q
=\mathcal P_0,
\]

where

\[
Z=\|W\|_2^2,
\qquad
Q=\|\nabla W\|_2^2.
\]

On an RSS orbit rotations preserve `Z`, so

\[
Z_s
=2\alpha\langle W,\mathcal GW\rangle
=0.
\]

Hence the RSS pointwise balance is simply

\[
\boxed{
\frac14Z+\nu Q=\mathcal P_0.
}
\]

There is no `alpha` term.

Thus the H0 recurrent strain/vorticity stretching tax cannot distinguish a stationary self-similar profile from a rigidly rotating one by angular speed.

---

## 4. H1 recurrence tax is also exactly rotation-blind

The H1 strain/vorticity identity may be written

\[
\frac14Q_s
+\frac38Q
+\frac\nu2R
=N_1,
\]

with

\[
R=\|\Delta W\|_2^2.
\]

Because `G` is skew-adjoint and commutes with gradients,

\[
Q_s
=2\alpha
\langle\nabla W,\nabla\mathcal GW\rangle
=0.
\]

Equivalently, since `-Delta` is self-adjoint and commutes with `G`,

\[
\langle-\Delta W,\mathcal GW\rangle=0.
\]

Therefore every exact RSS profile satisfies

\[
\boxed{
\frac38Q
+\frac\nu2R
=N_1,
}
\]

again with no `alpha` dependence.

The same statement holds for any rotationally invariant fixed Sobolev norm: its derivative along a pure rotation orbit is zero.

---

## 5. Direct Betchov barrier is rotation-blind for the same reason

The direct Betchov recurrence barrier uses only scalar rotation invariants such as

\[
Z,
\quad Q,
\quad
\int W^T\Sigma W,
\quad
\int\det\Sigma.
\]

Rigid rotation preserves all these scalar integrals.

Consequently the Betchov frequency/enstrophy thresholds constrain whether an RSS profile can exist at all in the admitted norm class, but they do not by themselves distinguish small, intermediate, or large `alpha`.

This is an important negative result:

\[
\boxed{
\text{H0/H1/Betchov norm taxes cannot resolve the intermediate-rotation problem through }\alpha\text{-dependence.}
}
\]

---

## 6. Leray vorticity equation with the rotation generator

The dynamic Leray vorticity equation is

\[
\boxed{
W_s
+W
+\frac12(Y\cdot\nabla)W
+(V\cdot\nabla)W
-(W\cdot\nabla)V
-\nu\Delta W
=0.
}
\]

At `s=0` on an RSS orbit, `V=U`, `W=Omega`, and

\[
W_s=\alpha\mathcal G\Omega.
\]

Thus the RSS profile vorticity equation is

\[
\boxed{
\alpha\mathcal G\Omega
+\Omega
+\frac12(Y\cdot\nabla)\Omega
+(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U
-\nu\Delta\Omega
=0.
}
\]

This equation displays the rotation channel explicitly.

---

## 7. Pair with the rotation generator

Take the real `L2` inner product with

\[
\mathcal G\Omega.
\]

The zeroth-order term vanishes by skew-adjointness:

\[
\langle\Omega,\mathcal G\Omega\rangle=0.
\]

The viscous term also vanishes because `G` commutes with `-Delta` and is skew-adjoint:

\[
\boxed{
\langle-\Delta\Omega,\mathcal G\Omega\rangle=0.
}
\]

Therefore one obtains the exact rotation-channel identity

\[
\boxed{
\alpha\|\mathcal G\Omega\|_2^2
+
\frac12
\langle Y\cdot\nabla\Omega,\mathcal G\Omega\rangle
+
\left\langle
(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U,
\mathcal G\Omega
\right\rangle
=0.
}
\]

Equivalently,

\[
\boxed{
\alpha\|\mathcal G\Omega\|_2^2
=
-\frac12
\langle Y\cdot\nabla\Omega,\mathcal G\Omega\rangle
-
\left\langle
(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U,
\mathcal G\Omega
\right\rangle.
}
\]

This is the first exact identity in the present ledger that directly sees `alpha`.

---

## 8. Why the dilation-rotation cross term is not zero automatically

The operators

\[
Y\cdot\nabla+\frac32
\]

and `G` are both skew-adjoint on `L2` and commute, but the quadratic cross term of two commuting skew operators need not vanish.

Therefore one may not delete

\[
\langle Y\cdot\nabla\Omega,\mathcal G\Omega\rangle
\]

without an additional radial/angular phase hypothesis.

This term measures radial-angular phase twisting of the vorticity profile and is a genuine new channel.

For a profile whose angular phase is independent of radius it may simplify, but no such structure is assumed in the general RSS problem.

---

## 9. Preliminary alpha estimate

If `G Omega` is nonzero, Cauchy-Schwarz gives the formal bound

\[
\boxed{
|\alpha|\,\|\mathcal G\Omega\|_2
\le
\frac12\|Y\cdot\nabla\Omega\|_2
+
\|(U\cdot\nabla)\Omega-(\Omega\cdot\nabla)U\|_2.
}
\]

Thus any useful upper bound on the right side together with a lower angular-activity bound on

\[
\|\mathcal G\Omega\|_2
\]

would produce an explicit upper bound for `|alpha|`.

This is qualitatively aligned with the fact that very large rotation is rigid, but the present identity alone does not yield a universal numerical contradiction.

If

\[
\mathcal G\Omega=0,
\]

the vorticity is invariant under the selected rotation group and the RSS motion is dynamically invisible at the vorticity level; this is a symmetry-degenerate subcase rather than an intermediate rotating orbit.

---

## 10. Relation to the Pineau-Vicol speed floor

For exact RSS,

\[
\partial_sV=\alpha\mathcal GV.
\]

On the spatial Type-I / pressure-admissible singular subbranch, the one-slice theorem forces a local/weighted speed floor.

Thus a nontrivial RSS survivor must satisfy a lower angular-motion condition of the schematic form

\[
\boxed{
|\alpha|\,\|\mathcal GV\|_{loc,w}
\gtrsim\delta_0.
}
\]

The new generator identity supplies an independent upper-side relation involving

\[
|\alpha|\,\|\mathcal G\Omega\|_2.
\]

Closing the intermediate-alpha RSS subcase would therefore require a quantitative bridge between the local velocity rotation mode and the global vorticity generator mode, together with control of the radial-angular cross term and the nonlinear generator pairing.

None of those bridges is currently proved.

---

## 11. DSD audit

The rotation generator is a distinct dynamic channel.

- rotationally invariant norms: `Z,Q,R,...`;
- phase speed: `alpha`;
- angular activity: `G Omega`, `G V`;
- radial-angular phase twisting: `<Y.grad Omega,G Omega>`;
- nonlinear rotational transfer: the final generator pairing.

These must not be collapsed into one generic recurrence quantity.

The calculation uses a finite set of formed channels and an exact PDE identity.

---

## 12. Updated frontier

The existing recurrence taxes do **not** secretly solve the open RSS difficulty: they are exactly blind to pure rotation speed.

The first genuinely new structured target is the rotation-generator balance

\[
\boxed{
\alpha\|\mathcal G\Omega\|_2^2
=
-\frac12\langle Y\cdot\nabla\Omega,\mathcal G\Omega\rangle
-
\langle
(U\cdot\nabla)\Omega-(\Omega\cdot\nabla)U,
\mathcal G\Omega
\rangle.
}
\]

A future successful RSS closure must control this non-invariant phase channel, not merely sharpen the old H0/H1 scalar constants.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
