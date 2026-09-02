# DSD M5-585 — Ergodic Wedge Enstrophy ODE and Similarity-Balance Recovery

Date: 2026-09-02

Status: **THE q-AVERAGED WEDGE ENSTROPHY LAW EXACTLY REPRODUCES THE M5-486 SIMILARITY ENSTROPHY BALANCE AFTER THE NATURAL z^(1/2) INTEGRATION. NEW INFORMATION CAN ONLY COME FROM LOCALIZED z-INTERVAL FLUX STRUCTURE. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Wedge vorticity coefficient

Define

\[
\boxed{
\omega(x,s)
=\nabla\times u(x,s)
=r^{-2}G(z,q,\omega),
}
\]

where \(G\) is the scale-normalized physical-vorticity coefficient generated from \(F\) by the wedge curl operator.

The similarity vorticity is

\[
W(y,\theta)=(-s)\omega(x,s).
\]

Since

\[
(-s)/r^2=z,
\]

we have the exact relation

\[
\boxed{W=zG.}
\]

---

## 2. Wedge vorticity equation

The physical vorticity equation is

\[
\partial_s\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\Delta\omega.
\]

Because

\[
\partial_s\omega=-r^{-4}\partial_zG,
\]

all terms scale as \(r^{-4}\).

Using the homogeneity-two wedge Laplacian

\[
\mathfrak L_2
:=
(\mathfrak D-2)(\mathfrak D-1)+\Delta_{S^2},
\]

the equation can be written schematically but exactly as

\[
\boxed{
-\partial_zG
+\mathfrak A(F,G)
=
\mathfrak S(G,F)
+\mathfrak L_2G,
}
\]

where \(\mathfrak A\) is wedge advection and \(\mathfrak S\) is wedge vortex stretching.

---

## 3. Enstrophy density and flux

Set

\[
\boxed{
K(z,q,\omega)
:=\frac12|G|^2.
}
\]

The physical vorticity-enstrophy density is

\[
\frac12|\omega|^2=r^{-4}K.
\]

The incompressible local enstrophy identity is

\[
\partial_s\frac{|\omega|^2}{2}
+\nabla\cdot
\left[
 u\frac{|\omega|^2}{2}
-\nabla\frac{|\omega|^2}{2}
\right]
=
\omega\cdot\Sigma\omega
-|\nabla\omega|^2.
\]

Define the wedge enstrophy flux

\[
\boxed{
\mathcal J_\omega
:=
KF-\mathfrak G_4K,
}
\]

where

\[
\mathfrak G_4K
=
e_r(\mathfrak D-4)K+\nabla_{S^2}K.
\]

Then the physical flux is

\[
r^{-5}\mathcal J_\omega.
\]

---

## 4. Stretching and dissipation densities

Define the wedge strain coefficient by

\[
\nabla u=r^{-2}\mathbb G_F,
\qquad
\Sigma_u=r^{-2}\Sigma_F.
\]

Then

\[
\omega\cdot\Sigma_u\omega
=r^{-6}\mathcal Q_F,
\]

where

\[
\boxed{
\mathcal Q_F
:=G\cdot\Sigma_FG.
}
\]

Similarly,

\[
|\nabla\omega|^2
=r^{-6}\mathcal P_G,
\]

with

\[
\boxed{
\mathcal P_G
:=
|(\mathfrak D-2)G|^2
+|\nabla_{S^2}G|^2
\ge0.
}
\]

---

## 5. Exact wedge enstrophy equality

A vector flux of homogeneity \(r^{-5}\) has divergence

\[
\nabla\cdot(r^{-5}\mathcal J_\omega)
=r^{-6}
\left[
(\mathfrak D-3)(\mathcal J_\omega)_r
+\operatorname{div}_{S^2}(\mathcal J_\omega)_T
\right].
\]

Since

\[
\partial_s(r^{-4}K)
=-r^{-6}\partial_zK,
\]

the local enstrophy equation becomes

\[
-\partial_zK
+(\mathfrak D-3)(\mathcal J_\omega)_r
+\operatorname{div}_{S^2}(\mathcal J_\omega)_T
=
\mathcal Q_F-\mathcal P_G.
\]

Thus

\[
\boxed{
\partial_zK
=
(\mathfrak D-3)(\mathcal J_\omega)_r
+\operatorname{div}_{S^2}(\mathcal J_\omega)_T
-\mathcal Q_F
+\mathcal P_G.
}
\]

---

## 6. q-ergodic sphere average

Define

\[
\boxed{
\mathscr K_\omega(z)
:=
\left\langle
\int_{S^2}K\,d\omega
\right\rangle_q,
}
\]

\[
\boxed{
\mathscr J_\omega(z)
:=
\left\langle
\int_{S^2}(\mathcal J_\omega)_r\,d\omega
\right\rangle_q,
}
\]

\[
\boxed{
\mathscr Q_\omega(z)
:=
\left\langle
\int_{S^2}\mathcal Q_F\,d\omega
\right\rangle_q,
}
\]

and

\[
\boxed{
\mathscr P_\omega(z)
:=
\left\langle
\int_{S^2}\mathcal P_G\,d\omega
\right\rangle_q
\ge0.
}
\]

The \(q\)-derivative averages to zero and the angular divergence integrates to zero. Therefore

\[
\boxed{
\mathscr K_\omega'(z)
+2z\mathscr J_\omega'(z)
+3\mathscr J_\omega(z)
=
\mathscr P_\omega(z)-\mathscr Q_\omega(z).
}
\]

This is the exact q-averaged wedge enstrophy ODE.

---

## 7. Convert wedge depth to similarity volume measure

Since

\[
z=|y|^{-2},
\]

write

\[
\rho=|y|=z^{-1/2}.
\]

Then

\[
\rho^2|d\rho|
=\frac12z^{-5/2}dz.
\]

Because

\[
W=zG,
\]

the similarity enstrophy is

\[
\begin{aligned}
\langle E\rangle
&=
\left\langle\int_{\mathbb R^3}|W|^2dy\right\rangle
\\
&=
\boxed{
\int_0^\infty
z^{-1/2}\mathscr K_\omega(z)\,dz.
}
\end{aligned}
\]

Likewise the similarity palinstrophy and stretching production are

\[
\boxed{
\langle P\rangle
=
\frac12\int_0^\infty
z^{1/2}\mathscr P_\omega(z)\,dz,
}
\]

\[
\boxed{
\langle Q\rangle
=
\frac12\int_0^\infty
z^{1/2}\mathscr Q_\omega(z)\,dz.
}
\]

---

## 8. Weighted integration of the wedge ODE

Multiply

\[
\mathscr K_\omega'
+2z\mathscr J_\omega'
+3\mathscr J_\omega
=
\mathscr P_\omega-\mathscr Q_\omega
\]

by

\[
\frac12z^{1/2}
\]

and integrate over \(z\in(0,\infty)\).

### Enstrophy-density term

Integration by parts gives

\[
\frac12\int_0^\infty z^{1/2}\mathscr K_\omega' dz
=
-\frac14
\int_0^\infty z^{-1/2}\mathscr K_\omega dz
=
\boxed{-\frac14\langle E\rangle},
\]

provided the natural endpoint terms vanish.

### Flux terms

The combination is

\[
\int_0^\infty z^{3/2}\mathscr J_\omega'dz
+\frac32\int_0^\infty z^{1/2}\mathscr J_\omega dz.
\]

After integration by parts, these cancel exactly, leaving only the endpoint term

\[
[z^{3/2}\mathscr J_\omega]_{0}^{\infty}.
\]

The retained terminal regularity at \(z=0\) and smooth Type-I core behavior as \(z\to\infty\) make this boundary contribution zero on the hard class.

Therefore

\[
-\frac14\langle E\rangle
=
\langle P\rangle-\langle Q\rangle.
\]

Hence

\[
\boxed{
\frac14\langle E\rangle
+\langle P\rangle
=
\langle Q\rangle.
}
\]

This exactly reproduces M5-486.

---

## 9. Significance of the exact recovery

This agreement is a strong consistency check:

- M5-486 was derived directly in similarity variables;
- M5-585 derives the same invariant balance through a new exact physical-spacetime coordinate system, q-ergodic averaging, and weighted z-integration.

The two derivations coincide without inserting the M5-486 result by hand.

Therefore the wedge transformation and the q-averaged enstrophy bookkeeping pass a nontrivial audit.

---

## 10. Anti-proof conclusion

The full z-integral produces no new contradiction. It collapses exactly to the already known positive-stretching identity

\[
\langle Q\rangle
=\frac14\langle E\rangle+\langle P\rangle>0.
\]

Therefore any new gain must come from **localized z-depth information** before the flux terms cancel globally.

For \(0<z_1<z_2<\infty\), one has the exact partial-depth ledger

\[
\boxed{
\frac12\int_{z_1}^{z_2}z^{1/2}(\mathscr P_\omega-\mathscr Q_\omega)dz
=
\frac12[z^{1/2}\mathscr K_\omega]_{z_1}^{z_2}
+[z^{3/2}\mathscr J_\omega]_{z_1}^{z_2}
-rac14\int_{z_1}^{z_2}z^{-1/2}\mathscr K_\omega dz.
}
\]

This localized identity preserves the boundary fluxes that disappear in the global integral.

The next target is to identify whether the positive terminal log-density \(c_\omega\) forces a one-sign or nonvanishing boundary term as \(z\downarrow0\), and whether that can be reconciled with the remote spectator/first-jet structure.

Status: **THE WEDGE ENSTROPHY ODE IS EXACT AND CONSISTENT WITH THE ORIGINAL SIMILARITY BALANCE. GLOBAL INTEGRATION IS CLOSED; THE ONLY NEW LEVER IS LOCALIZED z-DEPTH FLUX. GLOBAL REGULARITY REMAINS UNPROVED.**