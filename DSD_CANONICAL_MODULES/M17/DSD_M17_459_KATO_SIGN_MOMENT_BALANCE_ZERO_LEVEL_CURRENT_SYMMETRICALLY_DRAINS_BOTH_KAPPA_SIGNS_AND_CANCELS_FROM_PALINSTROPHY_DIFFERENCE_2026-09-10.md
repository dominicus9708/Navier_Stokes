# DSD M17-459 — Kato sign-moment balance: the regular zero-level current symmetrically drains both coefficient signs and cancels from their palinstrophy difference

Date: 2026-09-10  
Canonical ID: **M17-459**

Status: **ACTIVE EXACT SIGN-BALANCE THEOREM / ZERO-CURRENT SOURCE-RETURN REDUCTION / M17-458 CONNECTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope and normalization

Work on a smooth whole-space exact CE-H interval in the viscosity-one normalization used by the coefficient equation in the late-M17 chain:

\[
\Delta\Omega=\kappa\Omega,
\qquad
\rho=|\Omega|,
\]

\[
D_t\kappa=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

where

\[
L_\rho f
:=\Delta f+2\nabla\log\rho\cdot\nabla f
=\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

The corresponding viscosity-one amplitude law is

\[
D_t\rho=(\sigma+\kappa)\rho,
\qquad
D_t(\rho^2)=2(\sigma+\kappa)\rho^2.
\]

All identities below are first derived in this common normalization. Restoring a general viscosity in individual terms is representation-sensitive and is not needed for the structural conclusion of this module.

## 2. Positive and negative coefficient moments

Define

\[
\kappa_+:=\max\{\kappa,0\},
\qquad
\kappa_-:=\max\{-\kappa,0\},
\]

and

\[
K_+(t):=\int_{\mathbb R^3}\kappa_+\rho^2\,dx,
\qquad
K_-(t):=\int_{\mathbb R^3}\kappa_-\rho^2\,dx.
\]

Set

\[
A(t):=K_+(t)+K_-(t)
=\int|\kappa|\rho^2\,dx,
\]

and recall the whole-space CE-H sign identity

\[
\boxed{
P(t):=\|\nabla\Omega(t)\|_2^2
=K_-(t)-K_+(t)\ge0.
}
\]

Also define the second sign moments

\[
Q_+:=\int\kappa_+^2\rho^2\,dx,
\qquad
Q_-:=\int\kappa_-^2\rho^2\,dx,
\]

so that

\[
\boxed{
Q_++Q_-
=\int\kappa^2\rho^2\,dx
=\|\Delta\Omega\|_2^2
=:H_{\rm raw}.
}
\]

For the strain-weighted first moments write

\[
S_+:=\int\kappa_+\sigma\rho^2\,dx,
\qquad
S_-:=\int\kappa_-\sigma\rho^2\,dx.
\]

Finally define the signed geometric source pieces

\[
G_+:=\int_{\{\kappa>0\}}\mathcal R_{\rm geom}\rho^2\,dx,
\]

\[
G_-:=-\int_{\{\kappa<0\}}\mathcal R_{\rm geom}\rho^2\,dx.
\]

## 3. Kato identity and the sign of the zero-level term

For a smooth scalar coefficient, distributionally,

\[
\boxed{
L_\rho|\kappa|
=\operatorname{sgn}(\kappa)L_\rho\kappa
+2\delta(\kappa)|\nabla\kappa|^2.
}
\]

Equivalently,

\[
\boxed{
\operatorname{sgn}(\kappa)L_\rho\kappa
=L_\rho|\kappa|
-2\delta(\kappa)|\nabla\kappa|^2.
}
\]

Because `L_rho` is in weighted divergence form,

\[
\int\rho^2L_\rho f\,dx=0
\]

for the decaying whole-space fields under consideration.

Define the regular zero-level coefficient current

\[
\boxed{
J_0(t)
:=\int\rho^2\delta(\kappa)|\nabla\kappa|^2\,dx
\ge0.
}
\]

Therefore the diffusion contribution to the absolute sign moment is

\[
\boxed{
\int\rho^2\operatorname{sgn}(\kappa)L_\rho\kappa\,dx
=-2J_0.
}
\]

This fixes an important sign convention:

\[
\boxed{
J_0\text{ is a dissipative sink in }A'(t),
\text{ not a positive source.}
}
\]

At a regular zero level, coarea gives

\[
\boxed{
J_0
=\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|\,dS.
}
\]

Thus `J_0` is exactly the regular-zero level density used in the M17-343--346 architecture, up to the localization/cutoff conventions used there.

## 4. The common zero-level strain trace

The `L_rho sigma` term produces a second zero-level trace. Define

\[
\boxed{
C_{0\sigma}
:=\int\rho^2\delta(\kappa)
\nabla\kappa\cdot\nabla\sigma\,dx.
}
\]

For a regular zero hypersurface with

\[
n=\frac{\nabla\kappa}{|\nabla\kappa|},
\]

this becomes

\[
\boxed{
C_{0\sigma}
=\int_{\{\kappa=0\}}\rho^2\partial_n\sigma\,dS.
}
\]

Weighted integration by parts gives the same sign in the `K_+` and `K_-` equations:

\[
\int_{\{\kappa>0\}}\rho^2L_\rho\sigma\,dx
=-C_{0\sigma},
\]

\[
-\int_{\{\kappa<0\}}\rho^2L_\rho\sigma\,dx
=-C_{0\sigma}.
\]

## 5. Exact positive-sign balance

Using incompressibility to differentiate the whole-space integral,

\[
\frac d{dt}K_+
=\int D_t(\kappa_+\rho^2)\,dx.
\]

The coefficient diffusion contributes `-J_0`, the `L_rho sigma` term contributes `-C_{0sigma}`, the geometry term contributes `G_+`, and the amplitude law contributes

\[
2\int\kappa_+(\sigma+\kappa)\rho^2dx
=2S_++2Q_+.
\]

Hence

\[
\boxed{
\dot K_+ +J_0
=-C_{0\sigma}+G_+ +2S_+ +2Q_+.
}
\]

## 6. Exact negative-sign balance

Similarly,

\[
\frac d{dt}K_-
=\int D_t(\kappa_-\rho^2)\,dx.
\]

The coefficient diffusion again contributes `-J_0`, and the `L_rho sigma` term again gives `-C_{0sigma}`. The amplitude term now contains

\[
2\kappa_-(\sigma+\kappa)
=2\kappa_-\sigma-2\kappa_-^2.
\]

Therefore

\[
\boxed{
\dot K_- +J_0
=-C_{0\sigma}+G_- +2S_- -2Q_-.
}
\]

The key structural fact is already visible:

\[
\boxed{
J_0\text{ drains }K_+\text{ and }K_-\text{ at exactly the same rate.}
}
\]

## 7. Absolute-moment balance

Add the two sign equations. Since

\[
A=K_-+K_+,
\]

we obtain

\[
\boxed{
\dot A+2J_0
=-2C_{0\sigma}
+(G_++G_-)
+2(S_++S_-)
+2(Q_+-Q_-).
}
\]

Define the total source-return term

\[
\boxed{
\mathscr S_A
:=-2C_{0\sigma}
+(G_++G_-)
+2(S_++S_-)
+2(Q_+-Q_-).
}
\]

Then

\[
\boxed{
\dot A+2J_0=\mathscr S_A.
}
\]

Thus persistent regular zero-current cannot be free. It must be replenished by endpoint release or by the combined strain/geometry/second-moment source return.

Integrating over `I=[t_0,t_1]` gives

\[
\boxed{
2\int_IJ_0dt
=A(t_0)-A(t_1)+\int_I\mathscr S_A\,dt.
}
\]

Since `A>=0`, a one-sided consequence is

\[
2\int_IJ_0dt
\le A(t_0)+\int_I|\mathscr S_A|dt.
\]

There is therefore no standalone monotone finite `J_0` budget unless the source-return terms are separately controlled.

## 8. Signed-difference / palinstrophy balance

Subtract the positive-sign equation from the negative-sign equation. Because

\[
P=K_--K_+,
\]

both `J_0` and `C_{0sigma}` cancel exactly:

\[
\boxed{
\dot P
=(G_--G_+)
+2(S_--S_+)
-2(Q_-+Q_+).
}
\]

Since

\[
Q_-+Q_+=H_{\rm raw},
\]

we have

\[
\boxed{
\dot P+2H_{\rm raw}
=(G_--G_+)+2(S_--S_+).
}
\]

This is the required consistency check with the usual viscosity-one palinstrophy evolution: the highest-order dissipative term is `-2 H_raw`.

The zero-current architecture therefore has a precise role:

\[
\boxed{
J_0\text{ can reduce the total absolute coefficient moment }A,
\text{ but cannot directly change }P=K_--K_+.
}
\]

## 9. Connection to M17-458

M17-458 shows that on surviving parent-length diffuse records, the good-time signed imbalance must satisfy, in time average,

\[
K_--K_+=P\ll K_-+K_+.
\]

M17-459 now says that a large regular zero-current does not by itself destroy this near-cancellation. It drains the two sign moments symmetrically.

Therefore a surviving state with

\[
K_-\sim K_+\sim O(1),
\qquad
P\ll1,
\qquad
J_0\not\ll1
\]

must replenish **both** coefficient signs through the common source-return architecture.

This converts the previous qualitative statement `rapid sign turnover needs replenishment` into an exact balance law.

## 10. First-moment cancellation does not control the second-moment asymmetry

A new firewall appears in the absolute-moment equation. M17-458 controls

\[
K_--K_+
=\int(\kappa_- -\kappa_+)\rho^2dx,
\]

but the source term in `A'` contains

\[
\boxed{
Q_+-Q_-
=\int(\kappa_+^2-\kappa_-^2)\rho^2dx.
}
\]

Small first-moment imbalance does not imply small second-moment imbalance.

Thus one must distinguish

\[
\boxed{
G_{\rm common\ magnitude\ shell}
\quad\text{vs}\quad
G_{\rm sign\text{-}dependent\ coefficient\ magnitude\ dispersion}.
}
\]

If both signs are confined to one narrow common magnitude shell `|kappa| approximately kappa_*`, then

\[
Q_+-Q_-
\approx
\kappa_*(K_+-K_-)
=-\kappa_*P,
\]

which is small on the M17-458 survivor.

If the positive and negative signs occupy different coefficient magnitudes/scales, however, `Q_+-Q_-` may remain order one even while `P` is tiny. This is a genuine new source-return route and must not be silently discarded.

## 11. The zero-level strain trace is not yet a bulk budget

Formally,

\[
|C_{0\sigma}|
\le
J_0^{1/2}
J_{\sigma,0}^{1/2},
\]

where

\[
J_{\sigma,0}
:=\int\rho^2\delta(\kappa)|\nabla\sigma|^2dx.
\]

Thus for any `epsilon>0`,

\[
2|C_{0\sigma}|
\le
\epsilon J_0
+\epsilon^{-1}J_{\sigma,0}.
\]

However `J_{sigma,0}` is a codimension-one trace. It is **not** automatically controlled by the global bulk quantity `int rho^2 |nabla sigma|^2` without a regular zero-tube thickness/trace theorem.

This is the next natural audit point and connects directly to M17-343--346 and the M17-457 interface geometry.

## 12. Updated split

The M17-458 near-perfect sign-cancellation survivor now satisfies

\[
\boxed{
\begin{aligned}
H_{\rm balanced\ signs}
\Longrightarrow{}&
H_{\rm weak\ zero\ current}\\
&\lor H_{\rm strong\ zero\ current+source\ return}.
\end{aligned}
}
\]

In the strong-current branch,

\[
\boxed{
\mathscr S_A
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q
}
\]

must repay the symmetric sink, where

\[
G_A=G_++G_-,
\qquad
S_A=S_++S_-,
\qquad
\Delta Q=Q_+-Q_-.
\]

This creates four explicit next routes:

1. zero-level strain-trace replenishment;
2. geometry-source replenishment;
3. strain-weighted sign-moment replenishment;
4. sign-dependent coefficient-magnitude / second-moment asymmetry.

## 13. DSD audit role

DSD is used only to choose the absolute and signed coefficient moments as audit currencies and to check which terms survive addition/subtraction. The derivation itself is standard distributional Kato calculus, weighted integration by parts, incompressible transport, and exact CE-H identities.

## 14. Audit verdict

**PASS — the zero-current architecture has an exact sign-moment meaning.**

The regular zero-level current is a positive dissipation currency when moved to the left side of the absolute-moment balance, but it drains positive and negative coefficient moments symmetrically and therefore cancels from the palinstrophy difference.

Consequently M17-458's increasingly precise `K_- approximately K_+` cancellation is compatible with large zero-current only if both signs are continuously replenished by the explicitly listed source-return channels.

The next target is to determine whether the codimension-one strain trace `C_{0sigma}` can be thickened into a bulk palinstrophy payer on regular zero tubes, and to separate that route from sign-dependent second-moment dispersion.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
