# Direction curvature -> palinstrophy / sparseness / third derivative

Date: 2026-08-25

Status: **ACTIVE CONDITIONAL GEOMETRIC DESCENT — GLOBAL REGULARITY NOT PROVED**

This note continues `TRANSVERSE_SECOND_VORTICITY_DERIVATIVE_GATE_2026-08-25.md` at the structured survivor

\[
C_{\xi,2}=r^2|\xi\times\nabla^2\xi|
\]

near a maximum-vorticity point.

The purpose is to join this curvature branch to the already-existing occupancy / sparseness / palinstrophy track.

---

## 1. Setup

Let `x_*` be a maximum-vorticity point at a fixed smooth time:

\[
W=|\omega(x_*)|=\|\omega\|_\infty,
\qquad
r=\left(\frac\nu W\right)^{1/2},
\qquad
\xi=\frac\omega{|\omega|}.
\]

Assume the vorticity direction is smooth on the high-vorticity region under discussion.

Define the centered transverse direction curvature amplitude

\[
\boxed{
b
:=
r^2
|P_{\xi_*^\perp}\nabla^2\xi(x_*)|.
}
\]

Up to fixed tensor constants this is the same geometric content selected by `C_{xi,2}`.

Define the normalized third direction derivative on `B_r(x_*)`:

\[
\boxed{
k_3
:=
r^3
\|\nabla^3\xi\|_{L^\infty(B_r(x_*))}.
}
\]

---

## 2. Curvature persistence creates a first-direction-derivative region

Choose a spatial second-derivative component/direction realizing a fixed fraction of `b/r^2`.  Along the corresponding line, the derivative of `nabla xi` is of size `b/r^2` at the center.

If `k_3` is not too large, the second derivative cannot immediately disappear.  A one-dimensional Taylor/mean-value argument yields a scale

\[
\boxed{
\delta
\gtrsim
r\,
\min\left\{1,\frac{b}{1+k_3}\right\}.
}
\]

Let

\[
s:=\frac\delta r
\gtrsim
\min\left\{1,\frac{b}{1+k_3}\right\}.
\]

Then there exists a point `y` with `|y-x_*| lesssim delta` and, after reducing the radius by a universal constant if needed, a ball `B_{c delta}(y)` on which

\[
\boxed{
|\nabla\xi|
\gtrsim
\frac{b\,s}{r}.
}
\]

Status: **PROVED AS A DETERMINISTIC TAYLOR PERSISTENCE LEMMA**, provided `xi` is smooth on the ball.

---

## 3. High-vorticity occupancy converts this to palinstrophy

Fix an occupancy threshold `0<a<1`.

Assume

\[
|\omega(x)|\ge aW
\qquad
\text{throughout }B_{c\delta}(y).
\]

Using

\[
|\nabla\omega|^2
=|\nabla|\omega||^2+|\omega|^2|\nabla\xi|^2,
\]

we obtain on that ball

\[
|\nabla\omega|^2
\gtrsim
W^2\frac{b^2s^2}{r^2}.
\]

Define the critical palinstrophy cost at the descended radius `delta` by

\[
\boxed{
\mathcal P_\delta
:=
\delta^3
\int_{B_{c\delta}(y)}|\nabla\omega|^2dx.
}
\]

Since `W=nu/r^2` and `delta=sr`,

\[
\boxed{
\frac{\mathcal P_\delta}{\nu^2}
\gtrsim_a
b^2s^8.
}
\]

Equivalently,

\[
\boxed{
\frac{\mathcal P_\delta}{\nu^2}
\gtrsim_a
b^2
\min\left\{1,
\left(\frac{b}{1+k_3}\right)^8
\right\}.
}
\]

Status: **PROVED CONDITIONAL ON HIGH-VORTICITY OCCUPANCY.**

---

## 4. If the high-vorticity ball does not exist

If the occupancy hypothesis fails, then within distance `O(delta)` of the maximum-vorticity point there is a point or nontrivial subregion with

\[
|\omega|<aW.
\]

This is not a contradiction by itself.  It places the branch into the repository's existing high/low vorticity segregation / sparseness track:

\[
\boxed{
\text{direction curvature}
\Longrightarrow
\text{palinstrophy occupancy}
\lor
\text{high-vorticity occupancy failure}
\lor
\text{third-direction-derivative escalation}.
}
\]

To turn mere existence of a low point into a quantitative volume-fraction statement requires an additional persistence/regularity estimate; that conversion is **NOT DERIVED here**.

---

## 5. Small palinstrophy cost forces the third direction derivative upward

On the occupied branch, suppose

\[
\frac{\mathcal P_\delta}{\nu^2}<\varepsilon.
\]

For large `b`, the full-radius branch of the minimum cannot remain active if `epsilon` is small.  In the derivative-limited branch,

\[
\varepsilon
\gtrsim_a
b^2\left(\frac{b}{1+k_3}\right)^8.
\]

Hence

\[
\boxed{
1+k_3
\gtrsim_a
\varepsilon^{-1/8}b^{5/4}.
}
\]

Thus occupied large second direction curvature that avoids critical palinstrophy cost must force a superlinear third-direction-derivative rise.

Status: **PROVED CONDITIONAL.**

---

## 6. Relation to the first-hitting survivor

The previous first-hitting gate gave

\[
\text{vorticity growth}
\Longrightarrow
C_{\xi,2}
\lor
K_{\omega,3}
\lor
\text{far enstrophy tax}.
\]

The present note refines the `C_{xi,2}` branch to

\[
\boxed{
C_{\xi,2}
\Longrightarrow
\text{critical palinstrophy cost}
\lor
\text{high-vorticity sparsity/segregation}
\lor
\text{third-direction-derivative escalation}.
}
\]

Therefore the local maximum-vorticity route now meets two already-existing global/local tracks rather than generating a wholly new survivor:

1. occupancy / segregation / palinstrophy;
2. higher-derivative concentration.

---

## 7. Current obstruction

The remaining difficulty is no longer arbitrary local vortex stretching.  It is the possibility of an infinite cascade that repeatedly chooses one or more of:

1. increasingly thin high-vorticity occupancy sets;
2. critical palinstrophy packets whose total historical cost has not yet been shown nonsummable;
3. third-and-higher direction/vorticity derivative needles.

A global contradiction still requires a genealogy or recurrence statement showing that one of those costs accumulates too strongly for the available energy/enstrophy budget.

---

## 8. Audit verdict

- large second direction curvature plus controlled third derivative creates a nearby first-direction-derivative region: **PROVED**;
- if high vorticity occupies that region, a critical palinstrophy lower bound follows: **PROVED CONDITIONAL**;
- failure of high-vorticity occupancy immediately gives quantitative volume sparseness: **NOT DERIVED**;
- small occupied palinstrophy cost forces superlinear third-direction-derivative escalation: **PROVED CONDITIONAL**;
- these alternatives alone contradict blowup: **NOT DERIVED**;
- global regularity: **UNPROVED**.
