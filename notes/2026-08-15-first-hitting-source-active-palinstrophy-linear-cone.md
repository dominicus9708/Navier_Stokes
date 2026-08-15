# First-hitting source-active palinstrophy linear cone

Date: 2026-08-15

Status: **DERIVED WHOLE-SPACE FIRST-HITTING CONE. UNDER THE TERMINAL NORMALIZED VORTICITY CAP `||Omega||_infinity <= 1`, ANY TIME OF NONDECREASING GLOBAL ENSTROPHY SATISFIES `P <= C_nu E`, MUCH STRONGER THAN THE GENERIC `P <= C E^3` BETCHOV--GN CONE. LOCAL HIGH-FREQUENCY SPIKES OF SMALL GLOBAL MASS ARE NOT EXCLUDED AND ARE ROUTED TO THE SPATIAL-CONCENTRATION/MATERIAL BRANCH. GLOBAL REGULARITY NOT PROVED.**

## 1. First-hitting cap and enstrophy identity

On the terminal normalized first-hitting past,

\[
\boxed{\|\Omega(t)\|_\infty\le1.}
\]

Define

\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2,
\qquad
Q=\int\Omega\cdot S\Omega\,dx.
\]

The enstrophy identity is

\[
\boxed{
\frac12E'+\nu P=Q.
}
\]

## 2. Linear source bound under the vorticity cap

By Holder,

\[
|Q|
\le
\|S\|_2\,\|\Omega\|_4^2.
\]

The whole-space Calderon--Zygmund identity/bound for incompressible velocity gives

\[
\|S\|_2\lesssim\|\Omega\|_2=E^{1/2}.
\]

Also

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2
\le E^{1/2}.
\]

Therefore

\[
\boxed{
|Q|\le C E.
}
\]

More generally, under a cap `||Omega||_infinity <= a`,

\[
\boxed{|Q|\le CaE.}
\]

## 3. Source-active linear cone

If at a time

\[
E'\ge0,
\]

then

\[
\nu P\le Q\le CE.
\]

Hence

\[
\boxed{
P\le C_\nu E
\qquad(E'\ge0).
}
\]

Equivalently,

\[
\boxed{
P>C_\nu E
\quad\Longrightarrow\quad
E'<0.
}
\]

This is far stronger than the generic source-active cone obtained only from Betchov--GN,

\[
P\lesssim E^3.
\]

The improvement comes entirely from the terminal first-hitting `L^infinity` vorticity cap.

## 4. Quantitative decay above the cone

If

\[
P\ge \lambda C_\nu E
\]

for a sufficiently large fixed `lambda`, then

\[
Q\le CE\le\frac{\nu}{\lambda'}P
\]

with `lambda'>1`, and therefore

\[
\boxed{
E'\le-c_\nu P.
}
\]

Thus a globally dominant high-palinstrophy episode above the linear cone is strongly dissipative in terminal normalized variables.

## 5. Consequence for derivative-radius collapse

A derivative-radius collapse may be measured globally by

\[
\frac PE\to\infty.
\]

Such a global collapse cannot coincide with nondecreasing enstrophy on the terminal first-hitting past. It belongs to an enstrophy-decay interval.

Therefore a **globally source-active** derivative branch is excluded:

\[
\boxed{
E'\ge0
\quad\Longrightarrow\quad
P/E\le C_\nu.
}
\]

## 6. Local-spike caveat

The whole-space ratio `P/E` need not detect a small-mass localized derivative spike.

A region may have

\[
P_{\rm loc}/E_{\rm loc}\gg1
\]

while its contribution to global `P` and `E` is negligible.

Such a spike is not claimed to be excluded by the linear cone. Its defining feature is spatial concentration: high derivative frequency supported on a small fraction of the total vorticity mass.

This returns it to the already typed alternatives:

- spatial non-tightness / concentration;
- shell or material import;
- local palinstrophy/viscous flux;
- deformation needed to create the concentrated material geometry.

Thus the local-spike caveat does not reopen an untyped global source mechanism.

## 7. Interaction with the far-checkpoint enstrophy reset

The far adaptive checkpoint supplies a small previous normalized global enstrophy, while a fresh Gaussian residual source forces a later much larger global enstrophy maximum.

Hence every fresh-source first-hitting step contains an enstrophy-increasing portion.

On that increasing portion,

\[
\boxed{P/E\le C_\nu.}
\]

Therefore the actual global enstrophy creation stage cannot simultaneously rely on an arbitrarily small derivative radius.

If the local dangerous core nevertheless needs derivative-radius collapse, that collapse must be localized and/or occur during an enstrophy-decreasing redistribution stage, returning to the material/spatial channel.

## 8. Revised causal merger

Inside the terminal normalized first-hitting interval:

\[
\boxed{
\text{global high-derivative source}
\text{ is impossible on }E'\ge0,
}
\]

while

\[
\boxed{
\text{local high-derivative spike}
\Rightarrow
\text{spatial concentration/material geometry}.
}
\]

Since the material branch has already been reduced to

\[
\text{viscous derivative flux}
\lor
\text{large symmetric-strain deformation},
\]

the high-derivative remainder is increasingly forced back into the final critical strain/deformation branch rather than remaining a separate global production mechanism.

Status: **FIRST-HITTING SOURCE-ACTIVE GLOBAL DERIVATIVE COLLAPSE EXCLUDED / LOCAL DERIVATIVE SPIKES RETAINED ONLY AS SPATIAL-CONCENTRATION SUBCASES / FINAL SOURCE-ACTIVE FRONTIER FURTHER CONCENTRATED INTO CRITICAL STRAIN/MATERIAL DEFORMATION / GLOBAL REGULARITY NOT PROVED.**
