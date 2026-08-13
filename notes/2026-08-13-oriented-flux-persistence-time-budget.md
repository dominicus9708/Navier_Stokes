# Oriented-flux persistence: finite time-integrated length budget

Date: 2026-08-13

Status: **DERIVED COROLLARY OF THE PERSISTENT-FLUX LEMMA + GLOBAL ENERGY DISSIPATION / OPEN NATURAL-TIME CLOSURE**.

This note converts the instantaneous persistent-tube occupancy cost into a finite time-integrated budget.

No global-regularity claim is made.

---

## 1. Persistent robust tube hypothesis

At time `t`, let

\[
W(t)=\|\omega(t)\|_\infty.
\]

Choose the natural radius

\[
\boxed{
r(t)=aW(t)^{-1/2},
\qquad a>0.
}
\]

Suppose there is a straight-cylinder branch of length `L(t)` and a radius

\[
\rho(t)\in[r(t),2r(t)]
\]

such that the signed axial vorticity flux keeps one orientation and obeys

\[
|\Phi_{\rho(t)}(s,t)|
\ge
\kappa W(t)r(t)^2
\]

throughout the axial interval of length `L(t)`.

The previous persistent-flux lemma gives

\[
\int_{C_t}|\omega|^2dx
\ge
\frac{\kappa^2}{4\pi}
W(t)^2r(t)^2L(t).
\]

Since the global enstrophy

\[
E_\omega(t)=\|\omega(t)\|_2^2
\]

dominates the cylinder contribution,

\[
E_\omega(t)
\ge
\frac{\kappa^2}{4\pi}
W(t)^2r(t)^2L(t).
\]

Substituting `r=a W^{-1/2}` gives

\[
\boxed{
E_\omega(t)
\ge
\frac{\kappa^2a^2}{4\pi}
W(t)L(t).
}
\]

Thus physical persistence length is controlled instantaneously by

\[
\boxed{
W(t)L(t)
\le
\frac{4\pi}{\kappa^2a^2}
E_\omega(t).
}
\]

---

## 2. Natural-length count

Define the number of natural radii occupied axially by

\[
\boxed{
N_{\rm tube}(t)
=\frac{L(t)}{r(t)}
=\frac{L(t)\sqrt{W(t)}}{a}.
}
\]

Then

\[
W(t)L(t)
=aN_{\rm tube}(t)\sqrt{W(t)},
\]

so the same estimate becomes

\[
\boxed{
N_{\rm tube}(t)\sqrt{W(t)}
\le
\frac{4\pi}{\kappa^2a^3}
E_\omega(t).
}
\]

This is scale invariant under the Navier--Stokes scaling.

---

## 3. Global viscous budget

For smooth finite-energy whole-space incompressible Navier--Stokes flow,

\[
\frac12\|u(t)\|_2^2
+\nu\int_0^t\|\nabla u(s)\|_2^2ds
=
\frac12\|u_0\|_2^2.
\]

For a divergence-free decaying field,

\[
\|\nabla u\|_2^2=\|\omega\|_2^2=E_\omega.
\]

Therefore

\[
\boxed{
\int_0^{T}E_\omega(t)dt
\le
\frac{\|u_0\|_2^2}{2\nu}
}
\]

for every smooth time interval `[0,T]`.

Combining this with the tube lower bound yields

\[
\boxed{
\int_{\mathcal T}
W(t)L(t)dt
\le
\frac{2\pi}{\kappa^2a^2\nu}
\|u_0\|_2^2,
}
\]

where `mathcal T` is any set of times on which the robust persistent-tube hypothesis holds.

Equivalently,

\[
\boxed{
\int_{\mathcal T}
N_{\rm tube}(t)\sqrt{W(t)}dt
\le
\frac{2\pi}{\kappa^2a^3\nu}
\|u_0\|_2^2.
}
\]

Hence long oriented-flux persistence has a finite global time budget.

---

## 4. Consequence for macroscopic persistence

Suppose a hypothetical blowup branch also satisfies a lower vorticity-growth estimate of the already recorded form

\[
W(t)\gtrsim\frac{1}{T^*-t}
\]

on a terminal interval.

If a robust oriented tube had a physical length bounded below by

\[
L(t)\ge L_0>0
\]

throughout that terminal interval, then

\[
\int^{T^*}W(t)L(t)dt
\gtrsim
L_0\int^{T^*}\frac{dt}{T^*-t}
=\infty,
\]

contradicting the finite persistence budget.

Therefore such a robust intense tube cannot remain macroscopically long all the way to a finite-time singularity.

The allowed residual geometry must shrink its physical axial length.

This statement does **not** rule out a tube that remains `O(1)` or larger in **natural-radius units** while both its radius and physical length shrink to zero.

---

## 5. Relation to the existing natural-window channel

The already active natural-window enstrophy channel is

\[
\mathcal Z_\omega(t_0)
=
\sqrt{W(t_0)}
\int_{I_{t_0}}E_\omega(s)ds.
\]

On the subset of a natural window where

\[
W(s)\ge\theta W(t_0),
\qquad 0<\theta<1,
\]

the instantaneous persistence estimate gives

\[
N_{\rm tube}(s)
\le
C_{a,\kappa,\theta}
\frac{E_\omega(s)}{\sqrt{W(t_0)}}.
\]

Consequently

\[
\boxed{
W(t_0)
\int_{I_{t_0}\cap\{W\ge\theta W(t_0)\}}
N_{\rm tube}(s)ds
\le
C_{a,\kappa,\theta}
\mathcal Z_\omega(t_0).
}
\]

If the active part of the window has duration comparable to `1/W(t_0)`, then the average number of natural tube lengths is controlled by `Z_omega`.

Thus the long-persistence branch is not completely independent of the previously defined natural-window enstrophy cost.

---

## 6. Residual interpretation

The oriented-flux branch is now constrained by two simultaneous budgets:

1. **instantaneous occupancy**
   \[
   N_{\rm tube}\sqrt W
   \lesssim E_\omega;
   \]
2. **time-integrated viscous budget**
   \[
   \int N_{\rm tube}\sqrt Wdt<\infty.
   \]

Therefore a residual singular cascade cannot maintain a strong oriented tube of fixed physical length.

It must instead use a shrinking tube geometry and keep paying the natural-window enstrophy cost as the vorticity scale increases.

---

## 7. Next target

The remaining cheap-looking escape is a tube whose physical length shrinks together with its radius while the number

\[
N_{\rm tube}=L/r
\]

stays bounded or grows slowly enough to respect the finite weighted budget.

To close that branch one needs a **temporal vorticity-flux balance** for a transported or moving cross-section.

For Euler transport, material vorticity flux is frozen.  In the viscous equation, flux change is generated by a boundary derivative term.  The next calculation should therefore separate

\[
\boxed{
\text{material transport}
\quad\text{from}\quad
\text{viscous flux erosion}
}
\]

and test whether order-one flux loss over a natural time `O(W^{-1})` forces a critical palinstrophy cost.

Status: **OPEN MATERIAL-FLUX / VISCOUS-EROSION CLOSURE**.
