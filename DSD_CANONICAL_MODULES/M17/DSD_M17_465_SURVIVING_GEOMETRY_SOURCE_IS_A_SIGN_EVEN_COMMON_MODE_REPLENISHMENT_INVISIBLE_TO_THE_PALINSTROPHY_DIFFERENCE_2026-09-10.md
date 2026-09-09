# DSD M17-465 — The surviving geometry source is a sign-even common-mode replenishment invisible to the palinstrophy difference

Date: 2026-09-10  
Canonical ID: **M17-465**

Status: **ACTIVE COMMON-MODE SOURCE REDUCTION / FINAL UNCLASSIFIED M17-459 SOURCE CHANNEL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Common and differential geometry channels

Define

\[
G_{\rm cm}:=\frac{G_A}{2},
\qquad
G_{\rm diff}:=\frac{G_D}{2}.
\]

Then

\[
G_-=G_{\rm cm}+G_{\rm diff},
\qquad
G_+=G_{\rm cm}-G_{\rm diff}.
\]

M17-464 classifies `G_diff` by endpoint palinstrophy and raw-H2. Therefore the only unclassified geometry-source channel is `G_cm`.

## 2. Exact sign equations in common/differential form

M17-459 becomes

\[
\boxed{
\dot K_+ +J_0
=-C_{0\sigma}+G_{\rm cm}-G_{\rm diff}+2S_+ +2Q_+,
}
\]

\[
\boxed{
\dot K_- +J_0
=-C_{0\sigma}+G_{\rm cm}+G_{\rm diff}+2S_- -2Q_-.
}
\]

Adding gives

\[
\boxed{
\dot A+2J_0
=-2C_{0\sigma}+2G_{\rm cm}+2S_A+2\Delta Q.
}
\]

Subtracting gives

\[
\boxed{
\dot P+2H_{\rm raw}
=2G_{\rm diff}+2S_D.
}
\]

Thus `G_cm` is exactly invisible to the palinstrophy-difference equation.

## 3. Interpretation on the M17-458 survivor

M17-458 forces

\[
K_-\approx K_+\sim O(1),
\qquad
P=K_--K_+\ll1
\]

on typical retained good times.

A large `G_diff` would try to change the two sign populations differently and is detected by the `P` equation; M17-464 therefore attaches it to endpoint palinstrophy/raw-H2.

A large `G_cm`, however, pushes both sign moments in the same direction and can replenish the symmetric zero-current sink without producing a first-order signed imbalance.

Hence the only geometry source compatible with persistent near-perfect sign cancellation without immediately appearing in `P` is

\[
\boxed{G_{\rm cm}.}
\]

## 4. Strong zero-current implication

Suppose over an interval `I` the absolute moment remains endpoint-bounded,

\[
|A(t_1)-A(t_0)|\le C_A,
\]

while

\[
\int_IJ_0dt\gg C_A.
\]

Then from the absolute balance,

\[
2\int_IG_{\rm cm}dt
= A(t_1)-A(t_0)
+2\int_IJ_0dt
+2\int_IC_{0\sigma}dt
-2\int_IS_Adt
-2\int_I\Delta Qdt.
\]

After M17-460--462 and M17-461 classify the other terms, any part of the strong zero-current sink not paid by palinstrophy/trace loss, raw-H2, or coefficient-magnitude dispersion must satisfy

\[
\boxed{
\int_I(G_{\rm cm})_+dt
\gtrsim
\int_IJ_0dt
}
\]

up to those explicitly accounted currencies and endpoints.

Thus `G_cm` is not a vague remainder: it is the unique possible **sign-even replenishment** left in the M17-459 source-return architecture.

## 5. No finite budget is asserted

The exact termwise M17-339 formula for `R_geom` has not been recovered in the current audit pass. Therefore M17-465 makes no claim that

\[
G_{\rm cm}
\]

has a sign, is a divergence, is controlled by palinstrophy, or is controlled by raw-H2.

The canonical alternatives are

\[
\boxed{
G_{\rm cm}
\Longrightarrow
G_{\rm verified\ termwise\ payer}
\lor
G_{\rm persistent\ common\text{-}mode\ geometry\ return}
\lor
G_{\rm high\text{-}jet/chart/domain/genealogy\ loss}.
}
\]

Until the first alternative is certified, the second is an explicit OPEN channel.

## 6. Compression of the M17-459 source tree

After M17-460--465:

\[
\boxed{
\begin{aligned}
C_{0\sigma}&\to \text{palinstrophy or trace/high-jet loss},\\
S_A&\to \text{raw-H2 cubic firewall},\\
\Delta Q&\to \text{sign-dependent coefficient-scale dispersion + small }P,\\
G_{\rm diff}&\to \text{endpoint }P + \text{ raw-H2},\\
G_{\rm cm}&\to \text{only remaining unclassified common-mode source}.
\end{aligned}
}
\]

Therefore the late diffuse sign-compensation branch no longer contains several unnamed source-return mechanisms. It contains one precisely identified common-mode geometry channel plus the already explicit remote/interface/high-jet/genealogy exits.

## 7. DSD audit role

DSD is used only to diagonalize the sign-source bookkeeping into common and differential modes and to prevent a source invisible to one equation from being falsely declared controlled by that equation. The mathematical content is exact algebra on M17-459.

## 8. Audit verdict

**PASS — the unresolved geometry remainder has been compressed to one sign-even common-mode source channel.**

The next rigorous advance requires either recovery of the verified termwise M17-339 remainder or an independent estimate on `G_cm`. Until then, further termwise claims would be speculative and are prohibited by M17-463.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
