# Source-active palinstrophy cone and merger of the derivative branch

Date: 2026-08-15

Status: **EXACT ENSTROPHY-SIGN DICHOTOMY USING THE STRICT BETCHOV--GN SOURCE GAP. PALINSTROPHY ABOVE THE CRITICAL `E^3` CONE IS INSTANTANEOUSLY DISSIPATIVE; A DERIVATIVE-CONCENTRATION EPISODE THAT PARTICIPATES IN GLOBAL ENSTROPHY GROWTH MUST BE SUPPORTED BY COMPARABLY LARGE ENSTROPHY/STRAIN PRODUCTION. THIS MERGES THE SOURCE-ACTIVE PART OF BRANCH 1 INTO BRANCH 3. GLOBAL REGULARITY NOT PROVED.**

## 1. Whole-space enstrophy equation

Let

\[
E(t)=\|\omega(t)\|_2^2,
\qquad
P(t)=\|\nabla\omega(t)\|_2^2,
\]

and

\[
Q(t)=\int\omega\cdot S\omega\,dx.
\]

Then

\[
\boxed{
E'=2Q-2\nu P.
}
\]

The repository's universal incompressibility gap below the formal Betchov--sharp-GN source constant gives

\[
\boxed{
Q
\le C_*E^{3/4}P^{3/4},
}
\]

where

\[
C_*=(1-\delta_{\rm inc})C_0<C_0.
\]

Only the existence of a finite universal `C_*` is needed for the sign argument below; the strict gap improves the numerical threshold but not the critical powers.

## 2. Critical source-active cone

If

\[
E'(t)\ge0,
\]

then

\[
\nu P\le Q.
\]

Combining with the source bound,

\[
\nu P
\le C_*E^{3/4}P^{3/4}.
\]

For `P>0`, divide by `P^(3/4)`:

\[
\nu P^{1/4}
\le C_*E^{3/4}.
\]

Hence

\[
\boxed{
P
\le
\left(\frac{C_*}{\nu}\right)^4E^3
\qquad\text{whenever }E'\ge0.
}
\]

Equivalently,

\[
\boxed{
P>
\left(\frac{C_*}{\nu}\right)^4E^3
\quad\Longrightarrow\quad
E'<0.
}
\]

Thus palinstrophy arbitrarily above the scale-critical `E^3` level is not a positive singular source at that instant: viscosity dominates and global enstrophy decreases.

## 3. Quantitative strict decay above the cone

Suppose for some `lambda>1`,

\[
P
\ge
\lambda^4
\left(\frac{C_*}{\nu}\right)^4E^3.
\]

Then

\[
C_*E^{3/4}P^{3/4}
\le
\frac{\nu}{\lambda}P.
\]

Therefore

\[
\boxed{
E'
\le
-2\nu\left(1-\lambda^{-1}\right)P.
}
\]

So a strongly supercritical derivative spike pays immediate enstrophy decay proportional to its palinstrophy.

## 4. Consequence for Branch 1 derivative-radius collapse

Branch 1 was reduced to factorial derivative-radius collapse / endpoint derivative concentration.

Such an episode now has two causal types.

### D-decay — derivative spike above the source-active cone

If

\[
P\gg E^3,
\]

then

\[
E'<0
\]

with a quantitative negative rate. This episode is dissipative rather than a source of global enstrophy growth.

It may still redistribute vorticity spatially and allow a local maximum to increase while global enstrophy falls. But then its role is concentration/transport rather than net creation, and it is routed through the spatial/material branch already reduced to

\[
\text{material deformation}
\lor
\text{viscous flux/derivative action}.
\]

Thus it does not reopen an independent positive high-Hermite source.

### D-active — derivative concentration while enstrophy grows

If the derivative episode participates in a time set where

\[
E'\ge0,
\]

then necessarily

\[
\boxed{
P\lesssim_\nu E^3.
}
\]

Hence large palinstrophy requires large enstrophy at the corresponding critical power. It cannot diverge independently while `E` remains small.

## 5. First-hitting fresh-source consequence

The existing far-checkpoint argument shows that a fresh intermediate Gaussian source forces a large global-enstrophy escalation relative to an earlier reset checkpoint.

Therefore any first-hitting interval in which derivative concentration is causally responsible for the fresh source has only two possibilities:

1. it occurs mainly on enstrophy-increasing portions, where it is trapped in the critical cone `P <= C E^3` and therefore requires large `E` / strain production;
2. it occurs mainly on enstrophy-decreasing portions, in which case it acts as concentration/redistribution and must be accompanied by the spatial/material transfer needed to build the local dangerous state despite global loss.

The second route has already been merged into material deformation or derivative flux. The first route is Branch 3.

## 6. Positive middle-strain routing on the increasing part

Whenever enstrophy rises from `E_0` to `E_1>E_0`, the exact strain determinant identity yields

\[
\boxed{
\int\!\!\int\lambda_2^+|S|^2\,dxdt
\gtrsim E_1-E_0.
}
\]

Thus the source-active derivative branch enters the positive-middle-strain channel quantitatively.

In particular, a large `E` required by the cone is not an untyped reservoir: if it is newly created during the adaptive step, its increase already carries a middle-strain production cost.

## 7. Combined causal merger

The previous branch tree was

\[
\text{Branch 1 derivative concentration}
\quad\lor\quad
\text{Branch 3 critical strain saturation}.
\]

The present sign dichotomy refines this to

\[
\boxed{
\text{source-active derivative concentration}
\Rightarrow
\text{critical enstrophy/strain saturation},
}
\]

while

\[
\boxed{
\text{strongly supercritical derivative concentration}
\Rightarrow
\text{dissipation / spatial redistribution}.
}
\]

The latter redistribution route is already handled by the material/spatial reduction.

Thus derivative-radius collapse is no longer retained as a fully independent **positive source** branch.

## 8. Remaining irreducible branch

After the sequential reductions, the genuinely source-active survivor is concentrated into

\[
\boxed{
\text{critical strain/enstrophy saturation}
}
\]

with geometric manifestations including

- positive-middle-strain production;
- extensional material-area contraction;
- compensating Betchov boundary flux;
- near-critical `P~E^3` derivative support;
- or loss of compactness/shape that returns to the already typed redistribution channels.

No contradiction is obtained from the critical cone itself. The scalar adversarial Riccati skeleton can still saturate the same powers. A final proof would need to show that actual 3D incompressible geometry cannot repeat this coupled critical saturation indefinitely.

Status: **SOURCE-ACTIVE BRANCH 1 MERGED INTO BRANCH 3 / SUPERCRITICAL PALINSTROPHY IS DISSIPATIVE / FINAL POSITIVE BRANCH = CRITICAL STRAIN-ENSTROPHY SATURATION / GLOBAL REGULARITY NOT PROVED.**
