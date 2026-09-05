# DSD M17-148 — Peak tangency kills `xi-k` log-amplitude Hessian mixing and splits the `3/4` convexity gate into three geometric payers

Date: 2026-09-05  
Canonical ID: **M17-148**

Status: **PEAK-FRAME CONVEXITY DECOMPOSITION / M17-147 SHOWS THAT A QUIET HIGH-JET GENERIC FOLD REQUIRING ORDER-ONE `|D_xi kappa|` CANNOT BE RECURRENTLY REGENERATED IN AN INTERIOR CORRIDOR UNLESS `lambda_max(Hess log rho) >= 3/4-o(1)` SOMEWHERE, OR GRADIENT IS IMPORTED THROUGH A BOUNDARY/HARD-HULL EXIT. AT A PURE-KERNEL LINE PEAK `g=D_xi log rho=0`, THE LOG-AMPLITUDE HESSIAN SATISFIES `H_xixi=D_xi g-(D_xi xi)·grad log rho`, `H_xik=D_k g`, AND `H_xin=D_n g-(D_n xi)·grad log rho`. THEREFORE AT DIRECTOR-AREA TANGENCY `D_k g=0`, THE `xi-k` HESSIAN ENTRY VANISHES EXACTLY. FOR A STRICT LINE MAXIMUM `C_xi:=D_xi g<0`, ANY AXIAL CONTRIBUTION `H_xixi >= 3/4-delta` REQUIRES THE SHARP CURVATURE-GRADIENT PAYMENT `-(D_xi xi)·grad log rho >= 3/4-delta+|C_xi|`. IF THAT PAYMENT AND THE `xi-n` MIXING `D_n g-(D_n xi)·grad log rho` ARE BOTH SMALL, THE REQUIRED `3/4` EIGENVALUE MUST LIE IN THE PURE TRANSVERSE `(k,n)` HESSIAN BLOCK. THUS THE QUIET FOLD FIREWALL SPLITS INTO AXIAL CURVATURE COMPENSATION, TILT/MIXED COMPENSATION, OR TRANSVERSE LOG-AMPLITUDE CONVEXITY. NONE IS YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pure-kernel peak frame

Work at a full-rank pure-transverse-kernel peak and use the orthonormal frame

\[
(\xi,k,n),
\qquad
D_k\xi=0.
\]

Write

\[
\boxed{\psi:=\log\rho}
\]

and

\[
\boxed{g:=D_\xi\psi.}
\]

At a line peak,

\[
\boxed{g=0.}
\]

Set the two surviving director jets

\[
\boxed{
\mathfrak b:=D_\xi\xi=pk+qn,
}
\]

and

\[
\boxed{
\mathfrak a:=D_n\xi=rk.
}
\]

Full Rank 2 requires

\[
q\neq0,
\qquad
r\neq0,
\]

and

\[
|J_\xi|=|rq|
\]

up to the fixed orientation convention.

Since `g=0`, write the log-amplitude gradient as

\[
\boxed{
\nabla\psi=u\,k+v\,n,
}
\]

where

\[
u:=D_k\psi,
\qquad
v:=D_n\psi.
\]

---

## 2. Directional derivatives of `g` are Hessian entries plus frame curvature

Let

\[
H:=\nabla^2\psi.
\]

For any unit frame direction `e`,

\[
D_e g
=D_e(\xi\cdot\nabla\psi)
=(D_e\xi)\cdot\nabla\psi
+H(e,\xi).
\]

Hence

\[
\boxed{
H_{\xi\xi}
=D_\xi g-\mathfrak b\cdot\nabla\psi
}
\]

or in components

\[
\boxed{
H_{\xi\xi}
=D_\xi g-pu-qv.
}
\]

Because

\[
D_k\xi=0,
\]

we have the especially simple identity

\[
\boxed{
H_{\xi k}=D_k g.
}
\]

Finally,

\[
\boxed{
H_{\xi n}
=D_n g-\mathfrak a\cdot\nabla\psi
=D_n g-r u.
}
\]

These are exact Euclidean identities.

---

## 3. Tangency kills one Hessian mixing channel exactly

A director-area/peak tangency is

\[
\boxed{D_k g=0.}
\]

Therefore

\[
\boxed{H_{\xi k}=0.}
\]

At a peak tangency the log-amplitude Hessian has the exact form

\[
\boxed{
H=
\begin{pmatrix}
A & 0 & C\\
0 & B & D\\
C & D & E
\end{pmatrix}_{(\xi,k,n)},
}
\]

where

\[
\boxed{
A=D_\xi g-pu-qv,
}
\]

\[
\boxed{
C=D_n g-r u,
}
\]

and

\[
B=H_{kk},
\qquad
D=H_{kn},
\qquad
E=H_{nn}.
\]

Thus the `xi-k` mixing channel is completely absent at the fold contact.

---

## 4. Strict line maximum constrains the axial Hessian through a curvature payment

For a strict line-amplitude maximum define

\[
\boxed{C_\xi:=D_\xi g<0.}
\]

Then

\[
A
=C_\xi-\mathfrak b\cdot\nabla\psi
=-|C_\xi|-\mathfrak b\cdot\nabla\psi.
\]

Therefore an axially positive Hessian entry of size at least `tau` requires

\[
A\ge\tau
\]

and hence

\[
\boxed{
-\mathfrak b\cdot\nabla\psi
\ge
\tau+|C_\xi|.
}
\]

In components,

\[
\boxed{
-(pu+qv)
\ge
\tau+|C_\xi|.
}
\]

For the M17-147 threshold

\[
\tau=\frac34-\delta,
\]

this becomes

\[
\boxed{
-(D_\xi\xi)\cdot\nabla\log\rho
\ge
\frac34-\delta+|D_\xi g|.
}
\]

Thus a strict line maximum can still have strongly positive straight-line Hessian curvature in the `xi` direction only if the curvature of the vortex integral curve contributes a still larger opposite-signed geometric term.

This is the **axial curvature-compensation payer**.

---

## 5. The only surviving axial mixing is `xi-n`

At tangency,

\[
H_{\xi n}
=D_n g-rD_k\psi.
\]

Define

\[
\boxed{
M_{\xi n}
:=D_n g-(D_n\xi)\cdot\nabla\psi
=D_n g-r u.
}
\]

This is the sole off-diagonal Hessian entry coupling the vortex direction to the transverse plane.

On the orthogonal-stretch subbranch used in M17-071, the maximum-surface tilt ratio is

\[
\Theta
:=\frac{D_n g}{-D_\xi g}.
\]

Hence there

\[
\boxed{
M_{\xi n}
=|D_\xi g|\,\Theta-rD_k\psi.
}
\]

So large `xi-n` Hessian mixing means a mismatch between

1. the geometric tilt of the peak surface, and
2. the director-curvature-weighted kernel gradient of `log rho`.

This is the **tilt/mixed-compensation payer**.

---

## 6. Pure transverse Hessian block

Define the transverse block

\[
\boxed{
H_\perp
:=
\begin{pmatrix}
H_{kk} & H_{kn}\\
H_{kn} & H_{nn}
\end{pmatrix}.
}
\]

Let

\[
\lambda_\perp
:=\lambda_{max}(H_\perp).
\]

This block is not directly constrained by the line-peak condition `D_xi g<0`.
It represents genuine convexity of `log rho` in the plane orthogonal to the vortex direction.

This is the **transverse-convexity payer**.

---

## 7. Quantitative three-payer split for the `3/4` gate

At tangency write

\[
H=H_0+E_{mix},
\]

with

\[
H_0
=
A\,\xi\otimes\xi
\oplus H_\perp
\]

and

\[
E_{mix}
=C(\xi\otimes n+n\otimes\xi).
\]

The operator norm of the mixing perturbation is

\[
\boxed{\|E_{mix}\|_{op}=|C|.}
\]

By Weyl's inequality,

\[
\lambda_{max}(H)
\le
\max\{A,\lambda_\perp\}+|C|.
\]

Suppose M17-147 requires

\[
\lambda_{max}(H)
\ge
\frac34-\varepsilon_R,
\qquad
\varepsilon_R\to0.
\]

Fix any `delta>0`.
For all sufficiently large `R`, at least one of the following must hold:

\[
\boxed{
A
\ge
\frac34-\delta,
}
\]

or

\[
\boxed{
\lambda_\perp
\ge
\frac34-\delta,
}
\]

or

\[
\boxed{
|M_{\xi n}|
\ge
\delta-\varepsilon_R.
}
\]

More invariantly, the required convexity must be paid by at least one of

\[
\boxed{
\begin{aligned}
G_{axial}:&\quad
-(D_\xi\xi)\cdot\nabla\log\rho
\gtrsim
\frac34+|D_\xi g|,\\
G_{mix}:&\quad
\left|D_n g-(D_n\xi)\cdot\nabla\log\rho\right|
\gtrsim1,\\
G_{trans}:&\quad
\lambda_{max}\left(\nabla^2\log\rho\big|_{\xi^\perp}\right)
\gtrsim\frac34.
\end{aligned}
}
\]

Constants here are threshold-scale statements; the exact `delta` version above is the rigorous local split.

---

## 8. Scalar CE-H trace identity in the peak frame

M17-144/M17-147 give

\[
\kappa
=\Delta\psi+|\nabla\psi|^2-|\nabla\xi|^2.
\]

At the peak,

\[
|\nabla\psi|^2=u^2+v^2.
\]

Also

\[
|\nabla\xi|^2
=|D_\xi\xi|^2+|D_n\xi|^2
=p^2+q^2+r^2
\]

because `D_k xi=0`.

Therefore

\[
\boxed{
A+B+E
=
\kappa-u^2-v^2+p^2+q^2+r^2.
}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}H_\perp
=
\kappa-u^2-v^2+p^2+q^2+r^2-A.
}
\]

This constrains the sum of the transverse curvatures but does not control their largest eigenvalue from above.

---

## 9. Full-rank director area supplies a geometric floor but not a contradiction

Since

\[
|J_\xi|=|rq|,
\]

an order-one nondegenerate director-area branch has

\[
|rq|\ge c_J>0.
\]

Hence

\[
q^2+r^2
\ge2|rq|
\ge2c_J.
\]

Thus the positive director metric contribution in the trace identity cannot disappear.

However this makes positive log-amplitude trace easier, not harder, so it does **not** contradict the M17-147 convexity gate.
It explains why the scale-free director geometry can support nontrivial normalized amplitude curvature even when the physical amplitude tends to zero.

---

## 10. Orthogonal-stretch specialization

On the orthogonal-stretch subbranch,

\[
p=0,
\qquad
D_\xi\xi=q n.
\]

The axial entry becomes

\[
\boxed{
H_{\xi\xi}
=D_\xi g-qD_n\psi.
}
\]

If it alone pays the threshold,

\[
H_{\xi\xi}\ge\frac34-\delta,
\]

then

\[
\boxed{
-qD_n\log\rho
\ge
\frac34-\delta+|D_\xi g|.
}
\]

Thus `q` and the `n`-gradient of log amplitude must have opposite signs with quantitatively large product.

The mixed entry becomes

\[
\boxed{
H_{\xi n}
=D_n g-rD_k\log\rho.
}
\]

These are direct descriptors that can be compared to the M17-071 tilted-maximum compensation branch.

---

## 11. DSD audit

### Audit A — line maximum makes the log-amplitude Hessian negative in the `xi` direction

Rejected.
The line follows a curved vortex trajectory. The straight Euclidean Hessian entry differs from the trajectory second derivative by `(D_xi xi)·grad log rho`.

### Audit B — tangency kills all vortex/transverse Hessian mixing

Rejected.
It kills `H_xik` exactly, but `H_xin` remains.

### Audit C — `lambda_max(H)>=3/4` means the transverse block alone has eigenvalue at least `3/4`

Rejected unless the axial entry and `xi-n` mixing are separately controlled.

### Audit D — full-rank director area makes the Hessian threshold impossible

Rejected.
The director metric enters the CE-H trace with a positive sign.

### Audit E — the three-payer split is a contradiction

Rejected.
It is a finite geometric classification of the only ways the M17-147 threshold can be realized.

---

## 12. Updated frontier

The quiet generic-fold branch now satisfies the chain

\[
\boxed{
\text{generic fold}
\Rightarrow
|D_\xi\kappa|\gtrsim1
\Rightarrow
|\nabla\kappa|\gtrsim1
\Rightarrow
\lambda_{max}(\nabla^2\log\rho)\ge\frac34-o(1)
}
\]

for recurrently regenerated interior fold gradients under the retained high-jet assumptions.

At peak tangency this last gate splits into

\[
\boxed{
G_{axial}
\lor
G_{mix}
\lor
G_{trans}.
}
\]

The next efficient calculation is to compare these three payers with the pre-existing pure-kernel maximum compensation laws, especially the orthogonal-stretch M17-071 branch, and test whether any payer is already equivalent to a previously closed Riccati/focusing class.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
