# M19-308 — The local-energy ball identity sharpens large-z whole-sphere radial-current decay from z^{-3/2} to z^{-2} without pressure-gauge estimates

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE SHARPENING / WHOLE-SPHERE CANCELLATION / M19-303 ENDPOINT IMPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why M19-303 is not sharp at the integrated-sphere level

M19-303 estimated the normalized energy-current density pointwise and obtained

\[
|j(z,Y)|\lesssim z^{-3/2}.
\]

That estimate is valid as a coarse endpoint bound, but it does not exploit cancellation after integration over the closed observation sphere.

The physical local-energy identity gives a stronger route that automatically includes convection, pressure work, and viscous energy flux.

## 2. Physical local-energy equality on a fixed ball

For the smooth ancient solution,

\[
e_{ph}:=\frac12|V|^2
\]

satisfies

\[
\partial_s e_{ph}
+
\nabla\cdot J_{ph}
=
-\nu|\nabla V|^2,
\]

where `J_ph` is the full local-energy flux, including pressure and viscosity.

Integrate over the fixed ball `B_r`:

\[
\boxed{
\int_{S_r}J_{ph}\cdot n\,dS
=
-\frac d{ds}\int_{B_r}e_{ph}dx
-\nu\int_{B_r}|\nabla V|^2dx.
}
\]

No pressure gauge appears in this identity.

## 3. Type-I derivative rates

Let

\[
T=-s\gg1.
\]

M5-475 plus the parabolic rescaling argument of M19-303 gives

\[
\boxed{
|V|\lesssim T^{-1/2},
\qquad
|\nabla V|\lesssim T^{-1},
\qquad
|\partial_sV|\lesssim T^{-3/2}
}
\]

uniformly on every fixed ball when `T` is large.

The time-derivative rate follows from the same Type-I unit-scale smoothing, or equivalently from the rescaled equation after one parabolic derivative.

## 4. Bound the local-energy time derivative

Since

\[
\partial_se_{ph}=V\cdot\partial_sV,
\]

we have

\[
|\partial_se_{ph}|\lesssim T^{-2}.
\]

Therefore

\[
\boxed{
\left|
\frac d{ds}
\int_{B_r}e_{ph}dx
\right|
\lesssim
r^3T^{-2}.
}
\]

Likewise,

\[
\boxed{
\nu\int_{B_r}|\nabla V|^2dx
\lesssim
r^3T^{-2}.
}
\]

Hence the complete physical energy flux through the closed sphere satisfies

\[
\boxed{
\left|
\int_{S_r}J_{ph}\cdot n\,dS
\right|
\lesssim
r^3T^{-2}.
}
\]

## 5. Convert the closed-sphere flux to wedge current

M5-583 writes the physical energy-flux density as

\[
J_{ph}=r^{-3}\mathcal J.
\]

Since

\[
dS_x=r^2d\omega,
\]

the physical flux through `S_r` is

\[
\int_{S_r}J_{ph}\cdot n\,dS
=
r^{-1}
\int_{S^2}\mathcal J_r d\omega
=
r^{-1}j(z,Y).
\]

Therefore

\[
|j(z,Y)|
\lesssim
r^4T^{-2}.
\]

Using

\[
T=zr^2,
\]

we obtain

\[
\boxed{
|j(z,Y)|\lesssim z^{-2}.
}
\]

This is uniform on the retained smooth Type-I hull for fixed large-z wedge depth.

## 6. Sharpened endpoints

Consequently

\[
\boxed{
\sqrt z\,j(z,Y)=O(z^{-3/2})\to0,
}
\]

and

\[
\boxed{
zj(z,Y)=O(z^{-1})\to0.
}
\]

The conditioned and invariant means obey the same estimates:

\[
\boxed{
\mathscr J_m(z)=O(z^{-2}),
\qquad
z\mathscr J_m(z)=O(z^{-1}).
}
\]

## 7. Improvement over M19-303

M19-303 remains a valid pointwise-component/gauge audit and supplied the first certified zero endpoint.

M19-308 strengthens only the **closed-sphere integrated current** by exploiting the exact local-energy balance:

\[
\boxed{
O(z^{-3/2})
\quad\leadsto\quad
O(z^{-2}).
}
\]

This sharper rate is particularly useful because it avoids separately estimating the pressure contribution and displays the angular/closed-sphere cancellation automatically.

## 8. Integrated-tail consequence

The radial current now has the stronger tail estimate

\[
\boxed{
\int_R^\infty|\mathscr J_m(z)|dz
\lesssim R^{-1}.
}
\]

Thus all radial-current compensation beyond large depth `R` is quantitatively small.

Any order-one current reversal/payment required by the production-conditioned event must therefore occur in a bounded/intermediate depth region rather than escaping indefinitely to `z=infinity`.

## 9. Updated localization target

M19-305 shows total-budget excess cannot close the branch.

M19-308 now prevents an order-one conditioned transport burden from being hidden arbitrarily deep in the Type-I core.

The surviving phase/rigidity question can therefore be localized to a finite depth interval:

\[
\boxed{
\mathcal T_{phase}^{bounded-z}:
\text{classify the production/current hysteresis and return geometry on one bounded wedge-depth corridor.}
}
\]

This is stronger than the previous global factor statement because the large-z tail is quantitatively negligible for radial transport.

---

\[
\boxed{\text{M19-308 COMPLETE; WHOLE-SPHERE RADIAL CURRENT DECAYS AS }z^{-2}\text{ AND ORDER-ONE RETURN CANNOT ESCAPE TO ARBITRARILY LARGE DEPTH.}}
\]