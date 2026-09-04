# DSD M17-042 — Frozen-angle shear has an exact material surface charge but is not independent of director-area flux

Date: 2026-09-04
Canonical ID: **M17-042**

Status: **INTERNAL SHEAR-TURNOVER LEDGER AUDIT / ON THE FROZEN-ANGLE PURE-KERNEL BRANCH, THE SIGNED SHEAR `m=a·b` OBEYS `D_B m=(sigma_k-1)m`. A MATERIAL AREA ELEMENT WHOSE NORMAL IS THE DIRECTOR-AREA CURRENT DIRECTION `k` OBEYS `D_B log dA_k=1-sigma_k`, SO `m dA_k` IS AN EXACT MATERIAL SURFACE CHARGE. HOWEVER THE DIRECTOR-AREA FLUX `|J_xi| dA_k` IS ALREADY CONSERVED AND M17-041 GIVES THE MATERIAL-INVARIANT RATIO `m/|J_xi|=c/sqrt(1-c^2)`. THEREFORE THE SHEAR SURFACE CHARGE IS ONLY A FIXED MULTIPLE OF THE EXISTING DIRECTOR-AREA FLUX, NOT A SECOND INDEPENDENT LEDGER. A DUAL-CHARGE TURNOVER CONTRADICTION CANNOT BE CLAIMED FROM FROZEN-ANGLE SHEAR ALONE. THE VALUE OF THE RESULT IS NEGATIVE BUT IMPORTANT: IT REMOVES A FALSE CLOSURE ROUTE AND SHOWS THAT ANY FURTHER OBSTRUCTION MUST COME FROM THE SHEAR-STRESS PDE, CURVATURE, OR INTERACTION WITH THE M5 VORTICITY-FLUX LEDGER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Signed frozen-angle shear

On the M17-041 branch define

\[
\boxed{m:=a\cdot b.}
\]

The target-angle invariant gives

\[
\frac{m}{|J_\xi|}
=\frac{c}{\sqrt{1-c^2}},
\qquad
D_Bc=0.
\]

M17-041 also gives

\[
\boxed{
D_Bm=(\sigma_k-1)m.
}
\]

Hence while `m!=0`,

\[
\boxed{
D_B\log|m|=\sigma_k-1.
}
\]

---

## 2. Material area normal to k

Let `dA_k` be a material surface area element whose instantaneous unit normal is

\[
k=J_\xi/|J_\xi|.
\]

For a material area element with normal `nu`, the similarity-flow area law is

\[
D_B\log dA
=\nabla\cdot B-\nu\cdot(\nabla B)\nu.
\]

Since

\[
\nabla\cdot B=\frac32
\]

and the antisymmetric part drops from the quadratic form,

\[
k\cdot(\nabla B)k
=\sigma_k+\frac12.
\]

Therefore

\[
\boxed{
D_B\log dA_k
=1-\sigma_k.
}
\]

---

## 3. Exact shear surface charge

Add the two logarithmic laws:

\[
D_B\log|m|
+D_B\log dA_k
=(\sigma_k-1)+(1-\sigma_k)=0.
\]

Hence

\[
\boxed{
D_B(|m|dA_k)=0.
}
\]

With fixed orientation/sign on a regular material patch,

\[
\boxed{
D_B(m\,dA_k)=0.
}
\]

Thus the off-diagonal weighted-harmonic shear carries an exact material surface charge.

---

## 4. Director-area flux through the same material patch

The director-area current obeys the Cauchy frozen-in law and is divergence free.
Therefore its flux through a material surface is conserved:

\[
\boxed{
D_B(|J_\xi|dA_k)=0
}
\]

on the aligned local patch.

Equivalently,

\[
D_B\log|J_\xi|
=\sigma_k-1,
\]

which is exactly the same pointwise multiplier as `m`.

---

## 5. The two surface charges are proportional

From M17-041,

\[
\boxed{
\frac{m}{|J_\xi|}
=\frac{c}{\sqrt{1-c^2}}
}
\]

with material-constant `c`.

Therefore

\[
\boxed{
 m\,dA_k
=
\frac{c}{\sqrt{1-c^2}}
|J_\xi|dA_k.
}
\]

The shear surface charge is a fixed multiple of the director-area flux.

It is not an independent conservation law.

---

## 6. Consequence for turnover arguments

Suppose a bounded Eulerian frozen-angle core is repopulated by material turnover.
Conservation of the director-area flux already requires entering material to carry the required `J_xi` charge.

Because the target angle `c` is frozen on each material carrier, the accompanying shear charge is automatically

\[
\frac{c}{\sqrt{1-c^2}}
\]

times that area flux.

Thus servicing the shear ledger does **not** impose a second independent amount of conserved material data beyond servicing the director-area flux itself.

The proposed closure

\[
\text{two independent geometric ledgers}
\Longrightarrow
\text{turnover contradiction}
\]

fails at this level.

---

## 7. What remains genuinely independent

The M5 vorticity-flux/amplification ledger is still distinct.

The two relevant systems are therefore

\[
\boxed{
\text{director-area/shear flux}
}
\]

and

\[
\boxed{
\text{vorticity flux with kappa amplification/hysteresis}.
}
\]

Their relationship is nontrivial because M17-026 makes `J_xi` co-frozen with the **rescaled** vorticity `W/a`, not with raw `W`.

Thus the remaining turnover question is still a two-ledger problem, but the ledgers are

1. director-area/shear;
2. raw vorticity flux/amplification;

not three independent quantities.

---

## 8. DSD interpretation

A new formula can look like a new invariant while actually being the same structural information in another descriptor.

Here

\[
m\,dA_k
\]

and

\[
|J_\xi|dA_k
\]

are two descriptions of one material charge, related by the frozen target angle.

This is exactly the kind of redundant descriptor that DSD audit is intended to identify before it is counted twice in a contradiction argument.

---

## 9. DSD audit

### Audit A — counting shear and director-area as two charges
Rejected. They are proportional on each regular frozen-angle material carrier.

### Audit B — claiming the proportionality is globally constant across all carriers
Rejected. The value of `c` can differ between distinct material labels; it is constant only along each label.

### Audit C — discarding shear as useless
Rejected. Although not a new conservation law, shear enters the weighted-harmonic stress equations dynamically and can still create a PDE obstruction.

### Audit D — proof status
No branch is closed by this conservation audit.

---

## 10. Updated frozen-angle target

The next closure must use the actual stress dynamics

\[
\boxed{
\begin{aligned}
D_\xi d+D_nm
+m(2D_n\log\rho-2q-\gamma)&=E\nabla\cdot\xi,\\
D_nd&=D_\xi m+A^2(2D_n\log\rho-\gamma)+2dq,
\end{aligned}
}
\]

or couple director-area flux to the distinct M5 raw-vorticity amplification ledger.

A purely kinematic second-charge argument is exhausted.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
