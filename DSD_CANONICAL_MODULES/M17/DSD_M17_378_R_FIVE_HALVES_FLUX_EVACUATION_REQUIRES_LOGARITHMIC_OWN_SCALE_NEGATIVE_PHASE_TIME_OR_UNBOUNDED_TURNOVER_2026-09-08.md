# DSD M17-378 — `r^{5/2}` flux evacuation requires logarithmic own-scale negative-phase time or unbounded turnover

Date: 2026-09-08  
Canonical ID: **M17-378**

Status: **ACTIVE OWN-SCALE RESIDENCE/TURNOVER GATE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-372

On one preserved material family, evacuation from fixed positive flux to the M17-371 scale-`r` bound requires

\[
\boxed{
\int_{\theta_0}^{\theta_r}
\overline{\kappa_-}_{\Phi,F}(\theta)d\theta
\ge
\frac52\log\frac1r-C_0.
}
\]

Here

\[
\overline{\kappa_-}_{\Phi,F}
=
\frac{1}{\Phi_F}
\int_F\kappa_-d\Phi.
\]

## 2. Scale-comparable coefficient ceiling

Assume the evacuation remains in a coefficient-scale-`r` compact class, meaning

\[
\boxed{
\kappa_-(\lambda,\theta)
\le K_\kappa r^{-2}
}
\]

on the participating family during the negative-exposure episodes.

If this fails, record instead

\[
\boxed{G_{coefficient\ supercritical\ spike}.}
\]

The family average then satisfies

\[
0\le
\overline{\kappa_-}_{\Phi,F}
\le K_\kappa r^{-2}.
\]

## 3. Physical similarity-time measure of the negative phase

Let

\[
E_r
:=
\left\{
\theta\in[\theta_0,\theta_r]:
\overline{\kappa_-}_{\Phi,F}(\theta)>0
\right\}.
\]

Then

\[
\int_{\theta_0}^{\theta_r}
\overline{\kappa_-}_{\Phi,F}d\theta
\le
K_\kappa r^{-2}|E_r|.
\]

Combining with M17-372 gives

\[
\boxed{
|E_r|
\ge
\frac{r^2}{K_\kappa}
\left(
\frac52\log\frac1r-C_0
\right).
}
\]

For sufficiently small `r`,

\[
\boxed{
|E_r|
\gtrsim
r^2\log\frac1r.
}
\]

## 4. Own-scale time

Measure time in the coefficient own-scale variable

\[
\tau_r:=\frac{\theta-\theta_{ref}}{r^2}.
\]

The total negative-phase measure becomes

\[
|E_r|_{own}
:=r^{-2}|E_r|.
\]

Hence

\[
\boxed{
|E_r|_{own}
\gtrsim
\log\frac1r
\to\infty.
}
\]

Thus strict-subscale flux evacuation cannot be produced by an `O(1)` amount of own-scale negative-coefficient time under a scale-comparable coefficient ceiling.

## 5. Residence versus turnover

Write the open set `E_r` as a union of connected intervals

\[
E_r=\bigcup_{m=1}^{N_r}I_{r,m}
\]

when the number of components is finite.

If

\[
N_r\le N_*<\infty,
\]

then at least one component satisfies

\[
|I_{r,m}|
\ge
\frac{|E_r|}{N_*}
\gtrsim
r^2\log\frac1r.
\]

Therefore in own-scale units

\[
\boxed{
|I_{r,m}|_{own}
\gtrsim
\log\frac1r.
}
\]

This is a **logarithmically long negative-coefficient residence episode**.

If no such long connected episode exists, then necessarily

\[
\boxed{N_r\to\infty,}
\]

which is an unbounded negative-phase turnover branch.

Thus

\[
\boxed{
H_{r^{5/2}\ flux\ evacuation}
\Longrightarrow
H_{log\text{-}long\ own\text{-}scale\ negative\ residence}
\lor
H_{unbounded\ coefficient\ turnover}
\lor
G_{coefficient\ supercritical\ spike}.
}
\]

## 6. Why this is stronger than M17-372

M17-372 provided only an integrated signed-exposure requirement.

The present theorem uses the natural coefficient scale to show that the exposure cannot be compressed into a bounded own-scale time interval unless the coefficient itself becomes supercritical.

Hence a compact strict-subscale bubble must be dynamically long-lived in its own scale or repeatedly recreated.

## 7. Compactness opportunity

On the long-residence branch, rescaling space by `r` and time by `r^2` yields intervals whose lengths tend to infinity.

If the corresponding normalized velocity/vorticity, coefficient, geometry, and material-domain bounds are uniform, one may recenter inside these intervals and extract a complete long-time CE-H tangent carrying a persistent negative coefficient phase.

This extraction is **not yet asserted** here. It requires the same no-defect compactness and domain/genealogy checks used in earlier M17 own-scale tangent modules.

The alternative is explicit:

\[
G_{own\text{-}scale\ compactness/domain/genealogy}.
\]

## 8. DSD-theory role

The useful heuristic is to convert an integrated structural exposure into its intrinsic scale clock before judging whether it is cheap or expensive. The proof is the elementary exposure ceiling estimate above.

## 9. Audit verdict

**PASS.**

The compact flux-evacuation branch now requires either logarithmically long own-scale negative residence, unbounded turnover, or a coefficient-supercritical spike.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]