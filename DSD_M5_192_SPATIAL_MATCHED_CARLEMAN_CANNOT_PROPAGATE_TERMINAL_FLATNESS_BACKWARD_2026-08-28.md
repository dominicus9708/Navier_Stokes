# DSD M5-192 — Spatial Matched Carleman Cannot Propagate Terminal Flatness Backward

Date: 2026-08-28

Status: **ENDPOINT-ADAPTATION CORRECTION / THE IGNATOVA–KUKAVICA MATCHED LAPLACE/HEAT CARLEMAN USES A PURELY SPATIAL SINGULAR WEIGHT; A ONE-SIDED TIME CUTOFF REMOVES THE TERMINAL BOUNDARY BECAUSE THE W1 DIFFERENCE IS ALL-JET FLAT THERE, BUT THE LOWER-TIME CUTOFF COMMUTATOR RECEIVES EXACTLY THE SAME SPATIAL EXPONENTIAL WEIGHT AND CANNOT BE SUPPRESSED BY THE CARLEMAN PARAMETER / THEREFORE THE MATCHED SPATIAL CARLEMAN IS A SPATIAL PROPAGATION TOOL, NOT A BACKWARD-TIME TOOL; NAIVE HALF-CYLINDER ADAPTATION IS RED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact heat Carleman used in the external proof

Ignatova–Kukavica Lemma 3.2 uses

\[
\psi(x)=|x|^{-m}
\]

and, schematically,

\[
\boxed{
\tau^3\iint |u|^2e^{2\tau\psi}
+
\tau\iint |\nabla u|^2e^{2\tau\psi}
\lesssim
\iint |(\partial_t-\Delta)u|^2e^{2\tau\psi}.
}
\]

The same purely spatial weight is paired with the elliptic pressure Carleman.

The estimate is stated for functions compactly supported in the **interior of the time interval**.

---

## 2. One-sided terminal cutoff

Shift terminal time to `t=0` and suppose the W1 difference is defined for

\[
-\delta^2<t\le0.
\]

Choose a smooth time cutoff `chi(t)` such that

- `chi=0` near `t=-delta^2`;
- `chi=1` for `-delta^2/2<t<0`.

Because M5-145 gives every terminal time jet of `Z` equal to zero on an exterior ball, extending `chi Z` by zero for `t>0` produces no terminal distributional delta term at `t=0`.

This part is **GREEN**.

---

## 3. The unavoidable lower-time commutator

For the parabolic part,

\[
(\partial_t-\Delta)(\chi Z)
=
\chi(\partial_t-\Delta)Z
+
\chi' Z.
\]

The support of `chi'` is a lower-time slab

\[
I_-\Subset(-\delta^2,-\delta^2/2).
\]

The Carleman contribution is

\[
\boxed{
\iint_{I_-}|\chi'Z|^2e^{2\tau\psi(x)}\,dxdt.
}
\]

Since `psi` depends only on `x`, this term has the **same exponential spatial factor** as the desired left-hand norm at later times and the same spatial location.

There is no factor of the form

\[
e^{-c\tau}
\]

separating the lower-time cutoff from the terminal region.

---

## 4. Why terminal flatness does not price the lower cutoff

Terminal all-jet flatness controls

\[
Z(t)\quad\text{as }t\uparrow0,
\]

but `chi' Z` is supported a fixed positive time distance away from `0`.

No already-proved W1 estimate forces

\[
Z=0
\]

or exponentially small on `I_-`.

Therefore the lower cutoff term is an uncontrolled source of the same Carleman order.

Taking

\[
\tau\to\infty
\]

does not remove it.

---

## 5. Structural verdict

The matched spatial weight is excellent for

\[
\boxed{
\text{spatial propagation of smallness at fixed/interior times}
}
\]

but it does not distinguish earlier and later time slices.

Hence

\[
\boxed{
\text{terminal all-jet flatness}
+
\text{Ignatova--Kukavica spatial Carleman}
\not\Rightarrow
\text{backward equality}.
}
\]

The naive one-sided endpoint adaptation is **RED**.

---

## 6. What kind of weight is actually required

A genuine backward-time estimate must contain a time-dependent phase

\[
\Phi(x,t)
\]

such that the lower-time cutoff region is exponentially disfavored relative to the terminal target region.

Schematically one needs

\[
\Phi(x,t_{lower})<\Phi(x,t_{target})
\]

on the same spatial set, so that

\[
e^{2s\Phi(t_{lower})}
\ll
e^{2s\Phi(t_{target})}
\qquad(s\to\infty).
\]

This is the missing dynamic axis that a purely spatial strong-UC weight cannot supply.

---

## 7. Pressure matching becomes the new problem

Once the parabolic weight depends on time, the pressure elliptic equation at each time must be estimated with the **same time-parameterized spatial phase**.

Thus the new target is

\[
\boxed{
\text{terminal-singular backward heat/Oseen Carleman}
+
\text{time-parameterized elliptic pressure Carleman}.
}
\]

This is different from both:

- the rejected pure `-log rho` Type-I center weight of M5-187;
- the fixed-time spatial matched weight of M5-191.

---

## 8. DSD audit

### Formation — GREEN

The lower time-cutoff term is an actual term in the conjugated PDE.

### Axis — GREEN

Spatial strong UC and temporal backward propagation are explicitly separated.

### Static aggregation — GREEN

Terminal flatness is not reused to pay a source located a fixed time distance away.

### Dynamics — RED for naive endpoint adaptation

The spatial weight has no backward-time discrimination.

### Cross-audit — GREEN

This prevents a circular argument in which terminal flatness is silently assumed to control earlier-time data.

---

## 9. Next calculation

Construct or import a terminal-time backward parabolic phase and test whether its spatial slice satisfies a uniform elliptic pseudoconvexity estimate for the pressure equation.

The first candidate should be drawn from established backward-uniqueness heat weights rather than from an ad hoc logarithmic Type-I weight.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
