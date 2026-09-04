# DSD M17-037 — Pure-kernel rank-two anisotropy splits into a frozen angle and a strain-driven stretch ratio

Date: 2026-09-04
Canonical ID: **M17-037**

Status: **INTERNAL RANK-TWO ANISOTROPY EVOLUTION / ON THE PURE-TRANSVERSE-KERNEL CLASS, M17-033 GIVES TWO INDEPENDENT TARGET-TANGENT JETS `b=(xi·grad)xi` AND `a=(n·grad)xi` WITH EXACT SCALAR MATERIAL LAWS. CONSEQUENTLY THEIR UNIT DIRECTIONS ARE BOTH MATERIALLY FIXED, SO THE ANGLE BETWEEN `a` AND `b` IS AN EXACT MATERIAL INVARIANT. ONLY THE MAGNITUDE RATIO `r=|a|/|b|` CAN EVOLVE, WITH `D_B log r = sigma-sigma_n`. THE NORMALIZED CONFORMAL DEFECT IS THEREFORE AN EXPLICIT FUNCTION OF ONE DYNAMIC SCALAR `r` AND ONE FROZEN SCALAR `c=ahat·bhat`. IF `c!=0`, THE DEFECT HAS THE STRICT MATERIAL LOWER BOUND `delta_conf>=c^2`; SUCH AN ANGULAR-ANISOTROPIC MARKER CAN NEVER ENTER THE CONFORMAL SUBBRANCH WITHOUT RANK LOSS/TURNOVER. IF `c=0`, ANISOTROPY IS PURE STRETCH AND CONFORMALITY IS REACHED ONLY AT `r=1`. SAME-MARKER RECURRENCE OF BOTH JET MAGNITUDES FORCES ZERO MEAN `sigma-sigma_n`, SO THE STRETCH RATIO CAN RECYCLE WITHOUT CONTRADICTION. THE REMAINING ANISOTROPIC RANK-TWO BRANCH IS THUS CLEANLY SPLIT INTO AN IRREDUCIBLE ANGULAR CLASS AND AN ORTHOGONAL STRETCH CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two scalar jet amplitudes and one frozen angle

Use the pure-kernel frame of M17-033:

\[
b=(\xi\cdot\nabla)\xi,
\qquad
a=(n\cdot\nabla)\xi.
\]

Full rank two gives

\[
a\ne0,
\qquad
b\ne0,
\qquad
a\wedge b\ne0.
\]

Define

\[
A:=|a|,
\qquad
B:=|b|
\]

and unit directions

\[
\widehat a:=a/A,
\qquad
\widehat b:=b/B.
\]

M17-033 gives

\[
D_B\widehat a=0,
\qquad
D_B\widehat b=0.
\]

Therefore

\[
\boxed{
c:=\widehat a\cdot\widehat b}
\]

satisfies

\[
\boxed{D_Bc=0.}
\]

Since full rank two requires linear independence,

\[
|c|<1.
\]

---

## 2. Magnitude-ratio law

The exact multiplier laws are

\[
D_B\log B
=-\sigma-\frac12
\]

and

\[
D_B\log A
=-\sigma_n-\frac12.
\]

Define

\[
\boxed{r:=\frac AB>0.}
\]

Then

\[
\boxed{
D_B\log r
=\sigma-\sigma_n.
}
\]

Thus all same-marker shape change is carried by one scalar strain difference.

---

## 3. Director-area magnitude

The area-current magnitude is

\[
|J_\xi|
=|a\times b|
=AB\sqrt{1-c^2}.
\]

Hence

\[
\boxed{
|J_\xi|
=B^2 r\sqrt{1-c^2}.
}
\]

The factor

\[
\sqrt{1-c^2}
\]

is material invariant.

Thus rank loss through vanishing target angle cannot occur continuously on one regular material marker unless one of the jet amplitudes itself degenerates.

---

## 4. Normalized conformal defect

The director energy is

\[
E=A^2+B^2.
\]

Define

\[
\boxed{
\delta_{conf}
:=
1-\frac{4|J_\xi|^2}{E^2}
=
\frac{E^2-4|J_\xi|^2}{E^2}.
}
\]

Using

\[
A=rB
\]

and

\[
|J_\xi|^2=A^2B^2(1-c^2),
\]

we get

\[
\boxed{
\delta_{conf}(r,c)
=
1-
\frac{4r^2(1-c^2)}{(1+r^2)^2}.
}
\]

This lies in

\[
0\le\delta_{conf}<1
\]

for full rank two.

---

## 5. Frozen angular-anisotropy floor

For fixed material angle `c`, the factor

\[
\frac{4r^2}{(1+r^2)^2}
\]

has maximum `1` at

\[
r=1.
\]

Therefore

\[
\boxed{
\delta_{conf}(r,c)
\ge c^2.
}
\]

Equality occurs at equal magnitudes `r=1`.

Hence if

\[
\boxed{c\ne0,}
\]

then

\[
\boxed{
\delta_{conf}\ge c^2>0
}
\]

for the entire lifetime of the regular material marker.

Such a marker can **never** reach the conformal class

\[
\delta_{conf}=0
\]

by smooth strain-driven deformation alone.

It must instead leave through

\[
\boxed{
\text{jet/rank degeneration}
\ \lor\ 
\text{material turnover/interface}.
}
\]

---

## 6. Orthogonal stretch-anisotropy class

If

\[
\boxed{c=0,}
\]

then

\[
a\perp b
\]

for all material time.

The defect reduces to

\[
\boxed{
\delta_{conf}
=
\frac{(r^2-1)^2}{(r^2+1)^2}.
}
\]

Thus conformality is possible exactly when

\[
\boxed{r=1.}
\]

The orthogonal anisotropic class can therefore approach or cross the conformal interface through the single scalar stretch-ratio channel.

---

## 7. Exact defect evolution

Let

\[
x:=\log r.
\]

Then

\[
D_Bx=\sigma-\sigma_n.
\]

Since `c` is fixed,

\[
D_B\delta_{conf}
=
\frac{\partial\delta_{conf}}{\partial x}
(\sigma-\sigma_n).
\]

A direct differentiation gives

\[
\boxed{
\frac{\partial\delta_{conf}}{\partial x}
=
\frac{8r^2(1-c^2)(r^2-1)}{(1+r^2)^3}.
}
\]

Hence

\[
\boxed{
D_B\delta_{conf}
=
\frac{8r^2(1-c^2)(r^2-1)}{(1+r^2)^3}
(\sigma-\sigma_n).
}
\]

There is no fixed sign: strain may drive the marker toward or away from equal jet magnitudes.

---

## 8. Same-marker recurrence

If both nonzero jet magnitudes recur with bounded logarithms, M17-033 gives

\[
\langle\sigma\rangle=-\frac12
\]

and

\[
\langle\sigma_n\rangle=-\frac12.
\]

Therefore

\[
\boxed{
\langle\sigma-\sigma_n\rangle=0.
}
\]

Equivalently,

\[
\boxed{
\langle D_B\log r\rangle=0.
}
\]

Thus a recurrent stretch ratio is fully compatible with the resonant mean frame.

No mean-exponent contradiction appears.

---

## 9. Two intrinsic anisotropic classes

The unresolved anisotropic pure-kernel branch is now split canonically into

\[
\boxed{
R_{aniso}^{pure-kernel}
\Longrightarrow
R_{angle}^{frozen}
\ \lor\ 
R_{stretch}^{orthogonal}.
}
\]

### Frozen angular class

\[
\boxed{c\ne0.}
\]

The nonorthogonality angle is a material invariant and creates a strict conformal-defect floor.

### Orthogonal stretch class

\[
\boxed{c=0,\quad r\ne1.}
\]

The target directions remain orthogonal and only the magnitude ratio carries anisotropy.

---

## 10. DSD interpretation

The single undifferentiated descriptor `anisotropy` hides two structurally different channels:

1. **angle channel** — frozen by the material equations;
2. **stretch channel** — dynamically driven by `sigma-sigma_n`.

Only the second can reach the conformal firewall without a degeneracy event.

This is a clean describability split: two states with the same scalar `delta_conf` may have completely different allowed future transitions depending on how much of that defect is angle versus stretch.

---

## 11. DSD audit

### Audit A — assuming anisotropy is materially invariant
Rejected. Only the target angle is invariant; the magnitude ratio evolves.

### Audit B — assuming every anisotropic marker can become conformal
Rejected when `c!=0`.

### Audit C — claiming the stretch evolution has a preferred sign
Rejected. `sigma-sigma_n` is signed and may oscillate.

### Audit D — deriving a contradiction from zero mean stretch drift
Rejected. It is precisely compatible with compact recurrence.

### Audit E — proof status
The anisotropic branch is refined but remains open.

---

## 12. Updated intrinsic Rank-2 frontier

After M17-037,

\[
\boxed{
R_2^{intrinsic}
\Longrightarrow
R_{angle}^{frozen}
\ \lor\ 
R_{stretch}^{orthogonal}
\ \lor\ 
T_{2\to1}
\ \lor\ 
I_2^{turnover/interface}.
}
\]

The complete conformal class has already been closed by M17-036.

---

## 13. Next target

The orthogonal stretch class is closer to the closed conformal branch because it can reach `r=1` continuously.
The next calculation should impose the weighted-harmonic stress equations with

\[
a\perp b,
\qquad
|a|\ne|b|
\]

and determine whether Euclidean flatness drives the stretch ratio toward the M17-036 Riccati interface or permits a genuinely recurrent unequal-stretch geometry.

The frozen angular class can then be treated separately as an irreducible nonorthogonal branch.

This is the **Orthogonal Stretch Rank-Two Gate (OSR2G)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
