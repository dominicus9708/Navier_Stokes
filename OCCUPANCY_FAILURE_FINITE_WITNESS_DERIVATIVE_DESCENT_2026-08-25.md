# Occupancy-Failure Finite Witness -> Palinstrophy / Derivative Descent

Date: 2026-08-25

Status: **FINITE-WITNESS DESCENT PROVED / OCCUPANCY-FAILURE PRIMITIVE BRANCH PRUNED / GLOBAL REGULARITY NOT PROVED.**

This note continues the DSD-internal local-core audit after `DIRECTION_CURVATURE_TO_PALINSTROPHY_OR_SPARSENESS_2026-08-25.md`.

The previous note correctly warned that failure of high-vorticity occupancy at one point does **not** by itself imply a quantitative volume-fraction sparseness statement. The present note does not try to manufacture volume sparseness. Instead it uses the failed occupancy statement exactly as DSD forms it: a **finite counter-witness point**. That finite witness already forces a large first-vorticity derivative somewhere between the maximum and the low point.

---

## 1. Setup inherited from the direction-curvature descent

Let

\[
W=|\omega(x_*)|=\|\omega\|_\infty,
\qquad
r=\left(\frac\nu W\right)^{1/2}.
\]

The previous direction-curvature persistence step produced a descended radius

\[
\delta=sr,
\qquad
s\gtrsim
\min\left\{1,\frac{b}{1+k_3}\right\},
\]

where

\[
b=r^2|P_{\xi_*^\perp}\nabla^2\xi(x_*)|,
\qquad
k_3=r^3\|\nabla^3\xi\|_{L^\infty(B_r(x_*))}.
\]

Fix an occupancy level

\[
0<a<1.
\]

The occupied branch assumes \(|\omega|\ge aW\) throughout the relevant descended ball. Here we audit the failure branch.

---

## 2. A single low-vorticity point is already a finite DSD witness

Suppose there exists a point \(y\) with

\[
|y-x_*|\le C_0\delta
\]

such that

\[
|\omega(y)|<aW.
\]

This is a finite witness to the failure of the universal occupancy statement.

By the reverse triangle inequality,

\[
|\omega(x_*)-\omega(y)|
\ge
\bigl||\omega(x_*)|-|\omega(y)|\bigr|
>
(1-a)W.
\]

Parameterize the segment from \(x_*\) to \(y\) by \(\gamma\). Since \(\omega\) is smooth before the hypothetical singular time,

\[
\omega(y)-\omega(x_*)
=
\int_0^{|y-x_*|}
(\nabla\omega)(\gamma(\ell))e\,d\ell
\]

for the unit segment direction \(e\). Hence

\[
(1-a)W
<
\int_0^{|y-x_*|}|\nabla\omega(\gamma(\ell))|\,d\ell.
\]

Therefore there exists a point \(z\) on the segment for which

\[
\boxed{
|\nabla\omega(z)|
\ge
c_0\frac{(1-a)W}{\delta}.
}
\]

This argument uses the smooth vector field \(\omega\) directly and does not require the direction field \(\xi=\omega/|\omega|\) to be defined at the low point.

**Status: PROVED.**

---

## 3. Large first derivative either persists or forces a second-derivative needle

Write

\[
G:=|\nabla\omega(z)|,
\qquad
H_2:=\|\nabla^2\omega\|_{L^\infty(B_{C\delta}(x_*))}.
\]

Define the normalized second-vorticity-derivative amplitude

\[
\boxed{
h_2
:=
\frac{r^2}{W}H_2
=
\frac{r^4}{\nu}H_2.
}
\]

Choose a persistence radius

\[
\eta
:=
c_1\min\left\{
\delta,
\frac{G}{H_2}
\right\},
\]

with the usual convention that the second entry is infinite if \(H_2=0\), and with \(c_1>0\) small enough that the ball remains in the audited region.

The mean-value estimate for \(\nabla\omega\) then gives

\[
|\nabla\omega(x)|\ge c_2G
\qquad
(x\in B_\eta(z)).
\]

Using

\[
G\gtrsim\frac{(1-a)W}{sr}
\]

and

\[
H_2=\frac{W}{r^2}h_2,
\]

we obtain

\[
\boxed{
\frac\eta r
\gtrsim
\min\left\{
s,
\frac{1-a}{s h_2}
\right\}.
}
\]

Thus an occupancy-failure witness has only two ways to avoid a spatially persistent first derivative:

1. the first derivative persists on a finite ball;
2. \(h_2\) is large enough to destroy that persistence rapidly.

**Status: PROVED.**

---

## 4. Persistent first derivative pays a critical palinstrophy packet

Define

\[
\boxed{
\mathcal P_\eta
:=
\eta^3
\int_{B_\eta(z)}|\nabla\omega|^2dx.
}
\]

On the persistence ball,

\[
\int_{B_\eta(z)}|\nabla\omega|^2dx
\gtrsim
G^2\eta^3,
\]

so

\[
\mathcal P_\eta
\gtrsim
G^2\eta^6.
\]

Because

\[
W=\frac\nu{r^2},
\qquad
\delta=sr,
\]

we have

\[
\frac{G^2}{\nu^2}
\gtrsim
\frac{(1-a)^2}{s^2r^6}.
\]

Therefore

\[
\boxed{
\frac{\mathcal P_\eta}{\nu^2}
\gtrsim
(1-a)^2s^{-2}
\min\left\{
s^6,
\left(\frac{1-a}{s h_2}\right)^6
\right\}.
}
\]

Equivalently,

\[
\boxed{
\frac{\mathcal P_\eta}{\nu^2}
\gtrsim
(1-a)^2
\min\left\{
s^4,
\frac{(1-a)^6}{s^8h_2^6}
\right\}.
}
\]

This is a scale-invariant finite packet lower bound.

**Status: PROVED.**

---

## 5. Small palinstrophy forces a quantitative Hessian needle

Suppose

\[
\frac{\mathcal P_\eta}{\nu^2}<\varepsilon.
\]

If \(\varepsilon\) is below a fixed fraction of the full-persistence value

\[
(1-a)^2s^4,
\]

then the second branch of the minimum must be active. Hence

\[
\varepsilon
\gtrsim
\frac{(1-a)^8}{s^8h_2^6}.
\]

Therefore

\[
\boxed{
h_2
\gtrsim
(1-a)^{4/3}s^{-4/3}\varepsilon^{-1/6}.
}
\]

Substituting the direction-curvature persistence scale

\[
s\gtrsim
\min\left\{1,\frac{b}{1+k_3}\right\}
\]

shows that a very short high-to-low transition either pays palinstrophy or forces a correspondingly large second-vorticity-derivative needle.

**Status: PROVED CONDITIONAL ON THE SMALL-PALINSTROPHY BRANCH.**

---

## 6. DSD interpretation: failure is not absence and does not need volume completion

The occupancy statement

\[
|\omega|\ge aW
\quad\text{throughout a descended region}
\]

is a universal property assignment on that finite region.

Its failure does not create a `zero occupancy channel`, nor does it imply volume sparseness. DSD records the failure by an actual counter-witness

\[
\boxed{y:\ |\omega(y)|<aW.}
\]

That witness is enough to form a different channel: a finite high-to-low transition between \(x_*\) and \(y\). The transition then deterministically forms a first-derivative witness \(z\).

Thus the correct DSD chain is

\[
\boxed{
\text{occupancy failure witness}
\to
\text{high/low transition channel}
\to
\text{large }\nabla\omega\text{ witness}
\to
\begin{cases}
\text{palinstrophy packet},\\
\text{second-derivative needle}.
\end{cases}
}
\]

No unproved promotion from `one low point` to `positive low-volume fraction` is needed.

---

## 7. Updated local survivor tree

The previous direction-curvature branch was

\[
C_{\xi,2}
\Longrightarrow
\text{palinstrophy}
\lor
\text{occupancy failure/sparseness}
\lor
\text{third-direction-derivative escalation}.
\]

The finite-witness descent refines the middle branch:

\[
\boxed{
\text{occupancy failure}
\Longrightarrow
\text{palinstrophy packet}
\lor
\text{second-vorticity-derivative needle}.
}
\]

Hence, as a **primitive independent survivor**, `occupancy failure / sparseness` can be removed from this local proof tree.

The sharpened local tree is

\[
\boxed{
C_{\xi,2}
\Longrightarrow
\text{critical palinstrophy packet}
\lor
\text{second-vorticity-derivative transition needle}
\lor
\text{third-direction/vorticity-derivative needle}.
}
\]

This does **not** say that geometric sparseness is irrelevant or that no separate sparseness regularity criterion can be useful. It says only that the particular occupancy-failure branch generated here no longer has to remain unresolved merely because a volume-fraction estimate was absent.

---

## 8. Audit status

### PROVED

- one low-vorticity point within \(O(\delta)\) of the maximum forces a point with \(|\nabla\omega|\gtrsim(1-a)W/\delta\);
- controlled second derivative makes that first derivative persist on a calculable finite radius;
- persistence yields a critical palinstrophy packet;
- avoiding that packet forces a quantitative second-vorticity-derivative needle.

### CORRECTED / PRUNED

- `one low point -> quantitative volume sparseness`: still **NOT DERIVED** and no longer needed for this descent;
- occupancy failure as an independent primitive survivor: **PRUNED**.

### NOT DERIVED

- historical nonsummability of the resulting palinstrophy packets;
- a finite lower-order energy budget for arbitrary second/higher derivative needles through a hypothetical singularity;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
