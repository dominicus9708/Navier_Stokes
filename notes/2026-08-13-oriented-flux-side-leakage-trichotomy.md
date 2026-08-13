# Oriented-flux side-leakage trichotomy

Date: 2026-08-13

Status: **DERIVED CYLINDRICAL DIVERGENCE-FREE / COAREA LEMMA + OPEN PERSISTENCE-IN-TIME CLOSURE**.

This note continues the projective-axis polarity branch.  It treats a straight cylinder aligned with a locally selected **constant** axis `n`.  Curvature of a variable local axis is a separate typed error channel and is not hidden here.

No global-regularity claim is made.

---

## 1. Cylinder and axial flux

Write

\[
x=s n+y,
\qquad y\in n^\perp.
\]

For `rho>0`, define the cross-section

\[
D_\rho(s)=\{s n+y:|y|<\rho\}
\]

and the signed axial vorticity flux

\[
\boxed{
\Phi_\rho(s)
=\int_{D_\rho(s)}\omega\cdot n\,dA.
}
\]

Let

\[
\omega_\perp
=\omega-(\omega\cdot n)n.
\]

Because

\[
\nabla\cdot\omega=0,
\]

the divergence theorem on a cylinder of radius `rho` and axial interval `[s_1,s_2]` gives

\[
\boxed{
\Phi_\rho(s_2)-\Phi_\rho(s_1)
=-\int_{\Sigma_\rho(s_1,s_2)}
\omega_\perp\cdot\nu_\perp\,dS,
}
\]

where `Sigma_rho` is the lateral cylindrical surface.

Thus axial signed flux can change only through transverse side flux.

---

## 2. Radial coarea converts side flux into a volumetric off-axis channel

Fix a natural radial band

\[
r\le\rho\le2r
\]

and an axial length

\[
L=s_2-s_1>0.
\]

Let

\[
\mathcal A_{r,2r;L}
=\{s n+y:s_1<s<s_2,\ r<|y|<2r\}.
\]

By cylindrical coarea,

\[
\int_r^{2r}
\int_{\Sigma_\rho}
|\omega_\perp|^2dS\,d\rho
=
\int_{\mathcal A_{r,2r;L}}
|\omega_\perp|^2dx.
\]

Hence there exists

\[
\rho_*\in[r,2r]
\]

such that

\[
\int_{\Sigma_{\rho_*}}|\omega_\perp|^2dS
\le
\frac1r
\int_{\mathcal A_{r,2r;L}}|\omega_\perp|^2dx.
\]

The lateral area obeys

\[
|\Sigma_{\rho_*}|
=2\pi\rho_*L
\le4\pi rL.
\]

Cauchy--Schwarz therefore gives the explicit estimate

\[
\begin{aligned}
|\Phi_{\rho_*}(s_2)-\Phi_{\rho_*}(s_1)|^2
&\le
|\Sigma_{\rho_*}|
\int_{\Sigma_{\rho_*}}|\omega_\perp|^2dS\\
&\le
4\pi L
\int_{\mathcal A_{r,2r;L}}|\omega_\perp|^2dx.
\end{aligned}
\]

Thus

\[
\boxed{
\int_{\mathcal A_{r,2r;L}}|\omega_\perp|^2dx
\ge
\frac{
|\Phi_{\rho_*}(s_2)-\Phi_{\rho_*}(s_1)|^2
}{4\pi L}.
}
\]

This closes the basic side-flux target into the existing off-axis `L^2` projective channel.

---

## 3. Robust flux-loss lemma

The coarea-selected radius is not known in advance.  Therefore formulate the clean scale statement with a robust radial-band hypothesis.

Assume that for every

\[
\rho\in[r,2r]
\]

the flux has the same orientation and loses at least

\[
\Delta\Phi_0>0
\]

between `s_1` and `s_2`:

\[
|\Phi_\rho(s_2)-\Phi_\rho(s_1)|
\ge\Delta\Phi_0.
\]

Then in particular this holds at the coarea radius `rho_*`, so

\[
\boxed{
\int_{\mathcal A_{r,2r;L}}|\omega_\perp|^2dx
\ge
\frac{\Delta\Phi_0^2}{4\pi L}.
}
\]

Suppose more specifically

\[
\Delta\Phi_0
\ge
\eta\kappa W r^2,
\qquad
L=\lambda r,
\]

with fixed positive dimensionless `eta,kappa,lambda`.

Then

\[
\boxed{
r
\int_{\mathcal A_{r,2r;L}}|\omega_\perp|^2dx
\ge
\frac{\eta^2\kappa^2}{4\pi\lambda}
(Wr^2)^2.
}
\]

At the natural vorticity radius

\[
r\asymp W^{-1/2},
\]

the factor `W r^2` is order one.  Therefore order-one robust loss of an oriented natural-scale flux over `L=O(r)` forces an order-one scale-invariant off-axis enstrophy cost.

This returns the oriented branch to the local projective-defect gate.

---

## 4. Persistent-flux cost

The alternative is that a signed flux stays large.

Fix one radius

\[
\rho\in[r,2r]
\]

and suppose

\[
|\Phi_\rho(s)|\ge\Phi_0
\]

for every `s in [s_1,s_2]`.

On each cross-section, Cauchy--Schwarz gives

\[
\int_{D_\rho(s)}|\omega|^2dA
\ge
\int_{D_\rho(s)}|\omega\cdot n|^2dA
\ge
\frac{\Phi_\rho(s)^2}{\pi\rho^2}.
\]

Since `rho<=2r`, integrating in `s` yields

\[
\boxed{
\int_{C_{\rho,L}}|\omega|^2dx
\ge
\frac{L\Phi_0^2}{4\pi r^2}.
}
\]

If

\[
\Phi_0\ge\kappa W r^2,
\]

then

\[
\boxed{
r
\int_{C_{\rho,L}}|\omega|^2dx
\ge
\frac{\kappa^2}{4\pi}
(Wr^2)^2
\frac{L}{r}.
}
\]

At the natural radius `r asymp W^{-1/2}`,

\[
\boxed{
r
\int_{C_{\rho,L}}|\omega|^2dx
\gtrsim
c_\kappa\frac{L}{r}.
}
\]

Hence an oriented intense tube that persists for `N=L/r` natural lengths pays a scale-invariant enstrophy cost growing at least linearly in `N`.

This is not yet a contradiction because instantaneous global enstrophy need not be uniformly bounded near a hypothetical singular time.  It is, however, a precise occupancy cost.

---

## 5. Radial cancellation is the third branch

The robust-loss hypothesis can fail even if a strong inner-core flux is present.

Suppose at some axial location

\[
\Phi_r\ge\kappa W r^2>0,
\]

but for some

\[
\rho\in[r,2r]
\]

one has

\[
\Phi_\rho
\le
(1-\eta)\kappa W r^2.
\]

Then the annular axial flux satisfies

\[
\int_{D_\rho\setminus D_r}
\omega\cdot n\,dA
\le
-\eta\kappa W r^2.
\]

Writing

\[
\alpha_-=\max\{-\omega\cdot n,0\},
\]

we obtain

\[
\boxed{
\int_{D_\rho\setminus D_r}\alpha_-dA
\ge
\eta\kappa W r^2.
}
\]

Since the annular area is at most `3 pi r^2`, another Cauchy--Schwarz estimate gives

\[
\boxed{
\int_{D_\rho\setminus D_r}\alpha_-^2dA
\ge
\frac{\eta^2\kappa^2}{3\pi}
W^2r^2.
}
\]

Thus failure of robust outward orientation requires a quantitatively nontrivial opposite-polarity axial population in the radial annulus.

If this cancellation persists over an axial interval of length comparable to `r`, it becomes a three-dimensional mixed-polarity population and feeds the previous Poincare/palinstrophy lemma.

A cancellation occurring only on isolated cross-sections is not by itself a volumetric regularity certificate; that temporal/axial persistence issue remains typed separately.

---

## 6. Oriented-flux trichotomy

A projectively aligned, one-polarity intense core with natural-scale signed flux therefore has only three ways to continue:

### F1. Side leakage / termination

The robust flux decays over `L=O(r)`.

Then

\[
r\int|\omega_\perp|^2
\gtrsim1,
\]

so the flow leaves the nearly one-axis projective branch.

### F2. Axial persistence

The flux remains of order `W r^2` over `N` natural lengths.

Then

\[
r\int_{\rm tube}|\omega|^2
\gtrsim N.
\]

Long persistence is therefore paid for by large scale-invariant enstrophy occupancy.

### F3. Radial polarity cancellation

The positive inner flux is canceled before the coarea-selected lateral boundary is reached.

Then the radial annulus contains an opposite-polarity axial population; if persistent in axial measure, the previous mixed-polarity/palinstrophy branch reactivates.

Hence there is no fourth 'free termination' branch.

---

## 7. DSD channel interpretation

The three channels are typed as

\[
\boxed{
\mathsf F_{\rm orient}
=
(
\Phi_{\rm ax},
\mathcal L_\perp,
\mathcal O_{\rm tube},
\mathcal P_{\pm}
),
}
\]

where

- `Phi_ax`: signed axial vorticity flux;
- `L_perp`: side-leakage/off-axis `L^2` cost;
- `O_tube`: axial occupancy length in natural-radius units;
- `P_+-`: opposite-polarity cancellation channel.

This complements the projective covariance matrix because the covariance is sign-free while `Phi_ax` and `P_+-` retain orientation.

---

## 8. Relation to the current residual class

The oriented projective branch is now reduced to

\[
\boxed{
\text{off-axis leakage}
\quad\text{or}\quad
\text{long natural-scale occupancy}
\quad\text{or}\quad
\text{mixed polarity}.
}
\]

The first and third branches return to already active projective/palinstrophy gates.

The genuinely new residual subbranch is therefore **long oriented-flux persistence**.

A proof-producing next step would control the dimensionless persistence length

\[
\boxed{
\mathcal N_{\rm tube}=L/r
}
\]

through a quantity already known to be time-integrable or through the moving-window natural-time cost.

Until such a time-integrated persistence estimate is established, this route remains open.
