# DSD M17-181 — At a regular M5 `kappa=0` crossing, the local `l=3` pressure-source orientation depends on third `kappa` and amplitude jets beyond the crossing-rate sign

Date: 2026-09-06  
Canonical ID: **M17-181**

Status: **REGULAR-CROSSING LOCAL PRESSURE AUDIT / AFTER M17-178--180, THE CORRECT M5 SUPPORT IS A REGULAR VORTEX-LINE CROSSING WITH `rho>0`, NOT THE NODAL FILAMENT. EXPANDING THE `-kappa rho^2` PRESSURE-PRODUCTION DENSITY AT SUCH A POINT SHOWS THAT THE FIRST CUBIC STF TENSOR IS `-STF[(1/6)sym(k tensor H_R + g tensor H_kappa)+(R/6)T_kappa]`, WHERE `R=rho^2`, `k=grad kappa`, `g=grad R`, `H_R=Hess R`, `H_kappa=Hess kappa`, AND `T_kappa=grad^3 kappa`. M5'S CONSTITUTIVE CROSSING LAW AT `kappa=0` CONTROLS ONLY `L_rho kappa=tr H_kappa+(g dot k)/R` TOGETHER WITH THE STRAIN/GEOMETRIC TERMS. IT DOES NOT CONTROL THE STF PART OF `H_kappa` OR `T_kappa`. THEREFORE THE SIGN OF `h` OR THE GLOBAL M5 HYSTERESIS DOES NOT DETERMINE THE REGULAR LOCAL `l=3` PRESSURE ORIENTATION. THE NODAL SIMPLIFICATION OF M17-090 WAS SPECIAL BECAUSE `rho=0` AND THE NODAL JET IDENTITIES COLLAPSED THESE LOWER-ORDER FREEDOMS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular M5 crossing data

Work at a regular material vortex-line point where

\[
\boxed{
\kappa(0)=0,
\qquad
\rho(0)>0,
\qquad
\nabla\kappa(0)\neq0.
}
\]

Set

\[
\boxed{R:=\rho^2.}
\]

At the crossing define

\[
\boxed{
R_0=R(0)>0,
\quad
k=\nabla\kappa(0),
\quad
g=\nabla R(0),
}
\]

\[
\boxed{
H_\kappa=\nabla^2\kappa(0),
\quad
H_R=\nabla^2R(0),
\quad
T_\kappa=\nabla^3\kappa(0).
}
\]

The relevant pressure-production source piece is

\[
\boxed{f=-\kappa R.}
\]

---

## 2. Taylor expansion through cubic order

Expand

\[
\kappa(x)
=k\cdot x
+\frac12H_\kappa[x,x]
+\frac16T_\kappa[x,x,x]
+O(|x|^4),
\]

and

\[
R(x)
=R_0+g\cdot x
+\frac12H_R[x,x]
+O(|x|^3).
\]

Their product gives

\[
\begin{aligned}
-\kappa R
={}&-R_0(k\cdot x)\\
&-\left[(k\cdot x)(g\cdot x)+\frac{R_0}{2}H_\kappa[x,x]\right]\\
&-\left[
\frac12(k\cdot x)H_R[x,x]
+\frac12(g\cdot x)H_\kappa[x,x]
+\frac{R_0}{6}T_\kappa[x,x,x]
\right]\\
&+O(|x|^4).
\end{aligned}
\]

The linear and quadratic pieces contain only `l<=2` angular information.
The first possible `l=3` contribution is the cubic line.

---

## 3. Exact regular local cubic tensor

Use the convention

\[
f_3(x)=T_{ijk}x_ix_jx_k.
\]

For a vector `v` and symmetric matrix `H`,

\[
\operatorname{sym}(v\otimes H)_{ijk}
=v_iH_{jk}+v_jH_{ik}+v_kH_{ij}.
\]

Since contraction with `x_i x_j x_k` produces

\[
3(v\cdot x)H[x,x],
\]

the cubic coefficient tensor is

\[
\boxed{
T_{reg}
=-\left[
\frac16\operatorname{sym}(k\otimes H_R)
+\frac16\operatorname{sym}(g\otimes H_\kappa)
+\frac{R_0}{6}T_\kappa
\right].
}
\]

Therefore the local regular-crossing octupole is

\[
\boxed{
\mathcal O_{reg}^{(3)}
=STF_3(T_{reg}).
}
\]

Equivalently,

\[
\boxed{
\mathcal O_{reg}^{(3)}
=-STF_3\!\left[
\frac16\operatorname{sym}(k\otimes H_R+g\otimes H_\kappa)
+\frac{R_0}{6}T_\kappa
\right].
}
\]

---

## 4. What the M5 crossing rate controls

M5-682 gives at `kappa=0`

\[
\boxed{
h
=L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{geom}.
}
\]

The weighted operator is

\[
L_\rho f
=\Delta f+2\nabla\log\rho\cdot\nabla f.
\]

Since

\[
\nabla\log\rho
=\frac{\nabla R}{2R}
=\frac{g}{2R_0}
\]

at the crossing,

\[
\boxed{
L_\rho\kappa
=\operatorname{tr}H_\kappa
+\frac{g\cdot k}{R_0}.
}
\]

Thus the scalar crossing rate controls, after subtracting the strain/geometric channels, only the scalar combination

\[
\boxed{
\operatorname{tr}H_\kappa
+\frac{g\cdot k}{R_0}.
}
\]

---

## 5. The missing angular information

The octupole tensor in Section 3 depends on

1. `H_R`;
2. the **full anisotropic tensor** `H_kappa`, not only its trace;
3. the full symmetric rank-three tensor `T_kappa`.

Hence even if `h` is known exactly, the data

\[
\boxed{
STF(H_\kappa),
\qquad
STF_3(T_\kappa),
\qquad
H_R
}
\]

remain available to rotate or cancel the local `l=3` orientation.

There is no implication

\[
\boxed{
\operatorname{sgn}h
\Longrightarrow
\operatorname{sgn}(E:\mathcal O_{reg}^{(3)})
}
\]

for a fixed STF test tensor `E` without additional jet control.

---

## 6. Why the nodal formula was much stronger

At the vertical nodal filament, M17-090 has

\[
R_0=\rho^2=0,
\]

plus

\[
\nabla_h\kappa=0,
\qquad
q_{13}=q_{23}=0,
\]

and the vorticity Jacobian has a special block form.

Those identities collapse the local cubic vertical component to

\[
O_V=-\frac15|Q|_F^2\kappa_3
\]

at `kappa=0`.

The regular M5 crossing has none of these nodal cancellations.
Therefore the nodal sign bridge cannot simply be extended to regular positive-vorticity labels.

---

## 7. Consequence for the corrected Rank-1 strategy

After M17-178--180, there are two legitimate routes:

### Route A — nodal localization
Prove that the regular M5 zero-current localizes with controlled trace to the nodal critical level.
Then M17-090 and M17-164 become usable.

### Route B — regular-label angular rigidity
Stay on the actual M5 regular support and derive new PDE constraints controlling

\[
STF(H_\kappa),
\quad
T_\kappa,
\quad
H_R
\]

well enough to constrain `O_reg^(3)`.

M5-682 alone does not supply that rigidity.

---

## 8. DSD audit

### Audit A — treating `h` as an octupole sign
Rejected. `h` controls a scalar second-jet trace balance.

### Audit B — importing the nodal simplification to `rho>0`
Rejected.

### Audit C — blind differentiation
Differentiating M5-682 may expose the missing jets but risks rebuilding the same unclosed higher-jet ladder found in M17-151--154. A new coercive principle is preferred.

### Audit D — proof status
The corrected regular-label route reaches a precise third-jet angular firewall, not a contradiction.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
