# DSD M5-683 — Push the CE-H kappa constitutive law to enstrophy-weighted kappa space

Date: 2026-09-03

Status: **INTERNAL KAPPA-SPACE CONSTITUTIVE IDENTITY / ON A SMOOTH HIGH-AMPLITUDE CUTOFF, PUSHING THE M5-682 LAW `h=L_rho kappa + L_rho sigma - kappa + R_geom` THROUGH THE ENSTROPHY WEIGHT `chi(rho) rho^2 dy` GIVES `G_E^chi = partial_k(A_kk + A_ks) - k F_E^chi + R_chi`; THE PURE KAPPA PART `A_kk=int delta(k-kappa) chi rho^2 |grad kappa|^2` IS NONNEGATIVE AND IS A GENUINE KAPPA-SPACE DIFFUSION DENSITY, BUT THE MIXED STRAIN TERM `A_ks=int delta chi rho^2 grad kappa·grad sigma` HAS NO SIGN AND CAN CANCEL OR REVERSE THE DIFFUSIVE CURRENT / CUTOFF-TRANSITION AND EXPLICIT GEOMETRIC TERMS FORM A CONTROLLED REMAINDER / THUS THE PDE CONSTITUTIVE LAW IS STRONGER THAN THE ABSTRACT OSCILLATOR BUT DOES NOT YET GIVE A ONE-SIGN FOKKER-PLANCK CLOSURE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why use a high-amplitude cutoff

The scalar multiplier `kappa` is canonically defined on `rho=|W|>0` by

\[
\Delta W=\kappa W.
\]

At a vorticity zero, the division formula for `kappa` need not be regular even though the original vector equation remains smooth.

Choose a fixed smooth cutoff

\[
\chi=\chi(\rho)
\]

with

\[
0\le\chi\le1,
\]

\[
\chi(\rho)=0
\quad(\rho\le a_0/2),
\]

and

\[
\chi(\rho)=1
\quad(\rho\ge a_0).
\]

All scalar kappa-space quantities below are therefore supported where `rho` has a fixed positive lower bound.

---

## 2. Enstrophy-weighted kappa distribution and current

Define

\[
\boxed{
F_E^\chi(k,\theta)
:=
\int_{\mathbb R^3}
\delta(k-\kappa(y,\theta))
\chi(\rho)\rho^2dy.
}
\]

Define the corresponding material-kappa current

\[
\boxed{
G_E^\chi(k,\theta)
:=
\int
h(y,\theta)
\delta(k-\kappa(y,\theta))
\chi(\rho)\rho^2dy,
}
\]

where

\[
h=D_B\kappa.
\]

These are spatial/enstrophy-weighted objects.
They are **not** the same measure as the pure transverse material-flux distribution `F,G` of M5-681; that distinction is audited below.

---

## 3. Insert the M5-682 constitutive law

M5-682 gives

\[
\boxed{
h=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom},}
\]

with

\[
L_\rho f
=\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

Hence

\[
G_E^\chi
=I_\kappa+I_\sigma-kF_E^\chi+R_{geom}^\chi,
\]

where

\[
I_\kappa
:=
\int
\delta(k-\kappa)\chi
\nabla\cdot(\rho^2\nabla\kappa)dy,
\]

\[
I_\sigma
:=
\int
\delta(k-\kappa)\chi
\nabla\cdot(\rho^2\nabla\sigma)dy,
\]

and

\[
R_{geom}^\chi
:=
\int
\delta(k-\kappa)\chi\rho^2\mathcal R_{geom}dy.
\]

---

## 4. Pure kappa principal term

Integrate by parts in space.
Because

\[
\nabla_y\delta(k-\kappa)
=-\partial_k\delta(k-\kappa)\nabla\kappa,
\]

we obtain

\[
\begin{aligned}
I_\kappa
={}&
\partial_k
\int
\delta(k-\kappa)
\chi\rho^2|\nabla\kappa|^2dy\\
&-
\int
\delta(k-\kappa)
\chi'(\rho)\rho^2
\nabla\rho\cdot\nabla\kappa\,dy.
\end{aligned}
\]

Define

\[
\boxed{
A_{\kappa\kappa}(k)
:=
\int
\delta(k-\kappa)
\chi\rho^2|\nabla\kappa|^2dy
\ge0.
}
\]

Thus

\[
\boxed{
I_\kappa
=\partial_kA_{\kappa\kappa}
-B_{\kappa}^{\chi}.
}
\]

The first term is a genuine nonnegative kappa-space diffusion density.

---

## 5. Strain-gradient principal term

The same calculation gives

\[
\begin{aligned}
I_\sigma
={}&
\partial_k
\int
\delta(k-\kappa)
\chi\rho^2
\nabla\kappa\cdot\nabla\sigma\,dy\\
&-
\int
\delta(k-\kappa)
\chi'(\rho)\rho^2
\nabla\rho\cdot\nabla\sigma\,dy.
\end{aligned}
\]

Define

\[
\boxed{
A_{\kappa\sigma}(k)
:=
\int
\delta(k-\kappa)
\chi\rho^2
\nabla\kappa\cdot\nabla\sigma\,dy.
}
\]

This quantity has no fixed sign.

Therefore

\[
\boxed{
I_\sigma
=\partial_kA_{\kappa\sigma}
-B_{\sigma}^{\chi}.
}
\]

---

## 6. Exact constitutive current

Collect the cutoff-transition terms and the explicit geometry into

\[
\boxed{
\mathcal R_\chi(k)
:=
R_{geom}^\chi(k)
-
\int
\delta(k-\kappa)
\chi'(\rho)\rho^2
\nabla\rho\cdot\nabla(\kappa+\sigma)dy.
}
\]

Then

\[
\boxed{
G_E^\chi(k)
=
\partial_k
\left[
A_{\kappa\kappa}(k)
+A_{\kappa\sigma}(k)
\right]
-kF_E^\chi(k)
+\mathcal R_\chi(k).
}
\]

This is the desired enstrophy-weighted kappa-space constitutive identity.

---

## 7. Diffusion is real but not autonomous

The first principal coefficient satisfies

\[
A_{\kappa\kappa}\ge0.
\]

If it were the only derivative-current term, the kappa distribution would have a genuine one-dimensional diffusion structure.

But the actual principal derivative current is

\[
A_{\kappa\kappa}+A_{\kappa\sigma}
=
\int
\delta(k-\kappa)
\chi\rho^2
\nabla\kappa\cdot\nabla(\kappa+\sigma)dy.
\]

Equivalently,

\[
\nabla\kappa\cdot\nabla(\kappa+\sigma)
=
\frac12
\left(
|\nabla\kappa|^2
+|\nabla(\kappa+\sigma)|^2
-|\nabla\sigma|^2
\right).
\]

Therefore no sign follows without additional control on the strain-eigenvalue gradient.

This is the first exact PDE obstruction to the naive statement

\[
\text{`Delta kappa produces diffusion, so the multi-sheet oscillator cannot recur.'}
\]

---

## 8. Explicit remainder

Recall

\[
\mathcal R_{geom}
=
-
\frac2\rho\Sigma:\nabla^2\rho
+
2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+
(\nabla\times W)\cdot\nabla\log\rho.
\]

Thus `R_chi` contains only fixed-order CE-H fields on the retained high-amplitude set.
The compact all-order hull gives uniform bounds for every term.

Uniform boundedness, however, is not a sign condition and does not prevent a stationary current through `kappa=0`.

---

## 9. Measure mismatch with M5-681

M5-681 uses the transverse material-flux measure

\[
d\mu_\Phi=d\Phi
\]

on material vortex-line labels.

The present identity uses

\[
\rho^2dy.
\]

In a local vortex flow box with arclength `ds`,

\[
dy=\frac{d\Phi\,ds}{\rho},
\]

so

\[
\boxed{
\rho^2dy
=\rho\,d\Phi\,ds.
}
\]

Because `kappa` and `h` are constant along each vortex line at a fixed time (`W·grad kappa=W·grad h=0`), the present distribution is the M5-681 leaf distribution weighted by the line factor

\[
\boxed{
L_\rho(\lambda)
:=
\int \rho\,ds.
}
\]

Hence the strict flux current

\[
\overline G_\Phi(0)<0
\]

of M5-681 does **not** automatically imply the same sign for `G_E^chi(0)` unless the line weight is controlled in the relevant population.

This measure mismatch is a mandatory firewall.

---

## 10. Updated target

The PDE constitutive law exposes two precise remaining issues:

1. control/couple the line weight `L_rho` so the directed flux-label current of M5-681 can be compared to the spatial current above;
2. determine whether the mixed strain-gradient current `A_{kappa sigma}` and `R_chi` can sustain the required negative current through `kappa=0` indefinitely.

A valid final closure must solve at least one of these rather than treating `A_kk>=0` alone as a contradiction.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
