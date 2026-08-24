# Maximum-vorticity direction-diffusion cancellation

Date: 2026-08-25

Status: **ACTIVE CALCULATION — GLOBAL REGULARITY NOT PROVED**

This note refines `VORTICITY_FIRST_HITTING_STRAIN_ENERGY_TAX_2026-08-25.md`.  The previous near-field branch was expressed through `||nabla omega||_infty`.  At a maximum-vorticity point, part of that branch is not an independent escape: it is paired with the negative direction-diffusion term in the exact vorticity-magnitude equation.

---

## 1. Maximum-point geometry

Write

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|,
\qquad
|\xi|=1.
\]

At a spatial point `x_*` with

\[
\rho(x_*,t)=W(t):=\|\omega(t)\|_\infty>0,
\]

smoothness gives

\[
\nabla\rho(x_*,t)=0.
\]

Since

\[
\nabla\omega
=\xi\otimes\nabla\rho+\rho\nabla\xi,
\]

we have the exact maximum-point identity

\[
\boxed{
\nabla\omega(x_*,t)
=W(t)\nabla\xi(x_*,t).
}
\]

Thus the first spatial derivative of vorticity at the magnitude maximum is purely a direction-change derivative.

Status: **PROVED.**

---

## 2. Local strain with one more Taylor step

At the natural radius

\[
r=\left(\frac\nu W\right)^{1/2},
\]

write the strain singular integral as

\[
S=S_{<r}+S_{>r}.
\]

Kernel cancellation gives

\[
|S_{<r}(x_*)|
\lesssim
r\sup_{B_r(x_*)}|\nabla\omega|.
\]

For `y in B_r(x_*)`, the mean-value estimate gives

\[
|\nabla\omega(y)|
\le
|\nabla\omega(x_*)|
+r\|\nabla^2\omega\|_{L^\infty(B_r(x_*))}.
\]

Hence

\[
|S_{<r}(x_*)|
\lesssim
rW|\nabla\xi(x_*)|
+r^2\|\nabla^2\omega\|_{L^\infty(B_r(x_*))}.
\]

Define

\[
a:=r|\nabla\xi(x_*)|
\]

and the normalized second-vorticity-derivative amplitude

\[
\boxed{
K_{\omega,2}(r,t;x_*)
:=
\frac{r^2}{W}
\|\nabla^2\omega\|_{L^\infty(B_r(x_*))}
=
\frac{r^4}{\nu}
\|\nabla^2\omega\|_{L^\infty(B_r(x_*))}.
}
\]

Then

\[
\boxed{
\frac{|S_{<r}(x_*)|}{W}
\lesssim
a+K_{\omega,2}.
}
\]

Status: **PROVED.**

---

## 3. Direction diffusion cancels arbitrarily large first-derivative growth

The exact vorticity-magnitude equation is

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
\rho\left(\gamma-\nu|\nabla\xi|^2\right),
\qquad
\gamma=\xi^TS\xi.
\]

At the maximum point, divide the local strain/direction contribution by `W`.

Because

\[
\frac{\nu|\nabla\xi|^2}{W}
=r^2|\nabla\xi|^2
=a^2,
\]

we have

\[
\frac{\gamma_{<r}-\nu|\nabla\xi|^2}{W}
\lesssim
Ca+CK_{\omega,2}-a^2.
\]

The elementary quadratic bound

\[
Ca-a^2\le \frac{C^2}{4}
\]

therefore yields

\[
\boxed{
\frac{\gamma_{<r}-\nu|\nabla\xi|^2}{W}
\lesssim
1+K_{\omega,2}.
}
\]

This is the key cancellation: arbitrarily large `|nabla omega(x_*)|/W=|nabla xi(x_*)|` cannot by itself produce arbitrarily large normalized maximum-vorticity growth, because the same direction variation incurs a quadratic viscous penalty.

Status: **PROVED.**

---

## 4. Far strain remains an enstrophy channel

As before,

\[
|S_{>r}(x_*)|
\lesssim
r^{-3/2}\|\omega\|_2.
\]

With

\[
Z_r(t)=\frac r{\nu^2}\|\omega(t)\|_2^2,
\]

we have

\[
\boxed{
\frac{|S_{>r}(x_*)|}{W}
\lesssim
Z_r^{1/2}.
}
\]

Combining local and far pieces at a maximum point gives

\[
\boxed{
\frac{(D^+W)_+}{W^2}
\lesssim
1+K_{\omega,2}+Z_r^{1/2}.
}
\]

The positive part is written only to emphasize the first-hitting application; the upper-Dini estimate itself follows from the maximum principle.

Status: **PROVED.**

---

## 5. Refined first-hitting gate

Use the running maximum `overline W`, levels `W_j=q^jW_0`, first-hitting intervals `I_j`, and

\[
\Theta_j=W_{j-1}|I_j|
=\frac{\nu|I_j|}{r_{j-1}^2}.
\]

On the contact set `C_j={overline W=W, overline W'>0}`, the dynamic natural radius is comparable with `r_{j-1}`.

Define

\[
\boxed{
\mathfrak K_{2,j}
:=
W_{j-1}
\int_{C_j}K_{\omega,2}(r(t),t;x_t)dt,
}
\]

where `x_t` is a maximizing point (or a standard maximizing sequence in the Dini formulation), and retain

\[
\mathfrak Z_j
:=
\frac1{\nu r_{j-1}}
\int_{I_j}\|\omega(t)\|_2^2dt.
\]

Integrating the previous maximum-growth estimate and using Cauchy-Schwarz on the far term gives

\[
\boxed{
1-q^{-1}
\lesssim
\Theta_j
+
\mathfrak K_{2,j}
+
\sqrt{\Theta_j\mathfrak Z_j}.
}
\]

This strictly refines the previous first-derivative gate.

For sufficiently small fixed thresholds `theta_q,kappa_q>0`,

\[
\boxed{
\Theta_j\le\theta_q,
\quad
\mathfrak K_{2,j}\le\kappa_q
\Longrightarrow
\mathfrak Z_j\gtrsim_q\Theta_j^{-1}.
}
\]

Thus a compressed first-hitting epoch that is quiet in **second vorticity derivative occupancy** must pay the inverse-duration enstrophy tax.

Status: **PROVED.**

---

## 6. Global energy consequence

From the energy identity,

\[
\sum_jr_{j-1}\mathfrak Z_j
\le
L_E,
\qquad
L_E:=\frac{E_0}{\nu^2}.
\]

Therefore on the set

\[
Q_2:=\{j:\Theta_j\le\theta_q,\ \mathfrak K_{2,j}\le\kappa_q\},
\]

we obtain

\[
\boxed{
\sum_{j\in Q_2}
\frac{r_{j-1}/L_E}{\Theta_j}
<\infty.
}
\]

In particular, infinitely many epochs satisfying

\[
\Theta_j\lesssim\frac{r_{j-1}}{L_E}
\]

cannot all remain second-derivative quiet.

Equivalently,

\[
\boxed{
|I_j|\lesssim\frac{r_{j-1}^3}{\nu L_E}
\text{ infinitely often}
\Longrightarrow
\mathfrak K_{2,j}\ge\kappa_q
\text{ infinitely often},
}
\]

unless the corresponding energy-tax sum already contradicts the energy inequality.

Status: **PROVED RATE-CLASS REDUCTION.**

---

## 7. Interpretation

The compressed-vorticity first-hitting branch is now reduced from

\[
\nabla\omega\text{ concentration}
\lor
\text{enstrophy tax}
\]

to the sharper

\[
\boxed{
\nabla^2\omega\text{ space-time occupancy}
\lor
\text{enstrophy tax}
\lor
\text{non-compressed epoch}.
}
\]

The first vorticity derivative is not a free survivor at the magnitude maximum: its direction-changing component is automatically paired with viscous direction damping.

---

## 8. What remains open

The remaining difficult branch is the time-integrated normalized second derivative

\[
\mathfrak K_{2,j}.
\]

Large instantaneous `nabla^2 omega` can still concentrate into increasingly thin space-time needles.  The next step is to combine:

1. the existing derivative persistence-radius lemma;
2. the time-integrated occupancy `mathfrak K_{2,j}`;
3. a Taylor/Landau derivative log-convexity estimate;
4. any available projection back to first-order energy or local-enstrophy cost.

No contradiction with an infinite higher-derivative chain has yet been proved.

---

## 9. Audit verdict

- `nabla omega = W nabla xi` at a maximum-vorticity point: **PROVED**;
- near strain `lesssim r W |nabla xi| + r^2 ||nabla^2 omega||_infty`: **PROVED**;
- first-derivative direction strain minus viscous direction diffusion is uniformly bounded after normalization: **PROVED**;
- compressed first-hitting reduces to second-vorticity-derivative occupancy or enstrophy tax: **PROVED**;
- ultra-compressed second-derivative-quiet epochs excluded by global energy: **PROVED RATE-CLASS EXCLUSION**;
- second-derivative occupancy itself contradicted: **NOT DERIVED**;
- global regularity: **UNPROVED**.
