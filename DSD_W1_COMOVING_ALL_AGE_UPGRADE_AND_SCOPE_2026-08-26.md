# DSD W1 Co-Moving All-Age Upgrade and Scope Audit

Date: 2026-08-26

Status: **FIXED-AGE CO-MOVING DEFECT UPGRADED TO AN H-INDEPENDENT ALL-AGE DEFECT ON THE W1 INVARIANT CORRIDOR / THE UPGRADE IS AN INTERNAL W1 STATEMENT AND DOES NOT BY ITSELF GIVE EXPANDING-WINDOW CONVERGENCE OF THE FINITE-ENERGY PRELIMIT / GLOBAL REGULARITY UNPROVED.**

## 1. Starting point

For a W1 Leray orbit define

\[
\lambda(h)=Re^{h/2},
\qquad
W_R(z,h)=\lambda(h)U(\lambda(h)z,h).
\]

The exact co-moving equation is

\[
\boxed{
\partial_hW_R
=R^{-2}e^{-h}
\left[
\nu\Delta_zW_R
-\mathbb P\nabla_z\cdot(W_R\otimes W_R)
\right].
}
\]

The earlier co-moving note used this only for fixed finite `h` and concluded

\[
\|W_R(h)-W_R(0)\|_{H^{-1}(A^*)}
\le C_hR^{-2}.
\]

This note checks whether `C_h` can be made independent of `h` on the W1 invariant corridor.

---

## 2. Uniform fixed-annulus H1 bound for all W1 times

The established remote W1/Type-I shell bounds are uniform on the recurrent corridor:

\[
\|U(\cdot,s)\|_{L^\infty(A_\rho)}
\le A_0\rho^{-1},
\]

and

\[
\|\nabla U(\cdot,s)\|_{L^2(A_\rho)}
\le G_0\rho^{-1/2}
\]

for large `rho`, uniformly in W1 time `s`.

Set `rho=lambda(h)`.  On a fixed annulus `A^*` in the z variable,

\[
\|W_R(h)\|_2^2
=
\lambda(h)^{-1}
\int_{A^*_{\lambda(h)}}|U(Y,h)|^2dY.
\]

The Type-I bound gives

\[
\int_{A^*_{\lambda}}|U|^2dY
\lesssim
\lambda^3\left(A_0\lambda^{-1}\right)^2
\lesssim A_0^2\lambda,
\]

hence

\[
\boxed{
\|W_R(h)\|_2\le C A_0.
}
\]

For the gradient,

\[
\|\nabla_zW_R(h)\|_2^2
=
\lambda(h)
\int_{A^*_{\lambda(h)}}|\nabla_YU(Y,h)|^2dY
\le C G_0^2.
\]

Therefore

\[
\boxed{
\sup_{h\ge0}\|W_R(h)\|_{H^1(A^*)}
\le C_*
}
\]

with `C_*` independent of both large `R` and `h`.

This is the additional input that was not written explicitly in the fixed-age co-moving note.

---

## 3. Uniform H^{-1} nonlinear bound

On the fixed enlarged annulus,

\[
\|\Delta W_R\|_{H^{-1}}
\lesssim
\|\nabla W_R\|_2
\le C_*,
\]

while

\[
\|\mathbb P\nabla\cdot(W_R\otimes W_R)\|_{H^{-1}}
\lesssim
\|W_R\otimes W_R\|_2
\lesssim
\|W_R\|_4^2
\le C_*^2.
\]

Thus

\[
\boxed{
\|\partial_hW_R(h)\|_{H^{-1}(A^*)}
\le
C R^{-2}e^{-h}.
}
\]

Integrating from `0` to arbitrary `H>=0` gives

\[
\boxed{
\|W_R(H)-W_R(0)\|_{H^{-1}(A^*)}
\le
CR^{-2}
\int_0^He^{-h}dh
\le
CR^{-2}.
}
\]

The constant is independent of `H`.

Status: **PROVED on the W1 invariant corridor under the already established uniform remote shell bounds.**

---

## 4. All-age L2 and L3 upgrades

The H1 norm of the difference is uniformly bounded by `2C_*`.
Interpolating `H^{-1}` and `H^1`,

\[
\boxed{
\|W_R(H)-W_R(0)\|_2
\le CR^{-1}
\qquad\forall H\ge0.
}
\]

The fixed-annulus Sobolev bound gives a uniform L6 ceiling, hence L2--L6 interpolation gives

\[
\boxed{
\|W_R(H)-W_R(0)\|_3
\le CR^{-1/2}
\qquad\forall H\ge0.
}
\]

Consequently the critical shell mass obeys

\[
\boxed{
\left|
\Psi_{e^{H/2}R}(\Phi_HU)
-
\Psi_R(U)
\right|
\le CR^{-1/2}
\qquad\forall H\ge0.
}
\]

Thus the outward dilation conveyor is genuinely all-age inside W1.

---

## 5. What the all-age theorem does and does not say

The theorem compares two states on the **W1 limit orbit**:

\[
U\in M,
\qquad
\Phi_HU\in M.
\]

It does not state that the original finite-energy normalized prelimit `U^{pre}(s_n+H)` converges to `\Phi_HU` uniformly for `H=H_n\to\infty`.

The omega-limit construction only supplies, without an additional theorem,

\[
U^{pre}(s_n+H)\to\Phi_HU
\]

for each fixed `H` on each fixed spatial window.

Therefore one may not set an `n`-dependent age `H_n->infinity` and pass to the limit automatically.

This is the first scope boundary.

---

## 6. Physical-radius interpretation

Let

\[
\ell_n=e^{-s_n/2}
\]

be the similarity length at a prelimit time `s_n`.
A W1 normalized shell of radius `R` corresponds at that base time to physical radius

\[
r_n=\ell_nR.
\]

Under the W1 co-moving flow by age `H`, its normalized radius becomes

\[
e^{H/2}R,
\]

while the similarity length would become

\[
\ell_ne^{-H/2}.
\]

Their product remains

\[
\boxed{
r_n=\ell_nR.}
\]

Hence the all-age W1 conveyor preserves one physical radius relative to the chosen base time.

But for every fixed normalized `R`,

\[
r_n=e^{-s_n/2}R\to0.
\]

Thus the theorem transports memory down to a shrinking physical radius as the blow-up sequence is taken.  It does not place a fixed positive amount of energy on a fixed macroscopic physical shell.

---

## 7. Why a fixed physical radius requires an expanding normalized window

To represent a fixed physical radius `r_0>0` at time `s_n`, one needs

\[
\boxed{
R_n=r_0e^{s_n/2}\to\infty.
}
\]

Therefore a passage from the W1 critical tail to one fixed physical shell requires convergence of the actual normalized prelimit on spatial windows whose radius grows like

\[
R_n\asymp e^{s_n/2}.
\]

Local compactness on every fixed normalized ball does not provide this.

Call the missing bridge the **Expanding-Window Gate (EWG)**.

A schematic sufficient statement would be a convergence estimate of the form

\[
U^{pre}(s_n)\to U
\]

in a critical shell topology uniformly for

\[
1\ll R\le c e^{s_n/2},
\]

or another theorem that directly controls the interchange

\[
\lim_{n\to\infty}
\lim_{R\to\infty}
\quad\leftrightarrow\quad
\lim_{R\to\infty}
\lim_{n\to\infty}.
\]

No such EWG is currently proved.

---

## 8. DSD audit verdict

### Proved

- the co-moving W1 defect is `O(R^-2)` in H^-1 uniformly for all forward W1 ages;
- the corresponding L2 defect is `O(R^-1)` uniformly in age;
- the corresponding L3 defect is `O(R^-1/2)` uniformly in age;
- W1 critical shell memory is therefore genuinely all-age along the dilation conveyor.

### Not proved

- uniform approximation of the original finite-energy prelimit by the W1 orbit for ages tending to infinity;
- convergence on normalized radii of order `e^(s_n/2)`;
- transfer of the W1 far tail to a fixed nonshrinking physical radius;
- global regularity.

The all-age upgrade strengthens the W1 internal dynamics, but it does not erase the scale-infinity/prelimit interface.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
