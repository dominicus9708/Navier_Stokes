# Transverse second-vorticity-derivative gate

Date: 2026-08-25

Status: **ACTIVE CALCULATION — GLOBAL REGULARITY NOT PROVED**

This note sharpens `STRAIN_KERNEL_SECOND_MOMENT_CANCELLATION_2026-08-25.md` by using the fact that first-hitting growth depends on the scalar vortex-stretching contraction `gamma=xi^T S xi`, not on the full strain norm.

---

## 1. Direction-contracted strain formula

Fix a point `x_*` with

\[
W=|\omega(x_*)|>0,
\qquad
\xi_*=\frac{\omega(x_*)}{W}.
\]

For the standard strain kernel, contraction with `xi_*` on both matrix indices gives a representation of the form

\[
\boxed{
\gamma(x_*)
:=\xi_*^TS(x_*)\xi_*
=
c_0\operatorname{p.v.}\int_{\mathbb R^3}
\frac{(\xi_*\cdot\widehat z)
\left[(\xi_*\times\omega(x_*-z))\cdot\widehat z\right]}
{|z|^3}\,dz,
}
\]

up to the fixed conventional sign of the Biot-Savart kernel.

For estimates only the absolute value and kernel parity matter.

Crucially,

\[
\xi_*\times\omega(x_*)=0.
\]

Thus locally aligned vorticity magnitude, no matter how large, does not by itself contribute to `gamma` through the singular part.

Status: **STANDARD KINEMATIC IDENTITY / PROVED.**

---

## 2. Linear transverse jet cancels by parity

Define

\[
F(z):=\xi_*\times\omega(x_*-z).
\]

Then

\[
F(0)=0.
\]

Taylor expand

\[
F(z)
=DF(0)z+\mathcal R_2(z),
\]

where

\[
|\mathcal R_2(z)|
\le
C|z|^2
\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|.
\]

The angular factor

\[
(\xi_*\cdot\widehat z)
\left[(\,\cdot\,)\cdot\widehat z\right]
\]

contains two factors linear in `widehat z`; consequently the effective kernel in the direction-contracted integral is even under `z -> -z`.

The linear Taylor term `DF(0)z` is odd.  On the centered ball it therefore integrates to zero.

Hence the local stretching starts at second transverse derivative order:

\[
\boxed{
|\gamma_{<r}(x_*)|
\lesssim
r^2
\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|.
}
\]

Status: **PROVED.**

---

## 3. Natural-scale transverse curvature

At a maximum-vorticity point let

\[
r=\left(\frac\nu W\right)^{1/2}.
\]

Define

\[
\boxed{
Q_{\perp,2}(r,t;x_*)
:=
\frac{r^2}{W}
\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|
=
\frac{r^4}{\nu}
\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|.
}
\]

Then

\[
\boxed{
\frac{|\gamma_{<r}(x_*)|}{W}
\lesssim
Q_{\perp,2}.
}
\]

This is strictly more selective than

\[
\frac{|S_{<r}|}{W}
\lesssim
K_{\omega,2},
\]

because any second derivative parallel to the maximum-vorticity direction is projected out.

---

## 4. Meaning at the exact magnitude maximum

Write locally

\[
\omega=\rho\xi.
\]

At a magnitude maximum `x_*`,

\[
\nabla\rho(x_*)=0,
\]

so

\[
\partial_{ab}\omega(x_*)
=
\xi_*\partial_{ab}\rho(x_*)
+W\partial_{ab}\xi(x_*).
\]

Crossing with `xi_*` eliminates the entire magnitude-Hessian term:

\[
\boxed{
\xi_*\times\partial_{ab}\omega(x_*)
=
W\,\xi_*\times\partial_{ab}\xi(x_*).
}
\]

Therefore the centered second-order survivor is a **direction-curvature / axis-conversion quantity**, not a vorticity-magnitude curvature quantity.

This aligns the first-hitting branch with the repository's projective-direction and axis-conversion tracks.

Status: **PROVED.**

---

## 5. Center curvature versus third derivative

The ball supremum can be separated by one mean-value step:

\[
\sup_{B_r(x_*)}
|\xi_*\times\nabla^2\omega|
\le
|\xi_*\times\nabla^2\omega(x_*)|
+
Cr\|\nabla^3\omega\|_{L^\infty(B_r(x_*))}.
\]

Define

\[
\boxed{
C_{\xi,2}(r,t;x_*)
:=
r^2
|\xi_*\times\nabla^2\xi(x_*)|
}
\]

and

\[
\boxed{
K_{\omega,3}(r,t;x_*)
:=
\frac{r^3}{W}
\|\nabla^3\omega\|_{L^\infty(B_r(x_*))}
=
\frac{r^5}{\nu}
\|\nabla^3\omega\|_{L^\infty(B_r(x_*))}.
}
\]

Then

\[
\boxed{
Q_{\perp,2}
\lesssim
C_{\xi,2}+K_{\omega,3}.
}
\]

Thus the transverse second-derivative branch itself splits into:

1. actual second curvature of the vorticity direction at the maximum;
2. a third-vorticity-derivative spatial needle.

Status: **PROVED.**

---

## 6. Far field remains the energy channel

As in the previous note,

\[
\frac{|\gamma_{>r}(x_*)|}{W}
\le
\frac{|S_{>r}(x_*)|}{W}
\lesssim
Z_r^{1/2},
\qquad
Z_r=\frac r{\nu^2}\|\omega\|_2^2.
\]

At a maximum point the magnitude equation gives, after dropping favorable diffusion terms,

\[
\boxed{
\frac{(D^+W)_+}{W^2}
\lesssim
Q_{\perp,2}+Z_r^{1/2}.
}
\]

Equivalently,

\[
\boxed{
\frac{(D^+W)_+}{W^2}
\lesssim
C_{\xi,2}+K_{\omega,3}+Z_r^{1/2}.
}
\]

Status: **PROVED.**

---

## 7. First-hitting consequence

For the running maximum, levels `W_j=q^jW_0`, first-hitting intervals `I_j`, contact set `C_j`, and

\[
\Theta_j=W_{j-1}|I_j|,
\]

define

\[
\mathfrak Q_{2,j}
:=
W_{j-1}\int_{C_j}Q_{\perp,2}(t)dt.
\]

Retain

\[
\mathfrak Z_j
=\frac1{\nu r_{j-1}}
\int_{I_j}\|\omega(t)\|_2^2dt.
\]

Then

\[
\boxed{
1-q^{-1}
\lesssim
\mathfrak Q_{2,j}
+
\sqrt{\Theta_j\mathfrak Z_j}.
}
\]

Therefore a first-hitting epoch must pay through either:

1. transverse direction-curvature / third-derivative occupancy near maximum-vorticity points;
2. the natural-window enstrophy tax.

If `mathfrak Q_{2,j}` is below a fixed small threshold, then

\[
\boxed{
\mathfrak Z_j\gtrsim_q\Theta_j^{-1}.
}
\]

The global energy summability from the previous notes then applies unchanged.

---

## 8. Updated survivor

The local first-hitting derivative tree is now

\[
\boxed{
\text{vorticity growth}
\Longrightarrow
\text{transverse second direction curvature}
\lor
\text{third-derivative needle}
\lor
\text{far enstrophy tax}.
}
\]

Arbitrary second derivative of the **magnitude** is no longer an active local-stretching survivor.

---

## 9. Next frontier

The most structured remaining object is

\[
C_{\xi,2}=r^2|\xi\times\nabla^2\xi|.
\]

A useful next calculation is to compare sustained `C_{xi,2}` with:

1. the negative direction-diffusion term `nu|nabla xi|^2`;
2. local projective-axis dispersion and axis-conversion quantities already in `CURRENT_ROUTE.md`;
3. a persistence-radius argument showing that large second direction curvature with small first direction gradient must either create nearby direction-gradient energy or force `nabla^3 omega` still higher.

No such contradiction is asserted yet.

---

## 10. Audit verdict

- direction-contracted strain depends on transverse vorticity relative to `xi_*`: **PROVED / STANDARD**;
- constant transverse jet vanishes: **PROVED**;
- linear transverse jet cancels on a centered ball by parity: **PROVED**;
- local vortex stretching begins at transverse second-vorticity-derivative order: **PROVED**;
- magnitude Hessian at the exact maximum contributes to the centered transverse term: **FALSE / PROJECTED OUT**;
- survivor reduces to direction curvature or third derivative: **PROVED**;
- these survivors contradict finite energy by themselves: **NOT DERIVED**;
- global regularity: **UNPROVED**.
