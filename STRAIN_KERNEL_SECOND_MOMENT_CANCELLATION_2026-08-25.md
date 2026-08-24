# Strain-kernel second-moment cancellation

Date: 2026-08-25

Status: **ACTIVE CALCULATION — GLOBAL REGULARITY NOT PROVED**

This note sharpens `MAX_VORTICITY_DIRECTION_DIFFUSION_CANCELLATION_2026-08-25.md`.

The previous note removed the first-vorticity-derivative branch by pairing it with direction diffusion at a maximum-vorticity point.  The strain kernel has an even stronger purely kinematic cancellation: on a centered ball, both the constant and linear Taylor jets of vorticity vanish in the strain singular integral.  Therefore the near strain begins at second derivative order.

---

## 1. Strain singular-integral structure

For a smooth divergence-free velocity field on `R^3`, with `omega=curl u`, the symmetric strain

\[
S=\frac12(\nabla u+\nabla u^T)
\]

has a principal-value representation

\[
\boxed{
S_{ij}(x)
=\operatorname{p.v.}\int_{\mathbb R^3}
K_{ijm}(z)\,\omega_m(x-z)\,dz,
}
\]

where the kernel is homogeneous of degree `-3`, has zero spherical average, and is even:

\[
K(-z)=K(z).
\]

The possible local delta contribution in `nabla u` is antisymmetric and cancels after taking the symmetric strain part.  Thus no zeroth-order local multiple of `omega(x)` remains in `S`.

Status: **STANDARD / PROVED KINEMATIC REPRESENTATION.**

---

## 2. Constant and linear Taylor jets both cancel

Fix `x` and a centered ball `|z|<r`.  Taylor expand

\[
\omega(x-z)
=
\omega(x)-\nabla\omega(x)z+\mathcal R_2(x,z),
\]

with

\[
|\mathcal R_2(x,z)|
\le
C|z|^2
\|\nabla^2\omega\|_{L^\infty(B_r(x))}.
\]

For the constant term, the zero spherical average of `K` gives

\[
\operatorname{p.v.}\int_{|z|<r}K(z)\,\omega(x)\,dz=0.
\]

For the linear term, `K` is even while `z` is odd, hence on the symmetric ball

\[
\int_{|z|<r}K(z)\,[\nabla\omega(x)z]\,dz=0.
\]

Therefore

\[
S_{<r}(x)
=
\operatorname{p.v.}\int_{|z|<r}K(z)\mathcal R_2(x,z)dz.
\]

Using `|K(z)| lesssim |z|^{-3}`,

\[
|S_{<r}(x)|
\lesssim
\|\nabla^2\omega\|_{L^\infty(B_r(x))}
\int_0^r \rho^{-3}\rho^2\rho^2d\rho.
\]

Hence

\[
\boxed{
|S_{<r}(x)|
\lesssim
r^2\|\nabla^2\omega\|_{L^\infty(B_r(x))}.
}
\]

Status: **PROVED.**

This is strictly sharper than the first-order Lipschitz estimate

\[
|S_{<r}|\lesssim r\|\nabla\omega\|_\infty.
\]

---

## 3. Natural-scale normalization

At a maximum-vorticity time define

\[
W(t)=\|\omega(t)\|_\infty,
\qquad
r(t)=\left(\frac\nu{W(t)}\right)^{1/2}.
\]

Define

\[
\boxed{
K_{\omega,2}(r,t;x)
:=
\frac{r^2}{W}
\|\nabla^2\omega\|_{L^\infty(B_r(x))}
=
\frac{r^4}{\nu}
\|\nabla^2\omega\|_{L^\infty(B_r(x))}.
}
\]

Then

\[
\boxed{
\frac{|S_{<r}(x)|}{W}
\lesssim
K_{\omega,2}(r,t;x).
}
\]

No independent normalized `nabla omega` term remains.

---

## 4. Far strain and enstrophy

The far field is unchanged:

\[
|S_{>r}(x)|
\lesssim
r^{-3/2}\|\omega\|_2.
\]

Define

\[
Z_r(t)=\frac r{\nu^2}\|\omega(t)\|_2^2.
\]

Since `W=nu/r^2`,

\[
\boxed{
\frac{|S_{>r}(x)|}{W}
\lesssim
Z_r^{1/2}.
}
\]

Thus at a maximum-vorticity point,

\[
\boxed{
\frac{(D^+W)_+}{W^2}
\lesssim
K_{\omega,2}+Z_r^{1/2}.
}
\]

The negative direction-diffusion term may only improve this inequality; it is no longer needed to eliminate the first derivative.

Status: **PROVED.**

---

## 5. Sharpened first-hitting gate

Use the running maximum `overline W`, levels `W_j=q^jW_0`, first-hitting intervals `I_j`, and

\[
\Theta_j=W_{j-1}|I_j|
=\frac{\nu|I_j|}{r_{j-1}^2}.
\]

Let `C_j` denote the contact set where the running maximum rises.  Define

\[
\mathfrak K_{2,j}
:=
W_{j-1}
\int_{C_j}
K_{\omega,2}(r(t),t;x_t)dt,
\]

and

\[
\mathfrak Z_j
:=
\frac1{\nu r_{j-1}}
\int_{I_j}\|\omega(t)\|_2^2dt.
\]

The first-hitting identity and Cauchy-Schwarz give the sharper estimate

\[
\boxed{
1-q^{-1}
\lesssim
\mathfrak K_{2,j}
+
\sqrt{\Theta_j\mathfrak Z_j}.
}
\]

Unlike the previous direction-diffusion estimate, there is no additive `Theta_j` near-field constant.

Therefore, for a fixed sufficiently small `kappa_q>0`,

\[
\boxed{
\mathfrak K_{2,j}\le\kappa_q
\Longrightarrow
\mathfrak Z_j\gtrsim_q\Theta_j^{-1}.
}
\]

This implication holds for every finite `Theta_j`, not only for a preselected compressed regime.

Status: **PROVED.**

---

## 6. Global energy summability on the second-derivative-quiet branch

The energy identity gives

\[
\sum_jr_{j-1}\mathfrak Z_j
\le
L_E,
\qquad
L_E=\frac{E_0}{\nu^2}.
\]

Thus on

\[
Q_2=\{j:\mathfrak K_{2,j}\le\kappa_q\},
\]

we obtain

\[
\boxed{
\sum_{j\in Q_2}
\frac{r_{j-1}/L_E}{\Theta_j}
<\infty.
}
\]

Consequently an infinite second-derivative-quiet subsequence cannot satisfy

\[
\Theta_j
\le
C\frac{r_{j-1}}{L_E}
\]

with one fixed `C`.

Equivalently, hitting intervals obeying

\[
|I_j|
\lesssim
\frac{r_{j-1}^3}{\nu L_E}
\]

infinitely often must enter the second-vorticity-derivative branch infinitely often.

---

## 7. What this prunes

The earlier local first-hitting tree contained

\[
\text{near }\nabla\omega
\lor
\text{far enstrophy}.
\]

The even-kernel Taylor cancellation removes the first derivative entirely and replaces it by

\[
\boxed{
\text{near }\nabla^2\omega
\lor
\text{far enstrophy}.
}
\]

Thus the active derivative survivor has been pushed up by one full spatial derivative without assuming direction coherence or boundedness of an auxiliary critical norm.

---

## 8. Next frontier

The remaining hard quantity is

\[
\mathfrak K_{2,j}
=
W_{j-1}\int_{C_j}
\frac{r(t)^4}{\nu}
\|\nabla^2\omega(t)\|_{L^\infty(B_{r(t)}(x_t))}
\,dt.
\]

The next calculation should test whether sustained `mathfrak K_{2,j}` can be converted into:

1. a spatially occupied critical `L^2` cost for `nabla^2 omega`;
2. a still higher derivative via a persistence-radius / Landau inequality;
3. or, preferably, a lower-order vorticity/enstrophy cost by exploiting the fact that `nabla^2 omega` is being sampled specifically near repeated **maximum-vorticity points**.

---

## 9. Audit verdict

- strain kernel is degree `-3`, even, zero-mean: **STANDARD / PROVED**;
- constant vorticity jet cancels in centered near strain: **PROVED**;
- linear vorticity jet cancels by parity: **PROVED**;
- `|S_<r| lesssim r^2 ||nabla^2 omega||_infty`: **PROVED**;
- first-vorticity-derivative survivor is necessary: **FALSE / PRUNED**;
- first-hitting gate reduces to second derivative or enstrophy tax: **PROVED**;
- global energy excludes all second-derivative-active epochs: **NOT DERIVED**;
- global regularity: **UNPROVED**.
