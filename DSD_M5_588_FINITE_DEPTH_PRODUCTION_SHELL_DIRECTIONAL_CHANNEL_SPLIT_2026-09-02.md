# DSD M5-588 — Finite-Depth Production Shell / Directional-Channel Split

Date: 2026-09-02

Status: **THE FORCED FINITE-DEPTH STRETCHING SURPLUS DECOMPOSES EXACTLY INTO MAGNITUDE-GRADIENT AND ORIENTATION-GRADIENT CHARGES. THE UNPROVED BRIDGE IS SPATIAL/GENEALOGICAL OVERLAP WITH THE PERSISTENT DUAL-FLUX PAIR. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-587

There exists a finite wedge depth

\[
z_*\in(0,\infty)
\]

or equivalently a finite similarity radius

\[
\rho_*=z_*^{-1/2}
\]

such that the q/time-averaged sphere quantities obey

\[
\boxed{
Q_*-P_*
=
\frac14E_*
>0.
}
\]

Here

\[
E_*
=
\left\langle
\int_{S_{\rho_*}}|W|^2dS
\right\rangle,
\]

\[
P_*
=
\left\langle
\int_{S_{\rho_*}}|\nabla W|^2dS
\right\rangle,
\]

and

\[
Q_*
=
\left\langle
\int_{S_{\rho_*}}W\cdot\Sigma_UW\,dS
\right\rangle.
\]

---

## 2. Magnitude-direction decomposition on the shell

On the active set write

\[
\boxed{W=\rho\xi,}
\qquad
\rho=|W|,
\qquad
|\xi|=1.
\]

As in M5-486,

\[
\boxed{
|\nabla W|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
}
\]

Define the shell-averaged charges

\[
\boxed{
P_{mag,*}
:=
\left\langle
\int_{S_{\rho_*}}|\nabla\rho|^2dS
\right\rangle,
}
\]

and

\[
\boxed{
P_{dir,*}
:=
\left\langle
\int_{S_{\rho_*}}\rho^2|\nabla\xi|^2dS
\right\rangle.
}
\]

Then

\[
\boxed{P_*=P_{mag,*}+P_{dir,*}.}
\]

---

## 3. Axial stretching representation

Let

\[
\sigma
:=
\xi\cdot\Sigma_U\xi.
\]

Then

\[
W\cdot\Sigma_UW
=\rho^2\sigma,
\]

so

\[
\boxed{
Q_*
=
\left\langle
\int_{S_{\rho_*}}\rho^2\sigma\,dS
\right\rangle.
}
\]

Substitute into the M5-587 production-shell equality:

\[
\left\langle
\int\rho^2\sigma\right\rangle
-
P_{mag,*}
-
P_{dir,*}
=
\frac14
\left\langle
\int\rho^2\right\rangle.
\]

Therefore

\[
\boxed{
\left\langle
\int_{S_{\rho_*}}
\rho^2
\left(\sigma-\frac14\right)dS
\right\rangle
=
P_{mag,*}+P_{dir,*}.
}
\]

This is an exact finite-depth direction/magnitude ledger.

---

## 4. Two charged subbranches when P_* > 0

If

\[
P_*>0,
\]

then at least one of the two nonnegative pieces carries at least half the total:

\[
\boxed{
P_{mag,*}
\ge\frac12P_*
}
\]

or

\[
\boxed{
P_{dir,*}
\ge\frac12P_*.
}
\]

Thus the stretching-dominant shell has a quantitative dichotomy:

### M branch — magnitude-gradient shell

\[
\boxed{
P_{mag,*}\ge\frac12P_*>0.
}
\]

The shell must maintain nontrivial amplitude variation of vorticity.

### D branch — orientation-gradient shell

\[
\boxed{
P_{dir,*}\ge\frac12P_*>0.
}
\]

The shell must maintain nontrivial weighted variation of vorticity direction.

The D branch is directly of the same analytic type as M5-487's weighted orientation Dirichlet quantity.

---

## 5. Degenerate flat-vorticity subbranch

It remains possible at the level of the present argument that

\[
\boxed{P_*=0.}
\]

Then

\[
P_{mag,*}=P_{dir,*}=0
\]

and the production-shell equality reduces to

\[
\boxed{
Q_*=\frac14E_*>0.
}
\]

This corresponds to an unusually rigid shell where the full spatial vorticity gradient vanishes in the averaged nonnegative sense, while axial strain still supplies the exact similarity damping.

This branch should be recorded explicitly rather than silently excluded.

A separate unique-continuation/rigidity argument would be needed to rule it out.

---

## 6. Relation to M5-487 weighted tension

M5-487 distinguished

\[
P_{dir}
=
\int\rho^2|\nabla\xi|^2
\]

from the weighted harmonic tension

\[
T_{dir}
=
\int\rho^2|\mathcal D_\xi|^2.
\]

Therefore even on the D branch one may **not** infer a positive tension charge directly from

\[
P_{dir,*}>0.
\]

The earlier local helical witness showed precisely that orientation gradient can be nonzero while projected diffusion tension vanishes.

Thus the correct finite-depth channels remain separate:

\[
\boxed{
P_{dir,*}>0
\not\Rightarrow
T_{dir,*}>0.
}
\]

---

## 7. Genealogical overlap firewall

The persistent dual-flux pair extracted in M5-490/M5-491 is a material-lineage object.

The production shell \(S_{\rho_*}\) extracted in M5-587 is an Eulerian/time-averaged finite-depth object.

Nothing proved so far guarantees that the persistent pair intersects this particular shell with positive frequency.

Therefore the implication

\[
\text{production shell}
\Longrightarrow
\text{same persistent dual pair pays its stretching surplus}
\]

is **not yet valid**.

This is now the main bridge problem.

---

## 8. Precise next bridge target

Define a production-shell neighborhood

\[
\mathcal A_*
:=
\{y:\rho_* -\delta<|y|<\rho_*+\delta\}
\]

for a small fixed normalized thickness \(\delta>0\).

The desired bridge is a statement of the form

\[
\boxed{
\text{positive-density persistent material lineage}
+
\text{positive finite-depth production charge}
\Longrightarrow
\text{positive-density lineage visits to }\mathcal A_*
}
\]

or else a typed alternative:

\[
\boxed{
\text{lineage avoids }\mathcal A_*
\Longrightarrow
\text{radial export / replacement / separator defect}.
}
\]

If this bridge can be proved, then M5-487's tilt/tension charge and M5-491's relative-angle cancellation can be localized onto the same finite-depth production region.

---

## 9. Updated finite-depth endpoint

Every hard branch now contains a finite similarity shell satisfying

\[
\boxed{
\left\langle
\int\rho^2(\sigma-1/4)
\right\rangle
=P_{mag,*}+P_{dir,*}\ge0,
}
\]

with the subbranches

\[
\boxed{
M_{mag}
\lor
D_{dir}
\lor
F_{flat}.
}
\]

The next proof bottleneck is no longer finding positive stretching production; it is **forcing the persistent material architecture to encounter the Eulerian shell where that production is localized.**

Status: **THE FINITE-DEPTH PRODUCTION SURPLUS IS NOW CHANNEL-TYPED, BUT MATERIAL/EULERIAN OVERLAP IS UNPROVED. GLOBAL REGULARITY REMAINS UNPROVED.**