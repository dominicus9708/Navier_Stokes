# DSD M17-041 — Frozen-angle pure-kernel rank two carries irreducible weighted-harmonic shear locked to director area

Date: 2026-09-04
Canonical ID: **M17-041**

Status: **INTERNAL FROZEN-ANGLE RANK-TWO STRESS REDUCTION / ON THE PURE-KERNEL CLASS WITH NONORTHOGONAL MATERIAL TARGET JETS `a` AND `b`, DEFINE `m=a·b`. THE PULLBACK DIRECTOR METRIC HAS AN OFF-DIAGONAL `(xi,n)` ENTRY `m`, SO THE WEIGHTED HARMONIC STRESS HAS AN IRREDUCIBLE SHEAR `rho^2 m`. BECAUSE THE UNIT-JET ANGLE `c=ahat·bhat` IS MATERIAL INVARIANT, `m/|J_xi|=c/sqrt(1-c^2)` IS ALSO MATERIAL INVARIANT; THE SHEAR CANNOT RELAX TO ZERO ON THE SAME REGULAR MARKER UNLESS DIRECTOR AREA DEGENERATES. PROJECTING THE WEIGHTED STRESS EQUATION GIVES A CLOSED THREE-EQUATION SYSTEM FOR THE SIGNED STRETCH `d`, SHEAR `m`, ENERGY `E`, AMPLITUDE GRADIENT AND FRAME CURVATURE. AFTER USING `div(rho xi)=0`, THE APPARENT `m D_xi log rho` TERMS CANCEL FROM THE `n` BALANCE, LEAVING A CLEAN SHEAR-TRANSFER LAW. NO UNIVERSAL SIGN CONTRADICTION APPEARS; THE FROZEN-ANGLE CLASS IS AN IRREDUCIBLE SHEAR-CARRYING SURVIVOR THAT MUST EXIT BY RANK LOSS/TURNOVER OR SATISFY THIS COUPLED STRESS SYSTEM INDEFINITELY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen-angle pure-kernel branch

Use the M17-033 canonical frame

\[
(\xi,k,n),
\qquad
(k\cdot\nabla)\xi=0.
\]

Define

\[
b=(\xi\cdot\nabla)\xi,
\qquad
a=(n\cdot\nabla)\xi.
\]

Let

\[
A:=|a|,
\qquad
B:=|b|,
\]

and assume the frozen target angle satisfies

\[
\boxed{
c:=\widehat a\cdot\widehat b\ne0.}
\]

Full rank two also gives

\[
|c|<1.
\]

Define the signed shear descriptor

\[
\boxed{m:=a\cdot b=ABc.}
\]

---

## 2. Shear is locked to director-area magnitude

The director-area current magnitude is

\[
|J_\xi|
=|a\times b|
=AB\sqrt{1-c^2}.
\]

Therefore

\[
\boxed{
\frac{m}{|J_\xi|}
=\frac{c}{\sqrt{1-c^2}}.
}
\]

Because `c` is materially invariant by M17-037,

\[
\boxed{
D_B\left(
\frac{m}{|J_\xi|}
\right)=0.
}
\]

Thus nonzero angular shear cannot disappear independently of director-area degeneration.

---

## 3. Material law for m

M17-033 gives

\[
D_Ba
=-\left(\sigma_n+\frac12\right)a
\]

and

\[
D_Bb
=-\left(\sigma+\frac12\right)b.
\]

Hence

\[
D_Bm
=-(\sigma+\sigma_n+1)m.
\]

Trace-free strain gives

\[
\sigma+\sigma_k+\sigma_n=0.
\]

Therefore

\[
\boxed{
D_Bm=(\sigma_k-1)m.
}
\]

This is exactly the same scalar multiplier as the magnitude of `J_xi`, consistent with Section 2.

---

## 4. Pullback metric and stress

Define

\[
E=A^2+B^2
\]

and

\[
 d:=\frac{B^2-A^2}{2}.
\]

In the domain frame `(xi,k,n)`, the pullback metric is

\[
\boxed{
G=
\begin{pmatrix}
B^2&0&m\\
0&0&0\\
m&0&A^2
\end{pmatrix}.
}
\]

With

\[
w=\rho^2,
\]

the weighted harmonic stress

\[
S=w\left(G-\frac12EI\right)
\]

is

\[
\boxed{
S=w
\begin{pmatrix}
d&0&m\\
0&-E/2&0\\
m&0&-d
\end{pmatrix}.
}
\]

The nonzero off-diagonal shear is exactly `w m`.

---

## 5. Frame notation

Write

\[
b=p\,k+q\,n,
\qquad
a=r\,k+t\,n.
\]

The relevant frame connections are

\[
D_\xi k=-p\xi+\omega_\xi n,
\]

\[
D_k k=\gamma n,
\]

\[
D_n k=-r\xi+\omega_n n.
\]

Also

\[
\boxed{
\nabla\cdot\xi=t
}
\]

and divergence-free vorticity gives

\[
\boxed{
D_\xi\log w=-2t.
}
\]

---

## 6. Exact xi stress balance

The weighted harmonic stress equation is

\[
\operatorname{div}S
=-\frac E2\nabla w.
\]

The `xi` projection gives, before using vorticity divergence,

\[
D_\xi d
+D_nm
+mD_n\log w
+B^2D_\xi\log w
+2dt
-m(2q+\gamma)=0.
\]

Use

\[
D_\xi\log w=-2t
\]

and

\[
2(d-B^2)=-E.
\]

Then

\[
\boxed{
D_\xi d
+D_nm
+m\left(D_n\log w-2q-\gamma\right)
=Et.
}
\]

Equivalently,

\[
\boxed{
D_\xi d
+D_nm
+m\left(2D_n\log\rho-2q-\gamma\right)
=E\nabla\cdot\xi.
}
\]

This replaces the simpler orthogonal line law of M17-038.

---

## 7. Exact n stress balance

The `n` projection gives initially

\[
D_\xi m
-D_nd
+mD_\xi\log w
+2mt
+A^2(D_n\log w-\gamma)
+2dq=0.
\]

The two material-amplitude terms cancel exactly because

\[
D_\xi\log w=-2t.
\]

Therefore

\[
\boxed{
D_nd
=D_\xi m
+A^2(D_n\log w-\gamma)
+2dq.
}
\]

or

\[
\boxed{
D_nd
=D_\xi m
+A^2(2D_n\log\rho-\gamma)
+2dq.
}
\]

This is the clean shear-transfer equation of the frozen-angle branch.

---

## 8. Kernel stress balance

The `k` projection again loses the weight and gives

\[
\boxed{
D_kE
=2B^2p
-2A^2\omega_n
+2m(r-\omega_\xi).
}
\]

This is the full nonorthogonal version of the geometric kernel identity.

The additional term

\[
2m(r-\omega_\xi)
\]

is the irreducible angular-shear contribution.

---

## 9. Orthogonal branch as the exact m=0 limit

Set

\[
m=0.
\]

Then Section 6 reduces to

\[
D_\xi d=Et=-E D_\xi\log\rho,
\]

and Section 7 becomes

\[
D_nd=A^2(2D_n\log\rho-\gamma)+2dq,
\]

exactly M17-038.

Thus the frozen-angle equations are a genuine extension rather than a separate ansatz.

---

## 10. No conformal relaxation on one regular marker

Conformality requires

\[
m=0
\]

and

\[
d=0.
\]

But on the present branch

\[
\frac{m}{|J_\xi|}
=\frac{c}{\sqrt{1-c^2}}
e0
\]

is materially invariant.

Therefore as long as

\[
|J_\xi|>0,
\]

we have

\[
\boxed{m\ne0.}
\]

No amount of smooth stretch evolution can bring this marker into the M17-035/M17-036 conformal class.

---

## 11. Recurrent shear is compatible with the resonant mean frame

If `|m|` and `|J_xi|` remain recurrent and bounded above/below, their common multiplier gives

\[
\boxed{
\langle\sigma_k\rangle=1.
}

If `A` and `B` recur as in M17-033, then

\[
\langle\sigma\rangle
=\langle\sigma_n\rangle
=-\frac12.
\]

Thus the same resonant mean frame

\[
\boxed{
(-1/2,1,-1/2)
}
\]

supports nonzero frozen shear without mean-exponent contradiction.

---

## 12. DSD interpretation

The scalar conformal defect of M17-037 hides a signed stress channel.
For `c!=0`, anisotropy is not merely unequal stretching: it is an irreducible off-diagonal director stress whose ratio to director-area charge is frozen.

The branch therefore cannot be closed by showing that stretch ratio tends to one.
A closure must destroy/turn over the director-area carrier or contradict the coupled shear-stress equations themselves.

---

## 13. DSD audit

### Audit A — treating m as an independently adjustable shear
Rejected. `m/|J_xi|` is fixed by the material target angle.

### Audit B — assuming nonzero shear has a fixed energetic sign
Rejected. `m` is signed and the projected equations contain signed geometric terms.

### Audit C — claiming recurrent shear contradicts the mean strain frame
Rejected. It is exactly compatible with `(-1/2,1,-1/2)`.

### Audit D — silently using orthogonal formulas at c!=0
Avoided. M17-038 is recovered only in the exact `m=0` limit.

### Audit E — proof status
The frozen-angle branch is reduced to an irreducible shear system but remains open.

---

## 14. Updated frozen-angle frontier

A same-marker frozen-angle survivor must satisfy simultaneously

\[
\boxed{
\begin{aligned}
D_B\left(m/|J_\xi|\right)&=0,\\
D_\xi d+D_nm
+m(2D_n\log\rho-2q-\gamma)&=E\nabla\cdot\xi,\\
D_nd&=D_\xi m+A^2(2D_n\log\rho-\gamma)+2dq,\\
D_kE&=2B^2p-2A^2\omega_n+2m(r-\omega_\xi).
\end{aligned}
}
\]

with `m!=0` until rank loss/turnover.

---

## 15. Next target

The most promising closure for this irreducible branch is not conformal approach but a **shear-turnover ledger**:

- combine the material law `D_Bm=(sigma_k-1)m` with the co-frozen `J_xi` flux and exact similarity-volume expansion;
- determine whether a bounded recurrent Eulerian region can continually replace nonzero frozen-angle shear without servicing a second independent conserved geometric charge beyond M17-034's area-curvature ledger.

In parallel, the orthogonal oscillatory critical network can be tested by the CUSFG flatness equations.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
