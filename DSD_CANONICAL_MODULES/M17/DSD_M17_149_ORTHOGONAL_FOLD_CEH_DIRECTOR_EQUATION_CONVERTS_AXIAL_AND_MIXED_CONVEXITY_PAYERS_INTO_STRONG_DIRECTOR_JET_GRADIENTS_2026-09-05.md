# DSD M17-149 — On an orthogonal fold, the CE-H director equation converts axial and mixed convexity payers into strong director-jet gradients

Date: 2026-09-05  
Canonical ID: **M17-149**

Status: **ORTHOGONAL-STRETCH FOLD REFINEMENT / M17-148 SPLITS THE M17-147 `3/4` LOG-AMPLITUDE CONVEXITY GATE INTO AXIAL CURVATURE COMPENSATION, `xi-n` MIXING, OR PURE TRANSVERSE CONVEXITY. ON THE ORTHOGONAL-STRETCH PEAK SUBBRANCH, `D_xi xi=q n`, `D_n xi=r k`, `D_k xi=0`. COMBINING THE EXACT NORMALIZED CE-H DIRECTOR EQUATION `Delta xi+2 grad(log rho)·grad xi+|grad xi|^2 xi=0` WITH THE M17-047 FLATNESS CONNECTIONS AT A PEAK TANGENCY GIVES TWO NEW EXACT RELATIONS: `D_n g=D_xi q-D_k r`, HENCE `H_xin=D_xi q-D_k r-rD_k log rho`; AND `2rD_n log rho=-(q/r)D_xi g+q^3/r+2qr-D_n r`. CONSEQUENTLY THE AXIAL HESSIAN ENTRY IS `H_xixi=C_xi(1+q^2/(2r^2))-q^2-q^4/(2r^2)+(q/(2r))D_n r`, `C_xi=D_xi g<0`. IF THIS AXIAL ENTRY PAYS A THRESHOLD `tau>0`, THEN `(q/r)D_n r` MUST EXCEED A STRICTLY POSITIVE QUANTITATIVE BOUND. THUS AXIAL CONVEXITY IS NOT A FREE AMPLITUDE EFFECT: IT REQUIRES A STRONG TRANSVERSE GRADIENT OF THE NONZERO DIRECTOR JET `r`. THE MIXED PAYER SIMILARLY REQUIRES A MISMATCH AMONG `D_xi q`, `D_k r`, AND `rD_k log rho`. PURE TRANSVERSE HESSIAN CONVEXITY REMAINS A SEPARATE FIREWALL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Orthogonal-stretch critical frame

On the orthogonal pure-kernel branch M17-047 gives, at a line critical point,

\[
\boxed{
D_\xi\xi=q n,
\qquad
D_n\xi=r k,
\qquad
D_k\xi=0,
}
\]

with

\[
q\neq0,
\qquad
r\neq0.
\]

Define

\[
\psi:=\log\rho,
\qquad
g:=D_\xi\psi.
\]

At the peak,

\[
g=0,
\]

so write

\[
\boxed{
\nabla\psi=u k+v n,
}
\]

where

\[
u:=D_k\psi,
\qquad
v:=D_n\psi.
\]

Let

\[
\boxed{C_\xi:=D_\xi g<0}
\]

for a strict line maximum.

At a director-area tangency,

\[
\boxed{D_k g=0.}
\]

---

## 2. Flatness connection data at the orthogonal critical point

M17-047 uses

\[
D_\xi k=\alpha n,
\qquad
D_\xi n=-q\xi-\alpha k,
\]

\[
D_k k=\beta n,
\qquad
D_k n=-\beta k,
\]

\[
D_n k=-r\xi+\delta n,
\qquad
D_n n=-\delta k
\]

at the critical point.

Its flatness identities give

\[
\boxed{
\alpha=\frac{q^2}{r},
}
\]

and

\[
\boxed{
\delta=-\frac{D_k r}{r}.
}
\]

Also, because `t=-g` in the general orthogonal frame,

\[
\beta=q-\frac{D_k t}{r}
=q+\frac{D_k g}{r}.
\]

Therefore at tangency,

\[
\boxed{\beta=q.}
\]

The exact critical Riccati relation is

\[
\boxed{
D_nq=2q^2-C_\xi.
}
\]

---

## 3. Normalized CE-H director equation

Starting from

\[
\Delta W=\kappa W,
\qquad
W=\rho\xi,
\]

and separating the component orthogonal to `xi` gives the exact normalized director equation

\[
\boxed{
\Delta\xi
+2\nabla\psi\cdot\nabla\xi
+|\nabla\xi|^2\xi
=0.
}
\]

At the orthogonal peak,

\[
\nabla\psi=u k+v n,
\]

and

\[
D_k\xi=0,
\qquad
D_n\xi=r k.
\]

Hence

\[
2\nabla\psi\cdot\nabla\xi
=2rv\,k.
\]

Also

\[
|\nabla\xi|^2=q^2+r^2.
\]

Therefore

\[
\boxed{
\Delta\xi
=-2rv\,k-(q^2+r^2)\xi.
}
\]

In particular the `n` component of `Delta xi` vanishes exactly.

---

## 4. Compute the moving-frame Laplacian at the critical point

For an arbitrary orthonormal moving frame in Euclidean space,

\[
\Delta\xi
=
\sum_{e\in\{\xi,k,n\}}
\left(
D_eD_e\xi-D_{D_e e}\xi
\right).
\]

The critical alignment `p=t=0` must be imposed only after differentiating the general orthogonal relations, as in M17-047.

A direct calculation gives the `n` component

\[
\boxed{
(\Delta\xi)\cdot n
=D_\xi q+r\delta-D_n g.
}
\]

Because the normalized director equation gives zero `n` component,

\[
0=D_\xi q+r\delta-D_ng.
\]

Using

\[
r\delta=-D_k r,
\]

we obtain the new exact critical identity

\[
\boxed{
D_n g
=D_\xi q-D_k r.
}
\]

---

## 5. Exact mixed log-amplitude Hessian entry

M17-148 gives at every peak

\[
H_{\xi n}
=D_ng-rD_k\psi.
\]

Insert Section 4:

\[
\boxed{
H_{\xi n}
=D_\xi q-D_k r-rD_k\log\rho.
}
\]

Thus the mixed convexity payer cannot be treated as an arbitrary Hessian coefficient.
It is exactly the mismatch among

1. the vortex-direction derivative of the vortex-curvature coefficient `q`,
2. the kernel-direction derivative of the transverse director jet `r`,
3. the normalized kernel amplitude gradient multiplied by `r`.

For a threshold `delta>0`, the M17-148 mixed payer

\[
|H_{\xi n}|\ge\delta
\]

is equivalently

\[
\boxed{
\left|
D_\xi q-D_k r-rD_k\log\rho
\right|
\ge\delta.
}
\]

---

## 6. The `k` component of the director equation

The same moving-frame Laplacian calculation gives

\[
(\Delta\xi)\cdot k
=
D_\xi p-q\alpha-qr-\beta r+D_n r
\]

at the critical point.

On the orthogonal branch the general relation is

\[
p=\frac{gq}{r}.
\]

Hence at `g=0`,

\[
\boxed{
D_\xi p
=\frac qr D_\xi g
=\frac qr C_\xi.
}
\]

At tangency,

\[
\alpha=\frac{q^2}{r},
\qquad
\beta=q.
\]

Therefore

\[
(\Delta\xi)\cdot k
=
\frac qr C_\xi
-\frac{q^3}{r}
-2qr
+D_n r.
\]

The normalized CE-H director equation requires this to equal

\[
-2rv.
\]

Thus

\[
\boxed{
2rD_n\log\rho
=-\frac qr C_\xi
+\frac{q^3}{r}
+2qr
-D_n r.
}
\]

Equivalently,

\[
\boxed{
D_n\log\rho
=-\frac{qC_\xi}{2r^2}
+\frac{q^3}{2r^2}
+q
-\frac{D_n r}{2r}.
}
\]

This is the exact orthogonal peak-tangency amplitude/director-curvature balance.

---

## 7. Eliminate the amplitude gradient from the axial Hessian payer

M17-148 gives on the orthogonal branch

\[
H_{\xi\xi}
=C_\xi-qD_n\psi.
\]

Use Section 6:

\[
qD_n\psi
=-\frac{q^2C_\xi}{2r^2}
+\frac{q^4}{2r^2}
+q^2
-\frac{qD_nr}{2r}.
\]

Therefore

\[
\boxed{
H_{\xi\xi}
=
C_\xi\left(1+\frac{q^2}{2r^2}\right)
-q^2
-\frac{q^4}{2r^2}
+\frac{q}{2r}D_n r.
}
\]

This removes `D_n log rho` completely from the axial payer.

---

## 8. Positive axial convexity forces a strong `D_n r` payment

Suppose the axial entry pays a positive threshold

\[
H_{\xi\xi}\ge\tau,
\qquad
\tau>0.
\]

Since

\[
C_\xi=-|C_\xi|,
\]

Section 7 implies

\[
\boxed{
\frac{q}{2r}D_n r
\ge
\tau
+|C_\xi|\left(1+\frac{q^2}{2r^2}\right)
+q^2
+\frac{q^4}{2r^2}.
}
\]

Equivalently,

\[
\boxed{
\frac qrD_n r
\ge
2\tau
+2|C_\xi|
+|C_\xi|\frac{q^2}{r^2}
+2q^2
+\frac{q^4}{r^2}.
}
\]

Every term on the right is nonnegative and the first is strictly positive.

For the M17-148 axial threshold

\[
\tau=\frac34-\delta>0,
\]

the required `D_n r` payment is uniformly order one on a compact nondegenerate hard hull.

Thus

\[
\boxed{
\text{axial }3/4\text{ convexity}
\Longrightarrow
\text{strong transverse director-jet gradient }D_nr.
}
\]

---

## 9. Relation to director-area magnitude

At the orthogonal critical point,

\[
|J_\xi|=|rq|.
\]

The logarithmic derivative is

\[
D_n\log|J_\xi|
=
\frac{D_n r}{r}
+rac{D_nq}{q}
\]

where defined.

M17-047 gives

\[
D_nq=2q^2+|C_\xi|.
\]

The axial payer gives a strong signed condition on

\[
\frac qrD_n r
=qD_n\log|r|.
\]

Hence, on any orientation sector in which `q` has a fixed sign and stays separated from zero, sustained axial convexity forces strong spatial variation of the director-area density as well.

However this is an instantaneous spatial statement, not yet a complete-curve growth theorem: the fold/maximum conditions need not persist along the `n` integral curve.

---

## 10. Comparison with M17-071

M17-071 shows that an orthogonal tilted maximum surface avoids its Riccati focusing mechanism only through the signed compensation

\[
D_ng\,D_\xi q<-C_\xi^2.
\]

M17-149 does not make the axial or mixed Hessian payer algebraically identical to this condition.
Instead it adds two independent finite-jet requirements:

\[
\boxed{
G_{axial}
\Rightarrow
\frac qrD_n r\gg1,
}
\]

and

\[
\boxed{
G_{mix}
\Rightarrow
\left|D_\xi q-D_k r-rD_k\log\rho\right|\gtrsim1.
}
\]

Therefore the M17-071 compensation firewall and the M17-147/148 convexity firewall intersect but do not collapse into the same scalar condition.

---

## 11. Remaining third payer

The pure transverse block

\[
H_\perp
=
\begin{pmatrix}
H_{kk} & H_{kn}\\
H_{kn} & H_{nn}
\end{pmatrix}
\]

can still satisfy

\[
\lambda_{max}(H_\perp)\ge\frac34-\delta
\]

without requiring either strong axial `D_nr` payment or strong `xi-n` mixing.

No current flatness identity bounds this transverse log-amplitude Hessian eigenvalue from above.
Thus it remains a genuine normalized-amplitude firewall.

---

## 12. DSD audit

### Audit A — cross alignment may be differentiated as `p=0` in a neighborhood

Rejected.
The derivation uses the full orthogonal relation `p=gq/r` before setting `g=0`, exactly as required by M17-047.

### Audit B — the arbitrary moving-frame formula for `Delta xi` is the naive sum `sum D_eD_e xi`

Rejected.
The connection correction `-D_{D_e e}xi` is retained explicitly.

### Audit C — axial convexity is purely an amplitude-Hessian effect

Rejected.
The normalized CE-H director equation converts it into a quantitative `D_nr` payment.

### Audit D — the mixed payer is arbitrary

Rejected.
It equals `D_xi q-D_k r-rD_k log rho` exactly on the orthogonal critical branch.

### Audit E — strong `D_nr` immediately proves finite-distance blowup

Rejected.
The threshold is local to the peak-tangency event; persistence along an `n` curve is not established.

---

## 13. Updated orthogonal-fold frontier

For an interior quiet high-jet orthogonal generic fold, recurrent order-one `D_xi kappa` maintenance requires the M17-147 convexity gate, which M17-148/149 now refines to

\[
\boxed{
\begin{aligned}
&\frac qrD_n r\gtrsim1
&&\text{axial director-jet payer},\\
&\left|D_\xi q-D_k r-rD_k\log\rho\right|\gtrsim1
&&\text{mixed payer},\\
&\lambda_{max}(H_\perp)\gtrsim\frac34
&&\text{pure transverse amplitude-convexity payer},
\end{aligned}
}
\]

up to the explicit threshold constants and hard-hull errors.

The next highest-value calculation is to ask whether a positive director-flux population can pay the first two director-jet gradients at bounded dyadic spacing without violating the analytic finite-jet/zero-count architecture, while treating the pure transverse Hessian branch separately.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
