# Cauchy-vorticity material turnover: deformation versus viscous defect

Date: 2026-08-13

Status: **EXACT LAGRANGIAN CAUCHY-DEFECT IDENTITY + TURNOVER VOLUME BOUND / OPEN HIGH-DERIVATIVE SUMMABILITY**.

The threshold-crossing formulation decomposed material turnover into strain production and diffusion.  A cleaner Lagrangian variable absorbs the strain exactly and shows that genuine change of a material label's vorticity state is purely viscous.

---

## 1. Restarted incompressible flow map

Restart at `t_0`:

\[
X(a,t_0)=a,
\qquad
\partial_tX(a,t)=u(X(a,t),t).
\]

Let

\[
F(a,t)=D_aX(a,t).
\]

For incompressible flow,

\[
\det F=1,
\]

and

\[
\boxed{
\partial_tF=(\nabla u)(X,t)F.
}
\]

Hence

\[
\boxed{
\partial_tF^{-1}
=-F^{-1}(\nabla u)(X,t).
}
\]

---

## 2. Cauchy-vorticity variable

The vorticity equation can be written

\[
D_t\omega
=(\nabla u)\omega+\nu\Delta\omega.
\]

Define the material/reference vorticity

\[
\boxed{
\zeta(a,t)
=F(a,t)^{-1}\omega(X(a,t),t).
}
\]

Differentiate:

\[
\begin{aligned}
\partial_t\zeta
&=(\partial_tF^{-1})\omega
+F^{-1}D_t\omega\\
&=-F^{-1}(\nabla u)\omega
+F^{-1}\bigl[(\nabla u)\omega+\nu\Delta\omega\bigr].
\end{aligned}
\]

The stretching terms cancel exactly, giving

\[
\boxed{
\partial_t\zeta(a,t)
=\nu F(a,t)^{-1}
\Delta\omega(X(a,t),t).
}
\]

For Euler (`nu=0`), `zeta` is exactly constant along each material label: this is the Cauchy vorticity invariant.

For Navier--Stokes, viscosity is the only source of Cauchy-invariant defect.

---

## 3. Duhamel form

Because the restarted map has `F(t_0)=I`,

\[
\zeta(a,t_0)=\omega(a,t_0).
\]

Therefore

\[
\boxed{
\zeta(a,t)-\omega(a,t_0)
=\nu
\int_{t_0}^{t}
F(a,s)^{-1}
\Delta\omega(X(a,s),s)ds.
}
\]

This is an exact separation:

- `F`: inviscid material deformation/stretching/rotation;
- `zeta-zeta_0`: viscous alteration of the material vorticity state.

---

## 4. `L^2` viscous-defect bound

Let `A_0` be a material label region and

\[
A(s)=X(A_0,s).
\]

Define

\[
K_-(I)
=\sup_{a\in A_0,\ s\in I}
\|F(a,s)^{-1}\|_{\rm op}.
\]

For `I=[t_0,t_1]` of duration `tau`, Minkowski and Cauchy--Schwarz give

\[
\begin{aligned}
\|\zeta(t_1)-\zeta(t_0)\|_{L^2(A_0)}
&\le
\nu
\int_I
K_-(I)
\|\Delta\omega(s)\|_{L^2(A(s))}ds\\
&\le
\nu K_-(I)\sqrt\tau
\left(
\int_I\int_{A(s)}|\Delta\omega|^2dxds
\right)^{1/2}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\zeta(t_1)-\zeta(t_0)\|_{L^2(A_0)}^2
\le
\nu^2K_-^2\tau
\int_I\int_{A(s)}|\Delta\omega|^2dxds.
}
\]

The volume element needs no Jacobian correction because `det F=1`.

---

## 5. Low-to-high material recruitment bound

Assume also

\[
K_+(I)
=\sup_{a,s}\|F(a,s)\|_{\rm op}
\le K.
\]

Suppose a set of material labels `R subset A_0` is initially below an oriented/intense magnitude threshold

\[
|\omega(a,t_0)|\le h_-
\qquad(a\in R)
\]

but at `t_1` becomes physically intense:

\[
|\omega(X(a,t_1),t_1)|\ge h_+.
\]

Since

\[
\omega(X,t_1)=F(a,t_1)\zeta(a,t_1),
\]

we have

\[
|\zeta(a,t_1)|
\ge
\frac{h_+}{K}.
\]

Hence, provided

\[
\delta_h
:=\frac{h_+}{K}-h_->0,
\]

every recruited label satisfies

\[
|\zeta(a,t_1)-\zeta(a,t_0)|
\ge\delta_h.
\]

Therefore

\[
\delta_h^2|R|
\le
\|\zeta(t_1)-\zeta(t_0)\|_{L^2(A_0)}^2.
\]

Combining with the viscous-defect bound,

\[
\boxed{
|R|
\le
\frac{\nu^2K_-^2\tau}{\delta_h^2}
\int_I\int_{A(s)}|\Delta\omega|^2dxds.
}
\]

If `K_+,K_-<=K`, this becomes

\[
\boxed{
|R|
\le
\frac{\nu^2K^2\tau}{(h_+/K-h_-)^2}
\int_I\int_{A(s)}|\Delta\omega|^2.
}
\]

Thus order-one material recruitment cannot occur under bounded recent deformation without paying a second-vorticity-derivative cost.

---

## 6. Natural-window scaling

Take

\[
W_0=W(t_0),
\qquad
r=aW_0^{-1/2},
\qquad
\tau=\lambda W_0^{-1}.
\]

Choose relative thresholds

\[
h_-=b_-W_0,
\qquad
h_+=b_+W_0,
\]

and a deformation bound `K` satisfying

\[
\boxed{
\delta_b
:=b_+/K-b_->0.
}
\]

Then

\[
\delta_h=\delta_bW_0.
\]

If the recruited volume is a fixed fraction `theta` of one natural volume,

\[
|R|
\ge\theta r^3
=\theta a^3W_0^{-3/2},
\]

the previous estimate forces

\[
\boxed{
\int_I\int_{A(s)}|\Delta\omega|^2dxds
\ge
\frac{
\theta a^3\delta_b^2
}{
\nu^2K^2\lambda
}
W_0^{3/2}.
}
\]

This is precisely the natural scale of the time-integrated `k=2` vorticity derivative energy.

Hence a natural-volume material replacement has the critical alternatives

\[
\boxed{
\text{large recent deformation}
\quad\text{or}\quad
\int_I\|\Delta\omega\|_2^2
\gtrsim W_0^{3/2}.
}
\]

---

## 7. Deformation charge

For material vectors,

\[
\frac d{dt}|Fv|^2
=2(Fv)^TS(Fv),
\]

so restarted forward and inverse deformation satisfy schematically

\[
K_+,K_-
\le
\exp\left(
\int_I\|S(t)\|_\infty dt
\right).
\]

Therefore failure of the bounded-deformation threshold needed above is itself charged to the strain/deformation branch.

The material-turnover escape is thus reduced to

\[
\boxed{
\text{strain-driven strong deformation}
\quad\text{or}\quad
\text{critical }k=2\text{ viscous Cauchy defect}.
}
\]

---

## 8. Relation to the threshold-crossing lemma

The previous Eulerian scalar formula was

\[
D_t(n\cdot\omega)
=n\cdot S\omega+\nu\Delta(n\cdot\omega).
\]

The Cauchy variable shows why the two terms appeared:

- the `S omega` term is the physical deformation of the same material vorticity;
- the `Delta omega` term is the actual alteration of the Cauchy material invariant.

Thus `zeta=F^{-1}omega` is the cleaner variable for separating **material identity** from **instantaneous geometric amplification**.

---

## 9. Residual-class update

The new-material branch no longer remains as an untyped escape.

A hypothetical singular cascade that repeatedly replaces a fixed fraction of one natural-volume core must, on every such replacement window, generate at least one of:

1. order-one scale-critical strain deformation;
2. order-`W^(3/2)` integrated second-vorticity-derivative energy.

The first is already in the Lagrangian/strain chain.  The second enters the derivative hierarchy two steps above base vorticity.

---

## 10. Principal open target

The remaining question is not whether turnover has a cost; it does.

The question is whether repeated critical `k=2` Cauchy-defect costs can be summably compatible with the factorial derivative-radius / projective-dissipation hierarchy already derived in the repository.

A proof-producing next step would connect the natural-window lower bound

\[
\int_I\|\Delta\omega\|_2^2
\gtrsim W^{3/2}
\]

for repeated turnover windows to one of:

- the factorial-normalized derivative radius;
- higher-derivative sparseness/analyticity;
- the energy-weighted projective dissipation `D_k`;
- or a blowup-rate incompatibility.

Status: **OPEN REPEATED CAUCHY-DEFECT / HIGH-DERIVATIVE CLOSURE**.
