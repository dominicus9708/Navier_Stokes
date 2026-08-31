# DSD M5-380 — Thin-reach material circulation destruction still forces divergent normalized palinstrophy

Date: 2026-08-31

Status: **THE SHEET-LIKE CANCELLATION GEOMETRY OF M5-379 DOES NOT PROVIDE A CHEAP WAY TO DESTROY THE OLD MATERIAL CIRCULATION / FOR A MATERIAL CROSS-SECTION OF AREA O(d^2), A MOLLIFIED FLUX TEST WITH TUBULAR THICKNESS h HAS GRADIENT NORM O(d h^(-3/2)) / CHANGING A FIXED FRACTION OF Gamma ~ W d^2 IN ONE NATURAL FIRST-HITTING STAGE FORCES NORMALIZED SPACETIME PALINSTROPHY >= c (d/r)^2 (h/r)^3 / Theta / EVEN AT THE MINIMAL NON-SUB-NATURAL REACH h ~ r THIS DIVERGES LIKE (d/r)^2 ~ r^(-2/5) / THEREFORE A REGULAR THIN SHEET CAN MIX APPARENT SIGNS BUT CANNOT ACTUALLY ERASE THE LARGE MATERIAL CIRCULATION ON A NO-H CORRIDOR / AVOIDING H REQUIRES SUB-NATURAL REACH OR LOSS OF A REGULAR MATERIAL FLUX SURFACE, I.E. H_HIGH-FREQ OR T_FRAGMENT/MIX/SHAPE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-379 showed that a cancellation-ready opposite-sign reservoir with shield-scale transverse area `d_j^2` must become only `O(r_j)` thick if normalized palinstrophy is to stay bounded at one time.

That left a sheet-like T geometry.

However, there are two different meanings of "cancellation":

1. **apparent/eulerian cancellation** — positive and negative vorticity interleave so that a coarse signed descriptor becomes small;
2. **material circulation destruction** — the circulation carried by the old material loop/surface actually decreases by a fixed fraction.

Only the second disposes of the growing material circulation inventory from M5-356--359.

For a material loop, Kelvin's Navier--Stokes identity shows that the second process is viscous. The present note quantifies its cost when the regular tubular reach has collapsed from `d_j` down to a thinner scale `h_j`.

---

## 2. Scales and circulation to be destroyed

Use the saturated affine shield scales

\[
W_j\asymp\frac\nu{r_j^2},
\qquad
 d_j\asymp r_j^{4/5}.
\]

The coherent material cross-section carries

\[
\boxed{
|\Gamma_j|
\asymp
W_jd_j^2.
}
\]

Suppose a fixed fraction is genuinely destroyed during one first-hitting stage:

\[
\boxed{
|\Delta\Gamma_j|
\ge c_\Gamma W_jd_j^2.
}
\]

Let

\[
|I_j|
=
\Theta_j\frac{r_j^2}{\nu}
\]

with bounded normalized stage duration on the retained corridor.

---

## 3. Thin mollified material-flux test

Let `Sigma_j(t)` be a regular material spanning surface for the descendant loop, with relevant area comparable to

\[
A_j\asymp d_j^2.
\]

Assume it has a regular tubular neighborhood of thickness

\[
0<h_j\le c d_j.
\]

Construct a smooth co-moving flux test `psi_j` supported in that tubular neighborhood so that

\[
\int\omega\cdot\psi_j\,dx
\asymp
\Gamma_j.
\]

To approximate a surface flux using a volume layer of thickness `h_j`, the test has the scaling

\[
|\psi_j|\asymp h_j^{-1}
\]

on volume

\[
\asymp d_j^2h_j.
\]

Its transition occurs across thickness `h_j`, so

\[
|\nabla\psi_j|
\asymp h_j^{-2}.
\]

Therefore

\[
\boxed{
\|\nabla\psi_j\|_2
\asymp
 d_j h_j^{-3/2}.
}
\]

For `h_j=d_j`, this recovers the M5-356 scaling

\[
\|\nabla\psi_j\|_2\asymp d_j^{-1/2}.
\]

Thus the present calculation is the thin-reach extension of the older regular-tube estimate.

---

## 4. Kelvin-viscous flux estimate

Choose the test to move according to the material 2-form transport so that inviscid transport/stretching is absorbed into the test evolution, as in M5-356.

Then the circulation change is controlled by viscosity:

\[
|\Delta\Gamma_j|
\lesssim
\nu
\int_{I_j}
\|\nabla\omega(t)\|_{L^2(N_j(t))}
\|\nabla\psi_j(t)\|_2dt.
\]

Using the thin-test norm and Cauchy--Schwarz in time,

\[
|\Delta\Gamma_j|
\lesssim
\nu d_jh_j^{-3/2}|I_j|^{1/2}
\left(
\int_{I_j}\!\!\int_{N_j(t)}
|\nabla\omega|^2dxdt
\right)^{1/2}.
\]

Hence

\[
\boxed{
\int_{I_j}\!\!\int_{N_j(t)}|\nabla\omega|^2dxdt
\gtrsim
\frac{|\Delta\Gamma_j|^2h_j^3}
{\nu^2d_j^2|I_j|}.
}
\]

---

## 5. Insert the first-hitting scales

Use

\[
|\Delta\Gamma_j|
\gtrsim
c_\Gamma W_jd_j^2
\asymp
c_\Gamma\frac{\nu d_j^2}{r_j^2}
\]

and

\[
|I_j|=\Theta_j\frac{r_j^2}{\nu}.
\]

Then

\[
\begin{aligned}
\int_{I_j}\!\!\int|\nabla\omega|^2
&\gtrsim
\frac{
(\nu^2d_j^4r_j^{-4})h_j^3
}
{
\nu^2d_j^2(\Theta_jr_j^2/\nu)
}\\
&=
\boxed{
\frac{\nu d_j^2h_j^3}{\Theta_jr_j^6}.
}
\end{aligned}
\]

---

## 6. Natural normalized spacetime palinstrophy

Under the first-hitting scaling

\[
Y=\frac{x-X_j}{r_j},
\qquad
\tau=\frac{\nu(t-t_j)}{r_j^2},
\qquad
\Omega_j=\frac{r_j^2}{\nu}\omega,
\]

we have

\[
\boxed{
\int |\nabla_Y\Omega_j|^2dYd\tau
=
\frac{r_j}{\nu}
\int |\nabla_x\omega|^2dxdt.
}
\]

Define

\[
\widehat{\mathfrak P}_j
:=
\int_{\widehat I_j}\!\!\int
|\nabla_Y\Omega_j|^2dYd\tau.
\]

Section 5 yields

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\frac1{\Theta_j}
\frac{d_j^2h_j^3}{r_j^5}.
}
\]

Equivalently,

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\frac1{\Theta_j}
\left(\frac{d_j}{r_j}\right)^2
\left(\frac{h_j}{r_j}\right)^3.
}
\]

This is the main formula.

---

## 7. Even natural-scale tubular reach diverges

The M5-379 no-H sheet corridor had thickness/reach of order at most the natural scale.

Consider first the last non-sub-natural regular case

\[
h_j\asymp r_j.
\]

Then

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\frac1{\Theta_j}
\left(\frac{d_j}{r_j}\right)^2.
}
\]

Since

\[
d_j\asymp r_j^{4/5},
\]

\[
\frac{d_j}{r_j}
\asymp
r_j^{-1/5},
\]

and therefore

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\Theta_j^{-1}r_j^{-2/5}
\to\infty
}
\]

whenever the normalized stage durations remain uniformly bounded above.

Thus the regular `O(r_j)`-thin sheet geometry does **not** make true material circulation destruction cheap.

It forces a divergent normalized palinstrophy H event.

---

## 8. Thicker reach is even more expensive

If

\[
h_j\gg r_j,
\]

then

\[
\left(\frac{h_j}{r_j}\right)^3\to\infty,
\]

so the lower bound is stronger.

At the old regular-tube scale

\[
h_j\asymp d_j,
\]

we recover

\[
\widehat{\mathfrak P}_j
\gtrsim
\Theta_j^{-1}
\left(\frac{d_j}{r_j}\right)^5
\asymp
\Theta_j^{-1}r_j^{-1},
\]

consistent with M5-356.

Hence shrinking the tubular reach from `d_j` to `r_j` weakens the exponent but does not remove divergence.

---

## 9. Sub-natural reach is not a free escape

The only way the formula in Section 6 can avoid the `h_j >= c r_j` divergence is to let

\[
\frac{h_j}{r_j}\to0
\]

sufficiently rapidly.

But then the material flux surface has sub-natural tubular reach.

This means at least one of the following:

- vorticity/magnitude transition occurs on a scale `h_j << r_j`;
- the surface curvature/reach degenerates below the natural scale;
- the co-moving flux test requires gradients above the natural derivative scale.

These are already

\[
\boxed{
H_{\rm high-freq/der}
\lor
T_{\rm microshape/reach}.
}
\]

Thus sub-natural reach is retained explicitly; it is not counted as successful quiet cancellation.

---

## 10. Apparent cancellation versus true charge destruction

Suppose positive and negative vorticity are interleaved so that a coarse eulerian signed flux appears small, but the old material loop still carries circulation comparable to `Gamma_j`.

Then no large `Delta Gamma_j` has occurred and the Kelvin-viscous lower bound need not be paid.

However, the old circulation charge has **not been disposed of**.

It survives in a geometrically mixed, folded, fragmented, or non-coherent material configuration.

Therefore this alternative belongs to

\[
\boxed{
T_{\rm mix/fragment/shape}
}
\]

and must remain in the absolute material-circulation inventory even if it disappears from a coarse signed eulerian descriptor.

This distinction is essential for the M5-358 sequential-renewal firewall.

---

## 11. Consequence for the no-H sequential-renewal branch

Combining M5-359, M5-379, and the present thin-reach estimate gives

\[
\boxed{
\text{old descendant disposal}
\Longrightarrow
H_{\rm Lip/log}
\lor
H_{\rm visc/pal/high-freq}
\lor
T_{\rm spatial/export}
\lor
T_{\rm mix/fragment/microshape}.
}
\]

A bounded-geometry opposite-sign sheet is no longer an independent T leaf if it truly destroys circulation; it returns to H.

Therefore on a strict no-H corridor, the old material circulation can disappear from the **coherent** inventory only by becoming geometrically non-coherent/non-tight:

\[
\boxed{
\text{no-H descendant loss}
\Longrightarrow
T_{\rm spatial/export/mix/fragment/microshape}.
}
\]

---

## 12. DSD audit

### Derived

- thin surface-flux test scaling `||grad psi||_2 ~ d h^(-3/2)`;
- fixed-fraction material circulation destruction lower bound
  \[
  \widehat{\mathfrak P}_j
  \gtrsim
  \Theta_j^{-1}(d_j/r_j)^2(h_j/r_j)^3;
  \]
- at `h_j ~ r_j`, normalized palinstrophy diverges as `r_j^(-2/5)`;
- at `h_j ~ d_j`, the older `r_j^(-1)` divergence is recovered;
- sub-natural reach is an H/high-frequency or microshape T escape;
- apparent cancellation without material circulation loss is T-mixing, not charge destruction.

### Required corridor assumptions

- a material spanning surface remains identifiable;
- its active area is comparable to `d_j^2`;
- a regular tubular neighborhood of thickness `h_j` exists;
- test deformation remains controlled at that reach;
- the fixed circulation fraction is destroyed during one bounded normalized stage.

Failure of these assumptions is retained as T rather than ignored.

---

## 13. Updated circulation frontier

The circulation lane has now sharpened from

\[
\text{viscous destruction}
\lor
\text{opposite cancellation}
\lor
\text{spatial/shape turnover}
\]

to

\[
\boxed{
\text{true material charge destruction}
\Longrightarrow
H,
}
\]

while

\[
\boxed{
\text{charge preserved but no longer coherently describable}
\Longrightarrow
T.
}
\]

This is a particularly clean DSD distinction between **destruction of a structural charge** and **loss of a chosen description of that charge**.

The next question is whether the T process can repeatedly hide an increasing sequence of material circulations without either recovering a finite-memory energy packet or creating a derivative/reach H event.

---

## 14. Audit verdict

### NEW BARRIER

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\Theta_j^{-1}
\left(\frac{d_j}{r_j}\right)^2
\left(\frac{h_j}{r_j}\right)^3.
}
\]

### NO-H CONSEQUENCE

A regular cancellation layer with `h_j >= c r_j` cannot destroy a fixed fraction of the old material circulation on late stages.

### REMAINING T

- material charge preserved but geometrically mixed/folded/fragmented;
- spatial export/non-tightness;
- sub-natural reach/microshape degeneration.

### STILL OPEN

- whether those T states admit a scale-independent energy/circulation inventory bound;
- global exclusion of recurrent T;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
