# DSD M17-339 — Physical CE-H kappa constitutive law has no minus-kappa relaxation after the exact similarity dictionary

Date: 2026-09-08  
Canonical ID: **M17-339**

Status: **ACTIVE REPRESENTATION-CORRECTED CONSTITUTIVE LAW**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-338

Write

\[
r=-t>0,
\qquad
W=r\Omega,
\qquad
\kappa^{sim}=r\kappa^{ph}.
\]

M17-338 proved

\[
\boxed{
h^{sim}:=D_B\kappa^{sim}
=-\kappa^{sim}+r^2h^{ph},}
\]

where

\[
h^{ph}:=D_t\kappa^{ph}.
\]

Thus

\[
\boxed{
h^{sim}+\kappa^{sim}=r^2h^{ph}.}
\]

## 2. Similarity constitutive law

M5-682 gives on exact regular CE-H

\[
\boxed{
h^{sim}
=L_{\rho^{sim}}\kappa^{sim}
+L_{\rho^{sim}}\sigma^{sim}
-\kappa^{sim}
+\mathcal R_{geom}^{sim}.}
\]

Here

\[
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

Adding `kappa^sim` to both sides,

\[
\boxed{
h^{sim}+\kappa^{sim}
=L_{\rho^{sim}}\kappa^{sim}
+L_{\rho^{sim}}\sigma^{sim}
+\mathcal R_{geom}^{sim}.}
\]

## 3. Scaling dictionary for rho and sigma

The similarity/physical fields satisfy

\[
\boxed{
\rho^{sim}=r\rho^{ph},
}
\]

and because

\[
U=\sqrt r\,u,
\qquad
\nabla_yU=r\nabla_xu,
\]

the aligned strain eigenvalue satisfies

\[
\boxed{
\sigma^{sim}=r\sigma^{ph}.}
\]

Also

\[
\nabla_y=\sqrt r\,\nabla_x.
\]

## 4. Weighted operator scaling

For a scalar of the form

\[
f^{sim}=rf^{ph},
\]

we have

\[
\nabla_y f^{sim}=r^{3/2}\nabla_x f^{ph}.
\]

Then

\[
(\rho^{sim})^2\nabla_yf^{sim}
=r^{7/2}(\rho^{ph})^2\nabla_xf^{ph}.
\]

Taking one `y` divergence contributes another factor `sqrt r`, so

\[
\nabla_y\cdot
\left((\rho^{sim})^2\nabla_yf^{sim}\right)
=r^4
\nabla_x\cdot
\left((\rho^{ph})^2\nabla_xf^{ph}\right).
\]

Dividing by

\[
(\rho^{sim})^2=r^2(\rho^{ph})^2
\]

gives

\[
\boxed{
L_{\rho^{sim}}f^{sim}
=r^2L_{\rho^{ph}}f^{ph}.}
\]

Therefore

\[
\boxed{
L_{\rho^{sim}}\kappa^{sim}
=r^2L_{\rho^{ph}}\kappa^{ph},
}
\]

and

\[
\boxed{
L_{\rho^{sim}}\sigma^{sim}
=r^2L_{\rho^{ph}}\sigma^{ph}.}
\]

## 5. Geometric remainder scaling

M5-682 defines

\[
\mathcal R_{geom}^{sim}
=
-
\frac{2}{\rho^{sim}}
\Sigma^{sim}:\nabla_y^2\rho^{sim}
+
2\Sigma^{sim}_{ij}
\partial_{y_i}\xi\cdot\partial_{y_j}\xi
+
(\nabla_y\times W)\cdot\nabla_y\log\rho^{sim}.
\]

Each term carries exactly `r^2`:

- `Sigma^sim=r Sigma^ph`;
- `nabla_y^2 rho^sim=r^2 nabla_x^2 rho^ph`;
- `partial_y xi=sqrt r partial_x xi`;
- `curl_y W=r^(3/2) curl_x Omega`;
- `nabla_y log rho^sim=sqrt r nabla_x log rho^ph`.

Hence

\[
\boxed{
\mathcal R_{geom}^{sim}
=r^2\mathcal R_{geom}^{ph},
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal R_{geom}^{ph}
:={}&
-
\frac{2}{\rho^{ph}}
\Sigma^{ph}:\nabla_x^2\rho^{ph}\\
&+
2\Sigma^{ph}_{ij}
\partial_{x_i}\xi\cdot\partial_{x_j}\xi
+
(\nabla_x\times\Omega)\cdot\nabla_x\log\rho^{ph}.
\end{aligned}
}
\]

## 6. Physical constitutive law

Substitute the scaling identities into Section 2:

\[
r^2h^{ph}
=
r^2L_{\rho^{ph}}\kappa^{ph}
+r^2L_{\rho^{ph}}\sigma^{ph}
+r^2\mathcal R_{geom}^{ph}.
\]

Cancel `r^2`:

\[
\boxed{
D_t\kappa^{ph}
=
L_{\rho^{ph}}\kappa^{ph}
+
L_{\rho^{ph}}\sigma^{ph}
+
\mathcal R_{geom}^{ph}.
}
\]

There is **no** physical `-kappa` relaxation term.

## 7. Meaning of the similarity minus-kappa term

The similarity law contained

\[
-\kappa^{sim}.
\]

M17-339 shows that this term is exactly the derivative of the similarity normalization factor in

\[
\kappa^{sim}=(-t)\kappa^{ph}.
\]

Therefore the interpretation

\[
\boxed{
-\kappa\text{ is an intrinsic physical relaxation mechanism}
}
\]

is rejected.

It is a legitimate term in the similarity-coordinate constitutive equation, but it must be removed when translating to the scale-homogeneous physical coefficient.

## 8. Zero-level simplification

At

\[
\kappa^{ph}=0,
\]

the physical coefficient velocity is

\[
\boxed{
h^{ph}
=L_{\rho^{ph}}\kappa^{ph}
+L_{\rho^{ph}}\sigma^{ph}
+\mathcal R_{geom}^{ph}.}
\]

This gives the correct physical constitutive object underlying the scale-critical zero-crossing currency salvaged in M17-338.

The zero-level current cannot be paid by a representation `-kappa` term because that term is absent physically and vanishes at zero even in similarity variables.

## 9. Physical kappa-space push-forward

On a regular high-amplitude physical population, define

\[
F_E^{ph}(k,t)
:=
\int\delta(k-\kappa^{ph})\chi\,(\rho^{ph})^2dx,
\]

\[
G_E^{ph}(k,t)
:=
\int h^{ph}\delta(k-\kappa^{ph})\chi\,(\rho^{ph})^2dx.
\]

Repeating the M5-683 integration by parts now yields schematically

\[
\boxed{
G_E^{ph}
=
\partial_k
\left(A_{\kappa\kappa}^{ph}
+A_{\kappa\sigma}^{ph}\right)
+\mathcal R_\chi^{ph},
}
\]

with no `-kF_E` term.

This is the scale-homogeneous physical current identity.

The exact cutoff terms must be transported consistently if this formula is used across record generations.

## 10. DSD-theory role

The useful DSD heuristic was to ask whether a term survives removal of the representation map.

The answer here is decisive:

\[
\boxed{
\text{similarity }(-\kappa)
\text{ does not survive as physical dynamics.}
}
\]

The canonical result is entirely the standard similarity-variable change of variables.

## 11. Updated target

The next valid cross-generation route is now:

\[
\boxed{
\text{similarity zero-current}
\xrightarrow[\kappa=0]{\text{M17-338 dictionary}}
\text{physical zero-crossing currency}
\xrightarrow{\text{M17-339 constitutive law}}
\text{physical diffusion/strain/geometry channels}.
}
\]

This avoids the invalid positive-threshold scaling shortcut of M17-336/337.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
