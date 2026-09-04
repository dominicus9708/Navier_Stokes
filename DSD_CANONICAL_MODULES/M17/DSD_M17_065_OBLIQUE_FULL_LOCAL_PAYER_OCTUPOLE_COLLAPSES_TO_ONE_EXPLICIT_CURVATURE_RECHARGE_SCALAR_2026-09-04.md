# DSD M17-065 — Oblique full local payer octupole collapses to one explicit curvature–recharge scalar

Date: 2026-09-04
Canonical ID: **M17-065**

Status: **INTERNAL OBLIQUE FULL-OCTUPOLE REDUCTION / FIX THE MATERIAL-INVARIANT PRINCIPAL FRAME OF THE NONCONFORMAL NODAL HESSIAN `Q=diag(q_1,q_2)` AND WRITE THE FROZEN SLANT DIRECTION AS `phat=(cos vartheta,sin vartheta)`, `p=P phat`. M17-058 ALREADY REDUCES THE KAPPA-GRADIENT SHARE TO `epsilon_E sqrt(2)/15 * kappa_3 P(q_1^2+q_2^2)sin(2vartheta)`. A DIRECT FULL STF CONTRACTION OF M17-057'S VORTICITY-CURVATURE TENSOR, USING THE TWO SEMILINEAR TRACE RELATIONS FOR `H=grad^3q`, GIVES `epsilon_E sqrt(2) kappa_0/15` TIMES ONE EXPLICIT LINEAR COMBINATION `Xi_vartheta` OF THE SEVEN ALLOWED THIRD-q JETS. HENCE THE COMPLETE LOCAL PAYER-OCTUPOLE MISMATCH IS ONE SCALAR: `o_loc=epsilon_E sqrt(2)/15 [kappa_0 Xi_vartheta + kappa_3 P |Q|_F^2 sin(2vartheta)]`. THE PRINCIPAL LIMIT `vartheta=0` RECOVERS M17-059 EXACTLY. FOR GENUINE OBLIQUE SLANT, LOCAL OCTUPOLE SILENCE IS AN EXACT INTERNAL CANCELLATION MANIFOLD BETWEEN THE CURVATURE THIRD-q JET AND THE H-GRADIENT-RECHARGED KAPPA-GRADIENT CHANNEL. NO SIGN PREVENTS THIS CANCELLATION. THE NEW VALUE IS THAT THE LOCAL L=3 PAYER GEOMETRY HAS BEEN REDUCED FROM A GENERIC STF RANK-THREE TENSOR TO ONE MATERIAL-FRAME SCALAR WITH A KNOWN RECHARGE TERM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen material principal frame

Because M17-014 freezes the normalized nonconformal Hessian shape, choose its principal basis once and for all:

\[
\boxed{
Q=\operatorname{diag}(q_1,q_2).
}
\]

Write the nonzero slant as

\[
\boxed{
p=P u,
\qquad
u=(c,s)=(\cos\vartheta,\sin\vartheta),
\qquad P=|p|>0.
}
\]

M17-024 freezes `u`, so `vartheta` is materially invariant.

Choose the Frobenius-unit forbidden tensor direction

\[
\boxed{
E_Q
=\varepsilon_E\frac1{\sqrt2}
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\varepsilon_E\in\{+1,-1\}.
}
\]

---

## 2. Kappa-gradient share

M17-058 gives

\[
\gamma_{Qp}
=\varepsilon_E\frac1{2\sqrt2}\sin2\vartheta.
\]

Therefore

\[
\boxed{
\mathfrak o_\kappa
=\varepsilon_E\frac{\sqrt2}{15}
\kappa_3P(q_1^2+q_2^2)\sin2\vartheta.
}
\]

Equivalently,

\[
\boxed{
\mathfrak o_\kappa
=\varepsilon_E\frac{\sqrt2}{15}
\kappa_3P|Q|_F^2\sin2\vartheta.
}
\]

This share vanishes exactly on principal slant and is nontrivial on genuine oblique slant when `kappa_3 != 0`.

---

## 3. Third-q jet notation

Let

\[
\boxed{H_{ijk}:=\partial_i\partial_j\partial_kq}
\]

be the fully symmetric third streamfunction jet.

The semilinear trace relations from M17-058 are

\[
H_{111}+H_{122}+H_{133}=0,
\]

\[
H_{112}+H_{222}+H_{233}=0.
\]

Thus

\[
\boxed{
H_{133}=-H_{111}-H_{122},
\qquad
H_{233}=-H_{112}-H_{222}.
}
\]

Seven physically visible third-q components remain.

---

## 4. Full STF curvature contraction

M17-057 gives

\[
T^{(W)}_{ijk}
=\frac{\kappa_0}{3}
\left(
A_{ai}B_{ajk}
+A_{aj}B_{aik}
+A_{ak}B_{aij}
\right),
\]

with

\[
A=JQL_p,
\qquad
B_{aij}=J_{a\alpha}H_{\alpha ij}.
\]

The forbidden scalar is

\[
\mathfrak o_W
=E_Q:TF_h[u\lrcorner STF_3(T^{(W)})].
\]

A direct contraction, followed by the two trace eliminations of Section 3, gives

\[
\boxed{
\mathfrak o_W
=\varepsilon_E\frac{\sqrt2\kappa_0}{15}
\Xi_\vartheta,
}
\]

where

\[
\boxed{
\begin{aligned}
\Xi_\vartheta
={}&2P c^2 q_1H_{123}
+2Pcs\left(q_1H_{113}+q_2H_{223}\right)
+2Ps^2 q_2H_{123}\\
&+c\left[(8q_1+5q_2)H_{112}-2q_2H_{222}\right]\\
&+s\left[-2q_1H_{111}+(5q_1+8q_2)H_{122}\right].
\end{aligned}
}
\]

Thus the seven-dimensional admissible third-q jet enters the forbidden local octupole through **one scalar projection only**.

---

## 5. Principal-limit audit

Set

\[
\vartheta=0,
\qquad c=1,
\qquad s=0.
\]

Then

\[
\Xi_0
=2Pq_1H_{123}
+(8q_1+5q_2)H_{112}
-2q_2H_{222}.
\]

Use

\[
H_{222}=-H_{112}-H_{233}.
\]

Therefore

\[
\boxed{
\Xi_0
=(8q_1+7q_2)H_{112}
+2Pq_1H_{123}
+2q_2H_{233},
}
\]

which is exactly the principal scalar `Xi` of M17-059.

This provides a nontrivial consistency check on the full STF contraction.

---

## 6. Complete local payer-octupole scalar

Combine Sections 2 and 4:

\[
\boxed{
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}
\left[
\kappa_0\Xi_\vartheta
+\kappa_3P|Q|_F^2\sin2\vartheta
\right].
}
\]

This is the canonical OFORG reduction.

The complete local `l=3` payer geometry is therefore encoded by the pair

\[
\boxed{
(\Xi_\vartheta,\kappa_3)
}
\]

inside one signed scalar combination.

---

## 7. Exact local-octupole silence manifold

For genuine oblique slant,

\[
\sin2\vartheta\ne0.
\]

Then

\[
\mathfrak o_{loc}=0
\]

is equivalent to

\[
\boxed{
\kappa_0\Xi_\vartheta
=-\kappa_3P|Q|_F^2\sin2\vartheta.
}
\]

If `kappa_0 != 0`,

\[
\boxed{
\Xi_\vartheta
=-\frac{\kappa_3}{\kappa_0}
P|Q|_F^2\sin2\vartheta.
}
\]

Thus the third-q curvature channel can exactly cancel the kappa-gradient payer octupole.
No sign obstruction prevents this cancellation.

At a nodal phase with

\[
\kappa_0=0,
\]

local silence instead requires

\[
\boxed{
\kappa_3=0
}
\]

on genuine oblique slant, unless `P|Q|` loses regularity.

This makes simultaneous `kappa_0=0` and local-octupole silence a sharp axial-gradient event.

---

## 8. Insert the M17-064 recharge law

M17-064 gives

\[
\boxed{
D_B\kappa_3
=\partial_3h
+\left(2\lambda-\frac12\right)\kappa_3.
}
\]

Therefore the second term in the local-octupole scalar is not freely adjustable.
Its material evolution contains the explicit recharge

\[
\boxed{\partial_3h.}
\]

Consequently a persistent local cancellation manifold must make the curvature scalar `Xi_vartheta` track a channel whose recharge is tied to the same `h=D_Bkappa` used by the M5 hysteresis ledger.

This is the first exact local relation placing third-q curvature and kappa-hysteresis derivative in the same `l=3` scalar balance.

---

## 9. Zero-kappa crossing consequence

Suppose the marked nodal value passes through

\[
\kappa_0=0
\]

while the oblique slant remains regular.

Then

\[
\boxed{
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}
\kappa_3P|Q|_F^2\sin2\vartheta.
}
\]

Hence at a regular oblique zero-kappa phase:

\[
\boxed{
\mathfrak o_{loc}=0
\iff
\kappa_3=0.
}
\]

Thus a regular zero-kappa crossing with nonzero axial multiplier gradient necessarily carries a nonzero local payer octupole in the forbidden frame.

This is not itself a contradiction because DSAIG does not require the payer octupole scalar to vanish.
It is a bridge descriptor that must be compared with pressure/viscous locking.

---

## 10. DSD analysis

M17-057 began with a generic STF rank-three local payer tensor.
The great-circle, semilinear, nodal, slant, and trace constraints reduce the relevant information chain to

\[
\boxed{
\mathcal O_{loc}^{(3)}
\to
\mathfrak o_{loc}
\to
(\Xi_\vartheta,\kappa_3).
}
\]

The second component is dynamically recharged by `partial_3h`.
The first is a curvature projection of `grad^3q`.

Thus the local octupole no longer has an unstructured tensor orientation escape.

---

## 11. DSD audit

### Audit A — treating the seven H components as seven independent locking costs
Rejected. Only `Xi_vartheta` is visible to this forbidden scalar.

### Audit B — dropping the 3D STF trace subtraction
Avoided. The numerical coefficients in `Xi_vartheta` depend on the full STF correction.

### Audit C — assuming local octupole silence is required by DSAIG
Rejected. This is a payer-geometry bridge descriptor, not the pressure tensor itself.

### Audit D — claiming curvature cannot cancel kappa-gradient octupole
Rejected. The exact cancellation manifold is displayed explicitly.

### Audit E — claiming zero kappa implies zero local octupole
Rejected. On oblique slant it remains proportional to `kappa_3`.

### Audit F — proof status
OFORG is an exact finite-dimensional reduction but not a branch contradiction.

---

## 12. Updated oblique local frontier

\[
\boxed{
R_{oblique}
\Longrightarrow
R_{cancel}^{\kappa_0\Xi_\vartheta
+\kappa_3P|Q|^2\sin2\vartheta}
\ \lor\
R_{local-oct\ne0}
\ \lor\
T_{\kappa_3/nodal/rank}.
}
\]

The curvature scalar `Xi_vartheta` must now be evolved materially and compared with the exact recharge law of `kappa_3`.

---

## 13. Next target

The next calculation is to derive the material evolution of `Xi_vartheta` in the frozen `(Qhat,phat)` frame and test whether the local cancellation manifold can be invariant.

Because the principal case showed dramatic source annihilation, the key question is whether genuine obliquity reintroduces unavoidable third-phi forcing or whether another exact reduced cocycle exists.

This is the **Oblique Curvature-Cancellation Invariance Gate (OCCIG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
