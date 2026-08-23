# Relative Campanato Remote-Strain Gate — 2026-08-23

Status: **PARTIAL CLOSURE — GLOBAL REGULARITY NOT PROVED.**

This note replaces the absolute-velocity Morrey form of the remote-strain estimate by a Galilean-invariant relative-velocity Campanato form. The point is that strain is invariant under addition of a constant velocity, so the natural quantity is local velocity variance, not absolute local kinetic energy.

---

## 1. Remote strain functional

At a normalized first-hitting snapshot, let

\[
\mathcal S_R
=
\int_{\mathbb R^3}K(y)\,\psi_R(y)\,\Omega(y)\,dy,
\qquad
\Omega=\nabla\times U,
\]

where `psi_R` vanishes near the core and is one in the remote region. The Biot–Savart strain kernel satisfies

\[
|K(y)|\lesssim |y|^{-3}.
\]

Integrating by parts gives

\[
\mathcal S_R
=
\int_{\mathbb R^3}L_R(y)U(y)\,dy,
\qquad
L_R=\pm\nabla\times(K\psi_R),
\]

with

\[
\boxed{|L_R(y)|\lesssim |y|^{-4}.}
\]

Because the cutoff removes the origin singularity and `K psi_R` decays like `|y|^{-3}` at infinity, the boundary integral at radius `R_out` is `O(R_out^{-1})`. Hence

\[
\boxed{\int_{\mathbb R^3}L_R(y)\,dy=0.}
\]

Therefore, for every constant vector `c`,

\[
\boxed{
\mathcal S_R
=
\int L_R(y)(U(y)-c)\,dy.
}
\]

This is the exact Galilean cancellation needed below.

---

## 2. Relative Campanato quantity

Define

\[
\boxed{
\mathcal C_\rho
:=
\rho^{-1}
\int_{B_\rho}
|U-(U)_{B_\rho}|^2\,dy.
}
\]

This is scale invariant for the Navier–Stokes scaling and insensitive to a constant drift.

Let

\[
\rho_k=2^kR,
\qquad
A_k=\{\rho_k\lesssim |y|\lesssim 2\rho_k\}.
\]

The kernel estimates give

\[
\|L_R\|_{L^2(A_k)}\lesssim \rho_k^{-5/2},
\qquad
\|L_R\|_{L^1(A_k)}\lesssim \rho_k^{-1}.
\]

For

\[
m_k=(U)_{B_{2\rho_k}},
\]

we have

\[
\|U-m_k\|_{L^2(B_{2\rho_k})}
\lesssim
\rho_k^{1/2}\mathcal C_{2\rho_k}^{1/2}.
\]

The difference of neighboring means satisfies

\[
|m_{j+1}-m_j|
\lesssim
\rho_j^{-1}\mathcal C_{2\rho_{j+1}}^{1/2}.
\]

Thus the mean difference from the first remote scale telescopes, and after summing dyadic annuli and reordering the resulting double sum one obtains

\[
\boxed{
|\mathcal S_R|
\le
C_{Camp}R^{-2}
\sum_{k\ge0}2^{-2k}
\mathcal C_{2^{k+1}R}^{1/2}.
}
\]

`C_Camp` depends only on the fixed cutoff profile and universal kernel constants.

---

## 3. Uniform relative-energy corridor closes active remote strain

If

\[
\sup_{\rho\ge R}\mathcal C_\rho\le C_*,
\]

then

\[
\boxed{
|\mathcal S_R|
\le
C'_{Camp}C_*^{1/2}R^{-2}.
}
\]

Consequently an order-one active remote-strain threshold

\[
|\mathcal S_R|\ge s_0>0
\]

is possible only for

\[
\boxed{
R\le
\left(\frac{C'_{Camp}C_*^{1/2}}{s_0}\right)^{1/2}.
}
\]

Therefore, in a uniform relative-Campanato corridor, the dynamically active part of `H_remote` cannot migrate to normalized radius infinity.

---

## 4. Converse: active remote strain forces Campanato escalation

Suppose

\[
|\mathcal S_R|\ge s_0.
\]

Since

\[
\sum_{k\ge0}2^{-2k}<\infty,
\]

the preceding estimate implies that at least one dyadic radius

\[
\rho\ge R
\]

must satisfy

\[
\boxed{
\mathcal C_\rho
\ge
c_{Camp}s_0^2R^4.
}
\]

Thus an active remote halo cannot remain both very remote and low-variance. It forces a large relative-velocity reservoir on some parent scale.

The growth `R^4` is the natural scaling of a coherent affine field

\[
U(y)\approx Ay,
\qquad |A|\sim1,
\]

because then

\[
\mathcal C_R\sim R^4.
\]

Therefore the surviving obstruction is more accurately described as a **coherent affine-strain / relative-energy escalation corridor**, not as diffuse remote derivative mass.

---

## 5. Global kinetic energy gives a fallback physical-radius barrier

At first-hitting scale

\[
r=W^{-1/2},
\qquad
U(y)=r\,u(X+ry),
\]

so

\[
\|U\|_2^2
=r^{-1}\|u\|_2^2
=W^{1/2}\|u\|_2^2.
\]

Because local variance is minimized over constants,

\[
\mathcal C_\rho
\le
\rho^{-1}\|U\|_2^2
\le
E_0W^{1/2}\rho^{-1},
\]

where `E_0` is controlled by the initial kinetic energy.

Combine this with the active lower bound

\[
\mathcal C_\rho\gtrsim s_0^2R^4,
\qquad
\rho\ge R.
\]

Then

\[
s_0^2R^4
\lesssim
E_0W^{1/2}R^{-1},
\]

hence

\[
\boxed{R\lesssim W^{1/10}.}
\]

The corresponding physical radius

\[
\ell=RW^{-1/2}
\]

therefore obeys

\[
\boxed{\ell\lesssim W^{-2/5}.}
\]

This improves the earlier `W^{-1/3}` and `W^{-1/7}` physical contraction exponents obtained through less direct derivative/enstrophy routes.

---

## 6. Relation to the Type-I compactness bridge

The standard local Type-I energy quantity is

\[
A(R)
=R^{-1}\int_{B_R}|U|^2.
\]

A coherent affine field has

\[
A(R)\sim R^4,
\]

modulo the drift gauge. Hence the same affine-strain corridor that saturates the active-remote Campanato estimate is exactly an obstruction to obtaining a uniform expanding-radius Type-I energy bound.

This identifies the compactness gap more sharply:

\[
\boxed{
\text{active remote influence}
\Longrightarrow
\text{relative Campanato escalation}
\Longrightarrow
\text{coherent affine-strain / local-energy obstruction}.
}
\]

---

## 7. What is and is not closed

Proved at the level of the present smooth first-hitting calculation:

1. the remote-strain functional annihilates constant drift;
2. remote strain is controlled by a dyadic relative-Campanato ledger;
3. uniform relative Campanato control forces `R^{-2}` decay;
4. order-one active remote strain forces `R^4` relative-energy escalation;
5. global kinetic energy restricts the active physical radius to `O(W^{-2/5})`.

Still open:

\[
\boxed{
\text{prove a scale-uniform bound on }\mathcal C_\rho
\quad\text{or}\quad
\text{show that its escalation pays a finite-stage turnover cost }T.
}
\]

Status: **ACTIVE `H_remote` HAS BEEN REDUCED TO A GALILEAN-INVARIANT RELATIVE-CAMPANATO / AFFINE-STRAIN CORRIDOR. THIS IS A SUBSTANTIAL PRUNING STEP, NOT A GLOBAL REGULARITY PROOF.**