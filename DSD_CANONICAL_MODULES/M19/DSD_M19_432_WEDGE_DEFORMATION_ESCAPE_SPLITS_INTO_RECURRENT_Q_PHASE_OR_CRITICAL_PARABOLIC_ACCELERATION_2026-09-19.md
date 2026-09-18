# M19-432 — The wedge-deformation escape splits into recurrent q-phase motion or critical parabolic acceleration; neither yields a new overlap contradiction

Date: 2026-09-19  
Canonical ID: **M19-432**  
Status: **DEFORMATION-BRANCH CLASSIFICATION / THE M19-431 D-FLOOR FORCES EITHER FIXED q-PHASE SPEED OR FIXED z-DEPTH DERIVATIVE ON THE COMPACT WEDGE CORRIDOR / q-PHASE MOTION IS A RECURRENT SIMILARITY-TIME TANGENT AND z-DERIVATIVE IS AN EXACT CRITICAL PHYSICAL ACCELERATION / BOTH ARE MEAN-TANGENT TO THE ENERGY SPHERE AT THE ENERGY MAXIMUM AND BOTH REMAIN CRITICAL / NAIVE HODGE-OVERLAP ROUTE DOES NOT CLOSE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-431

At the residual-slope energy maximum

\[
z_E\in[a_*,b_*],
\qquad
0<a_*<b_*<\infty,
\]

M19-431 gives the exact fork

\[
\boxed{
\mathscr K_\omega(z_E)
\ge
k_E>0
}
\]

or

\[
\boxed{
\mathscr X(z_E)
:=
\left\langle
\|\mathfrak DF(z_E)\|_2^2
\right\rangle
\ge
x_E>0,
}
\]

where

\[
\mathfrak D
=
\partial_q-2z\partial_z.
\]

The first branch gives same-depth vorticity mass but not yet a stretching-surplus sign.

The present module classifies the second branch.

## 2. Elementary decomposition of the D-deformation

At any fixed depth,

\[
\mathfrak DF
=
F_q-2zF_z.
\]

Therefore

\[
\|\mathfrak DF\|_2^2
\le
2\|F_q\|_2^2
+
8z^2\|F_z\|_2^2.
\]

After q-averaging,

\[
\boxed{
\mathscr X(z)
\le
2\mathscr V_q(z)
+
8z^2\mathscr V_z(z),
}
\]

where

\[
\boxed{
\mathscr V_q(z)
:=
\left\langle
\|F_q(z)\|_2^2
\right\rangle,
}
\]

and

\[
\boxed{
\mathscr V_z(z)
:=
\left\langle
\|F_z(z)\|_2^2
\right\rangle.
}
\]

Hence if

\[
\mathscr X(z_E)\ge x_E,
\]

then at least one of

\[
\boxed{
\mathscr V_q(z_E)
\ge
\frac{x_E}{4}
}
\]

or

\[
\boxed{
z_E^2\mathscr V_z(z_E)
\ge
\frac{x_E}{16}
}
\]

must hold.

Because

\[
a_*\le z_E\le b_*,
\]

the second branch implies the absolute depth-derivative floor

\[
\boxed{
\mathscr V_z(z_E)
\ge
\frac{x_E}{16b_*^2}.
}
\]

## 3. q-phase branch is a similarity-time tangent

At fixed z,

\[
|y|=z^{-1/2}
\]

is fixed in similarity variables, and

\[
q
=
\log|y|-rac\theta2.
\]

Thus

\[
\boxed{
\partial_\theta U
=
-rac1{2|y|}
F_q
}
\]

at the corresponding fixed similarity radius.

Therefore a lower bound on

\[
\mathscr V_q(z_E)
\]

is exactly a lower bound on recurrent similarity-time motion of the field on that fixed similarity sphere.

It is a phase-speed certificate, not an unsigned physical depletion.

## 4. q-phase activity is compatible with the hard recurrent dynamics

M19-146 already shows, on its certified one-slice observability lane, that a surviving singular hard orbit may in fact be forced to satisfy a positive q-speed floor.

That result explicitly warns that

\[
\boxed{
\text{positive q-speed}
\not\Rightarrow
\text{recurrence contradiction}.
}
\]

Periodic, relative-periodic, and quasiperiodic histories may move with nonzero speed indefinitely.

M19-073 independently shows that repeated normalized similarity-boundary events have geometrically summable original-variable energy/dissipation cost.

Therefore

\[
\boxed{
\mathscr V_q(z_E)>0
}
\]

does not supply the noncritical resource needed to close the branch.

## 5. z-depth derivative is exact physical acceleration

M5-582 gives

\[
\boxed{
\partial_su(x,s)
=
-r^{-3}F_z(z,q,\omega).
}
\]

Thus an order-one normalized depth derivative

\[
F_z
]

is exactly an order-one critical physical acceleration coefficient.

On a physical fixed-ratio annulus of radius R, the corresponding acceleration scales as

\[
R^{-3}.
\]

Its homogeneous negative Sobolev scaling in three dimensions is

\[
\boxed{
\|u_t\|_{\dot H^{-1}(A_R)}
\sim
R^{-1/2}
}
\]

for one normalized order-one event.

This is precisely the critical acceleration exponent isolated in M19-416.

## 6. Acceleration branch remains summable/critical

The annular test function needed to detect a signed order-one acceleration event has

\[
\|\nabla\chi_R\|_2
\asymp
R^{1/2}.
\]

Hence

\[
R^{-1/2}\cdot R^{1/2}
=
O(1).
\]

There is no physical scale gain.

Likewise an L2 shell charge for an order-one normalized acceleration has size

\[
\boxed{
\int_{A_R}|u_t|^2dx
\sim
R^{-3},
}
\]

which is geometrically summable across increasing scales.

Thus

\[
\boxed{
\mathscr V_z(z_E)>0
\not\Rightarrow
\text{standard energy/acceleration budget contradiction}.
}
\]

## 7. Both deformation subbranches are tangent motions at the energy maximum

For q-phase motion,

\[
\boxed{
\left\langle
\int F\cdot F_q
\right\rangle
=
0
}
\]

at every depth by q-translation invariance.

At the energy maximum,

\[
\mathscr E'(z_E)
=
\left\langle
\int F\cdot F_z
\right\rangle
=
0.
\]

Therefore

\[
\boxed{
\left\langle F,F_q\right\rangle=0,
\qquad
\left\langle F,F_z\right\rangle=0
}
\]

at \(z_E\).

Consequently both possible deformation payers are mean-tangent to the fixed-energy sphere in state space.

The M19-431 identity

\[
\left\langle F,\mathfrak DF\right\rangle=0
\]

is therefore the sum of two separately vanishing tangent pairings at the maximum.

This explains structurally why scalar energy cannot see the deformation branch.

## 8. Refined energy-maximum fork

The residual-slope energy maximum therefore satisfies at least one of three formed conditions:

\[
\boxed{
K_E:
\mathscr K_\omega(z_E)\ge k_E>0,
}
\]

\[
\boxed{
Q_E:
\mathscr V_q(z_E)\ge v_q^E>0,
}
\]

or

\[
\boxed{
Z_E:
\mathscr V_z(z_E)\ge v_z^E>0.
}
\]

The last two are exact tangent-motion channels.

## 9. Overlap-route verdict

The hoped-for shortcut

\[
\text{energy maximum}
\Longrightarrow
\text{same-depth stretching-dominant enstrophy shell}
\]

fails at the first Hodge level.

Even

\[
\text{energy maximum}
\Longrightarrow
\text{same-depth large vorticity}
\]

has the explicit alternative

\[
Q_E\lor Z_E.
\]

And when the vorticity branch does occur, positive vorticity mass alone still does not imply

\[
\mathscr Q_\omega-\mathscr P_\omega>0.
\]

Thus the current overlap theorem cannot be obtained from ordinary Hodge coercivity plus the scalar energy extremum alone.

## 10. What remains potentially useful

The common compact corridor from M19-430 remains valuable because all three energy-maximum channels occur on a bounded domain with uniform coefficients.

But any further overlap theorem must use a genuinely dynamical coupling, for example:

1. the wedge momentum PDE to relate \(F_z\) or \(F_q\) to strain/vorticity production;
2. the vorticity PDE to constrain a large tangent motion;
3. a bounded-corridor observability estimate linking tangent energy to \(\mathscr Q_\omega-\mathscr P_\omega\);
4. a same-event unique-continuation/rigidity theorem.

Another purely elliptic/Hodge norm comparison will only reproduce the critical tangent-motion alternatives above.

## 11. Updated immediate target

The next highest-value calculation is to insert the exact wedge PDE

\[
F_z
=
-\mathfrak L_1F
+
\mathfrak N(F,F)
+
\mathfrak G_2H
\]

into the \(Z_E\) depth-derivative branch and ask whether an order-one \(F_z\) can be supported with simultaneously small

- vorticity production \(\mathscr Q_\omega\);
- vorticity-gradient dissipation \(\mathscr P_\omega\);
- and q-phase activity.

If yes, the overlap route has a genuine PDE anti-model/firewall.

If no, one obtains the desired bounded-corridor dynamic coupling.

\[
\boxed{\text{M19-432 COMPLETE; THE WEDGE-DEFORMATION ESCAPE IS q-PHASE OR CRITICAL ACCELERATION, BOTH TANGENT AND SCALE-CRITICAL.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
